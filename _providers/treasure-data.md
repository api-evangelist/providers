---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 235
  human_in_the_loop: 25
  name: Treasure Data Agentic Access
  operation_count: 440
  slug: treasure-data-agentic-access
  summary_line: 440 operations · 235 acting · 25 human-in-the-loop
api_count: 7
apis:
- description: REST API for configuring and managing bulk load sessions that import data from external sources into Treasure Data.
  name: Treasure Data Bulk Loads API
  slug: treasure-data-bulk-loads-api
- description: REST API for managing users, access control, and authentication within a Treasure Data account.
  name: Treasure Data User API
  slug: treasure-data-user-api
- description: REST API for checking server health and infrastructure status of the Treasure Data platform.
  name: Treasure Data System API
  slug: treasure-data-system-api
- description: JSON-based event ingestion API for submitting data records to Treasure Data from systems that cannot use the JavaScript SDK.
  name: Treasure Data Postback API
  slug: treasure-data-postback-api
- description: REST API for orchestrating and automating data workflows within the Treasure Data platform using Digdag-based workflow engine.
  name: Treasure Workflow API
  slug: treasure-workflow-api
- description: Bulk data import sessions
  name: Treasure Data Bulk Import API
  slug: treasure-data-bulk-import-api
- description: Bulk load sessions from external sources
  name: Treasure Data Bulk Loads API
  slug: treasure-data-bulk-loads-api
- description: Manage output connectors
  name: Treasure Data Connectors API
  slug: treasure-data-connectors-api
- description: Manage Treasure Data databases
  name: Treasure Data Databases API
  slug: treasure-data-databases-api
- description: Submit and manage query jobs
  name: Treasure Data Jobs API
  slug: treasure-data-jobs-api
- description: Identity federation and SSO settings
  name: Treasure Data SSO API
  slug: treasure-data-sso-api
- description: System health and status
  name: Treasure Data System API
  slug: treasure-data-system-api
- description: Manage tables within databases
  name: Treasure Data Tables API
  slug: treasure-data-tables-api
- description: User management
  name: Treasure Data Users API
  slug: treasure-data-users-api
- description: Treasure Workflow — the Digdag-based orchestration API. 43 operations over projects, workflow definitions, revisions, schedules, sessions, attempts, tasks, logs, secrets and resource pools.
  name: Treasure Workflow API
  slug: treasure-data-workflow-api
- description: JSON event ingestion endpoint used by the JavaScript, iOS, Android, React Native and Cordova SDKs for small, frequent payloads.
  name: Treasure Data Postback API
  slug: treasure-data-postback-api
- description: 'Two Model Context Protocol servers — the official @treasuredata/mcp-server (23 tools, local stdio, public preview) and a live remote documentation MCP endpoint on the docs host whose six tools return '
  name: Treasure Data MCP Servers
  slug: treasure-data-mcp
- description: The Access Control - Permissions API from Treasure Data — 2 operation(s) for access control - permissions.
  name: Treasure Data Access Control - Permissions API
  slug: treasure-data-access-control-permissions-api
- description: The Access Control - Policies API from Treasure Data — 5 operation(s) for access control - policies.
  name: Treasure Data Access Control - Policies API
  slug: treasure-data-access-control-policies-api
- description: The Access Control - Policy Groups API from Treasure Data — 3 operation(s) for access control - policy groups.
  name: Treasure Data Access Control - Policy Groups API
  slug: treasure-data-access-control-policy-groups-api
- description: The Access Control - Users API from Treasure Data — 6 operation(s) for access control - users.
  name: Treasure Data Access Control - Users API
  slug: treasure-data-access-control-users-api
- description: The Action API from Treasure Data — 2 operation(s) for action.
  name: Treasure Data Action API
  slug: treasure-data-action-api
- description: Marketers find creating an activation challenging because they have to enter technical information they might not understand, which can lead to activations failing due to misconfigurations. Treasure D
  name: Treasure Data Activation Templates API
  slug: treasure-data-activation-templates-api
- description: 'Activation is the process that allows marketers to personalize communication to users interested in your brand. <br> <ul> <li> **Funnel activation** &mdash; Create a funnel activation for each funnel '
  name: Treasure Data Activations API
  slug: treasure-data-activations-api
- description: The Agent API from Treasure Data — 2 operation(s) for agent.
  name: Treasure Data Agent API
  slug: treasure-data-agent-api
- description: The AgentSchedule API from Treasure Data — 4 operation(s) for agentschedule.
  name: Treasure Data Agent Schedule API
  slug: treasure-data-agentschedule-api
- description: The Artifact API from Treasure Data — 1 operation(s) for artifact.
  name: Treasure Data Artifact API
  slug: treasure-data-artifact-api
- description: The Attempt API from Treasure Data — 5 operation(s) for attempt.
  name: Treasure Data Attempt API
  slug: treasure-data-attempt-api
- description: The Chat API from Treasure Data — 5 operation(s) for chat.
  name: Treasure Data Chat API
  slug: treasure-data-chat-api
- description: The ChatAttachment API from Treasure Data — 2 operation(s) for chatattachment.
  name: Treasure Data Chat Attachment API
  slug: treasure-data-chatattachment-api
- description: The ChatInterface API from Treasure Data — 2 operation(s) for chatinterface.
  name: Treasure Data Chat Interface API
  slug: treasure-data-chatinterface-api
- description: The Connections API from Treasure Data — 5 operation(s) for connections.
  name: Treasure Data Connections API
  slug: treasure-data-connections-api
- description: The Data Connector Restrictions API from Treasure Data — 1 operation(s) for data connector restrictions.
  name: Treasure Data Data Connector Restrictions API
  slug: treasure-data-data-connector-restrictions-api
- description: The Dwh API from Treasure Data — 6 operation(s) for dwh.
  name: Treasure Data Dwh API
  slug: treasure-data-dwh-api
- description: Folders are containers in which you can organize information. Nested folders offer flexible organization controls. Large volumes of data and application assets can be organized into multi-nested folde
  name: Treasure Data Folders API
  slug: treasure-data-folders-api
- description: The FormInterface API from Treasure Data — 2 operation(s) for forminterface.
  name: Treasure Data Form Interface API
  slug: treasure-data-forminterface-api
- description: One of the challenges of targeting customers with relevant campaigns is understanding where they are in their customer journey. Many organizations use the traditional marketing funnel to understand wh
  name: Treasure Data Funnels API
  slug: treasure-data-funnels-api
- description: The Guess API from Treasure Data — 1 operation(s) for guess.
  name: Treasure Data Guess API
  slug: treasure-data-guess-api
- description: The ImageGenerator API from Treasure Data — 2 operation(s) for imagegenerator.
  name: Treasure Data Image Generator API
  slug: treasure-data-imagegenerator-api
- description: The Integration API from Treasure Data — 2 operation(s) for integration.
  name: Treasure Data Integration API
  slug: treasure-data-integration-api
- description: In Audience Studio, a journey represents a timeline of events that can help you motivate a customer’s behavior about your product. After marketers create journey stages, they can further analyze and r
  name: Treasure Data Journeys API
  slug: treasure-data-journeys-api
- description: The KnowledgeBase API from Treasure Data — 3 operation(s) for knowledgebase.
  name: Treasure Data Knowledge Base API
  slug: treasure-data-knowledgebase-api
- description: The Log API from Treasure Data — 2 operation(s) for log.
  name: Treasure Data Log API
  slug: treasure-data-log-api
- description: Defining a data model for customer data is done by defining parent segments. Parent segments give you an ability to build a single view of a customer, including capturing all interactions, such as att
  name: Treasure Data Parent Segment Configurations API
  slug: treasure-data-parent-segment-configurations-api
- description: After you have created the parent segment, you can view data about the parent segment, such as details about a single segment, audience data, the list of segment folders it contains, or a list of pare
  name: Treasure Data Parent Segments API
  slug: treasure-data-parent-segments-api
- description: The Personalization Service API from Treasure Data — 1 operation(s) for personalization service.
  name: Treasure Data Personalization Service API
  slug: treasure-data-personalization-service-api
- description: The PlazmaQueryTool API from Treasure Data — 2 operation(s) for plazmaquerytool.
  name: Treasure Data Plazma Query Tool API
  slug: treasure-data-plazmaquerytool-api
- description: The Policy Group Tags API from Treasure Data — 2 operation(s) for policy group tags.
  name: Treasure Data Policy Group Tags API
  slug: treasure-data-policy-group-tags-api
- description: The Pool API from Treasure Data — 4 operation(s) for pool.
  name: Treasure Data Pool API
  slug: treasure-data-pool-api
- description: Using Treasure Data’s predictive scoring model, based on predictive segments, marketers can predict profile behavior such as who is likely to churn, purchase, click, or convert in the near future. <br
  name: Treasure Data Predictive Segments API
  slug: treasure-data-predictive-segments-api
- description: The PresentationArtifactTool API from Treasure Data — 2 operation(s) for presentationartifacttool.
  name: Treasure Data Presentation Artifact Tool API
  slug: treasure-data-presentationartifacttool-api
- description: The Project API from Treasure Data — 10 operation(s) for project.
  name: Treasure Data Project API
  slug: treasure-data-project-api
- description: The Prompt API from Treasure Data — 2 operation(s) for prompt.
  name: Treasure Data Prompt API
  slug: treasure-data-prompt-api
- description: The Realtime Journeys API from Treasure Data — 21 operation(s) for realtime journeys.
  name: Treasure Data Realtime Journeys API
  slug: treasure-data-realtime-journeys-api
- description: The Realtime Personalization API from Treasure Data — 7 operation(s) for realtime personalization.
  name: Treasure Data Realtime Personalization API
  slug: treasure-data-realtime-personalization-api
- description: The Schedule API from Treasure Data — 6 operation(s) for schedule.
  name: Treasure Data Schedule API
  slug: treasure-data-schedule-api
- description: The Schedules API from Treasure Data — 6 operation(s) for schedules.
  name: Treasure Data Schedules API
  slug: treasure-data-schedules-api
- description: In marketing, a segment is a container that groups profiles (usually people) who share one or more common characteristics. In Treasure Data, the parent segment is your total population of people, acco
  name: Treasure Data Segments API
  slug: treasure-data-segments-api
- description: The Session API from Treasure Data — 3 operation(s) for session.
  name: Treasure Data Session API
  slug: treasure-data-session-api
- description: The TextKnowledgeBase API from Treasure Data — 2 operation(s) for textknowledgebase.
  name: Treasure Data Text Knowledge Base API
  slug: treasure-data-textknowledgebase-api
- description: The TextResource API from Treasure Data — 2 operation(s) for textresource.
  name: Treasure Data Text Resource API
  slug: treasure-data-textresource-api
- description: The Profiles API Token enables your ability to increase personalized content based on detailed customer information. This REST API returns customer data in real-time and updates your segment informati
  name: Treasure Data Tokens API
  slug: treasure-data-tokens-api
- description: The ToolTarget API from Treasure Data — 2 operation(s) for tooltarget.
  name: Treasure Data Tool Target API
  slug: treasure-data-tooltarget-api
- description: The User API from Treasure Data — 2 operation(s) for user.
  name: Treasure Data User API
  slug: treasure-data-user-api
- description: The Util API from Treasure Data — 1 operation(s) for util.
  name: Treasure Data Util API
  slug: treasure-data-util-api
- description: The WebSearchTool API from Treasure Data — 2 operation(s) for websearchtool.
  name: Treasure Data Web Search Tool API
  slug: treasure-data-websearchtool-api
- description: The WorkflowExecutor API from Treasure Data — 1 operation(s) for workflowexecutor.
  name: Treasure Data Workflow Executor API
  slug: treasure-data-workflowexecutor-api
artifact_total: 97
asyncapis:
- description: ''
  name: Treasure Data Webhooks
  slug: treasure-data-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Treasure Data TD Bulk Import API
  slug: open-treasure-data-bulk-import-api
- collection_type: open
  name: Treasure Data TD Bulk Import Bulk Loads API
  slug: open-treasure-data-bulk-loads-api
- collection_type: open
  name: Treasure Data TD Bulk Import Connectors API
  slug: open-treasure-data-connectors-api
- collection_type: open
  name: Treasure Data TD Bulk Import Databases API
  slug: open-treasure-data-databases-api
- collection_type: open
  name: Treasure Data TD Bulk Import Jobs API
  slug: open-treasure-data-jobs-api
- collection_type: open
  name: Treasure Data TD Bulk Import SSO API
  slug: open-treasure-data-sso-api
- collection_type: open
  name: Treasure Data TD Bulk Import System API
  slug: open-treasure-data-system-api
- collection_type: open
  name: Treasure Data TD Bulk Import Tables API
  slug: open-treasure-data-tables-api
- collection_type: open
  name: Treasure Data TD Bulk Import Users API
  slug: open-treasure-data-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/treasure-data-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/treasure-data-td-api-v3-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/treasure-data-cdp-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/treasure-data-llm-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/treasure-data-dwh-integration-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/treasure-data-personalization-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/treasure-data-postback-api-v2-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/treasure-data-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/treasure-data-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/treasure-data-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/treasure-data-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.treasure.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.treasure.ai/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/treasure-data-inc-
- group: company
  title: ''
  type: Blog
  url: https://www.treasure.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.treasure.ai/product/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.treasure.ai/
- group: other
  title: ''
  type: X
  url: https://twitter.com/TreasureData
- group: commercial
  title: ''
  type: Plans
  url: plans/treasure-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/treasure-data-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/treasure-data-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/treasure-data-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/treasure-data-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/treasure-data-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/treasure-data-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/treasure-data-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/treasure-data-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/treasure-data-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/treasure-data-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/treasure-data-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/treasure-data-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/treasure-data-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/treasure-data-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/treasure-data-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/treasure-data-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.treasure.ai/security/
- group: design
  title: ''
  type: DataModel
  url: data-model/treasure-data-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/treasure-data-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/treasure-data-sandbox.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/treasure-data-vocabulary.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.treasure.ai/apis
- group: docs
  title: ''
  type: APIReference
  url: https://docs.treasure.ai/apis/td_api_v3-public
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.treasure.ai/apis/td-api
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.treasure.ai/release-notes
- group: start
  title: ''
  type: Login
  url: https://console.treasuredata.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.treasure.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.treasure.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/treasure-data
created: '2026-06-13'
description: 'Treasure Data — rebranded Treasure AI in April 2026 — is an enterprise customer data platform that unifies first-party customer data and activates it across marketing, service and AI agent workloads. It publishes eight OpenAPI descriptions covering 405 operations: the Treasure Data API v3 for databases, tables, query jobs, schedules and access control; the CDP (Audience) API for parent segments, segments, journeys, funnels, predictive segments and activations; the LLM API for AI agents, chats and knowledge bases; Treasure Workflow for Digdag orchestration; a Data Warehouse Integration API for Snowflake and Databricks; the Personalization Service for real-time offers; and Postback v1 and v2 for event ingestion. Queries run on Trino/Presto and Hive. An official MCP server exposes 23 tools over stdio and the documentation site serves a live remote MCP endpoint.'
examples:
- key_count: 10
  name: Bulk Import Session
  slug: bulk-import-session
- key_count: 3
  name: Issue Job Response
  slug: issue-job-response
- key_count: 1
  name: List Databases Response
  slug: list-databases-response
- key_count: 1
  name: User List Response
  slug: user-list-response
finops:
- name: Treasure Data Finops
  service_category: ''
  slug: treasure-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/treasure-data.png
json_schemas:
- name: BulkImport
  property_count: 10
  slug: bulk-import
- name: Database
  property_count: 5
  slug: database
- name: Job
  property_count: 14
  slug: job
- name: User
  property_count: 14
  slug: user
jsonld:
- class_count: 38
  name: Treasure Data Context
  property_count: 2
  slug: treasure-data-context
layout: provider
mcp_servers:
- description: 'Treasure Data ships two distinct Model Context Protocol servers. The official product server, @treasuredata/mcp-server, is a local stdio server run with npx that exposes 23 tools over the TD API, the '
  name: Treasure Data MCP Servers
  slug: treasure-data-mcp-servers
modified: '2026-08-13'
name: Treasure Data
nav: Providers
network: true
overview: 'Treasure Data publishes 65 APIs on the [APIs.io](https://apis.io/) network, including Bulk Loads API, User API, System API, and 62 more. Tagged areas include Customer Data Platform, CDP, Big Data, Data Warehouse, and Hive.


  The Treasure Data catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Treasure Data''s developer surface includes authentication, documentation, engineering blog, pricing, CLI, changelog, sandbox, and 42 more developer resources.'
plans:
- name: Treasure Data Plans Pricing
  plan_count: 3
  slug: treasure-data-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 17
  name: Treasure Data Rate Limits
  slug: treasure-data-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Treasure Data API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: treasure-data-jsonschema-spectral-rules
scopes:
- name: Treasure Data Scopes
  scope_count: 4
  slug: treasure-data-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 74.1
  coverage:
    artifact_dirs: 32
    catalog_gap: 34.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 43.2
    contract_quality: 67.4
    developer_ergonomics: 81.0
    discoverability: 75.9
    governance: 43.2
    operational_transparency: 73.7
  previous_composite: 74.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/treasure-data/refs/heads/main/screenshots/treasure-data-2026-06-20T195643.png
security:
- kind: authentication
  name: Treasure Data Authentication
  slug: treasure-data-authentication
  summary_line: apiKey/http/openIdConnect · 8 schemes
- kind: domain-security
  name: Treasure Data Domain Security
  slug: treasure-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Treasure Data Trust Center
  slug: treasure-data-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR, CSA STAR
slug: treasure-data
tags:
- Customer Data Platform
- CDP
- Big Data
- Data Warehouse
- Hive
- Presto
- Enterprise
- Artificial Intelligence
- Marketing
- Analytics
website: https://www.treasure.ai/
---
