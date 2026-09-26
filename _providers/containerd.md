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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Containerd Agentic Access
  operation_count: 1
  slug: containerd-agentic-access
  summary_line: 1 operation
api_count: 1
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
- baseURL: http://localhost:1338
  baseurl_source: spec
  description: Prometheus-compatible metrics endpoints exposing containerd runtime statistics including gRPC request rates, snapshot usage, and task lifecycle counts.
  name: Containerd Metrics API
  slug: containerd-metrics-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Containerd Metrics API
  slug: open-containerd-metrics-api
- collection_type: open
  name: Containerd Metrics API
  slug: open-containerd-metrics
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/containerd/nri/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/containerd/nri/releases
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/containerd/refs/heads/main/agentic-access/containerd-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/containerd-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/containerd/refs/heads/main/security/containerd-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/containerd/refs/heads/main/json-ld/containerd-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/containerd-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/containerd/refs/heads/main/json-schema/containerd-config-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/containerd-config-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/containerd/refs/heads/main/json-schema/containerd-oci-runtime-spec-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/containerd-oci-runtime-spec-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/containerd/refs/heads/main/rules/containerd-rules.yml
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
overview: 'Containerd publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Metrics API, and 3 more. Tagged areas include Cloud-Native, Container Runtime, CRI, Docker, and gRPC.


  The Containerd catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Containerd''s developer surface includes documentation, getting-started guide, changelog, and 14 more developer resources.'
plans:
- name: Containerd Plans Pricing
  plan_count: 1
  slug: containerd-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Containerd Rate Limits
  slug: containerd-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Containerd API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: containerd-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Containerd API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 2
  slug: containerd-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 51.5
    catalog_earned_first_party: 0.0
    catalog_gap: 48.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 53.8
    developer_ergonomics: 31.0
    discoverability: 55.4
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 25.0
  previous_composite: 31.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/containerd/refs/heads/main/screenshots/containerd-2026-06-20T174921.png
security:
- kind: domain-security
  name: Containerd Domain Security
  slug: containerd-domain-security
  summary_line: TLSv1.3 · HSTS
slug: containerd
tags:
- Cloud-Native
- Container Runtime
- CRI
- Docker
- gRPC
- Kubernetes
- OCI
website: https://containerd.io/
---
