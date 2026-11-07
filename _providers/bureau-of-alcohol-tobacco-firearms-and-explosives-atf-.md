---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - finops
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ATF publishes annual firearms trace data reports covering the source and age of crime guns traced by law enforcement agencies across the United States. Data includes state-level statistics on firearms
  name: ATF Firearms Trace Data
  slug: atf-firearms-trace-data
- description: ATF publishes listings of all active Federal Firearms Licensees (FFLs) by state. The data is available as downloadable files and can be accessed programmatically for compliance verification purposes.
  name: ATF Federal Firearms Licensee (FFL) Listing
  slug: atf-federal-firearms-licensee-listing
- description: An anonymous Esri GeoServices REST feature service carrying 77,514 geocoded Federal Firearms Licensee premises, published by ATF's National Geospatial Intelligence Branch from the same source as the a
  name: ATF Federal Firearm Licensee Locations (ArcGIS Feature Service)
  slug: atf-ffl-locations-feature-service
- description: An anonymous Esri GeoServices REST feature service listing 537 ATF offices and field divisions across the United States, with office type, name, street address, city, state, ZIP and the field division
  name: ATF Office Locations (ArcGIS Feature Service)
  slug: atf-office-locations-feature-service
- baseURL: https://www.atf.gov/firearms/docs/report/
  baseurl_source: declared
  description: Structural differences between two versions of a part.
  name: Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) Diffs API
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--diffs-api
- baseURL: https://www.atf.gov/firearms/docs/report/
  baseurl_source: declared
  description: Federal Register notices that amend the ATF parts.
  name: Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) Notices API
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--notices-api
- baseURL: https://www.atf.gov/firearms/docs/report/
  baseurl_source: declared
  description: The CFR part tree and its effective versions.
  name: Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) Regulations API
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--regulations-api
- baseURL: https://www.atf.gov/firearms/docs/report/
  baseurl_source: declared
  description: Full-text search across regulation text.
  name: Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) Search API
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--search-api
artifact_total: 19
common:
- group: auth
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/security/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--domain-security.yml
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
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/openapi/_original/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--eregulations-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--eregulations-openapi.yml
- group: other
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/overlays/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--eregulations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--eregulations-overlay.yaml
- group: docs
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/json-schema/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--ffl-locations.json
  title: ''
  type: JSONSchema
  url: json-schema/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--ffl-locations.json
- group: design
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/data-model/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--data-model.yml
  title: ''
  type: DataModel
  url: data-model/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--data-model.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/conformance/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--conformance.yml
  title: ''
  type: Conformance
  url: conformance/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--conformance.yml
- group: auth
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/authentication/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--authentication.yml
  title: ''
  type: Authentication
  url: authentication/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--authentication.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/conventions/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--conventions.yml
  title: ''
  type: Conventions
  url: conventions/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--conventions.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/errors/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--problem-types.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/lifecycle/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/rate-limits/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/plans/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/packages/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--packages.yml
  title: ''
  type: Packages
  url: packages/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--packages.yml
- group: agent
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/mcp/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--mcp.yml
- group: agent
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/llms/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--llms.txt
- group: commercial
  href: https://artifacts.apis.io/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/finops/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--finops.yml
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
- has_sources: true
  method: searched
  name: Bureau Of Alcohol Tobacco Firearms And Explosives Atf  Finops
  primary_unit: ''
  service_category: API
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--finops
  template: false
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
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--mcp-yml
modified: '2026-09-16'
name: Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF)
nav: Providers
network: true
overview: 'Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Diffs API, Notices API, Regulations API, and 5 more. Tagged areas include Alcohol, Explosives, Federal Government, Firearms, and Geospatial.


  The Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) catalog on APIs.io includes 1 Spectral governance ruleset.


  Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF)''s developer surface includes authentication, documentation, API reference, and 23 more developer resources.'
plans:
- name: Bureau Of Alcohol Tobacco Firearms And Explosives Atf  Plans Pricing
  plan_count: 0
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Bureau Of Alcohol Tobacco Firearms And Explosives Atf  Rate Limits
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--rules
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.9
    catalog_earned_first_party: 0.0
    catalog_gap: 73.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 31.8
    contract_quality: 46.2
    developer_ergonomics: 30.4
    discoverability: 57.1
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 30.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/bureau-of-alcohol-tobacco-firearms-and-explosives-atf--2026-06-20T173802.png
security:
- kind: authentication
  name: Bureau Of Alcohol Tobacco Firearms And Explosives Atf  Authentication
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bureau Of Alcohol Tobacco Firearms And Explosives Atf  Domain Security
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 2
skills:
- name: find-atf-federal-firearms-licensees
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--find-federal-firearms-licensees
- name: track-atf-cfr-amendment
  slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf--track-cfr-amendment
slug: bureau-of-alcohol-tobacco-firearms-and-explosives-atf-
tags:
- Alcohol
- Explosives
- Federal Government
- Firearms
- Geospatial
- Law Enforcement
- Open Data
- Public Safety
- Regulations
- Tobacco
website: https://www.atf.gov/
---
