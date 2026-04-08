---
aid: informatica
url: https://raw.githubusercontent.com/api-evangelist/informatica/refs/heads/main/apis.yml
apis:
- aid: informatica:informatica
  name: Informatica Platform REST API
  description: The Informatica Intelligent Cloud Services Platform REST API provides access to platform-level resources including login and authentication, roles and privileges, user and user group management, organizations, connections, schedules, runtime environments, Secure Agent services, object permissions, export and import, source control, projects and folders, licenses, metering data, and security logs. Supports version 2 (JSON and XML) and version 3 (JSON) resource formats.
  humanURL: https://docs.informatica.com/integration-cloud/cloud-platform/current-version/rest-api-reference/informatica-intelligent-cloud-services-rest-api.html
  tags:
  - Authentication
  - Platform
  - Roles
  - Users
  properties:
  - type: Documentation
    url: https://docs.informatica.com/integration-cloud/cloud-platform/current-version/rest-api-reference/informatica-intelligent-cloud-services-rest-api.html
  - type: Documentation
    url: https://docs.informatica.com/integration-cloud/b2b-gateway/current-version/rest-api-reference/platform-rest-api-version-3-resources.html
  - type: Documentation
    url: https://docs.informatica.com/integration-cloud/b2b-gateway/current-version/rest-api-reference/platform-rest-api-version-3-resources/roles.html
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/informatica/refs/heads/main/openapi/informatica-platform-rest-api-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/informatica/refs/heads/main/json-schema/informatica-connection-schema.json
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/informatica/refs/heads/main/json-ld/informatica-context.jsonld
- aid: informatica:data-integration-rest-api
  name: Informatica Data Integration REST API
  description: The Data Integration REST API provides programmatic access to manage data integration assets and operations, including connections, mappings, mapping tasks, dynamic mapping tasks, taskflows, code tasks, connectors, data preview, fields, file listeners, file transfer, and hierarchical mappers. Uses version 2 resources with JSON or XML format.
  humanURL: https://docs.informatica.com/integration-cloud/data-integration/current-version/rest-api-reference/data-integration-rest-api.html
  tags:
  - Connections
  - Data Integration
  - ETL
  - Mappings
  properties:
  - type: Documentation
    url: https://docs.informatica.com/integration-cloud/data-integration/current-version/rest-api-reference/data-integration-rest-api.html
  - type: Documentation
    url: https://docs.informatica.com/integration-cloud/data-integration/current-version/rest-api-reference/rest-api-resource-quick-references/data-integration-resource-quick-reference.html
- aid: informatica:cloud-data-governance-and-catalog-api
  name: Informatica Cloud Data Governance and Catalog API
  description: The Cloud Data Governance and Catalog API enables programmatic creation and management of assets, searching for assets, and viewing asset details within Informatica Data Governance and Catalog. Calls can be made using a REST client, the cURL tool, or a suitable programming interface.
  humanURL: https://docs.informatica.com/data-quality-cloud/cloud-data-governance-and-catalog/current-version.html
  tags:
  - Data Catalog
  - Data Governance
  properties:
  - type: Documentation
    url: https://docs.informatica.com/data-quality-cloud/cloud-data-governance-and-catalog/current-version.html
- aid: informatica:cloud-data-profiling-rest-api
  name: Informatica Cloud Data Profiling REST API
  description: The Cloud Data Profiling REST API allows interaction with the Data Profiling Service through API calls to create, delete, update, and run queries and profiles within your organization. Supports platform REST API version 2 and version 3 resources and service-specific resources.
  humanURL: https://docs.informatica.com/data-governance-and-quality-cloud/cloud-data-profiling/current-version/data-profiling/data-profiling/data-profiling-rest-api.html
  tags:
  - Data Profiling
  - Data Quality
  properties:
  - type: Documentation
    url: https://docs.informatica.com/data-governance-and-quality-cloud/cloud-data-profiling/current-version/data-profiling/data-profiling/data-profiling-rest-api.html
  - type: GettingStarted
    url: https://docs.informatica.com/data-governance-and-quality-cloud/cloud-data-profiling/h2l/1547-getting-started-with-cloud-data-profiling-rest-api/getting-started-with-cloud-data-profiling-rest-api/overview.html
- aid: informatica:cloud-address-verification-api
  name: Informatica Cloud Address Verification API
  description: The Cloud Address Verification API is a REST API-based solution for verifying and validating postal addresses in real time. You can integrate the Address Verification service API endpoints into your application using a REST client, the cURL tool, or any suitable programming interface.
  humanURL: https://docs.informatica.com/data-governance-and-quality-cloud/data-quality/current-version/cloud-address-verification-api/introduction.html
  tags:
  - Address Verification
  - Data Quality
  properties:
  - type: Documentation
    url: https://docs.informatica.com/data-governance-and-quality-cloud/data-quality/current-version/cloud-address-verification-api/introduction.html
- aid: informatica:b2b-gateway-rest-api
  name: Informatica B2B Gateway REST API
  description: The B2B Gateway REST APIs enable running inbound and outbound partner flows, querying the status of events, and getting control numbers for outbound EDI X12 and EDIFACT messages through programmatic API calls.
  humanURL: https://docs.informatica.com/ipaas/b2b-gateway/current-version/rest-api-reference/informatica-intelligent-cloud-services-rest-api.html
  tags:
  - B2B
  - EDI
  - Gateway
  properties:
  - type: Documentation
    url: https://docs.informatica.com/ipaas/b2b-gateway/current-version/rest-api-reference/informatica-intelligent-cloud-services-rest-api.html
- aid: informatica:reference-360-rest-api
  name: Informatica Reference 360 REST API
  description: The Reference 360 REST API enables programmatic management of reference data, including exporting and importing reference data sets, managing code values and value mappings, retrieving asset details, managing code lists, crosswalks, hierarchies, and audit trails. Supports multiple API versions for model import and export operations.
  humanURL: https://docs.informatica.com/master-data-management-cloud/reference-360/current-version/reference-360/reference-360-rest-api.html
  tags:
  - Master Data Management
  - Reference Data
  properties:
  - type: Documentation
    url: https://docs.informatica.com/master-data-management-cloud/reference-360/current-version/reference-360/reference-360-rest-api.html
name: Informatica
tags:
- Address Verification
- B2B Gateway
- Cloud Services
- Data Governance
- Data Integration
- Data Profiling
- Data Quality
- Enterprise Software
- ETL
- IDMC
- IICS
- Master Data Management
- Reference Data Management
type: Index
image: https://companieslogo.com/img/orig/INFA-3e1d4e5a.png
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-07'
position: Consumer
description: Collection of APIs for Informatica Intelligent Cloud Services (IICS) and Intelligent Data Management Cloud (IDMC), providing programmatic access to data integration, data governance, data quality, master data management, B2B gateway, and platform administration capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

