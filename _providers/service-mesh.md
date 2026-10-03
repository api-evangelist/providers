---
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-03'
api_count: 5
apis:
- description: Istio is the most widely deployed service mesh. Istio's control plane exposes APIs for traffic management (VirtualService, DestinationRule, Gateway), security (PeerAuthentication, AuthorizationPolicy)
  name: Istio API
  slug: istio-api
- description: Linkerd is a lightweight CNCF-graduated service mesh focused on simplicity and security. Linkerd exposes an admin API for metrics, health checks, and edge proxy management. It uses the SMI (Service Me
  name: Linkerd Admin API
  slug: linkerd-api
- description: HashiCorp Consul provides service discovery and a service mesh (Consul Connect) with mutual TLS, intentions-based access control, and multi-datacenter support. Consul exposes a REST API for service ca
  name: Consul Connect / Service Mesh API
  slug: consul-api
- description: AWS App Mesh is a managed service mesh that provides application-level networking for microservices on AWS. It integrates with ECS, EKS, EC2, and Fargate. The App Mesh API manages virtual services, vi
  name: AWS App Mesh API
  slug: aws-app-mesh-api
- description: SMI is a standard interface for service meshes on Kubernetes. It defines common APIs for traffic policy, traffic telemetry, and traffic management so that applications work with any SMI-compatible ser
  name: Service Mesh Interface (SMI)
  slug: service-mesh-interface
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://github.com/api-evangelist/service-mesh
- group: docs
  title: ''
  type: Documentation
  url: https://istio.io/latest/docs/
- group: docs
  title: ''
  type: Guide
  url: https://linkerd.io/2.14/getting-started/
- group: other
  title: ''
  type: Standard
  url: https://smi-spec.io/
- group: other
  title: ''
  type: CNCF
  url: https://landscape.cncf.io/guide#orchestration-management--service-mesh
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/service-mesh/refs/heads/main/json-schema/service-mesh-configuration-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/service-mesh-configuration-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/service-mesh/refs/heads/main/json-structure/service-mesh-traffic-policy-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/service-mesh-traffic-policy-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/service-mesh/refs/heads/main/json-ld/service-mesh-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/service-mesh-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/service-mesh/refs/heads/main/vocabulary/service-mesh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/service-mesh-vocabulary.yml
created: '2026-03-27'
description: Service mesh is a dedicated infrastructure layer for handling service-to-service communication in microservices architectures. It provides traffic management, mutual TLS security, observability, policy enforcement, and resilience features without requiring changes to application code. Key implementations include Istio, Linkerd, Consul Connect, and AWS App Mesh. This index tracks service mesh specifications, implementations, and related APIs across the ecosystem.
examples:
- key_count: 4
  name: Service Mesh Mtls Example
  slug: service-mesh-mtls-example
- key_count: 4
  name: Service Mesh Traffic Split Example
  slug: service-mesh-traffic-split-example
finops:
- name: Service Mesh Finops
  service_category: API
  slug: service-mesh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: Service Mesh Configuration
  property_count: 4
  slug: service-mesh-configuration
json_structures:
- name: Service Mesh Traffic Policy Structure
  property_count: 0
  slug: service-mesh-traffic-policy-structure
jsonld:
- class_count: 38
  name: Service Mesh Context
  property_count: 2
  slug: service-mesh-context
layout: provider
modified: '2026-05-02'
name: Service Mesh
nav: Providers
network: true
overview: 'Service Mesh publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Istio API, Consul Connect / Service Mesh API, and 3 more. Tagged areas include Service Mesh, Microservices, Cloud-Native, Kubernetes, and Networking.


  The Service Mesh catalog on APIs.io includes 1 JSON-LD context.


  Service Mesh''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Service Mesh Plans Pricing
  plan_count: 3
  slug: service-mesh-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Service Mesh Rate Limits
  slug: service-mesh-rate-limits
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 72.1
    catalog_earned_first_party: 0.0
    catalog_gap: 42.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.3
    contract_governance: 13.6
    contract_quality: 34.7
    developer_ergonomics: 9.5
    discoverability: 62.5
    operational_transparency: 33.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: service-mesh
tags:
- Service Mesh
- Microservices
- Cloud-Native
- Kubernetes
- Networking
- Observability
- Zero Trust
---
