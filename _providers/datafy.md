---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - https://www.datafy.com/pricing
  - https://www.datafy.com/docs
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The Datafy Data API is a beta JSON-over-HTTP reporting API that returns aggregated visitation analytics for a destination. It is RPC-shaped rather than resource-shaped: three fixed endpoints, with the'
  name: Datafy Data API
  slug: datafy-data-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datafy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/datafy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/datafy-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/datafy-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/datafy-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/datafy-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datafy-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/datafy-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/datafy-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/datafy-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/datafy-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/datafy-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.datafy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.datafy.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.datafy.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.datafy.com/pixel/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datafy.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.datafy.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datafy.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.datafy.com/contact
- group: start
  title: ''
  type: Login
  url: https://portal.datafy.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datafy-hq/
- group: company
  title: ''
  type: Careers
  url: https://www.datafy.com/careers
- group: other
  title: ''
  type: DoNotSell
  url: https://www.datafy.com/opt-out
- group: commercial
  title: ''
  type: PrivacyMetrics
  url: https://www.datafy.com/ccpa-metrics
created: '2026-07-17'
description: Datafy is a location-analytics and advertising platform, founded in 2018 and headquartered in Ogden, Utah, that helps destinations and communities turn visitation, spending, and behavioral signals into marketing decisions. It serves travel and tourism boards, attractions, downtowns, retail partners, and civic organizations with three core offerings — data analytics, targeted advertising, and real-world attribution — alongside Tally, a hardware attendance-measurement sensor. Datafy does publish a public API reference at https://www.datafy.com/docs covering the Datafy Data API, a self-described beta JSON-over-HTTP reporting API at api.datafy.com with three endpoints (data, options, progress), authenticated by a 30-day portal-issued bearer JWT that a customer-experience representative must unlock before the API Access page becomes visible. No OpenAPI, SDK, package, or self-service signup is published, and the company's widest developer-touching surface is its per-customer measurement
  tag family — website pixel, 1x1 media impression pixels, and click tags. The company reports 500+ clients and holds a SOC 2 Type II certification from A-LIGN.
image: https://www.datafy.com/favicon.ico
layout: provider
modified: '2026-08-12'
name: Datafy
nav: Providers
network: true
overview: 'Datafy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Advertising, Location Intelligence, and Attribution.


  Datafy''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 18 more developer resources.'
plans:
- name: Datafy Plans Pricing
  plan_count: 0
  slug: datafy-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Datafy Rate Limits
  slug: datafy-rate-limits
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 26.4
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datafy/refs/heads/main/screenshots/datafy-2026-07-25T211320.png
security:
- kind: authentication
  name: Datafy Authentication
  slug: datafy-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Datafy Domain Security
  slug: datafy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datafy
tags:
- Company
- Analytics
- Advertising
- Location Intelligence
- Attribution
- Tourism
- Marketing
- Visitation Data
- Destination Marketing
- Measurements
website: https://www.datafy.com/
---
