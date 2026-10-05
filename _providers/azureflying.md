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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azureflying/refs/heads/main/hosts/azureflying-hosts.yml
  title: ''
  type: Hosts
  url: hosts/azureflying-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://azureflying.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azureflying/refs/heads/main/security/azureflying-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azureflying-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://azureflying.com
coverage:
  checked: 2026-09-27
  detail: API host https://api.azureflying.com returned no OpenAPI spec and no documentation was found.
  evidence:
  - status: 0
    url: https://api.azureflying.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Azureflying (蔚复来) is a Zhejiang‑based technology company that leverages AI and digital solutions for green waste recycling, smart city infrastructure, and sustainable resource management. It offers AI‑enabled waste classification hardware, end‑to‑end waste processing services, and digital platforms that enable traceability, data analytics, and carbon‑neutral operations for municipalities and enterprises. The firm reports over 200 patents, operates across 200 cities, and focuses on turning waste into valuable resources through AI‑driven processes.
layout: provider
modified: '2026-09-27'
name: Azureflying
nav: Providers
network: true
overview: Azureflying is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Waste Management, Green Technology, and Smart Cities.
random_paper: 12
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
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Azureflying Domain Security
  slug: azureflying-domain-security
  summary_line: TLSv1.2
slug: azureflying
tags:
- Company
- Artificial Intelligence
- Waste Management
- Green Technology
- Smart Cities
website: https://azureflying.com
---
