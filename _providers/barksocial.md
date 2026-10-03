---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API for Barksocial platform (dog‑friendly bar and community).
  name: Barksocial API
  slug: barksocial-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/barksocial/refs/heads/main/llms/barksocial-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/barksocial-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/barksocial/refs/heads/main/well-known/barksocial-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/barksocial-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/barksocial/refs/heads/main/hosts/barksocial-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barksocial-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/barksocial/refs/heads/main/vendors/barksocial-vendors.yml
  title: ''
  type: Vendors
  url: vendors/barksocial-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://barksocial.com/blogs/press
- group: start
  title: ''
  type: Login
  url: https://www.barksocial.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/barksocial/refs/heads/main/security/barksocial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barksocial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://barksocial.com
created: '2026-09-27'
description: Barksocial operates a dog‑friendly bar and community space offering memberships, day‑care, grooming, boarding, and a full‑service restaurant. Located in Baltimore and Columbia, it provides a social hub for dog owners to connect, host events, and enjoy amenities for both pets and people. The brand emphasizes a safe, dog‑centric environment with park rules, events, and a loyalty program.
image: http://barksocial.com/cdn/shop/files/IMG_5104_2_99b66d36-68ed-444c-b0bc-ec090bb42180.webp?v=1757087713
layout: provider
modified: '2026-09-27'
name: Barksocial
nav: Providers
network: true
overview: Barksocial publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Dog, Bar, Community, and Membership.
random_paper: 17
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Barksocial Domain Security
  slug: barksocial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: barksocial
tags:
- Company
- Dog
- Bar
- Community
- Membership
website: https://barksocial.com
---
