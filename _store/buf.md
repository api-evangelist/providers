---
aid: buf
name: Buf
description: Buf is a modern developer platform for Protocol Buffers and gRPC, providing a CLI toolchain, schema registry, and streaming infrastructure. It replaces traditional protoc-based workflows with linting, breaking change detection, code generation, remote plugins, and the Buf Schema Registry (BSR) for centralized schema distribution. Buf also offers Bufstream, a Kafka-compatible streaming platform built on Protobuf. Used by enterprises including EA, Intel, IBM, OpenAI, and Okta.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/buf/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Code Generation
  - gRPC
  - Kafka
  - Open Source
  - Protocol Buffers
  - Schema Registry
  - SDKs
  - Streaming
apis:
  - aid: buf:buf-schema-registry
    name: Buf Schema Registry (BSR)
    description: The Buf Schema Registry (BSR) is a centralized repository for managing, distributing, and documenting Protobuf schemas. It provides dependency management, generated SDKs in multiple languages, remote plugins for code generation, and a Reflection API for runtime schema discovery.
    humanURL: https://buf.build/product/bsr
    tags:
      - Code Generation
      - Protocol Buffers
      - Schema Registry
      - SDKs
    properties:
      - type: Documentation
        url: https://buf.build/docs/bsr/
      - type: Getting Started
        url: https://buf.build/docs/bsr/introduction/
      - type: Authentication
        url: https://buf.build/docs/bsr/authentication/
      - type: Reference
        url: https://buf.build/docs/reference/
  - aid: buf:buf-cli
    name: Buf CLI
    description: The Buf CLI is a local Protobuf development toolchain providing linting, breaking change detection, code generation, formatting, dependency management, and schema push/pull to the Buf Schema Registry. It replaces protoc with a faster, more developer-friendly interface.
    humanURL: https://buf.build/product/cli
    tags:
      - CLI
      - Code Generation
      - Linting
      - Protocol Buffers
    properties:
      - type: Documentation
        url: https://buf.build/docs/cli/
      - type: Getting Started
        url: https://buf.build/docs/tutorials/getting-started-with-buf-cli
      - type: GitHubRepository
        url: https://github.com/bufbuild/buf
  - aid: buf:bufstream
    name: Bufstream
    description: Bufstream is a Kafka-compatible streaming platform built on Protocol Buffers. It provides schema enforcement, Iceberg integration, and administrative tooling for managing Kafka-compatible streaming workloads with Protobuf as the data format.
    humanURL: https://buf.build/product/bufstream
    tags:
      - Kafka
      - Protocol Buffers
      - Streaming
    properties:
      - type: Documentation
        url: https://buf.build/docs/bufstream/
      - type: Getting Started
        url: https://buf.build/docs/bufstream/introduction/
common:
  - type: Website
    url: https://buf.build
  - type: Documentation
    url: https://buf.build/docs
  - type: GitHubOrganization
    url: https://github.com/bufbuild
  - type: GitHubRepository
    url: https://github.com/bufbuild/buf
  - type: Blog
    url: https://buf.build/blog
  - type: Pricing
    url: https://buf.build/pricing
  - type: SignUp
    url: https://buf.build/signup
  - type: Login
    url: https://buf.build/login
  - type: Contact
    url: https://buf.build/contact
  - type: TermsOfService
    url: https://buf.build/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://buf.build/legal/privacy-policy
  - type: Community
    url: https://buf.build/b/slack
  - type: SchemaRegistry
    url: https://buf.build/registry
  - name: Use Cases
    type: UseCases
    data:
      - name: Protobuf Schema Management
        url: https://buf.build/product/bsr
        features:
          - Centralized Schema Registry
          - Module Versioning
          - Dependency Management
          - Schema Discovery
          - API Documentation Generation
          - Breaking Change Prevention
      - name: Code Generation
        url: https://buf.build/docs/generate/
        features:
          - Multi-Language SDK Generation
          - Remote Plugin Execution
          - Go SDK Generation
          - Python SDK Generation
          - TypeScript/npm SDK Generation
          - Java/Maven SDK Generation
          - Rust/Cargo SDK Generation
          - Swift SDK Generation
          - .NET/NuGet SDK Generation
      - name: API Linting and Governance
        url: https://buf.build/docs/lint/
        features:
          - Protobuf Style Enforcement
          - Breaking Change Detection
          - CI/CD Integration
          - Custom Policy Rules
          - Field Deprecation Tracking
      - name: gRPC and ConnectRPC Development
        url: https://connectrpc.com/
        features:
          - gRPC Server Support
          - Connect Protocol
          - Browser-Compatible RPC
          - Mobile Client Support
          - Protovalidate Semantic Validation
  - name: Features
    type: Features
    data:
      - name: buf lint
        url: https://buf.build/docs/lint/
        features:
          - Style Guide Enforcement
          - Default and Custom Rules
          - CI/CD Compatible
          - Per-File Ignore Rules
      - name: buf breaking
        url: https://buf.build/docs/breaking/
        features:
          - Breaking Change Detection
          - Wire Compatibility Checks
          - Source Compatibility Checks
          - Git-Based Comparison
      - name: buf generate
        url: https://buf.build/docs/generate/
        features:
          - Multi-Language Code Generation
          - Remote Plugin Support
          - Managed Mode
          - Template Configuration
      - name: buf push / buf dep
        url: https://buf.build/docs/bsr/
        features:
          - Schema Publishing
          - Dependency Resolution
          - Module Locking
          - Version Tagging
      - name: Reflection API
        url: https://buf.build/docs/bsr/reflection/
        features:
          - Runtime Schema Discovery
          - gRPC Server Reflection
          - Prototransform Integration
      - name: Language Server Protocol
        url: https://buf.build/docs/cli/
        features:
          - IDE Integration
          - Inline Linting
          - Autocomplete Support
          - VS Code Compatible
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
