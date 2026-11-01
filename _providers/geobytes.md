---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Geobytes provides free and paid JSON/JSON‑P IP location APIs such as Get City Details, GeoDirection, and Get Nearby Cities.
  name: Geobytes IP Location APIs
  slug: geobytes-ip-location-apis
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/geobytes/hosts/geobytes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/geobytes-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://geobytes.com/status/
- group: auth
  href: https://artifacts.apis.io/geobytes/security/geobytes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geobytes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://geobytes.com/
- group: docs
  title: ''
  type: Documentation
  url: https://geobytes.com/geobytes-apis/
- group: docs
  title: ''
  type: APIReference
  url: https://geobytes.com/geobytes-apis/
- group: operate
  title: ''
  type: Support
  url: https://geobytes.com/faq/
coverage:
  checked: '2026-10-26'
  detail: The provider offers JSON‑P APIs but no machine‑readable OpenAPI or other contract was found.
  evidence:
  - status: 404
    url: https://geobytes.com/openapi.json
  - status: 404
    url: https://geobytes.com/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Geobytes provides IP geolocation and location-based services since 1999, offering a suite of free and paid JSON/JSON‑P APIs such as GetCityDetails, GeoDirection, GeoIf, and distance calculations. Their services are used by thousands of websites to obtain city, country, region, and IP‑based location data, with generous free limits and optional Mapbytes micro‑payment plans for higher usage.
layout: provider
modified: '2026-10-26'
name: Geobytes
nav: Providers
network: true
overview: 'Geobytes is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geolocation, IP, API, and Free.


  Geobytes'' developer surface includes documentation, API reference, support, and 4 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Geobytes Domain Security
  slug: geobytes-domain-security
  summary_line: TLSv1.3 · DMARC
slug: geobytes
tags:
- Company
- Geolocation
- IP
- API
- Free
website: https://geobytes.com/
---
