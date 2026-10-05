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
  href: https://raw.githubusercontent.com/api-evangelist/archsystems/refs/heads/main/hosts/archsystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/archsystems-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/archsystems/refs/heads/main/security/archsystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/archsystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://archsystems.com
coverage:
  checked: 2026-09-26
  detail: All attempted OpenAPI spec URLs on archsystems.com, catalog.archsystems.com, and api.archsystems.com returned 404.
  evidence:
  - status: 404
    url: https://archsystems.com/openapi.json
  - status: 404
    url: https://catalog.archsystems.com/openapi.json
  - status: 404
    url: https://api.archsystems.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Archsystems, also known as Architectural Systems, Inc., is a leading global provider of innovative, distinctive, and sustainable interior finishes. The company collaborates with architects, designers, and decision‑makers across market segments, offering material expertise, project management, material take‑offs, on‑site support, and a commitment to service. Their product lines include wood panels, porcelains, surfacing materials, and luxury vinyls, showcased through an online catalog and extensive resources.
image: https://archsystems.com/wp-content/uploads/2025/04/ASI-WoodPanels-collage.png
layout: provider
modified: '2026-09-25'
name: Archsystems
nav: Providers
network: true
overview: Archsystems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Architecture, Interior Design, Materials, Manufacturing, and Sustainable.
random_paper: 18
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 4
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
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Archsystems Domain Security
  slug: archsystems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: archsystems
tags:
- Architecture
- Interior Design
- Materials
- Manufacturing
- Sustainable
- Company
website: https://archsystems.com
---
