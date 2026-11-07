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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/coinledger/plans/coinledger-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coinledger-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/coinledger/llms/coinledger-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinledger-llms.txt
- group: auth
  href: https://artifacts.apis.io/coinledger/well-known/coinledger-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coinledger-help-security.txt
- group: agent
  href: https://artifacts.apis.io/coinledger/well-known/coinledger-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coinledger-well-known.yml
- group: other
  href: https://artifacts.apis.io/coinledger/hosts/coinledger-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinledger-hosts.yml
- group: other
  href: https://artifacts.apis.io/coinledger/vendors/coinledger-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinledger-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.coinledger.io/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coinledger.io/
- group: auth
  href: https://artifacts.apis.io/coinledger/security/coinledger-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinledger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coinledger.io/
- group: docs
  title: ''
  type: Documentation
  url: https://coinledger.io/docs
- group: company
  title: ''
  type: Blog
  url: https://coinledger.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://coinledger.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://coinledger.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coinledger.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coinledger.io/privacy
coverage:
  checked: '2026-10-09'
  detail: Documentation pages return soft-404 "Page Not Found" without machine‑readable API spec.
  evidence:
  - status: 200
    url: https://coinledger.io/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: CoinLedger provides free crypto tax software that helps individuals and professionals generate tax reports for cryptocurrency transactions. Founded in 2018, the platform offers tools for portfolio tracking, NFT and DeFi tax calculations, and integrates with major exchanges. It aims to simplify crypto tax compliance for users worldwide, supporting multiple jurisdictions and offering both DIY and professional services.
image: https://cdn.prod.website-files.com/614c99cf4f23708b27a37503/65b27fbcb59958df9b71bf6e_CoinLedger%20Open%20Graph.png
layout: provider
modified: '2026-10-09'
name: CoinLedger
nav: Providers
network: true
overview: 'CoinLedger is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Tax, Finance, and Software.


  CoinLedger''s developer surface includes support, documentation, engineering blog, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Coinledger Plans Pricing
  plan_count: 4
  slug: coinledger-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 55.4
    operational_transparency: 18.4
  previous_composite: 27.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/coinledger/coinledger-2026-11-03T124823.png
security:
- kind: domain-security
  name: Coinledger Domain Security
  slug: coinledger-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: coinledger
tags:
- Company
- Cryptocurrency
- Tax
- Finance
- Software
website: https://coinledger.io/
---
