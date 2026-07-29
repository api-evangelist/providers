---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 73
  human_in_the_loop: 8
  name: Unit Co Agentic Access
  operation_count: 138
  slug: unit-co-agentic-access
  summary_line: 138 operations · 73 acting · 8 human-in-the-loop
api_count: 17
apis:
- description: Deposit and credit accounts.
  name: Unit Accounts API
  slug: unit-co-accounts-api
- description: Org-level and customer-level authentication tokens.
  name: Unit API Tokens API
  slug: unit-co-api-tokens-api
- description: Individual and business application onboarding (KYC/KYB).
  name: Unit Applications API
  slug: unit-co-applications-api
- description: Completed card authorizations and real-time authorization requests.
  name: Unit Authorizations API
  slug: unit-co-authorizations-api
- description: Debit and credit card issuance and management.
  name: Unit Cards API
  slug: unit-co-cards-api
- description: Check deposits and outbound check payments.
  name: Unit Checks API
  slug: unit-co-checks-api
- description: External bank accounts and routing-number institution lookups.
  name: Unit Counterparties API
  slug: unit-co-counterparties-api
- description: Repayments on credit accounts and receivables.
  name: Unit Credit and Repayments API
  slug: unit-co-credit-and-repayments-api
- description: Customer profiles created from approved applications.
  name: Unit Customers API
  slug: unit-co-customers-api
- description: Platform activity log.
  name: Unit Events API
  slug: unit-co-events-api
- description: Ad hoc fees and cashback-style rewards.
  name: Unit Fees and Rewards API
  slug: unit-co-fees-and-rewards-api
- description: Book, ACH, wire, recurring, and cash-deposit payments.
  name: Unit Payments API
  slug: unit-co-payments-api
- description: Stop payments and card/ACH disputes.
  name: Unit Risk and Fraud API
  slug: unit-co-risk-and-fraud-api
- description: Monthly account statements.
  name: Unit Statements API
  slug: unit-co-statements-api
- description: Annual tax documents.
  name: Unit Tax Forms API
  slug: unit-co-tax-forms-api
- description: Posted, immutable ledger entries.
  name: Unit Transactions API
  slug: unit-co-transactions-api
- description: Subscriptions that deliver events as signed HTTP callbacks.
  name: Unit Webhooks API
  slug: unit-co-webhooks-api
artifact_total: 26
collections:
- collection_type: open
  name: Unit API
  slug: open-unit-co
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unit-co-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/unit-co-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unit-co-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unit-co-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unit-co-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unit-finance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unit-finance
- group: company
  title: ''
  type: Website
  url: https://www.unit.co/
- group: docs
  title: ''
  type: Documentation
  url: https://www.unit.co/docs/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/unit-co-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unit-co-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unit-co-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.unit.co/blog/
created: '2026-07-02'
description: Unit is a Banking-as-a-Service (BaaS) platform that lets companies embed deposit accounts, cards, payments, and lending into their own products without becoming a bank. A single REST API, built on the JSON:API specification (media type application/vnd.api+json) and secured with Bearer/JWT tokens, covers onboarding (Applications), Customers, Deposit and Credit Accounts, Debit and Credit Cards, real-time card Authorizations, Payments (Book, ACH, Wire, Recurring, Cash Deposits), Counterparties, Checks, Transactions, Statements, Tax Forms, Fees, Rewards, Credit and Repayments, and Events delivered as signed HTTP webhooks. Unit publishes an official OpenAPI 3.0.2 specification (github.com/unit-finance/openapi-unit-sdk) plus generated Node.js, Python, Ruby, and Java SDKs. Sandbox runs at api.s.unit.sh; production access is provisioned per signed BaaS agreement with Unit's partner banks.
finops:
- name: Unit Co Finops
  service_category: Banking as a Service
  slug: unit-co-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unit-co.png
layout: provider
modified: '2026-07-02'
name: Unit
nav: Providers
network: true
overview: 'Unit publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, API Tokens API, Applications API, and 14 more. Tagged areas include FinTech, BaaS, Banking, Payments, and Card Issuing.


  Unit''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Unit Co Plans Pricing
  plan_count: 2
  slug: unit-co-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 4
  name: Unit Co Rate Limits
  slug: unit-co-rate-limits
score:
  band: thin
  composite: 35.2
  delta: -4.7
  facets:
    commercial_clarity: 36.8
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 29.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Unit Co Authentication
  slug: unit-co-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Unit Co Domain Security
  slug: unit-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Unit Co Vulnerability Disclosure
  slug: unit-co-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Unit Co Trust Center
  slug: unit-co-trust-center
  summary_line: SOC 2, PCI DSS
slug: unit-co
tags:
- FinTech
- BaaS
- Banking
- Payments
- Card Issuing
- ACH
- Lending
- JSON:API
website: https://www.unit.co/
---
