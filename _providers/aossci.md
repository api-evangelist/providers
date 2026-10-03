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
  href: https://raw.githubusercontent.com/api-evangelist/aossci/refs/heads/main/hosts/aossci-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aossci-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.aossci.com/news/185
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aossci/refs/heads/main/security/aossci-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aossci-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aossci.com
coverage:
  checked: 2026-09-25
  detail: Main website renders a JavaScript shell and no machine‑readable API spec was found.
  evidence:
  - status: 200
    url: https://www.aossci.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Aossci (傲势科技) designs and manufactures long-endurance electric and hybrid unmanned aerial vehicles for public safety, forest fire fighting, emergency rescue, energy inspection and other industrial applications. Based in Chengdu, China, the company offers a portfolio of fixed‑wing and VTOL drones such as the XC‑150, XC‑25 and XB‑12, integrated with cloud platforms for mission planning, data analytics and satellite communications.
image: https://www.aossci.com/_nuxt/img/8a8e867.png
layout: provider
modified: '2026-09-25'
name: Aossci
nav: Providers
network: true
overview: Aossci is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Drone, UAV, Public Safety, Energy Inspection, and China.
random_paper: 4
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 5
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
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aossci Domain Security
  slug: aossci-domain-security
  summary_line: TLSv1.3
slug: aossci
tags:
- Drone
- UAV
- Public Safety
- Energy Inspection
- China
website: https://www.aossci.com
---
