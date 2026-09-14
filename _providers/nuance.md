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
api_count: 5
apis:
- description: 'Automatic Speech Recognition as a Service — convert speech to text in real time over a gRPC streaming API (Recognizer service), with wordsets, training and ForgetMe operations. Secured with OAuth 2.0 '
  name: Nuance Mix ASRaaS gRPC API
  slug: nuance-mix-asraas-grpc-api
- description: Natural Language Understanding as a Service — interpret user input against NLU models built in Mix.nlu, over a gRPC Runtime service.
  name: Nuance Mix NLUaaS gRPC API
  slug: nuance-mix-nluaas-grpc-api
- description: Dialog as a Service — execute conversational dialog flows authored in Mix.dialog over a gRPC Dialog service.
  name: Nuance Mix DLGaaS gRPC API
  slug: nuance-mix-dlgaas-grpc-api
- description: Text-to-Speech as a Service — turn text into synthesized speech (including neural voices) over a gRPC Synthesizer service.
  name: Nuance Mix TTSaaS gRPC API
  slug: nuance-mix-ttsaas-grpc-api
- description: Grammar-based recognition as a Service — grammar-driven speech recognition over a gRPC runtime service.
  name: Nuance Mix NRaaS gRPC API
  slug: nuance-mix-nraas-grpc-api
artifact_total: 7
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/microsoft/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nuance.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mix.nuance.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nuance.com/mix/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nuance.com/mix/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/nuance-communications/mix-quickstart-projects
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nuance-communications
- group: start
  title: ''
  type: SignUp
  url: https://mix.nuance.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/nuance-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/nuance-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nuance-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/nuance-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nuance-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nuance-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nuance-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nuance-llms.txt
created: '2026-07-17'
description: 'Nuance Communications (NASDAQ: NUAN) is a conversational-AI and speech-recognition pioneer, acquired by Microsoft in 2022. Its self-service developer platform, Nuance Mix, provides tooling and runtime services for building conversational applications: Automatic Speech Recognition (ASRaaS), Natural Language Understanding (NLUaaS), Dialog management (DLGaaS), Text-to-Speech (TTSaaS) and grammar-based recognition (NRaaS) — all exposed as gRPC/protobuf runtime services secured with OAuth 2.0 client-credentials. Design-time tooling (Mix.nlu, Mix.dialog) and a first-party CLI (@nuance-mix/mix-cli) round out the platform. Nuance also ships Dragon speech solutions, including Dragon Medical SpeechKit for healthcare voice capture.'
image: https://github.com/nuance-communications.png
layout: provider
modified: '2026-07-20'
name: Nuance
nav: Providers
network: true
overview: 'Nuance publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Speech Recognition, Conversational AI, Natural Language Understanding, and Text-to-Speech.


  Nuance''s developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, CLI, and 11 more developer resources.'
random_paper: 4
screenshot: https://raw.githubusercontent.com/api-evangelist/nuance/refs/heads/main/screenshots/nuance-2026-08-07T185712.png
security:
- kind: authentication
  name: Nuance Authentication
  slug: nuance-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Nuance Domain Security
  slug: nuance-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: nuance
tags:
- Company
- Speech Recognition
- Conversational AI
- Natural Language Understanding
- Text-to-Speech
- Speech Synthesis
- Voice
- Dialog
- gRPC
- Healthcare AI
website: https://www.nuance.com
---
