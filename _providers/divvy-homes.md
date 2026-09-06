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
  url: https://www.divvyhomes.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.divvyhomes.com/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.divvyhomes.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.divvyhomes.com/terms
- group: auth
  title: ''
  type: DomainSecurity
  url: security/divvy-homes-domain-security.yml
created: '2026-07-17'
description: Divvy Homes is a San Francisco-based proptech company operating a rent-to-own home ownership program. A customer chooses a home on the open market, Divvy purchases it, and the customer moves in as a renter while a portion of each monthly payment builds toward a future down payment, giving aspiring buyers who are not yet mortgage-ready a path toward eventual ownership. The consumer web experience integrates third-party services such as Plaid for bank connectivity and Stripe for payments, but Divvy exposes no public developer API, developer portal, or API documentation surface of its own. This profile was surfaced from venture-portfolio data (a16z, Threshold Ventures) and enriched from Divvy's public consumer website only.
image: https://www.divvyhomes.com/apple-touch-icon.png
layout: provider
modified: '2026-07-18'
name: Divvy Homes
nav: Providers
network: true
overview: Divvy Homes is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Estate, PropTech, Rent-to-Own, and Homeownership.
random_paper: 13
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 2
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 10.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/divvy-homes/refs/heads/main/screenshots/divvy-homes-2026-07-25T212132.png
security:
- kind: domain-security
  name: Divvy Homes Domain Security
  slug: divvy-homes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: divvy-homes
tags:
- Company
- Real-Estate
- PropTech
- Rent-to-Own
- Homeownership
- Fintech
- Housing
website: https://www.divvyhomes.com/
---
