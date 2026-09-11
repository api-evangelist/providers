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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-09-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dagger Agentic Access
  operation_count: 2
  slug: dagger-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
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
- baseURL: http://127.0.0.1:{DAGGER_SESSION_PORT}
  baseurl_source: declared
  description: The GraphQL API from Dagger — 1 operation(s) for graphql.
  name: Dagger GraphQL API
  slug: dagger-graphql-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dagger HTTP GraphQL API
  slug: open-dagger-graphql-api
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
  url: https://dagger.cloud
- group: start
  title: ''
  type: SignUp
  url: https://dagger.cloud
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/dagger-io
- group: operate
  title: ''
  type: Community
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
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dagger-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/dagger-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dagger-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dagger-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dagger-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/dagger-tool-crosswalk.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dagger-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dagger-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dagger-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dagger.io
- group: design
  title: ''
  type: Conventions
  url: conventions/dagger-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dagger-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://dagger.io/changelog
- group: build
  title: ''
  type: CLI
  url: cli/dagger-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dagger-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dagger-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dagger-rate-limits.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dagger.io/legal_pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dagger.io/legal_pages/privacy-policy
- group: operate
  title: ''
  type: FAQ
  url: https://docs.dagger.io/faq/
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
mcp_servers:
- description: ''
  name: Container Use
  slug: container-use
modified: '2026-09-07'
name: Dagger
nav: Providers
network: true
overview: 'Dagger publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Build Automation, BuildKit, CI/CD, Containers, and DAG.


  The Dagger catalog on APIs.io includes 1 JSON-LD context.


  Dagger''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, signup flow, YouTube channel, and 41 more developer resources.'
plans:
- name: Dagger Plans Pricing
  plan_count: 3
  slug: dagger-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Dagger Rate Limits
  slug: dagger-rate-limits
score:
  band: strong
  composite: 55.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 65.0
    catalog_earned_first_party: 12.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 33.3
    contract_quality: 57.8
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 33.3
    operational_transparency: 26.3
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/dagger/refs/heads/main/screenshots/dagger-2026-06-20T175437.png
security:
- kind: authentication
  name: Dagger Authentication
  slug: dagger-authentication
  summary_line: http/oidc · 3 schemes
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
- Open-Source
- Pipelines
- Programmable Pipelines
- SDK
website: https://dagger.io/
---
