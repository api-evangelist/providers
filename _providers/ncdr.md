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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/ncdr/hosts/ncdr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ncdr-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ncdr/security/ncdr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ncdr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ncdr.nat.gov.tw/
coverage:
  checked: '2026-10-28'
  detail: Provider's site returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 200
    url: https://ncdr.nat.gov.tw/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: The National Center for Disaster Reduction (NCDR) in Taiwan is a government-affiliated organization that focuses on research, technology development, and coordination for disaster prevention, mitigation, response, and recovery. It provides data, tools, and services to support emergency management, public safety, and resilience across the nation, collaborating with agencies, academia, and industry to improve disaster preparedness and reduce risk.
layout: provider
modified: '2026-10-28'
name: NCDR (Taiwan)
nav: Providers
network: true
overview: NCDR (Taiwan) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Disaster Management, Taiwan, Public Safety, and Data Services.
random_paper: 15
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ncdr Domain Security
  slug: ncdr-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: ncdr
tags:
- Government
- Disaster Management
- Taiwan
- Public Safety
- Data Services
website: https://ncdr.nat.gov.tw/
---
