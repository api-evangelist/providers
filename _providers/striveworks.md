---
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Per-tenant REST API for the Chariot AI operations platform, organized as versioned microservice paths under /api/{service}/{version}/ — identity, training, evaluation, notification, catalog, serve and
  name: Chariot Platform API
  slug: chariot-platform-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/striveworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.striveworks.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://production.chariot.striveworks.us/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://production.chariot.striveworks.us/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://production.chariot.striveworks.us/docs/sdk_api_docs/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://production.chariot.striveworks.us/docs/sdk/sdk
- group: company
  title: ''
  type: Blog
  url: https://www.striveworks.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Striveworks
- group: operate
  title: ''
  type: ChangeLog
  url: https://production.chariot.striveworks.us/docs/release_notes/notes
- group: auth
  title: ''
  type: Authentication
  url: authentication/striveworks-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/striveworks-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/striveworks-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/striveworks-conformance.yml
- group: build
  title: ''
  type: CLI
  url: cli/striveworks-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/striveworks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/striveworks-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/striveworks-llms.txt
- group: company
  title: ''
  type: Careers
  url: https://job-boards.greenhouse.io/striveworks
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/striveworks_stock/
created: '2026-08-05'
description: 'Striveworks is an Austin, Texas enterprise AI operations (AIOps) company whose platform, Chariot, lets organizations build, deploy, monitor and continuously retrain machine-learning models — in hours rather than months — across cloud, on-premises, disconnected and edge environments. Chariot covers the full model lifecycle: dataset management and versioning, AI-assisted annotation, code-free and custom-code training, a model catalog with model cards and staging, evaluation and model comparison, inference servers and pluggable inference engines (vLLM, TorchServe, KServe v2, OpenAI-compatible and Hugging Face), an inference store for querying production predictions, drift detection and monitoring, and an alpha agentic-workflows framework that runs guard-railed AI agents wired to remote MCP servers. Programmatic access is through a per-tenant REST API secured with OAuth 2.0 client credentials, a first-party Python SDK (chariot-client) and the `chariot` CLI. Striveworks works heavily
  with US defense and federal customers, including US Army and US Navy AI programs.'
image: https://cdn.prod.website-files.com/687f6a68c97e16777c3d2778/689f6daf828285a886335b48_open%20graph.png
layout: provider
modified: '2026-08-05'
name: Striveworks
nav: Providers
network: true
overview: 'Striveworks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, MLOps, and AIOps.


  Striveworks'' developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, authentication, CLI, and 12 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 66.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 27.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Striveworks Authentication
  slug: striveworks-authentication
  summary_line: oauth2/http/mutualTLS · 3 schemes
- kind: domain-security
  name: Striveworks Domain Security
  slug: striveworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: striveworks
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- MLOps
- AIOps
- Model Deployment
- Model Monitoring
- Inference
- Data Annotation
- Computer-Vision
- Agentic Workflows
- Defense
- GovTech
- Edge Computing
website: https://www.striveworks.com/
---
