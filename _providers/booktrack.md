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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/booktrack/refs/heads/main/hosts/booktrack-hosts.yml
  title: ''
  type: Hosts
  url: hosts/booktrack-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/booktrack/refs/heads/main/vendors/booktrack-vendors.yml
  title: ''
  type: Vendors
  url: vendors/booktrack-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.booktrack.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.booktrack.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/booktrack
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/booktrack/refs/heads/main/security/booktrack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/booktrack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.booktrack.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-02'
description: Booktrack provides immersive audiobook production services, creating original soundtracks, sound design, and synchronized audio for publishers, authors, and studios. Since 2011, they have delivered over 300 immersive titles, leveraging patented technology to enhance the listening experience with multi‑layered soundscapes and Dolby Atmos. Their services include full‑production, post‑production, narration, quality control, and studio facilities, partnering with global publishers such as Penguin Random House and Simon & Schuster.
layout: provider
modified: '2026-10-02'
name: Booktrack
nav: Providers
network: true
overview: Booktrack is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Audiobooks, Production, Technology, and Publishing.
random_paper: 14
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Booktrack Domain Security
  slug: booktrack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: booktrack
tags:
- Company
- Audiobooks
- Production
- Technology
- Publishing
website: https://www.booktrack.com/
---
