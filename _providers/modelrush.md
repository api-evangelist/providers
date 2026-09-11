---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.8
  scored_at: '2026-09-10'
api_count: 1
apis:
- description: OpenAI-style hosted inference. GET /v1/models answers keyless with the live catalog (verified 2026-09-09); calls authenticate with Bearer mr_live_ keys.
  name: ModelRush API
  slug: modelrush-api
artifact_total: 9
asyncapis:
- description: ''
  name: Modelrush Webhooks
  slug: modelrush-webhooks
collections:
- collection_type: postman
  name: ModelRush Public API
  slug: postman-ModelRush-Public-API
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modelrush-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/modelrush-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/modelrush-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/modelrush-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://modelrush.ai
- group: company
  title: ''
  type: Blog
  url: https://modelrush.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Moonveil-AI
- group: operate
  title: ''
  type: Support
  url: https://modelrush.ai/docs/faq
- group: start
  title: ''
  type: Login
  url: https://modelrush.ai/dashboard
- group: start
  title: ''
  type: SignUp
  url: https://modelrush.ai/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://modelrush.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modelrush.ai/privacy
created: '2026-09-10'
description: A multilingual multimodal AI API platform (text, image, video, speech) serving a hosted model catalog -- open-weight families (DeepSeek, GLM, CosyVoice, Fun-ASR) alongside grok-family entries -- behind one bearer key with a public keyless model inventory and per-model regional pricing.
layout: provider
mcp_servers:
- description: ''
  name: ModelRush MCP Server
  slug: modelrush-mcp-server
modified: '2026-09-10'
name: ModelRush
nav: Providers
network: true
overview: 'ModelRush publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, LLM, Inference, Multimodal, and Model Hosting.


  The ModelRush catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ModelRush''s developer surface includes authentication, engineering blog, support, signup flow, and 8 more developer resources.'
plans:
- name: Modelrush Plans Pricing
  plan_count: 0
  slug: modelrush-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Modelrush Rate Limits
  slug: modelrush-rate-limits
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 62.4
    developer_ergonomics: 54.2
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Modelrush Authentication
  slug: modelrush-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Modelrush Domain Security
  slug: modelrush-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Modelrush Vulnerability Disclosure
  slug: modelrush-vulnerability-disclosure
  summary_line: Hackerone
slug: modelrush
tags:
- AI
- LLM
- Inference
- Multimodal
- Model Hosting
- Speech
- Image Generation
website: https://modelrush.ai
---
