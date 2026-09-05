---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://api.webapp.prod.blv.foodcase-services.com/BLV_WebApp_WS
  baseurl_source: declared
  description: The data API from Swiss Food Composition Database — 13 operation(s) for data.
  name: Swiss Food Composition Database Data API
  slug: swiss-food-composition-database-data-api
- baseURL: https://api.webapp.prod.blv.foodcase-services.com/BLV_WebApp_WS
  baseurl_source: declared
  description: The stats API from Swiss Food Composition Database — 1 operation(s) for stats.
  name: Swiss Food Composition Database Stats API
  slug: swiss-food-composition-database-stats-api
- baseURL: https://api.webapp.prod.blv.foodcase-services.com/BLV_WebApp_WS
  baseurl_source: declared
  description: The system API from Swiss Food Composition Database — 5 operation(s) for system.
  name: Swiss Food Composition Database System API
  slug: swiss-food-composition-database-system-api
- baseURL: https://api.webapp.prod.blv.foodcase-services.com/BLV_WebApp_WS
  baseurl_source: declared
  description: The system configuration API from Swiss Food Composition Database — 1 operation(s) for system configuration.
  name: Swiss Food Composition Database system configuration API
  slug: swiss-food-composition-database-system-configuration-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/swiss-food-composition-database-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swiss-food-composition-database-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://naehrwertdaten.ch
- group: docs
  title: ''
  type: Documentation
  url: https://naehrwertdaten.ch/en/downloads/
- group: docs
  title: ''
  type: APIReference
  url: https://api.webapp.prod.blv.foodcase-services.com/BLV_WebApp_WS
- group: operate
  title: ''
  type: Support
  url: https://naehrwertdaten.ch/en/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://naehrwertdaten.ch/en/legal-information/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://naehrwertdaten.ch/en/legal-information/
- group: operate
  title: ''
  type: ChangeLog
  url: https://naehrwertdaten.ch/en/versions-and-updates/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/swiss-food-composition-database-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/swiss-food-composition-database-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swiss-food-composition-database-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/swiss-food-composition-database-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/swiss-food-composition-database-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/swiss-food-composition-database-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/swiss-food-composition-database-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/swiss-food-composition-database-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/swiss-food-composition-database-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/swiss-food-composition-database-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/swiss-food-composition-database-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/swiss-food-composition-database-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: security/swiss-food-composition-database-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swiss-food-composition-database-authentication.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/swiss-food-composition-database-openapi-overlay.yaml
created: '2026-08-27'
description: The Swiss Food Composition Database is the official reference dataset on the nutrient composition of foods available in Switzerland, published by the Federal Food Safety and Veterinary Office (FSVO / BLV). Version 7.1 (1 July 2026) covers 1,246 mostly generic foods across 19 main categories and 106 subcategories, with macronutrients, water, alcohol and energy for nearly every food, plus vitamins, minerals, fatty acid groups and individual fatty acids for most. The data is published free of charge in German, French, Italian and English, for commercial as well as scientific use, subject to acknowledgement of the source. Alongside the Excel export and the public search application, the FSVO operates a documented, entirely unauthenticated JSON REST API on the FoodCASE platform, described by a served OpenAPI 3.0.1 document with 21 read-only operations covering food search, single-food retrieval, nutrient values and their sources, ingredients, LanguaL codes, the category tree, component/unit
  reference data and the current database version.
image: https://naehrwertdaten.ch/wp-content/uploads/2018/04/favicon.png
layout: provider
modified: '2026-08-27'
name: Swiss Food Composition Database
nav: Providers
network: true
overview: 'Swiss Food Composition Database publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Data API, Stats API, System API, and 1 more. Tagged areas include Food, Nutrition, food-composition, Health, and Open Data.


  Swiss Food Composition Database''s developer surface includes documentation, API reference, support, changelog, authentication, and 20 more developer resources.'
plans:
- name: Swiss Food Composition Database Plans Pricing
  plan_count: 1
  slug: swiss-food-composition-database-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Swiss Food Composition Database Rate Limits
  slug: swiss-food-composition-database-rate-limits
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 41.2
    developer_ergonomics: 35.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 41.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swiss-food-composition-database/refs/heads/main/screenshots/swiss-food-composition-database-2026-09-02T161420.png
security:
- kind: authentication
  name: Swiss Food Composition Database Authentication
  slug: swiss-food-composition-database-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Swiss Food Composition Database Domain Security
  slug: swiss-food-composition-database-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Swiss Food Composition Database Vulnerability Disclosure
  slug: swiss-food-composition-database-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: swiss-food-composition-database
tags:
- Food
- Nutrition
- food-composition
- Health
- Open Data
- Government
- Switzerland
- Reference Data
- Public Sector
- Research
website: https://naehrwertdaten.ch
---
