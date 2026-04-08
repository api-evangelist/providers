---
aid: google-cloud-api-gateway
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-api-gateway/refs/heads/main/apis.yml
apis:
- name: Google Cloud API Gateway API
  description: The API Gateway API allows you to create and manage API gateways, API configurations, and deploy APIs described using OpenAPI specifications. It provides programmatic access to manage gateways that proxy requests to your serverless backends.
  humanURL: https://cloud.google.com/api-gateway/docs
  baseURL: https://apigateway.googleapis.com
  properties:
  - type: Documentation
    url: https://cloud.google.com/api-gateway/docs/reference/rest
  - type: OpenAPI
    url: openapi/openapi.yml
  - type: Authentication
    url: https://cloud.google.com/api-gateway/docs/authentication-method
  - type: Getting Started
    url: https://cloud.google.com/api-gateway/docs/quickstart
  - type: JSONSchema
    url: json-schema/json-schema.yml
  tags:
  - API Gateway
  - API Management
  - Serverless
name: Google Cloud API Gateway
tags:
- API Gateway
- API Management
- Authentication
- Google Cloud
- Security
- Serverless
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud API Gateway enables you to provide secure access to your backend services through a well-defined REST API that is consistent across all of your services. It is a fully managed, pay-per-use gateway designed for serverless workloads, supporting Cloud Functions, Cloud Run, and App Engine backends. API Gateway includes security features like authentication and API key validation, as well as monitoring, logging, and tracing capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

