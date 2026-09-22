---
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Liquidagent Ai Agentic Access
  operation_count: 17
  slug: liquidagent-ai-agentic-access
  summary_line: 17 operations · 9 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.liquidagent.ai
  baseurl_source: declared
  description: Agent-facing REST API on Base (eip155:8453). Free reads (basket constituents and live prices, vault NAV and weights, an address's vaults and shares, a purchase quote, the plain-English guide) and free
  name: Liquid Agent Tokenized Stock Index and Gas Sponsor API
  slug: liquid-agent-api
artifact_total: 6
common:
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
  href: https://raw.githubusercontent.com/api-evangelist/liquidagent-ai/refs/heads/main/plans/liquidagent-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/liquidagent-ai-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/liquidagent-ai/refs/heads/main/a2a/liquidagent-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/liquidagent-ai-a2a.yml
- group: other
  title: ''
  type: AgentCard
  url: https://api.liquidagent.ai/.well-known/agent-card.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/liquidagent-ai/refs/heads/main/well-known/liquidagent-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/liquidagent-ai-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/liquidagent-ai/refs/heads/main/llms/liquidagent-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/liquidagent-ai-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/liquidagent-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/liquidagent-ai/refs/heads/main/packages/liquidagent-ai-packages.yml
  title: ''
  type: Packages
  url: packages/liquidagent-ai-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/liquidagent-ai/refs/heads/main/security/liquidagent-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/liquidagent-ai-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/liquidagent-ai/refs/heads/main/regulatory/liquidagent-ai-regulatory-posture.yml
  title: ''
  type: X-RegulatoryPosture
  url: regulatory/liquidagent-ai-regulatory-posture.yml
created: '2026-09-19'
description: 'Liquid Agent is an agent-native money layer on Base: a USDC account for people (yield, payments and stocks from one balance, through the app) and, for AI agents, a permissionless HTTP API at api.liquidagent.ai that mints a self-custodied ERC-4626 vault holding Coinbase''s tokenized NVDA, META, AAPL and GOOGL, buys in from $1, sets custom weights, rebalances and exits to USDC or in-kind any block. Reads are free and need no key; every write returns unsigned calldata the agent signs with its own wallet. Three paid surfaces settle per call in USDC over x402 v2: basket rebalancing signals ($0.04), a shareable portfolio page ($0.25) and an ERC-4337 / ERC-7677 gas sponsor (from $0.03) on Base, Polygon and Solana. The contract is a 17-operation OpenAPI 3.1.0 at api.liquidagent.ai/openapi.json, with an A2A agent card, llms.txt, agents.txt, an x402 resource catalog, an ERC-8004 on-chain identity and two provider-authored Agent Skills in the open-source examples repo.'
image: https://liquidagent.ai/icon.png
layout: provider
modified: '2026-09-19'
name: Liquid Agent
nav: Providers
network: true
overview: 'Liquid Agent publishes 1 API on the [APIs.io](https://apis.io/) network: Tokenized Stock Index and Gas Sponsor API. Tagged areas include Tokenized Stocks, DeFi, Investing, Agentic Commerce, and x402.


  Liquid Agent''s developer surface includes pricing and 14 more developer resources.'
plans:
- name: Liquidagent Ai Plans Pricing
  plan_count: 4
  slug: liquidagent-ai-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Liquidagent Ai Rate Limits
  slug: liquidagent-ai-rate-limits
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 60.5
    developer_ergonomics: 47.6
    discoverability: 75.9
    operational_transparency: 21.1
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Liquidagent Ai Authentication
  slug: liquidagent-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Liquidagent Ai Domain Security
  slug: liquidagent-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
- agent-native
- A2A
- Portfolio-Management
- Market Data
website: https://liquidagent.ai/
---
