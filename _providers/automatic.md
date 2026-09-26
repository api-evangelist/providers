---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 0
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automatic/refs/heads/main/lifecycle/automatic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/automatic-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/automatic/refs/heads/main/packages/automatic-packages.yml
  title: ''
  type: Packages
  url: packages/automatic-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automatic/refs/heads/main/llms/automatic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/automatic-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Automatic
created: '2026-07-17'
description: 'Automatic (Automatic Labs, Inc.) was a San Francisco connected-car company founded in 2011 by Thejo Kote and Jerry Jariyasunant. Its OBD-II adapter and companion mobile app turned almost any car built since 1996 into a connected car, adding trip logging, fuel and MPG tracking, engine-light diagnostics, parking recall, and automatic crash alerts. Automatic ran a public developer platform at developer.automatic.com built around three surfaces: a REST API exposing trip, user, and vehicle data; an Events API delivering real-time driving events such as ignition on/off, hard braking, acceleration, speeding, and location changes over webhooks and websockets; and a private-beta Streaming SDK that read raw OBD-II data from the second-generation adapter over Bluetooth. SiriusXM acquired the company on 2017-04-27 for approximately $115 million, and all operations were shut down on 2020-05-28. THIS COMPANY IS DEFUNCT — no API, developer portal, or documentation remains online, and the
  automatic.com domain now belongs to the unrelated company Automattic. This profile is retained as a historical record of a notable connected-car API platform.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/automatic.png
layout: provider
modified: '2026-07-19'
name: Automatic
nav: Providers
network: true
overview: Automatic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Connected Car, Telematics, and IoT.
random_paper: 21
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 4
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
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/automatic/refs/heads/main/screenshots/automatic-2026-07-25T201844.png
slug: automatic
tags:
- Company
- Automotive
- Connected Car
- Telematics
- IoT
- Vehicle Data
- OBD-II
- Defunct
---
