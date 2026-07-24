---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 59.6
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Aqua Security Agentic Access
  operation_count: 10
  slug: aqua-security-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 8
apis:
- description: Trivy is a comprehensive open source security scanner for containers, Kubernetes, code repositories, clouds, and more — finding vulnerabilities, misconfigurations, secrets, and SBOMs.
  name: Trivy
  slug: trivy
- description: Tracee is a runtime security and forensics tool for Linux that uses eBPF technology to trace system events and detect suspicious behavioral patterns.
  name: Tracee
  slug: tracee
- description: User authentication and token management
  name: Aqua Security Authentication API
  slug: aqua-security-authentication-api
- description: Running container monitoring and enforcement
  name: Aqua Security Containers API
  slug: aqua-security-containers-api
- description: Container image scanning and vulnerability management
  name: Aqua Security Images API
  slug: aqua-security-images-api
- description: Security policy management
  name: Aqua Security Policies API
  slug: aqua-security-policies-api
- description: Container registry configuration
  name: Aqua Security Registries API
  slug: aqua-security-registries-api
- description: User and role management
  name: Aqua Security Users API
  slug: aqua-security-users-api
arazzos:
- description: Authenticate, create an image assurance security policy, then list policies to confirm it was registered.
  name: Aqua Security Create Assurance Policy
  slug: aqua-security-create-assurance-policy-workflow
- description: Authenticate, poll an image scan to completion, then branch on whether critical or high vulnerabilities were found to pass or fail a compliance gate.
  name: Aqua Security Image Compliance Gate
  slug: aqua-security-image-compliance-gate-workflow
- description: Authenticate, list registered images filtered by registry and repository, then fetch full vulnerability detail for the first match.
  name: Aqua Security Image Vulnerability Lookup
  slug: aqua-security-image-vulnerability-lookup-workflow
- description: Authenticate, confirm the target registry is configured, register an image from it, then poll the scan to completion.
  name: Aqua Security Onboard Registry Image
  slug: aqua-security-onboard-registry-image-workflow
- description: Authenticate, list configured registries, then enumerate the images registered under the first connected registry.
  name: Aqua Security Registry Inventory
  slug: aqua-security-registry-inventory-workflow
- description: Authenticate, re-register an image to trigger a fresh scan, poll until it completes, then delete the image when its scan failed.
  name: Aqua Security Rescan And Cleanup
  slug: aqua-security-rescan-and-cleanup-workflow
- description: Authenticate, list running containers monitored by the enforcer, then read the image detail behind the first running container.
  name: Aqua Security Running Container Inventory
  slug: aqua-security-running-container-inventory-workflow
- description: Authenticate, register a container image for scanning, then poll until the scan completes and read its vulnerability counts.
  name: Aqua Security Scan Image On Demand
  slug: aqua-security-scan-image-on-demand-workflow
artifact_total: 102
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aqua-security-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aqua-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aqua-security-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aqua-security-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aqua-security-create-assurance-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aqua-security-image-compliance-gate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aqua-security-image-vulnerability-lookup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aqua-security-onboard-registry-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aqua-security-registry-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aqua-security-rescan-and-cleanup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aqua-security-running-container-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aqua-security-scan-image-on-demand-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aquasecteam
- group: start
  title: ''
  type: Portal
  url: https://www.aquasec.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aquasec.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aquasecurity
- group: company
  title: ''
  type: Blog
  url: https://www.aquasec.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aquasec.com/aqua-cloud/
- group: start
  title: ''
  type: Signup
  url: https://www.aquasec.com/demo/
- group: operate
  title: ''
  type: Support
  url: https://support.aquasec.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aquasec.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aquasec.com/aqua-cloud/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aquasec.com/privacy-policy/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.aquasec.com/docs/release-notes
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/aqua-security/refs/heads/main/rules/aqua-security-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/aqua-security/refs/heads/main/vocabulary/aqua-security-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/aqua-security/refs/heads/main/json-ld/aqua-security-api-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/aquasecurity/trivy-mcp
created: '2026-03-26'
description: Aqua Security provides cloud-native security for the full application lifecycle, protecting containers, serverless functions, and cloud workloads with vulnerability scanning, runtime protection, and compliance enforcement.
examples:
- key_count: 6
  name: Aqua Security Api Container Example
  slug: aqua-security-api-container-example
- key_count: 2
  name: Aqua Security Api Container List Example
  slug: aqua-security-api-container-list-example
- key_count: 2
  name: Aqua Security Api Error Response Example
  slug: aqua-security-api-error-response-example
- key_count: 11
  name: Aqua Security Api Image Detail Example
  slug: aqua-security-api-image-detail-example
- key_count: 7
  name: Aqua Security Api Image Example
  slug: aqua-security-api-image-example
- key_count: 2
  name: Aqua Security Api Image List Example
  slug: aqua-security-api-image-list-example
- key_count: 2
  name: Aqua Security Api Image Request Example
  slug: aqua-security-api-image-request-example
- key_count: 2
  name: Aqua Security Api Login Request Example
  slug: aqua-security-api-login-request-example
- key_count: 1
  name: Aqua Security Api Login Response Example
  slug: aqua-security-api-login-response-example
- key_count: 4
  name: Aqua Security Api Policy Example
  slug: aqua-security-api-policy-example
- key_count: 2
  name: Aqua Security Api Policy List Example
  slug: aqua-security-api-policy-list-example
- key_count: 4
  name: Aqua Security Api Policy Request Example
  slug: aqua-security-api-policy-request-example
- key_count: 5
  name: Aqua Security Api Registry Example
  slug: aqua-security-api-registry-example
- key_count: 2
  name: Aqua Security Api Registry List Example
  slug: aqua-security-api-registry-list-example
- key_count: 4
  name: Aqua Security Api User Example
  slug: aqua-security-api-user-example
- key_count: 2
  name: Aqua Security Api User List Example
  slug: aqua-security-api-user-list-example
- key_count: 5
  name: Aqua Security Api Vulnerability Counts Example
  slug: aqua-security-api-vulnerability-counts-example
features:
- description: Comprehensive scanning of container images, VM workloads, and serverless functions for known CVEs and misconfigurations.
  name: Vulnerability Scanning
- description: Real-time protection of running containers and cloud workloads using behavioral analysis and policy enforcement.
  name: Runtime Protection
- description: Cloud Security Posture Management to identify and remediate misconfigurations across AWS, Azure, and GCP.
  name: CSPM
- description: Protect the software supply chain by scanning code, open source dependencies, and CI/CD pipelines.
  name: Supply Chain Security
- description: Native Kubernetes security including admission control, runtime policies, and compliance benchmarks.
  name: Kubernetes Security
- description: Automated compliance checks against CIS, PCI-DSS, HIPAA, NIST, and other regulatory frameworks.
  name: Compliance Enforcement
- description: Detect and prevent secrets and credentials from being embedded in container images and code repositories.
  name: Secrets Detection
- description: Visualize and enforce container network connectivity and micro-segmentation policies.
  name: Network Policy
finops:
- name: Aqua Security Finops
  service_category: Security
  slug: aqua-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aqua-security.png
integrations:
- description: Native integrations with AWS ECS, EKS, Lambda, ECR, Security Hub, and other AWS services.
  name: AWS
- description: Integrations with Azure Kubernetes Service, Azure Container Registry, and Azure Security Center.
  name: Azure
- description: Support for GKE, Google Container Registry, and Cloud Run on Google Cloud Platform.
  name: Google Cloud
- description: Trivy GitHub Action for automated vulnerability scanning in CI/CD workflows.
  name: GitHub Actions
- description: Jenkins plugin for container image scanning and policy enforcement in pipelines.
  name: Jenkins
- description: Terraform provider for declarative management of Aqua Security platform configuration.
  name: Terraform
- description: Official Helm charts for deploying Aqua Security components on Kubernetes.
  name: Helm
- description: Integration with Splunk for centralized security event logging and SIEM.
  name: Splunk
- description: Alert routing to PagerDuty for runtime security event notifications.
  name: PagerDuty
- description: Security alert notifications delivered to Slack channels.
  name: Slack
json_schemas:
- name: ContainerList
  property_count: 2
  slug: aqua-security-api-container-list
- name: Container
  property_count: 6
  slug: aqua-security-api-container
- name: ErrorResponse
  property_count: 2
  slug: aqua-security-api-error-response
- name: ImageDetail
  property_count: 11
  slug: aqua-security-api-image-detail
- name: ImageList
  property_count: 2
  slug: aqua-security-api-image-list
- name: ImageRequest
  property_count: 2
  slug: aqua-security-api-image-request
- name: Image
  property_count: 7
  slug: aqua-security-api-image
- name: LoginRequest
  property_count: 2
  slug: aqua-security-api-login-request
- name: LoginResponse
  property_count: 1
  slug: aqua-security-api-login-response
- name: PolicyList
  property_count: 2
  slug: aqua-security-api-policy-list
- name: PolicyRequest
  property_count: 4
  slug: aqua-security-api-policy-request
- name: Policy
  property_count: 4
  slug: aqua-security-api-policy
- name: RegistryList
  property_count: 2
  slug: aqua-security-api-registry-list
- name: Registry
  property_count: 5
  slug: aqua-security-api-registry
- name: UserList
  property_count: 2
  slug: aqua-security-api-user-list
- name: User
  property_count: 4
  slug: aqua-security-api-user
- name: VulnerabilityCounts
  property_count: 5
  slug: aqua-security-api-vulnerability-counts
json_structures:
- name: Aqua Security Api Container List Structure
  property_count: 2
  slug: aqua-security-api-container-list-structure
- name: Aqua Security Api Container Structure
  property_count: 6
  slug: aqua-security-api-container-structure
- name: Aqua Security Api Error Response Structure
  property_count: 2
  slug: aqua-security-api-error-response-structure
- name: Aqua Security Api Image Detail Structure
  property_count: 11
  slug: aqua-security-api-image-detail-structure
- name: Aqua Security Api Image List Structure
  property_count: 2
  slug: aqua-security-api-image-list-structure
- name: Aqua Security Api Image Request Structure
  property_count: 2
  slug: aqua-security-api-image-request-structure
- name: Aqua Security Api Image Structure
  property_count: 7
  slug: aqua-security-api-image-structure
- name: Aqua Security Api Login Request Structure
  property_count: 2
  slug: aqua-security-api-login-request-structure
- name: Aqua Security Api Login Response Structure
  property_count: 1
  slug: aqua-security-api-login-response-structure
- name: Aqua Security Api Policy List Structure
  property_count: 2
  slug: aqua-security-api-policy-list-structure
- name: Aqua Security Api Policy Request Structure
  property_count: 4
  slug: aqua-security-api-policy-request-structure
- name: Aqua Security Api Policy Structure
  property_count: 4
  slug: aqua-security-api-policy-structure
- name: Aqua Security Api Registry List Structure
  property_count: 2
  slug: aqua-security-api-registry-list-structure
- name: Aqua Security Api Registry Structure
  property_count: 5
  slug: aqua-security-api-registry-structure
- name: Aqua Security Api User List Structure
  property_count: 2
  slug: aqua-security-api-user-list-structure
- name: Aqua Security Api User Structure
  property_count: 4
  slug: aqua-security-api-user-structure
- name: Aqua Security Api Vulnerability Counts Structure
  property_count: 5
  slug: aqua-security-api-vulnerability-counts-structure
jsonld:
- class_count: 20
  name: Aqua Security Api Context
  property_count: 28
  slug: aqua-security-api-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Aqua Security
nav: Providers
network: true
overview: 'Aqua Security publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Containers API, Images API, and 3 more. Tagged areas include Cloud Native, Containers, Kubernetes, Runtime Protection, and Security.


  The Aqua Security catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Aqua Security''s developer surface includes authentication, developer portal, documentation, engineering blog, pricing, signup flow, support, and 21 more developer resources.'
plans:
- name: Aqua Security Plans Pricing
  plan_count: 1
  slug: aqua-security-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 1
  name: Aqua Security Rate Limits
  slug: aqua-security-rate-limits
rules:
- name: Aqua Security API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: aqua-security-jsonschema-spectral-rules
- name: Aqua Security API Rules
  rule_count: 36
  severity_counts:
    error: 12
    hint: 0
    info: 3
    warn: 21
  slug: aqua-security-spectral-rules
score:
  band: strong
  composite: 66.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 77.0
    developer_ergonomics: 43.5
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 57.9
  previous_composite: 66.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aqua-security/refs/heads/main/screenshots/aqua-security-2026-06-20T172346.png
security:
- kind: authentication
  name: Aqua Security Authentication
  slug: aqua-security-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aqua Security Domain Security
  slug: aqua-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aqua Security Vulnerability Disclosure
  slug: aqua-security-vulnerability-disclosure
  summary_line: Bugcrowd
slug: aqua-security
tags:
- Cloud Native
- Containers
- Kubernetes
- Runtime Protection
- Security
- Vulnerability Scanning
use_cases:
- description: Secure Docker and OCI containers throughout the build-to-runtime lifecycle.
  name: Container Security
- description: Enforce security policies, runtime protection, and compliance for Kubernetes clusters.
  name: Kubernetes Security
- description: Protect AWS Lambda, Azure Functions, and Google Cloud Functions from vulnerabilities and runtime attacks.
  name: Serverless Security
- description: Integrate security scanning into CI/CD pipelines to shift security left and prevent vulnerabilities from reaching production.
  name: DevSecOps
- description: Protect VMs and cloud workloads across multi-cloud environments from threats and misconfigurations.
  name: Cloud Workload Protection
- description: Generate Software Bill of Materials (SBOM) for container images and code repositories to understand component risk.
  name: SBOM Generation
website: https://www.aquasec.com/
---
