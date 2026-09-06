---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 8.3
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: The Canada Energy Regulator operates its own ArcGIS Online organization (portal neb-gis.maps.arcgis.com, organization id vNzamREXvX2WcX6d) and hosts 23 public feature services on it. This is the one g
  name: CER ArcGIS Online Feature Services
  slug: cer-arcgis-feature-services
- description: The CER's Environmental and Socio-economic Assessments (ESA) layer, published through the Government of Canada's Federal Geospatial Platform at maps-cartes.services.geo.ca under the NRCan folder and s
  name: CER Assessments Map Service (Federal Geospatial Platform)
  slug: cer-assessments-map-service
- description: 'The Canada Energy Regulator publishes no API of its own for tabular data, but all of its open data is machine-readable through the Government of Canada Open Government Portal''s CKAN Action API, which '
  name: CER Open Data via the Open Government Portal CKAN API
  slug: cer-open-data-ckan
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canada-energy-regulator-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cer-rec.gc.ca/en/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cer-rec.gc.ca/en/data-analysis/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cer-rec.gc.ca/en/about/open-government/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cer-rec.gc.ca/en/data-visualization/
- group: docs
  title: ''
  type: APIReference
  url: https://open.canada.ca/data/api/3/action/help_show?name=package_search
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CER-REC
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/CER-REC/pipeline-profiles
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/CER-REC/conditions
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/CER-REC/incidents-pipeliniers_pipeline-incidents
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cer-rec.gc.ca/en/terms-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cer-rec.gc.ca/en/terms-conditions.html#s1
- group: operate
  title: ''
  type: Support
  url: https://www.cer-rec.gc.ca/en/about/contact/index.html
- group: company
  title: ''
  type: Blog
  url: https://www.cer-rec.gc.ca/en/about/news-room/index.html
- group: commercial
  title: ''
  type: License
  url: https://open.canada.ca/en/open-government-licence-canada
- group: auth
  title: ''
  type: Authentication
  url: authentication/canada-energy-regulator-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/canada-energy-regulator-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/canada-energy-regulator-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/canada-energy-regulator-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/canada-energy-regulator-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/canada-energy-regulator-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/canada-energy-regulator-glossary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/canada-energy-regulator-arcgis-layers.schema.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/canada-energy-regulator-llms.txt
created: '2026-07-27'
description: 'The Canada Energy Regulator (CER / Régie de l''énergie du Canada) is Canada''s federal energy regulator, created by the Canadian Energy Regulator Act in 2019 to replace the National Energy Board. Its remit is the interprovincial and international layer of the energy system: pipelines and power lines that cross a provincial or national border, imports and exports of oil, natural gas, NGLs, LNG and electricity, oil and gas activity on frontier and offshore lands, and offshore renewable energy projects. It does not regulate the distribution utilities that meter and bill Canadian households — electricity and gas distribution is provincial, which is why the only consumer energy data mandate in the country, Ontario''s Green Button regulation O. Reg. 633/21, is administered by the Ontario Energy Board and not by the CER. The CER''s API posture is the cleanest possible statement of that split: it is genuinely open on market and system data and entirely absent on consumer data. It publishes
  83 datasets and 944 resources on the Government of Canada Open Government Portal, every one of them under the Open Government Licence – Canada, 894 of them CSV files served anonymously from its own www.cer-rec.gc.ca/open/ tree, all of it queryable without a key through the portal''s CKAN Action API. It operates its own ArcGIS Online organization whose 23 hosted feature services — pipeline systems, incidents, provincial pipeline status, resource areas, refineries — answered anonymous ArcGIS REST queries on 2026-07-27, and it publishes an Environmental and Socio-economic Assessments layer through the Federal Geospatial Platform as both an Esri ArcGIS REST MapServer and an OGC WMS 1.3.0 service. It also open-sources the front ends for its own visualizations on GitHub. What it does not have is a developer portal, an OpenAPI definition, an API key, a rate-limit policy, or a single machine-readable path to an individual customer''s usage or billing data. No mandate obliges it to have one. Home
  market Canada.'
image: https://www.cer-rec.gc.ca/global/images/logo_cer_en.png
json_schemas:
- name: Canada Energy Regulator ArcGIS feature layer attributes
  property_count: 0
  slug: canada-energy-regulator-arcgis-layers.schema
layout: provider
modified: '2026-07-27'
name: Canada Energy Regulator
nav: Providers
network: true
overview: 'Canada Energy Regulator publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Canada, Regulations, Government, and Pipelines.


  Canada Energy Regulator''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 19 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 51.0
    catalog_earned_first_party: 5.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 33.3
    contract_quality: 8.0
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 33.3
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 27.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canada-energy-regulator/refs/heads/main/screenshots/canada-energy-regulator-2026-08-07T162922.png
security:
- kind: authentication
  name: Canada Energy Regulator Authentication
  slug: canada-energy-regulator-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Canada Energy Regulator Domain Security
  slug: canada-energy-regulator-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: canada-energy-regulator
tags:
- Energy
- Canada
- Regulations
- Government
- Pipelines
- Electricity
- Natural Gas
- Crude Oil
- Energy Markets
- Open Data
- Geospatial
website: https://www.cer-rec.gc.ca/en/
---
