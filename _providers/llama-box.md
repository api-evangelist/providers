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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Llama Box Agentic Access
  operation_count: 10
  slug: llama-box-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- description: 'Agent2Agent surface of the same service: an agent card at https://llama.box/yo/.well-known/agent.json (protocolVersion 0.2.5, version 1.1.0, provider "Chado Studio") declaring four skills — Best Yield'
  name: crvUSD Yield Optimizer A2A Agent
  slug: crvusd-yield-optimizer-a2a-agent
- baseURL: https://llama.box/yo
  baseurl_source: declared
  description: The A2a API from Chado Studio — 2 operation(s) for a2a.
  name: Chado Studio A2a API
  slug: llama-box-a2a-api
- baseURL: https://llama.box/yo
  baseurl_source: declared
  description: The Access Log API from Chado Studio — 1 operation(s) for access log.
  name: Chado Studio Access Log API
  slug: llama-box-access-log-api
- baseURL: https://llama.box/yo
  baseurl_source: declared
  description: The Best Yield API from Chado Studio — 1 operation(s) for best yield.
  name: Chado Studio Best Yield API
  slug: llama-box-best-yield-api
- baseURL: https://llama.box/yo
  baseurl_source: declared
  description: The Health API from Chado Studio — 1 operation(s) for health.
  name: Chado Studio Health API
  slug: llama-box-health-api
- baseURL: https://llama.box/yo
  baseurl_source: declared
  description: The Pools API from Chado Studio — 1 operation(s) for pools.
  name: Chado Studio Pools API
  slug: llama-box-pools-api
- baseURL: https://llama.box/yo
  baseurl_source: declared
  description: The Pricing API from Chado Studio — 1 operation(s) for pricing.
  name: Chado Studio Pricing API
  slug: llama-box-pricing-api
- baseURL: https://llama.box/yo
  baseurl_source: declared
  description: The Rebalance API from Chado Studio — 1 operation(s) for rebalance.
  name: Chado Studio Rebalance API
  slug: llama-box-rebalance-api
- baseURL: https://llama.box/yo
  baseurl_source: declared
  description: The Risk Score API from Chado Studio — 1 operation(s) for risk score.
  name: Chado Studio Risk Score API
  slug: llama-box-risk-score-api
- baseURL: https://llama.box/yo
  baseurl_source: declared
  description: The .well Known API from Chado Studio — 1 operation(s) for .well known.
  name: Chado Studio .well Known API
  slug: llama-box-well-known-api
artifact_total: 20
common:
- group: other
  href: https://artifacts.apis.io/llama-box/overlays/llama-box-crvusd-yield-optimizer-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/llama-box-crvusd-yield-optimizer-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/llama-box/agentic-access/llama-box-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/llama-box-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/llama-box/security/llama-box-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/llama-box-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://llama.box/
- group: docs
  title: ''
  type: Documentation
  url: https://llama.box/yo/redoc
- group: docs
  title: ''
  type: APIReference
  url: https://llama.box/yo/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://llama.box/yo/api/pricing
- group: other
  href: https://artifacts.apis.io/llama-box/a2a/llama-box-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/llama-box-a2a.yml
- group: agent
  href: https://artifacts.apis.io/llama-box/well-known/llama-box-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/llama-box-well-known.yml
- group: agent
  href: https://artifacts.apis.io/llama-box/llms/llama-box-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/llama-box-llms.txt
- group: auth
  href: https://artifacts.apis.io/llama-box/authentication/llama-box-authentication.yml
  title: ''
  type: Authentication
  url: authentication/llama-box-authentication.yml
- group: design
  href: https://artifacts.apis.io/llama-box/conventions/llama-box-conventions.yml
  title: ''
  type: Conventions
  url: conventions/llama-box-conventions.yml
- group: design
  href: https://artifacts.apis.io/llama-box/errors/llama-box-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/llama-box-problem-types.yml
- group: design
  href: https://artifacts.apis.io/llama-box/data-model/llama-box-data-model.yml
  title: ''
  type: DataModel
  url: data-model/llama-box-data-model.yml
- group: operate
  href: https://artifacts.apis.io/llama-box/rate-limits/llama-box-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/llama-box-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/llama-box/plans/llama-box-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/llama-box-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/llama-box/sandbox/llama-box-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/llama-box-sandbox.yml
- group: design
  href: https://artifacts.apis.io/llama-box/conformance/llama-box-conformance.yml
  title: ''
  type: Conformance
  url: conformance/llama-box-conformance.yml
- group: design
  href: https://artifacts.apis.io/llama-box/lifecycle/llama-box-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/llama-box-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/llama-box/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-19'
description: Chado Studio (contact api@chado.studio) operates llama.box, a desktop-style hub for the Curve Finance ecosystem — dashboards, analytics and curated links for Curve, crvUSD, LlamaLend, YieldBasis, Convex, Stake DAO, Yearn and Resupply. Its one machine-readable surface is the crvUSD Yield Optimizer, a FastAPI service mounted at https://llama.box/yo that discovers crvUSD yield across scrvUSD, LlamaLend, Convex and StakeDAO on Ethereum, Arbitrum, Base, Optimism and Fraxtal, scores pool risk 0-100 and simulates rebalances. It publishes an OpenAPI 3.1.0 contract (10 operations) at /yo/openapi.json with Swagger UI and ReDoc, an A2A 0.2.5 agent card at /yo/.well-known/agent.json declaring four skills, and charges for the risk, rebalance and A2A calls per request through the x402 protocol in USDC on the Base Sepolia testnet. The hub itself serves an llms.txt and a robots.txt that allows every major AI crawler.
image: https://llama.box/og-cover.png
layout: provider
modified: '2026-09-19'
name: Chado Studio
nav: Providers
network: true
overview: 'Chado Studio publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, Access Log API, Best Yield API, and 7 more. Tagged areas include Agents, A2A, x402, DeFi, and Yield.


  The Chado Studio catalog on APIs.io includes 1 Spectral governance ruleset.


  Chado Studio''s developer surface includes documentation, API reference, pricing, authentication, sandbox, and 15 more developer resources.'
plans:
- name: Llama Box Plans Pricing
  plan_count: 2
  slug: llama-box-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Llama Box Rate Limits
  slug: llama-box-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Chado Studio API Rules
  rule_count: 45
  severity_counts:
    error: 39
    hint: 0
    info: 3
    warn: 3
  slug: llama-box-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 31.6
    contract_governance: 31.8
    contract_quality: 45.1
    developer_ergonomics: 37.5
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/llama-box/llama-box-2026-10-11T110539.png
security:
- kind: authentication
  name: Llama Box Authentication
  slug: llama-box-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Llama Box Domain Security
  slug: llama-box-domain-security
  summary_line: TLSv1.3
skill_count: 4
skills:
- name: llama-box-ask-the-agent
  slug: llama-box-ask-the-agent
- name: llama-box-assess-pool-risk
  slug: llama-box-assess-pool-risk
- name: llama-box-find-best-yield
  slug: llama-box-find-best-yield
- name: llama-box-simulate-rebalance
  slug: llama-box-simulate-rebalance
slug: llama-box
tags:
- Agents
- A2A
- x402
- DeFi
- Yield
- Curve Finance
- crvUSD
- Stablecoins
- Risk Scoring
- Analytics
- Agent-Native
website: https://llama.box/
---
