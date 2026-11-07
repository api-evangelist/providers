---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    idempotency: verified
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
  score: 27.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Prodigi Agentic Access
  operation_count: 10
  slug: prodigi-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.prodigi.com/v4.0
  baseurl_source: declared
  description: Create, retrieve, list, and act on print orders.
  name: Prodigi Orders API
  slug: prodigi-orders-api
- baseURL: https://api.prodigi.com/v4.0
  baseurl_source: declared
  description: Query the product catalogue by SKU.
  name: Prodigi Products API
  slug: prodigi-products-api
- baseURL: https://api.prodigi.com/v4.0
  baseurl_source: declared
  description: Request pricing and shipping breakdowns before ordering.
  name: Prodigi Quotes API
  slug: prodigi-quotes-api
artifact_total: 14
collections:
- collection_type: open
  name: Prodigi Print Orders API
  slug: open-prodigi-orders-api
- collection_type: open
  name: Prodigi Print Orders Products API
  slug: open-prodigi-products-api
- collection_type: open
  name: Prodigi Print Orders Quotes API
  slug: open-prodigi-quotes-api
- collection_type: open
  name: Prodigi Print API
  slug: open-prodigi
common:
- group: other
  href: https://artifacts.apis.io/prodigi/capabilities/prodigi-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/prodigi-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/prodigi/agentic-access/prodigi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/prodigi-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/prodigi/security/prodigi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prodigi-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/prodigi/authentication/prodigi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/prodigi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Prodigi-Group
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prodigi
- group: company
  title: ''
  type: Website
  url: https://www.prodigi.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.prodigi.com/print-api/docs/
- group: commercial
  href: https://artifacts.apis.io/prodigi/plans/prodigi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/prodigi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/prodigi/rate-limits/prodigi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/prodigi-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/prodigi/finops/prodigi-finops.yml
  title: ''
  type: FinOps
  url: finops/prodigi-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.prodigi.com/blog/
created: '2026-06-25'
description: Prodigi is a global print-on-demand and dropshipping platform that connects merchants to a worldwide network of print labs. The Prodigi Print API (v4.0) lets developers create and manage print orders, fetch real-time quotes, and query the product catalogue, with print and shipping fulfilled at wholesale prices direct from the manufacturer.
finops:
- has_sources: true
  method: generated
  name: Prodigi Finops
  primary_unit: ''
  service_category: Print and Fulfillment
  slug: prodigi-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prodigi.png
layout: provider
modified: '2026-06-25'
name: Prodigi
nav: Providers
network: true
overview: 'Prodigi publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Orders API, Products API, and Quotes API. Tagged areas include Print on Demand, Printing, Dropshipping, Fulfillment, and E-Commerce.


  The Prodigi catalog on APIs.io includes 1 Spectral governance ruleset.


  Prodigi''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Prodigi Plans Pricing
  plan_count: 2
  slug: prodigi-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Prodigi Rate Limits
  slug: prodigi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Prodigi API Rules
  rule_count: 62
  severity_counts:
    error: 59
    hint: 0
    info: 2
    warn: 1
  slug: prodigi-rules
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 49.4
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 27.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
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
screenshot: https://apis.io/screenshots/prodigi/prodigi-2026-09-02T152115.png
security:
- kind: authentication
  name: Prodigi Authentication
  slug: prodigi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Prodigi Domain Security
  slug: prodigi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: prodigi
tags:
- Print on Demand
- Printing
- Dropshipping
- Fulfillment
- E-Commerce
website: https://www.prodigi.com
---
