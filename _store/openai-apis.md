---
aid: openai-apis
name: OpenAI APIs
description: Collection of OpenAI's artificial intelligence APIs for natural language processing, image generation, speech, and embeddings including Chat Completions, Completions, Images, Audio, Embeddings, Moderations, and Assistants APIs.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artificial Intelligence
  - Embeddings
  - Image Generation
  - Language Models
  - Speech
url: https://raw.githubusercontent.com/api-evangelist/openai-apis/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: openai-apis:openai-chat-completions-api
    name: OpenAI Chat Completions API
    description: API for conversational AI using GPT models.
    humanURL: https://platform.openai.com/docs/api-reference/chat
    baseURL: https://api.openai.com/v1
    tags:
      - Chat
      - GPT
    properties:
      - type: Documentation
        url: https://platform.openai.com/docs/api-reference/chat
      - type: OpenAPI
        url: openapi/openai-chat-completions-openapi.yml
  - aid: openai-apis:openai-completions-api
    name: OpenAI Completions API
    description: Legacy text completion API for generating text continuations from a prompt.
    humanURL: https://platform.openai.com/docs/api-reference/completions
    baseURL: https://api.openai.com/v1
    tags:
      - Completions
      - GPT
    properties:
      - type: Documentation
        url: https://platform.openai.com/docs/api-reference/completions
      - type: OpenAPI
        url: openapi/openai-completions-openapi.yml
  - aid: openai-apis:openai-images-api
    name: OpenAI Images API
    description: API for generating, editing, and creating image variations using DALL-E.
    humanURL: https://platform.openai.com/docs/api-reference/images
    baseURL: https://api.openai.com/v1
    tags:
      - DALL-E
      - Image Generation
    properties:
      - type: Documentation
        url: https://platform.openai.com/docs/api-reference/images
      - type: OpenAPI
        url: openapi/openai-images-openapi.yml
  - aid: openai-apis:openai-embeddings-api
    name: OpenAI Embeddings API
    description: API for converting text into vector representations.
    humanURL: https://platform.openai.com/docs/api-reference/embeddings
    baseURL: https://api.openai.com/v1
    tags:
      - Embeddings
      - Vectors
    properties:
      - type: Documentation
        url: https://platform.openai.com/docs/api-reference/embeddings
      - type: OpenAPI
        url: openapi/openai-embeddings-openapi.yml
  - aid: openai-apis:openai-audio-api
    name: OpenAI Audio API
    description: API for speech-to-text transcription and text-to-speech generation.
    humanURL: https://platform.openai.com/docs/api-reference/audio
    baseURL: https://api.openai.com/v1
    tags:
      - Audio
      - Speech
    properties:
      - type: Documentation
        url: https://platform.openai.com/docs/api-reference/audio
      - type: OpenAPI
        url: openapi/openai-audio-openapi.yml
  - aid: openai-apis:openai-moderations-api
    name: OpenAI Moderations API
    description: API for detecting potentially harmful or unsafe content across text and images.
    humanURL: https://platform.openai.com/docs/api-reference/moderations
    baseURL: https://api.openai.com/v1
    tags:
      - Moderation
      - Safety
    properties:
      - type: Documentation
        url: https://platform.openai.com/docs/api-reference/moderations
      - type: OpenAPI
        url: openapi/openai-moderations-openapi.yml
  - aid: openai-apis:openai-assistants-api
    name: OpenAI Assistants API
    description: API for building AI assistants with custom instructions and tool access.
    humanURL: https://platform.openai.com/docs/api-reference/assistants
    baseURL: https://api.openai.com/v1
    tags:
      - Agents
      - Assistants
    properties:
      - type: Documentation
        url: https://platform.openai.com/docs/api-reference/assistants
      - type: OpenAPI
        url: openapi/openai-assistants-openapi.yml
common:
  - type: Authentication
    url: https://platform.openai.com/docs/api-reference/authentication
  - type: Pricing
    url: https://openai.com/api/pricing/
  - type: Terms of Service
    url: https://openai.com/policies/terms-of-use
  - type: Privacy Policy
    url: https://openai.com/policies/privacy-policy
  - type: Status
    url: https://status.openai.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
