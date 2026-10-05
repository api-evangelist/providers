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
  href: https://raw.githubusercontent.com/api-evangelist/biplus/refs/heads/main/hosts/biplus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biplus-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biplus/refs/heads/main/vendors/biplus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biplus-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://biplus.com.vn/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biplus/refs/heads/main/security/biplus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biplus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biplus.com.vn
coverage:
  checked: '2026-09-28'
  detail: OpenAPI endpoints returned HTML pages instead of machine‑readable specs.
  evidence:
  - status: 200
    url: https://biplus.com.vn/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Biplus is a Vietnam‑based software solutions and IT outsourcing company offering custom software development, Atlassian partnership, AI‑tailored solutions, and consulting services across telecommunications, finance, e‑commerce, and fintech sectors. It provides enterprise‑grade development, personnel outsourcing, and SaaS integration, positioning itself as a trusted partner for digital transformation.
image: https://biplus.com.vn/assets/image/meta-image.png
layout: provider
modified: '2026-09-28'
name: Biplus
nav: Providers
network: true
overview: 'Biplus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software, IT Outsourcing, Vietnam, and Artificial Intelligence.


  Biplus'' developer surface includes engineering blog and 4 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 6
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
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - vietnam
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biplus Domain Security
  slug: biplus-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: biplus
tags:
- Company
- Software
- IT Outsourcing
- Vietnam
- Artificial Intelligence
website: https://biplus.com.vn
---
