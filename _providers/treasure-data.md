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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 63.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 235
  human_in_the_loop: 25
  name: Treasure Data Agentic Access
  operation_count: 440
  slug: treasure-data-agentic-access
  summary_line: 440 operations · 235 acting · 25 human-in-the-loop
api_count: 23
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
- description: 'The provider-published Treasure Data API v3 — 79 operations across databases, tables, query jobs, schedules, result connections, access-control policies and policy groups, users and delegated admins. '
  name: Treasure Data API v3
  slug: treasure-data-api-v3
- description: The CDP (Audience) API — 183 operations covering parent segments, segments, activations and syndications, journeys and realtime journeys, funnels, predictive segments, folders, tokens and activation t
  name: Treasure Data CDP API
  slug: treasure-data-cdp-api
- description: The LLM API — 87 operations for AI agents, agent schedules, chats and chat interfaces, actions, knowledge bases, artifacts, image generation, integrations and projects. The programmatic surface behind
  name: Treasure Data LLM API
  slug: treasure-data-llm-api
- description: Treasure Workflow — the Digdag-based orchestration API. 43 operations over projects, workflow definitions, revisions, schedules, sessions, attempts, tasks, logs, secrets and resource pools.
  name: Treasure Workflow API
  slug: treasure-data-workflow-api
- description: First class Data Warehouse Integration API — 10 operations for creating and running bulkload sessions against Snowflake and Databricks, with schedules, session attempts and workflow runs.
  name: Treasure Data Data Warehouse Integration API
  slug: treasure-data-dwh-integration-api
- description: Real-time personalization — ingest a single event and receive personalization offers from the real-time engines. Versioned by content type (Accept application/vnd.treasuredata.v1+json) and routed by a
  name: Treasure Data Personalization Service
  slug: treasure-data-personalization-api
- description: JSON event ingestion endpoint used by the JavaScript, iOS, Android, React Native and Cordova SDKs for small, frequent payloads.
  name: Treasure Data Postback API
  slug: treasure-data-postback-api
- description: Next-generation event ingestion on records.in.treasuredata.com with header-based authentication (X-TD-Write-Key or a full TD1 key) and a region-templated host.
  name: Treasure Data Postback API v2
  slug: treasure-data-postback-api-v2
- description: 'Two Model Context Protocol servers — the official @treasuredata/mcp-server (23 tools, local stdio, public preview) and a live remote documentation MCP endpoint on the docs host whose six tools return '
  name: Treasure Data MCP Servers
  slug: treasure-data-mcp
artifact_total: 53
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
- description: ''
  name: treasure-data-mcp.yml
  slug: treasure-data-mcpyml
modified: '2026-08-13'
name: Treasure Data
nav: Providers
network: true
overview: 'Treasure Data publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Bulk Loads API, System API, Postback API, and 17 more. Tagged areas include Customer Data Platform, CDP, Big Data, Data Warehouse, and Hive.


  The Treasure Data catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Treasure Data''s developer surface includes authentication, documentation, engineering blog, pricing, CLI, changelog, sandbox, and 35 more developer resources.'
plans:
- name: Treasure Data Plans Pricing
  plan_count: 3
  slug: treasure-data-plans-pricing
random_paper: 138
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
  composite: 77.2
  delta: -6.2
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 55.3
    contract_quality: 71.9
    developer_ergonomics: 81.0
    discoverability: 81.5
    governance: 55.3
    operational_transparency: 73.7
  previous_composite: 83.4
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
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
- AI
- Marketing
- Analytics
website: https://www.treasure.ai/
---
