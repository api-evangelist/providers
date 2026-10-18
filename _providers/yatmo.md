---
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Yatmo Agentic Access
  operation_count: 40
  slug: yatmo-agentic-access
  summary_line: 40 operations · 2 acting
api_count: 1
apis:
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The BikePaths API from Yatmo — 1 operation(s) for bikepaths.
  name: Yatmo Bike Paths API
  slug: yatmo-bikepaths-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The Categories API from Yatmo — 3 operation(s) for categories.
  name: Yatmo Categories API
  slug: yatmo-categories-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The Enrichment API from Yatmo — 1 operation(s) for enrichment.
  name: Yatmo Enrichment API
  slug: yatmo-enrichment-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The FrenchNeighbourhoods API from Yatmo — 1 operation(s) for frenchneighbourhoods.
  name: Yatmo French Neighbourhoods API
  slug: yatmo-frenchneighbourhoods-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The Geolocation API from Yatmo — 2 operation(s) for geolocation.
  name: Yatmo Geolocation API
  slug: yatmo-geolocation-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The GeoPositionEncoder API from Yatmo — 2 operation(s) for geopositionencoder.
  name: Yatmo Geo Position Encoder API
  slug: yatmo-geopositionencoder-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The Image API from Yatmo — 1 operation(s) for image.
  name: Yatmo Image API
  slug: yatmo-image-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The ImmotopCategories API from Yatmo — 1 operation(s) for immotopcategories.
  name: Yatmo Immotop Categories API
  slug: yatmo-immotopcategories-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The Isochrone API from Yatmo — 3 operation(s) for isochrone.
  name: Yatmo Isochrone API
  slug: yatmo-isochrone-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The NearCheck API from Yatmo — 1 operation(s) for nearcheck.
  name: Yatmo Near Check API
  slug: yatmo-nearcheck-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The Neighbourhood API from Yatmo — 1 operation(s) for neighbourhood.
  name: Yatmo Neighbourhood API
  slug: yatmo-neighbourhood-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The Points API from Yatmo — 1 operation(s) for points.
  name: Yatmo Points API
  slug: yatmo-points-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The Route API from Yatmo — 2 operation(s) for route.
  name: Yatmo Route API
  slug: yatmo-route-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The Scores API from Yatmo — 1 operation(s) for scores.
  name: Yatmo Scores API
  slug: yatmo-scores-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The Shape API from Yatmo — 1 operation(s) for shape.
  name: Yatmo Shape API
  slug: yatmo-shape-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The SimplifiedCategories API from Yatmo — 1 operation(s) for simplifiedcategories.
  name: Yatmo Simplified Categories API
  slug: yatmo-simplifiedcategories-api
- baseURL: https://be.yatmo.com
  baseurl_source: declared
  description: The Summary API from Yatmo — 6 operation(s) for summary.
  name: Yatmo Summary API
  slug: yatmo-summary-api
artifact_total: 29
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Yatmo
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yatmo/refs/heads/main/agentic-access/yatmo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/yatmo-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/yatmo/refs/heads/main/plans/yatmo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yatmo-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yatmo/refs/heads/main/rules/yatmo-rules.yml
  title: ''
  type: Spectral
  url: rules/yatmo-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yatmo/refs/heads/main/json-ld/yatmo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/yatmo-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yatmo/refs/heads/main/vocabulary/yatmo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/yatmo-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yatmo/refs/heads/main/data-model/yatmo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/yatmo-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yatmo/refs/heads/main/authentication/yatmo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/yatmo-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yatmo/refs/heads/main/errors/yatmo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/yatmo-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yatmo/refs/heads/main/conformance/yatmo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/yatmo-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yatmo/refs/heads/main/llms/yatmo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yatmo-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/yatmo/refs/heads/main/hosts/yatmo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yatmo-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/yatmo/refs/heads/main/packages/yatmo-packages.yml
  title: ''
  type: SDKs
  url: packages/yatmo-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/yatmo/refs/heads/main/packages/yatmo-packages.yml
  title: ''
  type: Packages
  url: packages/yatmo-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://yatmo.com/fr/legal/termsofsales
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://documentation.yatmo.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://yatmo.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.yatmo.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.yatmo.com/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yatmo/refs/heads/main/security/yatmo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yatmo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yatmo.com
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.yatmo.com
created: '2026-10-08'
description: Yatmo provides location intelligence, points‑of‑interest data and mapping APIs for real‑estate portals, software and apps. Their REST API offers neighbourhood content, POI lookup, isochrone calculations and map embeds, enabling developers to integrate rich geographic context into their products.
image: https://yatmo.com/v5/og/og-default.jpg
json_schemas:
- name: Category
  property_count: 5
  slug: yatmo-category
- name: CustomerItemSummary
  property_count: 3
  slug: yatmo-customer-item-summary
- name: ImmotopCategory
  property_count: 3
  slug: yatmo-immotop-category
- name: ListingEnrichment
  property_count: 6
  slug: yatmo-listing-enrichment
- name: PointOfInterestForSmallOptimizedJson
  property_count: 11
  slug: yatmo-point-of-interest-for-small-optimized-json
- name: RouteResponse
  property_count: 5
  slug: yatmo-route-response
jsonld:
- class_count: 23
  name: Yatmo Context
  property_count: 74
  slug: yatmo-context
layout: provider
modified: '2026-10-08'
name: Yatmo
nav: Providers
network: true
overview: 'Yatmo publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bike Paths API, Categories API, Enrichment API, and 14 more. Tagged areas include Company, Real Estate, LocationIntelligence, MappingAPI, and POIData.


  The Yatmo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Yatmo''s developer surface includes authentication, pricing, getting-started guide, API reference, documentation, and 17 more developer resources.'
plans:
- name: Yatmo Plans Pricing
  plan_count: 1
  slug: yatmo-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Yatmo API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 1
  slug: yatmo-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 50.9
    developer_ergonomics: 47.6
    discoverability: 73.2
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Yatmo Authentication
  slug: yatmo-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Yatmo Domain Security
  slug: yatmo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: yatmo
tags:
- Company
- Real Estate
- LocationIntelligence
- MappingAPI
- POIData
website: https://yatmo.com
---
