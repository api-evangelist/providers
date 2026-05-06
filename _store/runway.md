---
aid: runway
name: Runway
description: Runway is an applied AI research company that builds generative AI tools for creative professionals. Their developer platform provides APIs for video generation, image generation, real-time conversational avatar experiences, media uploads, and audio synthesis powered by advanced generative models including Gen-4, Gen-4 Turbo, Gen-4.5, Gen-4 Aleph, Veo 3.1, Act Two, and GWM-1 (General World Model). The API uses asynchronous task processing with Bearer token authentication.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Video Generation
  - Image Generation
  - Artificial Intelligence
  - Machine Learning
  - Generative AI
  - Avatars
  - Characters
  - WebRTC
  - Creative Tools
url: https://raw.githubusercontent.com/api-evangelist/runway/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: runway:video-generation
    name: Runway Video Generation API
    description: The Runway Video Generation API allows developers to generate videos from text prompts, images, or existing videos using Gen-4, Gen-4 Turbo, Gen-4.5, Gen-4 Aleph, Veo 3.1, and Veo 3.1 Fast models. Supports text-to-video, image-to-video, video-to-video, character performance (Act Two), lip sync (28+ languages), video upscale, frame interpolation, and sound effect generation. Tasks are processed asynchronously with polling via task ID. Authentication via Bearer token plus X-Runway-Version header set to 2024-11-06.
    humanURL: https://docs.dev.runwayml.com/api/
    baseURL: https://api.dev.runwayml.com/v1
    tags:
      - Video Generation
      - Artificial Intelligence
      - Machine Learning
      - Text To Video
      - Image To Video
      - Generative AI
      - Gen-4
    properties:
      - type: Documentation
        url: https://docs.dev.runwayml.com/api/
      - type: OpenAPI
        url: openapi/runway-video-generation-openapi.yml
      - type: Spectral Rules
        url: rules/runway-rules.yml
      - type: NaftikoCapability
        url: capabilities/generative-media-production.yaml
  - aid: runway:image-generation
    name: Runway Image Generation API
    description: The Runway Image Generation API provides text-to-image generation using the Gen-4 Image and Gemini 3 Pro Image models. Accepts text prompts up to 1000 characters and supports multiple aspect ratios. Also includes task status polling. Uses the same asynchronous task pattern and Bearer token authentication as the video API. As of April 2026, Gemini 3 Pro Image supports up to 5,500-character prompts and 14 reference images.
    humanURL: https://docs.dev.runwayml.com/api/
    baseURL: https://api.dev.runwayml.com/v1
    tags:
      - Image Generation
      - Artificial Intelligence
      - Machine Learning
      - Text To Image
      - Generative AI
      - Gen-4
    properties:
      - type: Documentation
        url: https://docs.dev.runwayml.com/api/
      - type: OpenAPI
        url: openapi/runway-image-generation-openapi.yml
      - type: Spectral Rules
        url: rules/runway-rules.yml
      - type: NaftikoCapability
        url: capabilities/generative-media-production.yaml
  - aid: runway:characters
    name: Runway Characters API
    description: The Runway Characters API enables developers to build real-time conversational avatars powered by GWM-1 (Runway's General World Model). Avatars are fully custom conversational video agents created from a single reference image with no fine-tuning. Supports photorealistic or animated styles, human or non-human appearances. Manages avatars, real-time WebRTC sessions (max 5 minutes), and knowledge documents (up to 50,000 tokens per avatar). Authentication via Bearer token.
    humanURL: https://docs.dev.runwayml.com/characters/
    baseURL: https://api.dev.runwayml.com/v1
    tags:
      - Avatars
      - Characters
      - Conversational AI
      - Real Time
      - WebRTC
      - Video Agents
      - Generative AI
      - GWM-1
    properties:
      - type: Documentation
        url: https://docs.dev.runwayml.com/characters/
      - type: OpenAPI
        url: openapi/runway-characters-openapi.yml
      - type: AsyncAPI
        url: asyncapi/runway-characters-asyncapi.yml
      - type: NaftikoCapability
        url: capabilities/generative-media-production.yaml
      - type: Spectral Rules
        url: rules/runway-rules.yml
  - aid: runway:python-sdk
    name: Runway Python SDK
    description: The Runway Python SDK provides a convenient Python library for interacting with the Runway API. Supports Python 3.8+ with type annotations compatible with MyPy. Includes automatic retries, best-practice error handling, and type safety to simplify integration of Runway's video and image generation capabilities into Python applications.
    humanURL: https://docs.dev.runwayml.com/api-details/sdks/
    tags:
      - Python
      - SDK
      - Libraries
      - Artificial Intelligence
      - Video Generation
    properties:
      - type: Documentation
        url: https://docs.dev.runwayml.com/api-details/sdks/
      - type: GitHub Repository
        url: https://github.com/runwayml/sdk-python
  - aid: runway:nodejs-sdk
    name: Runway Node.js SDK
    description: The Runway Node.js SDK provides a JavaScript and TypeScript library for integrating with the Runway API. Supports Node.js 18+ with TypeScript bindings, automatic retries, and best-practice error handling. Install via npm, yarn, or pnpm.
    humanURL: https://docs.dev.runwayml.com/api-details/sdks/
    tags:
      - Node.js
      - JavaScript
      - TypeScript
      - SDK
      - Libraries
      - Video Generation
    properties:
      - type: Documentation
        url: https://docs.dev.runwayml.com/api-details/sdks/
      - type: GitHub Repository
        url: https://github.com/runwayml/sdk-node
common:
  - type: Portal
    url: https://docs.dev.runwayml.com/
  - type: Documentation
    url: https://docs.dev.runwayml.com/api/
  - type: Website
    url: https://runwayml.com/
  - type: Developer Portal
    url: https://dev.runwayml.com/
  - type: Privacy Policy
    url: https://runwayml.com/privacy-policy
  - type: Terms Of Service
    url: https://runwayml.com/terms-of-use
  - type: Blog
    url: https://runwayml.com/blog
  - type: Login
    url: https://app.runwayml.com/
  - type: GitHub Organization
    url: https://github.com/runwayml
  - type: Changelog
    url: https://docs.dev.runwayml.com/api-details/api_changelog/
  - type: Vocabulary
    url: vocabulary/runway-vocabulary.yml
  - type: JSONLD
    url: json-ld/runway-context.jsonld
  - type: Features
    data:
      - 'Free: 125 one-time credits with Gen-4 Turbo image'
      - 'Standard at $12/mo annual: 625 credits, all video models'
      - 'Pro at $28/mo: 2,250 credits, custom voices'
      - 'Unlimited at $76/mo: 2,250 credits + unlimited Explore Mode'
      - 'Enterprise: SSO, custom org spaces, Workspace Analytics'
      - Gen-4.5, Gen-4, Gen-4 Turbo video generation
      - Image generation (Gen-4, Gemini 3 Pro/2.5)
      - Text-to-Speech with custom voices
      - Lip Sync
      - Upscaling and watermark removal
      - REST API for video/image generation
      - Webhooks for completion notification
      - OAuth 2.0 + API tokens
      - Asset storage (5 GB Free, 100/500 GB paid)
      - Video editor with unlimited projects on paid
      - Enterprise integrations with internal tools
    sources:
      - https://runwayml.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
