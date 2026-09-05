---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Vector ships with a local gRPC API that lets you interact with a running Vector instance — inspect component topology, read internal metrics and health, and tap live events flowing through the pipelin
  name: Vector Observability API
  slug: vector-observability-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/timber-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://vector.dev/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://vector.dev/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://vector.dev/docs/setup/quickstart/
- group: docs
  title: ''
  type: APIReference
  url: https://vector.dev/docs/reference/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vectordotdev
- group: company
  title: ''
  type: Blog
  url: https://vector.dev/blog/
- group: operate
  title: ''
  type: Support
  url: https://vector.dev/community/
- group: other
  title: ''
  type: Download
  url: https://vector.dev/download/
- group: other
  title: ''
  type: Protobuf
  url: grpc/timber-observability.proto
- group: build
  title: ''
  type: CLI
  url: cli/timber-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/timber-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/timber-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/timber-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/timber-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/timber-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/timber-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/timber-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/timber-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://vector.dev/highlights/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/timber-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/timber-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/timber-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/vectordotdev/vector/blob/master/SECURITY.md
created: '2026-07-17'
description: 'Timber (timber.io) is the developer-tools company, backed by Lux Capital, that built Vector — an open-source, high-performance observability data pipeline written in Rust. The timber.io domain now redirects to vector.dev, and the project is stewarded by Datadog (which acquired Timber in 2021). Vector collects, transforms, and routes logs, metrics, and traces from many sources through a Vector Remap Language (VRL) transform layer to many sinks, running as a single static binary in agent or aggregator roles. Vector is configuration- driven (YAML/TOML/JSON) rather than an HTTP SaaS; its programmable surface is a local gRPC "Observability API" that lets tooling inspect and interact with a running Vector instance (component topology, metrics, health, live event tapping). This profile enriches the Timber/Vector lead with the real developer surface: the gRPC API, the vector CLI, distribution packages, and project security posture.'
image: https://vector.dev/img/open-graph.png
layout: provider
modified: '2026-07-21'
name: Timber
nav: Providers
network: true
overview: 'Timber publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Observability, Logs, and Metrics.


  Timber''s developer surface includes documentation, getting-started guide, API reference, engineering blog, support, CLI, authentication, and 17 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 32.4
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/timber/refs/heads/main/screenshots/timber-2026-09-02T163748.png
security:
- kind: authentication
  name: Timber Authentication
  slug: timber-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Timber Domain Security
  slug: timber-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Timber Vulnerability Disclosure
  slug: timber-vulnerability-disclosure
  summary_line: contact published
slug: timber
tags:
- Company
- Developer Tools
- Observability
- Logs
- Metrics
- Data Pipeline
- Logging
- Monitoring
- Open-Source
- gRPC
- Rust
- Datadog
website: https://vector.dev/docs/
---
