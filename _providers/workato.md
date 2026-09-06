---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 40
  human_in_the_loop: 5
  name: Workato Agentic Access
  operation_count: 60
  slug: workato-agentic-access
  summary_line: 60 operations · 40 acting · 5 human-in-the-loop
api_count: 4
apis:
- description: The Workato Embedded Partner APIs enable partners to programmatically create and manage customers, recipes, connections, and other assets within the Workato Embedded platform. These APIs support provi
  name: Workato Embedded Partner API
  slug: embedded-api
- baseURL: https://www.workato.com
  baseurl_source: spec
  description: Data tables are structured storage within Workato for persisting and querying records used in recipe automation.
  name: Workato Data Tables API
  slug: workato-data-tables-api
- baseURL: https://www.workato.com
  baseurl_source: spec
  description: AI agents (genies) that can be configured with skills, knowledge bases, and instructions to automate complex workflows.
  name: Workato Genies API
  slug: workato-genies-api
- baseURL: https://www.workato.com
  baseurl_source: spec
  description: Knowledge bases provide AI agents with contextual data from configured data sources such as documents, tables, and external systems.
  name: Workato Knowledge Bases API
  slug: workato-knowledge-bases-api
- baseURL: https://www.workato.com
  baseurl_source: spec
  description: MCP servers expose Workato API endpoints as tools accessible to AI agents via the Model Context Protocol.
  name: Workato MCP Servers API
  slug: workato-mcp-servers-api
- baseURL: https://event-streams.workato.com
  baseurl_source: spec
  description: Endpoints for publishing messages to event topics and consuming messages from event topics.
  name: Workato Messages API
  slug: workato-messages-api
- baseURL: https://www.workato.com
  baseurl_source: spec
  description: Security policies that govern rate limits, quotas, and IP access controls for MCP servers.
  name: Workato Policies API
  slug: workato-policies-api
- baseURL: https://www.workato.com
  baseurl_source: spec
  description: Recipes are automated workflows that connect applications and services. Manage recipe lifecycle including creation, activation, and versioning.
  name: Workato Recipes API
  slug: workato-recipes-api
- baseURL: https://www.workato.com
  baseurl_source: spec
  description: Skills are recipe-backed capabilities that can be assigned to AI agents to give them actionable tools.
  name: Workato Skills API
  slug: workato-skills-api
- baseURL: https://www.workato.com
  baseurl_source: spec
  description: Tools are individual API endpoints or actions exposed through an MCP server and available to AI agents.
  name: Workato Tools API
  slug: workato-tools-api
- baseURL: https://www.workato.com
  baseurl_source: spec
  description: Identity provider user groups used to control access to MCP servers.
  name: Workato User Groups API
  slug: workato-user-groups-api
arazzos:
- description: Publish a batch of messages to a topic, then consume them back.
  name: Workato Batch Publish Events and Drain the Topic
  slug: workato-batch-publish-events-workflow
- description: Create a genie, confirm it, and start it so it can handle requests.
  name: Workato Build and Launch an AI Agent
  slug: workato-build-and-launch-genie-workflow
- description: Find running recipes in a folder and stop the first match.
  name: Workato Stop the First Running Recipe in a Folder
  slug: workato-bulk-stop-recipes-in-folder-workflow
- description: Duplicate an existing recipe and bring the copy online.
  name: Workato Clone and Activate a Recipe
  slug: workato-clone-and-activate-recipe-workflow
- description: Refine a tool's description on an MCP server, or remove it.
  name: Workato Curate an MCP Server's Tools
  slug: workato-curate-mcp-server-tool-workflow
- description: Stop a genie if running, then permanently delete it.
  name: Workato Decommission an AI Agent
  slug: workato-decommission-genie-workflow
- description: Create a knowledge base and attach it to an AI agent for context.
  name: Workato Equip a Genie with a Knowledge Base
  slug: workato-equip-genie-with-knowledge-base-workflow
- description: Create a data table with a schema and confirm it was provisioned.
  name: Workato Provision a Data Table
  slug: workato-provision-data-table-workflow
- description: Create an MCP server, assign tools, and confirm the tool list.
  name: Workato Provision an MCP Server with Tools
  slug: workato-provision-mcp-server-with-tools-workflow
- description: Publish a message to a topic, then long-poll to consume it back.
  name: Workato Publish and Verify an Event Message
  slug: workato-publish-and-consume-event-workflow
- description: Convert an existing recipe into a skill and assign it to an AI agent.
  name: Workato Turn a Recipe into a Genie Skill
  slug: workato-recipe-to-genie-skill-workflow
- description: Review a recipe's version history and restore an earlier version's code.
  name: Workato Inspect and Roll Back a Recipe Version
  slug: workato-recipe-version-rollback-workflow
- description: Truncate a data table's records, then update its schema in place.
  name: Workato Reset a Data Table's Data and Schema
  slug: workato-reset-data-table-schema-workflow
- description: Find an MCP server by name and renew its authentication token.
  name: Workato Rotate an MCP Server Token
  slug: workato-rotate-mcp-server-token-workflow
- description: Apply security policies and grant a user group access to an MCP server.
  name: Workato Secure MCP Server Access
  slug: workato-secure-mcp-server-access-workflow
- description: Activate a recipe and confirm it is running and healthy.
  name: Workato Start a Recipe and Verify Its Health
  slug: workato-start-recipe-with-health-check-workflow
- description: Safely decommission a recipe by stopping it before deletion.
  name: Workato Stop and Delete a Recipe
  slug: workato-stop-and-delete-recipe-workflow
artifact_total: 190
asyncapis:
- description: Workato Event Streams provides a publish-subscribe messaging system within the Workato platform. Topics act as channels through which producers publish messages and consumers retrieve them. Event Stre
  name: Workato Event Streams
  slug: workato-event-streams-asyncapi
collections:
- collection_type: postman
  name: Workato Agent Studio API
  slug: postman-workato-agent-studio
- collection_type: postman
  name: Workato Developer API
  slug: postman-workato-developer-api
- collection_type: postman
  name: Workato Event Streams Public API
  slug: postman-workato-event-streams
- collection_type: postman
  name: Workato MCP Server API
  slug: postman-workato-mcp-server
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Workato Agent Studio API
  slug: open-workato-agent-studio
- collection_type: open
  name: Workato Agent Studio Data Tables API
  slug: open-workato-data-tables-api
- collection_type: open
  name: Workato Developer API
  slug: open-workato-developer-api
- collection_type: open
  name: Workato Event Streams Public API
  slug: open-workato-event-streams
- collection_type: open
  name: Workato Agent Studio Data Tables Genies API
  slug: open-workato-genies-api
- collection_type: open
  name: Workato Agent Studio Data Tables Knowledge Bases API
  slug: open-workato-knowledge-bases-api
- collection_type: open
  name: Workato MCP Server API
  slug: open-workato-mcp-server
- collection_type: open
  name: Workato Agent Studio Data Tables MCP Servers API
  slug: open-workato-mcp-servers-api
- collection_type: open
  name: Workato Agent Studio Data Tables Messages API
  slug: open-workato-messages-api
- collection_type: open
  name: Workato Agent Studio Data Tables Policies API
  slug: open-workato-policies-api
- collection_type: open
  name: Workato Agent Studio Data Tables Recipes API
  slug: open-workato-recipes-api
- collection_type: open
  name: Workato Agent Studio Data Tables Skills API
  slug: open-workato-skills-api
- collection_type: open
  name: Workato Agent Studio Data Tables Tools API
  slug: open-workato-tools-api
- collection_type: open
  name: Workato Agent Studio Data Tables User Groups API
  slug: open-workato-user-groups-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/workato-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workato-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workato-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workato-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/workato/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-batch-publish-events-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-build-and-launch-genie-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-bulk-stop-recipes-in-folder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-clone-and-activate-recipe-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-curate-mcp-server-tool-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-decommission-genie-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-equip-genie-with-knowledge-base-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-provision-data-table-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-provision-mcp-server-with-tools-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-publish-and-consume-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-recipe-to-genie-skill-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-recipe-version-rollback-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-reset-data-table-schema-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-rotate-mcp-server-token-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-secure-mcp-server-access-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-start-recipe-with-health-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workato-stop-and-delete-recipe-workflow.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/workato
- group: commercial
  title: ''
  type: Pricing
  url: https://www.workato.com/pricing
- group: auth
  title: ''
  type: Security
  url: https://www.workato.com/platform/security
- group: other
  title: ''
  type: Resources
  url: https://www.workato.com/resources
- group: company
  title: ''
  type: Blog
  url: https://www.workato.com/the-connector/
- group: other
  title: ''
  type: ' WhatsNew'
  url: https://www.workato.com/product-hub/whats-new/
- group: other
  title: ''
  type: ' WhatsNew'
  url: https://www.workato.com/product-hub/whats-new/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.workato.com/product-hub/changelog/
- group: other
  title: ''
  type: Customers
  url: https://www.workato.com/the-connector/category/customer-stories/americas/
- group: company
  title: ''
  type: Partners
  url: https://partners.workato.com/consultants
- group: start
  title: ''
  type: Portal
  url: https://docs.workato.com/en/
- group: start
  title: ''
  type: Portal
  url: https://docs.workato.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.workato.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workato.com/legal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workato.com/legal/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://www.workato.com/legal/security
- group: company
  title: ''
  type: About
  url: https://www.workato.com/about_us
- group: company
  title: ''
  type: Website
  url: https://www.workato.com/
- group: start
  title: ''
  type: Login
  url: https://app.workato.com/users/sign_in?_gl=1*191kgyn*_gcl_au*MjA2NDIyNDEyNS4xNzQ5MTM5OTgw
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.workato.com/en/workato-api.html#http-response-codes
- group: docs
  title: ''
  type: Documentation
  url: https://docs.workato.com/en/mcp.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.workato.com/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.workato.com/workato-api/authentication.html
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.workato.com/workato-api/rate-limiting.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workato.com/
- group: operate
  title: ''
  type: Community
  url: https://community.workato.com/
- group: operate
  title: ''
  type: Support
  url: https://support.workato.com/
- group: start
  title: ''
  type: Signup
  url: https://www.workato.com/users/sign_up
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/workato/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/workato
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/workato
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/workato/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/workatohq/
- group: learn
  title: ''
  type: Academy
  url: https://academy.workato.com/
- group: auth
  title: ''
  type: Certification
  url: https://www.workato.com/certification
- group: operate
  title: ''
  type: Forums
  url: https://systematic.workato.com/
- group: other
  title: ''
  type: Events
  url: https://www.workato.com/events
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.workato.com/
- group: company
  title: ''
  type: Press
  url: https://www.workato.com/press
- group: company
  title: ''
  type: Careers
  url: https://www.workato.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.workato.com/request_demo
- group: other
  title: ''
  type: Product
  url: https://www.workato.com/embed-saas-integrations
- group: docs
  title: ''
  type: Documentation
  url: https://docs.workato.com/on-prem.html
- group: build
  title: ''
  type: SDKs
  url: https://docs.workato.com/developing-connectors/sdk.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.workato.com/api-management.html
- group: start
  title: ''
  type: Portal
  url: https://docs.workato.com/api-mgmt/api-developer-portal.html
- group: company
  title: ''
  type: Partners
  url: https://partners.workato.com/
- group: other
  title: ''
  type: Events
  url: https://www.workato.com/events/automate
- group: design
  title: ''
  type: JSONLD
  url: json-ld/workato-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workato-recipe-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workato-genie-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workato-developer-api-recipe-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workato-developer-api-data-table-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workato-agent-studio-genie-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workato-agent-studio-skill-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workato-agent-studio-knowledge-base-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workato-event-streams-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workato-mcp-server-mcp-server-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workato-mcp-server-tool-schema.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/workato-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/workato-vocabulary.yml
created: '2025-06-05T00:00:00.000Z'
description: Workato is an enterprise automation and integration platform that enables organizations to integrate their apps and automate business workflows without extensive coding. It provides a low-code/no-code interface for creating integrations between cloud applications, on-premises systems, and databases. The platform now layers Enterprise MCP, Workato Genies AI agents, Agent Studio, and Workato Embedded on top of its iPaaS foundation, with API Edge Gateway for on-premises deployment and RBAC 2.0 with environment- and project-scoped roles.
examples:
- key_count: 4
  name: Workato Agent Studio Data Source Example
  slug: workato-agent-studio-data-source-example
- key_count: 9
  name: Workato Agent Studio Genie Example
  slug: workato-agent-studio-genie-example
- key_count: 8
  name: Workato Agent Studio Genie Input Example
  slug: workato-agent-studio-genie-input-example
- key_count: 8
  name: Workato Agent Studio Knowledge Base Example
  slug: workato-agent-studio-knowledge-base-example
- key_count: 5
  name: Workato Agent Studio Knowledge Base Input Example
  slug: workato-agent-studio-knowledge-base-input-example
- key_count: 7
  name: Workato Agent Studio Skill Example
  slug: workato-agent-studio-skill-example
- key_count: 2
  name: Workato Agent Studio User Group Example
  slug: workato-agent-studio-user-group-example
- key_count: 4
  name: Workato Developer Api Data Table Column Example
  slug: workato-developer-api-data-table-column-example
- key_count: 6
  name: Workato Developer Api Data Table Example
  slug: workato-developer-api-data-table-example
- key_count: 3
  name: Workato Developer Api Data Table Input Example
  slug: workato-developer-api-data-table-input-example
- key_count: 11
  name: Workato Developer Api Recipe Example
  slug: workato-developer-api-recipe-example
- key_count: 1
  name: Workato Developer Api Recipe Input Example
  slug: workato-developer-api-recipe-input-example
- key_count: 4
  name: Workato Developer Api Recipe Version Example
  slug: workato-developer-api-recipe-version-example
- key_count: 1
  name: Workato Event Streams Batch Publish Request Example
  slug: workato-event-streams-batch-publish-request-example
- key_count: 2
  name: Workato Event Streams Batch Publish Response Example
  slug: workato-event-streams-batch-publish-response-example
- key_count: 4
  name: Workato Event Streams Consume Request Example
  slug: workato-event-streams-consume-request-example
- key_count: 1
  name: Workato Event Streams Consume Response Example
  slug: workato-event-streams-consume-response-example
- key_count: 3
  name: Workato Event Streams Message Example
  slug: workato-event-streams-message-example
- key_count: 1
  name: Workato Event Streams Publish Response Example
  slug: workato-event-streams-publish-response-example
- key_count: 15
  name: Workato Genie Example
  slug: workato-genie-example
- key_count: 7
  name: Workato Mcp Server Mcp Server Example
  slug: workato-mcp-server-mcp-server-example
- key_count: 3
  name: Workato Mcp Server Mcp Server Input Example
  slug: workato-mcp-server-mcp-server-input-example
- key_count: 4
  name: Workato Mcp Server Server Policy Example
  slug: workato-mcp-server-server-policy-example
- key_count: 4
  name: Workato Mcp Server Tool Example
  slug: workato-mcp-server-tool-example
- key_count: 2
  name: Workato Mcp Server User Group Example
  slug: workato-mcp-server-user-group-example
- key_count: 17
  name: Workato Recipe Example
  slug: workato-recipe-example
features:
- Base Workspace from ~$10K/year
- 'Typical mid-market: $15K-$50K/year'
- Cost based on recipes + tasks + connectors + user seats
- High-Volume Recipes (HVR) flat-rate option
- 'Enterprise: on-prem agent, dedicated support'
- 1,200+ pre-built connectors
- Recipes (workflows) and Tasks (actions)
- Workbot for chat-driven automation
- Embedded iPaaS for SaaS vendors
- AI Copilot for recipe generation
- RecipeIQ for performance tuning
- 'Recipe API trigger: 6,000 req/min/recipe'
- 'Concurrent runtime: 100 per workspace'
- Connector SDK for custom integrations
- SOC 2 Type 2 + HIPAA + GDPR compliant
- On-prem agent for behind-the-firewall systems
finops:
- name: Workato Finops
  service_category: iPaaS
  slug: workato-finops
graphqls:
- description: ''
  name: Workato GraphQL API
  slug: workato-graphql
image: https://www.workato.com/wp-content/uploads/2023/01/workato-logo.svg
integrations:
- features:
  - Salesforce
  - CRM
  - Lead Management
  - Order-To-Cash
  - Sales Automation
  - Data Synchronization
  - Workflow Automation
  name: Salesforce
  url: https://www.workato.com/integrations/salesforce
- features:
  - Slack
  - Team Messaging
  - Approval Workflows
  - ChatOps
  - Notifications
  - Workbot
  - Collaboration
  name: Slack
  url: https://www.workato.com/integrations/slack
- features:
  - Marketo
  - Marketing Automation
  - Lead Management
  - Lead Scoring
  - Campaign Management
  - Sales Alignment
  - Demand Generation
  name: Marketo
  url: https://www.workato.com/integrations/marketo
- features:
  - NetSuite
  - ERP
  - Financial Management
  - Record Management
  - SuiteQL
  - Order Management
  - Enterprise Resource Planning
  name: NetSuite REST
  url: https://www.workato.com/integrations/netsuite_rest
- features:
  - Google Drive
  - Cloud Storage
  - File Management
  - Document Automation
  - Sales Enablement
  - Folder Monitoring
  - Google Workspace
  name: Google Drive
  url: https://www.workato.com/integrations/google_drive
- features:
  - Workday
  - HRIS
  - Employee Onboarding
  - Offboarding
  - Recruiting Automation
  - HR Workflows
  - Payroll
  name: Workday
  url: https://www.workato.com/integrations/workday
- features:
  - ServiceNow
  - ITSM
  - Incident Management
  - IT Operations
  - Help Desk
  - Employee Onboarding
  - Ticket Routing
  name: ServiceNow
  url: https://www.workato.com/integrations/service_now
- features:
  - Snowflake
  - Data Warehouse
  - Data Synchronization
  - SQL Queries
  - Data Consolidation
  - Analytics
  - Cloud Database
  name: Snowflake
  url: https://www.workato.com/integrations/snowflake
- features:
  - Zendesk
  - Customer Support
  - Ticket Management
  - Help Desk
  - Cross-System Routing
  - Notifications
  - CRM Integration
  name: Zendesk
  url: https://www.workato.com/integrations/zendesk
- features:
  - Jira
  - Project Management
  - DevOps Automation
  - Issue Tracking
  - Support Escalation
  - Agile Workflows
  - ChatOps
  name: Jira
  url: https://www.workato.com/integrations/jira
- features:
  - OpenAI
  - Artificial Intelligence
  - Text Analysis
  - Content Generation
  - Image Processing
  - Language Translation
  - AI Automation
  name: OpenAI
  url: https://www.workato.com/integrations/open_ai
- features:
  - DeepSeek
  - Artificial Intelligence
  - Chat Completion
  - Large Language Model
  - AI Automation
  - Model Integration
  - Generative AI
  name: DeepSeek
  url: https://www.workato.com/integrations/deepseek
- features:
  - Google Gemini
  - Artificial Intelligence
  - Text Analysis
  - Content Generation
  - Image Analysis
  - Language Translation
  - Google AI
  name: Google Gemini
  url: https://www.workato.com/integrations/google-gemini
- features:
  - AWS Bedrock
  - Amazon Web Services
  - Foundation Models
  - Text Generation
  - Image Generation
  - AI Automation
  - Cloud AI
  name: AWS Bedrock
  url: https://www.workato.com/integrations/aws-bedrock
- features:
  - Azure OpenAI
  - Microsoft Azure
  - Artificial Intelligence
  - Text Analysis
  - Content Generation
  - Language Translation
  - Enterprise AI
  name: Azure OpenAI
  url: https://www.workato.com/integrations/azure_open_ai
- features:
  - Amazon S3
  - Cloud Storage
  - File Management
  - Data Consolidation
  - AWS
  - Object Storage
  - Data Pipeline
  name: Amazon S3
  url: https://www.workato.com/integrations/amazon_s3
- features:
  - Amazon Redshift
  - Data Warehouse
  - Cloud Analytics
  - Data Centralization
  - SQL
  - AWS
  - Business Intelligence
  name: Amazon Redshift
  url: https://www.workato.com/integrations/redshift
- features:
  - Azure Blob Storage
  - Microsoft Azure
  - Cloud Storage
  - File Management
  - Blob Management
  - Event Triggers
  - Data Pipeline
  name: Azure Blob Storage
  url: https://www.workato.com/integrations/azure_blob_storage
- features:
  - MongoDB
  - NoSQL Database
  - Document Management
  - Data Synchronization
  - Cloud Database
  - Atlas
  - Data Replication
  name: MongoDB Atlas
  url: https://www.workato.com/integrations/mongodb
- features:
  - PostgreSQL
  - Relational Database
  - Data Migration
  - SQL Queries
  - Data Pipeline
  - Backup Automation
  - Data Warehouse Integration
  name: PostgreSQL
  url: https://www.workato.com/integrations/postgresql
- features:
  - Microsoft SQL Server
  - Relational Database
  - SQL
  - Data Integration
  - Enterprise Database
  - Workflow Automation
  - Data Synchronization
  name: Microsoft SQL Server
  url: https://www.workato.com/integrations/microsoftsqlserver
json_schemas:
- name: DataSource
  property_count: 4
  slug: workato-agent-studio-data-source
- name: GenieInput
  property_count: 8
  slug: workato-agent-studio-genie-input
- name: Genie
  property_count: 9
  slug: workato-agent-studio-genie
- name: KnowledgeBaseInput
  property_count: 5
  slug: workato-agent-studio-knowledge-base-input
- name: KnowledgeBase
  property_count: 8
  slug: workato-agent-studio-knowledge-base
- name: Skill
  property_count: 7
  slug: workato-agent-studio-skill
- name: UserGroup
  property_count: 2
  slug: workato-agent-studio-user-group
- name: DataTableColumn
  property_count: 4
  slug: workato-developer-api-data-table-column
- name: DataTableInput
  property_count: 3
  slug: workato-developer-api-data-table-input
- name: DataTable
  property_count: 6
  slug: workato-developer-api-data-table
- name: RecipeInput
  property_count: 1
  slug: workato-developer-api-recipe-input
- name: Recipe
  property_count: 11
  slug: workato-developer-api-recipe
- name: RecipeVersion
  property_count: 4
  slug: workato-developer-api-recipe-version
- name: BatchPublishRequest
  property_count: 1
  slug: workato-event-streams-batch-publish-request
- name: BatchPublishResponse
  property_count: 2
  slug: workato-event-streams-batch-publish-response
- name: ConsumeRequest
  property_count: 4
  slug: workato-event-streams-consume-request
- name: ConsumeResponse
  property_count: 1
  slug: workato-event-streams-consume-response
- name: Message
  property_count: 3
  slug: workato-event-streams-message
- name: PublishResponse
  property_count: 1
  slug: workato-event-streams-publish-response
- name: Workato Genie
  property_count: 15
  slug: workato-genie
- name: McpServerInput
  property_count: 3
  slug: workato-mcp-server-mcp-server-input
- name: McpServer
  property_count: 7
  slug: workato-mcp-server-mcp-server
- name: ServerPolicy
  property_count: 4
  slug: workato-mcp-server-server-policy
- name: Tool
  property_count: 4
  slug: workato-mcp-server-tool
- name: UserGroup
  property_count: 2
  slug: workato-mcp-server-user-group
- name: Workato Recipe
  property_count: 17
  slug: workato-recipe
json_structures:
- name: Workato Agent Studio Data Source Structure
  property_count: 4
  slug: workato-agent-studio-data-source-structure
- name: Workato Agent Studio Genie Input Structure
  property_count: 8
  slug: workato-agent-studio-genie-input-structure
- name: Workato Agent Studio Genie Structure
  property_count: 9
  slug: workato-agent-studio-genie-structure
- name: Workato Agent Studio Knowledge Base Input Structure
  property_count: 5
  slug: workato-agent-studio-knowledge-base-input-structure
- name: Workato Agent Studio Knowledge Base Structure
  property_count: 8
  slug: workato-agent-studio-knowledge-base-structure
- name: Workato Agent Studio Skill Structure
  property_count: 7
  slug: workato-agent-studio-skill-structure
- name: Workato Agent Studio User Group Structure
  property_count: 2
  slug: workato-agent-studio-user-group-structure
- name: Workato Developer Api Data Table Column Structure
  property_count: 4
  slug: workato-developer-api-data-table-column-structure
- name: Workato Developer Api Data Table Input Structure
  property_count: 3
  slug: workato-developer-api-data-table-input-structure
- name: Workato Developer Api Data Table Structure
  property_count: 6
  slug: workato-developer-api-data-table-structure
- name: Workato Developer Api Recipe Input Structure
  property_count: 1
  slug: workato-developer-api-recipe-input-structure
- name: Workato Developer Api Recipe Structure
  property_count: 11
  slug: workato-developer-api-recipe-structure
- name: Workato Developer Api Recipe Version Structure
  property_count: 4
  slug: workato-developer-api-recipe-version-structure
- name: Workato Event Streams Batch Publish Request Structure
  property_count: 1
  slug: workato-event-streams-batch-publish-request-structure
- name: Workato Event Streams Batch Publish Response Structure
  property_count: 2
  slug: workato-event-streams-batch-publish-response-structure
- name: Workato Event Streams Consume Request Structure
  property_count: 4
  slug: workato-event-streams-consume-request-structure
- name: Workato Event Streams Consume Response Structure
  property_count: 1
  slug: workato-event-streams-consume-response-structure
- name: Workato Event Streams Message Structure
  property_count: 3
  slug: workato-event-streams-message-structure
- name: Workato Event Streams Publish Response Structure
  property_count: 1
  slug: workato-event-streams-publish-response-structure
- name: Workato Genie Structure
  property_count: 15
  slug: workato-genie-structure
- name: Workato Mcp Server Mcp Server Input Structure
  property_count: 3
  slug: workato-mcp-server-mcp-server-input-structure
- name: Workato Mcp Server Mcp Server Structure
  property_count: 7
  slug: workato-mcp-server-mcp-server-structure
- name: Workato Mcp Server Server Policy Structure
  property_count: 4
  slug: workato-mcp-server-server-policy-structure
- name: Workato Mcp Server Tool Structure
  property_count: 4
  slug: workato-mcp-server-tool-structure
- name: Workato Mcp Server User Group Structure
  property_count: 2
  slug: workato-mcp-server-user-group-structure
- name: Workato Recipe Structure
  property_count: 17
  slug: workato-recipe-structure
jsonld:
- class_count: 25
  name: Workato Context
  property_count: 56
  slug: workato-context
layout: provider
modified: '2026-05-22'
name: Workato
nav: Providers
network: true
overview: 'Workato publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Data Tables API, Genies API, Knowledge Bases API, and 7 more. Tagged areas include Agentic, API Management, Automation, B2B, and Embedded iPaaS.


  The Workato catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Workato''s developer surface includes authentication, pricing, engineering blog, changelog, developer portal, documentation, support, and 76 more developer resources.'
plans:
- name: Workato Plans Pricing
  plan_count: 4
  slug: workato-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 6
  name: Workato Rate Limits
  slug: workato-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Workato API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: workato-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Workato API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: workato-jsonschema-spectral-rules
- effective_rule_count: 84
  extends:
  - spectral:oas
  name: Workato API Rules
  rule_count: 43
  severity_counts:
    error: 12
    hint: 0
    info: 8
    warn: 23
  slug: workato-spectral-rules
score:
  band: strong
  composite: 63.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 71.5
    catalog_earned_first_party: 0.0
    catalog_gap: 43.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 28.8
    contract_quality: 83.1
    developer_ergonomics: 63.1
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 55.3
  previous_composite: 63.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workato/refs/heads/main/screenshots/workato-2026-06-20T201551.png
security:
- kind: authentication
  name: Workato Authentication
  slug: workato-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Workato Domain Security
  slug: workato-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: workato
tags:
- Agentic
- API Management
- Automation
- B2B
- Embedded iPaaS
- Enterprise
- Integration
- iPaaS
- Orchestration
- Workflows
use_cases:
- features:
  - Order To Cash
  - ERP Integration
  - CRM Automation
  - Invoice Processing
  - Revenue Operations
  - Deal Desk Automation
  - Days Sales Outstanding
  name: Order-to-Cash
  url: https://www.workato.com/use_cases/order_to_cash
- features:
  - Employee Onboarding
  - HR Automation
  - ATS Integration
  - HRIS Integration
  - Application Provisioning
  - Talent Acquisition
  - Workflow Automation
  name: Employee Onboarding
  url: https://www.workato.com/use_cases/employee_onboarding
- features:
  - Product Led Sales
  - Customer 360
  - Reverse ETL
  - Go-To-Market Automation
  - Sales Signals
  - Data Synchronization
  - Revenue Operations
  name: Product-Led Sales
  url: https://www.workato.com/use_cases/product_led_sales
- features:
  - IT Automation
  - Incident Management
  - Help Desk
  - Employee Onboarding
  - ChatOps
  - Access Management
  - Workflow Automation
  name: IT Automation
  url: https://www.workato.com/editions/it
- features:
  - Finance Automation
  - Order To Cash
  - Accounts Payable
  - Financial Reporting
  - Month End Close
  - ERP Integration
  - Revenue Realization
  name: Finance Automation
  url: https://www.workato.com/editions/finance
- features:
  - HR Automation
  - Talent Acquisition
  - Employee Onboarding
  - People Operations
  - Offboarding
  - Workday Integration
  - Workflow Automation
  name: HR Automation
  url: https://www.workato.com/editions/hr
- features:
  - Sales Automation
  - Lead To Opportunity
  - Deal Desk
  - Order To Cash
  - Account Management
  - CRM Integration
  - Pipeline Management
  name: Sales Automation
  url: https://www.workato.com/editions/sales
- features:
  - Marketing Automation
  - Campaign Operations
  - Lead Management
  - Data Orchestration
  - CRM Integration
  - Demand Generation
  - Customer Journey
  name: Marketing Operations
  url: https://www.workato.com/editions/marketing
- features:
  - Support Automation
  - Customer Experience
  - Ticket Management
  - Churn Prevention
  - Customer Intelligence
  - Mean Time To Resolution
  - AI Powered Support
  name: Support Automation
  url: https://www.workato.com/editions/support
- features:
  - Revenue Operations
  - Pipeline Generation
  - Deal Management
  - Customer Retention
  - Sales Operations
  - Marketing Operations
  - Customer Success
  name: Revenue Operations
  url: https://www.workato.com/revops
- features:
  - Manufacturing Automation
  - Supply Chain
  - Factory Automation
  - ERP Integration
  - Inventory Management
  - Workforce Productivity
  - Data Integration
  name: Manufacturing
  url: https://www.workato.com/industry/manufacturing
- features:
  - Financial Services
  - Banking Automation
  - KYC AML Compliance
  - Customer Onboarding
  - Claims Processing
  - Regulatory Reporting
  - AI Agents
  name: Financial Services
  url: https://www.workato.com/industry/financial_services
- features:
  - Retail Automation
  - Order Management
  - Inventory Synchronization
  - Supply Chain
  - EDI Integration
  - E-Commerce Integration
  - Omnichannel
  name: Retail
  url: https://www.workato.com/industry/retail
- features:
  - Logistics Automation
  - Supply Chain Visibility
  - Quote To Cash
  - Workforce Optimization
  - Green Logistics
  - Partner Portal Integration
  - Administrative Automation
  name: Logistics
  url: https://www.workato.com/industry/logistics
- features:
  - Healthcare Automation
  - Patient Data Integration
  - Compliance Automation
  - Interoperability
  - Value Based Care
  - Legacy System Integration
  - Regulatory Compliance
  name: Healthcare
  url: https://www.workato.com/industry/healthcare
- features:
  - Media Automation
  - Content Distribution
  - Hyper Personalization
  - Campaign Optimization
  - Media Production
  - Data Integration
  - Workflow Automation
  name: Media
  url: https://www.workato.com/industry/media
website: https://www.workato.com/
---
