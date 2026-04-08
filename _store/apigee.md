---
aid: apigee
url: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/apis.yml
apis:
- name: Apigee API Management
  description: APIs for programmatically managing Apigee organizations, API proxies, products, developers, apps, environments, deployments, and analytics. Provides full lifecycle management of APIs on the Apigee platform.
  image: https://www.apigee.com/about/sites/default/files/apigee-logo.png
  humanURL: https://cloud.google.com/apigee/docs
  baseURL: https://apigee.googleapis.com
  tags:
  - Analytics
  - API Management
  - API Proxies
  - Developers
  - Environments
  properties:
  - type: Documentation
    url: https://cloud.google.com/apigee/docs/api-platform/get-started/what-apigee
  - type: OpenAPI
    url: openapi/apigee-api-management-openapi.yml
  - type: JSONSchema
    url: json-schema/apigee-organization-schema.json
  - type: JSONSchema
    url: json-schema/apigee-api-proxy-schema.json
  - type: JSONSchema
    url: json-schema/apigee-api-product-schema.json
  - type: JSONSchema
    url: json-schema/apigee-developer-schema.json
  - type: JSONSchema
    url: json-schema/apigee-developer-app-schema.json
  - type: JSONSchema
    url: json-schema/apigee-environment-schema.json
  - type: JSONSchema
    url: json-schema/apigee-deployment-schema.json
  - type: Authentication
    url: https://cloud.google.com/apigee/docs/api-platform/system-administration/auth-tools
  - type: Pricing
    url: https://cloud.google.com/apigee/pricing
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/apigee/support
  - type: Getting Started
    url: https://cloud.google.com/apigee/docs/api-platform/get-started/overview
  - type: SDKs
    url: https://cloud.google.com/apigee/docs/api-platform/reference/apis
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://cloud.google.com/terms/cloud-privacy-notice
  - type: API Reference
    url: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest
  - type: Tutorials
    url: https://cloud.google.com/apigee/docs/api-platform/get-started/tutorials
  - type: Release Notes
    url: https://cloud.google.com/apigee/docs/release-notes
  - type: Quickstart
    url: https://cloud.google.com/apigee/docs/api-platform/get-started/get-started
  - type: Change Log
    url: https://cloud.google.com/apigee/docs/release/release-notes
- name: Apigee API Hub API
  description: API for cataloging, organizing, and governing APIs across an organization. Enables API discovery, metadata management, dependency mapping, deployment tracking, and AI-powered specification boost.
  image: https://www.apigee.com/about/sites/default/files/apigee-logo.png
  humanURL: https://cloud.google.com/apigee/docs/apihub/what-is-api-hub
  baseURL: https://apihub.googleapis.com
  tags:
  - API Catalog
  - API Discovery
  - API Governance
  - Metadata
  - Specifications
  properties:
  - type: Documentation
    url: https://cloud.google.com/apigee/docs/apihub/what-is-api-hub
  - type: OpenAPI
    url: openapi/apigee-api-hub-openapi.yml
  - type: API Reference
    url: https://cloud.google.com/apigee/docs/reference/apis/apihub/rest
  - type: Quickstart
    url: https://cloud.google.com/apigee/docs/apihub/quickstart-intro
  - type: Release Notes
    url: https://cloud.google.com/apigee/docs/apihub/release-notes
  - type: Pricing
    url: https://cloud.google.com/apigee/pricing
  - type: Support
    url: https://cloud.google.com/apigee/support
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://cloud.google.com/terms/cloud-privacy-notice
  - type: SDKs
    url: https://cloud.google.com/apigee/docs/apihub/libraries
- name: Apigee Integrations API
  description: API for creating, managing, and executing integrations within Google Cloud. Supports authentication, certificate management, scheduled execution, and connectors for third-party services.
  image: https://www.apigee.com/about/sites/default/files/apigee-logo.png
  humanURL: https://cloud.google.com/apigee/docs/api-platform/integration/using-application-integration
  baseURL: https://integrations.googleapis.com
  tags:
  - Automation
  - Cloud Services
  - Connectors
  - Integrations
  - Workflows
  properties:
  - type: Documentation
    url: https://cloud.google.com/apigee/docs/api-platform/integration/using-application-integration
  - type: OpenAPI
    url: openapi/apigee-integrations-openapi.yml
  - type: JSONSchema
    url: json-schema/apigee-integration-schema.json
  - type: API Reference
    url: https://cloud.google.com/apigee/docs/reference/apis/integrations/rest
  - type: Tutorials
    url: https://cloud.google.com/apigee/docs/api-platform/integration/tutorials
  - type: Pricing
    url: https://cloud.google.com/apigee/pricing
  - type: Support
    url: https://cloud.google.com/apigee/support
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://cloud.google.com/terms/cloud-privacy-notice
  - type: Getting Started
    url: https://cloud.google.com/apigee/docs/api-platform/connectors/get-started-connectors
- name: Apigee API Management API
  description: API for discovering and observing shadow APIs in existing Google Cloud infrastructure, enabling organizations to identify undocumented or unmanaged APIs operating within their environments.
  image: https://www.apigee.com/about/sites/default/files/apigee-logo.png
  humanURL: https://cloud.google.com/apigee/docs/reference/apis/apim/rest
  baseURL: https://apim.googleapis.com
  tags:
  - API Discovery
  - API Governance
  - API Observation
  - Security
  - Shadow APIs
  properties:
  - type: Documentation
    url: https://cloud.google.com/apigee/docs/reference/apis/apim/rest
  - type: OpenAPI
    url: openapi/apigee-apim-openapi.yml
  - type: API Reference
    url: https://cloud.google.com/apigee/docs/reference/apis/apim/rest
  - type: Pricing
    url: https://cloud.google.com/apigee/pricing
  - type: Support
    url: https://cloud.google.com/apigee/support
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://cloud.google.com/terms/cloud-privacy-notice
- name: Apigee Registry API
  description: API for tracking and managing machine-readable descriptions of APIs, including specifications, versions, deployments, and related metadata. This is a legacy API and Google recommends using the Apigee API Hub APIs instead.
  image: https://www.apigee.com/about/sites/default/files/apigee-logo.png
  humanURL: https://cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest
  baseURL: https://apigeeregistry.googleapis.com
  tags:
  - API Catalog
  - API Registry
  - API Specifications
  - Legacy
  - Metadata
  properties:
  - type: Documentation
    url: https://cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest
  - type: OpenAPI
    url: openapi/apigee-registry-openapi.yml
  - type: API Reference
    url: https://cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest
  - type: GitHub
    url: https://github.com/apigee/registry
  - type: Release Notes
    url: https://cloud.google.com/apigee/docs/registry/release-notes
  - type: Pricing
    url: https://cloud.google.com/apigee/pricing
  - type: Support
    url: https://cloud.google.com/apigee/support
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://cloud.google.com/terms/cloud-privacy-notice
name: Apigee
tags:
- Analytics
- API Gateway
- API Governance
- API Hub
- API Management
- Developer Portal
- Enterprise
- Hybrid
- Integrations
- Microservices
- Monetization
type: Contract
image: https://www.apigee.com/about/sites/default/files/apigee-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Apigee is Google Cloud's native API management platform for building, managing, and securing APIs across any use case, environment, or scale. It provides API proxies, security, rate limiting, quotas, analytics, monetization, and developer portal capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

