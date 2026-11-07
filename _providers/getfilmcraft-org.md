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
api_count: 1
apis:
- description: FilmCraft provides a CLI, JSON channel, and MCP server for automation of video editing.
  name: FilmCraft API
  slug: filmcraft-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/getfilmcraft-org/llms/getfilmcraft-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getfilmcraft-org-llms.txt
- group: other
  href: https://artifacts.apis.io/getfilmcraft-org/hosts/getfilmcraft-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getfilmcraft-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/getfilmcraft-org/vendors/getfilmcraft-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getfilmcraft-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getfilmcraft.org/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getfilmcraft.org/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/storytold/filmcraft/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://getfilmcraft.org/guides/filmcraft-web-setup-troubleshooting
- group: auth
  href: https://artifacts.apis.io/getfilmcraft-org/security/getfilmcraft-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getfilmcraft-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getfilmcraft.org/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/storytold/filmcraft
coverage:
  checked: '2026-11-05'
  detail: The provider's documentation site renders via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://getfilmcraft.org/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: FilmCraft is a free, open-source video editor from ArtCraft. It runs on macOS, Windows, and Linux, and also offers a browser‑based online editor. Users can download the desktop application or edit videos directly in the web UI, with features comparable to Adobe Premiere Pro. The project is community‑driven, MIT‑licensed, and provides a CLI, JSON channel, and an MCP server for automation.
image: https://getfilmcraft.org/imgs/filmcraft/hero.webp
layout: provider
modified: '2026-11-05'
name: Filmcraft
nav: Providers
network: true
overview: 'Filmcraft is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video Editing, Open Source, Cross-Platform, CLI, and Automation.


  Filmcraft''s developer surface includes changelog, getting-started guide, documentation, and 7 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Getfilmcraft Org Domain Security
  slug: getfilmcraft-org-domain-security
  summary_line: TLSv1.3 · HSTS
slug: getfilmcraft-org
tags:
- Video Editing
- Open Source
- Cross-Platform
- CLI
- Automation
website: https://getfilmcraft.org/
---
