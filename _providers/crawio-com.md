---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
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
  score: 25.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Crawio offers a single POST endpoint to scrape any web page, handling proxies, anti-bot detection, optional JavaScript rendering, and session management.
  name: Crawio Web Scraping API
  slug: crawio-web-scraping-api
- baseURL: https://api.crawio.com
  baseurl_source: declared
  description: 'crawio-com API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: crawio-com API
  slug: crawio-com-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/crawio-com/rate-limits/crawio-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crawio-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/crawio-com/plans/crawio-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crawio-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/crawio-com/rules/crawio-com-rules.yml
  title: ''
  type: Spectral
  url: rules/crawio-com-rules.yml
- group: design
  href: https://artifacts.apis.io/crawio-com/json-ld/crawio-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crawio-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/crawio-com/vocabulary/crawio-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crawio-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/crawio-com/data-model/crawio-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crawio-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/crawio-com/conventions/crawio-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/crawio-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/crawio-com/conventions/crawio-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/crawio-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/crawio-com/authentication/crawio-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crawio-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/crawio-com/errors/crawio-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crawio-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crawio-com/conformance/crawio-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crawio-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/crawio-com/hosts/crawio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crawio-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/crawio-com/vendors/crawio-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crawio-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/crawio-com/security/crawio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crawio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crawio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://crawio.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://crawio.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://crawio.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://crawio.com/support/
- group: company
  title: ''
  type: Blog
  url: https://crawio.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://crawio.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crawio.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crawio.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://crawio.com/signup/
coverage:
  checked: '2026-10-30'
  detail: The provider's documentation is public HTML but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other spec is published.
  evidence:
  - status: 200
    url: https://crawio.com/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Crawio provides a web scraping API that handles proxies, anti-bot detection, and offers a single endpoint to fetch any web page from any country. It supports optional JavaScript rendering, session handling, and returns status, headers, and body. Users can start for free without a credit card. The service includes AI integration prompts, detailed pricing plans, and comprehensive documentation.
image: https://crawio.com/og.png
json_schemas:
- name: GetAccountResponse
  property_count: 10
  slug: crawio-com-get-account-response
- name: GetPluginGoogleMapsReviewsResponse
  property_count: 6
  slug: crawio-com-get-plugin-google-maps-reviews-response
- name: GetPluginGoogleMapsSearchResponse
  property_count: 5
  slug: crawio-com-get-plugin-google-maps-search-response
- name: PostScrapeRequest
  property_count: 1
  slug: crawio-com-post-scrape-request
jsonld:
- class_count: 4
  name: Crawio Com Context
  property_count: 19
  slug: crawio-com-context
layout: provider
modified: '2026-10-30'
name: crawio-com
nav: Providers
network: true
overview: 'crawio-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Web Scraping, Proxy, Anti-Bot, and Data Extraction.


  The crawio-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  crawio-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Crawio Com Plans Pricing
  plan_count: 5
  slug: crawio-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Crawio Com Rate Limits
  slug: crawio-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: crawio-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: crawio-com-rules
scopes:
- name: Crawio Com Scopes
  scope_count: 0
  slug: crawio-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 78.8
    catalog_earned_first_party: 24.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 29.8
    discoverability: 57.1
    operational_transparency: 31.6
  previous_composite: 46.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/crawio-com/crawio-com-2026-11-03T125528.png
security:
- kind: authentication
  name: Crawio Com Authentication
  slug: crawio-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Crawio Com Domain Security
  slug: crawio-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: crawio-com
tags:
- Web Scraping
- Proxy
- Anti-Bot
- Data Extraction
website: https://crawio.com/
---
