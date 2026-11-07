---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.5
  scored_at: '2026-11-06'
api_count: 8
apis:
- baseURL: https://api.rezdy-staging.com
  baseurl_source: declared
  description: The Availability API from Rezdy — 2 operation(s) for availability.
  name: Rezdy Availability API
  slug: rezdy-availability-api
- baseURL: https://api.rezdy-staging.com
  baseurl_source: declared
  description: The Bookings API from Rezdy — 3 operation(s) for bookings.
  name: Rezdy Bookings API
  slug: rezdy-bookings-api
- baseURL: https://api.rezdy-staging.com
  baseurl_source: declared
  description: The Categories API from Rezdy — 2 operation(s) for categories.
  name: Rezdy Categories API
  slug: rezdy-categories-api
- baseURL: https://api.rezdy-staging.com
  baseurl_source: declared
  description: The Companies API from Rezdy — 1 operation(s) for companies.
  name: Rezdy Companies API
  slug: rezdy-companies-api
- baseURL: https://api.rezdy-staging.com
  baseurl_source: declared
  description: The Manifest API from Rezdy — 1 operation(s) for manifest.
  name: Rezdy Manifest API
  slug: rezdy-manifest-api
- baseURL: https://api.rezdy-staging.com
  baseurl_source: declared
  description: The Products API from Rezdy — 5 operation(s) for products.
  name: Rezdy Products API
  slug: rezdy-products-api
- baseURL: https://api.rezdy-staging.com
  baseurl_source: declared
  description: The Resources API from Rezdy — 4 operation(s) for resources.
  name: Rezdy Resources API
  slug: rezdy-resources-api
- baseURL: https://api.rezdy-staging.com
  baseurl_source: declared
  description: The Vouchers API from Rezdy — 1 operation(s) for vouchers.
  name: Rezdy Vouchers API
  slug: rezdy-vouchers-api
artifact_total: 22
asyncapis:
- description: ''
  name: Rezdy Webhooks
  slug: rezdy-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/rezdy/well-known/rezdy-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rezdy-status-security.txt
- group: commercial
  href: https://artifacts.apis.io/rezdy/plans/rezdy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rezdy-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/rezdy/rules/rezdy-rules.yml
  title: ''
  type: Spectral
  url: rules/rezdy-rules.yml
- group: design
  href: https://artifacts.apis.io/rezdy/json-ld/rezdy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rezdy-context.jsonld
- group: design
  href: https://artifacts.apis.io/rezdy/vocabulary/rezdy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rezdy-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/rezdy/asyncapi/rezdy-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/rezdy-webhooks.yml
- group: design
  href: https://artifacts.apis.io/rezdy/data-model/rezdy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rezdy-data-model.yml
- group: design
  href: https://artifacts.apis.io/rezdy/conformance/rezdy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rezdy-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rezdy/llms/rezdy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rezdy-llms.txt
- group: agent
  href: https://artifacts.apis.io/rezdy/well-known/rezdy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rezdy-well-known.yml
- group: other
  href: https://artifacts.apis.io/rezdy/hosts/rezdy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rezdy-hosts.yml
- group: other
  href: https://artifacts.apis.io/rezdy/vendors/rezdy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rezdy-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rezdy.com/
- group: auth
  title: ''
  type: Security
  url: https://rezdy.com/security/
- group: company
  title: ''
  type: Newsroom
  url: https://rezdy.com/category/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rezdy
- group: auth
  href: https://artifacts.apis.io/rezdy/security/rezdy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/rezdy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/rezdy/security/rezdy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rezdy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rezdy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.rezdy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.rezdy.com/rezdyapi/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.rezdy.com/rezdyapi/index-agent.html
- group: start
  title: ''
  type: GettingStarted
  url: https://rezdy.com/book-a-demo/
- group: operate
  title: ''
  type: Support
  url: https://support.rezdy.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://rezdy.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://rezdy.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.rezdy.com/join
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rezdy.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rezdy.com/privacy/
coverage:
  checked: '2026-10-12'
  detail: Developer portal provides HTML documentation but no machine‑readable OpenAPI or other contract files were found.
  evidence:
  - status: 200
    url: https://api.rezdy.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Rezdy provides a comprehensive online booking system for tour and experience providers, offering a full-featured platform that includes automated communications, live availability, reporting and analytics, channel management, and integration tools. Their API enables developers to embed booking functionality, manage inventory, process payments, and access a large distribution network, supporting businesses of all sizes in the travel and tourism industry.
finops:
- has_sources: true
  method: derived
  name: Rezdy Finops
  primary_unit: seat
  service_category: ''
  slug: rezdy-finops
  template: false
image: https://rezdy.com/wp-content/uploads/2017/09/rezdy-og-image.png
json_schemas:
- name: PostBookingsRequest
  property_count: 3
  slug: rezdy-post-bookings-request
- name: PostProductsProductcodeImagesRequest
  property_count: 1
  slug: rezdy-post-products-productcode-images-request
- name: PostProductsProductcodeRequest
  property_count: 3
  slug: rezdy-post-products-productcode-request
- name: PutBookingsOrdernumberRequest
  property_count: 3
  slug: rezdy-put-bookings-ordernumber-request
- name: PutBookingsRequest
  property_count: 5
  slug: rezdy-put-bookings-request
- name: PutProductsProductcodeRequest
  property_count: 3
  slug: rezdy-put-products-productcode-request
jsonld:
- class_count: 13
  name: Rezdy Context
  property_count: 16
  slug: rezdy-context
layout: provider
modified: '2026-10-12'
name: Rezdy
nav: Providers
network: true
overview: 'Rezdy is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Bookings API, Categories API, and 5 more. Tagged areas include Company, Travel, Booking, and Software-as-a-Service.


  The Rezdy catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Rezdy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Rezdy Plans Pricing
  plan_count: 3
  slug: rezdy-plans-pricing
- name: Rezdy Price Estimates
  plan_count: 0
  slug: rezdy-price-estimates
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Rezdy API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: rezdy-rules
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 75.8
    catalog_earned_first_party: 12.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.8
  facets:
    access_clarity: 61.8
    contract_governance: 22.0
    contract_quality: 35.5
    developer_ergonomics: 22.6
    discoverability: 70.5
    operational_transparency: 23.7
  previous_composite: 51.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/rezdy/rezdy-2026-11-03T142248.png
security:
- kind: domain-security
  name: Rezdy Domain Security
  slug: rezdy-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Rezdy Vulnerability Disclosure
  slug: rezdy-vulnerability-disclosure
  summary_line: no policy recorded
slug: rezdy
tags:
- Company
- Travel
- Booking
- Software-as-a-Service
website: https://rezdy.com/
---
