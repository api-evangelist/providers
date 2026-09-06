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
  url: https://ftcash.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ftcash.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ftcash.com/terms
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ft-cash-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ft-cash-llms.txt
created: '2026-07-17'
description: FTCash (ftcash) is a Mumbai, India based financial services / fintech company focused on financial inclusion for micro-merchants and small and medium enterprises (SMEs). It provides digital payment acceptance and working-capital business loans to small offline retailers and merchants who are typically underserved by traditional banking, enabling them to accept digital payments and access short-term credit. FTCash was surfaced as a portfolio company of 500 Global (500 Startups) and added to the API Evangelist network. At this time FTCash operates a public marketing website but publishes no public developer program, API documentation, or machine-readable API artifacts, so this profile is limited to verified company identity plus a live domain-security probe.
image: https://www.ftcash.com/instant_loans/img/ftcash-color.png
layout: provider
modified: '2026-07-19'
name: FT Cash
nav: Providers
network: true
overview: FT Cash is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Payments, and Lending.
random_paper: 6
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 8.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ft-cash/refs/heads/main/screenshots/ft-cash-2026-07-25T215246.png
security:
- kind: domain-security
  name: Ft Cash Domain Security
  slug: ft-cash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ft-cash
tags:
- Company
- Financial-Services
- Fintech
- Payments
- Lending
- SME
- Financial Inclusion
- India
website: https://ftcash.com
---
