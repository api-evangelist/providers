---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/keyrock-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keyrock-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://keyrock.com/
- group: company
  title: ''
  type: About
  url: https://keyrock.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://keyrock.com/knowledge-hub/
- group: operate
  title: ''
  type: Support
  url: https://keyrock.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://keyrock.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://keyrock.com/privacy-complaints-notice/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KeyrockEU
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keyrock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keyrock-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/keyrock-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/keyrock-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/keyrock-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/keyrock-plans-pricing.yml
coverage:
  checked: '2026-08-23'
  detail: Keyrock's own Yoast-generated llms.txt (HTTP 200) enumerates every public page on keyrock.com — five services, the FAQ, knowledge hub, testimonials, legal and about — and contains no developer, API, documentation or sign-up entry; the firm sells market making, OTC, options and onchain liquidity under bilateral contracts and reports to clients through a credentialed dashboard, so there is no public contract to harvest.
  evidence:
  - status: 200
    url: https://keyrock.com/llms.txt
  - status: 404
    url: https://keyrock.com/.well-known/api-catalog
  - status: 403
    url: https://keyrock.com/openapi.json
  - status: 404
    url: https://keyrock.com/.well-known/agent-card.json
  - status: 403
    url: https://trust.keyrock.com/
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: 'Keyrock is a digital asset market maker and liquidity provider founded in Brussels in 2017 and now operating as a global crypto investment group. It runs in-house algorithmic and high-frequency trading infrastructure to supply market making, over-the-counter (OTC) trading, an options desk, onchain/DEX liquidity, validator services, ecosystem development and a Smart Beta fund to token issuers, exchanges, brokerages and institutional counterparties across 85+ centralised and decentralised venues. Keyrock also publishes proprietary crypto, FX, commodity and US equity pricing into the Pyth Network oracle. Its commercial surface is bilateral rather than self-serve: engagements are contracted, and clients receive execution analytics and PnL attribution through a credentialed dashboard. As of this profiling round Keyrock publishes no public developer portal, API reference or machine-readable contract of any kind. The group holds a MiCA licence through its French entity Keyrock FR
  SAS and has publicly announced SOC 2 Type II compliance.'
image: https://avatars.githubusercontent.com/u/41155949?v=4
layout: provider
modified: '2026-08-23'
name: Keyrock
nav: Providers
network: true
overview: 'Keyrock is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Market Making, Liquidity, Digital Assets, and Cryptocurrency.


  Keyrock''s developer surface includes engineering blog, support, and 13 more developer resources.'
plans:
- name: Keyrock Plans Pricing
  plan_count: 0
  slug: keyrock-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 19.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keyrock/refs/heads/main/screenshots/keyrock-2026-09-02T150032.png
security:
- kind: domain-security
  name: Keyrock Domain Security
  slug: keyrock-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Keyrock Trust Center
  slug: keyrock-trust-center
  summary_line: SOC 2 Type 2, DORA
slug: keyrock
tags:
- Company
- Market Making
- Liquidity
- Digital Assets
- Cryptocurrency
- Trading
- OTC
- Options
- Market Data
- Financial-Services
website: https://keyrock.com/
---
