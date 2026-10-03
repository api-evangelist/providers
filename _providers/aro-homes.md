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
  href: https://raw.githubusercontent.com/api-evangelist/aro-homes/refs/heads/main/hosts/aro-homes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aro-homes-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://arohomes.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aro-homes/refs/heads/main/security/aro-homes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aro-homes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arohomes.com
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found at standard endpoints on api.arohomes.com.
  evidence:
  - status: 0
    url: https://api.arohomes.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Aro Homes is a Mexican construction and remodeling company specializing in new builds, renovations, and detailed architectural projects. Their portfolio showcases residential and commercial works, emphasizing quality craftsmanship and client-focused design. The company provides services from project conception through completion, aiming to transform client visions into reality with integrated design and construction solutions.
image: https://wp-uphome.astroon.pro/wp-content/uploads/2020/02/todd-quackenbush-JJB_K8aCPU4-unsplash-2048x1343-1-2.jpg
layout: provider
modified: '2026-09-26'
name: Aro Homes
nav: Providers
network: true
overview: 'Aro Homes is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Remodeling, Real Estate, and Mexico.


  Aro Homes'' developer surface includes engineering blog and 3 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 3.8
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
    developer_ergonomics: 2.4
    discoverability: 48.2
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
  name: Aro Homes Domain Security
  slug: aro-homes-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aro-homes
tags:
- Company
- Construction
- Remodeling
- Real Estate
- Mexico
website: https://arohomes.com
---
