---
aid: portainer
name: Portainer
description: Portainer is an open source container management platform that simplifies deploying, managing, and monitoring Docker, Swarm, Podman, and Kubernetes environments through a unified web UI and REST API.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Container Management
  - Containers
  - Docker
  - Kubernetes
url: https://raw.githubusercontent.com/api-evangelist/portainer/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: portainer:portainer
    name: Portainer
    description: Portainer's HTTP API exposes everything the Portainer UI can do, including authentication, environment and endpoint management, stacks, containers, images, volumes, networks, registries, edge computing, Kubernetes namespaces and resources, RBAC, and backup and restore for managing containerized infrastructure programmatically.
    humanURL: https://www.portainer.io/
    baseURL: https://api-docs.portainer.io
    tags:
      - Container Management
      - Containers
      - Docker
      - Kubernetes
      - Edge Computing
    properties:
      - type: Documentation
        url: https://docs.portainer.io/
      - type: APIReference
        url: https://api-docs.portainer.io/
      - type: GettingStarted
        url: https://docs.portainer.io/start
      - type: OpenAPI
        url: openapi/portainer-openapi.yml
common:
  - type: Website
    url: https://www.portainer.io/
  - type: Documentation
    url: https://docs.portainer.io/
  - type: APIReference
    url: https://api-docs.portainer.io/
  - type: Blog
    url: https://www.portainer.io/blog
  - type: Pricing
    url: https://www.portainer.io/pricing
  - type: GitHubOrg
    url: https://github.com/portainer
  - type: GitHubRepository
    url: https://github.com/portainer/portainer
  - type: Community
    url: https://www.portainer.io/community
  - type: Slack
    url: https://www.portainer.io/slack
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
