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
- description: ArchiveTeam provides tools and documentation for archiving projects, listed on their wiki.
  name: ArchiveTeam API
  slug: archiveteam-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/archiveteam/hosts/archiveteam-hosts.yml
  title: ''
  type: Hosts
  url: hosts/archiveteam-hosts.yml
- group: auth
  href: https://artifacts.apis.io/archiveteam/security/archiveteam-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/archiveteam-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://archiveteam.org/
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.archiveteam.org/
coverage:
  checked: '2026-10-28'
  detail: The wiki pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://wiki.archiveteam.org/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: ArchiveTeam (Warrior) is a loose collective of rogue archivists, programmers, writers, and loudmouths dedicated to saving digital heritage since 2009. The organization runs the archiveteam.org wiki as an information depot for archiving projects, providing tools, advice, and a hub for preserving websites and data at risk of loss.
layout: provider
modified: '2026-10-28'
name: ArchiveTeam (Warrior)
nav: Providers
network: true
overview: 'ArchiveTeam (Warrior) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Archiving, Open Source, Digital Preservation, and Community.


  ArchiveTeam (Warrior)''s developer surface includes documentation and 3 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.9
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/archiveteam/archiveteam-2026-11-03T121105.png
security:
- kind: domain-security
  name: Archiveteam Domain Security
  slug: archiveteam-domain-security
  summary_line: TLSv1.3 · HSTS
slug: archiveteam
tags:
- Company
- Archiving
- Open Source
- Digital Preservation
- Community
website: https://archiveteam.org/
---
