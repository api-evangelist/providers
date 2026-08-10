---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Orbii Agentic Access
  operation_count: 161
  slug: orbii-agentic-access
  summary_line: 161 operations · 29 acting
api_count: 15
apis:
- description: The Business Category Assignment API from Orbii — 1 operation(s) for business category assignment.
  name: Orbii Business Category Assignment API
  slug: orbii-business-category-assignment-api
- description: The Categories API from Orbii — 1 operation(s) for categories.
  name: Orbii Categories API
  slug: orbii-categories-api
- description: The Clients API from Orbii — 2 operation(s) for clients.
  name: Orbii Clients API
  slug: orbii-clients-api
- description: The Company Management API from Orbii — 1 operation(s) for company management.
  name: Orbii Company Management API
  slug: orbii-company-management-api
- description: The Data Check API from Orbii — 1 operation(s) for data check.
  name: Orbii Data Check API
  slug: orbii-data-check-api
- description: The General API from Orbii — 1 operation(s) for general.
  name: Orbii General API
  slug: orbii-general-api
- description: The IBANs API from Orbii — 1 operation(s) for ibans.
  name: Orbii IBANs API
  slug: orbii-ibans-api
- description: The Invoices API from Orbii — 11 operation(s) for invoices.
  name: Orbii Invoices API
  slug: orbii-invoices-api
- description: The KPIs API from Orbii — 6 operation(s) for kpis.
  name: Orbii KPIs API
  slug: orbii-kpis-api
- description: The Lending Actions API from Orbii — 1 operation(s) for lending actions.
  name: Orbii Lending Actions API
  slug: orbii-lending-actions-api
- description: The Merchants API from Orbii — 8 operation(s) for merchants.
  name: Orbii Merchants API
  slug: orbii-merchants-api
- description: The PDFs API from Orbii — 4 operation(s) for pdfs.
  name: Orbii PDFs API
  slug: orbii-pdfs-api
- description: The Risk Assessment API from Orbii — 5 operation(s) for risk assessment.
  name: Orbii Risk Assessment API
  slug: orbii-risk-assessment-api
- description: The Subcategories API from Orbii — 1 operation(s) for subcategories.
  name: Orbii Subcategories API
  slug: orbii-subcategories-api
- description: The Transactions API from Orbii — 16 operation(s) for transactions.
  name: Orbii Transactions API
  slug: orbii-transactions-api
artifact_total: 19
common:
- group: company
  title: ''
  type: Website
  url: https://orbii.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.docs.orbii.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api.docs.orbii.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api.docs.orbii.ai/uae/docs/orbii-api-v-1-0-5-oas3
- group: company
  title: ''
  type: Blog
  url: https://www.orbii.ai/news
- group: operate
  title: ''
  type: Support
  url: https://join.slack.com/t/orbii/shared_invite/zt-3dyey2n3l-6E880uPZ33_TsUPW3XMgkQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orbiiai
- group: auth
  title: ''
  type: Authentication
  url: authentication/orbii-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/orbii-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/orbii-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/orbii-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/orbii-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/orbii-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/orbii-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orbii-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orbii-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/orbii-uae-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/orbii-ksa-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/orbii-omn-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orbii-domain-security.yml
created: '2026-07-17'
description: Orbii is a Riyadh-based credit infrastructure company providing AI-powered underwriting and lending infrastructure for banks, fintechs, neobanks, and B2B platforms across the MENA region. Its APIs ingest and enrich transaction and invoice data to produce borrower intelligence — client and predictive KPIs, risk assessments, band classifications, and suggested loan allocations — so lenders can launch SME lending products (salary advance, merchant financing, working capital, BNPL, embedded lending) without building an internal credit function. Orbii exposes region-specific REST APIs for Saudi Arabia (KSA), the United Arab Emirates (UAE), and Oman (OMN), documented on a SwaggerHub portal. Backed by a $3.6M seed round led by Prosus Ventures.
image: https://cdn.prod.website-files.com/6894ac031d066c1f144fb082/68bdc4495f740a290c12b9c4_dark.webp
layout: provider
mcp_servers:
- description: ''
  name: orbii-mcp.yml
  slug: orbii-mcpyml
modified: '2026-07-20'
name: Orbii
nav: Providers
network: true
overview: 'Orbii publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Business Category Assignment API, Categories API, Clients API, and 12 more. Tagged areas include Company, Ai, Lending, Credit, and Fintech.


  Orbii''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 16 more developer resources.'
random_paper: 69
score:
  band: thin
  composite: 30.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 50.7
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orbii/refs/heads/main/screenshots/orbii-2026-08-07T190850.png
security:
- kind: authentication
  name: Orbii Authentication
  slug: orbii-authentication
  summary_line: query-credentials · 1 scheme
- kind: domain-security
  name: Orbii Domain Security
  slug: orbii-domain-security
  summary_line: TLSv1.3
slug: orbii
tags:
- Company
- Ai
- Lending
- Credit
- Fintech
- Underwriting
- Banking
- SME
- Embedded Finance
- MENA
- Risk
website: https://orbii.ai
---
