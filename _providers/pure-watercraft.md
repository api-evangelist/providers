---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  - '{''url'': ''https://purewatercraft.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.pureoutboards.com/ — a different registrable domain (purewatercraft.com -> pureoutboards.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://purewatercraft.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pure-watercraft-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pure-watercraft-domain-security.yml
coverage:
  checked: '2026-08-26'
  detail: Pure Watercraft, Inc. wound down and sold its assets in 2024, and purewatercraft.com — including app.purewatercraft.com, the host that served its telemetry companion app — now 301s to www.pureoutboards.com, a WooCommerce storefront run by the acquirer of the outboard line, so there is no Pure Watercraft surface left to profile.
  evidence:
  - status: 301
    url: https://purewatercraft.com/
  - status: 301
    url: https://app.purewatercraft.com/
  - status: 404
    url: https://www.pureoutboards.com/openapi.json
  - status: 404
    url: https://www.pureoutboards.com/.well-known/agent-card.json
  - status: 200
    url: https://github.com/purewatercraft
  reason: defunct
  state: none
created: '2026-08-26'
description: Pure Watercraft was a Seattle, Washington electric marine propulsion company founded in 2011 by Andy Rebele. It built electric outboard motors marketed as drop-in replacements for 20 to 50 horsepower gas engines, along with lithium-ion battery packs, chargers and Wi-Fi throttle controls, plus a consumer companion mobile app that pulled trip history and telemetry off the outboard over Bluetooth and pushed firmware updates to it. General Motors took a reported 25 percent stake in 2021. The company wound down and sold its assets in 2024, with the outboard line acquired by Raider Outboards and other assets going to a Seattle electric boat club. purewatercraft.com and the former companion-app host app.purewatercraft.com both now 301 to www.pureoutboards.com, the Pure Electric Outboard storefront operated by the acquirer. Pure Watercraft never published a public developer program, API reference, SDK, or machine-readable API contract; its telemetry cloud was private to its own mobile
  app.
image: https://www.pureoutboards.com/wp-content/uploads/2025/07/cropped-PURE-neon-green-cmyk-scaled-1.webp
layout: provider
modified: '2026-08-26'
name: Pure Watercraft
nav: Providers
network: true
overview: Pure Watercraft is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electric Vehicles, Marine, Manufacturing, and Hardware.
plans:
- name: Pure Watercraft Plans Pricing
  plan_count: 0
  slug: pure-watercraft-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Pure Watercraft Rate Limits
  slug: pure-watercraft-rate-limits
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pure-watercraft/refs/heads/main/screenshots/pure-watercraft-2026-09-02T152330.png
security:
- kind: domain-security
  name: Pure Watercraft Domain Security
  slug: pure-watercraft-domain-security
  summary_line: TLSv1.3
slug: pure-watercraft
tags:
- Company
- Electric Vehicles
- Marine
- Manufacturing
- Hardware
- Consumer Products
- Mobility
- Defunct
website: https://purewatercraft.com/
---
