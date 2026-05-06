---
aid: confluence
name: Confluence
description: APIs for Atlassian Confluence - team collaboration and knowledge management software.
image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
tags:
  - Collaboration
  - Content Management
  - Documentation
  - Knowledge Base
  - Wiki
created: '2024'
modified: '2026-05-04'
url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/
apis:
  - name: Confluence Cloud REST API v1
    description: Primary REST API for Confluence Cloud for content, spaces, and user management.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Cloud
      - Content
      - Rest
      - Spaces
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/
      - type: OpenAPI
        url: https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
      - type: CodeExamples
        url: https://developer.atlassian.com/cloud/confluence/rest-api-examples/
      - type: GettingStarted
        url: https://developer.atlassian.com/cloud/confluence/getting-started/
      - type: ChangeLog
        url: https://developer.atlassian.com/cloud/confluence/changelog/
      - type: SDK
        url: https://www.postman.com/api-evangelist/atlassian-confluence/collection/k3y2x73/atlassian-confluence-cloud
  - name: Confluence Cloud REST API v2
    description: Next generation Confluence Cloud REST API with improved performance and new features.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Cloud
      - Pages
      - Rest
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/
      - type: OpenAPI
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-spec/
      - type: OpenAPI
        url: openapi/confluence-cloud-v2.yml
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
      - type: GettingStarted
        url: https://developer.atlassian.com/cloud/confluence/getting-started/
      - type: ChangeLog
        url: https://developer.atlassian.com/cloud/confluence/changelog/
      - type: SDK
        url: https://www.postman.com/api-reference-library/atlassian-cloud/collection/0a0hjxk/the-confluence-cloud-rest-api-v2
  - name: Confluence Content Properties API
    description: Store and retrieve custom data against Confluence content.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-properties/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Custom Data
      - Metadata
      - Properties
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-properties/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Search API
    description: Search for content in Confluence using CQL (Confluence Query Language).
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-search/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Cql
      - Query
      - Search
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-search/
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/advanced-searching-using-cql/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Content API
    description: Create, read, update, delete, and archive content including pages and blog posts in Confluence Cloud.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Blog Posts
      - Content
      - Create
      - Pages
      - Update
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Space API
    description: Manage Confluence spaces including creation, configuration, permissions, and settings.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-space/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Permissions
      - Settings
      - Spaces
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-space/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Content Labels API
    description: Add, remove, and manage labels on Confluence content for organization and discovery.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-labels/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Content Organization
      - Labels
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-labels/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Analytics API
    description: Retrieve analytics data including content views and viewer counts for Confluence Cloud.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-analytics/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Analytics
      - Metrics
      - Views
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-analytics/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Audit API
    description: Access and manage audit log records for compliance and security tracking in Confluence Cloud.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-audit/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Audit
      - Compliance
      - Logging
      - Security
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-audit/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Template API
    description: Manage content templates and blueprints for standardized page creation in Confluence Cloud.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-template/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Blueprints
      - Content Creation
      - Templates
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-template/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Group API
    description: Manage user groups and group membership in Confluence Cloud.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-group/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Groups
      - Membership
      - Users
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-group/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Users API
    description: Retrieve user information, manage user properties, and check permissions in Confluence Cloud.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-users/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Permissions
      - Profiles
      - Users
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-users/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Content States API
    description: Manage content workflow states such as draft, in progress, and review in Confluence Cloud.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-states/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Content States
      - Status
      - Workflow
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-states/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Content Restrictions API
    description: Manage read and update restrictions on Confluence content for access control.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-restrictions/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Access Control
      - Permissions
      - Restrictions
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-restrictions/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Space Permissions API
    description: Manage permissions for Confluence spaces including user and group access levels.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-space-permissions/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Access Control
      - Authorization
      - Space Permissions
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-space-permissions/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence GraphQL API
    description: Query Confluence data using GraphQL for efficient cross-product data retrieval with field-level precision.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/graphql/
    baseURL: https://your-domain.atlassian.net/gateway/api/graphql
    tags:
      - Cloud
      - Graphql
      - Query
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/graphql/
      - type: Documentation
        url: https://developer.atlassian.com/platform/atlassian-graphql-api/
  - name: Confluence Data Center REST API
    description: REST API for Confluence Data Center and Server for on-premise content, space, and user management.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/server/confluence/confluence-server-rest-api/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Data Center
      - On-Premise
      - Rest
      - Server
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/server/confluence/confluence-server-rest-api/
      - type: APIReference
        url: https://developer.atlassian.com/server/confluence/rest/v9217/
      - type: CodeExamples
        url: https://developer.atlassian.com/server/confluence/confluence-rest-api-examples/
      - type: DeveloperPortal
        url: https://developer.atlassian.com/server/confluence/
      - type: ChangeLog
        url: https://developer.atlassian.com/server/confluence/changelog/
  - name: Confluence Content Attachments API
    description: Upload, retrieve, update, and delete file attachments on Confluence content.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content---attachments/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Attachments
      - Files
      - Uploads
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content---attachments/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Content Body API
    description: Convert content body representations between storage, editor, view, and export formats.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-body/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Content Body
      - Conversion
      - Formats
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-body/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Content Children and Descendants API
    description: Retrieve children and descendants of Confluence content for navigating content hierarchies.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content---children-and-descendants/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Children
      - Descendants
      - Hierarchy
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content---children-and-descendants/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Content Macro Body API
    description: Retrieve the body of a macro in Confluence content by macro ID.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content---macro-body/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Content Body
      - Macros
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content---macro-body/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Content Permissions API
    description: Check content permissions for users to determine read and update access.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-permissions/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Access Control
      - Content
      - Permissions
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-permissions/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Content Versions API
    description: Manage content version history including retrieval, restoration, and deletion of versions.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-versions/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Content Management
      - History
      - Versions
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-versions/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Content Watches API
    description: Manage content and space watches to receive notifications on updates.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-watches/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Notifications
      - Subscriptions
      - Watches
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-watches/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Dynamic Modules API
    description: Register and manage dynamic modules for Confluence Connect apps.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-dynamic-modules/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Connect Apps
      - Extensions
      - Modules
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-dynamic-modules/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Experimental API
    description: Experimental endpoints for Confluence Cloud that may change or be removed.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-experimental/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Experimental
      - Preview
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-experimental/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Label Info API
    description: Retrieve information about labels used across Confluence content.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-label-info/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Information
      - Labels
      - Metadata
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-label-info/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Long-Running Task API
    description: Monitor the status and results of long-running asynchronous tasks in Confluence.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-long-running-task/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Async
      - Long-Running
      - Tasks
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-long-running-task/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Relation API
    description: Manage relationships between Confluence entities such as content and users.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-relation/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Associations
      - Links
      - Relations
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-relation/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Settings API
    description: Retrieve and manage Confluence site settings and configuration.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-settings/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Configuration
      - Settings
      - Site
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-settings/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Space Settings API
    description: Manage settings for individual Confluence spaces.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-space-settings/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Configuration
      - Space Settings
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-space-settings/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence Themes API
    description: Retrieve theme information for Confluence spaces and the global site.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-themes/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Appearance
      - Customization
      - Themes
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-themes/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence User Properties API
    description: Store and retrieve custom properties associated with Confluence users.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-user-properties/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Custom Data
      - Metadata
      - User Properties
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-user-properties/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth
  - name: Confluence V2 Page API
    description: Create, retrieve, update, and delete pages using the Confluence Cloud REST API v2.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Content
      - Pages
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Blog Post API
    description: Create, retrieve, update, and delete blog posts using the Confluence Cloud REST API v2.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-blog-post/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Blog Posts
      - Content
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-blog-post/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Space API
    description: Retrieve and manage spaces using the Confluence Cloud REST API v2.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Spaces
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Comment API
    description: Create, retrieve, update, and delete comments on pages and blog posts using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-comment/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Comments
      - Discussions
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-comment/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Attachment API
    description: Manage file attachments on content using the Confluence Cloud REST API v2.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-attachment/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Attachments
      - Files
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-attachment/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Label API
    description: Manage labels on content using the Confluence Cloud REST API v2.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-label/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Labels
      - Organization
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-label/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Task API
    description: Retrieve and manage tasks within Confluence content using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-task/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Action Items
      - Tasks
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-task/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Whiteboard API
    description: Create and manage whiteboards in Confluence using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - V2
      - Visual Collaboration
      - Whiteboards
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Custom Content API
    description: Create and manage custom content types in Confluence using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-custom-content/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Custom Content
      - Extensions
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-custom-content/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Ancestors API
    description: Retrieve ancestor pages in the content hierarchy using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-ancestors/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Ancestors
      - Hierarchy
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-ancestors/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Children API
    description: Retrieve child pages and content in the hierarchy using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-children/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Children
      - Hierarchy
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-children/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Descendants API
    description: Retrieve all descendant pages in the content hierarchy using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-descendants/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Descendants
      - Hierarchy
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-descendants/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Version API
    description: Manage content versions and version history using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-version/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - History
      - V2
      - Versions
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-version/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Like API
    description: Manage likes on Confluence content using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-like/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Engagement
      - Likes
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-like/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Space Permissions API
    description: Manage space-level permissions using the Confluence Cloud REST API v2.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Access Control
      - Space Permissions
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Space Properties API
    description: Store and retrieve custom properties on Confluence spaces using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-properties/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Metadata
      - Space Properties
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-properties/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Space Roles API
    description: Manage roles assigned to users and groups within Confluence spaces using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-roles/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Authorization
      - Space Roles
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-roles/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Content Properties API
    description: Store and manage custom properties on content using the Confluence Cloud REST API v2.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-content-properties/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Content Properties
      - Metadata
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-content-properties/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Folder API
    description: Create and manage folders for organizing pages in Confluence using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-folder/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Folders
      - Organization
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-folder/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Database API
    description: Create and manage databases in Confluence using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-database/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Databases
      - Structured Data
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-database/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Smart Link API
    description: Manage smart links for rich content previews in Confluence using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Previews
      - Smart Links
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Operation API
    description: Check permitted operations on content using the Confluence Cloud REST API v2.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-operation/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Operations
      - Permissions
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-operation/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 User API
    description: Retrieve user information and details using the Confluence Cloud REST API v2.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-user/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Profiles
      - Users
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-user/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 App Properties API
    description: Store and retrieve app-specific properties in Confluence using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-app-properties/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - App Properties
      - Extensions
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-app-properties/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Content API
    description: Manage content including conversions and permissions using the Confluence Cloud REST API v2.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-content/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Content
      - Management
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-content/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Data Policies API
    description: Retrieve data policy information for Confluence workspaces using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-data-policies/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Data Policies
      - Governance
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-data-policies/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Classification Level API
    description: Manage content classification levels for data protection in Confluence using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-classification-level/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Classification
      - Data Protection
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-classification-level/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Redactions API
    description: Manage content redactions for sensitive information in Confluence using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-redactions/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Data Protection
      - Redactions
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-redactions/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
  - name: Confluence V2 Admin Key API
    description: Manage admin API keys for Confluence Cloud using the v2 API.
    image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-admin-key/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Admin
      - Api Keys
      - V2
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-admin-key/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#authentication
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://developer.atlassian.com/
  - type: Documentation
    url: https://www.atlassian.com/software/confluence
  - type: GettingStarted
    url: https://developer.atlassian.com/cloud/confluence/getting-started/
  - type: DeveloperPortal
    url: https://developer.atlassian.com/cloud/confluence/
  - type: RateLimits
    url: https://developer.atlassian.com/cloud/confluence/rate-limiting/
  - type: ChangeLog
    url: https://developer.atlassian.com/cloud/confluence/changelog/
  - type: ChangeLog
    url: https://developer.atlassian.com/changelog/
  - type: Support
    url: https://support.atlassian.com/
  - type: Support
    url: https://community.atlassian.com/
  - type: Support
    url: https://community.developer.atlassian.com/
  - type: StatusPage
    url: https://status.atlassian.com/
  - type: Authentication
    url: https://developer.atlassian.com/cloud/confluence/security-overview/
  - type: Authentication
    url: https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/
  - type: Authentication
    url: https://developer.atlassian.com/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/
  - type: Authentication
    url: https://developer.atlassian.com/cloud/confluence/basic-auth-for-rest-apis/
  - type: Documentation
    url: https://developer.atlassian.com/cloud/confluence/using-webhooks/
  - type: CodeExamples
    url: https://developer.atlassian.com/cloud/confluence/rest-api-examples/
  - type: Documentation
    url: https://developer.atlassian.com/cloud/confluence/using-the-rest-api/
  - type: Documentation
    url: https://developer.atlassian.com/cloud/confluence/advanced-searching-using-cql/
  - type: Documentation
    url: https://developer.atlassian.com/cloud/confluence/deprecation-notice-user-privacy-api-migration-guide/
  - type: Documentation
    url: https://developer.atlassian.com/platform/forge/
  - type: PrivacyPolicy
    url: https://www.atlassian.com/legal/privacy-policy
  - type: TermsOfService
    url: https://www.atlassian.com/legal/cloud-terms-of-service
  - type: Blog
    url: https://www.atlassian.com/blog/confluence
  - type: Blog
    url: https://www.atlassian.com/blog/developer
  - type: SignUp
    url: https://www.atlassian.com/try/cloud/signup?bundle=confluence&edition=free
  - type: Login
    url: https://id.atlassian.com/login
  - type: Pricing
    url: https://www.atlassian.com/software/confluence/pricing
  - type: Marketplace
    url: https://marketplace.atlassian.com/
  - type: GitHubOrganization
    url: https://github.com/atlassian
  - type: YouTube
    url: https://www.youtube.com/@Atlassian
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/atlassian-confluence
  - type: LinkedIn
    url: https://www.linkedin.com/company/atlassian
  - type: X
    url: https://twitter.com/Atlassian
  - type: SDK
    url: https://developer.atlassian.com/server/framework/atlassian-sdk/
  - type: SDK
    url: https://github.com/atlassian-api/atlassian-python-api
  - type: SDK
    url: https://mrrefactoring.github.io/confluence.js/
  - type: SDK
    url: https://www.postman.com/api-evangelist/atlassian-confluence/collection/k3y2x73/atlassian-confluence-cloud
  - type: Features
    data:
      - 'Free: up to 10 users, 2 GB storage'
      - 'Standard: $6.05/user/mo with 250 GB storage'
      - 'Premium: $11.55/user/mo with unlimited storage and analytics'
      - Enterprise typically $23-$25/user/mo with AI, 99.95% uptime
      - REST API at api.atlassian.com/wiki
      - Rate limit ~10 req/sec/app/user
      - Bulk operations max 100 items/request
      - Pages, blog posts, comments, attachments, spaces APIs
      - Webhooks for content changes
      - OAuth 2.0 (3LO) and API tokens
      - CQL (Confluence Query Language) for search
      - Atlassian Connect framework for marketplace apps
      - Forge for serverless app development
      - Atlassian Intelligence (Enterprise)
      - Page tree, macros, templates, smart links
      - External collaboration via guest access
    sources:
      - https://www.atlassian.com/software/confluence/pricing
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Knowledge Base
        description: Build and maintain internal knowledge bases for teams with structured content and search.
      - name: Project Documentation
        description: Create and collaborate on project documentation with version tracking and approvals.
      - name: Content Migration
        description: Programmatically migrate content between Confluence instances or from other platforms.
      - name: Compliance and Auditing
        description: Track content changes, manage access controls, and maintain audit trails.
      - name: Automated Publishing
        description: Generate and publish content programmatically from CI/CD pipelines or other systems.
  - type: Integrations
    data:
      - name: Jira
        description: Link Confluence pages to Jira issues for seamless project management workflows.
      - name: Slack
        description: Receive Confluence notifications and preview pages directly in Slack channels.
      - name: Microsoft Teams
        description: Collaborate on Confluence content within Microsoft Teams conversations.
      - name: Trello
        description: Embed Trello boards in Confluence pages and link cards to documentation.
      - name: GitHub
        description: Embed code snippets and link repositories to Confluence documentation.
  - type: OpenAPI
    url: openapi/confluence-cloud-v2.yml
  - type: OpenAPI
    url: https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json
  - type: AsyncAPI
    url: asyncapi/confluence-webhooks.yml
  - type: JSONSchema
    url: json-schema/confluence-page-schema.json
  - type: JSONSchema
    url: json-schema/confluence-space-schema.json
  - type: JSONLD
    url: json-ld/confluence-context.jsonld
  - type: JSONLD
    url: json-ld/confluence-cloud-v2-context.jsonld
---
