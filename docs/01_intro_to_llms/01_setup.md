---
title: '0. Setup'
layout: default
nav_order: 1
parent: 'Exercise 01: Introduction to LLMs and Azure AI Services'
---

# Exercise 01 - Setup AI Project and AI Hub Resources

## Description

In this setup task, you will learn how to **start a new project** by creating a **GitHub repository** and an **AI Project** in a centralized **Azure AI Hub**. The **Azure AI Hub** is a top-level resource in Azure AI Studio that enables **governance, self-service, security**, and **collaboration for AI projects**.

## Success Criteria

* Verify Prerequisites for Workshop
* Initialize a GitHub Repository for Your Project
* Set Up an Azure AI Hub and Project

## Prerequisites
<details markdown="block">
<summary>Expand this section to view the prerequisites</summary>

### Required Tools
* [Azure CLI (az)](https://aka.ms/install-az) - to manage Azure resources.
* [Azure Developer CLI (azd)](https://aka.ms/install-azd) - to manage Azure deployments.
* [GitHub CLI (gh)](https://cli.github.com/) - to create GitHub repo.
* [Git](https://git-scm.com/downloads) - to update repository contents.

### You will also need:
* [Azure Subscription](https://azure.microsoft.com/free/) - sign up for a free account.
* [GitHub Account](https://github.com/signup) - sign up for a free account.
* [Access to Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/limited-access) - submit a form to request access.
* Permissions to create a Service Principal (SP) in your Azure AD Tenant.
* Permissions to assign the Owner role or Contributor and User Access Administrator to the SP within the subscription.

> **Note:**   
> The Windows installers makes modifications your PATH. When using Windows Terminal or VS Code Terminal or other environment, you will need to **open a new window** for the changes to take effect. (Simply opening a new tab will _not_ be sufficient.)

### Verifiy tools are installed

**from a commandline verify the tools are installed and on your path**

   Open a Windows Terminal or Command Prompt:

   ```sh
    az -v
    azd version
    git -v
    gh --version
   ```
> **Note:**
> if any of the tools suggest an upgrade please do so this can be acomplished with the ```winget upgrade``` conmand 


### Check Azure OpenAI Model Availability:
You will need 40k TPM of gpt-35-turbo, gpt-4o and text-embedding-ada-002 models. If the region you want to use does not have availability, you can choose another region. You can run the following command in powershell or bash to check how many TPMs do you have available for those models in the desired region/sub.

#### Powershell

```powershell
$subscriptionId = "replace by your subscription id" 
$region = "replace by the desired region" 
$results = az cognitiveservices usage list --subscription $subscriptionId --location $region 
$results | ConvertFrom-Json | Where-Object { $_.name.value -eq 'OpenAI.Standard.gpt-4o' } | Select-Object *
$results | ConvertFrom-Json | Where-Object { $_.name.value -eq 'OpenAI.Standard.gpt-35-turbo' } | Select-Object *
$results | ConvertFrom-Json | Where-Object { $_.name.value -eq 'OpenAI.Standard.text-embedding-ada-002' } | Select-Object *
```

#### bash

```bash
subscriptionId="replace by your subscription id" 
region="replace by the desired region" 
results=$(az cognitiveservices usage list --subscription $subscriptionId --location $region) 
echo $results | jq -r '.[] | select(.name.value == "OpenAI.Standard.gpt-4o")'
echo $results | jq -r '.[] | select(.name.value == "OpenAI.Standard.gpt-35-turbo")'
echo $results | jq -r '.[] | select(.name.value == "OpenAI.Standard.text-embedding-ada-002")'
```
</details>

## Setup Steps
<details markdown="block">
<summary>Expand this section to view the solution</summary>

### Steps to Bootstrap a Project

The bootstrapping process involves **creating a new project repository on GitHub** and populating it with content from a project template. Additionally, it sets up the **development environment** for your project. This environment will include an **Azure AI Studio project** and deploy the necessary resources to support a centralized **Azure AI Hub**.

1. **Clone the GenAIOps Repo into a temporary directory**

   Clone the repository from GitHub into a temporary directory:

   ```sh
    mkdir temp
    cd temp
    git clone https://github.com/azure/GenAIOps
   ```

2. **Define Properties for Bootstrapping**

    Go to the `GenAIOps` directory.

   ```sh
    cd GenAIOps
   ```

   Create a copy of the `bootstrap.properties.template` file with this filename `bootstrap.properties`.

    ```sh
    cp bootstrap.properties.template bootstrap.properties
    ```

    Open the `bootstrap.properties` with a text editor and update it with the following information:

   - **GitHub Repo Creation** (related to the new repository to be created)
     - `github_username`: Your GitHub **username**.
     - `github_use_ssh`: Set to **false** to use [HTTPS](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls) or **true** to interact with GitHub repos using [SSH](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-ssh-urls).
     - `github_template_repo`: Set **azure/GenAIOps-project-template**.
     - `github_new_repo`: The bootstrapped project repo to be created. Ex: *placerda/my-rag-project*.
     - `github_new_repo_visibility`: Set to **public**.

   - **Dev Environment Provision Properties**
     - `azd_dev_env_provision`: Set to **true** to provision a development environment.
     
          > If you set it to **false**, you will need to manually create the environment for the project.

     - `azd_dev_env_name`: The name of the development environment. Ex: *rag-project-dev*.
     - `azd_dev_env_subscription`: Your Azure subscription ID.
     - `azd_dev_env_location`: The Azure region for your dev environment. Ex: *eastus2*.

    > The dev environment resources will be created in the selected subscription and region. This decision should consider the quota available for the resources to be created in the region, as well as the fact that some resources have specific features enabled only in certain regions. Therefore, ensure that the resources to be created by the IaC of your template project have quota and availability in the chosen subscription and region. More information about the resources to be created can be found on the template page, as shown in this project template example: [GenAIOps Project Template Resources](https://github.com/Azure/GenAIOps-project-template/blob/main/README.md#project-resources).

   Here is an example of the `bootstrap.properties` file:

   ```properties
   github_username="placerda"
   github_use_ssh="false"
   github_template_repo="azure/GenAIOps-project-template"
   github_new_repo="placerda/my-rag-project"
   github_new_repo_visibility="public"
   azd_dev_env_provision="true"
   azd_dev_env_name="rag-project-dev"
   azd_dev_env_subscription="12345678-1234-1234-1234-123456789098"
   azd_dev_env_location="eastus2"
   ```

3. **Authenticate with Azure and GitHub**

   Log in to Azure CLI:

   ```sh
   az login
   ```

   Log in to Azure Developer CLI:

   ```sh
   azd auth login
   ```

   Log in to GitHub CLI:

   ```sh
   gh auth login
   ```

4. **Run the Bootstrap Script**

   The bootstrap script is available in two versions: Bash (`bootstrap.sh`) and PowerShell (`bootstrap.ps1`).

   Run the appropriate script for your environment.

   **For Bash:**

   ```sh
   ./bootstrap.sh
   ```

   **For PowerShell:**

   ```powershell
   .\bootstrap.ps1
   ```

    At the end of its execution, the script will have created and initialized the new repository and provisioned the development environment resources, provided you set `azd_dev_env_provision` to true. During its execution, the script checks if the new repository exists and creates it if it does not. It then clones the template repository and mirrors it to the new repository. Additionally, it sets the default branch for the new repository.

5. **Create a Service Principal**

   Create a service principal using the following command:

   ```sh
   az ad sp create-for-rbac --name "<your-service-principal-name>" --role Owner --scopes /subscriptions/<your-subscription-id> --sdk-auth
   ```

   > Ensure that the output information created here is properly saved for future use.

6. **Set GitHub Environment Variables**

   Go to the newly created project repository and set the following GitHub environment variables and secret for three environments: `dev`, `qa`, and `prod`.

   - **Environment Variables:**
     - `AZURE_ENV_NAME`
     - `AZURE_LOCATION`
     - `AZURE_SUBSCRIPTION_ID`
   
   - **Secret:**
     - `AZURE_CREDENTIALS`

   After creating the variables and secret, your Environments page should resemble the following example:
   
   ![Environments Page](images/bootstrapping_environments.png)
   
   Below is an example of environment variable values for a development environment:
   
   ![Environment Variables](images/bootstrapping_env_vars.png)
   
   The `AZURE_CREDENTIALS` secret should be formatted as follows:
    
   ```json
   {
       "clientId": "your-client-id",
       "clientSecret": "your-client-secret",
       "subscriptionId": "your-subscription-id",
       "tenantId": "your-tenant-id"
   }
   ```

   > **Note:** If you are only interested in experimenting with this accelerator, you can use the same subscription, varying only `AZURE_ENV_NAME` for each enviornment.

7. **Enable GitHub Actions**

   Ensure that GitHub Actions are enabled in your repository, as in some cases, organizational policies may not have this feature enabled by default. To do this, simply click the button indicated in the figure below:

   ![Enable Actions](images/enable_github_actions.png)

That's all! Your new project is now bootstrapped and you are ready to start the workshop.
</details>