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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: REST API for text-to-3D, image-to-3D, multi-image-to-3D, mesh refinement, retexturing, animation, and rigging. Async task-based pattern (POST /v2/openapi/task to submit, GET to poll) at https://api.tr
  name: Tripo3D API
  slug: platform
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tripo3d-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tripoai
- group: company
  title: ''
  type: Website
  url: https://www.tripo3d.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.tripo3d.ai/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/tripo3d-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tripo3d-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tripo3d-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tripo3d.ai/blog
created: '2026-05-08'
description: Tripo3D (by VAST) is an AI 3D generation platform with text-to-3D, image-to-3D, mesh refinement, and texturing APIs producing game-ready 3D assets. The Tripo API uses an async task-based REST pattern at https://api.tripo3d.ai/v2/openapi/task. Authenticate with API key.
finops:
- name: Tripo3D Finops
  service_category: AI
  slug: tripo3d-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tripo3d.png
layout: provider
modified: '2026-05-08'
name: Tripo3D
nav: Providers
network: true
overview: 'Tripo3D publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, 3D, Generation, API, and Mesh.


  Tripo3D''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Tripo3D Plans Pricing
  plan_count: 3
  slug: tripo3d-plans-pricing
random_paper: 113
rate_limits:
- limit_count: 3
  name: Tripo3D Rate Limits
  slug: tripo3d-rate-limits
score:
  band: emerging
  composite: 11.5
  delta: -1.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tripo3d/refs/heads/main/screenshots/tripo3d-2026-06-20T195747.png
security:
- kind: domain-security
  name: Tripo3D Domain Security
  slug: tripo3d-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tripo3d
tags:
- AI
- 3D
- Generation
- API
- Mesh
- Texturing
website: https://www.tripo3d.ai/
---
