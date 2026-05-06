---
aid: pipy
name: Pipy
description: Pipy is a high-performance, programmable network proxy designed for cloud, edge, and IoT environments. Written in C++ with an embedded JavaScript engine (PipyJS), it provides a small footprint, broad CPU architecture support, and a modular filter-based architecture for protocol conversion, traffic recording, message signing, and other networking tasks. Pipy is developed by Flomesh.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Proxy
  - Networking
  - Edge
  - Cloud
  - IoT
created: '2026-04-28'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/pipy/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: pipy:admin-api
    name: Pipy Admin API
    description: Pipy exposes an Admin UI and administrative interface, accessible via the built-in repo-mode HTTP server (default port 6060). The administrative surface allows operators to manage Pipy repositories, configurations, and programmable filter chains written in PipyJS.
    humanURL: https://flomesh.io/pipy/docs/reference/api
    baseURL: http://localhost:6060
    tags:
      - Admin
      - Proxy
      - Configuration
    properties:
      - type: Documentation
        url: https://flomesh.io/pipy/docs/reference/api
      - type: GettingStarted
        url: https://flomesh.io/pipy/docs/getting-started/quick-start
common:
  - type: Website
    url: https://flomesh.io/pipy
    name: Pipy Website
  - type: Documentation
    url: https://flomesh.io/pipy/docs
    name: Pipy Documentation
  - type: GettingStarted
    url: https://flomesh.io/pipy/docs/getting-started/quick-start
    name: Pipy Quick Start
  - type: Download
    url: https://flomesh.io/pipy/download
    name: Pipy Downloads
  - type: Blog
    url: https://blog.flomesh.io
    name: Flomesh Blog
  - type: GitHubOrg
    url: https://github.com/flomesh-io/pipy
    name: Pipy GitHub Repository
  - type: Twitter
    url: https://twitter.com/pipyproxy
    name: Pipy on Twitter
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
