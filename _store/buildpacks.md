---
aid: buildpacks
name: Cloud Native Buildpacks
description: Cloud Native Buildpacks (CNBs) transform application source code into OCI-compliant container images that can run on any cloud, without requiring Dockerfiles. Initiated by Pivotal and Heroku in January 2018, CNBs are a CNCF incubating project licensed under Apache-2.0. They centralize container expertise through composable buildpacks, enable layer rebasing for efficient OS updates, and generate Software Bills of Materials (SBOM). The pack CLI and kpack platform operator are primary integration points.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/buildpacks/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Build Tools
  - CI/CD
  - Cloud Native
  - CNCF
  - Container Images
  - Containers
  - OCI
  - Open Source
apis:
  - aid: buildpacks:buildpack-api
    name: Buildpack API Specification
    description: The Buildpack API defines the contract between a buildpack and the lifecycle that executes it. It specifies detect, build, and export phases, layer contribution formats, environment variable handling, and SBOM generation interfaces.
    humanURL: https://buildpacks.io/docs/reference/spec/buildpack-api/
    tags:
      - API Specification
      - Buildpacks
      - Container Images
      - OCI
    properties:
      - type: Documentation
        url: https://buildpacks.io/docs/reference/spec/buildpack-api/
      - type: GitHubRepository
        url: https://github.com/buildpacks/spec
  - aid: buildpacks:platform-api
    name: Platform API Specification
    description: The Platform API defines the contract between a platform (such as pack or kpack) and the CNB lifecycle. It covers builder configuration, build inputs and outputs, stack definitions, and run image management.
    humanURL: https://buildpacks.io/docs/reference/spec/platform-api/
    tags:
      - API Specification
      - Container Images
      - Platforms
    properties:
      - type: Documentation
        url: https://buildpacks.io/docs/reference/spec/platform-api/
      - type: GitHubRepository
        url: https://github.com/buildpacks/spec
  - aid: buildpacks:distribution-api
    name: Distribution API Specification
    description: The Distribution API defines the OCI-based format for packaging and distributing buildpacks and builders via container registries, including the buildpackage format.
    humanURL: https://buildpacks.io/docs/reference/spec/distribution-api/
    tags:
      - API Specification
      - Distribution
      - OCI
      - Packaging
    properties:
      - type: Documentation
        url: https://buildpacks.io/docs/reference/spec/distribution-api/
      - type: GitHubRepository
        url: https://github.com/buildpacks/spec
common:
  - type: Website
    url: https://buildpacks.io
  - type: Documentation
    url: https://buildpacks.io/docs/
  - type: GitHubOrganization
    url: https://github.com/buildpacks
  - type: Blog
    url: https://medium.com/buildpacks
  - type: Community
    url: https://buildpacks.io/community/
  - type: Registry
    url: https://registry.buildpacks.io/
  - type: Specification
    url: https://github.com/buildpacks/spec/blob/main/buildpack.md
  - type: MailingList
    url: https://lists.cncf.io/g/cncf-buildpacks/join
  - type: Slack
    url: https://slack.cncf.io
  - type: CNCF
    url: https://www.cncf.io/projects/buildpacks/
  - type: DevStats
    url: https://buildpacks.devstats.cncf.io/
  - name: Use Cases
    type: UseCases
    data:
      - name: App Developer Image Building
        url: https://buildpacks.io/docs/for-app-developers/
        features:
          - No Dockerfile Required
          - Automatic Dependency Detection
          - Multi-Language Support
          - Reproducible Builds
          - ARM Container Support
          - Windows Container Support
      - name: Platform Operator Integration
        url: https://buildpacks.io/docs/for-platform-operators/
        features:
          - CI/CD Pipeline Integration
          - pack CLI Integration
          - kpack Kubernetes Operator
          - Tekton Pipeline Support
          - CircleCI Integration
          - GitLab CI Integration
          - Custom Builder Creation
      - name: Buildpack Authoring
        url: https://buildpacks.io/docs/for-buildpack-authors/
        features:
          - Custom Language Support
          - Framework-Specific Buildpacks
          - Buildpack Packaging
          - Registry Distribution
          - Extension Authoring
          - Composable Buildpack Groups
      - name: OS-Level Security Patching
        url: https://buildpacks.io/docs/reference/spec/platform-api/
        features:
          - Layer Rebasing
          - Base Image Updates Without Rebuild
          - Minimal Rebuild Surface
          - Stack Switching
  - name: Features
    type: Features
    data:
      - name: pack build
        url: https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/cli/
        features:
          - Source-to-Image Conversion
          - Builder Selection
          - Environment Variable Injection
          - Volume Mount Support
          - Cache Integration
      - name: pack builder
        url: https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/cli/
        features:
          - Create Custom Builders
          - Inspect Builder Contents
          - Trust Builder Configuration
          - Suggest Default Builders
      - name: pack rebase
        url: https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/cli/
        features:
          - Update Base Image Layers
          - No Source Rebuild Required
          - Fast Security Patching
      - name: pack sbom download
        url: https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/cli/
        features:
          - Software Bill of Materials
          - Dependency Inventory
          - Security Auditing
          - License Tracking
      - name: Buildpack Registry
        url: https://registry.buildpacks.io/
        features:
          - Community Buildpack Discovery
          - Namespace Registration
          - Version Tracking
          - Verified Buildpacks
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
