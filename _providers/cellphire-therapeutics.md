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
  href: https://raw.githubusercontent.com/api-evangelist/cellphire-therapeutics/refs/heads/main/hosts/cellphire-therapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cellphire-therapeutics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cellphire-therapeutics/refs/heads/main/vendors/cellphire-therapeutics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cellphire-therapeutics-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cellphire.com/terms-of-use
- group: company
  title: ''
  type: Newsroom
  url: https://www.cellphire.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cellphire-therapeutics/refs/heads/main/security/cellphire-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cellphire-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cellphire.com
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract discovered on api.cellphire.com or any docs host.
  evidence:
  - status: 0
    url: https://api.cellphire.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: CellPhire Therapeutics develops platelet‑based therapeutics to treat acute hemorrhage and promote vascular repair. Their platform includes CLPH‑511, a frozen activated platelet product, and the FPH platform targeting hemostasis and vascular permeability. The company aims to save lives in trauma, surgery, and critical care by providing innovative biologics that address platelet availability challenges.
layout: provider
modified: '2026-10-07'
name: CellPhire Therapeutics
nav: Providers
network: true
overview: CellPhire Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Platelet, and Hemostasis.
random_paper: 6
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cellphire Therapeutics Domain Security
  slug: cellphire-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cellphire-therapeutics
tags:
- Company
- Biotechnology
- Therapeutics
- Platelet
- Hemostasis
website: https://www.cellphire.com
---
