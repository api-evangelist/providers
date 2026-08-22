---
access_model:
  confidence: high
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
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
- acting_count: 1
  human_in_the_loop: 0
  name: Coconut Agentic Access
  operation_count: 4
  slug: coconut-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 2
apis:
- description: Create and retrieve encoding jobs.
  name: Coconut Jobs API
  slug: coconut-jobs-api
- description: Retrieve technical metadata for input and output files.
  name: Coconut Metadata API
  slug: coconut-metadata-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Coconut Jobs API
  slug: open-coconut-jobs-api
- collection_type: open
  name: Coconut Jobs Metadata API
  slug: open-coconut-metadata-api
- collection_type: open
  name: Coconut API
  slug: open-coconut
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coconut-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coconut-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coconut-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opencoconut
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coconut-co
- group: company
  title: ''
  type: Website
  url: https://www.coconut.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coconut.co
- group: commercial
  title: ''
  type: Plans
  url: plans/coconut-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coconut-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/coconut-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.coconut.co/articles
created: '2026-06-20'
description: Coconut is a cloud video and audio encoding/transcoding service. The Coconut API v2 lets developers submit a single asynchronous job that transcodes source media into multiple formats, packages adaptive HLS/MPEG-DASH streams, and generates thumbnails and GIF animations, delivering results to cloud storage and reporting progress through webhooks.
finops:
- name: Coconut Finops
  service_category: Media and Content
  slug: coconut-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coconut.png
layout: provider
modified: '2026-06-20'
name: Coconut
nav: Providers
network: true
overview: 'Coconut publishes 2 APIs on the [APIs.io](https://apis.io/) network: Jobs API and Metadata API. Tagged areas include Video, Audio, Encoding, Transcoding, and Media.


  Coconut''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Coconut Plans Pricing
  plan_count: 2
  slug: coconut-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Coconut Rate Limits
  slug: coconut-rate-limits
score:
  band: thin
  composite: 36.4
  delta: -0.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 58.4
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coconut/refs/heads/main/screenshots/coconut-2026-06-20T174648.png
security:
- kind: authentication
  name: Coconut Authentication
  slug: coconut-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Coconut Domain Security
  slug: coconut-domain-security
  summary_line: TLSv1.3 · HSTS
slug: coconut
tags:
- Video
- Audio
- Encoding
- Transcoding
- Media
website: https://www.coconut.co
---
