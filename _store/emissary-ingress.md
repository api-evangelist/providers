---
aid: emissary-ingress
name: Emissary-Ingress
description: Emissary-Ingress is a CNCF incubating Kubernetes-native API gateway built on the Envoy proxy. It provides ingress control, load balancing, authentication, rate limiting, and traffic management for microservices. Emissary-Ingress is configured through Kubernetes custom resources and supports canary releases, circuit breaking, and automatic retries.
url: https://www.getambassador.io/products/api-gateway
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - Cloud Native
  - Envoy
  - Incubating
  - Ingress
  - Kubernetes
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
apis:
  - aid: emissary-ingress:emissary-ingress-api
    name: Emissary-Ingress Configuration API
    description: Emissary-Ingress is configured through Kubernetes custom resources including Mapping for routing rules, Host for domain configuration, TLSContext for TLS termination, RateLimitService for rate limiting, and AuthService for external authentication. These CRDs provide declarative API gateway configuration within the Kubernetes ecosystem.
    humanURL: https://www.getambassador.io/docs/emissary/
    properties:
      - type: Documentation
        url: https://www.getambassador.io/docs/emissary/
      - type: Getting Started
        url: https://www.getambassador.io/docs/emissary/latest/topics/install/yaml-install
      - type: Reference
        url: https://www.getambassador.io/docs/emissary/latest/topics/running/
      - type: Change Log
        url: https://archive.getambassador.io/docs/emissary/3.1/release-notes/
      - type: OpenAPI
        url: openapi/emissary-ingress-openapi.yml
      - type: JSONSchema
        url: json-schema/emissary-ingress-mapping-schema.json
      - type: Authentication
        url: https://www.getambassador.io/docs/emissary/latest/topics/running/services/auth-service
      - type: Quotas
        url: https://www.getambassador.io/docs/emissary/latest/topics/running/services/rate-limit-service
    tags:
      - API Gateway
      - Configuration
      - Routing
  - aid: emissary-ingress:emissary-ingress-gateway-api
    name: Emissary-Ingress Gateway API
    description: Emissary-Ingress supports a subset of the Kubernetes Gateway API standard, including GatewayClass, Gateway, and HTTPRoute resources. This enables teams to use the next-generation Kubernetes ingress standard for defining routing rules, with support for path matching, header matching, and weighted load balancing across backend services.
    humanURL: https://emissary-ingress.dev/docs/3.8/topics/using/gateway-api/
    properties:
      - type: Documentation
        url: https://emissary-ingress.dev/docs/3.8/topics/using/gateway-api/
    tags:
      - Gateway API
      - HTTPRoute
      - Kubernetes
      - Routing
common:
  - type: Website
    url: https://www.getambassador.io/products/api-gateway
  - type: Documentation
    url: https://www.getambassador.io/docs/emissary/
  - type: Getting Started
    url: https://www.getambassador.io/docs/emissary/latest/topics/install/yaml-install
  - type: GitHub Organization
    url: https://github.com/emissary-ingress
  - type: GitHubRepository
    url: https://github.com/emissary-ingress/emissary
  - type: Support
    url: https://www.getambassador.io/docs/emissary/latest/about/support
  - type: Community
    url: https://emissary-ingress.dev/docs/4.0/community/
  - type: Issue Tracker
    url: https://github.com/emissary-ingress/emissary/issues
  - type: Blog
    url: https://blog.getambassador.io/
  - type: Change Log
    url: https://archive.getambassador.io/docs/emissary/3.1/release-notes/
  - type: JSON-LD
    url: json-ld/emissary-ingress-context.jsonld
  - type: JSONSchema
    url: json-schema/emissary-ingress-mapping-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
