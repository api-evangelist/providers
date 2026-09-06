---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST API (/api/v1) for managing Ascend workspaces, deployments, environments, projects, profiles, flows, flow runs, and Otto. Service-account Bearer authentication.
  name: Ascend Instance API
  slug: ascend-instance-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.ascend.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ascend.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ascend.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ascend.io/reference/api/ascend-api
- group: start
  title: ''
  type: Quickstart
  url: https://docs.ascend.io/getting-started/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ascend-io
- group: start
  title: ''
  type: SignUp
  url: https://app.ascend.io/signup
- group: operate
  title: ''
  type: Support
  url: https://docs.ascend.io/support
- group: build
  title: ''
  type: Packages
  url: packages/ascendio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ascendio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ascendio-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ascendio-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ascendio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ascendio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ascendio-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ascendio-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ascendio-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ascendio-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ascendio-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ascendio-llms.txt
created: '2026-07-17'
description: Ascend.io is a data engineering platform for building declarative, DataAware data pipelines that unify ingestion, transformation, and orchestration across warehouses like BigQuery, Snowflake, Databricks, and MotherDuck. Pipelines are authored in SQL, Python, and YAML and operated through Otto, Ascend's agentic AI assistant. Its developer surface is the Ascend Instance web API (/api/v1, service-account Bearer auth) exposed through the ascend-tools CLI, first-party Python/JavaScript/Rust SDKs, and an official 25-tool MCP server. Ascend announced in 2026 that it is winding down operations; the open-source tooling and documentation remain published at capture time. Added to the API Evangelist network as an Accel portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ascendio.png
layout: provider
mcp_servers:
- description: Official MCP server for the Ascend Instance web API. Exposes 25 tools for managing workspaces, deployments, environments, projects, profiles, flows, flow runs, and Otto (Ascend's agentic AI assistant)
  name: Ascend.io MCP Server
  slug: ascendio-mcp-server
modified: '2026-07-18'
name: Ascend.io
nav: Providers
network: true
overview: 'Ascend.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Big Data, Data Engineering, Data Pipeline, and ETL.


  Ascend.io''s developer surface includes documentation, API reference, quickstart, signup flow, support, CLI, authentication, and 14 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 22.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ascendio/refs/heads/main/screenshots/ascendio-2026-07-25T201409.png
security:
- kind: authentication
  name: Ascendio Authentication
  slug: ascendio-authentication
  summary_line: http-bearer/service-account · 1 scheme
- kind: domain-security
  name: Ascendio Domain Security
  slug: ascendio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ascendio
tags:
- Company
- Big Data
- Data Engineering
- Data Pipeline
- ETL
- Orchestration
- Data Automation
- MCP
- Developer Tools
website: https://www.ascend.io
---
