---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Boomi Agentic Access
  operation_count: 37
  slug: boomi-agentic-access
  summary_line: 37 operations · 24 acting
api_count: 20
apis:
- description: Boomi API Management supports the full lifecycle of APIs in any environment. Configure APIs and expose real-time integrations effortlessly.
  name: Boomi
  slug: boomi
- description: 'The Boomi API Management API provides programmatic access to API Management service functionality through REST, SOAP, and GraphQL implementations. It supports API objects and object-based operations, '
  name: Boomi API Management API
  slug: api-management-api
- description: 'The Boomi Flow API provides REST endpoints for programmatic access to Boomi Flow functionality. Built on an API-first architecture, many operations performed within Boomi Flow can be accessed through '
  name: Boomi Flow API
  slug: flow-api
- description: The Boomi Connector Deployment API provides programmatic access to deploy connectors created using the Boomi Connector SDK. It enables integration with CI/CD pipelines for automated connector deployme
  name: Boomi Connector Deployment API
  slug: connector-deployment-api
- description: The Boomi Platform SOAP API provides the same programmatic access to the Boomi Enterprise Platform as the REST API but through a SOAP interface. The WSDL is available at api.boomi.com and the API uses
  name: Boomi Platform SOAP API
  slug: platform-soap-api
- description: 'The Boomi Managed File Transfer (MFT) API provides two main types of APIs for interacting with MFT services: REST APIs and SOAP APIs. REST APIs are designed around a resource-oriented model using stan'
  name: Boomi MFT API
  slug: mft-api
- description: The Boomi API Gateway GraphQL API enables developers to retrieve and modify data related to API Gateway management through GraphQL. It supports queries and mutations across authentication sources, dep
  name: Boomi API Gateway GraphQL API
  slug: api-gateway-graphql-api
- description: The Boomi Agent Control Tower GraphQL API provides programmatic access to AI agent management capabilities within Boomi Agentstudio. It enables listing accounts and agents, including those from extern
  name: Boomi Agent Control Tower GraphQL API
  slug: agent-control-tower-graphql-api
- description: Manage Boomi Atoms — the lightweight runtime engines that execute integration processes.
  name: Boomi Atoms API
  slug: boomi-atoms-api
- description: Manage packaged components and integration pack attachments.
  name: Boomi Components API
  slug: boomi-components-api
- description: Manage deployed packages and the deployment of integration components to environments.
  name: Boomi Deployments API
  slug: boomi-deployments-api
- description: Manage runtime environments where Boomi Atoms and Molecules are deployed to run integration processes.
  name: Boomi Environments API
  slug: boomi-environments-api
- description: Execute integration processes and retrieve execution statistics and job results.
  name: Boomi Execution API
  slug: boomi-execution-api
- description: Query and manage the authoritative master records that result from matching and merging source records.
  name: Boomi Golden Records API
  slug: boomi-golden-records-api
- description: Endpoints for producing messages to Boomi Event Streams topics via HTTP REST calls.
  name: Boomi Messages API
  slug: boomi-messages-api
- description: Manage data models that define the schema and rules for master data domains.
  name: Boomi Models API
  slug: boomi-models-api
- description: Manage integration processes (recipes) within the Boomi platform.
  name: Boomi Processes API
  slug: boomi-processes-api
- description: Manage quarantined records that could not be automatically processed due to data quality issues.
  name: Boomi Quarantine API
  slug: boomi-quarantine-api
- description: Manage DataHub repositories that contain master data domains.
  name: Boomi Repositories API
  slug: boomi-repositories-api
- description: Manage data sources that contribute records to the master data hub for matching and merging.
  name: Boomi Sources API
  slug: boomi-sources-api
arazzos:
- description: Resolve an environment by name and inspect a deployed package within it.
  name: Boomi Audit Environment Deployments
  slug: boomi-audit-environment-deployments-workflow
- description: Create a new integration process, read it back, and apply an initial update.
  name: Boomi Create and Verify a Process
  slug: boomi-create-and-verify-process-workflow
- description: Confirm a repository exists, create a contributing source, and list sources to verify.
  name: Boomi DataHub Onboard a Source
  slug: boomi-datahub-onboard-source-workflow
- description: Create a repository, define a data model within it, and publish the model.
  name: Boomi DataHub Provision a Model
  slug: boomi-datahub-provision-model-workflow
- description: List models in a repository, read a draft model, and publish it if still in draft.
  name: Boomi DataHub Publish a Draft Model
  slug: boomi-datahub-publish-draft-model-workflow
- description: Pick a repository, list golden records for a domain, and review quarantined records.
  name: Boomi DataHub Review Data Quality
  slug: boomi-datahub-review-data-quality-workflow
- description: Find a process by name, confirm it exists, and delete it from the platform.
  name: Boomi Decommission a Process
  slug: boomi-decommission-process-workflow
- description: Find an integration process, package it, and deploy the package to an environment.
  name: Boomi Deploy a Process
  slug: boomi-deploy-process-workflow
- description: Trigger a process run on an Atom and poll execution records until it finishes.
  name: Boomi Execute and Monitor a Process
  slug: boomi-execute-and-monitor-process-workflow
- description: Run a process, read its execution record, and publish the outcome to an Event Streams topic.
  name: Boomi Execute a Process and Publish the Result
  slug: boomi-execute-process-and-publish-result-workflow
- description: Create a packaged component from a component version and read it back.
  name: Boomi Package and Inspect a Component
  slug: boomi-package-and-inspect-component-workflow
- description: Create a runtime environment and confirm an online Atom is available for it.
  name: Boomi Provision Environment With Atom
  slug: boomi-provision-environment-with-atom-workflow
- description: Take an existing deployment's package and deploy it to a freshly created environment.
  name: Boomi Redeploy a Package to a New Environment
  slug: boomi-redeploy-package-to-environment-workflow
- description: Find a process by name, read its current schedule, and update it.
  name: Boomi Schedule a Process
  slug: boomi-schedule-process-workflow
artifact_total: 137
asyncapis:
- description: Boomi Event Streams provides a publish-subscribe messaging system within the Boomi Enterprise Platform. Topics act as channels where producers publish messages and consumers receive them via Boomi rec
  name: Boomi Event Streams
  slug: boomi-event-streams-asyncapi
collections:
- collection_type: postman
  name: Boomi DataHub API
  slug: postman-boomi-datahub-api
- collection_type: postman
  name: Boomi Event Streams REST API
  slug: postman-boomi-event-streams
- collection_type: postman
  name: Boomi Platform REST API
  slug: postman-boomi-platform-rest-api
- collection_type: open
  name: Boomi DataHub API
  slug: open-boomi-datahub-api
- collection_type: open
  name: Boomi Event Streams REST API
  slug: open-boomi-event-streams
- collection_type: open
  name: Boomi Platform REST API
  slug: open-boomi-platform-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/boomi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boomi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/boomi-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/boomi-audit-environment-deployments-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/boomi-create-and-verify-process-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/boomi-datahub-onboard-source-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/boomi-datahub-provision-model-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/boomi-datahub-publish-draft-model-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/boomi-datahub-review-data-quality-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/boomi-decommission-process-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/boomi-deploy-process-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/boomi-execute-and-monitor-process-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/boomi-execute-process-and-publish-result-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/boomi-package-and-inspect-component-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/boomi-provision-environment-with-atom-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/boomi-redeploy-package-to-environment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/boomi-schedule-process-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boomi-inc/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/OfficialBoomi
- group: company
  title: ''
  type: Website
  url: https://boomi.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://boomi.com/pricing/
- group: auth
  title: ''
  type: Compliance
  url: https://boomi.com/compliance/
- group: start
  title: ''
  type: Trial
  url: https://boomi.com/form/trial/
- group: start
  title: ''
  type: RequestDemo
  url: https://boomi.com/custom-demo-request/
- group: other
  title: ''
  type: Marketplace
  url: https://discover.boomi.com/
- group: other
  title: ''
  type: CaseStudies
  url: https://boomi.com/customers/
- group: other
  title: ''
  type: Events
  url: https://boomi.com/company/events/?event_style=upcoming
- group: learn
  title: ''
  type: Webinars
  url: https://boomi.com/company/events/?event_style=upcoming
- group: company
  title: ''
  type: Blog
  url: https://boomi.com/blog/
- group: other
  title: ''
  type: eBooks
  url: https://boomi.com/resources/?content_type=ebook
- group: learn
  title: ''
  type: Training
  url: https://boomi.com/services/training/
- group: docs
  title: ''
  type: Documentation
  url: https://help.boomi.com/
- group: operate
  title: ''
  type: Support
  url: https://community.boomi.com/s/support
- group: other
  title: ''
  type: ' WhatsNew'
  url: https://boomi.com/product-updates/
- group: company
  title: ''
  type: Partners
  url: https://boomi.com/partners/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boomi.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boomi.com/legal/service/
- group: auth
  title: ''
  type: Trust
  url: https://boomi.com/compliance/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.boomi.com/
- group: operate
  title: ''
  type: Community
  url: https://community.boomi.com/s/
- group: operate
  title: ''
  type: Forums
  url: https://community.boomi.com/s/forums
- group: operate
  title: ''
  type: StatusPage
  url: https://status.boomi.com/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://help.boomi.com/docs/category/release-notes
- group: company
  title: ''
  type: About
  url: https://boomi.com/company/
- group: operate
  title: ''
  type: Contact
  url: https://boomi.com/company/contact/
- group: other
  title: ''
  type: X
  url: https://twitter.com/boomi
- group: start
  title: ''
  type: Login
  url: https://platform.boomi.com/
- group: other
  title: ''
  type: DataHub
  url: https://boomi.com/platform/master-data-hub/
- group: other
  title: ''
  type: Products
  url: https://boomi.com/platform/api-products/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/boomi-lp/boomi/overview
- group: company
  title: ''
  type: Careers
  url: https://boomi.com/company/careers/
- group: auth
  title: ''
  type: Authentication
  url: https://help.boomi.com/docs/Atomsphere/API%20Management/Topics/c-api-Authentication_3baf0ddd-3532-403f-b66b-4800c1e19098
- group: other
  title: ''
  type: Agentstudio
  url: https://boomi.com/platform/agentstudio/
- group: agent
  title: ''
  type: MCP
  url: https://boomi.com/model-context-protocol/
- group: docs
  title: ''
  type: APIReference
  url: https://help.boomi.com/docs/Atomsphere/Integration/int-Boomi_Platform_APIs
- group: other
  title: ''
  type: AgentManagement
  url: https://boomi.com/platform/ai/
- group: other
  title: ''
  type: PlatformAgents
  url: https://boomi.com/platform/ai-agents/
- group: other
  title: ''
  type: AgentConnectivity
  url: https://boomi.com/agent-connectivity/
- group: other
  title: ''
  type: ResponsibleAI
  url: https://boomi.com/responsible-ai/
- group: other
  title: ''
  type: Flow
  url: https://boomi.com/platform/flow/
- group: other
  title: ''
  type: EventStreams
  url: https://boomi.com/platform/event-streams/
- group: other
  title: ''
  type: B2BManagement
  url: https://boomi.com/platform/b2b-management/
- group: other
  title: ''
  type: TaskAutomation
  url: https://boomi.com/platform/task-automation/
- group: other
  title: ''
  type: ManagedFileTransfer
  url: https://boomi.com/platform/managed-file-transfer/
- group: other
  title: ''
  type: APIManagement
  url: https://boomi.com/platform/api-management/
- group: other
  title: ''
  type: APIGovernance
  url: https://boomi.com/platform/api-governance/
- group: auth
  title: ''
  type: Security
  url: https://boomi.com/platform/api-security/
- group: other
  title: ''
  type: DataManagement
  url: https://boomi.com/platform/data-management/
- group: other
  title: ''
  type: DataHub
  url: https://boomi.com/platform/datahub/
- group: build
  title: ''
  type: DataIntegration
  url: https://boomi.com/platform/boomi-data-integration/
- group: other
  title: ''
  type: MetaHub
  url: https://boomi.com/platform/metahub/
- group: other
  title: ''
  type: BoomiEmbedded
  url: https://boomi.com/platform/embedded/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/boomi-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/boomi-process-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/boomi-ai-agent-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.boomi.com/llms.txt
created: '2025-01-08'
description: Boomi is a leading integration platform that allows organizations to connect applications, data, and people across cloud and on-premise environments. By leveraging Boomi's intuitive visual interface and pre-built connectors, businesses can quickly and easily create integrations that streamline processes, improve productivity, and enhance the overall customer experience.
features:
- features:
  - AI Agents
  - Autonomous Agents
  - Agent Orchestration
  - LLM Integration
  - Intelligent Automation
  - Agent Lifecycle Management
  - Agent Deployment
  name: Agent Management
  url: https://boomi.com/platform/ai/
- features:
  - Agent Builder
  - No-Code Agent Creation
  - Agent Configuration
  - AI Agent Studio
  - Agent Design
  - Agent Management Console
  name: Agentstudio
  url: https://boomi.com/platform/agentstudio/
- features:
  - Pre-Built Agents
  - Enterprise Agents
  - Boomi Agents
  - Platform Automation Agents
  - Out-Of-The-Box Agents
  name: Platform Agents
  url: https://boomi.com/platform/ai-agents/
- features:
  - Agent Integrations
  - Agent Tools
  - API Connectivity
  - MCP Tools
  - Agent Access
  - Tool Connectivity
  - Agent API Access
  name: Agent Connectivity
  url: https://boomi.com/agent-connectivity/
- features:
  - MCP Server
  - Model Context Protocol
  - Tool Connectivity
  - AI Tool Access
  - LLM Tools
  - MCP Integration
  - Anthropic MCP
  name: Model Context Protocol (MCP)
  url: https://boomi.com/model-context-protocol/
- features:
  - AI Governance
  - AI Safety
  - AI Ethics
  - Guardrails
  - Responsible Automation
  - AI Compliance
  - Bias Prevention
  name: Responsible AI
  url: https://boomi.com/responsible-ai/
- features:
  - iPaaS
  - Integration Platform As A Service
  - Workflow Automation
  - Data Synchronization
  - App Connectivity
  - Enterprise Integration
  - API-Led Integration
  name: Integration & Automation
  url: https://boomi.com/platform/integration/
- features:
  - Process Automation
  - Workflow Builder
  - Low-Code Workflow
  - Business Process Automation
  - Decision Flows
  - UI Workflow
  - Citizen Developer
  name: Flow
  url: https://boomi.com/platform/flow/
- features:
  - Event-Driven Integration
  - Pub/Sub Messaging
  - Message Streaming
  - Real-Time Events
  - Event Broker
  - Topic-Based Messaging
  - Asynchronous Integration
  name: Event Streams
  url: https://boomi.com/platform/event-streams/
- features:
  - B2B Integration
  - EDI
  - Trading Partner Management
  - Supply Chain Integration
  - AS2
  - X12
  - EDIFACT
  - ANSI X12
  - Electronic Data Interchange
  name: B2B/EDI Management
  url: https://boomi.com/platform/b2b-management/
- features:
  - RPA
  - Robotic Process Automation
  - Task Scheduling
  - Automated Tasks
  - Process Execution
  - UI Automation
  - Desktop Automation
  name: Task Automation
  url: https://boomi.com/platform/task-automation/
- features:
  - MFT
  - Secure File Transfer
  - SFTP
  - FTP
  - File Exchange
  - Large File Transfer
  - File Automation
  - FTPS
  name: Managed File Transfer
  url: https://boomi.com/platform/managed-file-transfer/
- features:
  - API Gateway
  - API Lifecycle Management
  - API Proxy
  - API Publishing
  - API Versioning
  - API Developer Portal
  - API Monetization
  name: API Management
  url: https://boomi.com/platform/api-management/
- features:
  - API Policies
  - API Standards
  - API Compliance
  - API Quality
  - API Design Governance
  - API Linting
  - API Style Guides
  name: API Governance
  url: https://boomi.com/platform/api-governance/
- features:
  - API Authentication
  - OAuth
  - JWT
  - API Threat Protection
  - API Access Control
  - API Key Management
  - Rate Limiting
  name: API Security
  url: https://boomi.com/platform/api-security/
- features:
  - API Catalog
  - API Productization
  - API Packaging
  - API Marketplace
  - API Bundling
  - API Developer Experience
  - API Consumption
  name: API Products
  url: https://boomi.com/platform/api-products/
- features:
  - Master Data Management
  - MDM
  - Data Quality
  - Data Stewardship
  - Data Governance
  - Data Cleansing
  - Reference Data
  name: Data Management
  url: https://boomi.com/platform/data-management/
- features:
  - Data Hub
  - Golden Records
  - Master Data
  - Data Matching
  - Data Deduplication
  - Data Consolidation
  - Single Source Of Truth
  name: Data Hub
  url: https://boomi.com/platform/datahub/
- features:
  - ETL
  - Data Pipeline
  - Data Transformation
  - Data Migration
  - Data Synchronization
  - Batch Integration
  - Real-Time Data Integration
  name: Data Integration
  url: https://boomi.com/platform/boomi-data-integration/
- features:
  - Metadata Management
  - Data Catalog
  - Data Lineage
  - Data Discovery
  - Metadata Governance
  - Data Observability
  - Schema Registry
  name: Meta Hub
  url: https://boomi.com/platform/metahub/
- features:
  - Embedded iPaaS
  - White-Label Integration
  - OEM Integration
  - Embedded Platform
  - Integration As A Service
  - ISV Integration
  - Native Integrations
  name: Boomi Embedded
  url: https://boomi.com/platform/embedded/
finops:
- name: Boomi Finops
  service_category: Integration Platform (iPaaS)
  slug: boomi-finops
graphqls:
- description: 'The Boomi API Management API provides programmatic access to API Management service functionality through REST, SOAP, and GraphQL implementations. It supports API objects and object-based operations, '
  name: Boomi GraphQL API
  slug: boomi-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boomi.png
integrations:
- features:
  - SAP Integration
  - S/4HANA
  - SAP ERP
  - SAP BTP
  - BAPI
  - IDoc
  - RFC
  name: SAP
  url: https://boomi.com/solutions/application/sap/
- features:
  - Amazon Web Services
  - AWS Integration
  - S3
  - Lambda
  - SQS
  - DynamoDB
  - EC2
  name: AWS
  url: https://boomi.com/solutions/application/aws/
- features:
  - Salesforce CRM
  - Salesforce Integration
  - Salesforce Objects
  - Sales Cloud
  - Service Cloud
  - Marketing Cloud
  - Salesforce API
  name: Salesforce
  url: https://boomi.com/solutions/application/salesforce/
- features:
  - ServiceNow Integration
  - ITSM
  - IT Service Management
  - Incident Management
  - Change Management
  - ServiceNow API
  - CMDB
  name: ServiceNow
  url: https://boomi.com/solutions/application/servicenow/
- features:
  - NetSuite Integration
  - ERP Integration
  - Oracle NetSuite
  - SuiteAPI
  - Financial Management
  - Order Management
  - NetSuite SuiteTalk
  name: Oracle NetSuite
  url: https://boomi.com/solutions/application/netsuite/
- features:
  - Slack Integration
  - Slack Messaging
  - Slack Notifications
  - Slack API
  - Collaboration Integration
  - Slack Webhooks
  name: Slack
  url: https://boomi.com/solutions/application/slack/
- features:
  - Workday Integration
  - HCM Integration
  - Human Capital Management
  - Workday API
  - Workday Studio
  - HR Data Sync
  - Payroll Integration
  name: Workday
  url: https://boomi.com/solutions/application/workday/
- features:
  - Stripe Integration
  - Payment Processing
  - Stripe API
  - Billing Integration
  - Subscription Management
  - Payment Data Sync
  name: Stripe
  url: https://boomi.com/connectors/
- features:
  - Snowflake Integration
  - Cloud Data Warehouse
  - Snowflake Connector
  - Data Loading
  - Analytics Integration
  - Snowflake SQL
  name: Snowflake
  url: https://boomi.com/connectors/
- features:
  - OpenAI Integration
  - ChatGPT Integration
  - LLM Connectivity
  - AI API Integration
  - GPT Models
  - Generative AI
  name: OpenAI
  url: https://boomi.com/connectors/
- features:
  - Shopify Integration
  - E-Commerce Integration
  - Order Sync
  - Product Catalog Sync
  - Shopify API
  - Retail Integration
  name: Shopify
  url: https://boomi.com/connectors/
- features:
  - Google Drive Integration
  - Google Workspace
  - File Sync
  - Google API
  - Document Management
  - Cloud Storage Integration
  name: Google Drive
  url: https://boomi.com/connectors/
- features:
  - Pinecone Integration
  - Vector Database
  - AI Embeddings
  - Semantic Search
  - RAG
  - Knowledge Base Storage
  name: Pinecone
  url: https://boomi.com/connectors/
json_schemas:
- name: Boomi AI Agent
  property_count: 12
  slug: boomi-ai-agent
- name: Atom
  property_count: 7
  slug: boomi-atom
- name: AtomInput
  property_count: 2
  slug: boomi-atominput
- name: AtomQueryResult
  property_count: 3
  slug: boomi-atomqueryresult
- name: DeployedPackage
  property_count: 7
  slug: boomi-deployedpackage
- name: DeployedPackageInput
  property_count: 3
  slug: boomi-deployedpackageinput
- name: DeployedPackageQueryResult
  property_count: 3
  slug: boomi-deployedpackagequeryresult
- name: Environment
  property_count: 4
  slug: boomi-environment
- name: EnvironmentInput
  property_count: 2
  slug: boomi-environmentinput
- name: EnvironmentQueryResult
  property_count: 3
  slug: boomi-environmentqueryresult
- name: ErrorResponse
  property_count: 2
  slug: boomi-errorresponse
- name: ExecutionRecord
  property_count: 7
  slug: boomi-executionrecord
- name: ExecutionRecordQueryResult
  property_count: 3
  slug: boomi-executionrecordqueryresult
- name: ExecutionRequest
  property_count: 3
  slug: boomi-executionrequest
- name: ExecutionRequestResult
  property_count: 2
  slug: boomi-executionrequestresult
- name: GoldenRecord
  property_count: 5
  slug: boomi-goldenrecord
- name: MessageItem
  property_count: 2
  slug: boomi-messageitem
- name: Model
  property_count: 6
  slug: boomi-model
- name: ModelField
  property_count: 4
  slug: boomi-modelfield
- name: ModelInput
  property_count: 2
  slug: boomi-modelinput
- name: MultiMessageRequest
  property_count: 1
  slug: boomi-multimessagerequest
- name: PackagedComponent
  property_count: 6
  slug: boomi-packagedcomponent
- name: PackagedComponentInput
  property_count: 4
  slug: boomi-packagedcomponentinput
- name: Boomi Integration Process
  property_count: 10
  slug: boomi-process
- name: ProcessInput
  property_count: 2
  slug: boomi-processinput
- name: ProcessQueryResult
  property_count: 3
  slug: boomi-processqueryresult
- name: ProcessSchedules
  property_count: 4
  slug: boomi-processschedules
- name: PublishResponse
  property_count: 2
  slug: boomi-publishresponse
- name: QuarantineEntry
  property_count: 5
  slug: boomi-quarantineentry
- name: QueryRequest
  property_count: 1
  slug: boomi-queryrequest
- name: Repository
  property_count: 4
  slug: boomi-repository
- name: RepositoryInput
  property_count: 2
  slug: boomi-repositoryinput
- name: SingleMessageRequest
  property_count: 0
  slug: boomi-singlemessagerequest
- name: Source
  property_count: 4
  slug: boomi-source
- name: SourceInput
  property_count: 2
  slug: boomi-sourceinput
json_structures:
- name: Boomi Structure
  property_count: 0
  slug: boomi-structure
jsonld:
- class_count: 0
  name: Boomi Context
  property_count: 11
  slug: boomi-context
layout: provider
modified: '2026-05-19'
name: Boomi
nav: Providers
network: true
overview: 'Boomi publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Atoms API, Components API, Deployments API, and 9 more. Tagged areas include AI Agents, Automation, B2B, Data Integration, and EDI.


  The Boomi catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Boomi''s developer surface includes authentication, GitHub presence, pricing, engineering blog, training material, documentation, support, and 69 more developer resources.'
plans:
- name: Boomi Plans Pricing
  plan_count: 9
  slug: boomi-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 6
  name: Boomi Rate Limits
  slug: boomi-rate-limits
rules:
- name: Boomi API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: boomi-asyncapi-spectral-rules
- name: Boomi API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: boomi-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 72.4
  delta: 0.0
  facets:
    commercial_clarity: 100.0
    contract_quality: 85.3
    developer_ergonomics: 45.7
    discoverability: 59.3
    governance: 47.9
    operational_transparency: 78.9
  previous_composite: 72.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boomi/refs/heads/main/screenshots/boomi-2026-06-20T173607.png
security:
- kind: authentication
  name: Boomi Authentication
  slug: boomi-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Boomi Domain Security
  slug: boomi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: boomi
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
use_cases:
- features:
  - Sales Order Processing
  - Invoice Management
  - Revenue Recognition
  - Accounts Receivable
  - Quote To Cash
  - Order Management
  name: Order-to-Cash
  url: https://boomi.com/solutions/
- features:
  - Procurement Integration
  - Purchase Orders
  - Supplier Management
  - Accounts Payable
  - Spend Management
  - Vendor Onboarding
  name: Source-to-Pay
  url: https://boomi.com/solutions/
- features:
  - HR Integration
  - Employee Onboarding
  - Offboarding
  - Payroll Integration
  - Workforce Management
  - HCM Integration
  name: Hire-to-Retire
  url: https://boomi.com/solutions/
- features:
  - COE
  - Integration Governance
  - Reusable Integration
  - Integration Standards
  - Platform Governance
  - Best Practices
  name: Integration Center of Excellence
  url: https://boomi.com/solutions/
- features:
  - AI Adoption
  - Generative AI
  - LLM Integration
  - AI Automation
  - AI Use Cases
  - Agentic AI
  name: Practical AI
  url: https://boomi.com/solutions/
- features:
  - Customer Data Integration
  - CRM Integration
  - Unified Customer Profile
  - Data Unification
  - Customer Insights
  - Omnichannel Data
  name: Customer 360
  url: https://boomi.com/solutions/
- features:
  - Merger Integration
  - System Consolidation
  - Divestiture
  - Application Rationalization
  - Post-Merger Integration
  - IT Integration
  name: M&A and Divestiture
  url: https://boomi.com/solutions/
- features:
  - ERP Migration
  - SAP Migration
  - ERP Integration
  - Legacy ERP
  - Cloud ERP
  - S/4HANA Migration
  name: ERP Modernization
  url: https://boomi.com/solutions/
- features:
  - Cloud Migration
  - Hybrid Integration
  - On-Premises To Cloud
  - Multi-Cloud Connectivity
  - Lift And Shift
  - Cloud-Native Integration
  name: Cloud Migration Connectivity
  url: https://boomi.com/solutions/
- features:
  - Mainframe Integration
  - Legacy System Connectivity
  - Application Modernization
  - Technical Debt Reduction
  - API Enablement
  - System Replacement
  name: Legacy Modernization
  url: https://boomi.com/solutions/
- features:
  - Supply Chain Integration
  - IoT Integration
  - Shop Floor Connectivity
  - MES Integration
  - Industry 4.0
  - ERP To MES
  name: Manufacturing
  url: https://boomi.com/solutions/
- features:
  - HL7
  - FHIR
  - EHR Integration
  - Patient Data Integration
  - Clinical Data Exchange
  - Healthcare Interoperability
  name: Healthcare and Life Sciences
  url: https://boomi.com/solutions/
- features:
  - POS Integration
  - Inventory Management
  - Omnichannel
  - E-Commerce Integration
  - Order Management
  - Supplier Integration
  name: Retail
  url: https://boomi.com/solutions/
- features:
  - Core Banking Integration
  - Payments Integration
  - Regulatory Compliance
  - FinTech Connectivity
  - Risk Data Integration
  - Open Banking
  name: Financial Services
  url: https://boomi.com/solutions/
- features:
  - Student Information Systems
  - LMS Integration
  - Campus Integration
  - SIS Connectivity
  - Enrollment Management
  - Research Data Integration
  name: Higher Education
  url: https://boomi.com/solutions/
- features:
  - Government Integration
  - Citizen Services
  - FISMA Compliance
  - FedRAMP
  - Agency Data Sharing
  - Digital Government
  name: Public Sector
  url: https://boomi.com/solutions/
website: https://boomi.com/
---
