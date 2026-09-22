---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 65.6
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 432
  human_in_the_loop: 4
  name: Jira Agentic Access
  operation_count: 814
  slug: jira-agentic-access
  summary_line: 814 operations · 432 acting · 4 human-in-the-loop
api_count: 4
apis:
- description: Version 2 of the Jira Cloud platform REST API, offering the same operations as v3 but without Atlassian Document Format support.
  name: Jira Cloud Platform REST API v2
  slug: jira-cloud-platform-rest-api-v2
- description: Operations APIs for Jira Service Management covering schedules, on-call rotations, alerts, escalations, and incident management.
  name: Jira Service Management Operations REST API
  slug: jira-service-management-operations-rest-api
- description: REST API for Jira Align enterprise agile planning platform, providing access to portfolios, epics, features, and program management data.
  name: Jira Align REST API
  slug: jira-align-rest-api
- description: REST API for Atlassian Customer Service Management providing access to customers, organizations, products, and entitlements data.
  name: Jira Customer Service Management REST API
  slug: jira-customer-service-management-rest-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Manage comments on issues.
  name: Jira Issue Comments API
  slug: jira-issue-comments-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Retrieve issue priority levels.
  name: Jira Issue Priorities API
  slug: jira-issue-priorities-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Search for issues using JQL (Jira Query Language).
  name: Jira Issue Search API
  slug: jira-issue-search-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Retrieve issue statuses.
  name: Jira Issue Statuses API
  slug: jira-issue-statuses-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Retrieve and perform workflow transitions on issues.
  name: Jira Issue Transitions API
  slug: jira-issue-transitions-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Retrieve and manage issue types for projects.
  name: Jira Issue Types API
  slug: jira-issue-types-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Create, read, update, delete, and transition Jira issues.
  name: Jira Issues API
  slug: jira-issues-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Manage Jira projects including metadata, roles, and components.
  name: Jira Projects API
  slug: jira-projects-api
- description: Atlassian's official hosted Model Context Protocol server. An OAuth 2.1 protected endpoint that exposes Jira, Jira Service Management, Confluence, Bitbucket, Compass and Loom to MCP-capable AI clients
  name: Atlassian Remote MCP Server
  slug: atlassian-jira-remote-mcp-server
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Manage comments on issues.
  name: Atlassian Jira Issue Comments API
  slug: atlassian-jira-issue-comments-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Search issues using JQL.
  name: Atlassian Jira Issue Search API
  slug: atlassian-jira-issue-search-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: List and perform workflow transitions.
  name: Atlassian Jira Issue Transitions API
  slug: atlassian-jira-issue-transitions-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Manage worklogs on issues.
  name: Atlassian Jira Issue Worklogs API
  slug: atlassian-jira-issue-worklogs-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Create, read, update and delete Jira issues.
  name: Atlassian Jira Issues API
  slug: atlassian-jira-issues-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Manage Jira projects.
  name: Atlassian Jira Projects API
  slug: atlassian-jira-projects-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Read user information.
  name: Atlassian Jira Users API
  slug: atlassian-jira-users-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents an announcement banner. Use it to retrieve and update banner configuration.
  name: Jira Announcement banner API
  slug: jira-announcement-banner-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents app access rule data policies.
  name: Jira App data policies API
  slug: jira-app-data-policies-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource supports [app migrations](https://developer.atlassian.com/platform/app-migration/). Use it to: - [to request migrated workflow rules details](https://developer.atlassian.com/platform/app'
  name: Jira App migration API
  slug: jira-app-migration-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents app properties. Use it to store arbitrary data for your [Connect app](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps).
  name: Jira App properties API
  slug: jira-app-properties-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents application roles. Use it to get details of an application role or all application roles.
  name: Jira Application roles API
  slug: jira-application-roles-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Assets API from Jira — 2 operation(s) for assets.
  name: Jira Assets API
  slug: jira-assets-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents audits that record activities undertaken in Jira. Use it to get a list of audit records.
  name: Jira Audit records API
  slug: jira-audit-records-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents system and custom avatars. Use it to obtain the details of system or custom avatars, add and remove avatars from a project, issue type or priority and obtain avatar images.
  name: Jira Avatars API
  slug: jira-avatars-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: Apis related to the backlog
  name: Jira Backlog API
  slug: jira-backlog-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: Apis related to boards
  name: Jira Board API
  slug: jira-board-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'APIs related to integrating build data with Jira Software. These APIs are available to Atlassian Connect apps. To use these APIs you must have the `jiraBuildInfoProvider` module in your Connect app''s '
  name: Jira Builds API
  slug: jira-builds-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents classification levels.
  name: Jira Classification levels API
  slug: jira-classification-levels-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Customer API from Jira — 2 operation(s) for customer.
  name: Jira Customer API
  slug: jira-customer-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents dashboards. Use it to obtain the details of dashboards as well as get, create, update, or remove item properties and gadgets from dashboards.
  name: Jira Dashboards API
  slug: jira-dashboards-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: APIs related to integrating deployment data with Jira Software. These APIs are available to Atlassian Connect apps. To use these APIs you must have the `jiraDeploymentInfoProvider` module in your Conn
  name: Jira Deployments API
  slug: jira-deployments-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: APIs related to integrating development information (commits, branches and pull requests) with Jira. These APIs are available to Atlassian Connect apps and on-premise integrations using OAuth. Connect
  name: Jira Development Information API
  slug: jira-development-information-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: APIs related to integrating Dev Ops Components affected by Incident data with Jira Software. These APIs are available to Atlassian Connect apps. To use these APIs you must have the `jiraDevOpsComponen
  name: Jira DevOps Components API
  slug: jira-devops-components-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [modules registered dynamically](https://developer.atlassian.com/cloud/jira/platform/dynamic-modules/) by [Connect apps](https://developer.atlassian.com/cloud/jira/platform/in
  name: Jira Dynamic modules API
  slug: jira-dynamic-modules-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: Apis related to epics
  name: Jira Epic API
  slug: jira-epic-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: APIs related to integrating feature flags with Jira Software. These APIs are available to Atlassian Connect apps. To use these APIs you must have the `jiraFeatureFlagInfoProvider` module in your Conne
  name: Jira Feature Flags API
  slug: jira-feature-flags-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents field schemes which are replacing field configuration schemes to control field associations. They are currently in beta and only available to customers who have opted-in to th
  name: Jira Field schemes API
  slug: jira-field-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents options for sharing [filters](#api-group-Filters). Use it to get share scopes as well as add and remove share scopes from filters.
  name: Jira Filter sharing API
  slug: jira-filter-sharing-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [filters](https://confluence.atlassian.com/x/eQiiLQ). Use it to get, create, update, or delete filters. Also use it to configure the columns for a filter and set favorite filt
  name: Jira Filters API
  slug: jira-filters-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents a list of users and a list of groups. Use it to obtain the details to populate user and group picker suggestions list.
  name: Jira Group and user picker API
  slug: jira-group-and-user-picker-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents groups of users. Use it to get, create, find, and delete groups as well as add and remove users from groups. (\[WARNING\] The standard Atlassian group names are default names '
  name: Jira Groups API
  slug: jira-groups-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Info API from Jira — 1 operation(s) for info.
  name: Jira Info API
  slug: jira-info-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: Apis related to issues
  name: Jira Issue API
  slug: jira-issue-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue attachments and the attachment settings for Jira. Use it to get the metadata for an attachment, delete an attachment, and view the metadata for the contents of an attach
  name: Jira Issue attachments API
  slug: jira-issue-attachments-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the issue bulk operations. Use it to move multiple issues from one project to another project or edit fields of multiple issues in one go. For additional clarity, we have crea
  name: Jira Issue bulk operations API
  slug: jira-issue-bulk-operations-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [issue comment](#api-group-Issue-comments) properties, which provides for storing custom data against an issue comment. Use is to get, set, and delete issue comment properties
  name: Jira Issue comment properties API
  slug: jira-issue-comment-properties-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents the fields associated to project and issue type contexts. Use it to: * assign custom field to projects and issue types.'
  name: Jira Issue custom field associations API
  slug: jira-issue-custom-field-associations-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents configurations stored against a custom field context by a [Forge app](https://developer.atlassian.com/platform/forge/). Configurations are information used by the Forge app at
  name: Jira Issue custom field configuration (apps) API
  slug: jira-issue-custom-field-configuration-apps-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents issue custom field contexts. Use it to: * get, create, update, and delete custom field contexts. * get context to issue types and projects mappings. * get custom field context'
  name: Jira Issue custom field contexts API
  slug: jira-issue-custom-field-contexts-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents custom issue field select list options created in Jira or using the REST API. This resource supports the following field types: * Checkboxes. * Radio Buttons. * Select List (s'
  name: Jira Issue custom field options API
  slug: jira-issue-custom-field-options-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents custom issue field select list options created by a Connect app. See [Issue custom field options](#api-group-Issue-custom-field-options) to manipulate options created in Jira '
  name: Jira Issue custom field options (apps) API
  slug: jira-issue-custom-field-options-apps-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the values of custom fields added by [Forge apps](https://developer.atlassian.com/platform/forge/). Use it to update the value of a custom field on issues.
  name: Jira Issue custom field values (apps) API
  slug: jira-issue-custom-field-values-apps-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue field configurations. Use it to get, set, and delete field configurations and field configuration schemes.
  name: Jira Issue field configurations API
  slug: jira-issue-field-configurations-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue fields, both system and custom fields. Use it to get fields, field configurations, and create custom fields.
  name: Jira Issue fields API
  slug: jira-issue-fields-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [issue link](#api-group-Issue-links) types. Use it to get, create, update, and delete link issue types as well as get lists of all link issue types. To use it, the site must h
  name: Jira Issue link types API
  slug: jira-issue-link-types-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents links between issues. Use it to get, create, and delete links between issues. To use it, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.
  name: Jira Issue links API
  slug: jira-issue-links-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue navigator settings. Use it to get and set issue navigator default columns.
  name: Jira Issue navigator settings API
  slug: jira-issue-navigator-settings-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents notification schemes, lists of events and the recipients who will receive notifications for those events. Use it to get details of a notification scheme and a list of notifica
  name: Jira Issue notification schemes API
  slug: jira-issue-notification-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource supports bulk pinning and unpinning of [issue panels](https://developer.atlassian.com/platform/forge/) that are added by a Forge app. Only Jira administrators can use it.
  name: Jira Issue panels API
  slug: jira-issue-panels-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [issue](#api-group-Issues) properties, which provides for storing custom data against an issue. Use it to get, set, and delete issue properties as well as obtain details of al
  name: Jira Issue properties API
  slug: jira-issue-properties-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents Issue Redaction. Provides APIs to redact issue data.
  name: Jira Issue redaction API
  slug: jira-issue-redaction-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents remote issue links, a way of linking Jira to information in other systems. Use it to get, create, update, and delete remote issue links either by ID or global ID. The global I
  name: Jira Issue remote links API
  slug: jira-issue-remote-links-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue resolution values. Use it to obtain a list of all issue resolution values and the details of individual resolution values.
  name: Jira Issue resolutions API
  slug: jira-issue-resolutions-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue security levels. Use it to obtain the details of any issue security level. For more information about issue security levels, see [Configuring issue-level security](https
  name: Jira Issue security level API
  slug: jira-issue-security-level-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue security schemes. Use it to get an issue security scheme or a list of issue security schemes. Issue security schemes control which users or groups of users can view an i
  name: Jira Issue security schemes API
  slug: jira-issue-security-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents [issue type](#api-group-Issue-types) properties, which provides for storing custom data against an issue type. Use it to get, create, and delete issue type properties as well '
  name: Jira Issue type properties API
  slug: jira-issue-type-properties-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents issue type schemes in classic projects. Use it to: * get issue type schemes and a list of the projects that use them. * associate issue type schemes with projects. * add issue'
  name: Jira Issue type schemes API
  slug: jira-issue-type-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents issue type screen schemes. Use it to: * get issue type screen schemes and a list of the projects that use them. * create issue type screen schemes. * update issue type screen '
  name: Jira Issue type screen schemes API
  slug: jira-issue-type-screen-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents votes cast by users on an issue. Use it to get details of votes on an issue as well as cast and withdrawal votes.
  name: Jira Issue votes API
  slug: jira-issue-votes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents users watching an issue. Use it to get details of users watching an issue as well as start and stop a user watching an issue.
  name: Jira Issue watchers API
  slug: jira-issue-watchers-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [issue worklog](#api-group-Issue-worklogs) properties, which provides for storing custom data against an issue worklog. Use it to get, create, and delete issue worklog propert
  name: Jira Issue worklog properties API
  slug: jira-issue-worklog-properties-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource is a collection of operations for [Jira expressions](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/).
  name: Jira Jira expressions API
  slug: jira-jira-expressions-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents various settings in Jira. Use it to get and update Jira settings and properties.
  name: Jira Jira settings API
  slug: jira-jira-settings-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents JQL search auto-complete details. Use it to obtain JQL search auto-complete data and suggestions for use in programmatic construction of queries or custom query builders. It a
  name: Jira JQL API
  slug: jira-jql-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents JQL function's precomputations. Precomputation is a mapping between custom function call and JQL fragment returned by this function. Use it to get and update precomputations.
  name: Jira JQL functions (apps) API
  slug: jira-jql-functions-apps-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents available labels. Use it to get available labels for the global label field.
  name: Jira Labels API
  slug: jira-labels-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents license metrics. Use it to get available metrics for Jira licences.
  name: Jira License metrics API
  slug: jira-license-metrics-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource supports the migration of some Connect modules to their equivalent Forge modules.
  name: Jira Migration of Connect modules to Forge API
  slug: jira-migration-of-connect-modules-to-forge-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents information about the current user, such as basic details, group membership, application roles, preferences, and locale. Use it to get, create, update, and delete (restore def
  name: Jira Myself API
  slug: jira-myself-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: APIs related to integrating Incident and Post-Incident Review (PIR) data with Jira Software. These APIs are available to Atlassian Connect apps. To use these APIs you must have the `jiraOperationsInfo
  name: Jira Operations API
  slug: jira-operations-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Organization API from Jira — 6 operation(s) for organization.
  name: Jira Organization API
  slug: jira-organization-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents permission schemes. Use it to get, create, update, and delete permission schemes as well as get, create, update, and delete details of the permissions granted in those schemes
  name: Jira Permission schemes API
  slug: jira-permission-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents permissions. Use it to obtain details of all permissions and determine whether the user has certain permissions.
  name: Jira Permissions API
  slug: jira-permissions-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents plans. Use it to get, create, duplicate, update, trash and archive plans.
  name: Jira Plans API
  slug: jira-plans-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue priority schemes. Use it to get priority schemes and related information, and to create, update and delete priority schemes.
  name: Jira Priority schemes API
  slug: jira-priority-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents avatars associated with a project. Use it to get, load, set, and remove project avatars.
  name: Jira Project avatars API
  slug: jira-project-avatars-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents project categories. Use it to create, update, and delete project categories as well as obtain a list of all project categories and details of individual categories. For more i
  name: Jira Project categories API
  slug: jira-project-categories-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents classification levels used in a project. Use it to view and manage classification levels in your projects.
  name: Jira Project classification levels API
  slug: jira-project-classification-levels-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents project components. Use it to get, create, update, and delete project components. Also get components for project and get a count of issues by component.
  name: Jira Project components API
  slug: jira-project-components-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the email address used to send a project's notifications. Use it to get and set the [project's sender email address](https://confluence.atlassian.com/x/dolKLg).
  name: Jira Project email API
  slug: jira-project-email-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents project features. Use it to get the list of features for a project and modify the state of a feature. The project feature endpoint is available only for Jira Software, both fo
  name: Jira Project features API
  slug: jira-project-features-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource provides validation for project keys and names.
  name: Jira Project key and name validation API
  slug: jira-project-key-and-name-validation-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents permission schemes for a project. Use this resource to: * get details of a project''s issue security levels available to the calling user. * get the permission scheme associate'
  name: Jira Project permission schemes API
  slug: jira-project-permission-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [project](#api-group-Projects) properties, which provides for storing custom data against a project. Use it to get, create, and delete project properties as well as get a list
  name: Jira Project properties API
  slug: jira-project-properties-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the users assigned to [project roles](#api-group-Issue-comments). Use it to get, add, and remove default users from project roles. Also use it to add and remove users from a p
  name: Jira Project role actors API
  slug: jira-project-role-actors-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the roles that users can play in projects. Use this resource to get, create, update, and delete project roles.
  name: Jira Project roles API
  slug: jira-project-roles-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents project templates. Use it to create a new project from a custom template.
  name: Jira Project templates API
  slug: jira-project-templates-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents project types. Use it to obtain a list of all project types, a list of project types accessible to the calling user, and details of a project type.
  name: Jira Project types API
  slug: jira-project-types-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents project versions. Use it to get, get lists of, create, update, move, merge, and delete project versions. This resource also provides counts of issues by version.
  name: Jira Project versions API
  slug: jira-project-versions-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: APIs related to integrating remote link data with Jira Software. These APIs are available to Atlassian Connect apps. To use these APIs you must have the `jiraRemoteLinkInfoProvider` module in your Con
  name: Jira Remote Links API
  slug: jira-remote-links-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Request API from Jira — 18 operation(s) for request.
  name: Jira Request API
  slug: jira-request-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Rest API from Jira — 4 operation(s) for rest.
  name: Jira Rest API
  slug: jira-rest-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents screen schemes in classic projects. Use it to get, create, update, and delete screen schemes.
  name: Jira Screen schemes API
  slug: jira-screen-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the screen tab fields used to record issue details. Use it to get, add, move, and remove fields from screen tabs.
  name: Jira Screen tab fields API
  slug: jira-screen-tab-fields-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the screen tabs used to record issue details. Use it to get, create, update, move, and delete screen tabs.
  name: Jira Screen tabs API
  slug: jira-screen-tabs-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents the screens used to record issue details. Use it to: * get details of all screens. * get details of all the fields available for use on screens. * create screens. * delete scr'
  name: Jira Screens API
  slug: jira-screens-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: Send security information to Jira Software and enable your teams to turn unplanned vulnerabilities into planned and tracked work. Security is everyone's responsibility, and the security feature in Jir
  name: Jira Security Information API
  slug: jira-security-information-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource provides information about the Jira instance.
  name: Jira Server info API
  slug: jira-server-info-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents a service registry. Use it to retrieve attributes related to a [service registry](https://support.atlassian.com/jira-service-management-cloud/docs/what-is-services/) in JSM.
  name: Jira Service Registry API
  slug: jira-service-registry-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Servicedesk API from Jira — 16 operation(s) for servicedesk.
  name: Jira Servicedesk API
  slug: jira-servicedesk-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: Apis related to sprints
  name: Jira Sprint API
  slug: jira-sprint-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents statuses. Use it to search, get, create, delete, and change statuses.
  name: Jira Status API
  slug: jira-status-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents a [long-running asynchronous tasks](#async-operations). Use it to obtain details about the progress of a long-running task or cancel a long-running task.
  name: Jira Tasks API
  slug: jira-tasks-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents planning settings for plan-only and Atlassian teams in a plan. Use it to get, create, update and delete planning settings.
  name: Jira Teams in plan API
  slug: jira-teams-in-plan-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents time tracking and time tracking providers. Use it to get and set the time tracking provider, get and set the time tracking options, and disable time tracking.
  name: Jira Time tracking API
  slug: jira-time-tracking-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'UI modifications is a feature available for **Forge apps only**. It enables Forge apps to control how selected Jira and Jira Service Management fields behave on the following views: * Jira global issu'
  name: Jira UI modifications (apps) API
  slug: jira-ui-modifications-apps-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [user](#api-group-Users) properties and provides for storing custom data against a user. Use it to get, create, and delete user properties as well as get a list of property ke
  name: Jira User properties API
  slug: jira-user-properties-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents various ways to search for and find users. Use it to obtain list of users including users assignable to projects and issues, users with permissions, user lists for pickup fiel
  name: Jira User search API
  slug: jira-user-search-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents webhooks. Webhooks are calls sent to a URL when an event occurs in Jira for issues specified by a JQL query. Only Connect and OAuth 2.0 apps can register and manage webhooks. '
  name: Jira Webhooks API
  slug: jira-webhooks-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents draft workflow schemes. Use it to manage drafts of workflow schemes. A workflow scheme maps issue types to workflows. A workflow scheme can be associated with one or more proj
  name: Jira Workflow scheme drafts API
  slug: jira-workflow-scheme-drafts-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the associations between workflow schemes and projects. For more information, see [Managing your workflows](https://confluence.atlassian.com/x/q4hKLg).
  name: Jira Workflow scheme project associations API
  slug: jira-workflow-scheme-project-associations-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents workflow schemes. Use it to manage workflow schemes and the workflow scheme's workflows and issue types. A workflow scheme maps issue types to workflows. A workflow scheme can
  name: Jira Workflow schemes API
  slug: jira-workflow-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents status categories. Use it to obtain a list of all status categories and the details of a category. Status categories provided a mechanism for categorizing [statuses](#api-grou
  name: Jira Workflow status categories API
  slug: jira-workflow-status-categories-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue workflow statuses. Use it to obtain a list of all statuses associated with workflows and the details of a status.
  name: Jira Workflow statuses API
  slug: jira-workflow-statuses-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents workflow transition rules. Workflow transition rules define a Connect or a Forge app routine, such as a [workflow post functions](https://developer.atlassian.com/cloud/jira/pl
  name: Jira Workflow transition rules API
  slug: jira-workflow-transition-rules-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents workflows. Use it to: * Get workflows * Create workflows * Update workflows * Delete inactive workflows * Get workflow capabilities'
  name: Jira Workflows API
  slug: jira-workflows-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Knowledge Base API from Jira — 1 operation(s) for knowledge base.
  name: Jira Knowledge Base API
  slug: jira-knowledge-base-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Request Type API from Jira — 1 operation(s) for request type.
  name: Jira Request Type API
  slug: jira-request-type-api
arazzos:
- description: Read an issue, page through its comment thread oldest-first, then add a reply.
  name: Jira Read an Issue Comment Thread and Reply
  slug: jira-comment-thread-reply-workflow
- description: Resolve project metadata, create an issue, then read back the stored issue.
  name: Jira Create an Issue and Read It Back
  slug: jira-create-issue-read-back-workflow
- description: Search for an existing issue by JQL and either comment on the duplicate or create a new issue.
  name: Jira Deduplicate Issue Intake
  slug: jira-deduplicate-issue-intake-workflow
- description: Read an issue, apply a field edit and label operations, then re-read to verify.
  name: Jira Edit an Issue and Verify the Change
  slug: jira-edit-issue-verify-workflow
- description: Cache the projects, issue types, and priorities an issue-creation surface needs.
  name: Jira Bootstrap Issue Creation Metadata
  slug: jira-issue-metadata-bootstrap-workflow
- description: Run a JQL search via GET, then drill into the first matching issue and its comments.
  name: Jira Run a JQL Report and Drill Into a Result
  slug: jira-jql-issue-report-workflow
- description: Search projects by name, read the matched project, and map its per-issue-type statuses.
  name: Jira Discover a Project and Its Workflow Statuses
  slug: jira-project-discovery-workflow
- description: Read an issue and its sub-tasks first, then delete it with an explicit sub-task decision.
  name: Jira Safely Delete an Issue
  slug: jira-safe-issue-delete-workflow
- description: Find stale issues with JQL, annotate the first match, discover its transitions, and close it.
  name: Jira Sweep a Stale Issue Through a Transition
  slug: jira-stale-issue-sweep-workflow
- description: Read an issue, discover its legal transitions, apply one, and verify the new status.
  name: Jira Transition an Issue to a New Status
  slug: jira-transition-issue-workflow
artifact_total: 339
asyncapis:
- description: Jira Cloud webhooks deliver HTTP POST payloads to a configured URL whenever specified events occur in your Jira instance. Webhooks can be registered via the Jira REST API or through the Jira administr
  name: Jira Cloud Webhooks
  slug: jira-webhooks-asyncapi
- description: ''
  name: Jira Webhooks
  slug: jira-webhooks
collections:
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments API
  slug: postman-jira-issue-comments-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issue Priorities API
  slug: postman-jira-issue-priorities-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issue Search API
  slug: postman-jira-issue-search-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issue Statuses API
  slug: postman-jira-issue-statuses-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issue Transitions API
  slug: postman-jira-issue-transitions-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issue Types API
  slug: postman-jira-issue-types-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issues API
  slug: postman-jira-issues-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Projects API
  slug: postman-jira-projects-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jira Cloud Platform REST API
  slug: open-jira-cloud-platform-rest-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments API
  slug: open-jira-issue-comments-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issue Priorities API
  slug: open-jira-issue-priorities-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issue Search API
  slug: open-jira-issue-search-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issue Statuses API
  slug: open-jira-issue-statuses-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issue Transitions API
  slug: open-jira-issue-transitions-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issue Types API
  slug: open-jira-issue-types-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issues API
  slug: open-jira-issues-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Projects API
  slug: open-jira-projects-api
- collection_type: open
  name: Atlassian Jira Cloud Platform REST API v3
  slug: open-jira
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/overlays/jira-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/jira-platform-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/overlays/jira-software-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/jira-software-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/overlays/jira-service-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/jira-service-management-overlay.yaml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/plans/jira-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jira-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/finops/jira-finops.yml
  title: ''
  type: FinOps
  url: finops/jira-finops.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atlassian
- group: docs
  title: ''
  type: Documentation
  url: https://developer.atlassian.com/cloud/jira/platform/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atlassian.com/software/jira/pricing
- group: operate
  title: ''
  type: Community
  url: https://community.developer.atlassian.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atlassian
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/mcp/jira-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/jira-tool-crosswalk.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.atlassian.com/trust/compliance
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.atlassian.com/platform/marketplace/atlassian-rest-api-policy/
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/sandbox/jira-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/jira-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/asyncapi/jira-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/jira-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.atlassian.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.atlassian.com/roadmap/cloud
- group: start
  title: ''
  type: SignUp
  url: https://www.atlassian.com/try/cloud/signup?bundle=jira-software
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.atlassian.com/
- group: auth
  title: ''
  type: Trust
  url: https://www.atlassian.com/trust
- group: auth
  title: ''
  type: BugBounty
  url: https://bugcrowd.com/atlassian
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/collections/jira.postman_collection.json
  title: ''
  type: PostmanCollection
  url: collections/jira.postman_collection.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/collections/jira.opencollection.json
  title: ''
  type: OpenCollection
  url: collections/jira.opencollection.json
- group: company
  title: ''
  type: Website
  url: https://www.atlassian.com/software/jira
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/jira/overview
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/packages/jira-packages.yml
  title: ''
  type: Packages
  url: packages/jira-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/well-known/jira-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jira-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/well-known/jira-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jira-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/mcp/jira-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/jira-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/llms/jira-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jira-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/overlays/jira-cloud-platform-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/jira-cloud-platform-rest-api-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/conformance/jira-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jira-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/errors/jira-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jira-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/lifecycle/jira-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/jira-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/conventions/jira-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jira-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/changelog/jira-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/jira-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/cli/jira-cli.yml
  title: ''
  type: CLI
  url: cli/jira-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/components/jira-components.yml
  title: ''
  type: Components
  url: components/jira-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/data-model/jira-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jira-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/agentic-access/jira-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jira-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/security/jira-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/jira-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/security/jira-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jira-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/security/jira-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jira-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/authentication/jira-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jira-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/scopes/jira-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/jira-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/arazzo/jira-comment-thread-reply-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-comment-thread-reply-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/arazzo/jira-create-issue-read-back-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-create-issue-read-back-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/arazzo/jira-deduplicate-issue-intake-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-deduplicate-issue-intake-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/arazzo/jira-edit-issue-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-edit-issue-verify-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/arazzo/jira-issue-metadata-bootstrap-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-issue-metadata-bootstrap-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/arazzo/jira-jql-issue-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-jql-issue-report-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/arazzo/jira-project-discovery-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-project-discovery-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/arazzo/jira-safe-issue-delete-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-safe-issue-delete-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/arazzo/jira-stale-issue-sweep-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-stale-issue-sweep-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/arazzo/jira-transition-issue-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-transition-issue-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.atlassian.com/cloud/jira/platform/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.atlassian.com/cloud/jira/platform/getting-started/
- group: build
  title: ''
  type: SDKs
  url: https://developer.atlassian.com/cloud/jira/platform/libraries/
- group: auth
  title: OAuth 2.0
  type: Authentication
  url: https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/
- group: operate
  title: ''
  type: Support
  url: https://support.atlassian.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.atlassian.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlassian.com/legal/cloud-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlassian.com/legal/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.atlassian.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://www.atlassian.com/blog/developer
- group: other
  title: ''
  type: Marketplace
  url: https://developer.atlassian.com/platform/marketplace/getting-started/
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.atlassian.com/cloud/jira/platform/rate-limiting/
- group: auth
  title: ''
  type: Security
  url: https://developer.atlassian.com/cloud/jira/platform/security-overview/
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/json-schema/jira-issue-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/jira-issue-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/json-schema/jira-project-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/jira-project-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/json-ld/jira-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jira-context.jsonld
created: '2024'
description: APIs for Atlassian Jira project management and issue tracking platform.
examples:
- key_count: 3
  name: Jira Cloud Platform Rest Atlassian Document Format Example
  slug: jira-cloud-platform-rest-atlassian-document-format-example
- key_count: 8
  name: Jira Cloud Platform Rest Attachment Example
  slug: jira-cloud-platform-rest-attachment-example
- key_count: 4
  name: Jira Cloud Platform Rest Avatar Urls Example
  slug: jira-cloud-platform-rest-avatar-urls-example
- key_count: 3
  name: Jira Cloud Platform Rest Change History Example
  slug: jira-cloud-platform-rest-change-history-example
- key_count: 7
  name: Jira Cloud Platform Rest Change Item Example
  slug: jira-cloud-platform-rest-change-item-example
- key_count: 4
  name: Jira Cloud Platform Rest Changelog Example
  slug: jira-cloud-platform-rest-changelog-example
- key_count: 6
  name: Jira Cloud Platform Rest Comment Example
  slug: jira-cloud-platform-rest-comment-example
- key_count: 7
  name: Jira Cloud Platform Rest Component Example
  slug: jira-cloud-platform-rest-component-example
- key_count: 4
  name: Jira Cloud Platform Rest Created Issue Example
  slug: jira-cloud-platform-rest-created-issue-example
- key_count: 2
  name: Jira Cloud Platform Rest Entity Property Example
  slug: jira-cloud-platform-rest-entity-property-example
- key_count: 3
  name: Jira Cloud Platform Rest Error Collection Example
  slug: jira-cloud-platform-rest-error-collection-example
- key_count: 5
  name: Jira Cloud Platform Rest Field Update Operation Example
  slug: jira-cloud-platform-rest-field-update-operation-example
- key_count: 8
  name: Jira Cloud Platform Rest Issue Bean Example
  slug: jira-cloud-platform-rest-issue-bean-example
- key_count: 4
  name: Jira Cloud Platform Rest Issue Create Request Example
  slug: jira-cloud-platform-rest-issue-create-request-example
- key_count: 17
  name: Jira Cloud Platform Rest Issue Fields Example
  slug: jira-cloud-platform-rest-issue-fields-example
- key_count: 2
  name: Jira Cloud Platform Rest Issue Link Example
  slug: jira-cloud-platform-rest-issue-link-example
- key_count: 5
  name: Jira Cloud Platform Rest Issue Link Type Example
  slug: jira-cloud-platform-rest-issue-link-type-example
- key_count: 4
  name: Jira Cloud Platform Rest Issue Ref Example
  slug: jira-cloud-platform-rest-issue-ref-example
- key_count: 3
  name: Jira Cloud Platform Rest Issue Transition Request Example
  slug: jira-cloud-platform-rest-issue-transition-request-example
- key_count: 8
  name: Jira Cloud Platform Rest Issue Type Details Example
  slug: jira-cloud-platform-rest-issue-type-details-example
- key_count: 5
  name: Jira Cloud Platform Rest Issue Type With Status Example
  slug: jira-cloud-platform-rest-issue-type-with-status-example
- key_count: 4
  name: Jira Cloud Platform Rest Issue Update Request Example
  slug: jira-cloud-platform-rest-issue-update-request-example
- key_count: 7
  name: Jira Cloud Platform Rest Page Bean Project Example
  slug: jira-cloud-platform-rest-page-bean-project-example
- key_count: 4
  name: Jira Cloud Platform Rest Page Of Comments Example
  slug: jira-cloud-platform-rest-page-of-comments-example
- key_count: 4
  name: Jira Cloud Platform Rest Page Of Worklogs Example
  slug: jira-cloud-platform-rest-page-of-worklogs-example
- key_count: 6
  name: Jira Cloud Platform Rest Priority Example
  slug: jira-cloud-platform-rest-priority-example
- key_count: 4
  name: Jira Cloud Platform Rest Project Category Example
  slug: jira-cloud-platform-rest-project-category-example
- key_count: 17
  name: Jira Cloud Platform Rest Project Example
  slug: jira-cloud-platform-rest-project-example
- key_count: 5
  name: Jira Cloud Platform Rest Project Ref Example
  slug: jira-cloud-platform-rest-project-ref-example
- key_count: 4
  name: Jira Cloud Platform Rest Resolution Example
  slug: jira-cloud-platform-rest-resolution-example
- key_count: 1
  name: Jira Cloud Platform Rest Scope Example
  slug: jira-cloud-platform-rest-scope-example
- key_count: 8
  name: Jira Cloud Platform Rest Search Request Example
  slug: jira-cloud-platform-rest-search-request-example
- key_count: 8
  name: Jira Cloud Platform Rest Search Results Example
  slug: jira-cloud-platform-rest-search-results-example
- key_count: 5
  name: Jira Cloud Platform Rest Status Category Example
  slug: jira-cloud-platform-rest-status-category-example
- key_count: 5
  name: Jira Cloud Platform Rest Status Details Example
  slug: jira-cloud-platform-rest-status-details-example
- key_count: 7
  name: Jira Cloud Platform Rest Transition Example
  slug: jira-cloud-platform-rest-transition-example
- key_count: 1
  name: Jira Cloud Platform Rest Transition Ref Example
  slug: jira-cloud-platform-rest-transition-ref-example
- key_count: 2
  name: Jira Cloud Platform Rest Transitions Example
  slug: jira-cloud-platform-rest-transitions-example
- key_count: 7
  name: Jira Cloud Platform Rest User Details Example
  slug: jira-cloud-platform-rest-user-details-example
- key_count: 10
  name: Jira Cloud Platform Rest Version Example
  slug: jira-cloud-platform-rest-version-example
- key_count: 3
  name: Jira Cloud Platform Rest Visibility Example
  slug: jira-cloud-platform-rest-visibility-example
- key_count: 3
  name: Jira Cloud Platform Rest Votes Example
  slug: jira-cloud-platform-rest-votes-example
- key_count: 3
  name: Jira Cloud Platform Rest Watches Example
  slug: jira-cloud-platform-rest-watches-example
- key_count: 7
  name: Jira Cloud Platform Rest Worklog Example
  slug: jira-cloud-platform-rest-worklog-example
features:
- 'Free: up to 10 users'
- 'Standard: $7.91-$9.05/user/mo (volume tiered)'
- 'Premium: $14.54-$18.30/user/mo with Advanced Roadmaps'
- 'Enterprise custom: Atlassian Intelligence, 99.95% uptime, data residency'
- 'Volume discount: rates drop above 100 users (max 50K)'
- REST API v3 at api.atlassian.com
- GraphQL API for some products
- Token-bucket rate limit ~10 req/sec/app/user
- Bulk operations max 100 items/request
- Webhooks v3 for issue/project events
- OAuth 2.0 (3LO) and API tokens
- Atlassian Connect framework for marketplace apps
- Forge for serverless app development
- JQL (Jira Query Language) for advanced search
- Atlassian Intelligence AI assistant (Enterprise)
- Cross-product Analytics + Atlas integrations
finops:
- name: Jira Finops
  service_category: Project Management
  slug: jira-finops
graphqls:
- description: ''
  name: Jira GraphQL API
  slug: jira-graphql
image: https://www.atlassian.com/dam/jcr:e33efd9e-e0b8-4d61-a24d-68a48ef9bbe4/jira-icon-blue.svg
integrations:
- description: Link Jira issues to Confluence pages for seamless knowledge management and documentation alongside project tracking.
  name: Confluence
- description: Connect code repositories to Jira issues for automated status updates, smart commits, and development tracking.
  name: Bitbucket
- description: Link GitHub pull requests, branches, and commits to Jira issues for end-to-end development visibility.
  name: GitHub
- description: Create and manage Jira issues from Slack channels with bi-directional notifications and status updates.
  name: Slack
- description: Receive Jira notifications and manage issues directly from Microsoft Teams conversations.
  name: Microsoft Teams
json_schemas:
- name: AtlassianDocumentFormat
  property_count: 3
  slug: jira-cloud-platform-rest-atlassian-document-format
- name: Attachment
  property_count: 8
  slug: jira-cloud-platform-rest-attachment
- name: AvatarUrls
  property_count: 4
  slug: jira-cloud-platform-rest-avatar-urls
- name: ChangeHistory
  property_count: 3
  slug: jira-cloud-platform-rest-change-history
- name: ChangeItem
  property_count: 7
  slug: jira-cloud-platform-rest-change-item
- name: Changelog
  property_count: 4
  slug: jira-cloud-platform-rest-changelog
- name: Comment
  property_count: 6
  slug: jira-cloud-platform-rest-comment
- name: Component
  property_count: 7
  slug: jira-cloud-platform-rest-component
- name: CreatedIssue
  property_count: 4
  slug: jira-cloud-platform-rest-created-issue
- name: EntityProperty
  property_count: 2
  slug: jira-cloud-platform-rest-entity-property
- name: ErrorCollection
  property_count: 3
  slug: jira-cloud-platform-rest-error-collection
- name: FieldUpdateOperation
  property_count: 5
  slug: jira-cloud-platform-rest-field-update-operation
- name: IssueBean
  property_count: 8
  slug: jira-cloud-platform-rest-issue-bean
- name: IssueCreateRequest
  property_count: 4
  slug: jira-cloud-platform-rest-issue-create-request
- name: IssueFields
  property_count: 17
  slug: jira-cloud-platform-rest-issue-fields
- name: IssueLink
  property_count: 2
  slug: jira-cloud-platform-rest-issue-link
- name: IssueLinkType
  property_count: 5
  slug: jira-cloud-platform-rest-issue-link-type
- name: IssueRef
  property_count: 4
  slug: jira-cloud-platform-rest-issue-ref
- name: IssueTransitionRequest
  property_count: 3
  slug: jira-cloud-platform-rest-issue-transition-request
- name: IssueTypeDetails
  property_count: 8
  slug: jira-cloud-platform-rest-issue-type-details
- name: IssueTypeWithStatus
  property_count: 5
  slug: jira-cloud-platform-rest-issue-type-with-status
- name: IssueUpdateRequest
  property_count: 4
  slug: jira-cloud-platform-rest-issue-update-request
- name: PageBeanProject
  property_count: 7
  slug: jira-cloud-platform-rest-page-bean-project
- name: PageOfComments
  property_count: 4
  slug: jira-cloud-platform-rest-page-of-comments
- name: PageOfWorklogs
  property_count: 4
  slug: jira-cloud-platform-rest-page-of-worklogs
- name: Priority
  property_count: 6
  slug: jira-cloud-platform-rest-priority
- name: ProjectCategory
  property_count: 4
  slug: jira-cloud-platform-rest-project-category
- name: ProjectRef
  property_count: 5
  slug: jira-cloud-platform-rest-project-ref
- name: Project
  property_count: 17
  slug: jira-cloud-platform-rest-project
- name: Resolution
  property_count: 4
  slug: jira-cloud-platform-rest-resolution
- name: Scope
  property_count: 1
  slug: jira-cloud-platform-rest-scope
- name: SearchRequest
  property_count: 8
  slug: jira-cloud-platform-rest-search-request
- name: SearchResults
  property_count: 8
  slug: jira-cloud-platform-rest-search-results
- name: StatusCategory
  property_count: 5
  slug: jira-cloud-platform-rest-status-category
- name: StatusDetails
  property_count: 5
  slug: jira-cloud-platform-rest-status-details
- name: TransitionRef
  property_count: 1
  slug: jira-cloud-platform-rest-transition-ref
- name: Transition
  property_count: 7
  slug: jira-cloud-platform-rest-transition
- name: Transitions
  property_count: 2
  slug: jira-cloud-platform-rest-transitions
- name: UserDetails
  property_count: 7
  slug: jira-cloud-platform-rest-user-details
- name: Version
  property_count: 10
  slug: jira-cloud-platform-rest-version
- name: Visibility
  property_count: 3
  slug: jira-cloud-platform-rest-visibility
- name: Votes
  property_count: 3
  slug: jira-cloud-platform-rest-votes
- name: Watches
  property_count: 3
  slug: jira-cloud-platform-rest-watches
- name: Worklog
  property_count: 7
  slug: jira-cloud-platform-rest-worklog
- name: Jira Issue
  property_count: 10
  slug: jira-issue
- name: Jira Project
  property_count: 22
  slug: jira-project
json_structures:
- name: Jira Cloud Platform Rest Atlassian Document Format Structure
  property_count: 3
  slug: jira-cloud-platform-rest-atlassian-document-format-structure
- name: Jira Cloud Platform Rest Attachment Structure
  property_count: 8
  slug: jira-cloud-platform-rest-attachment-structure
- name: Jira Cloud Platform Rest Avatar Urls Structure
  property_count: 4
  slug: jira-cloud-platform-rest-avatar-urls-structure
- name: Jira Cloud Platform Rest Change History Structure
  property_count: 3
  slug: jira-cloud-platform-rest-change-history-structure
- name: Jira Cloud Platform Rest Change Item Structure
  property_count: 7
  slug: jira-cloud-platform-rest-change-item-structure
- name: Jira Cloud Platform Rest Changelog Structure
  property_count: 4
  slug: jira-cloud-platform-rest-changelog-structure
- name: Jira Cloud Platform Rest Comment Structure
  property_count: 6
  slug: jira-cloud-platform-rest-comment-structure
- name: Jira Cloud Platform Rest Component Structure
  property_count: 7
  slug: jira-cloud-platform-rest-component-structure
- name: Jira Cloud Platform Rest Created Issue Structure
  property_count: 4
  slug: jira-cloud-platform-rest-created-issue-structure
- name: Jira Cloud Platform Rest Entity Property Structure
  property_count: 2
  slug: jira-cloud-platform-rest-entity-property-structure
- name: Jira Cloud Platform Rest Error Collection Structure
  property_count: 3
  slug: jira-cloud-platform-rest-error-collection-structure
- name: Jira Cloud Platform Rest Field Update Operation Structure
  property_count: 5
  slug: jira-cloud-platform-rest-field-update-operation-structure
- name: Jira Cloud Platform Rest Issue Bean Structure
  property_count: 8
  slug: jira-cloud-platform-rest-issue-bean-structure
- name: Jira Cloud Platform Rest Issue Create Request Structure
  property_count: 4
  slug: jira-cloud-platform-rest-issue-create-request-structure
- name: Jira Cloud Platform Rest Issue Fields Structure
  property_count: 17
  slug: jira-cloud-platform-rest-issue-fields-structure
- name: Jira Cloud Platform Rest Issue Link Structure
  property_count: 2
  slug: jira-cloud-platform-rest-issue-link-structure
- name: Jira Cloud Platform Rest Issue Link Type Structure
  property_count: 5
  slug: jira-cloud-platform-rest-issue-link-type-structure
- name: Jira Cloud Platform Rest Issue Ref Structure
  property_count: 4
  slug: jira-cloud-platform-rest-issue-ref-structure
- name: Jira Cloud Platform Rest Issue Transition Request Structure
  property_count: 3
  slug: jira-cloud-platform-rest-issue-transition-request-structure
- name: Jira Cloud Platform Rest Issue Type Details Structure
  property_count: 8
  slug: jira-cloud-platform-rest-issue-type-details-structure
- name: Jira Cloud Platform Rest Issue Type With Status Structure
  property_count: 5
  slug: jira-cloud-platform-rest-issue-type-with-status-structure
- name: Jira Cloud Platform Rest Issue Update Request Structure
  property_count: 4
  slug: jira-cloud-platform-rest-issue-update-request-structure
- name: Jira Cloud Platform Rest Page Bean Project Structure
  property_count: 7
  slug: jira-cloud-platform-rest-page-bean-project-structure
- name: Jira Cloud Platform Rest Page Of Comments Structure
  property_count: 4
  slug: jira-cloud-platform-rest-page-of-comments-structure
- name: Jira Cloud Platform Rest Page Of Worklogs Structure
  property_count: 4
  slug: jira-cloud-platform-rest-page-of-worklogs-structure
- name: Jira Cloud Platform Rest Priority Structure
  property_count: 6
  slug: jira-cloud-platform-rest-priority-structure
- name: Jira Cloud Platform Rest Project Category Structure
  property_count: 4
  slug: jira-cloud-platform-rest-project-category-structure
- name: Jira Cloud Platform Rest Project Ref Structure
  property_count: 5
  slug: jira-cloud-platform-rest-project-ref-structure
- name: Jira Cloud Platform Rest Project Structure
  property_count: 17
  slug: jira-cloud-platform-rest-project-structure
- name: Jira Cloud Platform Rest Resolution Structure
  property_count: 4
  slug: jira-cloud-platform-rest-resolution-structure
- name: Jira Cloud Platform Rest Scope Structure
  property_count: 1
  slug: jira-cloud-platform-rest-scope-structure
- name: Jira Cloud Platform Rest Search Request Structure
  property_count: 8
  slug: jira-cloud-platform-rest-search-request-structure
- name: Jira Cloud Platform Rest Search Results Structure
  property_count: 8
  slug: jira-cloud-platform-rest-search-results-structure
- name: Jira Cloud Platform Rest Status Category Structure
  property_count: 5
  slug: jira-cloud-platform-rest-status-category-structure
- name: Jira Cloud Platform Rest Status Details Structure
  property_count: 5
  slug: jira-cloud-platform-rest-status-details-structure
- name: Jira Cloud Platform Rest Transition Ref Structure
  property_count: 1
  slug: jira-cloud-platform-rest-transition-ref-structure
- name: Jira Cloud Platform Rest Transition Structure
  property_count: 7
  slug: jira-cloud-platform-rest-transition-structure
- name: Jira Cloud Platform Rest Transitions Structure
  property_count: 2
  slug: jira-cloud-platform-rest-transitions-structure
- name: Jira Cloud Platform Rest User Details Structure
  property_count: 7
  slug: jira-cloud-platform-rest-user-details-structure
- name: Jira Cloud Platform Rest Version Structure
  property_count: 10
  slug: jira-cloud-platform-rest-version-structure
- name: Jira Cloud Platform Rest Visibility Structure
  property_count: 3
  slug: jira-cloud-platform-rest-visibility-structure
- name: Jira Cloud Platform Rest Votes Structure
  property_count: 3
  slug: jira-cloud-platform-rest-votes-structure
- name: Jira Cloud Platform Rest Watches Structure
  property_count: 3
  slug: jira-cloud-platform-rest-watches-structure
- name: Jira Cloud Platform Rest Worklog Structure
  property_count: 7
  slug: jira-cloud-platform-rest-worklog-structure
jsonld:
- class_count: 0
  name: Jira Cloud Platform Rest Context
  property_count: 0
  slug: jira-cloud-platform-rest-context
- class_count: 0
  name: Jira Context
  property_count: 15
  slug: jira-context
layout: provider
mcp_servers:
- description: ''
  name: Atlassian Rovo MCP Server
  slug: atlassian-rovo-mcp-server
modified: '2026-06-20'
name: Jira
nav: Providers
network: true
overview: 'Jira publishes 127 APIs on the [APIs.io](https://apis.io/) network, including Issue Comments API, Issue Priorities API, Issue Search API, and 124 more. Tagged areas include Agile, Issue Tracking, ITSM, Project Management, and Service Management.


  The Jira catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Jira''s developer surface includes documentation, pricing, sandbox, API reference, signup flow, changelog, CLI, and 66 more developer resources.'
plans:
- name: Jira Plans Pricing
  plan_count: 4
  slug: jira-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Jira Rate Limits
  slug: jira-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Jira API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: jira-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Jira API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: jira-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Jira API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 7
  slug: jira-spectral-rules
scopes:
- name: Jira Scopes
  scope_count: 5
  slug: jira-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: exemplar
  composite: 73.5
  coverage:
    artifact_dirs: 37
    catalog_earned: 53.5
    catalog_earned_first_party: 0.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 73.7
    developer_ergonomics: 81.5
    discoverability: 74.1
    operational_transparency: 73.7
  previous_composite: 72.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 6.6
      derived: 0
      marker_coverage: 0.0
      total: 122
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/screenshots/jira-2026-06-20T183734.png
security:
- kind: authentication
  name: Jira Authentication
  slug: jira-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Jira Domain Security
  slug: jira-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Jira Vulnerability Disclosure
  slug: jira-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Jira Trust Center
  slug: jira-trust-center
  summary_line: FedRAMP
slug: jira
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
- Jira
use_cases:
- description: Automate issue creation, assignment, and transitions based on external events from CI/CD pipelines, monitoring tools, or customer feedback systems.
  name: Issue Tracking Automation
- description: Programmatically manage sprints, backlogs, and board configurations for automated agile workflow orchestration.
  name: Sprint Management
- description: Integrate customer support channels with Jira Service Management for automated ticket creation and SLA tracking.
  name: Service Desk Integration
- description: Automate incident response workflows with on-call scheduling, alert routing, and escalation management.
  name: Incident Management
- description: Connect portfolio planning tools with Jira Align for cross-team dependency tracking and program-level reporting.
  name: Enterprise Agile Planning
website: https://www.atlassian.com/software/jira
---
