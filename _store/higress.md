---
aid: higress
name: Higress
description: Higress is a cloud-native API gateway built on Istio and Envoy, providing enterprise-grade API gateway capabilities including traffic management, security, observability, and AI plugin support. It is an open-source project under the CNCF ecosystem.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - Cloud Native
  - Istio
  - Kubernetes
url: https://raw.githubusercontent.com/api-evangelist/higress/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: higress:higress
    name: Higress
    description: Higress is a next-generation cloud-native API gateway that provides intelligent routing, traffic management, authentication, and observability capabilities for microservices architectures.
    humanURL: https://higress.io/en-us/
    tags:
      - API Gateway
      - Cloud Native
    properties:
      - type: Documentation
        url: https://higress.io/en-us/docs/
      - type: Getting Started
        url: https://higress.io/en-us/docs/user/quickstart
      - type: Reference
        url: https://higress.io/en-us/docs/ops/config/
      - type: Change Log
        url: https://github.com/alibaba/higress/releases
      - type: GitHubRepository
        url: https://github.com/alibaba/higress
  - aid: higress:higress-console-api
    name: Higress Console API
    description: The Higress Console API provides a RESTful management interface for configuring and administering a running Higress gateway instance. It supports management of ingress routes, service sources, TLS certificates, plugins, and gateway configuration through the built-in web console backend.
    humanURL: https://higress.io/en-us/docs/ops/api
    tags:
      - Admin
      - Configuration
      - Management
      - REST
    properties:
      - type: Documentation
        url: https://higress.io/en-us/docs/ops/api
      - type: GitHubRepository
        url: https://github.com/alibaba/higress-console
  - aid: higress:higress-ai-gateway
    name: Higress AI Gateway
    description: Higress AI Gateway extends the core Higress gateway with AI-specific capabilities including LLM proxy routing, multi-provider support for OpenAI-compatible APIs, prompt templating, token-based rate limiting, semantic caching, and AI observability. It enables teams to manage and govern traffic to large language model services.
    humanURL: https://higress.io/en-us/docs/plugins/ai/
    tags:
      - AI
      - API Gateway
      - Cloud Native
      - LLM
    properties:
      - type: Documentation
        url: https://higress.io/en-us/docs/plugins/ai/
      - type: Getting Started
        url: https://higress.io/en-us/docs/user/ai-proxy/
      - type: GitHubRepository
        url: https://github.com/alibaba/higress
  - aid: higress:higress-wasm-plugin-api
    name: Higress Wasm Plugin API
    description: The Higress Wasm Plugin API provides a WebAssembly-based extension interface for developing and deploying custom plugins on the Higress gateway. Plugins can be written in Go, Rust, C++, or any language that compiles to WebAssembly, and can intercept and transform HTTP requests and responses at the gateway level.
    humanURL: https://higress.io/en-us/docs/plugins/custom/
    tags:
      - Cloud Native
      - Extensions
      - Plugins
      - WebAssembly
    properties:
      - type: Documentation
        url: https://higress.io/en-us/docs/plugins/custom/
      - type: Reference
        url: https://higress.io/en-us/docs/plugins/custom/go-plugin/
      - type: GitHubRepository
        url: https://github.com/alibaba/higress
common:
  - type: Website
    url: https://higress.io/en-us/
  - type: Documentation
    url: https://higress.io/en-us/docs/
  - type: Getting Started
    url: https://higress.io/en-us/docs/user/quickstart
  - type: Blog
    url: https://higress.io/en-us/blog/
  - type: Change Log
    url: https://github.com/alibaba/higress/releases
  - type: GitHub Organization
    url: https://github.com/alibaba
  - type: GitHubRepository
    url: https://github.com/alibaba/higress
  - type: Issue Tracker
    url: https://github.com/alibaba/higress/issues
  - type: Community
    url: https://discord.gg/higress
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
