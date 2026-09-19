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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.9
  scored_at: '2026-09-18'
agentic_access:
- acting_count: 40
  human_in_the_loop: 0
  name: Elevenlabs Agentic Access
  operation_count: 62
  slug: elevenlabs-agentic-access
  summary_line: 62 operations · 40 acting
api_count: 11
apis:
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: The complete ElevenLabs REST API as the provider publishes it — one OpenAPI 3.1.0 document covering 301 paths and 390 operations across ElevenCreative (text to speech, speech to text, voice changer, v
  name: ElevenLabs API
  slug: elevenlabs-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for creating, managing, and configuring conversational AI agents with voice capabilities.
  name: elevenlabs Agents API
  slug: elevenlabs-agents-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for isolating vocals from background noise in audio recordings.
  name: elevenlabs Audio Isolation API
  slug: elevenlabs-audio-isolation-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for creating and managing Audio Native embedded players for web content.
  name: elevenlabs Audio Native API
  slug: elevenlabs-audio-native-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for managing chapters within Studio projects.
  name: elevenlabs Chapters API
  slug: elevenlabs-chapters-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for retrieving and managing conversation sessions and their associated data.
  name: elevenlabs Conversations API
  slug: elevenlabs-conversations-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for creating, managing, and retrieving dubbed audio and video content across languages.
  name: elevenlabs Dubbing API
  slug: elevenlabs-dubbing-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for managing individual dubbing resources including segments, translations, and dubbed output files.
  name: elevenlabs Dubbing Resources API
  slug: elevenlabs-dubbing-resources-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for creating voice clones from short audio samples with instant processing.
  name: elevenlabs Instant Voice Cloning API
  slug: elevenlabs-instant-voice-cloning-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for managing knowledge base documents that agents use to answer questions.
  name: elevenlabs Knowledge Base API
  slug: elevenlabs-knowledge-base-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for generating music from text prompts using AI models.
  name: elevenlabs Music Generation API
  slug: elevenlabs-music-generation-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for creating high-fidelity voice clones from longer audio recordings with professional-grade processing.
  name: elevenlabs Professional Voice Cloning API
  slug: elevenlabs-professional-voice-cloning-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for managing Studio projects including creation, editing, and rendering of long-form audio content.
  name: elevenlabs Projects API
  slug: elevenlabs-projects-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for managing pronunciation dictionaries used in Studio projects.
  name: elevenlabs Pronunciation Dictionaries API
  slug: elevenlabs-pronunciation-dictionaries-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for generating sound effects from text descriptions using AI models.
  name: elevenlabs Sound Effects API
  slug: elevenlabs-sound-effects-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for converting speech from one voice to another while preserving the original speech characteristics.
  name: elevenlabs Speech to Speech API
  slug: elevenlabs-speech-to-speech-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for converting audio into text transcriptions with support for multiple languages and audio formats.
  name: elevenlabs Speech to Text API
  slug: elevenlabs-speech-to-text-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for converting text scripts with multiple speakers into dialogue audio.
  name: elevenlabs Text to Dialogue API
  slug: elevenlabs-text-to-dialogue-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for converting text into speech audio with configurable voice, model, and output format settings.
  name: elevenlabs Text to Speech API
  slug: elevenlabs-text-to-speech-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for managing external tools and webhook integrations that agents can invoke during conversations.
  name: elevenlabs Tools API
  slug: elevenlabs-tools-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for browsing and adding shared voices from the public voice library.
  name: elevenlabs Voice Library API
  slug: elevenlabs-voice-library-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for managing voice-specific settings such as stability, similarity boost, and style parameters.
  name: elevenlabs Voice Settings API
  slug: elevenlabs-voice-settings-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for managing voices including listing, creating, editing, and deleting voices in the library.
  name: elevenlabs Voices API
  slug: elevenlabs-voices-api
artifact_total: 156
asyncapis:
- description: The ElevenLabs Conversational AI WebSocket API enables real-time, interactive voice conversations with AI agents. It supports bidirectional audio streaming, text events, and conversation lifecycle man
  name: ElevenLabs Conversational AI Events
  slug: elevenlabs-conversational-ai-asyncapi
- description: The ElevenLabs Text to Speech WebSocket API enables bidirectional streaming for text-to-speech conversion. Clients send text chunks incrementally and receive audio chunks as they are generated, enabli
  name: ElevenLabs Text to Speech Streaming Events
  slug: elevenlabs-text-to-speech-streaming-asyncapi
- description: The ElevenLabs Webhook system delivers event notifications to configured endpoints when specific actions occur within the platform. This includes post-call webhooks from Conversational AI conversation
  name: ElevenLabs Webhook Events
  slug: elevenlabs-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ElevenLabs Audio Isolation Agents API
  slug: open-elevenlabs-agents-api
- collection_type: open
  name: ElevenLabs Agents Audio Isolation API
  slug: open-elevenlabs-audio-isolation-api
- collection_type: open
  name: ElevenLabs Audio Isolation API
  slug: open-elevenlabs-audio-isolation
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Audio Native API
  slug: open-elevenlabs-audio-native-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Chapters API
  slug: open-elevenlabs-chapters-api
- collection_type: open
  name: ElevenLabs Conversational AI API
  slug: open-elevenlabs-conversational-ai
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Conversations API
  slug: open-elevenlabs-conversations-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Dubbing API
  slug: open-elevenlabs-dubbing-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Dubbing Resources API
  slug: open-elevenlabs-dubbing-resources-api
- collection_type: open
  name: ElevenLabs Dubbing API
  slug: open-elevenlabs-dubbing
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Instant Voice Cloning API
  slug: open-elevenlabs-instant-voice-cloning-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Knowledge Base API
  slug: open-elevenlabs-knowledge-base-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Music Generation API
  slug: open-elevenlabs-music-generation-api
- collection_type: open
  name: ElevenLabs Music Generation API
  slug: open-elevenlabs-music
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Professional Voice Cloning API
  slug: open-elevenlabs-professional-voice-cloning-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Projects API
  slug: open-elevenlabs-projects-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Pronunciation Dictionaries API
  slug: open-elevenlabs-pronunciation-dictionaries-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Sound Effects API
  slug: open-elevenlabs-sound-effects-api
- collection_type: open
  name: ElevenLabs Sound Effects API
  slug: open-elevenlabs-sound-effects
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Speech to Speech API
  slug: open-elevenlabs-speech-to-speech-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Speech to Text API
  slug: open-elevenlabs-speech-to-text-api
- collection_type: open
  name: ElevenLabs Speech to Text API
  slug: open-elevenlabs-speech-to-text
- collection_type: open
  name: ElevenLabs Studio API
  slug: open-elevenlabs-studio
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Text to Dialogue API
  slug: open-elevenlabs-text-to-dialogue-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Text to Speech API
  slug: open-elevenlabs-text-to-speech-api
- collection_type: open
  name: ElevenLabs Text to Speech API
  slug: open-elevenlabs-text-to-speech
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Tools API
  slug: open-elevenlabs-tools-api
- collection_type: open
  name: ElevenLabs Voice Changer API
  slug: open-elevenlabs-voice-changer
- collection_type: open
  name: ElevenLabs Voice Cloning API
  slug: open-elevenlabs-voice-cloning
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Voice Library API
  slug: open-elevenlabs-voice-library-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Voice Settings API
  slug: open-elevenlabs-voice-settings-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Voices API
  slug: open-elevenlabs-voices-api
- collection_type: open
  name: ElevenLabs Voices API
  slug: open-elevenlabs-voices
common:
- group: company
  title: ''
  type: Website
  url: https://www.elevenlabs.io/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/agentic-access/elevenlabs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/elevenlabs-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/security/elevenlabs-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/elevenlabs-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/security/elevenlabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elevenlabs-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/authentication/elevenlabs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/elevenlabs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elevenlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elevenlabsio
- group: company
  title: ''
  type: Blog
  url: https://elevenlabs.io/blog
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/json-ld/elevenlabs-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/elevenlabs-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/json-schema/elevenlabs-voice-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/elevenlabs-voice-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/json-schema/elevenlabs-agent-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/elevenlabs-agent-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/json-schema/elevenlabs-webhook-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/elevenlabs-webhook-event-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://elevenlabs.io/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://elevenlabs.io/docs/overview/intro
- group: start
  title: ''
  type: DeveloperPortal
  url: https://elevenlabs.io/api
- group: docs
  title: ''
  type: APIReference
  url: https://elevenlabs.io/docs/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://elevenlabs.io/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://elevenlabs.io/docs/help-center/help-center-directory
- group: commercial
  title: ''
  type: Pricing
  url: https://elevenlabs.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://elevenlabs.io/app/sign-up
- group: start
  title: ''
  type: Login
  url: https://elevenlabs.io/app/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://elevenlabs.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://elevenlabs.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.elevenlabs.io/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/lifecycle/elevenlabs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/elevenlabs-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/lifecycle/elevenlabs-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/elevenlabs-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/changelog/elevenlabs-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/elevenlabs-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/security/elevenlabs-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/elevenlabs-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/well-known/elevenlabs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/elevenlabs-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/well-known/elevenlabs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elevenlabs-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/well-known/elevenlabs-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/elevenlabs-api-catalog.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/security/elevenlabs-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/elevenlabs-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/conformance/elevenlabs-conformance.yml
  title: ''
  type: Compliance
  url: conformance/elevenlabs-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/conformance/elevenlabs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/elevenlabs-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/packages/elevenlabs-packages.yml
  title: ''
  type: Packages
  url: packages/elevenlabs-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/packages/elevenlabs-packages.yml
  title: ''
  type: SDKs
  url: packages/elevenlabs-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/cli/elevenlabs-cli.yml
  title: ''
  type: CLI
  url: cli/elevenlabs-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/components/elevenlabs-components.yml
  title: ''
  type: Components
  url: components/elevenlabs-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/data-model/elevenlabs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/elevenlabs-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/conventions/elevenlabs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/elevenlabs-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/errors/elevenlabs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/elevenlabs-problem-types.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/scopes/elevenlabs-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/elevenlabs-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/mcp/elevenlabs-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/elevenlabs-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/mcp/elevenlabs-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/elevenlabs-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/llms/elevenlabs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elevenlabs-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/overlays/elevenlabs-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elevenlabs-openapi-overlay.yaml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/plans/elevenlabs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elevenlabs-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/rate-limits/elevenlabs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/elevenlabs-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/finops/elevenlabs-finops.yml
  title: ''
  type: FinOps
  url: finops/elevenlabs-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/vocabulary/elevenlabs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/elevenlabs-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/rules/elevenlabs-asyncapi-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/elevenlabs-asyncapi-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/rules/elevenlabs-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/elevenlabs-jsonschema-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/asyncapi/elevenlabs-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/elevenlabs-webhooks-asyncapi.yml
created: '2026-05-04'
description: 'ElevenLabs is an AI research and product company building voice and audio models, founded in 2022 and launched publicly in January 2023 with the first human-like AI voice model. It sells across three platforms: ElevenCreative (text to speech, speech to text, voice cloning and design, music, sound effects, dubbing, Studio, image and video across 70+ languages), ElevenAgents (an enterprise platform for voice and chat agents with telephony, testing, evaluation and analytics), and ElevenAPI (direct developer access to the audio foundation models over HTTP and WebSocket). It publishes a single first-party OpenAPI 3.1.0 covering 390 operations, official SDKs for Python, JavaScript, React, React Native, Swift, Kotlin and Flutter, a Rust CLI, a hosted remote MCP server with four data-residency endpoints, and ten Agent Skills of its own.'
features:
- 'Free: 10k credits/mo with TTS/STT/Sound effects'
- 'Starter at $6/mo: 30k credits, commercial license, IVC'
- 'Creator at $11/mo: 121k credits, Professional Voice Cloning'
- 'Pro at $99/mo: 600k credits, 44.1kHz PCM'
- 'Scale at $299/mo: 1.8M credits, team collaboration'
- 'Business at $990/mo: 6M credits, low-latency TTS at 5c/min'
- 'Enterprise custom: HIPAA BAA, SSO, custom concurrency'
- 'Concurrent: 2 Free, 3 Starter, 5 Creator, 10 Pro, 15 Scale/Business'
- TTS API with multilingual voices
- STT (Scribe) API
- Dubbing API for video translation
- Voice cloning (Instant + Professional)
- Sound Effects generation
- Music generation
- Conversational AI (voice agents)
- WebSocket streaming for low-latency synthesis
finops:
- name: Elevenlabs Finops
  service_category: Voice AI
  slug: elevenlabs-finops
graphqls:
- description: 'title: ElevenLabs GraphQL Schema'
  name: ElevenLabs GraphQL Schema
  slug: elevenlabs-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elevenlabs.png
json_schemas:
- name: AddKnowledgeBaseRequest
  property_count: 3
  slug: elevenlabs-addknowledgebaserequest
- name: AddVoiceRequest
  property_count: 4
  slug: elevenlabs-addvoicerequest
- name: AddVoiceResponse
  property_count: 1
  slug: elevenlabs-addvoiceresponse
- name: ElevenLabs Conversational AI Agent
  property_count: 7
  slug: elevenlabs-agent
- name: AgentListResponse
  property_count: 3
  slug: elevenlabs-agentlistresponse
- name: AgentResponse
  property_count: 1
  slug: elevenlabs-agentresponse
- name: AgentSummary
  property_count: 3
  slug: elevenlabs-agentsummary
- name: AsyncTranscriptionResponse
  property_count: 2
  slug: elevenlabs-asynctranscriptionresponse
- name: AudioEvent
  property_count: 3
  slug: elevenlabs-audioevent
- name: AudioIsolationRequest
  property_count: 1
  slug: elevenlabs-audioisolationrequest
- name: AudioNativeResponse
  property_count: 2
  slug: elevenlabs-audionativeresponse
- name: Chapter
  property_count: 5
  slug: elevenlabs-chapter
- name: ChapterListResponse
  property_count: 1
  slug: elevenlabs-chapterlistresponse
- name: ChapterSummary
  property_count: 3
  slug: elevenlabs-chaptersummary
- name: Conversation
  property_count: 6
  slug: elevenlabs-conversation
- name: ConversationConfig
  property_count: 4
  slug: elevenlabs-conversationconfig
- name: ConversationListResponse
  property_count: 3
  slug: elevenlabs-conversationlistresponse
- name: ConversationSummary
  property_count: 5
  slug: elevenlabs-conversationsummary
- name: CreateAgentRequest
  property_count: 3
  slug: elevenlabs-createagentrequest
- name: CreateAudioNativeRequest
  property_count: 7
  slug: elevenlabs-createaudionativerequest
- name: CreateDubbingRequest
  property_count: 7
  slug: elevenlabs-createdubbingrequest
- name: CreateProjectRequest
  property_count: 5
  slug: elevenlabs-createprojectrequest
- name: CreateToolRequest
  property_count: 5
  slug: elevenlabs-createtoolrequest
- name: DialogueSegment
  property_count: 3
  slug: elevenlabs-dialoguesegment
- name: DubbingMetadata
  property_count: 6
  slug: elevenlabs-dubbingmetadata
- name: DubbingResource
  property_count: 3
  slug: elevenlabs-dubbingresource
- name: DubbingResponse
  property_count: 2
  slug: elevenlabs-dubbingresponse
- name: DubbingTranscript
  property_count: 1
  slug: elevenlabs-dubbingtranscript
- name: DubSegmentRequest
  property_count: 2
  slug: elevenlabs-dubsegmentrequest
- name: EditVoiceRequest
  property_count: 4
  slug: elevenlabs-editvoicerequest
- name: InstantVoiceCloneRequest
  property_count: 4
  slug: elevenlabs-instantvoiceclonerequest
- name: KnowledgeBaseDocument
  property_count: 4
  slug: elevenlabs-knowledgebasedocument
- name: KnowledgeBaseListResponse
  property_count: 1
  slug: elevenlabs-knowledgebaselistresponse
- name: MusicGenerationRequest
  property_count: 4
  slug: elevenlabs-musicgenerationrequest
- name: ProfessionalVoiceCloneRequest
  property_count: 2
  slug: elevenlabs-professionalvoiceclonerequest
- name: Project
  property_count: 8
  slug: elevenlabs-project
- name: ProjectListResponse
  property_count: 1
  slug: elevenlabs-projectlistresponse
- name: ProjectPronunciationRequest
  property_count: 1
  slug: elevenlabs-projectpronunciationrequest
- name: ProjectSummary
  property_count: 4
  slug: elevenlabs-projectsummary
- name: PronunciationDictionaryLocator
  property_count: 2
  slug: elevenlabs-pronunciationdictionarylocator
- name: SharedVoiceListResponse
  property_count: 3
  slug: elevenlabs-sharedvoicelistresponse
- name: SimulateConversationRequest
  property_count: 2
  slug: elevenlabs-simulateconversationrequest
- name: SimulationResult
  property_count: 2
  slug: elevenlabs-simulationresult
- name: Snapshot
  property_count: 3
  slug: elevenlabs-snapshot
- name: SnapshotListResponse
  property_count: 1
  slug: elevenlabs-snapshotlistresponse
- name: SoundEffectRequest
  property_count: 3
  slug: elevenlabs-soundeffectrequest
- name: SpeechToSpeechRequest
  property_count: 4
  slug: elevenlabs-speechtospeechrequest
- name: SpeechToTextAsyncRequest
  property_count: 4
  slug: elevenlabs-speechtotextasyncrequest
- name: SpeechToTextRequest
  property_count: 5
  slug: elevenlabs-speechtotextrequest
- name: TextToDialogueRequest
  property_count: 2
  slug: elevenlabs-texttodialoguerequest
- name: TextToSpeechRequest
  property_count: 8
  slug: elevenlabs-texttospeechrequest
- name: TimestampedAudioResponse
  property_count: 2
  slug: elevenlabs-timestampedaudioresponse
- name: Tool
  property_count: 7
  slug: elevenlabs-tool
- name: ToolListResponse
  property_count: 1
  slug: elevenlabs-toollistresponse
- name: TranscriptionResponse
  property_count: 5
  slug: elevenlabs-transcriptionresponse
- name: TranscriptionWord
  property_count: 4
  slug: elevenlabs-transcriptionword
- name: TranscriptSegment
  property_count: 4
  slug: elevenlabs-transcriptsegment
- name: TranslateSegmentRequest
  property_count: 2
  slug: elevenlabs-translatesegmentrequest
- name: UpdateAgentRequest
  property_count: 3
  slug: elevenlabs-updateagentrequest
- name: ElevenLabs Voice
  property_count: 10
  slug: elevenlabs-voice
- name: VoiceCloneResponse
  property_count: 1
  slug: elevenlabs-voicecloneresponse
- name: VoiceListResponse
  property_count: 1
  slug: elevenlabs-voicelistresponse
- name: VoiceSample
  property_count: 4
  slug: elevenlabs-voicesample
- name: VoiceSettings
  property_count: 4
  slug: elevenlabs-voicesettings
- name: ElevenLabs Webhook Event
  property_count: 2
  slug: elevenlabs-webhook-event
json_structures:
- name: Elevenlabs Structure
  property_count: 0
  slug: elevenlabs-structure
jsonld:
- class_count: 0
  name: Elevenlabs Context
  property_count: 11
  slug: elevenlabs-context
layout: provider
mcp_servers:
- description: ''
  name: ElevenLabs MCP Server
  slug: elevenlabs-mcp-server
modified: '2026-09-17'
name: ElevenLabs
nav: Providers
network: true
overview: 'ElevenLabs publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Audio Isolation API, and 21 more. Tagged areas include Artificial Intelligence, Text-to-Speech, Speech-to-Text, Voice, and Audio.


  The ElevenLabs catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  ElevenLabs'' developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, pricing, and 47 more developer resources.'
plans:
- name: Elevenlabs Plans Pricing
  plan_count: 7
  slug: elevenlabs-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 35
  name: Elevenlabs Rate Limits
  slug: elevenlabs-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: ElevenLabs API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: elevenlabs-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: ElevenLabs API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: elevenlabs-jsonschema-spectral-rules
scopes:
- name: Elevenlabs Scopes
  scope_count: 0
  slug: elevenlabs-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 82.3
  coverage:
    artifact_dirs: 34
    catalog_earned: 81.5
    catalog_earned_first_party: 24.0
    catalog_gap: 33.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 47.0
    contract_quality: 75.1
    developer_ergonomics: 78.6
    discoverability: 75.9
    operational_transparency: 92.1
  previous_composite: 82.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: true
    score: 33.3
security:
- kind: authentication
  name: Elevenlabs Authentication
  slug: elevenlabs-authentication
  summary_line: apiKey/oauth2/bearer · 3 schemes
- kind: domain-security
  name: Elevenlabs Domain Security
  slug: elevenlabs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Elevenlabs Vulnerability Disclosure
  slug: elevenlabs-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Elevenlabs Trust Center
  slug: elevenlabs-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: elevenlabs
tags:
- Artificial Intelligence
- Text-to-Speech
- Speech-to-Text
- Voice
- Audio
- Machine-Learning
- Conversational AI
- Agents
- Dubbing
- Music Generation
website: https://www.elevenlabs.io/
---
