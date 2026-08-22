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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Helm Agentic Access
  operation_count: 10
  slug: helm-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 10
apis:
- description: JSON Schema defining the structure and validation rules for Chart.yaml, the metadata file required in every Helm chart. Describes chart name, version, dependencies, maintainers, and other metadata fie
  name: Helm Chart.yaml Schema
  slug: chart-yaml-schema
- description: JSON Schema describing common conventional patterns for values.yaml files in Helm charts. Values.yaml provides default configuration values including container image settings, service configuration, i
  name: Helm Values YAML Schema
  slug: values-yaml-schema
- description: JSON Schema for the index.yaml file served by Helm chart repositories. The index is the primary discovery mechanism listing all available charts and versions with download URLs and integrity digests.
  name: Helm Repository Index Schema
  slug: repository-index-schema
- description: JSON-LD context document mapping Helm concepts to linked data vocabularies including Schema.org, Dublin Core, SPDX, FOAF, and W3C PROV. Enables semantic interoperability of Helm chart metadata.
  name: Helm JSON-LD Context
  slug: json-ld-context
- description: The Helm Go SDK provides Go packages for programmatically performing Helm actions such as install, upgrade, list, and rollback without using the CLI. The SDK is published as helm.sh/helm/v3 and provid
  name: Helm Go SDK
  slug: go-sdk
- description: The Helm Plugins API defines the interface for extending the Helm CLI with additional subcommands. Plugins live in a single directory with a plugin.yaml descriptor and can be implemented as shell scri
  name: Helm Plugins
  slug: plugins
- description: The Helm Chart Template API defines the Go template language extensions, built-in objects, and Sprig function library available for authoring Helm chart templates. Templates render Kubernetes manifest
  name: Helm Chart Template API
  slug: chart-template-api
- description: Extended API endpoints provided by ChartMuseum and compatible chart repository servers for JSON-based chart management.
  name: Helm ChartMuseum API
  slug: helm-chartmuseum-api
- description: Chart package download endpoints for retrieving packaged chart archives and provenance files for signature verification.
  name: Helm Charts API
  slug: helm-charts-api
- description: Standard Helm chart repository endpoints for index and chart download. These endpoints are required for any Helm-compatible chart repository.
  name: Helm Repository API
  slug: helm-repository-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Helm Chart Repository API
  slug: open-helm-chart-repository
- collection_type: open
  name: Helm Chart Repository ChartMuseum API
  slug: open-helm-chartmuseum-api
- collection_type: open
  name: Helm Chart Repository ChartMuseum Charts API
  slug: open-helm-charts-api
- collection_type: open
  name: Helm Chart ChartMuseum Repository API
  slug: open-helm-repository-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/helm/helm/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/helm/helm/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/helm/helm/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/helm/helm/blob/main/code-of-conduct.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/helm/helm/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/helm/helm/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/helm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helm-domain-security.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/helm-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/helm-plugin-schema.json
- group: company
  title: ''
  type: Website
  url: https://helm.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://helm.sh/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://helm.sh/docs/intro/quickstart/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/helm
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/helm/helm
- group: company
  title: ''
  type: Blog
  url: https://helm.sh/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://helm.sh/docs/changelog/
- group: operate
  title: ''
  type: Community
  url: https://helm.sh/community/
- group: operate
  title: ''
  type: Slack
  url: https://kubernetes.slack.com/messages/helm-users
- group: auth
  title: ''
  type: Security
  url: https://helm.sh/community/SECURITY
- group: other
  title: ''
  type: ArtifactHub
  url: https://artifacthub.io/
created: '2025'
description: Package manager for Kubernetes that helps you define, install, and upgrade complex Kubernetes applications using charts. Helm uses a packaging format called charts, which are collections of files that describe a related set of Kubernetes resources. A chart repository is an HTTP server that houses an index.yaml file and packaged chart archives.
finops:
- name: Helm Finops
  service_category: Open Source / DevOps
  slug: helm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/helm.png
json_schemas:
- name: Helm Chart.yaml
  property_count: 15
  slug: helm-chart-yaml
- name: Helm Plugin Descriptor
  property_count: 10
  slug: helm-plugin
- name: Helm Chart Repository Index
  property_count: 3
  slug: helm-repository-index
- name: Helm Values YAML
  property_count: 17
  slug: helm-values-yaml
jsonld:
- class_count: 0
  name: Helm Context
  property_count: 11
  slug: helm-context
layout: provider
modified: '2026-05-19'
name: Helm
nav: Providers
network: true
overview: 'Helm publishes 3 APIs on the [APIs.io](https://apis.io/) network: ChartMuseum API, Charts API, and Repository API. Tagged areas include Charts, Cloud Native, Container Orchestration, DevOps, and Kubernetes.


  The Helm catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Helm''s developer surface includes documentation, getting-started guide, engineering blog, changelog, and 17 more developer resources.'
plans:
- name: Helm Plans Pricing
  plan_count: 1
  slug: helm-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Helm Rate Limits
  slug: helm-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Helm API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: helm-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.8
  delta: -6.4
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 61.1
    developer_ergonomics: 28.6
    discoverability: 72.2
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/helm/refs/heads/main/screenshots/helm-2026-06-20T182629.png
security:
- kind: domain-security
  name: Helm Domain Security
  slug: helm-domain-security
  summary_line: TLSv1.3 · HSTS
slug: helm
tags:
- Charts
- Cloud Native
- Container Orchestration
- DevOps
- Kubernetes
- Package Manager
website: https://helm.sh/
---
