---
aid: deepgram
url: https://raw.githubusercontent.com/api-evangelist/deepgram/refs/heads/main/apis.yml
apis:
- aid: deepgram:speech-to-text-api
  name: Deepgram Speech-To-Text API
  tags:
  - Audio
  - Speech Recognition
  - Speech-To-Text
  - Transcription
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.deepgram.com
  humanURL: https://developers.deepgram.com/docs/stt/getting-started
  properties:
  - url: https://developers.deepgram.com/docs/stt/getting-started
    type: Documentation
  - url: openapi/deepgram-speech-to-text-openapi.yml
    type: OpenAPI
  - url: asyncapi/deepgram-speech-to-text-asyncapi.yml
    type: AsyncAPI
  description: The Deepgram Speech-to-Text API provides accurate, fast transcription of audio content using advanced AI models. It supports both pre-recorded audio files and real-time streaming audio, delivering transcripts in under 300 milliseconds. The API includes features such as punctuation, diarization, language detection, smart formatting, and support for multiple languages and audio formats.
- aid: deepgram:text-to-speech-api
  name: Deepgram Text-To-Speech API
  tags:
  - Audio
  - Speech Synthesis
  - Text-To-Speech
  - Voice
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.deepgram.com
  humanURL: https://developers.deepgram.com/reference/text-to-speech-api/speak
  properties:
  - url: https://developers.deepgram.com/reference/text-to-speech-api/speak
    type: Documentation
  - url: openapi/deepgram-text-to-speech-openapi.yml
    type: OpenAPI
  - url: asyncapi/deepgram-text-to-speech-asyncapi.yml
    type: AsyncAPI
  description: The Deepgram Text-to-Speech API converts text into natural-sounding speech using the Aura model family. It supports both single text requests and continuous streaming text-to-speech, delivering sub-200 millisecond latency suitable for real-time voice agents and conversational AI applications. The API offers multiple voice options and is designed for enterprise-grade deployments including voicebots, IVR systems, and interactive voice applications.
- aid: deepgram:voice-agent-api
  name: Deepgram Voice Agent API
  tags:
  - Conversational AI
  - Real-Time
  - Voice Agent
  - Voice AI
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.deepgram.com
  humanURL: https://deepgram.com/product/voice-agent-api
  properties:
  - url: https://developers.deepgram.com/docs/voice-agent/getting-started
    type: Documentation
  - url: asyncapi/deepgram-voice-agent-asyncapi.yml
    type: AsyncAPI
  description: The Deepgram Voice Agent API is an end-to-end solution that combines speech-to-text, LLM orchestration, and text-to-speech into a single real-time API. It simplifies the development of conversational voice agents by eliminating the need to stitch together multiple services. The API includes built-in barge-in detection, turn-taking prediction, function calling, and mid-session control to ensure smooth, natural conversations without pauses or interruptions.
- aid: deepgram:audio-intelligence-api
  name: Deepgram Audio Intelligence API
  tags:
  - Audio Intelligence
  - Sentiment Analysis
  - Summarization
  - Topic Detection
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.deepgram.com
  humanURL: https://developers.deepgram.com/docs/audio-intelligence
  properties:
  - url: https://developers.deepgram.com/docs/audio-intelligence
    type: Documentation
  - url: openapi/deepgram-speech-to-text-openapi.yml
    type: OpenAPI
  description: The Deepgram Audio Intelligence API provides advanced analysis capabilities for audio and text content. It offers features including sentiment analysis, summarization, topic detection, and intent recognition. These capabilities allow developers to extract structured insights from transcribed audio or text input, enabling use cases such as call center analytics, meeting summarization, and content categorization.
- aid: deepgram:management-api
  name: Deepgram Management API
  tags:
  - Administration
  - API Keys
  - Management
  - Projects
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.deepgram.com
  humanURL: https://developers.deepgram.com/docs/create-additional-api-keys
  properties:
  - url: https://developers.deepgram.com/docs/create-additional-api-keys
    type: Documentation
  - url: openapi/deepgram-management-openapi.yml
    type: OpenAPI
  description: The Deepgram Management API allows developers to programmatically manage their Deepgram account resources. It provides endpoints for creating and managing API keys, configuring projects, managing team members, and monitoring usage. This API enables automation of administrative tasks and integration of Deepgram account management into existing workflows and infrastructure tooling.
name: Deepgram
tags:
- Artificial Intelligence
- Speech-To-Text
- Text-To-Speech
- Transcription
- Voice AI
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Deepgram is an enterprise voice AI platform that provides speech-to-text, text-to-speech, and voice agent APIs powered by advanced AI models. The platform offers real-time and batch transcription through its Nova model family, natural-sounding speech synthesis through its Aura model family, and an end-to-end Voice Agent API that combines STT, LLM orchestration, and TTS into a single real-time interface.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

