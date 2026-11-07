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
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Liquidagent Ai Agentic Access
  operation_count: 17
  slug: liquidagent-ai-agentic-access
  summary_line: 17 operations · 9 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.liquidagent.ai
  baseurl_source: declared
  description: The Liquid Agent API from Liquid Agent — 15 operation(s) for liquid agent.
  name: Liquid Agent Liquid Agent API
  slug: liquidagent-ai-liquid-agent-api
artifact_total: 10
common:
- group: operate
  href: https://artifacts.apis.io/liquidagent-ai/rate-limits/liquidagent-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/liquidagent-ai-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/liquidagent-ai/overlays/liquidagent-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/liquidagent-ai-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/liquidagent-ai/skills/liquidagent-ai-liquid-agent-stocks.md
  title: ''
  type: AgentSkill
  url: skills/liquidagent-ai-liquid-agent-stocks.md
- group: agent
  href: https://artifacts.apis.io/liquidagent-ai/skills/liquidagent-ai-liquid-gas-sponsor.md
  title: ''
  type: AgentSkill
  url: skills/liquidagent-ai-liquid-gas-sponsor.md
- group: company
  title: ''
  type: Website
  url: https://liquidagent.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LiquidAgent
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/LiquidAgent/liquidagentx402
- group: company
  title: ''
  type: Twitter
  url: https://x.com/LiquidAgentAI
- group: operate
  title: ''
  type: StatusPage
  url: https://api.liquidagent.ai/v1/status
- group: commercial
  title: ''
  type: Pricing
  url: https://api.liquidagent.ai/.well-known/x402-resources
- group: commercial
  href: https://artifacts.apis.io/liquidagent-ai/plans/liquidagent-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/liquidagent-ai-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/liquidagent-ai/a2a/liquidagent-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/liquidagent-ai-a2a.yml
- group: other
  title: ''
  type: AgentCard
  url: https://api.liquidagent.ai/.well-known/agent-card.json
- group: agent
  href: https://artifacts.apis.io/liquidagent-ai/well-known/liquidagent-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/liquidagent-ai-well-known.yml
- group: agent
  href: https://artifacts.apis.io/liquidagent-ai/llms/liquidagent-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/liquidagent-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/liquidagent-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/liquidagent-ai/packages/liquidagent-ai-packages.yml
  title: ''
  type: Packages
  url: packages/liquidagent-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/liquidagent-ai/security/liquidagent-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/liquidagent-ai-domain-security.yml
- group: other
  href: https://artifacts.apis.io/liquidagent-ai/regulatory/liquidagent-ai-regulatory-posture.yml
  title: ''
  type: X-RegulatoryPosture
  url: regulatory/liquidagent-ai-regulatory-posture.yml
created: '2026-09-19'
description: 'Liquid Agent is an agent-native money layer on Base: a USDC account for people (yield, payments and stocks from one balance, through the app) and, for AI agents, a permissionless HTTP API at api.liquidagent.ai that mints a self-custodied ERC-4626 vault holding Coinbase''s tokenized NVDA, META, AAPL and GOOGL, buys in from $1, sets custom weights, rebalances and exits to USDC or in-kind any block. Reads are free and need no key; every write returns unsigned calldata the agent signs with its own wallet. Three paid surfaces settle per call in USDC over x402 v2: basket rebalancing signals ($0.04), a shareable portfolio page ($0.25) and an ERC-4337 / ERC-7677 gas sponsor (from $0.03) on Base, Polygon and Solana. The contract is a 17-operation OpenAPI 3.1.0 at api.liquidagent.ai/openapi.json, with an A2A agent card, llms.txt, agents.txt, an x402 resource catalog, an ERC-8004 on-chain identity and two provider-authored Agent Skills in the open-source examples repo.'
finops:
- has_sources: true
  method: derived
  name: Liquidagent Ai Finops
  primary_unit: ''
  service_category: ''
  slug: liquidagent-ai-finops
  template: true
image: https://liquidagent.ai/icon.png
layout: provider
modified: '2026-09-19'
name: Liquid Agent
nav: Providers
network: true
overview: 'Liquid Agent publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Liquid Agent API. Tagged areas include Tokenized Stocks, DeFi, Investing, Agentic Commerce, and x402.


  The Liquid Agent catalog on APIs.io includes 1 Spectral governance ruleset.


  Liquid Agent''s developer surface includes pricing and 18 more developer resources.'
plans:
- name: Liquidagent Ai Plans Pricing
  plan_count: 4
  slug: liquidagent-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Liquidagent Ai Rate Limits
  slug: liquidagent-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Liquid Agent API Rules
  rule_count: 55
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 7
  slug: liquidagent-ai-rules
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 42.1
    contract_governance: 31.8
    contract_quality: 55.6
    developer_ergonomics: 33.3
    discoverability: 73.2
    operational_transparency: 18.4
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 71.4
      total: 7
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 21.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/liquidagent-ai/liquidagent-ai-2026-10-11T110548.png
security:
- kind: authentication
  name: Liquidagent Ai Authentication
  slug: liquidagent-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Liquidagent Ai Domain Security
  slug: liquidagent-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: liquid-agent-stocks
  slug: liquidagent-ai-liquid-agent-stocks
- name: liquid-gas-sponsor
  slug: liquidagent-ai-liquid-gas-sponsor
slug: liquidagent-ai
tags:
- Tokenized Stocks
- DeFi
- Investing
- Agentic Commerce
- x402
- Stablecoins
- Account Abstraction
- Gas Sponsorship
- Base
- Solana
- AI Agents
- Agent-Native
- A2A
- Portfolio Management
- Market Data
website: https://liquidagent.ai/
---
