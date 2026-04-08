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
created: '2025-11-19'
modified: '2026-04-07'
position: Consumer
description: API for running large language models locally.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

