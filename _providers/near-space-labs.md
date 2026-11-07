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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.nearspacelabs.net
  baseurl_source: declared
  description: The Tile API from Near Space Labs — 19 operation(s) for tile.
  name: Near Space Labs Tile API
  slug: near-space-labs-tile-api
- baseURL: https://api.nearspacelabs.net
  baseurl_source: declared
  description: The Oauth API from Near Space Labs — 1 operation(s) for oauth.
  name: Near Space Labs OAUTH API
  slug: near-space-labs-oauth-api
artifact_total: 17
common:
- group: other
  href: https://artifacts.apis.io/near-space-labs/overlays/near-space-labs-tile-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/near-space-labs-tile-service-overlay.yaml
- group: other
  href: https://artifacts.apis.io/near-space-labs/overlays/near-space-labs-oauth-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/near-space-labs-oauth-service-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.nearspacelabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nearspacelabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nearspacelabs.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nearspacelabs.com/api/tile-server
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nearspacelabs.com/authentication
- group: operate
  title: ''
  type: Support
  url: https://www.nearspacelabs.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.nearspacelabs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nearspacelabs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nearspacelabs.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nearspacelabs.com/
- group: build
  title: ''
  type: Postman
  url: https://docs.nearspacelabs.com/nsl_postman.json
- group: agent
  href: https://artifacts.apis.io/near-space-labs/llms/near-space-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/near-space-labs-llms.txt
- group: build
  href: https://artifacts.apis.io/near-space-labs/packages/near-space-labs-packages.yml
  title: ''
  type: Packages
  url: packages/near-space-labs-packages.yml
- group: build
  href: https://artifacts.apis.io/near-space-labs/packages/near-space-labs-packages.yml
  title: ''
  type: SDKs
  url: packages/near-space-labs-packages.yml
- group: auth
  href: https://artifacts.apis.io/near-space-labs/authentication/near-space-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/near-space-labs-authentication.yml
- group: design
  href: https://artifacts.apis.io/near-space-labs/conventions/near-space-labs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/near-space-labs-conventions.yml
- group: design
  href: https://artifacts.apis.io/near-space-labs/errors/near-space-labs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/near-space-labs-problem-types.yml
- group: design
  href: https://artifacts.apis.io/near-space-labs/conformance/near-space-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/near-space-labs-conformance.yml
- group: design
  href: https://artifacts.apis.io/near-space-labs/data-model/near-space-labs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/near-space-labs-data-model.yml
- group: design
  href: https://artifacts.apis.io/near-space-labs/lifecycle/near-space-labs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/near-space-labs-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/near-space-labs/lifecycle/near-space-labs-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/near-space-labs-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/near-space-labs/rate-limits/near-space-labs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/near-space-labs-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/near-space-labs/plans/near-space-labs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/near-space-labs-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/near-space-labs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/near-space-labs/security/near-space-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/near-space-labs-domain-security.yml
- group: build
  href: https://artifacts.apis.io/near-space-labs/examples/near-space-labs-examples.yml
  title: ''
  type: Examples
  url: examples/near-space-labs-examples.yml
created: '2026-08-26'
description: 'Near Space Labs is a New York based Earth-observation company that operates a fleet of autonomous, wind-navigated stratospheric vehicles ("Swifty") flying at roughly 65,000 feet to capture 7cm-resolution orthoimagery across approximately 80% of the United States, refreshed twice a year. Imagery is delivered programmatically through a public developer surface at docs.nearspacelabs.com: an OAuth 2.0 client-credentials token service and a standards-based XYZ Tile Service on api.nearspacelabs.net that streams PNG/JPEG tiles at zoom 14-21, exposes paginated survey catalogs, GeoJSON footprints, WKT-based coverage queries and mosaic-update feeds. Both services publish machine-readable Swagger 2.0 contracts and share a single Postman collection. Customers use the imagery for P&C insurance underwriting and claims, state and local government GIS, utility and infrastructure monitoring, forestry and wildfire risk, mapping basemaps, and roofing and home services.'
examples:
- key_count: 1
  name: Near Space Labs Oauth Token 401 Example1
  slug: near-space-labs-oauth-token-401-example1
- key_count: 3
  name: Near Space Labs Tile Mosaic_Id Footprint 200 Example1
  slug: near-space-labs-tile-mosaic_id-footprint-200-example1
- key_count: 3
  name: Near Space Labs Tile Mosaic_Id Footprint 200 Example2
  slug: near-space-labs-tile-mosaic_id-footprint-200-example2
- key_count: 3
  name: Near Space Labs Tile V2 Mosaic_Id Footprint 200 Example1
  slug: near-space-labs-tile-v2-mosaic_id-footprint-200-example1
- key_count: 3
  name: Near Space Labs Tile V2 Mosaic_Id Footprint 200 Example2
  slug: near-space-labs-tile-v2-mosaic_id-footprint-200-example2
- key_count: 6
  name: Near Space Labs Tile V2 Surveys 200 Example1
  slug: near-space-labs-tile-v2-surveys-200-example1
image: https://cdn.prod.website-files.com/699b3c4514bfe203a098fbc3/69ea4c7bdbd743e1fa21e934_logo.png
layout: provider
modified: '2026-08-26'
name: Near Space Labs
nav: Providers
network: true
overview: 'Near Space Labs publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Tile API and OAUTH API. Tagged areas include Company, Earth Observation, Aerial Imagery, Geospatial, and Satellite and Remote Sensing.


  The Near Space Labs catalog on APIs.io includes 1 Spectral governance ruleset.


  Near Space Labs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, code examples, and 21 more developer resources.'
plans:
- name: Near Space Labs Plans Pricing
  plan_count: 0
  slug: near-space-labs-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Near Space Labs Rate Limits
  slug: near-space-labs-rate-limits
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Near Space Labs API Rules
  rule_count: 36
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 4
  slug: near-space-labs-rules
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 39.4
    developer_ergonomics: 70.8
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 38.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/near-space-labs/near-space-labs-2026-09-02T150728.png
security:
- kind: authentication
  name: Near Space Labs Authentication
  slug: near-space-labs-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Near Space Labs Domain Security
  slug: near-space-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: Authenticate with Near Space Labs
  slug: near-space-labs-authenticate
- name: Detect change in a survey over time
  slug: near-space-labs-detect-change
- name: Find imagery for an area of interest
  slug: near-space-labs-find-imagery-for-an-area
- name: Serve Near Space Labs tiles in a web map
  slug: near-space-labs-serve-a-basemap
slug: near-space-labs
tags:
- Company
- Earth Observation
- Aerial Imagery
- Geospatial
- Satellite and Remote Sensing
- Mapping
- Tiles
- Insurance
- Government
- Utilities
- Location
- Imagery
- Remote Sensing
website: https://www.nearspacelabs.com/
---
