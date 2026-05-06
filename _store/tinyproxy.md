---
aid: tinyproxy
name: Tinyproxy
description: Tinyproxy is a lightweight, open-source HTTP/HTTPS proxy daemon designed for POSIX operating systems. It is ideal for use cases in embedded deployments, small networks, and environments where a full-featured HTTP proxy is required with minimal system resource usage. Configuration is file-based with an internal statistics monitoring page.
type: Index
position: Consumer
access: Open Source
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Forward Proxy
  - Proxy
  - HTTP
  - Networking
  - Open Source
created: '2026-03-27'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tinyproxy/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tinyproxy:tinyproxy
    name: Tinyproxy
    description: Tinyproxy is a lightweight HTTP/HTTPS proxy daemon for POSIX operating systems with minimal system resource requirements. Provides forward proxying, HTTPS CONNECT tunneling, domain filtering, access control, upstream proxy chaining, transparent proxying, and an internal statistics monitoring page.
    humanURL: https://tinyproxy.github.io/
    tags:
      - Forward Proxy
      - Proxy
      - HTTP
      - Networking
    properties:
      - type: Documentation
        url: https://tinyproxy.github.io/
      - type: Getting Started
        url: https://github.com/tinyproxy/tinyproxy#readme
      - type: GitHub Repository
        url: https://github.com/tinyproxy/tinyproxy
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/tinyproxy/refs/heads/main/json-schema/tinyproxy-config-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/tinyproxy/refs/heads/main/json-structure/tinyproxy-config-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/tinyproxy/refs/heads/main/json-ld/tinyproxy-context.jsonld
features:
  - HTTP and HTTPS proxy support
  - CONNECT tunneling for HTTPS
  - Domain and URL filtering
  - Access control lists
  - Upstream proxy chaining
  - Transparent proxy mode
  - Internal statistics monitoring page
  - Privacy header filtering
  - Logging with configurable verbosity
  - Small memory footprint (~2MB with glibc)
useCases:
  - Embedded systems proxy
  - Small network HTTP proxy
  - Content filtering gateway
  - Development and testing proxy
  - Container sidecar proxy
  - IoT device internet access control
integrations:
  - Linux networking stack
  - systemd service management
  - Docker container deployments
solutions:
  - Network access control
  - Internet traffic filtering
  - Embedded proxy deployments
  - Development proxy environments
common:
  - type: Website
    url: https://tinyproxy.github.io/
  - type: Documentation
    url: https://tinyproxy.github.io/
  - type: GitHub Organization
    url: https://github.com/tinyproxy
  - type: GitHub Repository
    url: https://github.com/tinyproxy/tinyproxy
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/tinyproxy/refs/heads/main/json-schema/tinyproxy-config-schema.json
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/tinyproxy/refs/heads/main/json-structure/tinyproxy-config-structure.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/tinyproxy/refs/heads/main/json-ld/tinyproxy-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/tinyproxy/refs/heads/main/vocabulary/tinyproxy-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
