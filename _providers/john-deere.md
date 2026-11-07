---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 8
apis:
- description: The John Deere API allows developers to access and integrate data from John Deere's connected agricultural equipment and software platforms. The API surfaces equipment performance, field conditions, m
  name: John Deere API
  slug: john-deere
- description: Provides access to the organizations a John Deere Operations Center user belongs to. Organizations are the top-level container for users, fields, equipment, and partner relationships in Operations Cen
  name: John Deere Operations Center Organizations API
  slug: operations-center-organizations-api
- description: Exposes growers, farms, fields, and field boundaries in Operations Center so that partner applications can sync agronomic field metadata and boundary geometry.
  name: John Deere Operations Center Fields API
  slug: operations-center-fields-api
- description: Provides metadata, telematics, and engine information for connected John Deere machines, including machine locations, engine hours, hours of operation, alerts, and device state reports.
  name: John Deere Operations Center Machines API
  slug: operations-center-machines-api
- description: Returns information about field operations such as planting, application, tillage, and harvest performed by connected John Deere machines, with links to machine, field, and product data.
  name: John Deere Operations Center Field Operations API
  slug: operations-center-field-operations-api
- description: Manages crop, seed, chemical, and fertilizer products used in field operations, allowing applications to read and reconcile product catalogs across an organization.
  name: John Deere Operations Center Products API
  slug: operations-center-products-api
- description: Lets partner applications subscribe to event notifications from Operations Center so that changes to organizations, machines, fields, and field operations can be received without polling.
  name: John Deere Operations Center Webhook API
  slug: operations-center-webhook-api
- description: A suite of APIs supporting precision agriculture workflows including prescription maps, work plans, setup files, and equipment configuration for connected John Deere machinery.
  name: John Deere Precision Tech APIs
  slug: precision-tech-apis
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/john-deere/plans/john-deere-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/john-deere-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/john-deere/rate-limits/john-deere-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/john-deere-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/john-deere/finops/john-deere-finops.yml
  title: ''
  type: FinOps
  url: finops/john-deere-finops.yml
- group: auth
  href: https://artifacts.apis.io/john-deere/security/john-deere-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/john-deere-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JohnDeere
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/john-deere
- group: company
  title: ''
  type: Website
  url: https://developer.deere.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.deere.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.deere.com/
created: '2025-02-12'
description: John Deere is a renowned American corporation that specializes in manufacturing agricultural, construction, and forestry machinery. The company, founded in 1837 by John Deere, has a long history of innovation and has become a leader in the industry. John Deere's products include tractors, combines, excavators, and other equipment designed to support and improve farming and construction operations.
finops:
- has_sources: true
  method: generated
  name: John Deere Finops
  primary_unit: ''
  service_category: Agriculture / Equipment Telemetry
  slug: john-deere-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/john-deere.png
layout: provider
modified: '2026-04-28'
name: John Deere
nav: Providers
network: true
overview: 'John Deere is listed with 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Combines, Construction, Excavators, and Forestry.


  John Deere''s developer surface includes developer portal, documentation, and 7 more developer resources.'
plans:
- name: John Deere Plans Pricing
  plan_count: 1
  slug: john-deere-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: John Deere Rate Limits
  slug: john-deere-rate-limits
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 62.5
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/john-deere/john-deere-2026-06-20T183749.png
security:
- kind: domain-security
  name: John Deere Domain Security
  slug: john-deere-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: john-deere
tags:
- Agriculture
- Combines
- Construction
- Excavators
- Forestry
- Machinery
- Tractors
- AgTech
website: https://developer.deere.com/
---
