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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/differentiated-therapeutics/llms/differentiated-therapeutics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/differentiated-therapeutics-llms.txt
- group: other
  href: https://artifacts.apis.io/differentiated-therapeutics/hosts/differentiated-therapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/differentiated-therapeutics-hosts.yml
- group: other
  href: https://artifacts.apis.io/differentiated-therapeutics/vendors/differentiated-therapeutics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/differentiated-therapeutics-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.dxtherapeutics.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dx-tx
- group: company
  title: ''
  type: Blog
  url: https://www.dxtherapeutics.com/blog
- group: auth
  href: https://artifacts.apis.io/differentiated-therapeutics/security/differentiated-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/differentiated-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dxtherapeutics.com
coverage:
  checked: '2026-10-23'
  detail: No OpenAPI or other machine‑readable contract found; attempts at /openapi.json on API and website hosts returned 000 and 403.
  evidence:
  - status: 0
    url: https://api.dxtherapeutics.com/openapi.json
  - status: 403
    url: https://www.dxtherapeutics.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: Differentiated Therapeutics (dx/tx) is a protein degradation company focused on discovering and developing transformative therapies using targeted protein degradation. It operates an end‑to‑end discovery engine combining biophysics, chemoproteomics, molecular simulation, AI and automation to map and design novel protein degraders, aiming to eliminate genetically defined disease drivers.
image: https://static.wixstatic.com/media/83016c_732ad19aaa434fe1bd635140c4d41046%7Emv2.png/v1/fit/w_2500,h_1330,al_c/83016c_732ad19aaa434fe1bd635140c4d41046%7Emv2.png
layout: provider
modified: '2026-10-23'
name: Differentiated Therapeutics
nav: Providers
network: true
overview: 'Differentiated Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Therapeutics, Protein Degradation, Drug Discovery, Artificial Intelligence, and Biophysics.


  Differentiated Therapeutics'' developer surface includes engineering blog and 7 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
  name: Differentiated Therapeutics Domain Security
  slug: differentiated-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: differentiated-therapeutics
tags:
- Therapeutics
- Protein Degradation
- Drug Discovery
- Artificial Intelligence
- Biophysics
- chemoproteomics
- Molecular Simulation
website: https://www.dxtherapeutics.com
---
