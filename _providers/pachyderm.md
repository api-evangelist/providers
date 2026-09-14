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
