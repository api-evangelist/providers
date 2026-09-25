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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anghami/refs/heads/main/hosts/anghami-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anghami-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anghami/refs/heads/main/vendors/anghami-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anghami-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/anghami/refs/heads/main/packages/anghami-packages.yml
  title: ''
  type: SDKs
  url: packages/anghami-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/anghami/refs/heads/main/packages/anghami-packages.yml
  title: ''
  type: Packages
  url: packages/anghami-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.anghami.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anghami
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anghami/refs/heads/main/security/anghami-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anghami-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.anghami.com/
- group: operate
  title: ''
  type: Support
  url: https://support.anghami.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anghami.com/legal
coverage:
  checked: 2026-09-23
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract files were found at the API host.
  evidence:
  - status: 204
    url: https://api.anghami.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-23'
description: Anghami is a leading music streaming platform in the Middle East and North Africa, offering a vast library of songs, podcasts, and curated playlists. Users can enjoy personalized recommendations, high‑quality audio, and offline listening across multiple devices. The service provides both free ad‑supported and premium subscription tiers, catering to a diverse audience of music lovers and creators.
layout: provider
modified: '2026-09-23'
name: Anghami
nav: Providers
network: true
overview: 'Anghami is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Streaming, Middle East, North-Africa, and Entertainment.


  Anghami''s developer surface includes support and 9 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 46.3
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anghami Domain Security
  slug: anghami-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anghami
tags:
- Music
- Streaming
- Middle East
- North-Africa
- Entertainment
website: https://www.anghami.com/
---
