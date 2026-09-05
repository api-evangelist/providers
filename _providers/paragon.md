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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Paragon Agentic Access
  operation_count: 33
  slug: paragon-agentic-access
  summary_line: 33 operations · 20 acting
api_count: 2
apis:
- baseURL: https://managed-sync.useparagon.com
  baseurl_source: spec
  description: ReBAC-style access checks over synced objects and subjects.
  name: Paragon Permissions API
  slug: paragon-permissions-api
- baseURL: https://managed-sync.useparagon.com
  baseurl_source: spec
  description: Enable, monitor, and read records from Managed Sync pipelines.
  name: Paragon Sync API
  slug: paragon-sync-api
- baseURL: https://actionkit.useparagon.com
  baseurl_source: spec
  description: List and execute ActionKit Integration Tools for AI agents and apps.
  name: Paragon Tools API
  slug: paragon-tools-api
arazzos:
- description: Find an enabled integration for a Connected User, disconnect it, then confirm it is gone.
  name: Paragon Disconnect a User Integration and Confirm
  slug: paragon-disconnect-integration-workflow
- description: List the Integration Tools available to a Connected User, then execute one synchronously.
  name: Paragon Discover and Run an ActionKit Action
  slug: paragon-discover-and-run-action-workflow
- description: Enable a Managed Sync pipeline, poll until it has run, then read the normalized records.
  name: Paragon Enable a Sync and Pull Records
  slug: paragon-enable-sync-and-pull-records-workflow
- description: Search Task History for failed executions, then replay the most recent failure.
  name: Paragon Find and Replay a Failed Workflow Execution
  slug: paragon-find-and-replay-failed-execution-workflow
- description: Look up a Connected User's subscriptions and branch to update or unsubscribe.
  name: Paragon Find and Manage a Trigger Subscription
  slug: paragon-manage-trigger-subscription-workflow
- description: Pull a synced record, check the requester's access, and download its file content only if allowed.
  name: Paragon Permissioned Synced Record Retrieval
  slug: paragon-permissioned-record-retrieval-workflow
- description: Resolve a trigger from the catalog, preview its example payload, then subscribe the user to it.
  name: Paragon Preview and Subscribe to a Trigger
  slug: paragon-subscribe-to-trigger-workflow
- description: Confirm the Connected User has the integration enabled, then proxy a live API call to it.
  name: Paragon Verify Integration then Proxy a Request
  slug: paragon-verify-integration-and-proxy-request-workflow
artifact_total: 234
collections:
- collection_type: postman
  name: Paragon ActionKit API
  slug: postman-paragon-actionkit-api
- collection_type: postman
  name: Paragon Managed Sync API
  slug: postman-paragon-managed-sync-api
- collection_type: postman
  name: Paragon Proxy API
  slug: postman-paragon-proxy-api
- collection_type: postman
  name: Paragon Task History API
  slug: postman-paragon-task-history-api
- collection_type: postman
  name: Paragon Triggers API
  slug: postman-paragon-triggers-api
- collection_type: postman
  name: Paragon Users API
  slug: postman-paragon-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Paragon ActionKit API
  slug: open-paragon-actionkit-api
- collection_type: open
  name: Paragon ActionKit Credentials API
  slug: open-paragon-credentials-api
- collection_type: open
  name: Paragon ActionKit Credentials Custom Integrations API
  slug: open-paragon-custom-integrations-api
- collection_type: open
  name: Paragon ActionKit Credentials Integrations API
  slug: open-paragon-integrations-api
- collection_type: open
  name: Paragon Managed Sync API
  slug: open-paragon-managed-sync-api
- collection_type: open
  name: Paragon ActionKit Credentials Permissions API
  slug: open-paragon-permissions-api
- collection_type: open
  name: Paragon ActionKit Credentials Proxy API
  slug: open-paragon-proxy-api
- collection_type: open
  name: Paragon ActionKit Credentials Sync API
  slug: open-paragon-sync-api
- collection_type: open
  name: Paragon ActionKit Credentials Task History API
  slug: open-paragon-task-history-api
- collection_type: open
  name: Paragon ActionKit Credentials Tools API
  slug: open-paragon-tools-api
- collection_type: open
  name: Paragon ActionKit Credentials Triggers API
  slug: open-paragon-triggers-api
- collection_type: open
  name: Paragon ActionKit Credentials Users API
  slug: open-paragon-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paragon-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/paragon-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paragon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paragon-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/paragon/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paragon-disconnect-integration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paragon-discover-and-run-action-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paragon-enable-sync-and-pull-records-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paragon-find-and-replay-failed-execution-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paragon-manage-trigger-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paragon-permissioned-record-retrieval-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paragon-subscribe-to-trigger-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paragon-verify-integration-and-proxy-request-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paragon
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/useparagon
- group: docs
  title: ''
  type: Documentation
  url: https://docs.useparagon.com/overview
- group: company
  title: ''
  type: Blog
  url: https://www.useparagon.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.useparagon.com/
- group: build
  title: ''
  type: SDKs
  url: https://docs.useparagon.com/getting-started/installing-the-connect-sdk
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@useparagon/connect
- group: auth
  title: ''
  type: Authentication
  url: https://docs.useparagon.com/connect-portal/overview
- group: design
  title: ''
  type: Webhooks
  url: https://docs.useparagon.com/resources/custom-webhooks
- group: other
  title: ''
  type: RBAC
  url: https://docs.useparagon.com/managing-account/role-based-access-control
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://docs.useparagon.com/billing/concurrency-limits
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paragon-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/paragon-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/paragon-finops.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.useparagon.com/security/security
- group: auth
  title: ''
  type: Trust
  url: https://security.useparagon.com/
- group: auth
  title: ''
  type: GDPR
  url: https://docs.useparagon.com/security/gdpr
- group: auth
  title: ''
  type: HIPAA
  url: https://docs.useparagon.com/security/hipaa
- group: operate
  title: ''
  type: Support
  url: https://docs.useparagon.com/support/contacting-support
- group: design
  title: ''
  type: Workflow
  url: https://docs.useparagon.com/workflows/overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.useparagon.com/changelog/product-updates
- group: start
  title: ''
  type: Signup
  url: https://dashboard.useparagon.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.useparagon.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.useparagon.com/terms-of-service
- group: other
  title: ''
  type: Customers
  url: https://www.useparagon.com/customers
- group: commercial
  title: ''
  type: Pricing
  url: https://www.useparagon.com/pricing
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/useparagon/paragon-mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/useparagon/paragon-ai-skills
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/useparagon/paragon-connect-nextjs-example
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/useparagon/connect-headless-example
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/useparagon/paragon-rails-example
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/useparagon/rag-tutorials
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/useparagon/actionkit-playground
- group: other
  title: ''
  type: Deployment
  url: https://github.com/useparagon/aws-on-prem
- group: other
  title: ''
  type: Deployment
  url: https://github.com/useparagon/enterprise-installer
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/paragon-vocabulary.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/paragon-rules.yml
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/paragon-action-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/paragon-synced-record-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/paragon-trigger-subscription-structure.json
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.useparagon.com/llms.txt
created: '2025-06-05T00:00:00.000Z'
description: Paragon is the Integration Infrastructure Platform for B2B SaaS and AI products. The platform combines Connect Portal (managed user authentication for 130+ SaaS apps), Workflows (event-driven async orchestration), ActionKit (Universal API + MCP server giving AI agents synchronous CRUD access to Integration Tools), Triggers (event subscriptions), Managed Sync (normalized RAG-grade data ingestion with a permissions graph), the Proxy API (direct passthrough to third-party APIs on behalf of Connected Users), the Users API, and the Task History API.
examples:
- key_count: 1
  name: Actionkit List Actions Example
  slug: actionkit-list-actions-example
- key_count: 4
  name: Actionkit Run Action Example
  slug: actionkit-run-action-example
- key_count: 2
  name: Managed Sync Pull Records Example
  slug: managed-sync-pull-records-example
- key_count: 2
  name: Permissions Check Access Example
  slug: permissions-check-access-example
- key_count: 2
  name: Proxy Request Example
  slug: proxy-request-example
- key_count: 3
  name: Task History Workflow Executions Example
  slug: task-history-workflow-executions-example
- key_count: 2
  name: Triggers Subscribe Example
  slug: triggers-subscribe-example
- key_count: 4
  name: Users Get User Example
  slug: users-get-user-example
features:
- 130+ pre-built integrations (Connect Portal)
- Fully managed authentication (OAuth 2.0, API Key, custom)
- Workflows — event-driven async orchestration
- ActionKit Universal API + MCP server for AI agents
- Triggers API (Beta) — event subscriptions across 130+ integrations
- Managed Sync — normalized File / CRM / Ticketing ingestion for RAG
- Permissions API — ReBAC-style access checks over synced objects
- Proxy API — direct passthrough to any provider API
- Users API — manage Connected User state and metadata
- Task History API — query historical executions (Enterprise; 1,000 req / 10 min)
- Connect API rate limit — 600 req/min/workspace
- ActionKit API rate limit — 50 req/sec/workspace
- Concurrency — 5 (Trial) / 20 (Pro) / up to 1,000 (Enterprise) step executions
- Embedded UX or Headless SDK
- Bring Your Own Connector (BYOC) / Custom Integrations
- Dynamic Field Mapping (Enterprise)
- SOC 2 Type 2 + GDPR + HIPAA-eligible deployment
- Self-host / forward-deploy on AWS (Enterprise)
finops:
- name: Paragon Finops
  service_category: Integration Infrastructure
  slug: paragon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paragon.png
integrations:
- name: ActiveCampaign
- name: Adobe Acrobat Sign
- name: Adobe Commerce
- name: Adobe Experience Manager
- name: ADP Workforce Now
- name: Airtable
- name: Amazon S3
- name: Amplitude
- name: Apollo.io
- name: Asana
- name: Azure DevOps
- name: BambooHR
- name: BigQuery
- name: Box
- name: Calendly
- name: Chorus.ai
- name: ClickUp
- name: Close
- name: Coda
- name: Confluence
- name: Contentful
- name: Copper
- name: DocuSign
- name: Dropbox
- name: Dropbox Sign
- name: Dynamics 365 Business Central
- name: Dynamics 365 Finance
- name: Emarsys
- name: Excel
- name: Facebook Ads
- name: Facebook Pages
- name: Figma
- name: Freshdesk
- name: Freshsales
- name: Front
- name: Gainsight
- name: GitHub
- name: Gmail
- name: Gong
- name: Google Ad Manager
- name: Google Ads
- name: Google Analytics
- name: Google Analytics GA4
- name: Google Calendar
- name: Google Campaign Manager
- name: Google Docs
- name: Google Drive
- name: Google Search Console
- name: Google Sheets
- name: Greenhouse
- name: Guru
- name: Gusto
- name: Heap
- name: Hive
- name: HubSpot
- name: iManage
- name: Insightly
- name: Intellum
- name: Intercom
- name: Jira
- name: Keap
- name: Klaviyo
- name: Lever
- name: Linear
- name: LinkedIn
- name: LinkedIn Marketing
- name: Magento
- name: Mailchimp
- name: Marketo
- name: Microsoft Dynamics 365 Sales
- name: Microsoft Outlook
- name: Microsoft SharePoint
- name: Microsoft Teams
- name: Miro
- name: Mixpanel
- name: monday.com
- name: NetSuite
- name: Notion
- name: OneDrive
- name: OneNote
- name: OpenAI
- name: Oracle Eloqua
- name: Oracle Financials Cloud
- name: Outreach
- name: PagerDuty
- name: PandaDoc
- name: Pardot
- name: Pipedrive
- name: Power BI
- name: Productboard
- name: QuickBooks
- name: Quip
- name: Ramp
- name: Sage Accounting
- name: Sage Intacct
- name: Sailthru
- name: Salesforce
- name: Salesloft
- name: SAP S/4HANA
- name: SAP SuccessFactors
- name: Segment
- name: ServiceNow
- name: Shopify
- name: Shortcut
- name: Slack
- name: Snowflake
- name: Stack Overflow for Teams
- name: Stripe
- name: Tableau
- name: TikTok Ads
- name: Todoist
- name: Trello
- name: Typeform
- name: Unleashed
- name: Vanta
- name: Vimeo
- name: WhatsApp
- name: WooCommerce
- name: WordPress
- name: Workable
- name: Workday
- name: Xero
- name: Zendesk
- name: Zendesk Sell
- name: Zoho CRM
- name: Zoho People
- name: Zoom
json_schemas:
- name: Paragon Permissions Access Check
  property_count: 3
  slug: access-check
- name: Paragon ActionKit Action
  property_count: 4
  slug: action
- name: Paragon Credential
  property_count: 3
  slug: credential
- name: Paragon Integration
  property_count: 5
  slug: integration
- name: AccessCheck
  property_count: 3
  slug: paragon-accesscheck
- name: Action
  property_count: 4
  slug: paragon-action
- name: ActionResult
  property_count: 3
  slug: paragon-actionresult
- name: Credential
  property_count: 3
  slug: paragon-credential
- name: Integration
  property_count: 5
  slug: paragon-integration
- name: SyncedRecord
  property_count: 7
  slug: paragon-syncedrecord
- name: SyncStatus
  property_count: 5
  slug: paragon-syncstatus
- name: Trigger
  property_count: 4
  slug: paragon-trigger
- name: TriggerSubscription
  property_count: 7
  slug: paragon-triggersubscription
- name: TriggerSubscriptionRequest
  property_count: 3
  slug: paragon-triggersubscriptionrequest
- name: User
  property_count: 4
  slug: paragon-user
- name: UserIntegration
  property_count: 3
  slug: paragon-userintegration
- name: WorkflowExecution
  property_count: 8
  slug: paragon-workflowexecution
- name: WorkflowExecutionList
  property_count: 3
  slug: paragon-workflowexecutionlist
- name: Paragon Sync Status
  property_count: 5
  slug: sync-status
- name: Paragon Managed Sync Record
  property_count: 7
  slug: synced-record
- name: Paragon Trigger Subscription
  property_count: 7
  slug: trigger-subscription
- name: Paragon Trigger
  property_count: 4
  slug: trigger
- name: Paragon Connected User
  property_count: 4
  slug: user
- name: Paragon Workflow Execution List
  property_count: 3
  slug: workflow-execution-list
- name: Paragon Workflow Execution
  property_count: 8
  slug: workflow-execution
json_structures:
- name: Paragon Action Structure
  property_count: 4
  slug: paragon-action-structure
- name: Paragon Structure
  property_count: 0
  slug: paragon-structure
- name: Paragon Synced Record Structure
  property_count: 7
  slug: paragon-synced-record-structure
- name: Paragon Trigger Subscription Structure
  property_count: 7
  slug: paragon-trigger-subscription-structure
jsonld:
- class_count: 0
  name: Paragon Context
  property_count: 13
  slug: paragon-context
layout: provider
mcp_servers:
- description: ''
  name: Paragon MCP Server
  slug: paragon-mcp-server
modified: '2026-05-22'
name: Paragon
nav: Providers
network: true
overview: 'Paragon publishes 3 APIs on the [APIs.io](https://apis.io/) network: Permissions API, Sync API, and Tools API. Tagged areas include Embedded Integrations, Integration Infrastructure, iPaaS, AI Agents, and MCP.


  The Paragon catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Paragon''s developer surface includes authentication, documentation, engineering blog, support, changelog, signup flow, pricing, and 47 more developer resources.'
plans:
- name: Paragon Plans Pricing
  plan_count: 3
  slug: paragon-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 6
  name: Paragon Rate Limits
  slug: paragon-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Paragon API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: paragon-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Paragon API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: paragon-rules
score:
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 68.5
    catalog_earned_first_party: 0.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 28.8
    contract_quality: 69.4
    developer_ergonomics: 44.0
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 63.2
  previous_composite: 56.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 80.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paragon/refs/heads/main/screenshots/paragon-2026-06-20T191356.png
security:
- kind: authentication
  name: Paragon Authentication
  slug: paragon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Paragon Domain Security
  slug: paragon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Paragon Trust Center
  slug: paragon-trust-center
  summary_line: GDPR
skill_count: 3
skills:
- name: paragon-actionkit-skill
  slug: paragon-actionkit-skill
- name: paragon-managed-sync-skill
  slug: paragon-managed-sync-skill
- name: paragon-setup-skill
  slug: paragon-setup-skill
slug: paragon
tags:
- Embedded Integrations
- Integration Infrastructure
- iPaaS
- AI Agents
- MCP
- Integration
use_cases:
- name: AI Agent Tool Calling (ActionKit + MCP)
- name: RAG Ingestion With Source Permissions (Managed Sync)
- name: Agentic Actions Across Integrations
- name: Embedded Workflow Builder Actions
- name: File Upload via 3rd-Party Picker
- name: Ingest All Files From File Storage
- name: Real-Time Bidirectional CRM Sync
- name: Send Slack / Teams Notifications
---
