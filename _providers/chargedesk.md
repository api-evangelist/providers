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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Chargedesk Agentic Access
  operation_count: 31
  slug: chargedesk-agentic-access
  summary_line: 31 operations · 19 acting
api_count: 7
apis:
- description: RESTful API for managing charges, customers, subscriptions, products, and webhooks across multiple payment gateways. Supports creating and capturing charges, processing refunds, cancelling subscriptio
  name: ChargeDesk REST API
  slug: chargedesk-rest-api
- description: Manage charge records across payment gateways
  name: ChargeDesk Charges API
  slug: chargedesk-charges-api
- description: Manage customer billing records
  name: ChargeDesk Customers API
  slug: chargedesk-customers-api
- description: Live payment processing operations
  name: ChargeDesk Gateway API
  slug: chargedesk-gateway-api
- description: Manage products and pricing plans
  name: ChargeDesk Products API
  slug: chargedesk-products-api
- description: Manage recurring subscriptions
  name: ChargeDesk Subscriptions API
  slug: chargedesk-subscriptions-api
- description: Manage webhook configurations
  name: ChargeDesk Webhooks API
  slug: chargedesk-webhooks-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ChargeDesk REST Charges API
  slug: open-chargedesk-charges-api
- collection_type: open
  name: ChargeDesk REST Charges Customers API
  slug: open-chargedesk-customers-api
- collection_type: open
  name: ChargeDesk REST Charges Gateway API
  slug: open-chargedesk-gateway-api
- collection_type: open
  name: ChargeDesk REST Charges Products API
  slug: open-chargedesk-products-api
- collection_type: open
  name: ChargeDesk REST Charges Subscriptions API
  slug: open-chargedesk-subscriptions-api
- collection_type: open
  name: ChargeDesk REST Charges Webhooks API
  slug: open-chargedesk-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chargedesk-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chargedesk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chargedesk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chargedesk-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://chargedesk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://chargedesk.com/api-docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ChargeDesk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chargedesk
- group: company
  title: ''
  type: Blog
  url: https://chargedesk.com/help/general/whats-new
- group: commercial
  title: ''
  type: Pricing
  url: https://chargedesk.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chargedesk.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/chargedesk
- group: commercial
  title: ''
  type: Plans
  url: plans/chargedesk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chargedesk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chargedesk-finops.yml
created: '2026-06-13'
description: ChargeDesk is a payment management portal providing a REST API for creating and managing charges, subscriptions, refunds, and customer billing across Stripe, Braintree, PayPal, Authorize.Net, WooCommerce, Shopify, Square, GoCardless, and 14+ other payment gateways. It integrates directly with helpdesk platforms including Zendesk, Freshdesk, Intercom, HubSpot, Help Scout, and Front, enabling support teams to handle billing operations without leaving their customer support workflow.
examples:
- key_count: 4
  name: Create Charge
  slug: create-charge
- key_count: 4
  name: Gateway Create Charge
  slug: gateway-create-charge
- key_count: 4
  name: Gateway Create Subscription
  slug: gateway-create-subscription
- key_count: 4
  name: Gateway Refund Charge
  slug: gateway-refund-charge
- key_count: 4
  name: Gateway Request Payment
  slug: gateway-request-payment
- key_count: 4
  name: List Charges
  slug: list-charges
finops:
- name: Chargedesk Finops
  service_category: ''
  slug: chargedesk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chargedesk.png
json_schemas:
- name: Charge
  property_count: 16
  slug: charge
- name: Customer
  property_count: 17
  slug: customer
- name: Product
  property_count: 13
  slug: product
- name: Subscription
  property_count: 16
  slug: subscription
jsonld:
- class_count: 2
  name: Chargedesk Context
  property_count: 52
  slug: chargedesk-context
layout: provider
modified: '2026-06-13'
name: ChargeDesk
nav: Providers
network: true
overview: 'ChargeDesk publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Charges API, Customers API, Gateway API, and 3 more. Tagged areas include Payments, Billing, Subscriptions, Charges, and Refunds.


  The ChargeDesk catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ChargeDesk''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Chargedesk Plans Pricing
  plan_count: 4
  slug: chargedesk-plans-pricing
random_paper: 147
rate_limits:
- limit_count: 0
  name: Chargedesk Rate Limits
  slug: chargedesk-rate-limits
rules:
- name: ChargeDesk API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: chargedesk-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 62.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 45.5
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
    score: 35.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chargedesk/refs/heads/main/screenshots/chargedesk-2026-06-20T174221.png
security:
- kind: authentication
  name: Chargedesk Authentication
  slug: chargedesk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Chargedesk Domain Security
  slug: chargedesk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Chargedesk Vulnerability Disclosure
  slug: chargedesk-vulnerability-disclosure
  summary_line: disclosure policy published
slug: chargedesk
tags:
- Payments
- Billing
- Subscriptions
- Charges
- Refunds
- Customer Management
- Payment Gateway
- Helpdesk Integration
- REST API
website: https://chargedesk.com/
---
