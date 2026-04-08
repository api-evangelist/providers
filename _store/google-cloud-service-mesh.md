---
aid: google-cloud-service-mesh
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-service-mesh/refs/heads/main/apis.yml
apis:
- aid: google-cloud-service-mesh:network-services-api
  name: Google Cloud Network Services API
  description: The Network Services API provides programmatic configuration of application networking infrastructure for Cloud Service Mesh. It manages gateways, meshes, HTTP/gRPC/TCP/TLS routes, endpoint policies, service load balancing policies, WebAssembly plugins, and authorization extensions through a REST interface backed by the networkservices.googleapis.com service endpoint.
  humanURL: https://cloud.google.com/service-mesh/docs/reference/network-services/rest
  baseURL: https://networkservices.googleapis.com/
  tags:
  - Networking
  - REST
  - Service Mesh
  - Traffic Management
  properties:
  - type: Documentation
    url: https://cloud.google.com/service-mesh/docs/reference/network-services/rest
  - type: Reference
    url: https://cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.meshes
  - type: Discovery
    url: https://networkservices.googleapis.com/$discovery/rest?version=v1
- aid: google-cloud-service-mesh:network-security-api
  name: Google Cloud Network Security API
  description: The Network Security API manages security policies for Cloud Service Mesh, including authorization policies, client TLS policies, and server TLS policies. It provides REST endpoints for creating and managing mTLS configuration and fine-grained access control across projects and locations, served from the networksecurity.googleapis.com service endpoint.
  humanURL: https://cloud.google.com/service-mesh/docs/reference/network-security/rest
  baseURL: https://networksecurity.googleapis.com/
  tags:
  - Authorization
  - mTLS
  - Security
  - Service Mesh
  properties:
  - type: Documentation
    url: https://cloud.google.com/service-mesh/docs/reference/network-security/rest
  - type: Reference
    url: https://cloud.google.com/service-mesh/docs/reference/network-security/rest/v1/projects.locations.authorizationPolicies
  - type: Discovery
    url: https://networksecurity.googleapis.com/$discovery/rest?version=v1
- aid: google-cloud-service-mesh:xds-control-plane-api
  name: Google Cloud Service Mesh xDS Control Plane API
  description: Cloud Service Mesh uses the open-source xDS v3 control plane API to distribute configuration to Envoy sidecar proxies and proxyless gRPC clients. Configurations defined via the Network Services and Network Security REST APIs are translated and pushed to connected clients through the xDS protocol, supporting Listener Discovery Service (LDS), Route Discovery Service (RDS), Cluster Discovery Service (CDS), and Endpoint Discovery Service (EDS).
  humanURL: https://cloud.google.com/service-mesh/docs/service-routing/xds-control-plane-apis
  baseURL: https://trafficdirector.googleapis.com/
  tags:
  - Control Plane
  - Envoy
  - Service Mesh
  - xDS
  properties:
  - type: Documentation
    url: https://cloud.google.com/service-mesh/docs/service-routing/xds-control-plane-apis
name: Google Cloud Service Mesh
tags:
- Google Cloud
- Istio
- Kubernetes
- Microservices
- Service Mesh
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Service Mesh is Google's managed service mesh solution for GKE and supported GKE Enterprise environments, enabling secure, observable, and reliable communication between microservices. It provides a managed Istio control plane, Google Cloud-native service routing APIs, mTLS security, and built-in telemetry for distributed applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

