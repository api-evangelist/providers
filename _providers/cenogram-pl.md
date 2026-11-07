---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Cenogram Pl Agentic Access
  operation_count: 51
  slug: cenogram-pl-agentic-access
  summary_line: 51 operations · 2 acting
api_count: 1
apis:
- baseURL: https://cenogram.pl
  baseurl_source: declared
  description: Demographic and economic indicators from GUS BDL (Central Statistical Office)
  name: Cenogram Demographics API
  slug: cenogram-pl-demographics-api
- baseURL: https://cenogram.pl
  baseurl_source: declared
  description: 'Upcoming-infrastructure signals per municipality: public tenders, sewage-programme agglomerations, planned capital expenditure'
  name: Cenogram Infrastructure API
  slug: cenogram-pl-infrastructure-api
- baseURL: https://cenogram.pl
  baseurl_source: declared
  description: District and location discovery
  name: Cenogram Locations API
  slug: cenogram-pl-locations-api
- baseURL: https://cenogram.pl
  baseurl_source: declared
  description: 'Parcel-first lookup: resolve a cadastral identifier, read the parcel core, the deed history recorded against it, and per-parcel context layers (flood, zoning, permits, buildings, heritage, landslide, '
  name: Cenogram Parcels API
  slug: cenogram-pl-parcels-api
- baseURL: https://cenogram.pl
  baseurl_source: declared
  description: Geographic and polygon search
  name: Cenogram Spatial API
  slug: cenogram-pl-spatial-api
- baseURL: https://cenogram.pl
  baseurl_source: declared
  description: Market statistics and price data
  name: Cenogram Statistics API
  slug: cenogram-pl-statistics-api
- baseURL: https://cenogram.pl
  baseurl_source: declared
  description: Search and filter transactions
  name: Cenogram Transactions API
  slug: cenogram-pl-transactions-api
- description: The Districts API from Cenogram — 2 operation(s) for districts.
  name: Cenogram Districts API
  slug: cenogram-pl-districts-api
- description: The Infrastructure Signals API from Cenogram — 1 operation(s) for infrastructure signals.
  name: Cenogram Infrastructure Signals API
  slug: cenogram-pl-infrastructure-signals-api
- description: The Permits API from Cenogram — 1 operation(s) for permits.
  name: Cenogram Permits API
  slug: cenogram-pl-permits-api
- description: The Price Per M2 API from Cenogram — 1 operation(s) for price per m2.
  name: Cenogram Price Per M2 API
  slug: cenogram-pl-price-per-m2-api
- description: The Stats API from Cenogram — 2 operation(s) for stats.
  name: Cenogram Stats API
  slug: cenogram-pl-stats-api
- description: The Streets API from Cenogram — 1 operation(s) for streets.
  name: Cenogram Streets API
  slug: cenogram-pl-streets-api
- description: The Valuations API from Cenogram — 2 operation(s) for valuations.
  name: Cenogram Valuations API
  slug: cenogram-pl-valuations-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/cenogram-pl/agentic-access/cenogram-pl-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cenogram-pl-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/cenogram-pl/plans/cenogram-pl-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cenogram-pl-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cenogram-pl/rules/cenogram-pl-rules.yml
  title: ''
  type: Spectral
  url: rules/cenogram-pl-rules.yml
- group: design
  href: https://artifacts.apis.io/cenogram-pl/vocabulary/cenogram-pl-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cenogram-pl-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cenogram-pl/errors/cenogram-pl-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cenogram-pl-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cenogram-pl/conformance/cenogram-pl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cenogram-pl-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cenogram-pl/llms/cenogram-pl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cenogram-pl-llms.txt
- group: agent
  href: https://artifacts.apis.io/cenogram-pl/well-known/cenogram-pl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cenogram-pl-well-known.yml
- group: other
  href: https://artifacts.apis.io/cenogram-pl/hosts/cenogram-pl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cenogram-pl-hosts.yml
- group: other
  href: https://artifacts.apis.io/cenogram-pl/vendors/cenogram-pl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cenogram-pl-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://cenogram.pl/api/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cenogram
- group: auth
  href: https://artifacts.apis.io/cenogram-pl/authentication/cenogram-pl-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cenogram-pl-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cenogram-pl/security/cenogram-pl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cenogram-pl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cenogram.pl/
- group: docs
  title: ''
  type: Documentation
  url: https://cenogram.pl/api
- group: commercial
  title: ''
  type: Pricing
  url: https://cenogram.pl/api#cennik
created: '2026-11-04'
description: Cenogram provides a comprehensive database of real estate transaction prices across Poland, offering over 8 million transaction records from 2003 onward. Users can filter by region, date, and property type, view maps, and download comparable transaction sets for appraisal reports. The platform targets appraisers, analysts, and real estate professionals seeking accurate market data.
image: https://cenogram.pl/og/s/home/og.png
json_schemas:
- name: PostApiV1ParcelsSpatialRequest
  property_count: 1
  slug: cenogram-pl-post-api-v1-parcels-spatial-request
- name: PostApiV1TransactionsSpatialRequest
  property_count: 1
  slug: cenogram-pl-post-api-v1-transactions-spatial-request
jsonld:
- class_count: 2
  name: Cenogram Pl Context
  property_count: 1
  slug: cenogram-pl-context
layout: provider
modified: '2026-11-04'
name: Cenogram
nav: Providers
network: true
overview: 'Cenogram publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Demographics API, Infrastructure API, Locations API, and 11 more. Tagged areas include Company, Real Estate, Data, Analytics, and Poland.


  The Cenogram catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cenogram''s developer surface includes API reference, authentication, documentation, pricing, and 13 more developer resources.'
plans:
- name: Cenogram Pl Plans Pricing
  plan_count: 5
  slug: cenogram-pl-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Cenogram API Rules
  rule_count: 47
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 3
  slug: cenogram-pl-rules
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 30.2
    developer_ergonomics: 20.2
    discoverability: 57.1
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - poland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 43.8
      derived: 8
      marker_coverage: 50.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cenogram Pl Authentication
  slug: cenogram-pl-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cenogram Pl Domain Security
  slug: cenogram-pl-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cenogram-pl
tags:
- Company
- Real Estate
- Data
- Analytics
- Poland
website: https://cenogram.pl/
---
