---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: three_quarters
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Hightouch Agentic Access
  operation_count: 43
  slug: hightouch-agentic-access
  summary_line: 43 operations · 22 acting
api_count: 1
apis:
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: Warehouse and database sources Hightouch reads from.
  name: Hightouch Sources API
  phrasing_intents:
  - id: GetSource
    intent: Look up a data source
    question: How do I see the details of one connected source by its ID?
  - id: UpdateSource
    intent: Change a source's name or configuration
    question: Can I rename a source that's already connected?
  - id: ListSource
    intent: List data sources in the workspace
    question: Which data sources are connected to my workspace?
  - id: CreateSource
    intent: Connect a new data source
    question: How do I connect a new warehouse like Snowflake or Postgres as a source?
  phrasing_ops: 4
  slug: hightouch-sources-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: Model definitions (SQL, table, dbt, visual) over a source.
  name: Hightouch Models API
  phrasing_intents:
  - id: GetModel
    intent: Look up a model
    question: How do I see the query and settings of one model by its ID?
  - id: UpdateModel
    intent: Edit an existing model's query or settings
    question: Can I change the SQL query on a model I already created?
  - id: ListModel
    intent: List models in the workspace
    question: Which models exist in my workspace, including parent and related models?
  - id: CreateModel
    intent: Create a model on a source
    question: How do I create a new model from a SQL query on one of my sources?
  phrasing_ops: 4
  slug: hightouch-models-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: Destination connectors receiving synced data.
  name: Hightouch Destinations API
  phrasing_intents:
  - id: GetDestination
    intent: Look up a destination
    question: How do I see the details of one destination by its ID?
  - id: UpdateDestination
    intent: Change a destination's name or configuration
    question: Can I rename a destination I've already connected?
  - id: ListDestination
    intent: List destinations in the workspace
    question: Which destinations are connected in my workspace?
  - id: CreateDestination
    intent: Connect a new destination
    question: How do I add a new destination like Salesforce or HubSpot?
  phrasing_ops: 4
  slug: hightouch-destinations-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: Syncs, sync runs, sync sequences and their triggers.
  name: Hightouch Syncs API
  phrasing_intents:
  - id: GetSync
    intent: Look up a sync
    question: How do I see the mapping and schedule of one sync by its ID?
  - id: UpdateSync
    intent: Change a sync's schedule, mapping or status
    question: Can I pause an existing sync by disabling it?
  - id: ListSync
    intent: List syncs in the workspace
    question: Which syncs are set up in my workspace?
  - id: CreateSync
    intent: Create a sync from a model to a destination
    question: How do I set up a new sync that sends a model's rows to a destination?
  - id: ListSyncRuns
    intent: List the run history of a sync
    question: Did my sync run successfully in the last hour?
  - id: TriggerRun
    intent: Run a sync by its ID
    question: How do I kick off a sync run immediately using the sync's ID in the path?
  - id: TriggerRunCustom
    intent: Run a sync by its slug or ID globally
    question: Can I trigger a sync using its slug instead of its numeric ID?
  phrasing_ops: 7
  slug: hightouch-syncs-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: Trigger a campaign send to handle- or profile-based recipients and read back per-send status.
  name: Hightouch Campaigns API
  phrasing_intents:
  - id: TriggerCampaign
    intent: Send an API-triggered campaign to recipients
    question: How do I send an API-triggered campaign to a list of recipients in Hightouch?
  phrasing_ops: 1
  slug: hightouch-campaigns-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: First-party event governance — event contracts and event domains.
  name: Hightouch Events API
  phrasing_intents:
  - id: GetContract
    intent: Look up an event contract
    question: How do I view one event contract and its event definitions?
  - id: UpdateContract
    intent: Edit an event contract
    question: Can I change what happens to undeclared events on an existing contract?
  - id: ListContracts
    intent: List event contracts
    question: Which event contracts are defined in my workspace?
  - id: CreateContract
    intent: Create an event contract
    question: How do I define a new event contract to validate tracked events?
  - id: GetDomain
    intent: Look up an event domain
    question: How do I view an event domain with its events and reusable components?
  - id: UpdateDomain
    intent: Replace an event domain's events and components
    question: Can I replace the reusable components in an existing event domain?
  - id: ListDomains
    intent: List event domains
    question: Which event domains exist in my workspace?
  - id: CreateDomain
    intent: Create an event domain
    question: How do I set up a new event domain with shared components?
  phrasing_ops: 8
  slug: hightouch-events-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: The Decision Engine API from Hightouch — 5 operation(s) for decision engine.
  name: Hightouch Decision Engine API
  phrasing_intents:
  - id: GetFlow
    intent: Look up a decision engine flow
    question: How do I fetch the details of one decision engine flow by its ID?
  - id: ListFlows
    intent: List decision engine flows
    question: Which decision engine flows exist in my workspace?
  - id: ListMessages
    intent: List the messages in a decision flow
    question: What messages are set up inside a given decision engine flow?
  - id: CreateMessage
    intent: Add a message to a decision flow
    question: How do I add a new message to a decision engine flow?
  - id: GetMessage
    intent: Look up one message in a decision flow
    question: How do I see the details of a single message in a decision flow?
  - id: UpdateMessage
    intent: Edit an existing decision flow message
    question: Can I change the config or guardrails of a message already in a flow?
  - id: RunFlow
    intent: Run a decision engine flow now
    question: How do I kick off a decision engine run on demand?
  phrasing_ops: 7
  slug: hightouch-decision-engine-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: The Id Graphs API from Hightouch — 1 operation(s) for id graphs.
  name: Hightouch Id Graphs API
  phrasing_intents:
  - id: TriggerRunIdGraph
    intent: Run an identity graph (deprecated endpoint)
    question: How do I trigger an identity graph run through the older id_graphs endpoint?
  phrasing_ops: 1
  slug: hightouch-id-graphs-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: The Idr API from Hightouch — 4 operation(s) for idr.
  name: Hightouch Idr API
  phrasing_intents:
  - id: TriggerIdrRun
    intent: Start an identity resolution run
    question: How do I trigger a new identity resolution run for a graph?
  - id: ListIdrRuns
    intent: List identity resolution runs for a graph
    question: What identity resolution runs have happened on my graph recently?
  - id: QueueForReprocessing
    intent: Blocklist and reprocess identifier values
    question: How do I remove a bad email from identity resolution so it's ignored in future runs?
  - id: ReprocessStatus
    intent: Check the status of a reprocessing request
    question: Has my identifier reprocessing job finished yet?
  phrasing_ops: 4
  slug: hightouch-idr-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: The Sync Sequences API from Hightouch — 2 operation(s) for sync sequences.
  name: Hightouch Sync Sequences API
  phrasing_intents:
  - id: TriggerSequenceRun
    intent: Run a sync sequence
    question: How do I start a run of a sync sequence?
  - id: GetSyncSequenceRun
    intent: Check the status of a sync sequence run
    question: Has my sync sequence run finished?
  phrasing_ops: 2
  slug: hightouch-sync-sequences-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: The Signups API from Hightouch — 1 operation(s) for signups.
  name: Hightouch Signups API
  slug: hightouch-signups-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: The Sync Templates API from Hightouch — 2 operation(s) for sync templates.
  name: Hightouch Sync Templates API
  slug: hightouch-sync-templates-api
artifact_total: 35
asyncapis:
- description: ''
  name: Hightouch Webhooks
  slug: hightouch-webhooks
collections:
- collection_type: open
  name: Hightouch Management Destinations API
  slug: open-hightouch-destinations-api
- collection_type: open
  name: Hightouch Management Destinations Models API
  slug: open-hightouch-models-api
- collection_type: open
  name: Hightouch Management Destinations Sources API
  slug: open-hightouch-sources-api
- collection_type: open
  name: Hightouch Management Destinations Syncs API
  slug: open-hightouch-syncs-api
- collection_type: open
  name: Hightouch Management API
  slug: open-hightouch
common:
- group: other
  href: https://artifacts.apis.io/hightouch/capabilities/hightouch-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hightouch-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://hightouch.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hightouch.com/docs/developer-tools/api-guide
- group: docs
  title: ''
  type: Documentation
  url: https://hightouch.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://hightouch.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://hightouch.com/docs/getting-started/welcome
- group: company
  title: ''
  type: Blog
  url: https://hightouch.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://hightouch.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.hightouch.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.hightouch.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hightouch.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hightouch.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hightouchio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hightouchio
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hightouch.io
- group: auth
  title: ''
  type: Compliance
  url: https://hightouch.com/platform/security
- group: auth
  href: https://artifacts.apis.io/hightouch/security/hightouch-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hightouch-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hightouch/security/hightouch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hightouch-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/hightouch/authentication/hightouch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hightouch-authentication.yml
- group: auth
  href: https://artifacts.apis.io/hightouch/scopes/hightouch-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hightouch-scopes.yml
- group: design
  href: https://artifacts.apis.io/hightouch/conventions/hightouch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hightouch-conventions.yml
- group: design
  href: https://artifacts.apis.io/hightouch/conformance/hightouch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hightouch-conformance.yml
- group: design
  href: https://artifacts.apis.io/hightouch/errors/hightouch-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hightouch-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hightouch/errors/hightouch-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/hightouch-error-codes.yml
- group: design
  href: https://artifacts.apis.io/hightouch/lifecycle/hightouch-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hightouch-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hightouch/data-model/hightouch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hightouch-data-model.yml
- group: build
  href: https://artifacts.apis.io/hightouch/packages/hightouch-packages.yml
  title: ''
  type: Packages
  url: packages/hightouch-packages.yml
- group: build
  href: https://artifacts.apis.io/hightouch/packages/hightouch-packages.yml
  title: ''
  type: SDKs
  url: packages/hightouch-packages.yml
- group: build
  href: https://artifacts.apis.io/hightouch/cli/hightouch-cli.yml
  title: ''
  type: CLI
  url: cli/hightouch-cli.yml
- group: design
  href: https://artifacts.apis.io/hightouch/components/hightouch-components.yml
  title: ''
  type: Components
  url: components/hightouch-components.yml
- group: start
  href: https://artifacts.apis.io/hightouch/sandbox/hightouch-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/hightouch-sandbox.yml
- group: design
  href: https://artifacts.apis.io/hightouch/asyncapi/hightouch-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hightouch-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/hightouch/well-known/hightouch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hightouch-well-known.yml
- group: agent
  href: https://artifacts.apis.io/hightouch/mcp/hightouch-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hightouch-mcp.yml
- group: build
  href: https://artifacts.apis.io/hightouch/mcp/hightouch-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hightouch-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/hightouch/a2a/hightouch-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hightouch-a2a.yml
- group: agent
  href: https://artifacts.apis.io/hightouch/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/hightouch/agentic-access/hightouch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hightouch-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/hightouch/llms/hightouch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hightouch-llms.txt
- group: commercial
  href: https://artifacts.apis.io/hightouch/plans/hightouch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hightouch-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hightouch/rate-limits/hightouch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hightouch-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/hightouch/finops/hightouch-finops.yml
  title: ''
  type: FinOps
  url: finops/hightouch-finops.yml
- group: other
  href: https://artifacts.apis.io/hightouch/overlays/hightouch-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hightouch-api-overlay.yaml
created: '2026-03-27'
description: Hightouch is a composable Customer Data Platform (CDP) and agentic marketing platform that activates data directly from cloud warehouses and lakehouses such as Snowflake, BigQuery, Databricks and Redshift to more than 290 SaaS destinations, without copying or storing customer data. The platform covers Reverse ETL, Customer Studio audience building and journey orchestration, identity resolution, first-party event collection with SDKs for web and mobile, real-time personalization, AI Decisioning, Match Booster and an Ad Studio for advertising creative. Developers get a bearer-authenticated REST API at https://api.hightouch.com/api/v1 covering sources, models, destinations, syncs and runs, campaigns, decision-engine flows, event contracts and identity graphs, plus an `ht` CLI, Git Sync for version-controlled resource YAML, workspace environments with approval flows, a public documentation MCP server, and an A2A agent card for the Hightouch Marketing Agent.
finops:
- has_sources: true
  method: derived
  name: Hightouch Finops
  primary_unit: ''
  service_category: ''
  slug: hightouch-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hightouch.png
layout: provider
mcp_servers:
- description: Remote MCP server at hightouch.com over HTTP; 2 tools listed.
  name: Hightouch MCP Server
  slug: hightouch-docs
modified: '2026-08-13'
name: Hightouch
nav: Providers
network: true
overview: 'Hightouch publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Sources API, Models API, Destinations API, and 9 more. Tagged areas include CDP, Data Activation, Reverse ETL, Audience Management, and Identity Resolution.


  The Hightouch catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Hightouch''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 36 more developer resources.'
plans:
- name: Hightouch Plans Pricing
  plan_count: 3
  slug: hightouch-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Hightouch Rate Limits
  slug: hightouch-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Hightouch API Rules
  rule_count: 65
  severity_counts:
    error: 55
    hint: 0
    info: 2
    warn: 8
  slug: hightouch-rules
scopes:
- name: Hightouch Scopes
  scope_count: 4
  slug: hightouch-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 69.4
  coverage:
    artifact_dirs: 35
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 85.5
    contract_governance: 31.8
    contract_quality: 67.3
    developer_ergonomics: 75.6
    discoverability: 75.0
    operational_transparency: 47.4
  previous_composite: 68.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 54.5
      total: 22
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hightouch/hightouch-2026-06-20T182738.png
security:
- kind: authentication
  name: Hightouch Authentication
  slug: hightouch-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Hightouch Domain Security
  slug: hightouch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hightouch Trust Center
  slug: hightouch-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 7
skills:
- name: Build a warehouse-to-destination sync
  slug: hightouch-build-a-sync
- name: hightouch-docs
  slug: hightouch-docs-skill
- name: Govern first-party event schemas
  slug: hightouch-govern-event-schemas
- name: Run and reprocess an identity graph
  slug: hightouch-identity-resolution-run
- name: Operate an AI Decisioning flow
  slug: hightouch-run-ai-decisioning-flow
- name: Trigger a campaign send and confirm delivery
  slug: hightouch-send-campaign
- name: Trigger a sync run and monitor it to completion
  slug: hightouch-trigger-and-monitor-a-run
slug: hightouch
tags:
- CDP
- Data Activation
- Reverse ETL
- Audience Management
- Identity Resolution
- Event Collection
- Marketing
- Advertising
- AI Agents
- Data Warehouse
- A2A
- Customer Data Platform
website: https://hightouch.com/
---
