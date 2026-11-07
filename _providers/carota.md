---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/carota/hosts/carota-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carota-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://www.carota.ai/support/contact
- group: company
  title: ''
  type: Newsroom
  url: https://www.carota.ai/news/industry
- group: auth
  href: https://artifacts.apis.io/carota/security/carota-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carota-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carota.ai
coverage:
  checked: '2026-10-07'
  detail: The developer portal renders via JavaScript and no OpenAPI spec was discoverable.
  evidence:
  - status: 404
    url: https://api.carota.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Carota is a cutting‑edge leader in vehicle OTA (over‑the‑air) solutions, providing FOTA and OTA services for smart mobility, smart cockpit, MaaS, fleet management, and AIoT. The company offers a platform that enables automotive OEMs and suppliers to deploy software updates securely and efficiently across connected vehicles, enhancing safety, functionality, and user experience.
layout: provider
modified: '2026-10-07'
name: Carota
nav: Providers
network: true
overview: 'Carota is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, OTA, Smart Mobility, and AIoT.


  Carota''s developer surface includes support and 4 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 45.5
    operational_transparency: 0.0
  previous_composite: 4.2
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/carota/carota-2026-11-03T123412.png
security:
- kind: domain-security
  name: Carota Domain Security
  slug: carota-domain-security
  summary_line: TLSv1.2 · DMARC
slug: carota
tags:
- Company
- Automotive
- OTA
- Smart Mobility
- AIoT
website: https://www.carota.ai
---
