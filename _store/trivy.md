---
aid: trivy
name: Trivy
description: Trivy is a comprehensive and versatile open-source security scanner from Aqua Security that finds vulnerabilities, misconfigurations, secrets, and SBOM in containers, Kubernetes, code repositories, clouds, and more. Trivy runs as a CLI tool, in client/server mode with an HTTP API, and as a Kubernetes Operator (trivy-operator) that continuously scans clusters and generates security reports as native Kubernetes Custom Resources.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Containers
  - Kubernetes
  - SBOM
  - Security
  - Vulnerability Scanning
  - Open Source
  - DevSecOps
  - Cloud Security
url: https://raw.githubusercontent.com/api-evangelist/trivy/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: trivy:trivy-server
    name: Trivy Server API
    description: Trivy can run in client/server mode where the server maintains vulnerability databases and clients submit scan requests. The server exposes HTTP endpoints including /healthz for liveness checks and /version for server version information. Authentication is via token-based header (Trivy-Token).
    humanURL: https://trivy.dev/latest/docs/references/modes/client-server/
    baseURL: http://localhost:4954
    tags:
      - Security
      - Vulnerability Scanning
      - Server Mode
      - HTTP API
    properties:
      - type: Documentation
        url: https://trivy.dev/latest/docs/references/modes/client-server/
      - type: GitHub Repository
        url: https://github.com/aquasecurity/trivy
      - type: OpenAPI
        url: openapi/trivy-server-openapi.yml
  - aid: trivy:trivy-operator
    name: Trivy Operator
    description: The Trivy Operator is a Kubernetes-native security toolkit that automatically scans clusters and generates security reports as Kubernetes Custom Resources. It defines 12 CRDs covering vulnerability reports, config audit reports, exposed secret reports, SBOM reports, RBAC assessment reports, infrastructure assessment reports, and compliance reports.
    humanURL: https://github.com/aquasecurity/trivy-operator
    baseURL: https://kubernetes.default.svc
    tags:
      - Kubernetes
      - Security
      - CRD
      - Operator
      - Vulnerability Scanning
    properties:
      - type: Documentation
        url: https://aquasecurity.github.io/trivy-operator/
      - type: GitHub Repository
        url: https://github.com/aquasecurity/trivy-operator
      - type: KubernetesCRD
        url: crd/aquasecurity.github.io_vulnerabilityreports.yaml
      - type: KubernetesCRD
        url: crd/aquasecurity.github.io_configauditreports.yaml
      - type: KubernetesCRD
        url: crd/aquasecurity.github.io_exposedsecretreports.yaml
      - type: KubernetesCRD
        url: crd/aquasecurity.github.io_sbomreports.yaml
      - type: KubernetesCRD
        url: crd/aquasecurity.github.io_clustercompliancereports.yaml
      - type: KubernetesCRD
        url: crd/aquasecurity.github.io_clusterconfigauditreports.yaml
      - type: KubernetesCRD
        url: crd/aquasecurity.github.io_clusterinfraassessmentreports.yaml
      - type: KubernetesCRD
        url: crd/aquasecurity.github.io_clusterrbacassessmentreports.yaml
      - type: KubernetesCRD
        url: crd/aquasecurity.github.io_clustersbomreports.yaml
      - type: KubernetesCRD
        url: crd/aquasecurity.github.io_clustervulnerabilityreports.yaml
      - type: KubernetesCRD
        url: crd/aquasecurity.github.io_infraassessmentreports.yaml
      - type: KubernetesCRD
        url: crd/aquasecurity.github.io_rbacassessmentreports.yaml
  - aid: trivy:trivy-cli
    name: Trivy CLI
    description: The primary interface for Trivy is its command-line tool, which scans container images, filesystems, Git repositories, Kubernetes clusters, virtual machine images, and SBOMs. Supports multiple output formats including JSON, SARIF, CycloneDX, SPDX, and table output for CI/CD integration.
    humanURL: https://trivy.dev/latest/docs/
    baseURL: https://trivy.dev
    tags:
      - CLI
      - Security
      - DevSecOps
      - Containers
      - Kubernetes
    properties:
      - type: Documentation
        url: https://trivy.dev/latest/docs/
      - type: Getting Started
        url: https://trivy.dev/latest/getting-started/installation/
      - type: GitHub Repository
        url: https://github.com/aquasecurity/trivy
common:
  - type: Website
    url: https://trivy.dev/
  - type: Documentation
    url: https://aquasecurity.github.io/trivy/
  - type: Getting Started
    url: https://aquasecurity.github.io/trivy/latest/getting-started/installation/
  - type: GitHub Organization
    url: https://github.com/aquasecurity
  - type: GitHub Repository
    url: https://github.com/aquasecurity/trivy
  - type: Trivy Operator
    url: https://github.com/aquasecurity/trivy-operator
  - type: GitHub Action
    url: https://github.com/aquasecurity/trivy-action
  - type: VS Code Extension
    url: https://github.com/aquasecurity/trivy-vscode-extension
  - type: Helm Chart
    url: https://artifacthub.io/packages/helm/aqua/trivy-operator
  - type: Docker Image
    url: https://hub.docker.com/r/aquasec/trivy
  - type: Releases
    url: https://github.com/aquasecurity/trivy/releases
  - type: OpenAPI
    url: openapi/trivy-server-openapi.yml
  - type: JSONSchema
    url: json-schema/trivy-vulnerability-report-schema.json
  - type: JSONSchema
    url: json-schema/trivy-scan-result-schema.json
  - type: JSON Structure
    url: json-structure/trivy-scan-structure.json
  - type: JSON-LD
    url: json-ld/trivy-context.jsonld
  - type: Spectral Rules
    url: rules/trivy-rules.yml
  - type: Naftiko Capability
    url: capabilities/security-scanning.yaml
  - type: Vocabulary
    url: vocabulary/trivy-vocabulary.yml
  - type: x-profiled
    url: 2026-05
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
