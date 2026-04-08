---
aid: boomi
url: https://raw.githubusercontent.com/api-evangelist/boomi/refs/heads/main/apis.yml
apis:
- aid: boomi:boomi
  name: Boomi
  tags: []
  humanURL: https://boomi.com/platform/api-management/
  properties:
  - url: https://boomi.com/platform/api-management/
    type: Documentation
  description: Boomi API Management supports the full lifecycle of APIs in any environment. Configure APIs and expose real-time integrations effortlessly.
- aid: boomi:platform-rest-api
  name: Boomi Platform REST API
  tags:
  - Integration
  - Platform
  - REST
  humanURL: https://developer.boomi.com/docs/APIs/PlatformAPI/Introduction/Platform_API
  properties:
  - url: https://developer.boomi.com/docs/APIs/PlatformAPI/Introduction/Platform_API
    type: Documentation
  - url: https://developer.boomi.com/docs/APIs/PlatformAPI/APIReference/Platform_APIs_Overview
    type: APIReference
  - url: https://developer.boomi.com/docs/category/platform-rest-api-reference
    type: APIReference
  - url: https://developer.boomi.com/docs/APIs/PlatformAPI/Introduction/OpenAPI_3_0
    type: OpenAPI
  - url: https://developer.boomi.com/docs/category/introduction-to-boomi-platform-apis
    type: GettingStarted
  - url: openapi/boomi-platform-rest-api-openapi.yml
    type: OpenAPI
  - url: json-schema/boomi-process-schema.json
    type: JSONSchema
  description: The Boomi Platform REST API provides programmatic access to the Boomi Enterprise Platform functionality. It allows for control of many objects associated with your account including account administration, cloud management, component management, deployment, environment management, execution statistics, integration packs, process execution, and runtime management.
- aid: boomi:platform-partner-api
  name: Boomi Platform Partner API
  tags:
  - Partners
  - Platform
  - REST
  humanURL: https://developer.boomi.com/api/platformpartnerapi
  properties:
  - url: https://developer.boomi.com/api/platformpartnerapi
    type: Documentation
  - url: https://developer.boomi.com/docs/APIs/PlatformPartnerAPI/APIReference/Platform_Partner_APIs_Overview
    type: APIReference
  - url: https://developer.boomi.com/docs/APIs/PlatformAPI/Introduction/OpenAPI_3_0
    type: OpenAPI
  description: The Boomi Platform Partner API provides partners with programmatic access to the secondary accounts that they manage. It builds upon the standard Boomi Enterprise Platform API with additional capabilities including account CREATE and DELETE operations and account provisioning.
- aid: boomi:api-management-api
  name: Boomi API Management API
  tags:
  - API Management
  - GraphQL
  - REST
  - SOAP
  humanURL: https://help.boomi.com/docs/Atomsphere/API%20Management/Topics/r-api-API_Management_APIs_4307dcc3-1662-4e2a-9a82-d03ca043f340
  properties:
  - url: https://help.boomi.com/docs/Atomsphere/API%20Management/Topics/r-api-API_Management_APIs_4307dcc3-1662-4e2a-9a82-d03ca043f340
    type: Documentation
  - url: https://help.boomi.com/docs/Atomsphere/API%20Management/Topics/c-api-Getting_Started_f06ad982-c0d9-4c67-ab0f-7a19db534868
    type: GettingStarted
  - url: https://help.boomi.com/docs/Atomsphere/API%20Management/Topics/c-api-Authentication_3baf0ddd-3532-403f-b66b-4800c1e19098
    type: Authentication
  description: The Boomi API Management API provides programmatic access to API Management service functionality through REST, SOAP, and GraphQL implementations. It supports API objects and object-based operations, API actions, and audit log query types. The API enforces a rate limit of 10 requests per second.
- aid: boomi:datahub-api
  name: Boomi DataHub API
  tags:
  - Data Hub
  - Master Data
  - REST
  humanURL: https://help.boomi.com/docs/Atomsphere/Master%20Data%20Hub/REST%20APIs/r-mdm-REST_APIs_f43499a6-3d1c-4102-bf13-94b02659dd9f
  properties:
  - url: https://help.boomi.com/docs/Atomsphere/Master%20Data%20Hub/REST%20APIs/r-mdm-REST_APIs_f43499a6-3d1c-4102-bf13-94b02659dd9f
    type: Documentation
  - url: https://help.boomi.com/docs/Atomsphere/Master%20Data%20Hub/REST%20APIs/r-mdm-Platform_API_368dc28d-455d-4aa2-970e-d2332c7ada83
    type: APIReference
  - url: https://help.boomi.com/docs/Atomsphere/Master%20Data%20Hub/REST%20APIs/r-mdm-Repository_API_659e32f2-99ce-444e-8201-8a9ae1d92c9b
    type: APIReference
  - url: openapi/boomi-datahub-api-openapi.yml
    type: OpenAPI
  description: The Boomi DataHub REST APIs enable programmatic access to the master data management system through the DataHub Platform API and Repository API. The Platform API enables platform-level operations on master data domains, while the Repository API supports data repository operations with JWT authentication.
- aid: boomi:event-streams-api
  name: Boomi Event Streams REST API
  tags:
  - Events
  - Messaging
  - REST
  - Streaming
  humanURL: https://help.boomi.com/docs/Atomsphere/Event%20Streams/es-REST_API
  properties:
  - url: https://help.boomi.com/docs/Atomsphere/Event%20Streams/es-REST_API
    type: Documentation
  - url: openapi/boomi-event-streams-openapi.yml
    type: OpenAPI
  - url: asyncapi/boomi-event-streams-asyncapi.yml
    type: AsyncAPI
  description: The Boomi Event Streams REST API enables HTTP-based applications to produce messages to topics. It supports multiple message modes including multiple messages in predefined JSON format and single messages in their original format without transformation. The API accommodates messages up to 5MB and uses Bearer token authentication.
- aid: boomi:flow-api
  name: Boomi Flow API
  tags:
  - Automation
  - Low-Code
  - REST
  - Workflows
  humanURL: https://manywho.github.io/docs-api/
  properties:
  - url: https://manywho.github.io/docs-api/
    type: Documentation
  - url: https://github.com/manywho/docs-api
    type: GitHubRepository
  description: The Boomi Flow API provides REST endpoints for programmatic access to Boomi Flow functionality. Built on an API-first architecture, many operations performed within Boomi Flow can be accessed through this API. The API supports authorization using tenant-specific API keys.
- aid: boomi:connector-deployment-api
  name: Boomi Connector Deployment API
  tags:
  - Connectors
  - Deployment
  - REST
  - SDK
  humanURL: https://developer.boomi.com/docs/APIs/Connectors/APIReference/Connectors_API_Overview
  properties:
  - url: https://developer.boomi.com/docs/APIs/Connectors/APIReference/Connectors_API_Overview
    type: Documentation
  - url: https://developer.boomi.com/docs/Connectors/ConnectorSDK/Connector_sdk_overview
    type: GettingStarted
  - url: https://developer.boomi.com/docs/category/deploying-connector-to-the-boomi-enterprise-platform
    type: GettingStarted
  description: The Boomi Connector Deployment API provides programmatic access to deploy connectors created using the Boomi Connector SDK. It enables integration with CI/CD pipelines for automated connector deployment to the Boomi Enterprise Platform.
- aid: boomi:platform-soap-api
  name: Boomi Platform SOAP API
  tags:
  - Integration
  - Platform
  - SOAP
  humanURL: https://developer.boomi.com/docs/APIs/PlatformSOAPAPI/APIObjects/API_objects_and_object-based_operations
  properties:
  - url: https://developer.boomi.com/docs/APIs/PlatformSOAPAPI/APIObjects/API_objects_and_object-based_operations
    type: Documentation
  - url: https://developer.boomi.com/docs/APIs/PlatformAPI/Introduction/Platform_API
    type: GettingStarted
  description: The Boomi Platform SOAP API provides the same programmatic access to the Boomi Enterprise Platform as the REST API but through a SOAP interface. The WSDL is available at api.boomi.com and the API uses WS-Security with UsernameToken for authentication. It supports GET, QUERY, CREATE, UPDATE, EXECUTE, and DELETE operations on platform objects.
- aid: boomi:mft-api
  name: Boomi MFT API
  tags:
  - Managed File Transfer
  - MFT
  - REST
  - SOAP
  humanURL: https://developer.boomi.com/docs/APIs/MFT/overview
  properties:
  - url: https://developer.boomi.com/docs/APIs/MFT/overview
    type: Documentation
  description: 'The Boomi Managed File Transfer (MFT) API provides two main types of APIs for interacting with MFT services: REST APIs and SOAP APIs. REST APIs are designed around a resource-oriented model using standard HTTP methods, while SOAP APIs offer a structured, protocol-driven alternative. The API covers AFT Management, AuditLog, Content Upload and Download, Health Check, and File Sharing operations.'
- aid: boomi:api-gateway-graphql-api
  name: Boomi API Gateway GraphQL API
  tags:
  - API Gateway
  - API Management
  - GraphQL
  humanURL: https://developer.boomi.com/docs/APIs/GraphQL/APIM_GraphQL_apis_overview
  properties:
  - url: https://developer.boomi.com/docs/APIs/GraphQL/APIM_GraphQL_apis_overview
    type: Documentation
  - url: https://developer.boomi.com/docs/APIs/GraphQL
    type: GettingStarted
  - url: https://developer.boomi.com/docs/APIs/GraphQL/GraphQL_api_explorer
    type: Documentation
  description: The Boomi API Gateway GraphQL API enables developers to retrieve and modify data related to API Gateway management through GraphQL. It supports queries and mutations across authentication sources, deployed APIs and applications, API plans, environments and gateway configuration, metrics, and runtime operations. The API implements rate limiting and returns HTTP 429 when exceeded.
- aid: boomi:agent-control-tower-graphql-api
  name: Boomi Agent Control Tower GraphQL API
  tags:
  - AI Agents
  - Governance
  - GraphQL
  humanURL: https://developer.boomi.com/docs/APIs/GraphQL/ACT-Custom_API
  properties:
  - url: https://developer.boomi.com/docs/APIs/GraphQL/ACT-Custom_API
    type: Documentation
  - url: https://developer.boomi.com/docs/APIs/ACT/Agent_Control_Tower
    type: APIReference
  - url: https://help.boomi.com/docs/Atomsphere/Platform/Agent_Control_Tower
    type: Documentation
  - url: json-schema/boomi-ai-agent-schema.json
    type: JSONSchema
  description: The Boomi Agent Control Tower GraphQL API provides programmatic access to AI agent management capabilities within Boomi Agentstudio. It enables listing accounts and agents, including those from external providers, through Custom Account APIs. Authentication uses JWT tokens obtained via Basic Authentication against the Boomi platform.
name: Boomi
tags:
- AI Agents
- Automation
- B2B
- Data Integration
- EDI
- Integrations
- Management
- MFT
- Platform
- Workflows
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
- url: https://www.linkedin.com/company/boomi-inc/
  name: LinkedIn
  type: LinkedIn
- url: https://github.com/OfficialBoomi
  name: GitHub
  type: GitHub
- url: https://boomi.com/
  name: 'Boomi Integration Platform as a Service: Connect Everything'
  type: Website
  description: 'null'
- url: https://boomi.com/pricing/
  name: Boomi Enterprise Platform Pricing & Editions | Boomi
  type: Pricing
  description: 'null'
- url: https://boomi.com/compliance/
  name: 'Security & Privacy Compliance: We Keep Customer Data Safe'
  type: Compliance
  description: 'null'
- url: https://boomi.com/form/trial/
  name: Boomi Free Trial | Boomi
  type: Trial
  description: 'null'
- url: https://boomi.com/custom-demo-request/
  name: Custom Demo Request | Boomi
  type: RequestDemo
  description: 'null'
- url: https://discover.boomi.com/
  name: Discover Business Outcomes, Accelerated
  type: Marketplace
  description: 'null'
- url: https://boomi.com/customers/
  name: Customer Stories | Boomi
  type: CaseStudies
  description: 'null'
- url: https://boomi.com/company/events/?event_style=upcoming
  name: Events & Webinars | Boomi
  type: Events
  description: 'null'
- url: https://boomi.com/company/events/?event_style=upcoming
  name: Events & Webinars | Boomi
  type: Webinars
  description: 'null'
- url: https://boomi.com/blog/
  name: Boomi Blog
  type: Blog
  description: 'null'
- url: https://boomi.com/resources/?content_type=ebook
  name: Boomi Resource Center
  type: eBooks
  description: 'null'
- url: https://boomi.com/services/training/
  name: Training & Certification for Boomis iPaaS Platform
  type: Training
  description: 'null'
- url: https://help.boomi.com/
  name: Boomi Documentation
  type: Documentation
  description: 'null'
- url: https://community.boomi.com/s/support
  name: Support Center - Boomi Community
  type: Support
  description: 'null'
- url: https://boomi.com/product-updates/
  name: Product Updates | Boomi
  type: ' WhatsNew'
  description: 'null'
- url: https://boomi.com/partners/
  name: Boomi Partner Ecosystem Leading System Integrators & Innovators
  type: Partners
  description: 'null'
- url: https://boomi.com/privacy/
  name: Privacy Policy | Boomi
  type: PrivacyPolicy
  description: 'null'
- url: https://boomi.com/legal/service/
  name: Service Description - Legal | Boomi
  type: TermsOfService
  description: 'null'
- url: https://boomi.com/compliance/
  name: 'Security & Privacy Compliance: We Keep Customer Data Safe'
  type: Trust
  description: Compliance
created: '2025-01-08'
modified: '2026-04-07'
position: Consuming
description: Boomi is a leading integration platform that allows organizations to connect applications, data, and people across cloud and on-premise environments. By leveraging Boomi's intuitive visual interface and pre-built connectors, businesses can quickly and easily create integrations that streamline processes, improve productivity, and enhance the overall customer experience.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

