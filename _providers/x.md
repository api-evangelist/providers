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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: X Agentic Access
  operation_count: 8
  slug: x-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 4
apis:
- description: Get immediate access to the X API and unlock the potential of X data.
  name: X
  slug: x
- description: The Posts API from X — 4 operation(s) for posts.
  name: X Posts API
  slug: x-posts-api
- description: The Trends API from X — 1 operation(s) for trends.
  name: X Trends API
  slug: x-trends-api
- description: The Users API from X — 2 operation(s) for users.
  name: X Users API
  slug: x-users-api
artifact_total: 10
collections:
- collection_type: open
  name: X API v2
  slug: open-x
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/x-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/x-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/twitter
created: '2025-08-14'
description: Get immediate access to the X API and unlock the potential of X data.
finops:
- name: X Finops
  service_category: API
  slug: x-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/x.png
layout: provider
modified: '2026-03-16'
name: X
nav: Providers
network: true
overview: 'X publishes 3 APIs on the [APIs.io](https://apis.io/) network: Posts API, Trends API, and Users API.


  X''s developer surface includes authentication and 2 more developer resources.'
plans:
- name: X Plans Pricing
  plan_count: 3
  slug: x-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: X Rate Limits
  slug: x-rate-limits
score:
  band: thin
  composite: 33.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.4
    developer_ergonomics: 10.9
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 33.8
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
screenshot: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/screenshots/x-2026-06-20T201653.png
security:
- kind: authentication
  name: X Authentication
  slug: x-authentication
  summary_line: http · 1 scheme
slug: x
---
