---
aid: gloo
name: Gloo
description: Gloo is a suite of open-source and enterprise API gateway and service mesh products from Solo.io built on Envoy Proxy, offering advanced traffic management, security, observability, and developer portal capabilities for Kubernetes and cloud-native environments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consumer
tags:
  - API Gateway
  - Envoy
  - Kubernetes
  - Open Source
  - Service Mesh
url: https://raw.githubusercontent.com/api-evangelist/gloo/refs/heads/main/apis.yml
created: '2026-03-18'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: gloo:gloo-edge
    name: Gloo Edge
    description: Gloo Edge is a feature-rich, Kubernetes-native ingress controller and API gateway built on Envoy Proxy, supporting advanced routing, security policies, and observability for cloud-native workloads. It provides traffic management features such as rate limiting, transformation, and WebAssembly-based extensibility.
    humanURL: https://www.solo.io/products/gloo-gateway/
    baseURL: https://docs.solo.io/gloo-edge/latest/
    tags:
      - API Gateway
      - Envoy
      - Kubernetes
      - Open Source
    properties:
      - type: Documentation
        url: https://docs.solo.io/gloo-edge/latest/
      - type: Getting Started
        url: https://docs.solo.io/gloo-edge/latest/getting_started/
      - type: Reference
        url: https://docs.solo.io/gloo-edge/latest/reference/
      - type: Change Log
        url: https://docs.solo.io/gloo-edge/latest/changelog/
      - type: GitHubRepository
        url: https://github.com/solo-io/gloo
  - aid: gloo:gloo-gateway
    name: Gloo Gateway
    description: Gloo Gateway is the next-generation API gateway from Solo.io built on Envoy Proxy and implementing the Kubernetes Gateway API specification. It provides advanced traffic management, security, and extensibility for modern cloud-native applications with first-class support for AI and LLM traffic routing.
    humanURL: https://www.solo.io/products/gloo-gateway/
    baseURL: https://docs.solo.io/gateway/latest/
    tags:
      - API Gateway
      - Cloud Native
      - Envoy
      - Kubernetes Gateway API
    properties:
      - type: Documentation
        url: https://docs.solo.io/gateway/latest/
      - type: Getting Started
        url: https://docs.solo.io/gateway/latest/quickstart/
      - type: Reference
        url: https://docs.solo.io/gateway/latest/reference/
      - type: Change Log
        url: https://docs.solo.io/gateway/latest/changelog/
      - type: GitHubRepository
        url: https://github.com/solo-io/gloo
  - aid: gloo:gloo-mesh
    name: Gloo Mesh
    description: Gloo Mesh is an enterprise service mesh management platform from Solo.io built on Istio, providing multi-cluster and multi-mesh traffic management, security policy enforcement, and observability across hybrid cloud environments. It simplifies service mesh operations with a unified control plane and policy management interface.
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
  - aid: gloo:gloo-portal
    name: Gloo Portal
    description: Gloo Portal is a developer portal product from Solo.io that enables organizations to expose, document, and manage API products for internal and external consumers. It integrates with Gloo Gateway to provide self-service API discovery, subscription management, and usage analytics for API consumers.
    humanURL: https://www.solo.io/products/gloo-portal/
    baseURL: https://docs.solo.io/portal/latest/
    tags:
      - API Discovery
      - API Management
      - Developer Portal
      - Kubernetes
    properties:
      - type: Documentation
        url: https://docs.solo.io/portal/latest/
      - type: Getting Started
        url: https://docs.solo.io/portal/latest/getting_started/
      - type: Reference
        url: https://docs.solo.io/portal/latest/reference/
common:
  - type: Website
    url: https://www.solo.io/
  - type: Portal
    url: https://www.solo.io/products/
  - type: Documentation
    url: https://docs.solo.io/
  - type: Getting Started
    url: https://docs.solo.io/gloo-edge/latest/getting_started/
  - type: Blog
    url: https://www.solo.io/blog/
  - type: GitHub Organization
    url: https://github.com/solo-io
  - type: GitHubRepository
    url: https://github.com/solo-io/gloo
  - type: Change Log
    url: https://github.com/solo-io/gloo/releases
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
