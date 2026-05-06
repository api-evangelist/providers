---
aid: axway
name: Axway
description: Axway provides API management, integration, and security solutions enabling organizations to connect, secure, and manage APIs across hybrid IT environments. Axway offers the Amplify platform for API management and a range of integration and security products for enterprises.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Management
  - Enterprise
  - Integration
  - Security
url: https://raw.githubusercontent.com/api-evangelist/axway/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-21'
specificationVersion: '0.19'
apis:
  - aid: axway:axway-amplify-api
    name: Axway Amplify Platform API
    description: The Axway Amplify Platform provides APIs for managing API products, environments, and consumer subscriptions across the enterprise API management platform.
    humanURL: https://platform.axway.com/api-docs.html
    baseURL: https://platform.axway.com/api/v1
    tags:
      - Amplify
      - API Management
      - Enterprise
    properties:
      - type: Documentation
        url: https://platform.axway.com/api-docs.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/axway/refs/heads/main/openapi/axway-amplify-platform-openapi-original.json
      - type: SDK
        url: https://github.com/Axway/agent-sdk
        title: Go Agent SDK
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/axway/refs/heads/main/json-ld/axway-amplify-platform-context.jsonld
  - aid: axway:axway-amplify-central-api
    name: Axway Amplify Central API
    description: Axway Amplify Central is the unified API management hub that enables discovery, consumption, and governance of APIs across the enterprise. It provides a central catalog for registering APIs from any gateway and managing the full API lifecycle including publishing, subscriptions, and access control.
    humanURL: https://docs.axway.com/bundle/amplify-central/
    baseURL: https://apicentral.axway.com
    tags:
      - Amplify
      - API Catalog
      - API Management
      - Governance
    properties:
      - type: Documentation
        url: https://docs.axway.com/bundle/amplify-central/
      - type: GettingStarted
        url: https://docs.axway.com/bundle/amplify-central/page/docs/getting_started_with_amplify_central/index.html
      - type: APIReference
        url: https://docs.axway.com/bundle/amplify-central/page/docs/integrate_with_central/index.html
      - type: Authentication
        url: https://docs.axway.com/bundle/amplify-central/page/docs/integrate_with_central/cli_central/cli_install/index.html
  - aid: axway:axway-api-gateway
    name: Axway API Gateway
    description: Axway API Gateway is an enterprise-grade API gateway providing security, mediation, and traffic management for APIs deployed on-premises or in hybrid environments. It supports policy-based security with over 200 prebuilt security policies, OAuth, and integration with backend services for high-performance API delivery.
    humanURL: https://docs.axway.com/bundle/axway-open-docs/
    baseURL: https://docs.axway.com
    tags:
      - API Gateway
      - Enterprise
      - On-Premises
      - Security
    properties:
      - type: Documentation
        url: https://docs.axway.com/bundle/axway-open-docs/
      - type: GettingStarted
        url: https://docs.axway.com/bundle/axway-open-docs/page/docs/apigw_getstarted/index.html
      - type: ChangeLog
        url: https://docs.axway.com/bundle/axway-open-docs/page/docs/apigw_releasenotes/index.html
  - aid: axway:axway-api-manager
    name: Axway API Manager
    description: Axway API Manager is a web-based management interface layered on top of API Gateway that enables organizations to register, virtualize, secure, and publish APIs to internal and external consumers. It provides lifecycle management, consumer self-service, and usage analytics for the full API catalog.
    humanURL: https://docs.axway.com/bundle/axway-open-docs/page/docs/apim_administration/apimgr_admin/index.html
    baseURL: https://docs.axway.com
    tags:
      - Administration
      - API Lifecycle
      - API Management
      - Enterprise
    properties:
      - type: Documentation
        url: https://docs.axway.com/bundle/axway-open-docs/page/docs/apim_administration/apimgr_admin/index.html
      - type: APIReference
        url: https://docs.axway.com/bundle/axway-open-docs/page/docs/apim_reference/index.html
  - aid: axway:axway-api-builder
    name: Axway API Builder
    description: Axway API Builder is a low-code tool for building and deploying microservices and APIs from data sources and business logic. It provides a visual flow editor to compose API endpoints, connect to databases, and integrate with third-party services as containerized Node.js microservices.
    humanURL: https://docs.axway.com/bundle/api-builder/
    baseURL: https://docs.axway.com
    tags:
      - API Builder
      - Low-Code
      - Microservices
      - Node.js
    properties:
      - type: Documentation
        url: https://docs.axway.com/bundle/api-builder/
      - type: GettingStarted
        url: https://docs.axway.com/bundle/api-builder/page/docs/getting_started/index.html
      - type: ChangeLog
        url: https://docs.axway.com/bundle/api-builder/page/docs/release_notes/index.html
      - type: GitHubRepository
        url: https://github.com/Axway/api-builder-standalone-tech-enablement
  - aid: axway:axway-amplify-streams
    name: Axway Amplify Streams
    description: Axway Amplify Streams provides a real-time event streaming API platform enabling publishers to push data updates to subscribers over Server-Sent Events (SSE) or WebSocket connections. It decouples producers from consumers for low-latency, event-driven API patterns across enterprise applications.
    humanURL: https://docs.axway.com/bundle/amplify-streams/
    baseURL: https://streams-open-docs.netlify.app
    tags:
      - Event-Driven
      - Real-Time
      - Streaming
      - WebSocket
    properties:
      - type: Documentation
        url: https://docs.axway.com/bundle/amplify-streams/
      - type: GettingStarted
        url: https://docs.axway.com/bundle/amplify-streams/page/docs/getting-started/index.html
  - aid: axway:axway-amplify-engage
    name: Axway Amplify Engage
    description: Axway Amplify Engage is a centralized API marketplace solution that curates, packages, and monetizes APIs. It provides automated API discovery and threat detection, multi-gateway support via agent-based integration, API curation with categorization and versioning, and comprehensive observability dashboards tracking API adoption and usage.
    humanURL: https://www.axway.com/en/products/amplify-engage
    tags:
      - API Marketplace
      - API Monetization
      - Governance
      - Observability
    properties:
      - type: Documentation
        url: https://docs.axway.com/
  - aid: axway:axway-amplify-ai-gateway
    name: Axway Amplify AI Gateway
    description: Axway Amplify AI Gateway is a secure, enterprise-grade AI gateway that governs AI integration, orchestrates intelligence, and accelerates innovation by integrating LLMs, vector databases, and chatbots into compliant workflows. It provides policy enforcement, role-based access control, token usage monitoring, prompt management, and MCP server support.
    humanURL: https://www.axway.com/en/products/amplify-ai-gateway
    tags:
      - AI
      - AI Gateway
      - Governance
      - LLM
      - MCP
    properties:
      - type: Documentation
        url: https://docs.axway.com/
  - aid: axway:axway-amplify-fusion
    name: Axway Amplify Fusion
    description: Axway Amplify Fusion integrates applications, data, APIs, and AI systems into unified workflows across hybrid environments. It unifies APIs, file transfers, and B2B integrations with no-code and low-code interfaces, event-driven automation, and visual orchestration with out-of-the-box connectors and templates.
    humanURL: https://www.axway.com/en/products/amplify-fusion
    tags:
      - Automation
      - Integration
      - Low-Code
      - Workflow
    properties:
      - type: Documentation
        url: https://docs.axway.com/
  - aid: axway:axway-flow-manager
    name: Axway Flow Manager
    description: Axway Flow Manager is a managed file transfer and B2B integration orchestration solution that automates business flows involving file exchange with trading partners. It provides visibility, governance, and SLA management for cross-enterprise data flows in industries such as retail, finance, and logistics.
    humanURL: https://docs.axway.com/bundle/FlowManager_20_allOS_en_HTML5/
    baseURL: https://docs.axway.com
    tags:
      - B2B Integration
      - Enterprise
      - File Transfer
      - MFT
    properties:
      - type: Documentation
        url: https://docs.axway.com/bundle/FlowManager_20_allOS_en_HTML5/
  - aid: axway:axway-securetransport
    name: Axway SecureTransport
    description: Axway SecureTransport is a managed file transfer gateway for receiving and exchanging business data securely. It supports high-volume, mission-critical file transfers across cloud, on-premises, and hybrid environments with compliance and audit capabilities.
    humanURL: https://www.axway.com/en/products/managed-file-transfer
    tags:
      - Compliance
      - Enterprise
      - File Transfer
      - MFT
    properties:
      - type: Documentation
        url: https://docs.axway.com/
      - type: CodeExamples
        url: https://github.com/Axway/ST_API_Examples
        title: SecureTransport REST API Examples
  - aid: axway:axway-transfer-cft
    name: Axway Transfer CFT
    description: Axway Transfer CFT enables decentralized file transfers across cloud, on-premises, and data pipelines. It provides reliable, automated file exchange for enterprise integration scenarios requiring distributed transfer agents.
    humanURL: https://www.axway.com/en/products/managed-file-transfer
    tags:
      - Decentralized
      - Enterprise
      - File Transfer
      - MFT
    properties:
      - type: Documentation
        url: https://docs.axway.com/
  - aid: axway:axway-b2bi
    name: Axway B2Bi
    description: Axway B2Bi is a B2B and EDI integration solution for automating partner data exchange. It supports EDI, AS2, and other B2B protocols for trading partner onboarding, document transformation, and compliance with industry standards.
    humanURL: https://www.axway.com/en/products/b2b-integration
    tags:
      - B2B
      - EDI
      - Integration
      - Trading Partners
    properties:
      - type: Documentation
        url: https://docs.axway.com/
  - aid: axway:axway-open-banking
    name: Axway Open Banking
    description: Axway Open Banking provides prebuilt APIs for regulatory compliance and ecosystem engagement, supporting PSD2 and open banking standards. It enables financial institutions to expose and manage banking APIs securely.
    humanURL: https://www.axway.com/en/products/amplify-open-banking
    tags:
      - Banking
      - Compliance
      - Finance
      - Open Banking
      - PSD2
    properties:
      - type: Documentation
        url: https://docs.axway.com/
common:
  - type: Portal
    url: https://developer.axway.com/
  - type: Website
    url: https://www.axway.com/
  - type: Documentation
    url: https://docs.axway.com/
  - type: GettingStarted
    url: https://developer.axway.com/
  - type: Console
    url: https://platform.axway.com/
  - type: Support
    url: https://support.axway.com/
  - type: Blog
    url: https://blog.axway.com/
  - type: Community
    url: https://community.axway.com/
  - type: GitHubOrganization
    url: https://github.com/Axway
  - type: YouTube
    url: https://www.youtube.com/user/AxwaySoftware
  - type: X
    url: https://x.com/Axway
  - type: LinkedIn
    url: https://www.linkedin.com/company/axway
  - type: ChangeLog
    url: https://docs.axway.com/bundle/axway-open-docs/page/docs/apigw_releasenotes/index.html
  - type: StatusPage
    url: https://status.axway.com/
  - type: TrustCenter
    url: https://trust.axway.com/
  - type: Resources
    url: https://resources.axway.com/
  - type: SDK
    url: https://www.npmjs.com/package/@axway/swagger-tools
    title: Swagger Tools (Node.js)
  - type: CodeExamples
    url: https://github.com/Axway/api-builder-examples
    title: API Builder Examples
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/axway/refs/heads/main/rules/axway-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/axway/refs/heads/main/vocabulary/axway-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/axway/refs/heads/main/capabilities/identity-and-access.yaml
    title: Identity And Access
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/axway/refs/heads/main/capabilities/organization-management.yaml
    title: Organization Management
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/axway/refs/heads/main/capabilities/application-and-analytics.yaml
    title: Application And Analytics
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/axway/refs/heads/main/capabilities/identity-provider-management.yaml
    title: Identity Provider Management
  - type: TermsOfService
    url: https://www.axway.com/en/legal/terms
  - type: PrivacyPolicy
    url: https://www.axway.com/en/legal/privacy-statement
  - type: Features
    data:
      - name: API Lifecycle Management
        description: Manage the full API lifecycle from design, development, publishing to retirement.
      - name: API Gateway
        description: Enterprise-grade API gateway with over 200 prebuilt security policies, OAuth, and traffic management.
      - name: Unified API Catalog
        description: Centralized catalog for discovering and consuming APIs from any gateway.
      - name: Event Streaming
        description: Real-time event streaming with SSE and WebSocket for event-driven API patterns.
      - name: Managed File Transfer
        description: Automate B2B file exchange with trading partners with SLA governance.
      - name: Low-Code API Building
        description: Build and deploy microservices visually with Axway API Builder flow editor.
      - name: Consumer Self-Service
        description: Enable API consumers to discover, subscribe, and manage API access independently.
      - name: Hybrid Deployment
        description: Deploy across on-premises, cloud, and hybrid environments with a unified control plane.
      - name: AI Gateway
        description: Secure and govern AI integration with LLM orchestration, prompt management, and MCP server support.
      - name: API Marketplace
        description: Curate, package, and monetize APIs with automated discovery and multi-gateway support.
      - name: Federated Governance
        description: Enforce standardization and compliance across distributed API gateways and environments.
      - name: No-Code Integration
        description: Visual orchestration with out-of-the-box connectors and templates for business users.
  - type: UseCases
    data:
      - name: Enterprise API Management
        description: Govern and manage APIs across distributed enterprise teams and environments.
      - name: B2B Integration
        description: Automate partner data exchange with secure MFT and EDI workflows.
      - name: API Monetization
        description: Publish APIs to a marketplace with tiered subscription plans and usage billing.
      - name: Real-Time Data Streaming
        description: Deliver live data updates to clients using event streaming APIs.
      - name: Open Banking
        description: Implement open banking APIs compliant with PSD2 and regulatory requirements.
      - name: AI Integration
        description: Securely integrate LLMs and AI models into enterprise workflows with policy-based governance.
      - name: Managed File Transfer
        description: Exchange mission-critical files across cloud and on-premises environments with compliance and audit trails.
      - name: Supply Chain Integration
        description: Connect trading partners with EDI, eInvoicing, and track-and-trace capabilities.
  - type: Integrations
    data:
      - name: AWS
        description: Deploy Amplify Central and API Gateway on AWS infrastructure.
      - name: Azure
        description: Connect and manage Azure API Management services via Amplify Central.
      - name: MuleSoft Anypoint
        description: Discover and govern MuleSoft APIs from Amplify Central.
      - name: ServiceNow
        description: Integrate API incidents and change management with ServiceNow workflows.
      - name: Splunk
        description: Stream API analytics and security events to Splunk for SIEM analysis.
      - name: OpenAI
        description: Route and govern OpenAI LLM traffic through the Amplify AI Gateway.
      - name: SAP
        description: Integrate SAP systems and data via Amplify Fusion connectors.
  - type: Solutions
    data:
      - name: Financial Services
        description: Open banking, PSD2 compliance, and secure API-driven banking ecosystems.
      - name: Healthcare
        description: Secure data exchange and API governance for healthcare providers and payers.
      - name: Retail And Supply Chain
        description: B2B integration, EDI, and trading partner automation for retail and logistics.
      - name: Government
        description: Secure file transfer and API management for government agencies and compliance.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
