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
  url: security/peddlr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://peddlr.io
- group: company
  title: ''
  type: Blog
  url: https://peddlr.io/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://learn.peddlr.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://peddlr.io/peddlr-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://peddlr.io/terms-conditions
created: '2026-07-17'
description: Peddlr is a Philippine fintech startup offering free mobile point-of-sale (POS) and bookkeeping software for Filipino micro, small, and medium businesses (MSMEs). Its app spans sales recording, offline inventory management, expense tracking, cash and credit ledgers, bills payment, QRPH, e-loading and gaming pins, a payment ledger, and accounting reports, with over two million downloads across 1,400+ cities and municipalities. Peddlr is registered with the Bangko Sentral ng Pilipinas as an Operator of Payment Systems. The company publishes no public developer program or API at this time; this profile captures its identity, published web properties, and domain-security posture for the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peddlr.png
layout: provider
modified: '2026-07-20'
name: Peddlr
nav: Providers
network: true
overview: 'Peddlr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Point-of-Sale, Payments, and Small Business.


  Peddlr''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
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
    - southeast-asia
  previous_composite: 2.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peddlr/refs/heads/main/screenshots/peddlr-2026-09-02T150940.png
security:
- kind: domain-security
  name: Peddlr Domain Security
  slug: peddlr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: peddlr
tags:
- Company
- Fintech
- Point-of-Sale
- Payments
- Small Business
- Philippines
- Bookkeeping
- Mobile
website: https://peddlr.io
---
