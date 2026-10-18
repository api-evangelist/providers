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
api_count: 1
apis:
- description: API for Reclip social mobile app
  name: Reclip API
  slug: reclip-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/reclip/refs/heads/main/hosts/reclip-hosts.yml
  title: ''
  type: Hosts
  url: hosts/reclip-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/reclip/refs/heads/main/vendors/reclip-vendors.yml
  title: ''
  type: Vendors
  url: vendors/reclip-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reclip.app/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/reclip/refs/heads/main/security/reclip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reclip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reclip.app
coverage:
  checked: '2026-10-12'
  detail: The homepage renders only a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://reclip.app
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Reclip is a social mobile app that captures moments instantly, allowing users to share photos and videos with friends in real time. It emphasizes quick, spontaneous sharing, reducing time spent on editing and focusing on authentic experiences. The platform offers features like story creation, private messaging, and AI-powered highlights, positioning itself as a unique social networking tool for on‑the‑go users.
image: https://www.reclip.app/images/reclip/logo_bg_purple_256.png
layout: provider
modified: '2026-10-12'
name: Reclip
nav: Providers
network: true
overview: Reclip is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social, Mobile, PhotoSharing, VideoSharing, and Real-Time.
random_paper: 1
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Reclip Domain Security
  slug: reclip-domain-security
  summary_line: TLSv1.3 · DMARC
slug: reclip
tags:
- Social
- Mobile
- PhotoSharing
- VideoSharing
- Real-Time
website: https://reclip.app
---
