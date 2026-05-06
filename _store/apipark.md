---
aid: apipark
name: APIPark
description: APIPark is an open-source, cloud-native AI gateway and API developer portal that helps developers and enterprises manage, integrate, and deploy AI and API services. It supports 100+ AI models from all major AI providers, provides API lifecycle management, authentication, rate limiting, and cluster deployment for large-scale traffic. Teams can combine AI models with custom prompts to create new AI-powered services such as sentiment analysis, translation, or data analysis.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Gateway
  - API Gateway
  - API Management
  - Developer Portal
  - LLM
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/apipark/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apipark:apipark-api
    name: APIPark API
    description: The APIPark API provides programmatic access to manage the APIPark AI gateway and developer portal, including AI model integration, service management, team administration, and API publishing workflows.
    humanURL: https://apipark.com/
    baseURL: https://api.apipark.com/v1
    tags:
      - AI Gateway
      - API Gateway
      - API Management
      - Developer Portal
      - LLM
    properties:
      - type: Documentation
        url: https://docs.apipark.com/docs/overview
      - type: GitHubRepository
        url: https://github.com/APIParkLab/APIPark
      - type: ChangeLog
        url: https://docs.apipark.com/docs/release
      - type: OpenAPI
        url: openapi/apipark-api.yaml
      - type: JSONSchema
        url: json-schema/apipark-service-schema.json
      - type: JSONSchema
        url: json-schema/apipark-ai-model-schema.json
      - type: JSON-LD
        url: json-ld/apipark-context.jsonld
common:
  - type: Website
    url: https://apipark.com/
  - type: Documentation
    url: https://docs.apipark.com/docs/overview
  - type: GitHubOrganization
    url: https://github.com/APIParkLab
  - type: Blog
    url: https://apipark.com/blog
  - type: ChangeLog
    url: https://docs.apipark.com/docs/release
  - type: Features
    data:
      - name: AI Gateway
        description: Unified AI gateway supporting 100+ AI models from OpenAI, Anthropic, Google, Meta, Mistral, and other major providers.
      - name: Prompt Engineering
        description: Combine AI models with custom system prompts to create new API services for specific use cases.
      - name: API Developer Portal
        description: Full-featured developer portal for publishing, discovering, and subscribing to API services.
      - name: Multi-Tenant Teams
        description: Team-based multi-tenancy for separating API services and subscriptions across organizational units.
      - name: API Lifecycle Management
        description: Complete API lifecycle from service creation through publication, subscription, and deprecation.
      - name: Rate Limiting and Authentication
        description: Built-in API key authentication, rate limiting, and traffic management for all published services.
      - name: Cluster Deployment
        description: Cloud-native cluster deployment supporting large-scale production traffic with high availability.
  - type: UseCases
    data:
      - name: AI API Standardization
        description: Standardize access to 100+ AI models through a unified API interface, enabling model switching without code changes.
      - name: AI Service Creation
        description: Combine AI models with custom prompts to create specialized AI-powered APIs for specific domains.
      - name: Enterprise AI Governance
        description: Govern AI model access, usage costs, and rate limits across multiple teams from a centralized portal.
      - name: Internal API Marketplace
        description: Build an internal API marketplace for teams to discover and subscribe to AI and traditional API services.
  - type: Solutions
    data:
      - name: Open Source
        description: Free, Apache 2.0 licensed self-hosted deployment for organizations with full control over infrastructure.
      - name: Cloud
        description: Managed cloud deployment for teams who prefer not to manage infrastructure.
      - name: Enterprise
        description: Enterprise support, SLA guarantees, and professional services for large-scale deployments.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
