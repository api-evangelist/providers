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
api_count: 1
apis:
- description: Data API for Crelvo providing game data.
  name: Crelvo Data API
  slug: crelvo-data-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/crelvo-dev/llms/crelvo-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crelvo-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/crelvo-dev/hosts/crelvo-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crelvo-dev-hosts.yml
- group: auth
  href: https://artifacts.apis.io/crelvo-dev/security/crelvo-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crelvo-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crelvo.dev/
coverage:
  checked: '2026-11-04'
  detail: Front page renders a JavaScript shell with no machine‑readable docs.
  evidence:
  - status: 200
    url: https://crelvo.dev/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Crelvo is an independent game studio that creates browser and mobile games such as Tabletop Siege and Hinterhood. The studio leverages AI assistance in development and offers a range of titles that blend strategic gameplay with immersive graphics.
image: https://crelvo.dev/og-image.png
layout: provider
modified: '2026-11-04'
name: Crelvo
nav: Providers
network: true
overview: Crelvo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Game Studio, Browser Games, Mobile Games, AI-assisted, and Indie.
random_paper: 7
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crelvo Dev Domain Security
  slug: crelvo-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crelvo-dev
tags:
- Game Studio
- Browser Games
- Mobile Games
- AI-assisted
- Indie
website: https://crelvo.dev/
---
