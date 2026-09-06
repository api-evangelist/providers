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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wollit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wollit.com/
- group: operate
  title: ''
  type: Support
  url: https://www.wollit.com/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wollit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wollit.com/privacy-policy
created: '2026-07-17'
description: 'Wollit is a UK-based credit-health subscription service (£9.99/month) that helps consumers build and strengthen their credit profile. Authorised and regulated by the Financial Conduct Authority for credit-broking activities, Wollit reports rent and subscription payments to Experian, Equifax and TransUnion, and bundles a suite of consumer tools: Rent Reporting, Payment Reporting, an AI credit assistant (Olli), Affordability Boost, Credit Smart lessons, and Credit Wins. It is a consumer-facing fintech app and was surfaced as a portfolio company of Anthemis; it publishes no public API, developer portal, or SDKs.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wollit.png
layout: provider
modified: '2026-07-21'
name: Wollit
nav: Providers
network: true
overview: 'Wollit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Credit, Credit Building, and Personal Finance.


  Wollit''s developer surface includes support and 4 more developer resources.'
random_paper: 16
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
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 10.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wollit/refs/heads/main/screenshots/wollit-2026-09-02T170903.png
security:
- kind: domain-security
  name: Wollit Domain Security
  slug: wollit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wollit
tags:
- Company
- Fintech
- Credit
- Credit Building
- Personal Finance
- Consumer Finance
- United Kingdom
- Rent Reporting
website: https://www.wollit.com/
---
