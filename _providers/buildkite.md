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
- acting_count: 39
  human_in_the_loop: 5
  name: Buildkite Agentic Access
  operation_count: 74
  slug: buildkite-agentic-access
  summary_line: 74 operations · 39 acting · 5 human-in-the-loop
api_count: 20
apis:
- description: JSON over HTTPS REST API for the Buildkite control plane. Bearer-token auth with API access tokens.
  name: Buildkite REST API
  slug: rest
- description: 'Relay-compliant GraphQL API. Single endpoint for nested queries across organizations, pipelines, builds, jobs, agents, teams. Introspection supported. Bearer auth with the "Enable GraphQL API Access" '
  name: Buildkite GraphQL API
  slug: graphql
- description: API consumed by buildkite-agent — register, retrieve work, send job events and upload artifacts/annotations. Used by self-hosted and hosted agents.
  name: Buildkite Agent API
  slug: agent-api
- description: The AccessToken API from Buildkite — 1 operation(s) for accesstoken.
  name: Buildkite AccessToken API
  slug: buildkite-accesstoken-api
- description: The Agents API from Buildkite — 5 operation(s) for agents.
  name: Buildkite Agents API
  slug: buildkite-agents-api
- description: The AgentTokens API from Buildkite — 2 operation(s) for agenttokens.
  name: Buildkite AgentTokens API
  slug: buildkite-agenttokens-api
- description: The Annotations API from Buildkite — 2 operation(s) for annotations.
  name: Buildkite Annotations API
  slug: buildkite-annotations-api
- description: The Artifacts API from Buildkite — 4 operation(s) for artifacts.
  name: Buildkite Artifacts API
  slug: buildkite-artifacts-api
- description: The Builds API from Buildkite — 6 operation(s) for builds.
  name: Buildkite Builds API
  slug: buildkite-builds-api
- description: The Clusters API from Buildkite — 2 operation(s) for clusters.
  name: Buildkite Clusters API
  slug: buildkite-clusters-api
- description: The Emojis API from Buildkite — 1 operation(s) for emojis.
  name: Buildkite Emojis API
  slug: buildkite-emojis-api
- description: The Jobs API from Buildkite — 5 operation(s) for jobs.
  name: Buildkite Jobs API
  slug: buildkite-jobs-api
- description: The Meta API from Buildkite — 1 operation(s) for meta.
  name: Buildkite Meta API
  slug: buildkite-meta-api
- description: The Organizations API from Buildkite — 4 operation(s) for organizations.
  name: Buildkite Organizations API
  slug: buildkite-organizations-api
- description: The Pipelines API from Buildkite — 5 operation(s) for pipelines.
  name: Buildkite Pipelines API
  slug: buildkite-pipelines-api
- description: The PipelineTemplates API from Buildkite — 2 operation(s) for pipelinetemplates.
  name: Buildkite PipelineTemplates API
  slug: buildkite-pipelinetemplates-api
- description: The Queues API from Buildkite — 4 operation(s) for queues.
  name: Buildkite Queues API
  slug: buildkite-queues-api
- description: The Rules API from Buildkite — 2 operation(s) for rules.
  name: Buildkite Rules API
  slug: buildkite-rules-api
- description: The Teams API from Buildkite — 2 operation(s) for teams.
  name: Buildkite Teams API
  slug: buildkite-teams-api
- description: The User API from Buildkite — 1 operation(s) for user.
  name: Buildkite User API
  slug: buildkite-user-api
artifact_total: 29
collections:
- collection_type: open
  name: Buildkite REST API
  slug: open-buildkite
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/buildkite-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/buildkite-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buildkite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/buildkite-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/buildkite
- group: company
  title: ''
  type: Website
  url: https://buildkite.com/
- group: docs
  title: ''
  type: Documentation
  url: https://buildkite.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://buildkite.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/buildkite
- group: operate
  title: ''
  type: StatusPage
  url: https://buildkitestatus.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/buildkite-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/buildkite-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/buildkite-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://buildkite.com/blog.atom
created: '2026-05-08'
description: Buildkite is a CI/CD platform with self-hosted agents and a hosted control plane. The platform exposes a REST API, a GraphQL API and an Agent API used by buildkite-agent. Resources include organizations, pipelines, pipeline templates, builds, jobs, agents, clusters, queues, teams, rules, artifacts, annotations, and access tokens. Test Engine adds test execution and analytics endpoints.
finops:
- name: Buildkite Finops
  service_category: DevOps / CI/CD
  slug: buildkite-finops
graphqls:
- description: 'Relay-compliant GraphQL API. Single endpoint for nested queries across organizations, pipelines, builds, jobs, agents, teams. Introspection supported. Bearer auth with the "Enable GraphQL API Access" '
  name: Buildkite GraphQL API
  slug: buildkite-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buildkite.png
layout: provider
modified: '2026-05-08'
name: Buildkite
nav: Providers
network: true
overview: 'Buildkite publishes 17 APIs on the [APIs.io](https://apis.io/) network, including AccessToken API, Agents API, AgentTokens API, and 14 more. Tagged areas include DevOps, CI/CD, Pipelines, Agents, and Self-Hosted.


  Buildkite''s developer surface includes authentication, documentation, pricing, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Buildkite Plans Pricing
  plan_count: 4
  slug: buildkite-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 3
  name: Buildkite Rate Limits
  slug: buildkite-rate-limits
score:
  band: developing
  composite: 43.4
  delta: -2.1
  facets:
    commercial_clarity: 57.9
    contract_quality: 53.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buildkite/refs/heads/main/screenshots/buildkite-2026-06-20T173751.png
security:
- kind: authentication
  name: Buildkite Authentication
  slug: buildkite-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Buildkite Domain Security
  slug: buildkite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Buildkite Trust Center
  slug: buildkite-trust-center
  summary_line: SOC 2
slug: buildkite
tags:
- DevOps
- CI/CD
- Pipelines
- Agents
- Self-Hosted
- GraphQL
- Test Engine
website: https://buildkite.com/
---
