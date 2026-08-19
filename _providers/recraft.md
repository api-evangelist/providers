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
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Recraft Agentic Access
  operation_count: 19
  slug: recraft-agentic-access
  summary_line: 19 operations · 18 acting
api_count: 5
apis:
- description: REST API for raster and vector image generation (V4 Pro / V4 / V3 / V2), inpainting, image-to-image, background replacement, style creation, vectorization, upscaling (Crisp / Creative), background rem
  name: Recraft API
  slug: platform
- description: The Images API from Recraft — 16 operation(s) for images.
  name: Recraft Images API
  slug: recraft-images-api
- description: The Prompts API from Recraft — 1 operation(s) for prompts.
  name: Recraft Prompts API
  slug: recraft-prompts-api
- description: The Styles API from Recraft — 1 operation(s) for styles.
  name: Recraft Styles API
  slug: recraft-styles-api
- description: The Users API from Recraft — 1 operation(s) for users.
  name: Recraft Users API
  slug: recraft-users-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Recraft Images API
  slug: open-recraft-images-api
- collection_type: open
  name: Recraft Images Prompts API
  slug: open-recraft-prompts-api
- collection_type: open
  name: Recraft Images Styles API
  slug: open-recraft-styles-api
- collection_type: open
  name: Recraft Images Users API
  slug: open-recraft-users-api
- collection_type: open
  name: Recraft API
  slug: open-recraft
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/recraft-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/recraft-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/recraft-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recraft-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/recraft-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/recraft-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/recraftai
- group: company
  title: ''
  type: Website
  url: https://www.recraft.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.recraft.ai/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/recraft-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/recraft-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/recraft-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-05-08'
description: Recraft is an AI design platform offering raster and vector image generation, image editing, inpainting, background removal/generation, vectorization, upscaling, and style creation. The Recraft API is REST-based at https://external.api.recraft.ai/v1, compatible with the OpenAI Python client, and uses prepaid API Units billed at 1,000 units = $1.
finops:
- name: Recraft Finops
  service_category: AI
  slug: recraft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recraft.png
layout: provider
modified: '2026-05-30'
name: Recraft
nav: Providers
network: true
overview: 'Recraft publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Images API, Prompts API, and 3 more. Tagged areas include AI, Image Generation, Design, Vector, and Style.


  Recraft''s developer surface includes authentication, documentation, and 11 more developer resources.'
plans:
- name: Recraft Plans Pricing
  plan_count: 1
  slug: recraft-plans-pricing
random_paper: 147
rate_limits:
- limit_count: 2
  name: Recraft Rate Limits
  slug: recraft-rate-limits
score:
  band: thin
  composite: 29.2
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 46.2
    developer_ergonomics: 21.4
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 29.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/recraft/refs/heads/main/screenshots/recraft-2026-06-20T192705.png
security:
- kind: authentication
  name: Recraft Authentication
  slug: recraft-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Recraft Domain Security
  slug: recraft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Recraft Vulnerability Disclosure
  slug: recraft-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Recraft Trust Center
  slug: recraft-trust-center
  summary_line: SOC 2, GDPR
slug: recraft
tags:
- AI
- Image Generation
- Design
- Vector
- Style
website: https://www.recraft.ai/
---
