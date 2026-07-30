---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/werf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://werf.io/
- group: docs
  title: ''
  type: Documentation
  url: https://werf.io/docs/v2/
- group: start
  title: ''
  type: GettingStarted
  url: https://werf.io/getting_started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/werf
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/werf/werf
- group: build
  title: Werf CLI
  type: CLI
  url: https://github.com/werf/werf
- group: build
  title: Nelm (Helm 4 Alternative)
  type: GitHubRepository
  url: https://github.com/werf/nelm
- group: build
  title: Kubedog Kubernetes Watch Library
  type: GitHubRepository
  url: https://github.com/werf/kubedog
- group: build
  title: TRDL Secure Software Delivery
  type: GitHubRepository
  url: https://github.com/werf/trdl
- group: build
  title: GitHub Actions Integration
  type: GitHubRepository
  url: https://github.com/werf/actions
- group: build
  title: Nelm Chart TypeScript SDK
  type: GitHubRepository
  url: https://github.com/werf/nelm-chart-ts-sdk
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/werf/werf/releases
- group: operate
  title: ''
  type: Support
  url: https://github.com/werf/werf/discussions
created: '2025'
description: Werf is an open-source CNCF sandbox project providing a complete GitOps-based CI/CD solution for Kubernetes. It implements the full application delivery lifecycle — building images, managing dependencies, deploying Helm charts, and cleaning up container registries — using Git as the single source of truth (Giterminism). Werf integrates natively with all major CI systems, Buildah, Helm, and Kubernetes.
features:
- description: Uses Git as the single source of truth, ensuring all CI/CD configurations are reproducible and auditable from version control.
  name: Giterminism
- description: Rebuilds only modified components and reuses existing container registry layers, dramatically reducing build times.
  name: Incremental Builds
- description: Manages Helm chart deployments to Kubernetes with built-in rollback, planning, and drift detection (werf converge, werf plan, werf rollback).
  name: Kubernetes Deployment
- description: Automatically cleans up stale images from container registries using Git history-aware policies (werf cleanup, werf purge).
  name: Container Registry Cleanup
- description: Full Helm chart management including rendering, linting, bundling, and deploying with werf helm command suite.
  name: Helm Integration
- description: Native integration with GitHub Actions, GitLab CI, CircleCI, Jenkins, and other CI systems via werf ci-env.
  name: Multi-CI Support
- description: TRDL component provides TUF-based secure software update distribution with GPG signature verification.
  name: Secure Software Delivery
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/werf.png
integrations:
- description: Native GitHub Actions for incorporating werf into GitHub-hosted CI/CD pipelines.
  name: GitHub Actions
- description: First-class support for GitLab CI/CD environment variables and pipeline integration.
  name: GitLab CI
- description: Deep integration with Helm package manager for Kubernetes, extending it with werf-specific deployment guarantees.
  name: Helm
- description: Uses Buildah for rootless, daemonless OCI image builds without requiring Docker.
  name: Buildah
- description: Direct integration with Kubernetes API for deploying, monitoring, and managing application resources.
  name: Kubernetes
- description: Compatible with all OCI-compliant container registries including Docker Hub, GHCR, GitLab Registry, and cloud registries.
  name: OCI Registries
- description: CNCF Sandbox project integrating with the broader cloud-native ecosystem including Flux CD and other CNCF tools.
  name: CNCF Ecosystem
layout: provider
modified: '2026-05-03'
name: Werf
nav: Providers
network: true
overview: 'Werf is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include CI/CD, Deployment, DevOps, GitOps, and Kubernetes.


  Werf''s developer surface includes documentation, getting-started guide, CLI, changelog, support, and 9 more developer resources.'
random_paper: 26
score:
  band: emerging
  composite: 14.6
  delta: -1.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/werf/refs/heads/main/screenshots/werf-2026-06-20T201353.png
security:
- kind: domain-security
  name: Werf Domain Security
  slug: werf-domain-security
  summary_line: TLSv1.3
slug: werf
tags:
- CI/CD
- Deployment
- DevOps
- GitOps
- Kubernetes
- CNCF
- Helm
- Containers
- Open Source
use_cases:
- description: Build, test, and deploy containerized applications to Kubernetes clusters using GitOps principles.
  name: Kubernetes Application Delivery
- description: Manage CI/CD pipelines for monorepo projects with independent image tagging and selective component redeployment.
  name: Monorepo CI/CD
- description: Package, bundle, and deploy Helm charts with integrated dependency management and Kubernetes compatibility checks.
  name: Helm Chart Management
- description: Automate container image lifecycle from build to cleanup using content-based tagging and Git-aware retention policies.
  name: Container Registry Management
- description: Distribute software updates securely using TUF framework with TRDL, ensuring integrity and authenticity of delivered artifacts.
  name: Secure Software Distribution
website: https://werf.io/
---
