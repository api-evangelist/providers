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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Basetrip Agentic Access
  operation_count: 9
  slug: basetrip-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- baseURL: https://api.thebasetrip.com/v3
  baseurl_source: declared
  description: The Cities API from Basetrip — 2 operation(s) for cities.
  name: Basetrip Cities API
  slug: basetrip-cities-api
- baseURL: https://api.thebasetrip.com/v3
  baseurl_source: declared
  description: The Cost API from Basetrip — 1 operation(s) for cost.
  name: Basetrip Cost API
  slug: basetrip-cost-api
- baseURL: https://api.thebasetrip.com/v3
  baseurl_source: declared
  description: The Countries API from Basetrip — 2 operation(s) for countries.
  name: Basetrip Countries API
  slug: basetrip-countries-api
- baseURL: https://api.thebasetrip.com/v3
  baseurl_source: declared
  description: The Health API from Basetrip — 1 operation(s) for health.
  name: Basetrip Health API
  slug: basetrip-health-api
- baseURL: https://api.thebasetrip.com/v3
  baseurl_source: declared
  description: The Phrases API from Basetrip — 1 operation(s) for phrases.
  name: Basetrip Phrases API
  slug: basetrip-phrases-api
- baseURL: https://api.thebasetrip.com/v3
  baseurl_source: declared
  description: The Safety API from Basetrip — 1 operation(s) for safety.
  name: Basetrip Safety API
  slug: basetrip-safety-api
- baseURL: https://api.thebasetrip.com/v3
  baseurl_source: declared
  description: The Visa API from Basetrip — 1 operation(s) for visa.
  name: Basetrip Visa API
  slug: basetrip-visa-api
artifact_total: 76
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Basetrip API
  slug: open-basetrip-api
- collection_type: open
  name: Basetrip Cities API
  slug: open-basetrip-cities-api
- collection_type: open
  name: Basetrip Cities Cost API
  slug: open-basetrip-cost-api
- collection_type: open
  name: Basetrip Cities Countries API
  slug: open-basetrip-countries-api
- collection_type: open
  name: Basetrip Cities Health API
  slug: open-basetrip-health-api
- collection_type: open
  name: Basetrip Cities Phrases API
  slug: open-basetrip-phrases-api
- collection_type: open
  name: Basetrip Cities Safety API
  slug: open-basetrip-safety-api
- collection_type: open
  name: Basetrip Cities Visa API
  slug: open-basetrip-visa-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/basetrip-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/basetrip-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/basetrip-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-basetrip
- group: company
  title: ''
  type: Website
  url: https://www.thebasetrip.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thebasetrip.com/en/documentation/v3
- group: start
  title: ''
  type: Signup
  url: https://www.thebasetrip.com/en/sign_up
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thebasetrip.com/en/pricing
- group: design
  title: ''
  type: SpectralRules
  url: rules/basetrip-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/basetrip-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/basetrip-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://api.thebasetrip.com/llms.txt
created: '2024-11-13'
description: Basetrip is a travel intelligence platform providing APIs for country and city data, travel phrases, safety ratings, visa requirements, cost of living estimates, and health advisories. Designed to help travel apps, booking platforms, and trip planning tools differentiate their products and improve traveler experiences. The Basetrip API v3 uses API key authentication and returns JSON.
examples:
- key_count: 3
  name: City
  slug: city
- key_count: 4
  name: Citydetail
  slug: citydetail
- key_count: 2
  name: Citylistresponse
  slug: citylistresponse
- key_count: 5
  name: Costinfo
  slug: costinfo
- key_count: 4
  name: Country
  slug: country
- key_count: 5
  name: Countrydetail
  slug: countrydetail
- key_count: 2
  name: Countrylistresponse
  slug: countrylistresponse
- key_count: 3
  name: Errorresponse
  slug: errorresponse
- key_count: 5
  name: Healthinfo
  slug: healthinfo
- key_count: 4
  name: Phrase
  slug: phrase
- key_count: 2
  name: Phraselistresponse
  slug: phraselistresponse
- key_count: 5
  name: Safetyinfo
  slug: safetyinfo
- key_count: 5
  name: Visainfo
  slug: visainfo
features:
- description: Country names, slugs, alpha-2 codes, capital, currency, languages, population, and timezone.
  name: Country Data
- description: City names, slugs, geographic coordinates, and timezone information per country.
  name: City Data
- description: Language phrases for travel in English, French, German, Italian, and Spanish.
  name: Travel Phrases
- description: Country safety ratings and travel advisory levels from 1 (normal) to 4 (do not travel).
  name: Safety Ratings
- description: Daily budget estimates for budget, mid-range, and luxury traveler tiers.
  name: Cost Estimates
- description: Visa requirement lookup by passport country and destination country.
  name: Visa Requirements
- description: Vaccination requirements, health risks, drinking water safety, and medical facility ratings.
  name: Health Advisories
finops:
- name: Basetrip Finops
  service_category: API
  slug: basetrip-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/basetrip.png
json_schemas:
- name: City
  property_count: 3
  slug: city
- name: CityDetail
  property_count: 0
  slug: citydetail
- name: CityListResponse
  property_count: 2
  slug: citylistresponse
- name: CostInfo
  property_count: 6
  slug: costinfo
- name: Country
  property_count: 4
  slug: country
- name: CountryDetail
  property_count: 0
  slug: countrydetail
- name: CountryListResponse
  property_count: 2
  slug: countrylistresponse
- name: ErrorResponse
  property_count: 3
  slug: errorresponse
- name: HealthInfo
  property_count: 5
  slug: healthinfo
- name: Phrase
  property_count: 4
  slug: phrase
- name: PhraseListResponse
  property_count: 2
  slug: phraselistresponse
- name: SafetyInfo
  property_count: 5
  slug: safetyinfo
- name: VisaInfo
  property_count: 5
  slug: visainfo
json_structures:
- name: City
  property_count: 0
  slug: city
- name: Citydetail
  property_count: 0
  slug: citydetail
- name: Citylistresponse
  property_count: 0
  slug: citylistresponse
- name: Costinfo
  property_count: 0
  slug: costinfo
- name: Country
  property_count: 0
  slug: country
- name: Countrydetail
  property_count: 0
  slug: countrydetail
- name: Countrylistresponse
  property_count: 0
  slug: countrylistresponse
- name: Errorresponse
  property_count: 0
  slug: errorresponse
- name: Healthinfo
  property_count: 0
  slug: healthinfo
- name: Phrase
  property_count: 0
  slug: phrase
- name: Phraselistresponse
  property_count: 0
  slug: phraselistresponse
- name: Safetyinfo
  property_count: 0
  slug: safetyinfo
- name: Visainfo
  property_count: 0
  slug: visainfo
jsonld:
- class_count: 8
  name: Basetrip Context
  property_count: 32
  slug: basetrip-context
layout: provider
modified: '2026-05-19'
name: Basetrip
nav: Providers
network: true
overview: 'Basetrip publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Cities API, Cost API, Countries API, and 4 more. Tagged areas include Cities, Countries, Health, Safety, and Travel.


  The Basetrip catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Basetrip''s developer surface includes authentication, documentation, signup flow, pricing, and 8 more developer resources.'
plans:
- name: Basetrip Plans Pricing
  plan_count: 3
  slug: basetrip-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Basetrip Rate Limits
  slug: basetrip-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Basetrip API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: basetrip-jsonschema-spectral-rules
- effective_rule_count: 63
  extends:
  - spectral:oas
  name: Basetrip API Rules
  rule_count: 22
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 15
  slug: basetrip-spectral-rules
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 63.3
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/basetrip/refs/heads/main/screenshots/basetrip-2026-06-20T173027.png
security:
- kind: authentication
  name: Basetrip Authentication
  slug: basetrip-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Basetrip Domain Security
  slug: basetrip-domain-security
  summary_line: TLSv1.3
slug: basetrip
tags:
- Cities
- Countries
- Health
- Safety
- Travel
- Visa
use_cases:
- description: Embed country and city intelligence directly into travel booking apps.
  name: Travel App Integration
- description: Provide travelers with safety, cost, and visa information before booking.
  name: Trip Planning Tools
- description: Power destination content with live data on safety, costs, and health.
  name: Destination Guides
- description: Assess travel risk using safety ratings and health advisories for corporate travel.
  name: Travel Risk Assessment
- description: Surface travel phrases in destination language for traveler communication tools.
  name: Language Assistance
website: https://www.thebasetrip.com/
---
