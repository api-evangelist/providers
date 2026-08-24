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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Payflex Agentic Access
  operation_count: 5
  slug: payflex-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 4
apis:
- description: OAuth2 client credentials token endpoint
  name: Payflex Authentication API
  slug: payflex-authentication-api
- description: Retrieve merchant payment limits and settings
  name: Payflex Configuration API
  slug: payflex-configuration-api
- description: Create and manage BNPL payment orders
  name: Payflex Orders API
  slug: payflex-orders-api
- description: Initiate full or partial refunds on completed orders
  name: Payflex Refunds API
  slug: payflex-refunds-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Payflex Merchant Authentication API
  slug: open-payflex-authentication-api
- collection_type: open
  name: Payflex Merchant Authentication Configuration API
  slug: open-payflex-configuration-api
- collection_type: open
  name: Payflex Merchant Authentication Orders API
  slug: open-payflex-orders-api
- collection_type: open
  name: Payflex Merchant Authentication Refunds API
  slug: open-payflex-refunds-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/payflex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payflex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/payflex-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://payflex.co.za/
- group: start
  title: ''
  type: MerchantPortal
  url: https://merchant.payflex.co.za/login
- group: other
  title: ''
  type: MerchantHub
  url: https://payflex.co.za/merchant/
- group: operate
  title: ''
  type: Support
  url: https://payflex.co.za/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://payflex.co.za/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://payflex.co.za/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://payflex.co.za/merchant-hub/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/PayFlexSA
- group: build
  title: ''
  type: WooCommercePlugin
  url: https://wordpress.org/plugins/payflex-payment-gateway/
- group: build
  title: ''
  type: WooCommercePluginSource
  url: https://github.com/PayFlexSA/payflex-woocommerce-plugin
- group: other
  title: ''
  type: MagentoModule
  url: https://github.com/PayFlexSA/payflex-magento-2-4-module
- group: build
  title: ''
  type: OpenCartExtension
  url: https://github.com/PayFlexSA/payflex-opencart-4-extension
- group: other
  title: ''
  type: PrestaShopModule
  url: https://github.com/PayFlexSA/payflex-prestashop-8-module
created: '2026-06-13'
description: Payflex is a South African Buy Now Pay Later (BNPL) platform that enables merchants to offer interest-free installment payment options to consumers. Shoppers can split purchases into up to four interest-free payments over six weeks, with the first payment made upfront. Payflex pays merchants the full purchase amount upfront (less a commission) and assumes all credit and fraud risk. The REST API supports hosted and embedded checkout flows, order lifecycle management, refunds, and merchant configuration retrieval.
examples:
- key_count: 2
  name: Configuration Response
  slug: configuration-response
- key_count: 11
  name: Create Order Request
  slug: create-order-request
- key_count: 4
  name: Create Order Response
  slug: create-order-response
- key_count: 5
  name: Order Status Response
  slug: order-status-response
- key_count: 4
  name: Refund Request
  slug: refund-request
- key_count: 4
  name: Token Request
  slug: token-request
- key_count: 3
  name: Token Response
  slug: token-response
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://payflex.co.za/wp-content/uploads/2021/06/payflex-logo.png
json_schemas:
- name: Configuration Response
  property_count: 2
  slug: configuration-response
- name: Create Order Request
  property_count: 11
  slug: create-order-request
- name: Create Order Response
  property_count: 4
  slug: create-order-response
- name: Order Status Response
  property_count: 5
  slug: order-status-response
- name: Refund Request
  property_count: 4
  slug: refund-request
jsonld:
- class_count: 8
  name: context Context
  property_count: 43
  slug: context
layout: provider
modified: '2026-06-13'
name: Payflex
nav: Providers
network: true
overview: 'Payflex publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Configuration API, Orders API, and 1 more. Tagged areas include BNPL, Buy Now Pay Later, Payments, Installments, and South Africa.


  The Payflex catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Payflex''s developer surface includes authentication, support, engineering blog, GitHub presence, and 12 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 5
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Payflex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: payflex-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.2
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 69.1
    developer_ergonomics: 13.1
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payflex/refs/heads/main/screenshots/payflex-2026-06-20T191458.png
security:
- kind: authentication
  name: Payflex Authentication
  slug: payflex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Payflex Domain Security
  slug: payflex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: payflex
tags:
- BNPL
- Buy Now Pay Later
- Payments
- Installments
- South Africa
- Fintech
- E-Commerce
website: https://payflex.co.za/
---
