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
- group: company
  title: ''
  type: Website
  url: http://www.livingsocial.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.livingsocial.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.livingsocial.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.livingsocial.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.livingsocial.com/privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/livingsocial-domain-security.yml
created: '2026-07-17'
description: 'LivingSocial is a consumer daily-deals and local-experiences marketplace that sells discounted vouchers and offers across travel, events, dining, activities, and products, alongside a coupon and promo-code section for major retailers. Originally a pioneering group-buying company, its brand and marketplace now operate as an affiliate deals and coupons destination. It was surfaced as a portfolio company of Insight Partners and added to the API Evangelist network. As of this enrichment pass the public site (livingsocial.com) exposes no developer program, API, or documentation surface: probes of common developer subdomains (developer/api/docs) and /.well-known/ discovery endpoints returned redirects to the consumer site or 404s.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/livingsocial.png
layout: provider
modified: '2026-07-20'
name: LivingSocial
nav: Providers
network: true
overview: 'LivingSocial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Deals, Coupons, and E-Commerce.


  LivingSocial''s developer surface includes signup flow, support, and 4 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/livingsocial/refs/heads/main/screenshots/livingsocial-2026-07-25T225414.png
security:
- kind: domain-security
  name: Livingsocial Domain Security
  slug: livingsocial-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: livingsocial
tags:
- Company
- Consumer
- Deals
- Coupons
- E-Commerce
- Local
- Marketplace
website: http://www.livingsocial.com/
---
