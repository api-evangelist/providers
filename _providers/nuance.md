---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
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
  href: https://artifacts.apis.io/nuance/hosts/nuance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nuance-hosts.yml
- group: build
  href: https://artifacts.apis.io/nuance/integrations/nuance-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/nuance-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/nuance/vendors/nuance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nuance-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dragon.nuance.com/en-us/privacy-policies.html
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/microsoft/
- group: auth
  href: https://artifacts.apis.io/nuance/security/nuance-domain-security.yml
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
  href: https://artifacts.apis.io/nuance/authentication/nuance-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nuance-authentication.yml
- group: build
  href: https://artifacts.apis.io/nuance/packages/nuance-packages.yml
  title: ''
  type: Packages
  url: packages/nuance-packages.yml
- group: build
  href: https://artifacts.apis.io/nuance/packages/nuance-packages.yml
  title: ''
  type: SDKs
  url: packages/nuance-packages.yml
- group: build
  href: https://artifacts.apis.io/nuance/cli/nuance-cli.yml
  title: ''
  type: CLI
  url: cli/nuance-cli.yml
- group: design
  href: https://artifacts.apis.io/nuance/conventions/nuance-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nuance-conventions.yml
- group: design
  href: https://artifacts.apis.io/nuance/conformance/nuance-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nuance-conformance.yml
- group: agent
  href: https://artifacts.apis.io/nuance/mcp/nuance-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nuance-mcp.yml
created: '2026-07-17'
description: 'Nuance Communications (NASDAQ: NUAN) is a conversational-AI and speech-recognition pioneer, acquired by Microsoft in 2022. Its self-service developer platform, Nuance Mix, provides tooling and runtime services for building conversational applications: Automatic Speech Recognition (ASRaaS), Natural Language Understanding (NLUaaS), Dialog management (DLGaaS), Text-to-Speech (TTSaaS) and grammar-based recognition (NRaaS) — all exposed as gRPC/protobuf runtime services secured with OAuth 2.0 client-credentials. Design-time tooling (Mix.nlu, Mix.dialog) and a first-party CLI (@nuance-mix/mix-cli) round out the platform. Nuance also ships Dragon speech solutions, including Dragon Medical SpeechKit for healthcare voice capture.'
image: https://github.com/nuance-communications.png
layout: provider
modified: '2026-07-20'
name: Nuance
nav: Providers
network: true
overview: 'Nuance is listed with 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Speech Recognition, Conversational AI, Natural Language Understanding, and Text-to-Speech.


  Nuance''s developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, CLI, and 14 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.6
  facets:
    access_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 85.7
    operational_transparency: 2.6
  previous_composite: 25.1
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nuance/nuance-2026-08-07T185712.png
security:
- kind: authentication
  name: Nuance Authentication
  slug: nuance-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Nuance Domain Security
  slug: nuance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
