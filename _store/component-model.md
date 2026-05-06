---
aid: component-model
url: https://raw.githubusercontent.com/api-evangelist/component-model/refs/heads/main/apis.yml
name: Component Model
x-type: standard
description: The WebAssembly Component Model is a broad-reaching architecture for building interoperable WebAssembly libraries, applications, and environments. It defines components as portable, sandboxed units of code that can compose with each other across language and runtime boundaries. The model introduces interfaces, worlds, and the WebAssembly Interface Type (WIT) language, along with a canonical ABI, binary and text formats, and a concurrency model. The Component Model underpins the WebAssembly System Interface (WASI) Preview 2 and is the foundation for portable Wasm on browsers, servers, edge, and embedded environments.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - ABI
  - Bytecode Alliance
  - Component
  - Interface
  - Modular
  - Specification
  - WASI
  - WebAssembly
  - WIT
  - World
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: component-model:specification
    name: WebAssembly Component Model Specification
    description: The Component Model specification repository under the W3C WebAssembly Community Group. Contains design documents, the formal specification drafts, the WIT grammar, the canonical ABI, and the binary and text formats that define a WebAssembly component.
    humanURL: https://github.com/WebAssembly/component-model
    baseURL: https://github.com/WebAssembly
    tags:
      - Specification
      - W3C
      - WebAssembly
    properties:
      - type: GitHubRepository
        url: https://github.com/WebAssembly/component-model
      - type: Documentation
        url: https://github.com/WebAssembly/component-model/blob/main/design/mvp/Explainer.md
      - type: Specification
        url: https://github.com/WebAssembly/component-model/tree/main/design/mvp
      - type: Reference
        url: https://github.com/WebAssembly/component-model/blob/main/design/mvp/CanonicalABI.md
      - type: Reference
        url: https://github.com/WebAssembly/component-model/blob/main/design/mvp/WIT.md
    x-features:
      - Defines components, interfaces, and worlds
      - Introduces WIT, the WebAssembly Interface Type language
      - Specifies a canonical ABI between components and host
      - Provides binary and text formats for components
      - Foundation for WASI Preview 2 system interfaces
    x-useCases:
      - Tracking the evolving Component Model standard
      - Implementing language toolchains targeting components
      - Implementing runtimes that load and link components
  - aid: component-model:wit
    name: WebAssembly Interface Type (WIT)
    description: WIT is the interface definition language for the Component Model. WIT describes the imports and exports of a component using interfaces and worlds. WIT is consumed by language toolchains to generate bindings and by runtimes to validate and link components at load time.
    humanURL: https://component-model.bytecodealliance.org/design/wit.html
    baseURL: https://component-model.bytecodealliance.org
    tags:
      - Bindings
      - IDL
      - Interface
      - WIT
    properties:
      - type: Documentation
        url: https://component-model.bytecodealliance.org/design/wit.html
      - type: Specification
        url: https://github.com/WebAssembly/component-model/blob/main/design/mvp/WIT.md
      - type: Reference
        url: https://github.com/bytecodealliance/wit-bindgen
    x-features:
      - Declarative IDL for components
      - Records, variants, enums, flags, options, results
      - Resources with methods for borrowed and owned references
      - Interfaces compose into worlds
    x-useCases:
      - Authoring portable component interfaces
      - Generating language bindings via wit-bindgen
      - Defining stable contracts between platform and components
  - aid: component-model:wasi-preview-2
    name: WebAssembly System Interface Preview 2
    description: WASI Preview 2 is the first WASI release built on the Component Model. It defines a set of interfaces such as wasi:filesystem, wasi:io, wasi:http, wasi:cli, and wasi:sockets that components can import to interact with the host system in a portable, capability-based way.
    humanURL: https://wasi.dev/
    baseURL: https://wasi.dev
    tags:
      - System Interface
      - WASI
      - Capabilities
    properties:
      - type: Documentation
        url: https://wasi.dev/
      - type: GitHub Organization
        url: https://github.com/WebAssembly/WASI
      - type: Reference
        url: https://github.com/WebAssembly/wasi-http
      - type: Reference
        url: https://github.com/WebAssembly/wasi-filesystem
    x-features:
      - Capability-based system access
      - Defined as a collection of WIT worlds
      - wasi:http provides a portable HTTP server interface
      - Worlds for CLI, HTTP proxy, and embedder customization
    x-useCases:
      - Building portable WebAssembly server functions
      - Running components in Wasmtime, Jco, WasmEdge, and Spin
      - Implementing capability-secure host bindings
  - aid: component-model:bytecode-alliance-implementations
    name: Component Model Implementations
    description: A landscape of toolchains and runtimes that implement the Component Model, including Wasmtime, Jco, wit-bindgen language bindings, cargo-component for Rust, ComponentizeJS, and Spin for serverless Wasm. These implementations are largely stewarded by the Bytecode Alliance.
    humanURL: https://bytecodealliance.org/
    baseURL: https://bytecodealliance.org
    tags:
      - Bytecode Alliance
      - Implementations
      - Runtimes
      - Toolchains
    properties:
      - type: Reference
        url: https://github.com/bytecodealliance/wasmtime
      - type: Reference
        url: https://github.com/bytecodealliance/wit-bindgen
      - type: Reference
        url: https://github.com/bytecodealliance/cargo-component
      - type: Reference
        url: https://github.com/bytecodealliance/jco
      - type: Reference
        url: https://github.com/bytecodealliance/ComponentizeJS
      - type: Reference
        url: https://github.com/fermyon/spin
    x-features:
      - Wasmtime native runtime with component support
      - Jco JavaScript host and tooling
      - cargo-component for Rust component projects
      - wit-bindgen for cross-language bindings
    x-useCases:
      - Running components on the server, edge, or in browsers
      - Generating language bindings from WIT
      - Building serverless Wasm functions on Spin
common:
  - type: Website
    url: https://component-model.bytecodealliance.org/
  - type: Documentation
    url: https://component-model.bytecodealliance.org/design/
  - type: GitHubRepository
    url: https://github.com/WebAssembly/component-model
  - type: GitHub Organization
    url: https://github.com/WebAssembly
  - type: Reference
    url: https://wasi.dev/
  - type: Reference
    url: https://bytecodealliance.org/
  - type: Working Group
    url: https://www.w3.org/community/webassembly/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
