---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 4
  name: Mpesa Agentic Access
  operation_count: 14
  slug: mpesa-agentic-access
  summary_line: 14 operations · 9 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: The Account Balance API from M-Pesa (Safaricom Daraja) — 1 operation(s) for account balance.
  name: M-Pesa (Safaricom Daraja) Account Balance API
  slug: mpesa-account-balance-api
- description: The Authorization API from M-Pesa (Safaricom Daraja) — 1 operation(s) for authorization.
  name: M-Pesa (Safaricom Daraja) Authorization API
  slug: mpesa-authorization-api
- description: The B2B API from M-Pesa (Safaricom Daraja) — 2 operation(s) for b2b.
  name: M-Pesa (Safaricom Daraja) B2B API
  slug: mpesa-b2b-api
- description: The B2C API from M-Pesa (Safaricom Daraja) — 1 operation(s) for b2c.
  name: M-Pesa (Safaricom Daraja) B2C API
  slug: mpesa-b2c-api
- description: The C2B API from M-Pesa (Safaricom Daraja) — 2 operation(s) for c2b.
  name: M-Pesa (Safaricom Daraja) C2B API
  slug: mpesa-c2b-api
- description: The Dynamic QR API from M-Pesa (Safaricom Daraja) — 1 operation(s) for dynamic qr.
  name: M-Pesa (Safaricom Daraja) Dynamic QR API
  slug: mpesa-dynamic-qr-api
- description: The M-Pesa Express API from M-Pesa (Safaricom Daraja) — 2 operation(s) for m-pesa express.
  name: M-Pesa (Safaricom Daraja) M-Pesa Express API
  slug: mpesa-m-pesa-express-api
- description: The Reversal API from M-Pesa (Safaricom Daraja) — 1 operation(s) for reversal.
  name: M-Pesa (Safaricom Daraja) Reversal API
  slug: mpesa-reversal-api
- description: The Standing Order API from M-Pesa (Safaricom Daraja) — 1 operation(s) for standing order.
  name: M-Pesa (Safaricom Daraja) Standing Order API
  slug: mpesa-standing-order-api
- description: The Tax Remittance API from M-Pesa (Safaricom Daraja) — 1 operation(s) for tax remittance.
  name: M-Pesa (Safaricom Daraja) Tax Remittance API
  slug: mpesa-tax-remittance-api
- description: The Transaction Status API from M-Pesa (Safaricom Daraja) — 1 operation(s) for transaction status.
  name: M-Pesa (Safaricom Daraja) Transaction Status API
  slug: mpesa-transaction-status-api
artifact_total: 44
asyncapis:
- description: The asynchronous callback (webhook) surface of the M-Pesa Daraja API. Daraja delivers the real outcome of collections and funds-movement operations by POSTing JSON to caller-hosted HTTPS endpoints. Th
  name: M-Pesa Daraja Callbacks
  slug: mpesa-callbacks-asyncapi
collections:
- collection_type: postman
  name: M-Pesa Daraja Account Balance API
  slug: postman-mpesa-account-balance-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance Authorization API
  slug: postman-mpesa-authorization-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance B2B API
  slug: postman-mpesa-b2b-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance B2C API
  slug: postman-mpesa-b2c-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance C2B API
  slug: postman-mpesa-c2b-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance Dynamic QR API
  slug: postman-mpesa-dynamic-qr-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance M-Pesa Express API
  slug: postman-mpesa-m-pesa-express-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance Reversal API
  slug: postman-mpesa-reversal-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance Standing Order API
  slug: postman-mpesa-standing-order-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance Tax Remittance API
  slug: postman-mpesa-tax-remittance-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance Transaction Status API
  slug: postman-mpesa-transaction-status-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: M-Pesa Daraja Account Balance API
  slug: open-mpesa-account-balance-api
- collection_type: open
  name: M-Pesa Daraja Account Balance Authorization API
  slug: open-mpesa-authorization-api
- collection_type: open
  name: M-Pesa Daraja Account Balance B2B API
  slug: open-mpesa-b2b-api
- collection_type: open
  name: M-Pesa Daraja Account Balance B2C API
  slug: open-mpesa-b2c-api
- collection_type: open
  name: M-Pesa Daraja Account Balance C2B API
  slug: open-mpesa-c2b-api
- collection_type: open
  name: M-Pesa Daraja Account Balance Dynamic QR API
  slug: open-mpesa-dynamic-qr-api
- collection_type: open
  name: M-Pesa Daraja Account Balance M-Pesa Express API
  slug: open-mpesa-m-pesa-express-api
- collection_type: open
  name: M-Pesa Daraja Account Balance Reversal API
  slug: open-mpesa-reversal-api
- collection_type: open
  name: M-Pesa Daraja Account Balance Standing Order API
  slug: open-mpesa-standing-order-api
- collection_type: open
  name: M-Pesa Daraja Account Balance Tax Remittance API
  slug: open-mpesa-tax-remittance-api
- collection_type: open
  name: M-Pesa Daraja Account Balance Transaction Status API
  slug: open-mpesa-transaction-status-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/m-pesa-safaricom-daraja/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mpesa-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mpesa-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mpesa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mpesa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mpesa-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/safaricom
- group: company
  title: ''
  type: Website
  url: https://developer.safaricom.co.ke/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.safaricom.co.ke/APIs
- group: commercial
  title: ''
  type: Plans
  url: plans/mpesa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mpesa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mpesa-finops.yml
- group: auth
  title: ''
  type: Security
  url: security/mpesa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: security/mpesa-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mpesa-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/mpesa-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mpesa-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mpesa-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/mpesa-openapi-overlay.yaml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mpesa-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/mpesa-result-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mpesa-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mpesa-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/mpesa-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mpesa-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mpesa-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/mpesa-callbacks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mpesa-callbacks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.safaricom.co.ke/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.safaricom.co.ke/APIs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.safaricom.co.ke/
- group: operate
  title: ''
  type: Support
  url: https://developer.safaricom.co.ke/faqs
- group: start
  title: ''
  type: SignUp
  url: https://developer.safaricom.co.ke/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.safaricom.co.ke/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.safaricom.co.ke/data-privacy-statements
- group: build
  title: ''
  type: Postman
  url: collections/mpesa.postman_collection.json
created: '2026-07-17'
description: M-Pesa is Safaricom's mobile-money platform for Kenya, exposed to developers through the Daraja API. The Daraja REST APIs let businesses collect payments (M-Pesa Express / STK Push, C2B), disburse funds (B2C, B2B), query transactions and balances, reverse payments, generate dynamic QR codes, and run standing orders — authorized with OAuth bearer tokens minted from Basic credentials, priced in Kenyan Shillings (KES).
finops:
- name: Mpesa Finops
  service_category: Payments and Financial Services
  slug: mpesa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mpesa.png
layout: provider
mcp_servers:
- description: 'Safaricom does not operate an official hosted/remote MCP server for Daraja. Community MCP servers exist (e.g. mboya/daraja-mcp on lobehub) but are not first-party. The tool list below is a CANDIDATE, '
  name: M-Pesa (Safaricom Daraja) MCP Server
  slug: m-pesa-safaricom-daraja-mcp-server
modified: '2026-07-17'
name: M-Pesa (Safaricom Daraja)
nav: Providers
network: true
overview: 'M-Pesa (Safaricom Daraja) publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Account Balance API, Authorization API, B2B API, and 8 more. Tagged areas include Mobile Money, Payments, Fintech, Kenya, and Africa.


  The M-Pesa (Safaricom Daraja) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  M-Pesa (Safaricom Daraja)''s developer surface includes authentication, documentation, sandbox, API reference, getting-started guide, support, signup flow, and 30 more developer resources.'
plans:
- name: Mpesa Plans Pricing
  plan_count: 3
  slug: mpesa-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Mpesa Rate Limits
  slug: mpesa-rate-limits
score:
  band: strong
  composite: 62.3
  coverage:
    artifact_dirs: 23
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 4.5
    contract_quality: 57.5
    developer_ergonomics: 51.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 62.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mpesa/refs/heads/main/screenshots/mpesa-2026-08-07T184414.png
security:
- kind: authentication
  name: Mpesa Authentication
  slug: mpesa-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Mpesa Domain Security
  slug: mpesa-domain-security
  summary_line: HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mpesa Vulnerability Disclosure
  slug: mpesa-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Mpesa Trust Center
  slug: mpesa-trust-center
  summary_line: PCI DSS v4, ISO/IEC 27001, ISO/IEC 27701, GDPR-aligned / Kenya Data Protection Act 2019
slug: mpesa
tags:
- Mobile Money
- Payments
- Fintech
- Kenya
- Africa
- M-PESA
website: https://developer.safaricom.co.ke/
---
