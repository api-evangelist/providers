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
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Repsly Agentic Access
  operation_count: 24
  slug: repsly-agentic-access
  summary_line: 24 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export and import clients and client notes.
  name: Repsly Clients API
  slug: repsly-clients-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export completed forms and retail audits.
  name: Repsly Forms API
  slug: repsly-forms-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Bulk import surface and import job status.
  name: Repsly Import API
  slug: repsly-import-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export photos captured in the field.
  name: Repsly Photos API
  slug: repsly-photos-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export and import products, product lists, packages, and document types.
  name: Repsly Products API
  slug: repsly-products-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export purchase orders and update sales document status.
  name: Repsly Purchase Orders API
  slug: repsly-purchase-orders-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export representatives, users, and daily working time.
  name: Repsly Representatives API
  slug: repsly-representatives-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export visits, visit schedules, and realizations; import schedules.
  name: Repsly Visits API
  slug: repsly-visits-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export and import pricelists and pricelist items.
  name: Repsly Price Lists API
  slug: repsly-price-lists-api
artifact_total: 27
collections:
- collection_type: open
  name: Repsly Web Clients API
  slug: open-repsly-clients-api
- collection_type: open
  name: Repsly Web Clients Forms API
  slug: open-repsly-forms-api
- collection_type: open
  name: Repsly Web Clients Import API
  slug: open-repsly-import-api
- collection_type: open
  name: Repsly Web Clients Photos API
  slug: open-repsly-photos-api
- collection_type: open
  name: Repsly Web Clients Pricelists API
  slug: open-repsly-pricelists-api
- collection_type: open
  name: Repsly Web Clients Products API
  slug: open-repsly-products-api
- collection_type: open
  name: Repsly Web Clients Purchase Orders API
  slug: open-repsly-purchase-orders-api
- collection_type: open
  name: Repsly Web Clients Representatives API
  slug: open-repsly-representatives-api
- collection_type: open
  name: Repsly Web Clients Visits API
  slug: open-repsly-visits-api
- collection_type: open
  name: Repsly Web API (v3)
  slug: open-repsly
common:
- group: other
  href: https://artifacts.apis.io/repsly/capabilities/repsly-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/repsly-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/repsly/agentic-access/repsly-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/repsly-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/repsly/security/repsly-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/repsly-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/repsly/security/repsly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/repsly-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/repsly/authentication/repsly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/repsly-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/repsly
- group: company
  title: ''
  type: Website
  url: https://www.repsly.com
- group: docs
  title: ''
  type: Documentation
  url: https://repsly-dev.readme.io/reference/getting-started-1
- group: commercial
  href: https://artifacts.apis.io/repsly/plans/repsly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/repsly-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/repsly/rate-limits/repsly-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/repsly-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/repsly/finops/repsly-finops.yml
  title: ''
  type: FinOps
  url: finops/repsly-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.repsly.com/blog
created: '2026-07-04'
description: Repsly is a retail execution and field sales platform for CPG brands and field teams - covering in-store activity, merchandising, retail audits, order taking, and territory management. The Repsly Web API (v3) is a REST interface at https://api.repsly.com/v3 designed for ERP/CRM integration - it moves clients and products into Repsly (import) and pulls clients, visits, retail audits, forms, photos, purchase orders, pricelists, representatives, and schedules back out (export). Requests use HTTP Basic authentication over SSL, exchange JSON or XML, and paginate export results in batches of up to 50 records using timestamp or last-ID cursors until the response MetaCollectionResult TotalCount reaches zero.
finops:
- has_sources: true
  method: generated
  name: Repsly Finops
  primary_unit: ''
  service_category: Retail Execution and Field Sales Software
  slug: repsly-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/repsly.png
layout: provider
modified: '2026-07-04'
name: Repsly
nav: Providers
network: true
overview: 'Repsly publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Clients API, Forms API, Import API, and 6 more. Tagged areas include Retail Execution, Field Sales, Merchandising, Consumer Packaged Goods, and Retail Audits.


  The Repsly catalog on APIs.io includes 1 Spectral governance ruleset.


  Repsly''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Repsly Plans Pricing
  plan_count: 2
  slug: repsly-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 3
  name: Repsly Rate Limits
  slug: repsly-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Repsly API Rules
  rule_count: 63
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 2
  slug: repsly-rules
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 44.8
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 28.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/repsly/repsly-2026-09-02T153511.png
security:
- kind: authentication
  name: Repsly Authentication
  slug: repsly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Repsly Domain Security
  slug: repsly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Repsly Trust Center
  slug: repsly-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: repsly
tags:
- Retail Execution
- Field Sales
- Merchandising
- Consumer Packaged Goods
- Retail Audits
- Sales Force Automation
website: https://www.repsly.com
---
