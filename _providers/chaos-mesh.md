---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 40
  human_in_the_loop: 0
  name: Chaos Mesh Agentic Access
  operation_count: 75
  slug: chaos-mesh-agentic-access
  summary_line: 75 operations · 40 acting
api_count: 2
apis:
- baseURL: http://localhost:2333/api
  baseurl_source: spec
  description: Access archived (completed or deleted) experiments, schedules, and workflows
  name: Chaos Mesh Archives API
  slug: chaos-mesh-archives-api
- baseURL: http://localhost:2333/api
  baseurl_source: spec
  description: Utility endpoints for cluster metadata, namespaces, and configuration
  name: Chaos Mesh Common API
  slug: chaos-mesh-common-api
- baseURL: http://localhost:2333/api
  baseurl_source: spec
  description: Query chaos experiment events and audit logs
  name: Chaos Mesh Events API
  slug: chaos-mesh-events-api
- baseURL: http://localhost:2333/api
  baseurl_source: spec
  description: Create, manage, pause, and delete chaos experiments
  name: Chaos Mesh Experiments API
  slug: chaos-mesh-experiments-api
- baseURL: http://localhost:2333/api
  baseurl_source: spec
  description: Create and manage scheduled chaos experiments
  name: Chaos Mesh Schedules API
  slug: chaos-mesh-schedules-api
- baseURL: http://localhost:2333/api
  baseurl_source: spec
  description: Manage reusable status check templates for workflows
  name: Chaos Mesh Templates API
  slug: chaos-mesh-templates-api
- baseURL: http://localhost:2333/api
  baseurl_source: spec
  description: Create and manage chaos engineering workflows with multiple steps
  name: Chaos Mesh Workflows API
  slug: chaos-mesh-workflows-api
artifact_total: 82
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Chaos Mesh Dashboard Archives API
  slug: open-chaos-mesh-archives-api
- collection_type: open
  name: Chaos Mesh Dashboard Archives Common API
  slug: open-chaos-mesh-common-api
- collection_type: open
  name: Chaos Mesh Dashboard API
  slug: open-chaos-mesh-dashboard-api
- collection_type: open
  name: Chaos Mesh Dashboard API
  slug: open-chaos-mesh-dashboard
- collection_type: open
  name: Chaos Mesh Dashboard Archives Events API
  slug: open-chaos-mesh-events-api
- collection_type: open
  name: Chaos Mesh Dashboard Archives Experiments API
  slug: open-chaos-mesh-experiments-api
- collection_type: open
  name: Chaos Mesh Dashboard Archives Schedules API
  slug: open-chaos-mesh-schedules-api
- collection_type: open
  name: Chaos Mesh Dashboard Archives Templates API
  slug: open-chaos-mesh-templates-api
- collection_type: open
  name: Chaos Mesh Dashboard Archives Workflows API
  slug: open-chaos-mesh-workflows-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/chaos-mesh/chaos-mesh/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/chaos-mesh/chaos-mesh/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/chaos-mesh/chaos-mesh/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/chaos-mesh/chaos-mesh/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/chaos-mesh/chaos-mesh/blob/master/CONTRIBUTING.md
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
overview: 'Chaos Mesh publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Archives API, Common API, Events API, and 4 more. Tagged areas include Chaos Engineering, Cloud-Native, CNCF, Fault Injection, and Kubernetes.


  The Chaos Mesh catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chaos Mesh''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, GitHub presence, and 16 more developer resources.'
plans:
- name: Chaos Mesh Plans Pricing
  plan_count: 3
  slug: chaos-mesh-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Chaos Mesh Rate Limits
  slug: chaos-mesh-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Chaos Mesh API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: chaos-mesh-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 61.3
    catalog_earned_first_party: 0.0
    catalog_gap: 53.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 64.0
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 39.5
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Cloud-Native
- CNCF
- Fault Injection
- Kubernetes
- Observability
- Open-Source
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
