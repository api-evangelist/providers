---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Simplismart Agentic Access
  operation_count: 25
  slug: simplismart-agentic-access
  summary_line: 25 operations · 15 acting
api_count: 18
apis:
- baseURL: https://api.simplismart.live
  baseurl_source: declared
  description: Large Language Model chat completion services
  name: Simplismart Chat Completion API
  slug: simplismart-chat-completion-api
- baseURL: https://api.simplismart.live
  baseurl_source: declared
  description: Flux model training endpoints
  name: Simplismart Flux Training API
  slug: simplismart-flux-training-api
- baseURL: https://api.simplismart.live
  baseurl_source: declared
  description: The Llm API from Simplismart — 1 operation(s) for llm.
  name: Simplismart Llm API
  slug: simplismart-llm-api
- baseURL: https://api.simplismart.live
  baseurl_source: declared
  description: Performance and usage metrics for LLM requests
  name: Simplismart Metrics API
  slug: simplismart-metrics-api
- baseURL: https://api.simplismart.live
  baseurl_source: declared
  description: The Model API from Simplismart — 1 operation(s) for model.
  name: Simplismart Model API
  slug: simplismart-model-api
- baseURL: https://api.simplismart.live
  baseurl_source: declared
  description: The Speech to Text API from Simplismart — 2 operation(s) for speech to text.
  name: Simplismart Speech to Text API
  slug: simplismart-speech-to-text-api
- baseURL: https://api.simplismart.live
  baseurl_source: declared
  description: LLM/VLM model training endpoints
  name: Simplismart Training API
  slug: simplismart-training-api
artifact_total: 25
collections:
- collection_type: open
  name: DeepSeek R1 Distil Qwen-32B Chat Completion API
  slug: open-simplismart-chat-completion-api
- collection_type: open
  name: DeepSeek R1 Distil Qwen-32B Chat Completion Flux API
  slug: open-simplismart-flux-api
- collection_type: open
  name: DeepSeek R1 Distil Qwen-32B Chat Completion Flux Training API
  slug: open-simplismart-flux-training-api
- collection_type: open
  name: DeepSeek R1 Distil Qwen-32B Chat Completion Llm API
  slug: open-simplismart-llm-api
- collection_type: open
  name: DeepSeek R1 Distil Qwen-32B Chat Completion Metrics API
  slug: open-simplismart-metrics-api
- collection_type: open
  name: DeepSeek R1 Distil Qwen-32B Chat Completion Model API
  slug: open-simplismart-model-api
- collection_type: open
  name: DeepSeek R1 Distil Qwen-32B Chat Completion Speech to Text API
  slug: open-simplismart-speech-to-text-api
- collection_type: open
  name: DeepSeek R1 Distil Qwen-32B Chat Completion Training API
  slug: open-simplismart-training-api
common:
- group: commercial
  href: https://artifacts.apis.io/simplismart/plans/simplismart-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/simplismart-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/simplismart/capabilities/simplismart-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/simplismart-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.simplismart.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.simplismart.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.simplismart.ai/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.simplismart.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.simplismart.ai/quickstart/inference
- group: operate
  title: ''
  type: Support
  url: https://www.simplismart.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://www.simplismart.ai/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.simplismart.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.simplismart.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.simplismart.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.simplismart.ai/privacy-policy
- group: auth
  href: https://artifacts.apis.io/simplismart/authentication/simplismart-authentication.yml
  title: ''
  type: Authentication
  url: authentication/simplismart-authentication.yml
- group: build
  href: https://artifacts.apis.io/simplismart/packages/simplismart-packages.yml
  title: ''
  type: Packages
  url: packages/simplismart-packages.yml
- group: build
  href: https://artifacts.apis.io/simplismart/packages/simplismart-packages.yml
  title: ''
  type: SDKs
  url: packages/simplismart-packages.yml
- group: build
  href: https://artifacts.apis.io/simplismart/cli/simplismart-cli.yml
  title: ''
  type: CLI
  url: cli/simplismart-cli.yml
- group: agent
  href: https://artifacts.apis.io/simplismart/mcp/simplismart-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/simplismart-mcp.yml
- group: agent
  href: https://artifacts.apis.io/simplismart/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/simplismart/llms/simplismart-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/simplismart-llms.txt
- group: design
  href: https://artifacts.apis.io/simplismart/errors/simplismart-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/simplismart-problem-types.yml
- group: design
  href: https://artifacts.apis.io/simplismart/conventions/simplismart-conventions.yml
  title: ''
  type: Conventions
  url: conventions/simplismart-conventions.yml
- group: design
  href: https://artifacts.apis.io/simplismart/conformance/simplismart-conformance.yml
  title: ''
  type: Conformance
  url: conformance/simplismart-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.simplismart.ai/
- group: start
  href: https://artifacts.apis.io/simplismart/sandbox/simplismart-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/simplismart-sandbox.yml
- group: design
  href: https://artifacts.apis.io/simplismart/data-model/simplismart-data-model.yml
  title: ''
  type: DataModel
  url: data-model/simplismart-data-model.yml
- group: other
  href: https://artifacts.apis.io/simplismart/overlays/simplismart-flux-dev-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/simplismart-flux-dev-overlay.yaml
- group: other
  href: https://artifacts.apis.io/simplismart/overlays/simplismart-llm-training-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/simplismart-llm-training-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/simplismart/agentic-access/simplismart-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/simplismart-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/simplismart/security/simplismart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/simplismart-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/simplismart/security/simplismart-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/simplismart-trust-center.yml
created: '2026-07-17'
description: Simplismart is an AI inference and model-deployment platform that lets teams run, fine-tune, and self-host generative AI models on optimized GPU infrastructure. It offers OpenAI-compatible LLM chat inference (Llama, Qwen, Gemma, Mixtral, DeepSeek), Whisper speech-to-text transcription, and Flux image generation as shared or dedicated endpoints, plus a Training Suite for fine-tuning LLM/VLM and Flux models. A Model Suite handles model compilation, clusters (own-cloud EKS/Kubernetes / bring-your-own-compute), deployments with autoscaling, secrets, quotas, and observability (alerting and metric export to Datadog, New Relic, Prometheus). A Python SDK and `simplismart` CLI cover the full MLOps lifecycle. Simplismart is backed by Accel.
finops:
- has_sources: true
  method: derived
  name: Simplismart Finops
  primary_unit: 1m tokens
  service_category: ''
  slug: simplismart-finops
  template: false
image: https://cdn.prod.website-files.com/688cd7a9d1e409a52d962d73/689a55919a5ee5abe9a2ed5e_meta.png
layout: provider
modified: '2026-07-21'
name: Simplismart
nav: Providers
network: true
overview: 'Simplismart publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Chat Completion API, Flux Training API, Llm API, and 4 more. Tagged areas include Company, Artificial Intelligence, Machine Learning, Inference, and LLM.


  The Simplismart catalog on APIs.io includes 1 Spectral governance ruleset.


  Simplismart''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Simplismart Plans Pricing
  plan_count: 24
  slug: simplismart-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Simplismart API Rules
  rule_count: 57
  severity_counts:
    error: 47
    hint: 0
    info: 5
    warn: 5
  slug: simplismart-rules
score:
  band: strong
  composite: 60.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 53.4
    developer_ergonomics: 80.4
    discoverability: 78.6
    operational_transparency: 0.0
  previous_composite: 60.2
  provenance:
    agentic_access: derived
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
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/simplismart/simplismart-2026-08-17T081859.png
security:
- kind: authentication
  name: Simplismart Authentication
  slug: simplismart-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Simplismart Domain Security
  slug: simplismart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Simplismart Trust Center
  slug: simplismart-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 3
skills:
- name: Start and monitor an LLM/VLM fine-tuning job on Simplismart
  slug: simplismart-finetune-llm
- name: Run an LLM chat completion on Simplismart
  slug: simplismart-run-llm-chat
- name: Transcribe or translate audio with Whisper on Simplismart
  slug: simplismart-transcribe-audio
slug: simplismart
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Inference
- LLM
- Model Deployment
- Fine-Tuning
- MLOps
- GPU
- Speech-to-Text
- Image Generation
website: https://www.simplismart.ai/
---
