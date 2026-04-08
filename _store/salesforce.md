---
aid: salesforce
url: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/apis.yml
apis:
- aid: salesforce:salesforce-rest-api
  name: Salesforce REST API
  tags:
  - CRM
  - Objects
  - Records
  - REST
  - SOQL
  - SOSL
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/
  baseURL: https://{instance}.salesforce.com/services/data
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/quickstart.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/dome_versions.htm
    type: Reference
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_authentication.htm
    type: Authentication
  - url: openapi/salesforce-openapi.yml
    type: OpenAPI
  - url: openapi/salesforce-rest-api-openapi.yml
    type: OpenAPI
  - url: json-schema/salesforce-sobject-schema.json
    type: JSONSchema
  - url: json-schema/salesforce-query-result-schema.json
    type: JSONSchema
  description: The Salesforce REST API provides a simple and powerful web service interface to interact with Salesforce org data. It supports creating, reading, updating, deleting, and querying records using SOQL and SOSL, and is the primary API for building connected applications against Salesforce.
- aid: salesforce:salesforce-soap-api
  name: Salesforce SOAP API
  tags:
  - CRM
  - Enterprise
  - Objects
  - Records
  - SOAP
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/
  baseURL: https://{instance}.salesforce.com/services/Soap
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_quickstart_intro.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_list.htm
    type: Reference
  - url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_concepts_security.htm
    type: Authentication
  description: The Salesforce SOAP API enables developers to use SOAP calls to create, retrieve, update, and delete records such as accounts, leads, and custom objects. It provides robust enterprise-grade integration capabilities and supports batch processing of records.
- aid: salesforce:salesforce-bulk-api
  name: Salesforce Bulk API
  tags:
  - Bulk
  - CRM
  - Data Loading
  - ETL
  - Records
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/
  baseURL: https://{instance}.salesforce.com/services/async
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/asynch_api_quickstart.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/asynch_api_reference.htm
    type: Reference
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/asynch_api_concepts_security.htm
    type: Authentication
  description: The Salesforce Bulk API is a specialized REST-based interface that enables asynchronous processing of large numbers of records. It is optimized for loading or deleting large sets of data and supports CSV, XML, and JSON formats.
- aid: salesforce:salesforce-bulk-api-2
  name: Salesforce Bulk API 2.0
  tags:
  - Bulk
  - CRM
  - Data Loading
  - ETL
  - Records
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_bulk_v2.meta/api_bulk_v2/
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/jobs
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_bulk_v2.meta/api_bulk_v2/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_bulk_v2.meta/api_bulk_v2/get_job_info.htm
    type: Reference
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_bulk_v2.meta/api_bulk_v2/bulk_api_2_0_security.htm
    type: Authentication
  - url: openapi/salesforce-bulk-api-2-openapi.yml
    type: OpenAPI
  - url: json-schema/salesforce-bulk-job-schema.json
    type: JSONSchema
  description: Salesforce Bulk API 2.0 is a simplified, REST-based interface for bulk data operations that improves on the original Bulk API. It uses a straightforward job model and supports CSV format for ingest and query jobs processing millions of records.
- aid: salesforce:salesforce-streaming-api
  name: Salesforce Streaming API
  tags:
  - CRM
  - Events
  - Push Notifications
  - Real-Time
  - Streaming
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/
  baseURL: https://{instance}.salesforce.com/cometd
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/intro_stream.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/resources_top.htm
    type: Reference
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/using_streaming_api_auth.htm
    type: Authentication
  - url: asyncapi/salesforce-streaming-asyncapi.yml
    type: AsyncAPI
  description: The Salesforce Streaming API uses a publish-subscribe model based on Bayeux/CometD to push near-real-time event notifications to subscribed clients. It supports PushTopic events for record changes and Generic Streaming events for custom notifications.
- aid: salesforce:salesforce-metadata-api
  name: Salesforce Metadata API
  tags:
  - Configuration
  - CRM
  - Deployment
  - DevOps
  - Metadata
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/
  baseURL: https://{instance}.salesforce.com/services/Soap/m
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_quickstart.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_types_list.htm
    type: Reference
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_auth.htm
    type: Authentication
  description: The Salesforce Metadata API is a SOAP-based API that enables developers to retrieve, deploy, create, update, and delete customizations for Salesforce organizations. It is the foundation for tools like Salesforce CLI, Ant Migration Tool, and CI/CD pipelines.
- aid: salesforce:salesforce-tooling-api
  name: Salesforce Tooling API
  tags:
  - Apex
  - CRM
  - Development
  - IDE
  - Tooling
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/tooling
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_list.htm
    type: Reference
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/intro_rest_resources.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/intro_rest_overview.htm
    type: Authentication
  description: The Salesforce Tooling API provides SOAP and REST interfaces for building developer tools for Force.com applications. It exposes fine-grained access to Apex code, Visualforce pages, and other metadata for IDE integration, code coverage, and debugging workflows.
- aid: salesforce:salesforce-connect-api
  name: Salesforce Connect API (Chatter)
  tags:
  - Chatter
  - Collaboration
  - Connect
  - CRM
  - Feed
  - Social
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/chatter
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/quickstart.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_list.htm
    type: Reference
  - url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/authentication.htm
    type: Authentication
  description: The Salesforce Connect REST API (formerly Chatter API) provides access to Salesforce Chatter feeds, groups, users, topics, and file sharing features. It also exposes Experience Cloud (community) data and supports building custom social and collaboration experiences.
- aid: salesforce:salesforce-analytics-rest-api
  name: Salesforce Analytics REST API
  tags:
  - Analytics
  - CRM
  - CRM Analytics
  - Dashboards
  - Reports
  - Tableau CRM
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.bi_dev_guide_rest.meta/bi_dev_guide_rest/
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/wave
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.bi_dev_guide_rest.meta/bi_dev_guide_rest/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.bi_dev_guide_rest.meta/bi_dev_guide_rest/bi_rest_overview.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.bi_dev_guide_rest.meta/bi_dev_guide_rest/bi_rest_resources_list.htm
    type: Reference
  description: The Salesforce Analytics REST API (also known as CRM Analytics or Wave API) provides programmatic access to CRM Analytics datasets, lenses, dashboards, and queries. Developers can read and write analytics assets and run SAQL queries against analytics datasets.
- aid: salesforce:salesforce-reports-and-dashboards-rest-api
  name: Salesforce Reports and Dashboards REST API
  tags:
  - Analytics
  - CRM
  - Dashboards
  - Reports
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_analytics.meta/api_analytics/
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/analytics
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_analytics.meta/api_analytics/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_analytics.meta/api_analytics/sforce_analytics_rest_api_getstarted.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_analytics.meta/api_analytics/sforce_analytics_rest_api_resource_index.htm
    type: Reference
  description: The Salesforce Reports and Dashboards REST API enables developers to programmatically access report results, list reports and dashboards, and run and filter reports. It supports accessing standard and custom Salesforce reports without the need to navigate the UI.
- aid: salesforce:salesforce-einstein-platform-services-api
  name: Salesforce Einstein Platform Services API
  tags:
  - AI
  - Computer Vision
  - Einstein
  - Machine Learning
  - Natural Language Processing
  - Prediction
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://metamind.readme.io/
  baseURL: https://api.einstein.ai/v2
  properties:
  - url: https://metamind.readme.io/
    type: Documentation
  - url: https://metamind.readme.io/docs/getting-started
    type: Getting Started
  - url: https://metamind.readme.io/reference
    type: Reference
  - url: https://metamind.readme.io/docs/authentication
    type: Authentication
  - url: https://trailhead.salesforce.com/en/content/learn/modules/einstein_platform_services
    type: Getting Started
  description: The Salesforce Einstein Platform Services API provides REST-based access to Salesforce AI capabilities including image classification, object detection, and sentiment analysis. Developers can train custom models or use pre-built models for vision and natural language processing tasks.
- aid: salesforce:salesforce-einstein-prediction-service-api
  name: Salesforce Einstein Prediction Service API
  tags:
  - AI
  - CRM
  - Einstein
  - Machine Learning
  - Prediction
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.einstein_platform_services.meta/einstein_platform_services/
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/einstein
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.einstein_platform_services.meta/einstein_platform_services/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.einstein_platform_services.meta/einstein_platform_services/einstein_platform_intro.htm
    type: Getting Started
  description: The Salesforce Einstein Prediction Service API enables programmatic access to Einstein Analytics predictions and forecasts built on CRM data. It allows applications to retrieve AI-driven predictions for leads, opportunities, and custom objects configured in Salesforce.
- aid: salesforce:salesforce-graphql-api
  name: Salesforce GraphQL API
  tags:
  - CRM
  - GraphQL
  - Queries
  - Records
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/platform/graphql/guide/graphql-about.html
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/graphql
  properties:
  - url: https://developer.salesforce.com/docs/platform/graphql/guide/graphql-about.html
    type: Documentation
  - url: https://developer.salesforce.com/docs/platform/graphql/guide/graphql-get-started.html
    type: Getting Started
  - url: https://developer.salesforce.com/docs/platform/graphql/guide/graphql-reference.html
    type: Reference
  - url: https://developer.salesforce.com/docs/platform/graphql/guide/graphql-auth.html
    type: Authentication
  description: The Salesforce GraphQL API provides a GraphQL interface to query and mutate Salesforce data. It allows clients to request exactly the data they need in a single request, reducing over-fetching and under-fetching compared to traditional REST calls.
- aid: salesforce:salesforce-pub-sub-api
  name: Salesforce Pub/Sub API
  tags:
  - CRM
  - Events
  - gRPC
  - Platform Events
  - Pub/Sub
  - Real-Time
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/pub-sub-api-intro.html
  baseURL: https://api.pubsub.salesforce.com
  properties:
  - url: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/pub-sub-api-intro.html
    type: Documentation
  - url: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/pub-sub-api-get-started.html
    type: Getting Started
  - url: https://developer.salesforce.com/docs/platform/pub-sub-api/references/pubsub-api-reference.html
    type: Reference
  - url: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/pub-sub-api-auth.html
    type: Authentication
  - url: https://github.com/developerforce/pub-sub-api
    type: GitHubRepository
  description: The Salesforce Pub/Sub API is a gRPC-based API for publishing and subscribing to platform events, change data capture events, and other event types in real time. It supersedes the CometD-based Streaming API for high-throughput event-driven integrations.
- aid: salesforce:salesforce-platform-events-api
  name: Salesforce Platform Events API
  tags:
  - CRM
  - Event-Driven
  - Events
  - Integration
  - Platform Events
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/sobjects
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_intro.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_subscribe_api.htm
    type: Reference
  - url: asyncapi/salesforce-platform-events-asyncapi.yml
    type: AsyncAPI
  description: Salesforce Platform Events enables event-driven integration architectures built on the Salesforce platform. Developers define custom event types as Salesforce objects and publish or subscribe to events using the REST API, Apex, or Salesforce Flows.
- aid: salesforce:salesforce-change-data-capture-api
  name: Salesforce Change Data Capture API
  tags:
  - CDC
  - Change Data Capture
  - CRM
  - Events
  - Integration
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/
  baseURL: https://{instance}.salesforce.com/cometd
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_subscribe_api.htm
    type: Reference
  - url: asyncapi/salesforce-change-data-capture-asyncapi.yml
    type: AsyncAPI
  description: Salesforce Change Data Capture delivers change events that represent changes to Salesforce records including creates, updates, deletes, and undeletes. It enables external systems to receive near-real-time changes to Salesforce data for data replication and synchronization use cases.
- aid: salesforce:salesforce-ui-api
  name: Salesforce UI API
  tags:
  - Components
  - CRM
  - Lightning
  - UI
  - User Interface
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi/
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/ui-api
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi/ui_api_get_started.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi/ui_api_resources_list.htm
    type: Reference
  - url: openapi/salesforce-ui-api-openapi.yml
    type: OpenAPI
  description: The Salesforce UI API provides a comprehensive REST interface for building UIs that work with Salesforce metadata and data. It returns layout information, picklist values, list views, record data, and object metadata that Lightning components rely on.
- aid: salesforce:salesforce-composite-api
  name: Salesforce Composite API
  tags:
  - Batch
  - Composite
  - CRM
  - Performance
  - REST
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite.htm
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/composite
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite.htm
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite_intro.htm
    type: Reference
  description: The Salesforce Composite API allows developers to combine multiple Salesforce REST API requests into a single HTTP call. It reduces the number of round trips to the server and supports dependent requests using reference IDs, improving integration performance.
- aid: salesforce:salesforce-apex-rest-api
  name: Salesforce Apex REST API
  tags:
  - Apex
  - CRM
  - Custom APIs
  - Development
  - REST
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_rest.htm
  baseURL: https://{instance}.salesforce.com/services/apexrest
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_rest.htm
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_rest_code_sample_intro.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_rest_methods.htm
    type: Reference
  description: Salesforce Apex REST enables developers to expose custom Apex classes as RESTful web services. By annotating Apex classes and methods with @RestResource and HTTP method annotations, developers can create custom API endpoints that extend Salesforce functionality.
- aid: salesforce:salesforce-data-cloud-api
  name: Salesforce Data Cloud API
  tags:
  - CDP
  - CRM
  - Customer Data Platform
  - Data Cloud
  - Identity Resolution
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/platform/data-cloud-api/overview
  baseURL: https://{instance}.salesforce.com/api/v1
  properties:
  - url: https://developer.salesforce.com/docs/platform/data-cloud-api/overview
    type: Documentation
  - url: https://developer.salesforce.com/docs/platform/data-cloud-api/guide/dc-api-getting-started.html
    type: Getting Started
  - url: https://developer.salesforce.com/docs/platform/data-cloud-api/references/data-cloud-api.html
    type: Reference
  - url: https://developer.salesforce.com/docs/platform/data-cloud-api/guide/dc-api-auth.html
    type: Authentication
  description: The Salesforce Data Cloud API provides programmatic access to Data Cloud (formerly Customer Data Platform) for ingesting, querying, and managing unified customer profiles. It enables applications to read and write segments, calculated insights, and identity-resolved profile data.
- aid: salesforce:salesforce-marketing-cloud-rest-api
  name: Salesforce Marketing Cloud REST API
  tags:
  - Email
  - Journeys
  - Marketing Automation
  - Marketing Cloud
  - REST
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rest-api.html
  baseURL: https://{subdomain}.rest.marketingcloudapis.com
  properties:
  - url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rest-api.html
    type: Documentation
  - url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/get-started-spec.html
    type: Getting Started
  - url: https://developer.salesforce.com/docs/marketing/marketing-cloud/references/mc_rest_overview.html
    type: Reference
  - url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/access-token-s2s.html
    type: Authentication
  - url: openapi/salesforce-marketing-cloud-rest-openapi.yml
    type: OpenAPI
  description: The Salesforce Marketing Cloud REST API provides access to Marketing Cloud resources including contacts, journeys, data extensions, triggered sends, and transactional messaging. It uses OAuth 2.0 for authentication and is the primary interface for programmatic Marketing Cloud integrations.
- aid: salesforce:salesforce-marketing-cloud-soap-api
  name: Salesforce Marketing Cloud SOAP API
  tags:
  - Email
  - Marketing Automation
  - Marketing Cloud
  - SOAP
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/soap-api.html
  baseURL: https://{subdomain}.soap.marketingcloudapis.com
  properties:
  - url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/soap-api.html
    type: Documentation
  - url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/getting-started-with-mc-sdk.html
    type: Getting Started
  - url: https://developer.salesforce.com/docs/marketing/marketing-cloud/references/mc_soap_objects.html
    type: Reference
  description: The Salesforce Marketing Cloud SOAP API is a full-featured SOAP web service interface for Marketing Cloud that supports subscriber management, email send operations, automation activities, and data extension management.
- aid: salesforce:salesforce-pardot-api
  name: Salesforce Pardot API (Account Engagement)
  tags:
  - Account Engagement
  - B2B Marketing
  - Lead Generation
  - Marketing
  - Pardot
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/marketing/pardot/guide/overview.html
  baseURL: https://pi.pardot.com/api
  properties:
  - url: https://developer.salesforce.com/docs/marketing/pardot/guide/overview.html
    type: Documentation
  - url: https://developer.salesforce.com/docs/marketing/pardot/guide/getting-started.html
    type: Getting Started
  - url: https://developer.salesforce.com/docs/marketing/pardot/references/pardot-api-overview.html
    type: Reference
  - url: https://developer.salesforce.com/docs/marketing/pardot/guide/authentication.html
    type: Authentication
  description: The Salesforce Pardot API (now called Account Engagement API) provides programmatic access to Pardot marketing automation data including prospects, campaigns, forms, lists, and email statistics for B2B marketing use cases.
- aid: salesforce:salesforce-commerce-cloud-ocapi
  name: Salesforce Commerce Cloud OCAPI
  tags:
  - B2C Commerce
  - Commerce
  - OCAPI
  - Orders
  - Storefront
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/OCAPI.html
  baseURL: https://{instance}.dx.commercecloud.salesforce.com
  properties:
  - url: https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/OCAPI.html
    type: Documentation
  - url: https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/ocapi-get-started.html
    type: Getting Started
  - url: https://developer.salesforce.com/docs/commerce/b2c-commerce/references/b2c-commerce-api.html
    type: Reference
  - url: https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/auth-overview.html
    type: Authentication
  description: The Salesforce Commerce Cloud Open Commerce API (OCAPI) provides a REST interface for accessing Salesforce B2C Commerce data and functionality including products, catalogs, orders, promotions, and customer accounts for storefronts and back-office integrations.
- aid: salesforce:salesforce-commerce-cloud-shopper-apis
  name: Salesforce Commerce Cloud Shopper APIs (SCAPI)
  tags:
  - B2C Commerce
  - Commerce
  - Orders
  - Products
  - Shopper
  - Storefront
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/web-api.html
  baseURL: https://{shortCode}.api.commercecloud.salesforce.com
  properties:
  - url: https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/web-api.html
    type: Documentation
  - url: https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/build-your-first-commerce-app.html
    type: Getting Started
  - url: https://developer.salesforce.com/docs/commerce/salesforce-commerce/references/shopper-products.html
    type: Reference
  - url: https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/slas.html
    type: Authentication
  description: The Salesforce Commerce Cloud Shopper APIs (SCAPI) are a modern set of REST APIs for building B2C Commerce storefronts and headless commerce experiences. They cover shopper authentication, products, search, baskets, orders, and customer account management.
- aid: salesforce:salesforce-field-service-api
  name: Salesforce Field Service API
  tags:
  - Field Service
  - Mobile
  - Scheduling
  - Service Cloud
  - Work Orders
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.field_service_dev.meta/field_service_dev/
  baseURL: https://{instance}.salesforce.com/services/data/v{version}
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.field_service_dev.meta/field_service_dev/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.field_service_dev.meta/field_service_dev/fsl_developer_guide_intro.htm
    type: Getting Started
  description: The Salesforce Field Service API provides access to Field Service Lightning data and operations including work orders, service appointments, resource scheduling, and mobile workforce management. It enables custom integrations with scheduling systems and field service tools.
- aid: salesforce:salesforce-health-cloud-api
  name: Salesforce Health Cloud API
  tags:
  - Clinical
  - FHIR
  - Health Cloud
  - Healthcare
  - Patients
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.health_cloud_object_reference.meta/health_cloud_object_reference/
  baseURL: https://{instance}.salesforce.com/services/data/v{version}
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.health_cloud_object_reference.meta/health_cloud_object_reference/
    type: Documentation
  - url: https://developer.salesforce.com/docs/health/health-cloud/guide/health-cloud-intro.html
    type: Getting Started
  - url: https://developer.salesforce.com/docs/health/health-cloud/guide/fhir-api-overview.html
    type: Reference
  description: The Salesforce Health Cloud API provides FHIR R4-compliant REST APIs and platform APIs for accessing patient and provider data in Health Cloud. It enables healthcare applications to interact with clinical data, care plans, patient timelines, and care team information.
- aid: salesforce:salesforce-financial-services-cloud-api
  name: Salesforce Financial Services Cloud API
  tags:
  - Banking
  - CRM
  - Financial Services
  - Insurance
  - Wealth Management
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.financial_services_cloud_object_reference.meta/financial_services_cloud_object_reference/
  baseURL: https://{instance}.salesforce.com/services/data/v{version}
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.financial_services_cloud_object_reference.meta/financial_services_cloud_object_reference/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.financial_services_cloud_object_reference.meta/financial_services_cloud_object_reference/sforce_api_objects_interaction.htm
    type: Reference
  description: The Salesforce Financial Services Cloud API exposes financial services-specific data objects including financial accounts, assets, liabilities, financial goals, and household relationships. It enables wealth management, banking, and insurance applications to integrate with Salesforce CRM data.
- aid: salesforce:salesforce-experience-cloud-api
  name: Salesforce Experience Cloud API
  tags:
  - Communities
  - Experience Cloud
  - Portals
  - Sites
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.communities_dev.meta/communities_dev/
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/connect/communities
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.communities_dev.meta/communities_dev/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.communities_dev.meta/communities_dev/communities_dev_intro.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.communities_dev.meta/communities_dev/communities_dev_network.htm
    type: Reference
  description: The Salesforce Experience Cloud API provides REST access to Experience Cloud (formerly Community Cloud) data including community membership, navigation, managed content, and knowledge articles. It enables developers to build custom portals and community-driven experiences.
- aid: salesforce:salesforce-mulesoft-anypoint-platform-api
  name: Salesforce MuleSoft Anypoint Platform API
  tags:
  - API Management
  - Integration
  - iPaaS
  - MuleSoft
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/
  baseURL: https://anypoint.mulesoft.com/accounts/api
  properties:
  - url: https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/
    type: Documentation
  - url: https://docs.mulesoft.com/general/
    type: Getting Started
  - url: https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/
    type: Reference
  - url: https://docs.mulesoft.com/access-management/
    type: Authentication
  - url: https://github.com/mulesoft
    type: GitHubRepository
  description: The MuleSoft Anypoint Platform API provides programmatic access to the MuleSoft integration platform including API Manager, Runtime Manager, Exchange, and Access Management. It enables automation of API lifecycle management, deployment, and monitoring operations.
- aid: salesforce:salesforce-tableau-rest-api
  name: Salesforce Tableau REST API
  tags:
  - Analytics
  - Business Intelligence
  - Dashboards
  - Data Visualization
  - Tableau
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm
  baseURL: https://{server}/api/{version}
  properties:
  - url: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm
    type: Documentation
  - url: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_get_started.htm
    type: Getting Started
  - url: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref.htm
    type: Reference
  - url: https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_auth.htm
    type: Authentication
  - url: https://help.tableau.com/current/api/tableau-api-guide/en-us/
    type: Client Libraries
  - url: https://github.com/tableau
    type: GitHubRepository
  description: The Tableau REST API enables developers to programmatically manage Tableau Server and Tableau Cloud resources including workbooks, data sources, views, sites, users, and groups. It supports automation of Tableau administration and content lifecycle operations.
- aid: salesforce:salesforce-lightning-web-components
  name: Salesforce Lightning Web Components (LWC)
  description: Lightning Web Components (LWC) is Salesforce's standards-based JavaScript framework for building UI components on the Salesforce platform. It uses modern web standards including custom elements, templates, and decorators, and provides a reactive wire service for accessing Salesforce data via Lightning Data Service. LWC is the recommended component model for Lightning Experience, Experience Cloud, and Salesforce mobile, superseding the legacy Aura framework.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/platform/lwc/overview
  baseURL: https://developer.salesforce.com/docs/platform/lwc
  properties:
  - url: https://developer.salesforce.com/docs/platform/lwc/overview
    type: Documentation
  - url: https://developer.salesforce.com/docs/platform/lwc/guide/get-started-lwc.html
    type: Getting Started
  - url: https://developer.salesforce.com/docs/platform/lwc/guide/reference.html
    type: Reference
  - url: https://developer.salesforce.com/docs/platform/lwc/guide/reference-ui-api.html
    type: Reference
  - url: https://github.com/salesforce/lwc
    type: GitHubRepository
  tags:
  - Components
  - JavaScript
  - Lightning
  - LWC
  - UI Framework
- aid: salesforce:salesforce-aura-components
  name: Salesforce Aura Components
  description: Salesforce Aura Components is the legacy JavaScript component framework for building dynamic web applications on the Salesforce platform. It provides a data binding model, event system, and Apex controller integration through the Aura framework. Salesforce recommends migrating to Lightning Web Components for new development, but Aura components remain fully supported and can coexist with LWC components on the same page.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/intro_framework.htm
  baseURL: https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/intro_framework.htm
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/qs_aotp_app.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/ref_component_library.htm
    type: Reference
  tags:
  - Aura
  - Components
  - JavaScript
  - Legacy
  - Lightning
- aid: salesforce:salesforce-lightning-design-system
  name: Salesforce Lightning Design System (SLDS)
  description: The Salesforce Lightning Design System (SLDS) provides HTML and CSS component blueprints, design tokens, and utility classes for building applications visually consistent with Salesforce Lightning Experience. Developers reference SLDS in Lightning Web Components, Aura components, and Visualforce pages to match Salesforce's design language without including SLDS directly, as it is automatically available in the Lightning runtime.
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://www.lightningdesignsystem.com/
  baseURL: https://www.lightningdesignsystem.com
  properties:
  - url: https://www.lightningdesignsystem.com/
    type: Documentation
  - url: https://developer.salesforce.com/docs/platform/lwc/guide/create-components-css-slds.html
    type: Getting Started
  - url: https://github.com/salesforce/design-system-react
    type: GitHubRepository
  tags:
  - Components
  - CSS
  - Design System
  - Lightning
  - UI
- aid: salesforce:salesforce-agentforce-agent-api
  name: Salesforce Agentforce Agent API
  tags:
  - Agentforce
  - Agents
  - AI
  - Conversational AI
  - GenAI
  - REST
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api.html
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/agent
  properties:
  - url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api.html
    type: Documentation
  - url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api-get-started.html
    type: Getting Started
  - url: https://developer.salesforce.com/docs/ai/agentforce/references/agent-api
    type: Reference
  - url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api-examples.html
    type: Examples
  description: The Salesforce Agentforce Agent API is a REST API that enables developers to communicate with AI agents directly, starting sessions, sending messages, receiving responses, and ending sessions. It supports embedding agents on websites, creating headless agents for automation, and building multi-agent ecosystems.
- aid: salesforce:salesforce-models-api
  name: Salesforce Models API
  tags:
  - Agentforce
  - AI
  - Einstein
  - GenAI
  - LLM
  - Machine Learning
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/ai/agentforce/guide/models-api.html
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/einstein
  properties:
  - url: https://developer.salesforce.com/docs/ai/agentforce/guide/models-api.html
    type: Documentation
  - url: https://developer.salesforce.com/docs/ai/agentforce/guide/models-get-started.html
    type: Getting Started
  - url: https://developer.salesforce.com/docs/ai/agentforce/guide/access-models-api-with-rest.html
    type: Reference
  - url: https://developer.salesforce.com/docs/ai/agentforce/guide/supported-models.html
    type: Documentation
  description: The Salesforce Models API provides Apex classes and REST endpoints that connect applications to large language models (LLMs) from Salesforce partners including Anthropic, Google, and OpenAI. It supports chat conversations, text generation, embeddings, and feedback collection, with all requests going through the Einstein Trust Layer.
- aid: salesforce:salesforce-interaction-service-api
  name: Salesforce Interaction Service API
  tags:
  - BYOC
  - Customer Service
  - Messaging
  - Omnichannel
  - Service Cloud
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/service/interaction-service-api/overview
  baseURL: https://{instance}.salesforce.com/services/data/v{version}
  properties:
  - url: https://developer.salesforce.com/docs/service/interaction-service-api/overview
    type: Documentation
  - url: https://developer.salesforce.com/docs/service/interaction-service-api/guide/get-started.html
    type: Getting Started
  - url: https://developer.salesforce.com/docs/service/interaction-service-api/references
    type: Reference
  - url: https://developer.salesforce.com/docs/service/interaction-service-api/guide/authorization.html
    type: Authentication
  description: The Salesforce Interaction Service API enables automation and customization of the Bring Your Own Channel (BYOC) experience for messaging. It sends inbound messaging interactions from external end-user clients to Salesforce, including static content messages, typing indicators, file attachments, and message status updates.
- aid: salesforce:salesforce-b2b-commerce-api
  name: Salesforce B2B Commerce API
  tags:
  - B2B Commerce
  - Cart
  - Commerce
  - Orders
  - Products
  - Storefront
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-d2c-comm-storefront-apis-parent.html
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/commerce
  properties:
  - url: https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-d2c-comm-storefront-apis-parent.html
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.b2b_b2c_comm_dev.meta/b2b_b2c_comm_dev/b2b_b2c_comm_dev_guide.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_commerce.htm
    type: Reference
  description: The Salesforce B2B Commerce API provides REST endpoints for handling commerce data in B2B and D2C storefronts. It offers support for address management, cart management, checkout processing, order management, product handling, pricing, promotions, tax management, wishlist management, and search settings.
- aid: salesforce:salesforce-actions-api
  name: Salesforce Actions API
  tags:
  - Actions
  - Automation
  - CRM
  - Flow
  - Invocable
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_action.meta/api_action/actions_intro.htm
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/actions
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_action.meta/api_action/actions_intro.htm
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_action.meta/api_action/actions_intro_overview.htm
    type: Getting Started
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_actions_invocable.htm
    type: Reference
  description: The Salesforce Actions API provides a unified interface for invoking standard and custom actions across the Salesforce platform. It supports Apex actions, Flow actions, quick actions, and invocable actions, enabling developers to programmatically trigger automation and business logic from REST API calls.
- aid: salesforce:salesforce-iot-api
  name: Salesforce IoT REST API
  tags:
  - Events
  - IoT
  - Orchestrations
  - REST
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_iot.meta/api_iot/
  baseURL: https://{instance}.salesforce.com/services/data/v{version}/iot
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_iot.meta/api_iot/
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_iot.meta/api_iot/qs_auth.htm
    type: Authentication
  - url: https://developer.salesforce.com/docs/atlas.en-us.api_iot.meta/api_iot/examples_overview.htm
    type: Reference
  description: The Salesforce IoT REST API provides programmatic access to Salesforce IoT data including contexts, orchestrations, and usage data. It enables developers to manage IoT events and orchestration rules for processing device data and triggering automated business actions.
- aid: salesforce:salesforce-service-cloud-voice-api
  name: Salesforce Service Cloud Voice API
  tags:
  - Contact Center
  - CTI
  - Service Cloud
  - Telephony
  - Voice
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_intro.htm
  baseURL: https://{instance}.salesforce.com/services/data/v{version}
  properties:
  - url: https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_intro.htm
    type: Documentation
  - url: https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_rest_overview.htm
    type: Reference
  - url: https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_rest_authorization.htm
    type: Authentication
  - url: https://developer.salesforce.com/docs/atlas.en-us.voice_pt_developer_guide.meta/voice_pt_developer_guide/voice_pt_dev_guide.htm
    type: Documentation
  description: The Salesforce Service Cloud Voice API provides Telephony Integration REST API and Voice Toolkit API for programmatically managing voice calls and integrating telephony systems with Salesforce. It supports both Amazon Connect and partner telephony implementations for unified contact center experiences.
- aid: salesforce:salesforce-mobile-sdk
  name: Salesforce Mobile SDK
  tags:
  - Android
  - iOS
  - Mobile
  - React Native
  - SDK
  image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
  humanURL: https://developer.salesforce.com/docs/platform/mobile-sdk/overview
  baseURL: https://developer.salesforce.com/docs/platform/mobile-sdk
  properties:
  - url: https://developer.salesforce.com/docs/platform/mobile-sdk/overview
    type: Documentation
  - url: https://developer.salesforce.com/docs/platform/mobile-sdk/guide/intro.html
    type: Getting Started
  - url: https://developer.salesforce.com/developer-centers/mobile
    type: Portal
  - url: https://github.com/forcedotcom/SalesforceMobileSDK-Android
    type: GitHubRepository
  description: The Salesforce Mobile SDK provides libraries and tools for building native and hybrid mobile applications on iOS and Android that integrate with the Salesforce platform. It supports Swift, Objective-C, Java, Kotlin, and React Native development with built-in authentication, data synchronization, and offline capabilities.
- aid: salesforce:salesforce-salesforce
  name: Salesforce
  tags:
  - CRM
  humanURL: https://developer.salesforce.com/
  properties:
  - url: https://developer.salesforce.com/
    type: Documentation
  - url: openapi/salesforce-openapi.yml
    type: OpenAPI
  description: Salesforce is a cloud-based customer relationship management (CRM) platform that helps organizations manage and grow customer relationships across the entire lifecycle. It unifies sales, service, marketing, and commerce so teams can track leads and opportunities, support customers, run campaigns, and transact in one place.
name: Salesforce
tags:
- AI
- Analytics
- Cloud
- Commerce
- CRM
- Customer Service
- Enterprise
- Marketing
- Platform
- Sales
type: Index
image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
access: 3rd-Party
created: '2025-06-05'
modified: '2026-04-07'
position: Consumer
description: Salesforce is a cloud-based customer relationship management (CRM) platform that provides a comprehensive suite of enterprise applications for sales, service, marketing, and more.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

