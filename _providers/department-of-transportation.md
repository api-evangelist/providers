---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Department Of Transportation Agentic Access
  operation_count: 20
  slug: department-of-transportation-agentic-access
  summary_line: 20 operations · 1 acting
api_count: 4
apis:
- description: Public datasets and downloadable data products published by BTS.
  name: Bureau of Transportation Statistics Data Portal
  slug: bts-data-portal
- description: FRA Office of Safety Analysis - rail incident, accident, and inspection data.
  name: Federal Railroad Administration Safety Data
  slug: fra-safety-data
- description: Public-transportation operating, financial, and asset data submitted by transit agencies under the National Transit Database.
  name: Federal Transit Administration National Transit Database
  slug: fta-ntd-api
- description: Pipeline and Hazardous Materials Safety Administration incident, mileage, and operator data for U.S. pipelines.
  name: PHMSA Pipeline Safety Data
  slug: phmsa-pipeline-data
- baseURL: https://vpic.nhtsa.dot.gov/api
  baseurl_source: declared
  description: The Airport Status API from Department of Transportation — 1 operation(s) for airport status.
  name: Department of Transportation Airport Status API
  slug: department-of-transportation-airport-status-api
- baseURL: https://vpic.nhtsa.dot.gov/api
  baseurl_source: declared
  description: Operating authority records
  name: Department of Transportation Authority API
  slug: department-of-transportation-authority-api
- baseURL: https://vpic.nhtsa.dot.gov/api
  baseurl_source: declared
  description: Motor carrier lookups
  name: Department of Transportation Carriers API
  slug: department-of-transportation-carriers-api
- baseURL: https://vpic.nhtsa.dot.gov/api
  baseurl_source: declared
  description: Consumer complaint data
  name: Department of Transportation Complaints API
  slug: department-of-transportation-complaints-api
- baseURL: https://vpic.nhtsa.dot.gov/api
  baseurl_source: declared
  description: Crash data
  name: Department of Transportation Crashes API
  slug: department-of-transportation-crashes-api
- baseURL: https://vpic.nhtsa.dot.gov/api
  baseurl_source: declared
  description: Roadside inspection data
  name: Department of Transportation Inspections API
  slug: department-of-transportation-inspections-api
- baseURL: https://vpic.nhtsa.dot.gov/api
  baseurl_source: declared
  description: Vehicle makes
  name: Department of Transportation Makes API
  slug: department-of-transportation-makes-api
- baseURL: https://vpic.nhtsa.dot.gov/api
  baseurl_source: declared
  description: Vehicle manufacturers
  name: Department of Transportation Manufacturers API
  slug: department-of-transportation-manufacturers-api
- baseURL: https://vpic.nhtsa.dot.gov/api
  baseurl_source: declared
  description: Vehicle models
  name: Department of Transportation Models API
  slug: department-of-transportation-models-api
- baseURL: https://vpic.nhtsa.dot.gov/api
  baseurl_source: declared
  description: 5-Star Safety Ratings
  name: Department of Transportation Ratings API
  slug: department-of-transportation-ratings-api
- baseURL: https://vpic.nhtsa.dot.gov/api
  baseurl_source: declared
  description: Vehicle, equipment, child seat, and tire recalls
  name: Department of Transportation Recalls API
  slug: department-of-transportation-recalls-api
- baseURL: https://vpic.nhtsa.dot.gov/api
  baseurl_source: declared
  description: Vehicle variable definitions
  name: Department of Transportation Vehicle Variables API
  slug: department-of-transportation-vehicle-variables-api
- baseURL: https://vpic.nhtsa.dot.gov/api
  baseurl_source: declared
  description: Decode VINs into structured vehicle data
  name: Department of Transportation VIN Decode API
  slug: department-of-transportation-vin-decode-api
- baseURL: https://vpic.nhtsa.dot.gov/api
  baseurl_source: declared
  description: World Manufacturer Identifier (WMI) decoding
  name: Department of Transportation WMI API
  slug: department-of-transportation-wmi-api
artifact_total: 51
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FAA Airport Status API
  slug: open-department-of-transportation-airport-status-api
- collection_type: open
  name: FAA Airport Status Authority API
  slug: open-department-of-transportation-authority-api
- collection_type: open
  name: FAA Airport Status Carriers API
  slug: open-department-of-transportation-carriers-api
- collection_type: open
  name: FAA Airport Status Complaints API
  slug: open-department-of-transportation-complaints-api
- collection_type: open
  name: FAA Airport Status Crashes API
  slug: open-department-of-transportation-crashes-api
- collection_type: open
  name: FAA Airport Status Inspections API
  slug: open-department-of-transportation-inspections-api
- collection_type: open
  name: FAA Airport Status Makes API
  slug: open-department-of-transportation-makes-api
- collection_type: open
  name: FAA Airport Status Manufacturers API
  slug: open-department-of-transportation-manufacturers-api
- collection_type: open
  name: FAA Airport Status Models API
  slug: open-department-of-transportation-models-api
- collection_type: open
  name: FAA Airport Status Ratings API
  slug: open-department-of-transportation-ratings-api
- collection_type: open
  name: FAA Airport Status Recalls API
  slug: open-department-of-transportation-recalls-api
- collection_type: open
  name: FAA Airport Status Vehicle Variables API
  slug: open-department-of-transportation-vehicle-variables-api
- collection_type: open
  name: FAA Airport Status VIN Decode API
  slug: open-department-of-transportation-vin-decode-api
- collection_type: open
  name: FAA Airport Status WMI API
  slug: open-department-of-transportation-wmi-api
- collection_type: open
  name: FAA Airport Status API
  slug: open-faa-system-status-api
- collection_type: open
  name: FMCSA QCMobile API
  slug: open-fmcsa-qcmobile-api
- collection_type: open
  name: NHTSA Vehicle Safety API
  slug: open-nhtsa-recalls-api
- collection_type: open
  name: NHTSA vPIC (Vehicle Product Information Catalog) API
  slug: open-nhtsa-vpic-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/department-of-transportation-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/department-of-transportation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/department-of-transportation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/department-of-transportation-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usdot
- group: start
  title: ''
  type: Portal
  url: https://www.transportation.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.transportation.gov/digitalstrategy/developer
created: '2024-12-03'
description: The U.S. Department of Transportation (DOT) and its operating administrations - NHTSA, FMCSA, FAA, FRA, FTA, MARAD, PHMSA, and BTS - publish a number of public APIs covering vehicles, motor carriers, aviation, transit, freight, and transportation statistics.
examples:
- key_count: 3
  name: Recall Example
  slug: recall-example
- key_count: 4
  name: Vin Decode Example
  slug: vin-decode-example
finops:
- name: Department Of Transportation Finops
  service_category: Federal Government / Public Open Data
  slug: department-of-transportation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/department-of-transportation.png
json_schemas:
- name: Motor Carrier (FMCSA)
  property_count: 14
  slug: carrier
- name: NHTSA Vehicle Recall
  property_count: 12
  slug: recall
- name: Vehicle (NHTSA vPIC)
  property_count: 21
  slug: vehicle
jsonld:
- class_count: 0
  name: Dot Context
  property_count: 4
  slug: dot-context
layout: provider
modified: '2026-05-19'
name: Department of Transportation
nav: Providers
network: true
overview: 'Department of Transportation publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Airport Status API, Authority API, Carriers API, and 11 more. Tagged areas include Federal-Government, Transportation, Vehicles, Aviation, and Motor Carriers.


  The Department of Transportation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Department of Transportation''s developer surface includes authentication, developer portal, documentation, and 4 more developer resources.'
plans:
- name: Department Of Transportation Plans Pricing
  plan_count: 1
  slug: department-of-transportation-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Department Of Transportation Rate Limits
  slug: department-of-transportation-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Department of Transportation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: department-of-transportation-jsonschema-spectral-rules
- effective_rule_count: 0
  extends: []
  name: Department of Transportation API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: dot-rules
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 61.3
    catalog_earned_first_party: 0.0
    catalog_gap: 53.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 59.7
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 92.9
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/department-of-transportation/refs/heads/main/screenshots/department-of-transportation-2026-06-20T175923.png
security:
- kind: authentication
  name: Department Of Transportation Authentication
  slug: department-of-transportation-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Department Of Transportation Domain Security
  slug: department-of-transportation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: department-of-transportation
tags:
- Federal-Government
- Transportation
- Vehicles
- Aviation
- Motor Carriers
website: https://www.transportation.gov/
---
