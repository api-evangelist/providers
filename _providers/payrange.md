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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payrange-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.payrange.com
- group: operate
  title: ''
  type: Support
  url: https://support.payrange.com/hc/en-us/categories/360006635452-Operator-Support
- group: company
  title: ''
  type: Blog
  url: https://www.payrange.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.payrange.com/payrange-pricing-plans/
- group: start
  title: ''
  type: Login
  url: https://manage.payrange.com/
created: '2026-07-17'
description: PayRange is a fintech company providing cashless commerce and self-service retail technology for unattended machines. Its platform enables mobile payments, age and identity verification, and access control across laundromats, vending, car washes, campgrounds, hospitality, micro-markets, coffee, and transit ticketing. Hardware includes the BluKey family, BluCheck, and PayStation, paired with a consumer mobile app and an operator Business Management Suite. Backed by GV and Matrix Partners. No public developer API, documentation, or SDK surface was found during enrichment; integrations appear to run through direct partner and licensing channels.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/payrange.png
layout: provider
modified: '2026-07-20'
name: PayRange
nav: Providers
network: true
overview: 'PayRange is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Payments, Fintech, and Mobile Payments.


  PayRange''s developer surface includes support, engineering blog, pricing, and 3 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payrange/refs/heads/main/screenshots/payrange-2026-08-07T191653.png
security:
- kind: domain-security
  name: Payrange Domain Security
  slug: payrange-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: payrange
tags:
- Company
- Enterprise
- Payments
- Fintech
- Mobile Payments
- Unattended Retail
- Vending
- IoT
website: https://www.payrange.com
---
