---
aid: apiida
url: https://raw.githubusercontent.com/api-evangelist/apiida/refs/heads/main/apis.yml
apis:
- aid: apiida:api-control-plane
  name: APIIDA API Control Plane
  tags:
  - Lifecycle
  - Platform
  humanURL: https://apiida.com/product/apiida-api-control-plane/
  properties:
  - url: https://apiida.com/product/apiida-api-control-plane/
    type: Documentation
  - url: openapi/apiida-api-control-plane-openapi.yml
    type: OpenAPI
  - url: json-schema/apiida-api.json
    type: JSONSchema
  - url: json-schema/apiida-deployment.json
    type: JSONSchema
  - url: json-ld/apiida-context.jsonld
    type: JSONLD
  description: REST API for the APIIDA API Control Plane, enabling programmatic management of APIs across multiple API gateways. Supports validation of proxy specifications, API version management, and deployment to gateways from a central federated control plane.
- aid: apiida:api-gateway-manager
  name: APIIDA API Gateway Manager
  tags:
  - Deployments
  - Gateways
  - Monitoring
  humanURL: https://apiida.com/product/apiida-api-gateway-manager/
  properties:
  - url: https://apiida.com/product/apiida-api-gateway-manager/
    type: Documentation
  - url: https://apiida.atlassian.net/wiki/spaces/AAGM
    type: Documentation
  - url: openapi/apiida-api-gateway-manager-openapi.yml
    type: OpenAPI
  - url: json-schema/apiida-gateway.json
    type: JSONSchema
  - url: json-schema/apiida-deployment.json
    type: JSONSchema
  - url: json-ld/apiida-context.jsonld
    type: JSONLD
  description: REST API for the APIIDA API Gateway Manager, enabling programmatic management of Broadcom Layer7 API gateways. Supports gateway registration, API deployment and migration, monitoring and metrics collection, and alarm configuration across managed gateway instances.
name: APIIDA
tags:
- Gateways
- Platform
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-07'
position: Consumer
description: APIIDA provides market-leading solutions for multi-vendor, cross-platform federated API management. The APIIDA API Control Plane enables enterprises to discover, govern, and provision APIs from a central location, while the API Gateway Manager automates API operations for Broadcom Layer7 environments with comprehensive deployment, migration, monitoring, and alarming capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

