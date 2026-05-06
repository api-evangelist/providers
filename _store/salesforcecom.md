---
aid: salesforcecom
url: https://raw.githubusercontent.com/api-evangelist/salesforcecom/refs/heads/main/apis.yml
name: Salesforce
description: Salesforce is a global leader in customer relationship management (CRM) software and cloud-based applications. The Salesforce Platform provides a comprehensive suite of APIs for sales, service, marketing, commerce, integration, analytics, and platform development including Agentforce AI capabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CRM
  - Cloud
  - Sales
  - Marketing
  - Automation
  - AI
access: 3rd-Party
created: '2026-03-24'
modified: '2026-05-02'
x-profiled: 2026-05
specificationVersion: '0.19'
apis:
  - aid: salesforcecom:rest-api
    name: Salesforce REST API
    description: The Salesforce REST API provides programmatic access to your Salesforce org data, letting you create, read, update, and delete records, execute queries, and manage org metadata. Supports OAuth 2.0 authentication and returns JSON or XML responses.
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest
    tags:
      - CRM
      - Data
      - Records
      - Query
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest
      - type: Versioning
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/dome_versions.htm
      - type: OpenAPI
        url: openapi/salesforcecom-rest-openapi.yml
      - type: Summary
        data:
          numberOfAPITags: 6
          numberOfAPIGetMethods: 9
          numberOfAPIPostMethods: 3
          numberOfAPIPatchMethods: 1
          numberOfAPIDeleteMethods: 1
          numberOfAPIOperations: 14
  - aid: salesforcecom:bulk-api
    name: Salesforce Bulk API 2.0
    description: The Salesforce Bulk API 2.0 is a specialized REST API for loading large numbers of records asynchronously. It is optimized for processing jobs that contain large data sets, supporting insert, update, upsert, delete, and query operations.
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch
    tags:
      - Bulk Data
      - ETL
      - Async
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch
  - aid: salesforcecom:streaming-api
    name: Salesforce Streaming API
    description: The Salesforce Streaming API lets you subscribe to changes in Salesforce data using push technology based on the Bayeux protocol. It enables real-time notifications via PushTopic events, Change Data Capture, Platform Events, and Generic Events.
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming
    tags:
      - Streaming
      - Events
      - Real-Time
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming
  - aid: salesforcecom:metadata-api
    name: Salesforce Metadata API
    description: The Salesforce Metadata API enables you to retrieve, deploy, create, update, and delete customization information such as custom object definitions and page layouts for your organization. Used primarily by developer tools and CI/CD pipelines.
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta
    tags:
      - Metadata
      - DevOps
      - Configuration
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta
  - aid: salesforcecom:connect-api
    name: Salesforce Connect REST API
    description: Salesforce Connect REST API provides access to Salesforce Experience Cloud, Files, Chatter, and community features. Enables social features, file management, user feeds, and collaboration across Salesforce orgs.
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi
    tags:
      - Connect
      - Chatter
      - Community
      - Files
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi
  - aid: salesforcecom:marketing-cloud-api
    name: Salesforce Marketing Cloud REST API
    description: The Marketing Cloud REST API provides access to Marketing Cloud data and functionality including email, SMS, push messaging, contact management, journeys, and data extensions. Enables programmatic management of marketing campaigns and subscriber data.
    humanURL: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rest-api.html
    tags:
      - Marketing
      - Email
      - SMS
      - Campaigns
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rest-api.html
  - aid: salesforcecom:commerce-cloud-api
    name: Salesforce B2C Commerce API
    description: The Salesforce B2C Commerce API (SCAPI) provides RESTful access to commerce storefront functionality including products, catalogs, pricing, inventory, orders, customers, and baskets. Enables headless commerce implementations.
    humanURL: https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/b2c-commerce-api.html
    tags:
      - Commerce
      - Ecommerce
      - Storefront
      - B2C
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/b2c-commerce-api.html
  - aid: salesforcecom:agentforce-api
    name: Salesforce Agentforce API
    description: The Salesforce Agentforce API enables developers to build, deploy, and manage AI agents that can autonomously complete tasks across the Salesforce platform. Supports agent creation, customization, and integration with the Agentforce 360 Platform.
    humanURL: https://developer.salesforce.com/agentforce
    tags:
      - AI
      - Agents
      - Automation
      - Agentforce
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/agentforce
  - aid: salesforcecom:mulesoft-api
    name: Salesforce MuleSoft Anypoint Platform API
    description: The MuleSoft Anypoint Platform API enables programmatic management of APIs, integrations, and integration assets. Supports API lifecycle management, deployment, analytics, and policy enforcement across the MuleSoft integration platform.
    humanURL: https://docs.mulesoft.com/mule-runtime/latest/
    tags:
      - Integration
      - MuleSoft
      - API Management
      - iPaaS
    properties:
      - type: Documentation
        url: https://docs.mulesoft.com/mule-runtime/latest/
common:
  - type: Website
    url: https://www.salesforce.com
  - type: Portal
    url: https://developer.salesforce.com
  - type: Documentation
    url: https://developer.salesforce.com/docs
  - type: APILibrary
    url: https://developer.salesforce.com/docs/apis
  - type: Blog
    url: https://developer.salesforce.com/blogs
  - type: Community
    url: https://trailblazer.salesforce.com
  - type: Pricing
    url: https://www.salesforce.com/editions-pricing/
  - type: Status
    url: https://status.salesforce.com
  - type: Support
    url: https://help.salesforce.com
  - type: Signup
    url: https://www.salesforce.com/form/signup/freetrial-salesforce/
  - type: LinkedIn
    url: https://www.linkedin.com/company/salesforce
  - type: Twitter
    url: https://twitter.com/salesforce
  - type: GitHubOrganization
    url: https://github.com/forcedotcom
  - type: GitHubOrganization
    url: https://github.com/salesforcecli
  - type: CLI
    url: https://github.com/salesforcecli/cli
  - type: PostmanWorkspace
    url: https://www.postman.com/salesforce-developers/salesforce-developers
  - type: ChangeLog
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/api_rest_whats_new.htm
  - type: Trailhead
    url: https://trailhead.salesforce.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
