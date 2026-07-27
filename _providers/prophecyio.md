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
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 51.0
  scored_at: '2026-07-27'
api_count: 5
apis:
- description: The Connections API from Prophecy.io — 2 operation(s) for connections.
  name: Prophecy.io Connections API
  slug: prophecyio-connections-api
- description: The Fabrics API from Prophecy.io — 2 operation(s) for fabrics.
  name: Prophecy.io Fabrics API
  slug: prophecyio-fabrics-api
- description: The Pipeline Runs API from Prophecy.io — 3 operation(s) for pipeline runs.
  name: Prophecy.io Pipeline Runs API
  slug: prophecyio-pipeline-runs-api
- description: The Project Deployment API from Prophecy.io — 1 operation(s) for project deployment.
  name: Prophecy.io Project Deployment API
  slug: prophecyio-project-deployment-api
- description: The Secrets API from Prophecy.io — 2 operation(s) for secrets.
  name: Prophecy.io Secrets API
  slug: prophecyio-secrets-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/prophecyio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prophecyio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.prophecy.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.prophecy.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.prophecy.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.prophecy.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.prophecy.ai/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://www.prophecy.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.prophecy.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.prophecy.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prophecy-io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.prophecy.io/
- group: operate
  title: ''
  type: Support
  url: https://docs.prophecy.ai/administration/getting-help/get-in-touch
- group: auth
  title: ''
  type: Authentication
  url: authentication/prophecyio-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/prophecyio-connections-openapi.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prophecyio-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/prophecyio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/prophecyio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/prophecyio-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/prophecyio-mcp.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prophecyio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.prophecy.ai/releases/version-support
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/prophecyio-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/prophecyio-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/prophecyio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.prophecy.ai/
- group: design
  title: ''
  type: Conventions
  url: conventions/prophecyio-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/prophecyio-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/prophecyio-connections-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Prophecy is an AI-native, low-code data engineering and analytics platform for building, running, and managing data pipelines across SQL and Apache Spark environments on Databricks, Snowflake, and BigQuery. Data teams compose pipelines visually with gems (or natural language via the AI Copilot), and Prophecy generates clean Spark/SQL code committed to Git. The platform exposes a REST API (the Prophecy Orchestration/Deployment API) for programmatically managing fabrics, connections, secrets, deploying projects, and triggering pipeline runs and data tests, authenticated with per-user Personal Access Tokens. A companion CLI, the Prophecy Build Tool (PBT), integrates Prophecy projects into external CI/CD such as GitHub Actions and Jenkins.
image: https://www.prophecy.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: prophecyio-mcp.yml
  slug: prophecyio-mcpyml
modified: '2026-07-20'
name: Prophecy.io
nav: Providers
network: true
overview: 'Prophecy.io publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Connections API, Fabrics API, Pipeline Runs API, and 2 more. Tagged areas include Company, Data Engineering, Data Pipelines, ETL, and Apache Spark.


  Prophecy.io''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 23 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 51.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 46.0
    developer_ergonomics: 80.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 51.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Prophecyio Authentication
  slug: prophecyio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Prophecyio Domain Security
  slug: prophecyio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Prophecyio Trust Center
  slug: prophecyio-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: prophecyio
tags:
- Company
- Data Engineering
- Data Pipelines
- ETL
- Apache Spark
- Databricks
- Snowflake
- Low-Code
- Analytics
- AI
- Data Transformation
website: https://www.prophecy.io/
---
