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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: APILayer (formerly Any-API) is a curated marketplace of reliable and scalable APIs for developers. Offers a unified dashboard, single billing subscription, API sandboxing, SDK generation, and monitori
  name: APILayer Marketplace API
  slug: apilayer-marketplace-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/any-api-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://apilayer.com
- group: other
  title: ''
  type: Marketplace
  url: https://apilayer.com/marketplace
- group: commercial
  title: ''
  type: Pricing
  url: https://apilayer.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://apilayer.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apilayer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apilayer.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://apilayer.com/blog/feed/
created: '2026-03-26'
description: Any-API was a directory and documentation platform for discovering and testing public APIs with interactive Swagger-based API explorers. The domain now redirects to APILayer, a curated API marketplace offering reliable and scalable APIs across categories including AI, finance, content, and data. APILayer provides a unified developer experience with sandboxing, SDKs, and a single subscription for access to multiple API products.
finops:
- name: Any Api Finops
  service_category: API
  slug: any-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/any-api.png
layout: provider
modified: '2026-04-19'
name: Any-API
nav: Providers
network: true
overview: 'Any-API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Directory, API Explorer, API Marketplace, and Developer Tools.


  Any-API''s developer surface includes developer portal, pricing, signup flow, engineering blog, and 4 more developer resources.'
plans:
- name: Any Api Plans Pricing
  plan_count: 3
  slug: any-api-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Any Api Rate Limits
  slug: any-api-rate-limits
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 15.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/any-api/refs/heads/main/screenshots/any-api-2026-06-20T172031.png
security:
- kind: domain-security
  name: Any Api Domain Security
  slug: any-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: any-api
tags:
- API Directory
- API Explorer
- API Marketplace
- Developer Tools
website: https://apilayer.com
---
