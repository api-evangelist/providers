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
api_count: 1
apis:
- description: Brightspec provides a developer API for accessing spectroscopy data and instrument control. Documentation is limited to marketing pages without a machine‑readable spec.
  name: Brightspec API
  slug: brightspec-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brightspec/refs/heads/main/hosts/brightspec-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brightspec-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brightspec/refs/heads/main/vendors/brightspec-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brightspec-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brightspec.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://brightspec.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brightspec/refs/heads/main/security/brightspec-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brightspec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brightspec.com
coverage:
  checked: '2026-10-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract is published; the site only provides marketing pages.
  evidence:
  - status: 200
    url: https://brightspec.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Brightspec provides advanced molecular rotational resonance (MRR) spectroscopy instruments, consumables, and software solutions for analytical chemistry. Their platform offers high‑resolution spectral analysis for pharmaceuticals, food & beverage, cosmetics, and chemical industries, enabling precise identification, quantitation, and chiral analysis of compounds. Brightspec’s offerings include hardware such as SpectraMRR, IsoMRR, NanoMRR, and software like BrightHub and Edgar, supporting comprehensive analytical workflows.
image: https://brightspec.com/hubfs/Logos/BrightSpec%20Logo%20Social.png
layout: provider
modified: '2026-10-06'
name: Brightspec
nav: Providers
network: true
overview: 'Brightspec is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Spectroscopy, Molecular Analysis, Pharmaceuticals, Chemicals, and Consumer Goods.


  Brightspec''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
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
  name: Brightspec Domain Security
  slug: brightspec-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brightspec
tags:
- Spectroscopy
- Molecular Analysis
- Pharmaceuticals
- Chemicals
- Consumer Goods
- Instruments
- Software
- Consumables
website: https://brightspec.com
---
