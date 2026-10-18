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
  href: https://raw.githubusercontent.com/api-evangelist/cisinfo/refs/heads/main/llms/cisinfo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cisinfo-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cisinfo/refs/heads/main/hosts/cisinfo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cisinfo-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cisinfo/refs/heads/main/security/cisinfo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cisinfo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://cisinfo.com
coverage:
  checked: '2026-10-08'
  detail: The homepage returns a JavaScript shell with no readable content, preventing machine extraction of API specifications.
  evidence:
  - status: 200
    url: https://cisinfo.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: Cisinfo is a supplier and service provider of Manufacturing Execution Systems (MES), Laboratory Information Management Systems (LIMS), and an industrial cloud platform. The company focuses on delivering integrated solutions for material management, energy management, and production monitoring, targeting manufacturers and laboratories seeking digital transformation. Based in Beijing, Cisinfo develops software that enables real‑time data collection, analytics, and workflow automation across the enterprise, helping clients improve efficiency, compliance, and product quality.
layout: provider
modified: '2026-10-08'
name: Cisinfo
nav: Providers
network: true
overview: Cisinfo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, MES, LIMS, and Cloud.
random_paper: 21
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
    developer_ergonomics: 0.0
    discoverability: 51.8
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
  name: Cisinfo Domain Security
  slug: cisinfo-domain-security
  summary_line: TLSv1.3
slug: cisinfo
tags:
- Company
- Manufacturing
- MES
- LIMS
- Cloud
- Beijing
website: http://cisinfo.com
---
