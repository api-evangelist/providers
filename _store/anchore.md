---
aid: anchore
name: Anchore
description: Anchore is a container and software supply chain security company providing open source and enterprise tools for vulnerability scanning, SBOM generation, policy enforcement, and continuous compliance. Core open source products include Syft (SBOM generator for container images and filesystems), Grype (vulnerability scanner), and Grant (license scanner). The Anchore Enterprise platform adds policy engines, CI/CD integrations, registry connectors, Kubernetes admission control, and reporting. Anchore supports CycloneDX and SPDX SBOM formats and integrates with Docker, Kubernetes, GitHub Actions, Jenkins, and major cloud registries.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Container Security
  - Containers
  - SBOM
  - Software Supply Chain
  - Vulnerability Scanning
url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: anchore:anchore-enterprise-api
    name: Anchore Enterprise API
    description: REST API for Anchore Enterprise providing image analysis, vulnerability scanning, policy evaluation, SBOM generation, subscription management, and reporting endpoints for enterprise container security workflows.
    humanURL: https://docs.anchore.com/current/docs/using/api_usage/
    baseURL: https://anchore.example.com/v2
    tags:
      - Container Security
      - Enterprise
      - Policy
      - Vulnerability Scanning
    properties:
      - type: OpenAPI
        url: openapi/anchore-enterprise-api.yaml
      - type: Documentation
        url: https://docs.anchore.com/current/docs/using/api_usage/
      - type: JSONSchema
        url: json-schema/anchore-image-schema.json
      - type: JSONSchema
        url: json-schema/anchore-vulnerability-schema.json
      - type: JSONSchema
        url: json-schema/anchore-sbom-schema.json
      - type: SpectralRules
        url: rules/anchore-spectral-rules.yml
      - type: NaftikoCapability
        url: capabilities/anchore-container-security.yaml
      - type: JSONStructure
        url: json-structure/anchore-image-structure.json
      - type: JSONLD
        url: json-ld/anchore-enterprise-api-context.jsonld
      - type: Vocabulary
        url: vocabulary/anchore-vocabulary.yaml
common:
  - type: Portal
    url: https://anchore.com/
  - type: Documentation
    url: https://docs.anchore.com/
  - type: GettingStarted
    url: https://docs.anchore.com/current/docs/quickstart/
  - type: Authentication
    url: https://docs.anchore.com/current/docs/using/api_usage/
  - type: GitHubOrganization
    url: https://github.com/anchore
  - type: Blog
    url: https://anchore.com/blog/
  - type: Support
    url: https://anchore.com/support/
  - type: Pricing
    url: https://anchore.com/pricing/
  - type: StatusPage
    url: https://status.anchore.com/
  - type: TermsOfService
    url: https://anchore.com/terms-of-service/
  - type: PrivacyPolicy
    url: https://anchore.com/privacy-policy/
  - type: JSONSchema
    url: json-schema/anchore-image-schema.json
  - type: JSONSchema
    url: json-schema/anchore-vulnerability-schema.json
  - type: JSONSchema
    url: json-schema/anchore-sbom-schema.json
  - type: SpectralRules
    url: rules/anchore-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/anchore-vocabulary.yaml
  - type: JSONLD
    url: json-ld/anchore-enterprise-api-context.jsonld
  - type: Features
    data:
      - Container image vulnerability scanning (OS and language packages)
      - SBOM generation in CycloneDX and SPDX formats (Syft)
      - Policy-based compliance enforcement
      - Kubernetes admission controller integration
      - CI/CD pipeline integration (GitHub Actions, Jenkins, GitLab)
      - Registry connectors (Docker Hub, ECR, GCR, ACR, Harbor)
      - License scanning and compliance (Grant)
      - Grype vulnerability database with NVD, GitHub Advisory, and custom feeds
      - Anchore Enterprise reporting and audit logging
      - REST API for image analysis, subscriptions, and notifications
  - type: UseCases
    data:
      - Shift-left container security scanning in CI/CD pipelines
      - Generate SBOMs for software supply chain transparency
      - Enforce image policies at Kubernetes admission control
      - Track vulnerabilities across container registries and deployed images
      - License compliance scanning for open source components
      - Continuous compliance monitoring for regulated industries
      - Developer self-service security scanning via CLI tools
  - type: Integrations
    data:
      - GitHub Actions (syft-action, scan-action)
      - Kubernetes (anchore-charts, admission controller)
      - Docker and OCI registries
      - Jenkins pipeline integration
      - Harbor registry integration
      - Amazon ECR, Google GCR, Azure ACR
      - Grype vulnerability database
      - CycloneDX and SPDX SBOM standards
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
