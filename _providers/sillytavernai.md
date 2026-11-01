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
- description: SillyTavern provides API connections to various LLM back‑ends, documented in the API Connections guide.
  name: SillyTavern API
  slug: sillytavern-api
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/sillytavernai/changelog/sillytavernai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sillytavernai-changelog.yml
- group: agent
  href: https://artifacts.apis.io/sillytavernai/llms/sillytavernai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sillytavernai-llms.txt
- group: other
  href: https://artifacts.apis.io/sillytavernai/hosts/sillytavernai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sillytavernai-hosts.yml
- group: other
  href: https://artifacts.apis.io/sillytavernai/vendors/sillytavernai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sillytavernai-vendors.yml
- group: build
  href: https://artifacts.apis.io/sillytavernai/packages/sillytavernai-packages.yml
  title: ''
  type: SDKs
  url: packages/sillytavernai-packages.yml
- group: build
  href: https://artifacts.apis.io/sillytavernai/packages/sillytavernai-packages.yml
  title: ''
  type: Packages
  url: packages/sillytavernai-packages.yml
- group: auth
  href: https://artifacts.apis.io/sillytavernai/security/sillytavernai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sillytavernai-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SillyTavern
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sillytavern.app
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sillytavern.app
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/sillytavern
- group: company
  title: ''
  type: Website
  url: https://docs.sillytavern.app
coverage:
  checked: '2026-10-19'
  detail: Documentation is rendered via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.sillytavern.app
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: SillyTavern AI provides an open-source, extensible AI chat interface that allows users to create and customize AI characters for role‑playing, storytelling, and interactive experiences. It supports multiple AI back‑ends, plug‑in extensions, and a rich UI for managing character lore, dialogue, and visual assets. The platform is community‑driven, with frequent updates and a growing ecosystem of tools and integrations, enabling creators to build immersive conversational worlds.
image: https://docs.sillytavern.app/static/banner.png
layout: provider
modified: '2026-10-18'
name: SillyTavern AI
nav: Providers
network: true
overview: 'SillyTavern AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Chatbots, Open Source, RolePlaying, and Community.


  SillyTavern AI''s developer surface includes changelog, documentation, support, and 9 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 57.1
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sillytavernai Domain Security
  slug: sillytavernai-domain-security
  summary_line: TLSv1.3
slug: sillytavernai
tags:
- Artificial Intelligence
- Chatbots
- Open Source
- RolePlaying
- Community
website: https://docs.sillytavern.app
---
