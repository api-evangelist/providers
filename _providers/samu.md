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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Samu Agentic Access
  operation_count: 10
  slug: samu-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 1
apis:
- description: Hosted, remote MCP server that connects Samu to Claude, ChatGPT and other AI agents, published as a Pro-plan feature. The endpoint answers MCP JSON-RPC over HTTP POST at https://api.samu.ai/mcp and is
  name: Samu MCP Server
  slug: samu-mcp-server
- baseURL: https://api.samu.ai
  baseurl_source: declared
  description: The Meetings API from Samu — 4 operation(s) for meetings.
  name: Samu Meetings API
  slug: samu-meetings-api
- baseURL: https://api.samu.ai
  baseurl_source: declared
  description: Conversaciones (threads/messages/interactions) de WhatsApp y otros providers
  name: Samu Threads API
  slug: samu-threads-api
- baseURL: https://api.samu.ai
  baseurl_source: declared
  description: The Usuarios API from Samu — 1 operation(s) for usuarios.
  name: Samu Usuarios API
  slug: samu-usuarios-api
artifact_total: 18
collections:
- collection_type: open
  name: API Samu
  slug: open-samu
common:
- group: company
  title: ''
  type: Blog
  url: https://www.samu.ai/blog
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
  href: https://artifacts.apis.io/samu/llms/samu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/samu-llms.txt
- group: agent
  href: https://artifacts.apis.io/samu/well-known/samu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/samu-well-known.yml
- group: auth
  href: https://artifacts.apis.io/samu/security/samu-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/samu-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/samu/authentication/samu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/samu-authentication.yml
- group: auth
  href: https://artifacts.apis.io/samu/scopes/samu-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/samu-scopes.yml
- group: design
  href: https://artifacts.apis.io/samu/conventions/samu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/samu-conventions.yml
- group: design
  href: https://artifacts.apis.io/samu/conformance/samu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/samu-conformance.yml
- group: design
  href: https://artifacts.apis.io/samu/errors/samu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/samu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/samu/lifecycle/samu-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/samu-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/samu/data-model/samu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/samu-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/samu/plans/samu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/samu-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/samu/rate-limits/samu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/samu-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/samu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/samu/agentic-access/samu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/samu-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/samu/overlays/samu-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/samu-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/samu/security/samu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/samu-domain-security.yml
created: '2026-07-17'
description: Samu (samu.ai) is an AI-powered conversation-intelligence and sales-analytics platform built for sales managers and revenue leaders across Latin America. It automatically records and transcribes customer interactions across WhatsApp, phone calls, video calls, Microsoft Teams, and Google Meet, then analyzes them to surface actionable coaching insights. Features include an AI "Samu Score" that evaluates call quality against customizable criteria, custom data extractors (e.g. competitor mentions or company size), analysis using SPICED, BANT, and SANDLER sales frameworks, and auto-generated CRM notes, tasks, and meeting summaries. Samu integrates bidirectionally with HubSpot, Pipedrive, Salesforce, and other CRMs, and emphasizes high-accuracy Spanish-language transcription. Samu publishes a REST API (OpenAPI 3.0.0, "API Samu") at api.samu.ai covering users, meetings, transcriptions and WhatsApp/chat threads, authenticated with an account apiKey header, plus an OAuth-protected hosted
  MCP server at api.samu.ai/mcp that connects Samu to Claude, ChatGPT and other AI agents. API access is sold on the Enterprise plan and MCP on the Pro plan. Samu is backed by 500 Global.
finops:
- has_sources: true
  method: derived
  name: Samu Finops
  primary_unit: subscription
  service_category: ''
  slug: samu-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/samu.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.samu.ai over HTTP requiring OAuth.
  name: Samu MCP Server
  slug: samu
modified: '2026-10-06'
name: Samu
nav: Providers
network: true
overview: 'Samu publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Meetings API, Threads API, Usuarios API, and 1 more. Tagged areas include Company, Artificial Intelligence, Sales, Sales Intelligence, and Conversation Intelligence.


  The Samu catalog on APIs.io includes 1 Spectral governance ruleset.


  Samu''s developer surface includes engineering blog, pricing, signup flow, documentation, API reference, authentication, and 23 more developer resources.'
plans:
- name: Samu Plans Pricing
  plan_count: 3
  slug: samu-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Samu Rate Limits
  slug: samu-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Samu API Rules
  rule_count: 52
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 1
  slug: samu-rules
scopes:
- name: Samu Scopes
  scope_count: 1
  slug: samu-scopes
  summary_line: 1 scope · authorizationCode/refreshToken
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 44.7
    developer_ergonomics: 32.7
    discoverability: 75.0
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/samu/samu-2026-08-17T081719.png
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
skill_count: 3
skills:
- name: Export a date range of Samu meetings
  slug: samu-export-meetings
- name: Ingest an externally recorded call into Samu
  slug: samu-ingest-external-call
- name: Read Samu WhatsApp and chat conversation threads
  slug: samu-read-chat-threads
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
- Agent-Native
website: https://samu.ai
---
