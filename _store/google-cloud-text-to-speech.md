---
aid: google-cloud-text-to-speech
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-text-to-speech/refs/heads/main/apis.yml
apis:
- name: Google Cloud Text-to-Speech API
  description: Synthesizes natural-sounding speech from text or SSML input, supporting multiple languages, voices, and audio formats powered by Google's AI models.
  humanURL: https://cloud.google.com/text-to-speech
  baseURL: https://texttospeech.googleapis.com
  tags:
  - Audio
  - Speech Synthesis
  - Text-To-Speech
  properties:
  - type: Documentation
    url: https://cloud.google.com/text-to-speech/docs/reference/rest
  - type: OpenAPI
    url: openapi/openapi.yml
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Getting Started
    url: https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries
  - type: JSONSchema
    url: json-schema/speech-synthesis.json
  - type: JSONLD
    url: json-ld/context.jsonld
name: Google Cloud Text-To-Speech
tags:
- Audio
- Google Cloud
- Machine Learning
- Speech Synthesis
- Text-To-Speech
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Text-to-Speech converts text or Speech Synthesis Markup Language (SSML) input into audio data of natural human speech. It provides access to hundreds of voices across multiple languages and variants, powered by DeepMind's WaveNet technology and Google's neural network models.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

