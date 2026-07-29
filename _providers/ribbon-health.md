---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
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
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Ribbon Health Agentic Access
  operation_count: 73
  slug: ribbon-health-agentic-access
  summary_line: 73 operations · 34 acting
api_count: 10
apis:
- description: The Cost Estimates API from Ribbon Health — 4 operation(s) for cost estimates.
  name: Ribbon Health Cost Estimates API
  slug: ribbon-health-cost-estimates-api
- description: The Filters API from Ribbon Health — 4 operation(s) for filters.
  name: Ribbon Health Filters API
  slug: ribbon-health-filters-api
- description: The Focus Area Endpoints API from Ribbon Health — 6 operation(s) for focus area endpoints.
  name: Ribbon Health Focus Area Endpoints API
  slug: ribbon-health-focus-area-endpoints-api
- description: The Locations API from Ribbon Health — 5 operation(s) for locations.
  name: Ribbon Health Locations API
  slug: ribbon-health-locations-api
- description: The Networks API from Ribbon Health — 1 operation(s) for networks.
  name: Ribbon Health Networks API
  slug: ribbon-health-networks-api
- description: The Organizations API from Ribbon Health — 2 operation(s) for organizations.
  name: Ribbon Health Organizations API
  slug: ribbon-health-organizations-api
- description: The Price Transparency API from Ribbon Health — 8 operation(s) for price transparency.
  name: Ribbon Health Price Transparency API
  slug: ribbon-health-price-transparency-api
- description: The Providers API from Ribbon Health — 10 operation(s) for providers.
  name: Ribbon Health Providers API
  slug: ribbon-health-providers-api
- description: The Reference Endpoints API from Ribbon Health — 13 operation(s) for reference endpoints.
  name: Ribbon Health Reference Endpoints API
  slug: ribbon-health-reference-endpoints-api
- description: The TINs API from Ribbon Health — 2 operation(s) for tins.
  name: Ribbon Health TINs API
  slug: ribbon-health-tins-api
arazzos:
- description: Find a practice location by address and name, read its detail record, then list the insurances accepted in that state.
  name: Ribbon Health Location and Insurance Lookup
  slug: ribbon-health-location-insurance-workflow
- description: Upsert a custom provider record, set its locations and specialties, then confirm the maintained directory entry.
  name: Ribbon Health Provider Directory Management
  slug: ribbon-health-provider-directory-management-workflow
- description: Resolve an insurance carrier, find in-network providers by specialty and location, then read the matched provider's detail record.
  name: Ribbon Health Provider Directory Search
  slug: ribbon-health-provider-search-workflow
artifact_total: 85
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ribbon-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ribbon-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ribbon-health-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://h1.co
- group: docs
  title: ''
  type: Documentation
  url: https://ribbon.readme.io/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/nikothomas/ribbon-health
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ribbonhealth
- group: company
  title: ''
  type: Blog
  url: https://h1.co/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://h1.co/request-demo/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ribbonhealth.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/RibbonHealth
- group: commercial
  title: ''
  type: Plans
  url: plans/ribbon-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ribbon-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ribbon-health-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ribbon-health/refs/heads/main/vocabulary/ribbon-health-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/ribbon-health/refs/heads/main/json-ld/ribbon-health-context.jsonld
- group: company
  title: ''
  type: BlogRSS
  url: https://h1.co/blog/feed
- group: design
  title: ''
  type: ArazzoWorkflows
  url: ''
created: 2026-06-12
description: Ribbon Health (now part of H1) is a healthcare provider data platform offering a REST API for searching provider directories, verifying insurance networks, checking provider availability, and enriching clinical data. The H1 API provides comprehensive data on doctors, insurance plans, procedures, costs, and quality scores across the United States, enabling health plans, providers, and digital health solutions to build accurate provider directories and care navigation tools.
examples:
- key_count: 1
  name: Createcustomlocationfilter
  slug: createcustomlocationfilter
- key_count: 1
  name: Createcustomproviderfilter
  slug: createcustomproviderfilter
- key_count: 1
  name: Editcustomlocationfilter
  slug: editcustomlocationfilter
- key_count: 1
  name: Editcustomproviderfilter
  slug: editcustomproviderfilter
- key_count: 1
  name: Getclinicalarea
  slug: getclinicalarea
- key_count: 1
  name: Getclinicalareas
  slug: getclinicalareas
- key_count: 1
  name: Getcondition
  slug: getcondition
- key_count: 1
  name: Getconditions
  slug: getconditions
- key_count: 1
  name: Getcustominsurance
  slug: getcustominsurance
- key_count: 1
  name: Getcustomlocation
  slug: getcustomlocation
- key_count: 1
  name: Getcustomlocationtype
  slug: getcustomlocationtype
- key_count: 1
  name: Getcustomlocationtypes
  slug: getcustomlocationtypes
- key_count: 1
  name: Getcustomprovider
  slug: getcustomprovider
- key_count: 1
  name: Getcustomprovidertype
  slug: getcustomprovidertype
- key_count: 1
  name: Getcustomprovidertypes
  slug: getcustomprovidertypes
- key_count: 1
  name: Getcustomspecialty
  slug: getcustomspecialty
- key_count: 1
  name: Geteligibility
  slug: geteligibility
- key_count: 1
  name: Geteligibilityinsurancepartner
  slug: geteligibilityinsurancepartner
- key_count: 1
  name: Geteligibilityinsurancepartners
  slug: geteligibilityinsurancepartners
- key_count: 1
  name: Getinsurances
  slug: getinsurances
- key_count: 1
  name: Getlanguages
  slug: getlanguages
- key_count: 1
  name: Getorganization
  slug: getorganization
- key_count: 1
  name: Getpricingcarrier
  slug: getpricingcarrier
- key_count: 1
  name: Getpricingcarriernames
  slug: getpricingcarriernames
- key_count: 1
  name: Getpricingversioncarrier
  slug: getpricingversioncarrier
- key_count: 1
  name: Getprocedure
  slug: getprocedure
- key_count: 1
  name: Getprocedures
  slug: getprocedures
- key_count: 1
  name: Getspecialties
  slug: getspecialties
- key_count: 1
  name: Gettreatment
  slug: gettreatment
- key_count: 1
  name: Gettreatments
  slug: gettreatments
- key_count: 1
  name: Postcustominsurance
  slug: postcustominsurance
- key_count: 1
  name: Postcustomlocations
  slug: postcustomlocations
- key_count: 1
  name: Postcustomlocationtype
  slug: postcustomlocationtype
- key_count: 1
  name: Postcustomprovidertype
  slug: postcustomprovidertype
- key_count: 1
  name: Postcustomspecialty
  slug: postcustomspecialty
- key_count: 1
  name: Putcustominsurance
  slug: putcustominsurance
- key_count: 1
  name: Putcustomlocation
  slug: putcustomlocation
- key_count: 1
  name: Putcustomlocationclinicalareas
  slug: putcustomlocationclinicalareas
- key_count: 1
  name: Putcustomlocationinsurances
  slug: putcustomlocationinsurances
- key_count: 1
  name: Putcustomlocationorganizations
  slug: putcustomlocationorganizations
- key_count: 1
  name: Putcustomlocationtype
  slug: putcustomlocationtype
- key_count: 1
  name: Putcustomprovider
  slug: putcustomprovider
- key_count: 1
  name: Putcustomproviderclinicalareas
  slug: putcustomproviderclinicalareas
- key_count: 1
  name: Putcustomproviderlocation
  slug: putcustomproviderlocation
- key_count: 1
  name: Putcustomproviderlocationinsurances
  slug: putcustomproviderlocationinsurances
- key_count: 1
  name: Putcustomproviderlocationorganizations
  slug: putcustomproviderlocationorganizations
- key_count: 1
  name: Putcustomproviderlocations
  slug: putcustomproviderlocations
- key_count: 1
  name: Putcustomproviderprimaryspecialties
  slug: putcustomproviderprimaryspecialties
- key_count: 1
  name: Putcustomproviderprocedures
  slug: putcustomproviderprocedures
- key_count: 1
  name: Putcustomproviderspecialties
  slug: putcustomproviderspecialties
- key_count: 1
  name: Putcustomprovidertype
  slug: putcustomprovidertype
- key_count: 1
  name: Putcustomspecialty
  slug: putcustomspecialty
finops:
- name: Ribbon Health Finops
  service_category: ''
  slug: ribbon-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ribbon-health.png
json_schemas:
- name: getConditions
  property_count: 5
  slug: getconditions
- name: getCustomLocation
  property_count: 12
  slug: getcustomlocation
- name: getCustomLocations
  property_count: 2
  slug: getcustomlocations
- name: getCustomProvider
  property_count: 16
  slug: getcustomprovider
- name: getCustomProviders
  property_count: 2
  slug: getcustomproviders
- name: getEligibility
  property_count: 45
  slug: geteligibility
- name: getInsurances
  property_count: 4
  slug: getinsurances
- name: getNetworkAnalysis
  property_count: 2
  slug: getnetworkanalysis
- name: getOrganizations
  property_count: 2
  slug: getorganizations
- name: getPricingProviders
  property_count: 2
  slug: getpricingproviders
- name: getProcedureCostEstimate
  property_count: 2
  slug: getprocedurecostestimate
- name: getSpecialties
  property_count: 4
  slug: getspecialties
jsonld:
- class_count: 0
  name: Ribbon Health Context
  property_count: 43
  slug: ribbon-health-context
layout: provider
modified: 2026-06-12
name: Ribbon Health
nav: Providers
network: true
overview: 'Ribbon Health publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Cost Estimates API, Filters API, Focus Area Endpoints API, and 7 more. Tagged areas include Healthcare, Provider Directory, Insurance, Clinical Data, and Care Navigation.


  The Ribbon Health catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ribbon Health''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Ribbon Health Plans Pricing
  plan_count: 1
  slug: ribbon-health-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 8
  name: Ribbon Health Rate Limits
  slug: ribbon-health-rate-limits
rules:
- name: Ribbon Health API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ribbon-health-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.7
  delta: -5.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 72.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ribbon-health/refs/heads/main/screenshots/ribbon-health-2026-06-20T193110.png
security:
- kind: authentication
  name: Ribbon Health Authentication
  slug: ribbon-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ribbon Health Domain Security
  slug: ribbon-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ribbon-health
tags:
- Healthcare
- Provider Directory
- Insurance
- Clinical Data
- Care Navigation
- Eligibility
- Price Transparency
- Provider Search
- Health Plans
- Digital Health
website: https://h1.co
---
