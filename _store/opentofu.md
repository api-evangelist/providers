---
aid: opentofu
name: OpenTofu
description: Open-source infrastructure as code tool forked from Terraform, providing a community-driven alternative for provisioning and managing cloud infrastructure using declarative configuration files.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud
  - DevOps
  - Infrastructure as Code
  - Open Source
created: '2025-01-01'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/opentofu/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: opentofu:opentofu-cli
    name: OpenTofu CLI
    description: OpenTofu is a CLI-driven infrastructure-as-code tool forked from Terraform. The opentofu binary reads HashiCorp Configuration Language (HCL) configuration, plans changes, and applies them against cloud providers through their respective APIs. It supports state management via local files or pluggable remote state backends, encrypted state and plan files, provider plugin distribution through registries, and a module ecosystem for composable infrastructure. OpenTofu does not itself expose an HTTP API; programmatic interaction happens through the CLI, configuration files, and provider/backend plugin protocols.
    humanURL: https://opentofu.org/
    tags:
      - CLI
      - Cloud
      - DevOps
      - HCL
      - Infrastructure as Code
      - Open Source
      - Terraform
    properties:
      - type: Documentation
        url: https://opentofu.org/docs/
      - type: Reference
        url: https://opentofu.org/docs/cli/commands/
      - type: Getting Started
        url: https://opentofu.org/docs/intro/install/
      - type: GitHubRepository
        url: https://github.com/opentofu/opentofu
common:
  - url: https://opentofu.org/
    name: OpenTofu
    type: Website
    description: Official OpenTofu project website.
  - url: https://opentofu.org/docs/
    name: Documentation
    type: Documentation
    description: OpenTofu CLI, configuration, and provider documentation.
  - url: https://opentofu.org/docs/intro/install/
    name: Getting Started
    type: Getting Started
    description: Installation guide and getting started tutorial for OpenTofu.
  - url: https://github.com/opentofu/opentofu
    name: GitHub Repository
    type: GitHubRepository
    description: Source code for the OpenTofu CLI.
  - url: https://github.com/opentofu
    name: GitHub Organization
    type: GitHub Organization
    description: OpenTofu GitHub organization with related projects and tooling.
  - url: https://opentofu.org/blog/
    name: Blog
    type: Blog
    description: OpenTofu project blog with releases and engineering posts.
  - url: https://opentofu.org/community/
    name: Community
    type: Community
    description: OpenTofu community resources, Slack, and working groups.
  - url: https://github.com/opentofu/opentofu/blob/main/CHANGELOG.md
    name: Change Log
    type: Change Log
    description: Changelog for the OpenTofu CLI releases.
  - url: https://github.com/opentofu/opentofu/security/policy
    name: Security
    type: Security
    description: Security disclosure policy for OpenTofu.
  - url: https://opentofu.org/docs/intro/install/
    name: Downloads
    type: Downloads
    description: OpenTofu binary downloads and package repositories.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
