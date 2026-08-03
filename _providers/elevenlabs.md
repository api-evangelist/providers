---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 40
  human_in_the_loop: 0
  name: Elevenlabs Agentic Access
  operation_count: 62
  slug: elevenlabs-agentic-access
  summary_line: 62 operations · 40 acting
api_count: 22
apis:
- description: Endpoints for creating, managing, and configuring conversational AI agents with voice capabilities.
  name: elevenlabs Agents API
  slug: elevenlabs-agents-api
- description: Endpoints for isolating vocals from background noise in audio recordings.
  name: elevenlabs Audio Isolation API
  slug: elevenlabs-audio-isolation-api
- description: Endpoints for creating and managing Audio Native embedded players for web content.
  name: elevenlabs Audio Native API
  slug: elevenlabs-audio-native-api
- description: Endpoints for managing chapters within Studio projects.
  name: elevenlabs Chapters API
  slug: elevenlabs-chapters-api
- description: Endpoints for retrieving and managing conversation sessions and their associated data.
  name: elevenlabs Conversations API
  slug: elevenlabs-conversations-api
- description: Endpoints for creating, managing, and retrieving dubbed audio and video content across languages.
  name: elevenlabs Dubbing API
  slug: elevenlabs-dubbing-api
- description: Endpoints for managing individual dubbing resources including segments, translations, and dubbed output files.
  name: elevenlabs Dubbing Resources API
  slug: elevenlabs-dubbing-resources-api
- description: Endpoints for creating voice clones from short audio samples with instant processing.
  name: elevenlabs Instant Voice Cloning API
  slug: elevenlabs-instant-voice-cloning-api
- description: Endpoints for managing knowledge base documents that agents use to answer questions.
  name: elevenlabs Knowledge Base API
  slug: elevenlabs-knowledge-base-api
- description: Endpoints for generating music from text prompts using AI models.
  name: elevenlabs Music Generation API
  slug: elevenlabs-music-generation-api
- description: Endpoints for creating high-fidelity voice clones from longer audio recordings with professional-grade processing.
  name: elevenlabs Professional Voice Cloning API
  slug: elevenlabs-professional-voice-cloning-api
- description: Endpoints for managing Studio projects including creation, editing, and rendering of long-form audio content.
  name: elevenlabs Projects API
  slug: elevenlabs-projects-api
- description: Endpoints for managing pronunciation dictionaries used in Studio projects.
  name: elevenlabs Pronunciation Dictionaries API
  slug: elevenlabs-pronunciation-dictionaries-api
- description: Endpoints for generating sound effects from text descriptions using AI models.
  name: elevenlabs Sound Effects API
  slug: elevenlabs-sound-effects-api
- description: Endpoints for converting speech from one voice to another while preserving the original speech characteristics.
  name: elevenlabs Speech to Speech API
  slug: elevenlabs-speech-to-speech-api
- description: Endpoints for converting audio into text transcriptions with support for multiple languages and audio formats.
  name: elevenlabs Speech to Text API
  slug: elevenlabs-speech-to-text-api
- description: Endpoints for converting text scripts with multiple speakers into dialogue audio.
  name: elevenlabs Text to Dialogue API
  slug: elevenlabs-text-to-dialogue-api
- description: Endpoints for converting text into speech audio with configurable voice, model, and output format settings.
  name: elevenlabs Text to Speech API
  slug: elevenlabs-text-to-speech-api
- description: Endpoints for managing external tools and webhook integrations that agents can invoke during conversations.
  name: elevenlabs Tools API
  slug: elevenlabs-tools-api
- description: Endpoints for browsing and adding shared voices from the public voice library.
  name: elevenlabs Voice Library API
  slug: elevenlabs-voice-library-api
- description: Endpoints for managing voice-specific settings such as stability, similarity boost, and style parameters.
  name: elevenlabs Voice Settings API
  slug: elevenlabs-voice-settings-api
- description: Endpoints for managing voices including listing, creating, editing, and deleting voices in the library.
  name: elevenlabs Voices API
  slug: elevenlabs-voices-api
artifact_total: 129
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
  name: ElevenLabs Audio Isolation API
  slug: open-elevenlabs-audio-isolation
- collection_type: open
  name: ElevenLabs Conversational AI API
  slug: open-elevenlabs-conversational-ai
- collection_type: open
  name: ElevenLabs Dubbing API
  slug: open-elevenlabs-dubbing
- collection_type: open
  name: ElevenLabs Music Generation API
  slug: open-elevenlabs-music
- collection_type: open
  name: ElevenLabs Sound Effects API
  slug: open-elevenlabs-sound-effects
- collection_type: open
  name: ElevenLabs Speech to Text API
  slug: open-elevenlabs-speech-to-text
- collection_type: open
  name: ElevenLabs Studio API
  slug: open-elevenlabs-studio
- collection_type: open
  name: ElevenLabs Text to Speech API
  slug: open-elevenlabs-text-to-speech
- collection_type: open
  name: ElevenLabs Voice Changer API
  slug: open-elevenlabs-voice-changer
- collection_type: open
  name: ElevenLabs Voice Cloning API
  slug: open-elevenlabs-voice-cloning
- collection_type: open
  name: ElevenLabs Voices API
  slug: open-elevenlabs-voices
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elevenlabs-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/elevenlabs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elevenlabs-domain-security.yml
- group: auth
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
  title: ''
  type: JSONLD
  url: json-ld/elevenlabs-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/elevenlabs-voice-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/elevenlabs-agent-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/elevenlabs-webhook-event-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://elevenlabs.io/llms.txt
description: Converts text into speech using a voice of your choice and returns audio.
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
modified: '2026-05-19'
name: elevenlabs
nav: Providers
network: true
overview: 'elevenlabs publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Audio Isolation API, Audio Native API, and 19 more.


  The elevenlabs catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  elevenlabs'' developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Elevenlabs Plans Pricing
  plan_count: 7
  slug: elevenlabs-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 7
  name: Elevenlabs Rate Limits
  slug: elevenlabs-rate-limits
rules:
- name: elevenlabs API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: elevenlabs-asyncapi-spectral-rules
- name: elevenlabs API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: elevenlabs-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 83.1
    developer_ergonomics: 13.0
    discoverability: 50.0
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Elevenlabs Authentication
  slug: elevenlabs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Elevenlabs Domain Security
  slug: elevenlabs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Elevenlabs Vulnerability Disclosure
  slug: elevenlabs-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: elevenlabs
---
