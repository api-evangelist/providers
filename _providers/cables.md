---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: quarter
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 168
  human_in_the_loop: 0
  name: Cables Agentic Access
  operation_count: 168
  slug: cables-agentic-access
  summary_line: 168 operations · 168 acting
api_count: 1
apis:
- baseURL: https://mcp.cables.live
  baseurl_source: declared
  description: The Tools API from Cables — 168 operation(s) for tools.
  name: Cables Tools API
  slug: cables-tools-api
artifact_total: 12
common:
- group: other
  href: https://artifacts.apis.io/cables/capabilities/cables-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cables-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/cables/mcp/cables-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cables-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.cables.live/mcp
- group: company
  title: ''
  type: Website
  url: https://cables.live
- group: auth
  href: https://artifacts.apis.io/cables/authentication/cables-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cables-authentication.yml
- group: agent
  href: https://artifacts.apis.io/cables/agentic-access/cables-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cables-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cables/security/cables-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cables-domain-security.yml
- group: design
  href: https://artifacts.apis.io/cables/conformance/cables-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cables-conformance.yml
- group: design
  href: https://artifacts.apis.io/cables/errors/cables-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cables-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cables/conventions/cables-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cables-conventions.yml
- group: other
  href: https://artifacts.apis.io/cables/overlays/cables-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cables-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/cables/data-model/cables-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cables-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/cables/plans/cables-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cables-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cables/rate-limits/cables-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cables-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/cables/sandbox/cables-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cables-sandbox.yml
- group: design
  href: https://artifacts.apis.io/cables/lifecycle/cables-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cables-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/cables/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/cables/llms/cables-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cables-llms.txt
created: '2026-09-18'
description: An agent-native, pay-per-call MCP resource server exposing 168 TensorFlow.js machine-learning analytics tools (image classification, object detection, NLP, forecasting, and social-media analytics for YouTube, Instagram, TikTok, Twitter/X, Facebook, Discord, and Twitch). Each tool call is monetized via the x402 payment protocol at $0.05 per call, settled in USDC on Solana devnet. Unpaid requests receive an HTTP 402 challenge.
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.cables.live; 168 tools listed.
  name: Cables MCP Server
  slug: tensorflow-social-mcp
modified: '2026-09-18'
name: Cables
nav: Providers
network: true
overview: 'Cables publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Tools API. Tagged areas include MCP Server, Agent-Native, x402, Pay-per-call, and Machine Learning.


  The Cables catalog on APIs.io includes 1 Spectral governance ruleset.


  Cables'' developer surface includes authentication, sandbox, and 16 more developer resources.'
plans:
- name: Cables Plans Pricing
  plan_count: 1
  slug: cables-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Cables Rate Limits
  slug: cables-rate-limits
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Cables API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: cables-rules
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 44.5
    catalog_earned_first_party: 8.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 44.9
    developer_ergonomics: 20.8
    discoverability: 66.7
    operational_transparency: 0.0
  previous_composite: 25.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 14.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cables/cables-2026-10-11T184002.png
security:
- kind: authentication
  name: Cables Authentication
  slug: cables-authentication
  summary_line: none-for-discovery/x402-payment-for-execution · 0 schemes
- kind: domain-security
  name: Cables Domain Security
  slug: cables-domain-security
  summary_line: TLSv1.3
skill_count: 4
skills:
- name: Data forecasting & anomaly detection
  slug: cables-data-forecasting
- name: Image & vision analysis
  slug: cables-image-vision-analysis
- name: Social-media analytics
  slug: cables-social-media-analytics
- name: Text & NLP analysis
  slug: cables-text-nlp-analysis
slug: cables
tags:
- MCP Server
- Agent-Native
- x402
- Pay-per-call
- Machine Learning
- tensorflow-js
- Natural Language Processing
- Computer Vision
- Social Media Analytics
- OpenAPI
- Solana
- Crypto Payments
- testnet-devnet
website: https://cables.live
---
