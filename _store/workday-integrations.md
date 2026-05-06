---
aid: workday-integrations
name: Workday Integrations
description: Workday provides cloud-based enterprise software for finance, HR, and planning. This APIs.json file describes the integration capabilities and APIs available for connecting Workday with other systems.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2025-03-15'
modified: '2026-03-16'
specificationVersion: '0.19'
url: https://raw.githubusercontent.com/api-evangelist/workday-integrations/refs/heads/main/apis.yml
apis:
  - name: Workday REST API
    description: Modern REST API for accessing Workday business objects including employees, organizations, positions, and more.
    image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
    tags:
      - Enterprise
      - Finance
      - HR
      - REST
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/restapi/openapi.json
      - type: Authentication
        url: https://doc.workday.com/admin-guide/en-us/workday-rest-api/workday-rest-api-authentication.html
      - type: Rate Limits
        url: https://doc.workday.com/admin-guide/en-us/workday-rest-api/workday-rest-api-rate-limiting.html
      - type: OpenAPI
        url: openapi/workday-integrations-rest-api-openapi.yml
    contact:
      - FN: Workday Support
        email: support@workday.com
        url: https://www.workday.com/en-us/customer-experience/support.html
  - name: Workday SOAP Web Services
    description: Comprehensive SOAP-based web services for deep integration with Workday including Human Capital Management, Financial Management, and custom integrations.
    image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service/{tenant}
    tags:
      - Finance
      - HCM
      - Integration
      - SOAP
      - Web Services
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
      - type: WSDL
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/versions.html
      - type: Authentication
        url: https://doc.workday.com/admin-guide/en-us/integration/web-services/web-services-authentication.html
      - type: Integration Guide
        url: https://doc.workday.com/admin-guide/en-us/integration/integration-overview.html
    contact:
      - FN: Workday Support
        email: support@workday.com
        url: https://www.workday.com/en-us/customer-experience/support.html
  - name: Workday RaaS (Report-as-a-Service)
    description: Access custom and standard Workday reports as web services, enabling report data to be consumed by external systems.
    image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
    humanURL: https://doc.workday.com/admin-guide/en-us/integration/workday-reports/report-as-a-service-raas.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service/customreport2/{tenant}
    tags:
      - Analytics
      - Custom Reports
      - Data Export
      - Reports
    properties:
      - type: Documentation
        url: https://doc.workday.com/admin-guide/en-us/integration/workday-reports/report-as-a-service-raas.html
      - type: Tutorial
        url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/CIe8xMH~H~b1Cq7IqRfGHQ
      - type: Authentication
        url: https://doc.workday.com/admin-guide/en-us/integration/web-services/web-services-authentication.html
      - type: OpenAPI
        url: openapi/workday-integrations-raas-openapi.yml
    contact:
      - FN: Workday Support
        email: support@workday.com
  - name: Workday Prism Analytics API
    description: API for loading external data into Workday Prism Analytics for advanced reporting and analytics capabilities.
    image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
    humanURL: https://doc.workday.com/admin-guide/en-us/workday-prism-analytics/workday-prism-analytics-api.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/prismAnalytics/v2/{tenant}
    tags:
      - Analytics
      - Data Loading
      - External Data
      - Prism
    properties:
      - type: Documentation
        url: https://doc.workday.com/admin-guide/en-us/workday-prism-analytics/workday-prism-analytics-api.html
      - type: API Reference
        url: https://community.workday.com/sites/default/files/file-hosting/prism-analytics-api/index.html
      - type: Authentication
        url: https://doc.workday.com/admin-guide/en-us/workday-rest-api/workday-rest-api-authentication.html
      - type: OpenAPI
        url: openapi/workday-integrations-prism-analytics-openapi.yml
    contact:
      - FN: Workday Support
        email: support@workday.com
common:
  - type: Developer Portal
    url: https://community.workday.com/developer
  - type: Authentication Guide
    url: https://doc.workday.com/admin-guide/en-us/integration/integration-security/authentication-overview.html
  - type: Integration Cloud Platform
    url: https://www.workday.com/en-us/products/platform-product-extensions/workday-integration-cloud.html
  - type: Studio
    url: https://doc.workday.com/admin-guide/en-us/integration/workday-studio/workday-studio-overview.html
  - type: Community
    url: https://community.workday.com/
  - type: Support
    url: https://www.workday.com/en-us/customer-experience/support.html
  - type: Status Page
    url: https://status.workday.com/
  - type: Terms of Service
    url: https://www.workday.com/en-us/legal.html
  - type: Privacy Policy
    url: https://www.workday.com/en-us/privacy.html
  - type: JSON-LD
    url: json-ld/workday-integrations-context.jsonld
  - type: JSONSchema
    url: json-schema/workday-integrations-worker-schema.json
  - type: JSONSchema
    url: json-schema/workday-integrations-organization-schema.json
  - type: JSONSchema
    url: json-schema/workday-integrations-position-schema.json
  - type: JSONSchema
    url: json-schema/workday-integrations-compensation-schema.json
  - type: JSONSchema
    url: json-schema/workday-integrations-dataset-schema.json
  - type: Spectral Rules
    url: rules/workday-integrations-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/workforce-data-integration.yaml
  - type: Vocabulary
    url: vocabulary/workday-integrations-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
tags:
  - Cloud
  - Enterprise Software
  - ERP
  - Finance
  - HCM
  - HR
  - Integration
---
