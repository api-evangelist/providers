---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Cri O Agentic Access
  operation_count: 7
  slug: cri-o-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 6
apis:
- description: CRI-O implements the Kubernetes Container Runtime Interface (CRI) gRPC API that the kubelet uses to manage pod sandboxes, containers, image lifecycle, and runtime status. The CRI gRPC API is served ov
  name: CRI-O CRI gRPC API
  slug: cri-o-cri-grpc-api
- description: Endpoints that return information about live containers.
  name: CRI-O Containers API
  slug: cri-o-containers-api
- description: Golang debug endpoints for goroutines, heap, and profiling.
  name: CRI-O Debug API
  slug: cri-o-debug-api
- description: Runtime version, configuration, and general info endpoints.
  name: CRI-O Information API
  slug: cri-o-information-api
- description: Endpoints to pause and unpause running containers.
  name: CRI-O Lifecycle API
  slug: cri-o-lifecycle-api
- description: Prometheus metrics scraping endpoint.
  name: CRI-O Metrics API
  slug: cri-o-metrics-api
artifact_total: 15
collections:
- collection_type: open
  name: CRI-O Metrics API
  slug: open-cri-o-metrics
- collection_type: open
  name: CRI-O Status API
  slug: open-cri-o-status
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cri-o-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cri-o-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cri-o.io/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/cri-o/cri-o/tree/main/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/cri-o/cri-o/blob/main/install.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cri-o
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cri-o/cri-o
- group: company
  title: ''
  type: Blog
  url: https://cri-o.io/#blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/cri-o/cri-o/releases
- group: operate
  title: ''
  type: Community
  url: https://github.com/cri-o/cri-o#getting-started
- group: commercial
  title: ''
  type: License
  url: https://github.com/cri-o/cri-o/blob/main/LICENSE
- group: other
  title: ''
  type: CNCF
  url: https://www.cncf.io/projects/cri-o/
created: '2025-01-01'
description: CRI-O is a CNCF graduated, lightweight container runtime built specifically for Kubernetes. It implements the Kubernetes Container Runtime Interface (CRI) gRPC API and uses any Open Container Initiative (OCI) compatible runtime, including runc and crun, as the underlying container executor. CRI-O integrates with the containers/image and containers/storage libraries, the conmon container monitor, and CNI plugins to deliver a minimal kubelet-facing runtime surface, while also exposing an HTTP status API and Prometheus metrics endpoint for operations and observability.
finops:
- name: Cri O Finops
  service_category: Open Source Container Runtime
  slug: cri-o-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cri-o.png
layout: provider
modified: '2026-05-19'
name: CRI-O
nav: Providers
network: true
overview: 'CRI-O publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Containers API, Debug API, Information API, and 2 more. Tagged areas include Apache 2.0, CNCF, Cloud Native, conmon, and Container Runtime.


  The CRI-O catalog on APIs.io includes 2 Spectral governance rulesets.


  CRI-O''s developer surface includes documentation, getting-started guide, engineering blog, changelog, and 8 more developer resources.'
plans:
- name: Cri O Plans Pricing
  plan_count: 1
  slug: cri-o-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 4
  name: Cri O Rate Limits
  slug: cri-o-rate-limits
rules:
- name: CRI-O API Rules
  rule_count: 7
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 1
  slug: cri-o-metrics-rules
- name: CRI-O API Rules
  rule_count: 6
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 1
  slug: cri-o-status-rules
score:
  band: thin
  composite: 39.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 52.2
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cri-o/refs/heads/main/screenshots/cri-o-2026-06-20T175228.png
security:
- kind: domain-security
  name: Cri O Domain Security
  slug: cri-o-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: cri-o
tags:
- Apache 2.0
- CNCF
- Cloud Native
- conmon
- Container Runtime
- Containers
- CRI
- Go
- Graduated
- Kubernetes
- OCI
- Open Source
- Prometheus
- runc
website: https://cri-o.io/
---
