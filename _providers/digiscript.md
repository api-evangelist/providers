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
api_count: 1
apis:
- description: Provides digital reality capture services and data access for 3D scanning, aerial surveys, and virtual tours.
  name: DigiScript API
  slug: digiscript-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/digiscript/llms/digiscript-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/digiscript-llms.txt
- group: other
  href: https://artifacts.apis.io/digiscript/hosts/digiscript-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digiscript-hosts.yml
- group: other
  href: https://artifacts.apis.io/digiscript/vendors/digiscript-vendors.yml
  title: ''
  type: Vendors
  url: vendors/digiscript-vendors.yml
- group: auth
  href: https://artifacts.apis.io/digiscript/security/digiscript-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digiscript-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.digiscriptinc.com/
coverage:
  checked: '2026-10-23'
  detail: Homepage loads a JavaScript shell with no readable API documentation.
  evidence:
  - status: 200
    url: https://www.digiscriptinc.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: DigiScript Philippines provides digital reality capture solutions, offering services such as 3D laser scanning, aerial surveys, ground‑penetrating radar, and virtual tours. With over two decades of experience, they serve industrial, commercial, residential, and heritage sectors, delivering accurate as‑built drawings and digital twins to help clients plan, manage, and build projects efficiently.
layout: provider
modified: '2026-10-23'
name: DigiScript
nav: Providers
network: true
overview: DigiScript is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Reality Capture, 3D Scanning, AerialSurvey, and Construction.
random_paper: 18
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
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
  name: Digiscript Domain Security
  slug: digiscript-domain-security
  summary_line: TLSv1.3 · HSTS
slug: digiscript
tags:
- Company
- Reality Capture
- 3D Scanning
- AerialSurvey
- Construction
website: https://www.digiscriptinc.com/
---
