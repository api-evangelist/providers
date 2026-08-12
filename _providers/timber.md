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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Vector ships with a local gRPC API that lets you interact with a running Vector instance — inspect component topology, read internal metrics and health, and tap live events flowing through the pipelin
  name: Vector Observability API
  slug: vector-observability-api
artifact_total: 5
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: timber-mcp.yml
  slug: timber-mcpyml
modified: '2026-07-21'
name: Timber
nav: Providers
network: true
overview: 'Timber publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Observability, Logs, and Metrics.


  Timber''s developer surface includes documentation, getting-started guide, API reference, engineering blog, support, CLI, authentication, and 17 more developer resources.'
random_paper: 63
score:
  band: emerging
  composite: 25.3
  delta: -1.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 39.5
  previous_composite: 26.4
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
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
- Open Source
- gRPC
- Rust
- Datadog
website: https://vector.dev/docs/
---
