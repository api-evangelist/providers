---
aid: mosn
name: MOSN
description: MOSN (Modular Open Smart Network) is a cloud-native network proxy written in Go, open-sourced by Ant Group. It serves as a Service Mesh data plane and can function as L4/L7 load balancer, API gateway, and cloud-native ingress, with multi-protocol support including HTTP/1.1, HTTP/2, and gRPC.
type: Index
position: Consuming
access: Open-Source
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Service Mesh
  - Proxy
  - API Gateway
  - Cloud Native
  - Open Source
created: '2026-04-28'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/mosn/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: mosn:mosn
    name: MOSN
    description: MOSN is a cloud-native network proxy that supports multiple protocols (HTTP/1.1, HTTP/2, gRPC), dynamic routing, load balancing, observability via Prometheus metrics, TLS, and WASM-based custom extensions. It includes an admin API extension for runtime configuration and management.
    humanURL: https://mosn.io/
    tags:
      - Service Mesh
      - Proxy
      - API Gateway
    properties:
      - type: Documentation
        url: https://mosn.io/docs/
      - type: SourceCode
        url: https://github.com/mosn/mosn
commonProperties:
  - type: Website
    url: https://mosn.io/
  - type: SourceCode
    url: https://github.com/mosn/mosn
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
