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
  href: https://raw.githubusercontent.com/api-evangelist/bounce-imaging/refs/heads/main/hosts/bounce-imaging-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bounce-imaging-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bounce-imaging/refs/heads/main/vendors/bounce-imaging-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bounce-imaging-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bounceimaging.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bounceimaging.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://bounceimaging.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bounce-imaging/refs/heads/main/security/bounce-imaging-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bounce-imaging-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bounceimaging.com/
coverage:
  checked: '2026-10-03'
  detail: No developer portal or API documentation is publicly available.
  evidence:
  - status: 404
    url: https://bounceimaging.com/developer
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: Bounce Imaging provides advanced imaging solutions for law enforcement, public safety, and defense sectors. Their product line includes rugged thermal cameras, K‑9 mounted systems, and remote sensing platforms designed for tactical operations, rescue missions, and border security. The company emphasizes real‑time video analytics, durability in harsh environments, and integration with command‑and‑control systems.
layout: provider
modified: '2026-10-03'
name: Bounce Imaging
nav: Providers
network: true
overview: Bounce Imaging is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Imaging, Law Enforcement, Defense, and Public Safety.
random_paper: 5
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bounce Imaging Domain Security
  slug: bounce-imaging-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bounce-imaging
tags:
- Company
- Imaging
- Law Enforcement
- Defense
- Public Safety
website: https://bounceimaging.com/
---
