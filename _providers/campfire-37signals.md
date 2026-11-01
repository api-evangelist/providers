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
    mcp_server: documented
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/campfire-37signals/hosts/campfire-37signals-hosts.yml
  title: ''
  type: Hosts
  url: hosts/campfire-37signals-hosts.yml
- group: other
  href: https://artifacts.apis.io/campfire-37signals/vendors/campfire-37signals-vendors.yml
  title: ''
  type: Vendors
  url: vendors/campfire-37signals-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://once.com/campfire/changelog
- group: auth
  href: https://artifacts.apis.io/campfire-37signals/security/campfire-37signals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/campfire-37signals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://once.com/campfire
coverage:
  checked: '2026-10-27'
  detail: The Campfire product page provides no developer documentation or API references.
  evidence:
  - status: 200
    url: https://once.com/campfire
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: Campfire is an installable, self‑hosted group chat system developed by the team behind Basecamp. It lets companies run their own chat server with features like rooms, @mentions, direct messages, and mobile support, all without recurring subscription fees. The code is open‑source, allowing full customization and data ownership. Campfire aims to provide a simple, privacy‑focused alternative to services like Slack or Microsoft Teams.
image: https://once.com/assets/images/opengraph-campfire.png
layout: provider
modified: '2026-10-27'
name: Campfire
nav: Providers
network: true
overview: 'Campfire is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Chat, OpenSource, SelfHosted, Collaboration, and Privacy.


  Campfire''s developer surface includes changelog and 4 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 6
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
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Campfire 37Signals Domain Security
  slug: campfire-37signals-domain-security
  summary_line: TLSv1.3 · DMARC
slug: campfire-37signals
tags:
- Chat
- OpenSource
- SelfHosted
- Collaboration
- Privacy
website: https://once.com/campfire
---
