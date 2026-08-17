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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Colossyan Agentic Access
  operation_count: 10
  slug: colossyan-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 5
apis:
- description: List avatars/presenters and create custom Instant avatars.
  name: Colossyan Avatars API
  slug: colossyan-avatars-api
- description: Non-versioned, experimental endpoints subject to change.
  name: Colossyan Experimental API
  slug: colossyan-experimental-api
- description: Retrieve and delete completed videos.
  name: Colossyan Generated Videos API
  slug: colossyan-generated-videos-api
- description: Create and manage asynchronous video-generation jobs.
  name: Colossyan Video Generation API
  slug: colossyan-video-generation-api
- description: List available AI voices.
  name: Colossyan Voices API
  slug: colossyan-voices-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Colossyan Avatars API
  slug: open-colossyan-avatars-api
- collection_type: open
  name: Colossyan Avatars Experimental API
  slug: open-colossyan-experimental-api
- collection_type: open
  name: Colossyan Avatars Generated Videos API
  slug: open-colossyan-generated-videos-api
- collection_type: open
  name: Colossyan Avatars Video Generation API
  slug: open-colossyan-video-generation-api
- collection_type: open
  name: Colossyan Avatars Voices API
  slug: open-colossyan-voices-api
- collection_type: open
  name: Colossyan API
  slug: open-colossyan
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/colossyan-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/colossyan-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/colossyan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/colossyan-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/colossyan
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/colossyan
- group: company
  title: ''
  type: Website
  url: https://www.colossyan.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.colossyan.com
- group: commercial
  title: ''
  type: Plans
  url: plans/colossyan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/colossyan-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/colossyan-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.colossyan.com/blog
created: '2026-06-21'
description: Colossyan is an AI avatar and video generation platform for learning and development. Its REST API turns scripts into studio-quality videos with AI avatars and voices, lists avatars/presenters, voices and templates, supports instant avatar and voice clone creation, and exposes asynchronous video-generation jobs with webhook callbacks. API access requires a Business or Enterprise plan.
finops:
- name: Colossyan Finops
  service_category: AI and Machine Learning
  slug: colossyan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/colossyan.png
layout: provider
modified: '2026-06-21'
name: Colossyan
nav: Providers
network: true
overview: 'Colossyan publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Avatars API, Experimental API, Generated Videos API, and 2 more. Tagged areas include AI, Video Generation, Avatars, Text to Video, and Learning and Development.


  Colossyan''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Colossyan Plans Pricing
  plan_count: 5
  slug: colossyan-plans-pricing
random_paper: 93
rate_limits:
- limit_count: 4
  name: Colossyan Rate Limits
  slug: colossyan-rate-limits
score:
  band: thin
  composite: 40.6
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 58.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/colossyan/refs/heads/main/screenshots/colossyan-2026-07-25T210058.png
security:
- kind: authentication
  name: Colossyan Authentication
  slug: colossyan-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Colossyan Domain Security
  slug: colossyan-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Colossyan Trust Center
  slug: colossyan-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: colossyan
tags:
- AI
- Video Generation
- Avatars
- Text to Video
- Learning and Development
website: https://www.colossyan.com
---
