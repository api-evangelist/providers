---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 136
  human_in_the_loop: 4
  name: Modulr Agentic Access
  operation_count: 207
  slug: modulr-agentic-access
  summary_line: 207 operations · 136 acting · 4 human-in-the-loop
api_count: 9
apis:
- description: Create, retrieve, edit, block/unblock and close programmable eMoney accounts, manage access groups and account rules, and read balances — the core account fabric of the Modulr platform.
  name: Modulr Accounts API
  slug: modulr-accounts-api
- description: Initiate outbound, inbound, bulk, batch and future-dated payments over UK Faster Payments and Bacs, plus international SWIFT payments, with transaction retrieval and reconciliation.
  name: Modulr Payments API
  slug: modulr-payments-api
- description: Issue and manage virtual and physical cards, including tokenization, PIN management, card controls, transactions, secure card-detail retrieval and bulk card operations.
  name: Modulr Cards API
  slug: modulr-cards-api
- description: Set up and manage UK Bacs Direct Debit mandates and collections, outbound mandate operations and indemnity claims for recurring collection use cases.
  name: Modulr Direct Debits API
  slug: modulr-direct-debits-api
- description: Create and verify customers, run KYC/KYB onboarding, manage associates and tax identifiers, and upload supporting documents for compliance.
  name: Modulr Customers API
  slug: modulr-customers-api
- description: Confirmation of Payee (CoP) and Verification of Payee (VoP) account name checking to reduce misdirected-payment and APP fraud risk before payments are sent.
  name: Modulr Payee Verification API
  slug: modulr-verification-api
- description: Open Banking Payment Initiation Services (PIS) — initiate immediate account-to-account payments and standing orders from a payer's bank account through connected ASPSPs.
  name: Modulr Payment Initiation API
  slug: modulr-payment-initiation-api
- description: Consumer and commercial Variable Recurring Payments (VRP) — manage consents and execute recurring account-to-account payments under Open Banking.
  name: Modulr Variable Recurring Payments API
  slug: modulr-variable-recurring-payments-api
- description: Configure partner- and customer-level webhook subscriptions for account, payment, customer, compliance and Direct Debit events, and retrieve failed webhook deliveries.
  name: Modulr Notifications API
  slug: modulr-notifications-api
artifact_total: 15
asyncapis:
- description: ''
  name: Modulr Webhooks
  slug: modulr-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/modulr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modulr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/modulr-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.modulrfinance.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://modulr.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://modulr.readme.io/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://modulr.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://modulr.readme.io/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://modulr.readme.io/docs/authentication
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/modulr-api.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Modulr-finance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/modulr-finance
- group: operate
  title: ''
  type: StatusPage
  url: https://status.modulrfinance.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://knowledge.modulrfinance.com/knowledge-hub
- group: operate
  title: ''
  type: ChangeLog
  url: https://modulr.readme.io/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.modulrfinance.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.modulrfinance.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.modulrfinance.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/modulr-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/modulr-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/modulr-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/modulr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/modulr-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/modulr-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/modulr-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/modulr-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/modulr-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/modulr-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/modulr-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/modulr-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/modulr-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/modulr-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/modulr-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/modulr-api-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/modulr-data-model.yml
created: '2026-07-24'
description: 'Modulr is a United Kingdom-based embedded payments and Banking-as-a-Service platform that lets businesses and software platforms open programmable eMoney accounts and move money automatically via a single API. As a licensed e-money institution and direct participant in the UK Faster Payments and Bacs schemes (with SEPA reach in the EU through its Dutch entity), Modulr provides the underlying accounts, payment rails, card issuing, and Open Banking connectivity that fintechs, payroll providers, lenders, marketplaces, and travel and accounting platforms embed into their own products. Its REST API covers account creation, inbound and outbound payments (including bulk, batch, future-dated and SWIFT international), virtual and physical card issuing, Bacs Direct Debit collection, KYC/KYB customer onboarding, Confirmation of Payee and Verification of Payee, Payment Initiation Services and Variable Recurring Payments under Open Banking, plus a rich webhook notification layer. Modulr
  is API-native: it publishes a genuine public developer portal on ReadMe with reference docs and a downloadable OpenAPI 3.1 definition, and offers a self-serve sandbox.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: modulr-mcp.yml
  slug: modulr-mcpyml
modified: '2026-07-24'
name: Modulr
nav: Providers
network: true
overview: 'Modulr publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Payments API, Cards API, and 6 more. Tagged areas include Payments, United Kingdom, Banking-as-a-Service, Embedded Finance, and Payment Processing.


  The Modulr catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Modulr''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, pricing, engineering blog, and 29 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 2
  name: Modulr Rate Limits
  slug: modulr-rate-limits
score:
  band: developing
  composite: 47.7
  delta: -5.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 65.8
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Modulr Authentication
  slug: modulr-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Modulr Domain Security
  slug: modulr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: modulr
tags:
- Payments
- United Kingdom
- Banking-as-a-Service
- Embedded Finance
- Payment Processing
- Account-to-Account
- Open Banking
- Faster Payments
- Card Issuing
- Direct Debit
- Confirmation of Payee
- Variable Recurring Payments
website: https://www.modulrfinance.com/
---
