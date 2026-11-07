---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 57.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Phonic Agentic Access
  operation_count: 50
  slug: phonic-agentic-access
  summary_line: 50 operations · 32 acting
api_count: 1
apis:
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The agents API from Phonic — 5 operation(s) for agents.
  name: Phonic Agents API
  slug: phonic-agents-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The auth API from Phonic — 2 operation(s) for auth.
  name: Phonic Auth API
  slug: phonic-auth-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The conversationItems API from Phonic — 1 operation(s) for conversationitems.
  name: Phonic Conversation Items API
  slug: phonic-conversationitems-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The conversations API from Phonic — 9 operation(s) for conversations.
  name: Phonic Conversations API
  slug: phonic-conversations-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The extractionSchemas API from Phonic — 2 operation(s) for extractionschemas.
  name: Phonic Extraction Schemas API
  slug: phonic-extractionschemas-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The projects API from Phonic — 4 operation(s) for projects.
  name: Phonic Projects API
  slug: phonic-projects-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The tools API from Phonic — 2 operation(s) for tools.
  name: Phonic Tools API
  slug: phonic-tools-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The voices API from Phonic — 2 operation(s) for voices.
  name: Phonic Voices API
  slug: phonic-voices-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The workspace API from Phonic — 1 operation(s) for workspace.
  name: Phonic Workspace API
  slug: phonic-workspace-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The API Keys API from Phonic — 3 operation(s) for api keys.
  name: Phonic API Keys API
  slug: phonic-api-keys-api
artifact_total: 32
asyncapis:
- description: ''
  name: API Reference
  slug: phonic-sts-asyncapi-original
collections:
- collection_type: open
  name: API Reference agents API
  slug: open-phonic-agents-api
- collection_type: open
  name: API Reference agents apiKeys API
  slug: open-phonic-apikeys-api
- collection_type: open
  name: API Reference agents auth API
  slug: open-phonic-auth-api
- collection_type: open
  name: API Reference agents conversationItems API
  slug: open-phonic-conversationitems-api
- collection_type: open
  name: API Reference agents conversations API
  slug: open-phonic-conversations-api
- collection_type: open
  name: API Reference agents extractionSchemas API
  slug: open-phonic-extractionschemas-api
- collection_type: open
  name: API Reference agents projects API
  slug: open-phonic-projects-api
- collection_type: open
  name: API Reference agents tools API
  slug: open-phonic-tools-api
- collection_type: open
  name: API Reference agents voices API
  slug: open-phonic-voices-api
- collection_type: open
  name: API Reference agents workspace API
  slug: open-phonic-workspace-api
common:
- group: commercial
  href: https://artifacts.apis.io/phonic/plans/phonic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/phonic-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/phonic/overlays/phonic-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/phonic-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/phonic/agentic-access/phonic-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/phonic-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/phonic/security/phonic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/phonic-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/phonic/authentication/phonic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/phonic-authentication.yml
- group: build
  href: https://artifacts.apis.io/phonic/packages/phonic-packages.yml
  title: ''
  type: Packages
  url: packages/phonic-packages.yml
- group: build
  href: https://artifacts.apis.io/phonic/packages/phonic-packages.yml
  title: ''
  type: SDKs
  url: packages/phonic-packages.yml
- group: agent
  href: https://artifacts.apis.io/phonic/mcp/phonic-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/phonic-mcp.yml
- group: agent
  href: https://artifacts.apis.io/phonic/llms/phonic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/phonic-llms.txt
- group: design
  href: https://artifacts.apis.io/phonic/conformance/phonic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/phonic-conformance.yml
- group: design
  href: https://artifacts.apis.io/phonic/errors/phonic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/phonic-problem-types.yml
- group: design
  href: https://artifacts.apis.io/phonic/lifecycle/phonic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/phonic-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.phonic.ai/
- group: design
  href: https://artifacts.apis.io/phonic/conventions/phonic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/phonic-conventions.yml
- group: operate
  href: https://artifacts.apis.io/phonic/rate-limits/phonic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/phonic-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/phonic/data-model/phonic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/phonic-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: https://docs.phonic.co/webhooks/overview
- group: agent
  href: https://artifacts.apis.io/phonic/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.phonic.co/
- group: company
  title: ''
  type: Blog
  url: https://phonic.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Phonic-Co
- group: commercial
  title: ''
  type: Pricing
  url: https://phonic.co/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://phonic.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://phonic.co/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://phonic.ai/
created: '2026-07-17'
description: Phonic is a San Francisco voice AI company (founded 2024, seed-backed by Lux Capital) building the first end-to-end speech-to-speech platform for reliable conversational voice agents. The Phonic API lets developers create and configure voice agents, attach voices, place and receive inbound/outbound phone calls (including via SIP trunking and Amazon Connect), run real-time speech-to-speech conversations over a WebSocket, wire up webhook/WebSocket/context/transfer/MCP tools, and analyze, evaluate, and extract structured data from conversations. It ships an OpenAPI 3.1 REST spec, an AsyncAPI 2.6.0 WebSocket spec, official Node and Python SDKs, a hosted MCP server, and llms.txt docs for AI clients.
finops:
- has_sources: true
  method: derived
  name: Phonic Finops
  primary_unit: subscription
  service_category: ''
  slug: phonic-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/phonic.png
layout: provider
mcp_servers:
- description: Phonic's inbound MCP server exposes the Phonic API as MCP tools so a client such as Claude Code, Codex, or Cursor can manage agents, conversations, voices, and projects. It stays up to date with the P
  name: Phonic MCP Server
  slug: phonic
modified: '2026-07-20'
name: Phonic
nav: Providers
network: true
overview: 'Phonic publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Auth API, Conversation Items API, and 7 more. Tagged areas include Company, Artificial Intelligence, Voice AI, Conversational AI, and Speech.


  The Phonic catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Phonic''s developer surface includes authentication, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Phonic Plans Pricing
  plan_count: 3
  slug: phonic-plans-pricing
- name: Phonic Price Estimates
  plan_count: 0
  slug: phonic-price-estimates
random_paper: 17
rate_limits:
- limit_count: 3
  name: Phonic Rate Limits
  slug: phonic-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Phonic API Rules
  rule_count: 55
  severity_counts:
    error: 48
    hint: 0
    info: 2
    warn: 5
  slug: phonic-rules
score:
  band: strong
  composite: 60.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 59.7
    developer_ergonomics: 61.3
    discoverability: 75.0
    operational_transparency: 50.0
  previous_composite: 60.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/phonic/phonic-2026-08-17T081212.png
security:
- kind: authentication
  name: Phonic Authentication
  slug: phonic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Phonic Domain Security
  slug: phonic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: List, analyze, and extract data from Phonic conversations
  slug: phonic-analyze-conversations
- name: Create a Phonic voice agent and place an outbound call
  slug: phonic-create-agent-and-call
slug: phonic
tags:
- Company
- Artificial Intelligence
- Voice AI
- Conversational AI
- Speech
- Voice Agents
- Telephony
- Speech to Speech
- Real-Time
website: https://phonic.ai/
---
