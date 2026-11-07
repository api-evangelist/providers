---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Cloudprinter Agentic Access
  operation_count: 11
  slug: cloudprinter-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.cloudprinter.com/cloudcore/1.0
  baseurl_source: declared
  description: Create, list, retrieve, cancel, and audit print orders.
  name: Cloudprinter Orders API
  slug: cloudprinter-orders-api
- baseURL: https://api.cloudprinter.com/cloudcore/1.0
  baseurl_source: declared
  description: List products and retrieve product specifications and options.
  name: Cloudprinter Products API
  slug: cloudprinter-products-api
- baseURL: https://api.cloudprinter.com/cloudcore/1.0
  baseurl_source: declared
  description: Request real-time product and shipping price quotes.
  name: Cloudprinter Quotes API
  slug: cloudprinter-quotes-api
- baseURL: https://api.cloudprinter.com/cloudcore/1.0
  baseurl_source: declared
  description: Shipping levels, supported countries, and states reference data.
  name: Cloudprinter Shipping API
  slug: cloudprinter-shipping-api
artifact_total: 16
collections:
- collection_type: open
  name: Cloudprinter CloudCore Orders API
  slug: open-cloudprinter-orders-api
- collection_type: open
  name: Cloudprinter CloudCore Orders Products API
  slug: open-cloudprinter-products-api
- collection_type: open
  name: Cloudprinter CloudCore Orders Quotes API
  slug: open-cloudprinter-quotes-api
- collection_type: open
  name: Cloudprinter CloudCore Orders Shipping API
  slug: open-cloudprinter-shipping-api
- collection_type: open
  name: Cloudprinter CloudCore API
  slug: open-cloudprinter
common:
- group: company
  title: ''
  type: Blog
  url: https://www.cloudprinter.com/blog
- group: other
  href: https://artifacts.apis.io/cloudprinter/capabilities/cloudprinter-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cloudprinter-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/cloudprinter/agentic-access/cloudprinter-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudprinter-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cloudprinter/security/cloudprinter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudprinter-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cloudprinter/authentication/cloudprinter-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudprinter-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudprintercom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudprinter-com
- group: company
  title: ''
  type: Website
  url: https://www.cloudprinter.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudprinter.com
- group: commercial
  href: https://artifacts.apis.io/cloudprinter/plans/cloudprinter-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudprinter-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cloudprinter/rate-limits/cloudprinter-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloudprinter-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cloudprinter/finops/cloudprinter-finops.yml
  title: ''
  type: FinOps
  url: finops/cloudprinter-finops.yml
created: '2026-06-25'
description: Cloudprinter.com is a global print-on-demand and print-fulfillment API network connecting buyers to 170+ print partners worldwide. The CloudCore REST API lets developers fetch product catalogs, request real-time price and shipping quotes, submit and manage print orders, and receive production and shipment events via CloudSignal webhooks.
finops:
- has_sources: true
  method: generated
  name: Cloudprinter Finops
  primary_unit: ''
  service_category: Print and Fulfillment
  slug: cloudprinter-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudprinter.png
layout: provider
modified: '2026-10-06'
name: Cloudprinter
nav: Providers
network: true
overview: 'Cloudprinter publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Orders API, Products API, Quotes API, and 1 more. Tagged areas include Print on Demand, Print Fulfillment, Printing, Order, and Logistics.


  The Cloudprinter catalog on APIs.io includes 1 Spectral governance ruleset.


  Cloudprinter''s developer surface includes engineering blog, authentication, documentation, and 9 more developer resources.'
plans:
- name: Cloudprinter Plans Pricing
  plan_count: 3
  slug: cloudprinter-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Cloudprinter Rate Limits
  slug: cloudprinter-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Cloudprinter API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: cloudprinter-rules
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 50.7
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 28.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cloudprinter/cloudprinter-2026-07-25T205710.png
security:
- kind: authentication
  name: Cloudprinter Authentication
  slug: cloudprinter-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cloudprinter Domain Security
  slug: cloudprinter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloudprinter
tags:
- Print on Demand
- Print Fulfillment
- Printing
- Order
- Logistics
website: https://www.cloudprinter.com
---
