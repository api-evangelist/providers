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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Opennode Agentic Access
  operation_count: 14
  slug: opennode-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 1
apis:
- description: REST API for creating and managing Bitcoin payment charges. Supports both on-chain Bitcoin and Lightning Network BOLT11 invoices. Merchants create a charge with an amount and currency, and OpenNode re
  name: OpenNode Charges API
  slug: opennode-charges-api
- description: 'REST API for initiating Bitcoin withdrawals and payouts to on-chain addresses or Lightning Network invoices. Enables businesses to pay contractors, execute payroll, or send payouts to users. Supports '
  name: OpenNode Withdrawals API
  slug: opennode-withdrawals-api
- description: REST API for creating and managing Bitcoin payment refunds. Allows merchants to issue full or partial refunds for charges back to the original payer's Bitcoin or Lightning address. Supports listing an
  name: OpenNode Refunds API
  slug: opennode-refunds-api
- description: REST API for initiating Bitcoin exchange operations, enabling merchants to convert between Bitcoin and local currencies. Supports automatic conversion at the time of payment with exchange rates locked
  name: OpenNode Exchanges API
  slug: opennode-exchanges-api
- description: REST API for retrieving account balance, transaction activity, and managing scheduled bank withdrawals. Provides a unified view of Bitcoin holdings, fiat settlements, and transaction history for the a
  name: OpenNode Account API
  slug: opennode-account-api
- description: REST API for creating and managing static on-chain Bitcoin addresses and static Lightning Network addresses via LNURL-Pay. Static addresses allow merchants to accept Bitcoin payments at a fixed addres
  name: OpenNode Static Addresses API
  slug: opennode-static-addresses-api
- description: REST API for retrieving real-time Bitcoin exchange rates across supported fiat currencies and listing all currencies supported by the OpenNode platform. Useful for displaying prices in local currency,
  name: OpenNode Rates and Currencies API
  slug: opennode-rates-and-currencies-api
- description: Account balance and transaction activity
  name: OpenNode Account API
  slug: opennode-account-api
- description: Create and manage Bitcoin payment charges
  name: OpenNode Charges API
  slug: opennode-charges-api
- description: Bitcoin exchange rates and supported currencies
  name: OpenNode Rates API
  slug: opennode-rates-api
- description: Create and manage payment refunds
  name: OpenNode Refunds API
  slug: opennode-refunds-api
- description: Static on-chain and Lightning Network addresses
  name: OpenNode Static Addresses API
  slug: opennode-static-addresses-api
- description: Initiate Bitcoin withdrawals and payouts
  name: OpenNode Withdrawals API
  slug: opennode-withdrawals-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenNode Account API
  slug: open-opennode-account-api
- collection_type: open
  name: OpenNode Account Charges API
  slug: open-opennode-charges-api
- collection_type: open
  name: OpenNode Account Rates API
  slug: open-opennode-rates-api
- collection_type: open
  name: OpenNode Account Refunds API
  slug: open-opennode-refunds-api
- collection_type: open
  name: OpenNode Account Static Addresses API
  slug: open-opennode-static-addresses-api
- collection_type: open
  name: OpenNode Account Withdrawals API
  slug: open-opennode-withdrawals-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opennode-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opennode-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opennode-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://opennode.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.opennode.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.opennode.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.opennode.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developers.opennode.com/docs/authorization
- group: design
  title: ''
  type: Webhooks
  url: https://developers.opennode.com/docs/webhooks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opennode.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://opennode.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://blog.opennode.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opennode/
- group: other
  title: ''
  type: X
  url: https://x.com/OpenNode
- group: build
  title: ''
  type: GitHub
  url: https://github.com/opennode
- group: commercial
  title: ''
  type: Plans
  url: plans/opennode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opennode-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opennode-finops.yml
created: '2026-06-13'
description: OpenNode is a Bitcoin and Lightning Network payment processor providing a REST API for businesses and developers to accept Bitcoin payments, create payment charges, manage Lightning Network invoices, process on-chain transactions, handle webhooks for real-time payment notifications, initiate Bitcoin withdrawals and payouts, and access payment analytics. The platform supports automatic currency conversion at the time of payment, allowing merchants to settle in local currency or Bitcoin. OpenNode serves ecommerce merchants, enterprise clients, and developers needing Bitcoin payment infrastructure with pre-built integrations for Shopify, WooCommerce, Magento, and BigCommerce.
examples:
- key_count: 11
  name: Create Charge Request
  slug: create-charge-request
- key_count: 1
  name: Create Charge Response
  slug: create-charge-response
- key_count: 4
  name: Initiate Withdrawal Request
  slug: initiate-withdrawal-request
- key_count: 15
  name: Webhook Payment Notification
  slug: webhook-payment-notification
finops:
- name: Opennode Finops
  service_category: ''
  slug: opennode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opennode.png
json_schemas:
- name: OpenNode Charge
  property_count: 15
  slug: opennode-charge
- name: OpenNode Withdrawal
  property_count: 8
  slug: opennode-withdrawal
jsonld:
- class_count: 26
  name: Opennode Context
  property_count: 11
  slug: opennode-context
layout: provider
modified: '2026-06-13'
name: OpenNode
nav: Providers
network: true
overview: 'OpenNode publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Charges API, Withdrawals API, Refunds API, and 8 more. Tagged areas include Bitcoin, Lightning Network, Payments, Payment Processing, and Cryptocurrency.


  The OpenNode catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenNode''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, GitHub presence, and 11 more developer resources.'
plans:
- name: Opennode Plans Pricing
  plan_count: 3
  slug: opennode-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Opennode Rate Limits
  slug: opennode-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: OpenNode API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: opennode-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 36.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 66.0
    developer_ergonomics: 22.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 56.6
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opennode/refs/heads/main/screenshots/opennode-2026-06-20T191018.png
security:
- kind: authentication
  name: Opennode Authentication
  slug: opennode-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Opennode Domain Security
  slug: opennode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opennode
tags:
- Bitcoin
- Lightning Network
- Payments
- Payment Processing
- Cryptocurrency
- Fintech
- Webhook
- Invoicing
- Payouts
- LNURL
website: https://opennode.com/
---
