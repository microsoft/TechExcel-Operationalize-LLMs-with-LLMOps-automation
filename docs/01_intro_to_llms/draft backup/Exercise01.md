#### Introduction to LLMs and Azure AI Services

In this exercise, we will have an overview on how to use Azure AI to work with large language models.

The focus will be more on an overview of the creation process, so that in the next lessons we will delve deeper into the build, evaluation, deployment, and monitoring process.

#### Prerequisites

An Azure subscription is required, where you can create an AI Project along with its AI Hub Resource, a Content Safety service, and an AI Search service.

#### Setup

- [Create an AI Project and AI Hub Resources](#create-an-ai-project-and-ai-hub-resouces)
- [Deploy an Azure OpenAI model](#deploy-an-azure-openai-model)

#### Exercise Steps

1) Use AzureAI Studio Playground.
2) Work with an Open Source LLM Model.
3) Test the prompt in Content Safety.
4) Create a Prompt Flow flow.

#### Setup

#####  Create an AI Project and AI Hub Resouces

Let's start by creating a project in Azure AI Studio.

Go to your browser and type: https://ai.azure.com

After logging in with your Azure account, you will see the following screen:

![LLMOps Workshop](images/labgrab1.png)

Select **+ New project** to create a project.

Choose an unique name for your project.

![LLMOps Workshop](images/labgrab2.png)

Select the **Create a new hub** link and choose a name for your AI hub where your project resources will be created.

![LLMOps Workshop](images/labgrab3.png)

> Note: Choose the region where the GPT-4 models and text-embeddings-ada-002 are available.

Still on this screen, select the **Create a new Azure AI Search** option; this service will be used in the following lessons.

![LLMOps Workshop](images/labgrab4.png)

Finally, select Create a project for the creation of the resources to be used in your project.

![LLMOps Workshop](images/labgrab5.png)

![LLMOps Workshop](images/labgrab6.png)

##### Deploy an Azure OpenAI model

After creating your AI Project, the first step is to create a deployment of an OpenAI model so you can start experimenting with the prompts you will use in your application.

To do this, select the **Deployments** option on the bottom of the project panel, and click on **Create deployment**.

![LLMOps Workshop](images/labgrab7.png)

From the list of models, select **gpt-4**.

![LLMOps Workshop](images/labgrab8.png)

On the next screen, define the name of the deployment, in this case, you can use the same name as the model and in the version field select the latest available version, in the example below we chose version **0125-Preview** (gpt4-turbo).

![LLMOps Workshop](images/labgrab9.png)

> Click on **Advanced Options** and select at least 40K **Tokens per Minute Rate Limit*** to ensure the flows run smoothly in the upcoming lessons.

Now, just click on **Deploy** and your model deployment is created. You can now test it in the Playground.

##### Create a Content Safety Service

By the end of this exercise, you will test with Content Safety. Therefore, click on the following link to create it [https://aka.ms/acs-create](https://aka.ms/acs-create). 

Select the resource group that you previously used for your AI Project. After that, follow the steps presented in the subsequent screens to continue with the creation process, start by clicking on **Review + create** button

![LLMOps Workshop](images/labgrab10.png)

Then click on **Create** to create your service.

![LLMOps Workshop](images/labgrab11.png)

Done! The Content Safety service is now created.

![LLMOps Workshop](images/labgrab12.png)


#### Exercise Steps

##### 1) Use AzureAI Studio Playground

On the screen with the deployment information, select the **Open in playground** button.

![LLMOps Workshop](images/labgrab13.png)

In this exercise, we will run an example where the model will help us summarize and extract information from a conversation between a customer and a representative of a telco company.

Copy the following prompt into the system message field of the playground:

```
You're an AI assistant that helps telco company to extract valuable information from their conversations by creating JSON files for each conversation transcription you receive. You always try to extract and format as a JSON:
1. Customer Name [name]
2. Customer Contact Phone [phone]
3. Main Topic of the Conversation [topic]
4. Customer Sentiment (Neutral, Positive, Negative)[sentiment]
5. How the Agent Handled the Conversation [agent_behavior]
6. What was the FINAL Outcome of the Conversation [outcome]
7. A really brief Summary of the Conversation [summary]

Only extract information that you're sure. If you're unsure, write "Unknown/Not Found" in the JSON file.
```

After copying, select **Apply changes**, (if prompted start a new chat)

![LLMOps Workshop](images/labgrab14.png)

Then type the following text in the chat session and click the send button:

```
Agent: Hello, welcome to Telco's customer service. My name is Juan, how can I assist you?
Client: Hello, Juan. I'm calling because I'm having issues with my mobile data plan. It's very slow and I can't browse the internet or use my apps.
Agent: I'm very sorry for the inconvenience, sir. Could you please tell me your phone number and your full name?
Client: Yes, sure. My number is 011-4567-8910 and my name is Martín Pérez.
Agent: Thank you, Mr. Pérez. I'm going to check your plan and your data usage. One moment, please.
Client: Okay, thank you.
Agent: Mr. Pérez, I've reviewed your plan and I see that you have contracted the basic plan of 2 GB of data per month. Is that correct?
Client: Yes, that's correct.
Agent: Well, I inform you that you have consumed 90% of your data limit and you only have 200 MB available until the end of the month. That's why your browsing speed has been reduced.
Client: What? How is that possible? I barely use the internet on my cell phone. I only check my email and my social networks from time to time. I don't watch videos or download large files.
Agent: I understand, Mr. Pérez. But keep in mind that some applications consume data in the background, without you realizing it. For example, automatic updates, backups, GPS, etc.
Client: Well, but they didn't explain that to me when I contracted the plan. They told me that with 2 GB I would have enough for the whole month. I feel cheated.
Agent: I apologize, Mr. Pérez. It was not our intention to deceive you. I offer you a solution: if you want, you can change your plan to a higher one, with more GB of data and higher speed. This way you can enjoy a better browsing experience.
Client: And how much would that cost me?
Agent: We have a special offer for you. For only 10 pesos more per month, you can access the premium plan of 5 GB of data and 4G speed. Are you interested?
Client: Mmm, I don't know. Isn't there another option? Can't you give me more speed without charging me more?
Agent: I'm sorry, Mr. Pérez. That's the only option we have available. If you don't change your plan, you'll have to wait until next month to recover your normal speed. Or you can buy an additional data package, but it would be more expensive than changing plans.
Client: Well, let me think about it. Can I call later to confirm?
Agent: Of course, Mr. Pérez. You can call whenever you want. The number is the same one you dialed now. Is there anything else I can help you with?
Client: No, that's all. Thank you for your attention.
Agent: Thank you, Mr. Pérez. Have a good day. Goodbye.
```

![LLMOps Workshop](images/labgrab15.png)

You will see a result generated by the model similar to the one shown in the image below.

Notice that the model correctly followed the instructions indicated in the System message field:

![LLMOps Workshop](images/labgrab16.png)

##### 2) Work with an Open Source LLM Model

Now let's test an open source Llama2 model from Meta.

For this, go to the **Deployments** section in the **Build** tab and click on **Create deployment**.

![LLMOps Workshop](images/labgrab17.png)

Select the model **Llama-2-13b-chat** and click on **confirm**.

![LLMOps Workshop](images/labgrab18.png)

Select the deployment option **Managed Compute without Azure AI Content Safety**.

![LLMOps Workshop](images/labgrab19.png)

Check the box that shows **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**.

Select the **Standard_NC24s_v3** compute for inference with the selected model, for this workshop one instance is enough.

If you do not have enough quota you can access the AzureML Quota option in the Managed tab to request an increase in quota for the selected resource.

Click the **Deploy** button.

![LLMOps Workshop](images/labgrab20.png)

The creation of the deployment will take a few minutes, the time varies, but generally between 10 and 20 minutes. ( If you notice your Traffic allocation is 0% select **Update traffic** and set it to 100%, if you get an error try again.)

![LLMOps Workshop](images/labgrab21.png)

Done! Let's test this model by selecting the **Test** option on the deployment page.

Select the gear icon on the top right of the chat and adjust the ```max_next_tokens``` parameter to 1000 so we can test the same example we used with the gpt-4 model. **Click Accept**

![LLMOps Workshop](images/labgrab22.png)

Now just copy the text below into the "Start typing here text box" and then send to observe the response generated by the Llama2 model.

```
{
  "input_data": {
    "input_string": [
      {
        "role": "system",
        "content": "You're an AI assistant that helps telco company to extract valuable information from their conversations by creating JSON documents for each conversation transcription you receive. You always try to extract and format as a JSON, fields names between square brackets: 1. Customer Name [name] 2. Customer Contact Phone [phone] 3. Main Topic of the Conversation [topic] 4. Customer Sentiment (Neutral, Positive, Negative)[sentiment] 5. How the Agent Handled the Conversation [agent_behavior] 6. What was the FINAL Outcome of the Conversation [outcome] 7. A really brief Summary of the Conversation [summary] Only extract information that you're sure. If you're unsure, write 'Unknown/Not Found' in the JSON file. Your answers outputs contains only the json document."
      },
      {
        "role": "user",
        "content": "Agent: Hello, welcome to Telco's customer service. My name is Juan, how can I assist you? Client: Hello, Juan. I'm calling because I'm having issues with my mobile data plan. It's very slow and I can't browse the internet or use my apps. Agent: I'm very sorry for the inconvenience, sir. Could you please tell me your phone number and your full name? Client: Yes, sure. My number is 011-4567-8910 and my name is Martín Pérez. Agent: Thank you, Mr. Pérez. I'm going to check your plan and your data usage. One moment, please. Client: Okay, thank you. Agent: Mr. Pérez, I've reviewed your plan and I see that you have contracted the basic plan of 2 GB of data per month. Is that correct? Client: Yes, that's correct. Agent: Well, I inform you that you have consumed 90% of your data limit and you only have 200 MB available until the end of the month. That's why your browsing speed has been reduced. Client: What? How is that possible? I barely use the internet on my cell phone. I only check my email and my social networks from time to time. I don't watch videos or download large files. Agent: I understand, Mr. Pérez. But keep in mind that some applications consume data in the background, without you realizing it. For example, automatic updates, backups, GPS, etc. Client: Well, but they didn't explain that to me when I contracted the plan. They told me that with 2 GB I would have enough for the whole month. I feel cheated. Agent: I apologize, Mr. Pérez. It was not our intention to deceive you. I offer you a solution: if you want, you can change your plan to a higher one, with more GB of data and higher speed. This way you can enjoy a better browsing experience. Client: And how much would that cost me? Agent: We have a special offer for you. For only 10 pesos more per month, you can access the premium plan of 5 GB of data and 4G speed. Are you interested? Client: Mmm, I don't know. Isn't there another option? Can't you give me more speed without charging me more? Agent: I'm sorry, Mr. Pérez. That's the only option we have available. If you don't change your plan, you'll have to wait until next month to recover your normal speed. Or you can buy an additional data package, but it would be more expensive than changing plans. Client: Well, let me think about it. Can I call later to confirm? Agent: Of course, Mr. Pérez. You can call whenever you want. The number is the same one you dialed now. Is there anything else I can help you with? Client: No, that's all. Thank you for your attention. Agent: Thank you, Mr. Pérez. Have a good day. Goodbye."
      }
    ],
    "parameters": {
      "temperature": 0.8,
      "top_p": 0.8,
      "do_sample": true,
      "max_new_tokens": 1000
    }
  }
}
```

You will see a result generated by the model similar to the one shown in the image below.

![LLMOps Workshop](images/labgrab23.png)

##### 3) Discover Content Safety

Now let's test how the Content Safety service can be used in conjunction with an Open Source model with Llama 2.

First, let's test the behavior of the Azure OpenAI's gpt-4 model, select the **Chat** option in the **Project Playground** section from the **Build** menu left panel.

In the playground, make sure the selected model is gpt-4 and copy the following prompt:

```
You're an AI assistant that helps telco company to extract valuable information from their conversations by creating JSON files for each conversation transcription you receive. 

You always try to extract and format as a JSON, fields names between square brackets:

1. Customer Name [name]
2. Customer Contact Phone [phone]
3. Main Topic of the Conversation [topic]
4. Customer Sentiment (Neutral, Positive, Negative)[sentiment]
5. How the Agent Handled the Conversation [agent_behavior]
6. What was the FINAL Outcome of the Conversation [outcome]
7. A really brief Summary of the Conversation [summary]

Conversation:

Agent: Hi Mr. Perez, welcome to Telco's customer service. My name is Juan, how can I assist you?
Client: Hello, Juan. I am very dissatisfied with your services.
Agent: ok sir, I am sorry to hear that, how can I help you?
Client: I hate this company I will kill everyone with a bomb.
```

Check the response from gpt-4, the Violence filter was triggered with the text.

![LLMOps Workshop](images/labgrab24.png)

Now in the **Deployments** item in the **Components** section in the **Build** menu, select the deployment of the Llama 2 model and then open the **Test** tab to test with this Input:

```
{
  "input_data": {
    "input_string": [
      {
        "role": "system",
        "content": "You're an AI assistant that helps telco company to extract valuable information from their conversations by creating JSON documents for each conversation transcription you receive. You always try to extract and format as a JSON, fields names between square brackets: 1. Customer Name [name] 2. Customer Contact Phone [phone] 3. Main Topic of the Conversation [topic] 4. Customer Sentiment (Neutral, Positive, Negative)[sentiment] 5. How the Agent Handled the Conversation [agent_behavior] 6. What was the FINAL Outcome of the Conversation [outcome] 7. A really brief Summary of the Conversation [summary] Only extract information that you're sure. If you're unsure, write 'Unknown/Not Found' in the JSON file. Your answers outputs contains only the json document."
      },
      {
        "role": "user",
        "content": "Agent: Hi Mr. Perez, welcome to Telco's customer service. My name is Juan, how can I assist you? Client: Hello, Juan. I am very dissatisfied with your services. Agent: ok sir, I am sorry to hear that, how can I help you? Client: I hate this company I will kill everyone with a bomb."
      }
    ],
    "parameters": {
      "temperature": 0.8,
      "top_p": 0.8,
      "do_sample": true,
      "max_new_tokens": 1000
    }
  }
}
```

Notice the result of the model, content was not blocked.

![LLMOps Workshop](images/labgrab25.png)

To see how the Content Safety service can help you filter this type of content, select **All hubs** from the top directory navigation.

![LLMOps Workshop](images/labgrab26.png)

Select the **AI Services** option from the left side build pane. From that point scroll down to **Content Safety** and select that option. 

![LLMOps Workshop](images/labgrab27.png)

Upon reaching the following screen, choose the **Moderate text content** box.

![LLMOps Workshop](images/labgrab28.png)

Scroll down and paste the same text used earlier into the **2. Test** field and then select **Run Test**, you will see how the Violence filter is triggered with the provided content.

![LLMOps Workshop](images/labgrab29.png)

##### 4) Create a Prompt Flow flow

Great, now that you have seen how you can deploy models, test them in the playground, and also seen a bit of how Content Safety works, let's see how you can create an orchestration flow for your LLM application in Prompt Flow.

To start, let's go back to the Playground with the gpt-4 model, add the same system message that we used in the initial test and then click on the  **Apply Changes** option.

```
You're an AI assistant that helps telco company to extract valuable information from their conversations by creating JSON files for each conversation transcription you receive. You always try to extract and format as a JSON:
1. Customer Name [name]
2. Customer Contact Phone [phone]
3. Main Topic of the Conversation [topic]
4. Customer Sentiment (Neutral, Positive, Negative)[sentiment]
5. How the Agent Handled the Conversation [agent_behavior]
6. What was the FINAL Outcome of the Conversation [outcome]
7. A really brief Summary of the Conversation [summary]

Only extract information that you're sure. If you're unsure, write "Unknown/Not Found" in the JSON file.
```

![LLMOps Workshop](images/labgrab30.png)

By doing this, you will create a new flow in Prompt Flow.

Click **Prompt flow** then **Open** to open your newly created flow.

In the following figure, on the right side, a single node represents the step in the flow where the LLM model is called.

![LLMOps Workshop](images/labgrab31.png)

Observe that the Playground's configuration for deployment, prompt, and parameters like temperature and max_tokens were used to populate the created flow. (if you do not see this make sure the connection is specified)

To execute the flow within the Studio, you'll require a Runtime. To initiate it, simply choose the "Start compute session" option from the Runtime dropdown menu.

![LLMOps Workshop](images/labgrab32.png)

Done! Now just select the started Runtime and click on the blue **Chat** button to test your flow in the chat window.

![LLMOps Workshop](images/labgrab33.png)

Paste the same content used in the initial Playground test and send it in the chat, you will see the expected result as can be seen in the next image: (if you encounter a 404 error, please verify you selected a connection)

```
Agent: Hello, welcome to Telco's customer service. My name is Juan, how can I assist you?
Client: Hello, Juan. I'm calling because I'm having issues with my mobile data plan. It's very slow and I can't browse the internet or use my apps.
Agent: I'm very sorry for the inconvenience, sir. Could you please tell me your phone number and your full name?
Client: Yes, sure. My number is 011-4567-8910 and my name is Martín Pérez.
Agent: Thank you, Mr. Pérez. I'm going to check your plan and your data usage. One moment, please.
Client: Okay, thank you.
Agent: Mr. Pérez, I've reviewed your plan and I see that you have contracted the basic plan of 2 GB of data per month. Is that correct?
Client: Yes, that's correct.
Agent: Well, I inform you that you have consumed 90% of your data limit and you only have 200 MB available until the end of the month. That's why your browsing speed has been reduced.
Client: What? How is that possible? I barely use the internet on my cell phone. I only check my email and my social networks from time to time. I don't watch videos or download large files.
Agent: I understand, Mr. Pérez. But keep in mind that some applications consume data in the background, without you realizing it. For example, automatic updates, backups, GPS, etc.
Client: Well, but they didn't explain that to me when I contracted the plan. They told me that with 2 GB I would have enough for the whole month. I feel cheated.
Agent: I apologize, Mr. Pérez. It was not our intention to deceive you. I offer you a solution: if you want, you can change your plan to a higher one, with more GB of data and higher speed. This way you can enjoy a better browsing experience.
Client: And how much would that cost me?
Agent: We have a special offer for you. For only 10 pesos more per month, you can access the premium plan of 5 GB of data and 4G speed. Are you interested?
Client: Mmm, I don't know. Isn't there another option? Can't you give me more speed without charging me more?
Agent: I'm sorry, Mr. Pérez. That's the only option we have available. If you don't change your plan, you'll have to wait until next month to recover your normal speed. Or you can buy an additional data package, but it would be more expensive than changing plans.
Client: Well, let me think about it. Can I call later to confirm?
Agent: Of course, Mr. Pérez. You can call whenever you want. The number is the same one you dialed now. Is there anything else I can help you with?
Client: No, that's all. Thank you for your attention.
Agent: Thank you, Mr. Pérez. Have a good day. Goodbye.
```

Results:

![LLMOps Workshop](images/labgrab34.png)


#### Removing your Llama 2 deployment

In this exercise, you've used a **Standard_NC24s_v3** SKU to deploy your Llama2 model. To prevent incurring high costs, it's recommended to delete this deployment now since it won't be used in the next labs.

To do this, select **Delete deployment** on the screen with the Llama2 deployment.

![LLMOps Workshop](images/labgrab35.png)

Click on **Delete**, as shown in the following screen, to complete the removal.

![LLMOps Workshop](images/labgrab36.png)

Give it a few minutes or so then select **Refresh** to verify the llama-2 deployment is no longer available or in the status **Deleting**.
