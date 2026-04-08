---
aid: seismic
url: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/apis.yml
apis:
- name: Seismic Content API
  description: API for managing and accessing content within the Seismic platform, including documents, presentations, and other sales materials.
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
  contact:
  - FN: Seismic Support
    email: support@seismic.com
    url: https://seismic.com/support/
- name: Seismic LiveDocs API
  description: API for creating and managing LiveDocs, Seismic's dynamic document generation solution.
  image: https://seismic.com/wp-content/uploads/2023/02/seismic-logo.svg
  humanURL: https://seismic.com/products/livedocs/
  baseURL: https://api.seismic.com/integration/v2
  tags:
  - Document Generation
  - Dynamic Content
  - LiveDocs
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
  description: API for accessing analytics and reporting data on content usage, user engagement, and sales effectiveness.
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
  description: API for managing users, groups, and permissions within the Seismic platform.
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
name: Seismic
tags:
- API
type: Contract
image: https://seismic.com/wp-content/uploads/2023/02/seismic-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Seismic is the global leader in enablement, helping organizations engage customers, enable teams, and ignite revenue growth. The Seismic platform provides content management, learning and coaching, and buyer engagement capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

