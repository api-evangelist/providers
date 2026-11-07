---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Foundry/API provides a suite of AI‑enhanced automation APIs accessible via RapidAPI.
  name: Foundry/API
  slug: foundry-api
- description: 'prodapi-live API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: prodapi-live API
  slug: prodapi-live-api
artifact_total: 14
common:
- group: operate
  href: https://artifacts.apis.io/prodapi-live/rate-limits/prodapi-live-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/prodapi-live-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/prodapi-live/plans/prodapi-live-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/prodapi-live-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/prodapi-live/rules/prodapi-live-rules.yml
  title: ''
  type: Spectral
  url: rules/prodapi-live-rules.yml
- group: design
  href: https://artifacts.apis.io/prodapi-live/json-ld/prodapi-live-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/prodapi-live-context.jsonld
- group: design
  href: https://artifacts.apis.io/prodapi-live/vocabulary/prodapi-live-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/prodapi-live-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/prodapi-live/data-model/prodapi-live-data-model.yml
  title: ''
  type: DataModel
  url: data-model/prodapi-live-data-model.yml
- group: design
  href: https://artifacts.apis.io/prodapi-live/conformance/prodapi-live-conformance.yml
  title: ''
  type: Conformance
  url: conformance/prodapi-live-conformance.yml
- group: agent
  href: https://artifacts.apis.io/prodapi-live/mcp/prodapi-live-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/prodapi-live-mcp.yml
- group: other
  href: https://artifacts.apis.io/prodapi-live/hosts/prodapi-live-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prodapi-live-hosts.yml
- group: other
  href: https://artifacts.apis.io/prodapi-live/vendors/prodapi-live-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prodapi-live-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://prodapi.live/security
- group: auth
  href: https://artifacts.apis.io/prodapi-live/security/prodapi-live-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prodapi-live-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prodapi.live/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://prodapi.live/developers
- group: docs
  title: ''
  type: Documentation
  url: https://prodapi.live/developers
- group: docs
  title: ''
  type: APIReference
  url: https://prodapi.live/rendercloud
- group: start
  title: ''
  type: GettingStarted
  url: https://prodapi.live/start
- group: operate
  title: ''
  type: Support
  url: https://prodapi.live/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://prodapi.live/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prodapi.live/legal/privacy
- group: other
  title: ''
  type: AcceptableUse
  url: https://prodapi.live/legal/acceptable-use
- group: build
  title: ''
  type: Postman
  url: https://prodapi.live/developers
coverage:
  checked: '2026-10-31'
  detail: API contracts are only available via RapidAPI marketplace listings, not on the provider's own site.
  evidence:
  - status: 200
    url: https://prodapi.live/developers
  reason: marketplace-only
  state: gated
created: '2026-10-31'
description: Foundry/API (operating at prodapi.live) provides a suite of nine focused APIs that enable developers to automate complex workflows such as document rendering, web scraping, data extraction, AI‑driven retrieval‑augmented generation, monitoring, and feedback analysis. Each API is backed by a verification layer that enforces input constraints, offers transparent contract inspection, and integrates with RapidAPI for secure credential management. The platform emphasizes reliability, clear documentation, and a support hub, helping users quickly adopt AI‑enhanced automation without building infrastructure from scratch.
image: https://files.manuscdn.com/user_upload_by_module/web_dev_logo/310519663324634991/rXwQfRfqbgFeklcO.png
json_schemas:
- name: PostApiV1AuthScraperPriceListResponse
  property_count: 3
  slug: prodapi-live-post-api-v1-auth-scraper-price-list-response
- name: PostApiV1B2BDomainEnricherEnrichResponse
  property_count: 7
  slug: prodapi-live-post-api-v1-b2-bdomain-enricher-enrich-response
- name: PostApiV1GoogleMapsLeadExtractorSearchResponse
  property_count: 3
  slug: prodapi-live-post-api-v1-google-maps-lead-extractor-search-response
- name: PostApiV1JsonForgeForgeResponse
  property_count: 3
  slug: prodapi-live-post-api-v1-json-forge-forge-response
- name: PostApiV1RagFeederConvertResponse
  property_count: 5
  slug: prodapi-live-post-api-v1-rag-feeder-convert-response
- name: PostApiV1ReviewSentimentAnalyzerAnalyzeResponse
  property_count: 3
  slug: prodapi-live-post-api-v1-review-sentiment-analyzer-analyze-response
jsonld:
- class_count: 21
  name: Prodapi Live Context
  property_count: 47
  slug: prodapi-live-context
layout: provider
mcp_servers:
- description: Remote MCP server at prodapi.live.
  name: prodapi-live MCP Server
  slug: prodapi-live-mcp-yml
modified: '2026-10-31'
name: prodapi-live
nav: Providers
network: true
overview: 'prodapi-live is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Artificial Intelligence, Data Extraction, and Monitoring.


  The prodapi-live catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  prodapi-live''s developer surface includes documentation, API reference, getting-started guide, support, and 18 more developer resources.'
plans:
- name: Prodapi Live Plans Pricing
  plan_count: 1
  slug: prodapi-live-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Prodapi Live Rate Limits
  slug: prodapi-live-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: prodapi-live API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: prodapi-live-rules
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 68.8
    catalog_earned_first_party: 16.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 23.8
    discoverability: 48.3
    operational_transparency: 26.3
  previous_composite: 37.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/prodapi-live/prodapi-live-2026-11-03T141519.png
security:
- kind: domain-security
  name: Prodapi Live Domain Security
  slug: prodapi-live-domain-security
  summary_line: TLSv1.3 · HSTS
slug: prodapi-live
tags:
- Automation
- Artificial Intelligence
- Data Extraction
- Monitoring
website: https://prodapi.live/
---
