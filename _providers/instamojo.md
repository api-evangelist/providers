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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Instamojo Agentic Access
  operation_count: 10
  slug: instamojo-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 1
apis:
- description: OAuth2 token generation for API access
  name: Instamojo Authentication API
  slug: instamojo-authentication-api
- description: Create and manage orders
  name: Instamojo Orders API
  slug: instamojo-orders-api
- description: Create and manage payment requests
  name: Instamojo Payment Requests API
  slug: instamojo-payment-requests-api
- description: Retrieve payment details
  name: Instamojo Payments API
  slug: instamojo-payments-api
- description: Create and retrieve refunds
  name: Instamojo Refunds API
  slug: instamojo-refunds-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Instamojo Payments Authentication API
  slug: open-instamojo-authentication-api
- collection_type: open
  name: Instamojo Payments Authentication Orders API
  slug: open-instamojo-orders-api
- collection_type: open
  name: Instamojo Payments Authentication Payment Requests API
  slug: open-instamojo-payment-requests-api
- collection_type: open
  name: Instamojo Authentication Payments API
  slug: open-instamojo-payments-api
- collection_type: open
  name: Instamojo Payments Authentication Refunds API
  slug: open-instamojo-refunds-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/instamojo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instamojo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/instamojo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.instamojo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.instamojo.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Instamojo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/instamojo
- group: company
  title: ''
  type: Blog
  url: https://www.instamojo.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.instamojo.com/pricing/
- group: other
  title: ''
  type: X
  url: https://twitter.com/instamojo
- group: commercial
  title: ''
  type: Plans
  url: plans/instamojo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/instamojo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/instamojo-finops.yml
created: '2026-06-13'
description: Indian digital payments and e-commerce platform with a REST API for payment requests, refunds, store products, order management, and mobile payment links. Trusted by over 1.2 million Indian small businesses.
examples:
- key_count: 4
  name: Create Payment Request
  slug: create-payment-request
- key_count: 4
  name: Create Refund
  slug: create-refund
- key_count: 4
  name: Generate Access Token
  slug: generate-access-token
finops:
- name: Instamojo Finops
  service_category: ''
  slug: instamojo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instamojo.png
json_schemas:
- name: Instamojo Payment Request
  property_count: 16
  slug: payment-request
- name: Instamojo Refund
  property_count: 8
  slug: refund
jsonld:
- class_count: 1
  name: Instamojo Context
  property_count: 29
  slug: instamojo-context
layout: provider
modified: '2026-06-13'
name: Instamojo
nav: Providers
network: true
overview: 'Instamojo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Orders API, Payment Requests API, and 2 more. Tagged areas include Payments, E-Commerce, India, Payment Gateway, and Payment Links.


  The Instamojo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Instamojo''s developer surface includes authentication, documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Instamojo Plans Pricing
  plan_count: 8
  slug: instamojo-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Instamojo Rate Limits
  slug: instamojo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Instamojo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: instamojo-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 43.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 64.4
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instamojo/refs/heads/main/screenshots/instamojo-2026-06-20T183413.png
security:
- kind: authentication
  name: Instamojo Authentication
  slug: instamojo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Instamojo Domain Security
  slug: instamojo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: instamojo
tags:
- Payments
- E-Commerce
- India
- Payment Gateway
- Payment Links
- Refunds
- Order
website: https://www.instamojo.com/
---
