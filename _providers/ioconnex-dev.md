---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Ioconnex Dev Agentic Access
  operation_count: 30
  slug: ioconnex-dev-agentic-access
  summary_line: 30 operations · 14 acting
api_count: 3
apis:
- baseURL: https://convert.ioconnex.dev
  baseurl_source: declared
  description: The Affiliate API from ioconnex-dev — 1 operation(s) for affiliate.
  name: ioconnex-dev Affiliate API
  slug: ioconnex-dev-affiliate-api
- baseURL: https://convert.ioconnex.dev
  baseurl_source: declared
  description: The Billing API from ioconnex-dev — 6 operation(s) for billing.
  name: ioconnex-dev Billing API
  slug: ioconnex-dev-billing-api
- baseURL: https://convert.ioconnex.dev
  baseurl_source: declared
  description: The Convert API from ioconnex-dev — 4 operation(s) for convert.
  name: ioconnex-dev Convert API
  slug: ioconnex-dev-convert-api
- baseURL: https://convert.ioconnex.dev
  baseurl_source: declared
  description: The Fetch API from ioconnex-dev — 1 operation(s) for fetch.
  name: ioconnex-dev Fetch API
  slug: ioconnex-dev-fetch-api
- baseURL: https://convert.ioconnex.dev
  baseurl_source: declared
  description: The Health API from ioconnex-dev — 1 operation(s) for health.
  name: ioconnex-dev Health API
  slug: ioconnex-dev-health-api
- baseURL: https://convert.ioconnex.dev
  baseurl_source: declared
  description: The Paid API from ioconnex-dev — 3 operation(s) for paid.
  name: ioconnex-dev Paid API
  slug: ioconnex-dev-paid-api
- baseURL: https://convert.ioconnex.dev
  baseurl_source: declared
  description: The Price API from ioconnex-dev — 1 operation(s) for price.
  name: ioconnex-dev Price API
  slug: ioconnex-dev-price-api
- baseURL: https://convert.ioconnex.dev
  baseurl_source: declared
  description: The Search API from ioconnex-dev — 1 operation(s) for search.
  name: ioconnex-dev Search API
  slug: ioconnex-dev-search-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/ioconnex-dev/agentic-access/ioconnex-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ioconnex-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/ioconnex-dev/plans/ioconnex-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ioconnex-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ioconnex-dev/rules/ioconnex-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/ioconnex-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/ioconnex-dev/json-ld/ioconnex-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ioconnex-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/ioconnex-dev/vocabulary/ioconnex-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ioconnex-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ioconnex-dev/data-model/ioconnex-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ioconnex-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/ioconnex-dev/errors/ioconnex-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ioconnex-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ioconnex-dev/conformance/ioconnex-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ioconnex-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ioconnex-dev/llms/ioconnex-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ioconnex-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/ioconnex-dev/hosts/ioconnex-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ioconnex-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/ioconnex-dev/vendors/ioconnex-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ioconnex-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ioconnex-dev/security/ioconnex-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ioconnex-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ioconnex.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://convert.ioconnex.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://ioconnex.dev/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://search.ioconnex.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://search.ioconnex.dev/legal/privacy
created: '2026-10-29'
description: IOConnex provides one‑click MCP (Machine‑Control‑Protocol) superpowers for AI agents, offering web search, document conversion, and price tracking services through simple snippet configuration. The platform hosts three MCP servers—search, convert, and prices—delivered without accounts or API keys, targeting developers integrating AI tools. It offers a free tier with 50 credits per month and a paid Pro plan at $9/month, emphasizing speed, cost‑efficiency, and ease of use for AI‑driven applications.
json_schemas:
- name: AffiliateRequest
  property_count: 3
  slug: ioconnex-dev-affiliate-request
- name: Body_convert_ocr_convert_ocr_post
  property_count: 1
  slug: ioconnex-dev-body-convert-ocr-convert-ocr-post
- name: Body_convert_pdf_convert_pdf_post
  property_count: 1
  slug: ioconnex-dev-body-convert-pdf-convert-pdf-post
- name: Body_convert_pdf_paid_convert_pdf_post
  property_count: 1
  slug: ioconnex-dev-body-convert-pdf-paid-convert-pdf-post
- name: Body_convert_spreadsheet_convert_spreadsheet_post
  property_count: 1
  slug: ioconnex-dev-body-convert-spreadsheet-convert-spreadsheet-post
- name: FetchRequest
  property_count: 1
  slug: ioconnex-dev-fetch-request
- name: PriceRequest
  property_count: 1
  slug: ioconnex-dev-price-request
- name: SearchRequest
  property_count: 2
  slug: ioconnex-dev-search-request
- name: UrlRequest
  property_count: 1
  slug: ioconnex-dev-url-request
jsonld:
- class_count: 11
  name: Ioconnex Dev Context
  property_count: 12
  slug: ioconnex-dev-context
layout: provider
modified: '2026-10-29'
name: ioconnex-dev
nav: Providers
network: true
overview: 'ioconnex-dev publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Affiliate API, Billing API, Convert API, and 5 more. Tagged areas include Company, Artificial Intelligence, MCP, Search, and Document Conversion.


  The ioconnex-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ioconnex-dev''s developer surface includes API reference, pricing, and 15 more developer resources.'
plans:
- name: Ioconnex Dev Plans Pricing
  plan_count: 3
  slug: ioconnex-dev-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Ioconnex Dev Rate Limits
  slug: ioconnex-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ioconnex-dev API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: ioconnex-dev-rules
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 83.0
    catalog_earned_first_party: 20.0
    catalog_gap: 32.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 47.4
    contract_governance: 19.7
    contract_quality: 49.6
    developer_ergonomics: 3.6
    discoverability: 75.0
    operational_transparency: 21.1
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ioconnex-dev/ioconnex-dev-2026-11-03T134014.png
security:
- kind: domain-security
  name: Ioconnex Dev Domain Security
  slug: ioconnex-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 3
skills:
- name: ioconnex-dev-convert
  slug: ioconnex-dev-convert
- name: ioconnex-dev-prices
  slug: ioconnex-dev-prices
- name: ioconnex-dev-search
  slug: ioconnex-dev-search
slug: ioconnex-dev
tags:
- Company
- Artificial Intelligence
- MCP
- Search
- Document Conversion
- Price-Tracking
website: https://ioconnex.dev/
---
