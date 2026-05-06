---
aid: azure-cloud
name: Microsoft Azure Cloud
description: A comprehensive collection of Microsoft Azure cloud service APIs covering compute, storage, databases, AI, networking, security, and developer tools. Azure provides IaaS, PaaS, and SaaS delivery models through a global network of datacenters, with REST APIs secured by Microsoft Entra ID authentication.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Cloud Computing
  - Databases
  - IaaS
  - Infrastructure
  - Machine Learning
  - Microsoft
  - Networking
  - PaaS
  - Platform as a Service
  - SaaS
  - Storage
url: https://raw.githubusercontent.com/api-evangelist/azure-cloud/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: azure-cloud:azure-compute-api
    name: Azure Compute API
    description: Manage virtual machines, containers, serverless functions, and Kubernetes clusters. Includes Azure Virtual Machines, Azure Kubernetes Service (AKS), Azure Container Apps, Azure Functions, and App Service APIs.
    humanURL: https://learn.microsoft.com/en-us/rest/api/compute/
    baseURL: https://management.azure.com
    tags:
      - App Service
      - Compute
      - Containers
      - Functions
      - Kubernetes
      - Serverless
      - Virtual Machines
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/compute/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/azure/virtual-machines/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/compute/resource-manager/Microsoft.Compute/stable/2023-03-01/compute.json
  - aid: azure-cloud:azure-storage-api
    name: Azure Storage API
    description: Scalable cloud storage REST APIs for blobs, files, queues, and tables. Includes Blob Storage, Azure Files, Queue Storage, Table Storage, and Azure Data Lake Storage.
    humanURL: https://learn.microsoft.com/en-us/rest/api/storageservices/
    baseURL: https://management.azure.com
    tags:
      - Blob Storage
      - Cloud Storage
      - File Storage
      - Object Storage
      - Queue Storage
      - Storage
      - Table Storage
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/storageservices/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/storage/resource-manager/Microsoft.Storage/stable/2023-01-01/storage.json
  - aid: azure-cloud:azure-networking-api
    name: Azure Networking API
    description: REST APIs for Azure networking resources including Virtual Networks, Load Balancers, Application Gateways, VPN Gateways, Azure Firewall, Front Door, and ExpressRoute.
    humanURL: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/
    baseURL: https://management.azure.com
    tags:
      - ExpressRoute
      - Firewall
      - Load Balancer
      - Networking
      - Virtual Network
      - VPN
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/
  - aid: azure-cloud:azure-databases-api
    name: Azure Databases API
    description: Managed database REST APIs for Azure SQL Database, Azure Cosmos DB, Azure Database for PostgreSQL, Azure Database for MySQL, and Azure Cache for Redis.
    humanURL: https://learn.microsoft.com/en-us/rest/api/sql/
    baseURL: https://management.azure.com
    tags:
      - Cosmos DB
      - Databases
      - MySQL
      - NoSQL
      - PostgreSQL
      - Redis
      - SQL
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/sql/
  - aid: azure-cloud:azure-ai-api
    name: Azure AI Services API
    description: REST APIs for Azure AI and Machine Learning services including Azure OpenAI Service, Azure Machine Learning, Azure AI Search, Computer Vision, Speech, and Document Intelligence.
    humanURL: https://learn.microsoft.com/en-us/azure/ai-services/
    baseURL: https://management.azure.com
    tags:
      - AI
      - Artificial Intelligence
      - Computer Vision
      - Language
      - Machine Learning
      - OpenAI
      - Speech
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/ai-services/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/cognitiveservices/
  - aid: azure-cloud:azure-security-api
    name: Azure Security API
    description: REST APIs for Azure security services including Microsoft Defender for Cloud, Key Vault, Microsoft Sentinel, and Web Application Firewall.
    humanURL: https://learn.microsoft.com/en-us/rest/api/defenderforcloud/
    baseURL: https://management.azure.com
    tags:
      - Defender
      - Identity
      - Key Vault
      - Security
      - Sentinel
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/defenderforcloud/
  - aid: azure-cloud:azure-integration-api
    name: Azure Integration API
    description: REST APIs for Azure integration services including Service Bus, Event Grid, Logic Apps, and API Management for building event-driven and workflow-based applications.
    humanURL: https://learn.microsoft.com/en-us/rest/api/servicebus/
    baseURL: https://management.azure.com
    tags:
      - API Management
      - Event Grid
      - Integration
      - Logic Apps
      - Messaging
      - Service Bus
      - Workflows
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/servicebus/
  - aid: azure-cloud:azure-analytics-api
    name: Azure Analytics API
    description: REST APIs for Azure analytics services including Synapse Analytics, Data Factory, Stream Analytics, Data Explorer, and Microsoft Fabric for big data and real-time analytics workloads.
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/
    baseURL: https://management.azure.com
    tags:
      - Analytics
      - Big Data
      - Data Factory
      - ETL
      - Stream Analytics
      - Synapse
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/
  - aid: azure-cloud:azure-management-api
    name: Azure Management API
    description: REST APIs for Azure management and governance including Azure Resource Manager, Azure Monitor, Azure Policy, Cost Management, and Azure Advisor.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/
    baseURL: https://management.azure.com
    tags:
      - Cost Management
      - Governance
      - Management
      - Monitor
      - Policy
      - Resource Manager
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/resources/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/rest/api/azure/#register-your-client-application-with-microsoft-entra-id
  - aid: azure-cloud:azure-iot-api
    name: Azure IoT API
    description: REST APIs for Azure IoT services including IoT Hub, IoT Central, IoT Edge, and Azure Digital Twins for connecting, monitoring, and managing IoT devices at scale.
    humanURL: https://learn.microsoft.com/en-us/rest/api/iothub/
    baseURL: https://management.azure.com
    tags:
      - Digital Twins
      - IoT
      - IoT Central
      - IoT Edge
      - IoT Hub
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/iothub/
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/azure/developer/intro/azure-developer-overview
  - type: APIReference
    url: https://learn.microsoft.com/en-us/rest/api/azure/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-client-creds-grant-flow
  - type: StatusPage
    url: https://status.azure.com
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: TermsOfService
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: GitHubOrganization
    url: https://github.com/Azure
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/
  - type: SignUp
    url: https://azure.microsoft.com/en-us/free/
  - type: CLI
    url: https://learn.microsoft.com/en-us/cli/azure/
  - type: SDK
    url: https://azure.github.io/azure-sdk/
  - type: Features
    data:
      - name: Global Infrastructure
        description: Operates across 60+ regions worldwide with 99.99% SLA guarantees for most services.
      - name: Microsoft Entra ID Authentication
        description: All REST APIs use OAuth 2.0 / Microsoft Entra ID for secure, standards-based authentication.
      - name: Azure Resource Manager
        description: Consistent management layer for deploying and managing all Azure resources via ARM templates and REST.
      - name: Async Operations
        description: Long-running operations follow the async pattern with polling endpoints for status checks.
      - name: Throttling and Rate Limits
        description: Per-subscription throttling with remaining request counts returned in response headers.
      - name: Pagination
        description: List operations return nextLink for cursor-based pagination across large result sets.
      - name: Multi-Language SDKs
        description: Official SDKs available for .NET, Java, Python, JavaScript/TypeScript, Go, C++, and Rust.
      - name: Hybrid and Multi-Cloud
        description: Azure Arc extends Azure management to on-premises and multi-cloud environments.
  - type: UseCases
    data:
      - name: Enterprise Cloud Migration
        description: Migrate on-premises workloads to Azure using IaaS VMs or PaaS services with hybrid connectivity.
      - name: Cloud-Native Application Development
        description: Build microservices using Azure Kubernetes Service, Container Apps, and serverless Functions.
      - name: AI and Machine Learning Workloads
        description: Train and deploy ML models using Azure Machine Learning and Azure OpenAI Service.
      - name: Data Analytics and Business Intelligence
        description: Build data pipelines with Data Factory and analyze at scale with Synapse Analytics.
      - name: DevOps and CI/CD Automation
        description: Automate build, test, and deployment pipelines using Azure DevOps and GitHub Actions.
      - name: IoT Device Management
        description: Connect and manage millions of IoT devices with IoT Hub and IoT Central.
      - name: Security and Compliance
        description: Protect workloads and meet compliance requirements with Defender for Cloud and Sentinel.
  - type: Integrations
    data:
      - name: GitHub
        description: Native integration with GitHub for source control, Actions CI/CD, and Azure deployment.
      - name: Microsoft 365
        description: Integration with Microsoft 365 services via Microsoft Graph API.
      - name: Terraform
        description: Azure Provider for Terraform enables infrastructure-as-code deployments.
      - name: Visual Studio / VS Code
        description: First-class Azure extension support in Visual Studio and Visual Studio Code.
      - name: Kubernetes
        description: Azure Kubernetes Service provides managed Kubernetes with deep Azure ecosystem integration.
      - name: Datadog
        description: Native Datadog integration for monitoring Azure infrastructure and applications.
      - name: Splunk
        description: Splunk Add-on for Microsoft Azure for security and operational analytics.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
