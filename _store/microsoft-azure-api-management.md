---
aid: microsoft-azure-api-management
name: Microsoft Azure API Management
description: Microsoft Azure API Management is a hybrid, multicloud management platform for APIs across all environments. It provides an API gateway, management plane, and developer portal supporting the complete API lifecycle including publishing, securing, monitoring, and transforming APIs for external, partner, and internal developers. It includes an AI gateway for governing LLM deployments, MCP servers, and agentic AI workloads.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Gateway
  - API Gateway
  - API Management
  - Enterprise
  - Microsoft Azure
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-api-management/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-azure-api-management:azure-api-management-rest-api
    name: Azure API Management REST API
    description: The Azure API Management REST API provides programmatic access to manage API Management service instances and their entities, including APIs, products, subscriptions, users, groups, policies, gateways, backends, certificates, and workspaces. It uses Azure Resource Manager conventions and supports API versions up to 2024-05-01 with over 100 operation groups covering the full management plane.
    humanURL: https://learn.microsoft.com/en-us/rest/api/apimanagement/
    baseURL: https://management.azure.com/
    tags:
      - Azure Resource Manager
      - Configuration
      - Management Plane
      - REST
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/apimanagement/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/apimanagement/operation-groups
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/api-management/authentication-authorization-overview
      - type: SDK
        url: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/apimanagement
      - type: SDK
        url: https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/apimanagement
      - type: SDK
        url: https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/apimanagement
      - type: SDK
        url: https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/apimanagement
      - type: SDK
        url: https://github.com/Azure/azure-sdk-for-go/tree/main/sdk/resourcemanager/apimanagement
      - type: OpenAPI
        url: openapi/microsoft-azure-api-management-rest-api-openapi.yaml
      - type: NaftikoCapability
        url: capabilities/shared/rest-api.yaml
  - aid: microsoft-azure-api-management:azure-api-management-gateway
    name: Azure API Management Gateway
    description: The Azure API Management gateway (data plane) acts as a facade to backend services, routing API requests, enforcing policies, verifying credentials, applying rate limits and quotas, caching responses, and emitting telemetry. It supports managed cloud-hosted and self-hosted containerized deployments for hybrid and multicloud environments.
    humanURL: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts
    baseURL: https://azure-api.net
    tags:
      - API Gateway
      - Policies
      - Proxy
      - Traffic Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts
      - type: APIReference
        url: https://learn.microsoft.com/en-us/azure/api-management/api-management-policies
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/api-management/authentication-authorization-overview
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/azure/api-management/import-and-publish
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/azure/api-management/transform-api
      - type: PolicySnippets
        url: https://github.com/Azure/api-management-policy-snippets
      - type: Tools
        url: https://github.com/Azure/azure-api-management-policy-toolkit
      - type: OpenAPI
        url: openapi/microsoft-azure-api-management-gateway-openapi.yaml
      - type: NaftikoCapability
        url: capabilities/shared/gateway.yaml
  - aid: microsoft-azure-api-management:azure-api-management-self-hosted-gateway
    name: Azure API Management Self-Hosted Gateway
    description: The Azure API Management self-hosted gateway is a containerized, Linux-based Docker image that can be deployed to Kubernetes, Docker, or any container orchestration platform in on-premises or other cloud environments. It federates with a cloud-based API Management instance for centralized configuration and management while routing API traffic locally to reduce latency and address compliance requirements.
    humanURL: https://learn.microsoft.com/en-us/azure/api-management/self-hosted-gateway-overview
    baseURL: https://mcr.microsoft.com/product/azure-api-management/gateway
    tags:
      - Hybrid
      - Kubernetes
      - On-Premises
      - Self-Hosted
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/api-management/self-hosted-gateway-overview
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/azure/api-management/how-to-deploy-self-hosted-gateway-azure-kubernetes-service
      - type: GitHubRepository
        url: https://github.com/Azure/api-management-self-hosted-gateway
      - type: HelmChart
        url: https://github.com/Azure/api-management-self-hosted-gateway/tree/main/helm-charts/azure-api-management-gateway
      - type: CodeExamples
        url: https://github.com/Azure/api-management-self-hosted-gateway-ingress
      - type: OpenAPI
        url: openapi/microsoft-azure-api-management-self-hosted-gateway-openapi.yaml
      - type: NaftikoCapability
        url: capabilities/shared/self-hosted-gateway.yaml
  - aid: microsoft-azure-api-management:azure-api-management-ai-gateway
    name: Azure API Management AI Gateway
    description: The Azure API Management AI gateway is a set of capabilities for managing, securing, scaling, and observing AI backends including Microsoft Foundry and Azure OpenAI deployments, OpenAI-compatible LLM endpoints, MCP servers, and A2A agent APIs. It provides token rate limiting and quotas, semantic caching, load balancing across AI backends, content safety enforcement, and token usage observability through Application Insights.
    humanURL: https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities
    baseURL: https://management.azure.com/
    tags:
      - AI Gateway
      - Azure OpenAI
      - LLM
      - MCP
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/azure/api-management/azure-openai-api-from-specification
      - type: Quickstart
        url: https://learn.microsoft.com/en-us/azure/api-management/azure-ai-foundry-api
      - type: OpenAPI
        url: openapi/microsoft-azure-api-management-ai-gateway-openapi.yaml
      - type: JSONSchema
        url: json-schema/ai-gateway-chat-completion-request-schema.json
      - type: JSONSchema
        url: json-schema/ai-gateway-chat-completion-response-schema.json
      - type: JSONSchema
        url: json-schema/ai-gateway-completion-request-schema.json
      - type: JSONSchema
        url: json-schema/ai-gateway-completion-response-schema.json
      - type: JSONSchema
        url: json-schema/ai-gateway-embedding-request-schema.json
      - type: JSONSchema
        url: json-schema/ai-gateway-embedding-response-schema.json
      - type: JSONSchema
        url: json-schema/ai-gateway-mcp-request-schema.json
      - type: JSONSchema
        url: json-schema/ai-gateway-mcp-response-schema.json
      - type: JSONStructure
        url: json-structure/ai-gateway-chat-completion-request-structure.json
      - type: JSONStructure
        url: json-structure/ai-gateway-chat-completion-response-structure.json
      - type: JSONStructure
        url: json-structure/ai-gateway-completion-request-structure.json
      - type: JSONStructure
        url: json-structure/ai-gateway-completion-response-structure.json
      - type: JSONStructure
        url: json-structure/ai-gateway-embedding-request-structure.json
      - type: JSONStructure
        url: json-structure/ai-gateway-embedding-response-structure.json
      - type: JSONStructure
        url: json-structure/ai-gateway-mcp-request-structure.json
      - type: JSONStructure
        url: json-structure/ai-gateway-mcp-response-structure.json
      - type: JSONLD
        url: json-ld/microsoft-azure-api-management-ai-gateway-context.jsonld
      - type: Example
        url: examples/ai-gateway-chat-completion-request-example.json
      - type: Example
        url: examples/ai-gateway-chat-completion-response-example.json
      - type: Example
        url: examples/ai-gateway-completion-request-example.json
      - type: Example
        url: examples/ai-gateway-completion-response-example.json
      - type: Example
        url: examples/ai-gateway-embedding-request-example.json
      - type: Example
        url: examples/ai-gateway-embedding-response-example.json
      - type: Example
        url: examples/ai-gateway-mcp-request-example.json
      - type: Example
        url: examples/ai-gateway-mcp-response-example.json
      - type: NaftikoCapability
        url: capabilities/shared/ai-gateway.yaml
  - aid: microsoft-azure-api-management:azure-api-management-developer-portal
    name: Azure API Management Developer Portal
    description: The Azure API Management developer portal is an automatically generated, fully customizable website that allows API consumers to discover APIs, read documentation, test APIs through an interactive console, create accounts, subscribe to API products, and manage API keys. It can be self-hosted and extended with custom content and branding.
    humanURL: https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-developer-portal-customize
    baseURL: https://developer.azure-api.net
    tags:
      - API Discovery
      - Developer Portal
      - Documentation
      - Self-Service
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-developer-portal-customize
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-developer-portal-customize
      - type: GitHubRepository
        url: https://github.com/Azure/api-management-developer-portal
      - type: OpenAPI
        url: openapi/microsoft-azure-api-management-developer-portal-openapi.yaml
      - type: NaftikoCapability
        url: capabilities/shared/developer-portal.yaml
common:
  - type: Website
    url: https://azure.microsoft.com/products/api-management/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/api-management/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/azure/api-management/get-started-create-service-instance
  - type: Quickstart
    url: https://learn.microsoft.com/en-us/azure/api-management/get-started-create-service-instance-cli
  - type: APIReference
    url: https://learn.microsoft.com/en-us/rest/api/apimanagement/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/api-management/authentication-authorization-overview
  - type: Pricing
    url: https://azure.microsoft.com/pricing/details/api-management/
  - type: Tiers
    url: https://learn.microsoft.com/en-us/azure/api-management/api-management-features
  - type: ChangeLog
    url: https://learn.microsoft.com/en-us/azure/api-management/breaking-changes/overview
  - type: Support
    url: https://learn.microsoft.com/answers/tags/29/azure-api-management/
  - type: Console
    url: https://portal.azure.com/
  - type: CLI
    url: https://learn.microsoft.com/en-us/cli/azure/apim
  - type: SDK
    url: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/apimanagement
  - type: Tutorials
    url: https://learn.microsoft.com/en-us/azure/api-management/import-and-publish
  - type: Training
    url: https://learn.microsoft.com/en-us/training/modules/explore-api-management/
  - type: Security
    url: https://learn.microsoft.com/en-us/azure/api-management/authentication-authorization-overview
  - type: BestPractices
    url: https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-policies
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/azure/ct-p/Azure
  - type: GitHubRepository
    url: https://github.com/Azure/api-management-samples
  - type: GitHubOrganization
    url: https://github.com/Azure
  - type: TermsOfService
    url: https://azure.microsoft.com/support/legal/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/privacystatement
  - type: Regions
    url: https://azure.microsoft.com/explore/global-infrastructure/products-by-region/
  - type: Compliance
    url: https://learn.microsoft.com/en-us/azure/compliance/
  - type: TrustCenter
    url: https://www.microsoft.com/trust-center
  - type: SignUp
    url: https://azure.microsoft.com/free/
  - type: StatusPage
    url: https://status.azure.com/
  - type: DeveloperPortal
    url: https://learn.microsoft.com/en-us/azure/api-management/developer-portal-overview
  - type: SDK
    url: https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/apimanagement
  - type: SDK
    url: https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/apimanagement
  - type: SDK
    url: https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/apimanagement
  - type: SDK
    url: https://github.com/Azure/azure-sdk-for-go/tree/main/sdk/resourcemanager/apimanagement
  - type: CodeExamples
    url: https://github.com/Azure/api-management-samples
  - type: PolicySnippets
    url: https://github.com/Azure/api-management-policy-snippets
  - type: Tools
    url: https://github.com/Azure/azure-api-management-policy-toolkit
  - type: ChangeLog
    url: https://github.com/Azure/API-Management/blob/master/changelogs/api-management-service.md
  - type: SpectralRules
    url: rules/microsoft-azure-api-management-rules.yaml
  - type: Vocabulary
    url: vocabulary/microsoft-azure-api-management-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/ai-gateway-management.yaml
  - type: NaftikoCapability
    url: capabilities/api-lifecycle-management.yaml
  - type: NaftikoCapability
    url: capabilities/developer-onboarding.yaml
  - type: NaftikoCapability
    url: capabilities/gateway-operations.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
