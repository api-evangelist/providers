---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aspyriantherapeutics/refs/heads/main/well-known/aspyriantherapeutics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aspyriantherapeutics-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aspyriantherapeutics/refs/heads/main/hosts/aspyriantherapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aspyriantherapeutics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aspyriantherapeutics/refs/heads/main/vendors/aspyriantherapeutics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aspyriantherapeutics-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rakuten-med.com/us/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://rakuten-med.com/us/news
- group: other
  title: ''
  type: Leadership
  url: https://rakuten-med.com/us/about/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aspyriantherapeutics/refs/heads/main/security/aspyriantherapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aspyriantherapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rakuten-med.com
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the provider's API hosts.
  evidence:
  - status: dns_error
    url: https://api.rakuten-med.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Aspyriantherapeutics, now operating as Rakuten Medical, is a privately funded clinical‑stage biotechnology company based in San Diego, United States. Founded in 2010, it develops precision, cell‑targeting photoimmunotherapy based on its proprietary Alluminox® platform to treat solid tumours, particularly head and neck cancers. The company has raised significant funding and is advancing its pipeline through clinical trials and expanded access programs.
image: https://rakuten-med.com/us/wp-content/uploads/sites/6/2021/02/RakutenMedical_KV.png
layout: provider
modified: '2026-09-26'
name: Aspyriantherapeutics
nav: Providers
network: true
overview: Aspyriantherapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Photoimmunotherapy, Clinical Stage, and Oncology.
random_paper: 12
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aspyriantherapeutics Domain Security
  slug: aspyriantherapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aspyriantherapeutics
tags:
- Company
- Biotechnology
- Photoimmunotherapy
- Clinical Stage
- Oncology
website: https://rakuten-med.com
---
