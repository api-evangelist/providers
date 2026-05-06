---
aid: kuma
name: Kuma
description: Kuma is a platform-agnostic open-source service mesh built on top of Envoy proxy. It provides universal connectivity, security, and observability for services and microservices running on any infrastructure including Kubernetes and VMs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Envoy
  - Kubernetes
  - Microservices
  - Security
  - Service Mesh
url: https://raw.githubusercontent.com/api-evangelist/kuma/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kuma:kuma-api
    name: Kuma API
    description: Kuma's control plane REST API for managing service mesh policies, dataplanes, zones, and configurations. It provides endpoints for inspecting and managing all mesh resources including traffic policies, service discovery, and health checks across Universal and Kubernetes deployments.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://kuma.io/docs/latest/reference/http-api/
    baseURL: https://localhost:5681
    tags:
      - Control Plane
      - Management
      - REST API
      - Service Mesh
    properties:
      - type: Documentation
        url: https://kuma.io/docs/latest/reference/http-api/
      - type: Getting Started
        url: https://kuma.io/docs/latest/installation/
      - type: Reference
        url: https://kuma.io/docs/latest/reference/http-api/
      - type: OpenAPI
        url: openapi/kuma-api-openapi.yml
      - type: JSONSchema
        url: json-schema/kuma-mesh-schema.json
  - aid: kuma:kuma-kubernetes-policy-api
    name: Kuma Kubernetes Policy API
    description: Kuma extends the Kubernetes API server with Custom Resource Definitions (CRDs) for defining and managing service mesh policies. These resources include MeshTrafficPermission, MeshRetry, MeshTimeout, MeshCircuitBreaker, MeshHealthCheck, MeshFaultInjection, and MeshRateLimit, enabling fine-grained traffic management, security, and resilience policies for meshed workloads.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://kuma.io/docs/latest/policies/
    tags:
      - CRD
      - Kubernetes
      - Policy
      - Traffic Management
    properties:
      - type: Documentation
        url: https://kuma.io/docs/latest/policies/
      - type: Reference
        url: https://kuma.io/docs/latest/reference/kubernetes-annotations/
  - aid: kuma:kuma-multizone-api
    name: Kuma Multizone API
    description: Kuma's Multizone deployment API enables managing service meshes across multiple Kubernetes clusters and Universal zones from a single global control plane. It provides resources for zone management, cross-zone traffic routing, and zone egress and ingress configuration.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://kuma.io/docs/latest/production/deployment/multi-zone/
    tags:
      - Control Plane
      - Federation
      - Multi-Cluster
      - Multizone
    properties:
      - type: Documentation
        url: https://kuma.io/docs/latest/production/deployment/multi-zone/
      - type: Reference
        url: https://kuma.io/docs/latest/reference/http-api/
common:
  - type: Website
    url: https://kuma.io/
  - type: Documentation
    url: https://kuma.io/docs/
  - type: Getting Started
    url: https://kuma.io/docs/latest/installation/
  - type: GitHub Organization
    url: https://github.com/kumahq
  - type: GitHubRepository
    url: https://github.com/kumahq/kuma
  - type: Community
    url: https://kuma.io/community/
  - type: Blog
    url: https://kuma.io/blog/
  - type: Slack
    url: https://kuma-mesh.slack.com/
  - type: Change Log
    url: https://github.com/kumahq/kuma/releases
  - type: Support
    url: https://kuma.io/community/
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/kuma
  - type: Security
    url: https://github.com/kumahq/kuma/blob/master/SECURITY.md
  - type: YouTube
    url: https://www.youtube.com/@KumaMesh
  - type: JSONSchema
    url: json-schema/kuma-mesh-schema.json
  - type: JSON-LD
    url: json-ld/kuma-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
