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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 21.2
  scored_at: '2026-07-27'
api_count: 12
apis:
- description: The CDAP HTTP RESTful API, documented as "Microservices". All endpoints sit under a /v3 path prefix on a self-hosted CDAP router (default port 11015, or 10443 when SSL is enabled), and are scoped by n
  name: CDAP Microservices API
  slug: cdap-microservices
- description: Deploy, start, stop, and manage the lifecycle of CDAP applications and the programs they contain within a namespace.
  name: CDAP Lifecycle Microservices
  slug: cdap-lifecycle
- description: Manage CDAP artifacts — the packaged application and plugin JARs that applications are created from — including deployment, versioning, and plugin inspection.
  name: CDAP Artifact Microservices
  slug: cdap-artifact
- description: Search, annotate, and retrieve business and technical metadata and lineage for CDAP entities such as applications, datasets, programs, and fields.
  name: CDAP Metadata Microservices
  slug: cdap-metadata
- description: Query the metrics CDAP collects for system and user programs, including time-series queries across metric contexts and tags.
  name: CDAP Metrics Microservices
  slug: cdap-metrics
- description: Retrieve and download logs emitted by CDAP system services and by user applications and programs, with filtering by time range and log level.
  name: CDAP Logging Microservices
  slug: cdap-logging
- description: Create, list, and delete CDAP namespaces — the multi-tenancy boundary that isolates applications, datasets, and metadata. The cdap, default, and system namespaces are reserved.
  name: CDAP Namespace Microservices
  slug: cdap-namespace
- description: Programmatically create, deploy, run, and inspect CDAP data pipelines (the Hydrator / Data Fusion pipeline application type) and their plugin configurations.
  name: CDAP Pipeline Microservices
  slug: cdap-pipeline
- description: Manage CDAP replication (change data capture) jobs that stream changes from source databases into analytic targets such as BigQuery.
  name: CDAP Replication Microservices
  slug: cdap-replication
- description: Manage CDAP secure store keys and authorization privileges, roles, and policies for principals operating against a security-enabled CDAP cluster.
  name: CDAP Security Microservices
  slug: cdap-security
- description: Inspect and control CDAP workflows — multi-node program orchestration — including run records, node states, local datasets, and workflow tokens.
  name: CDAP Workflow Microservices
  slug: cdap-workflow
- description: Read and write preferences — the hierarchical configuration key/value pairs resolved across the instance, namespace, application, and program scopes.
  name: CDAP Preferences Microservices
  slug: cdap-preferences
artifact_total: 14
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cdap.io/
- group: docs
  title: ''
  type: Documentation
  url: https://cdap.atlassian.net/wiki/spaces/DOCS/overview
- group: docs
  title: ''
  type: APIReference
  url: https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477593807/CDAP+Microservices+Guide
- group: start
  title: ''
  type: GettingStarted
  url: https://cdap.io/get-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cdapio
- group: operate
  title: ''
  type: Support
  url: https://cdap.io/community/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/cdapio
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: build
  title: ''
  type: Packages
  url: packages/cask-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cask-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cask-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cask-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cask-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cask-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cask-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/cask-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cask-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cask-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cask-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cask-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cask-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cask-llms.txt
created: '2026-07-17'
description: Cask Data, Inc. was the enterprise big-data startup, backed by Andreessen Horowitz, that built and open-sourced CDAP — the Cask Data Application Platform — a framework for building and running data analytic applications and data pipelines on Hadoop, Spark, Kubernetes, and the cloud. Cask was acquired by Google Cloud; CDAP continues as an Apache-2.0 open source project under the github.com/cdapio organization and powers Google Cloud Data Fusion. CDAP's programmatic surface is its HTTP RESTful "Microservices" API — 21 documented service families (Lifecycle, Artifact, Metadata, Metrics, Logging, Namespace, Pipeline, Preferences, Profile, Provisioners, Replication, Reports, Security, Service, Workflow, Monitor, Dashboard, Configuration, Transaction Service, System Workers) served under a /v3 path prefix from a self-hosted CDAP router, with Bearer access tokens issued by the CDAP authentication server. The company's own cask.co domain and developer portal are gone; the surviving
  surfaces are cdap.io, the CDAP documentation wiki, the cdapio GitHub organization, and the io.cdap.cdap / co.cask.cdap artifact groups on Maven Central.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cask.png
layout: provider
modified: '2026-07-20'
name: Cask
nav: Providers
network: true
overview: 'Cask publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Big Data, Data Analytics, Data Pipelines, and Data Integration.


  Cask''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 16 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 30.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 71.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cask/refs/heads/main/screenshots/cask-2026-07-25T204726.png
security:
- kind: authentication
  name: Cask Authentication
  slug: cask-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cask Domain Security
  slug: cask-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cask
tags:
- Company
- Big Data
- Data Analytics
- Data Pipelines
- Data Integration
- ETL
- Hadoop
- Spark
- Open Source
- CDAP
- Metadata
- Data Governance
- Acquired
website: https://cdap.io/
---
