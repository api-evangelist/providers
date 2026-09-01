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
  url: security/baletu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://baletu.com/
- group: start
  title: ''
  type: Login
  url: http://partner.baletu.com/login
created: '2026-07-17'
description: Baletu (巴乐兔) is a landlord-direct online residential rental platform operated by Shanghai Wanjian Information Technology Co., Ltd. Founded in 2012 and based in Shanghai, it lets tenants rent apartments directly from landlords with monthly-payment ("月付") options, reducing agency fees. The platform spans first-tier Chinese cities including Beijing, Shanghai, and Shenzhen plus more than ten second-tier cities, listing over one million properties. Baletu is a consumer proptech company backed by DCM Ventures, Tiantu Capital, Nan Fung Group, and ZWC Partners, having raised roughly $140M through a 2018 Series C. It ships consumer iOS/Android apps and a partner portal; it does not publish a public developer API program (api.baletu.com serves its own apps).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/baletu.png
layout: provider
modified: '2026-07-18'
name: Baletu
nav: Providers
network: true
overview: Baletu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Real-Estate, Rental Housing, and PropTech.
random_paper: 7
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/baletu/refs/heads/main/screenshots/baletu-2026-07-25T202315.png
security:
- kind: domain-security
  name: Baletu Domain Security
  slug: baletu-domain-security
  summary_line: no transport/DNS hardening detected
slug: baletu
tags:
- Company
- Consumer
- Real-Estate
- Rental Housing
- PropTech
- Marketplace
- China
- Mobile
website: https://baletu.com/
---
