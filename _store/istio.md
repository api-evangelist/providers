---
aid: istio
url: https://raw.githubusercontent.com/api-evangelist/istio/refs/heads/main/apis.yml
apis:
  - aid: istio:networking-api
    name: Istio Networking API
    tags:
      - Networking
      - Service Mesh
      - Traffic Management
    humanURL: https://istio.io/latest/docs/reference/config/networking/
    properties:
      - url: https://istio.io/latest/docs/reference/config/networking/
        type: Documentation
      - url: openapi/istio-networking-api-openapi.yml
        type: OpenAPI
      - url: json-schema/virtual-service.json
        type: JSONSchema
      - url: json-schema/destination-rule.json
        type: JSONSchema
      - url: json-schema/gateway.json
        type: JSONSchema
      - url: json-schema/service-entry.json
        type: JSONSchema
      - url: json-schema/sidecar.json
        type: JSONSchema
      - url: json-schema/workload-entry.json
        type: JSONSchema
      - url: json-ld/istio-context.jsonld
        type: JSONLD
    description: The Istio Networking API (networking.istio.io) provides configuration resources for traffic management within an Istio service mesh.
  - aid: istio:security-api
    name: Istio Security API
    tags:
      - Authentication
      - Authorization
      - Security
      - Service Mesh
    humanURL: https://istio.io/latest/docs/reference/config/security/
    properties:
      - url: https://istio.io/latest/docs/reference/config/security/
        type: Documentation
      - url: openapi/istio-security-api-openapi.yml
        type: OpenAPI
      - url: json-schema/authorization-policy.json
        type: JSONSchema
      - url: json-schema/peer-authentication.json
        type: JSONSchema
      - url: json-schema/request-authentication.json
        type: JSONSchema
      - url: json-ld/istio-context.jsonld
        type: JSONLD
    description: The Istio Security API (security.istio.io) provides configuration resources for managing security policies within an Istio service mesh. It includes AuthorizationPolicy for fine-grained access control on workloads with ALLOW, DENY, AUDIT, and CUSTOM actions, PeerAuthentication for configuring mutual TLS (mTLS) between service proxies, and RequestAuthentication for validating JWT tokens attached to incoming requests. These resources enforce zero-trust security across the mesh.
  - aid: istio:telemetry-api
    name: Istio Telemetry API
    tags:
      - Metrics
      - Observability
      - Service Mesh
      - Telemetry
      - Tracing
    humanURL: https://istio.io/latest/docs/reference/config/telemetry/
    properties:
      - url: https://istio.io/latest/docs/reference/config/telemetry/
        type: Documentation
      - url: openapi/istio-telemetry-api-openapi.yml
        type: OpenAPI
      - url: json-schema/telemetry.json
        type: JSONSchema
      - url: json-ld/istio-context.jsonld
        type: JSONLD
    description: The Istio Telemetry API (telemetry.istio.io) provides configuration resources for managing observability within an Istio service mesh. The Telemetry resource enables flexible configuration of metrics, access logs, and distributed tracing for workloads. It uses the concept of providers to indicate the protocol or integration type, and supports fine-grained control over what telemetry data is collected and where it is sent.
  - aid: istio:extensions-api
    name: Istio Extensions API
    tags:
      - Extensions
      - Service Mesh
      - Wasm
      - WebAssembly
    humanURL: https://istio.io/latest/docs/reference/config/
    properties:
      - url: https://istio.io/latest/docs/reference/config/
        type: Documentation
      - url: openapi/istio-extensions-api-openapi.yml
        type: OpenAPI
      - url: json-schema/wasm-plugin.json
        type: JSONSchema
      - url: json-ld/istio-context.jsonld
        type: JSONLD
    description: The Istio Extensions API (extensions.istio.io) provides configuration resources for extending the Istio service mesh with custom functionality. The WasmPlugin resource enables deploying WebAssembly (Wasm) modules as plugins to the Envoy sidecar proxies, allowing custom processing of network traffic at various phases of the request lifecycle including authentication, authorization, metrics collection, and traffic transformation.
  - aid: istio:mesh-config-api
    name: Istio Mesh Config API
    tags:
      - Configuration
      - Networking
      - Proxy
      - Service Mesh
    humanURL: https://istio.io/latest/docs/reference/config/istio.mesh.v1alpha1/
    properties:
      - url: https://istio.io/latest/docs/reference/config/istio.mesh.v1alpha1/
        type: Documentation
      - url: https://github.com/istio/api/tree/master/mesh/v1alpha1
        type: GitHubRepository
    description: The Istio Mesh Config API (istio.mesh.v1alpha1) provides global configuration for the Istio service mesh control plane and data plane proxy behavior. It includes MeshConfig for mesh-wide settings such as access logging, tracing providers, and default proxy configuration, as well as ProxyConfig for per-workload proxy tuning and network topology settings. These settings are typically applied via the Istio ConfigMap or as annotations on workloads.
  - aid: istio:operator-api
    name: Istio Operator API
    tags:
      - Installation
      - Kubernetes
      - Operator
      - Service Mesh
    humanURL: https://istio.io/latest/docs/reference/config/istio.operator.v1alpha1/
    properties:
      - url: https://istio.io/latest/docs/reference/config/istio.operator.v1alpha1/
        type: Documentation
      - url: https://github.com/istio/istio/tree/master/operator
        type: GitHubRepository
    description: The Istio Operator API (istio.operator.v1alpha1) defines the IstioOperator custom resource used to install, configure, and upgrade Istio on Kubernetes clusters. It provides a declarative interface for selecting Istio profiles, enabling or disabling components such as ingress and egress gateways, and customizing the control plane configuration without editing raw Helm values.
name: Istio
tags:
  - CNCF
  - Kubernetes
  - Microservices
  - Open Source
  - Service Mesh
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-06-05'
modified: '2026-04-28'
position: Consumer
description: Istio is an open-source service mesh platform that provides a comprehensive solution for managing, securing, and monitoring microservices in a distributed system. It acts as a middle layer between services, handling communication, routing, and load balancing, as well as providing visibility into the traffic flowing between services. Istio also offers advanced security features such as access control, authentication, and encryption to ensure that communication between services is secure.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - type: JSON-LD
    url: json-ld/istio-context.jsonld
  - type: JSONSchema
    url: json-schema/virtual-service.json
  - type: JSONSchema
    url: json-schema/destination-rule.json
  - type: JSONSchema
    url: json-schema/gateway.json
  - name: Istio
    description: 'null'
    url: https://istio.io/
    type: Website
  - name: Istio / Blog
    description: 'null'
    url: https://istio.io/latest/blog/
    type: Blog
  - name: Istio / News
    description: 'null'
    url: https://istio.io/latest/news/
    type: News
  - name: Istio / Documentation
    description: 'null'
    url: https://istio.io/latest/docs/
    type: Documentation
  - name: Istio / Integrations
    description: 'null'
    url: https://istio.io/latest/docs/ops/integrations/
    type: Integrations
  - name: Istio / Glossary
    description: 'null'
    url: https://istio.io/latest/docs/reference/glossary/
    type: Glossary
  - name: Istio / GitHub
    description: 'null'
    url: https://github.com/istio/istio
    type: GitHub
  - name: Istio / API Repository
    description: 'null'
    url: https://github.com/istio/api
    type: GitHub
  - type: Getting Started
    url: https://istio.io/latest/docs/setup/getting-started/
  - type: GitHub Organization
    url: https://github.com/istio
  - type: Change Log
    url: https://github.com/istio/istio/releases
  - type: Community
    url: https://istio.io/latest/get-involved/
  - type: Support
    url: https://discuss.istio.io/
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/istio
  - type: Security
    url: https://istio.io/latest/docs/releases/security-vulnerabilities/
  - type: Issue Tracker
    url: https://github.com/istio/istio/issues
---
