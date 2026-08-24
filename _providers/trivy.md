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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Trivy Agentic Access
  operation_count: 2
  slug: trivy-agentic-access
  summary_line: 2 operations
api_count: 4
apis:
- description: The Trivy Operator is a Kubernetes-native security toolkit that automatically scans clusters and generates security reports as Kubernetes Custom Resources. It defines 12 CRDs covering vulnerability re
  name: Trivy Operator
  slug: trivy-operator
- description: 'The primary interface for Trivy is its command-line tool, which scans container images, filesystems, Git repositories, Kubernetes clusters, virtual machine images, and SBOMs. Supports multiple output '
  name: Trivy CLI
  slug: trivy-cli
- description: Server health and liveness checks
  name: Trivy Health API
  slug: trivy-health-api
- description: Server metadata and version information
  name: Trivy Server API
  slug: trivy-server-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trivy Server Health API
  slug: open-trivy-health-api
- collection_type: open
  name: Trivy Health Server API
  slug: open-trivy-server-api
- collection_type: open
  name: Trivy Server API
  slug: open-trivy-server
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/aquasecurity/trivy-operator/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trivy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trivy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trivy-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://trivy.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://aquasecurity.github.io/trivy/
- group: start
  title: ''
  type: GettingStarted
  url: https://aquasecurity.github.io/trivy/latest/getting-started/installation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aquasecurity
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/aquasecurity/trivy
- group: other
  title: ''
  type: Trivy Operator
  url: https://github.com/aquasecurity/trivy-operator
- group: build
  title: ''
  type: GitHub Action
  url: https://github.com/aquasecurity/trivy-action
- group: build
  title: ''
  type: VS Code Extension
  url: https://github.com/aquasecurity/trivy-vscode-extension
- group: other
  title: ''
  type: Helm Chart
  url: https://artifacthub.io/packages/helm/aqua/trivy-operator
- group: other
  title: ''
  type: Docker Image
  url: https://hub.docker.com/r/aquasec/trivy
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/aquasecurity/trivy/releases
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/trivy-server-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trivy-vulnerability-report-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trivy-scan-result-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/trivy-scan-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/trivy-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/trivy-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/trivy-vocabulary.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/aquasecurity/trivy-mcp
crds:
- name: aquasecurity.github.io clustercompliancereports
  url: https://raw.githubusercontent.com/api-evangelist/trivy/refs/heads/main/crd/aquasecurity.github.io_clustercompliancereports.yaml
- name: aquasecurity.github.io clusterconfigauditreports
  url: https://raw.githubusercontent.com/api-evangelist/trivy/refs/heads/main/crd/aquasecurity.github.io_clusterconfigauditreports.yaml
- name: aquasecurity.github.io clusterinfraassessmentreports
  url: https://raw.githubusercontent.com/api-evangelist/trivy/refs/heads/main/crd/aquasecurity.github.io_clusterinfraassessmentreports.yaml
- name: aquasecurity.github.io clusterrbacassessmentreports
  url: https://raw.githubusercontent.com/api-evangelist/trivy/refs/heads/main/crd/aquasecurity.github.io_clusterrbacassessmentreports.yaml
- name: aquasecurity.github.io clustersbomreports
  url: https://raw.githubusercontent.com/api-evangelist/trivy/refs/heads/main/crd/aquasecurity.github.io_clustersbomreports.yaml
- name: aquasecurity.github.io clustervulnerabilityreports
  url: https://raw.githubusercontent.com/api-evangelist/trivy/refs/heads/main/crd/aquasecurity.github.io_clustervulnerabilityreports.yaml
- name: aquasecurity.github.io configauditreports
  url: https://raw.githubusercontent.com/api-evangelist/trivy/refs/heads/main/crd/aquasecurity.github.io_configauditreports.yaml
- name: aquasecurity.github.io exposedsecretreports
  url: https://raw.githubusercontent.com/api-evangelist/trivy/refs/heads/main/crd/aquasecurity.github.io_exposedsecretreports.yaml
- name: aquasecurity.github.io infraassessmentreports
  url: https://raw.githubusercontent.com/api-evangelist/trivy/refs/heads/main/crd/aquasecurity.github.io_infraassessmentreports.yaml
- name: aquasecurity.github.io rbacassessmentreports
  url: https://raw.githubusercontent.com/api-evangelist/trivy/refs/heads/main/crd/aquasecurity.github.io_rbacassessmentreports.yaml
- name: aquasecurity.github.io sbomreports
  url: https://raw.githubusercontent.com/api-evangelist/trivy/refs/heads/main/crd/aquasecurity.github.io_sbomreports.yaml
- name: aquasecurity.github.io vulnerabilityreports
  url: https://raw.githubusercontent.com/api-evangelist/trivy/refs/heads/main/crd/aquasecurity.github.io_vulnerabilityreports.yaml
created: '2026-03-26'
description: Trivy is a comprehensive and versatile open-source security scanner from Aqua Security that finds vulnerabilities, misconfigurations, secrets, and SBOM in containers, Kubernetes, code repositories, clouds, and more. Trivy runs as a CLI tool, in client/server mode with an HTTP API, and as a Kubernetes Operator (trivy-operator) that continuously scans clusters and generates security reports as native Kubernetes Custom Resources.
examples:
- key_count: 4
  name: Trivy Health Check Example
  slug: trivy-health-check-example
- key_count: 4
  name: Trivy Vulnerability Report Example
  slug: trivy-vulnerability-report-example
finops:
- name: Trivy Finops
  service_category: API
  slug: trivy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trivy.png
json_schemas:
- name: Trivy Scan Result
  property_count: 5
  slug: trivy-scan-result
- name: Trivy Vulnerability Report
  property_count: 5
  slug: trivy-vulnerability-report
json_structures:
- name: Trivy Scan Structure
  property_count: 0
  slug: trivy-scan-structure
jsonld:
- class_count: 25
  name: Trivy Context
  property_count: 0
  slug: trivy-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Trivy
nav: Providers
network: true
overview: 'Trivy publishes 2 APIs on the [APIs.io](https://apis.io/) network: Health API and Server API. Tagged areas include Containers, Kubernetes, SBOM, Security, and Vulnerability Scanning.


  The Trivy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trivy''s developer surface includes authentication, documentation, getting-started guide, release notes, and 19 more developer resources.'
plans:
- name: Trivy Plans Pricing
  plan_count: 3
  slug: trivy-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Trivy Rate Limits
  slug: trivy-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Trivy API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: trivy-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Trivy API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: trivy-rules
score:
  band: thin
  composite: 32.9
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 17.4
    contract_quality: 53.8
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 17.4
    operational_transparency: 26.3
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trivy/refs/heads/main/screenshots/trivy-2026-06-20T195737.png
security:
- kind: authentication
  name: Trivy Authentication
  slug: trivy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Trivy Domain Security
  slug: trivy-domain-security
  summary_line: TLSv1.3
slug: trivy
tags:
- Containers
- Kubernetes
- SBOM
- Security
- Vulnerability Scanning
- Open-Source
- DevSecOps
- Cloud Security
website: https://trivy.dev/
---
