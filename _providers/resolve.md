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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.2
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: OAuth access keys are created in Merchant Dashboard and can be exchanged for bearer tokens. Use the `/access-keys/token` endpoint to mint a bearer token from a valid `client_id` and `client_secret`.
  name: Resolve Access Keys API
  slug: resolve-access-keys-api
- description: A charge represents an agreement by the customer to accept credit terms for a transaction. It consists of a charge amount, term length (i.e. 30, 60, 90), and reference to the merchant's original order
  name: Resolve Charges API
  slug: resolve-charges-api
- description: Credit Notes are issued to customers to reduce the amount they owe.
  name: Resolve Credit Notes API
  slug: resolve-credit-notes-api
- description: A customer represents a company that you do business with. For larger companies, there may be several users with access to the customer account that can make purchases with their credit line. For smal
  name: Resolve Customers API
  slug: resolve-customers-api
- description: 'The invoice represents the business transaction between you and your customer. In Resolve, an invoice must be tied to a customer and an advance can be taken on the invoice. For an advance to be taken '
  name: Resolve Invoices API
  slug: resolve-invoices-api
- description: Merchant-scoped operations for managing sub-merchant resources. The merchant document upload endpoint creates a document record and starts transfer into Resolve-managed storage for validation.
  name: Resolve Merchants API
  slug: resolve-merchants-api
- description: An order represents an authorization of credit for a customer transaction. Once authorized, an order can be partially or fully captured as goods or services are fulfilled, or canceled if the transacti
  name: Resolve Orders API
  slug: resolve-orders-api
- description: A payment represents a transaction where a customer pays towards their invoices. When a payment is made to Resolve, the customer's available credit balance is increased by the amount of the payment. P
  name: Resolve Payments API
  slug: resolve-payments-api
- description: Payout Transactions are the individual transactions like customer payments, Resolve advances, forwarded payments, etc. that are rolled into a Payout. Each Payout is the sum of one or more transactions
  name: Resolve Payout Transactions API
  slug: resolve-payout-transactions-api
- description: A Payout is a transfer of money between the Merchant and Resolve.
  name: Resolve Payouts API
  slug: resolve-payouts-api
- description: A shipment represents the fulfillment of goods or services for an invoice. Track shipments to monitor delivery status and fulfillment progress. Shipments can be fulfilled through various methods inclu
  name: Resolve Shipments API
  slug: resolve-shipments-api
- description: Webhooks allow you to receive real-time notifications about events in your Resolve account. When an event occurs, Resolve sends an HTTP POST request to your configured webhook endpoint with details ab
  name: Resolve Webhooks API
  slug: resolve-webhooks-api
artifact_total: 43
asyncapis:
- description: ''
  name: Resolve Webhooks
  slug: resolve-webhooks
collections:
- collection_type: postman
  name: Resolve API Reference Access Keys API
  slug: postman-resolve-access-keys-api
- collection_type: postman
  name: Resolve API Reference Access Keys Charges API
  slug: postman-resolve-charges-api
- collection_type: postman
  name: Resolve API Reference Access Keys Credit Notes API
  slug: postman-resolve-credit-notes-api
- collection_type: postman
  name: Resolve API Reference Access Keys Customers API
  slug: postman-resolve-customers-api
- collection_type: postman
  name: Resolve API Reference Access Keys Invoices API
  slug: postman-resolve-invoices-api
- collection_type: postman
  name: Resolve API Reference Access Keys Merchants API
  slug: postman-resolve-merchants-api
- collection_type: postman
  name: Resolve API Reference Access Keys Orders API
  slug: postman-resolve-orders-api
- collection_type: postman
  name: Resolve API Reference Access Keys Payments API
  slug: postman-resolve-payments-api
- collection_type: postman
  name: Resolve API Reference Access Keys Payout Transactions API
  slug: postman-resolve-payout-transactions-api
- collection_type: postman
  name: Resolve API Reference Access Keys Payouts API
  slug: postman-resolve-payouts-api
- collection_type: postman
  name: Resolve API Reference Access Keys Shipments API
  slug: postman-resolve-shipments-api
- collection_type: postman
  name: Resolve API Reference Access Keys Webhooks API
  slug: postman-resolve-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Resolve API Reference Access Keys API
  slug: open-resolve-access-keys-api
- collection_type: open
  name: Resolve API Reference Access Keys Charges API
  slug: open-resolve-charges-api
- collection_type: open
  name: Resolve API Reference Access Keys Credit Notes API
  slug: open-resolve-credit-notes-api
- collection_type: open
  name: Resolve API Reference Access Keys Customers API
  slug: open-resolve-customers-api
- collection_type: open
  name: Resolve API Reference Access Keys Invoices API
  slug: open-resolve-invoices-api
- collection_type: open
  name: Resolve API Reference Access Keys Merchants API
  slug: open-resolve-merchants-api
- collection_type: open
  name: Resolve API Reference Access Keys Orders API
  slug: open-resolve-orders-api
- collection_type: open
  name: Resolve API Reference Access Keys Payments API
  slug: open-resolve-payments-api
- collection_type: open
  name: Resolve API Reference Access Keys Payout Transactions API
  slug: open-resolve-payout-transactions-api
- collection_type: open
  name: Resolve API Reference Access Keys Payouts API
  slug: open-resolve-payouts-api
- collection_type: open
  name: Resolve API Reference Access Keys Shipments API
  slug: open-resolve-shipments-api
- collection_type: open
  name: Resolve API Reference Access Keys Webhooks API
  slug: open-resolve-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/resolve-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/resolve-merchant-api-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/resolve/overview
- group: company
  title: ''
  type: Website
  url: https://resolvepay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.resolvepay.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.resolvepay.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.resolvepay.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.resolvepay.com/guides
- group: operate
  title: ''
  type: Support
  url: https://help.resolvepay.com/
- group: company
  title: ''
  type: Blog
  url: https://resolvepay.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/resolvepay
- group: commercial
  title: ''
  type: Pricing
  url: https://resolvepay.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://resolvepay.com/signup/
- group: start
  title: ''
  type: Login
  url: https://app.resolvepay.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://resolvepay.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://resolvepay.com/privacy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.resolvepay.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.resolvepay.com
- group: operate
  title: ''
  type: Deprecation
  url: https://app.resolvepay.com/docs/api/v2
- group: agent
  title: ''
  type: MCPServer
  url: mcp/resolve-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/resolve-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/resolve-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/resolve-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/resolve-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/resolve-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/resolve-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/resolve-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/resolve-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/resolve-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/resolve-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/resolve-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/resolve-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/resolve-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/resolve-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Resolve is a B2B commerce and payments platform that lets businesses offer flexible net terms (typically NET 30-60) to their buyers without carrying the credit risk or waiting on cash. It combines automated credit underwriting, invoicing, agentic collections, and payment processing: sellers are paid upfront while customers pay on terms. Resolve exposes a Merchant API (V5) for direct integrations (customers, credit checks, invoices, orders, charges, shipments, payments, payouts), a Partners API for platform/marketplace sub-merchant management, a browser Checkout SDK, and an official MCP server with full Merchant-API parity for AI assistants. Backed by Insight Partners, QED Investors, and Y Combinator.'
image: https://resolvepay.com/favicon-32x32.png
layout: provider
mcp_servers:
- description: Official Resolve MCP server with full parity to the Merchant API. Manage a Resolve account (customers, credit checks, invoices, orders, charges, shipments, payments, payouts) from AI assistants like C
  name: Resolve MCP Server
  slug: resolve-mcp-server
modified: '2026-07-20'
name: Resolve
nav: Providers
network: true
overview: 'Resolve publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Access Keys API, Charges API, Credit Notes API, and 9 more. Tagged areas include Company, Payments, B2B, Net Terms, and Credit.


  The Resolve catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Resolve''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 1
  name: Resolve Rate Limits
  slug: resolve-rate-limits
scopes:
- name: Resolve Scopes
  scope_count: 2
  slug: resolve-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 22
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 64.9
    developer_ergonomics: 70.8
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 55.3
  previous_composite: 56.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/resolve/refs/heads/main/screenshots/resolve-2026-08-17T081532.png
security:
- kind: authentication
  name: Resolve Authentication
  slug: resolve-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Resolve Domain Security
  slug: resolve-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: resolve
tags:
- Company
- Payments
- B2B
- Net Terms
- Credit
- Invoicing
- Financing
- Embedded Finance
website: https://resolvepay.com/
---
