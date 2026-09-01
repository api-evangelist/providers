---
agent_readiness:
  band: agent-aware
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Nacha Agentic Access
  operation_count: 30
  slug: nacha-agentic-access
  summary_line: 30 operations · 25 acting
api_count: 24
apis:
- description: The Account Validation API from Nacha — 1 operation(s) for account validation.
  name: Nacha Account Validation API
  slug: nacha-account-validation-api
- description: The Accounts API from Nacha — 4 operation(s) for accounts.
  name: Nacha Accounts API
  slug: nacha-accounts-api
- description: The ACH Payments API from Nacha — 2 operation(s) for ach payments.
  name: Nacha ACH Payments API
  slug: nacha-ach-payments-api
- description: The ACH Transaction Status API from Nacha — 4 operation(s) for ach transaction status.
  name: Nacha ACH Transaction Status API
  slug: nacha-ach-transaction-status-api
- description: The Authorize to Pay API from Nacha — 1 operation(s) for authorize to pay.
  name: Nacha Authorize to Pay API
  slug: nacha-authorize-to-pay-api
- description: The Banks API from Nacha — 1 operation(s) for banks.
  name: Nacha Banks API
  slug: nacha-banks-api
- description: The Expand Bank Contact V2 API from Nacha — 1 operation(s) for expand bank contact v2.
  name: Nacha Expand Bank Contact V2 API
  slug: nacha-expand-bank-contact-v2-api
- description: The Get Corporate Account Balances API from Nacha — 1 operation(s) for get corporate account balances.
  name: Nacha Get Corporate Account Balances API
  slug: nacha-get-corporate-account-balances-api
- description: The Get Corporate Transaction History API from Nacha — 2 operation(s) for get corporate transaction history.
  name: Nacha Get Corporate Transaction History API
  slug: nacha-get-corporate-transaction-history-api
- description: The Get Participants Profile API from Nacha — 1 operation(s) for get participants profile.
  name: Nacha Get Participants Profile API
  slug: nacha-get-participants-profile-api
- description: The Initiate Payment API from Nacha — 1 operation(s) for initiate payment.
  name: Nacha Initiate Payment API
  slug: nacha-initiate-payment-api
- description: The Instant Payment API from Nacha — 1 operation(s) for instant payment.
  name: Nacha Instant Payment API
  slug: nacha-instant-payment-api
- description: The Instant Payment Transfer API from Nacha — 1 operation(s) for instant payment transfer.
  name: Nacha Instant Payment Transfer API
  slug: nacha-instant-payment-transfer-api
- description: The International ACH Remittance (IAR) API from Nacha — 2 operation(s) for international ach remittance (iar).
  name: Nacha International ACH Remittance (IAR) API
  slug: nacha-international-ach-remittance-iar-api
- description: The Proof of Authorization API from Nacha — 1 operation(s) for proof of authorization.
  name: Nacha Proof of Authorization API
  slug: nacha-proof-of-authorization-api
- description: The Reporting ACH Return Payments API from Nacha — 1 operation(s) for reporting ach return payments.
  name: Nacha Reporting ACH Return Payments API
  slug: nacha-reporting-ach-return-payments-api
- description: The Route Billing Information API from Nacha — 1 operation(s) for route billing information.
  name: Nacha Route Billing Information API
  slug: nacha-route-billing-information-api
- description: The Wire Transfer API from Nacha — 2 operation(s) for wire transfer.
  name: Nacha Wire Transfer API
  slug: nacha-wire-transfer-api
- description: The Written Statement of Unauthorized Debit (WSUD) API from Nacha — 1 operation(s) for written statement of unauthorized debit (wsud).
  name: Nacha Written Statement of Unauthorized Debit (WSUD) API
  slug: nacha-written-statement-of-unauthorized-debit-wsud-api
artifact_total: 47
collections:
- collection_type: open
  name: AV + Name + Return
  slug: open-nacha-account-validation-plus-name-ret
- collection_type: open
  name: Account Validation Plus Ownership API
  slug: open-nacha-account-validation-plus-name
- collection_type: open
  name: Account Validation APIs
  slug: open-nacha-account-validation
- collection_type: open
  name: Debit Authorizations
  slug: open-nacha-authorize-to-pay
- collection_type: open
  name: Bank Contact V2
  slug: open-nacha-bank-contact-v2
- collection_type: open
  name: Bank Contacts APIs
  slug: open-nacha-bank-contacts
- collection_type: open
  name: Get Corporate Account Balances API
  slug: open-nacha-corporate-account-balances
- collection_type: open
  name: Get Transaction Detail API
  slug: open-nacha-corporate-transaction-detail
- collection_type: open
  name: Get Corporate Transaction History API
  slug: open-nacha-corporate-transaction-history
- collection_type: open
  name: Get Wire Status
  slug: open-nacha-get-wire-status
- collection_type: open
  name: IAR Plus API
  slug: open-nacha-iar-plus
- collection_type: open
  name: IAR_API
  slug: open-nacha-iar
- collection_type: open
  name: Initiate Instant Payment API (IIP)
  slug: open-nacha-initiate-instant-payment
- collection_type: open
  name: Initiate Payment API
  slug: open-nacha-initiate-payment-api
- collection_type: open
  name: Initiate Payment API
  slug: open-nacha-initiate-payment
- collection_type: open
  name: Initiate Wire Payment API
  slug: open-nacha-initiate-wire-payment
- collection_type: open
  name: Instant Payment Transfer (IPT)
  slug: open-nacha-instant-payment-transfer
- collection_type: open
  name: Pay Me API
  slug: open-nacha-pay-me
- collection_type: open
  name: Payee Profile API
  slug: open-nacha-payee-profile
- collection_type: open
  name: Proof of Authorization API
  slug: open-nacha-proof-of-authorization
- collection_type: open
  name: Real Time Billing Account Validation User Story 1
  slug: open-nacha-realtime-billing-account-validation
- collection_type: open
  name: RET (Reporting ACH Return Payments) API
  slug: open-nacha-ret
- collection_type: open
  name: Transaction Status API
  slug: open-nacha-transaction-status
- collection_type: open
  name: Request Copy of Written Statement of Unauthorized Debit (WSUD) API
  slug: open-nacha-wsud
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-initiate-payment-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-iar-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-iar-plus-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-transaction-status-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-initiate-wire-payment-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-get-wire-status-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-initiate-instant-payment-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-instant-payment-transfer-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-initiate-payment-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-ret-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-authorize-to-pay-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-pay-me-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-account-validation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-account-validation-plus-name-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-account-validation-plus-name-ret-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-realtime-billing-account-validation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-corporate-account-balances-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-corporate-transaction-history-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-corporate-transaction-detail-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-payee-profile-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-wsud-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-proof-of-authorization-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-bank-contacts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nacha-bank-contact-v2-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/nacha-initiate-ach-payment.md
- group: start
  title: ''
  type: Login
  url: https://www.nacha.org/user/login
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nacha-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nacha-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nacha-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.nacha.org/
- group: company
  title: ''
  type: About
  url: https://www.nacha.org/content/about-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.nacha.org/content/apis-development
- group: docs
  title: ''
  type: APIReference
  url: https://www.nacha.org/content/afinis-api-catalog
- group: docs
  title: ''
  type: Documentation
  url: https://www.nacha.org/content/afinis-interoperability-standards
- group: start
  title: ''
  type: GettingStarted
  url: https://achdevguide.nacha.org/
- group: design
  title: ''
  type: Rules
  url: https://www.nacha.org/rules
- group: company
  title: ''
  type: Blog
  url: https://www.nacha.org/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nacha
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nacha.org/content/legal-information
- group: design
  title: ''
  type: Conventions
  url: conventions/nacha-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nacha-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nacha-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nacha-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nacha-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/nacha-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nacha-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/nacha-data-model.yml
- group: agent
  title: ''
  type: AgentSkills
  url: skills/_index.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nacha.org/content/privacy-policy
created: '2026-07-24'
description: 'Nacha (formerly the National Automated Clearing House Association) is the nonprofit, member-governed steward of the ACH Network, the batch-based account-to-account payment rail that moves consumer and business direct deposits, direct payments, bill pay, and B2B transfers across the United States — more than 30 billion payments and over $80 trillion in value annually. Nacha writes and enforces the Nacha Operating Rules that bind the network''s participating depository financial institutions, but it is not itself an ACH Operator (the Federal Reserve and The Clearing House clear and settle the files). Nacha is documentation- and rulebook-first rather than a self-serve PSP: it does not operate a public production payments API of its own. Its API posture is delivered through Afinis Interoperability Standards, the Nacha-stewarded group that publishes royalty-free, standardized financial-services API specifications (payment initiation, account validation, transaction status, returns
  reporting, and directory services) as Swagger/OpenAPI documents on SwaggerHub, and through Phixius, its payment-information exchange platform. Its home market is the United States.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Nacha MCP Server
  slug: nacha-mcp-server
modified: '2026-07-24'
name: Nacha
nav: Providers
network: true
overview: 'Nacha publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Account Validation API, Accounts API, ACH Payments API, and 16 more. Tagged areas include Payments, United States, ACH, Account-to-Account, and Real-Time Payments.


  Nacha''s developer surface includes authentication, API reference, documentation, getting-started guide, engineering blog, and 44 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 49.1
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 45.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nacha/refs/heads/main/screenshots/nacha-2026-08-07T184604.png
security:
- kind: authentication
  name: Nacha Authentication
  slug: nacha-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nacha Domain Security
  slug: nacha-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nacha
tags:
- Payments
- United States
- ACH
- Account-to-Account
- Real-Time Payments
- Account Validation
- Payment Rails
- ISO 20022
- Standards
- Afinis
website: https://www.nacha.org/
---
