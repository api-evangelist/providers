---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Microsoft Project Agentic Access
  operation_count: 63
  slug: microsoft-project-agentic-access
  summary_line: 63 operations · 31 acting
api_count: 16
apis:
- description: 'Client-Side Object Model API for programmatic access to Project Online and Project Server. Provides .NET, Silverlight, Windows Phone, and JavaScript interfaces for CRUD operations on projects, tasks, '
  name: Microsoft Project Online CSOM API
  slug: csom-api
- description: OData-based reporting feed for read-only access to Project Server and Project Online reporting data. Provides access to project, task, resource, assignment, and timesheet reporting tables and views vi
  name: Microsoft Project OData Reporting API
  slug: odata-reporting-api
- description: JavaScript API for building Office Add-ins that extend Microsoft Project desktop client. Enables reading task, resource, and view data from the active project within a task pane add-in.
  name: Microsoft Project JavaScript API
  slug: javascript-api
- baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer
  baseurl_source: declared
  description: Manage resource assignments to tasks
  name: Microsoft Project Assignments API
  slug: microsoft-project-assignments-api
- baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer
  baseurl_source: declared
  description: Manage enterprise calendars
  name: Microsoft Project Calendars API
  slug: microsoft-project-calendars-api
- baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer
  baseurl_source: declared
  description: Manage enterprise custom field definitions
  name: Microsoft Project Custom Fields API
  slug: microsoft-project-custom-fields-api
- baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer
  baseurl_source: declared
  description: Manage enterprise project type configurations
  name: Microsoft Project Enterprise Project Types API
  slug: microsoft-project-enterprise-project-types-api
- baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer
  baseurl_source: declared
  description: Manage event handler subscriptions
  name: Microsoft Project Event Handlers API
  slug: microsoft-project-event-handlers-api
- baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer
  baseurl_source: declared
  description: Manage lookup table definitions and entries
  name: Microsoft Project Lookup Tables API
  slug: microsoft-project-lookup-tables-api
- baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer
  baseurl_source: declared
  description: Manage workflow phases
  name: Microsoft Project Phases API
  slug: microsoft-project-phases-api
- baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer
  baseurl_source: declared
  description: Manage projects and project lifecycle operations
  name: Microsoft Project Projects API
  slug: microsoft-project-projects-api
- baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer
  baseurl_source: declared
  description: Manage enterprise resources and project resources
  name: Microsoft Project Resources API
  slug: microsoft-project-resources-api
- baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer
  baseurl_source: declared
  description: Manage workflow stages
  name: Microsoft Project Stages API
  slug: microsoft-project-stages-api
- baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer
  baseurl_source: declared
  description: Manage project tasks and subtasks
  name: Microsoft Project Tasks API
  slug: microsoft-project-tasks-api
- baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer
  baseurl_source: declared
  description: Manage timesheet periods, lines, and work entries
  name: Microsoft Project Timesheets API
  slug: microsoft-project-timesheets-api
- baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer
  baseurl_source: declared
  description: Manage workflow activities
  name: Microsoft Project Workflow Activities API
  slug: microsoft-project-workflow-activities-api
artifact_total: 105
collections:
- collection_type: postman
  name: Microsoft Project Online REST Assignments API
  slug: postman-microsoft-project-assignments-api
- collection_type: postman
  name: Microsoft Project Online REST Assignments Calendars API
  slug: postman-microsoft-project-calendars-api
- collection_type: postman
  name: Microsoft Project Online REST Assignments Custom Fields API
  slug: postman-microsoft-project-custom-fields-api
- collection_type: postman
  name: Microsoft Project Online REST Assignments Enterprise Project Types API
  slug: postman-microsoft-project-enterprise-project-types-api
- collection_type: postman
  name: Microsoft Project Online REST Assignments Event Handlers API
  slug: postman-microsoft-project-event-handlers-api
- collection_type: postman
  name: Microsoft Project Online REST Assignments Lookup Tables API
  slug: postman-microsoft-project-lookup-tables-api
- collection_type: postman
  name: Microsoft Project Online REST Assignments Phases API
  slug: postman-microsoft-project-phases-api
- collection_type: postman
  name: Microsoft Project Online REST Assignments Projects API
  slug: postman-microsoft-project-projects-api
- collection_type: postman
  name: Microsoft Project Online REST Assignments Resources API
  slug: postman-microsoft-project-resources-api
- collection_type: postman
  name: Microsoft Project Online REST Assignments Stages API
  slug: postman-microsoft-project-stages-api
- collection_type: postman
  name: Microsoft Project Online REST Assignments Tasks API
  slug: postman-microsoft-project-tasks-api
- collection_type: postman
  name: Microsoft Project Online REST Assignments Timesheets API
  slug: postman-microsoft-project-timesheets-api
- collection_type: postman
  name: Microsoft Project Online REST Assignments Workflow Activities API
  slug: postman-microsoft-project-workflow-activities-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Project Online REST Assignments API
  slug: open-microsoft-project-assignments-api
- collection_type: open
  name: Microsoft Project Online REST Assignments Calendars API
  slug: open-microsoft-project-calendars-api
- collection_type: open
  name: Microsoft Project Online REST Assignments Custom Fields API
  slug: open-microsoft-project-custom-fields-api
- collection_type: open
  name: Microsoft Project Online REST Assignments Enterprise Project Types API
  slug: open-microsoft-project-enterprise-project-types-api
- collection_type: open
  name: Microsoft Project Online REST Assignments Event Handlers API
  slug: open-microsoft-project-event-handlers-api
- collection_type: open
  name: Microsoft Project Online REST Assignments Lookup Tables API
  slug: open-microsoft-project-lookup-tables-api
- collection_type: open
  name: Microsoft Project Online REST Assignments Phases API
  slug: open-microsoft-project-phases-api
- collection_type: open
  name: Microsoft Project Online REST Assignments Projects API
  slug: open-microsoft-project-projects-api
- collection_type: open
  name: Microsoft Project Online REST Assignments Resources API
  slug: open-microsoft-project-resources-api
- collection_type: open
  name: Microsoft Project Online REST Assignments Stages API
  slug: open-microsoft-project-stages-api
- collection_type: open
  name: Microsoft Project Online REST Assignments Tasks API
  slug: open-microsoft-project-tasks-api
- collection_type: open
  name: Microsoft Project Online REST Assignments Timesheets API
  slug: open-microsoft-project-timesheets-api
- collection_type: open
  name: Microsoft Project Online REST Assignments Workflow Activities API
  slug: open-microsoft-project-workflow-activities-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-project/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-project-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-project-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-project-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-project-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-project-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/microsoft-365
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/en-us/office/client-developer/project/project-programming-tasks
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/project-blog/bg-p/ProjectBlog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/microsoft-365/project/compare-microsoft-project-management-software
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OfficeDev/Project-Samples
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/ms-project
- group: learn
  title: ''
  type: Training
  url: https://support.microsoft.com/en-us/project
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/office/client-developer/project/getting-started-developing-project-server-workflows
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev
- group: build
  title: Project Accelerator
  type: CodeExamples
  url: https://github.com/OfficeDev/Project-Accelerator
- group: build
  title: Dataverse Plugin Sample
  type: CodeExamples
  url: https://github.com/OfficeDev/Project-Dataverse-Plugin-Sample
- group: design
  title: ''
  type: SpectralRules
  url: rules/microsoft-project-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-project-vocabulary.yaml
created: '2024-01-15'
description: Microsoft Project is a project management software product developed by Microsoft. It provides tools for developing plans, assigning resources to tasks, tracking progress, managing budgets, and analyzing workloads. Microsoft Project offers REST APIs via SharePoint/Project Online, a Client-Side Object Model (CSOM), OData reporting feeds, and JavaScript APIs for building add-ins and integrations.
examples:
- key_count: 10
  name: Rest Api Assignment Example
  slug: rest-api-assignment-example
- key_count: 5
  name: Rest Api Calendar Example
  slug: rest-api-calendar-example
- key_count: 10
  name: Rest Api Custom Field Example
  slug: rest-api-custom-field-example
- key_count: 11
  name: Rest Api Enterprise Resource Example
  slug: rest-api-enterprise-resource-example
- key_count: 12
  name: Rest Api Project Example
  slug: rest-api-project-example
- key_count: 18
  name: Rest Api Task Example
  slug: rest-api-task-example
- key_count: 5
  name: Rest Api Time Sheet Example
  slug: rest-api-time-sheet-example
features:
- description: Visual timeline charts for project scheduling with task dependencies, critical path analysis, and milestone tracking.
  name: Gantt Charts
- description: Create, assign, and track tasks with predecessors, successors, constraints, and deadlines.
  name: Task Management
- description: Assign resources to tasks, view workloads, and manage resource availability and capacity.
  name: Resource Management
- description: Manage multiple projects as a portfolio with prioritization, budgeting, and resource allocation across projects.
  name: Portfolio Management
- description: Track project costs, budgets, and earned value metrics for financial project management.
  name: Budgeting and Cost Tracking
- description: Automatic scheduling with task dependencies, resource leveling, and critical path calculation.
  name: Scheduling Engine
- description: Time tracking and approval workflows for resource hours and project progress reporting.
  name: Timesheets
- description: Define enterprise custom fields, lookup tables, and formulas for extended project metadata.
  name: Custom Fields
- description: Pre-built and custom reports with Power BI integration for project, resource, and portfolio analytics.
  name: Reporting and Dashboards
- description: Demand management workflows for project proposals, approvals, and stage-gate governance.
  name: Workflow Automation
- description: SharePoint-based project sites with document libraries, issue tracking, and team communication.
  name: Collaboration
- description: Integration with Power BI, Power Automate, and Power Apps for extended project management scenarios.
  name: Power Platform Integration
finops:
- name: Microsoft Project Finops
  service_category: Project Management
  slug: microsoft-project-finops
image: /assets/icons/microsoft-project.png
integrations:
- description: View and manage project tasks directly within Microsoft Teams channels and tabs.
  name: Microsoft Teams
- description: Connect to Project Online data for interactive dashboards and portfolio analytics.
  name: Power BI
- description: SharePoint-based project sites for document management, collaboration, and task synchronization.
  name: SharePoint
- description: Deep integration with Outlook, Excel, Word, and other Microsoft 365 applications.
  name: Microsoft 365
- description: Automate project workflows, notifications, and approvals using Power Automate flows.
  name: Power Automate
- description: Build custom project management applications using Power Apps with Project data.
  name: Power Apps
- description: Connect project schedules with Azure DevOps work items for software development projects.
  name: Azure DevOps
- description: Integrate lightweight task planning in Planner with enterprise project management in Project.
  name: Microsoft Planner
- description: Project for the web stores data in Microsoft Dataverse, enabling custom integrations and extensions.
  name: Dataverse
- description: Export and import project data to Excel for custom analysis, reporting, and data manipulation.
  name: Excel
json_schemas:
- name: Assignment
  property_count: 10
  slug: rest-api-assignment
- name: Calendar
  property_count: 5
  slug: rest-api-calendar
- name: CustomField
  property_count: 10
  slug: rest-api-custom-field
- name: EnterpriseResource
  property_count: 11
  slug: rest-api-enterprise-resource
- name: Project
  property_count: 12
  slug: rest-api-project
- name: Task
  property_count: 18
  slug: rest-api-task
- name: TimeSheet
  property_count: 5
  slug: rest-api-time-sheet
json_structures:
- name: Rest Api Assignment Structure
  property_count: 10
  slug: rest-api-assignment-structure
- name: Rest Api Calendar Structure
  property_count: 5
  slug: rest-api-calendar-structure
- name: Rest Api Custom Field Structure
  property_count: 10
  slug: rest-api-custom-field-structure
- name: Rest Api Enterprise Resource Structure
  property_count: 11
  slug: rest-api-enterprise-resource-structure
- name: Rest Api Project Structure
  property_count: 12
  slug: rest-api-project-structure
- name: Rest Api Task Structure
  property_count: 18
  slug: rest-api-task-structure
- name: Rest Api Time Sheet Structure
  property_count: 5
  slug: rest-api-time-sheet-structure
jsonld:
- class_count: 11
  name: Microsoft Project Rest Api Context
  property_count: 47
  slug: microsoft-project-rest-api-context
layout: provider
modified: '2026-05-19'
name: Microsoft Project
nav: Providers
network: true
overview: 'Microsoft Project publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Assignments API, Calendars API, Custom Fields API, and 10 more. Tagged areas include Budgeting, Gantt Charts, Microsoft, Portfolio-Management, and Project Management.


  The Microsoft Project catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Microsoft Project''s developer surface includes authentication, developer portal, engineering blog, pricing, support, Stack Overflow tag, training material, and 15 more developer resources.'
plans:
- name: Microsoft Project Plans Pricing
  plan_count: 6
  slug: microsoft-project-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Microsoft Project Rate Limits
  slug: microsoft-project-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Microsoft Project API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: microsoft-project-jsonschema-spectral-rules
- effective_rule_count: 83
  extends:
  - spectral:oas
  name: Microsoft Project API Rules
  rule_count: 42
  severity_counts:
    error: 23
    hint: 0
    info: 7
    warn: 12
  slug: microsoft-project-spectral-rules
scopes:
- name: Microsoft Project Scopes
  scope_count: 2
  slug: microsoft-project-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 76.5
    catalog_earned_first_party: 0.0
    catalog_gap: 38.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 28.8
    contract_quality: 31.0
    developer_ergonomics: 65.5
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-project/refs/heads/main/screenshots/microsoft-project-2026-06-20T185526.png
security:
- kind: authentication
  name: Microsoft Project Authentication
  slug: microsoft-project-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Project Domain Security
  slug: microsoft-project-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Project Vulnerability Disclosure
  slug: microsoft-project-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-project
tags:
- Budgeting
- Gantt Charts
- Microsoft
- Portfolio-Management
- Project Management
- Resource Management
- Scheduling
- Task Management
use_cases:
- description: Plan and track IT infrastructure, software development, and digital transformation projects.
  name: IT Project Management
- description: Schedule construction phases, manage subcontractors, and track material costs.
  name: Construction Project Planning
- description: Coordinate product development timelines, milestones, and cross-functional team resources.
  name: Product Development
- description: Evaluate and prioritize project portfolios based on strategic alignment, ROI, and resource constraints.
  name: Portfolio Optimization
- description: Forecast resource demand, identify bottlenecks, and optimize resource allocation across projects.
  name: Resource Capacity Planning
- description: Manage interdependent projects as programs with shared resources and coordinated timelines.
  name: Program Management
- description: Track agile sprints, backlogs, and team velocity alongside traditional waterfall schedules.
  name: Agile Project Tracking
- description: Generate audit trails and compliance reports for project governance and regulatory requirements.
  name: Compliance Reporting
website: https://learn.microsoft.com/en-us/office/client-developer/project/project-programming-tasks
---
