---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 251
  human_in_the_loop: 11
  name: Mavenlink Agentic Access
  operation_count: 419
  slug: mavenlink-agentic-access
  summary_line: 419 operations · 251 acting · 11 human-in-the-loop
api_count: 2
apis:
- description: Remote Model Context Protocol server operated by Kantata on the Mavenlink API host. Advertised anonymously through RFC 9728 protected-resource metadata at https://api.mavenlink.com/.well-known/oauth-p
  name: Kantata OX MCP Server
  slug: kantata-ox-mcp-server
- description: Agent surface published on the Kantata developer portal. Serves an A2A agent card at /.well-known/agent-card.json (protocolVersion 0.3.0) that advertises an MCP extension, and an anonymous documentati
  name: Kantata OX Developer Documentation Agent
  slug: kantata-ox-developer-documentation-agent
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Access Groups allow you to manage product access for users. An Access Group Membership represents the connection of a user to an Access Group.
  name: Mavenlink Access Group Memberships API
  slug: mavenlink-access-group-memberships-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Account Colors are the colors available on a user's account that can be used to style workspaces.
  name: Mavenlink Account Colors API
  slug: mavenlink-account-colors-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Account Invitations represent invitations for non-users to join a Kantata OX account.
  name: Mavenlink Account Invitations API
  slug: mavenlink-account-invitations-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Represents a location associated with an account.
  name: Mavenlink Account Locations API
  slug: mavenlink-account-locations-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Each user on an account will have an account membership that describes their relationship to the account. When you add a user to an account, create a new `account_membership`. When you remove a user f
  name: Mavenlink Account Memberships API
  slug: mavenlink-account-memberships-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: The Rate Card activation endpoints allow you to check whether the Rate Cards feature has been activated on the user's account. It also allows you to activate the feature on the user's account.
  name: Mavenlink Activations API
  slug: mavenlink-activations-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: The Assignments object allows you to view and manage task assignments for named or [unnamed resources](https://mavenlink.zendesk.com/hc/en-us/articles/115004696493#Unnamed). **Note:** Because [Daily S
  name: Mavenlink Assignments API
  slug: mavenlink-assignments-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: An Attachment is a file asset that is attached to another Kantata OX object. Depending on the type of object, the file is used or displayed in different ways. The objects that Attachments can be attac
  name: Mavenlink Attachments API
  slug: mavenlink-attachments-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: A Backup Approver Association represents the relationship of a delegated approver to a range of specific dates. Approval responsibilities are delegated to a backup approver.
  name: Mavenlink Backup Approver Associations API
  slug: mavenlink-backup-approver-associations-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Represents the billable utilization target for an account member. Each record has an effective date; the active billable utilization is the one with the most recent effective date. These endpoints are
  name: Mavenlink Billable Utilizations API
  slug: mavenlink-billable-utilizations-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Billing milestones allow you to set up billable items in a project that are separate from the Task Tracker work and have invoicing rules. A set of billing milestones in a project is known as the [Bill
  name: Mavenlink Billing Milestones API
  slug: mavenlink-billing-milestones-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Represents the default configuration for presenting invoices to clients.
  name: Mavenlink Client Invoice Defaults API
  slug: mavenlink-client-invoice-defaults-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Cost Rate represents the hourly cost for an account member, specified in a specific currency. A cost rate with the same currency as the account default currency is called the `default cost rate`.
  name: Mavenlink Cost Rates API
  slug: mavenlink-cost-rates-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: This object allows you to view the [names, ISO codes, and symbols of currencies supported by Kantata OX](https://mavenlink.zendesk.com/hc/en-us/articles/360041576473).
  name: Mavenlink Currencies API
  slug: mavenlink-currencies-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: The Custom Branding API from Mavenlink — 1 operation(s) for custom branding.
  name: Mavenlink Custom Branding API
  slug: mavenlink-custom-branding-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Custom Field Choices are possible values for `'single'` and `'multi'` type custom fields.
  name: Mavenlink Custom Field Choices API
  slug: mavenlink-custom-field-choices-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Custom Field Sets contain custom fields and definitions of each fields' subject type. The supported subjects are currently *Workspace*, *Story*, *User*, and *WorkspaceGroup*.
  name: Mavenlink Custom Field Sets API
  slug: mavenlink-custom-field-sets-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: 'If [Custom Fields](/tag/Custom-Fields) represent the fields themselves, Custom Field Values represent the values in/of those fields. The Custom Field Values object allows you to view, create, update, '
  name: Mavenlink Custom Field Values API
  slug: mavenlink-custom-field-values-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: The [Custom Fields](https://mavenlink.zendesk.com/hc/en-us/articles/202924760-Custom-Fields-Overview-#arrange) object allows you to view, create, update, and delete extra fields for additional Estimat
  name: Mavenlink Custom Fields API
  slug: mavenlink-custom-fields-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Daily Scheduled Hours (also called Story Allocation Days) is the allocation of time for a resource to spend on a specific task, on a specific day. Daily Scheduled Hours are part of [Assignments](/tag/
  name: Mavenlink Daily Scheduled Hours (Story Allocation Days) API
  slug: mavenlink-daily-scheduled-hours-story-allocation-days-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: This object allows you to export specific data sets from Kantata OX. You can view the full schema of available data sets using this endpoint. To use this endpoint, you need to be an [account administr
  name: Mavenlink Data Export Schema API
  slug: mavenlink-data-export-schema-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: This object allows you to export specific data sets from Kantata OX. You can create or cancel exports. You can also view the full schema of available data sets, view details for all exports, and downl
  name: Mavenlink Data Exports API
  slug: mavenlink-data-exports-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Estimate Scenario Resource Allocations contain time-related data for scenario resources, used for calculating estimated cost and scheduled hours.
  name: Mavenlink Estimate Scenario Resource Allocations API
  slug: mavenlink-estimate-scenario-resource-allocations-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Estimate Scenario Resources represent placeholders for unnamed resources in a specific estimate scenario.
  name: Mavenlink Estimate Scenario Resources API
  slug: mavenlink-estimate-scenario-resources-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: An Estimate Scenario is a possible project configuration, consisting of an estimated budget, rate card, resources, and other related fields for a specified estimate.
  name: Mavenlink Estimate Scenarios API
  slug: mavenlink-estimate-scenarios-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: An Estimate represents a potential project. Estimates allow you to plan out a project's budget, resources, and allocations through associated estimate scenarios.
  name: Mavenlink Estimates API
  slug: mavenlink-estimates-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: 'A change is called a [Subscribed Event](https://mavenlink.zendesk.com/hc/en-us/articles/4407962435227), and the type of change is called a *Subscribed Event Type*. *Note:* Only Account Administrators '
  name: Mavenlink Event Types API
  slug: mavenlink-event-types-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Up to 9 days of trackable changes ("events") for an account can be accessed via the Subscribed Events API. For a list of all the event types tracked by Subscribed Events, please see the [Knowledge Bas
  name: Mavenlink Events API
  slug: mavenlink-events-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: This object allows you to view or edit foreign currency exchange rates, depending on your [Foreign Exchange Access Group Set](https://mavenlink.zendesk.com/hc/en-us/articles/360047485453) permissions.
  name: Mavenlink Exchange Tables API
  slug: mavenlink-exchange-tables-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Expense budgets allow you to plan for non-labor expenses.
  name: Mavenlink Expense Budgets API
  slug: mavenlink-expense-budgets-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: An Expense Category represents the type of expense that is being reported. Expense categories have no attributes and consist of just their name as a string. They can be changed by Account Administrato
  name: Mavenlink Expense Categories API
  slug: mavenlink-expense-categories-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Expense report submissions contain a set of expense line items. These expenses must be approved through an expense report submission before they can be added to an invoice. All submission expenses mus
  name: Mavenlink Expense Report Submissions API
  slug: mavenlink-expense-report-submissions-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Expenses are defined as costs incurred as part of a project, but not related to time. Once created, expenses can be included in generated invoices.
  name: Mavenlink Expenses API
  slug: mavenlink-expenses-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: An external payment is a manual record of a payment made outside of Kantata OX. An external payment can be applied to an invoice, or just recorded directly to a project.
  name: Mavenlink External Payments API
  slug: mavenlink-external-payments-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: External References allows users see which objects (one of `Assignment`, `BillingMilestone`, `CustomField`, `CustomFieldChoice`, `CustomFieldSet`, `CustomFieldValue`, `Estimate`, `EstimateScenario`, `
  name: Mavenlink External References API
  slug: mavenlink-external-references-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Story Follows allow users to follow a task to which they are not assigned.
  name: Mavenlink Followers API
  slug: mavenlink-followers-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: A Holiday Calendar Association represents the relationship between holiday objects and calendar objects. A Holiday can be associated with several different calendars. To associate a holiday with a cal
  name: Mavenlink Holiday Calendar Associations API
  slug: mavenlink-holiday-calendar-associations-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: A list of all calendars associated to an individual user.
  name: Mavenlink Holiday Calendar Memberships API
  slug: mavenlink-holiday-calendar-memberships-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Holiday Calendars define the days in which account members are unavailable to work due to company-wide days off.
  name: Mavenlink Holiday Calendars API
  slug: mavenlink-holiday-calendars-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Holidays are the company-wide days off that have been added to a user's Kantata OX account.
  name: Mavenlink Holidays API
  slug: mavenlink-holidays-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: '[Insights Access Groups](https://mavenlink.zendesk.com/hc/en-us/articles/115002115073) allow you to manage classic Insights access for users. An Insights Access Group Membership represents the connect'
  name: Mavenlink Insights Access Group Memberships API
  slug: mavenlink-insights-access-group-memberships-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: 'Built with an easy-to-use, modern, and intuitive dashboard editor, Insights dynamic dashboards are based on the same powerful data engine as classic dashboards and help you make data-driven decisions '
  name: Mavenlink Insights Dynamic Dashboards API
  slug: mavenlink-insights-dynamic-dashboards-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: This object allows you to manage scheduled exports of classic Insights reports from Kantata OX. An export of a classic Insights report that is scheduled to recur is called a scheduled job. You can cre
  name: Mavenlink Insights Report Exports API
  slug: mavenlink-insights-report-exports-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: View a list of classic Insights reports.
  name: Mavenlink Insights Reports API
  slug: mavenlink-insights-reports-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Users can create Invoices in a Kantata OX project. An Invoice must have at least one line item (a time entry, expense, fixed fee item, or additional item). By default, the recipient of an invoice is t
  name: Mavenlink Invoices API
  slug: mavenlink-invoices-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Line Item Locks provide a way for you to lock time in the past so that previous time entries cannot be edited or updated and new time entries cannot be created before the selected lock date. Line Item
  name: Mavenlink Line Item Locks API
  slug: mavenlink-line-item-locks-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: An Organization Membership represents the connection of a user and project to an organization.
  name: Mavenlink Organization Memberships API
  slug: mavenlink-organization-memberships-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: 'The Organizations feature in Kantata OX is composed of two independent trees: Department and Geography. Each has its own hierarchy structure. Users and Workspaces are associated to exact positions in '
  name: Mavenlink Organizations API
  slug: mavenlink-organizations-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: A participation represents the relationship between a participant and a project, including a participant's permission level, whether they're a provider or client, and many other properties. See the 20
  name: Mavenlink Participations API
  slug: mavenlink-participations-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: A Post represents a message written by participants in a project that appears in the project. Replies are only included if they are directly related to a post. Replies to events, such as Change Orders
  name: Mavenlink Posts API
  slug: mavenlink-posts-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: The [Project Accounting](https://mavenlink.zendesk.com/hc/en-us/articles/4403832107419-Project-Accounting) Records object allows you to view, create, and delete financial records related to revenue re
  name: Mavenlink Project Accounting Records API
  slug: mavenlink-project-accounting-records-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Project snapshots capture the state of a project at a specific point in time. Snapshots are useful for gaining a historical perspective on a project, and for comparing the current state of a project t
  name: Mavenlink Project Snapshots API
  slug: mavenlink-project-snapshots-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Project Template Additional Tabs are additional tabs configured in a project template that are added to a project when the template is applied.
  name: Mavenlink Project Template Additional Tabs API
  slug: mavenlink-project-template-additional-tabs-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Project Template Assignments(Project Template Resources) represent placeholders for task assignees in project templates. These assignments are mapped to project template stories and are assigned to re
  name: Mavenlink Project Template Assignments API
  slug: mavenlink-project-template-assignments-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Project Template Expense Budgets are expense budgets configured in a project template that are added to a project when the template is applied.
  name: Mavenlink Project Template Expense Budgets API
  slug: mavenlink-project-template-expense-budgets-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Project Templates are sets of tasks and attributes that can be applied to new or existing projects. A single template can be used on any number of projects. A project template's tasks are all stored i
  name: Mavenlink Project Templates API
  slug: mavenlink-project-templates-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Rate Card Roles belong to a Rate Card Version and represent the bill rate, in cents per hour, for a specific Role. For example, the rate for the role of Developer may be 2000 cents per hour. It is not
  name: Mavenlink Rate Card Role (Rate for a Role) API
  slug: mavenlink-rate-card-role-rate-for-a-role-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: In the Rate Card system, Rate Card Set Versions represent snapshots of a Rate Card Set, that take effect on the set published date. A Rate Card Set Version owns a copy of each Rate Card Version of a R
  name: Mavenlink Rate Card Set Version (Effective version by Date) API
  slug: mavenlink-rate-card-set-version-effective-version-by-date-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: A Rate Card Set represents a group of Rate Cards with multiple currencies that can be bundled together. A Rate Card Set belongs to an account and can have several Rate Card Set Versions, each represen
  name: Mavenlink Rate Card Sets (Group of Rate Cards) API
  slug: mavenlink-rate-card-sets-group-of-rate-cards-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Each Rate Card Table Row represents a role and its rates and currencies for a specific [Rate Card Set Version](/tag/Rate-Card-Set-Version-(Effective-version-by-Date)).
  name: Mavenlink Rate Card Table Rows API
  slug: mavenlink-rate-card-table-rows-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: 'Rate Card Versions represent a snapshot of a Rate Card at a specified point in time. They are used to set the default rate. Rate Card Versions belong to a Rate Card Set Version and own many Rate Card '
  name: Mavenlink Rate Card Versions API
  slug: mavenlink-rate-card-versions-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Rate Cards belong to a Rate Card Set and represent the currencies in that set. Rate Cards have many Rate Card Versions which represent the effective version of a Rate Card at a specified point of time
  name: Mavenlink Rate Cards (Multiple Currencies) API
  slug: mavenlink-rate-cards-multiple-currencies-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: A Recommendation suggests a User for an Unnamed Resource (or some other un-staffed position). The system recommends Users based on how well they match the attributes of a target resource. Attributes i
  name: Mavenlink Recommendations API
  slug: mavenlink-recommendations-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Resource Requests are used as a method for a requestor to ask an approver to staff a resource. Resource Requests are associated to a workspace resource and must have an approver associated.
  name: Mavenlink Resource Requests API
  slug: mavenlink-resource-requests-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Revenue recognition methods determine how revenue is recognized. Methods are configured at the account level, then each project can have an available method applied. Available only when the [early acc
  name: Mavenlink Revenue Recognition Methods API
  slug: mavenlink-revenue-recognition-methods-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: A Role represents the main position or title assigned to members on an account. Roles may be associated with account memberships, account invitations, participation, project template assignments, rate
  name: Mavenlink Roles API
  slug: mavenlink-roles-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: A Skill Category represents the classification for a group of skills. Options are 'Skill', 'Language', 'Certification', and 'Other'. Skill categories are defined by Kantata OX and cannot be modified o
  name: Mavenlink Skill Categories API
  slug: mavenlink-skill-categories-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Skill Memberships represent skills that has been assigned to a specified user.
  name: Mavenlink Skill Memberships API
  slug: mavenlink-skill-memberships-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Skills are used in Kantata OX to describe capabilities of users for the purposes of resource planning. They can be associated with a user through a Skill Membership. A user can be associated with up t
  name: Mavenlink Skills API
  slug: mavenlink-skills-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: A Status Report represents a snapshot of a Workspace's status across several categories at a moment in time. Status Reports are usually referred to as Health Reports in the UI.
  name: Mavenlink Status Reports API
  slug: mavenlink-status-reports-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Stories are tasks, milestones, deliverables, or issues in Kantata OX. They belong to Workspaces, show up in the local and global task trackers, can be linked to Posts, can have sub-Stories and TaskLis
  name: Mavenlink Stories API
  slug: mavenlink-stories-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Story dependencies define relationships between tasks and the sequence in which they must be completed in order to close a project. A dependency is between two tasks (stories) in a project (workspace)
  name: Mavenlink Story Dependencies API
  slug: mavenlink-story-dependencies-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Story State Changes in Kantata OX act as an audit trail for changes to the state of a Story. Story State Changes cannot be created directly. They will be created for you automatically when you set the
  name: Mavenlink Story State Changes API
  slug: mavenlink-story-state-changes-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Story Tasks are used in Kantata OX to track a list of checklist items within a Story. This model includes a completion boolean and a position integer.
  name: Mavenlink Story Tasks API
  slug: mavenlink-story-tasks-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Survey Answers (Legacy) appear on and can be responded to through surveys. Survey Answers (Legacy) are required to have a value for the answer (i.e. answers must have at least one choice selected or a
  name: Mavenlink Survey Answers (Legacy) API
  slug: mavenlink-survey-answers-legacy-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: 'Survey Questions (Legacy) appear on and can be responded to through surveys. **Note**: This feature requires the Surveys (Legacy) account add-on. This feature is unrelated to Pulse surveys.'
  name: Mavenlink Survey Questions (Legacy) API
  slug: mavenlink-survey-questions-legacy-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: 'Survey Templates (Legacy) define a set of questions and defaults from which Survey Responses can be created. **Note**: This feature requires the Surveys (Legacy) account add-on. This feature is unrela'
  name: Mavenlink Survey Templates (Legacy) API
  slug: mavenlink-survey-templates-legacy-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: 'Survey Response (Legacy) represents an instance of a particular survey that has been assigned for response. **Note**: This feature requires the Surveys (Legacy) account add-on. This feature is unrelat'
  name: Mavenlink Surveys Responses (Legacy) API
  slug: mavenlink-surveys-responses-legacy-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Task Status Sets allow you to create custom statuses for tasks (stories) that can then be applied to projects.
  name: Mavenlink Task Status Sets API
  slug: mavenlink-task-status-sets-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Custom task statuses can be created to be used on tasks (stories). Custom task statuses are associated to task status sets, which can be applied to projects (workspaces).
  name: Mavenlink Task Statuses API
  slug: mavenlink-task-statuses-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: This object allows you to manage Kantata OX time entries, depending on your permissions. Creating and updating time entries allows you to include time when invoicing clients.
  name: Mavenlink Time Entries API
  slug: mavenlink-time-entries-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Time Off Entries represent the time and dates that a user has requested off from work, such as PTO or vacation days.
  name: Mavenlink Time Off Entries API
  slug: mavenlink-time-off-entries-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: This section contains an endpoint to approve multiple Timesheet Submissions at once.
  name: Mavenlink Timesheet Approvals API
  slug: mavenlink-timesheet-approvals-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: This section contains an endpoint to cancel multiple Timesheet Submissions at once.
  name: Mavenlink Timesheet Cancellations API
  slug: mavenlink-timesheet-cancellations-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: This section contains an endpoint to reject multiple Timesheet Submissions at once.
  name: Mavenlink Timesheet Rejections API
  slug: mavenlink-timesheet-rejections-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Timesheet Submissions hold a set of time entries for a specified week, and can be approved, rejected, or canceled. You can enable timesheet submissions and approval in your [project settings](https://
  name: Mavenlink Timesheet Submissions API
  slug: mavenlink-timesheet-submissions-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: User File Associations in Kantata OX act as a join object between Users, Workspaces, and Attachments / Google Documents.
  name: Mavenlink User File Associations API
  slug: mavenlink-user-file-associations-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: A User Group Membership represents the connection of a user to a [Workspace Group](/tag/Workspace-Groups). You must be an [Account Administrator](https://knowledge.kantata.com/hc/en-us/articles/203041
  name: Mavenlink User Group Memberships API
  slug: mavenlink-user-group-memberships-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Users represent the individuals that are participating in Kantata OX projects . User objects are often returned as nested JSON objects within other returned items such as posts or tasks.
  name: Mavenlink Users API
  slug: mavenlink-users-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: A Vendor is an entity to which an expense can be paid.
  name: Mavenlink Vendors API
  slug: mavenlink-vendors-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: A workspace allocation represents a resource’s allocation over a specific period of time. A workspace allocation is always associate with a workspace resource.
  name: Mavenlink Workspace Allocations API
  slug: mavenlink-workspace-allocations-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: A Gantt workspace baseline is a snapshot of a workspace at a particular point in time. The snapshot contains aggregate statistics and certain data about each story (task).
  name: Mavenlink Workspace Baselines API
  slug: mavenlink-workspace-baselines-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Workspace Groups (also known as groups) allow for the categorization of Kantata OX Workspaces. Workspace Groups are unique to each Kantata OX Account.
  name: Mavenlink Workspace Groups API
  slug: mavenlink-workspace-groups-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Workspace Invoice Preferences specify the default values that are applied to new invoices created for the specified project. It is only used for projects that have financials enabled. These preference
  name: Mavenlink Workspace Invoice Preferences API
  slug: mavenlink-workspace-invoice-preferences-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Workspace Resource Skills represent skills that have been assigned to a workspace resource.
  name: Mavenlink Workspace Resource Skills API
  slug: mavenlink-workspace-resource-skills-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: 'A workspace resource is the object that is tied to assignments and allocations within a Workspace. Workspace Resources can be: - Named Resources: Resources with a user_id. - Unnamed Resources: Resourc'
  name: Mavenlink Workspace Resources API
  slug: mavenlink-workspace-resources-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Workspace Status Changes represent changes made to the status of a project.
  name: Mavenlink Workspace Status Changes API
  slug: mavenlink-workspace-status-changes-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Workspace Task Status Sets represent the connection between workspaces (projects) and task (story) status sets, which enable the use of custom task statuses.
  name: Mavenlink Workspace Task Status Sets API
  slug: mavenlink-workspace-task-status-sets-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Workspaces (also called projects) represent the space in which Kantata OX users plan, communicate, and collaborate.
  name: Mavenlink Workspaces API
  slug: mavenlink-workspaces-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: A Workweek Membership represents the relationship of a user to a workweek.
  name: Mavenlink Workweek Memberships API
  slug: mavenlink-workweek-memberships-api
- baseURL: https://api.mavenlink.com/api/v1/
  baseurl_source: declared
  description: Workweeks in Kantata OX are owned by an Account. They can be used as the default for an Account or can be associated to a User through a Workweek Membership.
  name: Mavenlink Workweeks API
  slug: mavenlink-workweeks-api
artifact_total: 115
asyncapis:
- description: ''
  name: Mavenlink Event Surface
  slug: mavenlink-event-surface
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/mavenlink-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mavenlink-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mavenlink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kantata.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.kantata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kantata.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.kantata.com/kantata/specification
- group: start
  title: ''
  type: GettingStarted
  url: https://knowledge.kantata.com/hc/en-us/articles/202811760-Kantata-API-Overview
- group: operate
  title: ''
  type: Support
  url: https://www.kantata.com/customer-resources
- group: operate
  title: ''
  type: HelpCenter
  url: https://knowledge.kantata.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.kantata.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mavenlink
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kantata.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.mavenlink.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kantata.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kantata.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/mavenlink-trust-center.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mavenlink.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mavenlink-changelog.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/mavenlink-openapi.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/mavenlink-connector.proto
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mavenlink-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mavenlink-well-known.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/mavenlink-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mavenlink-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/mavenlink-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mavenlink-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mavenlink-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mavenlink-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mavenlink-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mavenlink-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mavenlink-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mavenlink-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mavenlink-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/mavenlink-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mavenlink-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mavenlink-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mavenlink-rate-limits.yml
created: '2026-08-25'
description: 'Mavenlink is the professional services automation (PSA) platform now shipped as Kantata OX, following the 2022 merger of Mavenlink and Kimble Applications that formed Kantata. It combines project management, resource management and forecasting, time and expense tracking, project accounting, invoicing, rate cards, and business intelligence for services organizations. The public REST API is still served from the original Mavenlink domain at https://api.mavenlink.com/api/v1/ and is documented as the "Kantata OX API" at developer.kantata.com: a Swagger 2.0 contract covering 419 operations across 218 paths and roughly 100 resource groups, authenticated with OAuth 2.0 authorization-code bearer tokens issued from app.mavenlink.com. Alongside REST the company operates an OAuth-gated remote MCP server at https://api.mavenlink.com/mcp, publishes an A2A agent card and an anonymous documentation MCP server on its developer portal, and ships a gRPC connector service definition that third
  parties implement to extend the Kantata Workflow Platform with custom triggers and actions.'
image: https://www.kantata.com/images/logos/Kantata.png
layout: provider
mcp_servers:
- description: ''
  name: Mavenlink MCP Server
  slug: mavenlink-mcp-server
- description: ''
  name: Mavenlink MCP Server
  slug: mavenlink-mcp-server-2
- description: ''
  name: Mavenlink MCP Server
  slug: mavenlink-mcp-server-3
modified: '2026-08-25'
name: Mavenlink
nav: Providers
network: true
overview: 'Mavenlink publishes 101 APIs on the [APIs.io](https://apis.io/) network, including Access Group Memberships API, Account Colors API, Account Invitations API, and 98 more. Tagged areas include Professional Services Automation, Project Management, Resource Management, Time Tracking, and Expense Management.


  The Mavenlink catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mavenlink''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 32 more developer resources.'
plans:
- name: Mavenlink Plans Pricing
  plan_count: 0
  slug: mavenlink-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Mavenlink Rate Limits
  slug: mavenlink-rate-limits
scopes:
- name: Mavenlink Scopes
  scope_count: 6
  slug: mavenlink-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 24.0
    catalog_earned_first_party: 0.0
    catalog_gap: 91.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 4.5
    contract_quality: 61.1
    developer_ergonomics: 66.1
    discoverability: 51.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 101
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mavenlink/refs/heads/main/screenshots/mavenlink-2026-09-02T150445.png
security:
- kind: authentication
  name: Mavenlink Authentication
  slug: mavenlink-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Mavenlink Domain Security
  slug: mavenlink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mavenlink Vulnerability Disclosure
  slug: mavenlink-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Mavenlink Trust Center
  slug: mavenlink-trust-center
  summary_line: trust center published
slug: mavenlink
tags:
- Professional Services Automation
- Project Management
- Resource Management
- Time Tracking
- Expense Management
- Invoicing
- Project Accounting
- Business Intelligence
- Workflow-Automation
- MCP
- agent-native
- Company
website: https://www.kantata.com/
---
