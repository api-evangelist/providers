---
aid: kgateway
url: https://raw.githubusercontent.com/api-evangelist/kgateway/refs/heads/main/apis.yml
apis:
  - aid: kgateway:kgateway-kubernetes-gateway-api
    name: Kgateway Kubernetes Gateway API
    tags:
      - AI Gateway
      - API Gateway
      - Envoy
      - Gateways
      - Kubernetes
      - Traffic Management
    humanURL: https://kgateway.dev/docs/envoy/latest/reference/api/
    baseURL: https://kubernetes.default.svc/apis/gateway.kgateway.dev/v1alpha1
    properties:
      - url: https://kgateway.dev/docs/envoy/latest/reference/api/
        type: Documentation
      - url: openapi/kgateway-kubernetes-gateway-api-openapi.yml
        type: OpenAPI
      - url: json-schema/traffic-policy.json
        type: JSONSchema
      - url: json-schema/backend.json
        type: JSONSchema
      - url: json-schema/direct-response.json
        type: JSONSchema
      - url: json-schema/gateway-extension.json
        type: JSONSchema
      - url: json-schema/gateway-parameters.json
        type: JSONSchema
      - url: json-schema/http-listener-policy.json
        type: JSONSchema
      - url: json-schema/ai-backend.json
        type: JSONSchema
      - url: json-ld/kgateway-context.jsonld
        type: JSONLD
    description: The kgateway Kubernetes Gateway API provides custom resource definitions (CRDs) under the gateway.kgateway.dev/v1alpha1 API group for managing traffic policies, backends, direct responses, gateway extensions, gateway parameters, HTTP listener policies, and AI backends. kgateway is built on Envoy proxy and implements the Kubernetes Gateway API for microservices and AI agent traffic management.
name: Kgateway
tags:
  - Gateways
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-02'
modified: '2026-04-28'
position: Consumer
description: kgateway is the most widely deployed gateway in Kubernetes for microservices and AI agents. It is a feature-rich, fast, and flexible Kubernetes-native ingress controller and next-generation API gateway built on top of Envoy proxy and the Kubernetes Gateway API.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: kgateway
    description: 'null'
    url: https://kgateway.dev/
    type: Website
  - name: Videos – kgateway
    description: 'null'
    url: https://kgateway.dev/resources/videos/
    type: Videos
  - name: Blog – kgateway
    description: 'null'
    url: https://kgateway.dev/blog/
    type: Blog
  - name: Kgateway 2.1.x – kgateway
    description: 'null'
    url: https://kgateway.dev/docs/envoy/latest/
    type: Documentation
  - name: GitHub Repository
    description: 'null'
    url: https://github.com/kgateway-dev/kgateway
    type: GitHub
---
