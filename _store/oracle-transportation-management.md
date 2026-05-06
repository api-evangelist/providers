---
aid: oracle-transportation-management
name: Oracle Transportation Management
description: Oracle Transportation Management (OTM) is a logistics platform delivered as part of Oracle Fusion Cloud Transportation and Global Trade Management. OTM APIs provide programmatic access to shipment orders, carriers, lanes, rates, transportation plans, and logistics data, plus table-centric data export for integration with reporting, analytics, and data warehouse systems.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/oracle-transportation-management/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Logistics
  - Transportation
  - Freight
  - Supply Chain
  - Shipping
  - Global Trade
  - Oracle
apis:
  - name: Oracle Transportation Management Business Object Resources REST API
    description: Oracle Transportation Management Business Object Resources REST API enables programmatic access to in-system data and integrations with shipment orders, carriers, lanes, rates, and transportation plans in Oracle Fusion Cloud Transportation and Global Trade Management.
    image: https://www.oracle.com/a/ocom/img/social-og-oracle-cloud.jpg
    humanURL: https://docs.oracle.com/en/cloud/saas/transportation/26b/otmra/index.html
    baseURL: https://{host}/GC3/glog.integration.servlet.WMServlet/otm/rest/v1
    tags:
      - Freight
      - Logistics
      - REST
      - Transportation
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/transportation/26b/otmra/index.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/transportation/26b/otmra/rest-endpoints.html
      - type: OpenAPI
        url: openapi/oracle-otm-business-objects-openapi.yml
  - name: Oracle Transportation Management Data Export REST API
    description: Oracle Transportation Management Data Export REST API facilitates table-centric data extraction and integration with external systems for reporting, analytics, and data warehouse use cases.
    image: https://www.oracle.com/a/ocom/img/social-og-oracle-cloud.jpg
    humanURL: https://docs.oracle.com/en/cloud/saas/transportation/26b/otmro/index.html
    tags:
      - Data Export
      - Logistics
      - REST
      - Transportation
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/transportation/26b/otmro/index.html
common:
  - type: Portal
    url: https://docs.oracle.com/en/cloud/saas/transport-management/
  - type: Documentation
    url: https://docs.oracle.com/en/cloud/saas/logistics-cloud-suite/index.html
  - type: Website
    url: https://www.oracle.com/scm/transportation-management/
  - type: Support
    url: https://support.oracle.com/portal/
  - type: Blog
    url: https://blogs.oracle.com/scm/
  - type: Privacy Policy
    url: https://www.oracle.com/legal/privacy/privacy-policy/
  - type: Terms of Service
    url: https://www.oracle.com/legal/terms/
  - type: Developer Portal
    url: https://www.oracle.com/developer/
  - type: GitHub Organization
    url: https://github.com/oracle
  - type: Status
    url: https://ocistatus.oraclecloud.com/
  - type: OpenAPI
    url: openapi/oracle-otm-business-objects-openapi.yml
  - type: JSON Schema
    url: json-schema/oracle-otm-shipment-order-schema.json
  - type: JSON-LD Context
    url: json-ld/oracle-otm-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
