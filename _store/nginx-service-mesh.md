---
aid: nginx-service-mesh
name: NGINX Service Mesh
description: NGINX Service Mesh (NSM) is a service mesh from F5 NGINX powered by NGINX Plus, designed to manage container-to-container traffic in Kubernetes environments. It provides mTLS, traffic policies via the Service Mesh Interface (SMI), traffic splitting, rate limiting, observability (Prometheus, Grafana, Jaeger), and integration with NGINX Plus Ingress Controller. NGINX Service Mesh exposes a control-plane REST API and a `nginx-meshctl` CLI for installation, sidecar injection, certificate management, and policy configuration. The upstream GitHub repository is archived; F5 announced End of Sale (EoS) for the NGINX Microservices Bundle as of July 1, 2023, and the project's successor for ingress and L7 routing is NGINX Gateway Fabric.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Container Networking
  - End of Sale
  - F5
  - Kubernetes
  - mTLS
  - NGINX
  - Observability
  - Service Mesh
  - SMI
  - Traffic Management
url: https://raw.githubusercontent.com/api-evangelist/nginx-service-mesh/refs/heads/main/apis.yml
created: '2026-04-28'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: nginx-service-mesh:control-plane-api
    name: NGINX Service Mesh Control Plane API
    description: The NGINX Service Mesh control plane exposes a REST API used by the `nginx-meshctl` CLI to manage mesh configuration, sidecar injection, certificate authority operations, traffic policies, and resource lookups. The API is internal to the cluster and is not published as a public OpenAPI document; its surface is documented through the API Usage guide and the `nginx-meshctl` reference.
    humanURL: https://docs.nginx.com/nginx-service-mesh/reference/api-usage/
    tags:
      - API
      - Control Plane
      - Kubernetes
      - REST
    properties:
      - type: Documentation
        url: https://docs.nginx.com/nginx-service-mesh/reference/api-usage/
      - type: CLIReference
        url: https://docs.nginx.com/nginx-service-mesh/reference/nginx-meshctl/
      - type: GitHub
        url: https://github.com/nginxinc/nginx-service-mesh
common:
  - type: Website
    url: https://docs.nginx.com/nginx-service-mesh/
  - type: Documentation
    url: https://docs.nginx.com/nginx-service-mesh/
  - type: GettingStarted
    url: https://docs.nginx.com/nginx-service-mesh/get-started/
  - type: Architecture
    url: https://docs.nginx.com/nginx-service-mesh/about/architecture/
  - type: GitHub
    url: https://github.com/nginxinc/nginx-service-mesh
  - type: Successor
    url: https://docs.nginx.com/nginx-gateway-fabric/
  - type: Blog
    url: https://www.f5.com/company/blog/nginx
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
