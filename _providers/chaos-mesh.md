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
  band: agent-aware
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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 40
  human_in_the_loop: 0
  name: Chaos Mesh Agentic Access
  operation_count: 75
  slug: chaos-mesh-agentic-access
  summary_line: 75 operations · 40 acting
api_count: 7
apis:
- description: Access archived (completed or deleted) experiments, schedules, and workflows
  name: Chaos Mesh Archives API
  slug: chaos-mesh-archives-api
- description: Utility endpoints for cluster metadata, namespaces, and configuration
  name: Chaos Mesh Common API
  slug: chaos-mesh-common-api
- description: Query chaos experiment events and audit logs
  name: Chaos Mesh Events API
  slug: chaos-mesh-events-api
- description: Create, manage, pause, and delete chaos experiments
  name: Chaos Mesh Experiments API
  slug: chaos-mesh-experiments-api
- description: Create and manage scheduled chaos experiments
  name: Chaos Mesh Schedules API
  slug: chaos-mesh-schedules-api
- description: Manage reusable status check templates for workflows
  name: Chaos Mesh Templates API
  slug: chaos-mesh-templates-api
- description: Create and manage chaos engineering workflows with multiple steps
  name: Chaos Mesh Workflows API
  slug: chaos-mesh-workflows-api
artifact_total: 74
collections:
- collection_type: open
  name: Chaos Mesh Dashboard API
  slug: open-chaos-mesh-dashboard-api
- collection_type: open
  name: Chaos Mesh Dashboard API
  slug: open-chaos-mesh-dashboard
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chaos-mesh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chaos-mesh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chaos-mesh-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://chaos-mesh.org/
- group: docs
  title: ''
  type: Documentation
  url: https://chaos-mesh.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://chaos-mesh.org/docs/quick-start/
- group: company
  title: ''
  type: Blog
  url: https://chaos-mesh.org/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/chaos-mesh/chaos-mesh/blob/master/CHANGELOG.md
- group: build
  title: ''
  type: GitHub
  url: https://github.com/chaos-mesh
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/chaos-mesh/chaos-mesh
- group: operate
  title: ''
  type: Community
  url: https://chaos-mesh.org/community/
- group: commercial
  title: ''
  type: License
  url: https://github.com/chaos-mesh/chaos-mesh/blob/master/LICENSE
- group: other
  title: ''
  type: CNCF
  url: https://www.cncf.io/projects/chaos-mesh/
- group: operate
  title: ''
  type: Slack
  url: https://slack.cncf.io/
- group: other
  title: ''
  type: X
  url: https://x.com/chaos_mesh
- group: design
  title: ''
  type: JSONLD
  url: json-ld/chaos-mesh-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/chaos-mesh-experiment-schema.json
- group: other
  title: ''
  type: ChaosKinds
  url: ''
created: '2025-01-01'
description: Chaos Mesh is a CNCF graduated cloud-native chaos engineering platform that orchestrates chaos experiments on Kubernetes to test system resilience and reliability. It exposes Kubernetes Custom Resource Definitions (CRDs) for a wide range of chaos kinds (network, pod, IO, stress, DNS, time, kernel, JVM, HTTP), along with a Chaos Dashboard web UI backed by a REST API for creating, managing, and monitoring chaos experiments and workflows. Chaos Mesh integrates with Kubernetes, Argo Workflows, Prometheus, Grafana, and CI/CD pipelines to run experiments safely in staging and production environments.
features:
- name: Pod Chaos
- name: Network Chaos
- name: IO Chaos
- name: Stress Chaos
- name: Kernel Chaos
- name: Time Chaos
- name: DNS Chaos
- name: JVM Chaos
- name: HTTP Chaos
- name: AWS Chaos
- name: GCP Chaos
- name: Azure Chaos
- name: Block Chaos
- name: Physical Machine Chaos
- name: Workflows
- name: Schedules
- name: Chaos Dashboard
- name: Kubernetes CRDs
- name: REST API
- name: RBAC
- name: Audit Events
- name: Safe Mode
- name: Status Monitoring
finops:
- name: Chaos Mesh Finops
  service_category: API
  slug: chaos-mesh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chaos-mesh.png
integrations:
- name: Kubernetes
- name: EKS
- name: GKE
- name: AKS
- name: OpenShift
- name: Rancher
- name: Argo Workflows
- name: Argo CD
- name: Prometheus
- name: Grafana
- name: OpenTelemetry
- name: Jaeger
- name: Datadog
- name: Litmus
- name: GitHub Actions
- name: GitLab CI
- name: Jenkins
- name: Tekton
- name: Helm
- name: AWS
- name: Google Cloud
- name: Azure
json_schemas:
- name: Chaos Mesh Experiment
  property_count: 4
  slug: chaos-mesh-experiment
jsonld:
- class_count: 6
  name: Chaos Mesh Context
  property_count: 12
  slug: chaos-mesh-context
layout: provider
modified: '2026-05-19'
name: Chaos Mesh
nav: Providers
network: true
overview: 'Chaos Mesh publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Archives API, Common API, Events API, and 4 more. Tagged areas include Chaos Engineering, Cloud Native, CNCF, Fault Injection, and Kubernetes.


  The Chaos Mesh catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chaos Mesh''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, GitHub presence, and 11 more developer resources.'
plans:
- name: Chaos Mesh Plans Pricing
  plan_count: 3
  slug: chaos-mesh-plans-pricing
random_paper: 96
rate_limits:
- limit_count: 5
  name: Chaos Mesh Rate Limits
  slug: chaos-mesh-rate-limits
rules:
- name: Chaos Mesh API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: chaos-mesh-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.5
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chaos-mesh/refs/heads/main/screenshots/chaos-mesh-2026-06-20T174215.png
security:
- kind: authentication
  name: Chaos Mesh Authentication
  slug: chaos-mesh-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Chaos Mesh Domain Security
  slug: chaos-mesh-domain-security
  summary_line: TLSv1.3 · HSTS
slug: chaos-mesh
tags:
- Chaos Engineering
- Cloud Native
- CNCF
- Fault Injection
- Kubernetes
- Observability
- Open Source
- Reliability
- Resilience
- Testing
use_cases:
- name: Resilience Testing
- name: Disaster Recovery Drills
- name: SRE Game Days
- name: Canary Validation
- name: Production Reliability Testing
- name: Multi-Region Failover Testing
- name: Performance Bottleneck Discovery
- name: Observability Validation
- name: Continuous Chaos in CI/CD
- name: Microservices Dependency Testing
- name: Database Fault Tolerance Testing
website: https://chaos-mesh.org/
---
