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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axoft/refs/heads/main/llms/axoft-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/axoft-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axoft/refs/heads/main/hosts/axoft-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axoft-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Axoft
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axoft/refs/heads/main/security/axoft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axoft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.axoft.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Axoft is an Argentine software company offering the Tango ERP suite, a cloud and on‑premise platform for accounting, HR, point‑of‑sale and business management. Founded over 35 years ago, it serves thousands of SMEs and large enterprises across Argentina, providing automation, compliance and scalable solutions. The company emphasizes community support, extensive training, and integration capabilities, positioning itself as a leading ERP provider in the region.
layout: provider
modified: '2026-09-27'
name: Axoft
nav: Providers
network: true
overview: Axoft is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include ERP, Software, Argentina, Business Management, and Cloud.
random_paper: 18
score:
  band: minimal
  composite: 4.4
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
    discoverability: 51.8
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Axoft Domain Security
  slug: axoft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: axoft
tags:
- ERP
- Software
- Argentina
- Business Management
- Cloud
website: https://www.axoft.com
---
