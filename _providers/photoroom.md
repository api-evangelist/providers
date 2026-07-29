---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Photoroom Agentic Access
  operation_count: 7
  slug: photoroom-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 4
apis:
- description: The Account API from Photoroom — 2 operation(s) for account.
  name: Photoroom Account API
  slug: photoroom-account-api
- description: The Edit API from Photoroom — 1 operation(s) for edit.
  name: Photoroom Edit API
  slug: photoroom-edit-api
- description: The Render API from Photoroom — 1 operation(s) for render.
  name: Photoroom Render API
  slug: photoroom-render-api
- description: The Segment API from Photoroom — 1 operation(s) for segment.
  name: Photoroom Segment API
  slug: photoroom-segment-api
artifact_total: 11
collections:
- collection_type: open
  name: Photoroom API
  slug: open-photoroom
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/photoroom-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/photoroom-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/photoroom-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Photoroom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/photoroom
- group: company
  title: ''
  type: Website
  url: https://www.photoroom.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.photoroom.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/photoroom-openapi.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/photoroom-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/photoroom-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/photoroom-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.photoroom.com/llms.txt
created: '2026-05-08'
description: Photoroom is an AI image editing platform with strong background removal and e-commerce-style product photo generation. Public APIs include the Remove Background API and the Image Editing API (Plus plan), with specialized endpoints for PhotoFix, Reposition, Product Beautifier, Analyze QA, Image to Video, Photo Composition, Virtual Model, Flat Lay, and Ghost Mannequin. OpenAPI spec is published.
finops:
- name: Photoroom Finops
  service_category: AI
  slug: photoroom-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/photoroom.png
layout: provider
modified: '2026-05-19'
name: Photoroom
nav: Providers
network: true
overview: 'Photoroom publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Edit API, Render API, and 1 more. Tagged areas include AI, Image Editing, Background Removal, E-commerce, and Visual.


  Photoroom''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Photoroom Plans Pricing
  plan_count: 5
  slug: photoroom-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 3
  name: Photoroom Rate Limits
  slug: photoroom-rate-limits
score:
  band: thin
  composite: 38.6
  delta: -3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/photoroom/refs/heads/main/screenshots/photoroom-2026-06-20T191651.png
security:
- kind: authentication
  name: Photoroom Authentication
  slug: photoroom-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Photoroom Domain Security
  slug: photoroom-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: photoroom
tags:
- AI
- Image Editing
- Background Removal
- E-commerce
- Visual
website: https://www.photoroom.com/
---
