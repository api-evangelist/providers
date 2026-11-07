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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 16.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/guilded/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/guilded/well-known/guilded-guilded-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/guilded-guilded-security.txt
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/roblox
- group: auth
  href: https://artifacts.apis.io/guilded/well-known/guilded-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/guilded-security.txt
- group: auth
  href: https://artifacts.apis.io/guilded/well-known/guilded-partner-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/guilded-partner-security.txt
- group: auth
  href: https://artifacts.apis.io/guilded/well-known/guilded-opendata-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/guilded-opendata-security.txt
- group: auth
  href: https://artifacts.apis.io/guilded/well-known/guilded-open-data-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/guilded-open-data-security.txt
- group: auth
  href: https://artifacts.apis.io/guilded/well-known/guilded-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/guilded-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/guilded/well-known/guilded-developers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/guilded-developers-security.txt
- group: auth
  href: https://artifacts.apis.io/guilded/well-known/guilded-developer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/guilded-developer-security.txt
- group: auth
  href: https://artifacts.apis.io/guilded/well-known/guilded-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/guilded-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/guilded/well-known/guilded-datahub-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/guilded-datahub-security.txt
- group: auth
  href: https://artifacts.apis.io/guilded/well-known/guilded-data-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/guilded-data-security.txt
- group: auth
  href: https://artifacts.apis.io/guilded/well-known/guilded-apis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/guilded-apis-security.txt
- group: agent
  href: https://artifacts.apis.io/guilded/well-known/guilded-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/guilded-well-known.yml
- group: other
  href: https://artifacts.apis.io/guilded/hosts/guilded-hosts.yml
  title: ''
  type: Hosts
  url: hosts/guilded-hosts.yml
- group: other
  href: https://artifacts.apis.io/guilded/vendors/guilded-vendors.yml
  title: ''
  type: Vendors
  url: vendors/guilded-vendors.yml
- group: build
  href: https://artifacts.apis.io/guilded/packages/guilded-packages.yml
  title: ''
  type: SDKs
  url: packages/guilded-packages.yml
- group: build
  href: https://artifacts.apis.io/guilded/packages/guilded-packages.yml
  title: ''
  type: Packages
  url: packages/guilded-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.guilded.gg/
- group: auth
  href: https://artifacts.apis.io/guilded/security/guilded-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/guilded-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/guilded/security/guilded-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/guilded-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://guilded.gg/
coverage:
  checked: '2026-10-28'
  detail: The provider’s documentation redirects to a marketing site with no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://www.guilded.gg/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Guilded is a communication platform designed for gaming communities, offering chat, voice, video, and community management tools. It provides servers, channels, roles, and integrations, enabling gamers to organize events, share media, and collaborate in real-time. The service includes mobile and desktop apps, a web client, and extensive API access for developers to build bots and integrate Guilded features into other applications.
image: https://www.guilded.gg/asset/OpenGraph/GuildedLarge.png
layout: provider
modified: '2026-10-28'
name: Guilded
nav: Providers
network: true
overview: 'Guilded is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Communications, Gaming, Community, Chat, and Platform.


  Guilded''s developer surface includes documentation and 22 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 18.3
    discoverability: 48.2
    operational_transparency: 5.3
  previous_composite: 9.9
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/guilded/guilded-2026-11-03T133136.png
security:
- kind: domain-security
  name: Guilded Domain Security
  slug: guilded-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Guilded Vulnerability Disclosure
  slug: guilded-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: guilded
tags:
- Communications
- Gaming
- Community
- Chat
- Platform
website: https://guilded.gg/
---
