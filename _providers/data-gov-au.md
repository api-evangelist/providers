---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: CKAN Action API for data.gov.au Federal, a consistent JSON-over-HTTP interface over a catalog of 132,257 datasets. Standard actions include package_search, package_show, package_list, organization_lis
  name: data.gov.au Federal CKAN Action API
  slug: catalog
- baseURL: http://demo.ckan.org
  baseurl_source: declared
  description: 'data.gov.au Federal API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: data.gov.au Federal API
  slug: data-gov-au-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/data-gov-au/rules/data-gov-au-rules.yml
  title: ''
  type: Spectral
  url: rules/data-gov-au-rules.yml
- group: design
  href: https://artifacts.apis.io/data-gov-au/json-ld/data-gov-au-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/data-gov-au-context.jsonld
- group: design
  href: https://artifacts.apis.io/data-gov-au/vocabulary/data-gov-au-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/data-gov-au-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/data-gov-au/data-model/data-gov-au-data-model.yml
  title: ''
  type: DataModel
  url: data-model/data-gov-au-data-model.yml
- group: design
  href: https://artifacts.apis.io/data-gov-au/conventions/data-gov-au-conventions.yml
  title: ''
  type: Conventions
  url: conventions/data-gov-au-conventions.yml
- group: auth
  href: https://artifacts.apis.io/data-gov-au/authentication/data-gov-au-authentication.yml
  title: ''
  type: Authentication
  url: authentication/data-gov-au-authentication.yml
- group: design
  href: https://artifacts.apis.io/data-gov-au/lifecycle/data-gov-au-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/data-gov-au-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/data-gov-au/errors/data-gov-au-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/data-gov-au-problem-types.yml
- group: design
  href: https://artifacts.apis.io/data-gov-au/conformance/data-gov-au-conformance.yml
  title: ''
  type: Conformance
  url: conformance/data-gov-au-conformance.yml
- group: other
  href: https://artifacts.apis.io/data-gov-au/hosts/data-gov-au-hosts.yml
  title: ''
  type: Hosts
  url: hosts/data-gov-au-hosts.yml
- group: build
  href: https://artifacts.apis.io/data-gov-au/integrations/data-gov-au-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/data-gov-au-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/data-gov-au/vendors/data-gov-au-vendors.yml
  title: ''
  type: Vendors
  url: vendors/data-gov-au-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ckan.org/en/latest/maintaining/getting-started.html
- group: auth
  href: https://artifacts.apis.io/data-gov-au/security/data-gov-au-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/data-gov-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.gov.au/data
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datagovau
- group: commercial
  href: https://artifacts.apis.io/data-gov-au/plans/data-gov-au-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/data-gov-au-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/data-gov-au/rate-limits/data-gov-au-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/data-gov-au-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/data-gov-au/finops/data-gov-au-finops.yml
  title: ''
  type: FinOps
  url: finops/data-gov-au-finops.yml
- group: other
  href: https://artifacts.apis.io/data-gov-au/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: data.gov.au Federal is the Australian Government's national open-data portal, run on CKAN and (per its own maintenance notice) operated under the Australian Bureau of Statistics. It exposes the CKAN Action API, a standardized machine-readable JSON interface over approximately 132,257 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable. Its CKAN extensions (ckanext-datagovau and others) are published in the datagovau GitHub organization.
finops:
- has_sources: true
  method: generated
  name: Data Gov Au Finops
  primary_unit: ''
  service_category: Open Data
  slug: data-gov-au-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-gov-au.png
json_schemas:
- name: GetApiActionResourceUpdateResponse
  property_count: 1
  slug: data-gov-au-get-api-action-resource-update-response
- name: GetApiSearchDatasetResponse
  property_count: 1
  slug: data-gov-au-get-api-search-dataset-response
- name: GetApi3ActionGroupListResponse
  property_count: 3
  slug: data-gov-au-get-api3-action-group-list-response
- name: GetApi3ActionResourcePatchResponse
  property_count: 3
  slug: data-gov-au-get-api3-action-resource-patch-response
- name: GetResponse
  property_count: 3
  slug: data-gov-au-get-response
jsonld:
- class_count: 5
  name: Data Gov Au Context
  property_count: 5
  slug: data-gov-au-context
layout: provider
modified: '2026-10-21'
name: data.gov.au Federal
nav: Providers
network: true
overview: 'data.gov.au Federal is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  The data.gov.au Federal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  data.gov.au Federal''s developer surface includes authentication, getting-started guide, documentation, and 18 more developer resources.'
plans:
- name: Data Gov Au Plans Pricing
  plan_count: 1
  slug: data-gov-au-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Data Gov Au Rate Limits
  slug: data-gov-au-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: data.gov.au Federal API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: data-gov-au-rules
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 63.8
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 24.2
    developer_ergonomics: 27.4
    discoverability: 66.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
    - north-america
  previous_composite: 24.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/data-gov-au/data-gov-au-2026-06-20T175531.png
security:
- kind: authentication
  name: Data Gov Au Authentication
  slug: data-gov-au-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Data Gov Au Domain Security
  slug: data-gov-au-domain-security
  summary_line: TLSv1.3 · DMARC
slug: data-gov-au
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- Australia
- Federal Government
- Public Sector
website: https://data.gov.au/data
---
