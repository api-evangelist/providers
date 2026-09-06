---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Doubao Agentic Access
  operation_count: 7
  slug: doubao-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 1
apis:
- description: OpenAI-compatible chat, responses, embedding, batch, image (Seedream), video (Seedance), 3D, and TTS APIs serving the Doubao model family. Base URL https://ark.cn-beijing.volces.com/api/v3. Includes t
  name: Volcano Engine Ark API
  slug: ark
- baseURL: https://ark.cn-beijing.volces.com/api/v3
  baseurl_source: declared
  description: The Batch API from ByteDance Doubao — 1 operation(s) for batch.
  name: ByteDance Doubao Batch API
  slug: doubao-batch-api
- baseURL: https://ark.cn-beijing.volces.com/api/v3
  baseurl_source: declared
  description: The Chat API from ByteDance Doubao — 1 operation(s) for chat.
  name: ByteDance Doubao Chat API
  slug: doubao-chat-api
- baseURL: https://ark.cn-beijing.volces.com/api/v3
  baseurl_source: declared
  description: The Embeddings API from ByteDance Doubao — 1 operation(s) for embeddings.
  name: ByteDance Doubao Embeddings API
  slug: doubao-embeddings-api
- baseURL: https://ark.cn-beijing.volces.com/api/v3
  baseurl_source: declared
  description: The Images API from ByteDance Doubao — 1 operation(s) for images.
  name: ByteDance Doubao Images API
  slug: doubao-images-api
- baseURL: https://ark.cn-beijing.volces.com/api/v3
  baseurl_source: declared
  description: The Videos API from ByteDance Doubao — 2 operation(s) for videos.
  name: ByteDance Doubao Videos API
  slug: doubao-videos-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Volcano Engine Ark API (Doubao) Batch API
  slug: open-doubao-batch-api
- collection_type: open
  name: Volcano Engine Ark API (Doubao) Batch Chat API
  slug: open-doubao-chat-api
- collection_type: open
  name: Volcano Engine Ark API (Doubao) Batch Embeddings API
  slug: open-doubao-embeddings-api
- collection_type: open
  name: Volcano Engine Ark API (Doubao) Batch Images API
  slug: open-doubao-images-api
- collection_type: open
  name: Volcano Engine Ark API (Doubao) Batch Videos API
  slug: open-doubao-videos-api
- collection_type: open
  name: Volcano Engine Ark API (Doubao)
  slug: open-doubao
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/doubao-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/doubao-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doubao-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doubao-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bytedance
- group: company
  title: ''
  type: Website
  url: https://www.volcengine.com/product/doubao
- group: docs
  title: ''
  type: Documentation
  url: https://www.volcengine.com/docs/82379
- group: commercial
  title: ''
  type: Plans
  url: plans/doubao-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/doubao-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/doubao-finops.yml
created: '2026-05-08'
description: Doubao is ByteDance's foundation model family, served via the Volcano Engine Ark platform. Offers chat completions, deep reasoning, multimodal vision, embeddings, image generation (Seedream), video generation (Seedance), 3D generation, and TTS through OpenAI-compatible and native endpoints.
finops:
- name: Doubao Finops
  service_category: AI and Machine Learning
  slug: doubao-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doubao.png
layout: provider
modified: '2026-05-08'
name: ByteDance Doubao
nav: Providers
network: true
overview: 'ByteDance Doubao publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Batch API, Chat API, Embeddings API, and 2 more. Tagged areas include Artificial Intelligence, LLM, Inference, ByteDance, and Multi-Modal.


  ByteDance Doubao''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Doubao Plans Pricing
  plan_count: 2
  slug: doubao-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Doubao Rate Limits
  slug: doubao-rate-limits
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 45.0
    catalog_earned_first_party: 0.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doubao/refs/heads/main/screenshots/doubao-2026-06-20T180218.png
security:
- kind: authentication
  name: Doubao Authentication
  slug: doubao-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Doubao Domain Security
  slug: doubao-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Doubao Vulnerability Disclosure
  slug: doubao-vulnerability-disclosure
  summary_line: disclosure policy published
slug: doubao
tags:
- Artificial Intelligence
- LLM
- Inference
- ByteDance
- Multi-Modal
- Volcano Engine
website: https://www.volcengine.com/product/doubao
---
