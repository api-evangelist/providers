---
aid: wso2
name: WSO2
segments:
  - Gateways
description: WSO2 API Manager is an open-source API management platform supporting REST, SOAP, and GraphQL with flexible hybrid deployment. It provides a unified control plane for managing APIs, AI models, and agents across on-premises, hybrid, and cloud environments. WSO2 is recognized as a Leader in the Forrester Wave API Management Q3 2024 report.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Management
  - Gateways
  - Open Source
  - API Lifecycle
  - GraphQL
  - SOAP
  - REST
created: '2026-03-03'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/wso2/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: wso2:publisher-api
    name: WSO2 Publisher API
    description: The WSO2 API Manager Publisher API enables programmatic management of APIs within the WSO2 API Manager Publisher portal. It provides RESTful endpoints for creating, designing, implementing, versioning, and managing APIs through the full API lifecycle including design, publish, and deprecate.
    humanURL: https://apim.docs.wso2.com/en/latest/reference/product-apis/publisher-apis/publisher-v4/publisher-v4/
    tags:
      - API Management
      - Lifecycle
      - Publisher
    properties:
      - type: Documentation
        url: https://apim.docs.wso2.com/en/latest/reference/product-apis/publisher-apis/publisher-v4/publisher-v4/
      - type: OpenAPI
        url: openapi/wso2-publisher-api.yaml
  - aid: wso2:devportal-api
    name: WSO2 Developer Portal API
    description: The WSO2 API Manager Developer Portal API handles API discovery, application management, subscriptions, and access token generation. It enables consumption workflows for developers to discover, explore, subscribe to, and consume APIs.
    humanURL: https://apim.docs.wso2.com/en/latest/reference/product-apis/devportal-apis/devportal-v3/devportal-v3/
    tags:
      - Developer Portal
      - Discovery
      - Subscriptions
    properties:
      - type: Documentation
        url: https://apim.docs.wso2.com/en/latest/reference/product-apis/devportal-apis/devportal-v3/devportal-v3/
      - type: OpenAPI
        url: openapi/wso2-devportal-api.yaml
  - aid: wso2:admin-api
    name: WSO2 Admin Portal API
    description: The WSO2 API Manager Admin Portal API manages users, roles, policies, and system configurations. It provides administrative control over subscription tiers, application policies, advanced throttling policies, and system-wide settings.
    humanURL: https://apim.docs.wso2.com/en/latest/reference/product-apis/admin-apis/admin-v4/admin-v4/
    tags:
      - Administration
      - Configuration
      - Policies
    properties:
      - type: Documentation
        url: https://apim.docs.wso2.com/en/latest/reference/product-apis/admin-apis/admin-v4/admin-v4/
      - type: OpenAPI
        url: openapi/wso2-admin-api.yaml
  - aid: wso2:gateway-api
    name: WSO2 Gateway API
    description: The WSO2 API Manager Gateway API provides gateway deployment and management capabilities. It handles API deployment across multiple gateway environments and provides endpoints for managing gateway-level operations.
    humanURL: https://apim.docs.wso2.com/en/latest/reference/product-apis/gateway-apis/gateway-v2/gateway-v2/
    tags:
      - Deployment
      - Gateway
      - Traffic Management
    properties:
      - type: Documentation
        url: https://apim.docs.wso2.com/en/latest/reference/product-apis/gateway-apis/gateway-v2/gateway-v2/
      - type: OpenAPI
        url: openapi/wso2-gateway-api.yaml
  - aid: wso2:service-catalog-api
    name: WSO2 Service Catalog API
    description: The WSO2 API Manager Service Catalog API manages service discovery and cataloging. It enables developers to register their backend services in a RESTful manner and supports the API-first integration approach in WSO2 API Manager.
    humanURL: https://apim.docs.wso2.com/en/latest/reference/product-apis/service-catalog-apis/service-catalog-v1/service-catalog-v1/
    tags:
      - Discovery
      - Integration
      - Service Catalog
    properties:
      - type: Documentation
        url: https://apim.docs.wso2.com/en/latest/reference/product-apis/service-catalog-apis/service-catalog-v1/service-catalog-v1/
      - type: OpenAPI
        url: openapi/wso2-service-catalog-api.yaml
  - aid: wso2:devops-api
    name: WSO2 DevOps API
    description: The WSO2 API Manager DevOps API supports continuous deployment and operations workflows. It provides endpoints for managing API deployments, logging, and operational tasks in DevOps pipelines.
    humanURL: https://apim.docs.wso2.com/en/latest/reference/product-apis/devops-apis/devops-v0/devops-v0/
    tags:
      - Deployment
      - DevOps
      - Operations
    properties:
      - type: Documentation
        url: https://apim.docs.wso2.com/en/latest/reference/product-apis/devops-apis/devops-v0/devops-v0/
      - type: OpenAPI
        url: openapi/wso2-devops-api.yaml
  - aid: wso2:dcr-api
    name: WSO2 DCR API
    description: The WSO2 API Manager Dynamic Client Registration (DCR) API enables OAuth2 client applications to register themselves programmatically with the WSO2 Identity Server key manager. It follows the OpenID Connect Dynamic Client Registration specification and is used to automate application onboarding for API access.
    humanURL: https://apim.docs.wso2.com/en/latest/reference/product-apis/
    baseURL: https://apis.wso2.com
    tags:
      - Client Registration
      - Identity
      - OAuth2
      - Security
    properties:
      - type: Documentation
        url: https://apim.docs.wso2.com/en/latest/reference/product-apis/
      - type: OpenAPI
        url: openapi/wso2-dcr-api.yaml
  - aid: wso2:governance-api
    name: WSO2 Governance API
    description: The WSO2 API Manager Governance API provides endpoints for managing governance policies, rulesets, and API compliance. It enables teams to define and enforce API design standards, assess policy adherence, and validate artifact compliance across the API lifecycle.
    humanURL: https://apim.docs.wso2.com/en/latest/reference/product-apis/governance-apis/governance-v1/governance-v1/
    baseURL: https://apis.wso2.com
    tags:
      - API Management
      - Compliance
      - Governance
      - Policies
    properties:
      - type: Documentation
        url: https://apim.docs.wso2.com/en/latest/reference/product-apis/governance-apis/governance-v1/governance-v1/
      - type: OpenAPI
        url: openapi/wso2-governance-api.yaml
common:
  - type: Website
    name: WSO2 API Manager
    url: https://wso2.com/api-manager/
  - type: Documentation
    name: Documentation
    url: https://apim.docs.wso2.com/en/latest/
  - type: GettingStarted
    name: Quick Start Guide
    url: https://apim.docs.wso2.com/en/latest/get-started/api-manager-quick-start-guide/
  - type: Blog
    name: Blog
    url: https://wso2.com/library/blogs/
  - type: Pricing
    name: Pricing
    url: https://wso2.com/api-platform/pricing/
  - type: About
    name: About WSO2
    url: https://wso2.com/about/
  - type: GitHubOrg
    name: GitHub
    url: https://github.com/wso2
  - type: TermsOfService
    name: Terms of Use
    url: https://wso2.com/terms-of-use/
  - type: PrivacyPolicy
    name: Privacy Policy
    url: https://wso2.com/privacy-policy/
  - type: Support
    name: FAQ
    url: https://apim.docs.wso2.com/en/latest/reference/faq/
  - type: Authentication
    name: Authentication Overview
    url: https://apim.docs.wso2.com/en/latest/api-security/
  - type: ChangeLog
    name: What's New
    url: https://apim.docs.wso2.com/en/latest/get-started/overview/whats-new/
  - type: StatusPage
    name: WSO2 Status Page
    url: https://status.wso2.com/
  - type: Community
    name: WSO2 Community Forum
    url: https://stackoverflow.com/questions/tagged/wso2
  - type: StackOverflow
    name: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/wso2
  - type: GitHubRepository
    name: WSO2 API Manager GitHub
    url: https://github.com/wso2/product-apim
  - type: SpectralRules
    name: WSO2 Spectral Rules
    url: rules/wso2-rules.yml
  - type: NaftikoCapability
    name: WSO2 API Lifecycle Management Capability
    url: capabilities/api-lifecycle-management.yaml
  - type: NaftikoCapability
    name: WSO2 API Governance Capability
    url: capabilities/api-governance.yaml
  - type: Vocabulary
    name: WSO2 Vocabulary
    url: vocabulary/wso2-vocabulary.yaml
  - type: Features
    data:
      - name: Full API Lifecycle Management
        description: Design, publish, deprecate, and retire APIs across the full lifecycle.
      - name: Multi-Protocol Support
        description: Manages REST, GraphQL, gRPC, WebSocket, and Webhook APIs.
      - name: AI Gateway
        description: Routes and manages LLM traffic with guardrails and PII masking.
      - name: MCP Gateway
        description: Converts REST APIs into Model Context Protocol tools for AI agents.
      - name: API Governance
        description: Policy enforcement and compliance checking across API designs.
      - name: Dynamic Client Registration
        description: Programmatic OAuth2 client registration following OpenID Connect DCR spec.
      - name: Advanced Throttling
        description: Subscription tiers, application policies, and advanced rate limiting.
      - name: Analytics
        description: Real-time traffic analytics and usage insights via Moesif integration.
      - name: SDK Generation
        description: Auto-generates client SDKs in multiple languages from API definitions.
      - name: Service Catalog
        description: Registers and discovers backend services for API-first integration.
      - name: DevOps Integration
        description: CI/CD pipeline integration for automated API deployment.
      - name: Multi-Gateway Support
        description: Manages APIs across WSO2, Kong, AWS, Azure, and Envoy gateways.
  - type: UseCases
    data:
      - name: API Program Management
        description: Centrally manage the full lifecycle of all enterprise APIs.
      - name: Developer Self-Service
        description: Developer portal for API discovery, subscription, and key management.
      - name: AI Agent Integration
        description: Expose REST APIs as MCP tools for AI and agent consumption.
      - name: LLM Traffic Management
        description: Route, monitor, and govern traffic to large language model APIs.
      - name: Compliance and Governance
        description: Enforce API design standards and validate compliance across teams.
      - name: B2B API Monetization
        description: Define subscription tiers and billing for API usage-based monetization.
  - type: Integrations
    data:
      - name: OpenAI
        description: AI Gateway supports routing to OpenAI models.
      - name: Anthropic
        description: AI Gateway supports routing to Anthropic Claude models.
      - name: Azure OpenAI
        description: AI Gateway integrates with Azure OpenAI deployment.
      - name: Kong Gateway
        description: Multi-gateway management includes Kong.
      - name: AWS API Gateway
        description: Multi-gateway management includes AWS API Gateway.
      - name: Moesif
        description: Analytics integration powered by Moesif.
      - name: Kubernetes
        description: Native Kubernetes deployment support.
      - name: Keycloak
        description: Identity provider integration for OAuth2 flows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
