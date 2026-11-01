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
api_count: 1
apis:
- description: EteSync provides encrypted synchronization but does not publish a public developer API.
  name: EteSync API
  slug: etesync-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/etesync/plans/etesync-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/etesync-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/etesync/security/etesync-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/etesync-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/etesync/well-known/etesync-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/etesync-security.txt
- group: auth
  href: https://artifacts.apis.io/etesync/well-known/etesync-etesync-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/etesync-etesync-security.txt
- group: auth
  href: https://artifacts.apis.io/etesync/well-known/etesync-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/etesync-api-security.txt
- group: agent
  href: https://artifacts.apis.io/etesync/well-known/etesync-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/etesync-well-known.yml
- group: other
  href: https://artifacts.apis.io/etesync/hosts/etesync-hosts.yml
  title: ''
  type: Hosts
  url: hosts/etesync-hosts.yml
- group: build
  href: https://artifacts.apis.io/etesync/packages/etesync-packages.yml
  title: ''
  type: SDKs
  url: packages/etesync-packages.yml
- group: build
  href: https://artifacts.apis.io/etesync/packages/etesync-packages.yml
  title: ''
  type: Packages
  url: packages/etesync-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.etesync.com/tos/
- group: start
  title: ''
  type: SignUp
  url: https://www.etesync.com/accounts/signup/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blog.etesync.com/privacy-focused-mastodon-profiles-worth-following
- group: commercial
  title: ''
  type: Pricing
  url: https://www.etesync.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/etesync
- group: company
  title: ''
  type: Blog
  url: https://blog.etesync.com/
- group: auth
  href: https://artifacts.apis.io/etesync/security/etesync-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/etesync-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/etesync/security/etesync-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/etesync-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://etesync.com/
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published on any discovered host.
  evidence:
  - status: 404
    url: https://api.etesync.com/openapi.json
  - status: 404
    url: https://www.etesync.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: EteSync (Etebase) provides a secure, end‑to‑end encrypted synchronization service for contacts, calendars, tasks and notes across devices. It operates with a journaled, zero‑knowledge architecture, hosting servers in Austria while ensuring users never need to trust the server, emphasizing privacy as a basic right.
image: http://www.etesync.com/static/img/logo.e9587f014292.png
layout: provider
modified: '2026-10-27'
name: EteSync (Etebase)
nav: Providers
network: true
overview: 'EteSync (Etebase) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Sync, Privacy, and OpenSource.


  EteSync (Etebase)''s developer surface includes signup flow, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Etesync Plans Pricing
  plan_count: 2
  slug: etesync-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Etesync Domain Security
  slug: etesync-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Etesync Vulnerability Disclosure
  slug: etesync-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: etesync
tags:
- Company
- Security
- Sync
- Privacy
- OpenSource
website: https://etesync.com/
---
