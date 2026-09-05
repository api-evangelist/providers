---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 39
  human_in_the_loop: 5
  name: Buildkite Agentic Access
  operation_count: 74
  slug: buildkite-agentic-access
  summary_line: 74 operations · 39 acting · 5 human-in-the-loop
api_count: 1
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
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The AccessToken API from Buildkite — 1 operation(s) for accesstoken.
  name: Buildkite AccessToken API
  slug: buildkite-accesstoken-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The Agents API from Buildkite — 5 operation(s) for agents.
  name: Buildkite Agents API
  slug: buildkite-agents-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The AgentTokens API from Buildkite — 2 operation(s) for agenttokens.
  name: Buildkite AgentTokens API
  slug: buildkite-agenttokens-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The Annotations API from Buildkite — 2 operation(s) for annotations.
  name: Buildkite Annotations API
  slug: buildkite-annotations-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The Artifacts API from Buildkite — 4 operation(s) for artifacts.
  name: Buildkite Artifacts API
  slug: buildkite-artifacts-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The Builds API from Buildkite — 6 operation(s) for builds.
  name: Buildkite Builds API
  slug: buildkite-builds-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The Clusters API from Buildkite — 2 operation(s) for clusters.
  name: Buildkite Clusters API
  slug: buildkite-clusters-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The Emojis API from Buildkite — 1 operation(s) for emojis.
  name: Buildkite Emojis API
  slug: buildkite-emojis-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The Jobs API from Buildkite — 5 operation(s) for jobs.
  name: Buildkite Jobs API
  slug: buildkite-jobs-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The Meta API from Buildkite — 1 operation(s) for meta.
  name: Buildkite Meta API
  slug: buildkite-meta-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The Organizations API from Buildkite — 4 operation(s) for organizations.
  name: Buildkite Organizations API
  slug: buildkite-organizations-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The Pipelines API from Buildkite — 5 operation(s) for pipelines.
  name: Buildkite Pipelines API
  slug: buildkite-pipelines-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The PipelineTemplates API from Buildkite — 2 operation(s) for pipelinetemplates.
  name: Buildkite PipelineTemplates API
  slug: buildkite-pipelinetemplates-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The Queues API from Buildkite — 4 operation(s) for queues.
  name: Buildkite Queues API
  slug: buildkite-queues-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The Rules API from Buildkite — 2 operation(s) for rules.
  name: Buildkite Rules API
  slug: buildkite-rules-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The Teams API from Buildkite — 2 operation(s) for teams.
  name: Buildkite Teams API
  slug: buildkite-teams-api
- baseURL: https://api.buildkite.com/v2
  baseurl_source: declared
  description: The User API from Buildkite — 1 operation(s) for user.
  name: Buildkite User API
  slug: buildkite-user-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Buildkite REST AccessToken API
  slug: open-buildkite-accesstoken-api
- collection_type: open
  name: Buildkite REST AccessToken Agents API
  slug: open-buildkite-agents-api
- collection_type: open
  name: Buildkite REST AccessToken AgentTokens API
  slug: open-buildkite-agenttokens-api
- collection_type: open
  name: Buildkite REST AccessToken Annotations API
  slug: open-buildkite-annotations-api
- collection_type: open
  name: Buildkite REST AccessToken Artifacts API
  slug: open-buildkite-artifacts-api
- collection_type: open
  name: Buildkite REST AccessToken Builds API
  slug: open-buildkite-builds-api
- collection_type: open
  name: Buildkite REST AccessToken Clusters API
  slug: open-buildkite-clusters-api
- collection_type: open
  name: Buildkite REST AccessToken Emojis API
  slug: open-buildkite-emojis-api
- collection_type: open
  name: Buildkite REST AccessToken Jobs API
  slug: open-buildkite-jobs-api
- collection_type: open
  name: Buildkite REST AccessToken Meta API
  slug: open-buildkite-meta-api
- collection_type: open
  name: Buildkite REST AccessToken Organizations API
  slug: open-buildkite-organizations-api
- collection_type: open
  name: Buildkite REST AccessToken Pipelines API
  slug: open-buildkite-pipelines-api
- collection_type: open
  name: Buildkite REST AccessToken PipelineTemplates API
  slug: open-buildkite-pipelinetemplates-api
- collection_type: open
  name: Buildkite REST AccessToken Queues API
  slug: open-buildkite-queues-api
- collection_type: open
  name: Buildkite REST AccessToken Rules API
  slug: open-buildkite-rules-api
- collection_type: open
  name: Buildkite REST AccessToken Teams API
  slug: open-buildkite-teams-api
- collection_type: open
  name: Buildkite REST AccessToken User API
  slug: open-buildkite-user-api
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
random_paper: 12
rate_limits:
- limit_count: 3
  name: Buildkite Rate Limits
  slug: buildkite-rate-limits
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
