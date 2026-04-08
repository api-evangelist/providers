---
aid: contour
url: https://raw.githubusercontent.com/api-evangelist/contour/refs/heads/main/apis.yml
apis:
- aid: contour:contour-httpproxy-api
  name: Contour HTTPProxy API
  description: Kubernetes Custom Resource Definition that extends the standard Ingress API with advanced routing, multi-team support, TLS delegation, and weighted load balancing across multiple backend services. HTTPProxy is Contour's primary ingress configuration resource and supports inclusion of routing configuration across namespaces.
  humanURL: https://projectcontour.io/docs/main/config/api/
  baseURL: https://projectcontour.io
  tags:
  - Custom Resource
  - HTTPProxy
  - Ingress
  - Kubernetes
  - Routing
  properties:
  - type: Documentation
    url: https://projectcontour.io/docs/main/config/api/
  - type: Reference
    url: https://projectcontour.io/docs/main/config/api-reference.html
  - type: OpenAPI
    url: openapi/contour-httpproxy-openapi.yml
  - type: JSONSchema
    url: json-schema/contour-httpproxy-schema.json
- aid: contour:contour-gateway-api
  name: Contour Gateway API
  description: Contour's implementation of the Kubernetes Gateway API, supporting HTTPRoute and TLSRoute resources for defining ingress traffic routing rules. Gateway API is the next-generation Kubernetes ingress standard and Contour provides support for GatewayClass, Gateway, HTTPRoute, and related resources.
  humanURL: https://projectcontour.io/docs/1.30/config/gateway-api/
  baseURL: https://projectcontour.io
  tags:
  - Gateway API
  - Ingress
  - Kubernetes
  - Networking
  - Routing
  properties:
  - type: Documentation
    url: https://projectcontour.io/docs/1.30/config/gateway-api/
  - type: Reference
    url: https://projectcontour.io/docs/main/config/api-reference.html
  - type: OpenAPI
    url: openapi/contour-gateway-openapi.yml
- aid: contour:contour-kubernetes-ingress-api
  name: Contour Kubernetes Ingress API
  description: Contour's support for the standard Kubernetes Ingress v1 resource, enabling basic ingress use cases such as host-based and path-based routing to backend services. Contour watches Ingress v1 resources and translates them into Envoy proxy configuration, with support for IngressClass selection and Contour-specific annotations for extended configuration.
  humanURL: https://projectcontour.io/docs/main/config/ingress/
  baseURL: https://projectcontour.io
  tags:
  - Ingress
  - Kubernetes
  - Networking
  - Routing
  - Standard API
  properties:
  - type: Documentation
    url: https://projectcontour.io/docs/main/config/ingress/
  - type: Reference
    url: https://projectcontour.io/docs/main/config/annotations/
- aid: contour:contour-extensionservice-api
  name: Contour ExtensionService API
  description: Kubernetes Custom Resource Definition for binding gRPC-based extension services to the Contour API. ExtensionService resources allow external components to implement Contour API features such as external authorization and rate limiting by registering a network service that Contour will route to via Envoy's gRPC extension protocol (v3).
  humanURL: https://projectcontour.io/docs/main/config/api/
  baseURL: https://projectcontour.io
  tags:
  - Authorization
  - Custom Resource
  - Extension Service
  - gRPC
  - Kubernetes
  properties:
  - type: Documentation
    url: https://projectcontour.io/docs/main/config/api/
  - type: Reference
    url: https://projectcontour.io/docs/main/config/api-reference.html
- aid: contour:contour-configuration-api
  name: Contour Configuration API
  description: Contour's ContourConfiguration Custom Resource Definition (v1alpha1) that provides cluster-scoped configuration of a Contour instance, including ingress settings, TLS defaults, timeouts, and feature gates. This API allows operators to declaratively manage Contour's runtime behavior through Kubernetes resources instead of command-line flags or static config files.
  humanURL: https://projectcontour.io/docs/main/config/api/
  baseURL: https://projectcontour.io
  tags:
  - Configuration
  - Custom Resource
  - Kubernetes
  - Networking
  - Operator
  properties:
  - type: Documentation
    url: https://projectcontour.io/docs/main/config/api/
  - type: Reference
    url: https://projectcontour.io/docs/main/config/api-reference.html
name: Contour
tags:
- Envoy
- Ingress Controller
- Kubernetes
- Networking
- Proxy
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A Kubernetes ingress controller using Envoy proxy that provides dynamic configuration updates and advanced routing capabilities for managing external access to services in a cluster.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

