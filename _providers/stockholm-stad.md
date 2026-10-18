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
  href: https://raw.githubusercontent.com/api-evangelist/stockholm-stad/refs/heads/main/hosts/stockholm-stad-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stockholm-stad-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stockholm-stad/refs/heads/main/security/stockholm-stad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stockholm-stad-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stockholm.se/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://stockholm.se/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Stockholm stad is the municipal government of Sweden’s capital city, providing a wide range of public services, open data portals, and digital tools for residents and businesses. The city’s website offers information on education, transportation, urban planning, social services, cultural events, and e‑services such as permits, registrations, and contact centers. This profile aims to capture the APIs that power these digital services and support developers in building applications that interact with Stockholm’s public sector data.
image: https://start.stockholm/optimized/large/globalassets/stockholms-stadshus-vinter-riddarfjarden.jpg
layout: provider
modified: '2026-10-15'
name: Stockholm stad
nav: Providers
network: true
overview: Stockholm stad is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Sweden, Public Services, and Open Data.
random_paper: 1
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Stockholm Stad Domain Security
  slug: stockholm-stad-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: stockholm-stad
tags:
- Company
- Government
- Sweden
- Public Services
- Open Data
website: https://stockholm.se/
---
