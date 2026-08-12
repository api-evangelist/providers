---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.6
  scored_at: '2026-08-11'
api_count: 4
apis:
- description: 'Traffic Access Control defines the `TrafficTarget` resource, which associates a set of traffic rules with a service identity allocated to a group of pods. It is the authorization layer of SMI: which s'
  name: SMI Traffic Access Control
  slug: smi-traffic-access
- description: 'Traffic Specs describes a set of resources that allow users to specify how their traffic looks. It is used in concert with access control and other policies to concretely define what should happen to '
  name: SMI Traffic Specs
  slug: smi-traffic-specs
- description: Traffic Split defines the `TrafficSplit` resource, which allows users to incrementally direct percentages of traffic between various services. It is the canonical SMI primitive for canary deployments,
  name: SMI Traffic Split
  slug: smi-traffic-split
- description: 'Traffic Metrics is "a resource that provides a common integration point for tools that can benefit by consuming metrics related to HTTP traffic." It is exposed as a Kubernetes APIService extension at '
  name: SMI Traffic Metrics
  slug: smi-traffic-metrics
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/service-mesh-interface-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smi-spec.io
- group: docs
  title: ''
  type: Specification
  url: https://github.com/servicemeshinterface/smi-spec
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/servicemeshinterface
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/servicemeshinterface/smi-spec
- group: commercial
  title: ''
  type: License
  url: https://github.com/servicemeshinterface/smi-spec/blob/main/LICENSE
- group: other
  title: ''
  type: Governance
  url: https://www.cncf.io
- group: other
  title: ''
  type: ArchivalNotice
  url: https://www.cncf.io/blog/2023/10/03/cncf-archives-the-service-mesh-interface-smi-project/
- group: docs
  title: ''
  type: SuccessorSpecification
  url: https://gateway-api.sigs.k8s.io/mesh/gamma/
- group: operate
  title: ''
  type: SlackChannel
  url: https://cloud-native.slack.com
- group: build
  title: ''
  type: SDKs
  url: https://github.com/servicemeshinterface/smi-sdk-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/servicemeshinterface/smi-controller-sdk
- group: docs
  title: ''
  type: ReferenceImplementation
  url: https://github.com/servicemeshinterface/smi-metrics
- group: docs
  title: ''
  type: ReferenceImplementation
  url: https://github.com/servicemeshinterface/smi-adapter-istio
- group: docs
  title: ''
  type: ReferenceImplementation
  url: https://github.com/servicemeshinterface/istio-smi-controller
- group: other
  title: ''
  type: KnownImplementation
  url: https://linkerd.io
- group: other
  title: ''
  type: KnownImplementation
  url: https://openservicemesh.io
- group: other
  title: ''
  type: KnownImplementation
  url: https://www.consul.io/docs/connect
- group: other
  title: ''
  type: KnownImplementation
  url: https://traefik.io/traefik-mesh/
- group: other
  title: ''
  type: KnownImplementation
  url: https://www.solo.io/products/gloo-mesh/
- group: other
  title: ''
  type: KnownImplementation
  url: https://flagger.app
- group: other
  title: ''
  type: KnownImplementation
  url: https://meshery.io
- group: other
  title: ''
  type: KnownImplementation
  url: https://argoproj.github.io/rollouts/
- group: docs
  title: ''
  type: JSONSchema
  url: ./json-schema/
- group: design
  title: ''
  type: JSONLD
  url: ./json-ld/service-mesh-interface-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: ./vocabulary/service-mesh-interface-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: ./examples/
created: '2026-05-22'
description: 'Service Mesh Interface (SMI) was a CNCF Sandbox specification that defined a standard, vendor-neutral set of Kubernetes Custom Resource Definitions (CRDs) for the most common service mesh capabilities: traffic policy, traffic telemetry, and traffic management. SMI''s stated mission was "a standard interface for service meshes on Kubernetes," letting operators write portable traffic policy that worked across Linkerd, Open Service Mesh, Consul Connect, Istio (via adapter), Traefik Mesh, Gloo Mesh, and others without lock-in. The specification reached v0.6.0 (January 2021 / republished January 2024) and defined four resource groups across distinct API versions: Traffic Access Control (v1alpha3), Traffic Specs (v1alpha4), Traffic Split (v1alpha4), and Traffic Metrics (v1alpha1). Active development ceased in July 2022 when the maintainers shifted focus to the Kubernetes SIG-Network GAMMA initiative inside the Gateway API project. CNCF formally archived SMI on October 3, 2023, with
  the GitHub org and all repositories marked read-only on October 20, 2023. The CNCF announcement stated: "the maintainers have decided to consolidate efforts on a service mesh under the auspices of GAMMA under the Kubernetes SIG Network initiative." Gateway API GAMMA reached GA in the Standard Channel with Gateway API v1.1.0 and is now the de facto Kubernetes standard for service mesh configuration, superseding SMI. This profile documents SMI as a historical/archived standard. It is preserved so consumers of the API Evangelist network can (a) recognize legacy SMI manifests still deployed in the wild, (b) understand the conceptual lineage that fed into Gateway API GAMMA, and (c) migrate off SMI to Gateway API.'
examples:
- key_count: 7
  name: Traffic Metrics Example
  slug: traffic-metrics-example
image: https://avatars.githubusercontent.com/u/59054423
json_schemas:
- name: SMI HTTPRouteGroup
  property_count: 4
  slug: http-route-group
- name: SMI TCPRoute
  property_count: 4
  slug: tcp-route
- name: SMI TrafficMetrics
  property_count: 7
  slug: traffic-metrics
- name: SMI TrafficSplit
  property_count: 4
  slug: traffic-split
- name: SMI TrafficTarget
  property_count: 4
  slug: traffic-target
- name: SMI UDPRoute
  property_count: 4
  slug: udp-route
json_structures:
- name: Service Mesh Interface Structure
  property_count: 0
  slug: service-mesh-interface-structure
jsonld:
- class_count: 9
  name: Service Mesh Interface Context
  property_count: 3
  slug: service-mesh-interface-context
layout: provider
modified: '2026-05-23'
name: Service Mesh Interface (SMI)
nav: Providers
network: true
overview: 'Service Mesh Interface (SMI) publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Service Mesh, Kubernetes, Traffic Policy, Traffic Management, and Traffic Metrics.


  The Service Mesh Interface (SMI) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Service Mesh Interface (SMI)''s developer surface includes code examples and 26 more developer resources.'
random_paper: 13
rules:
- name: Service Mesh Interface (SMI) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: service-mesh-interface-jsonschema-spectral-rules
score:
  band: emerging
  composite: 22.9
  delta: -1.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 29.0
    developer_ergonomics: 6.5
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 24.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/service-mesh-interface/refs/heads/main/screenshots/service-mesh-interface-2026-06-20T193726.png
security:
- kind: domain-security
  name: Service Mesh Interface Domain Security
  slug: service-mesh-interface-domain-security
  summary_line: TLSv1.3 · HSTS
slug: service-mesh-interface
tags:
- Service Mesh
- Kubernetes
- Traffic Policy
- Traffic Management
- Traffic Metrics
- Standards
- CNCF
- Archived
- Specification
- Custom Resource Definitions
website: https://smi-spec.io
---
