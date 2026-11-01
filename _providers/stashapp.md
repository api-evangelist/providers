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
api_count: 1
apis:
- description: API documentation for Stash, an open-source self‑hosted media organizer.
  name: Stash API
  slug: stash-api
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/stashapp/well-known/stashapp-opencollective-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stashapp-opencollective-security.txt
- group: agent
  href: https://artifacts.apis.io/stashapp/well-known/stashapp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stashapp-well-known.yml
- group: other
  href: https://artifacts.apis.io/stashapp/hosts/stashapp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stashapp-hosts.yml
- group: other
  href: https://artifacts.apis.io/stashapp/vendors/stashapp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stashapp-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/stashapp/stash/releases/latest
- group: company
  title: ''
  type: Blog
  url: https://stashapp.cc/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stashapp.cc/faq/setup/
- group: auth
  href: https://artifacts.apis.io/stashapp/security/stashapp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stashapp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stashapp.cc/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stashapp.cc/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stashapp
- group: operate
  title: ''
  type: Support
  url: https://discourse.stashapp.cc/
- group: commercial
  title: ''
  type: Pricing
  url: https://opencollective.com/stashapp
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.stashapp.cc/api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Stash is an open-source self‑hosted media organizer designed for personal adult video and image collections. It provides a private, PornHub‑like experience, allowing users to browse, tag, rate, and stream their own content securely. Features include scene management, markers, galleries, metadata scraping, plugin support, and cross‑platform installations (Windows, macOS, Linux, Docker, Synology, TrueNAS, Unraid). The project is community‑driven, with documentation, source code, and donation options available.
layout: provider
modified: '2026-10-28'
name: Stash
nav: Providers
network: true
overview: 'Stash is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Open-source, Adult, and Organizer.


  Stash''s developer surface includes changelog, engineering blog, getting-started guide, documentation, support, pricing, and 7 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 53.6
    operational_transparency: 31.6
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
  name: Stashapp Domain Security
  slug: stashapp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stashapp
tags:
- Company
- Media
- Open-source
- Adult
- Organizer
website: https://stashapp.cc/
---
