---
aid: haproxy
name: HAProxy
description: HAProxy is a free, very fast and reliable reverse-proxy offering high availability, load balancing, and proxying for TCP and HTTP-based applications. It exposes a Data Plane API for dynamic configuration management and a stats socket for runtime management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - High Availability
  - Load Balancing
  - Networking
  - Reverse Proxy
url: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-03-18'
specificationVersion: '0.19'
apis:
  - aid: haproxy:haproxy-data-plane-api
    name: HAProxy Data Plane API
    description: The HAProxy Data Plane API is a REST API for managing HAProxy configuration dynamically. It allows runtime configuration of frontends, backends, servers, ACLs, and other HAProxy objects without requiring configuration file changes or restarts.
    humanURL: https://www.haproxy.com/documentation/dataplaneapi/latest/
    baseURL: https://localhost:5555/v2
    tags:
      - Configuration
      - Load Balancing
      - REST API
    properties:
      - type: Documentation
        url: https://www.haproxy.com/documentation/dataplaneapi/latest/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/haproxytech/dataplaneapi/master/swagger.yaml
      - type: Getting Started
        url: https://www.haproxy.com/documentation/dataplaneapi/latest/#getting-started
      - type: GitHubRepository
        url: https://github.com/haproxytech/dataplaneapi
      - type: Change Log
        url: https://github.com/haproxytech/dataplaneapi/releases
  - aid: haproxy:haproxy-runtime-api
    name: HAProxy Runtime API
    description: The HAProxy Runtime API (formerly known as the stats socket) is a socket-based interface for dynamically managing HAProxy at runtime. It allows operators to enable or disable servers, adjust weights, inspect stick tables, view statistics, and perform other live configuration changes without reloading the process.
    humanURL: https://www.haproxy.com/documentation/haproxy-runtime-api/
    baseURL: https://localhost
    tags:
      - Load Balancing
      - Runtime Management
      - Statistics
    properties:
      - type: Documentation
        url: https://www.haproxy.com/documentation/haproxy-runtime-api/
      - type: Reference
        url: https://www.haproxy.com/documentation/haproxy-runtime-api/reference/
  - aid: haproxy:haproxy-kubernetes-ingress-controller
    name: HAProxy Kubernetes Ingress Controller
    description: The HAProxy Kubernetes Ingress Controller implements routing rules defined in Kubernetes Ingress resources, dynamically updating HAProxy configuration as pods are added or removed from the cluster. It supports the Gateway API, custom resources, and certificate management via the HAProxy Runtime API.
    humanURL: https://www.haproxy.com/documentation/kubernetes-ingress/
    baseURL: https://localhost
    tags:
      - Ingress Controller
      - Kubernetes
      - Load Balancing
    properties:
      - type: Documentation
        url: https://www.haproxy.com/documentation/kubernetes-ingress/
      - type: Getting Started
        url: https://www.haproxy.com/documentation/kubernetes-ingress/overview/
      - type: Change Log
        url: https://www.haproxy.com/documentation/kubernetes-ingress/community/release-notes/
      - type: GitHubRepository
        url: https://github.com/haproxytech/kubernetes-ingress
common:
  - type: Website
    url: https://www.haproxy.org/
  - type: Documentation
    url: https://docs.haproxy.org/
  - type: GitHub Organization
    url: https://github.com/haproxy
  - type: GitHub Organization
    url: https://github.com/haproxytech
  - type: Community
    url: https://discourse.haproxy.org/
  - type: Blog
    url: https://www.haproxy.com/blog/
  - type: Support
    url: https://www.haproxy.com/support/support-options
  - type: Terms of Service
    url: https://www.haproxy.com/legal
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
