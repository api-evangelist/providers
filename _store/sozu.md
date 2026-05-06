---
aid: sozu
name: Sozu
description: Sōzu is an open-source, fast and lightweight HTTP reverse proxy written in Rust, designed for high-performance traffic management in immutable infrastructure environments. It is configurable at runtime through a protobuf-based IPC protocol without requiring restarts, making it ideal for always-up deployments. Sōzu supports TLS termination, load balancing, and dynamic cluster configuration, and is developed by the sozu-proxy open-source organization on GitHub.
url: https://raw.githubusercontent.com/api-evangelist/sozu/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Proxy
  - Reverse Proxy
  - Load Balancing
  - Rust
  - Open Source
apis:
  - aid: sozu:sozu-command-api
    name: Sozu Command API
    description: The Sozu Command API provides programmatic control of the Sōzu HTTP reverse proxy at runtime. External tools communicate with the Sozu main process through a secure Unix socket using a protobuf-based binary protocol (IPC). The sozu-command-lib crate ships the protobuf schema, configuration parser, replicated state, channels, and file descriptor passing helpers. This enables dynamic cluster configuration, certificate management, and backend routing changes without restarts.
    humanURL: https://docs.sozu.io/
    baseURL: https://github.com/sozu-proxy/sozu
    tags:
      - Proxy
      - Command API
      - Protobuf
      - Runtime Configuration
    properties:
      - type: Documentation
        url: https://docs.sozu.io/
      - type: GitHub
        url: https://github.com/sozu-proxy/sozu
      - type: Getting Started
        url: https://docs.sozu.io/getting-started/
      - type: Configuration
        url: https://github.com/sozu-proxy/sozu/blob/main/doc/configure.md
      - type: How To Use
        url: https://github.com/sozu-proxy/sozu/blob/main/doc/how_to_use.md
      - type: JSON Schema
        url: https://raw.githubusercontent.com/api-evangelist/sozu/refs/heads/main/json-schema/sozu-cluster-schema.json
      - type: JSON Schema
        url: https://raw.githubusercontent.com/api-evangelist/sozu/refs/heads/main/json-schema/sozu-frontend-schema.json
  - aid: sozu:sozu-acme-api
    name: Sozu ACME Integration
    description: The Sozu ACME integration automates TLS certificate requests from Let's Encrypt and other ACME-enabled certificate authorities. Originally a standalone tool in the sozu-acme repository, it has been integrated directly into the main Sōzu binary and is available as a command-line feature.
    humanURL: https://github.com/sozu-proxy/sozu-acme
    tags:
      - TLS
      - Certificates
      - ACME
      - Let's Encrypt
    properties:
      - type: GitHub
        url: https://github.com/sozu-proxy/sozu-acme
  - aid: sozu:sozu-command-futures-api
    name: Sozu Command Futures API
    description: The sozu-command-futures library provides a futures-based async Rust API for configuring the Sōzu HTTP reverse proxy programmatically. It wraps the low-level IPC protocol in an ergonomic async interface for Rust applications.
    humanURL: https://github.com/sozu-proxy/sozu-command-futures
    tags:
      - Proxy
      - Rust
      - Async
      - Command API
    properties:
      - type: GitHub
        url: https://github.com/sozu-proxy/sozu-command-futures
common:
  - type: Website
    url: https://www.sozu.io/
  - type: Documentation
    url: https://docs.sozu.io/
  - type: GitHub Organization
    url: https://github.com/sozu-proxy
  - type: GitHub Repository
    url: https://github.com/sozu-proxy/sozu
  - type: Releases
    url: https://github.com/sozu-proxy/sozu/releases
  - type: Dashboard
    url: https://github.com/sozu-proxy/dashboard
  - type: Integration Tests
    url: https://github.com/sozu-proxy/sozu-integration-tests
  - type: JSON-LD Context
    url: https://raw.githubusercontent.com/api-evangelist/sozu/refs/heads/main/json-ld/sozu-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/sozu/refs/heads/main/vocabulary/sozu-vocabulary.yml
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
