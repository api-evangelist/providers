---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Containerd Agentic Access
  operation_count: 1
  slug: containerd-agentic-access
  summary_line: 1 operation
api_count: 4
apis:
- description: Core gRPC API for managing the full container lifecycle including containers, images, content, snapshots, namespaces, tasks, leases, events, and plugins. Provides low-level access to all containerd fu
  name: Containerd gRPC API
  slug: containerd-grpc-api
- description: Container Runtime Interface (CRI) implementation that enables Kubernetes to use containerd as its container runtime. Supports pod sandbox management, container lifecycle operations, image pulling, and
  name: Containerd CRI API
  slug: containerd-cri-api
- description: The Node Resource Interface (NRI) is a framework for plugging extensions into OCI-compatible container runtimes. NRI plugins receive lifecycle event notifications and can make controlled modifications
  name: Containerd NRI API
  slug: containerd-nri-api
- description: Prometheus-compatible metrics endpoints exposing containerd runtime statistics including gRPC request rates, snapshot usage, and task lifecycle counts.
  name: Containerd Metrics API
  slug: containerd-metrics-api
artifact_total: 15
collections:
- collection_type: open
  name: Containerd Metrics API
  slug: open-containerd-metrics
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/containerd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/containerd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://containerd.io/
- group: docs
  title: ''
  type: Documentation
  url: https://containerd.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://containerd.io/docs/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/containerd
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/containerd/containerd
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/containerd/containerd/releases
- group: operate
  title: ''
  type: Community
  url: https://cloud-native.slack.com/
- group: other
  title: ''
  type: CNCF Project
  url: https://www.cncf.io/projects/containerd/
- group: commercial
  title: ''
  type: License
  url: https://github.com/containerd/containerd/blob/main/LICENSE
- group: design
  title: ''
  type: JSONLD
  url: json-ld/containerd-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/containerd-config-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/containerd-oci-runtime-spec-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/containerd-rules.yml
created: '2025-01-01'
description: An industry-standard container runtime with an emphasis on simplicity, robustness and portability.
finops:
- name: Containerd Finops
  service_category: Container Runtime / Open Source
  slug: containerd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/containerd.png
json_schemas:
- name: Containerd Configuration
  property_count: 16
  slug: containerd-config
- name: OCI Runtime Specification
  property_count: 9
  slug: containerd-oci-runtime-spec
jsonld:
- class_count: 0
  name: Containerd Context
  property_count: 12
  slug: containerd-context
layout: provider
modified: '2026-05-19'
name: Containerd
nav: Providers
network: true
overview: 'Containerd publishes 1 API on the [APIs.io](https://apis.io/) network: Metrics API. Tagged areas include Cloud Native, Container Runtime, CRI, Docker, and gRPC.


  The Containerd catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Containerd''s developer surface includes documentation, getting-started guide, changelog, and 12 more developer resources.'
plans:
- name: Containerd Plans Pricing
  plan_count: 1
  slug: containerd-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 3
  name: Containerd Rate Limits
  slug: containerd-rate-limits
rules:
- name: Containerd API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: containerd-jsonschema-spectral-rules
- name: Containerd API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 2
  slug: containerd-rules
score:
  band: developing
  composite: 50.6
  delta: 4.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 67.3
    developer_ergonomics: 23.9
    discoverability: 75.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 46.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/containerd/refs/heads/main/screenshots/containerd-2026-06-20T174921.png
security:
- kind: domain-security
  name: Containerd Domain Security
  slug: containerd-domain-security
  summary_line: TLSv1.3 · HSTS
slug: containerd
tags:
- Cloud Native
- Container Runtime
- CRI
- Docker
- gRPC
- Kubernetes
- OCI
website: https://containerd.io/
---
