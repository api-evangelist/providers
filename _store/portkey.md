---
aid: portkey
url: https://raw.githubusercontent.com/api-evangelist/portkey/refs/heads/main/apis.yml
apis:
  - aid: portkey:portkey
    name: Portkey
    tags:
      - AI Gateways
      - Governance
      - Guardrails
      - Observability
      - Prompt Management
    humanURL: https://portkey.ai/
    properties:
      - url: https://portkey.ai/docs/introduction/what-is-portkey
        type: Documentation
      - url: https://portkey.ai/docs/api-reference/inference-api/chat
        type: APIReference
      - url: openapi/portkey-openapi.yml
        type: OpenAPI
      - url: https://portkey.ai/docs/guides/getting-started/getting-started-with-ai-gateway
        type: GettingStarted
    description: Portkey equips AI teams with everything they need to go to production - Gateway, Observability, Guardrails, Governance, and Prompt Management, all in one platform.
  - aid: portkey:portkey-inference-api
    name: Portkey Inference API
    tags:
      - AI Gateways
      - Assistants
      - Audio
      - Batch
      - Chat Completions
      - Completions
      - Embeddings
      - Fine-Tuning
      - Images
      - Inference
      - Moderations
    humanURL: https://portkey.ai/docs/product/ai-gateway/universal-api
    baseURL: https://api.portkey.ai/v1
    properties:
      - url: https://portkey.ai/docs/api-reference/inference-api/chat
        type: APIReference
      - url: https://portkey.ai/docs/api-reference/inference-api/completions
        type: APIReference
      - url: https://portkey.ai/docs/api-reference/inference-api/embeddings
        type: APIReference
      - url: openapi/portkey-openapi.yml
        type: OpenAPI
    description: Portkey Inference API provides a universal API for routing to 200+ LLMs across chat completions, completions, embeddings, images, audio, assistants, fine-tuning, batch processing, and moderations endpoints with a single unified interface. Supports OpenAI, Anthropic, and Portkey API formats with automatic translation between providers.
  - aid: portkey:portkey-admin-api
    name: Portkey Admin API
    tags:
      - Administration
      - Analytics
      - API Keys
      - Audit Logs
      - Configs
      - Logs
      - Rate Limits
      - Users
      - Virtual Keys
      - Workspaces
    humanURL: https://portkey.ai/docs/api-reference/admin-api/introduction
    baseURL: https://api.portkey.ai/v1
    properties:
      - url: https://portkey.ai/docs/api-reference/admin-api/introduction
        type: APIReference
      - url: openapi/portkey-openapi.yml
        type: OpenAPI
    description: Portkey Admin API enables programmatic management of Portkey organizations and workspaces, including resource management for configs, virtual keys, and API keys, analytics and monitoring for usage statistics and performance trends, and user and workspace administration for managing accounts, permissions, and team membership. Includes audit logging of all administrative operations.
name: Portkey
tags:
  - AI Gateways
  - Gateways
  - Governance
  - Guardrails
  - Observability
  - Prompt Management
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://portkey.ai/
    name: Production Stack for Gen AI Builders|Portkey
    type: Website
    description: 'null'
  - url: https://portkey.ai/docs/introduction/what-is-portkey
    name: What is Portkey? - Portkey Docs
    type: Documentation
    description: 'null'
  - url: https://portkey.ai/docs/integrations/ecosystem
    name: Integrations - Portkey Docs
    type: Integrations
    description: 'null'
  - url: https://portkey.ai/docs/changelog/2025/july
    name: July - Portkey Docs
    type: ChangeLog
    description: 'null'
  - url: https://portkey.ai/blog
    name: LLMs in Prod Blog ● Portkey
    type: Blog
    description: 'null'
  - url: https://status.portkey.ai/
    name: Portkey AI status
    type: Status
    description: 'null'
  - url: https://portkey.ai/pricing
    name: Portkey | Control Panel for Production AI
    type: Pricing
    description: 'null'
  - url: https://portkey.ai/privacy-policy
    name: Privacy Policy | Portkey
    type: PrivacyPolicy
    description: 'null'
  - url: https://portkey.ai/terms
    name: Portkey | Control Panel for Production AI
    type: TermsOfService
    description: 'null'
  - url: https://new.portkey.ai/login
    name: Portkey Login
    type: Login
    description: 'null'
  - url: https://portkey.ai/docs/guides/getting-started/getting-started-with-ai-gateway
    name: Getting Started with AI Gateway - Portkey Docs
    type: GettingStarted
    description: 'null'
  - url: https://portkey.ai/docs/api-reference/inference-api/chat
    name: Portkey API Reference - Chat
    type: APIReference
    description: 'null'
  - url: https://portkey.ai/docs/api-reference/admin-api/introduction
    name: Portkey Admin API Reference
    type: APIReference
    description: 'null'
  - url: https://github.com/Portkey-AI/openapi
    name: Portkey OpenAPI Specification
    type: OpenAPI
    description: 'null'
  - url: https://github.com/Portkey-AI/gateway
    name: Portkey AI Gateway - Open Source
    type: GitHubOrg
    description: 'null'
  - url: https://github.com/Portkey-AI/portkey-python-sdk
    name: Portkey Python SDK - GitHub
    type: GitHubOrg
    description: 'null'
  - url: https://github.com/Portkey-AI/portkey-node-sdk
    name: Portkey Node.js SDK - GitHub
    type: GitHubOrg
    description: 'null'
  - url: https://pypi.org/project/portkey-ai/
    name: portkey-ai - PyPI
    type: PythonPackage
    description: 'null'
  - url: https://www.npmjs.com/package/portkey-ai
    name: portkey-ai - npm
    type: NodePackage
    description: 'null'
  - url: https://portkey.ai/docs/api-reference/portkey-sdk-client
    name: Portkey SDK Client - Portkey Docs
    type: SDK
    description: 'null'
  - url: https://portkey.ai/docs/support/developer-forum
    name: Developer Forum - Portkey Docs
    type: Forum
    description: 'null'
  - url: https://portkey.ai/features/security-compliance
    name: Enterprise-grade Security and Compliance - Portkey
    type: Security
    description: 'null'
  - url: https://portkey.ai/features/ai-gateway
    name: Enterprise-grade AI Gateway - Portkey
    type: Features
    description: 'null'
  - url: https://portkey.ai/features/observability
    name: Full-stack Observability for AI Apps - Portkey
    type: Observability
    description: 'null'
  - url: https://portkey.ai/features/guardrails
    name: Safeguard Your AI Requests with Guardrails - Portkey
    type: Guardrails
    description: 'null'
  - url: https://portkey.ai/docs/product/guardrails
    name: Guardrails - Portkey Docs
    type: Documentation
    description: 'null'
  - url: https://portkey.ai/docs/api-reference/inference-api/supported-providers
    name: Supported Providers - Portkey Docs
    type: Providers
    description: 'null'
  - url: https://www.linkedin.com/company/portkey-ai
    name: Portkey AI on LinkedIn
    type: LinkedIn
    description: 'null'
created: '2025-08-19'
modified: '2026-04-28'
position: Consumer
segments:
  - Gateways
description: Portkey equips AI teams with everything they need to go to production - Gateway, Observability, Guardrails, Governance, and Prompt Management, all in one platform.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
