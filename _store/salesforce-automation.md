---
aid: salesforce-automation
url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation/refs/heads/main/apis.yml
apis:
- name: Salesforce REST API
  description: Core REST API for accessing Salesforce data and metadata programmatically.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/
  baseURL: https://yourInstance.salesforce.com/services/data
  tags:
  - CRUD
  - Data
  - REST
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/
  - type: OpenAPI
    url: openapi/salesforce-rest-api-openapi.json
  - type: JSONSchema
    url: json-schema/salesforce-automation-flow-schema.json
  - type: JSONLD
    url: json-ld/salesforce-automation-context.jsonld
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/quickstart.htm
  - type: API Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_list.htm
  - type: Rate Limits
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_limits.htm
  - type: Change Log
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/rest_rns.htm
  - type: Postman Collection
    url: https://www.postman.com/salesforce-developers/workspace/salesforce-developers/overview
  contact:
  - FN: Salesforce Developer Support
    email: developer@salesforce.com
    url: https://developer.salesforce.com/support
- name: Salesforce SOAP API
  description: Enterprise-grade SOAP API for complex integrations and bulk operations.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/
  baseURL: https://yourInstance.salesforce.com/services/Soap/c
  tags:
  - Enterprise
  - Integration
  - SOAP
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/
  - type: WSDL
    url: https://yourInstance.salesforce.com/services/wsdl/enterprise
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_login.htm
  contact:
  - FN: Salesforce Developer Support
    email: developer@salesforce.com
    url: https://developer.salesforce.com/support
- name: Salesforce Bulk API 2.0
  description: Asynchronous API optimized for loading and querying large data sets.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/
  baseURL: https://yourInstance.salesforce.com/services/data/v63.0/jobs
  tags:
  - Async
  - Bulk
  - ETL
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/
  - type: OpenAPI
    url: openapi/salesforce-bulk-api-openapi.json
  - type: JSONLD
    url: json-ld/salesforce-automation-context.jsonld
  - type: Best Practices
    url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/asynch_api_best_practices.htm
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/asynch_api_quickstart.htm
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/authentication.htm
  contact:
  - FN: Salesforce Developer Support
    email: developer@salesforce.com
    url: https://developer.salesforce.com/support
- name: Salesforce Metadata API
  description: API for managing customizations and building tools for application lifecycle management.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/
  baseURL: https://yourInstance.salesforce.com/services/Soap/m
  tags:
  - Deployment
  - DevOps
  - Metadata
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/
  - type: WSDL
    url: https://yourInstance.salesforce.com/services/wsdl/metadata
  contact:
  - FN: Salesforce Developer Support
    email: developer@salesforce.com
    url: https://developer.salesforce.com/support
- name: Salesforce Streaming API
  description: Real-time event monitoring and push notifications using Bayeux protocol.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/
  baseURL: https://yourInstance.salesforce.com/cometd
  tags:
  - Events
  - Push
  - Real-Time
  - Streaming
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/
  - type: OpenAPI
    url: openapi/salesforce-streaming-api-openapi.json
  - type: JSONLD
    url: json-ld/salesforce-automation-context.jsonld
  - type: Quick Start
    url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/quick_start.htm
  contact:
  - FN: Salesforce Developer Support
    email: developer@salesforce.com
    url: https://developer.salesforce.com/support
- name: Salesforce Platform Events API
  description: Event-driven architecture for publishing and subscribing to custom events.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/
  baseURL: https://yourInstance.salesforce.com/services/data/v63.0/sobjects
  tags:
  - Events
  - Integration
  - Pub/Sub
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/
  - type: OpenAPI
    url: openapi/salesforce-platform-events-api-openapi.json
  - type: JSONLD
    url: json-ld/salesforce-automation-context.jsonld
  - type: Developer Guide
    url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_intro.htm
  contact:
  - FN: Salesforce Developer Support
    email: developer@salesforce.com
    url: https://developer.salesforce.com/support
- name: Salesforce Analytics API
  description: API for accessing and manipulating Analytics dashboards and datasets.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.bi_dev_guide_rest.meta/bi_dev_guide_rest/
  baseURL: https://yourInstance.salesforce.com/services/data/v63.0/wave
  tags:
  - Analytics
  - Dashboards
  - Reports
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.bi_dev_guide_rest.meta/bi_dev_guide_rest/
  - type: OpenAPI
    url: openapi/salesforce-analytics-api-openapi.json
  - type: JSONLD
    url: json-ld/salesforce-automation-context.jsonld
  contact:
  - FN: Salesforce Developer Support
    email: developer@salesforce.com
    url: https://developer.salesforce.com/support
- name: Salesforce Tooling API
  description: API for building custom development tools for Salesforce applications.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/
  baseURL: https://yourInstance.salesforce.com/services/data/v63.0/tooling
  tags:
  - Debugging
  - Development
  - Tooling
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/
  - type: OpenAPI
    url: openapi/salesforce-tooling-api-openapi.json
  - type: JSONSchema
    url: json-schema/salesforce-automation-flow-schema.json
  - type: JSONLD
    url: json-ld/salesforce-automation-context.jsonld
  - type: Flow Object Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_flow.htm
  contact:
  - FN: Salesforce Developer Support
    email: developer@salesforce.com
    url: https://developer.salesforce.com/support
- name: Salesforce Connect REST API
  description: REST API for integrating mobile apps, intranet sites, and third-party web applications with Salesforce, including Chatter feeds, groups, and users.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/intro_what_is_chatter_connect.htm
  baseURL: https://yourInstance.salesforce.com/services/data/v63.0/connect
  tags:
  - Chatter
  - Collaboration
  - Connect
  - Social
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/intro_what_is_chatter_connect.htm
  - type: OpenAPI
    url: openapi/salesforce-connect-rest-api-openapi.json
  - type: JSONLD
    url: json-ld/salesforce-automation-context.jsonld
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/quickstart.htm
  - type: API Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_overview.htm
  - type: Rate Limits
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/intro_rate_limits.htm
  - type: Examples
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/quickreference.htm
  contact:
  - FN: Salesforce Developer Support
    email: developer@salesforce.com
    url: https://developer.salesforce.com/support
- name: Salesforce Pub/Sub API
  description: gRPC-based API for publishing and subscribing to platform events, change data capture events, and custom channels in real time.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/platform/pub-sub-api/overview
  baseURL: https://api.pubsub.salesforce.com:7443
  tags:
  - Events
  - gRPC
  - Pub/Sub
  - Real-Time
  - Streaming
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/platform/pub-sub-api/overview
  - type: JSONLD
    url: json-ld/salesforce-automation-context.jsonld
  - type: Getting Started
    url: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/intro.html
  - type: Authentication
    url: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/supported-auth.html
  - type: API Reference
    url: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/grpc-api.html
  - type: Rate Limits
    url: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/allocations.html
  - type: GitHub
    url: https://github.com/forcedotcom/pub-sub-api
  contact:
  - FN: Salesforce Developer Support
    email: developer@salesforce.com
    url: https://developer.salesforce.com/support
- name: Salesforce GraphQL API
  description: GraphQL API for querying Salesforce data with a single endpoint, reducing round trips and improving application performance.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/platform/graphql/overview
  baseURL: https://yourInstance.salesforce.com/services/data/v63.0/graphql
  tags:
  - Data
  - GraphQL
  - Query
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/platform/graphql/overview
  - type: JSONLD
    url: json-ld/salesforce-automation-context.jsonld
  - type: Getting Started
    url: https://developer.salesforce.com/docs/platform/graphql/guide/graphql-about.html
  - type: Quick Start
    url: https://developer.salesforce.com/docs/platform/graphql/guide/get-started.html
  - type: API Reference
    url: https://developer.salesforce.com/docs/platform/graphql/guide/requests-and-responses.html
  contact:
  - FN: Salesforce Developer Support
    email: developer@salesforce.com
    url: https://developer.salesforce.com/support
- name: Salesforce Change Data Capture API
  description: API for receiving near-real-time notifications of changes to Salesforce records to synchronize corresponding records in external data stores.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture
  baseURL: https://yourInstance.salesforce.com/services/data/v63.0/sobjects
  tags:
  - CDC
  - Change Data Capture
  - Events
  - Real-Time
  - Synchronization
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture
  - type: OpenAPI
    url: openapi/salesforce-change-data-capture-api-openapi.json
  - type: JSONLD
    url: json-ld/salesforce-automation-context.jsonld
  - type: Developer Guide
    url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_what.htm
  - type: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/change-data-capture/understand-change-data-capture
  contact:
  - FN: Salesforce Developer Support
    email: developer@salesforce.com
    url: https://developer.salesforce.com/support
- name: Salesforce Invocable Actions API
  description: REST API for invoking standard and custom actions programmatically, including flow actions and process automation triggers.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_actions_invocable.htm
  baseURL: https://yourInstance.salesforce.com/services/data/v63.0/actions
  tags:
  - Actions
  - Automation
  - Flows
  - Invocable
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_actions_invocable.htm
  - type: OpenAPI
    url: openapi/salesforce-invocable-actions-api-openapi.json
  - type: JSONLD
    url: json-ld/salesforce-automation-context.jsonld
  - type: Standard Actions Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_actions_invocable_standard.htm
  - type: Custom Actions Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_actions_invocable_custom.htm
  - type: Flow Actions
    url: https://developer.salesforce.com/docs/atlas.en-us.api_action.meta/api_action/actions_obj_flow.htm
  - type: Launch a Flow from REST API
    url: https://help.salesforce.com/s/articleView?id=sf.flow_distribute_system_rest.htm&language=en_US&type=5
  contact:
  - FN: Salesforce Developer Support
    email: developer@salesforce.com
    url: https://developer.salesforce.com/support
- name: Salesforce Composite API
  description: REST API for executing multiple API requests in a single call, with the ability to use the output of one request as input to another.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite_composite.htm
  baseURL: https://yourInstance.salesforce.com/services/data/v63.0/composite
  tags:
  - Batch
  - Composite
  - Performance
  - REST
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite_composite.htm
  - type: OpenAPI
    url: openapi/salesforce-composite-api-openapi.json
  - type: JSONLD
    url: json-ld/salesforce-automation-context.jsonld
  - type: Developer Guide
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/using_composite_resources.htm
  - type: Composite Batch
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite_batch.htm
  - type: Composite Graph
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/using_resources_composite_graph.htm
  contact:
  - FN: Salesforce Developer Support
    email: developer@salesforce.com
    url: https://developer.salesforce.com/support
- name: Salesforce Apex REST API
  description: Framework for exposing Apex classes and methods as RESTful web services, enabling custom API endpoints on the Salesforce platform.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
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
    url: openapi/salesforce-apex-rest-api-openapi.json
  - type: JSONLD
    url: json-ld/salesforce-automation-context.jsonld
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_rest_intro.htm
  - type: API Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_restrequest.htm
  - type: Code Samples
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_rest_code_samples.htm
  contact:
  - FN: Salesforce Developer Support
    email: developer@salesforce.com
    url: https://developer.salesforce.com/support
name: Salesforce Automation
tags:
- Automation
- Cloud
- CRM
- Enterprise
- Sales
type: Contract
image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of Salesforce APIs for automating business processes, sales operations, and customer relationship management.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

