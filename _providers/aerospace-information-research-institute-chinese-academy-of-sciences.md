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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/aerospace-information-research-institute-chinese-academy-of-sciences/hosts/aerospace-information-research-institute-chinese-academy-of-sciences-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aerospace-information-research-institute-chinese-academy-of-sciences-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aerospace-information-research-institute-chinese-academy-of-sciences/security/aerospace-information-research-institute-chinese-academy-of-sciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aerospace-information-research-institute-chinese-academy-of-sciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.radi.ac.cn
coverage:
  checked: '2026-10-26'
  detail: The institute provides research services and does not expose a software API.
  evidence:
  - status: unreachable
    url: http://www.radi.ac.cn
  reason: not-a-software-company
  state: none
created: '2026-10-26'
description: The Aerospace Information Research Institute (AIRI) of the Chinese Academy of Sciences conducts advanced research and development in aerospace information technologies, including satellite data processing, remote sensing, and aerospace communications. It collaborates with national space programs and academic institutions, providing scientific insights, data services, and technical support for aerospace missions and related industries.
layout: provider
modified: '2026-10-26'
name: Aerospace Information Research Institute, Chinese Academy of Sciences
nav: Providers
network: true
overview: Aerospace Information Research Institute, Chinese Academy of Sciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Research, Satellite, and Data.
random_paper: 23
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
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aerospace Information Research Institute Chinese Academy Of Sciences Domain Security
  slug: aerospace-information-research-institute-chinese-academy-of-sciences-domain-security
  summary_line: no transport/DNS hardening detected
slug: aerospace-information-research-institute-chinese-academy-of-sciences
tags:
- Company
- Aerospace
- Research
- Satellite
- Data
- China
website: http://www.radi.ac.cn
---
