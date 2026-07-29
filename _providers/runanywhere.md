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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Hosted control plane the RunAnywhere SDKs talk to for model delivery, extraction, versioning, and configuration. Authenticated with an API key supplied at SDK initialization. No public OpenAPI is publ
  name: RunAnywhere Control Plane API
  slug: runanywhere-control-plane-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runanywhere-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.runanywhere.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.runanywhere.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runanywhere.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.runanywhere.ai/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RunanywhereAI
- group: company
  title: ''
  type: Blog
  url: https://www.runanywhere.ai/blog
- group: start
  title: ''
  type: Login
  url: https://runanywhere-frontend-production.up.railway.app/login
- group: operate
  title: ''
  type: Support
  url: mailto:san@runanywhere.ai
- group: build
  title: ''
  type: Packages
  url: packages/runanywhere-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/runanywhere-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/runanywhere-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/runanywhere-llms.txt
created: '2026-07-17'
description: RunAnywhere is a Y Combinator (W2026) infrastructure company building the layer for deploying fast, private, multimodal AI on-device at scale. It ships one open-source C++ core runtime with native bindings for Swift, Kotlin, React Native, Flutter, and the browser, plus hand-written GPU/NPU inference engines (MetalRT for Apple GPUs, QHexRT for Qualcomm Hexagon NPUs) that run LLM, VLM, speech-to-text, text-to-speech, and embedding workloads locally. The SDKs handle model delivery, extraction, storage management, versioning, and observability, and support hybrid routing that tries on-device inference first before optionally falling back to the cloud. A hosted control plane (api.runanywhere.ai) manages model delivery and configuration via API key.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/runanywhere.png
layout: provider
modified: '2026-07-21'
name: RunAnywhere
nav: Providers
network: true
overview: 'RunAnywhere publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, On-Device AI, Inference, Machine Learning, and SDK.


  RunAnywhere''s developer surface includes documentation, getting-started guide, engineering blog, support, CLI, and 8 more developer resources.'
random_paper: 74
score:
  band: emerging
  composite: 21.6
  delta: -0.5
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 22.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Runanywhere Domain Security
  slug: runanywhere-domain-security
  summary_line: TLSv1.2 · HSTS
slug: runanywhere
tags:
- Company
- On-Device AI
- Inference
- Machine Learning
- SDK
- Mobile
- Edge AI
- LLM
- Speech
- Y Combinator
website: https://www.runanywhere.ai/
---
