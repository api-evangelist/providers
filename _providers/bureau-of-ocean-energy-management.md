---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bureau Of Ocean Energy Management Agentic Access
  operation_count: 17
  slug: bureau-of-ocean-energy-management-agentic-access
  summary_line: 17 operations
api_count: 2
apis:
- description: BOEM provides ArcGIS REST Services exposing geospatial data for the Outer Continental Shelf (OCS) regions. Data includes active leases, offshore block grids, boundaries, wells, and pipelines for Atlan
  name: BOEM ArcGIS REST Services
  slug: boem-arcgis-rest-services
- description: ESPIS provides access to BOEM's environmental studies data, including research reports, environmental impact studies, and scientific literature related to offshore energy development. Searchable by to
  name: Environmental Studies Program Information System (ESPIS)
  slug: espis
- baseURL: https://hub.marinecadastre.gov/
  baseurl_source: declared
  description: The Catalog API from Bureau of Ocean Energy Management — 1 operation(s) for catalog.
  name: Bureau of Ocean Energy Management Catalog API
  slug: bureau-of-ocean-energy-management-catalog-api
- baseURL: https://hub.marinecadastre.gov/
  baseurl_source: declared
  description: The Collection API from Bureau of Ocean Energy Management — 2 operation(s) for collection.
  name: Bureau of Ocean Energy Management Collection API
  slug: bureau-of-ocean-energy-management-collection-api
- baseURL: https://hub.marinecadastre.gov/
  baseurl_source: declared
  description: The Geoservice-Beta API from Bureau of Ocean Energy Management — 6 operation(s) for geoservice-beta.
  name: Bureau of Ocean Energy Management Geoservice Beta API
  slug: bureau-of-ocean-energy-management-geoservice-beta-api
- baseURL: https://hub.marinecadastre.gov/
  baseurl_source: declared
  description: The OgcItem API from Bureau of Ocean Energy Management — 4 operation(s) for ogcitem.
  name: Bureau of Ocean Energy Management Ogc Item API
  slug: bureau-of-ocean-energy-management-ogcitem-api
- baseURL: https://hub.marinecadastre.gov/
  baseurl_source: declared
  description: The OgcItemAggregation API from Bureau of Ocean Energy Management — 1 operation(s) for ogcitemaggregation.
  name: Bureau of Ocean Energy Management Ogc Item Aggregation API
  slug: bureau-of-ocean-energy-management-ogcitemaggregation-api
- baseURL: https://hub.marinecadastre.gov/
  baseurl_source: declared
  description: The OgcRoot API from Bureau of Ocean Energy Management — 1 operation(s) for ogcroot.
  name: Bureau of Ocean Energy Management Ogc Root API
  slug: bureau-of-ocean-energy-management-ogcroot-api
- baseURL: https://hub.marinecadastre.gov/
  baseurl_source: declared
  description: The OgcRootConformance API from Bureau of Ocean Energy Management — 1 operation(s) for ogcrootconformance.
  name: Bureau of Ocean Energy Management Ogc Root Conformance API
  slug: bureau-of-ocean-energy-management-ogcrootconformance-api
- baseURL: https://hub.marinecadastre.gov/
  baseurl_source: declared
  description: The Queryable API from Bureau of Ocean Energy Management — 1 operation(s) for queryable.
  name: Bureau of Ocean Energy Management Queryable API
  slug: bureau-of-ocean-energy-management-queryable-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/agentic-access/bureau-of-ocean-energy-management-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bureau-of-ocean-energy-management-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/rules/bureau-of-ocean-energy-management-rules.yml
  title: ''
  type: Spectral
  url: rules/bureau-of-ocean-energy-management-rules.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/json-ld/bureau-of-ocean-energy-management-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bureau-of-ocean-energy-management-context.jsonld
- group: design
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/vocabulary/bureau-of-ocean-energy-management-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bureau-of-ocean-energy-management-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/lifecycle/bureau-of-ocean-energy-management-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/bureau-of-ocean-energy-management-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/hosts/bureau-of-ocean-energy-management-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bureau-of-ocean-energy-management-hosts.yml
- group: other
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/vendors/bureau-of-ocean-energy-management-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bureau-of-ocean-energy-management-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/finops/bureau-of-ocean-energy-management-finops.yml
  title: ''
  type: FinOps
  url: finops/bureau-of-ocean-energy-management-finops.yml
- group: auth
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/security/bureau-of-ocean-energy-management-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bureau-of-ocean-energy-management-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/security/bureau-of-ocean-energy-management-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bureau-of-ocean-energy-management-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boemgov
- group: company
  title: ''
  type: Website
  url: https://www.boem.gov
- group: start
  title: ''
  type: Portal
  url: https://marinecadastre.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doi.gov/privacy
- group: other
  title: ''
  type: Mapping and Data
  url: https://www.boem.gov/oil-gas-energy/mapping-and-data
- group: start
  title: ''
  type: Data Portal
  url: https://catalog.data.gov/dataset?organization=boem-gov
- group: company
  title: ''
  type: Blog
  url: https://www.boem.gov/rss.xml
- group: docs
  title: ''
  type: Documentation
  url: https://www.boem.gov/oil-gas-energy/mapping-and-data
- group: docs
  title: ''
  type: Documentation
  url: https://www.boem.gov/renewable-energy/mapping-and-data
- group: operate
  title: ''
  type: Support
  url: https://www.boem.gov/about-boem/contact-us
- group: company
  title: ''
  type: Newsroom
  url: https://www.boem.gov/newsroom
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.boem.gov/bss
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boem.gov/about-boem/disclaimer-liability-and-endorsement
- group: auth
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/security/bureau-of-ocean-energy-management-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bureau-of-ocean-energy-management-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/well-known/bureau-of-ocean-energy-management-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bureau-of-ocean-energy-management-security.txt
- group: agent
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/well-known/bureau-of-ocean-energy-management-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bureau-of-ocean-energy-management-well-known.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/conformance/bureau-of-ocean-energy-management-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bureau-of-ocean-energy-management-conformance.yml
- group: auth
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/authentication/bureau-of-ocean-energy-management-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bureau-of-ocean-energy-management-authentication.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/conventions/bureau-of-ocean-energy-management-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bureau-of-ocean-energy-management-conventions.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/data-model/bureau-of-ocean-energy-management-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bureau-of-ocean-energy-management-data-model.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/errors/bureau-of-ocean-energy-management-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bureau-of-ocean-energy-management-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/lifecycle/bureau-of-ocean-energy-management-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bureau-of-ocean-energy-management-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/mcp/bureau-of-ocean-energy-management-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bureau-of-ocean-energy-management-mcp.yml
- group: commercial
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/plans/bureau-of-ocean-energy-management-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bureau-of-ocean-energy-management-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bureau-of-ocean-energy-management/rate-limits/bureau-of-ocean-energy-management-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bureau-of-ocean-energy-management-rate-limits.yml
created: '2024-11-30'
description: The Bureau of Ocean Energy Management (BOEM) manages the nation's offshore resources in an environmentally and economically responsible way. BOEM oversees the responsible development of U.S. Outer Continental Shelf energy and mineral resources while protecting the environment and conserving natural resources.
finops:
- has_sources: false
  method: generated
  name: Bureau Of Ocean Energy Management Finops
  primary_unit: request
  service_category: API
  slug: bureau-of-ocean-energy-management-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-ocean-energy-management.png
json_schemas:
- name: CollectionWithLinksDto
  property_count: 8
  slug: bureau-of-ocean-energy-management-collection-with-links-dto
- name: FeatureLayerDto
  property_count: 67
  slug: bureau-of-ocean-energy-management-feature-layer-dto
- name: FeatureLayerQueryDto
  property_count: 10
  slug: bureau-of-ocean-energy-management-feature-layer-query-dto
- name: FeatureServerDto
  property_count: 35
  slug: bureau-of-ocean-energy-management-feature-server-dto
- name: OgcItemDto
  property_count: 5
  slug: bureau-of-ocean-energy-management-ogc-item-dto
- name: OgcQueryablesResponseDto
  property_count: 5
  slug: bureau-of-ocean-energy-management-ogc-queryables-response-dto
jsonld:
- class_count: 46
  name: Bureau Of Ocean Energy Management Context
  property_count: 209
  slug: bureau-of-ocean-energy-management-context
layout: provider
mcp_servers:
- description: MCP server; 9 tools listed. A candidate, not confirmed as published by the provider.
  name: Bureau of Ocean Energy Management MCP Server
  slug: bureau-of-ocean-energy-management-mcp-yml
modified: '2026-10-20'
name: Bureau of Ocean Energy Management
nav: Providers
network: true
overview: 'Bureau of Ocean Energy Management publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Catalog API, Collection API, Geoservice Beta API, and 7 more. Tagged areas include Energy, Federal Government, Marine, Ocean, and GIS.


  The Bureau of Ocean Energy Management catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bureau of Ocean Energy Management''s developer surface includes developer portal, engineering blog, documentation, support, authentication, and 30 more developer resources.'
plans:
- name: Bureau Of Ocean Energy Management Plans Pricing
  plan_count: 0
  slug: bureau-of-ocean-energy-management-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Bureau Of Ocean Energy Management Rate Limits
  slug: bureau-of-ocean-energy-management-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Bureau of Ocean Energy Management API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: bureau-of-ocean-energy-management-rules
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 33.3
    contract_quality: 55.0
    developer_ergonomics: 45.2
    discoverability: 74.1
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 29.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/bureau-of-ocean-energy-management/bureau-of-ocean-energy-management-2026-06-20T173814.png
security:
- kind: authentication
  name: Bureau Of Ocean Energy Management Authentication
  slug: bureau-of-ocean-energy-management-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bureau Of Ocean Energy Management Domain Security
  slug: bureau-of-ocean-energy-management-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bureau Of Ocean Energy Management Vulnerability Disclosure
  slug: bureau-of-ocean-energy-management-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bureau-of-ocean-energy-management
tags:
- Energy
- Federal Government
- Marine
- Ocean
- GIS
- Offshore
- Environmental
website: https://www.boem.gov
---
