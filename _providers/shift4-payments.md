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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Shift4 Payments Agentic Access
  operation_count: 54
  slug: shift4-payments-agentic-access
  summary_line: 54 operations · 26 acting
api_count: 20
apis:
- description: Shift4 Checkout provides a drop-in, frictionless checkout overlay that can be added to a website with copy-paste integration for fast and secure payment acceptance.
  name: Shift4 Checkout
  slug: shift4-checkout
- description: The Shift4 JavaScript library provides secure, customizable HTML/CSS components for building on-page payment forms and multi-step checkout pages.
  name: Shift4 JavaScript Library
  slug: shift4-js
- description: Manage blacklist rules for fraud prevention.
  name: Shift4 Payments Blacklist API
  slug: shift4-payments-blacklist-api
- description: Manage saved cards on customer records.
  name: Shift4 Payments Cards API
  slug: shift4-payments-cards-api
- description: Create, retrieve, update, capture, and list charges.
  name: Shift4 Payments Charges API
  slug: shift4-payments-charges-api
- description: Create hosted checkout sessions for drop-in payment acceptance.
  name: Shift4 Payments Checkout Sessions API
  slug: shift4-payments-checkout-sessions-api
- description: Send funds (credits) to recipients.
  name: Shift4 Payments Credits API
  slug: shift4-payments-credits-api
- description: Create, retrieve, update, delete, and list customers.
  name: Shift4 Payments Customers API
  slug: shift4-payments-customers-api
- description: Retrieve and respond to chargeback disputes.
  name: Shift4 Payments Disputes API
  slug: shift4-payments-disputes-api
- description: Retrieve event records that drive webhooks.
  name: Shift4 Payments Events API
  slug: shift4-payments-events-api
- description: Upload files such as dispute evidence.
  name: Shift4 Payments File Uploads API
  slug: shift4-payments-file-uploads-api
- description: Retrieve early-warning fraud notifications.
  name: Shift4 Payments Fraud Warnings API
  slug: shift4-payments-fraud-warnings-api
- description: Create and retrieve hosted payment links.
  name: Shift4 Payments Payment Links API
  slug: shift4-payments-payment-links-api
- description: Create and retrieve alternative payment methods (Apple Pay, Google Pay, 3D Secure, etc.).
  name: Shift4 Payments Payment Methods API
  slug: shift4-payments-payment-methods-api
- description: Retrieve scheduled and historical payouts to bank accounts.
  name: Shift4 Payments Payouts API
  slug: shift4-payments-payouts-api
- description: Define recurring billing plans used by subscriptions.
  name: Shift4 Payments Plans API
  slug: shift4-payments-plans-api
- description: Refund charges and manage refund records.
  name: Shift4 Payments Refunds API
  slug: shift4-payments-refunds-api
- description: Create and manage recurring subscriptions for customers.
  name: Shift4 Payments Subscriptions API
  slug: shift4-payments-subscriptions-api
- description: Tokenize card data for safe transmission.
  name: Shift4 Payments Tokens API
  slug: shift4-payments-tokens-api
- description: Register and manage webhook endpoints.
  name: Shift4 Payments Webhook Endpoints API
  slug: shift4-payments-webhook-endpoints-api
artifact_total: 49
collections:
- collection_type: open
  name: Shift4 Payments API
  slug: open-shift4-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shift4-payments-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shift4-payments-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shift4-payments-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shift4
- group: company
  title: ''
  type: Website
  url: https://www.shift4.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.shift4.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.shift4.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev.shift4.com/docs/api
- group: build
  title: ''
  type: CodeExamples
  url: https://dev.shift4.com/examples
- group: operate
  title: ''
  type: Support
  url: https://dev.shift4.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shift4developer
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/shift4-payments/main/vocabulary/shift4-payments-vocabulary.yml
created: '2026-05-04'
description: Shift4 Payments is a leading integrated payments and commerce technology provider and a Fortune 1000 company. The company processes payments for hospitality, retail, gaming, sports, e-commerce, and other verticals, offering checkout flows, custom payment forms, hosted UI components, and a developer API that supports global payment methods, subscriptions, fraud prevention, and 3D Secure. Developers integrate Shift4 through a REST API, JavaScript library, webhooks, and a sandbox testing environment.
examples:
- key_count: 3
  name: Shift4 Api Create Charge Example
  slug: shift4-api-create-charge-example
- key_count: 3
  name: Shift4 Api Create Checkout Session Example
  slug: shift4-api-create-checkout-session-example
- key_count: 3
  name: Shift4 Api Create Customer Example
  slug: shift4-api-create-customer-example
- key_count: 3
  name: Shift4 Api Create Refund Example
  slug: shift4-api-create-refund-example
- key_count: 3
  name: Shift4 Api Create Subscription Example
  slug: shift4-api-create-subscription-example
- key_count: 3
  name: Shift4 Api Create Token Example
  slug: shift4-api-create-token-example
- key_count: 3
  name: Shift4 Api List Events Example
  slug: shift4-api-list-events-example
finops:
- name: Shift4 Payments Finops
  service_category: API
  slug: shift4-payments-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shift4-payments.png
json_schemas:
- name: Shift4 Card
  property_count: 15
  slug: shift4-card
- name: Shift4 Charge
  property_count: 19
  slug: shift4-charge
- name: Shift4 Checkout Session
  property_count: 18
  slug: shift4-checkout-session
- name: Shift4 Customer
  property_count: 8
  slug: shift4-customer
- name: Shift4 Event
  property_count: 5
  slug: shift4-event
- name: Shift4 Plan
  property_count: 13
  slug: shift4-plan
- name: Shift4 Refund
  property_count: 8
  slug: shift4-refund
- name: Shift4 Subscription
  property_count: 18
  slug: shift4-subscription
- name: Shift4 Token
  property_count: 11
  slug: shift4-token
json_structures:
- name: Shift4 Charge Structure
  property_count: 19
  slug: shift4-charge-structure
- name: Shift4 Customer Structure
  property_count: 8
  slug: shift4-customer-structure
- name: Shift4 Subscription Structure
  property_count: 17
  slug: shift4-subscription-structure
jsonld:
- class_count: 0
  name: Shift4 Payments Context
  property_count: 9
  slug: shift4-payments-context
layout: provider
modified: '2026-05-19'
name: Shift4 Payments
nav: Providers
network: true
overview: 'Shift4 Payments publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Blacklist API, Cards API, Charges API, and 15 more. Tagged areas include Payments, Fintech, Commerce, and Checkout.


  The Shift4 Payments catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Shift4 Payments'' developer surface includes authentication, documentation, API reference, code examples, support, and 7 more developer resources.'
plans:
- name: Shift4 Payments Plans Pricing
  plan_count: 1
  slug: shift4-payments-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 2
  name: Shift4 Payments Rate Limits
  slug: shift4-payments-rate-limits
rules:
- name: Shift4 Payments API Rules
  rule_count: 15
  severity_counts:
    error: 3
    hint: 3
    info: 0
    warn: 9
  slug: shift4-api-rules
- name: Shift4 Payments API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: shift4-payments-jsonschema-spectral-rules
score:
  band: thin
  composite: 41.7
  delta: -4.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.4
    developer_ergonomics: 39.1
    discoverability: 50.0
    governance: 52.1
    operational_transparency: 26.3
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shift4-payments/refs/heads/main/screenshots/shift4-payments-2026-06-20T193806.png
security:
- kind: authentication
  name: Shift4 Payments Authentication
  slug: shift4-payments-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shift4 Payments Domain Security
  slug: shift4-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shift4-payments
tags:
- Payments
- Fintech
- Commerce
- Checkout
website: https://www.shift4.com
---
