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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Travis Ci Agentic Access
  operation_count: 24
  slug: travis-ci-agentic-access
  summary_line: 24 operations · 12 acting
api_count: 8
apis:
- description: Current REST API used by the Travis CI web UI. 50+ resource types covering builds, jobs, repositories, users, organizations, crons, caches, environment variables, requests and config validation. Hyper
  name: Travis CI REST API v3
  slug: v3
- description: Legacy v2/v2.1 REST API; superseded by v3 but still in use. Builds, jobs, branches, logs, env vars, caches, SSH keys, requests. Authenticated via Bearer access tokens exchanged with GitHub.
  name: Travis CI REST API v2.1 (deprecated)
  slug: v2
- description: The Builds API from Travis CI — 3 operation(s) for builds.
  name: Travis CI Builds API
  slug: travis-ci-builds-api
- description: The Jobs API from Travis CI — 4 operation(s) for jobs.
  name: Travis CI Jobs API
  slug: travis-ci-jobs-api
- description: The Logs API from Travis CI — 1 operation(s) for logs.
  name: Travis CI Logs API
  slug: travis-ci-logs-api
- description: The Organizations API from Travis CI — 4 operation(s) for organizations.
  name: Travis CI Organizations API
  slug: travis-ci-organizations-api
- description: The Repositories API from Travis CI — 6 operation(s) for repositories.
  name: Travis CI Repositories API
  slug: travis-ci-repositories-api
- description: The Users API from Travis CI — 4 operation(s) for users.
  name: Travis CI Users API
  slug: travis-ci-users-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Travis CI REST API v3 Builds API
  slug: open-travis-ci-builds-api
- collection_type: open
  name: Travis CI REST API v3 Builds Jobs API
  slug: open-travis-ci-jobs-api
- collection_type: open
  name: Travis CI REST API v3 Builds Logs API
  slug: open-travis-ci-logs-api
- collection_type: open
  name: Travis CI REST API v3 Builds Organizations API
  slug: open-travis-ci-organizations-api
- collection_type: open
  name: Travis CI REST API v3 Builds Repositories API
  slug: open-travis-ci-repositories-api
- collection_type: open
  name: Travis CI REST API v3 Builds Users API
  slug: open-travis-ci-users-api
- collection_type: open
  name: Travis CI REST API v3
  slug: open-travis-ci
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/travis-ci-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/travis-ci-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/travis-ci-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/travis-ci
- group: company
  title: ''
  type: Website
  url: https://www.travis-ci.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.travis-ci.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.travis-ci.com/pricing/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/travis-ci
- group: operate
  title: ''
  type: StatusPage
  url: https://www.traviscistatus.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/travis-ci-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/travis-ci-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/travis-ci-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.travis-ci.com/feed/
created: '2026-05-08'
description: 'Travis CI is a hosted continuous integration service supporting GitHub, GitLab and Bitbucket. Two REST APIs are available: the legacy v2/v2.1 API (deprecated) and the current v3 API used by the web UI. Travis CI is also available as Enterprise (on-premises) and Server (private cloud).'
finops:
- name: Travis Ci Finops
  service_category: DevOps / CI/CD
  slug: travis-ci-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/travis-ci.png
layout: provider
modified: '2026-05-08'
name: Travis CI
nav: Providers
network: true
overview: 'Travis CI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Builds API, Jobs API, Logs API, and 3 more. Tagged areas include DevOps, CI/CD, Build, Open Source, and Hosted.


  Travis CI''s developer surface includes authentication, documentation, pricing, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Travis Ci Plans Pricing
  plan_count: 6
  slug: travis-ci-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Travis Ci Rate Limits
  slug: travis-ci-rate-limits
score:
  band: thin
  composite: 33.4
  delta: -0.4
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/travis-ci/refs/heads/main/screenshots/travis-ci-2026-06-20T195637.png
security:
- kind: authentication
  name: Travis Ci Authentication
  slug: travis-ci-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Travis Ci Domain Security
  slug: travis-ci-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: travis-ci
tags:
- DevOps
- CI/CD
- Build
- Open Source
- Hosted
- GitHub
website: https://www.travis-ci.com/
---
