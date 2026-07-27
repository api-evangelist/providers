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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Runa Agentic Access
  operation_count: 10
  slug: runa-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 4
apis:
- description: Retrieve account balance by currency.
  name: Runa Balance API
  slug: runa-balance-api
- description: Create, retrieve, list, and estimate digital reward orders.
  name: Runa Orders API
  slug: runa-orders-api
- description: Browse the Runa product catalog by name, category, or country.
  name: Runa Products API
  slug: runa-products-api
- description: Utility endpoints for connectivity testing.
  name: Runa Utilities API
  slug: runa-utilities-api
artifact_total: 19
collections:
- collection_type: open
  name: Runa Payouts API
  slug: open-runa-payouts-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/runa-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/runa-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/runa-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/runapayouts
- group: start
  title: ''
  type: Portal
  url: https://developer.runa.io/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.runa.io/docs/getting-an-api-key
- group: start
  title: ''
  type: Signup
  url: https://app.runa.io/
- group: start
  title: ''
  type: Sandbox
  url: https://developer.runa.io/docs/playground
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runa.io/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runa.io/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://runa.io/blog/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.runa.io/llms.txt
created: '2025-02-08'
description: Runa is a global digital payouts platform that enables businesses to automate digital reward and gift card distribution through a single API. The platform provides access to over 5,000 gift cards and payout options across 190+ countries, supporting B2C payments, employee rewards, customer incentives, and loyalty programs. The Runa API supports synchronous and asynchronous order modes, balance management, product catalog browsing, and webhook-based event notifications for order completions.
examples:
- key_count: 2
  name: Runa Create Order Example
  slug: runa-create-order-example
- key_count: 2
  name: Runa Get Balance Example
  slug: runa-get-balance-example
finops:
- name: Runa Finops
  service_category: API
  slug: runa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/runa.png
json_schemas:
- name: Runa Order
  property_count: 6
  slug: runa-order
json_structures:
- name: Runa Structure
  property_count: 0
  slug: runa-structure
jsonld:
- class_count: 5
  name: Runa Context
  property_count: 14
  slug: runa-context
layout: provider
modified: '2026-05-19'
name: Runa
nav: Providers
network: true
overview: 'Runa publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Balance API, Orders API, Products API, and 1 more. Tagged areas include Gift Cards, Rewards, Payments, Incentives, and Payouts.


  The Runa catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Runa''s developer surface includes authentication, developer portal, signup flow, sandbox, engineering blog, and 8 more developer resources.'
plans:
- name: Runa Plans Pricing
  plan_count: 3
  slug: runa-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 5
  name: Runa Rate Limits
  slug: runa-rate-limits
rules:
- name: Runa API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: runa-jsonschema-spectral-rules
- name: Runa API Rules
  rule_count: 18
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 15
  slug: runa-spectral-rules
score:
  band: strong
  composite: 61.2
  delta: 2.8
  facets:
    commercial_clarity: 68.4
    contract_quality: 72.6
    developer_ergonomics: 28.3
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 31.6
  previous_composite: 58.4
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/runa/refs/heads/main/screenshots/runa-2026-06-20T193249.png
security:
- kind: authentication
  name: Runa Authentication
  slug: runa-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Runa Domain Security
  slug: runa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Runa Trust Center
  slug: runa-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: runa
tags:
- Gift Cards
- Rewards
- Payments
- Incentives
- Payouts
website: https://developer.runa.io/
---
