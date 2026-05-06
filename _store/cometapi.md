---
aid: cometapi
url: https://raw.githubusercontent.com/api-evangelist/cometapi/refs/heads/main/apis.yml
name: CometAPI
tags:
  - AI
  - Aggregator
  - Audio
  - Chat
  - Embeddings
  - Generative AI
  - Images
  - LLM
  - Multi-Model
  - OpenAI-Compatible
  - Video
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
x-type: company
created: '2026-03-16'
modified: '2026-04-26'
position: Consumer
description: CometAPI is an AI API aggregator that consolidates access to 500+ models from multiple providers (OpenAI, Anthropic, Google, xAI, DeepSeek, Alibaba, and more) behind a single OpenAI-compatible REST surface. It supports chat completions, embeddings, image generation, text-to-video and image-to-video, speech synthesis, and audio transcription. CometAPI positions itself as a drop-in replacement for the OpenAI SDK (changing only the base URL and key), with pay-as-you-go pricing reportedly 20-40% cheaper than direct vendor rates, sub-400ms median latency, and 99.9% service availability.
apis:
  - aid: cometapi:cometapi-unified-api
    name: CometAPI Unified API
    tags:
      - AI
      - Aggregator
      - Chat
      - Embeddings
      - Images
      - OpenAI-Compatible
      - Video
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cometapi.com/v1
    humanURL: https://apidoc.cometapi.com/
    properties:
      - url: https://apidoc.cometapi.com/
        type: Documentation
      - url: https://www.cometapi.com/
        type: Marketing
      - url: openapi/cometapi-unified-api-openapi.yml
        type: OpenAPI
    description: OpenAI-compatible REST API exposing chat completions, embeddings, image generation, video generation, speech synthesis, and audio transcription across hundreds of upstream models. Authentication uses a bearer token, and the `model` field on each request selects the upstream provider (e.g. gpt-5.5, claude-4-7-opus, gemini-2.5-pro, deepseek-v4, sora, veo, kling, whisper).
    x-features:
      - One bearer-token credential for 500+ models
      - OpenAI SDK drop-in (only base URL and key change)
      - Chat, embeddings, images, video, speech, and transcription
      - Streaming chat completions
      - Tool/function calling support
      - Pay-as-you-go billing with no monthly fees
      - Real-time usage analytics and per-key budget controls
      - Sub-400ms median latency, 99.9% availability
    x-use-cases:
      - Replacing single-vendor SDKs in SaaS apps
      - Cross-vendor model evaluation and A/B testing
      - Cost consolidation across an enterprise AI portfolio
      - Multi-modal pipelines combining text, image, video, and audio models
      - Internal model routers and prompt-experimentation tooling
common:
  - type: Website
    url: https://www.cometapi.com/
  - type: Documentation
    url: https://apidoc.cometapi.com/
  - type: HelpCenter
    url: https://apidoc.cometapi.com/help-center
  - type: GettingStarted
    url: https://apidoc.cometapi.com/how-to-use-cometapi-1792005m0
  - url: json-ld/cometapi-context.jsonld
    type: JSON-LD
  - url: json-schema/cometapi-chat-completion-schema.json
    type: JSONSchema
  - url: rules/cometapi-rules.yml
    type: Spectral
  - url: capabilities/cometapi-multi-model-capabilities.yml
    type: NaftikoCapabilities
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
