---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bureau Of Transportation Statistics Agentic Access
  operation_count: 22
  slug: bureau-of-transportation-statistics-agentic-access
  summary_line: 22 operations
api_count: 2
apis:
- description: The BTS Open Data portal powered by Socrata provides programmatic access to transportation datasets via the Socrata Open Data API (SODA). Supports filtering, querying, and aggregation across aviation,
  name: BTS Open Data SODA API
  slug: bts-open-data-soda-api
- description: TranStats is BTS's aviation and transportation statistics database providing flight on-time performance data, carrier and airport snapshots, fuel consumption data, and comprehensive airline statistics
  name: TranStats - Airline On-Time Performance Data
  slug: transtats
- description: The Freight Analysis Framework integrates data from multiple sources to create a comprehensive picture of freight flows to, from, within, and through the United States. Includes volume, value, and mod
  name: BTS Freight Analysis Framework (FAF)
  slug: bts-freight-data
- baseURL: https://data.bts.gov/resource/
  baseurl_source: declared
  description: Dataset and view metadata
  name: Bureau of Transportation Statistics Metadata API
  slug: bureau-of-transportation-statistics-metadata-api
- baseURL: https://data.bts.gov/resource/
  baseurl_source: declared
  description: Dataset resource queries via SoQL
  name: Bureau of Transportation Statistics Resource API
  slug: bureau-of-transportation-statistics-resource-api
- baseURL: https://data.bts.gov/resource/
  baseurl_source: declared
  description: The Catalog API from Bureau of Transportation Statistics — 1 operation(s) for catalog.
  name: Bureau of Transportation Statistics Catalog API
  slug: bureau-of-transportation-statistics-catalog-api
- baseURL: https://data.bts.gov/resource/
  baseurl_source: declared
  description: The Collection API from Bureau of Transportation Statistics — 2 operation(s) for collection.
  name: Bureau of Transportation Statistics Collection API
  slug: bureau-of-transportation-statistics-collection-api
- baseURL: https://data.bts.gov/resource/
  baseurl_source: declared
  description: The Geoservice-Beta API from Bureau of Transportation Statistics — 6 operation(s) for geoservice-beta.
  name: Bureau of Transportation Statistics Geoservice Beta API
  slug: bureau-of-transportation-statistics-geoservice-beta-api
- baseURL: https://data.bts.gov/resource/
  baseurl_source: declared
  description: The OgcItem API from Bureau of Transportation Statistics — 4 operation(s) for ogcitem.
  name: Bureau of Transportation Statistics Ogc Item API
  slug: bureau-of-transportation-statistics-ogcitem-api
- baseURL: https://data.bts.gov/resource/
  baseurl_source: declared
  description: The OgcItemAggregation API from Bureau of Transportation Statistics — 1 operation(s) for ogcitemaggregation.
  name: Bureau of Transportation Statistics Ogc Item Aggregation API
  slug: bureau-of-transportation-statistics-ogcitemaggregation-api
- baseURL: https://data.bts.gov/resource/
  baseurl_source: declared
  description: The OgcRoot API from Bureau of Transportation Statistics — 1 operation(s) for ogcroot.
  name: Bureau of Transportation Statistics Ogc Root API
  slug: bureau-of-transportation-statistics-ogcroot-api
- baseURL: https://data.bts.gov/resource/
  baseurl_source: declared
  description: The OgcRootConformance API from Bureau of Transportation Statistics — 1 operation(s) for ogcrootconformance.
  name: Bureau of Transportation Statistics Ogc Root Conformance API
  slug: bureau-of-transportation-statistics-ogcrootconformance-api
- baseURL: https://data.bts.gov/resource/
  baseurl_source: declared
  description: The Queryable API from Bureau of Transportation Statistics — 1 operation(s) for queryable.
  name: Bureau of Transportation Statistics Queryable API
  slug: bureau-of-transportation-statistics-queryable-api
artifact_total: 27
collections:
- collection_type: open
  name: BTS Open Data SODA Metadata API
  slug: open-bureau-of-transportation-statistics-metadata-api
- collection_type: open
  name: BTS Open Data SODA Metadata Resource API
  slug: open-bureau-of-transportation-statistics-resource-api
- collection_type: open
  name: BTS Open Data SODA API
  slug: open-bureau-of-transportation-statistics
common:
- group: other
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/capabilities/bureau-of-transportation-statistics-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bureau-of-transportation-statistics-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/finops/bureau-of-transportation-statistics-finops.yml
  title: ''
  type: FinOps
  url: finops/bureau-of-transportation-statistics-finops.yml
- group: other
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/overlays/bureau-of-transportation-statistics-geodata-search-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bureau-of-transportation-statistics-geodata-search-overlay.yaml
- group: docs
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/openapi/_original/bureau-of-transportation-statistics-geodata-search-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/bureau-of-transportation-statistics-geodata-search-openapi.json
- group: design
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/conformance/bureau-of-transportation-statistics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bureau-of-transportation-statistics-conformance.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/conventions/bureau-of-transportation-statistics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bureau-of-transportation-statistics-conventions.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/errors/bureau-of-transportation-statistics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bureau-of-transportation-statistics-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/lifecycle/bureau-of-transportation-statistics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bureau-of-transportation-statistics-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/changelog/bureau-of-transportation-statistics-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bureau-of-transportation-statistics-changelog.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/data-model/bureau-of-transportation-statistics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bureau-of-transportation-statistics-data-model.yml
- group: build
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/packages/bureau-of-transportation-statistics-packages.yml
  title: ''
  type: Packages
  url: packages/bureau-of-transportation-statistics-packages.yml
- group: commercial
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/plans/bureau-of-transportation-statistics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bureau-of-transportation-statistics-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/rate-limits/bureau-of-transportation-statistics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bureau-of-transportation-statistics-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/mcp/bureau-of-transportation-statistics-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bureau-of-transportation-statistics-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/llms/bureau-of-transportation-statistics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bureau-of-transportation-statistics-llms.txt
- group: agent
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/overlays/bureau-of-transportation-statistics-resource-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bureau-of-transportation-statistics-resource-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/overlays/bureau-of-transportation-statistics-metadata-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bureau-of-transportation-statistics-metadata-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/security/bureau-of-transportation-statistics-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bureau-of-transportation-statistics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.transportation.gov/vulnerability-disclosure-policy
- group: docs
  title: ''
  type: APIReference
  url: https://dev.socrata.com/docs/endpoints.html
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.socrata.com/consumers/getting-started.html
- group: docs
  title: ''
  type: Documentation
  url: https://dev.socrata.com/
- group: start
  title: ''
  type: SignUp
  url: https://data.bts.gov/signup
- group: operate
  title: ''
  type: Support
  url: https://www.bts.gov/learn-about-bts-and-our-work/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.bts.gov/newsroom
- group: agent
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/agentic-access/bureau-of-transportation-statistics-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bureau-of-transportation-statistics-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/security/bureau-of-transportation-statistics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bureau-of-transportation-statistics-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/bureau-of-transportation-statistics/authentication/bureau-of-transportation-statistics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bureau-of-transportation-statistics-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dotbts
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-transportation-statistics-bts
- group: company
  title: ''
  type: Website
  url: https://www.bts.gov
- group: start
  title: ''
  type: Portal
  url: https://data.bts.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.transportation.gov/privacy
- group: other
  title: ''
  type: TranStats
  url: https://www.transtats.bts.gov/
- group: start
  title: ''
  type: Data Portal
  url: https://catalog.data.gov/dataset?organization=dot-gov&q=bts
created: '2024-11-30'
description: The Bureau of Transportation Statistics (BTS), part of the Department of Transportation (DOT) is the preeminent source of statistics on commercial aviation, multimodal freight activity, and transportation economics, and provides context to decision makers and the public for understanding statistics on transportation.
finops:
- has_sources: true
  method: derived
  name: Bureau Of Transportation Statistics Finops
  primary_unit: ''
  service_category: ''
  slug: bureau-of-transportation-statistics-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-transportation-statistics.png
layout: provider
modified: '2026-09-16'
name: Bureau of Transportation Statistics
nav: Providers
network: true
overview: 'Bureau of Transportation Statistics publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Metadata API, Resource API, Catalog API, and 10 more. Tagged areas include Federal Government, Statistics, Transportation, Aviation, and Freight.


  The Bureau of Transportation Statistics catalog on APIs.io includes 1 Spectral governance ruleset.


  Bureau of Transportation Statistics'' developer surface includes changelog, API reference, getting-started guide, documentation, signup flow, support, engineering blog, and 29 more developer resources.'
plans:
- name: Bureau Of Transportation Statistics Plans Pricing
  plan_count: 0
  slug: bureau-of-transportation-statistics-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Bureau Of Transportation Statistics Rate Limits
  slug: bureau-of-transportation-statistics-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Bureau of Transportation Statistics API Rules
  rule_count: 54
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 7
  slug: bureau-of-transportation-statistics-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 31.8
    contract_quality: 41.0
    developer_ergonomics: 58.9
    discoverability: 57.1
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 20.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/bureau-of-transportation-statistics/bureau-of-transportation-statistics-2026-06-20T173820.png
security:
- kind: authentication
  name: Bureau Of Transportation Statistics Authentication
  slug: bureau-of-transportation-statistics-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Bureau Of Transportation Statistics Domain Security
  slug: bureau-of-transportation-statistics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bureau Of Transportation Statistics Vulnerability Disclosure
  slug: bureau-of-transportation-statistics-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: Find and query a BTS dataset
  slug: bureau-of-transportation-statistics-find-and-query-a-dataset
- name: Query BTS data with OData 4.0
  slug: bureau-of-transportation-statistics-query-with-odata
- name: Search the BTS geospatial catalog (NTAD)
  slug: bureau-of-transportation-statistics-search-the-geospatial-catalog
slug: bureau-of-transportation-statistics
tags:
- Federal Government
- Statistics
- Transportation
- Aviation
- Freight
- Open Data
website: https://www.bts.gov
---
