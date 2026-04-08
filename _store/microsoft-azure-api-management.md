---
aid: microsoft-azure-api-management
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-api-management/refs/heads/main/apis.yml
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
  - type: Reference
    url: https://learn.microsoft.com/en-us/rest/api/apimanagement/operation-groups
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/api-management/authentication-authorization-overview
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
  - type: Reference
    url: https://learn.microsoft.com/en-us/azure/api-management/api-management-policies
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/api-management/authentication-authorization-overview
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/api-management/import-and-publish
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
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/api-management/azure-openai-api-from-specification
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
name: Microsoft Azure API Management
tags:
- AI Gateway
- API Gateway
- API Management
- Enterprise
- Microsoft Azure
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Azure API Management is a hybrid, multicloud management platform for APIs across all environments. It provides an API gateway, management plane, and developer portal supporting the complete API lifecycle including publishing, securing, monitoring, and transforming APIs for external, partner, and internal developers. It includes an AI gateway for governing LLM deployments, MCP servers, and agentic AI workloads.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

