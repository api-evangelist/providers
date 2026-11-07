---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nansen Agentic Access
  operation_count: 6
  slug: nansen-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: 'REST API surfacing Nansen''s on-chain intelligence: smart-money flows, profiler (wallet labels and balances), token screener, portfolio, points, Hyperliquid analytics, prediction markets, and the Nanse'
  name: Nansen REST API
  slug: rest-api
- baseURL: https://api.nansen.ai/api/v1
  baseurl_source: declared
  description: Smart-money wallet flows and behavior.
  name: Nansen Smart Money API
  slug: nansen-smart-money-api
artifact_total: 13
collections:
- collection_type: open
  name: Nansen REST Smart Money API
  slug: open-nansen-smart-money-api
- collection_type: open
  name: Nansen REST API
  slug: open-nansen
common:
- group: company
  title: ''
  type: Website
  url: https://www.nansen.ai/
- group: agent
  href: https://artifacts.apis.io/nansen/agentic-access/nansen-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nansen-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/nansen/security/nansen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nansen-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/nansen/authentication/nansen-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nansen-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nansen-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nansen
- group: start
  title: ''
  type: Portal
  url: https://www.nansen.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nansen.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nansen.ai/pricing
- group: commercial
  href: https://artifacts.apis.io/nansen/plans/nansen-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nansen-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/nansen/rate-limits/nansen-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nansen-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nansen/finops/nansen-finops.yml
  title: ''
  type: FinOps
  url: finops/nansen-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.nansen.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://nansen.ai/blog
created: '2026-05-08'
description: Nansen is an onchain analytics platform with wallet labeling, smart-money tracking, token screener, portfolio, prediction markets, and AI Agent endpoints across 30+ chains. The Nansen API exposes REST endpoints under api.nansen.ai with Smart Money, Profiler, Token Screener, Portfolio, Points, Hyperliquid, Agent, and Prediction Markets categories.
finops:
- has_sources: true
  method: generated
  name: Nansen Finops
  primary_unit: ''
  service_category: Crypto Analytics
  slug: nansen-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nansen.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.nansen.ai over HTTP.
  name: Nansen MCP Server
  slug: nansen
- description: Remote MCP server at mcp.nansen.ai over HTTP.
  name: Nansen MCP Server
  slug: nansen-2
modified: '2026-05-08'
name: Nansen
nav: Providers
network: true
overview: 'Nansen publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Smart Money API, and 1 more. Tagged areas include Web3, Cryptocurrency, Onchain, Wallet Labels, and Smart Money.


  The Nansen catalog on APIs.io includes 1 Spectral governance ruleset.


  Nansen''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Nansen Plans Pricing
  plan_count: 2
  slug: nansen-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Nansen Rate Limits
  slug: nansen-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Nansen API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: nansen-rules
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 42.9
    developer_ergonomics: 33.3
    discoverability: 75.0
    operational_transparency: 10.5
  previous_composite: 27.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 10.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/nansen/nansen-2026-06-20T185943.png
security:
- kind: authentication
  name: Nansen Authentication
  slug: nansen-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nansen Domain Security
  slug: nansen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nansen
tags:
- Web3
- Cryptocurrency
- Onchain
- Wallet Labels
- Smart Money
- Analytics
- Multi-Chain
- Ethereum
website: https://www.nansen.ai/
---
