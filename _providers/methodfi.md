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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 55
  human_in_the_loop: 0
  name: Methodfi Agentic Access
  operation_count: 128
  slug: methodfi-agentic-access
  summary_line: 128 operations · 55 acting
api_count: 2
apis:
- description: Attribute data for accounts
  name: MethodFi Account Attributes API
  slug: methodfi-account-attributes-api
- description: Balance data for accounts
  name: MethodFi Account Balances API
  slug: methodfi-account-balances-api
- description: Card brand information for accounts
  name: MethodFi Account Card Brands API
  slug: methodfi-account-card-brands-api
- description: Consent management for accounts
  name: MethodFi Account Consent API
  slug: methodfi-account-consent-api
- description: Payment instruments for accounts
  name: MethodFi Account Payment Instruments API
  slug: methodfi-account-payment-instruments-api
- description: Payoff data for accounts
  name: MethodFi Account Payoffs API
  slug: methodfi-account-payoffs-api
- description: Products associated with accounts
  name: MethodFi Account Products API
  slug: methodfi-account-products-api
- description: Sensitive data for accounts
  name: MethodFi Account Sensitive API
  slug: methodfi-account-sensitive-api
- description: Subscriptions for accounts
  name: MethodFi Account Subscriptions API
  slug: methodfi-account-subscriptions-api
- description: Transactions for accounts
  name: MethodFi Account Transactions API
  slug: methodfi-account-transactions-api
- description: Update records for accounts
  name: MethodFi Account Updates API
  slug: methodfi-account-updates-api
- description: Verification sessions for accounts
  name: MethodFi Account Verification Sessions API
  slug: methodfi-account-verification-sessions-api
- description: Financial accounts (ACH, liability, clearing, debit card)
  name: MethodFi Accounts API
  slug: methodfi-accounts-api
- description: Card product definitions
  name: MethodFi Card Products API
  slug: methodfi-card-products-api
- description: Client-side Element endpoints
  name: MethodFi Elements API
  slug: methodfi-elements-api
- description: Individuals, corporations, and receive-only entities
  name: MethodFi Entities API
  slug: methodfi-entities-api
- description: Attribute data for entities
  name: MethodFi Entity Attributes API
  slug: methodfi-entity-attributes-api
- description: Account connection sessions for entities
  name: MethodFi Entity Connects API
  slug: methodfi-entity-connects-api
- description: Consent management for entities
  name: MethodFi Entity Consent API
  slug: methodfi-entity-consent-api
- description: Credit score data for entities
  name: MethodFi Entity Credit Scores API
  slug: methodfi-entity-credit-scores-api
- description: Identity verification data for entities
  name: MethodFi Entity Identities API
  slug: methodfi-entity-identities-api
- description: Products associated with entities
  name: MethodFi Entity Products API
  slug: methodfi-entity-products-api
- description: Subscriptions for entities
  name: MethodFi Entity Subscriptions API
  slug: methodfi-entity-subscriptions-api
- description: Vehicle data for entities
  name: MethodFi Entity Vehicles API
  slug: methodfi-entity-vehicles-api
- description: Verification sessions for entities
  name: MethodFi Entity Verification Sessions API
  slug: methodfi-entity-verification-sessions-api
- description: Webhook event log
  name: MethodFi Events API
  slug: methodfi-events-api
- description: Request forwarding with sensitive data injection
  name: MethodFi Forwarding Requests API
  slug: methodfi-forwarding-requests-api
- description: Method-managed accounts
  name: MethodFi Managed Accounts API
  slug: methodfi-managed-accounts-api
- description: Merchant directory
  name: MethodFi Merchants API
  slug: methodfi-merchants-api
- description: Opal client-side session and token management
  name: MethodFi Opal API
  slug: methodfi-opal-api
- description: Reversals for payments
  name: MethodFi Payment Reversals API
  slug: methodfi-payment-reversals-api
- description: ACH and clearing payments
  name: MethodFi Payments API
  slug: methodfi-payments-api
- description: Health check endpoint
  name: MethodFi Ping API
  slug: methodfi-ping-api
- description: Public key discovery endpoints for Message-Level Encryption.
  name: MethodFi Public Keys API
  slug: methodfi-public-keys-api
- description: Downloadable reports
  name: MethodFi Reports API
  slug: methodfi-reports-api
- description: Secure secret storage
  name: MethodFi Secrets API
  slug: methodfi-secrets-api
- description: Sandbox account simulation
  name: MethodFi Simulate Accounts API
  slug: methodfi-simulate-accounts-api
- description: Sandbox entity simulation
  name: MethodFi Simulate Entities API
  slug: methodfi-simulate-entities-api
- description: Sandbox event simulation
  name: MethodFi Simulate Events API
  slug: methodfi-simulate-events-api
- description: Sandbox payment simulation
  name: MethodFi Simulate Payments API
  slug: methodfi-simulate-payments-api
- description: Team and API key management
  name: MethodFi Teams API
  slug: methodfi-teams-api
- description: Webhook subscriptions
  name: MethodFi Webhooks API
  slug: methodfi-webhooks-api
- description: Liability discovery across Method's institution network.
  name: MethodFi Connect API
  slug: methodfi-connect-api
- description: Transaction history for an account.
  name: MethodFi Transactions API
  slug: methodfi-transactions-api
artifact_total: 141
asyncapis:
- description: ''
  name: Methodfi Webhooks
  slug: methodfi-webhooks
collections:
- collection_type: postman
  name: Method Account Attributes API
  slug: postman-methodfi-account-attributes-api
- collection_type: postman
  name: Method Account Attributes Account Balances API
  slug: postman-methodfi-account-balances-api
- collection_type: postman
  name: Method Account Attributes Account Card Brands API
  slug: postman-methodfi-account-card-brands-api
- collection_type: postman
  name: Method Account Attributes Account Consent API
  slug: postman-methodfi-account-consent-api
- collection_type: postman
  name: Method Account Attributes Account Payment Instruments API
  slug: postman-methodfi-account-payment-instruments-api
- collection_type: postman
  name: Method Account Attributes Account Payoffs API
  slug: postman-methodfi-account-payoffs-api
- collection_type: postman
  name: Method Account Attributes Account Products API
  slug: postman-methodfi-account-products-api
- collection_type: postman
  name: Method Account Attributes Account Sensitive API
  slug: postman-methodfi-account-sensitive-api
- collection_type: postman
  name: Method Account Attributes Account Subscriptions API
  slug: postman-methodfi-account-subscriptions-api
- collection_type: postman
  name: Method Account Attributes Account Transactions API
  slug: postman-methodfi-account-transactions-api
- collection_type: postman
  name: Method Account Attributes Account Updates API
  slug: postman-methodfi-account-updates-api
- collection_type: postman
  name: Method Account Attributes Account Verification Sessions API
  slug: postman-methodfi-account-verification-sessions-api
- collection_type: postman
  name: Method Account Attributes Accounts API
  slug: postman-methodfi-accounts-api
- collection_type: postman
  name: Method Account Attributes Card Products API
  slug: postman-methodfi-card-products-api
- collection_type: postman
  name: Method Account Attributes Elements API
  slug: postman-methodfi-elements-api
- collection_type: postman
  name: Method Account Attributes Entities API
  slug: postman-methodfi-entities-api
- collection_type: postman
  name: Method Account Attributes Entity Attributes API
  slug: postman-methodfi-entity-attributes-api
- collection_type: postman
  name: Method Account Attributes Entity Connects API
  slug: postman-methodfi-entity-connects-api
- collection_type: postman
  name: Method Account Attributes Entity Consent API
  slug: postman-methodfi-entity-consent-api
- collection_type: postman
  name: Method Account Attributes Entity Credit Scores API
  slug: postman-methodfi-entity-credit-scores-api
- collection_type: postman
  name: Method Account Attributes Entity Identities API
  slug: postman-methodfi-entity-identities-api
- collection_type: postman
  name: Method Account Attributes Entity Products API
  slug: postman-methodfi-entity-products-api
- collection_type: postman
  name: Method Account Attributes Entity Subscriptions API
  slug: postman-methodfi-entity-subscriptions-api
- collection_type: postman
  name: Method Account Attributes Entity Vehicles API
  slug: postman-methodfi-entity-vehicles-api
- collection_type: postman
  name: Method Account Attributes Entity Verification Sessions API
  slug: postman-methodfi-entity-verification-sessions-api
- collection_type: postman
  name: Method Account Attributes Events API
  slug: postman-methodfi-events-api
- collection_type: postman
  name: Method Account Attributes Forwarding Requests API
  slug: postman-methodfi-forwarding-requests-api
- collection_type: postman
  name: Method Account Attributes Managed Accounts API
  slug: postman-methodfi-managed-accounts-api
- collection_type: postman
  name: Method Account Attributes Merchants API
  slug: postman-methodfi-merchants-api
- collection_type: postman
  name: Method Account Attributes Opal API
  slug: postman-methodfi-opal-api
- collection_type: postman
  name: Method Account Attributes Payment Reversals API
  slug: postman-methodfi-payment-reversals-api
- collection_type: postman
  name: Method Account Attributes Payments API
  slug: postman-methodfi-payments-api
- collection_type: postman
  name: Method Account Attributes Ping API
  slug: postman-methodfi-ping-api
- collection_type: postman
  name: Method Account Attributes Public Keys API
  slug: postman-methodfi-public-keys-api
- collection_type: postman
  name: Method Account Attributes Reports API
  slug: postman-methodfi-reports-api
- collection_type: postman
  name: Method Account Attributes Secrets API
  slug: postman-methodfi-secrets-api
- collection_type: postman
  name: Method Account Attributes Simulate Accounts API
  slug: postman-methodfi-simulate-accounts-api
- collection_type: postman
  name: Method Account Attributes Simulate Entities API
  slug: postman-methodfi-simulate-entities-api
- collection_type: postman
  name: Method Account Attributes Simulate Events API
  slug: postman-methodfi-simulate-events-api
- collection_type: postman
  name: Method Account Attributes Simulate Payments API
  slug: postman-methodfi-simulate-payments-api
- collection_type: postman
  name: Method Account Attributes Teams API
  slug: postman-methodfi-teams-api
- collection_type: postman
  name: Method Account Attributes Webhooks API
  slug: postman-methodfi-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Method Financial API
  slug: open-method-fi
- collection_type: open
  name: Method Account Attributes API
  slug: open-methodfi-account-attributes-api
- collection_type: open
  name: Method Account Attributes Account Balances API
  slug: open-methodfi-account-balances-api
- collection_type: open
  name: Method Account Attributes Account Card Brands API
  slug: open-methodfi-account-card-brands-api
- collection_type: open
  name: Method Account Attributes Account Consent API
  slug: open-methodfi-account-consent-api
- collection_type: open
  name: Method Account Attributes Account Payment Instruments API
  slug: open-methodfi-account-payment-instruments-api
- collection_type: open
  name: Method Account Attributes Account Payoffs API
  slug: open-methodfi-account-payoffs-api
- collection_type: open
  name: Method Account Attributes Account Products API
  slug: open-methodfi-account-products-api
- collection_type: open
  name: Method Account Attributes Account Sensitive API
  slug: open-methodfi-account-sensitive-api
- collection_type: open
  name: Method Account Attributes Account Subscriptions API
  slug: open-methodfi-account-subscriptions-api
- collection_type: open
  name: Method Account Attributes Account Transactions API
  slug: open-methodfi-account-transactions-api
- collection_type: open
  name: Method Account Attributes Account Updates API
  slug: open-methodfi-account-updates-api
- collection_type: open
  name: Method Account Attributes Account Verification Sessions API
  slug: open-methodfi-account-verification-sessions-api
- collection_type: open
  name: Method Account Attributes Accounts API
  slug: open-methodfi-accounts-api
- collection_type: open
  name: Method Account Attributes Card Products API
  slug: open-methodfi-card-products-api
- collection_type: open
  name: Method Financial Accounts Connect API
  slug: open-methodfi-connect-api
- collection_type: open
  name: Method Account Attributes Elements API
  slug: open-methodfi-elements-api
- collection_type: open
  name: Method Account Attributes Entities API
  slug: open-methodfi-entities-api
- collection_type: open
  name: Method Account Attributes Entity Attributes API
  slug: open-methodfi-entity-attributes-api
- collection_type: open
  name: Method Account Attributes Entity Connects API
  slug: open-methodfi-entity-connects-api
- collection_type: open
  name: Method Account Attributes Entity Consent API
  slug: open-methodfi-entity-consent-api
- collection_type: open
  name: Method Account Attributes Entity Credit Scores API
  slug: open-methodfi-entity-credit-scores-api
- collection_type: open
  name: Method Account Attributes Entity Identities API
  slug: open-methodfi-entity-identities-api
- collection_type: open
  name: Method Account Attributes Entity Products API
  slug: open-methodfi-entity-products-api
- collection_type: open
  name: Method Account Attributes Entity Subscriptions API
  slug: open-methodfi-entity-subscriptions-api
- collection_type: open
  name: Method Account Attributes Entity Vehicles API
  slug: open-methodfi-entity-vehicles-api
- collection_type: open
  name: Method Account Attributes Entity Verification Sessions API
  slug: open-methodfi-entity-verification-sessions-api
- collection_type: open
  name: Method Account Attributes Events API
  slug: open-methodfi-events-api
- collection_type: open
  name: Method Account Attributes Forwarding Requests API
  slug: open-methodfi-forwarding-requests-api
- collection_type: open
  name: Method Account Attributes Managed Accounts API
  slug: open-methodfi-managed-accounts-api
- collection_type: open
  name: Method Account Attributes Merchants API
  slug: open-methodfi-merchants-api
- collection_type: open
  name: Method Account Attributes Opal API
  slug: open-methodfi-opal-api
- collection_type: open
  name: Method Account Attributes Payment Reversals API
  slug: open-methodfi-payment-reversals-api
- collection_type: open
  name: Method Account Attributes Payments API
  slug: open-methodfi-payments-api
- collection_type: open
  name: Method Account Attributes Ping API
  slug: open-methodfi-ping-api
- collection_type: open
  name: Method Account Attributes Public Keys API
  slug: open-methodfi-public-keys-api
- collection_type: open
  name: Method Account Attributes Reports API
  slug: open-methodfi-reports-api
- collection_type: open
  name: Method Account Attributes Secrets API
  slug: open-methodfi-secrets-api
- collection_type: open
  name: Method Account Attributes Simulate Accounts API
  slug: open-methodfi-simulate-accounts-api
- collection_type: open
  name: Method Account Attributes Simulate Entities API
  slug: open-methodfi-simulate-entities-api
- collection_type: open
  name: Method Account Attributes Simulate Events API
  slug: open-methodfi-simulate-events-api
- collection_type: open
  name: Method Account Attributes Simulate Payments API
  slug: open-methodfi-simulate-payments-api
- collection_type: open
  name: Method Account Attributes Teams API
  slug: open-methodfi-teams-api
- collection_type: open
  name: Method Financial Accounts Transactions API
  slug: open-methodfi-transactions-api
- collection_type: open
  name: Method Account Attributes Webhooks API
  slug: open-methodfi-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/methodfi-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/methodfi-openapi-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/methodfi/overview
- group: auth
  title: ''
  type: DomainSecurity
  url: security/methodfi-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/methodfi-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/methodfi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/methodfi-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/methodfi-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/methodfi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/methodfi-packages.yml
- group: design
  title: ''
  type: Components
  url: components/methodfi-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/methodfi-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/methodfi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://methodfi.statuspage.io
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/methodfi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/methodfi-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://methodfi.com/security
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/methodfi-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/methodfi-decline-codes.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/methodfi-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/methodfi-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/methodfi-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/methodfi-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/methodfi-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/methodfi-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://methodfi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.methodfi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.methodfi.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.methodfi.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.methodfi.com/guides/quickstart
- group: operate
  title: ''
  type: Support
  url: https://methodfi.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MethodFi
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/methodfi/method-api
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.methodfi.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://methodfi.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://methodfi.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: security/methodfi-trust-center.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/methodfi
- group: commercial
  title: ''
  type: Plans
  url: plans/methodfi-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/methodfi-finops.yml
created: '2026-07-17'
description: Method (Method Financial) is the infrastructure layer for consumer liability data and payments. Its API lets developers create entities, verify identity, and use Connect to discover a user's complete liability picture across 15,000+ institutions (credit cards, auto loans, student loans, mortgages, personal loans) without credential sharing, then normalize that data and move money via ACH to pay down those liabilities. Additional products include credit scores, card-brand enrichment, financial attributes, transactions, updates/subscriptions for monitoring, reports, and embeddable UI (Opal/Elements). Method powers lending, personal finance management, and commerce/card-linking use cases.
finops:
- name: Methodfi Finops
  service_category: Financial Services
  slug: methodfi-finops
image: https://framerusercontent.com/assets/ZHgWyxIoZ4u3muxNTrEuOhP9o.jpg
layout: provider
mcp_servers:
- description: No official hosted/remote Method MCP server was found (no @methodfi MCP package, no documented MCP endpoint). This is a DERIVED candidate tool surface mapping marquee Method operations to MCP tools, o
  name: MethodFi MCP Server
  slug: methodfi-mcp-server
modified: '2026-08-08'
name: MethodFi
nav: Providers
network: true
overview: 'MethodFi publishes 44 APIs on the [APIs.io](https://apis.io/) network, including Account Attributes API, Account Balances API, Account Card Brands API, and 41 more. Tagged areas include Company, Fintech, Liability Data, Payments, and Lending.


  The MethodFi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MethodFi''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, support, and 34 more developer resources.'
plans:
- name: Methodfi Plans Pricing
  plan_count: 2
  slug: methodfi-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 6
  name: Methodfi Rate Limits
  slug: methodfi-rate-limits
score:
  band: exemplar
  composite: 69.0
  coverage:
    artifact_dirs: 28
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 69.2
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 81.6
  previous_composite: 69.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 44
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/screenshots/methodfi-2026-08-07T172708.png
security:
- kind: authentication
  name: Methodfi Authentication
  slug: methodfi-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Methodfi Domain Security
  slug: methodfi-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: trust-center
  name: Methodfi Trust Center
  slug: methodfi-trust-center
  summary_line: SOC 2, PCI DSS
slug: methodfi
tags:
- Company
- Fintech
- Liability Data
- Payments
- Lending
- Personal Finance
- Credit
- ACH
- Debt
- Identity Verification
website: https://methodfi.com
---
