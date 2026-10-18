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
  href: https://raw.githubusercontent.com/api-evangelist/clinbrain/refs/heads/main/hosts/clinbrain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clinbrain-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clinbrain/refs/heads/main/vendors/clinbrain-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clinbrain-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clinbrain/refs/heads/main/security/clinbrain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clinbrain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/clinbrain
created: '2026-10-08'
description: Clinbrain is a company identified in the API Evangelist secondary‑market harvest. After searching major public sources (Crunchbase, PitchBook, DuckDuckGo) no official corporate website could be located, indicating the company may not maintain a public web presence or it is not indexed. The entry remains a stub for further profiling as more information becomes available.
layout: provider
modified: '2026-10-08'
name: Clinbrain
nav: Providers
network: true
overview: Clinbrain is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Data Analytics, and Neurology.
random_paper: 0
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clinbrain Domain Security
  slug: clinbrain-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clinbrain
tags:
- Company
- Healthcare
- Artificial Intelligence
- Data Analytics
- Neurology
website: https://equityzen.com/company/clinbrain
---
