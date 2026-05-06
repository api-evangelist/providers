---
aid: gitlab-container-registry
name: GitLab Container Registry
description: GitLab Container Registry is a built-in container registry that allows users to store Docker images alongside their code in GitLab repositories. It exposes a REST API for managing image repositories, tags, and cleanup policies.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Container Images
  - Containers
  - GitLab
  - Registry
url: https://raw.githubusercontent.com/api-evangelist/gitlab-container-registry/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: gitlab-container-registry:gitlab-container-registry
    name: GitLab Container Registry
    description: GitLab Container Registry is a built-in container registry that allows users to store Docker images alongside their code in GitLab repositories.
    humanURL: https://docs.gitlab.com/user/packages/container_registry/
    baseURL: https://gitlab.com/api/v4
    tags:
      - Container Images
      - Containers
      - GitLab
      - Registry
    properties:
      - type: Documentation
        url: https://docs.gitlab.com/user/packages/container_registry/
      - type: API Documentation
        url: https://docs.gitlab.com/api/container_registry/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/gitlab-container-registry/refs/heads/main/openapi/gitlab-container-registry-openapi.yml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/gitlab-container-registry/refs/heads/main/capabilities/gitlab-container-registry-capabilities.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/gitlab-container-registry/refs/heads/main/rules/gitlab-container-registry-rules.yml
common:
  - type: Website
    url: https://docs.gitlab.com/user/packages/container_registry/
  - type: Documentation
    url: https://docs.gitlab.com/user/packages/container_registry/
  - type: API Documentation
    url: https://docs.gitlab.com/api/container_registry/
  - type: GitHub Organization
    url: https://gitlab.com/gitlab-org
  - type: Pricing
    url: https://about.gitlab.com/pricing/
  - type: Status
    url: https://status.gitlab.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
