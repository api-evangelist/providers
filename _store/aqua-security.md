---
aid: aqua-security
name: Aqua Security
description: Aqua Security provides cloud-native security for the full application lifecycle, protecting containers, serverless functions, and cloud workloads with vulnerability scanning, runtime protection, and compliance enforcement.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Containers
  - Kubernetes
  - Runtime Protection
  - Security
  - Vulnerability Scanning
url: https://raw.githubusercontent.com/api-evangelist/aqua-security/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: aqua-security:aqua-security
    name: Aqua Security
    description: Aqua Security provides cloud-native security for the full application lifecycle, protecting containers, serverless functions, and cloud workloads with vulnerability scanning, runtime protection, and compliance enforcement.
    humanURL: https://www.aquasec.com/
    tags:
      - Cloud Native Security
      - Container Security
      - Kubernetes
      - Runtime Protection
      - Security
      - Vulnerability Scanning
      - CSPM
      - DevSecOps
    properties:
      - type: Documentation
        url: https://docs.aquasec.com/
      - type: GettingStarted
        url: https://docs.aquasec.com/docs/getting-started
      - type: APIReference
        url: https://docs.aquasec.com/reference/api-overview
      - type: Authentication
        url: https://docs.aquasec.com/reference/authentication
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/aqua-security/refs/heads/main/openapi/aqua-security-api.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/aqua-security/refs/heads/main/json-schema/aqua-security-api-container-list-schema.json
  - aid: aqua-security:trivy
    name: Trivy
    description: Trivy is a comprehensive open source security scanner for containers, Kubernetes, code repositories, clouds, and more — finding vulnerabilities, misconfigurations, secrets, and SBOMs.
    humanURL: https://trivy.dev/
    tags:
      - Container Scanning
      - Open Source
      - Vulnerability Scanner
      - SBOM
      - Kubernetes Security
    properties:
      - type: Documentation
        url: https://aquasecurity.github.io/trivy/
      - type: GettingStarted
        url: https://aquasecurity.github.io/trivy/latest/getting-started/installation/
      - type: GitHubRepository
        url: https://github.com/aquasecurity/trivy
  - aid: aqua-security:tracee
    name: Tracee
    description: Tracee is a runtime security and forensics tool for Linux that uses eBPF technology to trace system events and detect suspicious behavioral patterns.
    humanURL: https://aquasecurity.github.io/tracee/
    tags:
      - eBPF
      - Runtime Security
      - Linux Security
      - Forensics
      - Open Source
    properties:
      - type: Documentation
        url: https://aquasecurity.github.io/tracee/
      - type: GitHubRepository
        url: https://github.com/aquasecurity/tracee
common:
  - type: Portal
    url: https://www.aquasec.com/
  - type: Documentation
    url: https://docs.aquasec.com/
  - type: GitHubOrganization
    url: https://github.com/aquasecurity
  - type: Blog
    url: https://www.aquasec.com/blog/
  - type: Pricing
    url: https://www.aquasec.com/aqua-cloud/
  - type: SignUp
    url: https://www.aquasec.com/demo/
  - type: Support
    url: https://support.aquasec.com/
  - type: StatusPage
    url: https://status.aquasec.com/
  - type: TermsOfService
    url: https://www.aquasec.com/aqua-cloud/terms-of-service/
  - type: PrivacyPolicy
    url: https://www.aquasec.com/privacy-policy/
  - type: ReleaseNotes
    url: https://docs.aquasec.com/docs/release-notes
  - type: Features
    data:
      - name: Vulnerability Scanning
        description: Comprehensive scanning of container images, VM workloads, and serverless functions for known CVEs and misconfigurations.
      - name: Runtime Protection
        description: Real-time protection of running containers and cloud workloads using behavioral analysis and policy enforcement.
      - name: CSPM
        description: Cloud Security Posture Management to identify and remediate misconfigurations across AWS, Azure, and GCP.
      - name: Supply Chain Security
        description: Protect the software supply chain by scanning code, open source dependencies, and CI/CD pipelines.
      - name: Kubernetes Security
        description: Native Kubernetes security including admission control, runtime policies, and compliance benchmarks.
      - name: Compliance Enforcement
        description: Automated compliance checks against CIS, PCI-DSS, HIPAA, NIST, and other regulatory frameworks.
      - name: Secrets Detection
        description: Detect and prevent secrets and credentials from being embedded in container images and code repositories.
      - name: Network Policy
        description: Visualize and enforce container network connectivity and micro-segmentation policies.
  - type: UseCases
    data:
      - name: Container Security
        description: Secure Docker and OCI containers throughout the build-to-runtime lifecycle.
      - name: Kubernetes Security
        description: Enforce security policies, runtime protection, and compliance for Kubernetes clusters.
      - name: Serverless Security
        description: Protect AWS Lambda, Azure Functions, and Google Cloud Functions from vulnerabilities and runtime attacks.
      - name: DevSecOps
        description: Integrate security scanning into CI/CD pipelines to shift security left and prevent vulnerabilities from reaching production.
      - name: Cloud Workload Protection
        description: Protect VMs and cloud workloads across multi-cloud environments from threats and misconfigurations.
      - name: SBOM Generation
        description: Generate Software Bill of Materials (SBOM) for container images and code repositories to understand component risk.
  - type: Integrations
    data:
      - name: AWS
        description: Native integrations with AWS ECS, EKS, Lambda, ECR, Security Hub, and other AWS services.
      - name: Azure
        description: Integrations with Azure Kubernetes Service, Azure Container Registry, and Azure Security Center.
      - name: Google Cloud
        description: Support for GKE, Google Container Registry, and Cloud Run on Google Cloud Platform.
      - name: GitHub Actions
        description: Trivy GitHub Action for automated vulnerability scanning in CI/CD workflows.
      - name: Jenkins
        description: Jenkins plugin for container image scanning and policy enforcement in pipelines.
      - name: Terraform
        description: Terraform provider for declarative management of Aqua Security platform configuration.
      - name: Helm
        description: Official Helm charts for deploying Aqua Security components on Kubernetes.
      - name: Splunk
        description: Integration with Splunk for centralized security event logging and SIEM.
      - name: PagerDuty
        description: Alert routing to PagerDuty for runtime security event notifications.
      - name: Slack
        description: Security alert notifications delivered to Slack channels.
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/aqua-security/refs/heads/main/rules/aqua-security-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/aqua-security/refs/heads/main/vocabulary/aqua-security-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/aqua-security/refs/heads/main/json-ld/aqua-security-api-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
