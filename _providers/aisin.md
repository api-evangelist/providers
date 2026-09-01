---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aisin-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.aisin.com/en/aithink/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aisin_2
- group: company
  title: ''
  type: Website
  url: https://www.aisin.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/aisin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aisin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aisin-finops.yml
created: '2026-05-06'
description: Aisin Corporation is a Japanese global Tier 1 automotive supplier headquartered in Kariya, Aichi. Part of the Toyota Group, Aisin manufactures automatic transmissions, drivetrain components, body, chassis, and electronics for major automakers.
finops:
- name: Aisin Finops
  service_category: Industrial / Automotive
  slug: aisin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aisin.png
layout: provider
modified: '2026-05-06'
name: Aisin
nav: Providers
network: true
overview: 'Aisin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Tier 1 Supplier, Transmissions, Drivetrain, and Toyota Group.


  Aisin''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Aisin Plans Pricing
  plan_count: 1
  slug: aisin-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Aisin Rate Limits
  slug: aisin-rate-limits
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 14.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aisin/refs/heads/main/screenshots/aisin-2026-06-20T171439.png
security:
- kind: domain-security
  name: Aisin Domain Security
  slug: aisin-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aisin
tags:
- Automotive
- Tier 1 Supplier
- Transmissions
- Drivetrain
- Toyota Group
website: https://www.aisin.com/
---
