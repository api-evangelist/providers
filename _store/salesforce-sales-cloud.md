---
aid: salesforce-sales-cloud
url: https://raw.githubusercontent.com/api-evangelist/salesforce-sales-cloud/refs/heads/main/apis.yml
apis:
- name: Salesforce REST API
  description: Primary REST API for accessing Salesforce data including accounts, contacts, leads, opportunities, and custom objects. Supports JSON and XML formats with a lightweight request and response framework.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/salesforce-logo.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0
  tags:
  - CRUD
  - Data
  - Objects
  - Records
  - REST
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm
  - type: OpenAPI
    url: openapi/salesforce-sales-cloud-rest-api-openapi.yml
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_authentication.htm
  - type: Postman Collection
    url: https://www.postman.com/salesforce-developers/workspace/salesforce-developers
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/quickstart.htm
  - type: Change Log
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/rest_rns.htm
- name: Salesforce SOAP API
  description: Comprehensive SOAP-based API for enterprise integrations with full CRUD operations on Salesforce objects. Uses WSDL files to define parameters for accessing data through the API.
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/
  baseURL: https://yourInstance.salesforce.com/services/Soap/u/59.0
  tags:
  - Enterprise
  - Integration
  - SOAP
  - XML
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_quickstart_intro.htm
  - type: WSDL
    url: https://yourInstance.salesforce.com/services/wsdl/enterprise
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_login.htm
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_quickstart_steps.htm
- name: Bulk API 2.0
  description: Optimized API for loading, updating, or deleting large data sets asynchronously with better performance than REST API. Supports CSV, JSON, and XML data formats.
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/jobs/ingest
  tags:
  - Async
  - Bulk
  - Data Loading
  - ETL
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/asynch_api_intro.htm
  - type: Examples
    url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/asynch_api_code_samples.htm
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/bulk_api_2_0.htm
  - type: OpenAPI
    url: openapi/salesforce-sales-cloud-bulk-api-openapi.yml
- name: Metadata API
  description: API for retrieving, deploying, creating, updating, or deleting customization information such as custom object definitions and page layouts. Essential for managing org configuration and deployment workflows.
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/
  baseURL: https://yourInstance.salesforce.com/services/Soap/m/59.0
  tags:
  - Configuration
  - Customization
  - Deployment
  - Metadata
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_intro.htm
  - type: WSDL
    url: https://yourInstance.salesforce.com/services/wsdl/metadata
  - type: Change Log
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_rns.htm
- name: Streaming API
  description: Push notification API using Bayeux protocol to receive near real-time updates when data changes in Salesforce. Enables event-driven integrations without polling.
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/
  baseURL: https://yourInstance.salesforce.com/cometd/59.0
  tags:
  - Events
  - Push Notifications
  - Real-Time
  - Streaming
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/intro_stream.htm
  - type: Examples
    url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/code_sample_java_client_intro.htm
- name: Platform Events API
  description: Event-driven architecture API for publishing and subscribing to custom events for app integration. Supports defining custom event channels with schema for loosely coupled systems.
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/sobjects
  tags:
  - Events
  - Integration
  - Messaging
  - Pub/Sub
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_intro.htm
  - type: Guide
    url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_publish_api.htm
  - type: OpenAPI
    url: openapi/salesforce-sales-cloud-platform-events-api-openapi.yml
- name: Analytics REST API
  description: Access Salesforce reports, dashboards, and analytics data programmatically. Enables embedding analytics into custom applications and automating report generation.
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_analytics.meta/api_analytics/
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/analytics
  tags:
  - Analytics
  - Business Intelligence
  - Dashboards
  - Reports
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_analytics.meta/api_analytics/sforce_analytics_rest_api_intro.htm
  - type: OpenAPI
    url: openapi/salesforce-sales-cloud-analytics-api-openapi.yml
- name: Salesforce Composite API
  description: Executes a series of REST API requests in a single call, reducing round trips between client and server. Supports composite batches, composite requests, and composite graphs for complex multi-step operations.
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/using_composite_resources.htm
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/composite
  tags:
  - Batch
  - Composite
  - Integration
  - Performance
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/using_composite_resources.htm
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite_composite.htm
  - type: Guide
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite_graph_introduction.htm
  - type: OpenAPI
    url: openapi/salesforce-sales-cloud-composite-api-openapi.yml
- name: Salesforce GraphQL API
  description: Query Salesforce data using GraphQL, allowing clients to request exactly the fields they need in a single request. Reduces payload size and supports aggregation across object relationships.
  humanURL: https://developer.salesforce.com/docs/platform/graphql/overview
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/graphql
  tags:
  - Data Access
  - GraphQL
  - Query
  - Schema
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/platform/graphql/guide/intro-graphql-api.html
  - type: Getting Started
    url: https://developer.salesforce.com/docs/platform/graphql/guide/get-started.html
  - type: Reference
    url: https://developer.salesforce.com/docs/platform/graphql/guide/requests-and-responses.html
  - type: OpenAPI
    url: openapi/salesforce-sales-cloud-graphql-api-openapi.yml
- name: Salesforce Tooling API
  description: Build custom development tools for Salesforce applications by accessing metadata about Apex classes, triggers, Visualforce pages, and other development artifacts. Supports both REST and SOAP interfaces.
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/tooling
  tags:
  - Apex
  - Development
  - Metadata
  - Tooling
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/intro_rest_overview.htm
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/intro_rest_resources.htm
  - type: Examples
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/intro_rest_resource_examples.htm
  - type: OpenAPI
    url: openapi/salesforce-sales-cloud-tooling-api-openapi.yml
- name: Salesforce Pub/Sub API
  description: gRPC-based API for publishing and subscribing to platform events, change data capture events, and real-time event monitoring events. Uses Apache Avro format for efficient binary event message delivery over HTTP/2.
  humanURL: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/intro.html
  baseURL: https://yourInstance.salesforce.com
  tags:
  - Events
  - gRPC
  - Pub/Sub
  - Real-Time
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/intro.html
  - type: Getting Started
    url: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/grpc-api.html
  - type: Reference
    url: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/pub-sub-endpoints.html
- name: Salesforce Change Data Capture API
  description: Receive near-real-time notifications of changes to Salesforce records including creates, updates, deletes, and undeletes. Enables synchronization of external data stores with Salesforce data.
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0
  tags:
  - Change Data Capture
  - Events
  - Real-Time
  - Synchronization
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm
  - type: Guide
    url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_what.htm
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_message_structure.htm
  - type: OpenAPI
    url: openapi/salesforce-sales-cloud-change-data-capture-api-openapi.yml
- name: Salesforce Connect REST API
  description: Integrate mobile apps, intranet sites, and third-party web applications with Salesforce, including access to Chatter feeds, groups, users, and collaboration features.
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/intro_what_is_chatter_connect.htm
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/connect
  tags:
  - Chatter
  - Collaboration
  - Connect
  - Social
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/intro_what_is_chatter_connect.htm
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/quickstart.htm
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_overview.htm
  - type: Examples
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/quickreference.htm
  - type: Change Log
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/intro_release_notes.htm
  - type: OpenAPI
    url: openapi/salesforce-sales-cloud-connect-api-openapi.yml
- name: Salesforce User Interface API
  description: Build custom user interfaces for Salesforce data using the same API that powers Lightning Experience. Returns data and metadata in a single response with layout, picklist, and field-level security awareness.
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/ui-api
  tags:
  - Layouts
  - Lightning
  - Records
  - User Interface
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi/ui_api_get_started.htm
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi/ui_api_resources_overview.htm
  - type: OpenAPI
    url: openapi/salesforce-sales-cloud-ui-api-openapi.yml
- name: Salesforce Apex REST API
  description: Create custom REST endpoints in Salesforce using Apex classes annotated with REST resource annotations. Supports OAuth 2.0 authentication and JSON and XML request and response formats.
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_rest.htm
  baseURL: https://yourInstance.salesforce.com/services/apexrest
  tags:
  - Apex
  - Custom Endpoints
  - Development
  - REST
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_rest.htm
  - type: OpenAPI
    url: openapi/salesforce-sales-cloud-apex-rest-api-openapi.yml
name: Salesforce Sales Cloud
tags:
- Cloud
- CRM
- Customer Management
- Enterprise
- Sales
type: Contract
image: https://www.salesforce.com/content/dam/web/en_us/www/images/salesforce-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Enterprise CRM platform providing sales automation, customer relationship management, and business intelligence capabilities through REST and SOAP APIs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

