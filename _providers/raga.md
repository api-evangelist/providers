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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: RagaAI provides AI-driven language models and tools for developers.
  name: RagaAI API
  slug: ragaai-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/raga/vendors/raga-vendors.yml
  title: ''
  type: Vendors
  url: vendors/raga-vendors.yml
- group: agent
  href: https://artifacts.apis.io/raga/llms/raga-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/raga-llms.txt
- group: agent
  href: https://artifacts.apis.io/raga/well-known/raga-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/raga-well-known.yml
- group: other
  href: https://artifacts.apis.io/raga/hosts/raga-hosts.yml
  title: ''
  type: Hosts
  url: hosts/raga-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.raga.ai/ragaai-catalyst/user-quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.raga.ai/
- group: auth
  href: https://artifacts.apis.io/raga/security/raga-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/raga-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://raga.ai/
coverage:
  checked: '2026-10-21'
  detail: Docs at https://raga.ai/docs return a JavaScript shell with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://raga.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: RagaAI is an emerging artificial intelligence platform that provides developers with advanced natural language processing and generation capabilities. The company offers a suite of APIs enabling text analysis, content creation, sentiment detection, and conversational agents, targeting enterprises and developers seeking to integrate AI-driven features into their applications. RagaAI emphasizes privacy, scalability, and ease of integration, supporting multiple programming languages and offering comprehensive documentation and SDKs. The platform aims to democratize access to cutting‑edge language models while maintaining compliance with data protection standards.
image: https://raga.ai/og-image.png
layout: provider
modified: '2026-10-21'
name: RagaAI
nav: Providers
network: true
overview: 'RagaAI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Natural Language Processing, Platform, and Developer Tools.


  RagaAI''s developer surface includes getting-started guide, documentation, and 6 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 9.3
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/raga/raga-2026-11-03T141913.png
security:
- kind: domain-security
  name: Raga Domain Security
  slug: raga-domain-security
  summary_line: TLSv1.3 · DMARC
slug: raga
tags:
- Company
- Artificial Intelligence
- Natural Language Processing
- Platform
- Developer Tools
website: https://raga.ai/
---
