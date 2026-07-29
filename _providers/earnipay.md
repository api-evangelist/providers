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
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 50
  human_in_the_loop: 50
  name: Earnipay Agentic Access
  operation_count: 69
  slug: earnipay-agentic-access
  summary_line: 69 operations · 50 acting · 50 human-in-the-loop
api_count: 13
apis:
- description: The App API from Earnipay — 1 operation(s) for app.
  name: Earnipay App API
  slug: earnipay-app-api
- description: Third-party APP provider integration (Taxly) for FIRS submission
  name: Earnipay APP Provider API
  slug: earnipay-app-provider-api
- description: User authentication and authorization endpoints
  name: Earnipay Authentication API
  slug: earnipay-authentication-api
- description: The Bank API from Earnipay — 2 operation(s) for bank.
  name: Earnipay Bank API
  slug: earnipay-bank-api
- description: Business profile management and FIRS configuration
  name: Earnipay Business API
  slug: earnipay-business-api
- description: Customer management for invoicing
  name: Earnipay Customers API
  slug: earnipay-customers-api
- description: Invoice creation, management, and FIRS validation
  name: Earnipay Invoices API
  slug: earnipay-invoices-api
- description: Generate FIRS-compliant Invoice Reference Numbers
  name: Earnipay IRN Generator API
  slug: earnipay-irn-generator-api
- description: The Payment Details API from Earnipay — 2 operation(s) for payment details.
  name: Earnipay Payment Details API
  slug: earnipay-payment-details-api
- description: The Products API from Earnipay — 2 operation(s) for products.
  name: Earnipay Products API
  slug: earnipay-products-api
- description: Generate FIRS-compliant encrypted QR codes for invoices
  name: Earnipay QR Code Generator API
  slug: earnipay-qr-code-generator-api
- description: Team member and invitation management
  name: Earnipay Team API
  slug: earnipay-team-api
- description: User profile management
  name: Earnipay Users API
  slug: earnipay-users-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/earnipay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/earnipay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/earnipay-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/earnipay-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/earnipay-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/earnipay-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/earnipay-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/earnipay-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/earnipay-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/earnipay-e-invoicing-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/earnipay-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.earnipay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.earnipay.com/docs/e-invoice
- group: docs
  title: ''
  type: APIReference
  url: https://e-invoicing.earnipay.com/api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.earnipay.com/docs/e-invoice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Earnipay
- group: company
  title: ''
  type: Website
  url: https://earnipay.com/
created: '2026-07-17'
description: Earnipay is a Nigerian fintech that operates an NRS/FIRS-compliant e-invoicing platform for businesses. As an accredited Nigeria Revenue Service (NRS) and NITDA systems integrator, Earnipay lets developers programmatically create businesses, manage customers and products, generate FIRS-compliant invoices with IRN (Invoice Reference Number) and QR codes, and submit them to the tax authority through an Access Point Provider (APP) connection. The public Earnipay Invoicing API is an OpenAPI 3.0.0 REST service covering authentication, businesses, customers, products, payment details, invoices, IRN and QR generation, bank lookup/verification, and team management. It authenticates with JWT bearer tokens for user-facing flows and an X-API-Key header for third-party integrations. Added to the API Evangelist network as a portfolio company of Canaan Partners.
image: https://earnipay-api-storage-prod.s3.eu-west-1.amazonaws.com/business-documents/business-img-others.png
layout: provider
mcp_servers:
- description: ''
  name: earnipay-mcp.yml
  slug: earnipay-mcpyml
modified: '2026-07-18'
name: Earnipay
nav: Providers
network: true
overview: 'Earnipay publishes 13 APIs on the [APIs.io](https://apis.io/) network, including App API, APP Provider API, Authentication API, and 10 more. Tagged areas include Company, E-Invoicing, Invoicing, FIRS, and NRS.


  Earnipay''s developer surface includes authentication, documentation, API reference, getting-started guide, and 14 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 31.2
  delta: -4.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 47.4
    developer_ergonomics: 49.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/earnipay/refs/heads/main/screenshots/earnipay-2026-07-25T212700.png
security:
- kind: authentication
  name: Earnipay Authentication
  slug: earnipay-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Earnipay Domain Security
  slug: earnipay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: earnipay
tags:
- Company
- E-Invoicing
- Invoicing
- FIRS
- NRS
- Tax
- Compliance
- Fintech
- Nigeria
- Payments
- Financial Services
website: https://earnipay.com/
---
