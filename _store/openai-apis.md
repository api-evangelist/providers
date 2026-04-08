---
aid: openai-apis
url: https://raw.githubusercontent.com/api-evangelist/openai-apis/refs/heads/main/apis.yml
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
name: OpenAI APIs
tags:
- Artificial Intelligence
- Embeddings
- Image Generation
- Language Models
- Speech
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of OpenAI's artificial intelligence APIs for natural language processing, image generation, speech, and embeddings including Chat Completions, Images, Audio, Embeddings, Moderations, and Assistants APIs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

