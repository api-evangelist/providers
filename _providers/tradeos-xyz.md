---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: TradeOS provides AI‑powered trading APIs as described on the public website. No machine‑readable contract was found.
  name: TradeOS API
  slug: tradeos-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/tradeos-xyz/plans/tradeos-xyz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tradeos-xyz-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/tradeos-xyz/llms/tradeos-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tradeos-xyz-llms.txt
- group: agent
  href: https://artifacts.apis.io/tradeos-xyz/well-known/tradeos-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tradeos-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/tradeos-xyz/hosts/tradeos-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tradeos-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/tradeos-xyz/vendors/tradeos-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tradeos-xyz-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tradeos-xyz/security/tradeos-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tradeos-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tradeos.xyz/
- group: company
  title: ''
  type: Blog
  url: https://www.tradeos.xyz/blog
- group: start
  title: ''
  type: Login
  url: https://ai.tradeos.xyz/?utm_source=website&utm_medium=link&utm_campaign=2025
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tradeos.xyz/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ai.tradeos.xyz/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ai.tradeos.xyz/terms-of-service
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was discovered on any host.
  evidence:
  - status: 0
    url: https://api.tradeos.xyz/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: TradeOS provides an AI‑powered reasoning engine for financial markets, enabling traders and institutions to build autonomous trading agents that analyze charts, data, and strategies without coding. The platform integrates market data, technical indicators, and large language models to deliver explainable, 24/7 AI decision support across stocks, commodities, FX, and crypto. TradeOS offers a marketplace, pricing plans, and extensive documentation for building and deploying custom agents.
image: https://static.wixstatic.com/media/b34dfb_43a3f1f9844644c28904d9767831c266%7Emv2.jpeg/v1/fit/w_2500,h_1330,al_c/b34dfb_43a3f1f9844644c28904d9767831c266%7Emv2.jpeg
layout: provider
modified: '2026-10-30'
name: tradeos-xyz
nav: Providers
network: true
overview: 'tradeos-xyz is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Trading, Fintech, and Automation.


  tradeos-xyz''s developer surface includes engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Tradeos Xyz Plans Pricing
  plan_count: 4
  slug: tradeos-xyz-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 19.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tradeos-xyz/tradeos-xyz-2026-11-03T144959.png
security:
- kind: domain-security
  name: Tradeos Xyz Domain Security
  slug: tradeos-xyz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tradeos-xyz
tags:
- Company
- Artificial Intelligence
- Trading
- Fintech
- Automation
- Market Data
website: https://tradeos.xyz/
---
