---
aid: magento
url: https://raw.githubusercontent.com/api-evangelist/magento/refs/heads/main/apis.yml
apis:
- aid: magento:rest-api
  name: Magento REST API
  tags:
  - Catalog
  - Customers
  - E-Commerce
  - Orders
  - Products
  - REST
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://your-store.example.com/rest
  humanURL: https://developer.adobe.com/commerce/webapi/rest/
  properties:
  - url: https://developer.adobe.com/commerce/webapi/rest/
    type: Documentation
  - url: https://developer.adobe.com/commerce/webapi/rest/reference/
    type: Documentation
  - url: openapi/magento-rest-api-openapi.yml
    type: OpenAPI
  description: 'The Adobe Commerce (Magento) REST API provides a comprehensive set of endpoints for interacting with all major aspects of an e-commerce store, including catalog management, orders, customers, inventory, shipping, and payments. It supports three authentication mechanisms: OAuth 1.0a for third-party integrations, token-based authentication for mobile apps and administrators, and guest access for select public endpoints.'
- aid: magento:graphql-api
  name: Magento GraphQL API
  tags:
  - Cart
  - Catalog
  - E-Commerce
  - GraphQL
  - Headless Commerce
  - Storefront
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://your-store.example.com/graphql
  humanURL: https://developer.adobe.com/commerce/webapi/graphql/
  properties:
  - url: https://developer.adobe.com/commerce/webapi/graphql/
    type: Documentation
  - url: https://developer.adobe.com/commerce/webapi/graphql/reference/
    type: Documentation
  description: The Adobe Commerce GraphQL API offers a flexible, query-driven interface designed primarily for building headless storefronts and progressive web applications. It exposes a single endpoint and allows clients to request exactly the data they need through queries and mutations covering catalog browsing, product search, cart management, checkout, customer accounts, and order history.
- aid: magento:soap-api
  name: Magento SOAP API
  tags:
  - E-Commerce
  - Integration
  - SOAP
  - Web Services
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://your-store.example.com/soap
  humanURL: https://developer.adobe.com/commerce/webapi/get-started/soap-web-api-calls/
  properties:
  - url: https://developer.adobe.com/commerce/webapi/get-started/soap-web-api-calls/
    type: Documentation
  - url: wsdl/magento-soap.wsdl
    type: WSDL
  description: The Adobe Commerce SOAP API exposes the same service contracts as the REST API through a WSDL 1.2 interface compliant with WS-I 2.0 Basic Profile. It allows enterprise systems and legacy integrations to interact with Adobe Commerce store data using standard SOAP tooling. Developers can retrieve the WSDL for any service or combination of services by appending query parameters to the SOAP endpoint URL.
- aid: magento:webhooks
  name: Adobe Commerce Webhooks
  tags:
  - E-Commerce
  - Events
  - Extensibility
  - Real-Time
  - Webhooks
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer.adobe.com/commerce/extensibility/webhooks/
  properties:
  - url: https://developer.adobe.com/commerce/extensibility/webhooks/
    type: Documentation
  - url: asyncapi/magento-webhooks-asyncapi.yml
    type: AsyncAPI
  description: Adobe Commerce Webhooks enable developers to configure synchronous HTTP callbacks that fire when specific events occur within a Commerce instance, allowing external systems to react in real time to store activity. Webhooks can intercept and modify request data before Commerce processes it, or trigger outbound notifications after an event completes.
- aid: magento:admin-ui-sdk
  name: Adobe Commerce Admin UI SDK
  tags:
  - Admin Panel
  - App Builder
  - E-Commerce
  - Extensibility
  - UI Extensions
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer.adobe.com/commerce/extensibility/admin-ui-sdk/
  properties:
  - url: https://developer.adobe.com/commerce/extensibility/admin-ui-sdk/
    type: Documentation
  description: The Adobe Commerce Admin UI SDK enables App Builder developers to extend the Commerce Admin panel with custom menus, pages, and UI components built as out-of-process applications. Rather than modifying the Commerce codebase directly, developers build React-based UIs hosted on Adobe App Builder infrastructure and surface them inside the Admin through the SDK's extension point mechanism.
- aid: magento:events
  name: Adobe Commerce Eventing
  tags:
  - Adobe I/O
  - App Builder
  - E-Commerce
  - Events
  - Extensibility
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer.adobe.com/commerce/extensibility/events/
  properties:
  - url: https://developer.adobe.com/commerce/extensibility/events/
    type: Documentation
  - url: asyncapi/magento-events-asyncapi.yml
    type: AsyncAPI
  description: Adobe Commerce Eventing provides an asynchronous event-driven integration framework that publishes Commerce business events to Adobe I/O Events, enabling App Builder applications and other Adobe Experience Cloud services to subscribe and react to store activity. Supported event types cover the full commerce lifecycle including order placement, customer registration, product updates, inventory changes, and payment processing.
name: Magento
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Overview of the Adobe Commerce and Magento Open Source REST API documentation.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

