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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/betterhalf/refs/heads/main/hosts/betterhalf-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betterhalf-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/betterhalf/refs/heads/main/vendors/betterhalf-vendors.yml
  title: ''
  type: Vendors
  url: vendors/betterhalf-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/betterhalf/refs/heads/main/packages/betterhalf-packages.yml
  title: ''
  type: SDKs
  url: packages/betterhalf-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/betterhalf/refs/heads/main/packages/betterhalf-packages.yml
  title: ''
  type: Packages
  url: packages/betterhalf-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/betterhalf/refs/heads/main/security/betterhalf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betterhalf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.betterhalf.ai
coverage:
  checked: '2026-09-28'
  detail: OpenAPI spec endpoints on api.betterhalf.ai returned 404, indicating no machine‑readable contract is published.
  evidence:
  - status: 404
    url: https://api.betterhalf.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Betterhalf is an Indian matchmaking and matrimony mobile application that helps users find genuine and verified profiles for marriage. The app offers in‑app purchases, extensive profile verification, and a focus on Indian cultural preferences. It is available on Android via the Google Play Store and emphasizes privacy and secure matchmaking for its users.
layout: provider
modified: '2026-09-28'
name: Betterhalf
nav: Providers
network: true
overview: Betterhalf is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Matchmaking, Matrimony, Mobile App, and Indian.
random_paper: 1
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Betterhalf Domain Security
  slug: betterhalf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: betterhalf
tags:
- Company
- Matchmaking
- Matrimony
- Mobile App
- Indian
website: https://www.betterhalf.ai
---
