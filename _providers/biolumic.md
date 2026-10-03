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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biolumic/refs/heads/main/hosts/biolumic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biolumic-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biolumic/refs/heads/main/vendors/biolumic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biolumic-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.biolumic.com/headlines/category/Press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biolumic/refs/heads/main/security/biolumic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biolumic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.biolumic.com
coverage:
  checked: '2026-09-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.biolumic.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: BioLumic develops UV light technology to improve plant growth, sustainability and crop yields. Leveraging photobiology, the company creates innovative lighting solutions for agriculture, enhancing photosynthesis efficiency and reducing resource use. Based in New Zealand, BioLumic serves global agritech markets with science‑driven products and services aimed at sustainable food production.
image: http://static1.squarespace.com/static/5b7b502dfcf7fd913d0cc338/t/5cf09ada6451800001206edd/1782417760389/Screen+Shot+2019-05-31+at+3.07.49+pm.png?format=1500w
layout: provider
modified: '2026-09-28'
name: Biolumic
nav: Providers
network: true
overview: Biolumic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Photobiology, SustainableTech, New Zealand, and UVLighting.
random_paper: 16
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biolumic Domain Security
  slug: biolumic-domain-security
  summary_line: TLSv1.3 · HSTS
slug: biolumic
tags:
- Agriculture
- Photobiology
- SustainableTech
- New Zealand
- UVLighting
- Company
website: https://www.biolumic.com
---
