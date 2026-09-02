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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Ambient Mesh provides a sidecar-less service mesh via the Kubernetes Gateway API and Istio ambient mode. It exposes configuration APIs for traffic management, security policies, resilience settings, a
  name: Ambient Mesh
  slug: ambient-mesh
artifact_total: 23
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/istio/istio/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/istio/istio/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/istio/istio/blob/master/.github/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/istio/istio/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/istio/istio/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ambient-mesh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ambientmesh.io/
- group: docs
  title: ''
  type: Documentation
  url: https://ambientmesh.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://ambientmesh.io/docs/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://ambientmesh.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/istio
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/istio/istio
created: '2026-04-19'
description: Ambient Mesh is a sidecar-less service mesh architecture built on Istio that simplifies microservices communication, enhances zero-trust security, and improves observability without requiring sidecar proxy injection. It uses a shared per-node proxy (ztunnel) for zero-trust security and optional waypoint proxies for advanced Layer 7 policies, enabling seamless migration from sidecar-based meshes with zero downtime.
features:
- description: Operates at the platform layer without sidecar proxy injection, reducing resource overhead and operational complexity while maintaining full service mesh capabilities.
  name: Sidecar-Less Architecture
- description: SPIFFE-based workload identity with automatic mutual TLS encryption between workloads, certificate management, and zero-trust network policies enforced by ztunnel.
  name: Zero-Trust Security
- description: Advanced traffic routing, load balancing, traffic splitting, mirroring, blue-green deployments, and gateway management via Kubernetes Gateway API HTTPRoute resources.
  name: Traffic Management
- description: Zone-aware load balancing, circuit breaking, outlier detection, fault injection, timeouts, and retry budgets for high-availability workloads.
  name: Resilience
- description: Distributed tracing, performance metrics via Prometheus, Kiali observability console, and HTTP observability for traffic visualization and security verification.
  name: Observability
- description: Free migration tooling for upgrading from sidecar-based architectures with automated workload analysis and risk mitigation for waypoint proxy requirements.
  name: Zero-Downtime Migration
- description: Optional per-namespace or per-workload Layer 7 proxies that provide advanced policy enforcement without requiring per-pod sidecar containers.
  name: Waypoint Proxies
finops:
- name: Ambient Mesh Finops
  service_category: API
  slug: ambient-mesh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ambient-mesh.png
integrations:
- description: Ambient Mesh is built on Istio ambient mode, using its control plane and CRDs for configuration.
  name: Istio
- description: Uses the standard Kubernetes Gateway API with HTTPRoute, Gateway, and GRPCRoute resources for traffic management.
  name: Kubernetes Gateway API
- description: Integrates with Prometheus for metrics collection and monitoring of mesh traffic and performance.
  name: Prometheus
- description: Integrates with Kiali for service mesh observability, traffic visualization, and security verification.
  name: Kiali
- description: Solo.io's Gloo Mesh provides enterprise-grade ambient mesh management for scaling across enterprise workloads.
  name: Gloo Mesh
- description: Red Hat OpenShift Service Mesh 3.x supports Istio ambient mode for OpenShift deployments.
  name: OpenShift
layout: provider
modified: '2026-04-19'
name: Ambient Mesh
nav: Providers
network: true
overview: 'Ambient Mesh publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Service Mesh, Istio, Kubernetes, Zero Trust, and Observability.


  Ambient Mesh''s developer surface includes documentation, getting-started guide, engineering blog, and 9 more developer resources.'
plans:
- name: Ambient Mesh Plans Pricing
  plan_count: 3
  slug: ambient-mesh-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Ambient Mesh Rate Limits
  slug: ambient-mesh-rate-limits
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 85.0
  previous_composite: 27.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ambient-mesh/refs/heads/main/screenshots/ambient-mesh-2026-06-20T171854.png
security:
- kind: domain-security
  name: Ambient Mesh Domain Security
  slug: ambient-mesh-domain-security
  summary_line: TLSv1.3
slug: ambient-mesh
tags:
- Service Mesh
- Istio
- Kubernetes
- Zero Trust
- Observability
- Traffic Management
- Microservices
use_cases:
- description: Enforce mutual TLS and zero-trust policies across microservices without modifying application code or injecting sidecar proxies.
  name: Microservices Security
- description: Implement advanced traffic routing, A/B testing, canary deployments, and traffic mirroring across Kubernetes workloads.
  name: Traffic Management
- description: Migrate existing Istio sidecar-based deployments to ambient mode with zero downtime using the free migration tooling.
  name: Istio Migration
- description: Gain full visibility into service-to-service communication with metrics, tracing, and traffic visualization via Kiali and Prometheus.
  name: Kubernetes Observability
- description: Extend ambient mesh policies and security across multiple Kubernetes clusters for hybrid and multi-cloud architectures.
  name: Multi-Cluster Networking
website: https://ambientmesh.io/
---
