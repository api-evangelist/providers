---
aid: runc
url: https://raw.githubusercontent.com/api-evangelist/runc/refs/heads/main/apis.yml
apis:
- aid: runc:runc
  name: Runc
  description: runc is a CLI tool for spawning and running containers on Linux according to the OCI (Open Container Initiative) specification. It is the reference implementation of the OCI runtime specification, providing a lightweight and portable container runtime that can be used independently or embedded into higher-level container systems like Docker and containerd.
  humanURL: https://github.com/opencontainers/runc
  tags:
  - Container Runtime
  - Containers
  - Linux
  - OCI
  - Open Source
  properties:
  - type: Documentation
    url: https://github.com/opencontainers/runc/blob/main/README.md
  - type: Getting Started
    url: https://github.com/opencontainers/runc#creating-an-oci-bundle
name: Runc
tags:
- Container Runtime
- Containers
- Linux
- OCI
- Open Source
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: runc is a CLI tool for spawning and running containers on Linux according to the OCI (Open Container Initiative) specification. It is the reference implementation of the OCI runtime specification and is used as the default low-level container runtime by Docker, containerd, and other container platforms.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

