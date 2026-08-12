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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 55
  human_in_the_loop: 0
  name: Octane Agentic Access
  operation_count: 101
  slug: octane-agentic-access
  summary_line: 101 operations · 55 acting
api_count: 17
apis:
- description: Administrative operations
  name: Octane Admin API
  slug: octane-admin-api
- description: Avalara tax integration
  name: Octane Avalara API
  slug: octane-avalara-api
- description: Manage vendor billing settings
  name: Octane Billing Settings API
  slug: octane-billing-settings-api
- description: Manage discount coupons
  name: Octane Coupons API
  slug: octane-coupons-api
- description: Manage customer credit grants and ledgers
  name: Octane Credits API
  slug: octane-credits-api
- description: End-customer portal operations
  name: Octane Customer Portal API
  slug: octane-customer-portal-api
- description: Manage customers and their subscriptions, billing, and settings
  name: Octane Customers API
  slug: octane-customers-api
- description: Manage product features
  name: Octane Features API
  slug: octane-features-api
- description: Access and manage customer invoices
  name: Octane Invoices API
  slug: octane-invoices-api
- description: Real-time usage measurement retrieval
  name: Octane Live Measurements API
  slug: octane-live-measurements-api
- description: Submit usage measurements for customers
  name: Octane Measurements API
  slug: octane-measurements-api
- description: Manage usage meters that track events and aggregate data
  name: Octane Meters API
  slug: octane-meters-api
- description: Manage pricing plans with metered components and flat rates
  name: Octane Price Plans API
  slug: octane-price-plans-api
- description: Process customer refunds
  name: Octane Refunds API
  slug: octane-refunds-api
- description: Revenue recognition reporting
  name: Octane Revenue Recognition API
  slug: octane-revenue-recognition-api
- description: Manage customer subscriptions to price plans
  name: Octane Subscriptions API
  slug: octane-subscriptions-api
- description: Manage webhook endpoints
  name: Octane Webhooks API
  slug: octane-webhooks-api
artifact_total: 33
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/octane-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/octane-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/octane-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.getoctane.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getoctane.io
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/getoctane
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getoctane
- group: other
  title: ''
  type: X
  url: https://twitter.com/getoctaneio
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getoctane.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.getoctane.io/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/octane-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/octane-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/octane-finops.yml
created: '2026-06-13'
description: Usage-based pricing and monetization platform with a REST API for managing meters, pricing plans, customer entitlements, and real-time usage tracking for SaaS products. Octane enables infrastructure and SaaS companies to implement flexible pay-as-you-go billing similar to Snowflake and AWS, with support for counters, metered components, flat-rate schemes, discounts, trials, and add-ons.
examples:
- key_count: 6
  name: Octane Create Customer Example
  slug: octane-create-customer-example
- key_count: 12
  name: Octane Create Meter Example
  slug: octane-create-meter-example
- key_count: 9
  name: Octane Create Price Plan Example
  slug: octane-create-price-plan-example
- key_count: 6
  name: Octane Send Measurement Example
  slug: octane-send-measurement-example
finops:
- name: Octane Finops
  service_category: ''
  slug: octane-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/octane.png
json_schemas:
- name: Customer
  property_count: 6
  slug: octane-customer
- name: Measurement
  property_count: 8
  slug: octane-measurement
- name: Meter
  property_count: 13
  slug: octane-meter
- name: PricePlan
  property_count: 16
  slug: octane-price-plan
jsonld:
- class_count: 20
  name: Octane Context
  property_count: 101
  slug: octane-context
layout: provider
modified: '2026-06-13'
name: Octane
nav: Providers
network: true
overview: 'Octane publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Avalara API, Billing Settings API, and 14 more. Tagged areas include Usage-Based Billing, Metered Billing, Pricing Plans, SaaS Monetization, and FinTech.


  The Octane catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Octane''s developer surface includes authentication, documentation, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Octane Plans Pricing
  plan_count: 1
  slug: octane-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 1
  name: Octane Rate Limits
  slug: octane-rate-limits
rules:
- name: Octane API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: octane-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.7
  delta: -0.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/octane/refs/heads/main/screenshots/octane-2026-06-20T190608.png
security:
- kind: authentication
  name: Octane Authentication
  slug: octane-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Octane Domain Security
  slug: octane-domain-security
  summary_line: TLSv1.3
slug: octane
tags:
- Usage-Based Billing
- Metered Billing
- Pricing Plans
- SaaS Monetization
- FinTech
- Payments
- Usage Tracking
- Meters
- Entitlements
website: https://www.getoctane.io
---
