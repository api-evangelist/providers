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
  href: https://raw.githubusercontent.com/api-evangelist/insee/refs/heads/main/hosts/insee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/insee-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.insee.fr/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/insee/refs/heads/main/security/insee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/insee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.insee.fr
coverage:
  checked: '2026-10-14'
  detail: No public API documentation or machine‑readable contract was found after probing the API host.
  evidence:
  - status: 0
    url: https://api.insee.fr
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: INSEE (Institut national de la statistique et des études économiques) is France's national institute for statistics and economic studies. It provides official statistical data, analyses, and publications covering demographics, economy, society, and geography. The institute offers open data portals, APIs, and documentation for developers to access datasets on population, employment, inflation, and more, supporting research, policy making, and public information.
layout: provider
modified: '2026-10-14'
name: INSEE
nav: Providers
network: true
overview: 'INSEE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Statistics, Government, Data, France, and Economics.


  INSEE''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 3.8
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
    developer_ergonomics: 2.4
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Insee Domain Security
  slug: insee-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: insee
tags:
- Statistics
- Government
- Data
- France
- Economics
website: https://www.insee.fr
---
