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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bunchtechnology/refs/heads/main/llms/bunchtechnology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bunchtechnology-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bunchtechnology/refs/heads/main/well-known/bunchtechnology-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bunchtechnology-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bunchtechnology/refs/heads/main/well-known/bunchtechnology-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bunchtechnology-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bunchtechnology/refs/heads/main/hosts/bunchtechnology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bunchtechnology-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bunchtechnology/refs/heads/main/vendors/bunchtechnology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bunchtechnology-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.iot.bunchtech.io/
- group: company
  title: ''
  type: Blog
  url: https://www.bunchtech.io/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bunchtechnology/refs/heads/main/security/bunchtechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bunchtechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bunchtech.io
coverage:
  checked: '2026-10-06'
  detail: No developer program or API documentation is publicly available.
  evidence:
  - status: 200
    url: https://www.bunchtech.io
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Bunchtechnology (Bunch Tech) provides enterprise IoT solutions for intelligent real‑estate and smart building management. It designs, procures, and deploys multi‑sensor ecosystems that reduce operational costs, improve occupant experiences, and enable data‑driven building automation across energy, air quality, occupancy, leak detection, and more. The company serves large‑scale commercial properties, offering plug‑and‑play device access, cloud integration, and consulting to simplify IoT deployments and accelerate digital transformation.
layout: provider
modified: '2026-10-06'
name: Bunchtechnology
nav: Providers
network: true
overview: 'Bunchtechnology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Smart Buildings, Enterprise Solutions, and Real Estate.


  Bunchtechnology''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 5
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
    discoverability: 51.8
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bunchtechnology Domain Security
  slug: bunchtechnology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bunchtechnology
tags:
- Company
- IoT
- Smart Buildings
- Enterprise Solutions
- Real Estate
website: https://www.bunchtech.io
---
