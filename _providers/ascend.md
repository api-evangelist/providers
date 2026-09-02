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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 49
  human_in_the_loop: 0
  name: Ascend Agentic Access
  operation_count: 86
  slug: ascend-agentic-access
  summary_line: 86 operations · 49 acting
api_count: 1
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
artifact_total: 53
asyncapis:
- description: ''
  name: Ascend Webhooks
  slug: ascend-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ascend API V1 Accounts API
  slug: open-ascend-accounts-api
- collection_type: open
  name: Ascend API V1 Accounts Attachments API
  slug: open-ascend-attachments-api
- collection_type: open
  name: Ascend API V1 Accounts Billables API
  slug: open-ascend-billables-api
- collection_type: open
  name: Ascend API V1 Accounts CancelationReturns API
  slug: open-ascend-cancelationreturns-api
- collection_type: open
  name: Ascend API V1 Accounts Carriers API
  slug: open-ascend-carriers-api
- collection_type: open
  name: Ascend API V1 Accounts Contacts API
  slug: open-ascend-contacts-api
- collection_type: open
  name: Ascend API V1 Accounts CoverageTypes API
  slug: open-ascend-coveragetypes-api
- collection_type: open
  name: Ascend API V1 Accounts FinanceEstimate API
  slug: open-ascend-financeestimate-api
- collection_type: open
  name: Ascend API V1 Accounts InstallmentPlans API
  slug: open-ascend-installmentplans-api
- collection_type: open
  name: Ascend API V1 Accounts Installments API
  slug: open-ascend-installments-api
- collection_type: open
  name: Ascend API V1 Accounts Insureds API
  slug: open-ascend-insureds-api
- collection_type: open
  name: Ascend API V1 Accounts Invoices API
  slug: open-ascend-invoices-api
- collection_type: open
  name: Ascend API V1 Accounts Loans API
  slug: open-ascend-loans-api
- collection_type: open
  name: Ascend API V1 Accounts OneTimePayments API
  slug: open-ascend-onetimepayments-api
- collection_type: open
  name: Ascend API V1 Accounts Organization Account Users API
  slug: open-ascend-organization-account-users-api
- collection_type: open
  name: Ascend API V1 Accounts PaymentProposals API
  slug: open-ascend-paymentproposals-api
- collection_type: open
  name: Ascend API V1 Accounts Payouts API
  slug: open-ascend-payouts-api
- collection_type: open
  name: Ascend API V1 Accounts PremiumReducingEndorsements (Beta) API
  slug: open-ascend-premiumreducingendorsements-beta-api
- collection_type: open
  name: Ascend API V1 Accounts Programs API
  slug: open-ascend-programs-api
- collection_type: open
  name: Ascend API V1 Accounts Refunds API
  slug: open-ascend-refunds-api
- collection_type: open
  name: Ascend API V1 Accounts Returns API
  slug: open-ascend-returns-api
- collection_type: open
  name: Ascend API V1 Accounts Users API
  slug: open-ascend-users-api
- collection_type: open
  name: Ascend API V1 Accounts Wholesalers API
  slug: open-ascend-wholesalers-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ascend-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ascend-openapi-overlay.yaml
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
  name: Ascend MCP Server
  slug: ascend-mcp-server
modified: '2026-07-18'
name: Ascend
nav: Providers
network: true
overview: 'Ascend publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Attachments API, Billables API, and 20 more. Tagged areas include Company, Fintech, Insurance, Insurtech, and Payments.


  The Ascend catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ascend''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, sandbox, and 21 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 58.1
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 48.3
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Insurtech
- Payments
- Premium Financing
- Billing
- Invoicing
- Embedded Finance
- REST API
- Webhook
website: https://useascend.com/
---
