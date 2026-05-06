---
aid: google-cloud-text-to-speech
name: Google Cloud Text-To-Speech
description: Google Cloud Text-to-Speech converts text or Speech Synthesis Markup Language (SSML) input into audio data of natural human speech. It provides access to hundreds of voices across multiple languages and variants, powered by DeepMind's WaveNet technology and Google's neural network models.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-text-to-speech/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Audio
  - Google Cloud
  - Machine Learning
  - Speech Synthesis
  - Text-To-Speech
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
common:
  - type: Portal
    url: https://cloud.google.com/text-to-speech
  - type: Getting Started
    url: https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries
  - type: Documentation
    url: https://cloud.google.com/text-to-speech/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/text-to-speech/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/text-to-speech/docs/support
  - type: JSONLD
    url: json-ld/context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
