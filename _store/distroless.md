---
aid: distroless
name: Distroless
url: https://raw.githubusercontent.com/api-evangelist/distroless/refs/heads/main/apis.yml
modified: '2026-04-28'
created: '2026-03-26'
specificationVersion: '0.19'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Container Images
  - Containers
  - Google
  - Security
description: Distroless images by Google contain only the application and its runtime dependencies, stripping out package managers, shells, and other OS-level utilities to minimize attack surface and image size. The smallest variant (gcr.io/distroless/static-debian12) is roughly 2 MB. Distroless ships base images for static binaries, glibc-based binaries, C/C++, Java (17, 21, 25), Node.js (22, 24), and Python 3, with multi-architecture support including amd64, arm64, arm, s390x, ppc64le, and riscv64. Adopters include Kubernetes, Knative, Tekton, and Teleport.
apis:
  - aid: distroless:distroless
    name: Distroless
    description: Distroless images by Google contain only the application and its runtime dependencies, stripping out package managers, shells, and other OS-level utilities to minimize attack surface and image size.
    humanURL: https://github.com/GoogleContainerTools/distroless
    tags:
      - Container Images
      - Containers
      - Google
      - Security
    properties:
      - type: Documentation
        url: https://github.com/GoogleContainerTools/distroless/blob/main/README.md
      - type: Getting Started
        url: https://github.com/GoogleContainerTools/distroless/blob/main/README.md#how-do-i-use-distroless-images
      - type: SourceCode
        url: https://github.com/GoogleContainerTools/distroless
      - type: Container Registry
        url: https://gcr.io/distroless
common:
  - type: Website
    url: https://github.com/GoogleContainerTools/distroless
  - type: GitHub Organization
    url: https://github.com/GoogleContainerTools
  - type: Container Registry
    url: https://gcr.io/distroless
  - type: Issues
    url: https://github.com/GoogleContainerTools/distroless/issues
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
