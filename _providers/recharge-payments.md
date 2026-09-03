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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 36
  human_in_the_loop: 0
  name: Recharge Payments Agentic Access
  operation_count: 57
  slug: recharge-payments-agentic-access
  summary_line: 57 operations · 36 acting
api_count: 1
apis:
- baseURL: https://api.rechargeapps.com
  baseurl_source: declared
  description: Customer shipping addresses that group subscriptions and charges.
  name: Recharge Addresses API
  slug: recharge-payments-addresses-api
- baseURL: https://api.rechargeapps.com
  baseurl_source: declared
  description: Scheduled and processed charges against a customer's payment method.
  name: Recharge Charges API
  slug: recharge-payments-charges-api
- baseURL: https://api.rechargeapps.com
  baseurl_source: declared
  description: Customer records that own addresses, subscriptions, and payment methods.
  name: Recharge Customers API
  slug: recharge-payments-customers-api
- baseURL: https://api.rechargeapps.com
  baseurl_source: declared
  description: Discount codes applied to checkouts, addresses, and charges.
  name: Recharge Discounts API
  slug: recharge-payments-discounts-api
- baseURL: https://api.rechargeapps.com
  baseurl_source: declared
  description: One-time (non-recurring) products added to an upcoming charge.
  name: Recharge Onetimes API
  slug: recharge-payments-onetimes-api
- baseURL: https://api.rechargeapps.com
  baseurl_source: declared
  description: Orders generated from charges, plus one-time and recurring order management.
  name: Recharge Orders API
  slug: recharge-payments-orders-api
- baseURL: https://api.rechargeapps.com
  baseurl_source: declared
  description: Tokenized payment methods used to process charges.
  name: Recharge Payment Methods API
  slug: recharge-payments-payment-methods-api
- baseURL: https://api.rechargeapps.com
  baseurl_source: declared
  description: Products and subscription rules exposed to the storefront.
  name: Recharge Products API
  slug: recharge-payments-products-api
- baseURL: https://api.rechargeapps.com
  baseurl_source: declared
  description: Recurring subscription lines that drive future charges and orders.
  name: Recharge Subscriptions API
  slug: recharge-payments-subscriptions-api
- baseURL: https://api.rechargeapps.com
  baseurl_source: declared
  description: Webhook endpoints that receive event notifications from Recharge.
  name: Recharge Webhooks API
  slug: recharge-payments-webhooks-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Recharge Addresses API
  slug: open-recharge-payments-addresses-api
- collection_type: open
  name: Recharge Addresses Charges API
  slug: open-recharge-payments-charges-api
- collection_type: open
  name: Recharge Addresses Customers API
  slug: open-recharge-payments-customers-api
- collection_type: open
  name: Recharge Addresses Discounts API
  slug: open-recharge-payments-discounts-api
- collection_type: open
  name: Recharge Addresses Onetimes API
  slug: open-recharge-payments-onetimes-api
- collection_type: open
  name: Recharge Addresses Orders API
  slug: open-recharge-payments-orders-api
- collection_type: open
  name: Recharge Addresses Payment Methods API
  slug: open-recharge-payments-payment-methods-api
- collection_type: open
  name: Recharge Addresses Products API
  slug: open-recharge-payments-products-api
- collection_type: open
  name: Recharge Addresses Subscriptions API
  slug: open-recharge-payments-subscriptions-api
- collection_type: open
  name: Recharge Addresses Webhooks API
  slug: open-recharge-payments-webhooks-api
- collection_type: open
  name: Recharge API
  slug: open-recharge-payments
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/recharge-payments-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/recharge-payments-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recharge-payments-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/recharge-payments-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ReChargePayments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rechargepayments
- group: company
  title: ''
  type: Website
  url: https://getrecharge.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.rechargepayments.com
- group: commercial
  title: ''
  type: Plans
  url: plans/recharge-payments-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/recharge-payments-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/recharge-payments-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://getrecharge.com/blog/
created: '2026-07-10'
description: Recharge (Recharge Payments) is a subscription and recurring-billing platform for e-commerce, most widely used on Shopify. Its public REST API at https://api.rechargeapps.com lets developers manage the full subscription lifecycle - subscriptions, customers, addresses, charges, orders, products, payment methods, onetimes, discounts, and webhooks - programmatically. Requests are authenticated with a store API token in the X-Recharge-Access-Token header and versioned via the X-Recharge-Version header (supported versions 2021-11 and 2021-01). The API is resource-oriented JSON over HTTPS with cursor-based pagination and a leaky-bucket rate limiter.
finops:
- name: Recharge Payments Finops
  service_category: E-commerce and Subscription Billing
  slug: recharge-payments-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recharge-payments.png
layout: provider
modified: '2026-07-10'
name: Recharge
nav: Providers
network: true
overview: 'Recharge publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Charges API, Customers API, and 7 more. Tagged areas include Subscription, Recurring Billing, E-Commerce, Payments, and Shopify.


  Recharge''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Recharge Payments Plans Pricing
  plan_count: 3
  slug: recharge-payments-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Recharge Payments Rate Limits
  slug: recharge-payments-rate-limits
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/recharge-payments/refs/heads/main/screenshots/recharge-payments-2026-09-02T153123.png
security:
- kind: authentication
  name: Recharge Payments Authentication
  slug: recharge-payments-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Recharge Payments Domain Security
  slug: recharge-payments-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Recharge Payments Trust Center
  slug: recharge-payments-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: recharge-payments
tags:
- Subscription
- Recurring Billing
- E-Commerce
- Payments
- Shopify
- Retention
website: https://getrecharge.com
---
