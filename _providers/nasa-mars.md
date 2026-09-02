---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nasa Mars Agentic Access
  operation_count: 4
  slug: nasa-mars-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Mission manifest data per rover.
  name: NASA Mars Rovers Manifests API
  slug: nasa-mars-manifests-api
- description: Retrieve rover photos filtered by sol, Earth date, and camera.
  name: NASA Mars Rovers Photos API
  slug: nasa-mars-photos-api
- description: List and inspect Mars rover records.
  name: NASA Mars Rovers Rovers API
  slug: nasa-mars-rovers-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NASA Mars Rover Photos Manifests API
  slug: open-nasa-mars-manifests-api
- collection_type: open
  name: NASA Mars Rover Manifests Photos API
  slug: open-nasa-mars-photos-api
- collection_type: open
  name: NASA Mars Rover Photos Manifests Rovers API
  slug: open-nasa-mars-rovers-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nasa-mars-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nasa-mars-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nasa-mars-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://api.nasa.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://api.nasa.gov/#MarsPhotos
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/nasa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nasa/
- group: company
  title: ''
  type: Blog
  url: https://api.nasa.gov/
- group: commercial
  title: ''
  type: Pricing
  url: https://api.nasa.gov/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.api.nasa.gov/
- group: other
  title: ''
  type: X
  url: https://x.com/nasa
- group: commercial
  title: ''
  type: Plans
  url: plans/nasa-mars-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nasa-mars-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nasa-mars-finops.yml
created: '2026-06-13'
description: NASA Mars Rover Photos REST API providing images captured by Curiosity, Opportunity, Spirit, and Perseverance Mars rovers, filterable by sol (Martian day), camera type, and Earth date. Includes mission manifest data with landing dates, launch dates, rover status, and per-sol photo breakdowns.
examples:
- key_count: 1
  name: Manifest Curiosity
  slug: manifest-curiosity
- key_count: 1
  name: Photos By Earth Date
  slug: photos-by-earth-date
- key_count: 1
  name: Photos By Sol
  slug: photos-by-sol
finops:
- name: Nasa Mars Finops
  service_category: ''
  slug: nasa-mars-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nasa-mars.png
json_schemas:
- name: Manifest
  property_count: 8
  slug: manifest
- name: Photo
  property_count: 6
  slug: photo
jsonld:
- class_count: 6
  name: context Context
  property_count: 16
  slug: context
layout: provider
modified: '2026-06-13'
name: NASA Mars Rovers
nav: Providers
network: true
overview: 'NASA Mars Rovers publishes 3 APIs on the [APIs.io](https://apis.io/) network: Manifests API, Photos API, and Rovers API. Tagged areas include NASA, Mars, Rovers, Photos, and Image.


  The NASA Mars Rovers catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NASA Mars Rovers'' developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Nasa Mars Plans Pricing
  plan_count: 2
  slug: nasa-mars-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Nasa Mars Rate Limits
  slug: nasa-mars-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: NASA Mars Rovers API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nasa-mars-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 40.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 63.3
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 44.7
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nasa-mars/refs/heads/main/screenshots/nasa-mars-2026-06-20T185952.png
security:
- kind: authentication
  name: Nasa Mars Authentication
  slug: nasa-mars-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nasa Mars Domain Security
  slug: nasa-mars-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nasa-mars
tags:
- NASA
- Mars
- Rovers
- Photos
- Image
- Space
- Planetary Science
- Open Data
website: https://api.nasa.gov/
---
