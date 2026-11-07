---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Bold Commerce Agentic Access
  operation_count: 29
  slug: bold-commerce-agentic-access
  summary_line: 29 operations · 18 acting
api_count: 1
apis:
- baseURL: https://api.boldcommerce.com/subscriptions/v1
  baseurl_source: declared
  description: Customer records tied to a shop.
  name: Bold Commerce Customers API
  slug: bold-commerce-customers-api
- baseURL: https://api.boldcommerce.com/subscriptions/v1
  baseurl_source: declared
  description: Shop configuration and shop_identifier lookup.
  name: Bold Commerce Shops API
  slug: bold-commerce-shops-api
- baseURL: https://api.boldcommerce.com/subscriptions/v1
  baseurl_source: declared
  description: Recurring orders, intervals, and subscription management.
  name: Bold Commerce Subscriptions API
  slug: bold-commerce-subscriptions-api
- baseURL: https://api.boldcommerce.com/subscriptions/v1
  baseurl_source: declared
  description: Use these endpoints to create, update, or delete convertible adjustment plans, enabling automatic product conversions on subscription line items attached to a created plan.
  name: Bold Commerce Convertible Adjustments API
  slug: bold-commerce-convertible-adjustments-api
- baseURL: https://api.boldcommerce.com/subscriptions/v1
  baseurl_source: declared
  description: Contains information about future orders for subscriptions. Use these endpoints to list future orders for a shop or individual subscriptions.
  name: Bold Commerce Future Orders API
  slug: bold-commerce-future-orders-api
- baseURL: https://api.boldcommerce.com/subscriptions/v1
  baseurl_source: declared
  description: 'A child resource of Subscriptions. Contains information about payment methods for subscriptions, including public payment IDs, alternate payment methods, and available methods. Use these endpoints to '
  name: Bold Commerce Payment Methods API
  slug: bold-commerce-payment-methods-api
- baseURL: https://api.boldcommerce.com/subscriptions/v1
  baseurl_source: declared
  description: A child resource of Subscriptions. Contains information about future adjustments to a subscription or its orders. Use these endpoints to create, list, or delete adjustments for a subscription.
  name: Bold Commerce Subscription Adjustments API
  slug: bold-commerce-subscription-adjustments-api
- baseURL: https://api.boldcommerce.com/subscriptions/v1
  baseurl_source: declared
  description: Contains information about subscription groups for your store, including shop ID and subscription group configuration. Use these endpoints to add, remove, edit, or list subscription groups.
  name: Bold Commerce Subscription Groups API
  slug: bold-commerce-subscription-groups-api
- baseURL: https://api.boldcommerce.com/subscriptions/v1
  baseurl_source: declared
  description: A child resource of Subscriptions. Contains information about line items in a subscription, including price, details, and swappable products. Use these endpoints to get, remove, edit, or list line ite
  name: Bold Commerce Subscription Line Items API
  slug: bold-commerce-subscription-line-items-api
- baseURL: https://api.boldcommerce.com/subscriptions/v1
  baseurl_source: declared
  description: A child resource of Subscriptions. Contains information about orders in a subscription, including schedules, order histories, and current orders. Use these endpoints to list, get, skip, or unskip orde
  name: Bold Commerce Subscription Orders API
  slug: bold-commerce-subscription-orders-api
- baseURL: https://api.boldcommerce.com/subscriptions/v1
  baseurl_source: declared
  description: Contains information about webhook events, including webhook event ID, attempts, and webhook event metadata. Use these endpoints to get webhook event information.
  name: Bold Commerce Webhook Events API
  slug: bold-commerce-webhook-events-api
- baseURL: https://api.boldcommerce.com/subscriptions/v1
  baseurl_source: declared
  description: Contains webhook metadata. Use these endpoints to add, remove, edit, or list webhook subscriptions.
  name: Bold Commerce Webhook Subscriptions API
  slug: bold-commerce-webhook-subscriptions-api
- baseURL: https://api.boldcommerce.com/subscriptions/v1
  baseurl_source: declared
  description: Contains information about webhook topics. Use these endpoints to list all possible webhook topics.
  name: Bold Commerce Webhook Topics API
  slug: bold-commerce-webhook-topics-api
artifact_total: 28
collections:
- collection_type: open
  name: Bold Commerce Checkout API
  slug: open-bold-commerce-checkout-api
- collection_type: open
  name: Bold Commerce Checkout Customers API
  slug: open-bold-commerce-customers-api
- collection_type: open
  name: Bold Commerce Checkout Price Rules API
  slug: open-bold-commerce-price-rules-api
- collection_type: open
  name: Bold Commerce Checkout Products API
  slug: open-bold-commerce-products-api
- collection_type: open
  name: Bold Commerce Checkout Shops API
  slug: open-bold-commerce-shops-api
- collection_type: open
  name: Bold Commerce Checkout Subscriptions API
  slug: open-bold-commerce-subscriptions-api
- collection_type: open
  name: Bold Commerce API
  slug: open-bold-commerce
common:
- group: other
  href: https://artifacts.apis.io/bold-commerce/capabilities/bold-commerce-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bold-commerce-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/bold-commerce/agentic-access/bold-commerce-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bold-commerce-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bold-commerce/security/bold-commerce-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bold-commerce-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bold-commerce/security/bold-commerce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bold-commerce-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/bold-commerce/authentication/bold-commerce-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bold-commerce-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bold-commerce
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bold-commerce
- group: company
  title: ''
  type: Website
  url: https://boldcommerce.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.boldcommerce.com
- group: commercial
  href: https://artifacts.apis.io/bold-commerce/plans/bold-commerce-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bold-commerce-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bold-commerce/rate-limits/bold-commerce-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bold-commerce-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bold-commerce/finops/bold-commerce-finops.yml
  title: ''
  type: FinOps
  url: finops/bold-commerce-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://boldcommerce.com/blog
created: '2026-07-10'
description: Bold Commerce builds modular e-commerce apps and headless commerce APIs for subscriptions, checkout, and pricing. Merchants and developers integrate Bold Subscriptions (recurring orders and branded customer portals), Bold Checkout (a headless, fully customizable checkout across Frontend, Backend, and Admin surfaces), and Bold Price Rules (discounts, promotions, and dynamic pricing), alongside supporting Products, Customers, and Shops APIs. Requests are made against api.boldcommerce.com and authenticated with an OAuth 2.0 access token (public integrations) or a scoped API access token (private integrations), passed as a Bearer token.
finops:
- has_sources: true
  method: generated
  name: Bold Commerce Finops
  primary_unit: ''
  service_category: E-Commerce and Commerce Platform
  slug: bold-commerce-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bold-commerce.png
layout: provider
modified: '2026-07-10'
name: Bold Commerce
nav: Providers
network: true
overview: 'Bold Commerce publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Customers API, Shops API, Subscriptions API, and 10 more. Tagged areas include E-Commerce, Subscription, Checkout, Pricing, and Headless Commerce.


  The Bold Commerce catalog on APIs.io includes 1 Spectral governance ruleset.


  Bold Commerce''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Bold Commerce Plans Pricing
  plan_count: 7
  slug: bold-commerce-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Bold Commerce Rate Limits
  slug: bold-commerce-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Bold Commerce API Rules
  rule_count: 66
  severity_counts:
    error: 54
    hint: 0
    info: 4
    warn: 8
  slug: bold-commerce-rules
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 53.3
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 65.0
      total: 20
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/bold-commerce/bold-commerce-2026-07-25T203530.png
security:
- kind: authentication
  name: Bold Commerce Authentication
  slug: bold-commerce-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bold Commerce Domain Security
  slug: bold-commerce-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Bold Commerce Trust Center
  slug: bold-commerce-trust-center
  summary_line: PCI DSS, GDPR
slug: bold-commerce
tags:
- E-Commerce
- Subscription
- Checkout
- Pricing
- Headless Commerce
- Shopify
website: https://boldcommerce.com
---
