---
aid: service-mesh
name: Service Mesh
description: Service mesh is a dedicated infrastructure layer for handling service-to-service communication in microservices architectures. It provides traffic management, mutual TLS security, observability, policy enforcement, and resilience features without requiring changes to application code. Key implementations include Istio, Linkerd, Consul Connect, and AWS App Mesh. This index tracks service mesh specifications, implementations, and related APIs across the ecosystem.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Service Mesh
  - Microservices
  - Cloud Native
  - Kubernetes
  - Networking
  - Observability
  - Zero Trust
url: https://raw.githubusercontent.com/api-evangelist/service-mesh/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: service-mesh:istio-api
    name: Istio API
    description: Istio is the most widely deployed service mesh. Istio's control plane exposes APIs for traffic management (VirtualService, DestinationRule, Gateway), security (PeerAuthentication, AuthorizationPolicy), and telemetry configuration. The Istio API uses Kubernetes Custom Resource Definitions (CRDs) as its primary interface.
    humanURL: https://istio.io/latest/docs/reference/config/
    tags:
      - Service Mesh
      - Istio
      - Traffic Management
      - Kubernetes
      - mTLS
    properties:
      - type: Documentation
        url: https://istio.io/latest/docs/reference/config/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/istio/api/master/networking/v1alpha3/virtual_service.proto
  - aid: service-mesh:linkerd-api
    name: Linkerd Admin API
    description: Linkerd is a lightweight CNCF-graduated service mesh focused on simplicity and security. Linkerd exposes an admin API for metrics, health checks, and edge proxy management. It uses the SMI (Service Mesh Interface) API specification for traffic policy.
    humanURL: https://linkerd.io/2.14/reference/
    tags:
      - Service Mesh
      - Linkerd
      - CNCF
      - Observability
      - mTLS
    properties:
      - type: Documentation
        url: https://linkerd.io/2.14/reference/
      - type: GitHubOrganization
        url: https://github.com/linkerd
  - aid: service-mesh:consul-api
    name: Consul Connect / Service Mesh API
    description: HashiCorp Consul provides service discovery and a service mesh (Consul Connect) with mutual TLS, intentions-based access control, and multi-datacenter support. Consul exposes a REST API for service catalog, health checks, key-value store, and mesh configuration.
    humanURL: https://developer.hashicorp.com/consul/api-docs
    tags:
      - Service Mesh
      - Consul
      - HashiCorp
      - Service Discovery
      - Zero Trust
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/consul/api-docs
      - type: OpenAPI
        url: https://github.com/hashicorp/consul/blob/main/api/openapi-spec/swagger.json
  - aid: service-mesh:aws-app-mesh-api
    name: AWS App Mesh API
    description: AWS App Mesh is a managed service mesh that provides application-level networking for microservices on AWS. It integrates with ECS, EKS, EC2, and Fargate. The App Mesh API manages virtual services, virtual routers, virtual nodes, and routes.
    humanURL: https://docs.aws.amazon.com/app-mesh/latest/APIReference/
    tags:
      - Service Mesh
      - AWS
      - Cloud
      - EKS
      - ECS
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/
  - aid: service-mesh:service-mesh-interface
    name: Service Mesh Interface (SMI)
    description: SMI is a standard interface for service meshes on Kubernetes. It defines common APIs for traffic policy, traffic telemetry, and traffic management so that applications work with any SMI-compatible service mesh. SMI is hosted by the CNCF.
    humanURL: https://smi-spec.io/
    tags:
      - Service Mesh
      - SMI
      - Standard
      - Kubernetes
      - CNCF
    properties:
      - type: Documentation
        url: https://smi-spec.io/
      - type: GitHubOrganization
        url: https://github.com/servicemeshinterface
common:
  - type: Website
    url: https://github.com/api-evangelist/service-mesh
  - type: Documentation
    url: https://istio.io/latest/docs/
  - type: Guide
    url: https://linkerd.io/2.14/getting-started/
  - type: Standard
    url: https://smi-spec.io/
  - type: CNCF
    url: https://landscape.cncf.io/guide#orchestration-management--service-mesh
  - type: JSONSchema
    url: json-schema/service-mesh-configuration-schema.json
  - type: JSONStructure
    url: json-structure/service-mesh-traffic-policy-structure.json
  - type: JSONLDContext
    url: json-ld/service-mesh-context.jsonld
  - type: Vocabulary
    url: vocabulary/service-mesh-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
