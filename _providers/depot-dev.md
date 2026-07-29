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
  human_in_the_loop: 1
  name: Depot Dev Agentic Access
  operation_count: 14
  slug: depot-dev-agentic-access
  summary_line: 14 operations · 14 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: Managed, single-tenant GitHub Actions runners selected via runner labels (e.g. depot-ubuntu-24.04, depot-ubuntu-24.04-arm) across Intel, Arm/Graviton4, macOS, Windows, and GPU sizes. Runners are provi
  name: Depot GitHub Actions Runners
  slug: depot-dev-github-actions-runners
- description: Depot Cache is a remote build cache backend that plugs into tools supporting remote caching (GitHub Actions, Bazel, Go, Turborepo, Gradle, Pants, sccache). It is consumed through each tool's native re
  name: Depot Cache
  slug: depot-dev-cache
- description: Acquire a low-level BuildKit machine connection (depot.buildkit.v1.BuildKitService).
  name: Depot BuildKitService API
  slug: depot-dev-buildkitservice-api
- description: Register, finish, get, and list builds (depot.build.v1.BuildService).
  name: Depot BuildService API
  slug: depot-dev-buildservice-api
- description: Manage Depot projects and project tokens (depot.core.v1.ProjectService).
  name: Depot ProjectService API
  slug: depot-dev-projectservice-api
artifact_total: 12
collections:
- collection_type: open
  name: Depot API
  slug: open-depot-dev
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/depot-dev-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/depot-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/depot-dev-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/depot
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/depot-dev
- group: company
  title: ''
  type: Website
  url: https://depot.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://depot.dev/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/depot-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/depot-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/depot-dev-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://depot.dev/rss.xml
created: '2026-06-20'
description: Depot is a fast container-image build and remote cache service. It runs Docker builds and GitHub Actions jobs on managed, single-tenant cloud compute with persistent BuildKit cache, and exposes Depot Cache as a remote cache backend for tools like Bazel, Go, Turborepo, Gradle, and sccache. Depot is programmable through a public API at api.depot.dev built on Connect (multiprotocol gRPC, gRPC-Web, and HTTP/JSON) for managing projects, tokens, and builds, plus the depot CLI.
finops:
- name: Depot Dev Finops
  service_category: Developer Tools and CI/CD
  slug: depot-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/depot-dev.png
layout: provider
modified: '2026-06-20'
name: Depot
nav: Providers
network: true
overview: 'Depot publishes 3 APIs on the [APIs.io](https://apis.io/) network: BuildKitService API, BuildService API, and ProjectService API. Tagged areas include Container Builds, Docker, BuildKit, Remote Cache, and CI/CD.


  Depot''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Depot Dev Plans Pricing
  plan_count: 4
  slug: depot-dev-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Depot Dev Rate Limits
  slug: depot-dev-rate-limits
score:
  band: thin
  composite: 37.8
  delta: -2.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/depot-dev/refs/heads/main/screenshots/depot-dev-2026-06-20T175928.png
security:
- kind: authentication
  name: Depot Dev Authentication
  slug: depot-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Depot Dev Domain Security
  slug: depot-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: depot-dev
tags:
- Container Builds
- Docker
- BuildKit
- Remote Cache
- CI/CD
- GitHub Actions
website: https://depot.dev/
---
