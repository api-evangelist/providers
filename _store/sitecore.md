---
aid: sitecore
url: https://raw.githubusercontent.com/api-evangelist/sitecore/refs/heads/main/apis.yml
apis:
- aid: sitecore:xm-cloud-graphql-delivery-api
  name: Sitecore XM Cloud GraphQL Delivery API
  tags:
  - Content Delivery
  - Digital Experience Platform
  - GraphQL
  - Headless CMS
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://edge.sitecorecloud.io/api/graphql
  humanURL: https://doc.sitecore.com/xmc/en/developers/xm-cloud/delivery-api.html
  properties:
  - url: https://doc.sitecore.com/xmc/en/developers/xm-cloud/delivery-api.html
    type: Documentation
  description: The Sitecore XM Cloud GraphQL Delivery API provides access to approved and published content from Sitecore XM Cloud via a GraphQL endpoint optimized for production delivery. Developers use this API to query content items, fields, and relationships with precise control over the data returned in each request, reducing over-fetching in front-end applications. The API is authenticated via API keys and is designed for high availability and performance at scale.
- aid: sitecore:xm-cloud-authoring-management-graphql-api
  name: Sitecore XM Cloud Authoring and Management GraphQL API
  tags:
  - Content Management
  - Digital Experience Platform
  - GraphQL
  - Headless CMS
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://edge.sitecorecloud.io/api/graphql
  humanURL: https://doc.sitecore.com/xmc/en/developers/xm-cloud/sitecore-authoring-and-management-graphql-api.html
  properties:
  - url: https://doc.sitecore.com/xmc/en/developers/xm-cloud/sitecore-authoring-and-management-graphql-api.html
    type: Documentation
  description: The Sitecore XM Cloud Authoring and Management GraphQL API provides a single GraphQL endpoint and schema for managing Sitecore content programmatically. It supports creating, updating, and querying content items, templates, and site structures within an XM Cloud environment. This API is intended for integration builders, content migration tools, and CI/CD pipelines that need to automate content operations against an XM Cloud instance.
- aid: sitecore:xm-cloud-rest-api
  name: Sitecore XM Cloud REST API
  tags:
  - Collections
  - Content Management
  - Digital Experience Platform
  - REST
  - Sites
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://xmapps-api.sitecorecloud.io
  humanURL: https://doc.sitecore.com/xmc/en/developers/xm-cloud/sitecore-xm-cloud.html
  properties:
  - url: https://doc.sitecore.com/xmc/en/developers/xm-cloud/sitecore-xm-cloud.html
    type: Documentation
  - type: OpenAPI
    url: openapi/sitecore-xm-cloud-rest-api-openapi.yml
  description: The Sitecore XM Cloud REST API provides endpoints for creating and managing collections, sites, analytics identifiers, and languages within an XM Cloud tenant. It follows RESTful conventions and exposes over 34 endpoints covering the full lifecycle of site and collection management. Developers use this API to automate site provisioning, manage organizational hierarchies, and integrate XM Cloud administration tasks into external workflows.
- aid: sitecore:cdp-rest-api
  name: Sitecore CDP REST API
  tags:
  - Customer Data Platform
  - Guest Data
  - Personalization
  - REST
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api-engage-us.sitecorecloud.io
  humanURL: https://doc.sitecore.com/cdp/en/developers/api/rest-apis.html
  properties:
  - url: https://doc.sitecore.com/cdp/en/developers/api/rest-apis.html
    type: Documentation
  - type: OpenAPI
    url: openapi/sitecore-cdp-rest-api-openapi.yml
  description: The Sitecore CDP REST API allows developers to retrieve, create, update, and delete data stored in Sitecore Customer Data Platform. It provides access to guest profiles, orders, sessions, and behavioral data through standard HTTP methods. Developers use this API to build integrations that read or write customer data programmatically, enabling use cases such as audience segmentation, data enrichment, and reporting.
- aid: sitecore:cdp-stream-api
  name: Sitecore CDP Stream API
  tags:
  - Behavioral Data
  - Customer Data Platform
  - Event Tracking
  - Real-Time
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api-engage-us.sitecorecloud.io
  humanURL: https://doc.sitecore.com/cdp/en/developers/api/stream-api.html
  properties:
  - url: https://doc.sitecore.com/cdp/en/developers/api/stream-api.html
    type: Documentation
  - type: AsyncAPI
    url: asyncapi/sitecore-cdp-stream-api-asyncapi.yml
  description: The Sitecore CDP Stream API enables applications to send real-time behavioral and transactional events about users to the Sitecore Customer Data Platform. It is designed for high-throughput event ingestion from web, mobile, and server-side applications, capturing interactions such as page views, product views, and purchases. Events sent through the Stream API update guest profiles in near real-time, powering personalization and segmentation use cases.
- aid: sitecore:cdp-batch-api
  name: Sitecore CDP Batch API
  tags:
  - Batch Processing
  - Customer Data Platform
  - Data Import
  - Guest Data
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api-engage-us.sitecorecloud.io
  humanURL: https://doc.sitecore.com/cdp/en/developers/api/index-en.html
  properties:
  - url: https://doc.sitecore.com/cdp/en/developers/api/index-en.html
    type: Documentation
  description: The Sitecore CDP Batch API supports uploading large volumes of guest data and offline order records into Sitecore Customer Data Platform. It is intended for bulk data migration, historical data ingestion, and scenarios where real-time streaming is not practical, such as nightly data syncs from CRM or ERP systems. The API accepts structured data files and processes them asynchronously, updating guest profiles and order histories in CDP.
- aid: sitecore:personalize-rest-api
  name: Sitecore Personalize REST API
  tags:
  - Decisioning
  - Experiments
  - Personalization
  - REST
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.boxever.com
  humanURL: https://doc.sitecore.com/personalize/en/developers/api/index-en.html
  properties:
  - url: https://doc.sitecore.com/personalize/en/developers/api/index-en.html
    type: Documentation
  - type: OpenAPI
    url: openapi/sitecore-personalize-rest-api-openapi.yml
  description: The Sitecore Personalize REST API allows developers to programmatically interact with Sitecore Personalize experiments, decisioning flows, and connection configurations. It supports retrieving, creating, updating, and deleting personalization resources through standard HTTP methods. Developers use this API to integrate decisioning logic into server-side applications, trigger personalization flows programmatically, and manage personalization assets as part of automated deployment pipelines.
- aid: sitecore:content-hub-rest-api
  name: Sitecore Content Hub REST API
  tags:
  - Content Hub
  - Digital Asset Management
  - Media Management
  - REST
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://your-tenant.stylelabs.io/api
  humanURL: https://doc.sitecore.com/ch/en/developers/cloud-dev/rest-apis.html
  properties:
  - url: https://doc.sitecore.com/ch/en/developers/cloud-dev/rest-apis.html
    type: Documentation
  - type: OpenAPI
    url: openapi/sitecore-content-hub-rest-api-openapi.yml
  description: The Sitecore Content Hub REST API is a hypermedia API built on HTTP that provides programmatic access to the full range of Content Hub resources, including entities, assets, jobs, search, selections, and audit logs. Developers use it to automate digital asset management workflows, migrate content, build custom integrations, and manage Content Hub configuration. The API supports standard CRUD operations and is authenticated using OAuth 2.0 tokens obtained from the Content Hub identity provider.
- aid: sitecore:content-hub-admin-api
  name: Sitecore Content Hub Admin API
  tags:
  - Administration
  - Content Hub
  - Digital Asset Management
  - GraphQL
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://your-tenant.stylelabs.io/api/graphql/admin/v1
  humanURL: https://doc.sitecore.com/ch/en/developers/cloud-dev/content-hub-admin-api.html
  properties:
  - url: https://doc.sitecore.com/ch/en/developers/cloud-dev/content-hub-admin-api.html
    type: Documentation
  description: The Sitecore Content Hub Admin API is a GraphQL API that provides access to administrative functions within a Content Hub tenant, accessible at the path /api/graphql/admin/v1 relative to the Content Hub instance URL. It enables programmatic management of tenant-level configuration, schema definitions, and other administrative resources that are not exposed through the standard REST API.
- aid: sitecore:ordercloud-api
  name: Sitecore OrderCloud API
  tags:
  - B2B
  - B2C
  - Commerce
  - Order Management
  - REST
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.ordercloud.io/v1
  humanURL: https://api-docs.sitecore.com/ordercloud
  properties:
  - url: https://api-docs.sitecore.com/ordercloud
    type: Documentation
  - type: OpenAPI
    url: openapi/sitecore-ordercloud-api-openapi.yml
  - type: JSONSchema
    url: json-schema/sitecore-ordercloud-order-schema.json
  description: The Sitecore OrderCloud API is a headless, API-first commerce platform providing RESTful endpoints for managing the full range of e-commerce operations including products, catalogs, orders, buyers, sellers, promotions, and fulfillment. It is designed to support B2C, B2B, and B2B2C commerce models with a highly flexible and extensible data model that allows custom properties on most resources.
- aid: sitecore:discover-api
  name: Sitecore Discover API
  tags:
  - Commerce
  - Product Discovery
  - Recommendations
  - Search
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.rfksrv.com
  humanURL: https://doc.sitecore.com/discover/en/developers/discover-developer-guide/api-endpoints-and-methods.html
  properties:
  - url: https://doc.sitecore.com/discover/en/developers/discover-developer-guide/api-endpoints-and-methods.html
    type: Documentation
  - type: OpenAPI
    url: openapi/sitecore-discover-api-openapi.yml
  description: The Sitecore Discover API provides search and product discovery capabilities for commerce applications, enabling developers to build search experiences, product listing pages, and recommendation widgets. It exposes endpoints for full-text search, faceted filtering, product recommendations, and behavioral event tracking that feeds back into the discovery algorithms.
name: Sitecore
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Sitecore is a global digital experience platform that combines content management, marketing automation, e-commerce, customer insight, and personalization to help brands deliver personalized customer experiences.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

