---
aid: containerfile
url: https://raw.githubusercontent.com/api-evangelist/containerfile/refs/heads/main/apis.yml
name: Containerfile
x-type: standard
description: A Containerfile is a plain text file that contains instructions for building container images. It is fully compatible with Docker's Dockerfile format and is the default file name used by Buildah and Podman. Containerfile instructions describe a base image (FROM), the steps to assemble the image (RUN, COPY, ADD, ARG, ENV), and runtime defaults (CMD, ENTRYPOINT, EXPOSE, USER, WORKDIR, VOLUME). Modern build engines extend the format with cache, secret, and SSH mounts and with platform-aware multi-stage builds.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - BuildKit
  - Buildah
  - Containers
  - DevOps
  - Docker
  - Dockerfile
  - Image Build
  - OCI
  - Podman
  - Standard
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: containerfile:reference
    name: Containerfile Reference
    description: The official Containerfile reference shipped with the containers/common project. Documents every Containerfile instruction, syntax, and the ways Containerfile differs from Dockerfile, including secret mounts and platform-aware ARGs.
    humanURL: https://github.com/containers/common/blob/main/docs/Containerfile.5.md
    baseURL: https://github.com
    tags:
      - Containerfile
      - Reference
      - containers/common
    properties:
      - type: Specification
        url: https://github.com/containers/common/blob/main/docs/Containerfile.5.md
      - type: Documentation
        url: https://docs.podman.io/en/latest/markdown/podman-build.1.html
      - type: GitHubRepository
        url: https://github.com/containers/common
    x-features:
      - Documents FROM, RUN, COPY, ADD, ARG, ENV, CMD, ENTRYPOINT, EXPOSE, USER, WORKDIR, VOLUME, LABEL, ONBUILD
      - RUN --mount support for bind, cache, secret, ssh, and tmpfs mounts
      - Platform-aware ARGs (TARGETARCH, TARGETOS, TARGETPLATFORM, BUILDARCH, BUILDOS, BUILDPLATFORM)
      - HEREDOC syntax for inline RUN scripts
      - Multi-stage builds via FROM ... AS name
    x-useCases:
      - Authoring portable Containerfiles for Podman and Docker
      - Migrating between Docker and Podman build tooling
      - Defining cross-platform images with multi-arch support
  - aid: containerfile:dockerfile-reference
    name: Dockerfile Reference
    description: The Dockerfile format reference maintained by Docker. Containerfile is a strict superset of Dockerfile, so the Dockerfile reference covers the same instruction set with Docker-specific extensions such as directives like syntax= and check=.
    humanURL: https://docs.docker.com/reference/dockerfile/
    baseURL: https://docs.docker.com
    tags:
      - Docker
      - Dockerfile
      - Reference
    properties:
      - type: Specification
        url: https://docs.docker.com/reference/dockerfile/
      - type: Documentation
        url: https://docs.docker.com/build/
      - type: Reference
        url: https://docs.docker.com/build/buildkit/
    x-features:
      - Authoritative Dockerfile reference for all instructions
      - Directives such as syntax= and check= for builder behavior
      - BuildKit-specific RUN --mount syntax
      - Linting rules via the Dockerfile checker
    x-useCases:
      - Authoring Dockerfiles or Containerfiles for Docker BuildKit
      - Looking up the exact syntax of an instruction or flag
      - Adopting newer BuildKit features like SSH mounts
  - aid: containerfile:buildkit-frontend
    name: BuildKit Dockerfile Frontend
    description: Dockerfile and Containerfile parsing in modern Docker is performed by BuildKit's Dockerfile frontend, distributed as a container image (docker/dockerfile). The frontend version is selected via the `# syntax=` directive and adds new features without requiring a BuildKit upgrade.
    humanURL: https://github.com/moby/buildkit/blob/master/frontend/dockerfile/docs/reference.md
    baseURL: https://github.com
    tags:
      - BuildKit
      - Frontend
      - Moby
    properties:
      - type: Documentation
        url: https://github.com/moby/buildkit/blob/master/frontend/dockerfile/docs/reference.md
      - type: GitHubRepository
        url: https://github.com/moby/buildkit
      - type: Reference
        url: https://hub.docker.com/r/docker/dockerfile
    x-features:
      - Versioned Dockerfile frontend images
      - Pluggable parser via `# syntax=` directive
      - Adds RUN --mount, secret, ssh, and cache features
      - Used by docker buildx and BuildKit-based builders
    x-useCases:
      - Pinning the Dockerfile frontend version for reproducibility
      - Adopting new RUN features without upgrading the daemon
      - Authoring Dockerfile linting rules and tools
  - aid: containerfile:oci-image-spec
    name: OCI Image Specification
    description: The Open Container Initiative Image Specification defines the format of the image artifacts that Containerfile and Dockerfile builds produce. The spec covers manifests, configuration, layers, and indexes consumed by container runtimes such as runc, crun, and containerd.
    humanURL: https://github.com/opencontainers/image-spec
    baseURL: https://github.com
    tags:
      - Image
      - OCI
      - Standards
    properties:
      - type: Specification
        url: https://github.com/opencontainers/image-spec
      - type: GitHubRepository
        url: https://github.com/opencontainers/image-spec
      - type: Reference
        url: https://opencontainers.org/
    x-features:
      - Image manifest, configuration, and layer schema
      - Image index for multi-platform images
      - Foundational spec for OCI registries and runtimes
    x-useCases:
      - Building tools that produce OCI images directly
      - Verifying that Containerfile output conforms to OCI
      - Implementing multi-arch image manifests
common:
  - type: Specification
    url: https://github.com/containers/common/blob/main/docs/Containerfile.5.md
  - type: Documentation
    url: https://docs.docker.com/reference/dockerfile/
  - type: Reference
    url: https://github.com/moby/buildkit/blob/master/frontend/dockerfile/docs/reference.md
  - type: Reference
    url: https://opencontainers.org/
  - type: GitHub Organization
    url: https://github.com/containers
  - type: GitHubRepository
    url: https://github.com/containers/buildah
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
