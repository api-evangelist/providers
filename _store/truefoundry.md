---
aid: truefoundry
name: TrueFoundry
description: TrueFoundry is a Kubernetes-native enterprise AI platform for deploying and managing agentic AI workloads. It provides an AI Gateway, MCP Gateway, model serving, fine-tuning, and a full MLOps platform that works across on-premises, VPC, hybrid, or public cloud environments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Platform
  - Enterprise AI
  - Kubernetes
  - LLM Gateway
  - MLOps
url: https://raw.githubusercontent.com/api-evangelist/truefoundry/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: truefoundry:truefoundry-ai-gateway-api
    name: TrueFoundry AI Gateway API
    description: The TrueFoundry AI Gateway API is a proxy layer that sits between applications and LLM providers, enabling unified access to 1000+ language models through a single OpenAI-compatible endpoint. It supports chat completions, embeddings, image generation, audio processing, batch operations, file management, content moderation, and model management with centralized authentication, rate limiting, budget controls, and observability.
    humanURL: https://www.truefoundry.com/docs/ai-gateway/intro-to-llm-gateway
    baseURL: https://gateway.truefoundry.ai/api/llm
    tags:
      - AI Gateway
      - Chat Completions
      - Embeddings
      - LLM
    properties:
      - type: Documentation
        url: https://www.truefoundry.com/docs/ai-gateway/intro-to-llm-gateway
      - type: Getting Started
        url: https://www.truefoundry.com/docs/ai-gateway/quick-start
      - type: Authentication
        url: https://www.truefoundry.com/docs/ai-gateway/authentication
      - type: Reference
        url: https://www.truefoundry.com/docs/api-reference
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/truefoundry/refs/heads/main/openapi/truefoundry-ai-gateway-openapi.yml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/truefoundry/refs/heads/main/rules/truefoundry-rules.yml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/truefoundry/refs/heads/main/capabilities/llm-operations.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/truefoundry/refs/heads/main/json-schema/truefoundry-chat-completion-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/truefoundry/refs/heads/main/json-ld/truefoundry-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/truefoundry/refs/heads/main/vocabulary/truefoundry-vocabulary.yml
  - aid: truefoundry:truefoundry-mcp-gateway-api
    name: TrueFoundry MCP Gateway API
    description: The TrueFoundry MCP (Model Context Protocol) Gateway provides a centralized registry and proxy for managing MCP servers accessible to AI agents. It handles authentication, access control, schema validation, and tool orchestration across multiple MCP servers, supporting header auth, OAuth2, and token passthrough authentication modes.
    humanURL: https://www.truefoundry.com/docs/ai-gateway/mcp/mcp-server-getting-started
    baseURL: https://gateway.truefoundry.ai
    tags:
      - Agent Tools
      - AI Agents
      - MCP
      - Tool Registry
    properties:
      - type: Documentation
        url: https://www.truefoundry.com/docs/ai-gateway/mcp/mcp-server-getting-started
      - type: Authentication
        url: https://www.truefoundry.com/docs/ai-gateway/mcp/mcp-gateway-auth-security
  - aid: truefoundry:truefoundry-platform-api
    name: TrueFoundry Platform API
    description: The TrueFoundry Platform API provides programmatic access to the TrueFoundry MLOps platform for managing applications, deployments, users, and infrastructure resources. It enables automation of service deployments, training jobs, model registry operations, and workflow orchestration across Kubernetes-based compute environments.
    humanURL: https://www.truefoundry.com/docs
    baseURL: https://app.truefoundry.com/api
    tags:
      - Deployments
      - Management
      - MLOps
      - Platform
    properties:
      - type: Documentation
        url: https://www.truefoundry.com/docs
      - type: Client Libraries
        url: https://github.com/truefoundry/truefoundry-python-sdk
  - aid: truefoundry:truefoundry-model-serving-api
    name: TrueFoundry Model Serving API
    description: TrueFoundry's Model Serving capability enables deployment and management of LLM and embedding models using backends like vLLM and Triton on Kubernetes infrastructure. It provides APIs for deploying models from a community registry of 1000+ configurations, managing inference endpoints, and controlling autoscaling behavior including scale-to-zero.
    humanURL: https://www.truefoundry.com/docs/introduction-to-a-service
    baseURL: https://app.truefoundry.com
    tags:
      - Kubernetes
      - LLM Inference
      - MLOps
      - Model Serving
    properties:
      - type: Documentation
        url: https://www.truefoundry.com/docs/introduction-to-a-service
  - aid: truefoundry:truefoundry-model-registry-api
    name: TrueFoundry Model Registry API
    description: The TrueFoundry Model Registry provides a versioned repository for storing and managing machine learning models backed by cloud storage such as S3, GCS, Azure Blob, or Minio. It supports programmatic model logging via the truefoundry.ml Python client, multi-framework model formats, and automatic versioning with metadata management.
    humanURL: https://www.truefoundry.com/docs/model-registry
    baseURL: https://app.truefoundry.com
    tags:
      - Machine Learning
      - MLOps
      - Model Registry
      - Versioning
    properties:
      - type: Documentation
        url: https://www.truefoundry.com/docs/model-registry
common:
  - type: Website
    url: https://www.truefoundry.com/
  - type: Documentation
    url: https://www.truefoundry.com/docs
  - type: Getting Started
    url: https://www.truefoundry.com/docs/ai-gateway/quick-start
  - type: Authentication
    url: https://www.truefoundry.com/docs/ai-gateway/authentication
  - type: Pricing
    url: https://www.truefoundry.com/pricing
  - type: Blog
    url: https://www.truefoundry.com/blog
  - type: Change Log
    url: https://www.truefoundry.com/docs/changelog
  - type: GitHub Organization
    url: https://github.com/truefoundry
  - type: GitHubRepository
    url: https://github.com/truefoundry/truefoundry-python-sdk
  - type: SDKs
    url: https://github.com/truefoundry/truefoundry-python-sdk
  - type: Sign Up
    url: https://app.truefoundry.com/signup
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
