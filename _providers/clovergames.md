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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clovergames/refs/heads/main/hosts/clovergames-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clovergames-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clovergames/refs/heads/main/vendors/clovergames-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clovergames-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clovergames/refs/heads/main/security/clovergames-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clovergames-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/clovergames
coverage:
  checked: '2026-10-09'
  detail: No public API documentation or developer program could be found for Clovergames.
  evidence:
  - status: 403
    url: https://equityzen.com/company/clovergames
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Clovergames is a mobile game development studio known for titles such as Lord of Heroes and Heaven Hells. The company creates anime‑style RPGs and action games for Android and iOS platforms, targeting a global audience of casual gamers. While its public website is not reachable, the brand appears on app stores, social media, and third‑party listings, confirming its active presence in the gaming market. No public API documentation has been found.
layout: provider
modified: '2026-10-09'
name: Clovergames
nav: Providers
network: true
overview: Clovergames is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mobile, Gaming, Anime, rpg, and ios.
random_paper: 10
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clovergames Domain Security
  slug: clovergames-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clovergames
tags:
- Mobile
- Gaming
- Anime
- rpg
- ios
website: https://equityzen.com/company/clovergames
---
