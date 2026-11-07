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
  band: agent-ready
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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Country State City Api Agentic Access
  operation_count: 9
  slug: country-state-city-api-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- baseURL: https://api.countrystatecity.in/v1
  baseurl_source: declared
  description: City reference data with coordinates and time zones, scoped by country and state.
  name: Country State City API Cities API
  slug: country-state-city-api-cities-api
- baseURL: https://api.countrystatecity.in/v1
  baseurl_source: declared
  description: Country reference data including ISO codes, currencies, phone codes, and regions.
  name: Country State City API Countries API
  slug: country-state-city-api-countries-api
- baseURL: https://api.countrystatecity.in/v1
  baseurl_source: declared
  description: State, province, and region reference data scoped by country.
  name: Country State City API States API
  slug: country-state-city-api-states-api
artifact_total: 15
collections:
- collection_type: open
  name: Country State City Cities API
  slug: open-country-state-city-api-cities-api
- collection_type: open
  name: Country State City Cities Countries API
  slug: open-country-state-city-api-countries-api
- collection_type: open
  name: Country State City Cities States API
  slug: open-country-state-city-api-states-api
- collection_type: open
  name: Country State City API
  slug: open-country-state-city-api
common:
- group: commercial
  href: https://artifacts.apis.io/country-state-city-api/plans/country-state-city-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/country-state-city-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/country-state-city-api/rate-limits/country-state-city-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/country-state-city-api-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/country-state-city-api/finops/country-state-city-api-finops.yml
  title: ''
  type: FinOps
  url: finops/country-state-city-api-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://countrystatecity.in/blog/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/dr5hn/countries-states-cities-database/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/dr5hn/countries-states-cities-database/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/dr5hn/countries-states-cities-database/blob/master/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/dr5hn/countries-states-cities-database/blob/master/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/dr5hn/countries-states-cities-database/blob/master/LICENSE
- group: agent
  href: https://artifacts.apis.io/country-state-city-api/agentic-access/country-state-city-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/country-state-city-api-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/country-state-city-api/security/country-state-city-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/country-state-city-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/country-state-city-api/authentication/country-state-city-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/country-state-city-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://countrystatecity.in/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.countrystatecity.in/
- group: other
  title: ''
  type: APIIntroduction
  url: https://docs.countrystatecity.in/api/introduction
- group: start
  title: ''
  type: Console
  url: https://app.countrystatecity.in/
- group: commercial
  title: ''
  type: Pricing
  url: https://countrystatecity.in/pricing/
- group: other
  title: ''
  type: Downloads
  url: https://countrystatecity.in/downloads/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/dr5hn/countries-states-cities-database
- group: operate
  title: ''
  type: Contact
  url: https://countrystatecity.in/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://countrystatecity.in/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://countrystatecity.in/terms/
- group: design
  href: https://artifacts.apis.io/country-state-city-api/vocabulary/country-state-city-api-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/country-state-city-api-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.countrystatecity.in/llms.txt
created: '2024-03-30'
description: The Country State City API is a global geographic reference dataset and REST API published by countrystatecity.in. It exposes 247+ countries, 5,000+ states / provinces, and 150,000+ cities with ISO 3166 codes, phone codes, capitals, currencies, native names, regions, sub-regions, coordinates, time zones, and flag emoji. The data is also distributed as downloadable JSON, SQL, PostgreSQL, SQLite, XML, YAML, and CSV bundles for offline use, and the live API is authenticated with the X-CSCAPI-KEY header from a free developer plan.
finops:
- has_sources: false
  method: generated
  name: Country State City Api Finops
  primary_unit: request
  service_category: API
  slug: country-state-city-api-finops
  template: true
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/country-state-city-api.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.countrystatecity.in over HTTP; 3 tools listed.
  name: Country State City API MCP Server
  slug: country-state-city-api
modified: '2026-10-06'
name: Country State City API
nav: Providers
network: true
overview: 'Country State City API publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Cities API, Countries API, and States API. Tagged areas include Capital, Cities, Countries, Currency, and Geography.


  The Country State City API catalog on APIs.io includes 1 Spectral governance ruleset.


  Country State City API''s developer surface includes engineering blog, authentication, documentation, developer console, pricing, and 19 more developer resources.'
plans:
- name: Country State City Api Plans Pricing
  plan_count: 3
  slug: country-state-city-api-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Country State City Api Rate Limits
  slug: country-state-city-api-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Country State City API API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: country-state-city-api-rules
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 51.3
    catalog_earned_first_party: 0.0
    catalog_gap: 63.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.5
  facets:
    access_clarity: 52.6
    contract_governance: 25.0
    contract_quality: 47.8
    developer_ergonomics: 23.8
    discoverability: 75.0
    operational_transparency: 28.9
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/country-state-city-api/country-state-city-api-2026-06-20T175144.png
security:
- kind: authentication
  name: Country State City Api Authentication
  slug: country-state-city-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Country State City Api Domain Security
  slug: country-state-city-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: country-state-city-api
tags:
- Capital
- Cities
- Countries
- Currency
- Geography
- Geolocation
- ISO 3166
- JSON
- Phone Codes
- Provinces
- Reference Data
- Regions
- States
- Timezone
website: https://countrystatecity.in/
---
