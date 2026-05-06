---
aid: oras
name: ORAS
description: ORAS (OCI Registry As Storage) is a CNCF project that provides a CLI and a set of client libraries for pushing and pulling arbitrary OCI artifacts to and from OCI-compliant registries, allowing container registries to be used as a generic artifact distribution mechanism.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artifact Storage
  - Cloud Native
  - Container Registry
  - OCI
url: https://raw.githubusercontent.com/api-evangelist/oras/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: oras:cli
    name: ORAS CLI
    description: Generic command-line registry client used to push and pull OCI artifacts to and from any OCI-compliant container registry.
    humanURL: https://oras.land/docs/
    tags:
      - CLI
      - OCI
      - Artifacts
    properties:
      - type: Documentation
        url: https://oras.land/docs/
      - type: Installation
        url: https://oras.land/docs/installation
      - type: Commands
        url: https://oras.land/docs/commands/oras
      - type: Source Code
        url: https://github.com/oras-project/oras
  - aid: oras:client-libraries
    name: ORAS Client Libraries
    description: Client libraries for building custom OCI artifact tools and integrations on top of ORAS, available across multiple language ecosystems including Go, Rust, Python, JavaScript, .NET, and Java.
    humanURL: https://oras.land/docs/client_libraries/overview
    tags:
      - SDK
      - Libraries
      - OCI
    properties:
      - type: Documentation
        url: https://oras.land/docs/client_libraries/overview
      - type: Go
        url: https://github.com/oras-project/oras-go
      - type: Rust
        url: https://github.com/oras-project/rust-oci-client
      - type: Python
        url: https://github.com/oras-project/oras-py
      - type: JavaScript
        url: https://github.com/oras-project/oras-js
common:
  - type: Website
    url: https://oras.land/
  - type: Documentation
    url: https://oras.land/docs/
  - type: GitHub Organization
    url: https://github.com/oras-project
  - type: Community
    url: https://oras.land/community/
  - type: CNCF
    url: https://www.cncf.io/projects/oras/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
