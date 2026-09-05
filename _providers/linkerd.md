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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Linkerd Agentic Access
  operation_count: 12
  slug: linkerd-agentic-access
  summary_line: 12 operations · 7 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: The Linkerd Proxy Control Plane gRPC API defines the protobuf service contracts used by the data-plane proxy to communicate with the control plane. It includes the Destination API for service discover
  name: Linkerd Proxy Control Plane API
  slug: proxy-control-plane-api
- description: 'The Linkerd Multicluster extension provides Kubernetes CRDs and a gateway component that enables transparent, secure cross-cluster service communication. It uses mTLS to authenticate workloads across '
  name: Linkerd Multicluster API
  slug: multicluster-api
- baseURL: http://localhost:4191
  baseurl_source: declared
  description: API resource discovery
  name: Linkerd Discovery API
  slug: linkerd-discovery-api
- baseURL: http://localhost:4191
  baseurl_source: declared
  description: Connection topology between resources
  name: Linkerd Edges API
  slug: linkerd-edges-api
- baseURL: http://localhost:4191
  baseurl_source: declared
  description: Multicluster gateway metrics
  name: Linkerd Gateways API
  slug: linkerd-gateways-api
- baseURL: http://localhost:4191
  baseurl_source: declared
  description: Health and readiness check endpoints
  name: Linkerd Health API
  slug: linkerd-health-api
- baseURL: http://localhost:4191
  baseurl_source: declared
  description: Proxy lifecycle management endpoints
  name: Linkerd Lifecycle API
  slug: linkerd-lifecycle-api
- baseURL: http://localhost:4191
  baseurl_source: declared
  description: Prometheus metrics endpoints
  name: Linkerd Metrics API
  slug: linkerd-metrics-api
- baseURL: http://localhost:4191
  baseurl_source: declared
  description: Per-route metrics
  name: Linkerd Routes API
  slug: linkerd-routes-api
- baseURL: http://localhost:4191
  baseurl_source: declared
  description: Resource statistics and golden metrics
  name: Linkerd Statistics API
  slug: linkerd-statistics-api
- baseURL: http://localhost:4191
  baseurl_source: declared
  description: Real-time traffic inspection
  name: Linkerd Tap API
  slug: linkerd-tap-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Linkerd Proxy Admin Discovery API
  slug: open-linkerd-discovery-api
- collection_type: open
  name: Linkerd Proxy Admin Discovery Edges API
  slug: open-linkerd-edges-api
- collection_type: open
  name: Linkerd Proxy Admin Discovery Gateways API
  slug: open-linkerd-gateways-api
- collection_type: open
  name: Linkerd Proxy Admin Discovery Health API
  slug: open-linkerd-health-api
- collection_type: open
  name: Linkerd Proxy Admin Discovery Lifecycle API
  slug: open-linkerd-lifecycle-api
- collection_type: open
  name: Linkerd Proxy Admin Discovery Metrics API
  slug: open-linkerd-metrics-api
- collection_type: open
  name: Linkerd Proxy Admin API
  slug: open-linkerd-proxy-admin
- collection_type: open
  name: Linkerd Proxy Admin Discovery Routes API
  slug: open-linkerd-routes-api
- collection_type: open
  name: Linkerd Proxy Admin Discovery Statistics API
  slug: open-linkerd-statistics-api
- collection_type: open
  name: Linkerd Proxy Admin Discovery Tap API
  slug: open-linkerd-tap-api
- collection_type: open
  name: Linkerd Tap API
  slug: open-linkerd-tap
- collection_type: open
  name: Linkerd Viz Metrics API
  slug: open-linkerd-viz-metrics
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/linkerd-capability-edges.yml
- group: operate
  title: ''
  type: Releases
  url: https://github.com/linkerd/linkerd2-proxy-api/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/linkerd/linkerd2-proxy-api/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/linkerd/linkerd2-proxy-api/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/linkerd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linkerd-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/linkerd
- group: design
  title: ''
  type: JSONLD
  url: json-ld/linkerd-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/service-profile.json
- group: company
  title: ''
  type: Website
  url: https://linkerd.io/
- group: docs
  title: ''
  type: Documentation
  url: https://linkerd.io/2.19/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://linkerd.io/2.19/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linkerd
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/linkerd/linkerd2
- group: company
  title: ''
  type: Blog
  url: https://linkerd.io/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/linkerd/linkerd2/blob/main/CHANGES.md
- group: operate
  title: ''
  type: Community
  url: https://linkerd.io/community/get-involved/
- group: operate
  title: ''
  type: Slack
  url: https://slack.linkerd.io/
- group: operate
  title: ''
  type: Support
  url: https://linkerd.buoyant.io/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/linkerd/linkerd2/releases
- group: auth
  title: ''
  type: Security
  url: https://github.com/linkerd/linkerd2/blob/main/SECURITY.md
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/linkerd
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Linkerd
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buoyant.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buoyant.io/terms-of-service
created: '2025-08-19'
description: Service mesh without the mess. Linkerd adds security, observability, and reliability to any Kubernetes cluster without the complexity of bloat of other meshes.
finops:
- name: Linkerd Finops
  service_category: Service Mesh / Kubernetes Infrastructure
  slug: linkerd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linkerd.png
json_schemas:
- name: Linkerd Edge
  property_count: 5
  slug: edge
- name: Linkerd Gateway
  property_count: 8
  slug: gateway
- name: Linkerd ServiceProfile
  property_count: 4
  slug: service-profile
- name: Linkerd Stat Summary
  property_count: 2
  slug: stat-summary
- name: Linkerd Tap Event
  property_count: 9
  slug: tap-event
jsonld:
- class_count: 0
  name: Linkerd Context
  property_count: 6
  slug: linkerd-context
layout: provider
modified: '2026-05-19'
name: Linkerd
nav: Providers
network: true
overview: 'Linkerd publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Edges API, Gateways API, and 6 more. Tagged areas include Kubernetes, mTLS, Observability, Security, and Service Mesh.


  The Linkerd catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Linkerd''s developer surface includes documentation, getting-started guide, engineering blog, changelog, support, release notes, Stack Overflow tag, and 18 more developer resources.'
plans:
- name: Linkerd Plans Pricing
  plan_count: 5
  slug: linkerd-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Linkerd Rate Limits
  slug: linkerd-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Linkerd API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: linkerd-jsonschema-spectral-rules
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 57.3
    catalog_earned_first_party: 0.0
    catalog_gap: 57.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 56.6
    developer_ergonomics: 35.7
    discoverability: 55.6
    governance: 9.8
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 50.0
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linkerd/refs/heads/main/screenshots/linkerd-2026-06-20T184545.png
security:
- kind: domain-security
  name: Linkerd Domain Security
  slug: linkerd-domain-security
  summary_line: TLSv1.3
slug: linkerd
tags:
- Kubernetes
- mTLS
- Observability
- Security
- Service Mesh
website: https://linkerd.io/
---
