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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 136
  human_in_the_loop: 4
  name: Modulr Agentic Access
  operation_count: 207
  slug: modulr-agentic-access
  summary_line: 207 operations · 136 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: Operations on Access Group
  name: Modulr Access Group API
  slug: modulr-access-group-api
- description: Operations on Accounts
  name: Modulr Accounts API
  slug: modulr-accounts-api
- description: Asynchronous card task operations
  name: Modulr Async API
  slug: modulr-async-api
- description: Operations on Beneficiaries
  name: Modulr Beneficiaries API
  slug: modulr-beneficiaries-api
- description: Cards Simulator API
  name: Modulr Card Simulator API
  slug: modulr-card-simulator-api
- description: Cards API
  name: Modulr Cards API
  slug: modulr-cards-api
- description: The Cards Bulk Operations API from Modulr — 3 operation(s) for cards bulk operations.
  name: Modulr Cards Bulk Operations API
  slug: modulr-cards-bulk-operations-api
- description: The Channel Manager Card API from Modulr — 9 operation(s) for channel manager card.
  name: Modulr Channel Manager Card API
  slug: modulr-channel-manager-card-api
- description: The Channel Manager Webhook Notifications API from Modulr — 3 operation(s) for channel manager webhook notifications.
  name: Modulr Channel Manager Webhook Notifications API
  slug: modulr-channel-manager-webhook-notifications-api
- description: Account Name Checks
  name: Modulr Confirmation of Payee API
  slug: modulr-confirmation-of-payee-api
- description: Operations on Customers
  name: Modulr Customers API
  slug: modulr-customers-api
- description: The Direct Debit Outbound Mandate Operations API from Modulr — 3 operation(s) for direct debit outbound mandate operations.
  name: Modulr Direct Debit Outbound Mandate Operations API
  slug: modulr-direct-debit-outbound-mandate-operations-api
- description: Direct Debit operations
  name: Modulr Direct Debits API
  slug: modulr-direct-debits-api
- description: Operations on Documents
  name: Modulr Document API
  slug: modulr-document-api
- description: Upload payment files
  name: Modulr File Upload API
  slug: modulr-file-upload-api
- description: Inbound payments
  name: Modulr Inbound Payments API
  slug: modulr-inbound-payments-api
- description: The Integration Notification API from Modulr — 3 operation(s) for integration notification.
  name: Modulr Integration Notification API
  slug: modulr-integration-notification-api
- description: Operations on Notifications
  name: Modulr Notification API
  slug: modulr-notification-api
- description: The Payment Initiations API from Modulr — 5 operation(s) for payment initiations.
  name: Modulr Payment Initiations API
  slug: modulr-payment-initiations-api
- description: Operations on Payments
  name: Modulr Payments API
  slug: modulr-payments-api
- description: Restricted access API calls
  name: Modulr Restricted API
  slug: modulr-restricted-api
- description: Rules
  name: Modulr Rules API
  slug: modulr-rules-api
- description: Share secure card details operations
  name: Modulr Share secure card details API
  slug: modulr-share-secure-card-details-api
- description: Operations on Transactions
  name: Modulr Transactions API
  slug: modulr-transactions-api
- description: The Variable Recurring Payments API from Modulr — 5 operation(s) for variable recurring payments.
  name: Modulr Variable Recurring Payments API
  slug: modulr-variable-recurring-payments-api
- description: The Verification of Payee API from Modulr — 1 operation(s) for verification of payee.
  name: Modulr Verification of Payee API
  slug: modulr-verification-of-payee-api
artifact_total: 33
asyncapis:
- description: ''
  name: Modulr Webhooks
  slug: modulr-webhooks
collections:
- collection_type: open
  name: Modulr API
  slug: open-modulr-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/modulr-capability-edges.yml
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
  name: Modulr MCP Server
  slug: modulr-mcp-server
modified: '2026-07-24'
name: Modulr
nav: Providers
network: true
overview: 'Modulr publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Access Group API, Accounts API, Async API, and 23 more. Tagged areas include Payments, United Kingdom, Banking as a Service, Embedded Finance, and Payment Processing.


  The Modulr catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Modulr''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, pricing, engineering blog, and 30 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 2
  name: Modulr Rate Limits
  slug: modulr-rate-limits
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 23
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 63.1
    developer_ergonomics: 48.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 55.3
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 51.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/modulr/refs/heads/main/screenshots/modulr-2026-08-07T184038.png
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
- Banking as a Service
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
