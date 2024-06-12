---
title: 'Exercise 06: Automate Everything'
layout: default
nav_order: 7
has_children: true
---

# Exercise 06 - Automate Everything

## Scenario

In this exercise, you will learn how to automate the build, evaluation, and deployment of your LLM orchestration flow. To accomplish this, we will use the LLMOps with Prompt Flow template [**LLMOps with Prompt Flow**](https://github.com/microsoft/llmops-promptflow-template)  as a reference for deploying an LLM using **Prompt Flow** and **GitHub Actions**. This automation is crucial for Lamna Healthcare Company to ensure efficient and error-free deployment processes for their 24/7 support virtual agent.

By mastering these objectives, Lamna's team will enhance their ability to manage AI projects autonomously, ensuring streamlined operations and effective utilization of Azure AI services for their healthcare solutions.

## Setup and initial instruction

The **LLMOps with Prompt Flow** template includes three example use cases: `named_entity_recognition`, `web_classification`, and `math_coding`. The examples can serve as a reference for you to automate your own orchestration flow. For each example, a set of GitHub workflows has been provided to automate everything from unit testing to the deployment of the flow. These workflow files are located in the template's `.github/workflows` directory.

In this exercise, we will use the **named_entity_recognition** example, which comes with the following workflows:

- The initial workflow, named `named_entity_recognition_pr_dev_workflow.yml`, is automatically triggered whenever a pull request (PR) is created. The primary objective of this workflow is to ensure that the code standards are consistently maintained across all submitted PRs.

- The second workflow, named `named_entity_recognition_ci_dev_workflow.yml`, is configured to trigger automatically before a pull request (PR) is merged into the *development* branch. This workflow will perform a comprehensive execution and evaluation across the entire dataset for every prompt variant.

- The third workflow, named `named_entity_recognition_post_prod_eval.yml`, is designed to be run manually following the deployment of the Prompt Flow to the production environment. This workflow's purpose is to gather production logs in order to assess the performance of the Prompt Flow in the live setting.

The template example was designed for a branch structure where there is a development branch where the team integrates code changes that go into the development environment.

In this exercise, for simplicity's sake, we will only go up to step 5 of the diagram at the beginning of this page, but the knowledge gained can be easily applied to extend the flow and configuration files for automating steps 6 onwards.

## Objectives

After you complete this exercise, you will be able to:

- Discuss further the topics of this exercise
- Create a project and associate resources without instruction

## Lab Duration

- **Estimated Time:** 120 minutes
