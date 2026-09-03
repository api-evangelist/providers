---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Country Io Agentic Access
  operation_count: 6
  slug: country-io-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://country.io
  baseurl_source: declared
  description: Capital cities by ISO2 code.
  name: Country.io Capitals API
  slug: country-io-capitals-api
- baseURL: https://country.io
  baseurl_source: declared
  description: Continent codes by ISO2 country code.
  name: Country.io Continents API
  slug: country-io-continents-api
- baseURL: https://country.io
  baseurl_source: declared
  description: Currency codes by ISO2 country code.
  name: Country.io Currency API
  slug: country-io-currency-api
- baseURL: https://country.io
  baseurl_source: declared
  description: ISO 3166-1 alpha-3 codes by ISO2 country code.
  name: Country.io ISO3 API
  slug: country-io-iso3-api
- baseURL: https://country.io
  baseurl_source: declared
  description: Country names by ISO2 code.
  name: Country.io Names API
  slug: country-io-names-api
- baseURL: https://country.io
  baseurl_source: declared
  description: International dialing codes by ISO2 country code.
  name: Country.io Phone API
  slug: country-io-phone-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Country.io Data Capitals API
  slug: open-country-io-capitals-api
- collection_type: open
  name: Country.io Data Capitals Continents API
  slug: open-country-io-continents-api
- collection_type: open
  name: Country.io Data Capitals Currency API
  slug: open-country-io-currency-api
- collection_type: open
  name: Country.io Data API
  slug: open-country-io-data
- collection_type: open
  name: Country.io Data Capitals ISO3 API
  slug: open-country-io-iso3-api
- collection_type: open
  name: Country.io Data Capitals Names API
  slug: open-country-io-names-api
- collection_type: open
  name: Country.io Data Capitals Phone API
  slug: open-country-io-phone-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/country-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/country-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://country.io/
- group: other
  title: ''
  type: Data
  url: https://country.io/data/
- group: other
  title: ''
  type: Countries
  url: https://country.io/countries/
- group: other
  title: ''
  type: Rankings
  url: https://country.io/rankings/
- group: operate
  title: ''
  type: Contact
  url: https://country.io/contact/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/country-io-vocabulary.yml
created: '2025-02-21'
description: 'Country.io is a small open data project that publishes a set of static JSON files mapping ISO 3166-1 alpha-2 country codes to common reference data: country names, capital cities, ISO 3166-1 alpha-3 codes, continent codes, international telephone dialing prefixes, and ISO 4217 currency codes. The files are commonly consumed as a lightweight country-data dataset for forms, country pickers, and analytics enrichment.'
finops:
- name: Country Io Finops
  service_category: API
  slug: country-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/country-io.png
layout: provider
modified: '2026-05-19'
name: Country.io
nav: Providers
network: true
overview: 'Country.io publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Capitals API, Continents API, Currency API, and 3 more. Tagged areas include Capitals, Continents, Countries, Currency, and Currency Codes.


  The Country.io catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Country Io Plans Pricing
  plan_count: 3
  slug: country-io-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Country Io Rate Limits
  slug: country-io-rate-limits
rules:
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Country.io API Rules
  rule_count: 7
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 1
  slug: country-io-data-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 40.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 60.6
    contract_quality: 48.3
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 60.6
    operational_transparency: 7.9
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/country-io/refs/heads/main/screenshots/country-io-2026-06-20T175104.png
security:
- kind: domain-security
  name: Country Io Domain Security
  slug: country-io-domain-security
  summary_line: TLSv1.3
slug: country-io
tags:
- Capitals
- Continents
- Countries
- Currency
- Currency Codes
- Dialing Codes
- Geography
- ISO 3166
- JSON
- Open Data
- Phone Codes
- Reference Data
website: https://country.io/
---
