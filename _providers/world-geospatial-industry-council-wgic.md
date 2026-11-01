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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/world-geospatial-industry-council-wgic/llms/world-geospatial-industry-council-wgic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/world-geospatial-industry-council-wgic-llms.txt
- group: other
  href: https://artifacts.apis.io/world-geospatial-industry-council-wgic/hosts/world-geospatial-industry-council-wgic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/world-geospatial-industry-council-wgic-hosts.yml
- group: other
  href: https://artifacts.apis.io/world-geospatial-industry-council-wgic/vendors/world-geospatial-industry-council-wgic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/world-geospatial-industry-council-wgic-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://wgicouncil.org/media/
- group: auth
  href: https://artifacts.apis.io/world-geospatial-industry-council-wgic/security/world-geospatial-industry-council-wgic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/world-geospatial-industry-council-wgic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wgicouncil.org/
coverage:
  checked: '2026-10-23'
  detail: Home page renders via JavaScript, no machine-readable API spec found.
  evidence:
  - status: 200
    url: https://wgicouncil.org/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: The World Geospatial Industry Council (WGIC) is a registered not‑for‑profit trade association that represents commercial geospatial companies across the entire value chain. It provides a collaborative forum for members, advocates global policy matters relevant to the geospatial sector, and creates business opportunities for the industry.
image: https://wgicouncil.org/wp-content/uploads/2023/09/WGIC_FullLockup_Digital_Inverted.png
layout: provider
modified: '2026-10-23'
name: World Geospatial Industry Council (WGIC)
nav: Providers
network: true
overview: World Geospatial Industry Council (WGIC) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Geospatial, Trade Association, Industry Council, and Membership.
random_paper: 6
score:
  band: minimal
  composite: 2.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 41.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: World Geospatial Industry Council Wgic Domain Security
  slug: world-geospatial-industry-council-wgic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: world-geospatial-industry-council-wgic
tags:
- Geospatial
- Trade Association
- Industry Council
- Membership
website: https://wgicouncil.org/
---
