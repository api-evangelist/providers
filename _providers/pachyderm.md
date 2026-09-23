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
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-09-23'
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
  href: https://raw.githubusercontent.com/api-evangelist/pachyderm/refs/heads/main/packages/pachyderm-packages.yml
  title: ''
  type: Packages
  url: packages/pachyderm-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pachyderm/refs/heads/main/packages/pachyderm-packages.yml
  title: ''
  type: SDKs
  url: packages/pachyderm-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pachyderm/refs/heads/main/cli/pachyderm-cli.yml
  title: ''
  type: CLI
  url: cli/pachyderm-cli.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pachyderm/refs/heads/main/grpc/pachyderm-grpc.yml
  title: ''
  type: Protobuf
  url: grpc/pachyderm-grpc.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pachyderm/refs/heads/main/authentication/pachyderm-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pachyderm-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pachyderm/refs/heads/main/conformance/pachyderm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pachyderm-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pachyderm/refs/heads/main/conventions/pachyderm-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pachyderm-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pachyderm/refs/heads/main/lifecycle/pachyderm-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pachyderm-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pachyderm/refs/heads/main/changelog/pachyderm-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pachyderm-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pachyderm/refs/heads/main/llms/pachyderm-llms.txt
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
random_paper: 11
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 42.9
    discoverability: 75.9
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 50.0
  previous_composite: 28.2
  provenance:
    conformance: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
