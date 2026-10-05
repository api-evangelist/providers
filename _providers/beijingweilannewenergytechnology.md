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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beijingweilannewenergytechnology/refs/heads/main/hosts/beijingweilannewenergytechnology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beijingweilannewenergytechnology-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beijingweilannewenergytechnology/refs/heads/main/vendors/beijingweilannewenergytechnology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beijingweilannewenergytechnology-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beijingweilannewenergytechnology/refs/heads/main/security/beijingweilannewenergytechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beijingweilannewenergytechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.solidstatelion.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/beijingweilannewenergytechnology
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Beijing Weilan New Energy Technology Co., Ltd., operating under the trade name WeLion, is a Chinese private company founded in August 2016. It specializes in the development, production, and commercialization of semi‑solid and solid‑state lithium‑ion batteries for electric vehicles and energy storage. The firm is a spin‑off from the Institute of Physics, Chinese Academy of Sciences, and is headquartered in Fangshan District, Beijing. It has partnerships with Nio and has received significant investment from Geely, Huawei, and Xiaomi.
layout: provider
modified: '2026-09-27'
name: Beijingweilannewenergytechnology
nav: Providers
network: true
overview: Beijingweilannewenergytechnology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Battery, Energy, SolidState, and China.
random_paper: 0
score:
  band: minimal
  composite: 3.2
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beijingweilannewenergytechnology Domain Security
  slug: beijingweilannewenergytechnology-domain-security
  summary_line: TLSv1.3 · HSTS
slug: beijingweilannewenergytechnology
tags:
- Company
- Battery
- Energy
- SolidState
- China
website: https://www.solidstatelion.com
---
