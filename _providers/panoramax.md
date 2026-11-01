---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: This STAC API references data from several Panoramax instances
  name: Panoramax API
  slug: panoramax-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/panoramax/conformance/panoramax-conformance.yml
  title: ''
  type: Conformance
  url: conformance/panoramax-conformance.yml
- group: other
  href: https://artifacts.apis.io/panoramax/hosts/panoramax-hosts.yml
  title: ''
  type: Hosts
  url: hosts/panoramax-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.panoramax.fr/backend/dev/releases/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.panoramax.fr/web-viewer/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.panoramax.fr/web-viewer
- group: auth
  href: https://artifacts.apis.io/panoramax/security/panoramax-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/panoramax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://panoramax.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://panoramax.fr/docs
- group: company
  title: ''
  type: Blog
  url: https://panoramax.fr/blog
created: '2026-10-28'
description: Panoramax is a French open‑source initiative that federates local authorities, OpenStreetMap contributors, and the French National Geographic Institute (IGN) to create immersive, geocommunicated base views of territories. It provides tools and APIs for photo‑mapping, enabling communities to capture, share, and integrate high‑resolution panoramic imagery into geographic information systems, supporting open data and collaborative mapping projects.
layout: provider
modified: '2026-10-28'
name: Panoramax
nav: Providers
network: true
overview: 'Panoramax is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OpenData, Mapping, Photography, and GIS.


  Panoramax''s developer surface includes changelog, API reference, getting-started guide, documentation, engineering blog, and 4 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Panoramax Domain Security
  slug: panoramax-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: panoramax
tags:
- Company
- OpenData
- Mapping
- Photography
- GIS
website: https://panoramax.fr/
---
