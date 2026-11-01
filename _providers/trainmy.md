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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API integration page providing developer information.
  name: TrainMyAI API
  slug: trainmyai-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/trainmy/hosts/trainmy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trainmy-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://trainmy.ai/management/
- group: auth
  href: https://artifacts.apis.io/trainmy/security/trainmy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trainmy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trainmy.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://trainmy.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://trainmy.ai/api/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trainmy.ai/terms-of-use/
coverage:
  checked: '2026-10-19'
  detail: API reference page returns HTML with no OpenAPI or other machine-readable contract.
  evidence:
  - status: 200
    url: https://trainmy.ai/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: TrainMyAI provides a complete solution for building Retrieval Augmented Generation (RAG) AI chatbots. It offers customizable AI chatbot deployment on-premise or cloud, with integrations for WhatsApp, web, and private APIs. Features include fine-grained user management, usage history, and secure private data handling. The platform supports multiple language models and offers extensive documentation and API access for developers.
layout: provider
modified: '2026-10-19'
name: TrainMyAI
nav: Providers
network: true
overview: 'TrainMyAI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Chatbots, RAG, and Platform.


  TrainMyAI''s developer surface includes documentation, API reference, and 5 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Trainmy Domain Security
  slug: trainmy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: trainmy
tags:
- Company
- Artificial Intelligence
- Chatbots
- RAG
- Platform
website: https://trainmy.ai/
---
