---
aid: podman
name: Podman
description: Podman is a daemonless, open-source container engine for developing, managing, and running OCI containers on Linux, supporting both rootful and rootless operation as a drop-in replacement for Docker. The Podman REST API exposes a Docker-compatible surface alongside Libpod-specific endpoints for pods, volumes, networks, secrets, generators, and system management.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Containers
  - DevOps
  - OCI
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/podman/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: podman:podman-rest-api
    name: Podman REST API
    description: The Podman REST API (libpod) provides a Docker-compatible API surface plus Podman-specific Libpod endpoints for managing containers, images, pods, volumes, networks, secrets, manifests, and the Podman system service. The API is published as a Swagger 2.0 specification generated from the Podman source tree.
    humanURL: https://docs.podman.io/en/latest/_static/api.html
    baseURL: http://d/v6.0.0/libpod
    tags:
      - Containers
      - DevOps
      - OCI
    properties:
      - type: Documentation
        url: https://docs.podman.io/en/latest/_static/api.html
      - type: GettingStarted
        url: https://docs.podman.io/en/latest/markdown/podman-system-service.1.html
      - type: OpenAPI
        url: openapi/podman-openapi.yml
common:
  - type: Website
    url: https://podman.io/
  - type: Documentation
    url: https://docs.podman.io/
  - type: GitHubOrganization
    url: https://github.com/containers
  - type: SourceCode
    url: https://github.com/containers/podman
  - type: Blog
    url: https://podman.io/blogs/
  - type: Community
    url: https://podman.io/community/
  - type: GettingStarted
    url: https://podman.io/get-started
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
