---
aid: productiv
name: Productiv
description: The SaaS Management Platform that delivers the industrys most comprehensive view of your SaaS portfolio with deep usage analytics, spend data, and feature-level insights to power the technology decisions that support your business.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Application Portfolio
  - Provisioning
  - SaaS Management
  - Spend Management
  - Usage Analytics
created: '2025-07-11'
modified: '2026-04-18'
url: https://raw.githubusercontent.com/api-evangelist/productiv/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: productiv:developer-api
    name: Productiv Developer API
    description: The Productiv Developer APIs support integrating custom applications into the Productiv platform, allowing external developers to define and publish new connected applications. Includes APIs for pushing usage events and user information, Data Export APIs for fetching app portfolio details, provisioning workflows, and audit events.
    humanURL: https://docs.app.productiv.com/developer-api/index.html
    baseURL: https://public-api.productiv.com
    tags:
      - Application Portfolio
      - Audit Events
      - Data Export
      - Provisioning
      - SaaS Management
      - Spend Data
      - Usage Analytics
    properties:
      - type: Documentation
        url: https://docs.app.productiv.com/developer-api/index.html
      - type: OpenAPI
        url: openapi/productiv-developer-openapi.yml
      - type: Authentication
        url: https://docs.app.productiv.com/developer-api/authorization.html
      - type: GettingStarted
        url: https://docs.app.productiv.com/developer-api/data-export-getting-started.html
      - type: JSONSchema
        url: json-schema/application.json
      - type: JSONSchema
        url: json-schema/app-summary.json
      - type: JSONSchema
        url: json-schema/app-details.json
      - type: JSONSchema
        url: json-schema/usage-event.json
      - type: JSONSchema
        url: json-schema/spend-data.json
      - type: JSONSchema
        url: json-schema/provisioned-user.json
      - type: JSONSchema
        url: json-schema/org-chart-user.json
      - type: JSONSchema
        url: json-schema/provisioning-workflow.json
      - type: JSONSchema
        url: json-schema/audit-event.json
      - type: JSONLD
        url: json-ld/productiv-context.jsonld
common:
  - url: https://docs.app.productiv.com/
    name: Documentation
    type: Documentation
    description: 'null'
  - url: https://productiv.com/
    name: Website
    type: DeveloperPortal
    description: 'null'
  - url: https://docs.app.productiv.com/developer-api/authorization.html
    name: Authentication
    type: Authentication
    description: 'null'
  - name: Features
    type: Features
    data:
      - name: SaaS Portfolio Management
      - name: Usage Analytics
      - name: Spend Data Tracking
      - name: Provisioning Workflows
      - name: Audit Events
      - name: Org Chart Integration
      - name: Custom Application Connectors
      - name: Batch File Upload
      - name: Data Export
      - name: OAuth2 Authentication
  - name: Use Cases
    type: UseCases
    data:
      - name: Track SaaS Application Usage
      - name: Optimize Software Spend
      - name: Automate User Provisioning
      - name: Audit Platform Activity
      - name: Integrate Custom Applications
      - name: Export App Portfolio Data
  - name: Integrations
    type: Integrations
    data:
      - name: Okta
      - name: Azure Active Directory
      - name: Salesforce
      - name: ServiceNow
      - name: Workday
      - name: Slack
  - url: rules/productiv-spectral-rules.yml
    type: Rules
  - url: vocabulary/productiv-vocabulary.yaml
    type: Vocabulary
  - url: capabilities/shared/developer-api.yaml
    type: Capabilities
  - url: capabilities/saas-management.yaml
    type: Capabilities
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
