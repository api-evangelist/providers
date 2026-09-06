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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.3
  scored_at: '2026-09-05'
api_count: 4
apis:
- description: The APHIS Public Search Tool provides public access to search APHIS program data, permits, and regulatory information related to animal and plant health programs.
  name: APHIS Public Search Tool
  slug: aphis-public-search-api
- description: APHIS eFile is the web-based permitting system for submitting animal and plant health import/export permit applications, tracking application status, applying for renewals and amendments, and receivin
  name: APHIS eFile Permitting System
  slug: aphis-efile-api
- description: The Agricultural Commodity Import Requirements (ACIR) system provides searchable access to APHIS import requirements for agricultural commodities, including plants, plant products, animals, and animal
  name: Agricultural Commodity Import Requirements (ACIR)
  slug: aphis-acir-api
- description: The APHIS and AMS Geospatial Hub is the public geospatial surface of USDA Marketing and Regulatory Programs (MRP), the umbrella covering APHIS and AMS. Behind the landing page sits a genuinely machine
  name: APHIS and AMS Geospatial Hub
  slug: aphis-geospatial-hub
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/animal-and-plant-health-inspection-service-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usda-aphis
- group: company
  title: ''
  type: Website
  url: https://www.aphis.usda.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.aphis.usda.gov/efile
- group: start
  title: ''
  type: Portal
  url: https://efile.aphis.usda.gov/s/
- group: start
  title: ''
  type: Portal
  url: https://acir.aphis.usda.gov/s/
- group: start
  title: ''
  type: Portal
  url: https://aphis.my.site.com/PublicSearchTool/s/
- group: start
  title: ''
  type: GISPortal
  url: https://www.aphis.usda.gov/aphis-ams-geospatial-hub
- group: other
  title: ''
  type: DataVisualization
  url: https://www.aphis.usda.gov/data-visualization-tools
- group: other
  title: ''
  type: Reports
  url: https://www.aphis.usda.gov/wildlife-services/publications/pdr
- group: other
  title: ''
  type: FOIA
  url: https://www.aphis.usda.gov/freedom-information-act
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usda.gov/privacy-policy
- group: other
  title: ''
  type: OpenData
  url: https://catalog.data.gov/organization/usda
- group: operate
  title: ''
  type: Support
  url: https://www.aphis.usda.gov/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.aphis.usda.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.aphis.usda.gov/efile
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aphis.usda.gov/efile/training
- group: start
  title: ''
  type: SignUp
  url: https://www.eauth.usda.gov/eauth/b/usda/registration
- group: start
  title: ''
  type: Login
  url: https://www.eauth.usda.gov/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aphis.usda.gov/map-data-disclaimer
- group: agent
  title: ''
  type: WellKnown
  url: well-known/animal-and-plant-health-inspection-service-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/animal-and-plant-health-inspection-service-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/animal-and-plant-health-inspection-service-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/animal-and-plant-health-inspection-service-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/animal-and-plant-health-inspection-service-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/animal-and-plant-health-inspection-service-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/animal-and-plant-health-inspection-service-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/animal-and-plant-health-inspection-service-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/animal-and-plant-health-inspection-service-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/animal-and-plant-health-inspection-service-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/animal-and-plant-health-inspection-service-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/animal-and-plant-health-inspection-service-finops.yml
created: '2024-11-21'
description: USDA's Animal and Plant Health Inspection Service (APHIS) protects the health and value of U.S. agriculture and natural resources by safeguarding against agricultural pests and diseases, ensuring the welfare of animals, and supporting sustainable agricultural practices. APHIS provides digital services including the eFile permitting system for import/export permits, the Agricultural Commodity Import Requirements (ACIR) portal, a geospatial hub for spatial analysis, data visualization tools, and open datasets via data.gov.
finops:
- name: Animal And Plant Health Inspection Service Finops
  service_category: API
  slug: animal-and-plant-health-inspection-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/animal-and-plant-health-inspection-service.png
layout: provider
modified: '2026-09-02'
name: Animal and Plant Health Inspection Service
nav: Providers
network: true
overview: 'Animal and Plant Health Inspection Service publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Animal Health, Animal Welfare, Biotechnology, and Federal-Government.


  Animal and Plant Health Inspection Service''s developer surface includes developer portal, support, documentation, getting-started guide, signup flow, authentication, and 26 more developer resources.'
plans:
- name: Animal And Plant Health Inspection Service Plans Pricing
  plan_count: 0
  slug: animal-and-plant-health-inspection-service-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Animal And Plant Health Inspection Service Rate Limits
  slug: animal-and-plant-health-inspection-service-rate-limits
scopes:
- name: Animal And Plant Health Inspection Service Scopes
  scope_count: 0
  slug: animal-and-plant-health-inspection-service-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 39.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 64.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/animal-and-plant-health-inspection-service/refs/heads/main/screenshots/animal-and-plant-health-inspection-service-2026-06-20T172003.png
security:
- kind: authentication
  name: Animal And Plant Health Inspection Service Authentication
  slug: animal-and-plant-health-inspection-service-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Animal And Plant Health Inspection Service Domain Security
  slug: animal-and-plant-health-inspection-service-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: animal-and-plant-health-inspection-service
tags:
- Agriculture
- Animal Health
- Animal Welfare
- Biotechnology
- Federal-Government
- Import Export
- Permits
- Pest Control
- Plant Health
- Regulatory
- USDA
- Wildlife
website: https://www.aphis.usda.gov/
---
