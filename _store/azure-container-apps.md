---
aid: azure-container-apps
name: Azure Container Apps
description: Azure Container Apps is a serverless container service for running microservices and containerized applications with built-in autoscaling, traffic splitting, and Dapr integration. It enables developers to deploy containers without managing complex infrastructure while supporting event-driven architectures and microservices patterns.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Azure
  - Containers
  - Dapr
  - Kubernetes
  - Microservices
  - Serverless
url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: azure-container-apps:azure-container-apps
    name: Azure Container Apps
    description: Azure Container Apps is a serverless container service for running microservices and containerized applications with built-in autoscaling, traffic splitting, and Dapr integration. It enables developers to deploy containers without managing complex infrastructure while supporting event-driven architectures and microservices patterns.
    humanURL: https://azure.microsoft.com/en-us/products/container-apps
    tags:
      - Azure
      - Containers
      - Kubernetes
      - Microservices
      - Serverless
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/openapi/azure-container-apps-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/json-schema/azure-container-apps-container-app-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/json-schema/azure-container-apps-managed-environment-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/json-schema/azure-container-apps-job-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/json-schema/azure-container-apps-revision-schema.json
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/container-apps/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/azure/container-apps/get-started
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/resource-manager/containerapps/operation-groups
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/container-apps/authentication
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/container-apps/
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/container-apps/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/azure/container-apps/get-started
  - type: GitHubRepository
    url: https://github.com/microsoft/azure-container-apps
  - type: GitHubOrganization
    url: https://github.com/Azure
  - type: Blog
    url: https://techcommunity.microsoft.com/blog/appsonazureblog/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/container-apps/
  - type: StatusPage
    url: https://status.azure.com/
  - type: TermsOfService
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: SignUp
    url: https://azure.microsoft.com/en-us/free/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: FAQ
    url: https://learn.microsoft.com/en-us/azure/container-apps/faq
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/rules/azure-container-apps-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/vocabulary/azure-container-apps-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/capabilities/shared/azure-container-apps.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/capabilities/container-apps-management.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/json-ld/azure-container-apps-context.jsonld
  - type: Features
    data:
      - name: Serverless Containers
        description: Run containers without managing servers or Kubernetes cluster infrastructure.
      - name: Built-in Autoscaling
        description: Automatically scale based on HTTP traffic, event messages, or custom KEDA scalers.
      - name: Traffic Splitting
        description: Gradually shift traffic between container revisions for canary deployments and A/B testing.
      - name: Dapr Integration
        description: Built-in support for the Dapr distributed application runtime for service discovery and state management.
      - name: Managed Environments
        description: Shared networking and logging infrastructure for groups of container apps.
      - name: Dynamic Sessions
        description: Secure, ephemeral code-interpreter and custom container sessions with data-plane REST APIs.
      - name: Jobs Support
        description: Schedule and run containerized batch jobs on demand or on a schedule.
      - name: GPU Support
        description: Deploy AI/ML workloads on GPU-enabled container instances.
  - type: UseCases
    data:
      - name: Microservices Architecture
        description: Deploy and scale individual microservices independently with built-in service discovery.
      - name: API Backend Deployment
        description: Host REST APIs with automatic HTTPS, custom domains, and traffic management.
      - name: Event-Driven Processing
        description: Process messages from Service Bus, Event Hubs, and storage queues with KEDA-based scaling.
      - name: AI and ML Workloads
        description: Run AI inference workloads on GPU-enabled container instances with dynamic sessions.
      - name: Background Jobs
        description: Run scheduled and on-demand batch jobs without maintaining dedicated infrastructure.
      - name: Dapr Microservices
        description: Build microservices with Dapr for pub/sub messaging, service invocation, and state management.
  - type: Integrations
    data:
      - name: Azure Kubernetes Service
        description: Share underlying Kubernetes infrastructure while abstracting cluster management complexity.
      - name: Azure Container Registry
        description: Pull container images directly from private ACR registries with managed identity.
      - name: Azure Service Bus
        description: Trigger container app scaling based on Service Bus queue depth.
      - name: Azure Event Hubs
        description: Process streaming data from Event Hubs with auto-scaling.
      - name: GitHub Actions
        description: Deploy container apps directly from GitHub Actions CI/CD workflows.
      - name: Dapr
        description: Built-in Dapr runtime support for distributed systems patterns.
      - name: Azure Monitor
        description: Native integration with Azure Monitor and Log Analytics for observability.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
