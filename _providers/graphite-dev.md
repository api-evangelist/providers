---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Graphite Dev Agentic Access
  operation_count: 7
  slug: graphite-dev-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 4
apis:
- description: Graphite CLI authentication with a Graphite auth token.
  name: Graphite Authentication API
  slug: graphite-dev-authentication-api
- description: GitHub App install and webhook integration entry points.
  name: Graphite GitHub App API
  slug: graphite-dev-github-app-api
- description: Graphite merge queue actions.
  name: Graphite Merge Queue API
  slug: graphite-dev-merge-queue-api
- description: Create, submit, sync, and merge stacked pull requests via the gt CLI.
  name: Graphite Stacks API
  slug: graphite-dev-stacks-api
artifact_total: 11
collections:
- collection_type: open
  name: Graphite Platform
  slug: open-graphite-dev
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/graphite-dev-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphite-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/graphite-dev-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withgraphite
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/graphite-dev
- group: company
  title: ''
  type: Website
  url: https://graphite.dev
- group: docs
  title: ''
  type: Documentation
  url: https://graphite.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/graphite-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/graphite-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/graphite-dev-finops.yml
created: '2026-06-20'
description: Graphite is a code review platform built on top of GitHub for stacking pull requests, AI code review, and merging at scale. The gt CLI creates and submits stacked PRs, Graphite Agent (Diamond) provides codebase-aware AI review and chat, and a merge queue batches and tests PRs in parallel. Graphite has no standalone public REST API - it integrates through a GitHub App that consumes GitHub webhooks, the gt CLI (authenticated with a Graphite token), the GT MCP server, and label / GitHub-mediated integrations (Slack, Linear, external merge queue).
finops:
- name: Graphite Dev Finops
  service_category: Developer Tools
  slug: graphite-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/graphite-dev.png
layout: provider
modified: '2026-06-20'
name: Graphite
nav: Providers
network: true
overview: 'Graphite publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, GitHub App API, Merge Queue API, and 1 more. Tagged areas include Code Review, Stacked PRs, Merge Queue, AI Code Review, and Developer Tools.


  Graphite''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Graphite Dev Plans Pricing
  plan_count: 4
  slug: graphite-dev-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 4
  name: Graphite Dev Rate Limits
  slug: graphite-dev-rate-limits
score:
  band: thin
  composite: 37.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.8
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/graphite-dev/refs/heads/main/screenshots/graphite-dev-2026-06-20T182329.png
security:
- kind: authentication
  name: Graphite Dev Authentication
  slug: graphite-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Graphite Dev Domain Security
  slug: graphite-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: graphite-dev
tags:
- Code Review
- Stacked PRs
- Merge Queue
- AI Code Review
- Developer Tools
- GitHub
website: https://graphite.dev
---
