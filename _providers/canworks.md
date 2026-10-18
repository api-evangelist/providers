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
- description: Canworks provides a digital printing API for custom aluminum cans, allowing artwork upload and order management.
  name: Canworks API
  slug: canworks-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canworks/refs/heads/main/hosts/canworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canworks-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canworks/refs/heads/main/vendors/canworks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canworks-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.canworksprinting.com/terms-and-conditions
- group: company
  title: ''
  type: Blog
  url: https://www.canworksprinting.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canworks/refs/heads/main/security/canworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.canworksprinting.com/
coverage:
  checked: '2026-10-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's API host.
  evidence:
  - status: 0
    url: https://api.canworksprinting.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Canworks is a digital printing company specializing in direct‑to‑can aluminum printing for beverage brands. Based in the United States, it offers low‑minimum runs, fast turn‑around, and sustainable, sleeve‑free packaging solutions. The service includes artwork upload, prototyping, and full‑production printing, serving over 700 brands with high‑quality custom cans.
image: https://cdn.prod.website-files.com/69445227674ace7788bad5e6/6977d5b3547db0d38ea380d4_Canworks%20Open%20Graph.webp
layout: provider
modified: '2026-10-06'
name: Canworks
nav: Providers
network: true
overview: 'Canworks is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Printing, Aluminum Cans, Beverage Packaging, Direct-to-Can, and Low Minimums.


  Canworks'' developer surface includes engineering blog and 5 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 6
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
  name: Canworks Domain Security
  slug: canworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: canworks
tags:
- Digital Printing
- Aluminum Cans
- Beverage Packaging
- Direct-to-Can
- Low Minimums
- Sustainability
website: https://www.canworksprinting.com/
---
