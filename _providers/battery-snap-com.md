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
- group: agent
  href: https://artifacts.apis.io/battery-snap-com/llms/battery-snap-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/battery-snap-com-llms.txt
- group: other
  href: https://artifacts.apis.io/battery-snap-com/hosts/battery-snap-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/battery-snap-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/battery-snap-com/security/battery-snap-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/battery-snap-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://battery-snap.com/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI or other machine‑readable contract discovered on the provider’s website.
  evidence:
  - status: 301
    url: https://www.battery-snap.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BatterySnap provides comprehensive battery usage statistics and analytics for Android devices. The platform lets users install a free app to collect detailed graphs of battery life, compare across thousands of devices, and view aggregate data on device counts and battery events. It aims to help users monitor and improve battery performance through analytics and community insights.
image: https://www.battery-snap.com/static/favicon.png
layout: provider
modified: '2026-11-02'
name: BatterySnap
nav: Providers
network: true
overview: BatterySnap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Battery, Android, Analytics, Energy, and Monitoring.
random_paper: 22
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Battery Snap Com Domain Security
  slug: battery-snap-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: battery-snap-com
tags:
- Battery
- Android
- Analytics
- Energy
- Monitoring
website: https://battery-snap.com/
---
