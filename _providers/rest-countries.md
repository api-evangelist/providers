---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Rest Countries Agentic Access
  operation_count: 12
  slug: rest-countries-agentic-access
  summary_line: 12 operations
api_count: 11
apis:
- description: Bulk retrieval of every country in the dataset.
  name: REST Countries All API
  slug: rest-countries-all-api
- description: Lookup countries by ISO 3166-1 alpha-2, alpha-3, numeric, or CIOC code.
  name: REST Countries Alpha API
  slug: rest-countries-alpha-api
- description: Lookup countries by capital city.
  name: REST Countries Capital API
  slug: rest-countries-capital-api
- description: Lookup countries by ISO 4217 currency code or currency name.
  name: REST Countries Currency API
  slug: rest-countries-currency-api
- description: Lookup countries by demonym (citizen designation).
  name: REST Countries Demonym API
  slug: rest-countries-demonym-api
- description: Lookup countries filtered by ISO 3166-1 independence status.
  name: REST Countries Independent API
  slug: rest-countries-independent-api
- description: Lookup countries by ISO 639 language code or language name.
  name: REST Countries Language API
  slug: rest-countries-language-api
- description: Lookup countries by common or official name.
  name: REST Countries Name API
  slug: rest-countries-name-api
- description: Lookup countries within a UN geographic region.
  name: REST Countries Region API
  slug: rest-countries-region-api
- description: Lookup countries within a UN geographic subregion.
  name: REST Countries Subregion API
  slug: rest-countries-subregion-api
- description: Lookup countries by translated name.
  name: REST Countries Translation API
  slug: rest-countries-translation-api
artifact_total: 45
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: REST Countries All API
  slug: open-rest-countries-all-api
- collection_type: open
  name: REST Countries All Alpha API
  slug: open-rest-countries-alpha-api
- collection_type: open
  name: REST Countries All Capital API
  slug: open-rest-countries-capital-api
- collection_type: open
  name: REST Countries API
  slug: open-rest-countries-countries-api
- collection_type: open
  name: REST Countries All Currency API
  slug: open-rest-countries-currency-api
- collection_type: open
  name: REST Countries All Demonym API
  slug: open-rest-countries-demonym-api
- collection_type: open
  name: REST Countries All Independent API
  slug: open-rest-countries-independent-api
- collection_type: open
  name: REST Countries All Language API
  slug: open-rest-countries-language-api
- collection_type: open
  name: REST Countries All Name API
  slug: open-rest-countries-name-api
- collection_type: open
  name: REST Countries All Region API
  slug: open-rest-countries-region-api
- collection_type: open
  name: REST Countries All Subregion API
  slug: open-rest-countries-subregion-api
- collection_type: open
  name: REST Countries All Translation API
  slug: open-rest-countries-translation-api
- collection_type: open
  name: REST Countries
  slug: open-rest-countries
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rest-countries-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rest-countries-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://restcountries.com
- group: docs
  title: ''
  type: Documentation
  url: https://restcountries.com
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apilayer/restcountries
- group: other
  title: ''
  type: SourceRepository
  url: https://gitlab.com/restcountries/restcountries
- group: other
  title: ''
  type: Mirror
  url: https://github.com/restcountries/restcountries
- group: commercial
  title: ''
  type: License
  url: https://www.mozilla.org/en-US/MPL/2.0/
- group: design
  title: ''
  type: SpectralRules
  url: rules/rest-countries-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rest-countries-vocabulary.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rest-countries-authentication.yml
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/apilayer/restcountries
- group: commercial
  title: ''
  type: Pricing
  url: https://restcountries.com/plans
- group: operate
  title: ''
  type: StatusPage
  url: https://status.restcountries.com
- group: commercial
  title: ''
  type: Plans
  url: plans/rest-countries-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rest-countries-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rest-countries-finops.yml
created: '2026-05-28'
description: REST Countries is a free, open-source RESTful API that returns rich country reference data — ISO 3166-1 codes (cca2, cca3, ccn3, cioc), common/official and native names, translations, capitals, regions and subregions, continents, currencies, languages, calling codes, top-level domains, timezones, geographic coordinates, borders, area, population, demonyms, flags and coats of arms, postal code formats, Gini index, FIFA code, independence and UN membership status, driving side, and start of week. The canonical hosted instance runs at restcountries.com (v3.1) and the source is community-maintained at github.com/apilayer/restcountries (mirror of gitlab.com/restcountries/restcountries), licensed under MPL-2.0. The hosted API is unauthenticated and free; for production use the project encourages self-hosting from source.
examples:
- key_count: 1
  name: Error 401 Unauthorized
  slug: error-401-unauthorized
- key_count: 1
  name: List All Countries Response
  slug: list-all-countries-response
- key_count: 1
  name: Lookup By Alpha2 Code Response
  slug: lookup-by-alpha2-code-response
- key_count: 35
  name: Rest Countries Country Example
  slug: rest-countries-country-example
- key_count: 1
  name: Search By Name Response
  slug: search-by-name-response
finops:
- name: Rest Countries Finops
  service_category: ''
  slug: rest-countries-finops
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/rest-countries.png
json_schemas:
- name: CountriesListResponse
  property_count: 1
  slug: countries-list-response
- name: Country
  property_count: 29
  slug: country
- name: ErrorResponse
  property_count: 1
  slug: error-response
- name: Country
  property_count: 35
  slug: rest-countries-country
json_structures:
- name: Rest Countries Country Structure
  property_count: 35
  slug: rest-countries-country-structure
jsonld:
- class_count: 0
  name: Rest Countries Api Context
  property_count: 0
  slug: rest-countries-api
- class_count: 49
  name: Rest Countries Context
  property_count: 0
  slug: rest-countries-context
layout: provider
modified: '2026-08-08'
name: REST Countries
nav: Providers
network: true
overview: 'REST Countries publishes 11 APIs on the [APIs.io](https://apis.io/) network, including All API, Alpha API, Capital API, and 8 more. Tagged areas include Countries, Geocoding, Geography, ISO 3166, and Open Source.


  The REST Countries catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  REST Countries'' developer surface includes documentation, authentication, pricing, and 14 more developer resources.'
plans:
- name: Rest Countries Plans Pricing
  plan_count: 2
  slug: rest-countries-plans-pricing
random_paper: 138
rate_limits:
- limit_count: 3
  name: Rest Countries Rate Limits
  slug: rest-countries-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: REST Countries API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rest-countries-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: REST Countries API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 4
  slug: rest-countries-rules
score:
  band: developing
  composite: 46.4
  delta: -5.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 25.0
    contract_quality: 68.0
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 52.6
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/rest-countries/refs/heads/main/screenshots/rest-countries-2026-06-20T193018.png
security:
- kind: authentication
  name: Rest Countries Authentication
  slug: rest-countries-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Rest Countries Domain Security
  slug: rest-countries-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rest-countries
tags:
- Countries
- Geocoding
- Geography
- ISO 3166
- Open Source
- Public APIs
- Reference Data
- Currencies
- Languages
- Capitals
- Regions
- Subregions
- Translations
website: https://restcountries.com
---
