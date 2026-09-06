---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: The GraphQL API behind my.wingtra.com, Wingtra's customer and partner portal. The schema answers anonymous introspection and returns 84 types, 38 query root fields and 33 mutations covering drone regi
  name: Wingtra Customer and Partner Portal GraphQL API
  slug: wingtra-portal-graphql
- description: The versioned REST API the WingtraCLOUD browser client at cloud.wingtra.com calls — sites, flights, drones, layers, jobs, tenants, file registration and presigned upload, archiving, survey outcomes, a
  name: WingtraCLOUD API
  slug: wingtra-cloud-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wingtra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wingtra.com/
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge.wingtra.com/en
- group: operate
  title: ''
  type: Support
  url: https://wingtra.com/support/
- group: company
  title: ''
  type: Blog
  url: https://wingtra.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wingtra
- group: commercial
  title: ''
  type: Pricing
  url: https://wingtra.com/software/plans/
- group: start
  title: ''
  type: Login
  url: https://my.wingtra.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wingtra.com/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wingtra.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://knowledge.wingtra.com/en/wingtracloud-releases-
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wingtra-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/wingtra-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/wingtra-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wingtra-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wingtra-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wingtra-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/wingtra-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wingtra-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wingtra-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wingtra-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/wingtra-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wingtra-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wingtra-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wingtra-llms.txt
created: '2026-09-04'
description: 'Wingtra AG is a Swiss drone manufacturer headquartered at Giesshübelstrasse 40 in Zürich, with a second office in Fort Lauderdale, Florida. It builds the WingtraOne GEN II and WingtraRAY VTOL tail-sitter mapping drones — fixed-wing aircraft that take off and land vertically — together with the RGB, multispectral and LiDAR payloads they carry, the WingtraGROUND GNSS base station, and the software that turns a flight into survey-grade output: the tablet-based Wingtra App for flight planning and capture, and the browser-based WingtraCLOUD for site organization, PPK geotagging, coordinate transformation across 6,500-plus published coordinate systems, photogrammetry processing and sharing, sold in WingtraESSENTIAL, WingtraPRO and WingtraUNLIMITED tiers. Wingtra publishes no developer portal, API reference, SDK or partner API program. Its machine-readable surface is incidental rather than offered: the customer and partner portal at my.wingtra.com is backed by a GraphQL API at api.my.wingtra.com
  whose schema answers anonymous introspection, and the WingtraCLOUD web client calls a versioned REST API at api.sky.wingtra.com that is closed to unauthenticated callers. Integration with the wider geospatial toolchain is delivered as file exchange — Trimble Business Center, ArcGIS Online, Propeller, Pix4D, Bentley iTwin and DroneDeploy — not as an API.'
image: https://wingtra.com/wp-content/uploads/wingtraray-full-end-to-end-solution.png
layout: provider
modified: '2026-09-04'
name: Wingtra
nav: Providers
network: true
overview: 'Wingtra publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Drones, UAV, Aerial Surveying, and Mapping.


  Wingtra''s developer surface includes documentation, support, engineering blog, pricing, changelog, authentication, and 19 more developer resources.'
plans:
- name: Wingtra Plans Pricing
  plan_count: 3
  slug: wingtra-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Wingtra Rate Limits
  slug: wingtra-rate-limits
scopes:
- name: Wingtra Scopes
  scope_count: 0
  slug: wingtra-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 37.2
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 43.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Wingtra Authentication
  slug: wingtra-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Wingtra Domain Security
  slug: wingtra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wingtra
tags:
- Company
- Drones
- UAV
- Aerial Surveying
- Mapping
- Photogrammetry
- Geospatial
- Surveying
- LiDAR
- Hardware
- Switzerland
website: https://wingtra.com/
---
