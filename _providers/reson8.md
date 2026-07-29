---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Exchange an API key for a short-lived access token.
  name: Reson8 Auth API
  slug: reson8-auth-api
- description: Domain adaptation via custom phrase models.
  name: Reson8 Custom Models API
  slug: reson8-custom-models-api
- description: Realtime, turn-level, and prerecorded transcription.
  name: Reson8 Speech to Text API
  slug: reson8-speech-to-text-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reson8-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reson8.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.reson8.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reson8.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.reson8.dev/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.reson8.dev/
- group: company
  title: ''
  type: Blog
  url: https://www.reson8.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reson8labs
- group: start
  title: ''
  type: SignUp
  url: https://console.reson8.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reson8.dev/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reson8.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reson8.dev/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reson8.dev
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.reson8.dev/
- group: auth
  title: ''
  type: Authentication
  url: authentication/reson8-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reson8-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/reson8-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reson8-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reson8-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/reson8-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/reson8-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/reson8-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reson8-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/reson8-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/reson8-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reson8-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/reson8-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Reson8 (Resonate Labs B.V.) is a Balderton Capital-backed speech-recognition company offering an infrastructure-grade automatic speech recognition (ASR) API. Its differentiator is text-based, hyper-custom domain adaptation: feed up to ~1M tokens of domain vocabulary and a custom model adapts in under 60 seconds with no audio datasets or fine-tuning, cutting word error rate versus generic engines. The v1 API at api.reson8.dev provides realtime WebSocket streaming, turn-level events for conversational voice agents, prerecorded file transcription, speaker diarization, and custom-model phrase management across ten European languages, on EU-hosted infrastructure with zero audio retention.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reson8.png
layout: provider
mcp_servers:
- description: ''
  name: reson8-mcp.yml
  slug: reson8-mcpyml
modified: '2026-07-20'
name: Reson8
nav: Providers
network: true
overview: 'Reson8 publishes 3 APIs on the [APIs.io](https://apis.io/) network: Auth API, Custom Models API, and Speech to Text API. Tagged areas include Speech Recognition, Speech-to-Text, ASR, Voice AI, and Transcription.


  Reson8''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, pricing, authentication, and 21 more developer resources.'
random_paper: 47
score:
  band: developing
  composite: 51.2
  delta: -1.5
  facets:
    commercial_clarity: 52.6
    contract_quality: 62.7
    developer_ergonomics: 58.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 52.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Reson8 Authentication
  slug: reson8-authentication
  summary_line: apiKey/http-bearer · 3 schemes
- kind: domain-security
  name: Reson8 Domain Security
  slug: reson8-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Reson8 Trust Center
  slug: reson8-trust-center
  summary_line: trust center published
slug: reson8
tags:
- Speech Recognition
- Speech-to-Text
- ASR
- Voice AI
- Transcription
- Diarization
- Machine Learning
- Developers
website: https://www.reson8.dev/
---
