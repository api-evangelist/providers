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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The OpenMetadata REST API — a JWT-authenticated (Bearer) CRUD API over every data asset and governance entity in OpenMetadata (databases, schemas, tables, dashboards, charts, pipelines, topics, contai
  name: OpenMetadata REST API
  slug: collate-openmetadata-rest-api
artifact_total: 6
asyncapis:
- description: ''
  name: Collate Webhooks
  slug: collate-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://collate.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.open-metadata.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.open-metadata.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.open-metadata.org/latest/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.open-metadata.org/latest/quick-start
- group: auth
  title: ''
  type: Authentication
  url: authentication/collate-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.open-metadata.org/
- group: operate
  title: ''
  type: Support
  url: https://open-metadata.org/community
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/open-metadata
- group: start
  title: ''
  type: SignUp
  url: https://collate.com/#demo-request
- group: commercial
  title: ''
  type: TermsOfService
  url: https://collate.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://collate.com/legal/privacy
- group: start
  title: ''
  type: Sandbox
  url: sandbox/collate-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/collate-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/collate-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/collate-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/collate-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/collate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/collate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/collate-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/collate-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/collate-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/collate-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/collate-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/collate-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/collate-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/collate-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/collate-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/collate-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/collate-webhooks.yml
created: '2026-07-17'
description: Collate is the commercial company behind OpenMetadata, the open-source unified metadata platform and data catalog for data and AI. OpenMetadata provides a single place to discover, govern, observe, and collaborate on data assets — databases, tables, dashboards, pipelines, ML models, topics, containers, and API collections/endpoints — with a JSON-schema-first metadata standard, 90+ ingestion connectors, data quality and profiling, lineage, glossary, and role-based access control. Everything in the product is driven by a comprehensive JWT-authenticated REST API (plus Python and Java SDKs, a `metadata` CLI, webhook change-events, and a hosted MCP server), making the metadata layer fully programmable for humans, AI assistants, and agents. Collate offers a managed, enterprise SaaS edition of OpenMetadata. Backed by CRV and Redpoint Ventures.
image: https://avatars.githubusercontent.com/u/74767841
layout: provider
mcp_servers:
- description: ''
  name: collate-mcp.yml
  slug: collate-mcpyml
modified: '2026-07-18'
name: Collate
nav: Providers
network: true
overview: 'Collate publishes 1 API on the [APIs.io](https://apis.io/) network: OpenMetadata REST API. Tagged areas include Company, Data, Metadata, Data Catalog, and Data Governance.


  The Collate catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Collate''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, signup flow, and 23 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 48.2
  delta: 1.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 35.6
    developer_ergonomics: 80.4
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 46.6
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/collate/refs/heads/main/screenshots/collate-2026-07-25T210043.png
security:
- kind: authentication
  name: Collate Authentication
  slug: collate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Collate Domain Security
  slug: collate-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Collate Vulnerability Disclosure
  slug: collate-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: collate
tags:
- Company
- Data
- Metadata
- Data Catalog
- Data Governance
- Data Discovery
- Data Quality
- Data Lineage
- Open Source
- API
website: https://collate.com/
---
