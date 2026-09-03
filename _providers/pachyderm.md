---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Pachyderm's platform API, exposed over gRPC/protobuf. Core services are PFS (data versioning — repos, commits, branches, files) and PPS (pipelines — jobs, datums, pipelines, logs), plus an Auth servic
  name: Pachyderm gRPC API
  slug: pachyderm-grpc-api
artifact_total: 2
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/pachyderm/pachyderm/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/pachyderm/pachyderm/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/pachyderm/pachyderm/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/pachyderm/pachyderm/blob/master/LICENSE
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pachyderm
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/pachyderm/pachyderm/blob/master/README.md
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/pachyderm/pachyderm/tree/master/src
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pachyderm/pachyderm
- group: build
  title: ''
  type: Packages
  url: packages/pachyderm-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pachyderm-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/pachyderm-cli.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/pachyderm-grpc.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pachyderm-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pachyderm-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pachyderm-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pachyderm-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pachyderm-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pachyderm-llms.txt
created: '2026-07-17'
description: Pachyderm is an open-source (Apache-2.0) platform for data-centric pipelines and data versioning, widely used for MLOps. It provides immutable, git-like data lineage through the Pachyderm File System (PFS) and data-driven, containerized pipelines that reprocess only changed data through the Pachyderm Pipeline System (PPS), all running on Kubernetes. The platform is driven by a gRPC/protobuf API with first-party Python, Go, Ruby and Rust clients and the pachctl command-line tool. Pachyderm was acquired by Hewlett Packard Enterprise in January 2023; the standalone marketing, documentation and hosted (Pachyderm Hub) sites have since been retired, but the source, releases, SDKs and CLI remain actively published on GitHub and the language package registries (latest release v2.12.2, January 2025).
image: https://avatars.githubusercontent.com/u/10432478?v=4
layout: provider
modified: '2026-07-20'
name: Pachyderm
nav: Providers
network: true
overview: 'Pachyderm publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MLOps, Data Versioning, Data Pipeline, and Data Lineage.


  Pachyderm''s developer surface includes documentation, API reference, CLI, authentication, changelog, and 13 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 50.0
  previous_composite: 28.2
  provenance:
    conformance: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pachyderm/refs/heads/main/screenshots/pachyderm-2026-08-07T191241.png
security:
- kind: authentication
  name: Pachyderm Authentication
  slug: pachyderm-authentication
  summary_line: oidc/bearer-token · 3 schemes
slug: pachyderm
tags:
- Company
- MLOps
- Data Versioning
- Data Pipeline
- Data Lineage
- Machine-Learning
- Kubernetes
- gRPC
- Open-Source
---
