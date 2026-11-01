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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/arcboats-com/hosts/arcboats-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcboats-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/arcboats-com/vendors/arcboats-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcboats-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/arcboats-com/security/arcboats-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcboats-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arcboats.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://arcboats.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Arc designs and builds all‑electric boats in the United States. Its product line includes the Arc Sport wakesport boat for performance recreation, the Arc Coast center‑console boat for cruising, and the limited‑edition Arc One sport boat. Arc also offers electric power solutions for commercial water operations.
image: https://arcboats.com/images/Arc_Sport_Floating.jpg
layout: provider
modified: '2026-10-25'
name: Arc
nav: Providers
network: true
overview: Arc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Electric Boats, Recreation, and Commercial.
random_paper: 11
score:
  band: minimal
  composite: 2.6
  coverage:
    artifact_dirs: 5
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
    discoverability: 39.3
    operational_transparency: 0.0
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
  name: Arcboats Com Domain Security
  slug: arcboats-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arcboats-com
tags:
- Electric Boats
- Recreation
- Commercial
website: https://arcboats.com
---
