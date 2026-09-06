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
  url: security/sifi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sifi.app
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sifi.app/en/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.sifi.app/en/resources/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.sifi.app/en/support/get-help/
- group: start
  title: ''
  type: SignUp
  url: https://www.sifi.app/en/get-sifi/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sifi.app/en/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sifi.app/en/privacy-policy/
created: '2026-07-17'
description: SiFi (الحلول المبسطة المالية) is a Saudi Arabian fintech company offering a comprehensive corporate spend-management platform for businesses in the Kingdom. Licensed by the Saudi Central Bank (SAMA) and serving more than 5,000 clients, SiFi provides physical and virtual corporate cards with spending controls, real-time expense tracking, employee reimbursements, accounting automation, local vendor payments and international transfers (coming soon), and a cashback rewards program, delivered through web and iOS/Android mobile apps. SiFi is backed by QED Investors. No public developer API or documentation surface was found during this enrichment pass.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sifi.png
layout: provider
modified: '2026-07-21'
name: SiFi
nav: Providers
network: true
overview: 'SiFi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Spend Management, Corporate Cards, and Expense Management.


  SiFi''s developer surface includes pricing, engineering blog, support, signup flow, and 4 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - saudi-arabia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 13.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sifi/refs/heads/main/screenshots/sifi-2026-09-02T155411.png
security:
- kind: domain-security
  name: Sifi Domain Security
  slug: sifi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sifi
tags:
- Company
- Fintech
- Spend Management
- Corporate Cards
- Expense Management
- Payments
- Saudi Arabia
- Business
website: https://www.sifi.app
---
