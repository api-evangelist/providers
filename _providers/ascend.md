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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 49
  human_in_the_loop: 0
  name: Ascend Agentic Access
  operation_count: 86
  slug: ascend-agentic-access
  summary_line: 86 operations · 49 acting
api_count: 23
apis:
- description: The Accounts API from Ascend — 2 operation(s) for accounts.
  name: Ascend Accounts API
  slug: ascend-accounts-api
- description: Represents a file that is associated with a program.
  name: Ascend Attachments API
  slug: ascend-attachments-api
- description: Represents an insurance quote or endorsement to be billed to the insured.
  name: Ascend Billables API
  slug: ascend-billables-api
- description: Represents the cancelation of an insurance quote
  name: Ascend CancelationReturns API
  slug: ascend-cancelationreturns-api
- description: Represents the carriers Ascend supports for quote creation.
  name: Ascend Carriers API
  slug: ascend-carriers-api
- description: Represents the contacts that may be associated with an Insured account.
  name: Ascend Contacts API
  slug: ascend-contacts-api
- description: Represents the coverage types Ascend supports for quote creation.
  name: Ascend CoverageTypes API
  slug: ascend-coveragetypes-api
- description: Estimated financing terms.
  name: Ascend FinanceEstimate API
  slug: ascend-financeestimate-api
- description: A payment plan broken down over a seriies of regular installments
  name: Ascend InstallmentPlans API
  slug: ascend-installmentplans-api
- description: An single installment on a installment plan
  name: Ascend Installments API
  slug: ascend-installments-api
- description: Represents the person or business entity that is purchasing the collection of insurance quotes.
  name: Ascend Insureds API
  slug: ascend-insureds-api
- description: Represents records of a transaction between the insured and Ascend.
  name: Ascend Invoices API
  slug: ascend-invoices-api
- description: Loan details for a financed program
  name: Ascend Loans API
  slug: ascend-loans-api
- description: Represents records of a transaction between an insured and an agency or MGA.
  name: Ascend OneTimePayments API
  slug: ascend-onetimepayments-api
- description: The Organization Account Users API from Ascend — 2 operation(s) for organization account users.
  name: Ascend Organization Account Users API
  slug: ascend-organization-account-users-api
- description: The PaymentProposals API from Ascend — 1 operation(s) for paymentproposals.
  name: Ascend PaymentProposals API
  slug: ascend-paymentproposals-api
- description: Money transfers between accounts triggered after an insured pays a quote.
  name: Ascend Payouts API
  slug: ascend-payouts-api
- description: Represents a premium reducing endorsement for an insurance quote.
  name: Ascend PremiumReducingEndorsements (Beta) API
  slug: ascend-premiumreducingendorsements-beta-api
- description: A collection of insurance quotes pooled to produce 1 checkout link.
  name: Ascend Programs API
  slug: ascend-programs-api
- description: A collection of refunds to the insured.
  name: Ascend Refunds API
  slug: ascend-refunds-api
- description: A collection of returns on one time payments or installment plans.
  name: Ascend Returns API
  slug: ascend-returns-api
- description: Represent users that manage programs. They can be analysts, producers, support & admins.
  name: Ascend Users API
  slug: ascend-users-api
- description: The Wholesalers API from Ascend — 1 operation(s) for wholesalers.
  name: Ascend Wholesalers API
  slug: ascend-wholesalers-api
artifact_total: 29
asyncapis:
- description: ''
  name: Ascend Webhooks
  slug: ascend-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ascend-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ascend-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ascend-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://useascend.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.useascend.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.useascend.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.useascend.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.useascend.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.useascend.com/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.useascend.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.useascend.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://useascend.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://useascend.com/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://useascend.com/legal/security-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ascend-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ascend-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ascend-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ascend-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ascend-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ascend-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ascend-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ascend-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/ascend-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ascend-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ascend-vulnerability-disclosure.yml
created: '2026-07-17'
description: Ascend is a financial operations platform built for the insurance industry, offering AI-powered accounting automation, payments, and premium financing in a single vertically integrated solution. Its REST API (v1) lets insurance agencies, wholesalers, MGAs, and carriers automate billing and invoicing, premium financing and installment plans, cash application, carrier payables, and direct bill workflows — managing insureds, programs, billables, invoices, loans, payouts, refunds, and one-time payments programmatically, secured with bearer tokens and HMAC-signed webhooks for invoice, payout, and refund events. Trusted by over 4,000 insurance businesses, including over half of the 50 largest brokers.
image: https://www.useascend.com/favicons/icon-512.png
layout: provider
mcp_servers:
- description: ''
  name: ascend-mcp.yml
  slug: ascend-mcpyml
modified: '2026-07-18'
name: Ascend
nav: Providers
network: true
overview: 'Ascend publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Attachments API, Billables API, and 20 more. Tagged areas include Company, Fintech, Insurance, InsurTech, and Payments.


  The Ascend catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ascend''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, sandbox, and 19 more developer resources.'
random_paper: 48
score:
  band: developing
  composite: 51.1
  delta: -4.7
  facets:
    commercial_clarity: 42.1
    contract_quality: 59.5
    developer_ergonomics: 60.3
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 34.2
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ascend/refs/heads/main/screenshots/ascend-2026-07-25T201401.png
security:
- kind: authentication
  name: Ascend Authentication
  slug: ascend-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ascend Domain Security
  slug: ascend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ascend Vulnerability Disclosure
  slug: ascend-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: ascend
tags:
- Company
- Fintech
- Insurance
- InsurTech
- Payments
- Premium Financing
- Billing
- Invoicing
- Embedded Finance
- REST API
- Webhooks
website: https://useascend.com/
---
