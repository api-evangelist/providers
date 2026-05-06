---
name: Seismic
description: Seismic is the global leader in enablement, helping organizations engage customers, enable teams, and ignite revenue growth. The Seismic platform provides content management, learning and coaching, dynamic document generation, and buyer engagement capabilities through a comprehensive suite of APIs.
image: https://seismic.com/wp-content/uploads/2023/02/seismic-logo.svg
url: https://seismic.com
created: '2025-02-10'
modified: '2026-05-02'
specificationVersion: '0.18'
apis:
  - name: Seismic Content API
    description: API for managing and accessing content within the Seismic platform, including documents, presentations, folders, and other sales materials. Supports uploading, organizing, searching, delivering, and managing content items.
    image: https://seismic.com/wp-content/uploads/2023/02/seismic-logo.svg
    humanURL: https://seismic.com/products/content-management/
    baseURL: https://api.seismic.com/integration/v2
    tags:
      - Content
      - Content Management
      - Documents
      - Sales Enablement
    properties:
      - type: Documentation
        url: https://developer.seismic.com/seismicsoftware/reference/content-api
      - type: OpenAPI
        url: openapi/seismic-content-openapi.yml
      - type: Authentication
        url: https://developer.seismic.com/seismicsoftware/docs/authentication
      - type: JSONSchema
        url: json-schema/seismic-content-item-schema.json
      - type: JSONSchema
        url: json-schema/seismic-folder-schema.json
      - type: JSONStructure
        url: json-structure/seismic-content-item-structure.json
    contact:
      - FN: Seismic Support
        email: support@seismic.com
        url: https://seismic.com/support/
  - name: Seismic LiveDocs API
    description: API for creating and managing LiveDocs, Seismic's dynamic document generation solution. Enables automated creation of personalized proposals, presentations, and sales materials by merging CRM and other data into templates.
    image: https://seismic.com/wp-content/uploads/2023/02/seismic-logo.svg
    humanURL: https://seismic.com/products/livedocs/
    baseURL: https://api.seismic.com/integration/v2
    tags:
      - Document Generation
      - Dynamic Content
      - LiveDocs
      - Sales Enablement
    properties:
      - type: Documentation
        url: https://developer.seismic.com/seismicsoftware/reference/livedocs-api
      - type: OpenAPI
        url: openapi/seismic-livedocs-openapi.yml
      - type: JSONSchema
        url: json-schema/seismic-livedoc-template-schema.json
    contact:
      - FN: Seismic Support
        email: support@seismic.com
        url: https://seismic.com/support/
  - name: Seismic Analytics API
    description: API for accessing analytics and reporting data on content usage, user engagement, and sales effectiveness. Provides insights into content performance, user adoption, buyer engagement, and exportable reports.
    image: https://seismic.com/wp-content/uploads/2023/02/seismic-logo.svg
    humanURL: https://seismic.com/products/analytics/
    baseURL: https://api.seismic.com/integration/v2
    tags:
      - Analytics
      - Insights
      - Metrics
      - Reporting
    properties:
      - type: Documentation
        url: https://developer.seismic.com/seismicsoftware/reference/analytics-api
      - type: OpenAPI
        url: openapi/seismic-analytics-openapi.yml
    contact:
      - FN: Seismic Support
        email: support@seismic.com
        url: https://seismic.com/support/
  - name: Seismic User Management API
    description: API for managing users, groups, roles, teams, and permissions within the Seismic platform. Supports creating and organizing users, managing group hierarchies, assigning roles, and team structures for access control.
    image: https://seismic.com/wp-content/uploads/2023/02/seismic-logo.svg
    humanURL: https://seismic.com
    baseURL: https://api.seismic.com/integration/v2
    tags:
      - Administration
      - Groups
      - Permissions
      - Users
    properties:
      - type: Documentation
        url: https://developer.seismic.com/seismicsoftware/reference/user-management-api
      - type: OpenAPI
        url: openapi/seismic-user-management-openapi.yml
      - type: JSONSchema
        url: json-schema/seismic-user-schema.json
      - type: JSONSchema
        url: json-schema/seismic-group-schema.json
    contact:
      - FN: Seismic Support
        email: support@seismic.com
        url: https://seismic.com/support/
common:
  - type: Portal
    url: https://developer.seismic.com/
  - type: Getting Started
    url: https://developer.seismic.com/seismicsoftware/docs/getting-started
  - type: Authentication
    url: https://developer.seismic.com/seismicsoftware/docs/authentication
  - type: Rate Limits
    url: https://developer.seismic.com/seismicsoftware/docs/rate-limits
  - type: Webhooks
    url: https://developer.seismic.com/seismicsoftware/docs/webhooks
  - type: Support
    url: https://seismic.com/support/
  - type: Privacy Policy
    url: https://seismic.com/privacy-policy/
  - type: Terms of Service
    url: https://seismic.com/terms-of-service/
  - type: Status
    url: https://status.seismic.com/
  - type: Documentation
    url: https://developer.seismic.com/seismicsoftware/docs
  - type: Change Log
    url: https://developer.seismic.com/seismicsoftware/changelog
  - type: Website
    url: https://seismic.com
  - type: Blog
    url: https://seismic.com/resources/blog/
  - type: Login
    url: https://login.seismic.com/
  - type: SpectralRules
    url: rules/seismic-rules.yml
  - type: JSONLDContext
    url: json-ld/seismic-context.jsonld
  - type: Vocabulary
    url: vocabulary/seismic-vocabulary.yml
  - type: NaftikoCapabilities
    url: capabilities/content-management.yaml
  - type: NaftikoCapabilities
    url: capabilities/sales-enablement.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
