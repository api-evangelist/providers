---
aid: workday-studio
url: https://raw.githubusercontent.com/api-evangelist/workday-studio/refs/heads/main/apis.yml
apis:
- name: Workday Studio Integration API
  description: API for building and deploying custom integrations using Workday Studio, an Eclipse-based IDE that provides a graphical development environment with drag-and-drop reusable components for creating sophisticated integrations with flow control, data transformation, error handling, and scripting.
  image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
  humanUrl: https://doc.workday.com/
  baseUrl: https://{tenant}.workday.com/ccx/service
  tags:
  - Custom
  - Development
  - Integration
  properties:
  - type: Documentation
    url: https://doc.workday.com/reader/wsiU0cnNjCc_k7shLNxLEA/HdIduH8HQGat1qdv1nXNVQ
  - type: OpenAPI
    url: https://community.workday.com/api-specifications
  - type: Swagger
    url: https://community.workday.com/api-specifications
  - type: Authentication
    url: https://doc.workday.com/reader/wsiU0cnNjCc_k7shLNxLEA/rvVKnUi_v3MwKZ1VqF_1Jw
  - type: Getting Started
    url: https://doc.workday.com/reader/wsiU0cnNjCc_k7shLNxLEA/z~y4T3OBwNz42E1hT8azSA
  - type: SDK
    url: https://doc.workday.com/reader/wsiU0cnNjCc_k7shLNxLEA/HdIduH8HQGat1qdv1nXNVQ
  - type: Reference
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Integrations/v17/Integrations.html
- name: Workday Web Services API
  description: SOAP and REST web services for integrating with Workday applications, providing programmatic access to business management services with WSDL and XML Schema definitions across 55 service areas including Human Resources, Payroll, Benefits, and Financial Management.
  image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
  humanUrl: https://doc.workday.com/
  baseUrl: https://{tenant}.workday.com/ccx/service/{tenant}
  tags:
  - Enterprise
  - REST
  - SOAP
  - Web Services
  properties:
  - type: Documentation
    url: https://doc.workday.com/reader/J1YvL9yFQMumSgoRA4j4bA/root
  - type: WSDL
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/
  - type: API Reference
    url: https://community.workday.com/api
  - type: Rate Limits
    url: https://doc.workday.com/reader/J1YvL9yFQMumSgoRA4j4bA/L~jJl~pFV91hFVm2h3UFWQ
  - type: Reference
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
- name: Workday REST API
  description: RESTful API providing modern JSON-based access to Workday data and services. Uses OAuth 2.0 authentication and standard HTTP methods for operations across HCM, financial management, recruiting, payroll, and other Workday domains.
  image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
  humanUrl: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
  baseUrl: https://{tenant}.workday.com/ccx/api
  tags:
  - Data Access
  - JSON
  - OAuth
  - REST
  properties:
  - type: Documentation
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
  - type: Reference
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
  - type: Authentication
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html#authentication
- name: Workday Custom Reports API
  description: API for creating and executing custom reports built in Workday Studio. Exposes custom reports as RESTful web services through Report-as-a-Service (RaaS), enabling programmatic access to report data with support for query parameters and multiple output formats.
  image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
  humanUrl: https://doc.workday.com/
  baseUrl: https://{tenant}.workday.com/ccx/service/customreport2/{tenant}
  tags:
  - Analytics
  - Custom
  - Report as a Service
  - Reports
  properties:
  - type: Documentation
    url: https://doc.workday.com/reader/J1YvL9yFQMumSgoRA4j4bA/ziYjYJxh2YKGvz8I5V46bQ
  - type: Tutorial
    url: https://doc.workday.com/reader/wsiU0cnNjCc_k7shLNxLEA/kPBEj3_Lz04YDSUvAEKl4w
- name: Workday Orchestrate API
  description: Low-code integration and automation platform for building event-driven and batch integrations using a visual drag-and-drop builder. Enables developers to create workflows that connect Workday with external systems, automate business processes, and handle real-time data synchronization.
  image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
  humanUrl: https://www.workday.com/en-us/products/platform-product-extensions/integrations.html
  baseUrl: https://{tenant}.workday.com/ccx/api
  tags:
  - Automation
  - Event Driven
  - Low Code
  - Orchestration
  - Workflows
  properties:
  - type: Documentation
    url: https://www.workday.com/en-us/products/platform-product-extensions/integrations.html
name: Workday Studio
tags:
- Cloud
- Development
- Enterprise
- Finance
- HR
- IDE
- Integration
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Workday Studio is an integrated development environment (IDE) for building custom integrations and applications on the Workday platform. It provides tools for creating web services, custom reports, and integration solutions.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

