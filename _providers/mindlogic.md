---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Mindlogic Agentic Access
  operation_count: 17
  slug: mindlogic-agentic-access
  summary_line: 17 operations · 9 acting
api_count: 1
apis:
- baseURL: https://factchat-cloud.mindlogic.ai/v1/gateway
  baseurl_source: declared
  description: The Audio API from Mindlogic — 1 operation(s) for audio.
  name: Mindlogic Audio API
  slug: mindlogic-audio-api
- baseURL: https://factchat-cloud.mindlogic.ai/v1/gateway
  baseurl_source: declared
  description: The Chat API from Mindlogic — 1 operation(s) for chat.
  name: Mindlogic Chat API
  slug: mindlogic-chat-api
- baseURL: https://factchat-cloud.mindlogic.ai/v1/gateway
  baseurl_source: declared
  description: The Credits API from Mindlogic — 1 operation(s) for credits.
  name: Mindlogic Credits API
  slug: mindlogic-credits-api
- baseURL: https://factchat-cloud.mindlogic.ai/v1/gateway
  baseurl_source: declared
  description: The gateway API from Mindlogic — 7 operation(s) for gateway.
  name: Mindlogic gateway API
  slug: mindlogic-gateway-api
- baseURL: https://factchat-cloud.mindlogic.ai/v1/gateway
  baseurl_source: declared
  description: The Images API from Mindlogic — 2 operation(s) for images.
  name: Mindlogic Images API
  slug: mindlogic-images-api
- baseURL: https://factchat-cloud.mindlogic.ai/v1/gateway
  baseurl_source: declared
  description: The Models API from Mindlogic — 2 operation(s) for models.
  name: Mindlogic Models API
  slug: mindlogic-models-api
- baseURL: https://factchat-cloud.mindlogic.ai/v1/gateway
  baseurl_source: declared
  description: The Video API from Mindlogic — 3 operation(s) for video.
  name: Mindlogic Video API
  slug: mindlogic-video-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fast Audio API
  slug: open-mindlogic-audio-api
- collection_type: open
  name: Fast Audio Chat API
  slug: open-mindlogic-chat-api
- collection_type: open
  name: Fast Audio Credits API
  slug: open-mindlogic-credits-api
- collection_type: open
  name: Fast Audio gateway API
  slug: open-mindlogic-gateway-api
- collection_type: open
  name: Fast Audio Images API
  slug: open-mindlogic-images-api
- collection_type: open
  name: Fast Audio Models API
  slug: open-mindlogic-models-api
- collection_type: open
  name: Fast Audio Video API
  slug: open-mindlogic-video-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mindlogic.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mindlogic.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mindlogic.ai/docs/general/api-gateway/reference/chat-completions
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mindlogic.ai/docs/general/api-gateway/getting-started/overview
- group: auth
  title: ''
  type: Authentication
  url: authentication/mindlogic-authentication.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mindlogic-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mindlogic-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mindlogic-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mindlogic-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mindlogic-api-gateway-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/mindlogic-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mindlogic-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mindlogic-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mindlogic-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mindlogic-agentic-access.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.mindlogic.ai/
- group: operate
  title: ''
  type: Support
  url: https://docs.mindlogic.ai/docs/general/factchat/support/help-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://factchat-public.s3.ap-northeast-2.amazonaws.com/public/pdf/ko_terms_of_service.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://factchat-public.s3.ap-northeast-2.amazonaws.com/public/pdf/ko_privacy_policy.pdf
- group: company
  title: ''
  type: Website
  url: https://mindlogic.ai/
created: '2026-07-17'
description: Mindlogic is a South Korean generative-AI company whose products include FactChat (a multi-LLM enterprise chat platform with Studio chatbot building, deep research, meeting notes, and image/video generation), Bliss (a persona chatbot that learns a person's voice and personality for fan engagement), and Informe (a multilingual document-grounded website chatbot). For developers, Mindlogic operates the FactChat API Gateway — a unified, OpenAI- and Anthropic-compatible LLM proxy that fronts models from OpenAI, Anthropic, Google Gemini, xAI and Perplexity behind a single API key, metered in credits, with chat completions, an OpenAI Responses pass-through, an Anthropic Messages pass-through, text-to-speech, and image/video generation.
image: https://mindlogic.ai/apple-icon.png
layout: provider
modified: '2026-07-20'
name: Mindlogic
nav: Providers
network: true
overview: 'Mindlogic publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Chat API, Credits API, and 4 more. Tagged areas include Company, Ai Ml, Generative AI, Conversational AI, and LLM Gateway.


  Mindlogic''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, and 15 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 43.8
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mindlogic/refs/heads/main/screenshots/mindlogic-2026-08-07T172941.png
security:
- kind: authentication
  name: Mindlogic Authentication
  slug: mindlogic-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Mindlogic Domain Security
  slug: mindlogic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mindlogic
tags:
- Company
- Ai Ml
- Generative AI
- Conversational AI
- LLM Gateway
- Chatbots
- API Gateway
- Korea
website: https://mindlogic.ai/
---
