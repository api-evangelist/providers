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
- group: agent
  href: https://artifacts.apis.io/darkhiveinc/llms/darkhiveinc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/darkhiveinc-llms.txt
- group: other
  href: https://artifacts.apis.io/darkhiveinc/hosts/darkhiveinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/darkhiveinc-hosts.yml
- group: other
  href: https://artifacts.apis.io/darkhiveinc/vendors/darkhiveinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/darkhiveinc-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.darkhive.com/news
- group: company
  title: ''
  type: Blog
  url: https://www.darkhive.com/blog
- group: auth
  href: https://artifacts.apis.io/darkhiveinc/security/darkhiveinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/darkhiveinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.darkhive.com
coverage:
  checked: '2026-10-22'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the provider's API host.
  evidence:
  - status: 0
    url: https://api.darkhive.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Darkhiveinc (Darkhive Inc.) is a defense‑technology startup that designs and builds open‑architecture uncrewed aircraft systems, tactical drones, and integrated software platforms for military and public‑safety customers. The company emphasizes scalable hardware, secure software delivery, and rapid fielding to support modern battlefields, delivering end‑to‑end solutions from hardware to cloud services.
layout: provider
modified: '2026-10-22'
name: Darkhiveinc
nav: Providers
network: true
overview: 'Darkhiveinc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Defense, Aerospace, Robotics, Unmanned Systems, and Software.


  Darkhiveinc''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
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
  name: Darkhiveinc Domain Security
  slug: darkhiveinc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: darkhiveinc
tags:
- Defense
- Aerospace
- Robotics
- Unmanned Systems
- Software
website: https://www.darkhive.com
---
