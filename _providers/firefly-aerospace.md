---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
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
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Firefly Aerospace
  slug: open-firefly-aerospace
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/firefly-aerospace-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/firefly-aerospace
- group: company
  title: ''
  type: Website
  url: https://fireflyspace.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fireflyspace.com/wp-content/uploads/2025/07/Alpha-PUG-5.2.pdf
- group: commercial
  title: ''
  type: Plans
  url: plans/firefly-aerospace-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/firefly-aerospace-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/firefly-aerospace-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://fireflyspace.com/news/
- group: other
  title: ''
  type: ProductPage
  url: https://fireflyspace.com/alpha/
- group: other
  title: ''
  type: ProductPage
  url: https://fireflyspace.com/eclipse/
- group: other
  title: ''
  type: ProductPage
  url: https://fireflyspace.com/blue-ghost/
- group: other
  title: ''
  type: ProductPage
  url: https://fireflyspace.com/elytra/
created: '2026-06-20'
description: Firefly Aerospace is an end-to-end space transportation company building the Alpha small-lift rocket, the Eclipse (formerly MLV) medium-lift vehicle, the Blue Ghost lunar lander, and the Elytra orbital vehicle (with the Ocula lunar imaging service). Firefly sells launch, lunar delivery, and on-orbit services through sales and payload-user-guide channels; it does not publish a public developer API.
finops:
- name: Firefly Aerospace Finops
  service_category: Space and Launch Services
  slug: firefly-aerospace-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/firefly-aerospace.png
layout: provider
modified: '2026-07-25'
name: Firefly Aerospace
nav: Providers
network: true
overview: 'Firefly Aerospace publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Space, Aerospace, Launch, Lunar, and Spacecraft.


  Firefly Aerospace''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Firefly Aerospace Plans Pricing
  plan_count: 0
  slug: firefly-aerospace-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Firefly Aerospace Rate Limits
  slug: firefly-aerospace-rate-limits
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 85.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/firefly-aerospace/refs/heads/main/screenshots/firefly-aerospace-2026-06-20T181231.png
security:
- kind: domain-security
  name: Firefly Aerospace Domain Security
  slug: firefly-aerospace-domain-security
  summary_line: TLSv1.3 · DMARC
slug: firefly-aerospace
tags:
- Space
- Aerospace
- Launch
- Lunar
- Spacecraft
website: https://fireflyspace.com/
---
