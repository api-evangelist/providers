---
aid: envoy-gateway
name: Envoy Gateway
description: Envoy Gateway is a CNCF project providing a Kubernetes-native API gateway built on Envoy Proxy, implementing the Kubernetes Gateway API for simplified traffic management and ingress control. Envoy Gateway exposes its functionality through Kubernetes Gateway API resources and Custom Resource Definitions rather than a traditional REST API.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - CNCF
  - Envoy
  - Kubernetes
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: envoy-gateway:envoy-gateway
    name: Envoy Gateway
    description: Envoy Gateway provides an expressive, extensible, role-oriented API for Kubernetes gateway management built on Envoy Proxy. Configuration is done through Kubernetes Gateway API resources (Gateway, GatewayClass, HTTPRoute, GRPCRoute) and Envoy Gateway CRDs (BackendTrafficPolicy, ClientTrafficPolicy, SecurityPolicy).
    humanURL: https://gateway.envoyproxy.io/
    tags:
      - API Gateway
      - Kubernetes
      - CNCF
    properties:
      - type: Documentation
        url: https://gateway.envoyproxy.io/docs/
      - type: Getting Started
        url: https://gateway.envoyproxy.io/docs/tasks/quickstart/
      - type: API Reference
        url: https://gateway.envoyproxy.io/docs/api/extension_types/
      - type: GitHub
        url: https://github.com/envoyproxy/gateway
common:
  - type: Website
    url: https://gateway.envoyproxy.io/
  - type: Documentation
    url: https://gateway.envoyproxy.io/docs/
  - type: GitHub Organization
    url: https://github.com/envoyproxy
  - type: Source Code
    url: https://github.com/envoyproxy/gateway
  - type: Releases
    url: https://github.com/envoyproxy/gateway/releases
  - type: Slack
    url: https://envoyproxy.slack.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
