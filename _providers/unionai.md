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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Unionai Agentic Access
  operation_count: 29
  slug: unionai-agentic-access
  summary_line: 29 operations · 11 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: The union and pyflyte command-line tools plus the Flytekit and Union Python SDKs - the primary, fully-documented clients that register entities and drive the FlyteAdmin control plane (including Actors
  name: Union CLI & SDK
  slug: union-cli-sdk
- description: The Domains API from Union.ai — 1 operation(s) for domains.
  name: Union.ai Domains API
  slug: unionai-domains-api
- description: The Executions API from Union.ai — 6 operation(s) for executions.
  name: Union.ai Executions API
  slug: unionai-executions-api
- description: The Launch Plans API from Union.ai — 5 operation(s) for launch plans.
  name: Union.ai Launch Plans API
  slug: unionai-launch-plans-api
- description: The Node Executions API from Union.ai — 1 operation(s) for node executions.
  name: Union.ai Node Executions API
  slug: unionai-node-executions-api
- description: The Projects API from Union.ai — 2 operation(s) for projects.
  name: Union.ai Projects API
  slug: unionai-projects-api
- description: The Tasks API from Union.ai — 4 operation(s) for tasks.
  name: Union.ai Tasks API
  slug: unionai-tasks-api
- description: The Version API from Union.ai — 1 operation(s) for version.
  name: Union.ai Version API
  slug: unionai-version-api
- description: The Workflows API from Union.ai — 4 operation(s) for workflows.
  name: Union.ai Workflows API
  slug: unionai-workflows-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Union FlyteAdmin Control Plane API (HTTP/JSON Gateway) Domains API
  slug: open-unionai-domains-api
- collection_type: open
  name: Union FlyteAdmin Control Plane API (HTTP/JSON Gateway) Domains Executions API
  slug: open-unionai-executions-api
- collection_type: open
  name: Union FlyteAdmin Control Plane API (HTTP/JSON Gateway) Domains Launch Plans API
  slug: open-unionai-launch-plans-api
- collection_type: open
  name: Union FlyteAdmin Control Plane API (HTTP/JSON Gateway) Domains Node Executions API
  slug: open-unionai-node-executions-api
- collection_type: open
  name: Union FlyteAdmin Control Plane API (HTTP/JSON Gateway) Domains Projects API
  slug: open-unionai-projects-api
- collection_type: open
  name: Union FlyteAdmin Control Plane API (HTTP/JSON Gateway) Domains Tasks API
  slug: open-unionai-tasks-api
- collection_type: open
  name: Union FlyteAdmin Control Plane API (HTTP/JSON Gateway) Domains Version API
  slug: open-unionai-version-api
- collection_type: open
  name: Union FlyteAdmin Control Plane API (HTTP/JSON Gateway) Domains Workflows API
  slug: open-unionai-workflows-api
- collection_type: open
  name: Union FlyteAdmin Control Plane API (HTTP/JSON Gateway)
  slug: open-unionai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unionai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/unionai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unionai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unionai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/unionai-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unionai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flyteorg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unionai
- group: company
  title: ''
  type: Website
  url: https://www.union.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.union.ai/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/unionai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unionai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unionai-finops.yml
created: '2026-06-20'
description: Union.ai is the commercial AI/ML orchestration platform built on the open-source Flyte project. It exposes the Flyte/Union control plane (the FlyteAdmin service) for registering and running strongly-typed workflows, tasks, and launch plans, plus Union Serverless, Actors, and Artifacts. The control plane is primarily a gRPC API (FlyteIDL AdminService) with an auto-generated HTTP/JSON gateway exposed under /api/v1/, driven by the union / pyflyte CLI and Flytekit / Union SDKs.
finops:
- name: Unionai Finops
  service_category: AI and Machine Learning
  slug: unionai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unionai.png
layout: provider
modified: '2026-06-20'
name: Union.ai
nav: Providers
network: true
overview: 'Union.ai publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Domains API, Executions API, Launch Plans API, and 5 more. Tagged areas include AI, ML, Orchestration, Workflows, and MLOps.


  Union.ai''s developer surface includes authentication, documentation, and 11 more developer resources.'
plans:
- name: Unionai Plans Pricing
  plan_count: 3
  slug: unionai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Unionai Rate Limits
  slug: unionai-rate-limits
scopes:
- name: Unionai Scopes
  scope_count: 1
  slug: unionai-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: thin
  composite: 38.6
  delta: -0.4
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 51.9
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unionai/refs/heads/main/screenshots/unionai-2026-06-20T200031.png
security:
- kind: authentication
  name: Unionai Authentication
  slug: unionai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Unionai Domain Security
  slug: unionai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Unionai Trust Center
  slug: unionai-trust-center
  summary_line: SOC 2, HIPAA
slug: unionai
tags:
- AI
- ML
- Orchestration
- Workflows
- MLOps
- Flyte
- Serverless
website: https://www.union.ai
---
