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
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Roadsync Agentic Access
  operation_count: 77
  slug: roadsync-agentic-access
  summary_line: 77 operations · 27 acting
api_count: 18
apis:
- description: Authenticated operations not otherwise functionally categorized
  name: Roadsync authenticated API
  slug: roadsync-authenticated-api
- description: The brokers API from Roadsync — 2 operation(s) for brokers.
  name: Roadsync brokers API
  slug: roadsync-brokers-api
- description: Department operations
  name: Roadsync department API
  slug: roadsync-department-api
- description: The directory API from Roadsync — 1 operation(s) for directory.
  name: Roadsync directory API
  slug: roadsync-directory-api
- description: ETA (Estimated Time of Arrival) endpoints
  name: Roadsync eta API
  slug: roadsync-eta-api
- description: The funding sources API from Roadsync — 2 operation(s) for funding sources.
  name: Roadsync funding sources API
  slug: roadsync-funding-sources-api
- description: Invoice operations
  name: Roadsync invoice API
  slug: roadsync-invoice-api
- description: The loads API from Roadsync — 2 operation(s) for loads.
  name: Roadsync loads API
  slug: roadsync-loads-api
- description: Company location operations
  name: Roadsync location API
  slug: roadsync-location-api
- description: The payables API from Roadsync — 2 operation(s) for payables.
  name: Roadsync payables API
  slug: roadsync-payables-api
- description: The payees end point
  name: Roadsync payees API
  slug: roadsync-payees-api
- description: Payment API Operations
  name: Roadsync payment API
  slug: roadsync-payment-api
- description: The ping API from Roadsync — 1 operation(s) for ping.
  name: Roadsync ping API
  slug: roadsync-ping-api
- description: Product operations (company)
  name: Roadsync product API
  slug: roadsync-product-api
- description: Shift operations (company/ location)
  name: Roadsync shift API
  slug: roadsync-shift-api
- description: The transactions API from Roadsync — 2 operation(s) for transactions.
  name: Roadsync transactions API
  slug: roadsync-transactions-api
- description: Unauthenticated operations not otherwise functionally categorized
  name: Roadsync unauthenticated API
  slug: roadsync-unauthenticated-api
- description: The Workorders API
  name: Roadsync workorders API
  slug: roadsync-workorders-api
artifact_total: 41
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Client API v1.8 authenticated API
  slug: open-roadsync-authenticated-api
- collection_type: open
  name: Client API v1.8 authenticated brokers API
  slug: open-roadsync-brokers-api
- collection_type: open
  name: Client API v1.8 authenticated department API
  slug: open-roadsync-department-api
- collection_type: open
  name: Client API v1.8 authenticated directory API
  slug: open-roadsync-directory-api
- collection_type: open
  name: Client API v1.8 authenticated eta API
  slug: open-roadsync-eta-api
- collection_type: open
  name: Client API v1.8 authenticated funding sources API
  slug: open-roadsync-funding-sources-api
- collection_type: open
  name: Client API v1.8 authenticated invoice API
  slug: open-roadsync-invoice-api
- collection_type: open
  name: Client API v1.8 authenticated loads API
  slug: open-roadsync-loads-api
- collection_type: open
  name: Client API v1.8 authenticated location API
  slug: open-roadsync-location-api
- collection_type: open
  name: Client API v1.8 authenticated payables API
  slug: open-roadsync-payables-api
- collection_type: open
  name: Client API v1.8 authenticated payees API
  slug: open-roadsync-payees-api
- collection_type: open
  name: Client API v1.8 authenticated payment API
  slug: open-roadsync-payment-api
- collection_type: open
  name: Client API v1.8 authenticated ping API
  slug: open-roadsync-ping-api
- collection_type: open
  name: Client API v1.8 authenticated product API
  slug: open-roadsync-product-api
- collection_type: open
  name: Client API v1.8 authenticated shift API
  slug: open-roadsync-shift-api
- collection_type: open
  name: Client API v1.8 authenticated transactions API
  slug: open-roadsync-transactions-api
- collection_type: open
  name: Client API v1.8 authenticated unauthenticated API
  slug: open-roadsync-unauthenticated-api
- collection_type: open
  name: Client API v1.8 authenticated workorders API
  slug: open-roadsync-workorders-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/roadsync-client-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.roadsync.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.roadsync.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.roadsync.com/api/
- group: auth
  title: ''
  type: Authentication
  url: authentication/roadsync-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/roadsync-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/roadsync-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/roadsync-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/roadsync-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/roadsync-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: http://status.roadsync.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/roadsync-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/roadsync-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/roadsync-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/roadsync-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/roadsync-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/roadsync-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/roadsync-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/roadsync-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/roadsync-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://roadsync.com/contact-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://learn.roadsync.com/knowledge
- group: company
  title: ''
  type: Blog
  url: https://roadsync.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://roadsync.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://roadsync.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://www.roadsync.com/
created: '2026-07-17'
description: 'RoadSync is a digital payments and expense-management platform for the logistics and trucking industry, enabling warehouses, repair and tow shops, brokers, and carriers to accept and disburse payments faster. RoadSync publishes a REST API surface across six services: the RoadSyncPay Public API (payees, funding sources, payables, transactions, brokers, loads for ACH/paper-check/RTP carrier disbursements), the Invoice API (create, send, void, clone, refund, and embed invoices), the Company API (locations and product catalog), the WorkOrders API (create, send, approve work orders), a Payment API for taking payments, and a legacy Client API. All APIs are HTTPS REST, authenticated with an x-api-key header, versioned in the URI path, and split into test and production hosts.'
image: https://roadsync.com/wp-content/uploads/2022/05/cropped-RS-1000-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: roadsync-mcp.yml
  slug: roadsync-mcpyml
modified: '2026-07-21'
name: Roadsync
nav: Providers
network: true
overview: 'Roadsync publishes 18 APIs on the [APIs.io](https://apis.io/) network, including authenticated API, brokers API, department API, and 15 more. Tagged areas include Company, Financial Services, Payments, Logistics, and Trucking.


  Roadsync''s developer surface includes documentation, API reference, authentication, sandbox, support, engineering blog, and 21 more developer resources.'
random_paper: 122
score:
  band: thin
  composite: 41.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 56.8
    developer_ergonomics: 58.2
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Roadsync Authentication
  slug: roadsync-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Roadsync Domain Security
  slug: roadsync-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: roadsync
tags:
- Company
- Financial Services
- Payments
- Logistics
- Trucking
- Invoicing
- Transportation
- Fintech
website: https://www.roadsync.com/
---
