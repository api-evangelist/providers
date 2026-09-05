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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 31
  human_in_the_loop: 1
  name: Slng Agentic Access
  operation_count: 43
  slug: slng-agentic-access
  summary_line: 43 operations · 31 acting · 1 human-in-the-loop
api_count: 7
apis:
- baseURL: https://api.slng.ai
  baseurl_source: declared
  description: Inspect the authenticated account and organization.
  name: SLNG Account API
  slug: slng-account-api
- baseURL: https://api.slng.ai
  baseurl_source: declared
  description: Voice agent CRUD.
  name: SLNG Agents API
  slug: slng-agents-api
- baseURL: https://api.slng.ai
  baseurl_source: declared
  description: Call dispatch and status.
  name: SLNG Calls API
  slug: slng-calls-api
- baseURL: https://api.slng.ai
  baseurl_source: declared
  description: Discover and inspect available models in the SLNG catalog.
  name: SLNG Catalog API
  slug: slng-catalog-api
- baseURL: https://api.slng.ai
  baseurl_source: declared
  description: Deepgram Aura 2 for conversational voice agents.
  name: SLNG Deepgram Aura 2 API
  slug: slng-deepgram-aura-2-api
- baseURL: https://api.slng.ai
  baseurl_source: declared
  description: Deepgram Nova 3 with VAD and speaker diarization.
  name: SLNG Deepgram Nova 3 API
  slug: slng-deepgram-nova-3-api
- baseURL: https://api.slng.ai
  baseurl_source: declared
  description: Inworld Max 1.5 for multilingual, expressive synthesis.
  name: SLNG Inworld Max 1.5 API
  slug: slng-inworld-max-1-5-api
- baseURL: https://api.slng.ai
  baseurl_source: declared
  description: Orpheus TTS with emotion control.
  name: SLNG Orpheus English API
  slug: slng-orpheus-english-api
- baseURL: https://api.slng.ai
  baseurl_source: declared
  description: Manage reusable pronunciation rewrite dictionaries for TTS.
  name: SLNG Pronunciation dictionaries API
  slug: slng-pronunciation-dictionaries-api
- baseURL: https://api.slng.ai
  baseurl_source: declared
  description: Rime Arcana v2 TTS with multi-language support.
  name: SLNG Rime Arcana v2 API
  slug: slng-rime-arcana-v2-api
- baseURL: https://api.slng.ai
  baseurl_source: declared
  description: Rime Arcana v3 TTS with multilingual support (English, Hindi).
  name: SLNG Rime Arcana v3 API
  slug: slng-rime-arcana-v3-api
- baseURL: https://api.slng.ai
  baseurl_source: declared
  description: Rime Coda TTS for Bahasa Indonesian.
  name: SLNG Rime Coda API
  slug: slng-rime-coda-api
- baseURL: https://api.slng.ai
  baseurl_source: declared
  description: Web (non-telephony) sessions.
  name: SLNG Sessions API
  slug: slng-sessions-api
- baseURL: https://api.slng.ai
  baseurl_source: declared
  description: Create and manage asynchronous transcription jobs.
  name: SLNG Speechmatics API
  slug: slng-speechmatics-api
- baseURL: https://api.slng.ai
  baseurl_source: declared
  description: Whisper Large v3 with 99+ language support.
  name: SLNG Whisper Large v3 API
  slug: slng-whisper-large-v3-api
artifact_total: 53
asyncapis:
- description: SLNG Gateway API
  name: SLNG Gateway API - SLNG (WebSocket)
  slug: slng-slng-asyncapi
- description: SLNG Gateway API
  name: SLNG Gateway API - SLNG STT
  slug: slng-stt-slng-asyncapi
- description: SLNG Gateway API
  name: SLNG Gateway API - SLNG TTS
  slug: slng-tts-slng-asyncapi
collections:
- collection_type: postman
  name: SLNG Voice Agents Account API
  slug: postman-slng-account-api
- collection_type: postman
  name: SLNG Voice Account Agents API
  slug: postman-slng-agents-api
- collection_type: postman
  name: SLNG Voice Agents Account Calls API
  slug: postman-slng-calls-api
- collection_type: postman
  name: SLNG Voice Agents Account Catalog API
  slug: postman-slng-catalog-api
- collection_type: postman
  name: SLNG Voice Agents Account Deepgram Aura 2 API
  slug: postman-slng-deepgram-aura-2-api
- collection_type: postman
  name: SLNG Voice Agents Account Deepgram Nova 3 API
  slug: postman-slng-deepgram-nova-3-api
- collection_type: postman
  name: SLNG Voice Agents Account Inworld Max 1.5 API
  slug: postman-slng-inworld-max-1-5-api
- collection_type: postman
  name: SLNG Voice Agents Account Orpheus English API
  slug: postman-slng-orpheus-english-api
- collection_type: postman
  name: SLNG Voice Agents Account Pronunciation dictionaries API
  slug: postman-slng-pronunciation-dictionaries-api
- collection_type: postman
  name: SLNG Voice Agents Account Rime Arcana v2 API
  slug: postman-slng-rime-arcana-v2-api
- collection_type: postman
  name: SLNG Voice Agents Account Rime Arcana v3 API
  slug: postman-slng-rime-arcana-v3-api
- collection_type: postman
  name: SLNG Voice Agents Account Rime Coda API
  slug: postman-slng-rime-coda-api
- collection_type: postman
  name: SLNG Voice Agents Account Sessions API
  slug: postman-slng-sessions-api
- collection_type: postman
  name: SLNG Voice Agents Account Speechmatics API
  slug: postman-slng-speechmatics-api
- collection_type: postman
  name: SLNG Voice Agents Account Whisper Large v3 API
  slug: postman-slng-whisper-large-v3-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SLNG Voice Agents Account API
  slug: open-slng-account-api
- collection_type: open
  name: SLNG Voice Account Agents API
  slug: open-slng-agents-api
- collection_type: open
  name: SLNG Voice Agents Account Calls API
  slug: open-slng-calls-api
- collection_type: open
  name: SLNG Voice Agents Account Catalog API
  slug: open-slng-catalog-api
- collection_type: open
  name: SLNG Voice Agents Account Deepgram Aura 2 API
  slug: open-slng-deepgram-aura-2-api
- collection_type: open
  name: SLNG Voice Agents Account Deepgram Nova 3 API
  slug: open-slng-deepgram-nova-3-api
- collection_type: open
  name: SLNG Voice Agents Account Inworld Max 1.5 API
  slug: open-slng-inworld-max-1-5-api
- collection_type: open
  name: SLNG Voice Agents Account Orpheus English API
  slug: open-slng-orpheus-english-api
- collection_type: open
  name: SLNG Voice Agents Account Pronunciation dictionaries API
  slug: open-slng-pronunciation-dictionaries-api
- collection_type: open
  name: SLNG Voice Agents Account Rime Arcana v2 API
  slug: open-slng-rime-arcana-v2-api
- collection_type: open
  name: SLNG Voice Agents Account Rime Arcana v3 API
  slug: open-slng-rime-arcana-v3-api
- collection_type: open
  name: SLNG Voice Agents Account Rime Coda API
  slug: open-slng-rime-coda-api
- collection_type: open
  name: SLNG Voice Agents Account Sessions API
  slug: open-slng-sessions-api
- collection_type: open
  name: SLNG Voice Agents Account Speechmatics API
  slug: open-slng-speechmatics-api
- collection_type: open
  name: SLNG Voice Agents Account Whisper Large v3 API
  slug: open-slng-whisper-large-v3-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/slng/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.slng.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.slng.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.slng.ai/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.slng.ai/getting-started
- group: company
  title: ''
  type: Blog
  url: https://slng.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/slng-ai
- group: start
  title: ''
  type: SignUp
  url: https://app.slng.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://slng.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://slng.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://slng.ai/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@slng.ai
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/slng-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.slng.ai
- group: auth
  title: ''
  type: Compliance
  url: security/slng-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/slng-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slng-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/slng-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/slng-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/slng-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/slng-cli.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/slng-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/slng-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/slng-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/slng-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/slng-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/slng-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/slng-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/slng-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/slng-stt-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/slng-tts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/slng-agents-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/slng-batch-overlay.yaml
created: '2026-07-17'
description: SLNG is a compliance-first speech AI gateway that gives developers a single, unified API for speech-to-text, text-to-speech, and LLM-driven voice agents across 30+ models from providers like Deepgram, Rime, Cartesia, ElevenLabs, and OpenAI Whisper. The platform acts as an execution layer between an orchestrator and the models, routing each request to in-region compute across 60+ regions and 11 sovereign hubs for low latency and local data residency (GDPR), with ISO 27001 certification and HIPAA compliance. Every model is reachable over HTTP or streaming WebSocket, with bring-your-own-key billing, batch transcription, pronunciation dictionaries, and per-minute pricing. Founded in Barcelona in 2025 and backed by a pre-seed round led by Earlybird.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/slng.png
layout: provider
modified: '2026-07-21'
name: SLNG
nav: Providers
network: true
overview: 'SLNG publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Account API, Agents API, Calls API, and 12 more. Tagged areas include Company, Speech, Voice, Speech-to-Text, and Text-to-Speech.


  The SLNG catalog on APIs.io includes 3 event-driven AsyncAPI specifications.


  SLNG''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, pricing, support, and 27 more developer resources.'
random_paper: 16
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 70.3
    developer_ergonomics: 81.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 55.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/slng/refs/heads/main/screenshots/slng-2026-08-17T081926.png
security:
- kind: authentication
  name: Slng Authentication
  slug: slng-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Slng Domain Security
  slug: slng-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Slng Trust Center
  slug: slng-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: slng
tags:
- Company
- Speech
- Voice
- Speech-to-Text
- Text-to-Speech
- Voice AI
- Voice Agents
- Transcription
- Speech Recognition
- Artificial Intelligence
- API Gateway
website: https://docs.slng.ai
---
