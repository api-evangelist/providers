---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Anchore Agentic Access
  operation_count: 11
  slug: anchore-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 6
apis:
- description: The Images API from Anchore — 2 operation(s) for images.
  name: Anchore Images API
  slug: anchore-images-api
- description: The Policies API from Anchore — 2 operation(s) for policies.
  name: Anchore Policies API
  slug: anchore-policies-api
- description: The Registries API from Anchore — 1 operation(s) for registries.
  name: Anchore Registries API
  slug: anchore-registries-api
- description: The SBOM API from Anchore — 1 operation(s) for sbom.
  name: Anchore SBOM API
  slug: anchore-sbom-api
- description: The Subscriptions API from Anchore — 1 operation(s) for subscriptions.
  name: Anchore Subscriptions API
  slug: anchore-subscriptions-api
- description: The Vulnerabilities API from Anchore — 1 operation(s) for vulnerabilities.
  name: Anchore Vulnerabilities API
  slug: anchore-vulnerabilities-api
arazzos:
- description: Submit a container image for analysis, poll until analyzed, then pull its vulnerabilities and policy evaluation.
  name: Anchore Analyze Image End to End
  slug: anchore-analyze-image-workflow
- description: Create a new security policy, then immediately evaluate an analyzed image against it to observe the gate result.
  name: Anchore Create Policy and Evaluate Image
  slug: anchore-create-policy-and-evaluate-workflow
- description: Confirm an image is analyzed, then export its CycloneDX SBOM and its vulnerability report for downstream compliance use.
  name: Anchore Image SBOM and Vulnerability Pull
  slug: anchore-image-sbom-and-vulns-workflow
- description: Confirm a registry is configured, then submit an image from it for analysis and confirm the queue.
  name: Anchore Registry Image Onboarding
  slug: anchore-registry-scan-workflow
- description: Find an active analyzed image by tag, force a fresh vulnerability scan, and gate it against policy.
  name: Anchore Rescan Active Image and Gate
  slug: anchore-rescan-active-images-workflow
- description: Evaluate an analyzed image against policy and, when it fails the gate, subscribe to ongoing policy-evaluation notifications for its tag.
  name: Anchore Subscribe on Policy Failure
  slug: anchore-subscribe-on-policy-fail-workflow
artifact_total: 44
collections:
- collection_type: postman
  name: Anchore Enterprise API
  slug: postman-anchore-enterprise-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/anchore-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anchore-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anchore-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/anchore/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anchore-analyze-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anchore-create-policy-and-evaluate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anchore-image-sbom-and-vulns-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anchore-registry-scan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anchore-rescan-active-images-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anchore-subscribe-on-policy-fail-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/anchore
- group: start
  title: ''
  type: Portal
  url: https://anchore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anchore.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.anchore.com/current/docs/quickstart/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.anchore.com/current/docs/using/api_usage/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anchore
- group: company
  title: ''
  type: Blog
  url: https://anchore.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://anchore.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://anchore.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anchore.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anchore.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anchore.com/privacy-policy/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/anchore-image-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/anchore-vulnerability-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/anchore-sbom-schema.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/anchore-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/anchore-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/anchore-enterprise-api-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/anchore/grype-mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.anchore.com/llms.txt
created: '2026-03-26'
description: Anchore is a container and software supply chain security company providing open source and enterprise tools for vulnerability scanning, SBOM generation, policy enforcement, and continuous compliance. Core open source products include Syft (SBOM generator for container images and filesystems), Grype (vulnerability scanner), and Grant (license scanner). The Anchore Enterprise platform adds policy engines, CI/CD integrations, registry connectors, Kubernetes admission control, and reporting. Anchore supports CycloneDX and SPDX SBOM formats and integrates with Docker, Kubernetes, GitHub Actions, Jenkins, and major cloud registries.
features:
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
finops:
- name: Anchore Finops
  service_category: API
  slug: anchore-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anchore.png
json_schemas:
- name: Anchore Image
  property_count: 6
  slug: anchore-image
- name: Anchore SBOM
  property_count: 5
  slug: anchore-sbom
- name: Anchore Vulnerability
  property_count: 9
  slug: anchore-vulnerability
json_structures:
- name: Anchore Image Structure
  property_count: 0
  slug: anchore-image-structure
jsonld:
- class_count: 0
  name: Anchore Enterprise Api Context
  property_count: 14
  slug: anchore-enterprise-api-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Anchore
nav: Providers
network: true
overview: 'Anchore publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Images API, Policies API, Registries API, and 3 more. Tagged areas include Container Security, Containers, SBOM, Software Supply Chain, and Vulnerability Scanning.


  The Anchore catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Anchore''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, pricing, and 23 more developer resources.'
plans:
- name: Anchore Plans Pricing
  plan_count: 3
  slug: anchore-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 5
  name: Anchore Rate Limits
  slug: anchore-rate-limits
rules:
- name: Anchore API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: anchore-jsonschema-spectral-rules
- name: Anchore API Rules
  rule_count: 19
  severity_counts:
    error: 5
    hint: 1
    info: 1
    warn: 12
  slug: anchore-spectral-rules
score:
  band: exemplar
  composite: 66.5
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 72.1
    developer_ergonomics: 58.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 66.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/screenshots/anchore-2026-07-25T200203.png
security:
- kind: authentication
  name: Anchore Authentication
  slug: anchore-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Anchore Domain Security
  slug: anchore-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: anchore
tags:
- Container Security
- Containers
- SBOM
- Software Supply Chain
- Vulnerability Scanning
use_cases:
- Shift-left container security scanning in CI/CD pipelines
- Generate SBOMs for software supply chain transparency
- Enforce image policies at Kubernetes admission control
- Track vulnerabilities across container registries and deployed images
- License compliance scanning for open source components
- Continuous compliance monitoring for regulated industries
- Developer self-service security scanning via CLI tools
website: https://anchore.com/
---
