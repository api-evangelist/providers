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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.5
  scored_at: '2026-08-19'
api_count: 6
apis:
- description: 'Import/update master data: general ledger accounts, cost dimensions, additional delivery costs.'
  name: Candis Core Data API
  slug: candis-core-data-api
- description: Export approved invoices and postings to accounting/ERP systems.
  name: Candis Exports API
  slug: candis-exports-api
- description: Read and update invoice metadata.
  name: Candis Invoices API
  slug: candis-invoices-api
- description: The Organizations API from Candis — 1 operation(s) for organizations.
  name: Candis Organizations API
  slug: candis-organizations-api
- description: Read purchase request data.
  name: Candis Purchase Requests API
  slug: candis-purchase-requests-api
- description: The Reimbursements API from Candis — 1 operation(s) for reimbursements.
  name: Candis Reimbursements API
  slug: candis-reimbursements-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Candis Core Data API
  slug: open-candis-core-data-api
- collection_type: open
  name: Candis Core Data Exports API
  slug: open-candis-exports-api
- collection_type: open
  name: Candis Core Data Invoices API
  slug: open-candis-invoices-api
- collection_type: open
  name: Candis Core Data Organizations API
  slug: open-candis-organizations-api
- collection_type: open
  name: Candis Core Data Purchase Requests API
  slug: open-candis-purchase-requests-api
- collection_type: open
  name: Candis Core Data Reimbursements API
  slug: open-candis-reimbursements-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.candis.io/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.candis.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.candis.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.candis.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.candis.io/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.candis.io/en/blog
- group: operate
  title: ''
  type: Support
  url: https://hilfe.candis.io/en
- group: start
  title: ''
  type: Login
  url: https://my.candis.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.candis.io/en/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CandisIO
- group: operate
  title: ''
  type: StatusPage
  url: https://status.candis.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.candis.io/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/candis-changelog.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/candis-openapi.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/candis-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/candis-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/candis-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/candis-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/candis-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/candis-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/candis-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/candis-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/candis-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/candis-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/candis-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/candis-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/candis-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/candis-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/candis-export-approved-invoices.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/candis-import-core-data.md
created: '2026-07-17'
description: Candis is a Berlin-based fintech (founded 2015) offering an AI-driven financial process automation and accounts-payable platform for SMEs. It captures incoming invoices, reads invoice data via OCR (business partner, amount, date, IBAN), routes them through approval workflows, and exports approved postings to accounting systems and ERPs. As a licensed DATEV interface partner it also integrates with Sage and Wolters Kluwer, and supports three-way matching of invoices against purchase orders and goods receipts. Candis exposes a public REST API (developer.candis.io) with an Export API, Core Data API, and read-only Invoice, Reimbursement Item, and Purchase Request Data APIs, secured with OAuth2/OIDC and fronted by an official MCP server.
image: https://assets.my.candis.io/open_graph/CANDIS-UI.jpg
layout: provider
mcp_servers:
- description: ''
  name: candis-mcp.yml
  slug: candis-mcpyml
modified: '2026-07-18'
name: Candis
nav: Providers
network: true
overview: 'Candis publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Core Data API, Exports API, Invoices API, and 3 more. Tagged areas include Company, Fintech, Accounts Payable, Spend Management, and Invoice Management.


  Candis'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 23 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 1
  name: Candis Rate Limits
  slug: candis-rate-limits
scopes:
- name: Candis Scopes
  scope_count: 13
  slug: candis-scopes
  summary_line: 13 scopes · authorizationCode
score:
  band: developing
  composite: 42.9
  delta: -9.1
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 30.3
    contract_quality: 58.0
    developer_ergonomics: 39.9
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 31.6
  previous_composite: 52.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/candis/refs/heads/main/screenshots/candis-2026-07-25T204341.png
security:
- kind: authentication
  name: Candis Authentication
  slug: candis-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Candis Domain Security
  slug: candis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: candis
tags:
- Company
- Fintech
- Accounts Payable
- Spend Management
- Invoice Management
- Financial Process Automation
- Accounting
- DATEV
- OCR
- Germany
website: https://www.candis.io/en
---
