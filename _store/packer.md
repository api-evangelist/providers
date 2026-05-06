---
aid: packer
name: Packer
description: Packer is an open-source tool by HashiCorp for creating identical machine images for multiple platforms from a single source configuration. It automates the creation of pre-configured virtual machine and container images. HCP Packer adds a hosted artifact registry with a REST API for tracking image metadata, versions, channels, and security signals.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - DevOps
  - HashiCorp
  - Image Building
  - Infrastructure as Code
url: https://raw.githubusercontent.com/api-evangelist/packer/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: packer:packer
    name: Packer
    description: Open-source tool for creating identical machine images for multiple platforms from a single source configuration.
    humanURL: https://www.packer.io/
    tags:
      - Automation
      - DevOps
      - Infrastructure as Code
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/packer/docs
      - type: Getting Started
        url: https://developer.hashicorp.com/packer/tutorials
  - aid: packer:hcp-packer-artifact-registry
    name: HCP Packer Artifact Registry API
    description: REST API for managing Packer artifacts in the HashiCorp Cloud Platform Packer Artifact Registry, including buckets, versions, builds, channels, packages, SBOMs, vulnerabilities, and registry configuration.
    humanURL: https://developer.hashicorp.com/hcp/api-docs/packer
    baseURL: https://api.cloud.hashicorp.com
    tags:
      - Artifact Registry
      - HCP
      - Image Building
      - Infrastructure as Code
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/hcp/api-docs/packer
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/packer/refs/heads/main/openapi/packer-openapi.yml
      - type: Status
        url: https://status.hashicorp.com
common:
  - type: Website
    url: https://www.packer.io/
  - type: Documentation
    url: https://developer.hashicorp.com/packer/docs
  - type: GitHub Organization
    url: https://github.com/hashicorp/packer
  - type: Community
    url: https://discuss.hashicorp.com/c/packer
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
