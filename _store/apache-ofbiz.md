---
aid: apache-ofbiz
name: Apache OFBiz
description: Apache OFBiz is an open-source enterprise resource planning (ERP) system providing a suite of integrated business applications for CRM, e-commerce, supply chain management, manufacturing, accounting, order management, inventory, and warehousing. Built on a service-oriented architecture with a service engine, entity engine, and widget framework, OFBiz exposes a REST API plugin allowing any exported service to be invoked via JWT- authenticated HTTP endpoints. Governed by the Apache Software Foundation under the Apache License 2.0. Written in Java with Groovy scripting support.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - ERP
  - CRM
  - E-Commerce
  - Business Applications
  - Apache
  - Java
  - Open Source
  - Supply Chain
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-ofbiz:apache-ofbiz-rest-api
    name: Apache OFBiz REST API
    description: REST API plugin for Apache OFBiz that exposes any exported OFBiz service as a RESTful endpoint. Clients authenticate via HTTP Basic Auth to obtain a JWT token, then invoke services via GET (with URL-encoded JSON parameters) or POST (with JSON request body). Swagger UI is available at /docs/swagger-ui.html when the plugin is installed.
    humanURL: https://github.com/apache/ofbiz-plugins/tree/trunk/rest-api
    baseURL: https://localhost:8443/rest
    tags:
      - REST
      - JWT
      - Service Engine
      - ERP
    properties:
      - type: Documentation
        url: https://github.com/apache/ofbiz-plugins/blob/trunk/rest-api/src/docs/asciidoc/rest-api.adoc
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/openapi/apache-ofbiz-rest-api-openapi.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/json-schema/apache-ofbiz-token-response-schema.json
        title: Token Response Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/json-schema/apache-ofbiz-service-entry-schema.json
        title: Service Entry Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/json-schema/apache-ofbiz-service-response-schema.json
        title: Service Response Schema
common:
  - type: GitHubRepository
    url: https://github.com/apache/ofbiz-framework
    title: Apache OFBiz Framework GitHub Repository
  - type: GitHubOrganization
    url: https://github.com/apache
    title: Apache Software Foundation GitHub
  - type: Documentation
    url: https://ofbiz.apache.org/documentation.html
    title: Apache OFBiz Documentation
  - type: GettingStarted
    url: https://nightlies.apache.org/ofbiz/stable/ofbiz/html5/developer-manual.html
    title: OFBiz Developer Manual
  - type: Tutorials
    url: https://cwiki.apache.org/confluence/display/OFBIZ/Home
    title: OFBiz Wiki
  - type: FAQ
    url: https://ofbiz.apache.org/faqs.html
    title: Apache OFBiz FAQs
  - type: ReleaseNotes
    url: https://github.com/apache/ofbiz-framework/blob/trunk/CHANGELOG.md
    title: OFBiz Release Notes
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
    title: Apache License 2.0
  - type: Support
    url: https://ofbiz.apache.org/mailing-lists.html
    title: Mailing Lists
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/ofbiz
    title: OFBiz on Stack Overflow
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/rules/apache-ofbiz-spectral-rules.yml
    title: Apache OFBiz Spectral Rules
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/capabilities/apache-ofbiz-erp-operations.yaml
    title: Apache OFBiz ERP Operations
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/vocabulary/apache-ofbiz-vocabulary.yaml
    title: Apache OFBiz Vocabulary
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/json-ld/apache-ofbiz-context.jsonld
    title: Apache OFBiz JSON-LD Context
  - type: Features
    data:
      - name: Service-Oriented Architecture
        description: All business logic encapsulated in services accessible via multiple protocols including REST, XML-RPC, and Java.
      - name: REST API Plugin
        description: Plugin enabling any exported OFBiz service to be invoked via RESTful HTTP endpoints with JWT authentication.
      - name: JWT Authentication
        description: OAuth2-compatible JWT-based authentication with access tokens and refresh tokens for secure API access.
      - name: Entity Engine
        description: Flexible data access layer supporting multiple databases with entity-based query API and relationship management.
      - name: Service Engine
        description: Central business logic executor with transaction management, error handling, and event-driven service chaining.
      - name: Swagger UI Integration
        description: Built-in Swagger/OpenAPI UI at /docs/swagger-ui.html for API exploration and testing when REST plugin is deployed.
      - name: Groovy Scripting
        description: Groovy scripting support for service implementations and customizations without Java compilation.
      - name: Plugin Architecture
        description: Modular plugin system allowing feature extension without modifying core framework code.
      - name: Multi-Module ERP
        description: Integrated modules for accounting, order management, inventory, manufacturing, CRM, e-commerce, and HR.
      - name: Widget Framework
        description: XML-based UI component framework for building consistent web interfaces across ERP modules.
  - type: UseCases
    data:
      - name: ERP System Integration
        description: Integrate external systems (CRM, WMS, payment processors) with OFBiz via REST API service calls.
      - name: E-Commerce Backend
        description: Use OFBiz as a headless e-commerce backend with product catalog, pricing, order management, and fulfillment services.
      - name: Supply Chain Automation
        description: Automate supply chain workflows including purchase orders, inventory updates, and supplier communications via REST services.
      - name: Accounting Automation
        description: Automate accounting entries, invoicing, AR/AP processing, and financial reporting via OFBiz service API.
      - name: Manufacturing Operations
        description: Manage manufacturing resource planning, work orders, bill of materials, and production scheduling via OFBiz services.
      - name: Custom Business Workflows
        description: Build custom business process automations by chaining OFBiz services via the REST API.
  - type: Integrations
    data:
      - name: Apache Solr
        description: Integration for product and content search indexing across OFBiz data.
      - name: Groovy
        description: Groovy scripting engine integration for service implementations and data transformations.
      - name: PostgreSQL
        description: Supported relational database backend via the OFBiz entity engine.
      - name: MySQL
        description: Supported relational database backend for OFBiz data persistence.
      - name: Docker
        description: Official Docker support for containerized OFBiz deployments.
      - name: Swagger UI
        description: OpenAPI documentation and testing interface bundled with the REST API plugin.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
