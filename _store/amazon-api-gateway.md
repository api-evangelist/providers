---
name: Amazon API Gateway
segments:
  - Gateways
description: Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.
url: https://aws.amazon.com/api-gateway/
type: Index
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
tags:
- APIs
- Gateway
- Serverless
- REST API
- WebSocket
- HTTP API
- AWS
created: '2024'
modified: '2026-03-16'
apis:
- name: Amazon API Gateway REST API
  description: RESTful APIs that are optimized for serverless workloads and HTTP backends using HTTP APIs
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/api-gateway/
  baseURL: https://apigateway.{region}.amazonaws.com
  tags:
  - REST
  - API Management
  - Serverless
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html
  - type: OpenAPI
    url: https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html
  - type: Pricing
    url: https://aws.amazon.com/api-gateway/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/api-gateway/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/api-gateway/faqs/
  - type: Features
    url: https://aws.amazon.com/api-gateway/features/
  - type: Developer Guide
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html
  - type: API Reference
    url: https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html
  - type: Quotas
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html
  - type: OpenAPI
    url: openapi/amazon-api-gateway-rest-openapi.yml
  - type: JSON Schema
    url: json-schema/amazon-api-gateway-api-schema.json
  - type: JSON-LD
    url: json-ld/amazon-api-gateway-context.jsonld
- name: Amazon API Gateway WebSocket API
  description: Build real-time two-way communication applications with WebSocket APIs
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/api-gateway/
  baseURL: https://apigateway.{region}.amazonaws.com
  tags:
  - WebSocket
  - Real-time
  - Bi-directional
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html
  - type: Getting Started
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-overview.html
  - type: AsyncAPI
    url: asyncapi/amazon-api-gateway-websocket-asyncapi.yml
  - type: JSON-LD
    url: json-ld/amazon-api-gateway-context.jsonld
- name: Amazon API Gateway HTTP API
  description: Lower latency and lower cost alternative to REST APIs with essential features for building HTTP-based APIs
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/api-gateway/
  baseURL: https://apigateway.{region}.amazonaws.com
  tags:
  - HTTP
  - Low Latency
  - Cost Effective
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html
  - type: Comparison
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html
- name: Amazon API Gateway Management API
  description: >-
    API for directly managing runtime aspects of deployed APIs, including
    sending data to connected WebSocket clients via the @connections
    endpoint and managing connection state.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html
  baseURL: https://{api-id}.execute-api.{region}.amazonaws.com/{stage}
  tags:
  - Management
  - WebSocket
  - Connections
  - Runtime
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html
common:
- type: Blog
  url: https://aws.amazon.com/blogs/compute/category/application-services/amazon-api-gateway/
- type: Support
  url: https://aws.amazon.com/premiumsupport/
- type: Console
  url: https://console.aws.amazon.com/apigateway
- type: CLI Reference
  url: https://docs.aws.amazon.com/cli/latest/reference/apigateway/
- type: SDK
  url: https://aws.amazon.com/tools/
- type: Service Status
  url: https://status.aws.amazon.com/
- type: Compliance
  url: https://aws.amazon.com/compliance/
- type: Terms of Service
  url: https://aws.amazon.com/service-terms/
- type: Website
  url: https://aws.amazon.com/api-gateway/
- type: Documentation
  url: https://docs.aws.amazon.com/apigateway/
- type: Pricing
  url: https://aws.amazon.com/api-gateway/pricing/
- type: Getting Started
  url: https://aws.amazon.com/api-gateway/getting-started/
- type: FAQs
  url: https://aws.amazon.com/api-gateway/faqs/
- type: Privacy Policy
  url: https://aws.amazon.com/privacy/
- type: Sign Up
  url: https://portal.aws.amazon.com/billing/signup
- type: GitHub Organization
  url: https://github.com/aws
- type: Stack Overflow
  url: https://stackoverflow.com/questions/tagged/amazon-api-gateway
- type: Code Examples
  url: https://docs.aws.amazon.com/code-library/latest/ug/api-gateway_code_examples.html
maintainers:
- FN: Kin Lane
  email: kin@apievangelist.com
  url: https://apievangelist.com
include: []
---