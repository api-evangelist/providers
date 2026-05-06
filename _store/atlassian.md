---
aid: atlassian
name: Atlassian
description: Atlassian is a software company that develops collaboration, productivity, and project management tools to help teams work more efficiently. Its products are designed to enhance teamwork, streamline workflows, and support project tracking across a wide range of industries.
type: Contract
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Code
  - Collaboration
  - Platform
  - Productivity
  - Software Development
url: https://raw.githubusercontent.com/api-evangelist/atlassian/refs/heads/main/apis.yml
humanURL: https://developer.atlassian.com/
created: '2024-04-14'
modified: '2026-05-04'
specificationVersion: '0.19'
position: Consuming
apis:
  - aid: atlassian:atlassian-bitbucket-addon-api
    name: Atlassian Bitbucket Addon API
    description: The Atlassian Bitbucket Addon API allows developers to create custom add-ons and integrations for the Bitbucket platform, extending functionality with new features, tools, and services.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-group-addon
    tags:
      - Addons
      - Applications
      - Bitbucket
    properties:
      - type: OpenAPI
        url: openapi/atlassian-addon--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/
  - aid: atlassian:atlassian-bitbucket-hook-events-api
    name: Atlassian Bitbucket Hook Events API
    description: The Atlassian Bitbucket Hook Events API enables users to create webhooks in Bitbucket repositories to trigger custom actions whenever specific events occur.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-webhooks/#api-group-webhooks
    tags:
      - Bitbucket
      - Events
      - Webhooks
    properties:
      - type: OpenAPI
        url: openapi/atlassian-hook-events--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-webhooks/
      - type: JSONLD
        url: json-ld/atlassian-bitbucket-hook-events-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-bitbucket-hook-events-paginated_hook_events-schema.json
  - aid: atlassian:atlassian-bitbucket-pull-requests-api
    name: Atlassian Bitbucket Pull Requests API
    description: The Atlassian Bitbucket Pull Requests API allows users to interact with pull requests in their repositories, providing endpoints for viewing, creating, updating, and merging pull requests.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-group-pullrequests
    tags:
      - Bitbucket
      - Code Review
      - Pull Requests
    properties:
      - type: OpenAPI
        url: openapi/atlassian-pullrequests-selected-user--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/
      - type: JSONLD
        url: json-ld/atlassian-bitbucket-pull-requests-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-bitbucket-pull-requests-a_pullrequest_comment_task-schema.json
  - aid: atlassian:atlassian-bitbucket-repositories-api
    name: Atlassian Bitbucket Repositories API
    description: The Atlassian Bitbucket Repositories API allows users to interact with and manage repositories in their Bitbucket accounts programmatically.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-group-repositories
    tags:
      - Bitbucket
      - Repositories
      - Source Control
    properties:
      - type: OpenAPI
        url: openapi/atlassian-repositories--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/
      - type: JSONLD
        url: json-ld/atlassian-bitbucket-repositories-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-bitbucket-repositories-account-schema.json
  - aid: atlassian:atlassian-bitbucket-snippets-api
    name: Atlassian Bitbucket Snippets API
    description: The Atlassian Bitbucket Snippets API allows users to create, manage, and share code snippets within Bitbucket repositories for collaboration.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-group-snippets
    tags:
      - Bitbucket
      - Code
      - Snippets
    properties:
      - type: OpenAPI
        url: openapi/atlassian-snippets--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/
      - type: JSONLD
        url: json-ld/atlassian-bitbucket-snippets-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-bitbucket-snippets-account-schema.json
  - aid: atlassian:atlassian-bitbucket-teams-api
    name: Atlassian Bitbucket Teams API
    description: The Atlassian Bitbucket Teams API provides access to team management features including repository management, branching, and team activity.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-group-workspaces
    tags:
      - Bitbucket
      - Collaboration
      - Teams
    properties:
      - type: OpenAPI
        url: openapi/atlassian-teams--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/
      - type: JSONLD
        url: json-ld/atlassian-bitbucket-teams-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-bitbucket-teams-account-schema.json
  - aid: atlassian:atlassian-bitbucket-user-api
    name: Atlassian Bitbucket User API
    description: The Atlassian Bitbucket User API allows developers to interact with and manage user accounts within the Bitbucket platform.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-users/#api-group-users
    tags:
      - Bitbucket
      - Users
    properties:
      - type: OpenAPI
        url: openapi/atlassian-user-openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-users/
      - type: JSONLD
        url: json-ld/atlassian-bitbucket-user-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-bitbucket-user-account-schema.json
  - aid: atlassian:atlassian-bitbucket-workspaces-api
    name: Atlassian Bitbucket Workspaces API
    description: The Atlassian Bitbucket Workspaces API enables users to manage and interact with multiple projects within their Bitbucket account.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-group-workspaces
    tags:
      - Bitbucket
      - Workspaces
    properties:
      - type: OpenAPI
        url: openapi/atlassian-workspaces--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/
      - type: JSONLD
        url: json-ld/atlassian-bitbucket-workspaces-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-bitbucket-workspaces-account-schema.json
  - aid: atlassian:atlassian-confluence-analytics-api
    name: Atlassian Confluence Analytics API
    description: The Atlassian Confluence Analytics API provides tools to collect, analyze, and visualize user engagement and content performance within Confluence.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-analytics/#api-group-analytics
    tags:
      - Analytics
      - Confluence
      - Wiki
    properties:
      - type: OpenAPI
        url: openapi/atlassian-wiki-rest-api-analytics--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-analytics/
  - aid: atlassian:atlassian-confluence-audit-api
    name: Atlassian Confluence Audit API
    description: The Atlassian Confluence Audit API provides tools to track and monitor user activity within Confluence for compliance and accountability.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-audit/#api-group-audit
    tags:
      - Audit
      - Confluence
      - Wiki
    properties:
      - type: OpenAPI
        url: openapi/atlassian-wiki-rest-api-audit--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-audit/
      - type: JSONLD
        url: json-ld/atlassian-confluence-audit-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-confluence-audit-audit-record-schema.json
  - aid: atlassian:atlassian-confluence-connect-app-module-api
    name: Atlassian Confluence Connect App Module API
    description: The Atlassian Confluence Connect App Module API allows developers to create custom functionalities and integrations within Confluence.
    humanURL: https://developer.atlassian.com/cloud/confluence/connect-modules/
    tags:
      - Applications
      - Confluence
      - Connect
    properties:
      - type: OpenAPI
        url: openapi/atlassian-atlassian-connect-1-app-module--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/connect-modules/
  - aid: atlassian:atlassian-confluence-content-api
    name: Atlassian Confluence Content API
    description: The Atlassian Confluence Content API enables access and manipulation of content within Confluence including pages, blog posts, comments, and attachments.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#about
    tags:
      - Confluence
      - Content
      - Wiki
    properties:
      - type: OpenAPI
        url: openapi/atlassian-wiki-rest-api-content--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/
      - type: JSONLD
        url: json-ld/atlassian-confluence-content-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-confluence-content-async-content-body-schema.json
  - aid: atlassian:atlassian-confluence-content-body-api
    name: Atlassian Confluence Content Body API
    description: The Atlassian Confluence Content Body API enables programmatic manipulation of Confluence page content bodies and format conversion.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-body/#api-group-content-body
    tags:
      - Confluence
      - Content
      - Wiki
    properties:
      - type: OpenAPI
        url: openapi/atlassian-wiki-rest-api-contentbody--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-body/
      - type: JSONLD
        url: json-ld/atlassian-confluence-content-body-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-confluence-content-body-async-content-body-schema.json
  - aid: atlassian:atlassian-confluence-content-states-api
    name: Atlassian Confluence Content States API
    description: The Atlassian Confluence Content States API enables management and tracking of content lifecycle states within Confluence.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-states/#api-group-content-states
    tags:
      - Confluence
      - Content
      - States
      - Wiki
    properties:
      - type: OpenAPI
        url: openapi/atlassian-wiki-rest-api-content-states--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-states/
      - type: JSONLD
        url: json-ld/atlassian-confluence-content-states-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-confluence-content-states-async-id-schema.json
  - aid: atlassian:atlassian-confluence-group-api
    name: Atlassian Confluence Group API
    description: The Atlassian Confluence Group API enables management of user groups within Confluence including membership and access control.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-group/#api-wiki-rest-api-group-get
    tags:
      - Confluence
      - Groups
      - Wiki
    properties:
      - type: OpenAPI
        url: openapi/atlassian-wiki-rest-api-group--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-group/
      - type: JSONLD
        url: json-ld/atlassian-confluence-group-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-confluence-group-group-array-with-links-schema.json
  - aid: atlassian:atlassian-confluence-inline-tasks-api
    name: Atlassian Confluence Inline Tasks API
    description: The Atlassian Confluence Inline Tasks API enables creating, managing, and tracking tasks directly within Confluence pages.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-inline-tasks#api-group-inline-tasks
    tags:
      - Confluence
      - Tasks
      - Wiki
    properties:
      - type: OpenAPI
        url: openapi/atlassian-wiki-rest-api-inlinetasks--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-inline-tasks
      - type: JSONLD
        url: json-ld/atlassian-confluence-inline-tasks-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-confluence-inline-tasks-task-page-response-schema.json
  - aid: atlassian:atlassian-confluence-label-api
    name: Atlassian Confluence Label API
    description: The Atlassian Confluence Label API enables programmatic management of labels for categorization and organization of Confluence pages.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-labels/#api-group-content-labels
    tags:
      - Confluence
      - Labels
      - Wiki
    properties:
      - type: OpenAPI
        url: openapi/atlassian-wiki-rest-api-label--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-labels/
  - aid: atlassian:atlassian-confluence-longtask-api
    name: Atlassian Confluence Longtask API
    description: The Atlassian Confluence Longtask API enables tracking long-running tasks within Confluence with status updates and progress monitoring.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-long-running-task/#api-wiki-rest-api-longtask-get
    tags:
      - Confluence
      - Tasks
      - Wiki
    properties:
      - type: OpenAPI
        url: openapi/atlassian-wiki-rest-api-longtask--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-long-running-task/
      - type: JSONLD
        url: json-ld/atlassian-confluence-longtask-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-confluence-longtask-long-task-status-with-links-schema.json
  - aid: atlassian:atlassian-confluence-relation-api
    name: Atlassian Confluence Relation API
    description: The Atlassian Confluence Relation API enables creating and managing relationships between different pieces of content within Confluence.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-relation/
    tags:
      - Confluence
      - Relations
      - Wiki
    properties:
      - type: OpenAPI
        url: openapi/atlassian-wiki-rest-api-relation--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-relation/
      - type: JSONLD
        url: json-ld/atlassian-confluence-relation-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-confluence-relation-relation-data-schema.json
  - aid: atlassian:atlassian-confluence-search-api
    name: Atlassian Confluence Search API
    description: The Atlassian Confluence Search API enables programmatic content search within Confluence with customizable query filters.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-search/#api-group-search
    tags:
      - Confluence
      - Search
      - Wiki
    properties:
      - type: OpenAPI
        url: openapi/atlassian-wiki-rest-api-search--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-search/
      - type: JSONLD
        url: json-ld/atlassian-confluence-search-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-confluence-search-search-page-response-search-result-schema.json
  - aid: atlassian:atlassian-confluence-settings-api
    name: Atlassian Confluence Settings API
    description: The Atlassian Confluence Settings API enables customization and configuration of Confluence instance settings including themes and system information.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-settings/#api-group-settings
    tags:
      - Confluence
      - Settings
      - Wiki
    properties:
      - type: OpenAPI
        url: openapi/atlassian-wiki-rest-api-settings--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-settings/
      - type: JSONLD
        url: json-ld/atlassian-confluence-settings-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-confluence-settings-look-and-feel-schema.json
  - aid: atlassian:atlassian-confluence-space-api
    name: Atlassian Confluence Space API
    description: The Atlassian Confluence Space API enables programmatic management of Confluence spaces including creation, permissions, and content organization.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-space/#api-group-space
    tags:
      - Confluence
      - Spaces
      - Wiki
    properties:
      - type: OpenAPI
        url: openapi/atlassian-wiki-rest-api-space--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-space/
      - type: JSONLD
        url: json-ld/atlassian-confluence-space-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-confluence-space-content-state-settings-schema.json
  - aid: atlassian:atlassian-confluence-template-api
    name: Atlassian Confluence Template API
    description: The Atlassian Confluence Template API enables creating and customizing templates within Confluence for standardized content creation.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-template/#api-group-template
    tags:
      - Confluence
      - Templates
      - Wiki
    properties:
      - type: OpenAPI
        url: openapi/atlassian-wiki-rest-api-template--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-template/
      - type: JSONLD
        url: json-ld/atlassian-confluence-template-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-confluence-template-blueprint-template-array-schema.json
  - aid: atlassian:atlassian-confluence-user-api
    name: Atlassian Confluence User API
    description: The Atlassian Confluence User API enables management of user data within Confluence including profiles, groups, and permissions.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-user/#api-group-user
    tags:
      - Confluence
      - Users
      - Wiki
    properties:
      - type: OpenAPI
        url: openapi/atlassian-wiki-rest-api-user--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-user/
      - type: JSONLD
        url: json-ld/atlassian-confluence-user-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-confluence-user-account-id-email-record-schema.json
  - aid: atlassian:atlassian-jira-announcement-banner-api
    name: Atlassian Jira Announcement Banner API
    description: The Atlassian Jira Announcement Banner API allows managing custom announcement banners within Jira for important messages and alerts.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-announcement-banner/#api-group-announcement-banner
    tags:
      - Jira
      - Notifications
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-announcementbanner--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-announcement-banner/
  - aid: atlassian:atlassian-jira-app-api
    name: Atlassian Jira App API
    description: The Atlassian Jira App API allows developers to integrate and customize Jira with custom app properties and field values.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-app-properties/#api-group-app-properties
    tags:
      - Applications
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-app--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-custom-field-values--apps-/
  - aid: atlassian:atlassian-jira-application-properties-api
    name: Atlassian Jira Application Properties API
    description: The Atlassian Jira Application Properties API allows access and modification of Jira application configuration properties.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-app-openapi#api-group-app-properties
    tags:
      - Configuration
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-application-properties--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-app-openapi
  - aid: atlassian:atlassian-jira-application-role-api
    name: Atlassian Jira Application Role API
    description: The Atlassian Jira Application Role API enables management of application roles within Jira for controlling access and permissions.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-application-roles/#api-group-application-roles
    tags:
      - Jira
      - Roles
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-applicationrole--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-application-roles/
  - aid: atlassian:atlassian-jira-attachment-api
    name: Atlassian Jira Attachment API
    description: The Atlassian Jira Attachment API enables managing file attachments on Jira issues including upload, retrieval, and metadata.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-attachments/#api-group-issue-attachments
    tags:
      - Attachments
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-attachment--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-attachments/
  - aid: atlassian:atlassian-jira-auditing-api
    name: Atlassian Jira Auditing API
    description: The Atlassian Jira Auditing API allows tracking and monitoring all changes made within a Jira instance for compliance and accountability.
    humanURL: https://developer.atlassian.com/server/framework/atlassian-sdk/audit/
    tags:
      - Audit
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-auditing--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/server/framework/atlassian-sdk/audit/
  - aid: atlassian:atlassian-jira-avatar-api
    name: Atlassian Jira Avatar API
    description: The Atlassian Jira Avatar API enables programmatic management of user and project avatars within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-avatars/#api-group-avatars
    tags:
      - Avatars
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-avatar--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-avatars/
  - aid: atlassian:atlassian-jira-classification-levels-api
    name: Atlassian Jira Classification Levels API
    description: The Atlassian Jira Classification Levels API enables defining and customizing classification levels for categorizing issues.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-classification-levels/#api-group-classification-levels
    tags:
      - Classification
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-classification-levels--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-classification-levels/
  - aid: atlassian:atlassian-jira-comment-api
    name: Atlassian Jira Comment API
    description: The Atlassian Jira Comment API enables managing comments on Jira issues including creation, updates, and property management.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-comments/#api-group-issue-comments
    tags:
      - Comments
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-comment--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-comments/
  - aid: atlassian:atlassian-jira-component-api
    name: Atlassian Jira Component API
    description: The Atlassian Jira Component API allows managing project components for categorizing and organizing issues within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-components/#api-group-project-components
    tags:
      - Components
      - Jira
      - Projects
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-component--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-components/
  - aid: atlassian:atlassian-jira-configuration-api
    name: Atlassian Jira Configuration API
    description: The Atlassian Jira Configuration API provides access to Jira settings and configuration options including time tracking providers.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jira-settings/#api-group-jira-settings
    tags:
      - Configuration
      - Jira
      - Settings
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-configuration--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jira-settings/
  - aid: atlassian:atlassian-jira-connect-addons-api
    name: Atlassian Jira Connect Addons API
    description: The Atlassian Jira Connect Addons API enables building custom integrations and extensions for Jira using the Connect framework.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/getting-started-with-connect/
    tags:
      - Connect
      - Integrations
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-atlassian-connect-1-addons--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/getting-started-with-connect/
  - aid: atlassian:atlassian-jira-connect-app-api
    name: Atlassian Jira Connect App API
    description: The Atlassian Jira Connect App API enables creating custom integrations between Jira and other applications using dynamic modules.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/getting-started-with-connect/
    tags:
      - Applications
      - Connect
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-atlassian-connect-1-app--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/getting-started-with-connect/
  - aid: atlassian:atlassian-jira-connect-migration-api
    name: Atlassian Jira Connect Migration API
    description: The Atlassian Jira Connect Migration API enables migrating data and configurations between Jira Cloud instances.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/connect-api-migration/
    tags:
      - Connect
      - Jira
      - Migration
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-atlassian-connect-1-migration--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/connect-api-migration/
  - aid: atlassian:atlassian-jira-connect-service-registry-api
    name: Atlassian Jira Connect Service Registry API
    description: The Atlassian Jira Connect Service Registry API enables discovering and connecting services within the Jira platform.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-service-registry/#api-group-service-registry
    tags:
      - Connect
      - Jira
      - Services
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-atlassian-connect-1-service-registry--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-service-registry/
  - aid: atlassian:atlassian-jira-custom-field-option-api
    name: Atlassian Jira Custom Field Option API
    description: The Atlassian Jira Custom Field Option API enables managing custom field options for Jira issue fields.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options/#api-group-issue-custom-field-options
    tags:
      - Custom Fields
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-customfieldoption--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options/
  - aid: atlassian:atlassian-jira-dashboard-api
    name: Atlassian Jira Dashboard API
    description: The Atlassian Jira Dashboard API enables creating, customizing, and managing dashboards and gadgets within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-dashboards/#api-group-dashboards
    tags:
      - Dashboards
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-dashboard--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-dashboards/
  - aid: atlassian:atlassian-jira-data-policy-api
    name: Atlassian Jira Data Policy API
    description: The Atlassian Jira Data Policy API enables managing and enforcing data policies within Jira projects for compliance and governance.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/data-security-policy-developer-guide/
    tags:
      - Data Policy
      - Jira
      - Security
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-data-policy--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/data-security-policy-developer-guide/
  - aid: atlassian:atlassian-jira-events-api
    name: Atlassian Jira Events API
    description: The Atlassian Jira Events API enables tracking and responding to events within Jira for custom automation and notifications.
    humanURL: https://developer.atlassian.com/platform/forge/events-reference/jira/
    tags:
      - Events
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-events--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/platform/forge/events-reference/jira/
  - aid: atlassian:atlassian-jira-expression-api
    name: Atlassian Jira Expression API
    description: The Atlassian Jira Expression API enables creating custom expressions for complex calculations and data operations within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jira-expressions/#api-group-jira-expressions
    tags:
      - Expressions
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-expression--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jira-expressions/
  - aid: atlassian:atlassian-jira-field-api
    name: Atlassian Jira Field API
    description: The Atlassian Jira Field API enables managing custom and system fields within Jira including contexts, options, and configurations.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/#api-group-issue-fields
    tags:
      - Fields
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-field--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/
  - aid: atlassian:atlassian-jira-field-configuration-api
    name: Atlassian Jira Field Configuration API
    description: The Atlassian Jira Field Configuration API enables managing how fields behave and display within Jira projects.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-field-configurations/#api-group-issue-field-configurations
    tags:
      - Configuration
      - Fields
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-fieldconfiguration--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-field-configurations/
  - aid: atlassian:atlassian-jira-field-configuration-scheme-api
    name: Atlassian Jira Field Configuration Scheme API
    description: The Atlassian Jira Field Configuration Scheme API enables defining how custom fields appear across different issue screens.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-field-configurations/#api-group-issue-field-configurations
    tags:
      - Configuration
      - Fields
      - Jira
      - Schemes
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-fieldconfigurationscheme--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-field-configurations/
  - aid: atlassian:atlassian-jira-filter-api
    name: Atlassian Jira Filter API
    description: The Atlassian Jira Filter API enables creating, managing, and sharing issue filters within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-filters/#api-group-filters
    tags:
      - Filters
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-filter--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-filters/
  - aid: atlassian:atlassian-jira-forge-app-api
    name: Atlassian Jira Forge App API
    description: The Atlassian Jira Forge App API enables building custom Forge apps for Jira with serverless infrastructure.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/forge/
    tags:
      - Forge
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-forge-1-app--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/forge/
  - aid: atlassian:atlassian-jira-group-api
    name: Atlassian Jira Group API
    description: The Atlassian Jira Group API enables managing user groups within Jira for access control and permissions.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-groups/#api-group-groups
    tags:
      - Groups
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-group--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-groups/
  - aid: atlassian:atlassian-jira-group-user-picker-api
    name: Atlassian Jira Group User Picker API
    description: The Atlassian Jira Group User Picker API enables searching for and selecting users within specified groups in Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-group-and-user-picker/#api-group-group-and-user-picker
    tags:
      - Groups
      - Jira
      - Users
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-groupuserpicker--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-group-and-user-picker/
  - aid: atlassian:atlassian-jira-groups-api
    name: Atlassian Jira Groups API
    description: The Atlassian Jira Groups API enables programmatic management of user groups and group permissions within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-groups/#api-group-groups
    tags:
      - Groups
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-groups--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-groups/
  - aid: atlassian:atlassian-jira-issue-api
    name: Atlassian Jira Issue API
    description: The Atlassian Jira Issue API enables creating, updating, deleting, and querying issues within Jira including comments, attachments, and transitions.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/#api-group-issues
    tags:
      - Issues
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-issue--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/
  - aid: atlassian:atlassian-jira-issue-link-api
    name: Atlassian Jira Issue Link API
    description: The Atlassian Jira Issue Link API enables creating and managing links between different issues within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-links/#api-group-issue-links
    tags:
      - Issues
      - Jira
      - Links
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-issuelink--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-links/
  - aid: atlassian:atlassian-jira-issue-link-type-api
    name: Atlassian Jira Issue Link Type API
    description: The Atlassian Jira Issue Link Type API enables managing the types of links that can be created between issues.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-links/#api-group-issue-links
    tags:
      - Issues
      - Jira
      - Links
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-issuelinktype--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-links/
  - aid: atlassian:atlassian-jira-issue-security-schemes-api
    name: Atlassian Jira Issue Security Schemes API
    description: The Atlassian Jira Issue Security Schemes API enables managing security schemes that control which users can view specific issues.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-group-issue-security-schemes
    tags:
      - Jira
      - Security
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-issuesecurityschemes--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/
  - aid: atlassian:atlassian-jira-issue-type-api
    name: Atlassian Jira Issue Type API
    description: The Atlassian Jira Issue Type API enables managing issue types for organizing and categorizing work within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-types/#api-group-issue-types
    tags:
      - Issue Types
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-issuetype--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-types/
  - aid: atlassian:atlassian-jira-issue-type-scheme-api
    name: Atlassian Jira Issue Type Scheme API
    description: The Atlassian Jira Issue Type Scheme API enables managing and customizing issue type schemes within Jira projects.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-group-issue-type-schemes
    tags:
      - Issue Types
      - Jira
      - Schemes
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-issuetypescheme--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/
  - aid: atlassian:atlassian-jira-issue-type-screen-scheme-api
    name: Atlassian Jira Issue Type Screen Scheme API
    description: The Atlassian Jira Issue Type Screen Scheme API enables customizing the screens displayed for different issue types.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/#api-group-issue-type-screen-schemes
    tags:
      - Issue Types
      - Jira
      - Schemes
      - Screens
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-issuetypescreenscheme--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/
  - aid: atlassian:atlassian-jira-issues-api
    name: Atlassian Jira Issues API
    description: The Atlassian Jira Issues API enables bulk issue operations including archiving and exporting issues.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/#api-group-issues
    tags:
      - Issues
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-issues--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/
  - aid: atlassian:atlassian-jira-jql-api
    name: Atlassian Jira JQL API
    description: The Atlassian Jira JQL API enables creating complex queries to filter, search, and retrieve specific issues from Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-group-issue-search
    tags:
      - Jira
      - JQL
      - Search
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-jql--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/
  - aid: atlassian:atlassian-jira-label-api
    name: Atlassian Jira Label API
    description: The Atlassian Jira Label API enables managing labels for categorizing and organizing Jira issues.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-labels/#api-group-labels
    tags:
      - Jira
      - Labels
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-label--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-labels/
  - aid: atlassian:atlassian-jira-license-api
    name: Atlassian Jira License API
    description: The Atlassian Jira License API enables managing Jira software licenses programmatically.
    humanURL: https://developer.atlassian.com/platform/marketplace/license-api-for-cloud-apps/
    tags:
      - Jira
      - Licensing
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-license--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/platform/marketplace/license-api-for-cloud-apps/
  - aid: atlassian:atlassian-jira-license-metrics-api
    name: Atlassian Jira License Metrics API
    description: The Atlassian Jira License Metrics API provides access to license usage metrics for Jira instances.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-license-metrics/#api-group-license-metrics
    tags:
      - Jira
      - Licensing
      - Metrics
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-instance--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-license-metrics/
  - aid: atlassian:atlassian-jira-my-permissions-api
    name: Atlassian Jira My Permissions API
    description: The Atlassian Jira My Permissions API enables viewing the current user's permission levels within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-permissions/#api-group-permissions
    tags:
      - Jira
      - Permissions
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-mypermissions--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-permissions/
  - aid: atlassian:atlassian-jira-my-preferences-api
    name: Atlassian Jira My Preferences API
    description: The Atlassian Jira My Preferences API enables managing personal user preferences within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-myself/#api-group-myself
    tags:
      - Jira
      - Preferences
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-mypreferences--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-myself/
  - aid: atlassian:atlassian-jira-myself-api
    name: Atlassian Jira Myself API
    description: The Atlassian Jira Myself API enables accessing and updating the current user's own profile and account information.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-myself/#api-group-myself
    tags:
      - Jira
      - Users
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-myself--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-myself/
  - aid: atlassian:atlassian-jira-notification-scheme-api
    name: Atlassian Jira Notification Scheme API
    description: The Atlassian Jira Notification Scheme API enables managing notification schemes for Jira projects.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-notification-schemes/#api-group-issue-notification-schemes
    tags:
      - Jira
      - Notifications
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-notificationscheme--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-notification-schemes/
  - aid: atlassian:atlassian-jira-permission-scheme-api
    name: Atlassian Jira Permission Scheme API
    description: The Atlassian Jira Permission Scheme API enables creating and managing permission schemes for controlling access within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-permission-schemes/#api-group-project-permission-schemes
    tags:
      - Jira
      - Permissions
      - Schemes
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-permissionscheme--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-permission-schemes/
  - aid: atlassian:atlassian-jira-permissions-api
    name: Atlassian Jira Permissions API
    description: The Atlassian Jira Permissions API enables checking and managing permissions for users and groups within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-permissions/#api-group-permissions
    tags:
      - Jira
      - Permissions
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-permissions--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-permissions/
  - aid: atlassian:atlassian-jira-priority-api
    name: Atlassian Jira Priority API
    description: The Atlassian Jira Priority API enables managing issue priority levels within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-priorities/#api-group-issue-priorities
    tags:
      - Jira
      - Priorities
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-priority--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-priorities/
  - aid: atlassian:atlassian-jira-project-api
    name: Atlassian Jira Project API
    description: The Atlassian Jira Project API enables creating, managing, and configuring projects within Jira including roles and permissions.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-group-projects
    tags:
      - Jira
      - Projects
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-project--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/
  - aid: atlassian:atlassian-jira-project-category-api
    name: Atlassian Jira Project Category API
    description: The Atlassian Jira Project Category API enables managing project categories for organizing projects within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-categories/#api-group-project-categories
    tags:
      - Categories
      - Jira
      - Projects
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-projectcategory--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-categories/
  - aid: atlassian:atlassian-jira-project-validate-api
    name: Atlassian Jira Project Validate API
    description: The Atlassian Jira Project Validate API enables validating project keys and names before creation.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-key-and-name-validation/#api-group-project-key-and-name-validation
    tags:
      - Jira
      - Projects
      - Validation
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-projectvalidate--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-key-and-name-validation/
  - aid: atlassian:atlassian-jira-resolution-api
    name: Atlassian Jira Resolution API
    description: The Atlassian Jira Resolution API enables managing issue resolution types within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-resolutions/#api-group-issue-resolutions
    tags:
      - Jira
      - Resolutions
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-resolution--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-resolutions/
  - aid: atlassian:atlassian-jira-role-api
    name: Atlassian Jira Role API
    description: The Atlassian Jira Role API enables managing project roles and role actors within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-project-roles/#api-group-project-roles
    tags:
      - Jira
      - Roles
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-role--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-project-roles/
  - aid: atlassian:atlassian-jira-screens-api
    name: Atlassian Jira Screens API
    description: The Atlassian Jira Screens API enables creating and managing issue screens, tabs, and field layouts within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-screens/
    tags:
      - Jira
      - Screens
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-screens--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-screens/
  - aid: atlassian:atlassian-jira-screen-scheme-api
    name: Atlassian Jira Screen Scheme API
    description: The Atlassian Jira Screen Scheme API enables managing screen schemes that define default screens for issue operations.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-screen-schemes/#api-group-screen-schemes
    tags:
      - Jira
      - Schemes
      - Screens
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-screenscheme--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-screen-schemes/
  - aid: atlassian:atlassian-jira-search-api
    name: Atlassian Jira Search API
    description: The Atlassian Jira Search API enables searching for issues using JQL queries and filters.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-group-issue-search
    tags:
      - Jira
      - Search
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-search--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/
  - aid: atlassian:atlassian-jira-security-level-api
    name: Atlassian Jira Security Level API
    description: The Atlassian Jira Security Level API enables managing issue security levels for controlling access to specific issues.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-security-level/#api-group-issue-security-level
    tags:
      - Jira
      - Security
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-securitylevel--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-security-level/
  - aid: atlassian:atlassian-jira-server-info-api
    name: Atlassian Jira Server Info API
    description: The Atlassian Jira Server Info API provides information about the Jira server including version and build details.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-server-info/#api-group-server-info
    tags:
      - Jira
      - Server
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-serverinfo--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-server-info/
  - aid: atlassian:atlassian-jira-settings-api
    name: Atlassian Jira Settings API
    description: The Atlassian Jira Settings API enables managing Jira instance settings including issue navigator columns.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jira-settings/#api-group-jira-settings
    tags:
      - Jira
      - Settings
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-settings--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jira-settings/
  - aid: atlassian:atlassian-jira-status-api
    name: Atlassian Jira Status API
    description: The Atlassian Jira Status API enables retrieving workflow status information for Jira issues.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-statuses/#api-rest-api-3-status-get
    tags:
      - Jira
      - Status
      - Workflows
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-status--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-statuses/
  - aid: atlassian:atlassian-jira-status-category-api
    name: Atlassian Jira Status Category API
    description: The Atlassian Jira Status Category API enables accessing and managing workflow status categories within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-status-categories/#api-group-workflow-status-categories
    tags:
      - Jira
      - Status
      - Workflows
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-statuscategory--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-status-categories/
  - aid: atlassian:atlassian-jira-statuses-api
    name: Atlassian Jira Statuses API
    description: The Atlassian Jira Statuses API enables paginated search and management of workflow statuses within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-statuses/#api-rest-api-3-status-get
    tags:
      - Jira
      - Status
      - Workflows
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-statuses--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-statuses/
  - aid: atlassian:atlassian-jira-task-api
    name: Atlassian Jira Task API
    description: The Atlassian Jira Task API enables managing and tracking long-running tasks within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/#api-group-tasks
    tags:
      - Jira
      - Tasks
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-task--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/
  - aid: atlassian:atlassian-jira-ui-modifications-api
    name: Atlassian Jira UI Modifications API
    description: The Atlassian Jira UI Modifications API enables customizing and enhancing the Jira user interface for apps.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-ui-modifications--apps-/#api-group-ui-modifications--apps-
    tags:
      - Jira
      - UI
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-uimodifications--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-ui-modifications--apps-/
  - aid: atlassian:atlassian-jira-universal-avatar-api
    name: Atlassian Jira Universal Avatar API
    description: The Atlassian Jira Universal Avatar API enables managing avatars across different entity types within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-avatars/#api-group-avatars
    tags:
      - Avatars
      - Jira
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-universal-avatar--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-avatars/
  - aid: atlassian:atlassian-jira-user-api
    name: Atlassian Jira User API
    description: The Atlassian Jira User API enables managing user accounts, properties, and permissions within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/#api-group-users
    tags:
      - Jira
      - Users
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-user--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/
  - aid: atlassian:atlassian-jira-users-api
    name: Atlassian Jira Users API
    description: The Atlassian Jira Users API enables searching and managing multiple users within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/
    tags:
      - Jira
      - Users
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-users--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/
  - aid: atlassian:atlassian-jira-version-api
    name: Atlassian Jira Version API
    description: The Atlassian Jira Version API enables managing project versions and releases within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-versions/#api-group-project-versions
    tags:
      - Jira
      - Versions
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-version--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-versions/
  - aid: atlassian:atlassian-jira-webhook-api
    name: Atlassian Jira Webhook API
    description: The Atlassian Jira Webhook API enables managing webhooks for receiving real-time notifications about Jira events.
    humanURL: https://developer.atlassian.com/server/jira/platform/webhooks/
    tags:
      - Jira
      - Webhooks
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-webhook--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/server/jira/platform/webhooks/
  - aid: atlassian:atlassian-jira-workflow-api
    name: Atlassian Jira Workflow API
    description: The Atlassian Jira Workflow API enables managing workflows, transitions, and workflow rules within Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/#api-group-workflows
    tags:
      - Jira
      - Workflows
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-workflow--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/
  - aid: atlassian:atlassian-jira-workflow-scheme-api
    name: Atlassian Jira Workflow Scheme API
    description: The Atlassian Jira Workflow Scheme API enables managing workflow schemes and mapping workflows to issue types.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-workflow-schemes/#api-group-workflow-schemes
    tags:
      - Jira
      - Schemes
      - Workflows
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-workflowscheme--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-workflow-schemes/
  - aid: atlassian:atlassian-jira-workflows-api
    name: Atlassian Jira Workflows API
    description: The Atlassian Jira Workflows API enables bulk workflow operations including creation, validation, and capability checking.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/
    tags:
      - Jira
      - Workflows
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-workflows--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/
  - aid: atlassian:atlassian-jira-worklog-api
    name: Atlassian Jira Worklog API
    description: The Atlassian Jira Worklog API enables managing time tracking worklogs on Jira issues.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-worklogs/#api-group-issue-worklogs
    tags:
      - Jira
      - Time Tracking
      - Worklogs
    properties:
      - type: OpenAPI
        url: openapi/atlassian-rest-api-3-worklog--openapi-original.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-worklogs/
  - aid: atlassian:atlassian-jira-software-backlog-api
    name: Atlassian Jira Software Backlog API
    description: The Atlassian Jira Software Backlog API enables managing backlog items within Jira Software boards.
    humanURL: https://developer.atlassian.com/cloud/jira/software/rest/api-group-backlog/#api-group-backlog
    tags:
      - Agile
      - Backlog
      - Jira Software
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/software/rest/api-group-backlog/
  - aid: atlassian:atlassian-jira-software-board-api
    name: Atlassian Jira Software Board API
    description: The Atlassian Jira Software Board API enables managing Scrum and Kanban boards within Jira Software.
    humanURL: https://developer.atlassian.com/cloud/jira/software/rest/api-group-board/#api-group-board
    tags:
      - Agile
      - Boards
      - Jira Software
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/software/rest/api-group-board/
  - aid: atlassian:atlassian-jira-software-epic-api
    name: Atlassian Jira Software Epic API
    description: The Atlassian Jira Software Epic API enables managing epics in Jira Software for organizing large bodies of work.
    humanURL: https://developer.atlassian.com/cloud/jira/software/rest/api-group-epic/#api-group-epic
    tags:
      - Agile
      - Epics
      - Jira Software
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/software/rest/api-group-epic/
  - aid: atlassian:atlassian-jira-software-sprint-api
    name: Atlassian Jira Software Sprint API
    description: The Atlassian Jira Software Sprint API enables managing sprints within Jira Software Scrum boards.
    humanURL: https://developer.atlassian.com/cloud/jira/software/rest/api-group-sprint/#api-group-sprint
    tags:
      - Agile
      - Jira Software
      - Sprints
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/software/rest/api-group-sprint/
  - aid: atlassian:atlassian-jira-software-development-information-api
    name: Atlassian Jira Software Development Information API
    description: The Atlassian Jira Software Development Information API enables sending development data like commits, branches, and pull requests to Jira.
    humanURL: https://developer.atlassian.com/cloud/jira/software/rest/api-group-development-information/#api-group-development-information
    tags:
      - Development
      - Jira Software
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/software/rest/api-group-development-information/
  - aid: atlassian:atlassian-jira-software-feature-flags-api
    name: Atlassian Jira Software Feature Flags API
    description: The Atlassian Jira Software Feature Flags API enables sending feature flag information to Jira Software for release coordination.
    humanURL: https://developer.atlassian.com/cloud/jira/software/rest/api-group-feature-flags/#api-group-feature-flags
    tags:
      - Feature Flags
      - Jira Software
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/software/rest/api-group-feature-flags/
  - aid: atlassian:atlassian-jira-software-deployments-api
    name: Atlassian Jira Software Deployments API
    description: The Atlassian Jira Software Deployments API enables sending deployment information to Jira Software for CI/CD visibility.
    humanURL: https://developer.atlassian.com/cloud/jira/software/rest/api-group-deployments/#api-group-deployments
    tags:
      - CI/CD
      - Deployments
      - Jira Software
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/software/rest/api-group-deployments/
  - aid: atlassian:atlassian-jira-software-builds-api
    name: Atlassian Jira Software Builds API
    description: The Atlassian Jira Software Builds API enables sending build information to Jira Software for CI/CD visibility.
    humanURL: https://developer.atlassian.com/cloud/jira/software/rest/api-group-builds/#api-group-builds
    tags:
      - Builds
      - CI/CD
      - Jira Software
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/software/rest/api-group-builds/
  - aid: atlassian:atlassian-jira-software-remote-links-api
    name: Atlassian Jira Software Remote Links API
    description: The Atlassian Jira Software Remote Links API enables connecting Jira issues to external resources and tools.
    humanURL: https://developer.atlassian.com/cloud/jira/software/rest/api-group-remote-links/#api-group-remote-links
    tags:
      - Integrations
      - Jira Software
      - Remote Links
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/software/rest/api-group-remote-links/
  - aid: atlassian:atlassian-jira-software-security-information-api
    name: Atlassian Jira Software Security Information API
    description: The Atlassian Jira Software Security Information API enables sending vulnerability information to Jira for security tracking.
    humanURL: https://developer.atlassian.com/cloud/jira/software/rest/api-group-security-information/#api-group-security-information
    tags:
      - Jira Software
      - Security
      - Vulnerabilities
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/software/rest/api-group-security-information/
  - aid: atlassian:atlassian-jira-service-management-customer-api
    name: Atlassian Jira Service Management Customer API
    description: The Atlassian Jira Service Management Customer API enables managing customer accounts and access to service desks.
    humanURL: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-customer/#api-group-customer
    tags:
      - Customers
      - ITSM
      - Service Desk
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-customer/
  - aid: atlassian:atlassian-jira-service-management-info-api
    name: Atlassian Jira Service Management Info API
    description: The Atlassian Jira Service Management Info API provides runtime and version information about the JSM instance.
    humanURL: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-info/#api-group-info
    tags:
      - Info
      - ITSM
      - Service Desk
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-info/
  - aid: atlassian:atlassian-jira-service-management-knowledgebase-api
    name: Atlassian Jira Service Management Knowledgebase API
    description: The Atlassian Jira Service Management Knowledgebase API enables searching knowledge base articles for resolving customer requests.
    humanURL: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-knowledgebase/#api-group-knowledgebase
    tags:
      - ITSM
      - Knowledge Base
      - Service Desk
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-knowledgebase/
  - aid: atlassian:atlassian-jira-service-management-organization-api
    name: Atlassian Jira Service Management Organization API
    description: The Atlassian Jira Service Management Organization API enables managing organizations for grouping customers within JSM.
    humanURL: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-organization/#api-group-organization
    tags:
      - ITSM
      - Organizations
      - Service Desk
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-organization/
  - aid: atlassian:atlassian-jira-service-management-request-api
    name: Atlassian Jira Service Management Request API
    description: The Atlassian Jira Service Management Request API enables creating and managing service requests within JSM.
    humanURL: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-request/#api-group-request
    tags:
      - ITSM
      - Requests
      - Service Desk
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-request/
  - aid: atlassian:atlassian-jira-service-management-requesttype-api
    name: Atlassian Jira Service Management Request Type API
    description: The Atlassian Jira Service Management Request Type API enables managing request types within JSM service desks.
    humanURL: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-requesttype/#api-group-requesttype
    tags:
      - ITSM
      - Request Types
      - Service Desk
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-requesttype/
  - aid: atlassian:atlassian-jira-service-management-servicedesk-api
    name: Atlassian Jira Service Management Servicedesk API
    description: The Atlassian Jira Service Management Servicedesk API enables managing service desks, queues, and configurations within JSM.
    humanURL: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-servicedesk/#api-group-servicedesk
    tags:
      - ITSM
      - Queues
      - Service Desk
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-servicedesk/
  - aid: atlassian:atlassian-jira-service-management-assets-api
    name: Atlassian Jira Service Management Assets API
    description: The Atlassian Jira Service Management Assets API enables managing IT assets and CMDB within JSM.
    humanURL: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-assets/#api-group-assets
    tags:
      - Assets
      - CMDB
      - ITSM
      - Service Desk
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-assets/
  - aid: atlassian:atlassian-bitbucket-branch-restrictions-api
    name: Atlassian Bitbucket Branch Restrictions API
    description: The Atlassian Bitbucket Branch Restrictions API enables managing branch restrictions for repositories in Bitbucket Cloud.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-group-branch-restrictions
    tags:
      - Bitbucket
      - Branches
      - Restrictions
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/
  - aid: atlassian:atlassian-bitbucket-branching-model-api
    name: Atlassian Bitbucket Branching Model API
    description: The Atlassian Bitbucket Branching Model API enables managing branching model configurations for repositories.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/#api-group-branching-model
    tags:
      - Bitbucket
      - Branching
      - Git Flow
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/
  - aid: atlassian:atlassian-bitbucket-commit-statuses-api
    name: Atlassian Bitbucket Commit Statuses API
    description: The Atlassian Bitbucket Commit Statuses API enables managing build statuses associated with commits.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-commit-statuses/#api-group-commit-statuses
    tags:
      - Bitbucket
      - CI/CD
      - Commits
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-commit-statuses/
  - aid: atlassian:atlassian-bitbucket-commits-api
    name: Atlassian Bitbucket Commits API
    description: The Atlassian Bitbucket Commits API enables interacting with commits in Bitbucket Cloud repositories.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-commits/#api-group-commits
    tags:
      - Bitbucket
      - Commits
      - Source Control
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-commits/
  - aid: atlassian:atlassian-bitbucket-deployments-api
    name: Atlassian Bitbucket Deployments API
    description: The Atlassian Bitbucket Deployments API enables managing deployment information for Bitbucket Cloud repositories.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-group-deployments
    tags:
      - Bitbucket
      - CI/CD
      - Deployments
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/
  - aid: atlassian:atlassian-bitbucket-downloads-api
    name: Atlassian Bitbucket Downloads API
    description: The Atlassian Bitbucket Downloads API enables managing download artifacts for Bitbucket Cloud repositories.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-downloads/#api-group-downloads
    tags:
      - Artifacts
      - Bitbucket
      - Downloads
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-downloads/
  - aid: atlassian:atlassian-bitbucket-pipelines-api
    name: Atlassian Bitbucket Pipelines API
    description: The Atlassian Bitbucket Pipelines API enables managing Bitbucket Pipelines CI/CD configurations and builds.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-group-pipelines
    tags:
      - Automation
      - Bitbucket
      - CI/CD
      - Pipelines
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/
  - aid: atlassian:atlassian-bitbucket-projects-api
    name: Atlassian Bitbucket Projects API
    description: The Atlassian Bitbucket Projects API enables managing projects for grouping related repositories within workspaces.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-group-projects
    tags:
      - Bitbucket
      - Organization
      - Projects
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/
  - aid: atlassian:atlassian-bitbucket-refs-api
    name: Atlassian Bitbucket Refs API
    description: The Atlassian Bitbucket Refs API enables managing branches and tags within Bitbucket Cloud repositories.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-group-refs
    tags:
      - Bitbucket
      - Branches
      - Refs
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/
  - aid: atlassian:atlassian-bitbucket-source-api
    name: Atlassian Bitbucket Source API
    description: The Atlassian Bitbucket Source API enables browsing and retrieving source code files from Bitbucket repositories.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-source/#api-group-source
    tags:
      - Bitbucket
      - Files
      - Source
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-source/
  - aid: atlassian:atlassian-bitbucket-issue-tracker-api
    name: Atlassian Bitbucket Issue Tracker API
    description: The Atlassian Bitbucket Issue Tracker API enables managing the built-in issue tracker within Bitbucket repositories.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-group-issue-tracker
    tags:
      - Bitbucket
      - Issues
      - Tracking
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/
  - aid: atlassian:atlassian-bitbucket-reports-api
    name: Atlassian Bitbucket Reports API
    description: The Atlassian Bitbucket Reports API enables creating code insight reports with annotations for commits.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-reports/#api-group-reports
    tags:
      - Bitbucket
      - Code Quality
      - Reports
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-reports/
  - aid: atlassian:atlassian-bitbucket-ssh-api
    name: Atlassian Bitbucket SSH API
    description: The Atlassian Bitbucket SSH API enables managing SSH keys for secure Git operations in Bitbucket Cloud.
    humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-ssh/#api-group-ssh
    tags:
      - Authentication
      - Bitbucket
      - SSH
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-ssh/
  - aid: atlassian:atlassian-trello-api
    name: Atlassian Trello API
    description: The Atlassian Trello API enables programmatic interaction with Trello boards, cards, lists, and other resources.
    humanURL: https://developer.atlassian.com/cloud/trello/rest/
    tags:
      - Boards
      - Cards
      - Collaboration
      - Trello
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/trello/rest/
      - type: GettingStarted
        url: https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/
  - aid: atlassian:atlassian-compass-api
    name: Atlassian Compass API
    description: The Atlassian Compass API enables interacting with the Compass developer experience platform for managing software component health.
    humanURL: https://developer.atlassian.com/cloud/compass/rest/v1/intro/
    tags:
      - Components
      - Developer Experience
      - Service Catalog
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/compass/rest/v1/intro/
  - aid: atlassian:atlassian-statuspage-api
    name: Atlassian Statuspage API
    description: The Atlassian Statuspage API enables programmatic management of status pages, components, incidents, and subscribers.
    humanURL: https://developer.statuspage.io/
    tags:
      - Incidents
      - Monitoring
      - Status Pages
    properties:
      - type: Documentation
        url: https://developer.statuspage.io/
  - aid: atlassian:atlassian-admin-organizations-api
    name: Atlassian Admin Organizations API
    description: The Atlassian Admin Organizations API enables managing Atlassian organizations, user access, and organization-level settings.
    humanURL: https://developer.atlassian.com/cloud/admin/organization/rest/intro/#about
    tags:
      - Administration
      - Cloud Admin
      - Organizations
    properties:
      - type: OpenAPI
        url: openapi/atlassian-admin-api-openapi.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/admin/organization/rest/
      - type: JSONLD
        url: json-ld/atlassian-admin-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-admin-domain-page-schema.json
  - aid: atlassian:atlassian-admin-user-management-api
    name: Atlassian Admin User Management API
    description: The Atlassian Admin User Management API enables managing user accounts and profiles across an Atlassian organization.
    humanURL: https://developer.atlassian.com/cloud/admin/user-management/rest/intro/
    tags:
      - Accounts
      - Administration
      - Users
    properties:
      - type: OpenAPI
        url: openapi/atlassian-admin-api-openapi.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/admin/user-management/rest/
      - type: JSONLD
        url: json-ld/atlassian-admin-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-admin-domain-page-schema.json
  - aid: atlassian:atlassian-admin-user-provisioning-api
    name: Atlassian Admin User Provisioning API
    description: The Atlassian Admin User Provisioning API enables SCIM-based automated user and group provisioning between identity providers and Atlassian Cloud.
    humanURL: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/intro/
    tags:
      - Administration
      - Identity
      - Provisioning
      - SCIM
    properties:
      - type: OpenAPI
        url: openapi/atlassian-admin-api-openapi.yml
      - type: Documentation
        url: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/
      - type: JSONLD
        url: json-ld/atlassian-admin-context.jsonld
      - type: JSONSchema
        url: json-schema/atlassian-admin-domain-page-schema.json
  - aid: atlassian:atlassian-forge-platform-rest-api
    name: Atlassian Forge Platform REST API
    description: The Atlassian Forge Platform REST API provides programmatic access to the Forge serverless cloud app development platform.
    humanURL: https://developer.atlassian.com/platform/forge/rest/v2/
    tags:
      - Cloud Apps
      - Forge
      - Platform
      - Serverless
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/platform/forge/rest/v2/
      - type: GettingStarted
        url: https://developer.atlassian.com/platform/forge/getting-started/
  - aid: atlassian:atlassian-jira-service-management-ops-alerts-api
    name: Atlassian Jira Service Management Operations Alerts API
    description: The Atlassian Jira Service Management Operations Alerts API enables managing alerts for proactive incident management within JSM.
    humanURL: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/api-group-alerts/
    tags:
      - Alerts
      - ITSM
      - Operations
      - Service Desk
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/api-group-alerts/
      - type: GettingStarted
        url: https://developer.atlassian.com/cloud/jira/service-desk-ops/introduction/introduction/
  - aid: atlassian:atlassian-jira-service-management-ops-incidents-api
    name: Atlassian Jira Service Management Operations Incidents API
    description: The Atlassian Jira Service Management Operations Incidents API enables managing incident lifecycle operations within JSM.
    humanURL: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/intro/
    tags:
      - Incidents
      - ITSM
      - Operations
      - Service Desk
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/intro/
  - aid: atlassian:atlassian-incidents-rest-api
    name: Atlassian Incidents REST API
    description: The Atlassian Incidents REST API enables managing major incidents across Atlassian products.
    humanURL: https://developer.atlassian.com/cloud/incidents/
    tags:
      - Alerts
      - Incidents
      - ITSM
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/incidents/rest/api-group-major-incident/
  - aid: atlassian:atlassian-forge-app-rest-api
    name: Atlassian Forge App REST API
    description: The Atlassian Forge App REST API enables Forge apps to expose custom REST API endpoints for external system integration.
    humanURL: https://developer.atlassian.com/platform/forge/rest-apis-for-forge-apps/
    tags:
      - Apps
      - Custom APIs
      - Forge
      - Serverless
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/platform/forge/rest-apis-for-forge-apps/
      - type: APIReference
        url: https://developer.atlassian.com/platform/forge/apis-reference/product-rest-api-reference/
common:
  - type: Portal
    url: https://developer.atlassian.com/cloud/
  - type: GettingStarted
    url: https://developer.atlassian.com/developer-guide/using-the-documentation/
  - type: Authentication
    url: https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/
  - type: ChangeLog
    url: https://developer.atlassian.com/changelog/
  - type: Marketplace
    url: https://developer.atlassian.com/platform/marketplace/
  - type: RateLimits
    url: https://developer.atlassian.com/cloud/jira/platform/rate-limiting/
  - type: PrivacyPolicy
    url: https://www.atlassian.com/legal/privacy-policy
  - type: TermsOfService
    url: https://www.atlassian.com/legal/software-license-agreement
  - type: Support
    url: https://support.atlassian.com/
  - type: Blog
    url: https://blog.developer.atlassian.com/
  - type: StatusPage
    url: https://status.atlassian.com/
  - type: Security
    url: https://www.atlassian.com/trust/security
  - type: SDK
    url: https://developer.atlassian.com/server/framework/atlassian-sdk/
  - type: GitHubOrganization
    url: https://github.com/atlassian
  - type: X
    url: https://twitter.com/Atlassian
  - type: LinkedIn
    url: https://www.linkedin.com/company/atlassian/
  - type: YouTube
    url: https://www.youtube.com/atlassian
  - type: JSONLD
    url: json-ld/atlassian-context.jsonld
  - type: SpectralRules
    url: rules/atlassian-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/atlassian-vocabulary.yaml
  - type: Features
    data:
      - Jira (Software, Work Mgmt, Service Mgmt) per-user pricing
      - Confluence per-user pricing
      - Bitbucket Cloud per-user pricing
      - Trello free + paid tiers
      - Jira Product Discovery, Jira Align (separate)
      - 'Most products: Free up to 10 users (5 for Bitbucket)'
      - 'Standard tiers: Jira ~$9, Confluence ~$6, Bitbucket $3.65, JSM ~$23 per user/mo'
      - Premium adds Atlassian Intelligence, advanced features, 99.9% SLA
      - 'Enterprise: 99.95% uptime, data residency, centralized security'
      - REST API at api.atlassian.com (per-product paths)
      - GraphQL API (for some products)
      - Per-app per-user rate limit ~10 req/sec
      - OAuth 2.0 (3LO), API tokens, OAuth client credentials
      - Atlassian Connect framework for marketplace apps
      - Forge for serverless app dev
      - Atlassian Marketplace ecosystem
    sources:
      - https://www.atlassian.com/pricing
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Agile Software Development
        description: Plan, track, and release software using Scrum and Kanban workflows with Jira Software boards and sprints.
      - name: DevOps and CI/CD
        description: Automate build, test, and deployment pipelines using Bitbucket Pipelines integrated with Jira for end-to-end traceability.
      - name: IT Service Management
        description: Manage IT service requests, incidents, problems, and changes using Jira Service Management with SLA tracking.
      - name: Knowledge Management
        description: Create and organize team documentation, runbooks, and knowledge bases using Confluence spaces and templates.
      - name: Enterprise Administration
        description: Manage organization-wide user provisioning, access policies, and product licenses across Atlassian Cloud products.
      - name: Incident Management
        description: Detect, respond to, and resolve major incidents with JSM operations alerts, on-call schedules, and postmortem tracking.
  - type: Integrations
    data:
      - name: Slack
        description: Real-time notifications and two-way integration between Atlassian products and Slack channels for team communication.
      - name: Microsoft Teams
        description: Integration with Microsoft Teams for Jira and Confluence notifications, issue creation, and collaboration.
      - name: GitHub
        description: Connect GitHub repositories to Jira for linking commits, branches, and pull requests to Jira issues.
      - name: GitLab
        description: Integration with GitLab for development information visibility within Jira issues.
      - name: VS Code
        description: Official Atlassian VS Code extension for Jira issue management and Bitbucket code reviews from the IDE.
      - name: Jenkins
        description: Connect Jenkins CI/CD pipelines to Jira for build and deployment visibility on issues.
      - name: Terraform
        description: Terraform provider for managing Atlassian Operations resources as infrastructure-as-code.
      - name: Opsgenie
        description: Incident management and on-call alerting integration now part of Jira Service Management Operations.
      - name: Kubernetes
        description: Data Center Helm charts for deploying Atlassian products on Kubernetes clusters.
      - name: Backstage
        description: Integration with Backstage developer portal for service catalog and component tracking.
maintainers:
  - FN: Kin Lane
    url: http://apievangelist.com
    email: kin@apievangelist.com
---
