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
  href: https://raw.githubusercontent.com/api-evangelist/curaway/refs/heads/main/hosts/curaway-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curaway-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curaway/refs/heads/main/security/curaway-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curaway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.curaway.com
coverage:
  checked: '2026-10-12'
  detail: The homepage returns a JavaScript shell and no machine‑readable documentation was found.
  evidence:
  - status: 200
    url: https://www.curaway.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Curaway Medical Technology Co., Ltd. is a Chinese high‑tech enterprise specializing in precision minimally invasive medical devices. It develops and manufactures products for energy ablation, biopsy localization, delicate surgery and surgical robotics, serving oncology, peripheral intervention and smart medical fields. The company emphasizes innovative R&D, international quality standards, and provides solutions that reduce trauma, complications and recovery time for patients.
layout: provider
modified: '2026-10-12'
name: Curaway
nav: Providers
network: true
overview: Curaway is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical, Devices, Precision, Minimally-Invasive, and China.
random_paper: 16
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 5
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
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Curaway Domain Security
  slug: curaway-domain-security
  summary_line: TLSv1.3 · DMARC
slug: curaway
tags:
- Medical
- Devices
- Precision
- Minimally-Invasive
- China
website: https://www.curaway.com
---
