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
- description: API information not publicly available.
  name: Curi Bio API
  slug: curi-bio-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curi-bio/refs/heads/main/hosts/curi-bio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curi-bio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curi-bio/refs/heads/main/vendors/curi-bio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/curi-bio-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/curi-bio/refs/heads/main/packages/curi-bio-packages.yml
  title: ''
  type: SDKs
  url: packages/curi-bio-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/curi-bio/refs/heads/main/packages/curi-bio-packages.yml
  title: ''
  type: Packages
  url: packages/curi-bio-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.curibio.com/terms-privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.curibio.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CuriBio
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curi-bio/refs/heads/main/security/curi-bio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curi-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.curibio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.curibio.com/blog
- group: company
  title: ''
  type: About
  url: https://www.curibio.com/company
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on discovered hosts.
  evidence:
  - status: 404
    url: https://api.curibio.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Curi Bio develops human-relevant platforms integrating human cells, systems, and data to accelerate the discovery of new medicines. Their iPSC-based products enable scientists to build mature predictive tissue models for cardiac, skeletal muscle, and neuromuscular applications, supporting drug safety, efficacy, and potency testing.
image: http://static1.squarespace.com/static/5ea9dcad38347f7b8405d2f9/t/5eb9be09784e2246468d3e2c/1589231493964/Curi-Bio-Logo_full-color-for-dark-bgs_with-space.jpg?format=1500w
layout: provider
modified: '2026-10-12'
name: Curi Bio
nav: Providers
network: true
overview: 'Curi Bio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Drug Discovery, Human Cell Models, Platform, and Seattle.


  Curi Bio''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 58.9
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
  name: Curi Bio Domain Security
  slug: curi-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: curi-bio
tags:
- Biotechnology
- Drug Discovery
- Human Cell Models
- Platform
- Seattle
website: https://www.curibio.com/
---
