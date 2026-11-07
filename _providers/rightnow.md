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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.runinfra.ai/v1
  baseurl_source: declared
  description: The Audio API from RightNow AI — 2 operation(s) for audio.
  name: RightNow AI Audio API
  slug: rightnow-audio-api
- baseURL: https://api.runinfra.ai/v1
  baseurl_source: declared
  description: The Embeddings API from RightNow AI — 1 operation(s) for embeddings.
  name: RightNow AI Embeddings API
  slug: rightnow-embeddings-api
- baseURL: https://api.runinfra.ai/v1
  baseurl_source: declared
  description: The Images API from RightNow AI — 1 operation(s) for images.
  name: RightNow AI Images API
  slug: rightnow-images-api
- baseURL: https://api.runinfra.ai/v1
  baseurl_source: declared
  description: The Models API from RightNow AI — 2 operation(s) for models.
  name: RightNow AI Models API
  slug: rightnow-models-api
- baseURL: https://api.runinfra.ai/v1
  baseurl_source: declared
  description: The Rerank API from RightNow AI — 1 operation(s) for rerank.
  name: RightNow AI Rerank API
  slug: rightnow-rerank-api
- baseURL: https://api.runinfra.ai/v1
  baseurl_source: declared
  description: The Responses API from RightNow AI — 1 operation(s) for responses.
  name: RightNow AI Responses API
  slug: rightnow-responses-api
- baseURL: https://api.runinfra.ai/v1
  baseurl_source: declared
  description: The Chat Completions API from RightNow AI — 1 operation(s) for chat completions.
  name: RightNow AI Chat Completions API
  slug: rightnow-chat-completions-api
artifact_total: 25
collections:
- collection_type: open
  name: RunInfra Audio API
  slug: open-rightnow-audio-api
- collection_type: open
  name: RunInfra Audio Chat API
  slug: open-rightnow-chat-api
- collection_type: open
  name: RunInfra Audio Embeddings API
  slug: open-rightnow-embeddings-api
- collection_type: open
  name: RunInfra Audio Images API
  slug: open-rightnow-images-api
- collection_type: open
  name: RunInfra Audio Models API
  slug: open-rightnow-models-api
- collection_type: open
  name: RunInfra Audio Rerank API
  slug: open-rightnow-rerank-api
- collection_type: open
  name: RunInfra Audio Responses API
  slug: open-rightnow-responses-api
common:
- group: other
  href: https://artifacts.apis.io/rightnow/capabilities/rightnow-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/rightnow-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/rightnow/plans/rightnow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rightnow-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://runinfra.ai/news/rss.xml
- group: company
  title: ''
  type: Website
  url: https://www.runinfra.ai/
- group: agent
  href: https://artifacts.apis.io/rightnow/skills/rightnow-audio-transcription.md
  title: ''
  type: AgentSkill
  url: skills/rightnow-audio-transcription.md
- group: agent
  href: https://artifacts.apis.io/rightnow/mcp/rightnow-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rightnow-mcp.yml
- group: other
  href: https://artifacts.apis.io/rightnow/overlays/rightnow-runinfra-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rightnow-runinfra-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/rightnow/security/rightnow-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/rightnow-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/rightnow/security/rightnow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rightnow-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://runinfra.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://runinfra.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://runinfra.ai/docs/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://runinfra.ai/docs/introduction/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://runinfra.ai/docs/introduction/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://runinfra.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://runinfra.ai/sign-in
- group: commercial
  title: ''
  type: Pricing
  url: https://runinfra.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://runinfra.ai/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RightNow-AI
- group: operate
  title: ''
  type: Support
  url: https://runinfra.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runinfra.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runinfra.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.runinfra.ai/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/runinfrai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/runinfra/
- group: agent
  href: https://artifacts.apis.io/rightnow/llms/rightnow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rightnow-llms.txt
- group: agent
  href: https://artifacts.apis.io/rightnow/well-known/rightnow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rightnow-well-known.yml
- group: auth
  href: https://artifacts.apis.io/rightnow/well-known/rightnow-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rightnow-security.txt
- group: build
  href: https://artifacts.apis.io/rightnow/packages/rightnow-packages.yml
  title: ''
  type: SDKs
  url: packages/rightnow-packages.yml
- group: build
  href: https://artifacts.apis.io/rightnow/packages/rightnow-packages.yml
  title: ''
  type: Packages
  url: packages/rightnow-packages.yml
- group: design
  href: https://artifacts.apis.io/rightnow/conformance/rightnow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rightnow-conformance.yml
- group: design
  href: https://artifacts.apis.io/rightnow/lifecycle/rightnow-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rightnow-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/rightnow/lifecycle/rightnow-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/rightnow-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/rightnow/changelog/rightnow-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rightnow-changelog.yml
- group: auth
  href: https://artifacts.apis.io/rightnow/conformance/rightnow-conformance.yml
  title: ''
  type: Compliance
  url: conformance/rightnow-conformance.yml
- group: auth
  href: https://artifacts.apis.io/rightnow/security/rightnow-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/rightnow-vulnerability-disclosure.yml
created: '2026-07-17'
description: RightNow AI (RunInfra) turns plain-English descriptions of an inference workload into production, OpenAI-compatible AI endpoints. The platform selects open-source models from Hugging Face, benchmarks GPU options, applies kernel optimizations (quantization, speculative decoding, KV-cache tuning, Forge kernels), and deploys serverless, pay-per-token inference APIs on RunInfra Cloud, RunPod, Modal, or self-hosted GPUs. Its REST API is OpenAI-shaped and covers chat completions, responses, embeddings, rerank, image generation, audio speech and transcription, and model listing. A Y Combinator-backed research lab, RightNow AI also publishes open-source GPU-kernel and inference tooling.
finops:
- has_sources: true
  method: derived
  name: Rightnow Finops
  primary_unit: 1m input tokens
  service_category: ''
  slug: rightnow-finops
  template: false
image: https://runinfra.ai/favicon.ico
layout: provider
modified: '2026-10-06'
name: RightNow AI
nav: Providers
network: true
overview: 'RightNow AI publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audio API, Embeddings API, Images API, and 4 more. Tagged areas include Company, Artificial Intelligence, Machine Learning, Inference, and GPU.


  The RightNow AI catalog on APIs.io includes 1 Spectral governance ruleset.


  RightNow AI''s developer surface includes documentation, API reference, getting-started guide, quickstart, signup flow, pricing, engineering blog, and 29 more developer resources.'
plans:
- name: Rightnow Plans Pricing
  plan_count: 10
  slug: rightnow-plans-pricing
- name: Rightnow Price Estimates
  plan_count: 0
  slug: rightnow-price-estimates
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: RightNow AI API Rules
  rule_count: 62
  severity_counts:
    error: 58
    hint: 0
    info: 3
    warn: 1
  slug: rightnow-rules
score:
  band: strong
  composite: 62.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 52.2
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 44.7
  previous_composite: 62.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/rightnow/rightnow-2026-08-17T081603.png
security:
- kind: authentication
  name: Rightnow Authentication
  slug: rightnow-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rightnow Domain Security
  slug: rightnow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rightnow Vulnerability Disclosure
  slug: rightnow-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Rightnow Trust Center
  slug: rightnow-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 3
skills:
- name: audio-transcription
  slug: rightnow-audio-transcription
- name: rag-pipeline
  slug: rightnow-rag-pipeline
- name: streaming-chat
  slug: rightnow-streaming-chat
slug: rightnow
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Inference
- GPU
- Model Deployment
- Serverless
- OpenAI-Compatible
- Embeddings
- MLOps
website: https://www.runinfra.ai/
---
