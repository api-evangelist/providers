---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
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
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 55
  human_in_the_loop: 0
  name: Octane Agentic Access
  operation_count: 101
  slug: octane-agentic-access
  summary_line: 101 operations · 55 acting
api_count: 1
apis:
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Administrative operations
  name: Octane Admin API
  slug: octane-admin-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Avalara tax integration
  name: Octane Avalara API
  slug: octane-avalara-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Manage vendor billing settings
  name: Octane Billing Settings API
  slug: octane-billing-settings-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Manage discount coupons
  name: Octane Coupons API
  slug: octane-coupons-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Manage customer credit grants and ledgers
  name: Octane Credits API
  slug: octane-credits-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: End-customer portal operations
  name: Octane Customer Portal API
  slug: octane-customer-portal-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Manage customers and their subscriptions, billing, and settings
  name: Octane Customers API
  slug: octane-customers-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Manage product features
  name: Octane Features API
  slug: octane-features-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Access and manage customer invoices
  name: Octane Invoices API
  slug: octane-invoices-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Real-time usage measurement retrieval
  name: Octane Live Measurements API
  slug: octane-live-measurements-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Submit usage measurements for customers
  name: Octane Measurements API
  slug: octane-measurements-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Manage usage meters that track events and aggregate data
  name: Octane Meters API
  slug: octane-meters-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Manage pricing plans with metered components and flat rates
  name: Octane Price Plans API
  slug: octane-price-plans-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Process customer refunds
  name: Octane Refunds API
  slug: octane-refunds-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Revenue recognition reporting
  name: Octane Revenue Recognition API
  slug: octane-revenue-recognition-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Manage customer subscriptions to price plans
  name: Octane Subscriptions API
  slug: octane-subscriptions-api
- baseURL: https://api.getoctane.io
  baseurl_source: declared
  description: Manage webhook endpoints
  name: Octane Webhooks API
  slug: octane-webhooks-api
artifact_total: 51
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Octane REST Admin API
  slug: open-octane-admin-api
- collection_type: open
  name: Octane REST Admin Avalara API
  slug: open-octane-avalara-api
- collection_type: open
  name: Octane REST Admin Billing Settings API
  slug: open-octane-billing-settings-api
- collection_type: open
  name: Octane REST Admin Coupons API
  slug: open-octane-coupons-api
- collection_type: open
  name: Octane REST Admin Credits API
  slug: open-octane-credits-api
- collection_type: open
  name: Octane REST Admin Customer Portal API
  slug: open-octane-customer-portal-api
- collection_type: open
  name: Octane REST Admin Customers API
  slug: open-octane-customers-api
- collection_type: open
  name: Octane REST Admin Features API
  slug: open-octane-features-api
- collection_type: open
  name: Octane REST Admin Invoices API
  slug: open-octane-invoices-api
- collection_type: open
  name: Octane REST Admin Live Measurements API
  slug: open-octane-live-measurements-api
- collection_type: open
  name: Octane REST Admin Measurements API
  slug: open-octane-measurements-api
- collection_type: open
  name: Octane REST Admin Meters API
  slug: open-octane-meters-api
- collection_type: open
  name: Octane REST Admin Price Plans API
  slug: open-octane-price-plans-api
- collection_type: open
  name: Octane REST Admin Refunds API
  slug: open-octane-refunds-api
- collection_type: open
  name: Octane REST Admin Revenue Recognition API
  slug: open-octane-revenue-recognition-api
- collection_type: open
  name: Octane REST Admin Subscriptions API
  slug: open-octane-subscriptions-api
- collection_type: open
  name: Octane REST Admin Webhooks API
  slug: open-octane-webhooks-api
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
overview: 'Octane publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Avalara API, Billing Settings API, and 14 more. Tagged areas include Usage-Based Billing, Metered Billing, Pricing Plans, SaaS Monetization, and Fintech.


  The Octane catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Octane''s developer surface includes authentication, documentation, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Octane Plans Pricing
  plan_count: 1
  slug: octane-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Octane Rate Limits
  slug: octane-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Octane API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: octane-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 70.3
    catalog_earned_first_party: 0.0
    catalog_gap: 44.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 59.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Fintech
- Payments
- Usage Tracking
- Meters
- Entitlements
website: https://www.getoctane.io
---
