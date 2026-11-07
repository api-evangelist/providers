---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Edelweiss Hotel Polyana Api Agentic Access
  operation_count: 5
  slug: edelweiss-hotel-polyana-api-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://edelweiss-hotel.com.ua
  baseurl_source: spec
  description: Structured Markdown and text discovery endpoints for AI agents, including the Ukrainian /llms.txt, the English /en/llms.txt and the full knowledge base at /llms-full.txt.
  name: Edelweiss Hotel Polyana API AI & LLM Manifests API
  slug: edelweiss-hotel-polyana-api-ai-llm-manifests-api
- baseURL: https://edelweiss-hotel.com.ua
  baseurl_source: spec
  description: Real-time rates and XML listing feeds for Google Hotels & OTA aggregators
  name: Edelweiss Hotel Polyana API Availability & Pricing API
  slug: edelweiss-hotel-polyana-api-availability-pricing-api
- baseURL: https://edelweiss-hotel.com.ua
  baseurl_source: spec
  description: Public factual data, ratings, room tariffs, and resort profiles, plus guest reviews as JSON at GET /api/reviews (each review carries author, rating, source, content and date).
  name: Edelweiss Hotel Polyana API Hotel Information API
  slug: edelweiss-hotel-polyana-api-hotel-information-api
- baseURL: https://edelweiss-hotel.com.ua
  baseurl_source: spec
  description: Public content and room search query endpoint
  name: Edelweiss Hotel Polyana API Search API
  slug: edelweiss-hotel-polyana-api-search-api
- description: Returns one room category as a Markdown document (text/markdown) for AI agents, with nightly rate, distance to the mineral spring pump room and room characteristics, in Ukrainian. GET /api/markdown/ro
  name: Edelweiss Hotel Polyana Markdown Room API
  slug: edelweiss-hotel-polyana-api-markdown-room-api
- description: 'MCP server published by the hotel (io.github.kyivuinua/edelweiss-hotel-mcp) with four tools (get_hotel_tariffs, calculate_stay_quote, get_google_hotels_feed, search_faqs) backed by the hotel''s public '
  name: Edelweiss Hotel MCP Server
  slug: edelweiss-hotel-mcp-server
artifact_total: 19
common:
- group: other
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/capabilities/edelweiss-hotel-polyana-api-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/edelweiss-hotel-polyana-api-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/agentic-access/edelweiss-hotel-polyana-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/edelweiss-hotel-polyana-api-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/rules/edelweiss-hotel-polyana-api-rules.yml
  title: ''
  type: Spectral
  url: rules/edelweiss-hotel-polyana-api-rules.yml
- group: design
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/json-ld/edelweiss-hotel-polyana-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/edelweiss-hotel-polyana-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/vocabulary/edelweiss-hotel-polyana-api-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/edelweiss-hotel-polyana-api-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/lifecycle/edelweiss-hotel-polyana-api-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/edelweiss-hotel-polyana-api-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/hosts/edelweiss-hotel-polyana-api-hosts.yml
  title: ''
  type: Hosts
  url: hosts/edelweiss-hotel-polyana-api-hosts.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.edelweiss-hotel.com.ua
- group: other
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/overlays/edelweiss-hotel-polyana-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/edelweiss-hotel-polyana-api-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://edelweiss-hotel.com.ua/
- group: docs
  title: ''
  type: Documentation
  url: https://edelweiss-hotel.com.ua/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://edelweiss-hotel.com.ua/prices/
- group: operate
  title: ''
  type: Support
  url: https://edelweiss-hotel.com.ua/contacts/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://edelweiss-hotel.com.ua/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://edelweiss-hotel.com.ua/privacy/
- group: auth
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/authentication/edelweiss-hotel-polyana-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/edelweiss-hotel-polyana-api-authentication.yml
- group: agent
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/well-known/edelweiss-hotel-polyana-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/edelweiss-hotel-polyana-api-well-known.yml
- group: agent
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/mcp/edelweiss-hotel-polyana-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/edelweiss-hotel-polyana-api-mcp.yml
- group: design
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/conformance/edelweiss-hotel-polyana-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/edelweiss-hotel-polyana-api-conformance.yml
- group: design
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/conventions/edelweiss-hotel-polyana-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/edelweiss-hotel-polyana-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/data-model/edelweiss-hotel-polyana-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/edelweiss-hotel-polyana-api-data-model.yml
- group: design
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/lifecycle/edelweiss-hotel-polyana-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/edelweiss-hotel-polyana-api-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/plans/edelweiss-hotel-polyana-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/edelweiss-hotel-polyana-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/rate-limits/edelweiss-hotel-polyana-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/edelweiss-hotel-polyana-api-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/edelweiss-hotel-polyana-api/security/edelweiss-hotel-polyana-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/edelweiss-hotel-polyana-api-domain-security.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://edelweiss-hotel.com.ua/openapi.json
- group: other
  title: ''
  type: APIsJSON
  url: https://edelweiss-hotel.com.ua/apis.json
- group: build
  title: ''
  type: AIPlugin
  url: https://edelweiss-hotel.com.ua/.well-known/ai-plugin.json
- group: agent
  title: ''
  type: LLMsTxt
  url: https://edelweiss-hotel.com.ua/en/llms.txt
- group: agent
  title: ''
  type: LLMsFullTxt
  url: https://edelweiss-hotel.com.ua/llms-full.txt
created: '2026-09-18'
description: Public open REST API and structured data feeds for Edelweiss Hotel Polyana, a 3-star boutique eco-hotel in Polyana, Zakarpattia, Ukraine. Provides real-time room tariffs, hotel info, a Google Hotels XML pricing feed, quote calculation, and LLM knowledge bases. Open access, no authentication.
finops:
- has_sources: true
  method: derived
  name: Edelweiss Hotel Polyana Api Finops
  primary_unit: ''
  service_category: ''
  slug: edelweiss-hotel-polyana-api-finops
  template: true
image: https://edelweiss-hotel.com.ua/images/og-main.webp
json_schemas:
- name: HotelAiData
  property_count: 6
  slug: edelweiss-hotel-polyana-api-hotel-ai-data
jsonld:
- class_count: 2
  name: Edelweiss Hotel Polyana Api Context
  property_count: 21
  slug: edelweiss-hotel-polyana-api-context
layout: provider
mcp_servers:
- description: Official Model Context Protocol (MCP) server for Edelweiss Hotel Polyana (Carpathians, Ukraine). Enables AI assistants to query live tariffs, medical profiles for Polyana Kvasova mineral water, and co
  name: Edelweiss Hotel Polyana API MCP Server
  slug: io-github-kyivuinua-edelweiss-hotel-mcp
- description: ''
  name: Edelweiss Hotel Polyana API MCP Server
  slug: mcp-server-json
modified: '2026-09-18'
name: Edelweiss Hotel Polyana API
nav: Providers
network: true
overview: 'Edelweiss Hotel Polyana API publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI & LLM Manifests API, Availability & Pricing API, Hotel Information API, and 3 more. Tagged areas include Hotels, Hospitality, Travel, Tourism, and Ukraine.


  The Edelweiss Hotel Polyana API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Edelweiss Hotel Polyana API''s developer surface includes documentation, pricing, support, authentication, and 27 more developer resources.'
plans:
- name: Edelweiss Hotel Polyana Api Plans Pricing
  plan_count: 0
  slug: edelweiss-hotel-polyana-api-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Edelweiss Hotel Polyana Api Rate Limits
  slug: edelweiss-hotel-polyana-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Edelweiss Hotel Polyana API API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: edelweiss-hotel-polyana-api-rules
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 51.2
    catalog_earned_first_party: 0.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 31.6
    contract_governance: 35.6
    contract_quality: 59.8
    developer_ergonomics: 28.0
    discoverability: 66.7
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ukraine
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/edelweiss-hotel-polyana-api/edelweiss-hotel-polyana-api-2026-10-11T104017.png
security:
- kind: authentication
  name: Edelweiss Hotel Polyana Api Authentication
  slug: edelweiss-hotel-polyana-api-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Edelweiss Hotel Polyana Api Domain Security
  slug: edelweiss-hotel-polyana-api-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: get-hotel-info
  slug: edelweiss-hotel-polyana-api-get-hotel-info
- name: get-stay-quote
  slug: edelweiss-hotel-polyana-api-get-stay-quote
slug: edelweiss-hotel-polyana-api
tags:
- Hotels
- Hospitality
- Travel
- Tourism
- Ukraine
- Carpathians
- Mineral Water
- Balneology
- Booking
- Room Rates
- google-hotels
website: https://edelweiss-hotel.com.ua/
---
