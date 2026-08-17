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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Pika Labs Agentic Access
  operation_count: 5
  slug: pika-labs-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 5
apis:
- description: Pika's video generation models are exposed through the fal.ai inference platform. Use fal.ai's standard REST submission + polling API to access Pika models.
  name: Pika via fal.ai
  slug: fal
- description: Cancel an in-flight request.
  name: Pika Labs Cancel API
  slug: pika-labs-cancel-api
- description: Retrieve the result of a completed request.
  name: Pika Labs Result API
  slug: pika-labs-result-api
- description: Inspect request status.
  name: Pika Labs Status API
  slug: pika-labs-status-api
- description: Submit inference requests.
  name: Pika Labs Submission API
  slug: pika-labs-submission-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pika Labs via fal.ai Queue Cancel API
  slug: open-pika-labs-cancel-api
- collection_type: open
  name: Pika Labs via fal.ai Queue Cancel Result API
  slug: open-pika-labs-result-api
- collection_type: open
  name: Pika Labs via fal.ai Queue Cancel Status API
  slug: open-pika-labs-status-api
- collection_type: open
  name: Pika Labs via fal.ai Queue Cancel Submission API
  slug: open-pika-labs-submission-api
- collection_type: open
  name: Pika Labs via fal.ai Queue API
  slug: open-pika-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pika-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pika-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pika-labs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pika-Labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pika-labs
- group: company
  title: ''
  type: Website
  url: https://pika.art/
- group: docs
  title: ''
  type: Documentation
  url: https://fal.ai/models?keywords=pika
- group: commercial
  title: ''
  type: Plans
  url: plans/pika-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pika-labs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pika-labs-finops.yml
created: '2026-05-08'
description: Pika Labs is an AI video generation platform offering text-to-video, image-to-video, and video editing capabilities. As of May 2026 Pika does not publish a first-party REST API on its main domain; production API access is provided through partner aggregators (notably fal.ai) which host hosted endpoints for Pika models.
finops:
- name: Pika Labs Finops
  service_category: AI
  slug: pika-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pika-labs.png
layout: provider
modified: '2026-05-08'
name: Pika Labs
nav: Providers
network: true
overview: 'Pika Labs publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cancel API, Result API, Status API, and 1 more. Tagged areas include AI, Video Generation, Text-to-Video, Multimodal, and Generative.


  Pika Labs'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Pika Labs Plans Pricing
  plan_count: 2
  slug: pika-labs-plans-pricing
random_paper: 139
rate_limits:
- limit_count: 1
  name: Pika Labs Rate Limits
  slug: pika-labs-rate-limits
score:
  band: thin
  composite: 30.0
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 58.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pika-labs/refs/heads/main/screenshots/pika-labs-2026-06-20T191707.png
security:
- kind: authentication
  name: Pika Labs Authentication
  slug: pika-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pika Labs Domain Security
  slug: pika-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pika-labs
tags:
- AI
- Video Generation
- Text-to-Video
- Multimodal
- Generative
website: https://pika.art/
---
