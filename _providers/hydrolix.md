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
    error_semantics: false
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
  score: 9.6
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: Configure and manage a Hydrolix cluster — orgs, projects, tables, transforms, functions, jobs, and service accounts.
  name: Hydrolix Config API
  slug: hydrolix-config-api
- description: Real-time HTTP streaming data ingestion into Hydrolix tables.
  name: Hydrolix Stream API
  slug: hydrolix-stream-api
- description: Execute ClickHouse SQL queries against Hydrolix and retrieve results.
  name: Hydrolix Query API
  slug: hydrolix-query-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://hydrolix.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hydrolix.io/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hydrolix.io/latest/openapi/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hydrolix
- group: operate
  title: ''
  type: StatusPage
  url: https://hydrolixstatus.com
- group: start
  title: ''
  type: SignUp
  url: https://hydrolix.io/aws-marketplace
- group: build
  title: ''
  type: Packages
  url: packages/hydrolix-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hydrolix-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/hydrolix-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hydrolix-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hydrolix-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hydrolix-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hydrolix-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hydrolix-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hydrolix-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hydrolix-domain-security.yml
created: '2026-07-17'
description: 'Hydrolix is a real-time log analytics and observability platform built as a streaming data lake: it decouples ingest, storage, and compute so teams can retain full-fidelity log and event data cost-effectively for 15+ months while still serving low-latency queries and dashboards. Data is ingested through an HTTP Streaming API, Amazon Kinesis / Data Firehose, S3 autoingest, and OpenTelemetry, then queried with the ClickHouse SQL dialect via a Query API, MCP server, and connectors for Grafana, Trino, Spark/Databricks, and Splunk. Hydrolix deploys in the customer''s own cloud (BYOC on AWS/GCP/Kubernetes) and exposes a Config API, Stream API, and Query API, a hdxcli command-line tool, and an official Model Context Protocol server.'
image: https://avatars.githubusercontent.com/u/50281978?v=4
layout: provider
mcp_servers:
- description: ''
  name: Hydrolix MCP Server
  slug: hydrolix-mcp-server
modified: '2026-07-19'
name: Hydrolix
nav: Providers
network: true
overview: 'Hydrolix publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Observability, Log Analytics, Data Lake, and Streaming.


  Hydrolix''s developer surface includes documentation, API reference, signup flow, CLI, authentication, and 12 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 20.1
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hydrolix/refs/heads/main/screenshots/hydrolix-2026-07-25T221832.png
security:
- kind: authentication
  name: Hydrolix Authentication
  slug: hydrolix-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Hydrolix Domain Security
  slug: hydrolix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hydrolix
tags:
- Company
- Observability
- Log Analytics
- Data Lake
- Streaming
- ClickHouse
- Monitoring
- Time Series
website: https://hydrolix.io
---
