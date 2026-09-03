---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
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
    openapi_examples: partial
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
  name: Disease Sh Agentic Access
  operation_count: 41
  slug: disease-sh-agentic-access
  summary_line: 41 operations
api_count: 1
apis:
- baseURL: https://disease.sh/v3
  baseurl_source: declared
  description: (COVID-19 related mobility trend data from Apple, updated every 24 hours)
  name: 'disease.sh COVID-19: Apple API'
  slug: disease-sh-covid-19-apple-api
- baseURL: https://disease.sh/v3
  baseurl_source: declared
  description: (COVID-19 individual government reported data, updated every 24 hours)
  name: 'disease.sh COVID-19: Government API'
  slug: disease-sh-covid-19-government-api
- baseURL: https://disease.sh/v3
  baseurl_source: declared
  description: (COVID-19 data sourced from Johns Hopkins University, updated every 10 minutes)
  name: 'disease.sh COVID-19: JHUCSSE API'
  slug: disease-sh-covid-19-jhucsse-api
- baseURL: https://disease.sh/v3
  baseurl_source: declared
  description: (COVID-19 data sourced from the New York Times, updated every 24 hours)
  name: 'disease.sh COVID-19: NYT API'
  slug: disease-sh-covid-19-nyt-api
- baseURL: https://disease.sh/v3
  baseurl_source: declared
  description: (COVID-19 therapeutic trial data from raps.org, updated every 24 hours)
  name: 'disease.sh COVID-19: Therapeutics API'
  slug: disease-sh-covid-19-therapeutics-api
- baseURL: https://disease.sh/v3
  baseurl_source: declared
  description: (COVID-19 vaccine trial data from raps.org, updated every 24 hours)
  name: 'disease.sh COVID-19: Vaccine API'
  slug: disease-sh-covid-19-vaccine-api
- baseURL: https://disease.sh/v3
  baseurl_source: declared
  description: (COVID-19 data from The European Surveillance System -TESSy, provided by [Austria, Belgium, Bulgaria, Croatia, Cyprus, Czechia, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ir
  name: 'disease.sh COVID-19: Variants API'
  slug: disease-sh-covid-19-variants-api
- baseURL: https://disease.sh/v3
  baseurl_source: declared
  description: (COVID-19 data sourced from Worldometers, updated every 10 minutes)
  name: 'disease.sh COVID-19: Worldometers API'
  slug: disease-sh-covid-19-worldometers-api
- baseURL: https://disease.sh/v3
  baseurl_source: declared
  description: (Influenza data reported by the United States CDC, updated every 24 hours)
  name: 'disease.sh Influenza: CDC API'
  slug: disease-sh-influenza-cdc-api
artifact_total: 84
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 'disease.sh Docs - An open API for disease-related statistics COVID-19: Apple API'
  slug: open-disease-sh-covid-19-apple-api
- collection_type: open
  name: 'disease.sh Docs - An open API for disease-related statistics COVID-19: Apple COVID-19: Government API'
  slug: open-disease-sh-covid-19-government-api
- collection_type: open
  name: 'disease.sh Docs - An open API for disease-related statistics COVID-19: Apple COVID-19: JHUCSSE API'
  slug: open-disease-sh-covid-19-jhucsse-api
- collection_type: open
  name: 'disease.sh Docs - An open API for disease-related statistics COVID-19: Apple COVID-19: NYT API'
  slug: open-disease-sh-covid-19-nyt-api
- collection_type: open
  name: 'disease.sh Docs - An open API for disease-related statistics COVID-19: Apple COVID-19: Therapeutics API'
  slug: open-disease-sh-covid-19-therapeutics-api
- collection_type: open
  name: 'disease.sh Docs - An open API for disease-related statistics COVID-19: Apple COVID-19: Vaccine API'
  slug: open-disease-sh-covid-19-vaccine-api
- collection_type: open
  name: 'disease.sh Docs - An open API for disease-related statistics COVID-19: Apple COVID-19: Variants API'
  slug: open-disease-sh-covid-19-variants-api
- collection_type: open
  name: 'disease.sh Docs - An open API for disease-related statistics COVID-19: Apple COVID-19: Worldometers API'
  slug: open-disease-sh-covid-19-worldometers-api
- collection_type: open
  name: 'disease.sh Docs - An open API for disease-related statistics COVID-19: Apple Influenza: CDC API'
  slug: open-disease-sh-influenza-cdc-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/disease-sh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/disease-sh-domain-security.yml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/disease-sh
- group: docs
  title: ''
  type: Documentation
  url: https://disease.sh/docs/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/disease-sh/API/master/public/apidocs/swagger_v3.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://disease.sh/tos
created: '2026-06-13'
description: disease.sh is an open API providing reliable global disease statistics, including COVID-19 worldwide and country-level data, US state breakdowns, historical case counts, vaccine and therapeutic coverage, influenza outbreak data from the CDC, and mobility metrics from Apple and government sources. The API is completely free to use, requires no authentication, and supports CORS for browser-based integrations.
examples:
- key_count: 3
  name: Countriesfullvaccinetimeline
  slug: countriesFullVaccineTimeline
- key_count: 3
  name: Countriessimplevaccinetimeline
  slug: countriesSimpleVaccineTimeline
- key_count: 3
  name: Countryfullvaccinetimeline
  slug: countryFullVaccineTimeline
- key_count: 3
  name: Countrysimplevaccinetimeline
  slug: countrySimpleVaccineTimeline
- key_count: 3
  name: Fullvaccinetimeline
  slug: fullVaccineTimeline
- key_count: 7
  name: Get_Fulltimeline_200
  slug: get_fullTimeline_200
- key_count: 7
  name: Get_Simpletimeline_200
  slug: get_simpleTimeline_200
- key_count: 3
  name: Simplevaccinetimeline
  slug: simpleVaccineTimeline
- key_count: 3
  name: Statefullvaccinetimeline
  slug: stateFullVaccineTimeline
- key_count: 3
  name: Statesimplevaccinetimeline
  slug: stateSimpleVaccineTimeline
- key_count: 3
  name: Statesfullvaccinetimeline
  slug: statesFullVaccineTimeline
- key_count: 3
  name: Statessimplevaccinetimeline
  slug: statesSimpleVaccineTimeline
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/disease-sh.png
json_schemas:
- name: ILINet
  property_count: 9
  slug: ILINet
- name: USCL
  property_count: 7
  slug: USCL
- name: USPHL
  property_count: 9
  slug: USPHL
- name: covidAll
  property_count: 20
  slug: covidAll
- name: covidAppleCountries
  property_count: 0
  slug: covidAppleCountries
- name: covidAppleData
  property_count: 3
  slug: covidAppleData
- name: covidAppleSubregions
  property_count: 2
  slug: covidAppleSubregions
- name: covidContinent
  property_count: 20
  slug: covidContinent
- name: covidContinents
  property_count: 0
  slug: covidContinents
- name: covidCountries
  property_count: 0
  slug: covidCountries
- name: covidCountry
  property_count: 23
  slug: covidCountry
- name: covidGov
  property_count: 0
  slug: covidGov
- name: covidHistorical
  property_count: 0
  slug: covidHistorical
- name: covidHistoricalAll
  property_count: 3
  slug: covidHistoricalAll
- name: covidHistoricalCountries
  property_count: 0
  slug: covidHistoricalCountries
- name: covidHistoricalCountry
  property_count: 3
  slug: covidHistoricalCountry
- name: covidHistoricalProvince
  property_count: 3
  slug: covidHistoricalProvince
- name: covidHistoricalProvinces
  property_count: 0
  slug: covidHistoricalProvinces
- name: covidHistoricalUSCounties
  property_count: 0
  slug: covidHistoricalUSCounties
- name: covidHistoricalUSCounty
  property_count: 0
  slug: covidHistoricalUSCounty
- name: covidJHUCounties
  property_count: 0
  slug: covidJHUCounties
- name: covidJHUCountries
  property_count: 6
  slug: covidJHUCountries
- name: covidJHUCounty
  property_count: 6
  slug: covidJHUCounty
- name: covidNYTCounty
  property_count: 0
  slug: covidNYTCounty
- name: covidNYTState
  property_count: 0
  slug: covidNYTState
- name: covidNYTUSA
  property_count: 0
  slug: covidNYTUSA
- name: covidState
  property_count: 12
  slug: covidState
- name: covidStates
  property_count: 0
  slug: covidStates
- name: fullVaccineTimeline
  property_count: 0
  slug: fullVaccineTimeline
- name: influenzaILINet
  property_count: 3
  slug: influenzaILINet
- name: influenzaUSCL
  property_count: 3
  slug: influenzaUSCL
- name: influenzaUSPHL
  property_count: 3
  slug: influenzaUSPHL
- name: phases
  property_count: 2
  slug: phases
- name: simpleVaccineTimeline
  property_count: 1
  slug: simpleVaccineTimeline
- name: therapeutic
  property_count: 7
  slug: therapeutic
- name: therapeutics
  property_count: 4
  slug: therapeutics
- name: vaccine
  property_count: 6
  slug: vaccine
- name: vaccineCountriesCoverage
  property_count: 0
  slug: vaccineCountriesCoverage
- name: vaccineCountryCoverage
  property_count: 2
  slug: vaccineCountryCoverage
- name: vaccineCoverage
  property_count: 0
  slug: vaccineCoverage
- name: vaccineStateCoverage
  property_count: 2
  slug: vaccineStateCoverage
- name: vaccineStatesCoverage
  property_count: 0
  slug: vaccineStatesCoverage
- name: vaccines
  property_count: 4
  slug: vaccines
- name: variantsCountriesECDC
  property_count: 0
  slug: variantsCountriesECDC
- name: variantsECDC
  property_count: 0
  slug: variantsECDC
jsonld:
- class_count: 0
  name: Api Context
  property_count: 0
  slug: api
- class_count: 0
  name: context Context
  property_count: 18
  slug: context
layout: provider
modified: '2026-06-13'
name: disease.sh
nav: Providers
network: true
overview: 'disease.sh publishes 9 APIs on the [APIs.io](https://apis.io/) network, including COVID-19: Apple API, COVID-19: Government API, COVID-19: JHUCSSE API, and 6 more. Tagged areas include COVID-19, Disease, Health, Epidemiology, and Influenza.


  The disease.sh catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  disease.sh''s developer surface includes GitHub presence, documentation, and 4 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 11
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: disease.sh API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: disease-sh-jsonschema-spectral-rules
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 13
    catalog_gap: 55.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 45.8
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 27.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/disease-sh/refs/heads/main/screenshots/disease-sh-2026-06-20T180044.png
security:
- kind: domain-security
  name: Disease Sh Domain Security
  slug: disease-sh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: disease-sh
tags:
- COVID-19
- Disease
- Health
- Epidemiology
- Influenza
- Vaccine
- Open Data
- Public Health
---
