---
aid: capn-proto
url: https://raw.githubusercontent.com/api-evangelist/capn-proto/refs/heads/main/apis.yml
name: Cap'n Proto
description: Cap'n Proto is an open-source binary data interchange format and capability-based RPC protocol specification originally created by Kenton Varda. Unlike Protocol Buffers, Cap'n Proto's in-memory representation is identical to its wire format, enabling zero-copy deserialization, incremental reads, random field access, and memory-mapped I/O. The reference implementation is in C++; a broad ecosystem of community-maintained bindings covers C#, Erlang, Go, Haskell, JavaScript/Node, OCaml, Python, Rust, C, D, Java, Lua, Nim, Ruby, and Scala.
type: Index
x-type: standard
position: Producer
access: Open Source
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Binary Format
  - Capability-Based Security
  - Code Generation
  - IPC
  - Open Source
  - Protocol
  - RPC
  - Schema
  - SDKs
  - Serialization
  - Specification
  - Zero Copy
created: '2026-03-25'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: capn-proto:capn-proto-schema-language
    name: Cap'n Proto Schema Language
    description: The Cap'n Proto schema language is used to define message types in .capnp files that are then compiled into native code for each supported language. The schema language defines structs, unions, enums, interfaces (for RPC), groups, generics, and annotations, and carefully specifies evolution rules so schemas can be extended without breaking forward or backward compatibility.
    humanURL: https://capnproto.org/language.html
    tags:
      - Code Generation
      - Schema
      - Specification
    properties:
      - type: Specification
        url: https://capnproto.org/language.html
      - type: Documentation
        url: https://capnproto.org/language.html
      - type: GitHub Repository
        url: https://github.com/capnproto/capnproto
    x-features:
      - Struct, union, enum, interface, and group definitions
      - Generic parameters for reusable types
      - Annotations for custom metadata
      - Schema evolution rules for forward and backward compatibility
      - Compilation to native code in multiple languages
      - Cross-language ABI through a canonical wire format
    x-use-cases:
      - Defining message types for zero-copy IPC
      - Describing RPC interfaces across language boundaries
      - Long-lived storage formats with schema evolution
      - Replacing Protocol Buffers for latency-sensitive workloads
  - aid: capn-proto:capn-proto-encoding
    name: Cap'n Proto Encoding (Wire Format)
    description: The Cap'n Proto encoding specification defines the binary wire format. The in-memory layout is the wire format, enabling zero-copy reads and writes, random field access, and safe memory-mapped access to messages stored on disk.
    humanURL: https://capnproto.org/encoding.html
    tags:
      - Binary Format
      - Specification
      - Zero Copy
    properties:
      - type: Specification
        url: https://capnproto.org/encoding.html
    x-features:
      - In-memory layout equals the wire format
      - Zero-copy deserialization
      - Random field access without scanning
      - Support for mmap-based message storage
      - Packed encoding variant for bandwidth-constrained links
      - Canonicalization rules for deterministic encoding
    x-use-cases:
      - Ultra-low-latency inter-process communication
      - Large on-disk datasets with mmap access
      - Network protocols where parsing cost matters
      - Embedded or memory-constrained environments (packed form)
  - aid: capn-proto:capn-proto-rpc
    name: Cap'n Proto RPC Protocol
    description: Cap'n Proto's RPC protocol is a capability-based RPC layer that supports promise pipelining, object references passed as arguments or return values, and time-travel optimizations that eliminate round trips. It is the foundation of Cloudflare Workers' inter- service communication and Sandstorm's capability-oriented sandbox.
    humanURL: https://capnproto.org/rpc.html
    tags:
      - Capability-Based Security
      - Protocol
      - RPC
      - Specification
    properties:
      - type: Specification
        url: https://capnproto.org/rpc.html
      - type: Documentation
        url: https://capnproto.org/rpc.html
    x-features:
      - Capability-based security model
      - Object (capability) references passed in messages
      - Promise pipelining to eliminate round trips
      - Bidirectional calls over a single connection
      - Time-travel / path-compression optimizations
      - Transport-agnostic (TCP, TLS, WebSocket, shared memory)
    x-use-cases:
      - Microservice RPC with low round-trip overhead
      - Secure capability-oriented sandboxing (Sandstorm, Workers)
      - Bidirectional streaming between trusted peers
      - Inter-process communication with fine-grained authorization
  - aid: capn-proto:capn-proto-cpp-runtime
    name: Cap'n Proto C++ Reference Implementation
    description: The C++ reference implementation is the canonical runtime for Cap'n Proto, providing the capnp compiler, serialization library, and KJ/RPC runtime. Other language implementations are maintained by their respective authors and track the C++ reference.
    humanURL: https://github.com/capnproto/capnproto
    tags:
      - IPC
      - SDKs
      - Serialization
    properties:
      - type: GitHub Repository
        url: https://github.com/capnproto/capnproto
      - type: Getting Started
        url: https://capnproto.org/install.html
      - type: Documentation
        url: https://capnproto.org/cxx.html
    x-features:
      - capnp schema compiler
      - KJ async and concurrency library
      - RPC runtime over TCP and in-process transports
      - Arena allocator for fast message construction
      - Packed and canonical encoding support
  - aid: capn-proto:capn-proto-language-bindings
    name: Cap'n Proto Language Bindings
    description: Community-maintained language bindings implement Cap'n Proto serialization and, in many cases, the full RPC protocol. Serialization plus RPC is supported in C++, C#, Erlang, Go, Haskell, JavaScript (Node.js), OCaml, Python, and Rust. Serialization-only bindings exist for C, D, Java, Lua, Nim, Ruby, and Scala.
    humanURL: https://capnproto.org/otherlang.html
    tags:
      - Code Generation
      - SDKs
      - Serialization
    properties:
      - type: Documentation
        url: https://capnproto.org/otherlang.html
      - type: GitHub Organization
        url: https://github.com/capnproto
    x-features:
      - Serialization + RPC in C++, C#, Erlang, Go, Haskell, JavaScript, OCaml, Python, Rust
      - Serialization-only bindings in C, D, Java, Lua, Nim, Ruby, Scala
      - Shared canonical wire format across all implementations
      - Editor integrations and syntax highlighters for common IDEs
    x-use-cases:
      - Polyglot systems sharing message types across services
      - Compiling schemas into idiomatic bindings for each language
      - Migration paths from Protocol Buffers in non-C++ codebases
common:
  - type: Website
    url: https://capnproto.org/
  - type: Documentation
    url: https://capnproto.org/language.html
  - type: Getting Started
    url: https://capnproto.org/install.html
  - type: GitHub Organization
    url: https://github.com/capnproto
  - type: GitHub Repository
    url: https://github.com/capnproto/capnproto
  - type: Discussion Group
    url: https://groups.google.com/g/capnproto
  - type: License
    url: https://github.com/capnproto/capnproto/blob/master/LICENSE.txt
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
