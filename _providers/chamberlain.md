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
  href: https://raw.githubusercontent.com/api-evangelist/chamberlain/refs/heads/main/hosts/chamberlain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chamberlain-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chamberlain/refs/heads/main/security/chamberlain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chamberlain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chamberlain.com/
coverage:
  checked: '2026-10-08'
  detail: API endpoint https://api.chamberlain.com/mcp returns 403 opaque, requiring authentication.
  evidence:
  - status: 403
    url: https://api.chamberlain.com/mcp
  reason: partner-login
  state: gated
created: '2026-10-08'
description: Chamberlain, known for its MyQ smart garage door controllers, provides hardware and software solutions for residential garage door automation. The company offers Wi‑Fi enabled openers, accessories, and a mobile app that lets users monitor and control their garage doors remotely. While the public API was previously accessible for third‑party integrations, recent changes have restricted unauthorized access, impacting many home‑automation platforms. The brand is part of The Chamberlain Group, serving DIY installers and homeowners with reliable, cost‑effective garage door products.
layout: provider
modified: '2026-10-08'
name: Chamberlain
nav: Providers
network: true
overview: Chamberlain is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Garage Door, Smart Home, IoT, and Automation.
random_paper: 20
score:
  band: minimal
  composite: 3.1
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
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Chamberlain Domain Security
  slug: chamberlain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chamberlain
tags:
- Company
- Garage Door
- Smart Home
- IoT
- Automation
website: https://www.chamberlain.com/
---
