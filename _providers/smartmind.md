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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Smartmind Agentic Access
  operation_count: 34
  slug: smartmind-agentic-access
  summary_line: 34 operations · 18 acting
api_count: 8
apis:
- description: The file API from SmartMind — 4 operation(s) for file.
  name: SmartMind file API
  slug: smartmind-file-api
- description: The health API from SmartMind — 1 operation(s) for health.
  name: SmartMind health API
  slug: smartmind-health-api
- description: The metric API from SmartMind — 1 operation(s) for metric.
  name: SmartMind metric API
  slug: smartmind-metric-api
- description: The query API from SmartMind — 4 operation(s) for query.
  name: SmartMind query API
  slug: smartmind-query-api
- description: The schema API from SmartMind — 2 operation(s) for schema.
  name: SmartMind schema API
  slug: smartmind-schema-api
- description: The table API from SmartMind — 7 operation(s) for table.
  name: SmartMind table API
  slug: smartmind-table-api
- description: The table_template API from SmartMind — 2 operation(s) for table_template.
  name: SmartMind table_template API
  slug: smartmind-table-template-api
- description: The view API from SmartMind — 2 operation(s) for view.
  name: SmartMind view API
  slug: smartmind-view-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: THANOSQL api file API
  slug: open-smartmind-file-api
- collection_type: open
  name: THANOSQL api file health API
  slug: open-smartmind-health-api
- collection_type: open
  name: THANOSQL api file metric API
  slug: open-smartmind-metric-api
- collection_type: open
  name: THANOSQL api file query API
  slug: open-smartmind-query-api
- collection_type: open
  name: THANOSQL api file schema API
  slug: open-smartmind-schema-api
- collection_type: open
  name: THANOSQL api file table API
  slug: open-smartmind-table-api
- collection_type: open
  name: THANOSQL api file table_template API
  slug: open-smartmind-table-template-api
- collection_type: open
  name: THANOSQL api file view API
  slug: open-smartmind-view-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smartmind-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smartmind-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smartmind-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/smartmind-thanosql-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/smartmind-thanosql-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/smartmind-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/smartmind-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/smartmind-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/smartmind-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/smartmind-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/smartmind-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/smartmind-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/smartmind-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/smartmind-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://thanosql-sdk-python.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/smartmind-team/mintlify-docs/tree/main/api-reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smartmind-team
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smartmind-ai.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smartmind-ai.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://smartmind-ai.io/contact
- group: company
  title: ''
  type: Website
  url: https://smartmind-ai.io/
created: '2026-07-17'
description: SmartMind AI Inc. is a South Korean AI company (Techstars 2020, Seoul) building ontology-based enterprise AI. Its current products are Qurify — a natural-language data analysis platform that answers questions without SQL by combining structured databases and unstructured documents through a TAG+RAG hybrid architecture and a 2-tier ontology — and AI-Minwon, a government/public-administration application built on Qurify. SmartMind's earlier product, ThanoSQL, is an analytical relational database with a built-in LLM/DL/ML query layer, exposed through a REST API (OpenAPI 3.0.2, 34 operations across query, table, schema, view, template, file-manager, health, and metric resources) and an official Python SDK (pypi:thanosql). This profile captures the still-published ThanoSQL developer surface; the hosted ThanoSQL documentation has been decommissioned.
image: https://avatars.githubusercontent.com/u/103923556?v=4
layout: provider
mcp_servers:
- description: ''
  name: smartmind-mcp.yml
  slug: smartmind-mcpyml
modified: '2026-07-21'
name: SmartMind
nav: Providers
network: true
overview: 'SmartMind publishes 8 APIs on the [APIs.io](https://apis.io/) network, including file API, health API, metric API, and 5 more. Tagged areas include Company, Artificial Intelligence, Machine Learning, Database, and Analytics.


  SmartMind''s developer surface includes authentication, documentation, API reference, support, and 18 more developer resources.'
random_paper: 81
score:
  band: thin
  composite: 36.0
  delta: 1.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 51.5
    developer_ergonomics: 42.3
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Smartmind Authentication
  slug: smartmind-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Smartmind Domain Security
  slug: smartmind-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smartmind
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Database
- Analytics
- Data
- SQL
- Ontology
- RAG
- Enterprise AI
website: https://smartmind-ai.io/
---
