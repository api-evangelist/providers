---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Country State City Api Agentic Access
  operation_count: 9
  slug: country-state-city-api-agentic-access
  summary_line: 9 operations
api_count: 3
apis:
- description: City reference data with coordinates and time zones, scoped by country and state.
  name: Country State City API Cities API
  slug: country-state-city-api-cities-api
- description: Country reference data including ISO codes, currencies, phone codes, and regions.
  name: Country State City API Countries API
  slug: country-state-city-api-countries-api
- description: State, province, and region reference data scoped by country.
  name: Country State City API States API
  slug: country-state-city-api-states-api
artifact_total: 11
collections:
- collection_type: open
  name: Country State City API
  slug: open-country-state-city-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/country-state-city-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/country-state-city-api-domain-security.yml
- group: auth
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
- name: Country State City Api Finops
  service_category: API
  slug: country-state-city-api-finops
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/country-state-city-api.png
layout: provider
modified: '2026-05-19'
name: Country State City API
nav: Providers
network: true
overview: 'Country State City API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Cities API, Countries API, and States API. Tagged areas include Capitals, Cities, Countries, Currencies, and Geography.


  The Country State City API catalog on APIs.io includes 1 Spectral governance ruleset.


  Country State City API''s developer surface includes authentication, documentation, developer console, pricing, and 11 more developer resources.'
plans:
- name: Country State City Api Plans Pricing
  plan_count: 3
  slug: country-state-city-api-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Country State City Api Rate Limits
  slug: country-state-city-api-rate-limits
rules:
- name: Country State City API API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: country-state-city-api-rules
score:
  band: developing
  composite: 49.8
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 60.5
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 31.3
    operational_transparency: 31.6
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/country-state-city-api/refs/heads/main/screenshots/country-state-city-api-2026-06-20T175144.png
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
- Capitals
- Cities
- Countries
- Currencies
- Geography
- Geolocation
- ISO 3166
- JSON
- Phone Codes
- Provinces
- Reference Data
- Regions
- States
- Time Zones
website: https://countrystatecity.in/
---
