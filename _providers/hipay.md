---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Hipay Agentic Access
  operation_count: 55
  slug: hipay-agentic-access
  summary_line: 55 operations · 23 acting
api_count: 20
apis:
- description: Manage the balance of a HiPay account
  name: HiPay balance API
  slug: hipay-balance-api
- description: Manage bank informations of a HiPay account
  name: HiPay bank-info API
  slug: hipay-bank-info-api
- description: Generate captcha
  name: HiPay captcha-generation API
  slug: hipay-captcha-generation-api
- description: The Connector API from HiPay — 1 operation(s) for connector.
  name: HiPay Connector API
  slug: hipay-connector-api
- description: Manage your account with our API tools
  name: HiPay constants API
  slug: hipay-constants-api
- description: Manage your identification documents
  name: HiPay identification API
  slug: hipay-identification-api
- description: Manage marketplace invoices
  name: HiPay invoice API
  slug: hipay-invoice-api
- description: Perform operations (capture, refund) on transactions
  name: HiPay maintenance API
  slug: hipay-maintenance-api
- description: Manage merchant groups
  name: HiPay merchant-group API
  slug: hipay-merchant-group-api
- description: The Order API from HiPay — 2 operation(s) for order.
  name: HiPay Order API
  slug: hipay-order-api
- description: Everything you need to create orders and transactions
  name: HiPay payments API
  slug: hipay-payments-api
- description: The Routing API from HiPay — 1 operation(s) for routing.
  name: HiPay Routing API
  slug: hipay-routing-api
- description: The Sessions API from HiPay — 1 operation(s) for sessions.
  name: HiPay Sessions API
  slug: hipay-sessions-api
- description: Everything you need to get all settlement details
  name: HiPay settlement API
  slug: hipay-settlement-api
- description: Everything you need to tokenize payment cards
  name: HiPay tokenization API
  slug: hipay-tokenization-api
- description: The Transaction API from HiPay — 6 operation(s) for transaction.
  name: HiPay Transaction API
  slug: hipay-transaction-api
- description: Transfer funds between HiPay accounts
  name: HiPay transfer API
  slug: hipay-transfer-api
- description: Manage your Ultimate Beneficial Ownerships (UBO)
  name: HiPay ubo API
  slug: hipay-ubo-api
- description: Manage your HiPay account
  name: HiPay user-account API
  slug: hipay-user-account-api
- description: Request a withdrawal from a HiPay account
  name: HiPay withdrawal API
  slug: hipay-withdrawal-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hipay Payment Gateway balance API
  slug: open-hipay-balance-api
- collection_type: open
  name: Hipay Payment Gateway balance bank-info API
  slug: open-hipay-bank-info-api
- collection_type: open
  name: Hipay Payment Gateway balance captcha-generation API
  slug: open-hipay-captcha-generation-api
- collection_type: open
  name: Hipay Payment Gateway balance Connector API
  slug: open-hipay-connector-api
- collection_type: open
  name: Hipay Payment Gateway balance constants API
  slug: open-hipay-constants-api
- collection_type: open
  name: Hipay Payment Gateway balance identification API
  slug: open-hipay-identification-api
- collection_type: open
  name: Hipay Payment Gateway balance invoice API
  slug: open-hipay-invoice-api
- collection_type: open
  name: Hipay Payment Gateway balance maintenance API
  slug: open-hipay-maintenance-api
- collection_type: open
  name: Hipay Payment Gateway balance merchant-group API
  slug: open-hipay-merchant-group-api
- collection_type: open
  name: Hipay Payment Gateway balance Order API
  slug: open-hipay-order-api
- collection_type: open
  name: Hipay Payment Gateway balance payments API
  slug: open-hipay-payments-api
- collection_type: open
  name: Hipay Payment Gateway balance Routing API
  slug: open-hipay-routing-api
- collection_type: open
  name: Hipay Payment Gateway balance Sessions API
  slug: open-hipay-sessions-api
- collection_type: open
  name: Hipay Payment Gateway balance settlement API
  slug: open-hipay-settlement-api
- collection_type: open
  name: Hipay Payment Gateway balance tokenization API
  slug: open-hipay-tokenization-api
- collection_type: open
  name: Hipay Payment Gateway balance Transaction API
  slug: open-hipay-transaction-api
- collection_type: open
  name: Hipay Payment Gateway balance transfer API
  slug: open-hipay-transfer-api
- collection_type: open
  name: Hipay Payment Gateway balance ubo API
  slug: open-hipay-ubo-api
- collection_type: open
  name: Hipay Payment Gateway balance user-account API
  slug: open-hipay-user-account-api
- collection_type: open
  name: Hipay Payment Gateway balance withdrawal API
  slug: open-hipay-withdrawal-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hipay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hipay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hipay-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.hipay.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hipay.com
- group: docs
  title: ''
  type: OpenAPI Repository
  url: https://github.com/hipay/openapi-hipay
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hipay
- group: operate
  title: ''
  type: Support
  url: https://support.hipay.com
- group: company
  title: ''
  type: Blog
  url: https://blog.hipay.com
- group: company
  title: ''
  type: Website
  url: https://hipay.com/en/
- group: design
  title: ''
  type: Webhooks
  url: https://developer.hipay.com/online-payments/payment/notifications
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/hipay/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/hipay/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/hipay/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: HiPay is a European omnichannel payment platform headquartered in Levallois-Perret, France, offering REST APIs for online payments, in-store terminal management, fraud prevention, 3DS authentication, tokenization, marketplace payments, and payment reporting. Founded in 2011, HiPay is listed on Euronext Growth Paris and processes over €7.5 billion in transactions annually across five European countries.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hipay.png
layout: provider
modified: '2026-06-13'
name: HiPay
nav: Providers
network: true
overview: 'HiPay publishes 20 APIs on the [APIs.io](https://apis.io/) network, including balance API, bank-info API, captcha-generation API, and 17 more. Tagged areas include Payments, Fintech, Europe, Omnichannel, and Point-of-Sale.


  HiPay''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 14
rate_limits:
- limit_count: 4
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 37.4
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 52.6
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hipay/refs/heads/main/screenshots/hipay-2026-06-20T182747.png
security:
- kind: authentication
  name: Hipay Authentication
  slug: hipay-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Hipay Domain Security
  slug: hipay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hipay
tags:
- Payments
- Fintech
- Europe
- Omnichannel
- Point-of-Sale
- Fraud Prevention
- Tokenization
- Marketplace
website: https://hipay.com/en/
---
