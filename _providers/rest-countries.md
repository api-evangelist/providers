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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
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
artifact_total: 22
collections:
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
created: '2026-05-28'
description: REST Countries is a free, open-source RESTful API that returns rich country reference data — ISO 3166-1 codes (cca2, cca3, ccn3, cioc), common/official and native names, translations, capitals, regions and subregions, continents, currencies, languages, calling codes, top-level domains, timezones, geographic coordinates, borders, area, population, demonyms, flags and coats of arms, postal code formats, Gini index, FIFA code, independence and UN membership status, driving side, and start of week. The canonical hosted instance runs at restcountries.com (v3.1) and the source is community-maintained at github.com/apilayer/restcountries (mirror of gitlab.com/restcountries/restcountries), licensed under MPL-2.0. The hosted API is unauthenticated and free; for production use the project encourages self-hosting from source.
examples:
- key_count: 35
  name: Rest Countries Country Example
  slug: rest-countries-country-example
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/rest-countries.png
json_schemas:
- name: Country
  property_count: 35
  slug: rest-countries-country
json_structures:
- name: Rest Countries Country Structure
  property_count: 35
  slug: rest-countries-country-structure
jsonld:
- class_count: 49
  name: Rest Countries Context
  property_count: 0
  slug: rest-countries-context
layout: provider
modified: '2026-05-29'
name: REST Countries
nav: Providers
network: true
overview: 'REST Countries publishes 11 APIs on the [APIs.io](https://apis.io/) network, including All API, Alpha API, Capital API, and 8 more. Tagged areas include Countries, Geocoding, Geography, ISO 3166, and Open Source.


  The REST Countries catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  REST Countries'' developer surface includes documentation and 9 more developer resources.'
plans:
- name: Rest Countries Plans Pricing
  plan_count: 2
  slug: rest-countries-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Rest Countries Rate Limits
  slug: rest-countries-rate-limits
rules:
- name: REST Countries API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rest-countries-jsonschema-spectral-rules
- name: REST Countries API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 4
  slug: rest-countries-rules
score:
  band: developing
  composite: 43.4
  delta: -4.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 70.6
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rest-countries/refs/heads/main/screenshots/rest-countries-2026-06-20T193003.png
security:
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
