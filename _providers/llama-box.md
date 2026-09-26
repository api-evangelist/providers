---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Llama Box Agentic Access
  operation_count: 10
  slug: llama-box-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- baseURL: https://llama.box/yo
  baseurl_source: declared
  description: REST contract for the crvUSD Yield Optimizer (OpenAPI 3.1.0, info.version 1.1.0, servers[] "/yo" on llama.box). Free, unauthenticated reads list and filter crvUSD yield pools across chains and sources
  name: crvUSD Yield Optimizer API
  slug: crvusd-yield-optimizer-api
- description: 'Agent2Agent surface of the same service: an agent card at https://llama.box/yo/.well-known/agent.json (protocolVersion 0.2.5, version 1.1.0, provider "Chado Studio") declaring four skills — Best Yield'
  name: crvUSD Yield Optimizer A2A Agent
  slug: crvusd-yield-optimizer-a2a-agent
artifact_total: 7
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/llama-box/refs/heads/main/agentic-access/llama-box-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/llama-box-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/llama-box/refs/heads/main/security/llama-box-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/llama-box/refs/heads/main/a2a/llama-box-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/llama-box-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/llama-box/refs/heads/main/well-known/llama-box-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/llama-box-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/llama-box/refs/heads/main/llms/llama-box-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/llama-box-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/llama-box/refs/heads/main/authentication/llama-box-authentication.yml
  title: ''
  type: Authentication
  url: authentication/llama-box-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/llama-box/refs/heads/main/conventions/llama-box-conventions.yml
  title: ''
  type: Conventions
  url: conventions/llama-box-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/llama-box/refs/heads/main/errors/llama-box-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/llama-box-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/llama-box/refs/heads/main/data-model/llama-box-data-model.yml
  title: ''
  type: DataModel
  url: data-model/llama-box-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/llama-box/refs/heads/main/rate-limits/llama-box-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/llama-box-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/llama-box/refs/heads/main/plans/llama-box-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/llama-box-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/llama-box/refs/heads/main/sandbox/llama-box-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/llama-box-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/llama-box/refs/heads/main/conformance/llama-box-conformance.yml
  title: ''
  type: Conformance
  url: conformance/llama-box-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/llama-box/refs/heads/main/lifecycle/llama-box-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/llama-box-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/llama-box/refs/heads/main/skills/_index.yml
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
overview: 'Chado Studio publishes 2 APIs on the [APIs.io](https://apis.io/) network, including crvUSD Yield Optimizer API, and 1 more. Tagged areas include Agents, A2A, x402, DeFi, and Yield.


  Chado Studio''s developer surface includes documentation, API reference, pricing, authentication, sandbox, and 14 more developer resources.'
plans:
- name: Llama Box Plans Pricing
  plan_count: 2
  slug: llama-box-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Llama Box Rate Limits
  slug: llama-box-rate-limits
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 41.0
    developer_ergonomics: 37.5
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Llama Box Authentication
  slug: llama-box-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Llama Box Domain Security
  slug: llama-box-domain-security
  summary_line: TLSv1.3
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
