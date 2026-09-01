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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for image-to-3D, text-to-3D, and 3D world generation/simulation. API access is gated by CSM subscription plan tier. Documentation at https://docs.csm.ai/.
  name: CSM 3D Generation API
  slug: platform
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/csm-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/common-sense-machines
- group: company
  title: ''
  type: Website
  url: https://www.csm.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.csm.ai/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/CommonSenseMachines
- group: commercial
  title: ''
  type: Plans
  url: plans/csm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/csm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/csm-finops.yml
created: '2026-05-08'
description: Common Sense Machines (CSM) builds 3D world models with image-to-3D and 3D world simulation APIs aimed at games, robotics, and synthetic data. The CSM Cube product family released a single-click model pipeline with mesh-parts-based topology in early 2026. API access is bundled with mid-tier and enterprise CSM subscription plans.
finops:
- name: Csm Finops
  service_category: AI
  slug: csm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/csm.png
layout: provider
modified: '2026-05-08'
name: Common Sense Machines
nav: Providers
network: true
overview: 'Common Sense Machines publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, 3D, World Models, Scene Generation, and Generative.


  Common Sense Machines'' developer surface includes documentation, GitHub presence, and 6 more developer resources.'
plans:
- name: Csm Plans Pricing
  plan_count: 3
  slug: csm-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Csm Rate Limits
  slug: csm-rate-limits
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 15.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Csm Domain Security
  slug: csm-domain-security
  summary_line: DMARC
slug: csm
tags:
- Artificial Intelligence
- 3D
- World Models
- Scene Generation
- Generative
- Robotics
website: https://www.csm.ai/
---
