---
aid: github-container-registry
name: GitHub Container Registry
description: GitHub Container Registry stores container images within your GitHub organization or personal account, allows you to associate images with repositories, and provides fine-grained permissions for managing access. It supports Docker and OCI image formats and is integrated with GitHub Actions for automated workflows.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Container Images
  - Containers
  - GitHub
  - Packages
  - Registry
url: https://raw.githubusercontent.com/api-evangelist/github-container-registry/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: github-container-registry:github-container-registry
    name: GitHub Container Registry
    description: GitHub Container Registry stores container images within your GitHub organization or personal account, allows you to associate images with repositories, and provides fine-grained permissions with integration into GitHub Actions workflows.
    humanURL: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
    baseURL: https://api.github.com
    tags:
      - Container Images
      - Containers
      - GitHub
      - Registry
    properties:
      - type: Documentation
        url: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
      - type: Getting Started
        url: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-to-the-container-registry
      - type: API Documentation
        url: https://docs.github.com/en/rest/packages/packages
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/github-container-registry/refs/heads/main/openapi/github-container-registry-openapi.yml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/github-container-registry/refs/heads/main/capabilities/github-container-registry-capabilities.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/github-container-registry/refs/heads/main/rules/github-container-registry-rules.yml
      - type: Pricing
        url: https://docs.github.com/en/billing/managing-billing-for-github-packages/about-billing-for-github-packages
common:
  - type: Website
    url: https://github.com/features/packages
  - type: Documentation
    url: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
  - type: Getting Started
    url: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
  - type: GitHub Organization
    url: https://github.com/github
  - type: Pricing
    url: https://docs.github.com/en/billing/managing-billing-for-github-packages/about-billing-for-github-packages
  - type: Blog
    url: https://github.blog/
  - type: Status
    url: https://www.githubstatus.com/
  - type: Sign Up
    url: https://github.com/signup
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
