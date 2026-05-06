---
aid: werf
name: Werf
description: Werf is an open-source CNCF sandbox project providing a complete GitOps-based CI/CD solution for Kubernetes. It implements the full application delivery lifecycle — building images, managing dependencies, deploying Helm charts, and cleaning up container registries — using Git as the single source of truth (Giterminism). Werf integrates natively with all major CI systems, Buildah, Helm, and Kubernetes.
type: Index
url: https://werf.io/
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
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis: []
common:
  - type: Website
    url: https://werf.io/
  - type: Documentation
    url: https://werf.io/docs/v2/
  - type: GettingStarted
    url: https://werf.io/getting_started/
  - type: GitHubOrganization
    url: https://github.com/werf
  - type: GitHubRepository
    url: https://github.com/werf/werf
  - type: CLI
    url: https://github.com/werf/werf
    title: Werf CLI
  - type: GitHubRepository
    url: https://github.com/werf/nelm
    title: Nelm (Helm 4 Alternative)
  - type: GitHubRepository
    url: https://github.com/werf/kubedog
    title: Kubedog Kubernetes Watch Library
  - type: GitHubRepository
    url: https://github.com/werf/trdl
    title: TRDL Secure Software Delivery
  - type: GitHubRepository
    url: https://github.com/werf/actions
    title: GitHub Actions Integration
  - type: GitHubRepository
    url: https://github.com/werf/nelm-chart-ts-sdk
    title: Nelm Chart TypeScript SDK
  - type: ChangeLog
    url: https://github.com/werf/werf/releases
  - type: Support
    url: https://github.com/werf/werf/discussions
  - type: Features
    data:
      - name: Giterminism
        description: Uses Git as the single source of truth, ensuring all CI/CD configurations are reproducible and auditable from version control.
      - name: Incremental Builds
        description: Rebuilds only modified components and reuses existing container registry layers, dramatically reducing build times.
      - name: Kubernetes Deployment
        description: Manages Helm chart deployments to Kubernetes with built-in rollback, planning, and drift detection (werf converge, werf plan, werf rollback).
      - name: Container Registry Cleanup
        description: Automatically cleans up stale images from container registries using Git history-aware policies (werf cleanup, werf purge).
      - name: Helm Integration
        description: Full Helm chart management including rendering, linting, bundling, and deploying with werf helm command suite.
      - name: Multi-CI Support
        description: Native integration with GitHub Actions, GitLab CI, CircleCI, Jenkins, and other CI systems via werf ci-env.
      - name: Secure Software Delivery
        description: TRDL component provides TUF-based secure software update distribution with GPG signature verification.
  - type: UseCases
    data:
      - name: Kubernetes Application Delivery
        description: Build, test, and deploy containerized applications to Kubernetes clusters using GitOps principles.
      - name: Monorepo CI/CD
        description: Manage CI/CD pipelines for monorepo projects with independent image tagging and selective component redeployment.
      - name: Helm Chart Management
        description: Package, bundle, and deploy Helm charts with integrated dependency management and Kubernetes compatibility checks.
      - name: Container Registry Management
        description: Automate container image lifecycle from build to cleanup using content-based tagging and Git-aware retention policies.
      - name: Secure Software Distribution
        description: Distribute software updates securely using TUF framework with TRDL, ensuring integrity and authenticity of delivered artifacts.
  - type: Integrations
    data:
      - name: GitHub Actions
        description: Native GitHub Actions for incorporating werf into GitHub-hosted CI/CD pipelines.
      - name: GitLab CI
        description: First-class support for GitLab CI/CD environment variables and pipeline integration.
      - name: Helm
        description: Deep integration with Helm package manager for Kubernetes, extending it with werf-specific deployment guarantees.
      - name: Buildah
        description: Uses Buildah for rootless, daemonless OCI image builds without requiring Docker.
      - name: Kubernetes
        description: Direct integration with Kubernetes API for deploying, monitoring, and managing application resources.
      - name: OCI Registries
        description: Compatible with all OCI-compliant container registries including Docker Hub, GHCR, GitLab Registry, and cloud registries.
      - name: CNCF Ecosystem
        description: CNCF Sandbox project integrating with the broader cloud-native ecosystem including Flux CD and other CNCF tools.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
