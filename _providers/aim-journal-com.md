---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Aim Journal fitness platform providing workout logging and AI personalization.
  name: Aim Journal API
  slug: aim-journal-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/aim-journal-com/authentication/aim-journal-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aim-journal-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/aim-journal-com/llms/aim-journal-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aim-journal-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aim-journal-com/hosts/aim-journal-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aim-journal-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aim-journal-com/vendors/aim-journal-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aim-journal-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aim-journal-com/security/aim-journal-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aim-journal-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aim-journal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aim-journal.com/guides/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aim-journal.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aim-journal.com/support/
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://aim-journal.com/guides/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AIm Workout Journal is an AI‑powered fitness tracking platform that lets users log workouts, set goals, and receive personalized training programs via Claude or ChatGPT. Users sign up with an email link, connect their AI assistant, and the service records each set, offering charts, progress maps, and data export options. The app runs on the Model Context Protocol (MCP) enabling seamless read/write access for AI assistants, with automatic daily backups and secure data handling.
image: https://aim-journal.com/og/landing-en.png
layout: provider
modified: '2026-11-01'
name: AIm Workout Journal
nav: Providers
network: true
overview: 'AIm Workout Journal is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fitness, Artificial Intelligence, Workouts, Health, and Personalization.


  AIm Workout Journal''s developer surface includes authentication, documentation, support, and 6 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 13.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aim Journal Com Authentication
  slug: aim-journal-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aim Journal Com Domain Security
  slug: aim-journal-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aim-journal-com
tags:
- Fitness
- Artificial Intelligence
- Workouts
- Health
- Personalization
website: https://aim-journal.com/
---
