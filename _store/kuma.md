---
aid: kuma
url: https://raw.githubusercontent.com/api-evangelist/kuma/refs/heads/main/apis.yml
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
name: Kuma
tags:
- Envoy
- Kubernetes
- Microservices
- Security
- Service Mesh
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Kuma is a platform-agnostic open-source service mesh built on top of Envoy proxy. It provides universal connectivity, security, and observability for services and microservices running on any infrastructure including Kubernetes and VMs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

