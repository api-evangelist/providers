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
  href: https://raw.githubusercontent.com/api-evangelist/centurykangtai/refs/heads/main/hosts/centurykangtai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centurykangtai-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centurykangtai/refs/heads/main/security/centurykangtai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centurykangtai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tjsjkt.com/en/index.aspx
coverage:
  checked: '2026-10-07'
  detail: No machine‑readable API specification was discovered despite the company having a public website.
  evidence:
  - status: 200
    url: https://www.tjsjkt.com/en/index.aspx
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Centurykangtai, also known as Tianjin Century Healthcare Biomedical Engineering Co., Ltd., is a Class‑III high‑end medical device manufacturer in China specializing in ophthalmic implants, intraocular lenses, collagen biomaterials, and related diagnostic and treatment solutions. The company integrates research, development, production, and sales, operating a GMP‑certified factory of 20,000 m² and employing over 70 top ophthalmic R&D experts, including 10 PhDs. It holds more than 80 patents and collaborates with academic institutions, focusing on innovative eye‑care technologies and biomaterials.
layout: provider
modified: '2026-10-07'
name: Centurykangtai
nav: Providers
network: true
overview: Centurykangtai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Intraocular Lenses, Optometry, Collagen Products, and Biomedical Engineering.
random_paper: 17
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
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
  name: Centurykangtai Domain Security
  slug: centurykangtai-domain-security
  summary_line: TLSv1.3
slug: centurykangtai
tags:
- Intraocular Lenses
- Optometry
- Collagen Products
- Biomedical Engineering
website: https://www.tjsjkt.com/en/index.aspx
---
