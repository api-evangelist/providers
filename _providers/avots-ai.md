---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Drop-in OpenAI API offering 40+ models via a single base URL and av_mcp_ key.
  name: OpenAI-compatible API
  slug: openai-compatible-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/avots-ai/llms/avots-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avots-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/avots-ai/well-known/avots-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avots-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/avots-ai/hosts/avots-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avots-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/avots-ai/vendors/avots-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avots-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/avots-ai/security/avots-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avots-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avots.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://avots.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avots.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avots.ai/privacy-policy
coverage:
  checked: '2026-11-02'
  detail: The provider documents an OpenAI-compatible API at https://avots.ai/openai but offers no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://avots.ai/openai
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: avots.ai is an AI aggregator platform offering a single subscription that provides access to over 40 AI models, including GPT‑5, Claude, Gemini, Veo, FLUX, DeepSeek and many others. Users can generate text, images, video, music, and code through a unified web app, with plans ranging from a free tier to €149 per month. The service positions itself as a ChatGPT alternative, delivering a broad range of generative AI capabilities under one roof.
image: https://avots.ai/logo.png
layout: provider
modified: '2026-11-02'
name: avots.ai
nav: Providers
network: true
overview: 'avots.ai is listed with 1 API on the [APIs.io](https://apis.io/) network: OpenAI-compatible API. Tagged areas include Artificial Intelligence, Subscription, Generative AI, Platform, and Aggregator.


  avots.ai''s developer surface includes pricing and 8 more developer resources.'
plans:
- name: Avots Ai Plans Pricing
  plan_count: 0
  slug: avots-ai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Avots Ai Rate Limits
  slug: avots-ai-rate-limits
scopes:
- name: Avots Ai Scopes
  scope_count: 0
  slug: avots-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 20.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Avots Ai Authentication
  slug: avots-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Avots Ai Domain Security
  slug: avots-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: avots-ai
tags:
- Artificial Intelligence
- Subscription
- Generative AI
- Platform
- Aggregator
website: https://avots.ai/
---
