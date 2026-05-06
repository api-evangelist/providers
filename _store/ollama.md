---
aid: ollama
url: https://raw.githubusercontent.com/api-evangelist/ollama/refs/heads/main/apis.yml
apis:
  - aid: ollama:ollama-api
    name: Ollama API
    tags:
      - Inference
      - Large Language Models
      - Local AI
      - Models
    humanURL: https://docs.ollama.com/api/introduction
    baseURL: http://localhost:11434/api
    properties:
      - url: https://docs.ollama.com/
        type: Documentation
      - url: https://docs.ollama.com/openapi.yaml
        type: OpenAPI
      - url: https://docs.ollama.com/api/introduction
        type: Getting Started
      - url: https://docs.ollama.com/api/authentication
        type: Authentication
      - url: https://docs.ollama.com/api/generate
        type: Documentation
      - url: https://docs.ollama.com/api/chat
        type: Documentation
      - url: https://docs.ollama.com/api/embed
        type: Documentation
      - url: https://docs.ollama.com/api/tags
        type: Documentation
      - url: https://docs.ollama.com/api/ps
        type: Documentation
      - url: https://docs.ollama.com/api/create
        type: Documentation
      - url: https://docs.ollama.com/api/pull
        type: Documentation
      - url: https://docs.ollama.com/api/push
        type: Documentation
      - url: https://docs.ollama.com/api/copy
        type: Documentation
      - url: https://docs.ollama.com/api/delete
        type: Documentation
      - url: https://docs.ollama.com/api/show
        type: Documentation
      - url: https://docs.ollama.com/api/streaming
        type: Documentation
      - url: https://docs.ollama.com/api/errors
        type: Documentation
      - url: https://docs.ollama.com/api/usage
        type: Documentation
      - url: https://docs.ollama.com/api/blobs
        type: Documentation
      - url: https://docs.ollama.com/api/version
        type: Documentation
    description: Ollama provides a REST API for running and managing large language models locally. The API supports text generation, chat completions, embeddings, model management, and streaming responses. It serves as the primary interface for interacting with models running on the Ollama inference engine at localhost:11434.
  - aid: ollama:ollama-openai-compatibility-api
    name: Ollama OpenAI Compatibility API
    tags:
      - Chat
      - Compatibility
      - Large Language Models
      - OpenAI
    humanURL: https://docs.ollama.com/api/openai-compatibility
    baseURL: http://localhost:11434/v1
    properties:
      - url: https://docs.ollama.com/api/openai-compatibility
        type: Documentation
      - url: https://ollama.com/blog/openai-compatibility
        type: Blog
    description: Ollama provides compatibility with parts of the OpenAI API, allowing existing applications built for OpenAI to connect to locally-running models through Ollama. Supported endpoints include chat completions, completions, embeddings, models, and the Responses API.
  - aid: ollama:ollama-anthropic-compatibility-api
    name: Ollama Anthropic Compatibility API
    tags:
      - Anthropic
      - Chat
      - Compatibility
      - Large Language Models
    humanURL: https://docs.ollama.com/api/anthropic-compatibility
    baseURL: http://localhost:11434
    properties:
      - url: https://docs.ollama.com/api/anthropic-compatibility
        type: Documentation
      - url: https://ollama.com/blog/claude
        type: Blog
    description: Ollama provides compatibility with the Anthropic Messages API, enabling tools like Claude Code to work with locally-running open-source models. Supports messages, streaming, system prompts, tool calling, extended thinking, and vision input.
  - aid: ollama:ollama-cloud-api
    name: Ollama Cloud API
    tags:
      - Cloud
      - Inference
      - Large Language Models
    humanURL: https://docs.ollama.com/cloud
    baseURL: https://ollama.com/api
    properties:
      - url: https://docs.ollama.com/cloud
        type: Documentation
      - url: https://ollama.com/cloud
        type: Getting Started
      - url: https://ollama.com/pricing
        type: Pricing
      - url: https://ollama.com/settings/keys
        type: Authentication
      - url: https://ollama.com/search?c=cloud
        type: Models
    description: Ollama Cloud provides cloud-hosted inference for large language models, giving access to larger models and faster responses without requiring a powerful local GPU. Cloud models are accessed through the same API interface as local models, with requests encrypted in transit and no storage of prompts or outputs.
name: Ollama
tags:
  - Artificial Intelligence
  - Large Language Models
  - Models
type: Index
image: https://ollama.ai/public/ollama.png
access: 3rd-Party
common:
  - url: https://ollama.com/
    name: Ollama
    type: Website
    description: 'null'
  - url: https://docs.ollama.com/
    name: Ollamas documentation - Ollama
    type: Documentation
    description: 'null'
  - url: https://docs.ollama.com/faq
    name: FAQ - Ollama
    type: FAQ
    description: 'null'
  - url: https://signin.ollama.com/?client_id=client_01JX0QMHD43PFFCCNXH82A6K8B&redirect_uri=https%3A%2F%2Follama.com%2Fauth%2Fcallback&authorization_session_id=01KE5QZJQP6W24EJGN9TYDR5K8
    name: Sign in
    type: Login
    description: 'null'
  - url: https://signin.ollama.com/sign-up?redirect_uri=https%3A%2F%2Follama.com%2Fauth%2Fcallback&authorization_session_id=01KE5QZJQP6W24EJGN9TYDR5K8
    name: Sign up
    type: SignUp
    description: 'null'
  - url: https://ollama.com/cloud
    name: Cloud  Ollama
    type: Pricing
    description: 'null'
  - url: https://github.com/ollama/ollama
    type: GitHub
  - url: https://ollama.ai/blog
    type: Blog
  - url: https://ollama.ai/library
    type: Models
  - url: https://docs.ollama.com/openapi.yaml
    type: OpenAPI
  - url: https://docs.ollama.com/quickstart
    type: GettingStarted
  - url: https://docs.ollama.com/api/authentication
    type: Authentication
  - url: https://ollama.com/pricing
    type: Pricing
  - url: https://ollama.com/download
    type: Downloads
  - url: https://ollama.com/search
    type: Models
  - url: https://ollama.com/blog
    type: Blog
  - url: https://github.com/ollama/ollama/releases
    type: ChangeLog
  - url: https://github.com/ollama/ollama/security
    type: Security
  - url: https://github.com/ollama/ollama-python
    type: PythonSDK
  - url: https://github.com/ollama/ollama-js
    type: JavaScriptSDK
  - url: https://discord.gg/ollama
    type: Discord
  - url: https://reddit.com/r/ollama
    type: Reddit
  - url: https://twitter.com/ollama
    type: X
  - url: https://www.linkedin.com/company/ollama
    type: LinkedIn
  - url: https://docs.ollama.com/capabilities/tool-calling
    type: Documentation
  - url: https://docs.ollama.com/capabilities/structured-outputs
    type: Documentation
  - url: https://docs.ollama.com/capabilities/vision
    type: Documentation
  - url: https://docs.ollama.com/capabilities/embeddings
    type: Documentation
  - url: https://docs.ollama.com/capabilities/thinking
    type: Documentation
  - url: https://docs.ollama.com/capabilities/web-search
    type: Documentation
  - url: https://docs.ollama.com/capabilities/streaming
    type: Documentation
  - url: https://docs.ollama.com/integrations
    type: Integrations
  - url: https://docs.ollama.com/docker
    type: Docker
  - url: https://docs.ollama.com/modelfile
    type: Documentation
  - url: https://docs.ollama.com/cli
    type: CLI
  - url: https://docs.ollama.com/gpu
    type: Documentation
  - url: https://docs.ollama.com/troubleshooting
    type: Troubleshooting
  - url: https://docs.ollama.com/import
    type: Documentation
  - url: https://docs.ollama.com/context-length
    type: Documentation
  - url: https://github.com/ollama/ollama-dart
    type: Dart SDK
  - url: https://github.com/ollama/ollama-swift
    type: Swift SDK
  - url: https://stackoverflow.com/questions/tagged/ollama
    type: Stack Overflow
  - url: https://www.youtube.com/@Ollama-AI
    type: YouTube
  - url: https://github.com/ollama
    type: GitHub Organization
  - url: https://github.com/ollama/ollama/issues
    type: Issue Tracker
  - url: https://ollama.com/events
    type: Events
  - url: https://pkg.go.dev/github.com/ollama/ollama/api
    type: Go SDK
  - url: https://docs.ollama.com/llms.txt
    type: Documentation
  - url: https://docs.ollama.com/linux
    type: Documentation
  - url: https://docs.ollama.com/macos
    type: Documentation
  - url: https://docs.ollama.com/windows
    type: Documentation
created: '2025-11-19'
modified: '2026-04-28'
position: Consumer
description: API for running large language models locally.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
