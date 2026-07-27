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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Basetrip Agentic Access
  operation_count: 9
  slug: basetrip-agentic-access
  summary_line: 9 operations
api_count: 7
apis:
- description: The Cities API from Basetrip — 2 operation(s) for cities.
  name: Basetrip Cities API
  slug: basetrip-cities-api
- description: The Cost API from Basetrip — 1 operation(s) for cost.
  name: Basetrip Cost API
  slug: basetrip-cost-api
- description: The Countries API from Basetrip — 2 operation(s) for countries.
  name: Basetrip Countries API
  slug: basetrip-countries-api
- description: The Health API from Basetrip — 1 operation(s) for health.
  name: Basetrip Health API
  slug: basetrip-health-api
- description: The Phrases API from Basetrip — 1 operation(s) for phrases.
  name: Basetrip Phrases API
  slug: basetrip-phrases-api
- description: The Safety API from Basetrip — 1 operation(s) for safety.
  name: Basetrip Safety API
  slug: basetrip-safety-api
- description: The Visa API from Basetrip — 1 operation(s) for visa.
  name: Basetrip Visa API
  slug: basetrip-visa-api
artifact_total: 68
collections:
- collection_type: open
  name: Basetrip API
  slug: open-basetrip-api
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
random_paper: 42
rate_limits:
- limit_count: 5
  name: Basetrip Rate Limits
  slug: basetrip-rate-limits
rules:
- name: Basetrip API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: basetrip-jsonschema-spectral-rules
- name: Basetrip API Rules
  rule_count: 22
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 15
  slug: basetrip-spectral-rules
score:
  band: developing
  composite: 52.7
  delta: 2.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.1
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 31.6
  previous_composite: 49.9
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
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
