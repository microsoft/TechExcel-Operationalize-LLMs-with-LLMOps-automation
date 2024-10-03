from dotenv import load_dotenv
load_dotenv()

import os
import pathlib
import json
from ai_search import retrieve_documentation
from promptflow.tools.common import init_azure_openai_client
from promptflow.connections import AzureOpenAIConnection
from promptflow.core import (AzureOpenAIModelConfiguration, Prompty, tool)
from promptflow.tracing import trace
from azure_config import AzureConfig 

# Initialize AzureConfig
azure_config = AzureConfig()

def get_embedding(question: str):
    embedding_model = os.environ["AZURE_OPENAI_EMBEDDING_MODEL"]

    connection = AzureOpenAIConnection(
        azure_deployment=embedding_model,
        api_version=azure_config.aoai_api_version,
        api_base=azure_config.aoai_endpoint
    )
    client = init_azure_openai_client(connection)

    return client.embeddings.create(
        input=question,
        model=embedding_model,
    ).data[0].embedding

def get_context(question, embedding):
    return retrieve_documentation(
        question=question,
        index_name="rag-index",
        embedding=embedding,
        search_endpoint=azure_config.search_endpoint
    )


@trace
def get_response(question, chat_history):
    print("inputs:", question)
    
    # Obtain embedding and context based on the question
    embedding = get_embedding(question)
    context = get_context(question, embedding)
    print("context:", context)
    print("getting result...")

    # Retrieve deployment name from environment variables
    deployment_name = os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT")
    if not deployment_name:
        raise EnvironmentError("AZURE_OPENAI_CHAT_DEPLOYMENT environment variable not set.")

    # Configure the Azure OpenAI model
    configuration = AzureOpenAIModelConfiguration(
        azure_deployment=deployment_name,
        api_version=azure_config.aoai_api_version,
        azure_endpoint=azure_config.aoai_endpoint
    )
    override_model = {
        "configuration": configuration,
        "parameters": {"max_tokens": 512}
    }

    # Load the modified Prompt B
    data_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "./chat.prompty")
    prompty_obj = Prompty.load(data_path, model=override_model)

    # Generate the response using the AI assistant
    result = prompty_obj(question=question, documents=context)
    # print("raw result: ", result)

    # Initialize default values
    answer = ""
    sentiment = ""

    try:
        # Parse the JSON response
        parsed_result = json.loads(result)
        answer = parsed_result.get("answer", "").strip()
        sentiment = parsed_result.get("sentiment", "").strip()

        # Validate that both fields are present
        if not answer or not sentiment:
            print("Warning: 'answer' or 'sentiment' field is missing in the response.")
    except json.JSONDecodeError as e:
        print("Error parsing JSON response:", e)
        print("Response was:", result)
        # Handle the error as needed, e.g., set default values or raise an exception

    # Return the structured response
    return {
        "answer": answer,
        "sentiment": sentiment,
        "context": context
    }

if __name__ == "__main__":
    get_response("How can I access my medical records?", [])