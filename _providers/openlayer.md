---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Openlayer Agentic Access
  operation_count: 24
  slug: openlayer-agentic-access
  summary_line: 24 operations · 14 acting
api_count: 6
apis:
- description: Project versions (commits) and their test results.
  name: Openlayer Commits API
  slug: openlayer-commits-api
- description: Publish production inference data to a pipeline.
  name: Openlayer Data Stream API
  slug: openlayer-data-stream-api
- description: Production monitoring pipelines and their rows, sessions, and users.
  name: Openlayer Inference Pipelines API
  slug: openlayer-inference-pipelines-api
- description: Create, list, and delete projects.
  name: Openlayer Projects API
  slug: openlayer-projects-api
- description: Presigned URLs for uploading datasets and artifacts.
  name: Openlayer Storage API
  slug: openlayer-storage-api
- description: Define, evaluate, and read project tests.
  name: Openlayer Tests API
  slug: openlayer-tests-api
artifact_total: 14
collections:
- collection_type: open
  name: Openlayer API
  slug: open-openlayer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openlayer-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/openlayer-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openlayer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openlayer-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openlayer-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openlayer
- group: company
  title: ''
  type: Website
  url: https://www.openlayer.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.openlayer.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/openlayer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openlayer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openlayer-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.openlayer.com/blog
created: '2026-06-20'
description: Openlayer is an AI evaluation, testing, and observability platform for machine learning and LLM applications. Its REST API lets teams create projects, commit model versions and datasets, run tests, stream production inference data into monitoring pipelines, and retrieve test results - with official SDKs generated from a Stainless OpenAPI definition.
finops:
- name: Openlayer Finops
  service_category: AI and Machine Learning
  slug: openlayer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openlayer.png
layout: provider
modified: '2026-06-20'
name: Openlayer
nav: Providers
network: true
overview: 'Openlayer publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Commits API, Data Stream API, Inference Pipelines API, and 3 more. Tagged areas include AI, Evaluation, Testing, Observability, and LLM.


  Openlayer''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Openlayer Plans Pricing
  plan_count: 2
  slug: openlayer-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 3
  name: Openlayer Rate Limits
  slug: openlayer-rate-limits
score:
  band: thin
  composite: 38.7
  delta: -2.2
  facets:
    commercial_clarity: 36.8
    contract_quality: 59.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openlayer/refs/heads/main/screenshots/openlayer-2026-06-20T191012.png
security:
- kind: authentication
  name: Openlayer Authentication
  slug: openlayer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openlayer Domain Security
  slug: openlayer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Openlayer Trust Center
  slug: openlayer-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: openlayer
tags:
- AI
- Evaluation
- Testing
- Observability
- LLM
- MLOps
website: https://www.openlayer.com
---
