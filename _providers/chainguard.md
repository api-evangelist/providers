---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 6
apis:
- description: Chainguard API v2 is the current REST API for the Chainguard platform. Endpoints cover Identity and Access Management (IAM), image registry operations, and vulnerability data under /iam/v2beta1/, /reg
  name: Chainguard API v2
  slug: api-v2
- description: Chainguard API v1 is the legacy REST API for the Chainguard platform, covering the same broad surface as v2 (IAM, registry, vulnerabilities) and remaining available for existing integrations while cus
  name: Chainguard API v1
  slug: api-v1
- description: The unified Chainguard API specification combines API v1 and v2 definitions in a single reference, useful for tool builders and readers who need a consolidated view of the platform surface.
  name: Chainguard Unified API Spec
  slug: unified-api-spec
- description: chainctl is the official command-line interface for the Chainguard platform. It provides commands for authentication, IAM, image management, registry operations, event subscriptions, packages, librari
  name: Chainguard chainctl CLI
  slug: chainctl
- description: The chainguard-dev/chainguard Terraform provider lets platform engineers provision and manage Chainguard resources (organizations, groups, identities, roles, subscriptions, and more) as infrastructure
  name: Chainguard Terraform Provider
  slug: terraform-provider
- description: cgr.dev is the OCI-compliant distribution endpoint for Chainguard Images. Standard OCI and Docker tooling (docker pull, cosign verify, oras, crane, etc.) can authenticate with a pull token or IAM cred
  name: Chainguard Images Registry (cgr.dev)
  slug: images-registry
artifact_total: 47
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chainguard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chainguard.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://edu.chainguard.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://edu.chainguard.dev/chainguard/api/
- group: learn
  title: ''
  type: Academy
  url: https://edu.chainguard.dev/
- group: company
  title: ''
  type: Blog
  url: https://www.chainguard.dev/unchained
- group: build
  title: ''
  type: GitHub
  url: https://github.com/chainguard-dev
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chainguard.dev/pricing
- group: start
  title: ''
  type: Signup
  url: https://console.chainguard.dev/
- group: start
  title: ''
  type: Console
  url: https://console.chainguard.dev/
- group: operate
  title: ''
  type: Contact
  url: https://www.chainguard.dev/contact
- group: company
  title: ''
  type: Careers
  url: https://www.chainguard.dev/careers
- group: auth
  title: ''
  type: Security
  url: https://www.chainguard.dev/trust
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chainguard.dev/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chainguard.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chainguard.dev/legal/privacy
- group: other
  title: ''
  type: X
  url: https://x.com/chainguard_dev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chainguard/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@chainguard_dev
- group: other
  title: ''
  type: Products
  url: ''
- group: agent
  title: ''
  type: AgentSkills
  url: https://www.chainguard.dev/unchained/introducing-chainguard-agent-skills
created: '2026-03-26'
description: Chainguard builds, secures, and maintains a catalog of hardened, minimal container images and software supply chain security tools. Its flagship Chainguard Images rebuild open source software from source daily on a zero-known-CVE promise, signed with Sigstore, and distributed through the cgr.dev registry. The Chainguard platform exposes REST APIs, a command- line tool (chainctl), a Terraform provider, and an SDK for managing organizations, IAM, image repositories, registries, vulnerabilities, and event subscriptions. Chainguard Libraries extends the model to language ecosystems (Java, Python, Go, Node.js).
features:
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
finops:
- name: Chainguard Finops
  service_category: API
  slug: chainguard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chainguard.png
layout: provider
modified: '2026-05-19'
name: Chainguard
nav: Providers
network: true
overview: 'Chainguard publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Native, Container Images, Containers, DevSecOps, and Kubernetes.


  Chainguard''s developer surface includes documentation, academy / training, engineering blog, GitHub presence, pricing, signup flow, developer console, and 13 more developer resources.'
plans:
- name: Chainguard Plans Pricing
  plan_count: 3
  slug: chainguard-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Chainguard Rate Limits
  slug: chainguard-rate-limits
score:
  band: thin
  composite: 34.1
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 63.2
  previous_composite: 34.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chainguard/refs/heads/main/screenshots/chainguard-2026-06-20T174155.png
security:
- kind: domain-security
  name: Chainguard Domain Security
  slug: chainguard-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chainguard
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
use_cases:
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
website: https://www.chainguard.dev/
---
