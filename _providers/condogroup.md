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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/condogroup/refs/heads/main/hosts/condogroup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/condogroup-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/condogroup/refs/heads/main/security/condogroup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/condogroup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://condegroup.com
coverage:
  checked: '2026-10-10'
  detail: Conde Group provides staffing services and does not offer a public developer program or API.
  evidence:
  - status: 200
    url: https://condegroup.com
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: 'Condogroup is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling. No public website or detailed information is currently available for Condogroup, and attempts to locate an official domain have been unsuccessful. The entry exists primarily to enable future enrichment as more data becomes available.'
layout: provider
modified: '2026-10-10'
name: Condogroup
nav: Providers
network: true
overview: Condogroup is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Services, Finance, and Data.
random_paper: 10
score:
  band: minimal
  composite: 3.1
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
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Condogroup Domain Security
  slug: condogroup-domain-security
  summary_line: TLSv1.3 · DMARC
slug: condogroup
tags:
- Company
- Technology
- Services
- Finance
- Data
website: https://condegroup.com
---
