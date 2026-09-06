---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.remitbee.com
- group: operate
  title: ''
  type: Support
  url: https://www.remitbee.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.remitbee.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.remitbee.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.remitbee.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/remitbee-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/remitbee-domain-security.yml
created: '2026-07-17'
description: Remitbee is a Canadian licensed money-services business (FINTRAC-regulated, founded 2014, Mississauga, Ontario) offering low-cost international money transfers from Canada to 100+ countries across 89 published corridors, along with CAD/USD currency exchange, mobile top-ups / recharge, international bill payments, gift cards, travel eSIMs, and business money-transfer accounts. Customers fund transfers via Interac e-Transfer, EFT bank transfer, bill payment, or debit card, with zero fees on transfers above $500 CAD and live, transparent exchange rates. Remitbee operates consumer web and iOS/Android apps; it exposes partner/embedded integration APIs but publishes no public self-serve developer portal, OpenAPI, or OAuth surface. It does publish a /llms.txt agent-ingestion index of its corridor pages. Added to the API Evangelist network as a 500 Global portfolio company.
image: https://www.remitbee.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: Remitbee
nav: Providers
network: true
overview: 'Remitbee is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Money Transfer, Remittances, Currency Exchange, and Payments.


  Remitbee''s developer surface includes support, engineering blog, and 5 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/remitbee/refs/heads/main/screenshots/remitbee-2026-09-02T153358.png
security:
- kind: domain-security
  name: Remitbee Domain Security
  slug: remitbee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: remitbee
tags:
- Company
- Money Transfer
- Remittances
- Currency Exchange
- Payments
- Fintech
- Cross-Border Payments
- Mobile Top-Up
- Bill Payments
- Canada
website: https://www.remitbee.com
---
