---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/mesoblast/well-known/mesoblast-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mesoblast-well-known.yml
- group: other
  href: https://artifacts.apis.io/mesoblast/hosts/mesoblast-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mesoblast-hosts.yml
- group: other
  href: https://artifacts.apis.io/mesoblast/vendors/mesoblast-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mesoblast-vendors.yml
- group: auth
  href: https://artifacts.apis.io/mesoblast/security/mesoblast-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mesoblast-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mesoblast.com/
created: '2026-10-21'
description: Mesoblast Limited is an Australian regenerative medicine company headquartered in Melbourne, founded in 2004 by Silviu Itescu and listed on the ASX (MSB) and Nasdaq (MESO). It develops allogeneic cellular medicines based on mesenchymal lineage cells, including remestemcel-L for steroid-refractory acute graft versus host disease and rexlemestrocel-L for chronic heart failure and chronic low back pain. Its website answered our crawler with a bot challenge, and we found no public developer API or documentation.
layout: provider
modified: '2026-10-22'
name: Mesoblast
nav: Providers
network: true
overview: Mesoblast is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Regenerative Medicine, Cell Therapy, and Pharmaceuticals.
random_paper: 10
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 4.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mesoblast Domain Security
  slug: mesoblast-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mesoblast
tags:
- Company
- Biotechnology
- Regenerative Medicine
- Cell Therapy
- Pharmaceuticals
- Australia
website: https://mesoblast.com/
---
