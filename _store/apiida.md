---
aid: apiida
name: APIIDA
description: APIIDA provides market-leading solutions for multi-vendor, cross-platform federated API management. The APIIDA API Control Plane enables enterprises to discover, govern, and provision APIs from a central location, while the API Gateway Manager automates API operations for Broadcom Layer7 environments with comprehensive deployment, migration, monitoring, and alarming capabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - API Management
  - Federated API Management
  - Governance
  - Layer7
url: https://raw.githubusercontent.com/api-evangelist/apiida/refs/heads/main/apis.yml
created: '2025-01-08'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apiida:api-control-plane
    name: APIIDA API Control Plane
    description: REST API for the APIIDA API Control Plane, enabling programmatic management of APIs across multiple API gateways. Supports validation of proxy specifications, API version management, and deployment to gateways from a central federated control plane.
    humanURL: https://apiida.com/product/apiida-api-control-plane/
    baseURL: https://api.apiida.com
    tags:
      - API Lifecycle
      - API Management
      - Federated Control Plane
      - Governance
    properties:
      - type: Documentation
        url: https://apiida.com/product/apiida-api-control-plane/
      - type: OpenAPI
        url: openapi/apiida-api-control-plane-openapi.yml
      - type: JSONSchema
        url: json-schema/apiida-api.json
      - type: JSONSchema
        url: json-schema/apiida-deployment.json
      - type: JSON-LD
        url: json-ld/apiida-context.jsonld
  - aid: apiida:api-gateway-manager
    name: APIIDA API Gateway Manager
    description: REST API for the APIIDA API Gateway Manager, enabling programmatic management of Broadcom Layer7 API gateways. Supports gateway registration, API deployment and migration, monitoring and metrics collection, and alarm configuration across managed gateway instances.
    humanURL: https://apiida.com/product/apiida-api-gateway-manager/
    baseURL: https://api.apiida.com
    tags:
      - API Deployments
      - API Gateway
      - Layer7
      - Monitoring
    properties:
      - type: Documentation
        url: https://apiida.com/product/apiida-api-gateway-manager/
      - type: Documentation
        url: https://apiida.atlassian.net/wiki/spaces/AAGM
      - type: OpenAPI
        url: openapi/apiida-api-gateway-manager-openapi.yml
      - type: JSONSchema
        url: json-schema/apiida-gateway.json
      - type: JSONSchema
        url: json-schema/apiida-deployment.json
      - type: JSON-LD
        url: json-ld/apiida-context.jsonld
common:
  - type: Website
    url: https://apiida.com/
  - type: Documentation
    url: https://apiida.atlassian.net/wiki/spaces/AAGM
  - type: Support
    url: https://apiida.com/support/?lang=en
  - type: GitHubOrganization
    url: https://github.com/apiida
  - type: Features
    data:
      - name: Federated API Control Plane
        description: Centrally discover, govern, and provision APIs across multiple API gateway vendors from a single control plane.
      - name: Multi-Gateway Support
        description: Manage APIs across heterogeneous gateway environments including Broadcom Layer7, AWS API Gateway, Azure APIM, and others.
      - name: API Deployment Automation
        description: Automate API deployments and migrations across gateway instances with version management and rollback.
      - name: Monitoring and Alarming
        description: Collect gateway metrics and configure alarms for proactive API operations management.
      - name: Proxy Specification Validation
        description: Validate API proxy specifications before deployment to ensure compatibility and standards compliance.
  - type: UseCases
    data:
      - name: Enterprise API Governance
        description: Govern APIs across multiple teams and gateway technologies from a centralized control plane.
      - name: Gateway Migration
        description: Migrate APIs between gateway vendors with automated tooling and compatibility validation.
      - name: Layer7 Operations Automation
        description: Automate routine Broadcom Layer7 gateway operations including deployments, monitoring, and alarming.
      - name: Multi-Vendor API Management
        description: Unify API management operations across heterogeneous gateway infrastructure.
  - type: Solutions
    data:
      - name: API Control Plane
        description: Central API management and governance for multi-vendor API gateway environments.
      - name: API Gateway Manager
        description: Automated operations management for Broadcom Layer7 API gateway environments.
      - name: Enterprise
        description: Custom licensing with dedicated support for large-scale federated API management deployments.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
