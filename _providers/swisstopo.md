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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Swisstopo Agentic Access
  operation_count: 34
  slug: swisstopo-agentic-access
  summary_line: 34 operations · 2 acting
api_count: 1
apis:
- baseURL: https://webmap-api.swissgeol.ch
  baseurl_source: declared
  description: Endpoints to list layers and their filters
  name: swisstopo Layers API
  slug: swisstopo-layers-api
- baseURL: https://webmap-api.swissgeol.ch
  baseurl_source: declared
  description: Endpoints for listing vocabularies and their terms
  name: swisstopo Vocabularies API
  slug: swisstopo-vocabularies-api
- baseURL: https://webmap-api.swissgeol.ch
  baseurl_source: declared
  description: Endpoints to obtain WMS links for filtered layers
  name: swisstopo WMS API
  slug: swisstopo-wms-api
- baseURL: https://webmap-api.swissgeol.ch
  baseurl_source: declared
  description: Endpoints to obtain WMTS layer source data
  name: swisstopo WMTS API
  slug: swisstopo-wmts-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/swisstopo/agentic-access/swisstopo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/swisstopo-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/swisstopo/rules/swisstopo-rules.yml
  title: ''
  type: Spectral
  url: rules/swisstopo-rules.yml
- group: design
  href: https://artifacts.apis.io/swisstopo/json-ld/swisstopo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/swisstopo-context.jsonld
- group: design
  href: https://artifacts.apis.io/swisstopo/vocabulary/swisstopo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/swisstopo-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/swisstopo/data-model/swisstopo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/swisstopo-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://www.bacs.admin.ch/en/framework-conditions-and-rules-cvd
- group: design
  href: https://artifacts.apis.io/swisstopo/errors/swisstopo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/swisstopo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/swisstopo/conformance/swisstopo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/swisstopo-conformance.yml
- group: auth
  href: https://artifacts.apis.io/swisstopo/well-known/swisstopo-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/swisstopo-www-security.txt
- group: auth
  href: https://artifacts.apis.io/swisstopo/well-known/swisstopo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/swisstopo-security.txt
- group: agent
  href: https://artifacts.apis.io/swisstopo/well-known/swisstopo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/swisstopo-well-known.yml
- group: other
  href: https://artifacts.apis.io/swisstopo/hosts/swisstopo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/swisstopo-hosts.yml
- group: other
  href: https://artifacts.apis.io/swisstopo/vendors/swisstopo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/swisstopo-vendors.yml
- group: build
  href: https://artifacts.apis.io/swisstopo/packages/swisstopo-packages.yml
  title: ''
  type: SDKs
  url: packages/swisstopo-packages.yml
- group: build
  href: https://artifacts.apis.io/swisstopo/packages/swisstopo-packages.yml
  title: ''
  type: Packages
  url: packages/swisstopo-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.swisstopo.admin.ch/it/overview/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swisstopo
- group: auth
  href: https://artifacts.apis.io/swisstopo/authentication/swisstopo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/swisstopo-authentication.yml
- group: auth
  href: https://artifacts.apis.io/swisstopo/security/swisstopo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/swisstopo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/swisstopo/security/swisstopo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swisstopo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.swisstopo.admin.ch/
- group: docs
  title: ''
  type: Documentation
  url: https://www.swisstopo.admin.ch/en/documentation
- group: operate
  title: ''
  type: Support
  url: https://www.swisstopo.admin.ch/en/contactswisstopo
- group: company
  title: ''
  type: Blog
  url: https://www.swisstopo.admin.ch/en/news-overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.swisstopo.admin.ch/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.swisstopo.admin.ch/en/legal-framework
created: '2026-10-28'
description: Swisstopo, the Federal Office of Topography, is Switzerland’s national geoinformation centre. It provides comprehensive geospatial data, maps, and services to the public, businesses, and authorities. The agency promotes open, transparent, and reusable geodata, supporting applications ranging from environmental monitoring to urban planning and navigation.
json_schemas:
- name: DefaultFiltersResponse
  property_count: 2
  slug: swisstopo-default-filters-response
- name: inline_response_200_1
  property_count: 2
  slug: swisstopo-inline-response-200-1
- name: inline_response_200
  property_count: 2
  slug: swisstopo-inline-response-200
- name: WmsRequest
  property_count: 3
  slug: swisstopo-wms-request
- name: WmsResponse
  property_count: 4
  slug: swisstopo-wms-response
- name: WmtsResponse
  property_count: 2
  slug: swisstopo-wmts-response
jsonld:
- class_count: 23
  name: Swisstopo Context
  property_count: 39
  slug: swisstopo-context
layout: provider
modified: '2026-10-28'
name: swisstopo
nav: Providers
network: true
overview: 'swisstopo publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Layers API, Vocabularies API, WMS API, and 1 more. Tagged areas include Geodata, Government, Switzerland, Mapping, and Open Data.


  The swisstopo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  swisstopo''s developer surface includes authentication, documentation, support, engineering blog, and 22 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: swisstopo API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: swisstopo-rules
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 61.4
    developer_ergonomics: 27.4
    discoverability: 63.4
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/swisstopo/swisstopo-2026-11-03T144214.png
security:
- kind: authentication
  name: Swisstopo Authentication
  slug: swisstopo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Swisstopo Domain Security
  slug: swisstopo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Swisstopo Vulnerability Disclosure
  slug: swisstopo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: swisstopo
tags:
- Geodata
- Government
- Switzerland
- Mapping
- Open Data
website: https://www.swisstopo.admin.ch/
---
