---
access_model:
  confidence: medium
  label: Paid plans, API on Enterprise
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Samu Agentic Access
  operation_count: 10
  slug: samu-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 2
apis:
- description: Hosted, remote MCP server that connects Samu to Claude, ChatGPT and other AI agents, published as a Pro-plan feature. The endpoint answers MCP JSON-RPC over HTTP POST at https://api.samu.ai/mcp and is
  name: Samu MCP Server
  slug: samu-mcp-server
- description: The Meetings API from Samu — 4 operation(s) for meetings.
  name: Samu Meetings API
  slug: samu-meetings-api
- description: Conversaciones (threads/messages/interactions) de WhatsApp y otros providers
  name: Samu Threads API
  slug: samu-threads-api
- description: The Usuarios API from Samu — 1 operation(s) for usuarios.
  name: Samu Usuarios API
  slug: samu-usuarios-api
artifact_total: 14
collections:
- collection_type: open
  name: API Samu
  slug: open-samu
common:
- group: company
  title: ''
  type: Website
  url: https://samu.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://samu.ai/precios
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://samu.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://samu.ai/terminos-y-condiciones
- group: start
  title: ''
  type: Login
  url: https://dashboard.samu.ai
- group: start
  title: ''
  type: SignUp
  url: https://samu.ai/solicitar-una-demo
- group: company
  title: ''
  type: Blog
  url: https://primerareunion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.samu.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.samu.ai/docs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.samu.ai/
- group: auth
  title: ''
  type: Security
  url: https://samu.ai/politica-de-seguridad-y-manejo-de-informacion
- group: auth
  title: ''
  type: Compliance
  url: https://samu.ai/politica-de-seguridad-y-manejo-de-informacion
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/samu-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/samu-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/samu-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/samu-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/samu-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/samu-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/samu-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/samu-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/samu-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/samu-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/samu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/samu-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/samu-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/samu-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/samu-domain-security.yml
created: '2026-07-17'
description: Samu (samu.ai) is an AI-powered conversation-intelligence and sales-analytics platform built for sales managers and revenue leaders across Latin America. It automatically records and transcribes customer interactions across WhatsApp, phone calls, video calls, Microsoft Teams, and Google Meet, then analyzes them to surface actionable coaching insights. Features include an AI "Samu Score" that evaluates call quality against customizable criteria, custom data extractors (e.g. competitor mentions or company size), analysis using SPICED, BANT, and SANDLER sales frameworks, and auto-generated CRM notes, tasks, and meeting summaries. Samu integrates bidirectionally with HubSpot, Pipedrive, Salesforce, and other CRMs, and emphasizes high-accuracy Spanish-language transcription. Samu publishes a REST API (OpenAPI 3.0.0, "API Samu") at api.samu.ai covering users, meetings, transcriptions and WhatsApp/chat threads, authenticated with an account apiKey header, plus an OAuth-protected hosted
  MCP server at api.samu.ai/mcp that connects Samu to Claude, ChatGPT and other AI agents. API access is sold on the Enterprise plan and MCP on the Pro plan. Samu is backed by 500 Global.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/samu.png
layout: provider
mcp_servers:
- description: ''
  name: Samu MCP Server
  slug: samu-mcp-server
- description: ''
  name: Samu MCP Server
  slug: samu-mcp-server-2
modified: '2026-08-13'
name: Samu
nav: Providers
network: true
overview: 'Samu publishes 3 APIs on the [APIs.io](https://apis.io/) network: Meetings API, Threads API, and Usuarios API. Tagged areas include Company, Artificial Intelligence, Sales, Sales Intelligence, and Conversation Intelligence.


  Samu''s developer surface includes pricing, signup flow, engineering blog, documentation, API reference, authentication, and 22 more developer resources.'
plans:
- name: Samu Plans Pricing
  plan_count: 3
  slug: samu-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Samu Rate Limits
  slug: samu-rate-limits
scopes:
- name: Samu Scopes
  scope_count: 1
  slug: samu-scopes
  summary_line: 1 scope · authorizationCode/refreshToken
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 46.9
    developer_ergonomics: 32.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/samu/refs/heads/main/screenshots/samu-2026-08-17T081719.png
security:
- kind: authentication
  name: Samu Authentication
  slug: samu-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Samu Domain Security
  slug: samu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Samu Vulnerability Disclosure
  slug: samu-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: samu
tags:
- Company
- Artificial Intelligence
- Sales
- Sales Intelligence
- Conversation Intelligence
- CRM
- Call Recording
- Analytics
- Latin America
- Transcription
- WhatsApp
- MCP
- Agent Native
website: https://samu.ai
---
