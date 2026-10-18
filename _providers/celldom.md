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
  href: https://raw.githubusercontent.com/api-evangelist/celldom/refs/heads/main/hosts/celldom-hosts.yml
  title: ''
  type: Hosts
  url: hosts/celldom-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/celldom/refs/heads/main/vendors/celldom-vendors.yml
  title: ''
  type: Vendors
  url: vendors/celldom-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.celldom.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.celldom.com/leadership
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Celldom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/celldom/refs/heads/main/security/celldom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/celldom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.celldom.com
coverage:
  checked: '2026-10-07'
  detail: The homepage renders only a JavaScript shell and no machine‑readable API documentation was found.
  evidence:
  - status: 200
    url: https://www.celldom.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Celldom provides a high‑throughput single‑cell biology platform that captures cellular morphology, phenotypes, activity, and molecular profiles in real‑time. The platform enables drug screening, T‑cell potency assays, and detailed cell‑cell interaction studies, delivering multi‑parameter data from thousands of cells per plate. It serves researchers and biotech companies seeking scalable, automated single‑cell analysis for discovery and development.
image: http://static1.squarespace.com/static/645c24ad9669f64e4b2502a2/t/645c27331a4d403cec638810/1683760947516/CLDM_LOGO_FULL_PNG_1.png?format=1500w
layout: provider
modified: '2026-10-07'
name: Celldom
nav: Providers
network: true
overview: Celldom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Single Cell, Platform, and Drug Discovery.
random_paper: 10
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 5
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
    discoverability: 50.0
    operational_transparency: 5.3
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
  name: Celldom Domain Security
  slug: celldom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: celldom
tags:
- Company
- Biotechnology
- Single Cell
- Platform
- Drug Discovery
website: https://www.celldom.com
---
