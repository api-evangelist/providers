---
aid: wasmedge
name: WasmEdge
description: WasmEdge is a lightweight, high-performance, and extensible WebAssembly runtime for cloud native, edge, and decentralized applications. It powers serverless apps, embedded functions, microservices, smart contracts, and IoT devices. WasmEdge is a CNCF sandbox project providing an LLVM-based AoT compiler for maximum performance, and supporting WASI extensions for non-blocking networking, database access, and AI inference via TensorFlow, PyTorch, and OpenVINO.
url: https://wasmedge.org
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - CNCF
  - Edge Computing
  - High Performance
  - Runtime
  - Serverless
  - Wasm
  - WebAssembly
created: '2026-03-26'
modified: '2026-05-03'
specificationVersion: '0.19'
type: Index
apis:
  - aid: wasmedge:wasmedge-c-api
    name: WasmEdge C API
    description: The WasmEdge C API provides a low-level interface for embedding the WasmEdge runtime into C/C++ host applications. It exposes the full WasmEdge runtime capabilities including module instantiation, function invocation, memory access, and plugin management.
    humanURL: https://wasmedge.org/docs/embed/c/intro/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://wasmedge.org/docs/embed/c/intro/
      - type: GitHubRepository
        url: https://github.com/WasmEdge/WasmEdge
    tags:
      - C API
      - Embedding
      - Low Level
  - aid: wasmedge:wasmedge-rust-sdk
    name: WasmEdge Rust SDK
    description: The WasmEdge Rust SDK enables embedding WasmEdge WebAssembly functions in Rust host applications. It provides idiomatic Rust bindings for the WasmEdge C API, supporting module loading, instantiation, function calls, host function definitions, and plugin integration.
    humanURL: https://wasmedge.org/docs/embed/rust/intro/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://wasmedge.org/docs/embed/rust/intro/
      - type: GitHubRepository
        url: https://github.com/WasmEdge/wasmedge-rust-sdk
    tags:
      - Rust
      - SDK
      - Embedding
  - aid: wasmedge:wasmedge-go-sdk
    name: WasmEdge Go SDK
    description: The WasmEdge Go SDK provides Go language bindings for embedding the WasmEdge runtime in Go applications. It enables loading and executing WebAssembly modules from Go, defining host functions, and managing WasmEdge configurations programmatically.
    humanURL: https://wasmedge.org/docs/embed/go/intro/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://wasmedge.org/docs/embed/go/intro/
      - type: GitHubRepository
        url: https://github.com/second-state/WasmEdge-go
    tags:
      - Go
      - SDK
      - Embedding
  - aid: wasmedge:wasmedge-nodejs-sdk
    name: WasmEdge Node.js SDK
    description: The WasmEdge Node.js SDK allows embedding and calling WebAssembly functions from Node.js applications. It provides bindings for executing Wasm modules within the WasmEdge runtime from JavaScript, enabling high-performance compute from Node.js services.
    humanURL: https://wasmedge.org/docs/embed/node/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://wasmedge.org/docs/embed/node/
    tags:
      - Node.js
      - JavaScript
      - SDK
      - Embedding
  - aid: wasmedge:wasmedge-plugin-system
    name: WasmEdge Plugin System
    description: WasmEdge's plugin system enables extending the runtime with custom host function packages. Plugins can be developed in Rust or C/C++ and loaded at runtime, providing capabilities like TensorFlow AI inference, image processing, database drivers, and WASI networking extensions.
    humanURL: https://wasmedge.org/docs/contribute/plugin/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://wasmedge.org/docs/contribute/plugin/
      - type: GitHubRepository
        url: https://github.com/WasmEdge/WasmEdge
    tags:
      - Plugins
      - Extensions
      - TensorFlow
      - AI
common:
  - type: Website
    url: https://wasmedge.org/
  - type: Documentation
    url: https://wasmedge.org/docs/
  - type: Getting Started
    url: https://wasmedge.org/docs/start/getting-started/
  - type: GitHubOrganization
    url: https://github.com/WasmEdge
  - type: GitHubRepository
    url: https://github.com/WasmEdge/WasmEdge
  - type: Blog
    url: https://wasmedge.org/blog/
  - type: Slack
    url: https://wasmedge.slack.com/
  - type: Discord
    url: https://discord.gg/U4B5sFTkFc
  - type: Vocabulary
    url: vocabulary/wasmedge-vocabulary.yml
  - type: JSON-LD
    url: json-ld/wasmedge-context.jsonld
  - type: JSONSchema
    url: json-schema/wasmedge-config-schema.json
  - type: JSONStructure
    url: json-structure/wasmedge-config-structure.json
  - type: Vocabulary
    url: vocabulary/wasmedge-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
