---
aid: open-service-mesh
name: Open Service Mesh
description: Open Service Mesh (OSM) is a lightweight, extensible, cloud native service mesh built on Envoy and the Service Mesh Interface (SMI) specification. OSM provides traffic shifting, mutual TLS, access control, observability, and automatic sidecar injection for Kubernetes-based microservices. The project is now archived by the CNCF.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Envoy
  - Kubernetes
  - Microservices
  - Service Mesh
  - SMI
created: '2026-04-28'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/open-service-mesh/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: open-service-mesh:open-service-mesh
    name: Open Service Mesh
    description: Service mesh control plane for Kubernetes that implements the Service Mesh Interface (SMI) specification, providing traffic management, security, and observability for microservices via Envoy sidecar proxies.
    humanURL: https://openservicemesh.io
    tags:
      - Service Mesh
      - Kubernetes
    properties:
      - type: Documentation
        url: https://docs.openservicemesh.io
      - type: GitHubRepo
        url: https://github.com/openservicemesh/osm
common:
  - type: Website
    url: https://openservicemesh.io
  - type: Documentation
    url: https://docs.openservicemesh.io
  - type: GitHubRepo
    url: https://github.com/openservicemesh/osm
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
