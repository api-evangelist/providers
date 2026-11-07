---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Serpresult Com Agentic Access
  operation_count: 21
  slug: serpresult-com-agentic-access
  summary_line: 21 operations · 10 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.serpresult.com
  baseurl_source: declared
  description: The account behind the calling credential. Accepts an API key or a session cookie. Costs no credits.
  name: SerpResult Account API
  slug: serpresult-com-account-api
- baseURL: https://api.serpresult.com
  baseurl_source: declared
  description: Mint, list, rename, rotate and revoke secret keys. Session only.
  name: SerpResult API keys API
  slug: serpresult-com-api-keys-api
- baseURL: https://api.serpresult.com
  baseurl_source: declared
  description: The account's plan, where it stands against its quota, and buying or moving between plans through Polar. Session only.
  name: SerpResult Billing API
  slug: serpresult-com-billing-api
- baseURL: https://api.serpresult.com
  baseurl_source: declared
  description: Unauthenticated service endpoints.
  name: SerpResult Meta API
  slug: serpresult-com-meta-api
- baseURL: https://api.serpresult.com
  baseurl_source: declared
  description: The metered search endpoints. Accept an API key, a session cookie, the demo header or the marketplace proxy.
  name: SerpResult Search API
  slug: serpresult-com-search-api
- baseURL: https://api.serpresult.com
  baseurl_source: declared
  description: Account-wide reporting read off the query log. Session only.
  name: SerpResult Usage API
  slug: serpresult-com-usage-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/serpresult-com/agentic-access/serpresult-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/serpresult-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/serpresult-com/rate-limits/serpresult-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/serpresult-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/serpresult-com/plans/serpresult-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/serpresult-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/serpresult-com/rules/serpresult-com-rules.yml
  title: ''
  type: Spectral
  url: rules/serpresult-com-rules.yml
- group: design
  href: https://artifacts.apis.io/serpresult-com/json-ld/serpresult-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/serpresult-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/serpresult-com/vocabulary/serpresult-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/serpresult-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/serpresult-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/serpresult-com/data-model/serpresult-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/serpresult-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/serpresult-com/authentication/serpresult-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/serpresult-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/serpresult-com/lifecycle/serpresult-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/serpresult-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/serpresult-com/errors/serpresult-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/serpresult-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/serpresult-com/conformance/serpresult-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/serpresult-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/serpresult-com/llms/serpresult-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/serpresult-com-llms.txt
- group: other
  href: https://artifacts.apis.io/serpresult-com/hosts/serpresult-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/serpresult-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/serpresult-com/vendors/serpresult-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/serpresult-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/serpresult-com/security/serpresult-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/serpresult-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://serpresult.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.serpresult.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.serpresult.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.serpresult.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.serpresult.com/help/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://docs.serpresult.com/help/
- group: commercial
  title: ''
  type: Pricing
  url: https://serpresult.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.serpresult.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://serpresult.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://serpresult.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://serpresult.com/status
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.serpresult.com/openapi.json
  - status: null
    url: https://docs.serpresult.com/openapi.json
  - status: 401
    url: https://api.serpresult.com/mcp
  - status: 200
    url: https://serpresult.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: SerpResult is a SERP API that returns the organic results of a Google, Bing, DuckDuckGo, Yahoo, Brave or Yandex search as JSON over one HTTP call, resolved from any of 193 countries. It provides a simple REST endpoint to query search engine results, supporting parameters for location, language, device type, and safe search. The service includes rate limiting, bulk query capabilities, and detailed result fields such as titles, snippets, URLs, and rich snippets. SerpResult aims to help developers, marketers, and data analysts integrate search data into applications without scraping.
image: https://www.serpresult.com/brand/logo.png
json_schemas:
- name: BillingSummaryResponse
  property_count: 9
  slug: serpresult-com-billing-summary-response
- name: BulkRequest
  property_count: 5
  slug: serpresult-com-bulk-request
- name: BulkResponse
  property_count: 5
  slug: serpresult-com-bulk-response
- name: Me
  property_count: 4
  slug: serpresult-com-me
- name: SearchResponse
  property_count: 7
  slug: serpresult-com-search-response
- name: UsageSummaryResponse
  property_count: 7
  slug: serpresult-com-usage-summary-response
jsonld:
- class_count: 44
  name: Serpresult Com Context
  property_count: 89
  slug: serpresult-com-context
layout: provider
modified: '2026-10-31'
name: SerpResult
nav: Providers
network: true
overview: 'SerpResult publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, API keys API, Billing API, and 3 more. Tagged areas include Search, SERP, Data, JSON, and Cloud.


  The SerpResult catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SerpResult''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 20 more developer resources.'
plans:
- name: Serpresult Com Plans Pricing
  plan_count: 4
  slug: serpresult-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Serpresult Com Rate Limits
  slug: serpresult-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: SerpResult API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: serpresult-com-rules
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.3
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 66.5
    developer_ergonomics: 39.8
    discoverability: 66.1
    operational_transparency: 39.5
  previous_composite: 60.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/serpresult-com/serpresult-com-2026-11-03T143053.png
security:
- kind: authentication
  name: Serpresult Com Authentication
  slug: serpresult-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Serpresult Com Domain Security
  slug: serpresult-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 7
skills:
- name: serpresult-com-billing-purchase
  slug: serpresult-com-billing-purchase
- name: bulk
  slug: serpresult-com-bulk-skill
- name: getme
  slug: serpresult-com-getme-skill
- name: serpresult-com-manage-api-keys
  slug: serpresult-com-manage-api-keys
- name: query
  slug: serpresult-com-query-skill
- name: serpresult-com-search-multiple
  slug: serpresult-com-search-multiple
- name: usage-summary
  slug: serpresult-com-usage-summary-skill
slug: serpresult-com
tags:
- Search
- SERP
- Data
- JSON
- Cloud
website: https://serpresult.com/
---
