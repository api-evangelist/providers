---
aid: gloo-mesh
name: Gloo Mesh
description: Gloo Mesh is an enterprise service mesh management platform from Solo.io built on Istio, providing multi-cluster and multi-mesh traffic management, security policy enforcement, and observability across hybrid cloud environments. It simplifies service mesh operations with a unified control plane and policy management interface, exposing Kubernetes Custom Resource Definitions (CRDs) such as AccessPolicy, JwtPolicy, and RatelimitPolicy as the primary API surface.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-04-28'
modified: '2026-04-28'
position: Consumer
tags:
  - Istio
  - Kubernetes
  - Multi-Cluster
  - Open Source
  - Service Mesh
url: https://raw.githubusercontent.com/api-evangelist/gloo-mesh/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: gloo-mesh:gloo-mesh-enterprise
    name: Gloo Mesh Enterprise
    description: Gloo Mesh Enterprise (also called Gloo Platform) is a service mesh management platform built on Istio that provides intra-mesh and multi-cluster routing, access policies, JWT authentication, rate limiting, mTLS, fault injection, observability, and more. The platform exposes 100+ Kubernetes Custom Resources as its API surface, deployed via Helm and managed with the meshctl CLI.
    humanURL: https://www.solo.io/products/gloo-mesh/
    baseURL: https://docs.solo.io/gloo-mesh-enterprise/latest/
    tags:
      - Istio
      - Kubernetes
      - Multi-Cluster
      - Service Mesh
    properties:
      - type: Documentation
        url: https://docs.solo.io/gloo-mesh-enterprise/latest/
      - type: Getting Started
        url: https://docs.solo.io/gloo-mesh-enterprise/latest/getting_started/
      - type: Reference
        url: https://docs.solo.io/gloo-mesh-enterprise/latest/reference/
      - type: Change Log
        url: https://docs.solo.io/gloo-mesh-enterprise/latest/changelog/
  - aid: gloo-mesh:gloo-mesh-core
    name: Gloo Mesh Core
    description: Gloo Mesh Core extends a single Istio service mesh with insights, operational tooling, and lifecycle management for upstream Istio deployments. It surfaces Istio insights, telemetry, and a curated set of policies to simplify Day 2 operations across a Kubernetes cluster.
    humanURL: https://www.solo.io/products/gloo-mesh/
    baseURL: https://docs.solo.io/gloo-mesh-core/latest/
    tags:
      - Istio
      - Kubernetes
      - Service Mesh
    properties:
      - type: Documentation
        url: https://docs.solo.io/gloo-mesh-core/latest/
      - type: Getting Started
        url: https://docs.solo.io/gloo-mesh-core/latest/getting_started/
      - type: Reference
        url: https://docs.solo.io/gloo-mesh-core/latest/reference/
common:
  - type: Website
    url: https://www.solo.io/
  - type: Portal
    url: https://www.solo.io/products/gloo-mesh/
  - type: Documentation
    url: https://docs.solo.io/gloo-mesh-enterprise/latest/
  - type: Getting Started
    url: https://docs.solo.io/gloo-mesh-enterprise/latest/getting_started/
  - type: Blog
    url: https://www.solo.io/blog/
  - type: GitHub Organization
    url: https://github.com/solo-io
  - type: Change Log
    url: https://docs.solo.io/gloo-mesh-enterprise/latest/changelog/
  - type: Community
    url: https://slack.solo.io/
  - type: Support
    url: https://www.solo.io/company/contact/
  - type: Terms of Service
    url: https://www.solo.io/legal/terms-of-service/
  - type: Privacy Policy
    url: https://www.solo.io/legal/privacy-policy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
