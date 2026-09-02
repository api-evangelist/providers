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
  url: security/wevat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wevat.com
- group: company
  title: ''
  type: Blog
  url: https://www.wevat.com/blog-en
- group: operate
  title: ''
  type: Support
  url: https://www.wevat.com/contact-en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wevat.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wevat.com/terms-and-conditions
created: '2026-07-17'
description: Wevat is a Seedcamp-backed fintech and travel-tech company operating a mobile app that digitizes VAT (Value Added Tax) refunds for international travellers shopping in France. Instead of paper tax-free forms, shoppers photograph their invoices in the Wevat app, which consolidates purchases across stores into a single digital tax-refund form, validates it at the departure point, and pays out the refund (up to around 13% of spend) in the traveller's chosen currency via credit card, bank transfer, Alipay, or WeChat Pay. Wevat is a consumer mobile-app product and does not currently publish a public developer API, SDK, or API documentation surface; this profile captures its public web and business identity.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wevat.png
layout: provider
modified: '2026-07-21'
name: Wevat
nav: Providers
network: true
overview: 'Wevat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, VAT Refund, and Tax-Free Shopping.


  Wevat''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Wevat Domain Security
  slug: wevat-domain-security
  summary_line: TLSv1.3 · HSTS
slug: wevat
tags:
- Company
- Fintech
- Payments
- VAT Refund
- Tax-Free Shopping
- Travel
- Mobile App
- Consumer
website: https://www.wevat.com
---
