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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Custom Search Agentic Access
  operation_count: 2
  slug: google-custom-search-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://customsearch.googleapis.com
  baseurl_source: declared
  description: The Custom Search API from Google Custom Search — 2 operation(s) for custom search.
  name: Google Custom Search Custom Search API
  slug: google-custom-search-custom-search-api
artifact_total: 15
collections:
- collection_type: postman
  name: Google Custom Search JSON Customsearch API
  slug: postman-google-custom-search-customsearch-api
- collection_type: open
  name: Google Custom Search JSON Customsearch API
  slug: open-google-custom-search-customsearch-api
- collection_type: open
  name: Google Custom Search JSON API
  slug: open-openapi
common:
- group: commercial
  href: https://artifacts.apis.io/google-custom-search/plans/google-custom-search-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-custom-search-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-custom-search/rate-limits/google-custom-search-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-custom-search-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-custom-search/finops/google-custom-search-finops.yml
  title: ''
  type: FinOps
  url: finops/google-custom-search-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-custom-search/overview
- group: agent
  href: https://artifacts.apis.io/google-custom-search/agentic-access/google-custom-search-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-custom-search-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-custom-search/security/google-custom-search-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-custom-search-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-custom-search/security/google-custom-search-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-custom-search-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-custom-search/authentication/google-custom-search-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-custom-search-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/custom-search
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/custom-search/v1/overview
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/custom-search/v1/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/custom-search/v1/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/custom-search/v1/overview#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/custom-search/v1/overview#support
- group: design
  href: https://artifacts.apis.io/google-custom-search/json-ld/context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
created: '2026-03-13'
description: The Google Custom Search JSON API allows programmatic searches over a website or collection of websites. It returns metadata about the search performed, metadata about the search engine used, and the search results including web pages and images.
finops:
- has_sources: true
  method: derived
  name: Google Custom Search Finops
  primary_unit: queries per day
  service_category: ''
  slug: google-custom-search-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-custom-search.png
json_schemas:
- name: Google Custom Search Result
  property_count: 14
  slug: SearchResult
jsonld:
- class_count: 14
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Custom Search
nav: Providers
network: true
overview: 'Google Custom Search publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Custom Search API. Tagged areas include Custom Search, Google, Image Search, Search, and Web Search.


  The Google Custom Search catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Custom Search''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 13 more developer resources.'
plans:
- name: Google Custom Search Plans Pricing
  plan_count: 2
  slug: google-custom-search-plans-pricing
- name: Google Custom Search Price Estimates
  plan_count: 0
  slug: google-custom-search-price-estimates
random_paper: 8
rate_limits:
- limit_count: 5
  name: Google Custom Search Rate Limits
  slug: google-custom-search-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Custom Search — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-custom-search-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 67.7
    catalog_earned_first_party: 8.0
    catalog_gap: 47.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 9.8
    contract_quality: 56.3
    developer_ergonomics: 51.9
    discoverability: 66.1
    operational_transparency: 34.2
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/google-custom-search/google-custom-search-2026-06-20T182152.png
security:
- kind: authentication
  name: Google Custom Search Authentication
  slug: google-custom-search-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Google Custom Search Domain Security
  slug: google-custom-search-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Custom Search Vulnerability Disclosure
  slug: google-custom-search-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-custom-search
tags:
- Custom Search
- Google
- Image Search
- Search
- Web Search
website: https://www.google.com/
---
