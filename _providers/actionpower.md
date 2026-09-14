---
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Actionpower Agentic Access
  operation_count: 40
  slug: actionpower-agentic-access
  summary_line: 40 operations · 28 acting
api_count: 2
apis:
- baseURL: https://apis.daglo.ai
  baseurl_source: declared
  description: REST API for ActionPower's speech and language stack, served at https://apis.daglo.ai and authenticated with a bearer API token issued from the daglo Developers console. The published production contr
  name: daglo Cloud API
  slug: daglo-cloud-api
- description: Bidirectional gRPC streaming speech recognition served from apis.daglo.ai. The provider publishes the proto3 service definition (package dagloapis.speech.v1, rpc StreamingRecognize) in its developer g
  name: daglo Realtime Streaming STT (gRPC)
  slug: daglo-realtime-streaming-stt-grpc
artifact_total: 8
asyncapis:
- description: ''
  name: Actionpower Daglo Webhooks
  slug: actionpower-daglo-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/actionpower-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://daglo.ai/
- group: company
  title: ''
  type: Website
  url: https://actionpower.kr/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.daglo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.daglo.ai/guide/en/
- group: docs
  title: ''
  type: APIReference
  url: https://apis.daglo.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.daglo.ai/guide/en/Quick-Speech-Voice-To-Text.html
- group: operate
  title: ''
  type: Support
  url: https://developers.daglo.ai/guide/en/FAQ.html
- group: company
  title: ''
  type: Blog
  url: https://daglo.ai/d/ko/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://daglo.ai/d/ko/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/actionpower
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.daglo.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://daglo.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://developers.daglo.ai/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://daglo.ai/d/en/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://daglo.ai/d/en/legal/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://daglo.ai/d/en/enterprise
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/actionpower-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/actionpower-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/actionpower-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/actionpower-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/actionpower-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/actionpower-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/actionpower-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/actionpower-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/actionpower-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/actionpower-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/actionpower-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/actionpower-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/actionpower-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/actionpower-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/actionpower-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/actionpower-daglo-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/actionpower-speech.proto
- group: build
  title: ''
  type: Examples
  url: examples/actionpower-daglo-examples.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/actionpower-daglo-cloud-api-overlay.yaml
created: '2026-09-06'
description: 'ActionPower Corp. (주식회사 액션파워) is a Seoul-based deep-tech AI company founded in 2016 that builds its own end-to-end speech recognition, speaker diarization, speech synthesis and small-language-model stack, and sells it two ways: as daglo, a voice-intelligence workspace that records, transcribes, summarizes and translates meetings, calls and lectures for more than two million users; and as the daglo Cloud API, a developer platform at apis.daglo.ai offering synchronous and asynchronous speech-to-text, bidirectional-streaming realtime STT over gRPC, chat completion, dialogue summarization, meeting minutes, paragraph splitting and text-to-speech. The company is ISO 27001 certified, ships an on-premise closed-network deployment for public sector, finance, healthcare and broadcast customers, and reports customers including LG Electronics, KT Skylife, NH Nonghyup Bank and the Daegu Metropolitan Government.'
image: https://daglo.ai/d/og-image
layout: provider
modified: '2026-09-06'
name: Actionpower
nav: Providers
network: true
overview: 'Actionpower publishes 1 API on the [APIs.io](https://apis.io/) network: daglo Cloud API. Tagged areas include Speech Recognition, Speech To Text, Text To Speech, Natural Language Processing, and Artificial Intelligence.


  The Actionpower catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Actionpower''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Actionpower Plans Pricing
  plan_count: 3
  slug: actionpower-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Actionpower Rate Limits
  slug: actionpower-rate-limits
security:
- kind: authentication
  name: Actionpower Authentication
  slug: actionpower-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Actionpower Domain Security
  slug: actionpower-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: actionpower
tags:
- Speech Recognition
- Speech To Text
- Text To Speech
- Natural Language Processing
- Artificial Intelligence
- Transcription
- Voice
- Meeting Intelligence
- gRPC
- South Korea
website: https://daglo.ai/
---
