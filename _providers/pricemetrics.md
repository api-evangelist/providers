---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The PriceMetrics Pricing API provides programmatic access to price optimization recommendations, competitive price tracking, elasticity analysis, and revenue optimization insights. Clients submit tran
  name: PriceMetrics Pricing API
  slug: pricemetrics-pricing-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pricemetrics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pricimetrics.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.pricimetrics.com/documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/pricemetrics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pricimetrics
- group: company
  title: ''
  type: Blog
  url: https://www.pricimetrics.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pricimetrics.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pricemetrics.com
- group: other
  title: ''
  type: X
  url: https://x.com/pricemetrics
- group: commercial
  title: ''
  type: Plans
  url: plans/pricemetrics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pricemetrics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pricemetrics-finops.yml
created: '2026-06-13'
description: PriceMetrics is a price optimization and analytics platform that provides REST APIs for tracking competitive pricing data, performing elasticity analysis, and delivering revenue optimization recommendations. The platform enables businesses to integrate real-time pricing intelligence directly into their applications and workflows, supporting dynamic pricing strategies, margin analysis, and data-driven revenue management across retail, distribution, and manufacturing verticals.
finops:
- name: Pricemetrics Finops
  service_category: ''
  slug: pricemetrics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pricemetrics.png
layout: provider
modified: '2026-06-13'
name: PriceMetrics
nav: Providers
network: true
overview: 'PriceMetrics publishes 1 API on the [APIs.io](https://apis.io/) network: Pricing API. Tagged areas include Pricing, Price Optimization, Competitive Intelligence, Revenue Management, and Analytics.


  PriceMetrics'' developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Pricemetrics Plans Pricing
  plan_count: 4
  slug: pricemetrics-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Pricemetrics Rate Limits
  slug: pricemetrics-rate-limits
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 27.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pricemetrics/refs/heads/main/screenshots/pricemetrics-2026-06-20T192059.png
security:
- kind: domain-security
  name: Pricemetrics Domain Security
  slug: pricemetrics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pricemetrics
tags:
- Pricing
- Price Optimization
- Competitive Intelligence
- Revenue Management
- Analytics
- Elasticity Analysis
- Retail
- Commerce
website: https://www.pricimetrics.com
---
