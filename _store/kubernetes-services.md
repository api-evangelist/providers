---
aid: kubernetes-services
url: https://raw.githubusercontent.com/api-evangelist/kubernetes-services/refs/heads/main/apis.yml
apis:
- aid: kubernetes-services:kubernetes-services
  name: Kubernetes Services
  description: The Kubernetes Services API provides an abstraction for exposing groups of Pods over a network with a stable virtual IP address and DNS name. It supports ClusterIP, NodePort, LoadBalancer, and ExternalName service types for internal and external connectivity within Kubernetes clusters.
  humanURL: https://kubernetes.io/docs/concepts/services-networking/service/
  tags:
  - Kubernetes
  - Load Balancing
  - Networking
  - Service Discovery
  properties:
  - type: Documentation
    url: https://kubernetes.io/docs/concepts/services-networking/service/
  - type: Reference
    url: https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/
  - type: OpenAPI
    url: openapi/kubernetes-services-openapi.yml
  - type: AsyncAPI
    url: asyncapi/kubernetes-services-watch-asyncapi.yml
  - type: JSONSchema
    url: json-schema/kubernetes-services-schema.json
- aid: kubernetes-services:kubernetes-ingress
  name: Kubernetes Ingress
  description: The Kubernetes Ingress API manages external HTTP and HTTPS access to services within a cluster, providing load balancing, SSL termination, and name-based virtual hosting. Traffic routing is controlled by rules defined on the Ingress resource and fulfilled by an Ingress controller.
  humanURL: https://kubernetes.io/docs/concepts/services-networking/ingress/
  tags:
  - HTTP
  - Kubernetes
  - Load Balancing
  - Networking
  properties:
  - type: Documentation
    url: https://kubernetes.io/docs/concepts/services-networking/ingress/
  - type: Reference
    url: https://kubernetes.io/docs/reference/kubernetes-api/service-resources/ingress-v1/
  - type: OpenAPI
    url: openapi/kubernetes-ingress-openapi.yml
- aid: kubernetes-services:kubernetes-gateway-api
  name: Kubernetes Gateway API
  description: The Kubernetes Gateway API is a role-oriented, extensible API for managing ingress and mesh traffic routing in Kubernetes. It supports advanced traffic management including header-based matching, traffic weighting, and multi-protocol routing as a successor to the Ingress API.
  humanURL: https://kubernetes.io/docs/concepts/services-networking/gateway/
  tags:
  - Gateway
  - Kubernetes
  - Networking
  - Traffic Management
  properties:
  - type: Documentation
    url: https://kubernetes.io/docs/concepts/services-networking/gateway/
  - type: OpenAPI
    url: openapi/kubernetes-gateway-api-openapi.yml
- aid: kubernetes-services:kubernetes-endpoint-slices
  name: Kubernetes EndpointSlices
  description: The Kubernetes EndpointSlices API tracks IP addresses, ports, readiness, and topology information for Pods backing a Service. EndpointSlices replaced the older Endpoints API to improve scalability for large clusters and enable topology-aware routing.
  humanURL: https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/
  tags:
  - Kubernetes
  - Networking
  - Service Discovery
  - Topology
  properties:
  - type: Documentation
    url: https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/
  - type: Reference
    url: https://kubernetes.io/docs/reference/kubernetes-api/service-resources/endpoint-slice-v1/
  - type: OpenAPI
    url: openapi/kubernetes-endpoint-slices-openapi.yml
- aid: kubernetes-services:kubernetes-network-policies
  name: Kubernetes Network Policies
  description: The Kubernetes NetworkPolicy API controls how groups of Pods communicate with each other and with external network endpoints. Policies define ingress and egress rules based on Pod selectors, namespace selectors, and IP blocks to implement network segmentation.
  humanURL: https://kubernetes.io/docs/concepts/services-networking/network-policies/
  tags:
  - Kubernetes
  - Networking
  - Policy
  - Security
  properties:
  - type: Documentation
    url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
  - type: Reference
    url: https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/network-policy-v1/
  - type: OpenAPI
    url: openapi/kubernetes-network-policies-openapi.yml
- aid: kubernetes-services:kubernetes-dns
  name: Kubernetes DNS for Services and Pods
  description: Kubernetes provides DNS-based service discovery for Services and Pods within a cluster. DNS records are automatically created for Services, allowing workloads to locate services by name rather than by IP address.
  humanURL: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/
  tags:
  - DNS
  - Kubernetes
  - Networking
  - Service Discovery
  properties:
  - type: Documentation
    url: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/
name: Kubernetes Services
tags:
- Container Orchestration
- Kubernetes
- Load Balancing
- Networking
- Service Discovery
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Kubernetes Services provide an abstract way to expose an application running on a set of Pods as a network service. They provide stable networking endpoints and load balancing across pod replicas in a Kubernetes cluster.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

