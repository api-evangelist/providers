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
  href: https://artifacts.apis.io/decibelshield-app/llms/decibelshield-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/decibelshield-app-llms.txt
- group: other
  href: https://artifacts.apis.io/decibelshield-app/hosts/decibelshield-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/decibelshield-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/decibelshield-app/vendors/decibelshield-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/decibelshield-app-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://decibelshield.app/press/
- group: auth
  href: https://artifacts.apis.io/decibelshield-app/security/decibelshield-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decibelshield-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decibelshield.app/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://decibelshield.app/api/mcp
  - status: 200
    url: https://decibelshield.app/
  reason: no-developer-program
  state: none
created: '2026-11-05'
description: Decibel Shield provides a free online real-time sound level meter that runs entirely in the browser. Users can measure ambient noise with their device microphone, view live decibel readings, and see minimum, average, and maximum levels. The tool includes a guide to occupational exposure limits from NIOSH and OSHA, and offers a save‑report feature. No audio is recorded or uploaded, ensuring privacy while delivering instant feedback for personal, educational, or workplace awareness.
image: https://decibelshield.app/og/default.png
layout: provider
modified: '2026-11-05'
name: Decibel Shield
nav: Providers
network: true
overview: Decibel Shield is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sound Meter, Occupational Safety, Health, Web App, and Audio Measurement.
random_paper: 7
score:
  band: minimal
  composite: 3.9
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
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Decibelshield App Domain Security
  slug: decibelshield-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: decibelshield-app
tags:
- Sound Meter
- Occupational Safety
- Health
- Web App
- Audio Measurement
website: https://decibelshield.app/
---
