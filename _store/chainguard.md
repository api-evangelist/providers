---
aid: chainguard
url: https://raw.githubusercontent.com/api-evangelist/chainguard/refs/heads/main/apis.yml
name: Chainguard
x-type: company
description: Chainguard builds, secures, and maintains a catalog of hardened, minimal container images and software supply chain security tools. Its flagship Chainguard Images rebuild open source software from source daily on a zero-known-CVE promise, signed with Sigstore, and distributed through the cgr.dev registry. The Chainguard platform exposes REST APIs, a command- line tool (chainctl), a Terraform provider, and an SDK for managing organizations, IAM, image repositories, registries, vulnerabilities, and event subscriptions. Chainguard Libraries extends the model to language ecosystems (Java, Python, Go, Node.js).
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
tags:
  - Cloud Native
  - Container Images
  - Containers
  - DevSecOps
  - Kubernetes
  - Registry
  - Security
  - Software Supply Chain
  - Vulnerability Management
created: '2026-03-26'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
apis:
  - aid: chainguard:api-v2
    name: Chainguard API v2
    description: Chainguard API v2 is the current REST API for the Chainguard platform. Endpoints cover Identity and Access Management (IAM), image registry operations, and vulnerability data under /iam/v2beta1/, /registry/v2beta1/, and /vulnerabilities/v2beta1/. v2 introduces cursor-based pagination, server-side ordering, consistent resource patterns, and structured error responses.
    humanURL: https://edu.chainguard.dev/chainguard/api/spec-api-v2/
    baseURL: https://console-api.enforce.dev
    tags:
      - IAM
      - REST
      - Registry
      - Vulnerabilities
    properties:
      - type: Documentation
        url: https://edu.chainguard.dev/chainguard/api/spec-api-v2/
      - type: Tutorial
        url: https://edu.chainguard.dev/chainguard/api/api-v2-tutorial/
      - type: Authentication
        url: https://edu.chainguard.dev/chainguard/api/authentication/
  - aid: chainguard:api-v1
    name: Chainguard API v1
    description: Chainguard API v1 is the legacy REST API for the Chainguard platform, covering the same broad surface as v2 (IAM, registry, vulnerabilities) and remaining available for existing integrations while customers migrate to v2.
    humanURL: https://edu.chainguard.dev/chainguard/api/spec-api-v1/
    baseURL: https://console-api.enforce.dev
    tags:
      - IAM
      - Legacy
      - REST
      - Registry
      - Vulnerabilities
    properties:
      - type: Documentation
        url: https://edu.chainguard.dev/chainguard/api/spec-api-v1/
      - type: Authentication
        url: https://edu.chainguard.dev/chainguard/api/authentication/
  - aid: chainguard:unified-api-spec
    name: Chainguard Unified API Spec
    description: The unified Chainguard API specification combines API v1 and v2 definitions in a single reference, useful for tool builders and readers who need a consolidated view of the platform surface.
    humanURL: https://edu.chainguard.dev/chainguard/api/spec/
    tags:
      - OpenAPI
      - Reference
    properties:
      - type: Documentation
        url: https://edu.chainguard.dev/chainguard/api/spec/
  - aid: chainguard:chainctl
    name: Chainguard chainctl CLI
    description: chainctl is the official command-line interface for the Chainguard platform. It provides commands for authentication, IAM, image management, registry operations, event subscriptions, packages, libraries, and configuration. chainctl uses the same underlying APIs (v1 and v2) and is often the fastest path to automating Chainguard workflows.
    humanURL: https://edu.chainguard.dev/chainguard/chainctl/chainctl-docs/chainctl/
    tags:
      - Automation
      - CLI
      - Tooling
    properties:
      - type: Documentation
        url: https://edu.chainguard.dev/chainguard/chainctl/chainctl-docs/chainctl/
      - type: Authentication
        url: https://edu.chainguard.dev/chainguard/chainctl/chainctl-docs/chainctl_auth/
      - type: GitHubRepository
        url: https://github.com/chainguard-dev/chainctl-releases
  - aid: chainguard:terraform-provider
    name: Chainguard Terraform Provider
    description: The chainguard-dev/chainguard Terraform provider lets platform engineers provision and manage Chainguard resources (organizations, groups, identities, roles, subscriptions, and more) as infrastructure-as-code through the Chainguard API.
    humanURL: https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs
    tags:
      - IaC
      - Provisioning
      - Terraform
    properties:
      - type: Documentation
        url: https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs
      - type: GitHubRepository
        url: https://github.com/chainguard-dev/terraform-provider-chainguard
  - aid: chainguard:images-registry
    name: Chainguard Images Registry (cgr.dev)
    description: cgr.dev is the OCI-compliant distribution endpoint for Chainguard Images. Standard OCI and Docker tooling (docker pull, cosign verify, oras, crane, etc.) can authenticate with a pull token or IAM credentials to list tags, fetch images, and verify signatures and attestations.
    humanURL: https://edu.chainguard.dev/chainguard/chainguard-images/
    baseURL: https://cgr.dev
    tags:
      - Cosign
      - Distribution
      - OCI
      - Registry
      - Sigstore
    properties:
      - type: Documentation
        url: https://edu.chainguard.dev/chainguard/chainguard-images/
      - type: Overview
        url: https://edu.chainguard.dev/chainguard/chainguard-images/overview/
common:
  - type: Website
    url: https://www.chainguard.dev/
  - type: Documentation
    url: https://edu.chainguard.dev/
  - type: DeveloperPortal
    url: https://edu.chainguard.dev/chainguard/api/
  - type: Academy
    url: https://edu.chainguard.dev/
  - type: Blog
    url: https://www.chainguard.dev/unchained
  - type: GitHub
    url: https://github.com/chainguard-dev
  - type: Pricing
    url: https://www.chainguard.dev/pricing
  - type: SignUp
    url: https://console.chainguard.dev/
  - type: Console
    url: https://console.chainguard.dev/
  - type: Contact
    url: https://www.chainguard.dev/contact
  - type: Careers
    url: https://www.chainguard.dev/careers
  - type: Security
    url: https://www.chainguard.dev/trust
  - type: StatusPage
    url: https://status.chainguard.dev/
  - type: TermsOfService
    url: https://www.chainguard.dev/legal/terms
  - type: PrivacyPolicy
    url: https://www.chainguard.dev/legal/privacy
  - type: X
    url: https://x.com/chainguard_dev
  - type: LinkedIn
    url: https://www.linkedin.com/company/chainguard/
  - type: YouTube
    url: https://www.youtube.com/@chainguard_dev
  - name: Features
    type: Features
    data:
      - name: Hardened Images
      - name: Minimal Images
      - name: Distroless
      - name: Zero-Known-CVE
      - name: SBOMs
      - name: SLSA Attestations
      - name: Sigstore Signatures
      - name: Cosign Verification
      - name: Daily Rebuilds
      - name: Wolfi OS Base
      - name: OCI Registry
      - name: IAM
      - name: RBAC
      - name: Audit Logs
      - name: Event Subscriptions
      - name: Vulnerability Feed
      - name: Custom Assembly
      - name: FIPS Images
      - name: STIG Hardening
      - name: Libraries for Java
      - name: Libraries for Python
      - name: Libraries for Go
      - name: Libraries for Node.js
      - name: Terraform Provider
      - name: CLI (chainctl)
      - name: REST API
  - name: UseCases
    type: UseCases
    data:
      - name: Software Supply Chain Security
      - name: Container Hardening
      - name: CVE Remediation
      - name: Compliance (FedRAMP, FIPS, PCI, HIPAA)
      - name: Open Source Dependency Security
      - name: Secure Base Images
      - name: Air-Gapped Distribution
      - name: Kubernetes Workload Security
      - name: CI/CD Integration
      - name: Image Signing and Verification
      - name: Vulnerability Scanning Reduction
  - name: Integrations
    type: Integrations
    data:
      - name: Kubernetes
      - name: Docker
      - name: OCI
      - name: Sigstore
      - name: Cosign
      - name: SLSA
      - name: Terraform
      - name: GitHub Actions
      - name: GitLab CI
      - name: Jenkins
      - name: Argo CD
      - name: Tekton
      - name: Harbor
      - name: Quay
      - name: Amazon ECR
      - name: Google Artifact Registry
      - name: Azure Container Registry
      - name: Snyk
      - name: Prisma Cloud
      - name: Wiz
      - name: Trivy
      - name: Grype
      - name: Syft
      - name: AWS
      - name: Google Cloud
      - name: Azure
  - name: Products
    type: Products
    data:
      - name: Chainguard Images
      - name: Chainguard Libraries
      - name: Chainguard Enforce
      - name: Chainguard VMs
      - name: Chainguard Containers
      - name: Wolfi OS
      - name: Custom Assembly
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
