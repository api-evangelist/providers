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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Beam Cloud Agentic Access
  operation_count: 6
  slug: beam-cloud-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 3
apis:
- description: The Task Queues API from Beam — 1 operation(s) for task queues.
  name: Beam Task Queues API
  slug: beam-cloud-task-queues-api
- description: The Tasks API from Beam — 2 operation(s) for tasks.
  name: Beam Tasks API
  slug: beam-cloud-tasks-api
- description: The Web Endpoints API from Beam — 3 operation(s) for web endpoints.
  name: Beam Web Endpoints API
  slug: beam-cloud-web-endpoints-api
artifact_total: 12
asyncapis:
- description: AsyncAPI 2.6 description of Beam's **realtime endpoint** surface. Unlike the synchronous REST web endpoints, a Beam realtime app is deployed and, per the docs (https://docs.beam.cloud/v2/endpoint/real
  name: Beam Realtime Endpoints (WebSocket)
  slug: beam-cloud-asyncapi
collections:
- collection_type: open
  name: Beam API
  slug: open-beam-cloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/beam-cloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beam-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beam-cloud-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.beam.cloud/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/beam-cloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beam-cloud
- group: company
  title: ''
  type: Website
  url: https://www.beam.cloud
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beam.cloud
- group: commercial
  title: ''
  type: Plans
  url: plans/beam-cloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/beam-cloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/beam-cloud-finops.yml
created: '2026-06-20'
description: Beam (beam.cloud) is a serverless GPU and Python cloud-runtime platform. You write ordinary Python, decorate it, and Beam deploys it as a web endpoint, a task queue, a scheduled job, or a secure sandbox running on on-demand CPU and GPU containers with per-second billing, rapid cold starts, and automatic scaling.
finops:
- name: Beam Cloud Finops
  service_category: Compute
  slug: beam-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beam-cloud.png
layout: provider
modified: '2026-06-20'
name: Beam
nav: Providers
network: true
overview: 'Beam publishes 3 APIs on the [APIs.io](https://apis.io/) network: Task Queues API, Tasks API, and Web Endpoints API. Tagged areas include Serverless, GPU, Python, Inference, and Containers.


  The Beam catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Beam''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Beam Cloud Plans Pricing
  plan_count: 5
  slug: beam-cloud-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 4
  name: Beam Cloud Rate Limits
  slug: beam-cloud-rate-limits
rules:
- name: Beam API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: beam-cloud-asyncapi-spectral-rules
score:
  band: developing
  composite: 45.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 73.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 45.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beam-cloud/refs/heads/main/screenshots/beam-cloud-2026-06-20T173120.png
security:
- kind: authentication
  name: Beam Cloud Authentication
  slug: beam-cloud-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Beam Cloud Domain Security
  slug: beam-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beam-cloud
tags:
- Serverless
- GPU
- Python
- Inference
- Containers
website: https://www.beam.cloud
---
