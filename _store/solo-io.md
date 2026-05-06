---
aid: solo-io
url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/apis.yml
apis:
  - aid: solo-io:gloo-portal-server-api
    name: Solo.io Gloo Portal Server API
    tags:
      - API Gateway
      - API Keys
      - API Management
      - Developer Portal
    humanURL: https://docs.solo.io/gloo-mesh-gateway/latest/portal/openapi/
    properties:
      - url: https://docs.solo.io/gloo-mesh-gateway/latest/portal/openapi/
        type: Documentation
      - url: openapi/solo-io-gloo-portal-server-api-openapi.yml
        type: OpenAPI
      - url: json-schema/user.json
        type: JSONSchema
      - url: json-schema/api-product.json
        type: JSONSchema
      - url: json-schema/api-version.json
        type: JSONSchema
      - url: json-schema/usage-plan.json
        type: JSONSchema
      - url: json-schema/api-key.json
        type: JSONSchema
      - url: json-ld/solo-io-context.jsonld
        type: JSONLD
      - url: json-structure/gloo-portal-structure.json
        type: JSONStructure
      - url: rules/solo-io-rules.yml
        type: SpectralRules
      - url: capabilities/shared/gloo-portal.yaml
        type: NaftikoCapability
      - url: examples/gloo-portal-list-apis-example.json
        type: Example
      - url: examples/gloo-portal-create-api-key-example.json
        type: Example
    description: The Gloo Platform Portal Server API provides REST endpoints to manage user access to the developer portal and API resources. It enables developers to discover available APIs, view API schemas and documentation, manage API keys, and review usage plans for the Gloo developer portal.
  - aid: solo-io:gloo-gateway-management-api
    name: Solo.io Gloo Gateway Management API
    tags:
      - API Gateway
      - Cloud Native
      - Envoy Proxy
      - Service Mesh
      - Traffic Management
    humanURL: https://docs.solo.io/gloo-edge/latest/reference/api/
    properties:
      - url: https://docs.solo.io/gloo-edge/latest/reference/api/
        type: Documentation
      - url: openapi/solo-io-gloo-gateway-management-api-openapi.yml
        type: OpenAPI
      - url: json-schema/upstream.json
        type: JSONSchema
      - url: json-schema/virtual-service.json
        type: JSONSchema
      - url: json-schema/route.json
        type: JSONSchema
      - url: json-schema/route-table.json
        type: JSONSchema
      - url: json-schema/gateway.json
        type: JSONSchema
      - url: json-schema/proxy.json
        type: JSONSchema
      - url: json-schema/resource-metadata.json
        type: JSONSchema
      - url: json-schema/resource-status.json
        type: JSONSchema
      - url: json-ld/solo-io-context.jsonld
        type: JSONLD
      - url: json-structure/gloo-gateway-management-structure.json
        type: JSONStructure
      - url: rules/solo-io-rules.yml
        type: SpectralRules
      - url: capabilities/shared/gloo-gateway-management.yaml
        type: NaftikoCapability
      - url: examples/gloo-gateway-list-upstreams-example.json
        type: Example
      - url: examples/gloo-gateway-get-virtual-service-example.json
        type: Example
    description: The Gloo Gateway Management API provides administrative REST endpoints for managing and monitoring Gloo Gateway deployments. Gloo Gateway is a cloud-native API gateway and AI gateway built on Envoy Proxy that provides ingress control, traffic management, security, observability, and function-level routing for Kubernetes environments.
name: Solo.io
tags:
  - AI Gateway
  - Analytics
  - Automation
  - Gateways
  - Management
  - Monetization
  - Observability
  - Platform
  - Resiliency
  - Security
  - Service Mesh
  - Traffic Control
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-05-02'
position: Consuming
description: Cloud-native API management and service connectivity to automate security, observability, resiliency, and traffic control for any API or workload in any environment.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: Customers | Solo.io
    description: 'null'
    url: https://www.solo.io/customers
    type: Customers
  - name: Case Studies | Solo.io
    description: 'null'
    url: https://www.solo.io/resources/case-study
    type: CaseStudies
  - name: Blog | Solo.io
    description: 'null'
    url: https://www.solo.io/blog
    type: Blog
  - name: Docs | Solo.io
    description: 'null'
    url: https://www.solo.io/docs
    type: Documentation
  - name: White Papers | Solo.io
    description: 'null'
    url: https://www.solo.io/resources/white-paper
    type: WhitePapers
  - name: Videos | Solo.io
    description: 'null'
    url: https://www.solo.io/resources/video
    type: Videos
  - name: Webinars | Solo.io
    description: 'null'
    url: https://www.solo.io/resources/webinar
    type: Webinars
  - name: eBooks | Solo.io
    description: 'null'
    url: https://www.solo.io/resources/ebook
    type: eBooks
  - name: Partners | Solo.io
    description: 'null'
    url: https://www.solo.io/partners
    type: Partners
  - name: Get Support | Solo.io
    description: 'null'
    url: https://www.solo.io/company/get-support
    type: Support
  - name: Pricing | Solo.io
    description: 'null'
    url: https://www.solo.io/pricing
    type: Pricing
  - name: Gateway Operations Capability
    description: Unified workflow capability combining Gateway Management and Portal APIs
    url: capabilities/gateway-operations.yaml
    type: NaftikoCapability
  - name: Solo.io Vocabulary
    description: Domain vocabulary for Solo.io cloud-native API management platform
    url: vocabulary/solo-io-vocabulary.yml
    type: Vocabulary
---
