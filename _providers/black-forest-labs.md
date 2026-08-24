---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Black Forest Labs Agentic Access
  operation_count: 13
  slug: black-forest-labs-agentic-access
  summary_line: 13 operations · 9 acting
api_count: 4
apis:
- description: REST API for asynchronous image generation across the Flux model family. Submit a generation request, then poll the returned polling_url for the result. Global endpoint at https://api.bfl.ai with regi
  name: Flux Image Generation API
  slug: flux
- description: Image editing tools (fill, expand, erase).
  name: Black Forest Labs Editing API
  slug: black-forest-labs-editing-api
- description: Image generation endpoints.
  name: Black Forest Labs Generation API
  slug: black-forest-labs-generation-api
- description: Result polling, credits, fine-tune management.
  name: Black Forest Labs Utility API
  slug: black-forest-labs-utility-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Black Forest Labs FLUX Editing API
  slug: open-black-forest-labs-editing-api
- collection_type: open
  name: Black Forest Labs FLUX Editing Generation API
  slug: open-black-forest-labs-generation-api
- collection_type: open
  name: Black Forest Labs FLUX Editing Utility API
  slug: open-black-forest-labs-utility-api
- collection_type: open
  name: Black Forest Labs FLUX API
  slug: open-black-forest-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/black-forest-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/black-forest-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/black-forest-labs-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bflai
- group: company
  title: ''
  type: Website
  url: https://blackforestlabs.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bfl.ai/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/black-forest-labs
- group: commercial
  title: ''
  type: Plans
  url: plans/black-forest-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/black-forest-labs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/black-forest-labs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://bfl.ai/blog
created: '2026-05-08'
description: Black Forest Labs is the company behind the Flux family of image generation models. The Flux API exposes asynchronous image generation endpoints via global and regional base URLs with model-named paths (e.g. /v1/flux-2-pro). Models include FLUX.2 (flex/pro/max/klein), FLUX.1 Kontext, FLUX1.1 [pro] Ultra, FLUX1.1 [pro], FLUX.1 Fill, and FLUX Schnell. Auth via BFL_API_KEY bearer token.
finops:
- name: Black Forest Labs Finops
  service_category: AI
  slug: black-forest-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/black-forest-labs.png
layout: provider
modified: '2026-05-08'
name: Black Forest Labs
nav: Providers
network: true
overview: 'Black Forest Labs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Editing API, Generation API, and Utility API. Tagged areas include Artificial Intelligence, Image-Generation, Flux, Open Weights, and BFL.


  Black Forest Labs'' developer surface includes authentication, documentation, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Black Forest Labs Plans Pricing
  plan_count: 2
  slug: black-forest-labs-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Black Forest Labs Rate Limits
  slug: black-forest-labs-rate-limits
score:
  band: thin
  composite: 30.1
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 52.7
    developer_ergonomics: 23.8
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/black-forest-labs/refs/heads/main/screenshots/black-forest-labs-2026-06-20T173409.png
security:
- kind: authentication
  name: Black Forest Labs Authentication
  slug: black-forest-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Black Forest Labs Domain Security
  slug: black-forest-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: black-forest-labs
tags:
- Artificial Intelligence
- Image-Generation
- Flux
- Open Weights
- BFL
website: https://blackforestlabs.ai/
---
