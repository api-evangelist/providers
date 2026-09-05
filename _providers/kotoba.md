---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Kotoba Agentic Access
  operation_count: 2
  slug: kotoba-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 4
apis:
- baseURL: https://api.kotobatech.ai
  baseurl_source: declared
  description: The transcriptionApi API from Kotoba — 2 operation(s) for transcriptionapi.
  name: Kotoba transcriptionApi API
  slug: kotoba-transcriptionapi-api
artifact_total: 10
asyncapis:
- description: ''
  name: Live (WebSocket)
  slug: kotoba-asr-asyncapi
- description: ''
  name: Live (WebSocket)
  slug: kotoba-sts-asyncapi
- description: ''
  name: Live (WebSocket)
  slug: kotoba-tts-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Live (WebSocket) transcriptionApi API
  slug: open-kotoba-transcriptionapi-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/kotoba-tech/kotoba-python/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/kotoba-tech/kotoba-python/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/kotoba-tech/kotoba-python/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://kotoba.tech/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kotoba.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kotoba.tech/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kotoba.tech/s2t/streaming/asr/asr
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kotoba.tech/overview/introduction
- group: operate
  title: ''
  type: Support
  url: https://site.kotoba.tech/contact
- group: start
  title: ''
  type: SignUp
  url: https://app.kotoba.tech/
- group: start
  title: ''
  type: Login
  url: https://app.kotoba.tech/
- group: company
  title: ''
  type: Blog
  url: https://site.kotoba.tech/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dashboard.kotobatech.ai/terms_en.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dashboard.kotobatech.ai/privacy_en.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kotoba-tech
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/kotoba-tech/kotoba-python
- group: other
  title: ''
  type: X
  url: https://x.com/kotoba_tech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kotoba-tech/
- group: auth
  title: ''
  type: Authentication
  url: authentication/kotoba-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/kotoba-transcription-openapi-original.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/kotoba-asr-asyncapi.yml
- group: build
  title: ''
  type: Packages
  url: packages/kotoba-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kotoba-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kotoba-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kotoba-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kotoba-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kotoba-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kotoba-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kotoba-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kotoba-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kotoba-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kotoba-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kotoba-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/kotoba-transcription-overlay.yaml
created: '2026-07-17'
description: Kotoba Technologies is a Japan-founded frontier voice AI company building a foundational real-time speech model and simultaneous translation technology. Its developer platform exposes three JSON-over-WebSocket realtime capabilities — ASR (automatic speech recognition with live transcript deltas), STS (speech-to-speech translation that emits both a source transcript and synthesized target-language audio over one connection), and TTS (streaming text-to-speech) — alongside a REST transcription API for batch and offline workflows built on a submit-and-poll job model. Supported languages span English, Japanese, Korean, Chinese and Spanish. Each realtime channel is described by a published AsyncAPI 2.6.0 document and each REST surface by OpenAPI 3.1, with a first-party Python SDK, an llms.txt agent index, and a live remote MCP documentation server. The APIs are in private alpha, available to selected customers on request.
image: https://framerusercontent.com/images/7OW09ZoQn6c3oPwAHQgP3DCXI.png
layout: provider
mcp_servers:
- description: ''
  name: Kotoba MCP Server
  slug: kotoba-mcp-server
modified: '2026-07-19'
name: Kotoba
nav: Providers
network: true
overview: 'Kotoba publishes 1 API on the [APIs.io](https://apis.io/) network: transcriptionApi API. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Voice, and Speech Recognition.


  The Kotoba catalog on APIs.io includes 3 event-driven AsyncAPI specifications.


  Kotoba''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, engineering blog, authentication, and 28 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 57.7
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 25.0
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kotoba/refs/heads/main/screenshots/kotoba-2026-07-25T224316.png
security:
- kind: authentication
  name: Kotoba Authentication
  slug: kotoba-authentication
  summary_line: http/client-secret · 3 schemes
- kind: domain-security
  name: Kotoba Domain Security
  slug: kotoba-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kotoba
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Voice
- Speech Recognition
- Speech-to-Text
- Text-to-Speech
- Translation
- Real-Time
- WebSockets
- Audio
- Transcription
website: https://kotoba.tech/
---
