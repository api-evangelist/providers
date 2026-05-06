---
aid: infor
url: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/apis.yml
apis:
  - aid: infor:infor-ion-api-gateway
    name: Infor ION API Gateway
    tags:
      - Cloud
      - ERP
      - Integration
      - Middleware
      - OAuth2
    image: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/image.png
    humanURL: https://www.infor.com/products/ion
    baseURL: https://mingledev01-ionapi.mingle.infor.com
    properties:
      - url: https://www.infor.com/products/ion
        type: Documentation
      - url: https://github.com/infor-cloud/ion-api-sdk
        type: SDKs
      - url: https://github.com/infor-cloud/ion-api-sdk
        type: Getting Started
      - url: https://github.com/infor-cloud/ion-api-sdk
        type: Authentication
      - url: openapi/infor-ion-api-gateway-openapi.yml
        type: OpenAPI
      - url: asyncapi/infor-ion-events-asyncapi.yml
        type: AsyncAPI
    description: The Infor ION API Gateway provides a managed OAuth 2.0 API layer for integrating Infor CloudSuite applications with third-party systems. The gateway supports Authorization Code, Client Credentials, and SAML Bearer grant types with SDKs available for Java, .NET, and Go.
  - aid: infor:infor-m3-api
    name: Infor M3 / LN CloudSuite Industrial API
    tags:
      - Cloud
      - ERP
      - M3
      - Manufacturing
      - Supply Chain
    image: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/image.png
    humanURL: https://www.infor.com/
    baseURL: https://api.infor.com
    properties:
      - url: https://www.infor.com/
        type: Documentation
      - url: https://github.com/infor-cloud/m3-h5-sdk
        type: SDKs
    description: The Infor M3 (CloudSuite Industrial) APIs provide access to production orders, inventory management, supply chain planning, and financial data for discrete and process manufacturing enterprises. The M3 H5 SDK enables HTML5-based application development on the M3 platform.
  - aid: infor:infor-xtendm3-api
    name: Infor XtendM3 API
    tags:
      - ERP
      - Extension
      - Java
      - M3
      - Manufacturing
    image: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/image.png
    humanURL: https://www.infor.com/
    baseURL: https://api.infor.com
    properties:
      - url: https://www.infor.com/
        type: Documentation
      - url: https://github.com/infor-cloud/xtendm3-sdk-java
        type: SDKs
      - url: https://github.com/infor-cloud/xtendm3-extension-examples
        type: Getting Started
    description: Infor XtendM3 provides a Java SDK for extending and customizing Infor M3 (CloudSuite Industrial) business logic without modifying core code. Extensions are deployed and executed within the M3 runtime environment.
  - aid: infor:infor-cloudsuite-financials-api
    name: Infor CloudSuite Financials API
    tags:
      - Accounting
      - Cloud
      - ERP
      - Financials
    image: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/image.png
    humanURL: https://www.infor.com/
    baseURL: https://api.infor.com
    properties:
      - url: https://www.infor.com/
        type: Documentation
    description: Infor CloudSuite Financials APIs provide integration with general ledger, accounts payable, accounts receivable, cash management, and financial reporting for enterprise finance operations.
common:
  aid: infor
  name: Infor
  description: Infor provides industry-specific cloud ERP platforms including CloudSuite Industrial (M3), CloudSuite Financials, and Infor LN. The Infor ION API Gateway enables OAuth 2.0-based integration across Infor applications and third-party systems. SDKs are available via the infor-cloud GitHub organization for Java, .NET, Go, and HTML5 development.
  image: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/image.png
  tags:
    - ERP
    - Manufacturing
    - Supply Chain
    - Cloud
    - Integration
  properties:
    - url: https://www.infor.com/
      type: Portal
    - url: https://www.infor.com/
      type: Documentation
    - url: https://github.com/infor-cloud/ion-api-sdk
      type: Getting Started
    - url: https://github.com/infor-cloud/ion-api-sdk
      type: Authentication
    - url: https://www.infor.com/en/about/legal
      type: Terms of Service
    - url: https://www.infor.com/en/about/privacy
      type: Privacy Policy
    - url: https://www.infor.com/blog
      type: Blog
    - url: https://www.infor.com/
      type: Website
    - url: https://github.com/infor-cloud
      type: GitHub Organization
    - url: https://github.com/infor-cloud/ion-api-sdk
      type: SDKs
    - url: openapi/infor-ion-api-gateway-openapi.yml
      type: OpenAPI
    - url: json-schema/infor-m3-customer-schema.json
      type: JSONSchema
    - url: json-ld/infor-context.jsonld
      type: JSONLDContext
    - url: asyncapi/infor-ion-events-asyncapi.yml
      type: AsyncAPI
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
modified: '2026-04-28'
description: Infor is a global enterprise software company that builds business cloud software specialized by industry, including ERP, supply chain, finance, human capital management, and customer experience applications.
---
