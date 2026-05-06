---
name: Salesforce Automation
description: A collection of Salesforce APIs for automating business processes, sales operations, and customer relationship management.
image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
url: https://developer.salesforce.com
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.16'
tags:
  - Automation
  - Cloud
  - CRM
  - Enterprise
  - Sales
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
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
common:
  - type: Portal
    url: https://developer.salesforce.com
  - type: Website
    url: https://www.salesforce.com
  - type: Developer Portal
    url: https://developer.salesforce.com
  - type: Documentation
    url: https://developer.salesforce.com/docs
  - type: API Library
    url: https://developer.salesforce.com/docs/apis
  - type: Trailhead Learning
    url: https://trailhead.salesforce.com
  - type: API Status
    url: https://status.salesforce.com
  - type: Community
    url: https://developer.salesforce.com/forums
  - type: Blog
    url: https://developer.salesforce.com/blogs
  - type: Pricing
    url: https://www.salesforce.com/editions-pricing/overview/
  - type: Terms of Service
    url: https://www.salesforce.com/company/legal/agreements/
  - type: Privacy Policy
    url: https://www.salesforce.com/company/privacy/
  - type: Sign Up
    url: https://developer.salesforce.com/signup
  - type: Login
    url: https://login.salesforce.com
  - type: GitHub
    url: https://github.com/salesforce
  - type: GitHub Organization
    url: https://github.com/developerforce
  - type: Stack Exchange
    url: https://salesforce.stackexchange.com
  - type: X (Twitter)
    url: https://twitter.com/salesforcedevs
  - type: Support
    url: https://developer.salesforce.com/support
  - type: Contact
    url: https://www.salesforce.com/company/contact-us/
  - type: Rate Limits
    url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm
  - type: API Versioning
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_versions.htm
  - type: Postman Collection
    url: https://www.postman.com/salesforce-developers/workspace/salesforce-developers/overview
  - type: Postman GitHub
    url: https://github.com/forcedotcom/postman-salesforce-apis
  - type: SDKs
    url: https://jsforce.github.io/
  - type: Release Notes
    url: https://help.salesforce.com/s/articleView?id=release-notes.rn_api_nc.htm&language=en_US&release=248&type=5
  - type: API End-of-Life Policy
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/api_rest_eol.htm
  - type: SpectralRules
    url: rules/salesforce-automation-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/salesforce-automation-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/data-operations.yaml
    title: Data Operations Workflow
  - type: JSONStructure
    url: json-structure/salesforce-automation-flow-structure.json
  - type: Example
    url: examples/salesforce-automation-flow-example.json
    title: Flow Example
  - type: GitHubOrganization
    url: https://github.com/salesforce
  - type: Features
    data:
      - name: OAuth 2.0 Authentication
        description: Supports multiple OAuth flows including authorization code, JWT bearer, and client credentials.
      - name: SOQL Queries
        description: Salesforce Object Query Language for structured data queries across objects.
      - name: SOSL Search
        description: Full-text search across multiple objects using Salesforce Object Search Language.
      - name: Bulk Data Operations
        description: Asynchronous bulk API for loading, deleting, and querying millions of records.
      - name: Real-Time Events
        description: Platform events, Change Data Capture, and streaming API for real-time notifications.
      - name: Flow Automation
        description: Declarative automation with Flow Builder for record-triggered, scheduled, and screen flows.
      - name: Composite API
        description: Execute multiple API requests in a single call with request chaining.
      - name: GraphQL Support
        description: Single-endpoint GraphQL API for efficient data queries.
      - name: Invocable Actions
        description: Programmatic invocation of standard and custom automation actions.
      - name: Approval Processes
        description: Multi-step approval workflows with programmatic submission and management.
  - type: UseCases
    data:
      - name: Sales Pipeline Automation
        description: Automate lead assignment, opportunity stage progression, and deal closure workflows.
      - name: Data Migration
        description: Bulk import and export of large datasets between Salesforce and external systems.
      - name: Real-Time Data Sync
        description: Keep external systems in sync with Salesforce using Change Data Capture events.
      - name: Custom Integrations
        description: Build custom REST endpoints using Apex REST for bespoke integration scenarios.
      - name: Analytics and Reporting
        description: Programmatic access to Einstein Analytics dashboards and datasets.
      - name: Process Automation
        description: Trigger flows, approval processes, and invocable actions based on data changes.
  - type: Integrations
    data:
      - name: MuleSoft
        description: Native integration platform for connecting Salesforce with enterprise systems.
      - name: Slack
        description: Salesforce-owned collaboration platform with deep CRM integration.
      - name: Tableau
        description: Analytics and visualization platform integrated with Salesforce data.
      - name: Heroku
        description: Cloud application platform for extending Salesforce with custom apps.
      - name: Postman
        description: Official Postman workspace with pre-built API collections for testing.
---
