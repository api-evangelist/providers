---
aid: google-cloud-api-gateway
name: Google Cloud API Gateway
description: Google Cloud API Gateway enables you to provide secure access to your backend services through a well-defined REST API that is consistent across all of your services. It is a fully managed, pay-per-use gateway designed for serverless workloads, supporting Cloud Functions, Cloud Run, and App Engine backends. API Gateway includes security features like authentication and API key validation, as well as monitoring, logging, and tracing capabilities.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-api-gateway/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - API Gateway
  - API Management
  - Authentication
  - Google Cloud
  - Security
  - Serverless
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
common:
  - type: Portal
    url: https://cloud.google.com/api-gateway
  - type: Getting Started
    url: https://cloud.google.com/api-gateway/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/api-gateway/docs
  - type: Authentication
    url: https://cloud.google.com/api-gateway/docs/authentication-method
  - type: Pricing
    url: https://cloud.google.com/api-gateway/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/api-gateway/docs/support
  - type: JSONLD
    url: json-ld/json-ld.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
