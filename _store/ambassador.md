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
        type: GettingStarted
      - url: https://www.getambassador.io/docs/edge-stack/latest/topics/install/
        type: Documentation
      - url: https://www.getambassador.io/docs/edge-stack/latest/topics/install/helm/
        type: Documentation
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
        type: GettingStarted
      - url: https://github.com/datawire/edge-stack
        type: GitHubRepository
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
        type: GettingStarted
      - url: https://github.com/emissary-ingress/emissary
        type: GitHubRepository
      - url: https://github.com/emissary-ingress/emissary/blob/master/CHANGELOG.md
        type: ChangeLog
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
        type: GettingStarted
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
        type: GettingStarted
      - url: https://www.getambassador.io/docs/blackbird/latest/guides/api/quickstart
        type: GettingStarted
      - url: https://www.getambassador.io/docs/blackbird/latest/guides/code/quickstart
        type: GettingStarted
      - url: https://www.getambassador.io/docs/blackbird/latest/guides/deployments/quickstart
        type: GettingStarted
      - url: https://www.getambassador.io/docs/blackbird/latest/release-notes
        type: ReleaseNotes
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
        type: GettingStarted
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
    type: Customers
  - url: https://www.getambassador.io/pricing
    name: Ambassador Pricing | Scalable Plans for Edge Stack & Telepresence
    type: Pricing
  - url: https://www.getambassador.io/blog
    name: Blog | Ambassador
    type: Blog
  - url: https://www.getambassador.io/faq
    name: Edge Stack API Gateway and Telepresence FAQs
    type: FAQ
  - url: https://www.getambassador.io/docs
    name: Docs Home | Ambassador Labs
    type: Documentation
  - url: https://www.getambassador.io/support
    name: Support | Ambassador Labs
    type: Support
  - url: https://www.getambassador.io/company/partnerships
    name: Join the Ambassador Partner Program
    type: Partners
  - url: https://www.getambassador.io/docs/edge-stack/latest/tutorials/getting-started/
    type: GettingStarted
  - url: https://github.com/emissary-ingress/emissary
    type: GitHubRepository
  - url: https://github.com/emissary-ingress/emissary/blob/master/CHANGELOG.md
    type: ChangeLog
  - url: https://status.datawire.io/
    type: StatusPage
  - url: https://www.getambassador.io/products/edge-stack/api-gateway/security-authentication
    type: Authentication
  - url: https://www.getambassador.io/docs/edge-stack/latest/howtos/rate-limiting-tutorial
    type: RateLimits
  - url: https://x.com/ambassadorlabs
    type: X
  - url: https://www.linkedin.com/company/ambassadorlabs
    type: LinkedIn
  - url: https://app.getambassador.io/
    type: SignUp
  - url: https://github.com/datawire/ambassador-docs
    type: GitHubRepository
  - url: https://github.com/datawire
    type: GitHubOrganization
  - url: json-ld/ambassador-context.jsonld
    type: JSONLD
  - url: json-schema/ambassador-mapping-schema.json
    type: JSONSchema
  - type: Features
    data:
      - name: Kubernetes-Native API Gateway
        description: Purpose-built for Kubernetes with custom resource definitions (CRDs) for declarative configuration of routing, TLS, and rate limiting.
      - name: Envoy Proxy Foundation
        description: Built on Envoy Proxy for high-performance load balancing, circuit breaking, and observability at the edge.
      - name: Authentication and Security
        description: Integrated OAuth2, API key, and JWT-based authentication filters to secure API endpoints without custom code.
      - name: Rate Limiting
        description: Configurable rate limiting with labels and descriptors to control request throughput to backend services.
      - name: Developer Portal
        description: Automatic API documentation publishing from OpenAPI/Swagger specs with customizable developer portal for onboarding.
      - name: Local Development with Telepresence
        description: Intercept and debug remote Kubernetes services locally using Telepresence for fast inner-loop development.
      - name: API Mocking with Blackbird
        description: AI-powered API development platform with mock servers and production-like test environments for rapid iteration.
  - type: UseCases
    data:
      - name: Microservices API Gateway
        description: Route, secure, and observe traffic to microservices running in Kubernetes clusters.
      - name: API Development and Testing
        description: Design, mock, and test APIs locally with Blackbird before deploying to Kubernetes environments.
      - name: Multi-Team API Management
        description: Enable multiple teams to independently manage their API routing and configuration using Kubernetes CRDs.
      - name: Service Mesh Edge Gateway
        description: Serve as the edge gateway in a service mesh architecture, handling north-south traffic with TLS termination.
      - name: Developer Onboarding
        description: Provide a self-service developer portal for internal and external developers to discover and consume APIs.
  - type: Integrations
    data:
      - name: Kubernetes
        description: Native integration with Kubernetes using CRDs for Mapping, Host, TLSContext, and RateLimit resources.
      - name: Envoy Proxy
        description: Built on Envoy Proxy with full access to Envoy's load balancing, circuit breaking, and observability features.
      - name: Helm
        description: Install and manage Ambassador Edge Stack using Helm charts for Kubernetes deployments.
      - name: Prometheus and Grafana
        description: Export metrics to Prometheus and visualize API gateway performance in Grafana dashboards.
      - name: Cert-Manager
        description: Automatic TLS certificate management via cert-manager and ACME protocol integration.
created: '2025-01-08'
modified: '2026-04-18'
position: Consuming
segments:
  - Gateways
description: Ambassador is a Kubernetes-native API Gateway built on Envoy Proxy, providing routing, load balancing, authentication, and observability for microservices.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
  - name: Ambassador Labs (Datawire)
    email: support@datawire.io
    url: https://www.getambassador.io
specificationVersion: '0.19'
---
