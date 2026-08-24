---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Pinch Payments Agentic Access
  operation_count: 56
  slug: pinch-payments-agentic-access
  summary_line: 56 operations · 27 acting
api_count: 10
apis:
- description: Core Pinch REST API covering scheduled and realtime payments, plans and subscriptions, refunds, fees, events, and health — 14 paths / 19 operations. Assembled verbatim from Pinch's published per-endpo
  name: Pinch Core API
  slug: pinch-payments-core
- description: Payments product surface — create/update scheduled payments, take realtime card payments, retrieve and list payments, check payment nonces, and delete payments; 7 paths / 8 operations.
  name: Pinch Payments API
  slug: pinch-payments-payments
- description: Manage payer records and their payment sources (bank account or credit card) plus client-side tokenisation — create/update, retrieve, list, and delete payers and payment sources; 4 paths / 6 operation
  name: Pinch Payers API
  slug: pinch-payments-payers
- description: Generate hosted payment pages (payment links) and share them via email, SMS, or chat with no frontend work — create, retrieve, list by payer, and delete payment links; 3 paths / 5 operations.
  name: Pinch Payment Links API
  slug: pinch-payments-payment-links
- description: Payfac-as-a-Service / Managed Merchants — create sub-merchant accounts under your own credentials, update merchant details, list managed merchants, and upload compliance documents; 3 paths / 4 operati
  name: Pinch Merchants API
  slug: pinch-payments-merchants
- description: Configure webhooks to receive real-time notifications about Pinch events (payer created, payment success/failure, bank results, subscription lifecycle) — create/update, list, retrieve, and delete webh
  name: Pinch Webhooks API
  slug: pinch-payments-webhooks
- description: Manage contact records for the authenticated merchant — create/update, retrieve a single contact, list contacts (paginated), and delete contacts; 2 paths / 4 operations.
  name: Pinch Contacts API
  slug: pinch-payments-contacts
- description: Reconcile settlements — list all transfers of settled funds to your bank account, retrieve a transfer, and list its line items back to the underlying payments; 3 paths / 3 operations.
  name: Pinch Transfers API
  slug: pinch-payments-transfers
- description: Retrieve the current merchant financial data record and create/update merchant financial data used in compliance and onboarding; 2 paths / 2 operations.
  name: Pinch Merchant Financial Data API
  slug: pinch-payments-merchant-financial-data
- description: OAuth2 client-credentials token endpoint — POST /connect/token with HTTP Basic (merchant ID + secret key) and scope api1 to obtain a short-lived Bearer JWT used against the Pinch API; served from auth
  name: Pinch Authentication API
  slug: pinch-payments-authentication
artifact_total: 36
asyncapis:
- description: ''
  name: Pinch Payments Webhooks
  slug: pinch-payments-webhooks
collections:
- collection_type: postman
  name: authentication-api
  slug: postman-pinch-payments-authentication
- collection_type: postman
  name: pinch-api-contacts
  slug: postman-pinch-payments-contacts
- collection_type: postman
  name: pinch-api
  slug: postman-pinch-payments-core
- collection_type: postman
  name: pinch-api-merchant-financial-data
  slug: postman-pinch-payments-merchant-financial-data
- collection_type: postman
  name: pinch-api-merchants
  slug: postman-pinch-payments-merchants
- collection_type: postman
  name: pinch-api-payers
  slug: postman-pinch-payments-payers
- collection_type: postman
  name: pinch-api-payment-links
  slug: postman-pinch-payments-payment-links
- collection_type: postman
  name: pinch-api-payments
  slug: postman-pinch-payments-payments
- collection_type: postman
  name: pinch-api-transfers
  slug: postman-pinch-payments-transfers
- collection_type: postman
  name: pinch-api-webhooks
  slug: postman-pinch-payments-webhooks
- collection_type: open
  name: authentication-api
  slug: open-pinch-payments-authentication
- collection_type: open
  name: pinch-api-contacts
  slug: open-pinch-payments-contacts
- collection_type: open
  name: pinch-api
  slug: open-pinch-payments-core
- collection_type: open
  name: pinch-api-merchant-financial-data
  slug: open-pinch-payments-merchant-financial-data
- collection_type: open
  name: pinch-api-merchants
  slug: open-pinch-payments-merchants
- collection_type: open
  name: pinch-api-payers
  slug: open-pinch-payments-payers
- collection_type: open
  name: pinch-api-payment-links
  slug: open-pinch-payments-payment-links
- collection_type: open
  name: pinch-api-payments
  slug: open-pinch-payments-payments
- collection_type: open
  name: pinch-api-transfers
  slug: open-pinch-payments-transfers
- collection_type: open
  name: pinch-api-webhooks
  slug: open-pinch-payments-webhooks
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/pinch-payments/overview
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pinch-payments-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pinch-payments-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pinch-payments-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pinch-payments-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://getpinch.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getpinch.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getpinch.com.au/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getpinch.com.au/reference/things-to-know
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getpinch.com.au/docs/get-started-with-the-pinch-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PinchPayments
- group: build
  title: ''
  type: Postman
  url: https://github.com/PinchPayments/postman-pinch-api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getpinch.com.au/
- group: commercial
  title: ''
  type: Pricing
  url: https://getpinch.com.au/pricing
- group: company
  title: ''
  type: Blog
  url: https://getpinch.com.au/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpdesk.getpinch.com.au/
- group: start
  title: ''
  type: SignUp
  url: https://app.getpinch.com.au/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getpinch.com.au/Legal/Terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getpinch.com.au/Legal/Privacy/
- group: build
  title: ''
  type: Packages
  url: packages/pinch-payments-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pinch-payments-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pinch-payments-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/pinch-payments-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pinch-payments-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/pinch-payments-core-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/pinch-payments-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pinch-payments-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/pinch-payments-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pinch-payments-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.getpinch.com.au/docs/versioning
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pinch-payments-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pinch-payments-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/pinch-payments-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pinch-payments-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/pinch-payments-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pinch-payments-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/pinch-payments-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-24'
description: 'Pinch Payments is an Australian, Brisbane-based payment orchestration and payment-facilitator platform that automates invoice collection and receivables for service businesses, bookkeepers, and software platforms across Australia and New Zealand. Marketing itself as "Aussie-Made Payments Infrastructure," Pinch lets merchants accept direct debit (bank account) and card payments (Visa, Mastercard, American Express), build payment plans and subscriptions, tokenise payment sources client-side with its CaptureJS library, and reconcile settlements back into Xero, QuickBooks, and MYOB. Its Glassbox / Managed Merchants offering is a Payfac-as-a-Service seam with KYC, compliance, and sub-merchant onboarding for platforms acting as aggregators or marketplaces. Pinch is genuinely API-first: it ships a fully documented REST API (JSON, OAuth2 client-credentials auth), a ReadMe-hosted developer portal with a live API explorer, per-product OpenAPI 3.1 definitions, a published Postman collection,
  an official .NET SDK, Zapier/n8n/viaSocket no-code connectors, webhooks for real-time events, and an llms.txt + docs MCP server for AI-assisted integration.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Pinch API Docs MCP
  slug: pinch-api-docs-mcp
modified: '2026-07-24'
name: Pinch Payments
nav: Providers
network: true
overview: 'Pinch Payments publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Pinch Core API, Pinch Payers API, and 8 more. Tagged areas include Payments, Australia, Payment Gateway, Payment Processing, and Direct Debit.


  The Pinch Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pinch Payments'' developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, and 31 more developer resources.'
random_paper: 7
scopes:
- name: Pinch Payments Scopes
  scope_count: 1
  slug: pinch-payments-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: strong
  composite: 55.4
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 57.9
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 46.1
  previous_composite: 55.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pinch-payments/refs/heads/main/screenshots/pinch-payments-2026-08-17T081230.png
security:
- kind: authentication
  name: Pinch Payments Authentication
  slug: pinch-payments-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Pinch Payments Domain Security
  slug: pinch-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pinch-payments
tags:
- Payments
- Australia
- Payment Gateway
- Payment Processing
- Direct Debit
- Card Payments
- Subscription
- Billing
- Payment Facilitator
- Account-to-Account
- New Zealand
website: https://getpinch.com.au/
---
