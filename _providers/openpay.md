---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Openpay Agentic Access
  operation_count: 48
  slug: openpay-agentic-access
  summary_line: 48 operations · 25 acting
api_count: 1
apis:
- description: Manage customer bank accounts used as payout destinations.
  name: Openpay BankAccounts API
  slug: openpay-bankaccounts-api
- description: Store and manage cards at merchant or customer level.
  name: Openpay Cards API
  slug: openpay-cards-api
- description: Create and manage charges to cards, stores, and banks.
  name: Openpay Charges API
  slug: openpay-charges-api
- description: Manage customer records.
  name: Openpay Customers API
  slug: openpay-customers-api
- description: Charge commission fees to a customer's Openpay balance.
  name: Openpay Fees API
  slug: openpay-fees-api
- description: Send funds to registered bank accounts.
  name: Openpay Payouts API
  slug: openpay-payouts-api
- description: Templates defining amount and frequency for recurring charges.
  name: Openpay Plans API
  slug: openpay-plans-api
- description: Associate customers and cards to plans for recurring billing.
  name: Openpay Subscriptions API
  slug: openpay-subscriptions-api
- description: Client-side tokenization of card data.
  name: Openpay Tokens API
  slug: openpay-tokens-api
- description: Move funds between Openpay customers.
  name: Openpay Transfers API
  slug: openpay-transfers-api
- description: Register and manage webhook endpoints for event notifications.
  name: Openpay Webhooks API
  slug: openpay-webhooks-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Openpay BankAccounts API
  slug: open-openpay-bankaccounts-api
- collection_type: open
  name: Openpay BankAccounts Cards API
  slug: open-openpay-cards-api
- collection_type: open
  name: Openpay BankAccounts Charges API
  slug: open-openpay-charges-api
- collection_type: open
  name: Openpay BankAccounts Customers API
  slug: open-openpay-customers-api
- collection_type: open
  name: Openpay BankAccounts Fees API
  slug: open-openpay-fees-api
- collection_type: open
  name: Openpay BankAccounts Payouts API
  slug: open-openpay-payouts-api
- collection_type: open
  name: Openpay BankAccounts Plans API
  slug: open-openpay-plans-api
- collection_type: open
  name: Openpay BankAccounts Subscriptions API
  slug: open-openpay-subscriptions-api
- collection_type: open
  name: Openpay BankAccounts Tokens API
  slug: open-openpay-tokens-api
- collection_type: open
  name: Openpay BankAccounts Transfers API
  slug: open-openpay-transfers-api
- collection_type: open
  name: Openpay BankAccounts Webhooks API
  slug: open-openpay-webhooks-api
- collection_type: open
  name: Openpay API
  slug: open-openpay
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openpay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openpay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openpay-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/open-pay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openpay
- group: company
  title: ''
  type: Website
  url: https://www.openpay.mx
- group: docs
  title: ''
  type: Documentation
  url: https://documents.openpay.mx/docs/api
- group: commercial
  title: ''
  type: Plans
  url: plans/openpay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openpay-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openpay-finops.yml
created: '2026-06-21'
description: Openpay is a Mexican and Colombian online payments platform, part of the BBVA group, offering a REST API for accepting card payments, cash/store payments, and bank transfers (SPEI). The API covers charges, customers, cards, tokens, subscriptions, plans, payouts, transfers, fees, and webhooks under a per-merchant base path with HTTP Basic authentication using a private API key.
finops:
- name: Openpay Finops
  service_category: Payment Processing
  slug: openpay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openpay.png
layout: provider
modified: '2026-06-21'
name: Openpay
nav: Providers
network: true
overview: 'Openpay publishes 11 APIs on the [APIs.io](https://apis.io/) network, including BankAccounts API, Cards API, Charges API, and 8 more. Tagged areas include Payments, Fintech, Cards, SPEI, and Subscription.


  Openpay''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Openpay Plans Pricing
  plan_count: 2
  slug: openpay-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Openpay Rate Limits
  slug: openpay-rate-limits
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 49.2
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 30.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openpay/refs/heads/main/screenshots/openpay-2026-08-07T190624.png
security:
- kind: authentication
  name: Openpay Authentication
  slug: openpay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openpay Domain Security
  slug: openpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openpay
tags:
- Payments
- Fintech
- Cards
- SPEI
- Subscription
website: https://www.openpay.mx
---
