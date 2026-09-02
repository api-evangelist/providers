---
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pliops-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pliops.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pliops
- group: build
  title: ''
  type: Packages
  url: packages/pliops-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pliops-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/pliops-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pliops-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: Pliops sells a PCIe accelerator card whose only programmable surface is a host-side C/C++ library shipped under a sales/evaluation agreement (demo@pliops.com) — api., docs. and developer.pliops.com all fail to resolve, the github.com/pliops org holds only forks of vllm and fio, no "pliops" package exists in npm/PyPI/RubyGems/crates.io, and the company was absorbed by Astera Labs in February 2026.
  evidence:
  - status: 0
    url: https://developer.pliops.com/
  - status: 0
    url: https://api.pliops.com/
  - status: 200
    url: https://github.com/pliops
  - status: 202
    url: https://pliops.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Pliops is an Israeli data-acceleration semiconductor company, founded in 2017 and headquartered in Ramat Gan, that builds the Extreme Data Processor (XDP) — a low-profile PCIe accelerator card that offloads storage and key-value data-path work from server CPUs. Its software surface is delivered as host libraries rather than as a web API: XDP-AccelKV and XDP-Rocks expose a RocksDB-API-compatible key-value engine (the "storelib" shared library) used as a drop-in under MySQL/MyRocks, Redis, KVRocks, TiDB, Kafka and Spark, and XDP LightningAI extends the same acceleration to GenAI KV-cache offload for vLLM-based inference. Pliops raised roughly $205M from investors including Intel Capital, NVIDIA, AMD, SoftBank Ventures Asia and Western Digital, and was acquired by Astera Labs in February 2026, which took certain assets, IP and about half the staff into a new Israeli R&D center. Pliops has never operated a public developer program: there is no developer portal, no public API reference,
  no published OpenAPI or other machine-readable contract, and no published SDK in any package registry — product and library access runs through a sales/evaluation conversation.'
image: https://avatars.githubusercontent.com/u/74628350?v=4
layout: provider
modified: '2026-08-26'
name: Pliops
nav: Providers
network: true
overview: Pliops is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Hardware, Data Infrastructure, and Storage.
plans:
- name: Pliops Plans Pricing
  plan_count: 0
  slug: pliops-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Pliops Rate Limits
  slug: pliops-rate-limits
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Pliops Domain Security
  slug: pliops-domain-security
  summary_line: TLSv1.3
slug: pliops
tags:
- Company
- Semiconductors
- Hardware
- Data Infrastructure
- Storage
- Key-Value Store
- Data Acceleration
- Artificial Intelligence
- Israel
website: https://pliops.com/
---
