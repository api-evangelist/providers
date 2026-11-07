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
    mcp_server: documented
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for tracking airline Starlink devices.
  name: Airliner Starlink Tracker API
  slug: airliner-starlink-tracker-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/airlinestarlinktracker-com/llms/airlinestarlinktracker-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airlinestarlinktracker-com-llms.txt
- group: other
  href: https://artifacts.apis.io/airlinestarlinktracker-com/hosts/airlinestarlinktracker-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/airlinestarlinktracker-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/airlinestarlinktracker-com/vendors/airlinestarlinktracker-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/airlinestarlinktracker-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/airlinestarlinktracker-com/security/airlinestarlinktracker-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airlinestarlinktracker-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airlinestarlinktracker.com/
coverage:
  checked: '2026-11-01'
  detail: No public API documentation or machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://airlinestarlinktracker.com/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: Airline Starlink Tracker provides a comprehensive, publicly accessible database tracking the deployment of SpaceX Starlink satellite internet across major airlines worldwide. The site lists which airlines have Starlink Wi‑Fi installed, details per aircraft, fleet coverage, and offers tools to check individual flights and routes for connectivity. It aggregates data from airline announcements, flight tracking, and user reports to give travelers up‑to‑date information on in‑flight internet availability.
image: https://airlinestarlinktracker.com/static/social-image-hub.webp
layout: provider
modified: '2026-11-01'
name: Airline Starlink Tracker
nav: Providers
network: true
overview: Airline Starlink Tracker is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Aviation, Satellite, Wi-Fi, Data, and Tracking.
random_paper: 12
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 4.3
  provenance:
    mcp: first-party
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
security:
- kind: domain-security
  name: Airlinestarlinktracker Com Domain Security
  slug: airlinestarlinktracker-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airlinestarlinktracker-com
tags:
- Aviation
- Satellite
- Wi-Fi
- Data
- Tracking
website: https://airlinestarlinktracker.com/
---
