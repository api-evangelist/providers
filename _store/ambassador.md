---
aid: ambassador
url: https://raw.githubusercontent.com/api-evangelist/ambassador/refs/heads/main/apis.yml
apis:
- aid: ambassador:ambassador
  name: Ambassador
  tags:
  - Gateways
  - Mocking
  - Testing
  humanURL: https://www.getambassador.io/
  properties:
  - url: https://www.getambassador.io/
    type: Documentation
  description: Ambassador offers a suite of products designed to deliver API developer experiences that fuel innovation. These products, Blackbird API Development Platform, Edge Stack API Gateway, and Telepresence, accelerate development, expedite testing, and optimize the delivery of API resources.
- aid: ambassador:edge-stack-api-gateway
  name: Ambassador Edge Stack API Gateway
  tags:
  - API Management
  - Envoy
  - Gateways
  - Ingress
  - Kubernetes
  humanURL: https://www.getambassador.io/products/edge-stack/api-gateway
  properties:
  - url: https://www.getambassador.io/products/edge-stack/api-gateway
    type: Documentation
  - url: https://www.getambassador.io/docs/edge-stack/latest/tutorials/getting-started/
    type: Getting Started
  - url: https://www.getambassador.io/docs/edge-stack/latest/topics/install/
    type: Installation
  - url: https://www.getambassador.io/docs/edge-stack/latest/topics/install/helm/
    type: Helm Chart
  - url: https://www.getambassador.io/docs/edge-stack/latest/topics/using/intro-mappings
    type: Documentation
  - url: https://www.getambassador.io/docs/edge-stack/latest/topics/running/host-crd
    type: Documentation
  - url: https://www.getambassador.io/docs/edge-stack/latest/topics/using/rate-limits
    type: Documentation
  - url: https://www.getambassador.io/docs/edge-stack/latest/topics/using/filters/oauth2
    type: Documentation
  - url: https://www.getambassador.io/docs/edge-stack/latest/topics/using/filters/apikeys
    type: Documentation
  - url: https://www.getambassador.io/docs/edge-stack/latest/topics/using/gateway-api
    type: Documentation
  - url: https://www.getambassador.io/docs/edge-stack/latest/about/changes-2.x
    type: Documentation
  - url: https://www.getambassador.io/docs/edge-stack/latest/tutorials/quickstart-demo
    type: Getting Started
  - url: https://github.com/datawire/edge-stack
    type: GitHub
  - url: openapi/ambassador-openapi.yml
    type: OpenAPI
  description: Ambassador Edge Stack is a Kubernetes-native API gateway built on Envoy Proxy that provides routing, load balancing, authentication, rate limiting, and observability for microservices. It supports custom resource definitions (CRDs) including Mapping, Host, TLSContext, and RateLimit for declarative configuration.
- aid: ambassador:emissary-ingress
  name: Emissary-Ingress
  tags:
  - CNCF
  - Envoy
  - Gateways
  - Ingress
  - Kubernetes
  - Open Source
  humanURL: https://www.getambassador.io/docs/emissary
  properties:
  - url: https://www.getambassador.io/docs/emissary
    type: Documentation
  - url: https://emissary-ingress.dev/
    type: Documentation
  - url: https://www.getambassador.io/docs/emissary/latest/tutorials/quickstart-demo
    type: Getting Started
  - url: https://github.com/emissary-ingress/emissary
    type: GitHub
  - url: https://github.com/emissary-ingress/emissary/blob/master/CHANGELOG.md
    type: Changelog
  description: Emissary-Ingress is an open-source, Kubernetes-native API gateway built on Envoy Proxy and a CNCF incubating project, formerly known as Ambassador API Gateway. It uses custom resource definitions (CRDs) including Mapping, Host, Listener, and TLSContext for declarative edge management.
- aid: ambassador:telepresence-api
  name: Ambassador Telepresence RESTful API
  tags:
  - Debugging
  - Development
  - Intercepts
  - Kubernetes
  humanURL: https://www.getambassador.io/docs/telepresence/latest/reference/restapi
  properties:
  - url: https://www.getambassador.io/docs/telepresence/latest/reference/restapi
    type: Documentation
  - url: https://www.getambassador.io/docs/telepresence-oss/latest/quick-start
    type: Getting Started
  - url: https://www.getambassador.io/docs/telepresence/latest/howtos/intercepts
    type: Documentation
  - url: https://www.getambassador.io/docs/telepresence/latest/concepts/intercepts
    type: Documentation
  - url: https://www.getambassador.io/docs/telepresence/latest/reference/config
    type: Documentation
  - url: https://www.getambassador.io/products/telepresence
    type: Documentation
  description: Telepresence provides a RESTful API server that runs on the local host, both on the local workstation and in a pod that contains a traffic-agent. The API includes healthz, consume-here, and intercept-info endpoints for managing service intercepts in Kubernetes development environments.
- aid: ambassador:blackbird-api-development-platform
  name: Ambassador Blackbird API Development Platform
  tags:
  - API Development
  - Code Generation
  - Mocking
  - OpenAPI
  - Testing
  humanURL: https://www.getambassador.io/products/blackbird/api-development
  properties:
  - url: https://www.getambassador.io/products/blackbird/api-development
    type: Documentation
  - url: https://www.getambassador.io/docs/blackbird
    type: Documentation
  - url: https://www.getambassador.io/docs/blackbird/latest/install/quickstart
    type: Getting Started
  - url: https://www.getambassador.io/docs/blackbird/latest/guides/api/quickstart
    type: Getting Started
  - url: https://www.getambassador.io/docs/blackbird/latest/guides/code/quickstart
    type: Getting Started
  - url: https://www.getambassador.io/docs/blackbird/latest/guides/deployments/quickstart
    type: Getting Started
  - url: https://www.getambassador.io/docs/blackbird/latest/release-notes
    type: Changelog
  - url: https://www.getambassador.io/docs/blackbird/latest/reference/mcp
    type: Documentation
  description: Blackbird is an API development platform that helps developers design, build, test, and manage APIs with AI-powered code generation, mocking, and production-like test environments. It supports OpenAPI specifications and provides integrated debugging tools.
- aid: ambassador:edge-stack-developer-portal
  name: Ambassador Edge Stack Developer Portal
  tags:
  - API Catalog
  - Developer Portal
  - Documentation
  - OpenAPI
  humanURL: https://www.getambassador.io/docs/edge-stack/latest/tutorials/dev-portal-tutorial
  properties:
  - url: https://www.getambassador.io/docs/edge-stack/latest/tutorials/dev-portal-tutorial
    type: Getting Started
  - url: https://www.getambassador.io/docs/latest/topics/using/dev-portal/
    type: Documentation
  - url: https://www.getambassador.io/products/edge-stack/api-gateway/developer-portal
    type: Documentation
  description: The Ambassador Edge Stack Developer Portal automatically detects and publishes API documentation, serving as a single point of reference for all microservice APIs. It supports Swagger and OpenAPI V3 specifications and provides a fully customizable portal for internal and external developer onboarding.
name: Ambassador
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
type: Contract
image: https://www.getambassador.io/images/ambassador-logo.png
access: 3rd-Party
common:
- url: https://www.getambassador.io/case-studies
  name: 'Empowering Journeys: Customer Success Stories That Speak Volumes'
  type: CaseStudies
  description: 'null'
- url: https://www.getambassador.io/pricing
  name: Ambassador Pricing | Scalable Plans for Edge Stack & Telepresence
  type: Pricing
  description: 'null'
- url: https://www.getambassador.io/blog
  name: Blog | Ambassador
  type: Blog
  description: 'null'
- url: https://www.getambassador.io/faq
  name: Edge Stack API Gateway and Telepresence FAQs
  type: FAQ
  description: 'null'
- url: https://www.getambassador.io/docs
  name: Docs Home | Ambassador Labs
  type: Documentation
  description: 'null'
- url: https://www.getambassador.io/support
  name: Support | Ambassador Labs
  type: Support
  description: 'null'
- url: https://www.getambassador.io/company/partnerships
  name: Join the Ambassador Partner Program
  type: Partners
  description: 'null'
created: '2025-01-08'
modified: '2026-04-07'
position: Consuming
description: Ambassador is a Kubernetes-native API Gateway built on Envoy Proxy, providing routing, load balancing, authentication, and observability for microservices.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

