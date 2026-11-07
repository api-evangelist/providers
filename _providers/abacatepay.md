---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Abacatepay Agentic Access
  operation_count: 12
  slug: abacatepay-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.abacatepay.com/v1
  baseurl_source: declared
  description: Outbound webhook event notifications (billing.created, billing.paid, billing.refunded, billing.failed, subscription.created, subscription.canceled) delivered with a webhookSecret query string and HMAC
  name: AbacatePay Webhooks
  slug: abacatepay-webhooks-api
- baseURL: https://api.abacatepay.com/v1
  baseurl_source: declared
  description: Create and list billings (charges) with a shareable checkout URL.
  name: AbacatePay Billing API
  slug: abacatepay-billing-api
- baseURL: https://api.abacatepay.com/v1
  baseurl_source: declared
  description: Create and list discount coupons.
  name: AbacatePay Coupon API
  slug: abacatepay-coupon-api
- baseURL: https://api.abacatepay.com/v1
  baseurl_source: declared
  description: Create and list customers (clients).
  name: AbacatePay Customer API
  slug: abacatepay-customer-api
- baseURL: https://api.abacatepay.com/v1
  baseurl_source: declared
  description: Create, check, and simulate dynamic Pix QR Code payments.
  name: AbacatePay Pix QR Code API
  slug: abacatepay-pix-qr-code-api
- baseURL: https://api.abacatepay.com/v1
  baseurl_source: declared
  description: Create, retrieve, and list withdrawals (payouts) to a Pix key.
  name: AbacatePay Withdraw API
  slug: abacatepay-withdraw-api
artifact_total: 20
collections:
- collection_type: open
  name: AbacatePay Billing API
  slug: open-abacatepay-billing-api
- collection_type: open
  name: AbacatePay Billing Coupon API
  slug: open-abacatepay-coupon-api
- collection_type: open
  name: AbacatePay Billing Customer API
  slug: open-abacatepay-customer-api
- collection_type: open
  name: AbacatePay Billing Pix QR Code API
  slug: open-abacatepay-pix-qr-code-api
- collection_type: open
  name: AbacatePay Billing Withdraw API
  slug: open-abacatepay-withdraw-api
- collection_type: open
  name: AbacatePay API
  slug: open-abacatepay
common:
- group: company
  title: ''
  type: Blog
  url: https://www.abacatepay.com/blog
- group: other
  href: https://artifacts.apis.io/abacatepay/capabilities/abacatepay-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/abacatepay-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/abacatepay/agentic-access/abacatepay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/abacatepay-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/abacatepay/security/abacatepay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abacatepay-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/abacatepay/authentication/abacatepay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/abacatepay-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AbacatePay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abacatepay
- group: company
  title: ''
  type: Website
  url: https://www.abacatepay.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.abacatepay.com
- group: commercial
  href: https://artifacts.apis.io/abacatepay/plans/abacatepay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/abacatepay-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/abacatepay/rate-limits/abacatepay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/abacatepay-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/abacatepay/finops/abacatepay-finops.yml
  title: ''
  type: FinOps
  url: finops/abacatepay-finops.yml
created: '2026-06-21'
description: AbacatePay is a Brazilian payment gateway built for developers and indie hackers, focused on instant Pix payments. Its REST API lets you create billings and charges, generate and check Pix QR Codes, manage customers and coupons, request withdrawals, and receive webhooks - charging a flat per-transaction Pix fee with funds available immediately.
finops:
- has_sources: true
  method: generated
  name: Abacatepay Finops
  primary_unit: ''
  service_category: Payment Processing
  slug: abacatepay-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/abacatepay.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.abacatepay.com over HTTP.
  name: AbacatePay MCP Server
  slug: abacatepay
modified: '2026-10-06'
name: AbacatePay
nav: Providers
network: true
overview: 'AbacatePay publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Webhooks, Billing API, Coupon API, and 3 more. Tagged areas include Payments, Pix, Brazil, Fintech, and Developers.


  The AbacatePay catalog on APIs.io includes 1 Spectral governance ruleset.


  AbacatePay''s developer surface includes engineering blog, authentication, documentation, and 9 more developer resources.'
plans:
- name: Abacatepay Plans Pricing
  plan_count: 2
  slug: abacatepay-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Abacatepay Rate Limits
  slug: abacatepay-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: AbacatePay API Rules
  rule_count: 66
  severity_counts:
    error: 56
    hint: 0
    info: 3
    warn: 7
  slug: abacatepay-rules
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 51.3
    developer_ergonomics: 32.1
    discoverability: 68.3
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 30.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 20.0
      total: 25
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 10.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/abacatepay/abacatepay-2026-07-25T181328.png
security:
- kind: authentication
  name: Abacatepay Authentication
  slug: abacatepay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Abacatepay Domain Security
  slug: abacatepay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: abacatepay
tags:
- Payments
- Pix
- Brazil
- Fintech
- Developers
website: https://www.abacatepay.com
---
