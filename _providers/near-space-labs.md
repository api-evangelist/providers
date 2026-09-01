---
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: The Oauth API from Near Space Labs — 1 operation(s) for oauth.
  name: Near Space Labs OAUTH API
  slug: near-space-labs-oauth-api
- description: The Tile API from Near Space Labs — 19 operation(s) for tile.
  name: Near Space Labs Tile API
  slug: near-space-labs-tile-api
artifact_total: 12
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/near-space-labs-tile-service-overlay.yaml
- group: other
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
  title: ''
  type: LLMsTxt
  url: llms/near-space-labs-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/near-space-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/near-space-labs-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/near-space-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/near-space-labs-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/near-space-labs-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/near-space-labs-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/near-space-labs-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/near-space-labs-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/near-space-labs-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/near-space-labs-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/near-space-labs-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/near-space-labs-domain-security.yml
- group: build
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
overview: 'Near Space Labs publishes 2 APIs on the [APIs.io](https://apis.io/) network: OAUTH API and Tile API. Tagged areas include Company, Earth Observation, Aerial Imagery, Geospatial, and Satellite and Remote Sensing.


  Near Space Labs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, code examples, and 21 more developer resources.'
plans:
- name: Near Space Labs Plans Pricing
  plan_count: 0
  slug: near-space-labs-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Near Space Labs Rate Limits
  slug: near-space-labs-rate-limits
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 19
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 40.7
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 39.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 31.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Near Space Labs Authentication
  slug: near-space-labs-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Near Space Labs Domain Security
  slug: near-space-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
website: https://www.nearspacelabs.com/
---
