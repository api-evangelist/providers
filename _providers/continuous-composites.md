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
  href: https://raw.githubusercontent.com/api-evangelist/continuous-composites/refs/heads/main/hosts/continuous-composites-hosts.yml
  title: ''
  type: Hosts
  url: hosts/continuous-composites-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/continuous-composites/refs/heads/main/security/continuous-composites-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/continuous-composites-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://continuouscomposites.com/
coverage:
  checked: '2026-10-10'
  detail: Home page returns a JavaScript shell with no machine-readable docs.
  evidence:
  - status: 202
    url: https://continuouscomposites.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-10'
description: Continuous Composites advances composite manufacturing with its patented CF3D® continuous fiber 3D printing technology. Founded in 2012 in Coeur d'Alene, Idaho, the company delivers high‑performance aerospace and defense structures, offering rapid‑curing resins, intelligent automation, and scalable production for demanding applications.
layout: provider
modified: '2026-10-10'
name: Continuous Composites
nav: Providers
network: true
overview: Continuous Composites is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Aerospace, Defense, and 3D Printing.
random_paper: 6
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
  name: Continuous Composites Domain Security
  slug: continuous-composites-domain-security
  summary_line: TLSv1.3 · DMARC
slug: continuous-composites
tags:
- Company
- Manufacturing
- Aerospace
- Defense
- 3D Printing
- Composite Materials
website: https://continuouscomposites.com/
---
