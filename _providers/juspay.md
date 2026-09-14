---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Juspay Agentic Access
  operation_count: 8
  slug: juspay-agentic-access
  summary_line: 8 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.juspay.in
  baseurl_source: declared
  description: Create and retrieve customers.
  name: Juspay Customers API
  slug: juspay-customers-api
- baseURL: https://api.juspay.in
  baseurl_source: declared
  description: Create orders and read order status.
  name: Juspay Orders API
  slug: juspay-orders-api
- baseURL: https://api.juspay.in
  baseurl_source: declared
  description: Refund a charged order.
  name: Juspay Refunds API
  slug: juspay-refunds-api
- baseURL: https://api.juspay.in
  baseurl_source: declared
  description: Create a payment session for the Hyper Checkout / HyperSDK.
  name: Juspay Session API
  slug: juspay-session-api
- baseURL: https://api.juspay.in
  baseurl_source: declared
  description: Server-to-server transaction processing against an order.
  name: Juspay Transactions API
  slug: juspay-transactions-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Juspay Express Checkout Customers API
  slug: open-juspay-customers-api
- collection_type: open
  name: Juspay Express Checkout Customers Orders API
  slug: open-juspay-orders-api
- collection_type: open
  name: Juspay Express Checkout Customers Refunds API
  slug: open-juspay-refunds-api
- collection_type: open
  name: Juspay Express Checkout Customers Session API
  slug: open-juspay-session-api
- collection_type: open
  name: Juspay Express Checkout Customers Transactions API
  slug: open-juspay-transactions-api
- collection_type: open
  name: Juspay Express Checkout API
  slug: open-juspay
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/juspay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/juspay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/juspay-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/juspay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/juspay-technologies
- group: company
  title: ''
  type: Website
  url: https://juspay.io/in
- group: docs
  title: ''
  type: Documentation
  url: https://juspay.io/in/docs/api-reference/docs/express-checkout/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/juspay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/juspay-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/juspay-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://juspay.io/in/blog
created: '2026-07-12'
description: Juspay is an Indian payments orchestration and checkout platform that routes transactions across payment gateways, aggregators, UPI, cards, wallets, and netbanking for merchants, banks, and card networks. Its server-to-server Express Checkout / PG REST APIs create and track orders, process transactions, issue refunds, and manage customers, and pair with the HyperSDK / Hyper Checkout drop-in checkout. APIs authenticate with an API key over HTTP Basic plus a merchant ID header, against a sandbox and a production host.
finops:
- name: Juspay Finops
  service_category: Payments and Financial Infrastructure
  slug: juspay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/juspay.png
layout: provider
modified: '2026-07-12'
name: Juspay
nav: Providers
network: true
overview: 'Juspay publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Orders API, Refunds API, and 2 more. Tagged areas include Payments, Payment Orchestration, Checkout, India, and UPI.


  Juspay''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Juspay Plans Pricing
  plan_count: 3
  slug: juspay-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Juspay Rate Limits
  slug: juspay-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/juspay/refs/heads/main/screenshots/juspay-2026-07-25T223337.png
security:
- kind: authentication
  name: Juspay Authentication
  slug: juspay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Juspay Domain Security
  slug: juspay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: juspay
tags:
- Payments
- Payment Orchestration
- Checkout
- India
- UPI
- Cards
- Payment Gateway
- Fintech
- HyperSDK
- Financial Infrastructure
website: https://juspay.io/in
---
