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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/80l-app/hosts/80l-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/80l-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/80l-app/vendors/80l-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/80l-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://80l.app/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://80l.app/privacy-policy
- group: auth
  href: https://artifacts.apis.io/80l-app/security/80l-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/80l-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://80l.app/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://80l.app/
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: Eighty is a mobile application that gamifies real-life productivity by turning daily tasks and personal development into role‑playing game quests. Users create, complete, and share real‑world challenges, earning experience points, leveling up from 1 to 80, and building a character with stats like Health, Strength, Intelligence, Skill, and Charisma. The platform encourages habit formation, community interaction, and skill growth through a quest‑based system, available on iOS and soon Android, with a focus on personal growth and social motivation.
image: https://80l.app/og-image.png
layout: provider
modified: '2026-10-31'
name: Eighty
nav: Providers
network: true
overview: Eighty is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Productivity, Gamification, Lifestyle, Mobile, and RPG.
random_paper: 2
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 8.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 80L App Domain Security
  slug: 80l-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: 80l-app
tags:
- Productivity
- Gamification
- Lifestyle
- Mobile
- RPG
website: https://80l.app/
---
