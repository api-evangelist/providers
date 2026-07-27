---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 49.0
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Assemblyai Agentic Access
  operation_count: 16
  slug: assemblyai-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 3
apis:
- description: LeMUR related operations
  name: AssemblyAI LeMUR API
  slug: assemblyai-lemur-api
- description: Streaming Speech-to-Text
  name: AssemblyAI Streaming API
  slug: assemblyai-streaming-api
- description: Transcript related operations
  name: AssemblyAI Transcript API
  slug: assemblyai-transcript-api
artifact_total: 27
asyncapis:
- description: AsyncAPI specification for the AssemblyAI Universal Streaming Speech-to-Text WebSocket API (v3). Clients open a WebSocket to `wss://streaming.assemblyai.com/v3/ws`, send raw binary PCM audio frames, a
  name: AssemblyAI Universal Streaming Speech-to-Text API
  slug: assemblyai-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/assemblyai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/assemblyai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/assemblyai-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/assemblyai
- group: start
  title: AssemblyAI Website
  type: Portal
  url: https://www.assemblyai.com/
- group: docs
  title: Documentation
  type: Documentation
  url: https://www.assemblyai.com/docs/
- group: company
  title: Blog
  type: Blog
  url: https://www.assemblyai.com/blog
- group: start
  title: Sign Up
  type: Signup
  url: https://www.assemblyai.com/dashboard/signup
- group: start
  title: Login
  type: Login
  url: https://www.assemblyai.com/dashboard/login
- group: commercial
  title: Pricing
  type: Pricing
  url: https://www.assemblyai.com/pricing
- group: build
  title: AssemblyAI GitHub Organization
  type: GitHubOrganization
  url: https://github.com/AssemblyAI
- group: operate
  title: Status Page
  type: StatusPage
  url: https://status.assemblyai.com/
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/AssemblyAI/assemblyai-skill
created: '2024-06-06'
description: Built by AI experts, AssemblyAI's Speech AI models include accurate speech-to-text for voice data (such as calls, virtual meetings, and podcasts), speaker detection, sentiment analysis, chapter detection, PII redaction, and more. AssemblyAI provides powerful APIs for transcribing and understanding audio data at scale. The platform supports real-time streaming transcription via WebSocket, asynchronous batch transcription, and audio intelligence features including summarization, auto chapters, entity detection, and content safety filtering. SDKs are available for Python, Node.js, Ruby, Java, and Go.
features:
- description: High-accuracy transcription of audio files and streams using AssemblyAI's Universal-2 model with support for 99+ languages and custom vocabulary.
  name: Speech-to-Text Transcription
- description: WebSocket-based streaming transcription for live audio with partial results and final transcripts, supporting call centers, live captioning, and voice applications.
  name: Real-Time Streaming Transcription
- description: Automatic speaker detection and labeling that identifies who said what in multi-speaker recordings.
  name: Speaker Diarization
- description: Advanced understanding features including sentiment analysis, summarization, auto chapters, entity detection, content safety filtering, and PII redaction.
  name: Audio Intelligence
- description: LeMUR (Leveraging Large Language Models for Understanding Recordings) enables asking questions of audio transcripts using a conversational AI interface built on top of transcriptions.
  name: LeMUR
finops:
- name: Assemblyai Finops
  service_category: API
  slug: assemblyai-finops
graphqls:
- description: AssemblyAI is an AI speech-to-text and audio intelligence API. The API covers async and real-time transcription, speaker diarization, sentiment analysis, topic detection, PII redaction, chapter detect
  name: AssemblyAI GraphQL API
  slug: assemblyai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/assemblyai.png
integrations:
- description: Integration with Twilio Media Streams for transcribing phone calls in real-time using AssemblyAI's streaming API.
  name: Twilio
- description: Integration with Zoom recordings for batch transcription and meeting intelligence processing.
  name: Zoom
- description: Official Python SDK for AssemblyAI available on PyPI (assemblyai) for easy integration in Python applications.
  name: Python SDK
- description: Official Node.js SDK for AssemblyAI available on npm (@assemblyai/sdk) for JavaScript and TypeScript applications.
  name: Node.js SDK
layout: provider
modified: '2026-05-19'
name: AssemblyAI
nav: Providers
network: true
overview: 'AssemblyAI publishes 3 APIs on the [APIs.io](https://apis.io/) network: LeMUR API, Streaming API, and Transcript API. Tagged areas include AI, Artificial Intelligence, Audio, Speech, and Transcription.


  The AssemblyAI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  AssemblyAI''s developer surface includes developer portal, documentation, engineering blog, signup flow, pricing, and 8 more developer resources.'
plans:
- name: Assemblyai Plans Pricing
  plan_count: 3
  slug: assemblyai-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 5
  name: Assemblyai Rate Limits
  slug: assemblyai-rate-limits
rules:
- name: AssemblyAI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: assemblyai-asyncapi-spectral-rules
score:
  band: developing
  composite: 59.2
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 65.5
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 65.8
    operational_transparency: 52.6
  previous_composite: 59.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/assemblyai/refs/heads/main/screenshots/assemblyai-2026-06-20T172502.png
security:
- kind: domain-security
  name: Assemblyai Domain Security
  slug: assemblyai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Assemblyai Trust Center
  slug: assemblyai-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
skill_count: 1
skills:
- name: assemblyai
  slug: assemblyai
slug: assemblyai
tags:
- AI
- Artificial Intelligence
- Audio
- Speech
- Transcription
- Speech to Text
use_cases:
- description: Customer service teams transcribe and analyze customer calls for quality assurance, compliance, agent coaching, and sentiment analysis.
  name: Call Center Analytics
- description: Enterprises transcribe virtual meetings (Zoom, Teams, Meet) to generate summaries, action items, and searchable archives.
  name: Meeting Intelligence
- description: Podcast producers transcribe episodes for SEO, accessibility, show notes, and content repurposing.
  name: Podcast Processing
- description: Developers build voice-powered applications using real-time streaming transcription for voice commands, dictation, and conversation interfaces.
  name: Voice Application Development
- description: Legal and compliance teams transcribe depositions, hearings, and recorded communications with PII redaction and timestamped transcripts.
  name: Compliance and Legal
website: https://www.assemblyai.com/
---
