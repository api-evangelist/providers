---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 115
  human_in_the_loop: 0
  name: Openproject Agentic Access
  operation_count: 275
  slug: openproject-agentic-access
  summary_line: 275 operations · 115 acting
api_count: 1
apis:
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: An action is a change one can trigger within the OpenProject instance. This could be creating a work package, exporting work packages or updating a user. An action can also be something where the user
  name: OpenProject Actions & Capabilities API
  slug: openproject-actions-capabilities-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: '## Local Properties | Property | Description | Type | Constraints | Supported operations | | :---------: | ------------- | ---- | ----------- | -------------------- | | id | Activity id | Integer | x '
  name: OpenProject Activities API
  slug: openproject-activities-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'Attachments are files that were uploaded to OpenProject. Each attachment belongs to a single container (e.g. a work package or a board message). ## Actions | Link | Description | Condition | |:-------'
  name: OpenProject Attachments API
  slug: openproject-attachments-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: '*Note: Budgets are currently only implemented as a stub. Further properties of budgets might be added at a future date, however they will require the view budget permission to be displayed.* ## Linked'
  name: OpenProject Budgets API
  slug: openproject-budgets-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'The categories endpoints return collections or single entities of type `Category`. The following tables list the different properties of `Category` entities. ## Linked Properties | Link | Description '
  name: OpenProject Categories API
  slug: openproject-categories-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'Whenever a client calls a resource that can return more than one element, it will receive a collection of elements. However as collections can become quite large, the API will **not** simply return a '
  name: OpenProject Collections API
  slug: openproject-collections-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: The configuration endpoint allows to read certain configuration parameters of the OpenProject instance. Note that there is no 1:1 relationship between this endpoint and the settings an administrator h
  name: OpenProject Configuration API
  slug: openproject-configuration-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: Custom actions are a preconfigured set of changes that are applied to a work package. Currently, this resource is a stub. The conditions and changes defined for the custom action are not yet present i
  name: OpenProject Custom actions API
  slug: openproject-custom-actions-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: The Custom Field Items API from OpenProject — 2 operation(s) for custom field items.
  name: OpenProject Custom Field Items API
  slug: openproject-custom-field-items-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: The Custom Fields API from OpenProject — 1 operation(s) for custom fields.
  name: OpenProject Custom Fields API
  slug: openproject-custom-fields-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'The custom options endpoints return collections or single entities of type `CustomOption`. The following tables list the different properties of `CustomOption` entities. ## Linked Properties | Link | '
  name: OpenProject Custom Options API
  slug: openproject-custom-options-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'A document is a file containing a list of attachments. *Please note, that the endpoint is only a stub for now.* ## Actions None yet ## Linked Properties | Link | Description | Type | Constraints | Sup'
  name: OpenProject Documents API
  slug: openproject-documents-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: The EmojiReactions API from OpenProject — 2 operation(s) for emojireactions.
  name: OpenProject EmojiReactions API
  slug: openproject-emojireactions-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: The Favorites API from OpenProject — 2 operation(s) for favorites.
  name: OpenProject Favorites API
  slug: openproject-favorites-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: The File Links API from OpenProject — 14 operation(s) for file links.
  name: OpenProject File Links API
  slug: openproject-file-links-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'This API provides forms as a concept to aid in editing or creating resources. The goal of forms is to: * make writable properties of a resource discoverable * show to which values a property can be se'
  name: OpenProject Forms API
  slug: openproject-forms-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: A grid is a layout for a page or a part of the page of the OpenProject application. It defines the structure (number of rows and number of columns) as well as the contents of the page. The contents is
  name: OpenProject Grids API
  slug: openproject-grids-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: Groups are collections of users. They support assigning/unassigning multiple users to/from a project in one operation. This resource does not yet have the form and schema endpoints. But as all propert
  name: OpenProject Groups API
  slug: openproject-groups-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'The help texts endpoints return collections or single entities of type `HelpText`. The following tables list the different properties of `HelpText` entities. ## Linked Properties | Link | Description '
  name: OpenProject Help texts API
  slug: openproject-help-texts-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: The Meetings API from OpenProject — 2 operation(s) for meetings.
  name: OpenProject Meetings API
  slug: openproject-meetings-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: Users and groups can become members of a project. Such a membership will also have one or more roles assigned to it. By that, memberships control the permissions a user has within a project. There are
  name: OpenProject Memberships API
  slug: openproject-memberships-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'News are articles written by users in order to inform other users of important information. ## Actions | Link | Description | Condition | |:-------------------:|---------------------------------------'
  name: OpenProject News API
  slug: openproject-news-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: Notifications are created through notifiable actions in OpenProject. Notifications are triggered by actions carried out in the system by users, e.g. editing a work package, but can also be send out be
  name: OpenProject Notifications API
  slug: openproject-notifications-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: TBD
  name: OpenProject OAuth 2 API
  slug: openproject-oauth-2-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: Portfolios are one of the types of [workspaces](https://www.openproject.org/docs/api/endpoints/workspaces) in OpenProject structuring the information (e.g. work packages, wikis) into smaller sets. The
  name: OpenProject Portfolios API
  slug: openproject-portfolios-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'Represents a post in a board. Posts are also referred to as messages in the application. *This resource is currently a stub* ## Actions | Link | Description | Condition | |:-------------------:|------'
  name: OpenProject Posts API
  slug: openproject-posts-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: Throughout OpenProject user input for many properties can be formatted using *Markdown*. Using the appropriate rendering endpoint it is possible to render custom formatted inputs into HTML and thus re
  name: OpenProject Previewing API
  slug: openproject-previewing-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: Principals are the superclass of users, groups and placeholder users. This endpoint returns all principals within a joined collection but can be filtered to e.g. only return groups or users.
  name: OpenProject Principals API
  slug: openproject-principals-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'The priorities endpoints return collections or single entities of type `Priority`. The following tables list the different properties of `Priority` entities. ## Linked Properties | Link | Description '
  name: OpenProject Priorities API
  slug: openproject-priorities-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'Programs are one of the types of [workspaces](https://www.openproject.org/docs/api/endpoints/workspaces) in OpenProject structuring the information (e.g. work packages, wikis) into smaller sets. They '
  name: OpenProject Programs API
  slug: openproject-programs-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: Project phases separate the whole of the project's duration into smaller, distinct parts. Such a phase will then have different focus on certain aspects of project management. E.g. while the first pha
  name: OpenProject Project Phase Definitions API
  slug: openproject-project-phase-definitions-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: Project phases separate the whole of the project's duration into smaller, distinct parts where each phase has its own start and end date. Such a phase will then have different focus on certain aspects
  name: OpenProject Project Phases API
  slug: openproject-project-phases-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'Projects are one of the types of [workspaces](https://www.openproject.org/docs/api/endpoints/workspaces) in OpenProject structuring the information (e.g. work packages, wikis) into smaller sets. They '
  name: OpenProject Projects API
  slug: openproject-projects-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'A query defines how work packages can be filtered and displayed. Clients can define a query once, store it, and use it later on to load the same set of filters and display options. ## Actions | Link |'
  name: OpenProject Queries API
  slug: openproject-queries-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: A QueryColumn can be referenced by a Query to denote the work package properties the client should display for the work packages returned as query results. The columns maps to the WorkPackage by the i
  name: OpenProject Query Columns API
  slug: openproject-query-columns-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: A QueryFilterInstanceSchema is a Schema specifically for describing QueryFilterInstances. Because the behaviour of FilterInstances, with regards to the `values` property, differs from one another depe
  name: OpenProject Query Filter Instance Schema API
  slug: openproject-query-filter-instance-schema-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: A QueryFilter can be referenced by a filter instance defined for a Query to denote the filtering applied to the query's work package results. This resource is not an instance of an applicable filter b
  name: OpenProject Query Filters API
  slug: openproject-query-filters-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'A QueryOperator can be referenced by a QueryFilter to denote the operator to be applied to the filter relation. ## Actions As of now, no actions are defined. ## Linked Properties | Property | Descript'
  name: OpenProject Query Operators API
  slug: openproject-query-operators-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'A QuerySortBy can be referenced by a Query to denote the sorting applied to the query''s work package results. It consists of the columns to sort by as well as the direction (ascending/descending) ## A'
  name: OpenProject Query Sort Bys API
  slug: openproject-query-sort-bys-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: Work packages may be related to each other in different ways. ``` +--------------+ +--------------+ | | 1 1 | | | Work package +-------------+--------------+ Work package | | | from | to | | +--------
  name: OpenProject Relations API
  slug: openproject-relations-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: The Reminders API from OpenProject — 3 operation(s) for reminders.
  name: OpenProject Reminders API
  slug: openproject-reminders-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'Revisions are sets of updates to files in the context of repositories linked in OpenProject. ## Linked Properties | Link | Description | Type | Constraints | Supported operations | |:----------------:'
  name: OpenProject Revisions API
  slug: openproject-revisions-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: When principals (groups or users) are assigned to a project, they are receive roles in that project. Roles regulate access to specific resources by having permissions configured for them. Currently, t
  name: OpenProject Roles API
  slug: openproject-roles-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'The root resource contains links to available resources in the API. By following these links a client should be able to discover further resources in the API. *Note: Currently there is no list action '
  name: OpenProject Root API
  slug: openproject-root-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: The schema provides detailed information about the properties of a resource. The schema is represented by a dictionary where keys are names of resource properties and values are objects describing the
  name: OpenProject Schemas API
  slug: openproject-schemas-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'Work packages can be assigned to a sprint. This is employed in agile contexts such as Scrum or Kanban to group the work packages to be worked on within a defined time frame towards a defined goal. ## '
  name: OpenProject Sprints API
  slug: openproject-sprints-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'The statuses endpoints return collections or single entities of type `Status`. The following tables list the different properties of `Status` entities. ## Linked Properties | Link | Description | Type'
  name: OpenProject Statuses API
  slug: openproject-statuses-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: The Time Entries API from OpenProject — 6 operation(s) for time entries.
  name: OpenProject Time Entries API
  slug: openproject-time-entries-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'Time entries are classified by an activity which is one item of a set of user defined activities (e.g. Design, Specification, Development). ## Actions None ## Linked Properties | Link | Description | '
  name: OpenProject Time entry activities API
  slug: openproject-time-entry-activities-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'Work package types represented in the system. Types exist globally and are then activated for projects. ## Linked Properties | Link | Description | Type | Constraints | Supported operations | |:------'
  name: OpenProject Types API
  slug: openproject-types-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: User working times allow configuring per-user working hours and personal non-working days, in addition to the system-wide work schedule. A `UserWorkingHours` record defines how many hours a user works
  name: OpenProject User Working Times API
  slug: openproject-user-working-times-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'The user preferences endpoints return collections or single entities of type `UserPreferences`. The following tables list the different properties of `UserPreferences` entities. ## Linked Properties |'
  name: OpenProject UserPreferences API
  slug: openproject-userpreferences-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'The users endpoints return collections or single entities of type `User`. The following tables list the different properties of `User` entities. ## Actions | Link | Description | Condition | |:-------'
  name: OpenProject Users API
  slug: openproject-users-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: '`Values::Property` represents a single key - value pair. That pair typically is an excerpt of the properties of a resource. `Values::Property` itself is not an independent resource. It will always be '
  name: OpenProject Values::Property API
  slug: openproject-values-property-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: Work Packages can be assigned to a version. As such, versions serve to group Work Packages into logical units where each group comprises all the work packages that needs to be finished in order for th
  name: OpenProject Versions API
  slug: openproject-versions-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: A View is a representation of some information. That information might be a query (currently it always is). The view will store the configuration on how to display the information but not the informat
  name: OpenProject Views API
  slug: openproject-views-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'Represents an individual page in a project''s wiki. *This resource is currently a stub* ## Actions | Link | Description | Condition | |:-------------------:|--------------------------------------------'
  name: OpenProject Wiki Pages API
  slug: openproject-wiki-pages-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'The work packages endpoints return collections or single entities of type `WorkPackage`. The following tables list the different properties of `WorkPackage` entities. ## Actions | Link | Description |'
  name: OpenProject Work Packages API
  slug: openproject-work-packages-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: 'The work schedule defines if days are working days or non-working days. A day can be a non-working day if any of these two conditions are met: - the day is a recurring non-working week day: a weekend '
  name: OpenProject Work Schedule API
  slug: openproject-work-schedule-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: The WorkPackages API from OpenProject — 1 operation(s) for workpackages.
  name: OpenProject WorkPackages API
  slug: openproject-workpackages-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: The Workspace API from OpenProject — 1 operation(s) for workspace.
  name: OpenProject Workspace API
  slug: openproject-workspace-api
- baseURL: https://community.openproject.org/api/v3
  baseurl_source: declared
  description: Workspaces are containers for resources to be worked on and people with sets of permissions that work on the former. There is no actual workspace resource in OpenProject. Rather, it is the generic ter
  name: OpenProject Workspaces API
  slug: openproject-workspaces-api
artifact_total: 132
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities API
  slug: open-openproject-actions-capabilities-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Activities API
  slug: open-openproject-activities-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Attachments API
  slug: open-openproject-attachments-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Budgets API
  slug: open-openproject-budgets-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Categories API
  slug: open-openproject-categories-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Collections API
  slug: open-openproject-collections-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Configuration API
  slug: open-openproject-configuration-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Custom actions API
  slug: open-openproject-custom-actions-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Custom Field Items API
  slug: open-openproject-custom-field-items-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Custom Fields API
  slug: open-openproject-custom-fields-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Custom Options API
  slug: open-openproject-custom-options-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Documents API
  slug: open-openproject-documents-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities EmojiReactions API
  slug: open-openproject-emojireactions-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Favorites API
  slug: open-openproject-favorites-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities File Links API
  slug: open-openproject-file-links-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Forms API
  slug: open-openproject-forms-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Grids API
  slug: open-openproject-grids-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Groups API
  slug: open-openproject-groups-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Help texts API
  slug: open-openproject-help-texts-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Meetings API
  slug: open-openproject-meetings-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Memberships API
  slug: open-openproject-memberships-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities News API
  slug: open-openproject-news-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Notifications API
  slug: open-openproject-notifications-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities OAuth 2 API
  slug: open-openproject-oauth-2-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Portfolios API
  slug: open-openproject-portfolios-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Posts API
  slug: open-openproject-posts-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Principals API
  slug: open-openproject-principals-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Priorities API
  slug: open-openproject-priorities-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Programs API
  slug: open-openproject-programs-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Project Phase Definitions API
  slug: open-openproject-project-phase-definitions-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Project Phases API
  slug: open-openproject-project-phases-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Projects API
  slug: open-openproject-projects-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Queries API
  slug: open-openproject-queries-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Query Columns API
  slug: open-openproject-query-columns-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Query Filter Instance Schema API
  slug: open-openproject-query-filter-instance-schema-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Query Filters API
  slug: open-openproject-query-filters-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Query Operators API
  slug: open-openproject-query-operators-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Query Sort Bys API
  slug: open-openproject-query-sort-bys-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Relations API
  slug: open-openproject-relations-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Reminders API
  slug: open-openproject-reminders-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Revisions API
  slug: open-openproject-revisions-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Roles API
  slug: open-openproject-roles-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Root API
  slug: open-openproject-root-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Schemas API
  slug: open-openproject-schemas-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Sprints API
  slug: open-openproject-sprints-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Statuses API
  slug: open-openproject-statuses-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Time Entries API
  slug: open-openproject-time-entries-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Time entry activities API
  slug: open-openproject-time-entry-activities-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Types API
  slug: open-openproject-types-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities User Working Times API
  slug: open-openproject-user-working-times-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities UserPreferences API
  slug: open-openproject-userpreferences-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Users API
  slug: open-openproject-users-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Values::Property API
  slug: open-openproject-values-property-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Versions API
  slug: open-openproject-versions-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Views API
  slug: open-openproject-views-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Wiki Pages API
  slug: open-openproject-wiki-pages-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Work Packages API
  slug: open-openproject-work-packages-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Work Schedule API
  slug: open-openproject-work-schedule-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities WorkPackages API
  slug: open-openproject-workpackages-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Workspace API
  slug: open-openproject-workspace-api
- collection_type: open
  name: OpenProject API V3 (Stable) Actions & Capabilities Workspaces API
  slug: open-openproject-workspaces-api
- collection_type: open
  name: OpenProject API V3 (Stable)
  slug: open-openproject
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/openproject-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openproject-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/openproject-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openproject-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openproject-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openproject-gmbh
- group: company
  title: ''
  type: Website
  url: https://www.openproject.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.openproject.org/docs/
- group: other
  title: ''
  type: API
  url: https://www.openproject.org/docs/api/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/opf/openproject
- group: commercial
  title: ''
  type: Pricing
  url: https://www.openproject.org/pricing/
- group: other
  title: ''
  type: SelfHosting
  url: https://www.openproject.org/docs/installation-and-operations/
- group: start
  title: ''
  type: Login
  url: https://community.openproject.org/login
- group: operate
  title: ''
  type: Support
  url: https://www.openproject.org/docs/support/
- group: company
  title: ''
  type: Blog
  url: https://www.openproject.org/feed.xml
created: '2025-01-08'
description: OpenProject is an open source project management platform offering work package tracking, Gantt charts, agile boards, time tracking, BIM, and enterprise project portfolio management. The OpenProject APIv3 is a hypermedia (HAL+JSON) REST API that exposes work packages, projects, users, attachments, custom fields, and many other resources.
finops:
- name: Openproject Finops
  service_category: API
  slug: openproject-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openproject.png
layout: provider
modified: '2026-05-19'
name: OpenProject
nav: Providers
network: true
overview: 'OpenProject publishes 62 APIs on the [APIs.io](https://apis.io/) network, including Actions & Capabilities API, Activities API, Attachments API, and 59 more. Tagged areas include Agile, Gantt, Open-Source, Project Management, and Time Tracking.


  OpenProject''s developer surface includes authentication, documentation, GitHub presence, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Openproject Plans Pricing
  plan_count: 3
  slug: openproject-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Openproject Rate Limits
  slug: openproject-rate-limits
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 60.0
    developer_ergonomics: 23.8
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 62
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openproject/refs/heads/main/screenshots/openproject-2026-06-20T191026.png
security:
- kind: authentication
  name: Openproject Authentication
  slug: openproject-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openproject Domain Security
  slug: openproject-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Openproject Vulnerability Disclosure
  slug: openproject-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: openproject
tags:
- Agile
- Gantt
- Open-Source
- Project Management
- Time Tracking
- Work Packages
website: https://www.openproject.org
---
