---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
- acting_count: 30
  human_in_the_loop: 3
  name: Runloop Agentic Access
  operation_count: 49
  slug: runloop-agentic-access
  summary_line: 49 operations · 30 acting · 3 human-in-the-loop
api_count: 7
apis:
- description: Authenticated account information.
  name: Runloop Account API
  slug: runloop-account-api
- description: Group scenarios into benchmarks and run them.
  name: Runloop Benchmark API
  slug: runloop-benchmark-api
- description: Build reproducible devbox base images.
  name: Runloop Blueprint API
  slug: runloop-blueprint-api
- description: Create, manage and run commands in cloud devboxes.
  name: Runloop Devbox API
  slug: runloop-devbox-api
- description: Upload, list and download binary objects (blob storage).
  name: Runloop Object API
  slug: runloop-object-api
- description: Define and run coding-agent evaluation scenarios.
  name: Runloop Scenario API
  slug: runloop-scenario-api
- description: Manage devbox disk snapshots.
  name: Runloop Snapshot API
  slug: runloop-snapshot-api
artifact_total: 15
collections:
- collection_type: open
  name: Runloop API
  slug: open-runloop
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/runloop-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/runloop-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runloop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/runloop-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/runloopai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/runloopai
- group: company
  title: ''
  type: Website
  url: https://www.runloop.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runloop.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/runloop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/runloop-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/runloop-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://runloop.ai/blog
created: '2026-07-01'
description: Runloop provides AI-native cloud development environments (devboxes) and an agent benchmarking platform. The Runloop API lets you programmatically spin up isolated Linux devboxes, run and stream commands, mount code, snapshot state via blueprints and snapshots, and evaluate coding agents against scenarios and benchmarks - all over a Bearer-authenticated REST interface at api.runloop.ai/v1.
finops:
- name: Runloop Finops
  service_category: Compute
  slug: runloop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/runloop.png
layout: provider
modified: '2026-07-01'
name: Runloop
nav: Providers
network: true
overview: 'Runloop publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Benchmark API, Blueprint API, and 4 more. Tagged areas include AI, Developer Environments, Devboxes, Coding Agents, and Benchmarking.


  Runloop''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Runloop Plans Pricing
  plan_count: 5
  slug: runloop-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Runloop Rate Limits
  slug: runloop-rate-limits
score:
  band: thin
  composite: 38.9
  delta: -2.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Runloop Authentication
  slug: runloop-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Runloop Domain Security
  slug: runloop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Runloop Trust Center
  slug: runloop-trust-center
  summary_line: SOC 2, HIPAA, FedRAMP, GDPR
slug: runloop
tags:
- AI
- Developer Environments
- Devboxes
- Coding Agents
- Benchmarking
- Cloud IDE
website: https://www.runloop.ai/
---
