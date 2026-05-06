---
aid: llama
name: Llama
description: Llama is Meta's family of open-weight large language models, available for download, self-hosting, and via Meta's hosted Llama API for chat completions, text generation, and embeddings. The ecosystem also includes the open-source llama-models, llama-stack, and PurpleLlama safety projects on GitHub.
type: Index
position: Producing
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Large Language Models
  - Machine Learning
  - Meta
  - Open Source
  - LLM
  - Natural Language Processing
url: https://raw.githubusercontent.com/api-evangelist/llama/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: llama:llama-api
    name: Llama API
    description: Meta's hosted REST API providing access to Llama large language models for chat completions, text generation, and embeddings. Authentication is via API key issued through llama.developer.meta.com.
    humanURL: https://llama.developer.meta.com/docs/overview/
    baseURL: https://api.llama.com
    tags:
      - LLM
      - Chat
      - Embeddings
      - AI
    properties:
      - type: Documentation
        url: https://llama.developer.meta.com/docs/overview/
      - type: GettingStarted
        url: https://llama.developer.meta.com/docs/getting-started/
      - type: Portal
        url: https://llama.developer.meta.com/
      - type: Waitlist
        url: https://llama.developer.meta.com/join_waitlist
  - aid: llama:llama-models
    name: Llama Models (open weights)
    description: Open-weight Llama model family available for direct download and self-hosted inference, distributed under Meta's Llama Community License.
    humanURL: https://www.llama.com/llama-downloads/
    tags:
      - Open Source
      - Models
      - Self-Hosted
    properties:
      - type: Documentation
        url: https://www.llama.com/llama-downloads/
      - type: GitHub
        url: https://github.com/meta-llama/llama-models
      - type: License
        url: https://www.llama.com/llama3/license/
  - aid: llama:llama-stack
    name: Llama Stack
    description: Open-source framework standardizing the building blocks for Llama-based generative AI applications, including inference, safety, agents, and evaluation, with REST and SDK access across multiple providers.
    humanURL: https://github.com/meta-llama/llama-stack
    tags:
      - Framework
      - Agents
      - SDK
      - Open Source
    properties:
      - type: Documentation
        url: https://llama-stack.readthedocs.io/
      - type: GitHub
        url: https://github.com/meta-llama/llama-stack
  - aid: llama:purple-llama
    name: PurpleLlama
    description: Open-source project providing tools and evaluations for assessing and improving the safety and security of generative AI models, including Llama Guard and CyberSecEval.
    humanURL: https://github.com/meta-llama/PurpleLlama
    tags:
      - Safety
      - Security
      - Open Source
    properties:
      - type: Documentation
        url: https://github.com/meta-llama/PurpleLlama
      - type: GitHub
        url: https://github.com/meta-llama/PurpleLlama
common:
  - type: Website
    url: https://www.llama.com/
  - type: Documentation
    url: https://llama.developer.meta.com/docs/overview/
  - type: Portal
    url: https://llama.developer.meta.com/
  - type: Reference
    url: https://ai.meta.com/llama/
  - type: GitHubOrganization
    url: https://github.com/meta-llama
  - type: License
    url: https://www.llama.com/llama3/license/
  - type: AcceptableUsePolicy
    url: https://www.llama.com/llama3/use-policy/
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
