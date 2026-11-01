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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: ViaLoop provides smart vehicle tracking and monitoring solutions via its OBD device and companion app.
  name: ViaLoop API
  slug: vialoop-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/vialoop/llms/vialoop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vialoop-llms.txt
- group: other
  href: https://artifacts.apis.io/vialoop/hosts/vialoop-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vialoop-hosts.yml
- group: other
  href: https://artifacts.apis.io/vialoop/vendors/vialoop-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vialoop-vendors.yml
- group: auth
  href: https://artifacts.apis.io/vialoop/security/vialoop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vialoop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vialoop.in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://vialoop.in/
- group: docs
  title: ''
  type: Documentation
  url: https://vialoop.in/
- group: docs
  title: ''
  type: APIReference
  url: https://vialoop.in/
- group: start
  title: ''
  type: GettingStarted
  url: https://vialoop.in/fleet/
- group: company
  title: ''
  type: Blog
  url: https://vialoop.in/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vialoop.in/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vialoop.in/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vialoop.in
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the API host (api.vialoop.in) despite probing common spec endpoints.
  evidence:
  - status: 404
    url: https://api.vialoop.in/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: ViaLoop provides smart vehicle tracking and monitoring solutions through a pocket-sized OBD device and companion app. It offers real-time location, fuel intelligence, vehicle health monitoring, and safety alerts for individual drivers and fleet operators. The platform supports plug‑and‑play setup, live tracking, and analytics to improve fuel efficiency and fleet management.
image: https://vialoop.in/opengraph-image?3c5c61a79832df2c
layout: provider
modified: '2026-10-19'
name: ViaLoop
nav: Providers
network: true
overview: 'ViaLoop is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Vehicle Tracking, OBD Device, Fuel Monitoring, Driver Safety, and Car Sharing.


  ViaLoop''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Vialoop Domain Security
  slug: vialoop-domain-security
  summary_line: TLSv1.3 · HSTS
slug: vialoop
tags:
- Vehicle Tracking
- OBD Device
- Fuel Monitoring
- Driver Safety
- Car Sharing
- Multi‑vehicle
- GPS Tracking
website: https://vialoop.in/
---
