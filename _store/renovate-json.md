---
aid: renovate-json
name: Renovate
description: Renovate is an open-source, cross-platform dependency automation tool by Mend.io that automatically creates pull requests to keep software dependencies up to date. It supports over 90 package managers and language ecosystems including npm, PyPI, Maven, Docker, Helm, Go modules, Ruby Gems, NuGet, and more. Renovate runs as a CLI, Docker container, GitHub Action, or hosted cloud service (Mend Renovate App). It integrates with GitHub, GitLab, Bitbucket, Azure DevOps, Gitea, Forgejo, and AWS CodeCommit. Configuration is done via a renovate.json file in the repository root. The tool supports advanced scheduling, monorepo support, preset sharing, merge confidence scoring, and automatic replacement of deprecated packages.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - CI/CD
  - Configuration
  - Dependency Management
  - Open Source
  - DevOps
url: https://raw.githubusercontent.com/api-evangelist/renovate-json/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis: []
common:
  - url: https://github.com/renovatebot/renovate
    name: Renovate GitHub Repository
    type: GitHubRepository
    description: Main Renovate CLI source code repository (21k+ stars)
  - url: https://docs.renovatebot.com
    name: Renovate Documentation
    type: Documentation
    description: Official documentation for configuration, platforms, and self-hosting
  - url: https://www.mend.io/renovate/
    name: Mend Renovate
    type: Website
    description: Hosted Renovate service by Mend.io with cloud and self-hosted options
  - url: https://github.com/apps/renovate
    name: Renovate GitHub App
    type: GitHubApp
    description: Install the Mend Renovate GitHub App for automatic dependency updates
  - url: https://github.com/renovatebot/github-action
    name: Renovate GitHub Action
    type: GitHubAction
    description: GitHub Actions integration for self-hosted Renovate
  - url: https://www.npmjs.com/package/renovate
    name: Renovate npm Package
    type: SDK
    description: Renovate CLI distributed as an npm package for self-hosting
  - url: https://hub.docker.com/r/renovate/renovate
    name: Renovate Docker Image
    type: ContainerImage
    description: Official Docker image for self-hosted Renovate deployments
  - url: https://github.com/renovatebot/helm-charts
    name: Renovate Helm Charts
    type: HelmChart
    description: Kubernetes Helm charts for deploying Renovate in a cluster
  - url: https://github.com/orgs/renovatebot/repositories
    name: Renovate GitHub Organization
    type: GitHubOrganization
    description: All Renovate open-source projects including SDKs and integrations
  - url: https://github.com/renovatebot/tutorial
    name: Renovate Tutorial
    type: Tutorial
    description: Hands-on tutorial for getting started with Renovate
  - url: json-schema/renovate-config-schema.json
    name: Renovate Config Schema
    type: JSONSchema
    description: JSON Schema for renovate.json configuration file
  - url: json-structure/renovate-config-structure.json
    name: Renovate Config Structure
    type: JSONStructure
    description: Structural documentation for Renovate configuration
  - url: json-ld/renovate-context.jsonld
    name: Renovate JSON-LD Context
    type: JSONLD
    description: JSON-LD context for Renovate dependency management concepts
  - url: vocabulary/renovate-vocabulary.yml
    name: Renovate Vocabulary
    type: Vocabulary
    description: Dependency automation domain vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
