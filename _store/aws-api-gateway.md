---
aid: aws-api-gateway
url: https://raw.githubusercontent.com/api-evangelist/aws-api-gateway/refs/heads/main/apis.yml
apis:
- aid: aws-api-gateway:aws-api-gateway-v1
  name: Amazon API Gateway V1 (REST)
  description: The API Gateway V1 control plane API is used to create, deploy, and manage REST APIs in Amazon API Gateway. It exposes resources for RestApis, Resources, Methods, Stages, Deployments, Authorizers, API keys, usage plans, and related configuration.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html
  baseURL: https://apigateway.{region}.amazonaws.com
  tags:
  - API Gateway
  - AWS
  - REST
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/
  - type: Reference
    url: https://docs.aws.amazon.com/apigateway/latest/api/Welcome.html
  - type: Getting Started
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started.html
  - type: Authentication
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html
  - type: OpenAPI
    url: openapi/aws-api-gateway-v1-openapi.yml
- aid: aws-api-gateway:aws-api-gateway-v2
  name: Amazon API Gateway V2 (HTTP and WebSocket)
  description: The API Gateway V2 control plane API is used to create, deploy, and manage HTTP APIs and WebSocket APIs in Amazon API Gateway. It provides resources for Apis, Routes, Integrations, Stages, Deployments, and Authorizers for the newer HTTP and WebSocket API types.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html
  baseURL: https://apigateway.{region}.amazonaws.com
  tags:
  - API Gateway
  - AWS
  - HTTP
  - WebSocket
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html
  - type: Reference
    url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/Welcome.html
  - type: Getting Started
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop.html
  - type: WebSocket Guide
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html
  - type: OpenAPI
    url: openapi/aws-api-gateway-v2-openapi.yml
- aid: aws-api-gateway:aws-api-gateway-management
  name: Amazon API Gateway Management API
  description: The API Gateway Management API allows backend services to send messages to connected clients of a deployed WebSocket API and to disconnect clients. Requests are made against the deployed stage's callback URL.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://docs.aws.amazon.com/apigatewaymanagementapi/latest/reference/Welcome.html
  baseURL: https://{api-id}.execute-api.{region}.amazonaws.com/{stage}
  tags:
  - API Gateway
  - AWS
  - Callback
  - WebSocket
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html
  - type: Reference
    url: https://docs.aws.amazon.com/apigatewaymanagementapi/latest/reference/Welcome.html
  - type: OpenAPI
    url: openapi/aws-api-gateway-management-openapi.yml
name: Amazon API Gateway
tags:
- API Gateway
- AWS
- Cloud
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon API Gateway is a fully managed service that makes it easy to create, publish, maintain, monitor, and secure APIs at any scale.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

