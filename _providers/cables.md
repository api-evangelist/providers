---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-09-21'
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
  description: Hosted MCP resource server offering 168 ML analytics tools invoked via POST, gated by the x402 payment protocol (Solana devnet USDC). Machine-readable OpenAPI 3.0.0 contract available publicly.
  name: TensorFlow.js Social Media MCP Server
  slug: tensorflowjs-social-media-mcp-server
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://cables.live
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cables/refs/heads/main/authentication/cables-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cables-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cables/refs/heads/main/agentic-access/cables-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cables-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cables/refs/heads/main/security/cables-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cables-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cables/refs/heads/main/conformance/cables-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cables-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cables/refs/heads/main/errors/cables-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cables-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cables/refs/heads/main/conventions/cables-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cables-conventions.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cables/refs/heads/main/overlays/cables-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cables-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cables/refs/heads/main/data-model/cables-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cables-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cables/refs/heads/main/plans/cables-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cables-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cables/refs/heads/main/rate-limits/cables-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cables-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/cables/refs/heads/main/sandbox/cables-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cables-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cables/refs/heads/main/lifecycle/cables-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cables-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cables/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cables/refs/heads/main/llms/cables-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cables-llms.txt
created: '2026-09-18'
description: An agent-native, pay-per-call MCP resource server exposing 168 TensorFlow.js machine-learning analytics tools (image classification, object detection, NLP, forecasting, and social-media analytics for YouTube, Instagram, TikTok, Twitter/X, Facebook, Discord, and Twitch). Each tool call is monetized via the x402 payment protocol at $0.05 per call, settled in USDC on Solana devnet. Unpaid requests receive an HTTP 402 challenge.
layout: provider
mcp_servers:
- description: ''
  name: Cables MCP Server
  slug: cables-mcp-server
- description: ''
  name: MCP endpoint (live)
  slug: mcp-endpoint-live
modified: '2026-09-18'
name: Cables
nav: Providers
network: true
overview: 'Cables publishes 1 API on the [APIs.io](https://apis.io/) network: TensorFlow.js Social Media MCP Server. Tagged areas include MCP Server, agent-native, x402, pay-per-call, and Machine-Learning.


  Cables'' developer surface includes authentication, sandbox, and 13 more developer resources.'
plans:
- name: Cables Plans Pricing
  plan_count: 1
  slug: cables-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Cables Rate Limits
  slug: cables-rate-limits
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 39.5
    developer_ergonomics: 20.8
    discoverability: 66.7
    operational_transparency: 0.0
  previous_composite: 23.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cables Authentication
  slug: cables-authentication
  summary_line: none-for-discovery/x402-payment-for-execution · 0 schemes
- kind: domain-security
  name: Cables Domain Security
  slug: cables-domain-security
  summary_line: TLSv1.3
slug: cables
tags:
- MCP Server
- agent-native
- x402
- pay-per-call
- Machine-Learning
- tensorflow-js
- NLP
- Computer-Vision
- Social Media Analytics
- OpenAPI
- Solana
- Crypto Payments
- testnet-devnet
website: https://cables.live
---
