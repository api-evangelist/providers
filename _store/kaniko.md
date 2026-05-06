---
aid: kaniko
name: Kaniko
description: Kaniko is an open-source tool from Google that builds container images from a Dockerfile inside a container or Kubernetes cluster without requiring a Docker daemon. It executes each command within a Dockerfile in userspace, enabling secure container builds in environments where running a Docker daemon is impractical or insecure. The project was archived on June 3, 2025, and is now read-only.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Archived
  - Build Tools
  - CLI
  - Container Images
  - Containers
  - Daemonless
  - Google
  - Kubernetes
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/kaniko/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kaniko:kaniko-cli
    name: Kaniko CLI
    description: Kaniko is a command-line tool distributed as the container image gcr.io/kaniko-project/executor that builds container images from a Dockerfile. It supports multiple build context sources (GCS, S3, Azure Blob Storage, local directories, Git, stdin), layer caching, and credential helpers for GCR, Docker Hub, ECR, and ACR.
    humanURL: https://github.com/GoogleContainerTools/kaniko
    tags:
      - CLI
      - Build Tools
      - Container Images
      - Daemonless
    properties:
      - type: Documentation
        url: https://github.com/GoogleContainerTools/kaniko/blob/main/README.md
      - type: Tutorial
        url: https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md
      - type: Releases
        url: https://github.com/GoogleContainerTools/kaniko/releases
      - type: Contributing
        url: https://github.com/GoogleContainerTools/kaniko/blob/main/CONTRIBUTING.md
      - type: Source Code
        url: https://github.com/GoogleContainerTools/kaniko
common:
  - type: Website
    url: https://github.com/GoogleContainerTools/kaniko
  - type: Documentation
    url: https://github.com/GoogleContainerTools/kaniko/blob/main/README.md
  - type: Getting Started
    url: https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md
  - type: Development
    url: https://github.com/GoogleContainerTools/kaniko/blob/main/DEVELOPMENT.md
  - type: Contributing
    url: https://github.com/GoogleContainerTools/kaniko/blob/main/CONTRIBUTING.md
  - type: Releases
    url: https://github.com/GoogleContainerTools/kaniko/releases
  - type: GitHub Organization
    url: https://github.com/GoogleContainerTools
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
