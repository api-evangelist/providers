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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dagger Agentic Access
  operation_count: 2
  slug: dagger-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 5
apis:
- description: 'The Dagger Engine exposes a unified, introspectable GraphQL type system at a per-session endpoint. The schema includes Container, Directory, File, Secret, CacheVolume, and other first-class types and '
  name: Dagger Engine GraphQL API
  slug: graphql
- description: Native SDKs for Go, Python, TypeScript, PHP, Java, .NET, Elixir, and Rust that generate strongly typed clients against the Dagger Engine's GraphQL schema, allowing pipelines to be written as regular c
  name: Dagger SDKs
  slug: sdks
- description: Daggerverse is the free, public index of Dagger Modules. Developers search for, browse, and consume reusable Modules contributed by the Dagger community.
  name: Daggerverse Module Index
  slug: daggerverse
- description: Dagger Cloud is the hosted control plane providing pipeline traces, checks, module observability, and team collaboration. It integrates with the local Dagger Engine for seamless trace uploads.
  name: Dagger Cloud
  slug: cloud
- description: The GraphQL API from Dagger — 1 operation(s) for graphql.
  name: Dagger GraphQL API
  slug: dagger-graphql-api
artifact_total: 14
collections:
- collection_type: open
  name: Dagger HTTP GraphQL API
  slug: open-dagger
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/dagger/dagger/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/dagger/dagger/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/dagger/dagger/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/dagger/dagger/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dagger-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dagger-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dagger-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dagger-io
- group: company
  title: ''
  type: Website
  url: https://dagger.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dagger.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dagger.io/quickstart
- group: docs
  title: ''
  type: Reference
  url: https://docs.dagger.io/reference/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dagger
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/dagger/dagger
- group: other
  title: ''
  type: Daggerverse
  url: https://daggerverse.dev/
- group: company
  title: ''
  type: Blog
  url: https://dagger.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dagger.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://dagger.cloud/signup
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/dagger-io
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@dagger-io
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/dagger_io
- group: commercial
  title: ''
  type: License
  url: https://github.com/dagger/dagger/blob/main/LICENSE
- group: design
  title: ''
  type: JSONLD
  url: json-ld/dagger-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dagger-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.dagger.io/llms.txt
created: '2026-03-26'
description: Dagger is an open-source programmable CI/CD engine that runs pipelines in containers using a unified, introspectable GraphQL API. Pipelines are written as code in the developer's preferred language (Go, Python, TypeScript, PHP, Java, .NET, Elixir, or Rust) using Dagger SDKs and packaged as Dagger Modules that can be published to the Daggerverse module index. The Dagger Engine exposes Container, Directory, File, Secret, and CacheVolume as first-class GraphQL types backed by a content-addressed store, enabling deterministic builds and aggressive caching. Dagger Cloud provides the hosted control plane for pipeline traces, checks, and module observability. Dagger does not expose a public REST API; clients connect to a per-session Dagger Engine GraphQL endpoint and the optional Dagger Cloud Web UI.
finops:
- name: Dagger Finops
  service_category: API
  slug: dagger-finops
graphqls:
- description: 'The Dagger Engine exposes a unified, introspectable GraphQL type system at a per-session endpoint. The schema includes Container, Directory, File, Secret, CacheVolume, and other first-class types and '
  name: Dagger GraphQL API
  slug: dagger-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dagger.png
jsonld:
- class_count: 20
  name: Dagger Context
  property_count: 0
  slug: dagger-context
layout: provider
modified: '2026-04-28'
name: Dagger
nav: Providers
network: true
overview: 'Dagger publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Build Automation, BuildKit, CI/CD, Containers, and DAG.


  The Dagger catalog on APIs.io includes 1 JSON-LD context.


  Dagger''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, signup flow, YouTube channel, and 18 more developer resources.'
plans:
- name: Dagger Plans Pricing
  plan_count: 3
  slug: dagger-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Dagger Rate Limits
  slug: dagger-rate-limits
score:
  band: developing
  composite: 44.7
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.4
    developer_ergonomics: 43.5
    discoverability: 72.2
    governance: 10.4
    operational_transparency: 28.9
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dagger/refs/heads/main/screenshots/dagger-2026-06-20T175437.png
security:
- kind: authentication
  name: Dagger Authentication
  slug: dagger-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dagger Domain Security
  slug: dagger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dagger
tags:
- Build Automation
- BuildKit
- CI/CD
- Containers
- DAG
- Daggerverse
- DevOps
- GraphQL
- Modules
- OCI
- Open Source
- Pipelines
- Programmable Pipelines
- SDKs
website: https://dagger.io/
---
