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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curvafix/refs/heads/main/hosts/curvafix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curvafix-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curvafix/refs/heads/main/security/curvafix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curvafix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.curvafix.com
coverage:
  checked: '2026-10-12'
  detail: The main site returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 202
    url: http://www.curvafix.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Curvafix, based in Bellevue, Washington, develops a unique curved intramedullary implant for pelvic fracture repair. The device, cleared by the FDA, follows the natural bone curvature, offering flexible surgical insertion and rigid fixation. In 2023 the company raised $39 million to expand its market and improve treatment for fragility fractures.
layout: provider
modified: '2026-10-12'
name: Curvafix
nav: Providers
network: true
overview: Curvafix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical, Orthopedic, Implant, and PelvicFracture.
random_paper: 14
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
  name: Curvafix Domain Security
  slug: curvafix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: curvafix
tags:
- Company
- Medical
- Orthopedic
- Implant
- PelvicFracture
website: http://www.curvafix.com
---
