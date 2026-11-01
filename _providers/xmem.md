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
api_count: 1
apis:
- description: API for managing memory operations, types, LLM adapters, and vector stores in xMem.
  name: xMem API
  slug: xmem-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/xmem/hosts/xmem-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xmem-hosts.yml
- group: other
  href: https://artifacts.apis.io/xmem/vendors/xmem-vendors.yml
  title: ''
  type: Vendors
  url: vendors/xmem-vendors.yml
- group: auth
  href: https://artifacts.apis.io/xmem/security/xmem-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xmem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://xmem.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://www.xmem.xyz/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.xmem.xyz/docs/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://www.xmem.xyz/docs/api
coverage:
  checked: '2026-10-19'
  detail: Documentation pages are rendered via JavaScript and contain no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://www.xmem.xyz/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: xMem provides a hybrid memory orchestration platform for large language models (LLMs), combining long‑term knowledge storage with real‑time session context. It enables developers to integrate persistent and session memory into AI applications, improving relevance, accuracy, and user experience. Features include vector‑search backed knowledge graphs, support for open‑source LLMs, and easy API integration for seamless RAG and agent workflows.
image: https://www.xmem.xyz/thumbnail.png
layout: provider
modified: '2026-10-19'
name: xmem
nav: Providers
network: true
overview: 'xmem is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Memory, LLM, and Retrieval.


  xmem''s developer surface includes documentation, getting-started guide, API reference, and 4 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Xmem Domain Security
  slug: xmem-domain-security
  summary_line: TLSv1.3 · HSTS
slug: xmem
tags:
- Company
- Artificial Intelligence
- Memory
- LLM
- Retrieval
website: https://xmem.xyz/
---
