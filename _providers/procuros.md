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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Procuros Agentic Access
  operation_count: 8
  slug: procuros-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 4
apis:
- description: The All Transactions API from Procuros — 2 operation(s) for all transactions.
  name: Procuros All Transactions API
  slug: procuros-all-transactions-api
- description: The Incoming Transactions API from Procuros — 3 operation(s) for incoming transactions.
  name: Procuros Incoming Transactions API
  slug: procuros-incoming-transactions-api
- description: The Misc API from Procuros — 1 operation(s) for misc.
  name: Procuros Misc API
  slug: procuros-misc-api
- description: The Outgoing Transactions API from Procuros — 2 operation(s) for outgoing transactions.
  name: Procuros Outgoing Transactions API
  slug: procuros-outgoing-transactions-api
artifact_total: 8
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.procuros.io/en/api/v2/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.procuros.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.procuros.io/en/api/v2/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.procuros.io/en/api/v2/quick-start
- group: start
  title: ''
  type: Login
  url: https://portal.procuros.io/login
- group: company
  title: ''
  type: Blog
  url: https://procuros.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/procuros
- group: commercial
  title: ''
  type: TermsOfService
  url: https://procuros.io/saas-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://procuros.io/data-processing
- group: auth
  title: ''
  type: Authentication
  url: authentication/procuros-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/procuros-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/procuros-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/procuros-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/procuros-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/procuros-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/procuros-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/procuros-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/procuros-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/procuros-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/procuros-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/procuros-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://procuros.io/
created: '2026-07-17'
description: Procuros is a Hamburg-based B2B digital trade platform that connects suppliers with retailers and logistics partners through automated document exchange. A single connection lets trading partners exchange orders, order responses, invoices, credit notes, shipping notices, dispatch instructions, product catalogs and more — whether the partner runs EDI (AS2, SFTP, X.400), PDFs, or Excel. Procuros offers ERP connectors (SAP, Microsoft Business Central, Oracle, Odoo, Weclapp, Xentral, JTL), an AI-powered Order Agent for PDF/email orders, e-invoicing compliance (ZUGFeRD, X-Rechnung, PEPPOL), logistics automation and payment reconciliation. Its REST API v2 lets integrators list incoming transactions, send outgoing transactions, mark documents processed, and report errors — backed by an OpenAPI 3.0.3 spec, cursor pagination, Bearer-token auth, and a staging environment. Backed by Creandum and Point Nine.
image: https://github.com/procuros.png
layout: provider
mcp_servers:
- description: ''
  name: procuros-mcp.yml
  slug: procuros-mcpyml
modified: '2026-07-20'
name: Procuros
nav: Providers
network: true
overview: 'Procuros publishes 4 APIs on the [APIs.io](https://apis.io/) network, including All Transactions API, Incoming Transactions API, Misc API, and 1 more. Tagged areas include Company, SaaS, EDI, E-Invoicing, and Supply Chain.


  Procuros'' developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, changelog, sandbox, and 16 more developer resources.'
random_paper: 24
score:
  band: developing
  composite: 44.5
  delta: -2.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 54.9
    developer_ergonomics: 58.2
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Procuros Authentication
  slug: procuros-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Procuros Domain Security
  slug: procuros-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: procuros
tags:
- Company
- SaaS
- EDI
- E-Invoicing
- Supply Chain
- Procurement
- B2B Integration
- Logistics
- ERP Integration
website: https://procuros.io/
---
