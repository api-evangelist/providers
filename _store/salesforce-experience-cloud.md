---
aid: salesforce-experience-cloud
url: https://raw.githubusercontent.com/api-evangelist/salesforce-experience-cloud/refs/heads/main/apis.yml
apis:
- name: Experience Cloud Sites API
  description: Manage Experience Cloud sites, themes, and configurations. Provides programmatic access to create, update, and retrieve site settings, branding, and navigation for digital experience portals.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/salesforce-logo.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.exp_cloud_apis.meta/exp_cloud_apis/
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0
  tags:
  - CMS
  - Communities
  - Configuration
  - Digital Experiences
  - Sites
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.exp_cloud_apis.meta/exp_cloud_apis/
  - type: OpenAPI
    url: openapi/salesforce-experience-cloud-sites-openapi.yml
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.communities_dev.meta/communities_dev/communities_dev_intro_before.htm
- name: Connect REST API (Communities)
  description: Access community data, feeds, topics, and user engagement features. The Connect REST API provides endpoints for social collaboration, content sharing, and community management within Experience Cloud sites.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/salesforce-logo.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/connect
  tags:
  - Chatter
  - Communities
  - Feeds
  - Social
  - Topics
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/
  - type: OpenAPI
    url: openapi/salesforce-experience-cloud-connect-communities-openapi.yml
  - type: Postman Collection
    url: https://www.postman.com/salesforce-developers/workspace/salesforce-developers
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/features_communities.htm
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/quickstart_dev_org.htm
- name: CMS Connect API
  description: Manage content, channels, and media in Experience Cloud CMS. Supports creating, updating, and delivering managed content across channels for headless content delivery and site publishing.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/salesforce-logo.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_cms.htm
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/connect/cms
  tags:
  - Channels
  - CMS
  - Content
  - Media
  - Publishing
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_cms.htm
  - type: OpenAPI
    url: openapi/salesforce-experience-cloud-cms-connect-openapi.yml
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_cms_content.htm
  - type: Getting Started
    url: https://developer.salesforce.com/docs/platform/cms/guide/cms-developer-guide.html
- name: Salesforce REST API
  description: Core REST API for accessing Salesforce objects and data. Provides CRUD operations on standard and custom objects, query execution, and metadata access used as the foundation for Experience Cloud data integrations.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/salesforce-logo.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0
  tags:
  - CRUD
  - Data
  - Objects
  - Platform
  - REST
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/
  - type: OpenAPI
    url: openapi/salesforce-experience-cloud-rest-api-openapi.yml
  - type: Postman Collection
    url: https://www.postman.com/salesforce-developers/workspace/salesforce-developers
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
- name: Experience Cloud Templates API
  description: Retrieve and manage Experience Cloud site templates including Build Your Own and Microsite LWR templates. Supports programmatic theme and branding configuration for digital experience portals.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/salesforce-logo.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.exp_cloud_apis.meta/exp_cloud_apis/
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0
  tags:
  - Branding
  - Design
  - LWR
  - Templates
  - Themes
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.exp_cloud_apis.meta/exp_cloud_apis/
  - type: OpenAPI
    url: openapi/salesforce-experience-cloud-templates-openapi.yml
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.exp_cloud_lwr.meta/exp_cloud_lwr/template_overview.htm
- name: GraphQL API
  description: Query Salesforce data using GraphQL for Experience Cloud. Offers a flexible query language for retrieving exactly the data needed, reducing over-fetching and improving performance for digital experiences.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/salesforce-logo.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.graphql.meta/graphql/
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/graphql
  tags:
  - Data
  - GraphQL
  - Performance
  - Query
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.graphql.meta/graphql/
  - type: OpenAPI
    url: openapi/salesforce-experience-cloud-graphql-openapi.yml
  - type: Schema
    url: https://developer.salesforce.com/docs/atlas.en-us.graphql.meta/graphql/graphql_schema.htm
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.graphql.meta/graphql/
- name: CMS Managed Content API
  description: Retrieve and search published managed content versions for Experience Cloud sites. Provides endpoints for querying managed content delivery channels and searching content across workspaces.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/salesforce-logo.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_managed_content_resources.htm
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/connect/cms/delivery
  tags:
  - Channels
  - Content Management
  - Delivery
  - Headless CMS
  - Managed Content
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_managed_content_resources.htm
  - type: OpenAPI
    url: openapi/salesforce-experience-cloud-cms-managed-content-openapi.yml
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_managed_content_enhanced_resources.htm
  - type: Getting Started
    url: https://developer.salesforce.com/docs/platform/cms/guide/cms-dev-retrieve-cms-content-with-a-connected-app.html
- name: CMS Delivery API
  description: Delivers CMS content to external applications and headless frontends. Enables content retrieval by channel, content type, and content key for building decoupled digital experiences.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/salesforce-logo.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_cms_delivery_content.htm
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/connect/cms/delivery
  tags:
  - Channels
  - CMS
  - Content Delivery
  - Headless
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_cms_delivery_content.htm
  - type: OpenAPI
    url: openapi/salesforce-experience-cloud-cms-delivery-openapi.yml
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_cms_contents.htm
- name: User Interface API
  description: Access record data, layouts, list views, and navigation items for building custom user interfaces. Powers Lightning web components in Experience Cloud sites with metadata-driven UI rendering.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/salesforce-logo.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi/ui_api_get_started.htm
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/ui-api
  tags:
  - Layouts
  - Lightning
  - Navigation
  - Records
  - User Interface
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi/ui_api_get_started.htm
  - type: OpenAPI
    url: openapi/salesforce-experience-cloud-user-interface-openapi.yml
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.exp_cloud_lwr.meta/exp_cloud_lwr/get_started_comp_api.htm
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi/ui_api_get_started.htm
- name: Metadata API (Experience Cloud)
  description: Deploy and retrieve Experience Cloud site configurations, navigation menus, and digital experience bundles. Enables programmatic management of ExperienceBundle and Network metadata types for CI/CD workflows.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/salesforce-logo.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_experiencebundle.htm
  baseURL: https://yourInstance.salesforce.com/services/Soap/m/59.0
  tags:
  - CI/CD
  - Configuration
  - Deployment
  - DevOps
  - Metadata
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_intro.htm
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_experiencebundle.htm
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_digitalexperiencebundle.htm
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_network.htm
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_types_list.htm
- name: LWR Sites API
  description: Build and customize Lightning Web Runtime sites for Experience Cloud. Provides documentation for creating LWR-based digital experiences with custom components, page layouts, and theme configurations.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/salesforce-logo.svg
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.exp_cloud_lwr.meta/exp_cloud_lwr/intro.htm
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0
  tags:
  - Components
  - Lightning Web Runtime
  - LWR
  - Performance
  - Sites
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.exp_cloud_lwr.meta/exp_cloud_lwr/intro.htm
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.exp_cloud_lwr.meta/exp_cloud_lwr/get_started.htm
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.exp_cloud_lwr.meta/exp_cloud_lwr/get_started_navigation.htm
name: Salesforce Experience Cloud
tags:
- CMS
- Communities
- CRM
- Customer Portal
- Digital Experience
- Experience Cloud
- Partner Portal
type: Contract
image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/salesforce-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for building and managing Salesforce Experience Cloud sites, communities, and digital experiences including content management, theming, navigation, and Lightning Web Runtime powered portals.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

