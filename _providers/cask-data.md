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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 4
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/cdapio/cdap/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/cdapio/cdap/blob/develop/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/cdapio/cdap/blob/develop/CONTRIBUTING.rst
- group: company
  title: ''
  type: Website
  url: https://cdap.io
- group: docs
  title: ''
  type: Documentation
  url: https://cdap.atlassian.net/wiki/spaces/DOCS/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cdap.io/cdap/current/en/reference-manual/http-restful-api/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://cdap.io/get-started/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/cdapio
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cdapio
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cdapio/cdap
- group: operate
  title: ''
  type: Support
  url: https://groups.google.com/g/cdap-dev
- group: commercial
  title: ''
  type: License
  url: https://github.com/cdapio/cdap/blob/develop/LICENSE
- group: auth
  title: ''
  type: Security
  url: https://github.com/cdapio/cdap/blob/develop/SECURITY.md
- group: other
  title: ''
  type: DataFusion
  url: https://cloud.google.com/data-fusion
- group: build
  title: ''
  type: Packages
  url: packages/cask-data-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cask-data-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cask-data-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cask-data-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cask-data-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cask-data-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cask-data-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cask-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cask-data-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cask-data-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cask-data-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cask-data-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cask-data-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cask-data-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cask-data-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cask-data-llms.txt
created: '2026-07-17'
description: Cask Data was the developer-tools company (originally Continuuity) behind CDAP, the Cask Data Application Platform — a 100% open source, integrated framework for building and running batch and real-time data-analytics applications and self-service ETL/ELT data pipelines on Hadoop, Spark, and the cloud. Google acquired Cask Data in 2018; CDAP now powers Google Cloud Data Fusion while continuing as an Apache 2.0 open source project (github.com/cdapio) with a versioned HTTP RESTful API rooted at /v3/namespaces, a Java client library and CLI, and a downloadable local Sandbox. Backed by Amplify Partners and Battery Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cask-data.png
layout: provider
mcp_servers:
- description: ''
  name: cask-data-mcp.yml
  slug: cask-data-mcpyml
modified: '2026-07-18'
name: Cask Data
nav: Providers
network: true
overview: 'Cask Data is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Data Integration, Data Pipelines, and ETL.


  Cask Data''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, sandbox, and 23 more developer resources.'
random_paper: 61
score:
  band: emerging
  composite: 23.3
  delta: -1.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 57.4
    governance: 3.1
    operational_transparency: 31.6
  previous_composite: 24.4
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cask-data/refs/heads/main/screenshots/cask-data-2026-07-25T204727.png
security:
- kind: authentication
  name: Cask Data Authentication
  slug: cask-data-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cask Data Domain Security
  slug: cask-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cask Data Vulnerability Disclosure
  slug: cask-data-vulnerability-disclosure
  summary_line: contact published
slug: cask-data
tags:
- Company
- Developer Tools
- Data Integration
- Data Pipelines
- ETL
- Big Data
- Analytics
- Open Source
- Hadoop
- CDAP
website: https://cdap.io
---
