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
  href: https://raw.githubusercontent.com/api-evangelist/companion/refs/heads/main/hosts/companion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/companion-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/companion/refs/heads/main/vendors/companion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/companion-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/companion/refs/heads/main/security/companion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/companion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://companion.ai/
coverage:
  checked: '2026-10-10'
  detail: Companion's documentation pages return JavaScript shells with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://app.companion.ai/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Companion builds the interface for intelligence, creating a new medium where people and machines can interact seamlessly. Their flagship product, Relay, aims to connect human intent with machine capabilities, fostering lifelong collaboration. The company envisions expanding what is possible between humans and AI, focusing on intuitive, scalable solutions for intelligent communication.
image: https://companion.ai/og.png?v=ff4b5c-avatar60-symbol-favicon2-tiltminus15
layout: provider
modified: '2026-10-09'
name: Companion
nav: Providers
network: true
overview: Companion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Communications, interface, Intelligence, and Platform.
random_paper: 18
score:
  band: minimal
  composite: 3.4
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
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Companion Domain Security
  slug: companion-domain-security
  summary_line: TLSv1.3 · DMARC
slug: companion
tags:
- Artificial Intelligence
- Communications
- interface
- Intelligence
- Platform
website: https://companion.ai/
---
