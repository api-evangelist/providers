---
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
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Nacha Agentic Access
  operation_count: 30
  slug: nacha-agentic-access
  summary_line: 30 operations · 25 acting
api_count: 24
apis:
- description: Afinis Interoperability Standards API for initiating an ACH credit or debit payment instruction from an originator through their financial institution. Part of the Afinis standardized payments API set
  name: Afinis Initiate ACH Payment API
  slug: nacha-initiate-payment
- description: Afinis International ACH Remittance (IAR) API for sending remittance information tied to incoming IAT (International ACH Transaction) credits.
  name: Afinis International ACH Remittance (IAR) API
  slug: nacha-iar
- description: Afinis IAR Plus API, an extended International ACH Remittance message for incoming IAT credits carrying additional remittance detail.
  name: Afinis IAR Plus API
  slug: nacha-iar-plus
- description: Afinis Transaction Status API for querying the status of an ACH credit or debit payment by instruction ID or transaction ID.
  name: Afinis Transaction Status API
  slug: nacha-transaction-status
- description: Afinis Initiate Wire Payment API enabling a business to originate a wire transfer through its financial institution via a standardized API call.
  name: Afinis Initiate Wire Payment API
  slug: nacha-initiate-wire-payment
- description: Afinis Get Wire Status API enabling the originator of a wire to retrieve the status of the wire payment.
  name: Afinis Get Wire Status API
  slug: nacha-get-wire-status
- description: Afinis Initiate Instant Payment (IIP) API enabling a business to make an instant payment through its financial institution, mapping to US real-time rails (RTP and FedNow).
  name: Afinis Initiate Instant Payment API (IIP)
  slug: nacha-initiate-instant-payment
- description: Afinis Instant Payment Transfer (IPT) API enabling a financial institution to send another financial institution an instant payment via an API.
  name: Afinis Instant Payment Transfer API (IPT)
  slug: nacha-instant-payment-transfer
- description: Afinis Initiate Payment API used to request movement of funds from a debtor account to a creditor account across supported payment rails.
  name: Afinis Initiate Payment API
  slug: nacha-initiate-payment-api
- description: Afinis Reporting ACH Return (RET) API allowing originators and payment providers to share ACH return payment data in support of fraud and risk mitigation.
  name: Afinis Reporting ACH Return (RET) API
  slug: nacha-ret
- description: Afinis Authorize to Pay API letting a buyer business provide bank account or virtual card details, purpose of payment, and authorization for a seller to debit the account.
  name: Afinis Authorize to Pay (Debit Authorizations) API
  slug: nacha-authorize-to-pay
- description: Afinis Pay Me API for requesting a payment (request-for-payment) from a payer through standardized messaging.
  name: Afinis Pay Me API
  slug: nacha-pay-me
- description: Afinis Account Validation API for validating that a bank account is open and able to accept ACH credits or debits, reducing returns and fraud.
  name: Afinis Account Validation API
  slug: nacha-account-validation
- description: Afinis Account Validation Plus Ownership API validating account status together with account-owner name/ownership for confirmation-of-payee style checks.
  name: Afinis Account Validation Plus Ownership (Name) API
  slug: nacha-account-validation-plus-name
- description: Afinis Account Validation combined with name verification and ACH return-history signals in a single standardized message.
  name: Afinis Account Validation Plus Name Plus Return API
  slug: nacha-account-validation-plus-name-ret
- description: Afinis Real-Time Billing Account Validation API for validating a consumer bank account at the point of billing enrollment.
  name: Afinis Real-Time Billing Account Validation API
  slug: nacha-realtime-billing-account-validation
- description: Afinis Get Corporate Account Balances API letting a corporate/business customer retrieve balance information for their accounts for a date or date range.
  name: Afinis Get Corporate Account Balances API
  slug: nacha-corporate-account-balances
- description: Afinis Get Corporate Transaction History API letting a corporate bank customer retrieve financial transaction history for review or integration.
  name: Afinis Get Corporate Transaction History API
  slug: nacha-corporate-transaction-history
- description: Afinis Get Transaction Detail API letting a corporate financial professional request detailed information for a specific transaction in their account.
  name: Afinis Get Transaction Detail API
  slug: nacha-corporate-transaction-detail
- description: Afinis Payee Profile API for exchanging standardized payee onboarding and directory profile information between participants.
  name: Afinis Payee Profile API
  slug: nacha-payee-profile
- description: Afinis WSUD API letting an ODFI send an automated electronic request to an RDFI for a copy of a consumer's Written Statement of Unauthorized Debit.
  name: Afinis Written Statement of Unauthorized Debit (WSUD) API
  slug: nacha-wsud
- description: Afinis Proof of Authorization API providing a real-time alternative message for a request for an ACH proof of authorization to increase automation and reduce manual handling.
  name: Afinis Proof of Authorization API
  slug: nacha-proof-of-authorization
- description: Afinis Bank Contacts API for retrieving standardized operational contact information for financial institutions.
  name: Afinis Bank Contacts API
  slug: nacha-bank-contacts
- description: Afinis Bank Contact V2 API, a two-step input/retrieve interface for exchanging standardized financial-institution contact information.
  name: Afinis Bank Contact V2 API
  slug: nacha-bank-contact-v2
artifact_total: 28
common:
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
  type: AgentSkill
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
  name: nacha-mcp.yml
  slug: nacha-mcpyml
modified: '2026-07-24'
name: Nacha
nav: Providers
network: true
overview: 'Nacha publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Afinis Initiate ACH Payment API, Afinis International ACH Remittance (IAR) API, Afinis IAR Plus API, and 21 more. Tagged areas include Payments, United States, ACH, Account-to-Account, and Real-Time Payments.


  Nacha''s developer surface includes authentication, API reference, documentation, getting-started guide, engineering blog, and 18 more developer resources.'
random_paper: 27
score:
  band: thin
  composite: 32.4
  delta: -5.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 32.3
    developer_ergonomics: 51.6
    discoverability: 72.2
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 37.9
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
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
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
