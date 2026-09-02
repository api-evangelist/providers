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
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 26
  human_in_the_loop: 2
  name: Feldera Agentic Access
  operation_count: 60
  slug: feldera-agentic-access
  summary_line: 60 operations · 26 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The Input Connectors API from Feldera — 5 operation(s) for input connectors.
  name: Feldera Input Connectors API
  slug: feldera-input-connectors-api
- description: The Metrics & Debugging API from Feldera — 15 operation(s) for metrics & debugging.
  name: Feldera Metrics & Debugging API
  slug: feldera-metrics-debugging-api
- description: The Output Connectors API from Feldera — 2 operation(s) for output connectors.
  name: Feldera Output Connectors API
  slug: feldera-output-connectors-api
- description: The Pipeline CRUD API from Feldera — 2 operation(s) for pipeline crud.
  name: Feldera Pipeline CRUD API
  slug: feldera-pipeline-crud-api
- description: The Pipeline Lifecycle API from Feldera — 20 operation(s) for pipeline lifecycle.
  name: Feldera Pipeline Lifecycle API
  slug: feldera-pipeline-lifecycle-api
- description: The Platform API from Feldera — 9 operation(s) for platform.
  name: Feldera Platform API
  slug: feldera-platform-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Feldera Input Connectors API
  slug: open-feldera-input-connectors-api
- collection_type: open
  name: Feldera Input Connectors Metrics & Debugging API
  slug: open-feldera-metrics-debugging-api
- collection_type: open
  name: Feldera Input Connectors Output Connectors API
  slug: open-feldera-output-connectors-api
- collection_type: open
  name: Feldera Input Connectors Pipeline CRUD API
  slug: open-feldera-pipeline-crud-api
- collection_type: open
  name: Feldera Input Connectors Pipeline Lifecycle API
  slug: open-feldera-pipeline-lifecycle-api
- collection_type: open
  name: Feldera Input Connectors Platform API
  slug: open-feldera-platform-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.feldera.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.feldera.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.feldera.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.feldera.com/get-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/feldera-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/feldera-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/feldera-openapi-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/feldera-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/feldera-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/feldera-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/feldera-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/feldera-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/feldera-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/feldera-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/feldera-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/feldera-agentic-access.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/feldera-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/feldera-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://feldera.statuspage.io
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.feldera.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/feldera-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/feldera-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.feldera.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/feldera-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/feldera-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.feldera.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/feldera
- group: operate
  title: ''
  type: Support
  url: https://join.slack.com/t/felderacommunity/shared_invite/zt-3vf3n5dj5-HJuC1DFFY2wE1_AZUyNxqw
- group: commercial
  title: ''
  type: Pricing
  url: https://www.feldera.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://try.feldera.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.feldera.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.feldera.com/privacy
- group: company
  title: ''
  type: Website
  url: https://www.feldera.com
created: '2026-07-17'
description: Feldera is an incremental compute engine for running complex SQL data pipelines in real time. Rather than reprocessing entire datasets, it updates materialized views proportionally to the changes in the input data, delivering low-latency, low-cost results for use cases such as fraud detection, feature engineering, change data capture, and real-time dashboards. Feldera is built on the DBSP incremental computation theory and is available as an open-source engine, a self-hosted enterprise platform, and a hosted online sandbox (try.feldera.com). Developers define pipelines as SQL programs with input/output connectors and manage them through the Feldera REST API, a Python client, and the fda CLI. Backed by Costanoa Ventures.
image: https://cdn.sanity.io/images/nlte859i/production/1c2e10b5e5fe2946c6c16f7b4a0790214f186c81-1280x640.png
layout: provider
mcp_servers:
- description: ''
  name: Feldera MCP Server
  slug: feldera-mcp-server
modified: '2026-07-19'
name: Feldera
nav: Providers
network: true
overview: 'Feldera publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Input Connectors API, Metrics & Debugging API, Output Connectors API, and 3 more. Tagged areas include Company, Data Infrastructure, Streaming, SQL, and Incremental View Maintenance.


  Feldera''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, sandbox, changelog, and 27 more developer resources.'
random_paper: 9
score:
  band: strong
  composite: 57.6
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 63.0
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 57.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/feldera/refs/heads/main/screenshots/feldera-2026-07-25T214327.png
security:
- kind: authentication
  name: Feldera Authentication
  slug: feldera-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Feldera Domain Security
  slug: feldera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Feldera Trust Center
  slug: feldera-trust-center
  summary_line: SOC 2
slug: feldera
tags:
- Company
- Data Infrastructure
- Streaming
- SQL
- Incremental View Maintenance
- Real-Time Analytics
- Change Data Capture
- Materialized Views
- Data Pipeline
website: https://www.feldera.com
---
