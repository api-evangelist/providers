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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 25.2
  scored_at: '2026-09-05'
api_count: 5
apis:
- description: ATF publishes annual firearms trace data reports covering the source and age of crime guns traced by law enforcement agencies across the United States. Data includes state-level statistics on firearms
  name: ATF Firearms Trace Data
  slug: atf-firearms-trace-data
- description: ATF publishes listings of all active Federal Firearms Licensees (FFLs) by state. The data is available as downloadable files and can be accessed programmatically for compliance verification purposes.
  name: ATF Federal Firearms Licensee (FFL) Listing
  slug: atf-federal-firearms-licensee-listing
- baseURL: https://regulations.atf.gov/api
  baseurl_source: declared
  description: A read-only JSON API over the ATF regulations in Title 27 of the Code of Federal Regulations — Parts 447, 478, 479, 555, 646 and 771 — served by ATF's eRegulations deployment. It exposes the full nest
  name: ATF eRegulations API
  slug: atf-eregulations-api
- description: An anonymous Esri GeoServices REST feature service carrying 77,514 geocoded Federal Firearms Licensee premises, published by ATF's National Geospatial Intelligence Branch from the same source as the a
  name: ATF Federal Firearm Licensee Locations (ArcGIS Feature Service)
  slug: atf-ffl-locations-feature-service
- description: An anonymous Esri GeoServices REST feature service listing 537 ATF offices and field divisions across the United States, with office type, name, street address, city, state, ZIP and the field division
  name: ATF Office Locations (ArcGIS Feature Service)
  slug: atf-office-locations-feature-service
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atfweb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atf
- group: company
  title: ''
  type: Website
  url: https://www.atf.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atf.gov/privacy-policy
- group: start
  title: ''
  type: Data Portal
  url: https://opendata-atf-geoplatform.hub.arcgis.com/
- group: other
  title: ''
  type: Publications
  url: https://www.atf.gov/resource-center/publications
- group: other
  title: ''
  type: Statistics
  url: https://www.atf.gov/resource-center/data-statistics
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--eregulations-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--eregulations-overlay.yaml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--ffl-locations.json
- group: design
  title: ''
  type: DataModel
  url: data-model/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--llms.txt
- group: commercial
  title: ''
  type: FinOps
  url: finops/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://regulations.atf.gov/
- group: docs
  title: ''
  type: APIReference
  url: https://regulations.atf.gov/api/regulation
created: '2024-11-21'
description: ATF is a law enforcement agency in the United States Department of Justice that protects communities from violent criminals, criminal organizations, the illegal use and trafficking of firearms, the illegal use and storage of explosives, acts of arson and bombings, acts of terrorism, and the illegal diversion of alcohol and tobacco products. ATF publishes firearms trace data, crime statistics, and regulatory information.
finops:
- name: Bureau Of Alcohol Tobacco Firearms And Explosives Atf  Finops
  service_category: API
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-.png
json_schemas:
- name: Federal Firearm License Location
  property_count: 90
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--ffl-locations
- name: ATF Office Location
  property_count: 9
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--office-locations
layout: provider
mcp_servers:
- description: ''
  name: Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) MCP Server
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf-mcp-server
modified: '2026-09-05'
name: Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF)
nav: Providers
network: true
overview: 'Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) publishes 1 API on the [APIs.io](https://apis.io/) network: ATF eRegulations API. Tagged areas include Alcohol, Explosives, Federal-Government, Firearms, and Geospatial.


  Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF)''s developer surface includes authentication, documentation, API reference, and 23 more developer resources.'
plans:
- name: Bureau Of Alcohol Tobacco Firearms And Explosives Atf  Plans Pricing
  plan_count: 0
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Bureau Of Alcohol Tobacco Firearms And Explosives Atf  Rate Limits
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--rate-limits
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 20.3
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 51.7
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 14.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/refs/heads/main/screenshots/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--2026-06-20T173802.png
security:
- kind: authentication
  name: Bureau Of Alcohol Tobacco Firearms And Explosives Atf  Authentication
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bureau Of Alcohol Tobacco Firearms And Explosives Atf  Domain Security
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf-
tags:
- Alcohol
- Explosives
- Federal-Government
- Firearms
- Geospatial
- Law Enforcement
- Open Data
- Public Safety
- Regulations
- Tobacco
website: https://www.atf.gov/
---
