---
aid: elevenlabs
url: https://raw.githubusercontent.com/api-evangelist/elevenlabs/refs/heads/main/apis.yml
apis:
- aid: elevenlabs:text-to-speech
  name: ElevenLabs Text to Speech API
  tags:
  - AI
  - Audio
  - Speech Synthesis
  - Text to Speech
  - Voice
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.elevenlabs.io
  humanURL: https://elevenlabs.io/docs/api-reference/text-to-speech/convert
  properties:
  - url: https://elevenlabs.io/docs/api-reference/text-to-speech/convert
    type: Documentation
  - url: openapi/elevenlabs-text-to-speech-openapi.yml
    type: OpenAPI
  - url: asyncapi/elevenlabs-text-to-speech-streaming-asyncapi.yml
    type: AsyncAPI
  description: The ElevenLabs Text to Speech API converts text into lifelike spoken audio with nuanced intonation, pacing, and emotional awareness. It supports multiple output formats including MP3, PCM, and mu-law, and offers a range of models such as Flash v2.5 for ultra-low latency real-time applications and Multilingual v2 for support across 70+ languages. Developers can select from thousands of pre-built voices or use custom cloned voices to generate speech that sounds natural and expressive.
- aid: elevenlabs:speech-to-text
  name: ElevenLabs Speech to Text API
  tags:
  - AI
  - Audio
  - Speech to Text
  - Transcription
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.elevenlabs.io
  humanURL: https://elevenlabs.io/docs/api-reference/speech-to-text/convert
  properties:
  - url: https://elevenlabs.io/docs/api-reference/speech-to-text/convert
    type: Documentation
  - url: openapi/elevenlabs-speech-to-text-openapi.yml
    type: OpenAPI
  description: The ElevenLabs Speech to Text API provides state-of-the-art transcription capabilities, converting spoken audio into accurate text. It supports multiple audio formats and languages, enabling developers to build applications that require reliable audio transcription. The API is designed for both real-time and batch processing use cases.
- aid: elevenlabs:voice-cloning
  name: ElevenLabs Voice Cloning API
  tags:
  - AI
  - Audio
  - Voice
  - Voice Cloning
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.elevenlabs.io
  humanURL: https://elevenlabs.io/docs/api-reference/voices/ivc/create
  properties:
  - url: https://elevenlabs.io/docs/api-reference/voices/ivc/create
    type: Documentation
  - url: openapi/elevenlabs-voice-cloning-openapi.yml
    type: OpenAPI
  description: The ElevenLabs Voice Cloning API allows developers to create custom AI voices from audio recordings. Instant Voice Cloning requires as little as 60 seconds of clean audio to generate a usable voice clone, while Professional Voice Cloning produces higher fidelity results from a minimum of 30 minutes of recordings. Cloned voices can then be used with the Text to Speech API for generating speech that closely matches the original speaker.
- aid: elevenlabs:voices
  name: ElevenLabs Voices API
  tags:
  - AI
  - Voice Library
  - Voice Management
  - Voices
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.elevenlabs.io
  humanURL: https://elevenlabs.io/docs/api-reference/voices/get
  properties:
  - url: https://elevenlabs.io/docs/api-reference/voices/get
    type: Documentation
  - url: openapi/elevenlabs-voices-openapi.yml
    type: OpenAPI
  description: The ElevenLabs Voices API provides management capabilities for the voice library, including listing, retrieving, creating, editing, and deleting voices. Developers can access a library of over 5,000 pre-built voices and manage their own custom voices. The API also supports voice design, allowing creation of new AI voices from text descriptions specifying desired characteristics such as accent, age, and tone.
- aid: elevenlabs:sound-effects
  name: ElevenLabs Sound Effects API
  tags:
  - AI
  - Audio Generation
  - Sound Effects
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.elevenlabs.io
  humanURL: https://elevenlabs.io/docs/api-reference/sound-generation/create
  properties:
  - url: https://elevenlabs.io/docs/api-reference/sound-generation/create
    type: Documentation
  - url: openapi/elevenlabs-sound-effects-openapi.yml
    type: OpenAPI
  description: The ElevenLabs Sound Effects API generates cinematic sound effects from text descriptions. Developers can describe the desired sound in natural language and receive high-quality audio output. The API supports audio tags for controlling delivery, emotion, emphasis, pauses, and specific sound effects, making it suitable for game development, film production, and multimedia content creation.
- aid: elevenlabs:audio-isolation
  name: ElevenLabs Audio Isolation API
  tags:
  - Audio Isolation
  - Audio Processing
  - Noise Removal
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.elevenlabs.io
  humanURL: https://elevenlabs.io/docs/api-reference/audio-isolation/audio-isolation
  properties:
  - url: https://elevenlabs.io/docs/api-reference/audio-isolation/audio-isolation
    type: Documentation
  - url: openapi/elevenlabs-audio-isolation-openapi.yml
    type: OpenAPI
  description: The ElevenLabs Audio Isolation API removes background noise from audio recordings, isolating vocal tracks from ambient sounds and interference. This is useful for cleaning up recordings, improving audio quality for podcasts and interviews, and preparing audio files for further processing such as voice cloning or transcription. The API processes audio files and returns cleaned versions with the vocal content preserved.
- aid: elevenlabs:dubbing
  name: ElevenLabs Dubbing API
  tags:
  - Audio
  - Dubbing
  - Localization
  - Translation
  - Video
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.elevenlabs.io
  humanURL: https://elevenlabs.io/docs/api-reference/dubbing/resources/dub-segment
  properties:
  - url: https://elevenlabs.io/docs/api-reference/dubbing/resources/dub-segment
    type: Documentation
  - url: openapi/elevenlabs-dubbing-openapi.yml
    type: OpenAPI
  description: The ElevenLabs Dubbing API enables automatic translation and voice-over of audio and video content into different languages. It preserves the original speaker's voice characteristics while translating the spoken content, supporting seamless localization of multimedia content. The API handles the full dubbing pipeline including transcription, translation, and speech synthesis with lip-sync timing.
- aid: elevenlabs:voice-changer
  name: ElevenLabs Voice Changer API
  tags:
  - Audio Processing
  - Voice Changer
  - Voice Conversion
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.elevenlabs.io
  humanURL: https://elevenlabs.io/docs/api-reference/speech-to-speech/convert
  properties:
  - url: https://elevenlabs.io/docs/api-reference/speech-to-speech/convert
    type: Documentation
  - url: openapi/elevenlabs-voice-changer-openapi.yml
    type: OpenAPI
  description: The ElevenLabs Voice Changer API performs speech-to-speech conversion, replacing one voice with another while preserving the original speech content, timing, and emotional delivery. Developers can transform audio recordings to sound like a different speaker using any voice from the ElevenLabs library or a custom cloned voice. This is useful for content creation, privacy protection, and character voice generation.
- aid: elevenlabs:music
  name: ElevenLabs Music Generation API
  tags:
  - AI
  - Audio Generation
  - Music
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.elevenlabs.io
  humanURL: https://elevenlabs.io/docs/overview/capabilities/music
  properties:
  - url: https://elevenlabs.io/docs/overview/capabilities/music
    type: Documentation
  - url: openapi/elevenlabs-music-openapi.yml
    type: OpenAPI
  description: The ElevenLabs Music Generation API creates music from text prompts, allowing developers to generate original musical compositions programmatically. Users describe the desired genre, mood, tempo, and instrumentation in natural language and receive generated audio output. The API is designed for applications that need background music, jingles, or custom soundtracks without requiring manual composition.
- aid: elevenlabs:conversational-ai
  name: ElevenLabs Conversational AI API
  tags:
  - AI
  - Conversational AI
  - Real-Time
  - Voice Agents
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.elevenlabs.io
  humanURL: https://elevenlabs.io/docs/overview/capabilities/conversational-ai
  properties:
  - url: https://elevenlabs.io/docs/overview/capabilities/conversational-ai
    type: Documentation
  - url: openapi/elevenlabs-conversational-ai-openapi.yml
    type: OpenAPI
  - url: asyncapi/elevenlabs-conversational-ai-asyncapi.yml
    type: AsyncAPI
  - url: asyncapi/elevenlabs-webhooks-asyncapi.yml
    type: AsyncAPI
  description: The ElevenLabs Conversational AI API enables developers to build interactive voice agents that can engage in natural, real-time conversations. It combines speech recognition, language understanding, and speech synthesis into a unified interface supporting multi-turn dialogue across 70+ languages. The API is designed for building customer service agents, voice assistants, and interactive voice response systems with expressive, human-sounding voices.
- aid: elevenlabs:studio
  name: ElevenLabs Studio API
  tags:
  - Content Management
  - Projects
  - Studio
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.elevenlabs.io
  humanURL: https://elevenlabs.io/docs/overview/capabilities/projects
  properties:
  - url: https://elevenlabs.io/docs/overview/capabilities/projects
    type: Documentation
  - url: openapi/elevenlabs-studio-openapi.yml
    type: OpenAPI
  description: The ElevenLabs Studio API provides programmatic access to the ElevenLabs Studio project management system. Developers can create, manage, and render long-form audio content projects through the API, organizing text into chapters and assigning different voices to different sections. The Studio is designed for producing audiobooks, podcasts, and other long-form audio content at scale.
name: Elevenlabs
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Converts text into speech using a voice of your choice and returns audio.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

