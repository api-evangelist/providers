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
  href: https://raw.githubusercontent.com/api-evangelist/benchllm/refs/heads/main/hosts/benchllm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/benchllm-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/benchllm/refs/heads/main/packages/benchllm-packages.yml
  title: ''
  type: SDKs
  url: packages/benchllm-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/benchllm/refs/heads/main/packages/benchllm-packages.yml
  title: ''
  type: Packages
  url: packages/benchllm-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/benchllm/refs/heads/main/security/benchllm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/benchllm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://benchllm.com/
coverage:
  checked: '2026-10-16'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the API host or documentation pages.
  evidence:
  - status: 0
    url: https://api.benchllm.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: BenchLLM provides a comprehensive benchmarking platform for large language models (LLMs), enabling developers and researchers to evaluate model performance across a variety of tasks such as text generation, summarization, translation, and question answering. The service offers detailed metrics, comparative analysis, and customizable test suites, helping users make informed decisions about model selection and optimization. BenchLLM aims to accelerate AI development by delivering transparent, reproducible, and scalable benchmarking solutions for the rapidly evolving LLM landscape.
layout: provider
modified: '2026-10-16'
name: BenchLLM
nav: Providers
network: true
overview: BenchLLM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Benchmarking, LLM, and Evaluation.
random_paper: 1
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
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Benchllm Domain Security
  slug: benchllm-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: benchllm
tags:
- Company
- Artificial Intelligence
- Benchmarking
- LLM
- Evaluation
- Software-as-a-Service
website: https://benchllm.com/
---
