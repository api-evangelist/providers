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
  - url: https://developer.boomi.com/
    name: Boomi Developer Documentation
    type: DeveloperPortal
    description: 'null'
  - url: https://community.boomi.com/s/
    name: Boomi User Community
    type: Community
    description: 'null'
  - url: https://community.boomi.com/s/forums
    name: Boomi Community Forums
    type: Forums
    description: 'null'
  - url: https://status.boomi.com/
    name: Boomi Status
    type: StatusPage
    description: 'null'
  - url: https://help.boomi.com/docs/category/release-notes
    name: Release Notes | Boomi Documentation
    type: ReleaseNotes
    description: 'null'
  - url: https://boomi.com/company/
    name: About Boomi
    type: About
    description: 'null'
  - url: https://boomi.com/company/contact/
    name: Contact Boomi
    type: Contact
    description: 'null'
  - url: https://twitter.com/boomi
    name: Boomi on X
    type: X
    description: 'null'
  - url: https://platform.boomi.com/
    name: Boomi Enterprise Platform Sign In
    type: SignIn
    description: 'null'
  - url: https://boomi.com/connectors/
    name: Boomi Application Connectors
    type: Connectors
    description: 'null'
  - url: https://boomi.com/platform/master-data-hub/
    name: Boomi Data Hub | Enterprise Data Management
    type: DataHub
    description: 'null'
  - url: https://boomi.com/platform/api-products/
    name: API Products | Boomi
    type: Products
    description: 'null'
  - url: https://www.postman.com/boomi-lp/boomi/overview
    name: Boomi Postman Workspace
    type: PostmanWorkspace
    description: 'null'
  - url: https://boomi.com/company/careers/
    name: Careers | Boomi
    type: Careers
    description: 'null'
  - url: https://help.boomi.com/docs/Atomsphere/API%20Management/Topics/c-api-Authentication_3baf0ddd-3532-403f-b66b-4800c1e19098
    name: Authentication in API Management | Boomi
    type: Authentication
    description: 'null'
  - url: https://boomi.com/platform/agentstudio/
    name: Boomi Agentstudio | AI Agent Management
    type: Agentstudio
    description: 'null'
  - url: https://boomi.com/model-context-protocol/
    name: Model Context Protocol | Boomi
    type: MCP
    description: 'null'
  - url: https://help.boomi.com/docs/Atomsphere/Integration/int-Boomi_Platform_APIs
    name: Boomi Enterprise Platform APIs | Boomi Documentation
    type: APIReference
    description: 'null'
  - url: https://boomi.com/platform/integration/
    name: Enterprise Integration Platform | Boomi
    type: Integration
    description: 'null'
  - url: https://boomi.com/platform/ai/
    name: Agent Management | Boomi
    type: AgentManagement
  - url: https://boomi.com/platform/ai-agents/
    name: Platform Agents | Boomi
    type: PlatformAgents
  - url: https://boomi.com/agent-connectivity/
    name: Agent Connectivity | Boomi
    type: AgentConnectivity
  - url: https://boomi.com/responsible-ai/
    name: Responsible AI | Boomi
    type: ResponsibleAI
  - url: https://boomi.com/platform/flow/
    name: Boomi Flow | Process Automation
    type: Flow
  - url: https://boomi.com/platform/event-streams/
    name: Event Streams | Boomi
    type: EventStreams
  - url: https://boomi.com/platform/b2b-management/
    name: B2B/EDI Management | Boomi
    type: B2BManagement
  - url: https://boomi.com/platform/task-automation/
    name: Task Automation | Boomi
    type: TaskAutomation
  - url: https://boomi.com/platform/managed-file-transfer/
    name: Managed File Transfer | Boomi
    type: ManagedFileTransfer
  - url: https://boomi.com/platform/api-management/
    name: API Management | Boomi
    type: APIManagement
  - url: https://boomi.com/platform/api-governance/
    name: API Governance | Boomi
    type: APIGovernance
  - url: https://boomi.com/platform/api-security/
    name: API Security | Boomi
    type: APISecurity
  - url: https://boomi.com/platform/data-management/
    name: Data Management | Boomi
    type: DataManagement
  - url: https://boomi.com/platform/datahub/
    name: Data Hub | Boomi
    type: DataHub
  - url: https://boomi.com/platform/boomi-data-integration/
    name: Data Integration | Boomi
    type: DataIntegration
  - url: https://boomi.com/platform/metahub/
    name: Meta Hub | Boomi
    type: MetaHub
  - url: https://boomi.com/platform/embedded/
    name: Boomi Embedded | OEM Integration Platform
    type: BoomiEmbedded
  - url: https://boomi.com/solutions/
    name: Boomi Solutions
    type: Solutions
  - data:
      - name: Order-to-Cash
        url: https://boomi.com/solutions/
        features:
          - Sales Order Processing
          - Invoice Management
          - Revenue Recognition
          - Accounts Receivable
          - Quote To Cash
          - Order Management
      - name: Source-to-Pay
        url: https://boomi.com/solutions/
        features:
          - Procurement Integration
          - Purchase Orders
          - Supplier Management
          - Accounts Payable
          - Spend Management
          - Vendor Onboarding
      - name: Hire-to-Retire
        url: https://boomi.com/solutions/
        features:
          - HR Integration
          - Employee Onboarding
          - Offboarding
          - Payroll Integration
          - Workforce Management
          - HCM Integration
      - name: Integration Center of Excellence
        url: https://boomi.com/solutions/
        features:
          - COE
          - Integration Governance
          - Reusable Integration
          - Integration Standards
          - Platform Governance
          - Best Practices
      - name: Practical AI
        url: https://boomi.com/solutions/
        features:
          - AI Adoption
          - Generative AI
          - LLM Integration
          - AI Automation
          - AI Use Cases
          - Agentic AI
      - name: Customer 360
        url: https://boomi.com/solutions/
        features:
          - Customer Data Integration
          - CRM Integration
          - Unified Customer Profile
          - Data Unification
          - Customer Insights
          - Omnichannel Data
      - name: M&A and Divestiture
        url: https://boomi.com/solutions/
        features:
          - Merger Integration
          - System Consolidation
          - Divestiture
          - Application Rationalization
          - Post-Merger Integration
          - IT Integration
      - name: ERP Modernization
        url: https://boomi.com/solutions/
        features:
          - ERP Migration
          - SAP Migration
          - ERP Integration
          - Legacy ERP
          - Cloud ERP
          - S/4HANA Migration
      - name: Cloud Migration Connectivity
        url: https://boomi.com/solutions/
        features:
          - Cloud Migration
          - Hybrid Integration
          - On-Premises To Cloud
          - Multi-Cloud Connectivity
          - Lift And Shift
          - Cloud-Native Integration
      - name: Legacy Modernization
        url: https://boomi.com/solutions/
        features:
          - Mainframe Integration
          - Legacy System Connectivity
          - Application Modernization
          - Technical Debt Reduction
          - API Enablement
          - System Replacement
      - name: Manufacturing
        url: https://boomi.com/solutions/
        features:
          - Supply Chain Integration
          - IoT Integration
          - Shop Floor Connectivity
          - MES Integration
          - Industry 4.0
          - ERP To MES
      - name: Healthcare and Life Sciences
        url: https://boomi.com/solutions/
        features:
          - HL7
          - FHIR
          - EHR Integration
          - Patient Data Integration
          - Clinical Data Exchange
          - Healthcare Interoperability
      - name: Retail
        url: https://boomi.com/solutions/
        features:
          - POS Integration
          - Inventory Management
          - Omnichannel
          - E-Commerce Integration
          - Order Management
          - Supplier Integration
      - name: Financial Services
        url: https://boomi.com/solutions/
        features:
          - Core Banking Integration
          - Payments Integration
          - Regulatory Compliance
          - FinTech Connectivity
          - Risk Data Integration
          - Open Banking
      - name: Higher Education
        url: https://boomi.com/solutions/
        features:
          - Student Information Systems
          - LMS Integration
          - Campus Integration
          - SIS Connectivity
          - Enrollment Management
          - Research Data Integration
      - name: Public Sector
        url: https://boomi.com/solutions/
        features:
          - Government Integration
          - Citizen Services
          - FISMA Compliance
          - FedRAMP
          - Agency Data Sharing
          - Digital Government
    name: Use Cases
    type: UseCases
  - data:
      - name: SAP
        url: https://boomi.com/solutions/application/sap/
        features:
          - SAP Integration
          - S/4HANA
          - SAP ERP
          - SAP BTP
          - BAPI
          - IDoc
          - RFC
      - name: AWS
        url: https://boomi.com/solutions/application/aws/
        features:
          - Amazon Web Services
          - AWS Integration
          - S3
          - Lambda
          - SQS
          - DynamoDB
          - EC2
      - name: Salesforce
        url: https://boomi.com/solutions/application/salesforce/
        features:
          - Salesforce CRM
          - Salesforce Integration
          - Salesforce Objects
          - Sales Cloud
          - Service Cloud
          - Marketing Cloud
          - Salesforce API
      - name: ServiceNow
        url: https://boomi.com/solutions/application/servicenow/
        features:
          - ServiceNow Integration
          - ITSM
          - IT Service Management
          - Incident Management
          - Change Management
          - ServiceNow API
          - CMDB
      - name: Oracle NetSuite
        url: https://boomi.com/solutions/application/netsuite/
        features:
          - NetSuite Integration
          - ERP Integration
          - Oracle NetSuite
          - SuiteAPI
          - Financial Management
          - Order Management
          - NetSuite SuiteTalk
      - name: Slack
        url: https://boomi.com/solutions/application/slack/
        features:
          - Slack Integration
          - Slack Messaging
          - Slack Notifications
          - Slack API
          - Collaboration Integration
          - Slack Webhooks
      - name: Workday
        url: https://boomi.com/solutions/application/workday/
        features:
          - Workday Integration
          - HCM Integration
          - Human Capital Management
          - Workday API
          - Workday Studio
          - HR Data Sync
          - Payroll Integration
      - name: Stripe
        url: https://boomi.com/connectors/
        features:
          - Stripe Integration
          - Payment Processing
          - Stripe API
          - Billing Integration
          - Subscription Management
          - Payment Data Sync
      - name: Snowflake
        url: https://boomi.com/connectors/
        features:
          - Snowflake Integration
          - Cloud Data Warehouse
          - Snowflake Connector
          - Data Loading
          - Analytics Integration
          - Snowflake SQL
      - name: OpenAI
        url: https://boomi.com/connectors/
        features:
          - OpenAI Integration
          - ChatGPT Integration
          - LLM Connectivity
          - AI API Integration
          - GPT Models
          - Generative AI
      - name: Shopify
        url: https://boomi.com/connectors/
        features:
          - Shopify Integration
          - E-Commerce Integration
          - Order Sync
          - Product Catalog Sync
          - Shopify API
          - Retail Integration
      - name: Google Drive
        url: https://boomi.com/connectors/
        features:
          - Google Drive Integration
          - Google Workspace
          - File Sync
          - Google API
          - Document Management
          - Cloud Storage Integration
      - name: Pinecone
        url: https://boomi.com/connectors/
        features:
          - Pinecone Integration
          - Vector Database
          - AI Embeddings
          - Semantic Search
          - RAG
          - Knowledge Base Storage
    name: Integrations
    type: Integrations
  - data:
      - name: Agent Management
        url: https://boomi.com/platform/ai/
        features:
          - AI Agents
          - Autonomous Agents
          - Agent Orchestration
          - LLM Integration
          - Intelligent Automation
          - Agent Lifecycle Management
          - Agent Deployment
      - name: Agentstudio
        url: https://boomi.com/platform/agentstudio/
        features:
          - Agent Builder
          - No-Code Agent Creation
          - Agent Configuration
          - AI Agent Studio
          - Agent Design
          - Agent Management Console
      - name: Platform Agents
        url: https://boomi.com/platform/ai-agents/
        features:
          - Pre-Built Agents
          - Enterprise Agents
          - Boomi Agents
          - Platform Automation Agents
          - Out-Of-The-Box Agents
      - name: Agent Connectivity
        url: https://boomi.com/agent-connectivity/
        features:
          - Agent Integrations
          - Agent Tools
          - API Connectivity
          - MCP Tools
          - Agent Access
          - Tool Connectivity
          - Agent API Access
      - name: Model Context Protocol (MCP)
        url: https://boomi.com/model-context-protocol/
        features:
          - MCP Server
          - Model Context Protocol
          - Tool Connectivity
          - AI Tool Access
          - LLM Tools
          - MCP Integration
          - Anthropic MCP
      - name: Responsible AI
        url: https://boomi.com/responsible-ai/
        features:
          - AI Governance
          - AI Safety
          - AI Ethics
          - Guardrails
          - Responsible Automation
          - AI Compliance
          - Bias Prevention
      - name: Integration & Automation
        url: https://boomi.com/platform/integration/
        features:
          - iPaaS
          - Integration Platform As A Service
          - Workflow Automation
          - Data Synchronization
          - App Connectivity
          - Enterprise Integration
          - API-Led Integration
      - name: Flow
        url: https://boomi.com/platform/flow/
        features:
          - Process Automation
          - Workflow Builder
          - Low-Code Workflow
          - Business Process Automation
          - Decision Flows
          - UI Workflow
          - Citizen Developer
      - name: Event Streams
        url: https://boomi.com/platform/event-streams/
        features:
          - Event-Driven Integration
          - Pub/Sub Messaging
          - Message Streaming
          - Real-Time Events
          - Event Broker
          - Topic-Based Messaging
          - Asynchronous Integration
      - name: B2B/EDI Management
        url: https://boomi.com/platform/b2b-management/
        features:
          - B2B Integration
          - EDI
          - Trading Partner Management
          - Supply Chain Integration
          - AS2
          - X12
          - EDIFACT
          - ANSI X12
          - Electronic Data Interchange
      - name: Task Automation
        url: https://boomi.com/platform/task-automation/
        features:
          - RPA
          - Robotic Process Automation
          - Task Scheduling
          - Automated Tasks
          - Process Execution
          - UI Automation
          - Desktop Automation
      - name: Managed File Transfer
        url: https://boomi.com/platform/managed-file-transfer/
        features:
          - MFT
          - Secure File Transfer
          - SFTP
          - FTP
          - File Exchange
          - Large File Transfer
          - File Automation
          - FTPS
      - name: API Management
        url: https://boomi.com/platform/api-management/
        features:
          - API Gateway
          - API Lifecycle Management
          - API Proxy
          - API Publishing
          - API Versioning
          - API Developer Portal
          - API Monetization
      - name: API Governance
        url: https://boomi.com/platform/api-governance/
        features:
          - API Policies
          - API Standards
          - API Compliance
          - API Quality
          - API Design Governance
          - API Linting
          - API Style Guides
      - name: API Security
        url: https://boomi.com/platform/api-security/
        features:
          - API Authentication
          - OAuth
          - JWT
          - API Threat Protection
          - API Access Control
          - API Key Management
          - Rate Limiting
      - name: API Products
        url: https://boomi.com/platform/api-products/
        features:
          - API Catalog
          - API Productization
          - API Packaging
          - API Marketplace
          - API Bundling
          - API Developer Experience
          - API Consumption
      - name: Data Management
        url: https://boomi.com/platform/data-management/
        features:
          - Master Data Management
          - MDM
          - Data Quality
          - Data Stewardship
          - Data Governance
          - Data Cleansing
          - Reference Data
      - name: Data Hub
        url: https://boomi.com/platform/datahub/
        features:
          - Data Hub
          - Golden Records
          - Master Data
          - Data Matching
          - Data Deduplication
          - Data Consolidation
          - Single Source Of Truth
      - name: Data Integration
        url: https://boomi.com/platform/boomi-data-integration/
        features:
          - ETL
          - Data Pipeline
          - Data Transformation
          - Data Migration
          - Data Synchronization
          - Batch Integration
          - Real-Time Data Integration
      - name: Meta Hub
        url: https://boomi.com/platform/metahub/
        features:
          - Metadata Management
          - Data Catalog
          - Data Lineage
          - Data Discovery
          - Metadata Governance
          - Data Observability
          - Schema Registry
      - name: Boomi Embedded
        url: https://boomi.com/platform/embedded/
        features:
          - Embedded iPaaS
          - White-Label Integration
          - OEM Integration
          - Embedded Platform
          - Integration As A Service
          - ISV Integration
          - Native Integrations
    name: Features
    type: Features
  - url: json-ld/boomi-context.jsonld
    type: JSON-LD
  - url: json-schema/boomi-process-schema.json
    type: JSONSchema
  - url: json-schema/boomi-ai-agent-schema.json
    type: JSONSchema
created: '2025-01-08'
modified: '2026-04-19'
position: Consuming
segments:
  - Workflows
description: Boomi is a leading integration platform that allows organizations to connect applications, data, and people across cloud and on-premise environments. By leveraging Boomi's intuitive visual interface and pre-built connectors, businesses can quickly and easily create integrations that streamline processes, improve productivity, and enhance the overall customer experience.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
