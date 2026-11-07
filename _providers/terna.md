---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 7
apis:
- baseURL: https://api.terna.it
  baseurl_source: declared
  description: The Fees API from Terna — 1 operation(s) for fees.
  name: Terna Fees API
  slug: terna-fees-api
- baseURL: https://api.terna.it
  baseurl_source: declared
  description: The Generation API from Terna — 1 operation(s) for generation.
  name: Terna Generation API
  slug: terna-generation-api
- baseURL: https://api.terna.it
  baseurl_source: declared
  description: The Ifees API from Terna — 1 operation(s) for ifees.
  name: Terna Ifees API
  slug: terna-ifees-api
- baseURL: https://api.terna.it
  baseurl_source: declared
  description: The Load API from Terna — 1 operation(s) for load.
  name: Terna Load API
  slug: terna-load-api
- baseURL: https://api.terna.it
  baseurl_source: declared
  description: The Market API from Terna — 3 operation(s) for market.
  name: Terna Market API
  slug: terna-market-api
- baseURL: https://api.terna.it
  baseurl_source: declared
  description: The Public Api API from Terna — 1 operation(s) for public api.
  name: Terna Public API
  slug: terna-public-api-api
- baseURL: https://api.terna.it
  baseurl_source: declared
  description: The Transparency API from Terna — 1 operation(s) for transparency.
  name: Terna Transparency API
  slug: terna-transparency-api
artifact_total: 17
common:
- group: design
  href: https://artifacts.apis.io/terna/rules/terna-rules.yml
  title: ''
  type: Spectral
  url: rules/terna-rules.yml
- group: design
  href: https://artifacts.apis.io/terna/json-ld/terna-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/terna-context.jsonld
- group: design
  href: https://artifacts.apis.io/terna/vocabulary/terna-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/terna-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/terna/data-model/terna-data-model.yml
  title: ''
  type: DataModel
  url: data-model/terna-data-model.yml
- group: auth
  href: https://artifacts.apis.io/terna/authentication/terna-authentication.yml
  title: ''
  type: Authentication
  url: authentication/terna-authentication.yml
- group: design
  href: https://artifacts.apis.io/terna/conformance/terna-conformance.yml
  title: ''
  type: Conformance
  url: conformance/terna-conformance.yml
- group: other
  href: https://artifacts.apis.io/terna/hosts/terna-hosts.yml
  title: ''
  type: Hosts
  url: hosts/terna-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.terna.it/privacy_and_cookie_policy
- group: auth
  href: https://artifacts.apis.io/terna/security/terna-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/terna-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.terna.it/
- group: docs
  title: ''
  type: Documentation
  url: https://www.terna.it/it/developer
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.terna.it/it/developer
- group: start
  title: ''
  type: GettingStarted
  url: https://www.terna.it/it/chi-siamo/terna-breve
- group: operate
  title: ''
  type: Support
  url: https://www.terna.it/it/contatti
coverage:
  checked: 2026-09-23
  detail: Documentation is served as HTML pages without machine‑readable OpenAPI or other contracts.
  evidence:
  - status: 200
    url: https://developer.terna.it/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: Terna S.p.A. is Italy’s leading electricity transmission system operator, responsible for managing the high‑voltage grid, ensuring reliable power supply, and driving the energy transition toward renewable sources. The company operates over 75,000 km of transmission lines, connects with neighboring countries, and invests billions in digital innovation and sustainability initiatives.
image: https://www.terna.it/DesktopModules/AdactoBackend/API/download/get?image=12133
json_schemas:
- name: GetFeesV10MonthlySummaryResponse
  property_count: 2
  slug: terna-get-fees-v10-monthly-summary-response
- name: GetGenerationV20V20IdResponse
  property_count: 2
  slug: terna-get-generation-v20-v20-id-response
- name: GetIfeesV10MarketMarketidResponse
  property_count: 2
  slug: terna-get-ifees-v10-market-marketid-response
- name: GetMarketV10AsteFcrResponse
  property_count: 2
  slug: terna-get-market-v10-aste-fcr-response
- name: GetMarketV10OutputOutputidResponse
  property_count: 2
  slug: terna-get-market-v10-output-outputid-response
- name: GetTransparencyV10V10IdResponse
  property_count: 2
  slug: terna-get-transparency-v10-v10-id-response
jsonld:
- class_count: 9
  name: Terna Context
  property_count: 11
  slug: terna-context
layout: provider
modified: '2026-09-23'
name: Terna
nav: Providers
network: true
overview: 'Terna is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Fees API, Generation API, Ifees API, and 4 more. Tagged areas include Energy, Transmission, Infrastructure, Italy, and Renewables.


  The Terna catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Terna''s developer surface includes authentication, documentation, getting-started guide, support, and 10 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Terna API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: terna-rules
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 65.0
    catalog_earned_first_party: 0.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 5.3
    contract_governance: 19.7
    contract_quality: 26.1
    developer_ergonomics: 29.8
    discoverability: 71.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - italy
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - italy-southern-europe
  previous_composite: 27.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 15.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/terna/terna-2026-10-11T130808.png
security:
- kind: authentication
  name: Terna Authentication
  slug: terna-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Terna Domain Security
  slug: terna-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: terna
tags:
- Energy
- Transmission
- Infrastructure
- Italy
- Renewables
website: https://www.terna.it/
---
