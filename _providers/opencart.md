---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Opencart Agentic Access
  operation_count: 16
  slug: opencart-agentic-access
  summary_line: 16 operations · 12 acting
api_count: 10
apis:
- description: Affiliate session management
  name: OpenCart Affiliates API
  slug: opencart-affiliates-api
- description: API login and session token management
  name: OpenCart Authentication API
  slug: opencart-authentication-api
- description: Shopping cart product management
  name: OpenCart Cart API
  slug: opencart-cart-api
- description: Customer session and profile management
  name: OpenCart Customer API
  slug: opencart-customer-api
- description: Order creation, confirmation, and history
  name: OpenCart Orders API
  slug: opencart-orders-api
- description: Billing address management
  name: OpenCart Payment Address API
  slug: opencart-payment-address-api
- description: Available payment method retrieval and selection
  name: OpenCart Payment Methods API
  slug: opencart-payment-methods-api
- description: Shipping address management
  name: OpenCart Shipping Address API
  slug: opencart-shipping-address-api
- description: Available shipping method retrieval and selection
  name: OpenCart Shipping Methods API
  slug: opencart-shipping-methods-api
- description: Subscription order management
  name: OpenCart Subscriptions API
  slug: opencart-subscriptions-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenCart REST Affiliates API
  slug: open-opencart-affiliates-api
- collection_type: open
  name: OpenCart REST Affiliates Authentication API
  slug: open-opencart-authentication-api
- collection_type: open
  name: OpenCart REST Affiliates Cart API
  slug: open-opencart-cart-api
- collection_type: open
  name: OpenCart REST Affiliates Customer API
  slug: open-opencart-customer-api
- collection_type: open
  name: OpenCart REST Affiliates Orders API
  slug: open-opencart-orders-api
- collection_type: open
  name: OpenCart REST Affiliates Payment Address API
  slug: open-opencart-payment-address-api
- collection_type: open
  name: OpenCart REST Affiliates Payment Methods API
  slug: open-opencart-payment-methods-api
- collection_type: open
  name: OpenCart REST Affiliates Shipping Address API
  slug: open-opencart-shipping-address-api
- collection_type: open
  name: OpenCart REST Affiliates Shipping Methods API
  slug: open-opencart-shipping-methods-api
- collection_type: open
  name: OpenCart REST Affiliates Subscriptions API
  slug: open-opencart-subscriptions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opencart-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opencart-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opencart-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.opencart.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opencart.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/opencart
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/5224021/
- group: company
  title: ''
  type: Blog
  url: https://www.opencart.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.opencart.com/index.php?route=cms/download
- group: other
  title: ''
  type: X
  url: https://twitter.com/opencart
- group: operate
  title: ''
  type: Forums
  url: https://forum.opencart.com
- group: other
  title: ''
  type: Marketplace
  url: https://www.opencart.com/index.php?route=marketplace/extension
- group: commercial
  title: ''
  type: Plans
  url: plans/opencart-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opencart-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opencart-finops.yml
created: 2026-06-13
description: OpenCart is a free, open-source eCommerce platform providing a REST API for managing products, categories, orders, customers, returns, and store configuration in self-hosted environments. Built on PHP and MySQL, OpenCart powers over 470,000 online stores worldwide and offers token-based API authentication with IP-allowlist security controls.
examples:
- key_count: 4
  name: Add Product To Cart Request
  slug: add-product-to-cart-request
- key_count: 1
  name: Add Product To Cart Response
  slug: add-product-to-cart-response
- key_count: 4
  name: Confirm Order Response
  slug: confirm-order-response
- key_count: 2
  name: Login Request
  slug: login-request
- key_count: 2
  name: Login Response
  slug: login-response
- key_count: 8
  name: Set Customer Request
  slug: set-customer-request
finops:
- name: Opencart Finops
  service_category: ''
  slug: opencart-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opencart.png
json_schemas:
- name: Address
  property_count: 17
  slug: address
- name: CartProduct
  property_count: 10
  slug: cart-product
- name: Order
  property_count: 4
  slug: order
jsonld:
- class_count: 15
  name: Opencart Context
  property_count: 0
  slug: opencart-context
layout: provider
modified: 2026-06-13
name: OpenCart
nav: Providers
network: true
overview: 'OpenCart publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Affiliates API, Authentication API, Cart API, and 7 more. Tagged areas include eCommerce, Shopping Cart, Open Source, Self-Hosted, and Products.


  The OpenCart catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenCart''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Opencart Plans Pricing
  plan_count: 2
  slug: opencart-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Opencart Rate Limits
  slug: opencart-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: OpenCart API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: opencart-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.8
  delta: -6.3
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 59.4
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/opencart/refs/heads/main/screenshots/opencart-2026-06-20T190918.png
security:
- kind: authentication
  name: Opencart Authentication
  slug: opencart-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Opencart Domain Security
  slug: opencart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opencart
tags:
- eCommerce
- Shopping Cart
- Open Source
- Self-Hosted
- Products
- Orders
- Customers
- Categories
website: https://www.opencart.com
---
