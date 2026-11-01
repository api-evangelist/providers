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
  href: https://artifacts.apis.io/callejear-com/llms/callejear-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/callejear-com-llms.txt
- group: other
  href: https://artifacts.apis.io/callejear-com/hosts/callejear-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/callejear-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/callejear-com/vendors/callejear-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/callejear-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/callejear-com/security/callejear-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/callejear-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://callejear.com/
coverage:
  checked: '2026-10-30'
  detail: The site provides no public API documentation or machine‑readable contract; all spec URL probes returned 404.
  evidence:
  - status: 200
    url: https://callejear.com/
  - status: 404
    url: https://callejear.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Callejear.com is an independent Spanish project created by Yoel Castaño that provides a comprehensive municipal directory for all 8,132 municipalities of Spain. It offers open data on population, housing, employment, income, and a complete street directory, along with tools such as flood visualization and fiber coverage maps. The platform aggregates official municipal statistics and presents them through an easy‑to‑use web interface, supporting researchers, planners, and citizens seeking detailed local information.
image: https://callejear.com/img/og-default.png
layout: provider
modified: '2026-10-30'
name: callejear-com
nav: Providers
network: true
overview: callejear-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Geography, Spain, and Open-Data.
random_paper: 23
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 7
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
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Callejear Com Domain Security
  slug: callejear-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: callejear-com
tags:
- Company
- Data
- Geography
- Spain
- Open-Data
- Municipal
website: https://callejear.com/
---
