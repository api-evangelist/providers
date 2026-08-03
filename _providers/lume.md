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
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.3
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: 'REST API for automating data mappings and transformations with AI. Create and run Flows, manage target schemas, poll job/run status, and retrieve mapping results. Authenticated with a per-account API '
  name: Lume API
  slug: lume-api
artifact_total: 5
asyncapis:
- description: ''
  name: Lume Webhooks
  slug: lume-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lume.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lume.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lume.ai/pages/documentation/getting_started/quickstart.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lume-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/lume-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lume-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lume-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lume-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lume-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lume-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.lume.ai/pages/documentation/security/security.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lume-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lume-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lume-data-model.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lume-ai
- group: start
  title: ''
  type: SignUp
  url: https://app.lume.ai
- group: start
  title: ''
  type: Login
  url: https://app.lume.ai
- group: operate
  title: ''
  type: Support
  url: https://docs.lume.ai/pages/knowledge_base/faq.md
created: '2026-07-17'
description: Lume is an AI-powered customer data integration platform for software teams. Its models handle schema discovery, suggest intelligent field-level data mappings, validate data quality, and generate transformation code automatically, turning a manual data-onboarding process into a fast, repeatable pipeline. Teams create Flows and Projects that map arbitrary source data (CSV/S3, relational databases such as PostgreSQL or Snowflake, and API payloads) to their own internal target schemas. Lume exposes a REST API and first-party Python and TypeScript SDKs, delivers run results via webhooks, and is SOC 2 Type 1 and Type 2 compliant. Backed by General Catalyst, Khosla Ventures, Floodgate, Soma Capital, and Y Combinator; in March 2026 Lume joined Harvey AI.
image: https://app.lume.ai/assets/logo-256.png
layout: provider
mcp_servers:
- description: ''
  name: lume-mcp.yml
  slug: lume-mcpyml
modified: '2026-07-20'
name: Lume
nav: Providers
network: true
overview: 'Lume publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Integration, Data Mapping, ETL, and Data Transformation.


  The Lume catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lume''s developer surface includes documentation, getting-started guide, authentication, signup flow, support, and 13 more developer resources.'
random_paper: 55
score:
  band: thin
  composite: 39.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 13.2
  previous_composite: 39.5
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lume/refs/heads/main/screenshots/lume-2026-07-25T225704.png
security:
- kind: authentication
  name: Lume Authentication
  slug: lume-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lume Domain Security
  slug: lume-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lume
tags:
- Company
- Data Integration
- Data Mapping
- ETL
- Data Transformation
- Artificial Intelligence
- Schema Mapping
- Data Quality
- Developer Tools
website: https://docs.lume.ai
---
