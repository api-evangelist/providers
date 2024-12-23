---
aid: atlassian
url: https://raw.githubusercontent.com/api-search/code/main/_apis/atlassian/apis.md
apis:
  - aid: atlassian:atlassian-jira-announcement-banner-api
    name: Atlassian Jira Announcement Banner API
    tags:
      - Announcement
      - Banner
      - Configurations
      - REST
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-announcement-banner/#api-group-announcement-banner
    overlays:
      - url: overlays/atlassian-rest-api-3-announcementbanner--openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/atlassian-rest-api-3-announcementbanner--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-
          properties/atlassian-rest-api-3-announcementbanner--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-announcement-banner/
        type: Documentation
    description: >-
      This API resource provides the functionality to retrieve and update
      configuration settings for an announcement banner on a website or
      application. Users can access this resource to manage the appearance and
      content of the banner displayed to their audience.
  - aid: atlassian:atlassian-jira-app-api
    name: Atlassian Jira App API
    tags:
      - Applications
      - Custom
      - Fields
      - REST
      - Value
      - Configurations
      - Context
      - Keys
    overlays:
      - url: overlays/atlassian-rest-api-3-app--openapi-search.yml
        type: OpenAPI
      - url: overlays/atlassian-rest-api-3-app--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/atlassian-rest-api-3-app--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-custom-field-values--apps-/
        type: Documentation
    description: >-
      This resource represents the values of custom fields added by Forge apps.
      Use it to update the value of a custom field on issues.
  - aid: atlassian:atlassian-jira-application-properties-api
    name: Atlassian Jira Application Properties API
    tags:
      - Advanced
      - Applications
      - Properties
      - REST
      - Settings
      - Sets
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-app-properties/#api-group-app-properties
    overlays:
      - url: >-
          overlays/atlassian-rest-api-3-application-properties--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/atlassian-rest-api-3-application-properties--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-app-properties/
        type: Documentation
    description: >-
      This resource represents app properties. Use it to store arbitrary data
      for your Connect app.
  - aid: atlassian:atlassian-jira-application-role-api
    name: Atlassian Jira Application Role API
    tags:
      - Application Roles
      - Applications
      - Keys
      - REST
      - Roles
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-application-roles/#api-group-application-roles
    overlays:
      - url: overlays/atlassian-rest-api-3-applicationrole--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-applicationrole--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-application-roles/
        type: Documentation
    description: >-
      This resource represents application roles. Use it to get details of an
      application role or all application roles.
  - aid: atlassian:atlassian-jira-attachment-api
    name: Atlassian Jira Attachment API
    tags:
      - Attachments
      - Content
      - REST
      - Jira
      - Meta
      - Settings
      - Thumbnails
      - Metadata
      - Expand
      - Expanded
      - Human
      - Contents
      - Raw
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-attachments/#api-group-issue-attachments
    overlays:
      - url: overlays/atlassian-rest-api-3-attachment--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-attachment--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-attachments/
        type: Documentation
    description: >-
      This resource represents issue attachments and the attachment settings for
      Jira. Use it to get the metadata for an attachment, delete an attachment,
      and view the metadata for the contents of an attachment. Also, use it to
      get the attachment settings for Jira.
  - aid: atlassian:atlassian-jira-auditing-api
    name: Atlassian Jira Auditing API
    tags:
      - Audit
      - Auditing
      - REST
      - Record
      - Records
    humanURL: https://developer.atlassian.com/server/framework/atlassian-sdk/audit/
    overlays:
      - url: overlays/atlassian-rest-api-3-auditing--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-auditing--openapi-original.yml
        type: OpenAPI
      - url: https://developer.atlassian.com/server/framework/atlassian-sdk/audit/
        type: Documentation
    description: >+
      Atlassian Audit (Advanced Auditing for DC customers) is a cross-product
      feature available in Atlassian DC products (Bitbucket, Confluence, and
      Jira) which is responsible for storing and retrieving audited events.

  - aid: atlassian:atlassian-jira-avatar-api
    name: Atlassian Jira Avatar API
    tags:
      - Avatars
      - Systems
      - Types
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-avatars/#api-group-avatars
    overlays:
      - url: overlays/atlassian-rest-api-3-avatar--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-avatar--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-avatars/
        type: Documentation
    description: >-
      This resource represents system and custom avatars. Use it to obtain the
      details of system or custom avatars, add and remove avatars from a project
      or issue type, and obtain avatar images.
  - aid: atlassian:atlassian-jira-classification-levels-api
    name: Atlassian Jira Classification Levels API
    tags: []
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-classification-levels/#api-group-classification-levels
    overlays:
      - url: >-
          overlays/atlassian-rest-api-3-classification-levels--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/atlassian-rest-api-3-classification-levels--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-classification-levels/
        type: Documentation
    description: Use to manage the classification levels that are used across Jira.
  - aid: atlassian:atlassian-jira-comment-api
    name: Atlassian Jira Comment API
    tags:
      - Comments
      - IDs
      - REST
      - Keys
      - Properties
      - Sets
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-comments/#api-group-issue-comments
    overlays:
      - url: overlays/atlassian-rest-api-3-comment--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-comment--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-comments/
        type: Documentation
    description: >-
      This resource represents issue comments. Use it to get, create, update,
      and delete a comment from an issue, get all comments from issue, get a
      list of comments by comment ID.
  - aid: atlassian:atlassian-jira-component-api
    name: Atlassian Jira Component API
    tags:
      - Components
      - REST
      - Count
      - Counts
      - Issues
      - Related
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-components/#api-group-project-components
    overlays:
      - url: overlays/atlassian-rest-api-3-component--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-component--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-components/
        type: Documentation
    description: >-
      This resource represents project components. Use it to get, create,
      update, and delete project components. Also get components for project and
      get a count of issues by component.
  - aid: atlassian:atlassian-jira-configuration-api
    name: Atlassian Jira Configuration API
    tags:
      - Configurations
      - Providers
      - REST
      - Selected
      - Time
      - Time Tracking
      - Tracking
      - Options
      - Settings
      - Sets
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jira-settings/#api-group-jira-settings
    overlays:
      - url: overlays/atlassian-rest-api-3-configuration--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-configuration--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jira-settings/
        type: Documentation
    description: >-
      This resource represents various settings in Jira. Use it to get and
      update Jira settings and properties.
  - aid: atlassian:atlassian-jira-custom-field-option-api
    name: Atlassian Jira Custom Field Option API
    tags:
      - Custom
      - Fields
      - Options
      - REST
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options/#api-group-issue-custom-field-options
    overlays:
      - url: overlays/atlassian-rest-api-3-customfieldoption--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/atlassian-rest-api-3-customfieldoption--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options/
        type: Documentation
    description: >-
      This resource represents custom issue field select list options created in
      Jira or using the REST API. This resource supports the following field
      types Checkboxes, Radio Buttons, Select List (single choice), Select List
      (multiple choices), Select List (cascading).
  - aid: atlassian:atlassian-jira-dashboard-api
    name: Atlassian Jira Dashboard API
    tags:
      - Bulk
      - Dashboard
      - Dashboards
      - Edit
      - REST
      - Available
      - Gadgets
      - Search
      - Removes
      - Items
      - Keys
      - Properties
      - Sets
      - Copy
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-dashboards/#api-group-dashboards
    overlays:
      - url: overlays/atlassian-rest-api-3-dashboard--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-dashboard--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-dashboards/
        type: Documentation
    description: >-
      This resource represents dashboards. Use it to obtain the details of
      dashboards as well as get, create, update, or remove item properties and
      gadgets from dashboards.
  - aid: atlassian:atlassian-jira-data-policy-api
    name: Atlassian Jira Data Policy API
    tags:
      - EAP
      - Data
      - Policies
      - Projects
      - REST
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/data-security-policy-developer-guide/
    overlays:
      - url: overlays/atlassian-rest-api-3-data-policy--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-data-policy--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/data-security-policy-developer-guide/
        type: Documentation
    description: >+
      Atlassian is adding the ability for customers to block app access to data
      using data security policies with app access rules. App access rules may
      affect your app by blocking its access to certain data. This guide
      provides an overview of potential impacts to apps and how to address them.

  - aid: atlassian:atlassian-jira-events-api
    name: Atlassian Jira Events API
    tags: []
    humanURL: https://developer.atlassian.com/platform/forge/events-reference/jira/
    overlays:
      - url: overlays/atlassian-rest-api-3-events--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-events--openapi-original.yml
        type: OpenAPI
      - url: https://developer.atlassian.com/platform/forge/events-reference/jira/
        type: Documentation
    description: >-
      Used to manage events that are aavailable across the resources made
      available via Jira API.
  - aid: atlassian:atlassian-jira-expression-api
    name: Atlassian Jira Expression API
    tags:
      - Analysis
      - Expression
      - Jira
      - REST
      - EULA
      - Evaluate
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jira-expressions/#api-group-jira-expressions
    overlays:
      - url: overlays/atlassian-rest-api-3-expression--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-expression--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jira-expressions/
        type: Documentation
    description: >-
      Jira expressions is a domain-specific language designed with Jira in mind,
      evaluated on the Jira Cloud side. It can be used to evaluate custom code
      in the context of Jira entities.
  - aid: atlassian:atlassian-jira-field-api
    name: Atlassian Jira Field API
    tags:
      - Fields
      - Paginated
      - REST
      - Search
      - Trash
      - Trashed
      - Custom
      - Context
      - Contexts
      - Default
      - Value
      - Values
      - Sets
      - Issue Type Mappings
      - Issues
      - Types
      - Mapping
      - Projects
      - Project Mappings
      - Issue Types
      - Removes
      - (context)
      - Options
      - Move
      - Reorder
      - Assign
      - Screens
      - Keys
      - Edit
      - Selectable
      - Suggestions
      - Visible
      - Replace
      - Restore
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/#api-group-issue-fields
    overlays:
      - url: overlays/atlassian-rest-api-3-field--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-field--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/
        type: Documentation
    description: >-
      This resource represents issue fields, both system and custom fields. Use
      it to get fields, field configurations, and create custom fields.
  - aid: atlassian:atlassian-jira-field-configuration-api
    name: Atlassian Jira Field Configuration API
    tags:
      - Configurations
      - Field Configurations
      - Fields
      - REST
      - Items
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-field-configurations/#api-group-issue-field-configurations
    overlays:
      - url: overlays/atlassian-rest-api-3-fieldconfiguration--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/atlassian-rest-api-3-fieldconfiguration--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-field-configurations/
        type: Documentation
    description: >-
      This resource represents issue field configurations. Use it to get, set,
      and delete field configurations and field configuration schemes.
  - aid: atlassian:atlassian-jira-field-configuration-scheme-api
    name: Atlassian Jira Field Configuration Scheme API
    tags:
      - Configurations
      - Field Configuration Scheme
      - Fields
      - Issues
      - Items
      - Mapping
      - REST
      - Types
      - Projects
      - Schemes
      - Assign
      - Removes
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-field-configurations/#api-group-issue-field-configurations
    overlays:
      - url: >-
          overlays/atlassian-rest-api-3-fieldconfigurationscheme--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/atlassian-rest-api-3-fieldconfigurationscheme--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-field-configurations/
        type: Documentation
    description: >-
      This resource represents issue field configurations. Use it to get, set,
      and delete field configurations and field configuration schemes.
  - aid: atlassian:atlassian-jira-filter-api
    name: Atlassian Jira Filter API
    tags:
      - Default
      - Filter
      - REST
      - Scopes
      - Share
      - Sets
      - Favorite
      - Favourite
      - Filters
      - Search
      - Columns
      - Reset
      - Removes
      - Change
      - Owners
      - Permission
      - Permissions
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-filters/#api-group-filters
    overlays:
      - url: overlays/atlassian-rest-api-3-filter--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-filter--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-filters/
        type: Documentation
    description: >-

      Postman Collection

      OpenAPI

      This resource represents filters. Use it to get, create, update, or delete
      filters. Also use it to configure the columns for a filter and set
      favorite filters.
  - aid: atlassian:atlassian-jira-group-api
    name: Atlassian Jira Group API
    tags:
      - Bulk
      - Groups
      - REST
      - Members
      - Users
      - Removes
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-groups/#api-group-groups
    overlays:
      - url: overlays/atlassian-rest-api-3-group--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-group--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-groups/
        type: Documentation
    description: >-
      This resource represents groups of users. Use it to get, create, find, and
      delete groups as well as add and remove users from groups. ([WARNING] The
      standard Atlassian group names are default names only and can be edited or
      deleted. 
  - aid: atlassian:atlassian-jira-groups-api
    name: Atlassian Jira Groups API
    tags:
      - Find
      - Groups
      - Picker
      - REST
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-groups/#api-group-groups
    overlays:
      - url: overlays/atlassian-rest-api-3-groups--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-groups--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-groups/
        type: Documentation
    description: >-
      This resource represents groups of users. Use it to get, create, find, and
      delete groups as well as add and remove users from groups. ([WARNING] The
      standard Atlassian group names are default names only and can be edited or
      deleted. 
  - aid: atlassian:atlassian-jira-group-user-picker-api
    name: Atlassian Jira Group User Picker API
    tags: []
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-group-and-user-picker/#api-group-group-and-user-picker
    overlays:
      - url: overlays/atlassian-rest-api-3-groupuserpicker--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-groupuserpicker--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-group-and-user-picker/
        type: Documentation
    description: >-
      This resource represents a list of users and a list of groups. Use it to
      obtain the details to populate user and group picker suggestions list.
  - aid: atlassian:atlassian-jira-license-metrics-api
    name: Atlassian Jira License Metrics API
    tags:
      - Instances
      - Licenses
      - REST
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-license-metrics/#api-group-license-metrics
    overlays:
      - url: overlays/atlassian-rest-api-3-instance--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-instance--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-license-metrics/
        type: Documentation
    description: >-
      This resource represents license metrics. Use it to get available metrics
      for Jira licences.
  - aid: atlassian:atlassian-jira-issue-api
    name: Atlassian Jira Issue API
    tags:
      - Archive
      - Issues
      - JQL
      - REST
      - ID/key
      - Bulk
      - Meta
      - Metadata
      - Issue Types
      - Keys
      - Projects
      - Types
      - Fields
      - Picker
      - Suggestions
      - Properties
      - Sets
      - Multi
      - Keys/ID
      - Unarchive
      - Is
      - Watching
      - Edit
      - Assign
      - Assignee
      - Attachments
      - Change Logs
      - IDs
      - Comments
      - Notifications
      - Notify
      - Send
      - Global
      - ID
      - Link
      - Remote
      - Remote Links
      - Links
      - Transitions
      - Votes
      - Watchers
      - Worklogs
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/#api-group-issues
    overlays:
      - url: overlays/atlassian-rest-api-3-issue--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-issue--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/
        type: Documentation
    description: Used to managine issues for Jira resources.
  - aid: atlassian:atlassian-jira-issue-link-api
    name: Atlassian Jira Issue Link API
    tags:
      - Issues
      - Link
      - REST
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-links/#api-group-issue-links
    overlays:
      - url: overlays/atlassian-rest-api-3-issuelink--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-issuelink--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-links/
        type: Documentation
    description: >-
      This resource represents links between issues. Use it to get, create, and
      delete links between issues.
  - aid: atlassian:atlassian-jira-issue-link-type-api
    name: Atlassian Jira Issue Link Type API
    tags:
      - Issues
      - Link
      - REST
      - Types
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-links/#api-group-issue-links
    overlays:
      - url: overlays/atlassian-rest-api-3-issuelinktype--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-issuelinktype--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-links/
        type: Documentation
    description: >-
      This resource represents links between issues. Use it to get, create, and
      delete links between issues.
  - aid: atlassian:atlassian-jira-issue-link-type-api
    name: Atlassian Jira Issue Link Type API
    tags:
      - Issues
      - Link
      - REST
      - Types
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-link-types/#api-group-issue-link-types
    overlays:
      - url: overlays/atlassian-rest-api-3-issuelinktype--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-issuelinktype--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-link-types/
        type: Documentation
    description: >+
      This resource represents issue link types. Use it to get, create, update,
      and delete link issue types as well as get lists of all link issue types.

  - aid: atlassian:atlassian-jira-issues-api
    name: Atlassian Jira Issues API
    tags:
      - Archive
      - Archived
      - Exports
      - Issues
      - REST
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/#api-group-issues
    overlays:
      - url: overlays/atlassian-rest-api-3-issues--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-issues--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/
        type: Documentation
    description: This is for managing the issues across Jira resources.
  - aid: atlassian:atlassian-jira-issue-security-schemes-api
    name: Atlassian Jira Issue Security Schemes API
    tags:
      - Issue Security Schemes
      - Issues
      - Levels
      - REST
      - Security
      - Default
      - Sets
      - Members
      - Projects
      - Schemes
      - Using
      - Associate
      - Search
      - Removes
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-group-issue-security-schemes
    overlays:
      - url: overlays/atlassian-rest-api-3-issuesecurityschemes--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/atlassian-rest-api-3-issuesecurityschemes--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/
        type: Documentation
    description: >-
      This resource represents issue security schemes. Use it to get an issue
      security scheme or a list of issue security schemes. Issue security
      schemes control which users or groups of users can view an issue. When an
      issue security scheme is associated with a project, its security levels
      can be applied to issues in that project. Sub-tasks also inherit the
      security level of their parent issue.
  - aid: atlassian:atlassian-jira-issue-type-api
    name: Atlassian Jira Issue Type API
    tags:
      - Issue Types
      - Issues
      - Projects
      - REST
      - Types
      - Alternatives
      - Avatars
      - Load
      - Keys
      - Properties
      - Sets
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-types/#api-group-issue-types
    overlays:
      - url: overlays/atlassian-rest-api-3-issuetype--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-issuetype--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-types/
        type: Documentation
    description: >-
      This resource represents issues types. Use it to get, create, update, and
      delete issue types, get all issue types for a user, get alternative issue
      types, and set an avatar for an issue type.
  - aid: atlassian:atlassian-jira-issue-type-scheme-api
    name: Atlassian Jira Issue Type Scheme API
    tags:
      - Issue Type Schemes
      - Issues
      - Items
      - Mapping
      - REST
      - Schemes
      - Types
      - Projects
      - Assign
      - Issue Types
      - Change
      - Move
      - Orders
      - Removes
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-group-issue-type-schemes
    overlays:
      - url: overlays/atlassian-rest-api-3-issuetypescheme--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-issuetypescheme--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/
        type: Documentation
    description: >-
      This resource represents issue type schemes in classic projects. Use it to
      get issue type schemes and a list of the projects that use them, associate
      issue type schemes with projects, add issue types to issue type schemes,
      delete issue types from issue type schemes, create, update, and delete
      issue type schemes, change the order of issue types in issue type schemes.
  - aid: atlassian:atlassian-jira-issue-type-screen-scheme-api
    name: Atlassian Jira Issue Type Screen Scheme API
    tags:
      - Issue Type Screen Schemes
      - Issues
      - Items
      - Mapping
      - REST
      - Schemes
      - Screen
      - Types
      - Projects
      - Assign
      - Append
      - Default
      - Removes
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/#api-group-issue-type-screen-schemes
    overlays:
      - url: >-
          overlays/atlassian-rest-api-3-issuetypescreenscheme--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/atlassian-rest-api-3-issuetypescreenscheme--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/
        type: Documentation
    description: >-
      This resource represents issue type screen schemes. Use it to get issue
      type screen schemes and a list of the projects that use them, create issue
      type screen schemes, update issue type screen schemes, delete issue type
      screen schemes, associate issue type screen schemes with projects, append
      issue type to screen scheme mappings to issue type screen schemes, remove
      issue type to screen scheme mappings from issue type screen schemes.,
      update default screen scheme of issue type screen scheme.
  - aid: atlassian:atlassian-jira-jql-api
    name: Atlassian Jira Jql API
    tags:
      - (GET)
      - Autocomplete Data
      - Data
      - Fields
      - JQL
      - REST
      - References
      - (POST)
      - Auto
      - Complete
      - Suggestions
      - (apps)
      - Computation
      - Functions
      - Pre Computations
      - Against
      - Checks
      - Issues
      - Match
      - Parse
      - Queries
      - Accounts
      - Convert
      - IDs
      - Users
      - Sanitize
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-group-issue-search
    overlays:
      - url: overlays/atlassian-rest-api-3-jql--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-jql--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/
        type: Documentation
    description: >-
      This resource represents various ways to search for issues. Use it to
      search for issues with a JQL query and find issues to populate an issue
      picker.
  - aid: atlassian:atlassian-jira-label-api
    name: Atlassian Jira Label API
    tags: []
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-labels/#api-group-labels
    overlays:
      - url: overlays/atlassian-rest-api-3-label--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-label--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-labels/
        type: Documentation
    description: >-
      This resource represents available labels. Use it to get available labels
      for the global label field.
  - aid: atlassian:atlassian-jira-license-api
    name: Atlassian Jira License API
    tags:
      - Approximate
      - Count
      - Licenses
      - REST
      - Applications
      - Keys
      - Products
    humanURL: >-
      https://developer.atlassian.com/platform/marketplace/license-api-for-cloud-apps/
    overlays:
      - url: overlays/atlassian-rest-api-3-license--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-license--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/platform/marketplace/license-api-for-cloud-apps/
        type: Documentation
    description: >+
      Atlassian Connect provides a set of REST APIs specifically designed for
      use by cloud apps. Requests to these resources are made against the Jira
      or Confluence Cloud instance, not the Marketplace API.

  - aid: atlassian:atlassian-jira-my-permissions-api
    name: Atlassian Jira My Permissions API
    tags: []
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-permissions/#api-group-permissions
    overlays:
      - url: overlays/atlassian-rest-api-3-mypermissions--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-mypermissions--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-permissions/
        type: Documentation
    description: >-
      This resource represents permissions. Use it to obtain details of all
      permissions and determine whether the user has certain permissions.
  - aid: atlassian:atlassian-jira-my-preferences-api
    name: Atlassian Jira My Preferences API
    tags:
      - Locales
      - Prferences
      - REST
      - Sets
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-myself/#api-group-myself
    overlays:
      - url: overlays/atlassian-rest-api-3-mypreferences--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-mypreferences--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-myself/
        type: Documentation
    description: >-
      This resource represents information about the current user, such as basic
      details, group membership, application roles, preferences, and locale. Use
      it to get, create, update, and delete (restore default) values of the
      user's preferences and locale.
  - aid: atlassian:atlassian-jira-myself-api
    name: Atlassian Jira Myself API
    tags: []
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-myself/#api-group-myself
    overlays:
      - url: overlays/atlassian-rest-api-3-myself--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-myself--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-myself/
        type: Documentation
    description: >-
      This resource represents information about the current user, such as basic
      details, group membership, application roles, preferences, and locale. Use
      it to get, create, update, and delete (restore default) values of the
      user's preferences and locale.
  - aid: atlassian:atlassian-jira-notification-scheme-api
    name: Atlassian Jira Notification Scheme API
    tags:
      - Notifications
      - Notificationscheme
      - Paginated
      - Projects
      - REST
      - Schemes
      - Using
      - Removes
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-notification-schemes/#api-group-issue-notification-schemes
    overlays:
      - url: overlays/atlassian-rest-api-3-notificationscheme--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/atlassian-rest-api-3-notificationscheme--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-notification-schemes/
        type: Documentation
    description: >-
      This resource represents notification schemes, lists of events and the
      recipients who will receive notifications for those events. Use it to get
      details of a notification scheme and a list of notification schemes.
  - aid: atlassian:atlassian-jira-permissions-api
    name: Atlassian Jira Permissions API
    tags:
      - Bulk
      - Checks
      - Permissions
      - REST
      - Permitted
      - Projects
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-permissions/#api-group-permissions
    overlays:
      - url: overlays/atlassian-rest-api-3-permissions--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-permissions--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-permissions/
        type: Documentation
    description: >-
      This resource represents permissions. Use it to obtain details of all
      permissions and determine whether the user has certain permissions.
  - aid: atlassian:atlassian-jira-permission-scheme-api
    name: Atlassian Jira Permission Scheme API
    tags:
      - Permission
      - Permission Schemes
      - REST
      - Schemes
      - Grants
      - Grants""
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-permission-schemes/#api-group-project-permission-schemes
    overlays:
      - url: overlays/atlassian-rest-api-3-permissionscheme--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-permissionscheme--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-permission-schemes/
        type: Documentation
    description: >-
      This resource represents permission schemes for a project. Use this
      resource to get details of a project's issue security levels available to
      the calling user, get the permission scheme associated with the project or
      assign different permission scheme to the project, get details of a
      project's issue security scheme.
  - aid: atlassian:atlassian-jira-priority-api
    name: Atlassian Jira Priority API
    tags:
      - Default
      - Priorities
      - REST
      - Sets
      - Move
      - Search
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-priorities/#api-group-issue-priorities
    overlays:
      - url: overlays/atlassian-rest-api-3-priority--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-priority--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-priorities/
        type: Documentation
    description: >-
      his resource represents issue priorities. Use it to get, create and update
      issue priorities and details for individual issue priorities.
  - aid: atlassian:atlassian-jira-project-api
    name: Atlassian Jira Project API
    tags:
      - Projects
      - REST
      - Recent
      - Paginated
      - Search
      - Types
      - Accessible
      - Licensed
      - Keys
      - Archive
      - Avatars
      - Sets
      - Load
      - Classifications
      - Data
      - Default
      - Levels
      - Removes
      - Components
      - Asynchronously
      - Features
      - Feature
      - States
      - Properties
      - Archived
      - Restore
      - Roles
      - Actors
      - Details
      - Role Details
      - Statuses
      - Versions
      - Emails
      - Project's
      - Sender
      - Hierarchy
      - Issues
      - Issue Security Level Scheme
      - Schemes
      - Security
      - Notifications
      - Notificationscheme
      - Assigned
      - Permission
      - Permission Schemes
      - Assign
      - Security Levels
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-group-projects
    overlays:
      - url: overlays/atlassian-rest-api-3-project--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-project--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/
        type: Documentation
    description: >-
      This resource represents projects. Use it to get, create, update, and
      delete projects. Also get statuses available to a project, a project's
      notification schemes, and update a project's type.
  - aid: atlassian:atlassian-jira-project-category-api
    name: Atlassian Jira Project Category API
    tags:
      - Categories
      - Projects
      - REST
      - ID
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-categories/#api-group-project-categories
    overlays:
      - url: overlays/atlassian-rest-api-3-projectcategory--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-projectcategory--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-categories/
        type: Documentation
    description: >-
      This resource represents project categories. Use it to create, update, and
      delete project categories as well as obtain a list of all project
      categories and details of individual categories. For more information on
      managing project categories, see Adding, assigning, and deleting project
      categories.
  - aid: atlassian:atlassian-jira-project-validate-api
    name: Atlassian Jira Project Validate API
    tags:
      - Ate
      - Keys
      - Projects
      - Projectval
      - REST
      - Validate
      - Val
      - Valid
      - Names
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-key-and-name-validation/#api-group-project-key-and-name-validation
    overlays:
      - url: overlays/atlassian-rest-api-3-projectvalidate--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-projectvalidate--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-key-and-name-validation/
        type: Documentation
    description: This resource provides validation for project keys and names.
  - aid: atlassian:atlassian-jira-resolution-api
    name: Atlassian Jira Resolution API
    tags:
      - Default
      - REST
      - Resolutions
      - Sets
      - Move
      - Search
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-resolutions/#api-group-issue-resolutions
    overlays:
      - url: overlays/atlassian-rest-api-3-resolution--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-resolution--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-resolutions/
        type: Documentation
    description: >-
      This resource represents issue resolution values. Use it to obtain a list
      of all issue resolution values and the details of individual resolution
      values.
  - aid: atlassian:atlassian-jira-role-api
    name: Atlassian Jira Role API
    tags:
      - Projects
      - REST
      - Roles
      - ID
      - Partial
      - Actors
      - Default
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-project-roles/#api-group-project-roles
    overlays:
      - url: overlays/atlassian-rest-api-3-role--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-role--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-project-roles/
        type: Documentation
    description: >-
      This resource represents the roles that users can play in projects. Use
      this resource to get, create, update, and delete project roles.
  - aid: atlassian:atlassian-jira-screens-api
    name: Atlassian Jira Screens API
    tags:
      - Default
      - Fields
      - REST
      - Screen
      - Screens
      - Bulk
      - Tabs
      - Available
      - Removes
      - Move
      - POS
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-screens/
    overlays:
      - url: overlays/atlassian-rest-api-3-screens--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-screens--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-screens/
        type: Documentation
    description: >-
      This resource represents the screens used to record issue details. Use it
      to get details of all screens, get details of all the fields available for
      use on screens, create screens, delete screens, update screens, add a
      field to the default screen.
  - aid: atlassian:atlassian-jira-screens-scheme-api
    name: Atlassian Jira Screens Scheme API
    tags:
      - REST
      - Schemes
      - Screen
      - Screen Scheme
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-screen-schemes/#api-group-screen-schemes
    overlays:
      - url: overlays/atlassian-rest-api-3-screenscheme--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-screenscheme--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-screen-schemes/
        type: Documentation
    description: >-
      This resource represents screen schemes in classic projects. Use it to
      get, create, update, and delete screen schemes.
  - aid: atlassian:atlassian-jira-search-api
    name: Atlassian Jira Search API
    tags:
      - IDs
      - Issues
      - JQL
      - REST
      - Search
      - Using
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-group-issue-search
    overlays:
      - url: overlays/atlassian-rest-api-3-search--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-search--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/
        type: Documentation
    description: >-
      This resource represents various ways to search for issues. Use it to
      search for issues with a JQL query and find issues to populate an issue
      picker.
  - aid: atlassian:atlassian-jira-security-level-api
    name: Atlassian Jira Security Level API
    tags:
      - Issues
      - Levels
      - REST
      - Security
      - Security Levels
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-security-level/#api-group-issue-security-level
    overlays:
      - url: overlays/atlassian-rest-api-3-securitylevel--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-securitylevel--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-security-level/
        type: Documentation
    description: >-
      This resource represents issue security levels. Use it to obtain the
      details of any issue security level. For more information about issue
      security levels, see Configuring issue-level security.
  - aid: atlassian:atlassian-jira-server-info-api
    name: Atlassian Jira Server Info API
    tags: []
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-server-info/#api-group-server-info
    overlays:
      - url: overlays/atlassian-rest-api-3-serverinfo--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-serverinfo--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-server-info/
        type: Documentation
    description: This resource provides information about the Jira instance.
  - aid: atlassian:atlassian-jira-settings-api
    name: Atlassian Jira Settings API
    tags:
      - Columns
      - Default
      - Issues
      - Navigators
      - REST
      - Settings
      - Sets
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jira-settings/#api-group-jira-settings
    overlays:
      - url: overlays/atlassian-rest-api-3-settings--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-settings--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jira-settings/
        type: Documentation
    description: >-
      This resource represents various settings in Jira. Use it to get and
      update Jira settings and properties.
  - aid: atlassian:atlassian-jira-status-api
    name: Atlassian Jira Status API
    tags:
      - Names
      - REST
      - Status
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-statuses/#api-rest-api-3-status-get
    overlays:
      - url: overlays/atlassian-rest-api-3-status--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-status--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-statuses/
        type: Documentation
    description: >-
      This resource represents issue workflow statuses. Use it to obtain a list
      of all statuses associated with workflows and the details of a status.
  - aid: atlassian:atlassian-jira-status-category-api
    name: Atlassian Jira Status Category API
    tags:
      - Categories
      - Keys
      - REST
      - Status
      - Status Categories
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-status-categories/#api-group-workflow-status-categories
    overlays:
      - url: overlays/atlassian-rest-api-3-statuscategory--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-statuscategory--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-status-categories/
        type: Documentation
    description: >-
      This resource represents status categories. Use it to obtain a list of all
      status categories and the details of a category. Status categories
      provided a mechanism for categorizing statuses.
  - aid: atlassian:atlassian-jira-statuses-api
    name: Atlassian Jira Statuses API
    tags:
      - Paginated
      - REST
      - Search
      - Statuses
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-statuses/#api-rest-api-3-status-get
    overlays:
      - url: overlays/atlassian-rest-api-3-statuses--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-statuses--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-statuses/
        type: Documentation
    description: >-
      This resource represents issue workflow statuses. Use it to obtain a list
      of all statuses associated with workflows and the details of a status.
  - aid: atlassian:atlassian-jira-task-api
    name: Atlassian Jira Task API
    tags:
      - REST
      - Tasks
      - Cancel
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/#api-group-tasks
    overlays:
      - url: overlays/atlassian-rest-api-3-task--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-task--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/
        type: Documentation
    description: >-
      This resource represents a long-running asynchronous tasks. Use it to
      obtain details about the progress of a long-running task or cancel a
      long-running task.
  - aid: atlassian:atlassian-jira-ui-modifications-api
    name: Atlassian Jira UI Modifications API
    tags:
      - Modifications
      - REST
      - UI
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-ui-modifications--apps-/#api-group-ui-modifications--apps-
    overlays:
      - url: overlays/atlassian-rest-api-3-uimodifications--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-uimodifications--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-ui-modifications--apps-/
        type: Documentation
    description: >-
      UI modifications is a feature available for Forge apps only. It enables
      Forge apps to control how selected Jira fields behave on the following
      views: global issue create, issue view. For example: hide specific fields,
      set them as required, etc.
  - aid: atlassian:atlassian-jira-universal-avatar-api
    name: Atlassian Jira Universal Avatar API
    tags:
      - Avatars
      - Entities
      - Owners
      - REST
      - Types
      - Universal
      - Load
      - Objects
      - Owning
      - Images
      - View
      - ID
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-avatars/#api-group-avatars
    overlays:
      - url: overlays/atlassian-rest-api-3-universal-avatar--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-universal-avatar--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-avatars/
        type: Documentation
    description: >-
      This resource represents system and custom avatars. Use it to obtain the
      details of system or custom avatars, add and remove avatars from a project
      or issue type, and obtain avatar images.
  - aid: atlassian:atlassian-jira-user-api
    name: Atlassian Jira User API
    tags:
      - Assignable
      - Find
      - Multi
      - Projects
      - REST
      - Search
      - Users
      - Issues
      - Bulk
      - Accounts
      - IDs
      - Migrations
      - Columns
      - Default
      - Reset
      - Sets
      - Emails
      - Groups
      - Permission
      - Permissions
      - Picker
      - Keys
      - Properties
      - Queries
      - Browse
      - View Issues
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/#api-group-users
    overlays:
      - url: overlays/atlassian-rest-api-3-user--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-user--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/
        type: Documentation
    description: >-
      This resource represent users. Use it to get, get a list of, create, and
      delete users, get, set, and reset a user's default issue table columns,
      get a list of the groups the user belongs to, and get a list of user
      account IDs for a list of usernames or user keys.
  - aid: atlassian:atlassian-jira-users-api
    name: Atlassian Jira Users API
    tags:
      - REST
      - Search
      - Users
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/
    overlays:
      - url: overlays/atlassian-rest-api-3-users--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-users--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/
        type: Documentation
    description: >-
      This resource represent users. Use it to get, get a list of, create, and
      delete users, get, set, and reset a user's default issue table columns,
      get a list of the groups the user belongs to, and get a list of user
      account IDs for a list of usernames or user keys.
  - aid: atlassian:atlassian-jira-version-api
    name: Atlassian Jira Version API
    tags:
      - REST
      - Versions
      - Issues
      - Merge
      - Mergeto
      - Move
      - Count
      - Counts
      - Related
      - Version's
      - Related Work
      - Work
      - Removes
      - Replace
      - Swap
      - Unresolved
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-versions/#api-group-project-versions
    overlays:
      - url: overlays/atlassian-rest-api-3-version--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-version--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-versions/
        type: Documentation
    description: >-
      This resource represents project versions. Use it to get, get lists of,
      create, update, move, merge, and delete project versions. This resource
      also provides counts of issues by version.
  - aid: atlassian:atlassian-jira-webhook-api
    name: Atlassian Jira Webhook API
    tags:
      - Failed
      - REST
      - Webhooks
      - Extend
      - Life
      - Refresh
    humanURL: https://developer.atlassian.com/server/jira/platform/webhooks/
    overlays:
      - url: overlays/atlassian-rest-api-3-webhook--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-webhook--openapi-original.yml
        type: OpenAPI
      - url: https://developer.atlassian.com/server/jira/platform/webhooks/
        type: Documentation
    description: >-
      A webhook is a user-defined callback over HTTP. You can use Jira webhooks
      to notify your app or web application when certain events occur in Jira.
      For example, you might want to alert your remote application when an issue
      is updated or when sprint is started. Using a webhook to do this means
      that your remote application doesn't have to periodically poll Jira (via
      the REST APIs) to determine whether changes have occurred.
  - aid: atlassian:atlassian-jira-workflow-api
    name: Atlassian Jira Workflow API
    tags:
      - Configurations
      - REST
      - Rules
      - Transitions
      - Workflows
      - Paginated
      - Search
      - Properties
      - Entities
      - Inactive
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/#api-group-workflows
    overlays:
      - url: overlays/atlassian-rest-api-3-workflow--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-workflow--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/
        type: Documentation
    description: >-
      This resource represents workflows. Use it to Get workflows, Create
      workflows, Update workflows, Delete inactive workflows, Get workflow
      capabilities
  - aid: atlassian:atlassian-jira-workflows-api
    name: Atlassian Jira Workflows API
    tags:
      - Available
      - Capabilities
      - REST
      - Workflows
      - Bulk
      - Ation
      - Val
      - Validate
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/
    overlays:
      - url: overlays/atlassian-rest-api-3-workflows--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-workflows--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/
        type: Documentation
    description: >-
      This resource represents workflows. Use it to Get workflows, Create
      workflows, Update workflows, Delete inactive workflows, Get workflow
      capabilities
  - aid: atlassian:atlassian-jira-workflow-scheme-api
    name: Atlassian Jira Workflow Scheme API
    tags:
      - Associations
      - Projects
      - REST
      - Schemes
      - Workflow Scheme
      - Workflows
      - Assign
      - Bulk
      - Read
      - Mapping
      - Required
      - Status
      - Classic
      - Draft
      - Drafts
      - Default
      - Issue Types
      - Issues
      - Types
      - Sets
      - Publish
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-workflow-schemes/#api-group-workflow-schemes
    overlays:
      - url: overlays/atlassian-rest-api-3-workflowscheme--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-workflowscheme--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-workflow-schemes/
        type: Documentation
    description: >-
      This resource represents workflow schemes. Use it to manage workflow
      schemes and the workflow scheme's workflows and issue types. A workflow
      scheme maps issue types to workflows. A workflow scheme can be associated
      with one or more projects, which enables the projects to use the
      workflow-issue type mappings.
  - aid: atlassian:atlassian-jira-worklog-api
    name: Atlassian Jira Worklog API
    tags:
      - IDs
      - REST
      - Worklogs
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-worklogs/#api-group-issue-worklogs
    overlays:
      - url: overlays/atlassian-rest-api-3-worklog--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-api-3-worklog--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-worklogs/
        type: Documentation
    description: >-
      This resource represents issue worklogs. Use it to get, create, update,
      and delete worklogs, obtain lists of updated or deleted worklogs.
  - aid: atlassian:atlassian-jira-connect-addons-api
    name: Atlassian Jira Connect Addons API
    tags:
      - Addons
      - Applications
      - Atlassian
      - Connect
      - Keys
      - Properties
      - REST
      - Sets
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/getting-started-with-connect/
    overlays:
      - url: overlays/atlassian-rest-atlassian-connect-1-addons--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/atlassian-rest-atlassian-connect-1-addons--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/getting-started-with-connect/
        type: Documentation
    description: >+
      Connect is a development framework for extending Atlassian cloud products.
      Connect gives you control over the tech stack, infrastructure, and
      integration with Atlassian Cloud products. You determine your security
      implementation and authentication with external cloud providers, such as
      AWS, Google Cloud, or Heroku. It handles discovery, installation,
      authentication, and seamless integration into the user interface.

  - aid: atlassian:atlassian-jira-connect-app-api
    name: Atlassian Jira Connect App API
    tags:
      - Applications
      - Atlassian
      - Connect
      - Dynamic
      - Modules
      - REST
      - Removes
      - Register
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/getting-started-with-connect/
    overlays:
      - url: overlays/atlassian-rest-atlassian-connect-1-app--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/atlassian-rest-atlassian-connect-1-app--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/getting-started-with-connect/
        type: Documentation
    description: >+
      Connect is a development framework for extending Atlassian cloud products.
      Connect gives you control over the tech stack, infrastructure, and
      integration with Atlassian Cloud products. You determine your security
      implementation and authentication with external cloud providers, such as
      AWS, Google Cloud, or Heroku. It handles discovery, installation,
      authentication, and seamless integration into the user interface.

  - aid: atlassian:atlassian-jira-connect-migration-api
    name: Atlassian Jira Connect Migration API
    tags:
      - Atlassian
      - Bulk
      - Connect
      - Custom
      - Fields
      - Migrations
      - REST
      - Value
      - Entities
      - Properties
      - Types
      - Configurations
      - Rules
      - Search
      - Transitions
      - Workflows
    humanURL: https://developer.atlassian.com/cloud/jira/platform/connect-api-migration/
    overlays:
      - url: >-
          overlays/atlassian-rest-atlassian-connect-1-migration--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/atlassian-rest-atlassian-connect-1-migration--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/connect-api-migration/
        type: Documentation
    description: >-
      This Atlassian Connect feature provide a mechanism for apps to signal
      readiness for new API behaviors as well as selectively enrol during the
      introduction / deprecation period for the purposes of testing. Development
      of this mechanism was motivated by the introduction of API changes that
      are not backward compatible (e.g. the removal of legacy user references
      from our public cloud REST APIs). Such changes will break existing apps
      that do not yet support the new API version.
  - aid: atlassian:atlassian-jira-connect-service-registry-api
    name: Atlassian Jira Connect Service Registry API
    tags: []
    humanURL: >-
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-service-registry/#api-group-service-registry
    overlays:
      - url: >-
          overlays/atlassian-rest-atlassian-connect-1-service-registry--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/atlassian-rest-atlassian-connect-1-service-registry--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-service-registry/
        type: Documentation
    description: >-
      This resource represents a service registry. Use it to retrieve attributes
      related to a service registry in JSM.
  - aid: atlassian:atlassian-jira-forge-app-api
    name: Atlassian Jira Forge App API
    tags:
      - (Forge)
      - Applications
      - Forge
      - Keys
      - Properties
      - REST
      - Sets
    humanURL: https://developer.atlassian.com/cloud/jira/platform/forge/
    overlays:
      - url: overlays/atlassian-rest-forge-1-app--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-rest-forge-1-app--openapi-original.yml
        type: OpenAPI
      - url: https://developer.atlassian.com/cloud/jira/platform/forge/
        type: Documentation
    description: >-
      Forge is Atlassian's new development platform for building Jira and
      Confluence Cloud apps. 
  - aid: atlassian:atlassian-confluence-audit-api
    name: Atlassian Confluence Audit API
    tags:
      - Audit
      - Exports
      - REST
      - Records
      - Wiki
      - Period
      - Retention
      - Sets
      - Since
      - Time
    humanURL: >-
      https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-audit/#api-group-audit
    overlays:
      - url: overlays/atlassian-wiki-rest-api-audit--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-wiki-rest-api-audit--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-audit/
        type: Documentation
    description: Allows you to create, get, set, and export audit records from Confluence.
  - aid: atlassian:atlassian-confluence-content-api
    name: Atlassian Confluence Content API
    tags:
      - Archive
      - Content
      - Pages
      - REST
      - Wiki
      - Blueprints
      - Draft
      - Instances
      - Publish
      - Shared
      - Legacy
      - CQL
      - Search
      - ID
      - Page
      - Trees
      - Child
      - Children
      - Locations
      - Move
      - Positions
      - Relative
      - Targets
      - Attachments
      - Properties
      - Data
      - Download
      - URI
      - Comments
      - Types
      - Descendants
      - History
      - Body
      - Macro
      - Versions
      - Convert
      - Representation
      - Synchronously
      - Async
      - Asynchronously
      - Labels
      - Parameters
      - Queries
      - Removes
      - Using
      - Notifications
      - Watches
      - Space
      - Copy
      - Hierarchy
      - Page Hierarchy
      - Single
      - Checks
      - Permission
      - Permissions
      - Keys
      - Restrictions
      - Operation
      - Groups
      - Names
      - Status
      - Users
      - States
      - Publishes
      - Sets
      - Available
      - Restore
      - Numbers
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#about
    overlays:
      - url: overlays/atlassian-wiki-rest-api-content--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-wiki-rest-api-content--openapi-original.yml
        type: OpenAPI
      - url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/
        type: Documentation
    description: >-
      This is the reference for the Confluence Cloud REST API v2, with
      definitions and performance intended to be an improvement over v1. You can
      click on the meatball menu in the upper right to download the spec or
      Postman collection.
  - aid: atlassian:atlassian-confluence-content-states-api
    name: Atlassian Confluence Content States API
    tags:
      - Bulk
      - Content
      - REST
      - Removes
      - States
      - Wiki
      - Long
      - Running
      - Settings
      - Tasks
    humanURL: >-
      https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-states/#api-group-content-states
    overlays:
      - url: overlays/atlassian-wiki-rest-api-content-states--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/atlassian-wiki-rest-api-content-states--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-states/
        type: Documentation
    description: Allows you to manage the various state of content published to Confluence.
  - aid: atlassian:atlassian-confluence-content-body-api
    name: Atlassian Confluence Content Body API
    tags:
      - Body
      - Content
      - Content Body
      - Convert
      - REST
      - Wiki
      - Async
      - Asynchronously
      - Converted
      - Current
      - Status
      - Tasks
    humanURL: >-
      https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-body/#api-group-content-body
    overlays:
      - url: overlays/atlassian-wiki-rest-api-contentbody--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-wiki-rest-api-contentbody--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-body/
        type: Documentation
    description: Provides you the ability to manage the content body of Confluence pages.
  - aid: atlassian:atlassian-confluence-inline-tasks-api
    name: Atlassian Confluence Inline Tasks API
    tags:
      - Based
      - Inline
      - Inline Tasks
      - Parameters
      - REST
      - Search
      - Tasks
      - Wiki
      - Global
      - ID
      - Given
    humanURL: >-
      https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-inline-tasks#api-group-inline-tasks
    overlays:
      - url: overlays/atlassian-wiki-rest-api-inlinetasks--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-wiki-rest-api-inlinetasks--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-inline-tasks
        type: Documentation
    description: Allows you to manage inline tasks across Confluence.
  - aid: atlassian:atlassian-confluence-label-api
    name: Atlassian Confluence Label API
    tags: []
    humanURL: >-
      https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-labels/#api-group-content-labels
    overlays:
      - url: overlays/atlassian-wiki-rest-api-label--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-wiki-rest-api-label--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-labels/
        type: Documentation
    description: Provides the ability to label content across Confluence.
  - aid: atlassian:atlassian-confluence-group-api
    name: Atlassian Confluence Group API
    tags:
      - Groups
      - Names
      - REST
      - Wiki
      - Users
      - Members
      - Partial
      - Picker
      - Queries
      - Search
      - Removes
      - Using
    humanURL: >-
      https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-group/#api-wiki-rest-api-group-get
    overlays:
      - url: overlays/atlassian-wiki-rest-api-group--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-wiki-rest-api-group--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-group/
        type: Documentation
    description: >-
      Returns all user groups. The returned groups are ordered alphabetically in
      ascending order by group name.
  - aid: atlassian:atlassian-confluence-longtask-api
    name: Atlassian Confluence Longtask API
    tags:
      - Long Running
      - Longtask
      - REST
      - Tasks
      - Wiki
    humanURL: >-
      https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-long-running-task/#api-wiki-rest-api-longtask-get
    overlays:
      - url: overlays/atlassian-wiki-rest-api-longtask--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-wiki-rest-api-longtask--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-long-running-task/
        type: Documentation
    description: >-
      Returns information about all active long-running tasks (e.g. space
      export), such as how long each task has been running and the percentage of
      each task that has completed.
  - aid: atlassian:atlassian-confluence-relation-api
    name: Atlassian Confluence Relation API
    tags:
      - Entities
      - Find
      - Keys
      - Names
      - REST
      - Related
      - Relation
      - Sources
      - Targets
      - Types
      - Wiki
      - Relationships
    humanURL: >-
      https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-relation/
    overlays:
      - url: overlays/atlassian-wiki-rest-api-relation--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-wiki-rest-api-relation--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-relation/
        type: Documentation
    description: >-
      Provides the ability to manage relationships between content across
      Confluence.
  - aid: atlassian:atlassian-confluence-search-api
    name: Atlassian Confluence Search API
    tags:
      - REST
      - Search
      - Users
      - Wiki
    humanURL: >-
      https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-search/#api-group-search
    overlays:
      - url: overlays/atlassian-wiki-rest-api-search--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-wiki-rest-api-search--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-search/
        type: Documentation
    description: Searches content across Confluence.
  - aid: atlassian:atlassian-confluence-settings-api
    name: Atlassian Confluence Settings API
    tags:
      - Feel
      - REST
      - Settings
      - Wiki
      - Custom
      - Reset
      - Selected
      - Sets
      - Info
      - Systems
      - Theme
      - Themes
      - Global
      - Keys
    humanURL: >-
      https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-settings/#api-group-settings
    overlays:
      - url: overlays/atlassian-wiki-rest-api-settings--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-wiki-rest-api-settings--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-settings/
        type: Documentation
    description: Manages the settings for Confluence groups.
  - aid: atlassian:atlassian-confluence-space-api
    name: Atlassian Confluence Space API
    tags:
      - Private
      - REST
      - Space
      - Wiki
      - Keys
      - Content
      - Permission
      - Custom
      - Removes
      - Types
      - Properties
      - Settings
      - States
      - Suggested
      - Given
      - Theme
      - Sets
      - Reset
      - Watchers
      - Labels
    humanURL: >-
      https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-space/#api-group-space
    overlays:
      - url: overlays/atlassian-wiki-rest-api-space--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-wiki-rest-api-space--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-space/
        type: Documentation
    description: Used to manage all of the Confluence spaces for an account.
  - aid: atlassian:atlassian-confluence-template-api
    name: Atlassian Confluence Template API
    tags:
      - Blueprints
      - REST
      - Templates
      - Wiki
      - Content
      - Page
      - Removes
    humanURL: >-
      https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-template/#api-group-template
    overlays:
      - url: overlays/atlassian-wiki-rest-api-template--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-wiki-rest-api-template--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-template/
        type: Documentation
    description: Provides the ability to manage the templates applied across Confluence.
  - aid: atlassian:atlassian-confluence-user-api
    name: Atlassian Confluence User API
    tags:
      - Anonymous
      - REST
      - Users
      - Wiki
      - Current
      - Groups
      - Members
      - Memberships
      - Bulk
      - Ids
      - Multiple
      - Using
      - Content
      - Status
      - Watchers
      - Removes
      - Labels
      - Names
      - Keys
      - Space
      - Addresses
      - Emails
      - Batches
      - Properties
    humanURL: >-
      https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-user/#api-group-user
    overlays:
      - url: overlays/atlassian-wiki-rest-api-user--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-wiki-rest-api-user--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-user/
        type: Documentation
    description: Provides the ability to manage users as part of a Confluence instance.
  - aid: atlassian:atlassian-confluence-connect-app-module-api
    name: Atlassian Confluence Connect App Module API
    tags:
      - Applications
      - Atlassian
      - Connect
      - Dynamic
      - Modules
      - Register
      - Removes
    humanURL: https://developer.atlassian.com/cloud/confluence/connect-modules/
    overlays:
      - url: overlays/atlassian-atlassian-connect-1-app-module--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/atlassian-atlassian-connect-1-app-module--openapi-original.yml
        type: OpenAPI
      - url: https://developer.atlassian.com/cloud/confluence/connect-modules/
        type: Documentation
    description: >-
      Connect modules are how Connect apps extend and interact with Confluence.
      If you're not familiar with Connect apps, learn how Connect works first.
  - aid: atlassian:atlassian-confluence-analytics-api
    name: Atlassian Confluence Analytics API
    tags:
      - Analytics
      - Content
      - REST
      - Views
      - Wiki
      - Viewers
    humanURL: >-
      https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-analytics/#api-group-analytics
    overlays:
      - url: overlays/atlassian-wiki-rest-api-analytics--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-wiki-rest-api-analytics--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-analytics/
        type: Documentation
    description: >-
      The Confluence Cloud Analytics REST API provides endpoints to access
      analytics data for Confluence content. It allows you to retrieve
      information such as the total number of views and distinct viewers for
      specific content within Confluence Cloud. This API enables developers to
      integrate analytics functionalities into their applications or services,
      providing insights into content engagement and audience interactions
      within Confluence Cloud.
  - aid: atlassian:atlassian-bitbucket-addon-api
    name: Atlassian BitBucket Addon API
    tags:
      - Addons
      - Applications
      - Linkers
      - Keys
      - Linker
      - Values
      - Value
    humanURL: >-
      https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-group-addon
    overlays:
      - url: overlays/atlassian-addon--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-addon--openapi-original.yml
        type: OpenAPI
      - url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/
        type: Documentation
    description: >+
      The addon resource is intended to use used by Bitbucket Cloud Connect
      Apps, and only supports JWT authentication.

  - aid: atlassian:atlassian-bitbucket-hook-events-api
    name: Atlassian BitBucket Hook Events API
    tags:
      - Events
      - Hook
      - Subjects
      - Subscribable
      - Types
      - Webhooks
    humanURL: >-
      https://developer.atlassian.com/cloud/bitbucket/rest/api-group-webhooks/#api-group-webhooks
    overlays:
      - url: overlays/atlassian-hook-events--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-hook-events--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/bitbucket/rest/api-group-webhooks/
        type: Documentation
    description: >-
      Webhooks provide a way to configure Bitbucket Cloud to make requests to
      your server (or another external service) whenever certain events occur in
      Bitbucket Cloud.
  - aid: atlassian:atlassian-bitbucket-pull-requests-api
    name: Atlassian BitBucket Pull Requests API
    tags: []
    humanURL: >-
      https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-group-pullrequests
    overlays:
      - url: overlays/atlassian-pullrequests-selected-user--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-pullrequests-selected-user--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/
        type: Documentation
    description: >-
      Pull requests are a feature that makes it easier for developers to
      collaborate using Bitbucket. They provide a user-friendly web interface
      for discussing proposed changes before integrating them into the official
      project.
  - aid: atlassian:atlassian-bitbucket-repositories-api
    name: Atlassian BitBucket Repositories API
    tags:
      - Repositories
      - Workspaces
      - Slug
      - Branch
      - Restrictions
      - Rules
      - Branching
      - Models
      - Configurations
      - Settings
      - Commit
      - Approve
      - Unapprove
      - Comments
      - Commit's
      - Applications
      - Keys
      - Names
      - Properties
      - Contain
      - Pull
      - Pull Requests
      - Reports
      - Annotations
      - Bulk
      - Statuses
      - Build
      - Status
      - Commits
      - Include/exclude
      - Revisions
      - Using
      - Components
      - Issues
      - Default
      - Reviewers
      - Removes
      - Targets
      - User Names
      - Users
      - Deploy
      - Deployments
      - Uu
      - Environments
      - Variables
      - Compare
      - Difference
      - Statistics
      - Artifacts
      - Download
      - Downloads
      - Uploads
      - File Name
      - Link
      - Currently
      - Effective
      - Changes
      - File History
      - Files
      - Modified
      - Paths
      - Forks
      - Fork
      - Hooks
      - Webhooks
      - Exports
      - Checks
      - Tasks
      - Zip
      - Import
      - Attachments
      - Modify
      - States
      - Change
      - Objects
      - Votes
      - Current
      - If
      - Voted
      - Stop
      - Watching
      - Is
      - Ancestor
      - Base
      - Between
      - Common
      - Merge
      - Milestones
      - Inheritance
      - Overr
      - Sets
      - Patch
      - Explicit
      - Groups
      - Permissions
      - Permission
      - Selected
      - Pipelines
      - Runs
      - Caches
      - Cache
      - Content
      - URI
      - Steps
      - Logs
      - Container
      - Given
      - Services
      - Summaries
      - Tests
      - Cases
      - (output)
      - Case
      - Reasons
      - Next
      - Numbers
      - Schedules
      - Executions
      - Pairs
      - SSH
      - Hosts
      - Known
      - Host
      - Activity
      - Reopen
      - Resolve
      - Threads
      - Decline
      - Pullrequest
      - Branches
      - References
      - Tags
      - Directory
      - Root
      - Uploading
      - Contents
      - Defined
      - Versions
      - Watchers
    humanURL: >-
      https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-group-repositories
    overlays:
      - url: overlays/atlassian-repositories--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-repositories--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/
        type: Documentation
    description: >-
      A Git repository is a virtual storage of your project. It allows you to
      save versions of your code, which you can access when needed. The repo
      resource allows you to access public repos, or repos that belong to a
      specific workspace.
  - aid: atlassian:atlassian-bitbucket-snippets-api
    name: Atlassian BitBucket Snippets API
    tags:
      - Snippets
      - Workspaces
      - Encoded
      - Comments
      - Changes
      - Commits
      - Change
      - Previous
      - Revisions
      - Files
      - HEAD
      - Paths
      - Raw
      - Snippet's
      - Stop
      - Watching
      - Checks
      - Current
      - If
      - Is
      - Users
      - Watchers
      - Nodes
      - Between
      - Difference
      - Versions
      - Patch
    humanURL: >-
      https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-group-snippets
    overlays:
      - url: overlays/atlassian-snippets--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-snippets--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/
        type: Documentation
    description: >-
      Snippets allow you share code segments or files with yourself, members of
      your workspace, or the world. Like pull requests, repositories and
      workspaces, the full set of snippets is defined by what the current user
      has access to. This includes all snippets owned by any of the workspaces
      the user is a member of, or snippets by other users that the current user
      is either watching or has collaborated on (for instance by commenting on
      it).
  - aid: atlassian:atlassian-bitbucket-teams-api
    name: Atlassian BitBucket Teams API
    tags: []
    overlays:
      - url: overlays/atlassian-teams--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-teams--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: atlassian:atlassian-bitbucket-user-api
    name: Atlassian BitBucket User API
    tags:
      - Configurations
      - Explicit
      - Permissions
      - Repositories
      - Slug
      - Users
      - Workspaces
      - Permission
      - Selected
      - Current
      - Addresses
      - Emails
      - Pipelines
      - Variables
      - Uu
      - Applications
      - Keys
      - Names
      - Properties
      - Code
      - Search
      - SSH
      - Projects
    humanURL: >-
      https://developer.atlassian.com/cloud/bitbucket/rest/api-group-users/#api-group-users
    overlays:
      - url: overlays/atlassian-user-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-user-openapi-original.yml
        type: OpenAPI
      - url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-users/
        type: Documentation
    description: >-
      The users resource allows you to access public information associated with
      a user account. Most resources in the users endpoint have been deprecated
      in favor of workspaces.
  - aid: atlassian:atlassian-bitbucket-workspaces-api
    name: Atlassian BitBucket Workspaces API
    tags:
      - Workspaces
      - Hooks
      - Webhooks
      - Members
      - Users
      - Memberships
      - Permissions
      - Repositories
      - Slug
      - Configurations
      - Entities
      - ID
      - Known
      - OIDC
      - Pipelines
      - Keys
      - Keys Json
      - Variables
      - Uu
      - Projects
      - Branching
      - Models
      - Settings
      - Default
      - Reviewers
      - Project's
      - Removes
      - Selected
      - Specific
      - Deploy
      - Explicit
      - Groups
      - Permission
      - Code
      - Search
    humanURL: >-
      https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-group-workspaces
    overlays:
      - url: overlays/atlassian-workspaces--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/atlassian-workspaces--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/
        type: Documentation
    description: >-
      A workspace is where you create repositories, collaborate on your code,
      and organize different streams of work in your Bitbucket Cloud account.
      Workspaces replace the use of teams and users in API calls.
name: Atlassian
tags:
  - Productivity
  - Software Development
  - Code
type: Contract
access: 3rd-Party
created: 2024/04/14
modified: '2024-12-13'
position: Consuming
description: >-
  Atlassian is a software company that develops collaboration, productivity, and
  project management tools to help teams work more efficiently. Its products are
  designed to enhance teamwork, streamline workflows, and support project
  tracking across a wide range of industries.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'

---