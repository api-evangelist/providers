---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
artifact_total: 2
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://account.boltzbit.com/pricing
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/boltzbit/refs/heads/main/plans/boltzbit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boltzbit-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://boltzbit.com
- group: company
  title: ''
  type: Blog
  url: https://boltzbit.com/news
- group: operate
  title: ''
  type: Support
  url: https://boltzbit.com/contact
- group: start
  title: ''
  type: Login
  url: https://flow.boltzbit.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boltzbit.com/terms-of-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boltzbit.com/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boltzbit/refs/heads/main/security/boltzbit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boltzbit-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boltzbit/refs/heads/main/llms/boltzbit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boltzbit-llms.txt
created: '2026-07-17'
description: 'Boltzbit builds General Learning Intelligence (GLI) — AI systems that organizations can own, train, and control, learning continuously from proprietary data rather than depending on static, vendor-controlled models. Its product suite forms an operating system for AI-native software: BoltzHub, a marketplace where creators sell AI-powered apps and consumers subscribe to them; BoltzAgent, a self-learning assistant for research-backed chat, document editing, and production-ready code generation; BoltzLearn, an LLM fine-tuning platform for building custom models from your own data; and BoltzCloud, a multi-cloud deployment backbone across GCP, AWS, and Azure. Boltzbit is backed by Speedinvest. The company references an API product surface but does not yet publish public API documentation, an OpenAPI specification, SDKs, or a developer portal; this profile will be enriched as those surfaces are released.'
image: https://cdn.prod.website-files.com/686e2818d5523d438bf5b558/69124c29397e1d135e37dc97_boltzbit-webclip.png
layout: provider
modified: '2026-07-18'
name: Boltzbit
nav: Providers
network: true
overview: 'Boltzbit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine Learning, LLM, and Generative AI.


  Boltzbit''s developer surface includes pricing, engineering blog, support, and 7 more developer resources.'
plans:
- name: Boltzbit Plans Pricing
  plan_count: 3
  slug: boltzbit-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.1
  facets:
    access_clarity: 69.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 12.0
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/boltzbit/refs/heads/main/screenshots/boltzbit-2026-10-11T183741.png
security:
- kind: domain-security
  name: Boltzbit Domain Security
  slug: boltzbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boltzbit
tags:
- Company
- Artificial Intelligence
- Machine Learning
- LLM
- Generative AI
- Enterprise AI
- Model Fine-Tuning
- MLOps
website: https://boltzbit.com
---
