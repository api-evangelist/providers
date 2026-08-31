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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Deepgram Agentic Access
  operation_count: 24
  slug: deepgram-agentic-access
  summary_line: 24 operations · 11 acting
api_count: 3
apis:
- description: 'The Deepgram Voice Agent API is an end-to-end solution that combines speech-to-text, LLM orchestration, and text-to-speech into a single real-time API. It simplifies the development of conversational '
  name: Deepgram Voice Agent API
  slug: voice-agent-api
- description: Retrieve billing balance information for projects.
  name: Deepgram Balances API
  slug: deepgram-balances-api
- description: Manage project invitations.
  name: Deepgram Invitations API
  slug: deepgram-invitations-api
- description: Create, list, and manage API keys for projects.
  name: Deepgram Keys API
  slug: deepgram-keys-api
- description: Manage project team members.
  name: Deepgram Members API
  slug: deepgram-members-api
- description: Retrieve available model metadata.
  name: Deepgram Models API
  slug: deepgram-models-api
- description: Transcribe pre-recorded audio files or audio from URLs.
  name: Deepgram Pre-Recorded API
  slug: deepgram-pre-recorded-api
- description: Manage Deepgram projects and project settings.
  name: Deepgram Projects API
  slug: deepgram-projects-api
- description: Manage member scopes and permissions within projects.
  name: Deepgram Scopes API
  slug: deepgram-scopes-api
- description: Analyze text content for summarization, sentiment, topics, and intents.
  name: Deepgram Text Intelligence API
  slug: deepgram-text-intelligence-api
- description: Convert text into natural-sounding speech audio.
  name: Deepgram Text-To-Speech API
  slug: deepgram-text-to-speech-api
- description: Retrieve usage data and request logs for projects.
  name: Deepgram Usage API
  slug: deepgram-usage-api
arazzos:
- description: Pull a project's details, usage summary, request log, and billing balances into a single audit snapshot.
  name: Deepgram Audit Project Usage and Billing
  slug: deepgram-audit-project-usage-workflow
- description: Check a project's billing balance and only transcribe audio when sufficient credit remains.
  name: Deepgram Balance-Gated Transcription
  slug: deepgram-balance-gated-transcription-workflow
- description: Transcribe a multi-speaker recording with diarization, then run targeted text intelligence over the transcript.
  name: Deepgram Diarized Transcript Intelligence
  slug: deepgram-diarized-transcript-intelligence-workflow
- description: Send a project invitation, confirm it appears in the pending invitation list, and list current members.
  name: Deepgram Invite and Confirm a Project Member
  slug: deepgram-invite-and-confirm-member-workflow
- description: Create a new project, mint a scoped API key for it, and verify the key appears in the project key list.
  name: Deepgram Provision a Project API Key
  slug: deepgram-provision-project-key-workflow
- description: Mint a replacement API key in a project, verify it, then delete the old key to complete a rotation.
  name: Deepgram Rotate a Project API Key
  slug: deepgram-rotate-project-key-workflow
- description: Browse available models, read the metadata for a chosen model, then transcribe audio with that model.
  name: Deepgram Select a Model and Transcribe
  slug: deepgram-select-model-and-transcribe-workflow
- description: Transcribe audio to text, run text intelligence on the transcript, then synthesize a spoken response.
  name: Deepgram Transcribe, Analyze, and Synthesize
  slug: deepgram-transcribe-analyze-synthesize-workflow
- description: Transcribe a pre-recorded audio URL and then reconcile the request against project usage and request logs.
  name: Deepgram Transcribe Audio and Track Usage
  slug: deepgram-transcribe-and-track-usage-workflow
- description: Locate a project member, read their current scopes, update them, and confirm the new scopes took effect.
  name: Deepgram Update a Member's Scopes
  slug: deepgram-update-member-scopes-workflow
artifact_total: 120
asyncapis:
- description: The Deepgram Speech-to-Text streaming API provides real-time transcription of audio using a WebSocket connection. Audio data is sent as binary WebSocket messages and transcription results are returned
  name: Deepgram Speech-to-Text Streaming Events
  slug: deepgram-speech-to-text-asyncapi
- description: The Deepgram Text-to-Speech streaming API provides real-time speech synthesis over a WebSocket connection. Text is sent as JSON messages and audio data is returned as binary WebSocket messages, enabli
  name: Deepgram Text-to-Speech Streaming Events
  slug: deepgram-text-to-speech-asyncapi
- description: 'The Deepgram Voice Agent API is an end-to-end solution that combines speech-to-text, LLM orchestration, and text-to-speech into a single real-time WebSocket API. It simplifies building conversational '
  name: Deepgram Voice Agent Events
  slug: deepgram-voice-agent-asyncapi
collections:
- collection_type: postman
  name: Deepgram Management API
  slug: postman-deepgram-management
- collection_type: postman
  name: Deepgram Speech-to-Text API
  slug: postman-deepgram-speech-to-text
- collection_type: postman
  name: Deepgram Text-to-Speech API
  slug: postman-deepgram-text-to-speech
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Deepgram Management Balances API
  slug: open-deepgram-balances-api
- collection_type: open
  name: Deepgram Management Balances Invitations API
  slug: open-deepgram-invitations-api
- collection_type: open
  name: Deepgram Management Balances Keys API
  slug: open-deepgram-keys-api
- collection_type: open
  name: Deepgram Management API
  slug: open-deepgram-management
- collection_type: open
  name: Deepgram Management Balances Members API
  slug: open-deepgram-members-api
- collection_type: open
  name: Deepgram Management Balances Models API
  slug: open-deepgram-models-api
- collection_type: open
  name: Deepgram Management Balances Pre-Recorded API
  slug: open-deepgram-pre-recorded-api
- collection_type: open
  name: Deepgram Management Balances Projects API
  slug: open-deepgram-projects-api
- collection_type: open
  name: Deepgram Management Balances Scopes API
  slug: open-deepgram-scopes-api
- collection_type: open
  name: Deepgram Speech-to-Text API
  slug: open-deepgram-speech-to-text
- collection_type: open
  name: Deepgram Management Balances Text Intelligence API
  slug: open-deepgram-text-intelligence-api
- collection_type: open
  name: Deepgram Management Balances Text-To-Speech API
  slug: open-deepgram-text-to-speech-api
- collection_type: open
  name: Deepgram Text-to-Speech API
  slug: open-deepgram-text-to-speech
- collection_type: open
  name: Deepgram Management Balances Usage API
  slug: open-deepgram-usage-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deepgram-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deepgram-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deepgram-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/deepgram/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/deepgram-audit-project-usage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/deepgram-balance-gated-transcription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/deepgram-diarized-transcript-intelligence-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/deepgram-invite-and-confirm-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/deepgram-provision-project-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/deepgram-rotate-project-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/deepgram-select-model-and-transcribe-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/deepgram-transcribe-analyze-synthesize-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/deepgram-transcribe-and-track-usage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/deepgram-update-member-scopes-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deepgram
- group: docs
  title: ''
  type: Documentation
  url: https://developers.deepgram.com/home
- group: docs
  title: ''
  type: Documentation
  url: https://developers.deepgram.com/reference/deepgram-api-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://deepgram.com/pricing
- group: auth
  title: ''
  type: Authentication
  url: https://developers.deepgram.com/docs/authenticating
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.deepgram.com/changelog
- group: build
  title: ''
  type: SDKs
  url: https://github.com/deepgram/deepgram-python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/deepgram/deepgram-js-sdk
- group: company
  title: ''
  type: Website
  url: https://deepgram.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deepgram.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deepgram.com/tos
- group: design
  title: ''
  type: JSONLD
  url: json-ld/deepgram-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/deepgram-transcript-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/deepgram-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://deepgram.com/llms.txt
created: '2026-03-20'
description: Deepgram is an enterprise voice AI platform that provides speech-to-text, text-to-speech, and voice agent APIs powered by advanced AI models. The platform offers real-time and batch transcription through its Nova model family, natural-sounding speech synthesis through its Aura model family, and an end-to-end Voice Agent API that combines STT, LLM orchestration, and TTS into a single real-time interface.
features:
- 'Nova-3 STT: $0.0048/min mono, $0.0058/min multilingual'
- 'Flux STT: $0.0065/min English, $0.0078/min multilingual'
- Aura-1 TTS at $0.015/1k characters
- Aura-2 TTS at $0.030/1k characters with studio quality
- Streaming and pre-recorded transcription
- Speaker diarization, smart formatting
- Default 50 streaming concurrent (PAYG), 100 pre-recorded
- Voice cloning on Aura models
- Voice agents combining STT + LLM + TTS
- 30+ language support on multilingual models
- WebSocket streaming for real-time STT
- REST API for pre-recorded files
- 'Audio Intelligence: summarization, topics, sentiment, entities'
- Custom model training (Enterprise)
- Self-hosted on-prem option (Enterprise)
- OAuth 2.0 + API keys
finops:
- name: Deepgram Finops
  service_category: Speech AI
  slug: deepgram-finops
graphqls:
- description: 'This document describes the conceptual GraphQL schema for the Deepgram AI voice platform, covering speech-to-text transcription, text-to-speech synthesis, voice agent capabilities, audio intelligence '
  name: Deepgram GraphQL Schema
  slug: deepgram-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deepgram.png
json_schemas:
- name: Alternative
  property_count: 4
  slug: deepgram-alternative
- name: AudioUrlRequest
  property_count: 1
  slug: deepgram-audiourlrequest
- name: Balance
  property_count: 4
  slug: deepgram-balance
- name: BalanceList
  property_count: 1
  slug: deepgram-balancelist
- name: Channel
  property_count: 3
  slug: deepgram-channel
- name: Error
  property_count: 3
  slug: deepgram-error
- name: Intent
  property_count: 2
  slug: deepgram-intent
- name: IntentResults
  property_count: 1
  slug: deepgram-intentresults
- name: IntentSegment
  property_count: 4
  slug: deepgram-intentsegment
- name: Invitation
  property_count: 2
  slug: deepgram-invitation
- name: InvitationCreate
  property_count: 2
  slug: deepgram-invitationcreate
- name: InvitationList
  property_count: 1
  slug: deepgram-invitationlist
- name: Key
  property_count: 6
  slug: deepgram-key
- name: KeyCreate
  property_count: 4
  slug: deepgram-keycreate
- name: KeyList
  property_count: 1
  slug: deepgram-keylist
- name: KeyWithSecret
  property_count: 5
  slug: deepgram-keywithsecret
- name: Member
  property_count: 5
  slug: deepgram-member
- name: MemberList
  property_count: 1
  slug: deepgram-memberlist
- name: Metadata
  property_count: 8
  slug: deepgram-metadata
- name: Model
  property_count: 7
  slug: deepgram-model
- name: ModelInfo
  property_count: 3
  slug: deepgram-modelinfo
- name: ModelList
  property_count: 2
  slug: deepgram-modellist
- name: Paragraph
  property_count: 5
  slug: deepgram-paragraph
- name: ParagraphGroup
  property_count: 2
  slug: deepgram-paragraphgroup
- name: Project
  property_count: 3
  slug: deepgram-project
- name: ProjectList
  property_count: 1
  slug: deepgram-projectlist
- name: ProjectUpdate
  property_count: 2
  slug: deepgram-projectupdate
- name: RequestList
  property_count: 3
  slug: deepgram-requestlist
- name: Results
  property_count: 6
  slug: deepgram-results
- name: ScopeList
  property_count: 1
  slug: deepgram-scopelist
- name: ScopeUpdate
  property_count: 1
  slug: deepgram-scopeupdate
- name: Sentence
  property_count: 3
  slug: deepgram-sentence
- name: SentimentAverage
  property_count: 2
  slug: deepgram-sentimentaverage
- name: SentimentResults
  property_count: 2
  slug: deepgram-sentimentresults
- name: SentimentSegment
  property_count: 5
  slug: deepgram-sentimentsegment
- name: SpeakRequest
  property_count: 1
  slug: deepgram-speakrequest
- name: Summary
  property_count: 1
  slug: deepgram-summary
- name: TextAnalysisRequest
  property_count: 2
  slug: deepgram-textanalysisrequest
- name: TextAnalysisResponse
  property_count: 2
  slug: deepgram-textanalysisresponse
- name: Topic
  property_count: 2
  slug: deepgram-topic
- name: TopicResults
  property_count: 1
  slug: deepgram-topicresults
- name: TopicSegment
  property_count: 4
  slug: deepgram-topicsegment
- name: Deepgram Transcript
  property_count: 2
  slug: deepgram-transcript
- name: TranscriptionResponse
  property_count: 2
  slug: deepgram-transcriptionresponse
- name: UsageSummary
  property_count: 4
  slug: deepgram-usagesummary
- name: Utterance
  property_count: 8
  slug: deepgram-utterance
- name: Word
  property_count: 8
  slug: deepgram-word
json_structures:
- name: Deepgram Structure
  property_count: 0
  slug: deepgram-structure
jsonld:
- class_count: 0
  name: Deepgram Context
  property_count: 11
  slug: deepgram-context
layout: provider
modified: '2026-05-19'
name: Deepgram
nav: Providers
network: true
overview: 'Deepgram publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Voice Agent API, Balances API, Invitations API, and 9 more. Tagged areas include Artificial Intelligence, Speech-To-Text, Text-To-Speech, Transcription, and Voice AI.


  The Deepgram catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 5 Spectral governance rulesets.


  Deepgram''s developer surface includes authentication, documentation, pricing, changelog, and 25 more developer resources.'
plans:
- name: Deepgram Plans Pricing
  plan_count: 6
  slug: deepgram-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Deepgram Rate Limits
  slug: deepgram-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Deepgram API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: deepgram-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Deepgram API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: deepgram-jsonschema-spectral-rules
- effective_rule_count: 45
  extends:
  - spectral:oas
  name: Deepgram API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 4
  slug: deepgram-management-api-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Deepgram API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: deepgram-speech-to-text-api-rules
- effective_rule_count: 45
  extends:
  - spectral:oas
  name: Deepgram API Rules
  rule_count: 4
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 2
  slug: deepgram-text-to-speech-api-rules
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 28.8
    contract_quality: 73.4
    developer_ergonomics: 33.3
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 23.7
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deepgram/refs/heads/main/screenshots/deepgram-2026-06-20T175821.png
security:
- kind: authentication
  name: Deepgram Authentication
  slug: deepgram-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Deepgram Domain Security
  slug: deepgram-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deepgram
tags:
- Artificial Intelligence
- Speech-To-Text
- Text-To-Speech
- Transcription
- Voice AI
website: https://deepgram.com/
---
