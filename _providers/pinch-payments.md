---
agent_readiness:
  band: agent-native
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
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Pinch Payments Agentic Access
  operation_count: 56
  slug: pinch-payments-agentic-access
  summary_line: 56 operations · 27 acting
api_count: 10
apis:
- description: The Connect API from Pinch Payments — 1 operation(s) for connect.
  name: Pinch Payments Connect API
  slug: pinch-payments-connect-api
- description: The Contacts API from Pinch Payments — 2 operation(s) for contacts.
  name: Pinch Payments Contacts API
  slug: pinch-payments-contacts-api
- description: The Events API from Pinch Payments — 2 operation(s) for events.
  name: Pinch Payments Events API
  slug: pinch-payments-events-api
- description: The Fees API from Pinch Payments — 2 operation(s) for fees.
  name: Pinch Payments Fees API
  slug: pinch-payments-fees-api
- description: The Health API from Pinch Payments — 1 operation(s) for health.
  name: Pinch Payments Health API
  slug: pinch-payments-health-api
- description: The Merchant Financial Data API from Pinch Payments — 2 operation(s) for merchant financial data.
  name: Pinch Payments Merchant Financial Data API
  slug: pinch-payments-merchant-financial-data-api
- description: The Merchants API from Pinch Payments — 3 operation(s) for merchants.
  name: Pinch Payments Merchants API
  slug: pinch-payments-merchants-api
- description: The Payers API from Pinch Payments — 4 operation(s) for payers.
  name: Pinch Payments Payers API
  slug: pinch-payments-payers-api
- description: The Payment Links API from Pinch Payments — 3 operation(s) for payment links.
  name: Pinch Payments Payment Links API
  slug: pinch-payments-payment-links-api
- description: The Payments API from Pinch Payments — 7 operation(s) for payments.
  name: Pinch Payments Payments API
  slug: pinch-payments-payments-api
- description: The Plans API from Pinch Payments — 3 operation(s) for plans.
  name: Pinch Payments Plans API
  slug: pinch-payments-plans-api
- description: The Refund API from Pinch Payments — 1 operation(s) for refund.
  name: Pinch Payments Refund API
  slug: pinch-payments-refund-api
- description: The Refunds API from Pinch Payments — 2 operation(s) for refunds.
  name: Pinch Payments Refunds API
  slug: pinch-payments-refunds-api
- description: The Subscriptions API from Pinch Payments — 2 operation(s) for subscriptions.
  name: Pinch Payments Subscriptions API
  slug: pinch-payments-subscriptions-api
- description: The Tokens API from Pinch Payments — 1 operation(s) for tokens.
  name: Pinch Payments Tokens API
  slug: pinch-payments-tokens-api
- description: The Transfers API from Pinch Payments — 3 operation(s) for transfers.
  name: Pinch Payments Transfers API
  slug: pinch-payments-transfers-api
- description: The Webhooks API from Pinch Payments — 2 operation(s) for webhooks.
  name: Pinch Payments Webhooks API
  slug: pinch-payments-webhooks-api
artifact_total: 43
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
overview: 'Pinch Payments publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Connect API, Contacts API, Events API, and 14 more. Tagged areas include Payments, Australia, Payment Gateway, Payment Processing, and Direct Debit.


  The Pinch Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pinch Payments'' developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, and 31 more developer resources.'
random_paper: 7
scopes:
- name: Pinch Payments Scopes
  scope_count: 1
  slug: pinch-payments-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 58.5
    developer_ergonomics: 62.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 46.1
  previous_composite: 53.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
