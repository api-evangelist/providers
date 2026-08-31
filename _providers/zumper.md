---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Zumper API provides access to rental listings, property data, rental price insights, and tenant application management. Partners and property management software providers can use the API to syndi
  name: Zumper API
  slug: zumper-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zumper-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.zumper.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.zumper.com/blog/feed/
- group: operate
  title: ''
  type: Support
  url: https://help.zumper.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zumper.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zumper.com/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zumper
- group: other
  title: ''
  type: X
  url: https://x.com/Zumper
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/zumper/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/zumper/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/zumper/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Zumper is a rental listing marketplace that connects renters with landlords and property managers across the United States and Canada. The platform provides access to apartment listings, property data, rental price insights, and tenant application management. Zumper offers a REST API and syndication feeds enabling property management software providers and partners to publish listings, retrieve rental market data, and integrate tenant screening and leasing workflows. The platform processes over 76 million site visits annually and syndicates listings across PadMapper, ChatGPT, Microsoft Bing, and Realtor.com.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zumper.png
layout: provider
modified: '2026-06-13'
name: Zumper
nav: Providers
network: true
overview: 'Zumper publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, Rental Listings, Property Management, Apartments, and Tenant Screening.


  Zumper''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 8
  slug: plans
random_paper: 3
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zumper/refs/heads/main/screenshots/zumper-2026-06-20T201958.png
security:
- kind: domain-security
  name: Zumper Domain Security
  slug: zumper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zumper
tags:
- Real-Estate
- Rental Listings
- Property Management
- Apartments
- Tenant Screening
- Rental Market Data
- Housing
---
