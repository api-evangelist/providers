---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/refundid
- group: company
  title: ''
  type: Website
  url: https://www.refundid.com.au/
- group: commercial
  title: ''
  type: Plans
  url: plans/refundid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/refundid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/refundid-finops.yml
created: '2026-05-08'
description: Refundid is an instant-refund platform for e-commerce returns in Australia/NZ. Provides instant cash refund at the point of return initiation.
finops:
- name: Refundid Finops
  service_category: E-Commerce
  slug: refundid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/refundid.png
layout: provider
modified: '2026-05-08'
name: Refundid
nav: Providers
network: true
overview: Refundid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Returns, Refunds, Australia, and Post-Purchase.
plans:
- name: Refundid Plans Pricing
  plan_count: 1
  slug: refundid-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Refundid Rate Limits
  slug: refundid-rate-limits
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 4
    catalog_gap: 86.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 7.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
slug: refundid
tags:
- E-Commerce
- Returns
- Refunds
- Australia
- Post-Purchase
website: https://www.refundid.com.au/
---
