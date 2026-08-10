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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Drone Ci Agentic Access
  operation_count: 17
  slug: drone-ci-agentic-access
  summary_line: 17 operations · 9 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: Bearer-token authenticated REST API exposed by every Drone server. Endpoints under /api/ for repos, builds, cron, secrets, users, templates, logs and queue status. Default port 8080.
  name: Drone Server REST API
  slug: rest
- description: The Builds API from Drone — 9 operation(s) for builds.
  name: Drone Builds API
  slug: drone-ci-builds-api
- description: The Cron API from Drone — 1 operation(s) for cron.
  name: Drone Cron API
  slug: drone-ci-cron-api
- description: The Secrets API from Drone — 1 operation(s) for secrets.
  name: Drone Secrets API
  slug: drone-ci-secrets-api
- description: The Templates API from Drone — 1 operation(s) for templates.
  name: Drone Templates API
  slug: drone-ci-templates-api
- description: The User API from Drone — 1 operation(s) for user.
  name: Drone User API
  slug: drone-ci-user-api
artifact_total: 13
collections:
- collection_type: open
  name: Drone CI REST API
  slug: open-drone-ci
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/drone-ci-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drone-ci-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/drone-ci-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drone-io
- group: company
  title: ''
  type: Website
  url: https://www.drone.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.drone.io/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/harness/drone
- group: other
  title: ''
  type: Owner
  url: https://www.harness.io/products/continuous-integration
- group: commercial
  title: ''
  type: Plans
  url: plans/drone-ci-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/drone-ci-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/drone-ci-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.harness.io/blog/rss.xml
created: '2026-05-08'
description: Drone is a container-native open-source continuous delivery platform owned by Harness. Pipelines are defined in YAML and executed in Docker containers. The Drone server exposes a REST API used by the Drone CLI, dashboard and SDKs; Drone is now positioned as the open-source upstream of Harness Continuous Integration (Drone Enterprise / Harness CI).
finops:
- name: Drone Ci Finops
  service_category: DevOps / CI/CD
  slug: drone-ci-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drone-ci.png
layout: provider
modified: '2026-05-08'
name: Drone
nav: Providers
network: true
overview: 'Drone publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Builds API, Cron API, Secrets API, and 2 more. Tagged areas include DevOps, CI/CD, Container-Native, Open Source, and YAML.


  Drone''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Drone Ci Plans Pricing
  plan_count: 2
  slug: drone-ci-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 3
  name: Drone Ci Rate Limits
  slug: drone-ci-rate-limits
score:
  band: thin
  composite: 35.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 53.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/drone-ci/refs/heads/main/screenshots/drone-ci-2026-06-20T180242.png
security:
- kind: authentication
  name: Drone Ci Authentication
  slug: drone-ci-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Drone Ci Domain Security
  slug: drone-ci-domain-security
  summary_line: TLSv1.3 · HSTS
slug: drone-ci
tags:
- DevOps
- CI/CD
- Container-Native
- Open Source
- YAML
- Harness
website: https://www.drone.io/
---
