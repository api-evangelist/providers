---
aid: microsoft-azure-functions
name: Microsoft Azure Functions
description: Azure Functions is a serverless compute platform from Microsoft Azure enabling event-driven code execution triggered by HTTP requests, timers, queues, blobs, and other Azure services. The Azure Functions management API provides programmatic access to function app lifecycle management, deployment, configuration, scaling, and monitoring through Azure Resource Manager.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-functions/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-17'
specificationVersion: '0.19'
tags:
  - Azure
  - Cloud
  - Compute
  - Event-Driven
  - Microsoft
  - Serverless
apis:
  - aid: microsoft-azure-functions:azure-functions-management-api
    name: Azure Functions Management API
    description: The Azure App Service / Web Apps REST API provides management operations for Azure Functions apps including creating and configuring function apps, managing deployment slots, application settings, host keys, function keys, scaling configuration, and monitoring. Part of the Azure Resource Manager API surface.
    humanURL: https://learn.microsoft.com/en-us/rest/api/appservice/web-apps
    baseURL: https://management.azure.com
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/appservice/web-apps
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/azure/azure-functions/functions-get-started
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/appservice/web-apps/get
      - type: Authentication
        url: https://learn.microsoft.com/en-us/rest/api/azure/#register-your-client-application-with-azure-ad
      - type: OpenAPI
        url: openapi/azure-functions-management-api.json
    tags:
      - App Service
      - Deployment
      - Functions
      - Management
      - Resource Manager
      - Serverless
  - aid: microsoft-azure-functions:azure-functions-runtime-api
    name: Azure Functions Runtime API
    description: The Azure Functions host runtime provides HTTP endpoints for function invocation, admin operations, host status, function management, and key management. Includes endpoints for listing functions, getting function status, managing host and function keys, and triggering function execution.
    humanURL: https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference
    baseURL: https://{functionapp}.azurewebsites.net
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-csharp
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/azure-functions/security-concepts
    tags:
      - Event-Driven
      - Functions
      - HTTP Trigger
      - Runtime
      - Serverless
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/azure/azure-functions/functions-get-started
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/azure-functions/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/functions/
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: StatusPage
    url: https://status.azure.com/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/
  - type: ChangeLog
    url: https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions
  - type: GitHubOrganization
    url: https://github.com/Azure
  - type: GitHubRepository
    url: https://github.com/Azure/azure-functions-host
  - type: GitHubRepository
    url: https://github.com/Azure/azure-functions-core-tools
  - type: SDK
    url: https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker
    title: .NET SDK
  - type: SDK
    url: https://pypi.org/project/azure-functions/
    title: Python SDK
  - type: SDK
    url: https://www.npmjs.com/package/@azure/functions
    title: Node.js SDK
  - type: SDK
    url: https://central.sonatype.com/artifact/com.microsoft.azure.functions/azure-functions-java-library
    title: Java SDK
  - type: CLI
    url: https://github.com/Azure/azure-functions-core-tools
    title: Azure Functions Core Tools
  - type: CLI
    url: https://learn.microsoft.com/en-us/cli/azure/functionapp
    title: Azure CLI (az functionapp)
  - type: Training
    url: https://learn.microsoft.com/en-us/training/paths/create-serverless-applications/
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/azure-functions
  - type: X
    url: https://x.com/AzureFunctions
  - type: Features
    data:
      - name: HTTP Triggers
        description: Execute functions via HTTP requests with RESTful endpoint support and built-in authentication.
      - name: Timer Triggers
        description: Schedule function execution using CRON expressions for recurring tasks.
      - name: Queue Triggers
        description: Process messages from Azure Storage Queues and Service Bus for async workloads.
      - name: Blob Triggers
        description: React to blob storage changes for file processing and data pipeline automation.
      - name: Event Grid Triggers
        description: Handle events from Azure Event Grid for event-driven architectures.
      - name: Cosmos DB Triggers
        description: Process database changes in Azure Cosmos DB using the change feed.
      - name: Durable Functions
        description: Orchestrate complex stateful workflows with function chaining, fan-out/fan-in, and human interaction patterns.
      - name: Deployment Slots
        description: Manage staging and production slots for zero-downtime deployments and traffic splitting.
      - name: Custom Handlers
        description: Run functions in any language by implementing a lightweight HTTP server.
      - name: Managed Identity
        description: Authenticate to Azure services without managing credentials using system or user-assigned identities.
      - name: Scaling
        description: Automatic scaling from zero to thousands of instances based on event load.
      - name: Premium Plan
        description: Pre-warmed instances, VNET integration, and unlimited execution duration for enterprise workloads.
  - type: UseCases
    data:
      - name: API Backend
        description: Build serverless REST APIs with HTTP-triggered functions and Azure API Management integration.
      - name: Event Processing
        description: Process events from queues, topics, Event Grid, and IoT Hub for real-time data pipelines.
      - name: Scheduled Tasks
        description: Run scheduled jobs for data cleanup, report generation, and system maintenance.
      - name: File Processing
        description: Transform, validate, and process files uploaded to blob storage.
      - name: Webhook Handling
        description: Receive and process webhooks from third-party services and SaaS platforms.
      - name: Microservices
        description: Build lightweight microservices with independent scaling and deployment.
      - name: Data Transformation
        description: ETL workloads for transforming and loading data between Azure services.
      - name: IoT Backend
        description: Process IoT device telemetry and events with Event Hub and IoT Hub triggers.
  - type: Integrations
    data:
      - name: Azure API Management
        description: Front Azure Functions with API Management for rate limiting, authentication, and developer portal.
      - name: Azure DevOps
        description: CI/CD pipeline integration for automated function deployment and testing.
      - name: GitHub Actions
        description: Deploy Azure Functions directly from GitHub repositories with Actions workflows.
      - name: Visual Studio Code
        description: Full development experience with the Azure Functions VS Code extension.
      - name: Azure Monitor
        description: Application Insights integration for function monitoring, logging, and diagnostics.
      - name: Azure Key Vault
        description: Secure secrets management with Key Vault references in application settings.
      - name: Terraform
        description: Infrastructure-as-code management of function apps with the AzureRM Terraform provider.
  - type: Solutions
    data:
      - name: Consumption Plan
        description: Pay-per-execution pricing with automatic scaling and 5-minute execution timeout.
      - name: Premium Plan
        description: Pre-warmed instances, VNET integration, unlimited duration, and larger instance sizes.
      - name: Dedicated Plan
        description: Run functions on dedicated App Service plans for predictable pricing and always-on execution.
      - name: Container Apps
        description: Run containerized functions on Azure Container Apps for Kubernetes-based hosting.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
