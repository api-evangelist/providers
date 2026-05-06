---
aid: spin
name: Spin
description: Spin is an open source framework by Fermyon for building and running fast, secure, and composable cloud microservices with WebAssembly. Spin provides a developer experience for creating event-driven serverless applications that compile to WebAssembly and run on any platform that supports the Spin runtime including local dev environments, Kubernetes (via SpinKube), and Fermyon Cloud.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Microservices
  - Serverless
  - WebAssembly
url: https://raw.githubusercontent.com/api-evangelist/spin/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: spin:spin-http-trigger-api
    name: Spin HTTP Trigger API
    description: The Spin HTTP Trigger API handles incoming HTTP requests and routes them to the appropriate Spin component. Components receive an HTTP request object and return an HTTP response. Supported via the Spin SDK in Rust, Go, Python, JavaScript, and other languages that target WASI.
    humanURL: https://spinframework.dev/v3/http-trigger
    tags:
      - HTTP
      - Trigger
      - WebAssembly
    properties:
      - type: Documentation
        url: https://spinframework.dev/v3/http-trigger
      - type: GitHubRepository
        url: https://github.com/fermyon/spin
  - aid: spin:spin-key-value-api
    name: Spin Key-Value Store API
    description: The Spin Key-Value Store API provides Spin components with access to a persistent key-value storage service. Components read, write, and delete key-value pairs using the Spin SDK. The underlying store can be an in-memory store (for development), Redis, or cloud-managed storage depending on the deployment target.
    humanURL: https://spinframework.dev/v3/kv-store-api
    tags:
      - Key-Value
      - Storage
      - WebAssembly
    properties:
      - type: Documentation
        url: https://spinframework.dev/v3/kv-store-api
      - type: GitHubRepository
        url: https://github.com/fermyon/spin
  - aid: spin:spin-sqlite-api
    name: Spin SQLite API
    description: The Spin SQLite API provides Spin components with access to an embedded relational database. Components can execute SQL queries and statements using the Spin SDK's SQLite interface, enabling structured data persistence within Spin applications.
    humanURL: https://spinframework.dev/v3/sqlite-api
    tags:
      - Database
      - SQLite
      - Storage
      - WebAssembly
    properties:
      - type: Documentation
        url: https://spinframework.dev/v3/sqlite-api
      - type: GitHubRepository
        url: https://github.com/fermyon/spin
  - aid: spin:spin-serverless-ai-api
    name: Spin Serverless AI API
    description: The Spin Serverless AI API enables Spin components to run AI inference using built-in language model support (Llama 2, CodeLlama, etc.) via the Spin SDK's infer() function. Components must declare the ai_models they need in spin.toml. Supported on Fermyon Cloud and SpinKube deployments.
    humanURL: https://spinframework.dev/v3/serverless-ai-tutorial
    tags:
      - AI
      - LLM
      - Machine Learning
      - WebAssembly
    properties:
      - type: Documentation
        url: https://spinframework.dev/v3/serverless-ai-tutorial
      - type: GitHubRepository
        url: https://github.com/fermyon/spin
  - aid: spin:spin-variables-api
    name: Spin Variables API
    description: The Spin Variables API provides runtime access to application configuration variables defined in spin.toml. Variables can be required or optional with defaults, and can be marked as secrets. At runtime, variables are resolved from environment variables, Vault, or other configured providers.
    humanURL: https://spinframework.dev/v3/variables
    tags:
      - Configuration
      - Variables
      - WebAssembly
    properties:
      - type: Documentation
        url: https://spinframework.dev/v3/variables
      - type: GitHubRepository
        url: https://github.com/fermyon/spin
common:
  - type: JSONSchema
    url: json-schema/spin-manifest.json
  - type: SpectralRules
    url: rules/spin-rules.yml
  - type: Vocabulary
    url: vocabulary/spin-vocabulary.yml
  - type: Website
    url: https://spinframework.dev/
  - type: Documentation
    url: https://spinframework.dev/v3/
  - type: GettingStarted
    url: https://spinframework.dev/v3/quickstart
  - type: GitHubOrganization
    url: https://github.com/fermyon
  - type: GitHubRepository
    url: https://github.com/fermyon/spin
  - type: Releases
    url: https://github.com/fermyon/spin/releases
  - type: RoadMap
    url: https://github.com/fermyon/spin/blob/main/ROADMAP.md
  - type: Community
    url: https://www.fermyon.com/community
  - type: Blog
    url: https://www.fermyon.com/blog
  - type: Discord
    url: https://discord.gg/AAFNfS7NGf
  - type: X
    url: https://twitter.com/fermyon
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
