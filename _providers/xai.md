---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Xai Agentic Access
  operation_count: 33
  slug: xai-agentic-access
  summary_line: 33 operations · 16 acting
api_count: 1
apis:
- description: The v1 API from xAI — 30 operation(s) for v1.
  name: xAI v1 API
  slug: xai-v1-api
artifact_total: 12
asyncapis:
- description: 'AsyncAPI 2.6 description of xAI''s documented WebSocket APIs: - Real-time Speech-to-Text (STT) streaming at wss://api.x.ai/v1/stt - Voice Agent (bidirectional speech-to-speech) at wss://api.x.ai/v1/rea'
  name: xAI Realtime WebSocket APIs
  slug: xai-asyncapi
collections:
- collection_type: open
  name: xAI's REST API
  slug: open-xai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/xai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/xai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xai-org
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/x-ai
- group: company
  title: ''
  type: Website
  url: https://x.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.x.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/xai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/xai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/xai-finops.yml
created: '2026-05-08'
description: xAI is an AI research lab founded by Elon Musk. The xAI API exposes Grok foundation models for chat, function calling, vision, voice, image generation, and video generation, alongside research outputs from the Colossus training supercluster.
finops:
- name: Xai Finops
  service_category: AI and Machine Learning
  slug: xai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xai.png
layout: provider
modified: '2026-05-29'
name: xAI
nav: Providers
network: true
overview: 'xAI publishes 1 API on the [APIs.io](https://apis.io/) network: v1 API. Tagged areas include AI, LLM, Foundation Models, Grok, and Generative AI.


  The xAI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  xAI''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Xai Plans Pricing
  plan_count: 3
  slug: xai-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 3
  name: Xai Rate Limits
  slug: xai-rate-limits
rules:
- name: xAI API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: xai-asyncapi-spectral-rules
score:
  band: developing
  composite: 44.2
  delta: -4.4
  facets:
    commercial_clarity: 47.4
    contract_quality: 56.5
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xai/refs/heads/main/screenshots/xai-2026-06-20T201651.png
security:
- kind: authentication
  name: Xai Authentication
  slug: xai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Xai Domain Security
  slug: xai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Xai Vulnerability Disclosure
  slug: xai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Xai Trust Center
  slug: xai-trust-center
  summary_line: HIPAA, GDPR
slug: xai
tags:
- AI
- LLM
- Foundation Models
- Grok
- Generative AI
website: https://x.ai/
---
