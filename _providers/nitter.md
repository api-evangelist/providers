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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/nitter/hosts/nitter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nitter-hosts.yml
- group: other
  href: https://artifacts.apis.io/nitter/vendors/nitter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nitter-vendors.yml
- group: auth
  href: https://artifacts.apis.io/nitter/security/nitter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nitter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nitter.net
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/zedeus/nitter#readme
- group: docs
  title: ''
  type: APIReference
  url: https://nitter.net/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/zedeus/nitter#readme
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zedeus
coverage:
  checked: '2026-10-28'
  detail: The provider's site returns HTML for OpenAPI URLs, offering no machine‑readable specification.
  evidence:
  - status: 200
    url: https://nitter.net/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Nitter is an open-source, privacy-focused alternative front-end for Twitter, allowing users to view Twitter content without JavaScript, tracking, or a login. It provides a lightweight, fast, and ad‑free experience by fetching tweets server‑side and presenting them in a simple HTML interface. The project is community‑maintained, supports multiple instances, and aims to reduce data usage while preserving user privacy.
layout: provider
modified: '2026-10-28'
name: Nitter
nav: Providers
network: true
overview: 'Nitter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OpenSource, Privacy, TwitterAlternative, and Lightweight.


  Nitter''s developer surface includes documentation, API reference, getting-started guide, and 5 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
  name: Nitter Domain Security
  slug: nitter-domain-security
  summary_line: TLSv1.3 · HSTS
slug: nitter
tags:
- Company
- OpenSource
- Privacy
- TwitterAlternative
- Lightweight
website: https://nitter.net
---
