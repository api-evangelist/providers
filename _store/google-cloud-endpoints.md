---
aid: google-cloud-endpoints
name: Google Cloud Endpoints
description: Google Cloud Endpoints is an API management system that helps you secure, monitor, analyze, and set quotas on your APIs using the same infrastructure Google uses for its own APIs. Endpoints works with the Extensible Service Proxy (ESP) or ESPv2 to provide API management capabilities including authentication, monitoring, logging, and API key validation for APIs described using OpenAPI specifications. It supports APIs hosted on App Engine, GKE, Compute Engine, or any Docker-supported environment.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-endpoints/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - API Gateway
  - API Management
  - Authentication
  - Google Cloud
  - Monitoring
  - Rate Limiting
apis:
  - name: Google Cloud Service Management API
    description: The Service Management API enables management of managed services used by Cloud Endpoints. It allows you to create, configure, and deploy API configurations, manage service rollouts, and control access to your APIs.
    humanURL: https://cloud.google.com/endpoints/docs
    baseURL: https://servicemanagement.googleapis.com
    properties:
      - type: Documentation
        url: https://cloud.google.com/endpoints/docs/reference/service-management/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://cloud.google.com/endpoints/docs/grpc/authenticating-users
      - type: Getting Started
        url: https://cloud.google.com/endpoints/docs/openapi/get-started-cloud-run
      - type: JSONSchema
        url: json-schema/json-schema.yml
    tags:
      - API Management
      - Endpoints
      - Service Management
common:
  - type: Portal
    url: https://cloud.google.com/endpoints
  - type: Getting Started
    url: https://cloud.google.com/endpoints/docs/openapi/get-started-cloud-run
  - type: Documentation
    url: https://cloud.google.com/endpoints/docs
  - type: Authentication
    url: https://cloud.google.com/endpoints/docs/grpc/authenticating-users
  - type: Pricing
    url: https://cloud.google.com/endpoints/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/endpoints/docs/support
  - type: JSONLD
    url: json-ld/json-ld.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
