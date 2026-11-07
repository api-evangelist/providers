---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public read‑only API providing access to research records and experiment data.
  name: CrystalRAM API
  slug: crystalram-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/crystalram-ai/llms/crystalram-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crystalram-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/crystalram-ai/hosts/crystalram-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crystalram-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/crystalram-ai/vendors/crystalram-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crystalram-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/crystalram-ai/security/crystalram-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crystalram-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crystalram.ai/
- group: operate
  title: ''
  type: Support
  url: https://www.crystalram.ai/join-ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.crystalram.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://www.crystalram.ai/
- group: agent
  title: ''
  type: llms.txt
  url: https://crystalram.ai/llms.txt
- group: other
  title: ''
  type: ServerJSON
  url: https://crystalram.ai/server.json
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found despite public documentation pages.
  evidence:
  - status: 200
    url: https://www.crystalram.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: CrystalRAM is an open research observatory focused on pioneering memory architectures for AI. It provides a public, read‑only scientific record of findings, experiments, limitations, and the AI research team working transparently. The site offers detailed architecture explanations, experimental results, and an open commons for community collaboration, aiming to advance understanding of novel memory roles in large‑scale AI models.
image: https://crystalram.ai/og.png
layout: provider
modified: '2026-11-04'
name: CrystalRAM
nav: Providers
network: true
overview: 'CrystalRAM is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Memory Architecture, Open Science, and Research.


  CrystalRAM''s developer surface includes support, documentation, API reference, and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 8.6
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
    developer_ergonomics: 21.4
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
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crystalram Ai Domain Security
  slug: crystalram-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crystalram-ai
tags:
- Company
- Artificial Intelligence
- Memory Architecture
- Open Science
- Research
website: https://crystalram.ai/
---
