---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/hycom-core/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/hycom-core/hosts/hycom-core-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hycom-core-hosts.yml
- group: auth
  href: https://artifacts.apis.io/hycom-core/security/hycom-core-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hycom-core-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hycomcore.com
coverage:
  checked: '2026-10-29'
  detail: The provider's website does not expose any machine‑readable API specification or developer documentation.
  evidence:
  - status: 404
    url: https://www.hycomcore.com/openapi.json
  - status: 404
    url: https://www.hycomcore.com/openapi.yaml
  - status: 0
    url: https://api.hycomcore.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: HyCom Core builds cutting‑edge electro‑optic waveguide modulators that enable multi‑wavelength modulation in ultra‑compact form factors. Their technology consumes 30× less energy and transfers data up to 10× faster, positioning them as a key enabler for high‑performance AI clusters and modern data‑center infrastructure. From a small thought to a giant leap in data‑center technology, HyCom Core delivers innovative photonic solutions for the AI era.
image: https://www.hycomcore.com/wp-content/uploads/2022/11/HyComCore-Logo-Glow.jpg
layout: provider
modified: '2026-10-29'
name: HyCom Core
nav: Providers
network: true
overview: HyCom Core is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Data Center, Photonics, and Modulators.
random_paper: 6
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hycom Core Domain Security
  slug: hycom-core-domain-security
  summary_line: TLSv1.3 · HSTS
slug: hycom-core
tags:
- Company
- AI
- Data Center
- Photonics
- Modulators
- Technology
website: https://hycomcore.com
---
