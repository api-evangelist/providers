---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 70.7
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 55
  human_in_the_loop: 0
  name: Method Financial Agentic Access
  operation_count: 128
  slug: method-financial-agentic-access
  summary_line: 128 operations · 55 acting
api_count: 42
apis:
- description: Attribute data for accounts
  name: Method Financial Account Attributes API
  slug: method-financial-account-attributes-api
- description: Balance data for accounts
  name: Method Financial Account Balances API
  slug: method-financial-account-balances-api
- description: Card brand information for accounts
  name: Method Financial Account Card Brands API
  slug: method-financial-account-card-brands-api
- description: Consent management for accounts
  name: Method Financial Account Consent API
  slug: method-financial-account-consent-api
- description: Payment instruments for accounts
  name: Method Financial Account Payment Instruments API
  slug: method-financial-account-payment-instruments-api
- description: Payoff data for accounts
  name: Method Financial Account Payoffs API
  slug: method-financial-account-payoffs-api
- description: Products associated with accounts
  name: Method Financial Account Products API
  slug: method-financial-account-products-api
- description: Sensitive data for accounts
  name: Method Financial Account Sensitive API
  slug: method-financial-account-sensitive-api
- description: Subscriptions for accounts
  name: Method Financial Account Subscriptions API
  slug: method-financial-account-subscriptions-api
- description: Transactions for accounts
  name: Method Financial Account Transactions API
  slug: method-financial-account-transactions-api
- description: Update records for accounts
  name: Method Financial Account Updates API
  slug: method-financial-account-updates-api
- description: Verification sessions for accounts
  name: Method Financial Account Verification Sessions API
  slug: method-financial-account-verification-sessions-api
- description: Financial accounts (ACH, liability, clearing, debit card)
  name: Method Financial Accounts API
  slug: method-financial-accounts-api
- description: Card product definitions
  name: Method Financial Card Products API
  slug: method-financial-card-products-api
- description: Client-side Element endpoints
  name: Method Financial Elements API
  slug: method-financial-elements-api
- description: Individuals, corporations, and receive-only entities
  name: Method Financial Entities API
  slug: method-financial-entities-api
- description: Attribute data for entities
  name: Method Financial Entity Attributes API
  slug: method-financial-entity-attributes-api
- description: Account connection sessions for entities
  name: Method Financial Entity Connects API
  slug: method-financial-entity-connects-api
- description: Consent management for entities
  name: Method Financial Entity Consent API
  slug: method-financial-entity-consent-api
- description: Credit score data for entities
  name: Method Financial Entity Credit Scores API
  slug: method-financial-entity-credit-scores-api
- description: Identity verification data for entities
  name: Method Financial Entity Identities API
  slug: method-financial-entity-identities-api
- description: Products associated with entities
  name: Method Financial Entity Products API
  slug: method-financial-entity-products-api
- description: Subscriptions for entities
  name: Method Financial Entity Subscriptions API
  slug: method-financial-entity-subscriptions-api
- description: Vehicle data for entities
  name: Method Financial Entity Vehicles API
  slug: method-financial-entity-vehicles-api
- description: Verification sessions for entities
  name: Method Financial Entity Verification Sessions API
  slug: method-financial-entity-verification-sessions-api
- description: Webhook event log
  name: Method Financial Events API
  slug: method-financial-events-api
- description: Request forwarding with sensitive data injection
  name: Method Financial Forwarding Requests API
  slug: method-financial-forwarding-requests-api
- description: Method-managed accounts
  name: Method Financial Managed Accounts API
  slug: method-financial-managed-accounts-api
- description: Merchant directory
  name: Method Financial Merchants API
  slug: method-financial-merchants-api
- description: Opal client-side session and token management
  name: Method Financial Opal API
  slug: method-financial-opal-api
- description: Reversals for payments
  name: Method Financial Payment Reversals API
  slug: method-financial-payment-reversals-api
- description: ACH and clearing payments
  name: Method Financial Payments API
  slug: method-financial-payments-api
- description: Health check endpoint
  name: Method Financial Ping API
  slug: method-financial-ping-api
- description: Public key discovery endpoints for Message-Level Encryption.
  name: Method Financial Public Keys API
  slug: method-financial-public-keys-api
- description: Downloadable reports
  name: Method Financial Reports API
  slug: method-financial-reports-api
- description: Secure secret storage
  name: Method Financial Secrets API
  slug: method-financial-secrets-api
- description: Sandbox account simulation
  name: Method Financial Simulate Accounts API
  slug: method-financial-simulate-accounts-api
- description: Sandbox entity simulation
  name: Method Financial Simulate Entities API
  slug: method-financial-simulate-entities-api
- description: Sandbox event simulation
  name: Method Financial Simulate Events API
  slug: method-financial-simulate-events-api
- description: Sandbox payment simulation
  name: Method Financial Simulate Payments API
  slug: method-financial-simulate-payments-api
- description: Team and API key management
  name: Method Financial Teams API
  slug: method-financial-teams-api
- description: Webhook subscriptions
  name: Method Financial Webhooks API
  slug: method-financial-webhooks-api
artifact_total: 50
asyncapis:
- description: ''
  name: Method Financial Webhooks
  slug: method-financial-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/method-financial-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/method-financial-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://methodfi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.methodfi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.methodfi.com/guides/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.methodfi.com/reference/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.methodfi.com/guides/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.methodfi.com
- group: operate
  title: ''
  type: Support
  url: https://methodfi.com/company/contact
- group: company
  title: ''
  type: Blog
  url: https://methodfi.com/resources/perspectives
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MethodFi
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/methodfi/method-api/collection/8d5j00b/method-api-v2
- group: commercial
  title: ''
  type: TermsOfService
  url: https://methodfi.com/legal/terms-of-service-for-developers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://methodfi.com/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://security.methodfi.com/
- group: auth
  title: ''
  type: Security
  url: https://security.methodfi.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.methodfi.com/changelog
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/method-financial-openapi-original.yml
- group: build
  title: ''
  type: Packages
  url: packages/method-financial-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/method-financial-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/method-financial-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/method-financial-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/method-financial-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/method-financial-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/method-financial-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/method-financial-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/method-financial-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/method-financial-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.methodfi.com/reference/versioning
- group: auth
  title: ''
  type: Authentication
  url: authentication/method-financial-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/method-financial-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/method-financial-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/method-financial-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/method-financial-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/method-financial-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/method-financial-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/method-financial-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/method-financial-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/method-financial-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/method-financial-rate-limits.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/method-financial-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/method-financial-decline-codes.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/method-financial-method-api-overlay.yaml
created: '2026-08-04'
description: Method Financial is a US financial connectivity platform that gives developers a single REST API for consumer liability data and debt payments. Instead of asking a consumer to hand over bank credentials, Method verifies the consumer's identity and runs a permissioned soft credit pull to automatically discover every liability they hold — credit cards, auto loans, mortgages, student loans and personal loans — across 15,000+ financial institutions. It then normalizes balances, due dates, interest rates, payment amounts and limits into one data model, keeps them fresh through on-demand Updates and Subscriptions, and moves money directly to those creditors through its Payments API. The platform also ships embeddable Opal/Elements UI components, credit scores, financial attributes, card-brand enrichment, vehicle enrichment and a webhook event stream, and is used for lending origination, debt consolidation, portfolio intelligence, commerce card-linking and personal financial management.
image: https://framerusercontent.com/images/8VlzHm7NUhxHyDz7Bej54eBKKAc.png
layout: provider
mcp_servers:
- description: ''
  name: method-financial-mcp.yml
  slug: method-financial-mcpyml
modified: '2026-08-04'
name: Method Financial
nav: Providers
network: true
overview: 'Method Financial publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Account Attributes API, Account Balances API, Account Card Brands API, and 39 more. Tagged areas include Company, Financial Services, Fintech, Lending, and Payments.


  The Method Financial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Method Financial''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, changelog, and 37 more developer resources.'
random_paper: 111
rate_limits:
- limit_count: 6
  name: Method Financial Rate Limits
  slug: method-financial-rate-limits
score:
  band: strong
  composite: 65.1
  delta: -0.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 71.2
    developer_ergonomics: 84.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 78.9
  previous_composite: 65.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 55.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/method-financial/refs/heads/main/screenshots/method-financial-2026-08-07T172703.png
security:
- kind: authentication
  name: Method Financial Authentication
  slug: method-financial-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Method Financial Domain Security
  slug: method-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Method Financial Vulnerability Disclosure
  slug: method-financial-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Method Financial Trust Center
  slug: method-financial-trust-center
  summary_line: SOC 2 Type 2, PCI DSS v4.0.1
slug: method-financial
tags:
- Company
- Financial Services
- Fintech
- Lending
- Payments
- Liability Data
- Credit
- Debt
- Open Banking
- Identity Verification
- Personal Finance
website: https://methodfi.com/
---
