#### Building LLMs Orchestration Flows

Learn how to build prompt flow orchestrations for your LLM App.

#### Prerequisites

An Azure subscription where you can create an AI Hub Resource and a AI Search service.

#### Setup

If you are running this Lab after lesson 1, you don't need to worry about this step. Otherwise, follow **Setup** from **Lesson 1** to create a project and its associated resources in Azure AI Studio, as well as to deploy the GPT-4 model.

#### Lab Steps

During this lab, we will cover the following steps:

1) Create a conversational RAG flow.

##### 1) Create a conversational RAG flow

Open your web browser and navigate to: https://ai.azure.com

Now you will create a conversational flow using the RAG pattern, start by creating a new flow in the **Prompt Flow** item in the **Tools** section within the **Build** tab.

Select the **Multi-Round Q&A** on Your Data template after clicking the **Create** button.

![LLMOps Workshop](images/lab2grab1.png)

Click on the **Clone** button. A flow with the following structure will be created.

![LLMOps Workshop](images/lab2grab2.png)

Start the automatic runtime by selecting **Start compute session** in the **Runtime** drop down. The runtime will be useful for you to work with the flow moving forward.

![LLMOps Workshop](images/lab2grab3.png)

Click the **Save** button to save your flow.

![LLMOps Workshop](images/lab2grab4.png)

###### 2.1) Flow overview

The first node, `modify_query_with_history`, produces a search query using the user's question and their previous interactions. Next, in the `lookup` node, the flow uses the vector index to conduct a search within a vector store, which is where the RAG pattern retrieval step takes place. Following the search process, the `generate_prompt_context` node consolidates the results into a string. This string then serves as input for the `Prompt_variants` node, which formulates various prompts. Finally, these prompts are used to generate the user's answer in the `chat_with_context` node.

###### 2.2) Search index

Before you can start running your flow, a crucial step is to establish the search index for the Retrieval stage. This search index will be provided by the Azure AI Search service.

The AI Search service was originally created in the **Setup** section of this lab. If you have not yet created the Search service, you will need to set one up as explained below. With the search service created, you can now proceed to create the index.

In our case, we will create a **Vector index**. To do this, you just need to go back to the project in the **AI Studio**, select the **Indexes** option, and then click on the **New index** button.  
   
![LLMOps Workshop](images/lab2grab5.png)
   
At the `Source data` stage, select the `Upload files` option and upload the PDF `files/surface-pro-4-user-guide-EN.pdf` to the data folder of this lab, as shown in the next screen and click **Next**.  
   
![LLMOps Workshop](images/lab2grab6.png)
   
In `Index settings`, select the Search Service you created earlier.  

> If someone has created the AI Search service for you, you can also use it to create the index. Simply select it in the **Select Azure AI Search service** option and click **Next**.

![LLMOps Workshop](images/lab2grab7.png)
   
Under `Search settings`, select **Add vector search to this ...** as indicated in the following image and click **Next**.  
   
![LLMOps Workshop](images/lab2grab8.png)
   
> Note: If you want to select a virtual machine configuration, click on the **Select from recommended options**. If you don't select, the default configuration will use serverless processing.

Great, now just click on the **Create** button at the `Review and finish` stage.  
   
The indexing job will be created and submitted for execution, so please wait a while for it to complete.

It may take about 10 minutes from the time it enters the execution queue until it starts.  
   
Wait until the index status is `Completed` as in the next image, before proceeding with the next steps.  
   
![LLMOps Workshop](images/lab2grab9.png) 

Done! You have created the index, as can be seen in the **Indexes** item of the **Components** section.

![LLMOps Workshop](images/lab2grab10.png)

Now return to the RAG flow created in **Prompt flow** to configure the `lookup` node.

After selecting the `lookup` node, click on `mlindex_content`.

![LLMOps Workshop](images/lab2grab11.png)

A **Generate** window will appear. In this window, select the `Registered Index` option from the `index_type` field. Then, choose version 1 of the index you just created, as shown in the following image. After making these selections, click on **Save**.

![LLMOps Workshop](images/lab2grab12.png)

Now, let's go back to the `lookup` node. Select the `Hybrid (vector + keyword)` option from the query_type field, as shown in the subsequent image.

![LLMOps Workshop](images/lab2grab13.png)

###### 2.3) Updating connection information

Now you will need to update the Connections of the nodes that link with LLM models.  

Starting with the Connection in the `modify_query_with_history` node with the gpt-4 deployment, as indicated below:

![LLMOps Workshop](images/lab2grab14.png)

And the Connection for the `chat_with_context node` with the gpt-4 deployment, as indicated below:

![LLMOps Workshop](images/lab2grab15.png)

###### 2.4) Testing your RAG flow

Everything is now set up for you to initiate your chat flow. Simply click on the blue **Chat** button located at the top right corner of your page to begin interacting with the flow.

![LLMOps Workshop](images/lab2grab16.png.png)

