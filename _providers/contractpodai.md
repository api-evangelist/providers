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
api_count: 1
apis:
- description: API for ContractPodAi (Leah) platform
  name: ContractPodAi API
  slug: contractpodai-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contractpodai/refs/heads/main/llms/contractpodai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contractpodai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contractpodai/refs/heads/main/hosts/contractpodai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contractpodai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contractpodai/refs/heads/main/vendors/contractpodai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contractpodai-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leahai.com/privacy-statement
- group: company
  title: ''
  type: Newsroom
  url: https://leahai.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://leahai.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contractpodai/refs/heads/main/security/contractpodai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contractpodai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://leahai.com/
coverage:
  checked: '2026-10-10'
  detail: OpenAPI spec endpoints on https://api.leahai.com return HTTP 502, providing no machine‑readable contract.
  evidence:
  - status: 502
    url: https://api.leahai.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: ContractPodAi, now operating as Leah, is an agentic AI platform that unifies contract lifecycle management, legal transformation, and source‑to‑pay automation. It delivers end‑to‑end solutions for legal, procurement, and finance teams, leveraging AI to streamline contract creation, analysis, compliance, and execution across enterprises.
image: https://leahai.com/favicon.ico
layout: provider
modified: '2026-10-10'
name: ContractPodAi
nav: Providers
network: true
overview: 'ContractPodAi is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Legal Tech, ContractManagement, and Procurement.


  ContractPodAi''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contractpodai Domain Security
  slug: contractpodai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: contractpodai
tags:
- Company
- Artificial Intelligence
- Legal Tech
- ContractManagement
- Procurement
website: https://leahai.com/
---
