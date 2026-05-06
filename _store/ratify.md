---
aid: ratify
name: Ratify
description: Ratify is a CNCF Sandbox open-source verification framework for container images and other supply chain artifacts in Kubernetes environments. It enables policy-driven artifact ratification by coordinating any number of pluggable verifiers (signatures, SBOMs, scan results, attestations) against a given policy, integrating with Kubernetes admission webhooks via the Gatekeeper policy engine. Ratify is developed by the ratify-project GitHub organization (originally a Microsoft open-source project), written in Go, and distributed as a CLI tool, Go library, and Kubernetes admission webhook server. It supports OCI-compliant artifact stores including Azure Container Registry, Amazon ECR, and Docker Hub. Ratify exposes an internal HTTP verification API (v2alpha1) consumed by its webhook server but does not publish a public-facing REST API or OpenAPI specification.
type: Index
position: Consuming
access: 3rd-Party
url: https://raw.githubusercontent.com/api-evangelist/ratify/refs/heads/main/apis.yml
tags:
  - Artifact Verification
  - CNCF
  - Cloud Native
  - Container Security
  - Kubernetes
  - Open Source
  - Policy Enforcement
  - Security
  - Supply Chain
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis: []
common:
  - type: Website
    url: https://ratify.dev
  - type: Documentation
    url: https://ratify.dev/docs/what-is-ratify
  - type: SourceCode
    url: https://github.com/ratify-project/ratify
  - type: GitHubOrg
    url: https://github.com/ratify-project
  - type: PackageManager
    url: https://artifacthub.io/packages/helm/ratify/ratify
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
