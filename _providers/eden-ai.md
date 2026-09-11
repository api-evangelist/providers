---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-09-10'
agentic_access:
- acting_count: 28
  human_in_the_loop: 6
  name: Eden Ai Agentic Access
  operation_count: 53
  slug: eden-ai-agentic-access
  summary_line: 53 operations · 28 acting · 6 human-in-the-loop
api_count: 13
apis:
- description: Eden AI API is a versatile tool that leverages artificial intelligence to enhance and streamline various business processes. By providing access to advanced machine learning and natural language proce
  name: Eden AI API
  slug: eden-ai
- baseURL: https://api.edenai.run/v2
  baseurl_source: declared
  description: The Audio API from Eden AI — the first-party OpenAPI harvested from api.edenai.run declares 9 operation(s).
  name: Eden AI Audio API
  slug: eden-ai-audio-api
- baseURL: https://api.edenai.run/v2
  baseurl_source: declared
  description: The Image API from Eden AI — the first-party OpenAPI harvested from api.edenai.run declares 34 operation(s).
  name: Eden AI Image API
  slug: eden-ai-image-api
- baseURL: https://api.edenai.run/v2
  baseurl_source: declared
  description: The OCR API from Eden AI — the first-party OpenAPI harvested from api.edenai.run declares 22 operation(s).
  name: Eden AI OCR API
  slug: eden-ai-ocr-api
- baseURL: https://api.edenai.run/v2
  baseurl_source: declared
  description: The Text API from Eden AI — the first-party OpenAPI harvested from api.edenai.run declares 17 operation(s).
  name: Eden AI Text API
  slug: eden-ai-text-api
- baseURL: https://api.edenai.run/v2
  baseurl_source: declared
  description: The Translation API from Eden AI — the first-party OpenAPI harvested from api.edenai.run declares 3 operation(s).
  name: Eden AI Translation API
  slug: eden-ai-translation-api
- baseURL: https://api.edenai.run
  baseurl_source: declared
  description: 'The current Eden AI gateway: OpenAI-compatible chat completions, responses, embeddings, moderations, images and audio, an Anthropic Messages pass-through, the model-routed Universal AI expert-model en'
  name: Eden AI API V3
  slug: eden-ai-v3-api
- baseURL: https://api.edenai.run/v2
  baseurl_source: declared
  description: 'Asynchronous video features on the legacy v2 surface — generation, deepfake detection, explicit-content, face/label/logo/object/person/shot-change/text detection and question answering. 45 operations '
  name: Eden AI Video API
  slug: eden-ai-video-api
- baseURL: https://api.edenai.run/v2
  baseurl_source: declared
  description: The legacy v2 LLM chat endpoint. Superseded by the OpenAI-compatible /v3/chat/completions on the v3 gateway.
  name: Eden AI LLM API (v2)
  slug: eden-ai-llm-api
- baseURL: https://api.edenai.run/v2
  baseurl_source: declared
  description: The legacy v2 multimodal chat endpoint, accepting mixed text and image input across providers.
  name: Eden AI Multimodal API
  slug: eden-ai-multimodal-api
- baseURL: https://api.edenai.run/v2
  baseurl_source: declared
  description: Create, list, update, rotate and delete custom API tokens, including sandbox tokens, and introspect the calling key. 8 operations. Eden AI documents v2 as supported for token management through end of
  name: Eden AI User Management API
  slug: eden-ai-user-management-api
- baseURL: https://api.edenai.run/v2
  baseurl_source: declared
  description: Aggregated consumption over time and current credit balance, for FinOps reporting against a multi-provider AI spend.
  name: Eden AI Cost Monitoring API
  slug: eden-ai-cost-monitoring-api
- baseURL: https://api.edenai.run/v3
  baseurl_source: declared
  description: 'The management plane: an issuer key mints scoped worker keys, worker keys mint, rotate and revoke inference keys, and manage-scoped reads cover members, IdP-synced groups and organization usage. 16 op'
  name: Eden AI Organization Management API
  slug: eden-ai-organization-management-api
artifact_total: 31
asyncapis:
- description: ''
  name: Eden Ai Webhooks
  slug: eden-ai-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Eden AI Audio API
  slug: open-eden-ai-audio-api
- collection_type: open
  name: Eden AI Audio Image API
  slug: open-eden-ai-image-api
- collection_type: open
  name: Eden AI Audio OCR API
  slug: open-eden-ai-ocr-api
- collection_type: open
  name: Eden AI Audio Text API
  slug: open-eden-ai-text-api
- collection_type: open
  name: Eden AI Audio Translation API
  slug: open-eden-ai-translation-api
- collection_type: open
  name: Eden AI API
  slug: open-eden-ai
common:
- group: company
  title: ''
  type: Website
  url: https://www.edenai.co/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eden-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/eden-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eden-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eden-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edenai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/edenai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.edenai.co/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.edenai.co/docs
- group: operate
  title: ''
  type: RateLimits
  url: https://www.edenai.co/docs/v3/overview/rate-limits
- group: company
  title: ''
  type: Blog
  url: https://www.edenai.co/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.edenai.co/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.edenai.co/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.edenai.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.edenai.co/docs/api-reference/chat/chat-completions
- group: start
  title: ''
  type: GettingStarted
  url: https://www.edenai.co/docs/v3/quickstart/first-llm-call
- group: operate
  title: ''
  type: Support
  url: https://help.edenai.co/en/
- group: start
  title: ''
  type: SignUp
  url: https://app.edenai.run/register
- group: operate
  title: ''
  type: StatusPage
  url: https://app-edenai.instatus.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.edenai.co/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eden-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eden-ai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/eden-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/eden-ai-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eden-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eden-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eden-ai-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/eden-ai-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eden-ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/eden-ai-trust-center.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/eden-ai-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/eden-ai-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eden-ai-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eden-ai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/eden-ai-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/eden-ai-finops.yml
created: '2025-02-09'
description: 'Eden AI is a French AI gateway that puts one API, one key and one invoice in front of 500+ AI models from 50+ providers. Its v3 surface is deliberately OpenAI-wire-compatible — chat completions, responses, embeddings, moderations, images and audio — with an Anthropic Messages pass-through alongside it, so existing SDK code moves over by swapping a base URL. A single model-routed Universal AI endpoint covers the expert models that are not LLMs: OCR and document parsing, image and video analysis, speech, translation, text analysis and web research, synchronously or as async jobs with signed webhooks. Routing, provider fallback, response caching, per-key budgets, guardrails and per-request cost reporting are built into the gateway, and an EU endpoint restricts processing to providers cleared for European data residency.'
finops:
- name: Eden Ai Finops
  service_category: API
  slug: eden-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eden-ai.png
layout: provider
mcp_servers:
- description: 'Eden AI publishes a hosted, remote Model Context Protocol server that exposes its expert-model catalog (OCR, web, image, text, translation, audio, video) as MCP tools, plus three utility tools. Every '
  name: Eden AI MCP Server
  slug: eden-ai-mcp-server
modified: '2026-09-06'
name: Eden AI
nav: Providers
network: true
overview: 'Eden AI publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Image API, OCR API, and 9 more. Tagged areas include Artificial Intelligence, AI Gateway, LLM, Machine Learning, and OCR.


  The Eden AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Eden AI''s developer surface includes authentication, pricing, documentation, engineering blog, API reference, getting-started guide, support, and 30 more developer resources.'
plans:
- name: Eden Ai Plans Pricing
  plan_count: 2
  slug: eden-ai-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Eden Ai Rate Limits
  slug: eden-ai-rate-limits
scopes:
- name: Eden Ai Scopes
  scope_count: 0
  slug: eden-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 59.0
    catalog_earned_first_party: 16.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 57.4
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/eden-ai/refs/heads/main/screenshots/eden-ai-2026-06-20T180450.png
security:
- kind: authentication
  name: Eden Ai Authentication
  slug: eden-ai-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Eden Ai Domain Security
  slug: eden-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Eden Ai Vulnerability Disclosure
  slug: eden-ai-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Eden Ai Trust Center
  slug: eden-ai-trust-center
  summary_line: GDPR, ISO/IEC 27001:2022, SOC 2 Type 2
slug: eden-ai
tags:
- Artificial Intelligence
- AI Gateway
- LLM
- Machine Learning
- OCR
- Translation
- Speech
- Computer Vision
- Model Context Protocol
- Emotion Detection
website: https://www.edenai.co/
---
