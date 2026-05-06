---
aid: aimlapi
url: https://raw.githubusercontent.com/api-evangelist/aimlapi/refs/heads/main/apis.yml
apis:
  - aid: aimlapi:aimlapi
    name: AIMLAPI
    tags:
      - LLM
      - Chat Completions
      - Image Generation
      - Video Generation
      - Speech
      - Embeddings
      - Vision
      - Music
      - OpenAI Compatible
      - API Gateway
    humanURL: https://aimlapi.com/
    properties:
      - url: https://docs.aimlapi.com/
        type: Documentation
      - url: https://docs.aimlapi.com/api-references/text-models
        type: APIReference
        title: Text Models API Reference
      - url: https://docs.aimlapi.com/api-references/image-models
        type: APIReference
        title: Image Generation API Reference
      - url: openapi/aimlapi-openapi.yml
        type: OpenAPI
      - url: https://docs.aimlapi.com/quickstart
        type: Quickstart
      - url: https://aimlapi.com/app/sign-up/
        type: SignUp
      - url: https://docs.aimlapi.com/faq
        type: FAQ
    description: Access 400+ AI models from 40+ providers via a single OpenAI-compatible REST API. Supports chat completions, image generation, video generation, speech models, embeddings, music generation, and vision tasks with streaming support and function calling.
name: AIMLAPI
tags:
  - Artificial Intelligence
  - Machine Learning
  - AI Models
  - LLM
  - Image Generation
  - Video Generation
  - Speech
  - Embeddings
  - API Gateway
  - Developer Tools
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://github.com/aimlapi
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://aimlapi.com/blog
    name: Explore AI with AIMLAPI Blog - Insights, Innovations, and Success Stories
    type: Blog
    description: 'null'
  - url: https://aimlapi.com/ai-ml-api-pricing
    name: Pricing
    type: Pricing
    description: 'null'
  - url: https://docs.aimlapi.com/
    name: Introduction | AI/ML API Documentation
    type: Documentation
    description: 'null'
  - name: Can I use API in Python? | AI/ML API Documentation
    description: 'null'
    url: https://docs.aimlapi.com/faq/can-i-use-api-in-python
    type: FAQ
  - name: 'AI/ML API Changelog: Latest Features and Improvements'
    description: 'null'
    url: https://aimlapi.com/changelog
    type: ChangeLog
  - name: AI/ML API - Sign up
    description: 'null'
    url: https://aimlapi.com/app/sign-up/
    type: SignUp
  - name: 'Join the AI/ML API Affiliate Program: Empower Innovation & Earn Rewards'
    description: 'null'
    url: https://aimlapi.com/affiliate
    type: Affiliate
  - name: Privacy Policy
    description: 'null'
    url: https://aimlapi.com/privacy-policy
    type: PrivacyPolicy
  - name: Terms and Conditions - aimlapi.com - 200+ AI Models via 1 API
    description: 'null'
    url: https://aimlapi.com/terms-and-conditions
    type: TermsOfService
  - type: Features
    data:
      - name: 400+ AI Models
        description: Access to 400+ models from OpenAI, Anthropic, Google, Meta, DeepSeek, Mistral, Stability AI, and 40+ providers.
      - name: OpenAI-Compatible API
        description: Drop-in replacement for OpenAI API — use existing OpenAI client libraries with AIMLAPI endpoint.
      - name: Text and Chat Completions
        description: Chat completions, completion, function calling, streaming, reasoning, and code generation.
      - name: Image Generation
        description: Generate images via DALL-E, Flux, Stable Diffusion, and other image generation models.
      - name: Video Generation
        description: Generate video via Sora 2, Runway, and other video generation models.
      - name: Speech Models
        description: Text-to-speech and speech-to-text transcription via Whisper and other speech models.
      - name: Music Generation
        description: AI music generation via dedicated music models.
      - name: Vision and OCR
        description: Image understanding, visual question answering, and OCR via vision-capable LLMs.
      - name: Embeddings
        description: Generate vector embeddings for semantic search and RAG applications.
      - name: Playground
        description: Online playground for experimenting with all available models without writing code.
  - type: UseCases
    data:
      - name: AI Chatbot Development
        description: Build conversational AI chatbots and virtual assistants using leading LLMs.
      - name: Content Generation
        description: Automate text, image, video, and music content generation for media and marketing.
      - name: RAG Applications
        description: Build retrieval-augmented generation applications using embeddings and LLMs.
      - name: Code Generation
        description: Integrate AI code generation and review capabilities into developer tools.
      - name: Document Processing
        description: Extract information and summarize documents using vision and LLM models.
      - name: Voice Applications
        description: Add speech-to-text transcription and text-to-speech synthesis to applications.
  - type: Integrations
    data:
      - name: OpenAI SDK
        description: Use the official OpenAI Python and Node.js SDKs with AIMLAPI base URL.
      - name: LangChain
        description: Integrate AIMLAPI models with LangChain for agentic AI workflows.
      - name: LlamaIndex
        description: Use AIMLAPI with LlamaIndex for RAG and document intelligence pipelines.
      - name: Vercel AI SDK
        description: Build AI-powered web apps using Vercel AI SDK with AIMLAPI as backend.
      - name: Python
        description: Native Python integration via requests library or OpenAI client.
      - name: Node.js
        description: Node.js integration via OpenAI npm package pointed at AIMLAPI endpoint.
  - name: AIMLAPI Spectral Rules
    url: rules/aimlapi-spectral-rules.yml
    type: SpectralRules
    description: Spectral ruleset enforcing AIMLAPI API conventions.
  - name: AIMLAPI AI Model Operations
    url: capabilities/ai-model-operations.yaml
    type: NaftikoCapability
    description: Naftiko workflow capability for AI model operations.
  - name: AIMLAPI Vocabulary
    url: vocabulary/aimlapi-vocabulary.yaml
    type: Vocabulary
    description: Taxonomy vocabulary for AIMLAPI APIs.
created: '2025-01-07'
modified: '2026-04-19'
position: Consuming
description: AIMLAPI is a unified AI model API gateway providing access to 400+ state-of-the-art AI models from OpenAI, Anthropic, Google, Meta, DeepSeek, Mistral, Stability AI, and 40+ other providers through a single OpenAI-compatible API. Supported modalities include text/chat LLMs, image generation, video generation, music generation, speech-to-text, text-to-speech, vision/OCR, embeddings, and 3D generation.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
