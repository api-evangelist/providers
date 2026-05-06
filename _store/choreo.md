---
aid: choreo
name: Choreo
x-type: company
description: WSO2 Choreo is an enterprise-grade Internal Developer Platform (IDP) and application orchestration platform that helps organizations build, deploy, manage, and observe APIs, microservices, integrations, and AI applications across multi-cloud Kubernetes infrastructure (AWS, Azure, GCP, Vultr, or upstream Kubernetes). Choreo combines API management, CI/CD, GitOps, observability, FinOps, and platform engineering into a single AI-guided experience. Developers connect Git repos and deploy instantly, while platform teams use Choreo to enforce security, governance, and compliance with PCI DSS and SOC 2 Type 2 certifications. The platform orchestrates CNCF tools including Kubernetes, Argo CD, Cilium, Envoy, Helm, Prometheus, OpenSearch, Flux, and KEDA, and exposes APIs for API management, developer portal/marketplace consumption, and observability insights.
url: https://raw.githubusercontent.com/api-evangelist/choreo/refs/heads/main/apis.yml
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Apps
  - API Management
  - CI/CD
  - Cloud Native
  - DevOps
  - Developer Portal
  - FinOps
  - IDE
  - Internal Developer Platform
  - Kubernetes
  - Lifecycle
  - Observability
  - Orchestration
  - Platform Engineering
  - Pro-Code API Composition
  - Unified
  - WSO2
  - Workflows
created: '2025-06-05'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: choreo:api-management
    name: Choreo API Management API
    description: The Choreo API Management API provides programmatic access to manage the full lifecycle of APIs on the WSO2 Choreo platform. It allows API creators to create, publish, version, and manage APIs, manage organizations, projects, components, builds, and deployments.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://wso2.com/choreo/docs/
    tags:
      - API Management
      - Builds
      - Components
      - Deployments
      - Lifecycle
      - Organizations
      - Projects
    properties:
      - type: Documentation
        url: https://wso2.com/choreo/docs/
      - type: OpenAPI
        url: openapi/choreo-api-management-openapi.yml
      - type: JSONSchema
        url: json-schema/choreo-organization.json
      - type: JSONSchema
        url: json-schema/choreo-project.json
      - type: JSONSchema
        url: json-schema/choreo-component.json
      - type: JSONSchema
        url: json-schema/choreo-api.json
      - type: JSONSchema
        url: json-schema/choreo-build.json
      - type: JSONSchema
        url: json-schema/choreo-deployment.json
      - type: JSONSchema
        url: json-schema/choreo-environment.json
  - aid: choreo:developer-portal
    name: Choreo Developer Portal API
    description: The Choreo Developer Portal API enables API consumers to discover, evaluate, subscribe to, and consume APIs hosted on the Choreo platform. It provides access to the API marketplace, application management, subscription management, and credential generation for OAuth 2.0 and API key based authentication.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://devportal.choreo.dev/
    tags:
      - API Keys
      - API Marketplace
      - Applications
      - Developer Portal
      - OAuth
      - Subscriptions
    properties:
      - type: Documentation
        url: https://wso2.com/choreo/docs/consuming-services/manage-subscription/
      - type: OpenAPI
        url: openapi/choreo-developer-portal-openapi.yml
      - type: JSONSchema
        url: json-schema/choreo-application.json
      - type: JSONSchema
        url: json-schema/choreo-subscription.json
  - aid: choreo:insights
    name: Choreo Insights API
    description: The Choreo Insights API provides access to observability, monitoring, and analytics data for APIs and components deployed on the Choreo platform. It enables users to programmatically retrieve usage statistics, latency metrics, error analytics, and operational insights.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://wso2.com/choreo/docs/monitoring-and-insights/work-with-choreo-insights-api/access-the-choreo-insights-api/
    tags:
      - Alerts
      - Analytics
      - Logs
      - Metrics
      - Monitoring
      - Observability
    properties:
      - type: Documentation
        url: https://wso2.com/choreo/docs/monitoring-and-insights/work-with-choreo-insights-api/access-the-choreo-insights-api/
      - type: OpenAPI
        url: openapi/choreo-insights-openapi.yml
common:
  - type: Website
    url: https://wso2.com/choreo/
  - type: DeveloperPortal
    url: https://devportal.choreo.dev/
  - type: Console
    name: Choreo Console
    url: https://console.choreo.dev/
  - type: Documentation
    url: https://wso2.com/choreo/docs/
  - type: Login
    name: Choreo Console Login
    url: https://console.choreo.dev/login
  - type: SignUp
    name: Choreo Console Signup
    url: https://console.choreo.dev/signup
  - type: Pricing
    url: https://wso2.com/choreo/pricing/
  - type: Blog
    url: https://medium.com/choreo-tech-blog
  - type: Discord
    url: https://discord.com/invite/wso2
  - type: ParentCompany
    name: WSO2
    url: https://wso2.com
  - type: AWSMarketplace
    url: https://aws.amazon.com/marketplace/seller-profile?id=ec25fa2f-b833-43d8-9d4c-de13ade0eee7
  - type: AzureMarketplace
    url: https://azuremarketplace.microsoft.com/en-us/marketplace/apps/wso2.choreo
  - type: GCPMarketplace
    url: https://console.cloud.google.com/marketplace/product/wso2-public/choreo
  - type: TermsOfService
    url: https://wso2.com/terms-of-use/
  - type: PrivacyPolicy
    url: https://wso2.com/privacy-policy/
  - type: JSONLDContext
    url: json-ld/choreo-context.jsonld
  - type: Spectral
    url: spectral/choreo-spectral.yml
  - type: NaftikoCapabilities
    url: naftiko/choreo-capabilities.yml
  - name: Features
    type: Features
    data:
      - name: Multi-Cloud Kubernetes Deployment
      - name: Auto-scaling and Scale-to-Zero
      - name: AI-Powered FinOps Monitoring
      - name: AI Co-Pilot for Self-Service
      - name: GitOps and Commit-Based CI/CD
      - name: AI Agent and RAG Deployment
      - name: Managed Vector Databases
      - name: MCP Server Deployment
      - name: Centralized Logging and Metrics
      - name: Policy Enforcement (PCI DSS, SOC 2 Type 2)
      - name: Internal Developer Portal
      - name: Built-in API Marketplace
  - name: UseCases
    type: UseCases
    data:
      - name: ETL Automation
      - name: B2B EDI Integration
      - name: Microservices Architecture
      - name: Event-Driven GraphQL Backends
      - name: AI/RAG Application Deployment
      - name: Internal Developer Platform Provision
      - name: API Lifecycle Management
      - name: Developer Self-Service Enablement
      - name: DevSecOps and Platform Engineering
  - name: Standards
    type: Standards
    data:
      - name: OpenAPI Specification
      - name: OAuth 2.0
      - name: PCI DSS
      - name: SOC 2 Type 2
      - name: Kubernetes
      - name: GraphQL
      - name: WebSocket
      - name: gRPC
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
