---
access_model:
  confidence: medium
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
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Licenseplatedata Agentic Access
  operation_count: 3
  slug: licenseplatedata-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://api.licenseplatedata.com/v1
  baseurl_source: declared
  description: Vehicle imagery
  name: LicensePlateData Images API
  slug: licenseplatedata-images-api
- baseURL: https://api.licenseplatedata.com/v1
  baseurl_source: declared
  description: Convert license plates to VINs
  name: LicensePlateData Plate API
  slug: licenseplatedata-plate-api
- baseURL: https://api.licenseplatedata.com/v1
  baseurl_source: declared
  description: Decode VINs into vehicle attributes
  name: LicensePlateData VIN API
  slug: licenseplatedata-vin-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LicensePlateData Images API
  slug: open-licenseplatedata-images-api
- collection_type: open
  name: LicensePlateData Images Plate API
  slug: open-licenseplatedata-plate-api
- collection_type: open
  name: LicensePlateData Images VIN API
  slug: open-licenseplatedata-vin-api
- collection_type: open
  name: LicensePlateData API
  slug: open-licenseplatedata
common:
- group: company
  title: ''
  type: Website
  url: https://licenseplatedata.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/licenseplatedata/refs/heads/main/agentic-access/licenseplatedata-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/licenseplatedata-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/licenseplatedata/refs/heads/main/security/licenseplatedata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/licenseplatedata-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/licenseplatedata/refs/heads/main/authentication/licenseplatedata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/licenseplatedata-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://licenseplatedata.com/blog
created: '2025-02-24'
description: Developer-first tools that give access to a library of vehicle information, including license plate to VIN lookup, VIN decoding, and OEM-style vehicle imagery for passenger cars, ATVs, and light and heavy trucks and trailers from 1980 to current model years.
finops:
- name: Licenseplatedata Finops
  service_category: API
  slug: licenseplatedata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/licenseplatedata.png
layout: provider
modified: '2026-09-16'
name: LicensePlateData
nav: Providers
network: true
overview: 'LicensePlateData publishes 3 APIs on the [APIs.io](https://apis.io/) network: Images API, Plate API, and VIN API. Tagged areas include Vehicles, License Plates, VIN, Automotive, and Plate Lookup.


  LicensePlateData''s developer surface includes authentication, engineering blog, and 3 more developer resources.'
plans:
- name: Licenseplatedata Plans Pricing
  plan_count: 3
  slug: licenseplatedata-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Licenseplatedata Rate Limits
  slug: licenseplatedata-rate-limits
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 46.5
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/licenseplatedata/refs/heads/main/screenshots/licenseplatedata-2026-06-20T184505.png
security:
- kind: authentication
  name: Licenseplatedata Authentication
  slug: licenseplatedata-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Licenseplatedata Domain Security
  slug: licenseplatedata-domain-security
  summary_line: TLSv1.3 · DMARC
slug: licenseplatedata
tags:
- Vehicles
- License Plates
- VIN
- Automotive
- Plate Lookup
- VIN Decoding
website: https://licenseplatedata.com
---
