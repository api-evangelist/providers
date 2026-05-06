---
aid: assemblyai
name: AssemblyAI
description: Built by AI experts, AssemblyAI's Speech AI models include accurate speech-to-text for voice data (such as calls, virtual meetings, and podcasts), speaker detection, sentiment analysis, chapter detection, PII redaction, and more. AssemblyAI provides powerful APIs for transcribing and understanding audio data at scale. The platform supports real-time streaming transcription via WebSocket, asynchronous batch transcription, and audio intelligence features including summarization, auto chapters, entity detection, and content safety filtering. SDKs are available for Python, Node.js, Ruby, Java, and Go.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Artificial Intelligence
  - Audio
  - Speech
  - Transcription
  - Speech to Text
url: https://raw.githubusercontent.com/api-evangelist/assemblyai/refs/heads/main/apis.yml
created: '2024-06-06'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: assemblyai:assemblyai-api
    name: AssemblyAI API
    description: The AssemblyAI API provides speech-to-text transcription, speaker diarization, sentiment analysis, chapter detection, PII redaction, and other audio intelligence capabilities via REST and WebSocket interfaces.
    humanURL: https://www.assemblyai.com/docs/
    baseURL: https://api.assemblyai.com
    tags:
      - Audio Intelligence
      - Speech to Text
      - Transcription
    properties:
      - type: Documentation
        url: https://www.assemblyai.com/docs/
      - type: GettingStarted
        url: https://www.assemblyai.com/docs/getting-started/transcribe-an-audio-file
      - type: Authentication
        url: https://www.assemblyai.com/docs/concepts/authentication
      - type: APIReference
        url: https://www.assemblyai.com/docs/api-reference/overview
      - type: OpenAPI
        url: openapi/assemblyai-openapi-original.yml
      - type: AsyncAPI
        url: openapi/assemblyai-asyncapi-original.yml
common:
  - type: Portal
    url: https://www.assemblyai.com/
    title: AssemblyAI Website
  - type: Documentation
    url: https://www.assemblyai.com/docs/
    title: Documentation
  - type: Blog
    url: https://www.assemblyai.com/blog
    title: Blog
  - type: SignUp
    url: https://www.assemblyai.com/dashboard/signup
    title: Sign Up
  - type: Login
    url: https://www.assemblyai.com/dashboard/login
    title: Login
  - type: Pricing
    url: https://www.assemblyai.com/pricing
    title: Pricing
  - type: GitHubOrganization
    url: https://github.com/AssemblyAI
    title: AssemblyAI GitHub Organization
  - type: StatusPage
    url: https://status.assemblyai.com/
    title: Status Page
  - type: Features
    data:
      - name: Speech-to-Text Transcription
        description: High-accuracy transcription of audio files and streams using AssemblyAI's Universal-2 model with support for 99+ languages and custom vocabulary.
      - name: Real-Time Streaming Transcription
        description: WebSocket-based streaming transcription for live audio with partial results and final transcripts, supporting call centers, live captioning, and voice applications.
      - name: Speaker Diarization
        description: Automatic speaker detection and labeling that identifies who said what in multi-speaker recordings.
      - name: Audio Intelligence
        description: Advanced understanding features including sentiment analysis, summarization, auto chapters, entity detection, content safety filtering, and PII redaction.
      - name: LeMUR
        description: LeMUR (Leveraging Large Language Models for Understanding Recordings) enables asking questions of audio transcripts using a conversational AI interface built on top of transcriptions.
  - type: UseCases
    data:
      - name: Call Center Analytics
        description: Customer service teams transcribe and analyze customer calls for quality assurance, compliance, agent coaching, and sentiment analysis.
      - name: Meeting Intelligence
        description: Enterprises transcribe virtual meetings (Zoom, Teams, Meet) to generate summaries, action items, and searchable archives.
      - name: Podcast Processing
        description: Podcast producers transcribe episodes for SEO, accessibility, show notes, and content repurposing.
      - name: Voice Application Development
        description: Developers build voice-powered applications using real-time streaming transcription for voice commands, dictation, and conversation interfaces.
      - name: Compliance and Legal
        description: Legal and compliance teams transcribe depositions, hearings, and recorded communications with PII redaction and timestamped transcripts.
  - type: Integrations
    data:
      - name: Twilio
        description: Integration with Twilio Media Streams for transcribing phone calls in real-time using AssemblyAI's streaming API.
      - name: Zoom
        description: Integration with Zoom recordings for batch transcription and meeting intelligence processing.
      - name: Python SDK
        description: Official Python SDK for AssemblyAI available on PyPI (assemblyai) for easy integration in Python applications.
      - name: Node.js SDK
        description: Official Node.js SDK for AssemblyAI available on npm (@assemblyai/sdk) for JavaScript and TypeScript applications.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
