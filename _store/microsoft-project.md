---
aid: microsoft-project
name: Microsoft Project
description: Microsoft Project is a project management software product developed by Microsoft. It provides tools for developing plans, assigning resources to tasks, tracking progress, managing budgets, and analyzing workloads. Microsoft Project offers REST APIs via SharePoint/Project Online, a Client-Side Object Model (CSOM), OData reporting feeds, and JavaScript APIs for building add-ins and integrations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Budgeting
  - Gantt Charts
  - Microsoft
  - Portfolio Management
  - Project Management
  - Resource Management
  - Scheduling
  - Task Management
url: https://raw.githubusercontent.com/api-evangelist/microsoft-project/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-18'
specificationVersion: '0.19'
apis:
  - aid: microsoft-project:rest-api
    name: Microsoft Project Online REST API
    description: REST API for accessing and managing Microsoft Project Online and Project Server data including projects, tasks, resources, assignments, calendars, custom fields, timesheets, lookup tables, and workflow activities. Uses SharePoint-based REST endpoints via the ProjectServer service.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/office/client-developer/project/client-side-object-model-csom-for-project-2013
    baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer
    tags:
      - Assignments
      - Calendars
      - Custom Fields
      - Projects
      - Resources
      - REST
      - Tasks
      - Timesheets
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/client-developer/project/client-side-object-model-csom-for-project-2013
      - type: APIReference
        url: https://learn.microsoft.com/en-us/office/client-developer/project/javascript-library-and-rest-reference-for-project-server-2013
      - type: Authentication
        url: https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/authorization-and-authentication-of-sharepoint-add-ins
      - type: CodeExamples
        url: https://github.com/OfficeDev/Project-Samples/tree/main/O365-Project-Online-REST-Samples
      - type: CodeExamples
        url: https://github.com/OfficeDev/Project-Add-in-REST-BasicDataOperations
        title: REST CRUD Operations Sample
      - type: OpenAPI
        url: openapi/microsoft-project-rest-api.yaml
      - type: JSONSchema
        url: json-schema/rest-api-project-schema.json
        title: Project Schema
      - type: JSONSchema
        url: json-schema/rest-api-task-schema.json
        title: Task Schema
      - type: JSONSchema
        url: json-schema/rest-api-enterprise-resource-schema.json
        title: Enterprise Resource Schema
      - type: JSONSchema
        url: json-schema/rest-api-assignment-schema.json
        title: Assignment Schema
      - type: JSONSchema
        url: json-schema/rest-api-calendar-schema.json
        title: Calendar Schema
      - type: JSONSchema
        url: json-schema/rest-api-custom-field-schema.json
        title: Custom Field Schema
      - type: JSONSchema
        url: json-schema/rest-api-time-sheet-schema.json
        title: TimeSheet Schema
      - type: JSONStructure
        url: json-structure/rest-api-project-structure.json
        title: Project Structure
      - type: JSONStructure
        url: json-structure/rest-api-task-structure.json
        title: Task Structure
      - type: JSONStructure
        url: json-structure/rest-api-enterprise-resource-structure.json
        title: Enterprise Resource Structure
      - type: JSONStructure
        url: json-structure/rest-api-assignment-structure.json
        title: Assignment Structure
      - type: JSONStructure
        url: json-structure/rest-api-calendar-structure.json
        title: Calendar Structure
      - type: JSONStructure
        url: json-structure/rest-api-custom-field-structure.json
        title: Custom Field Structure
      - type: JSONStructure
        url: json-structure/rest-api-time-sheet-structure.json
        title: TimeSheet Structure
      - type: JSONLD
        url: json-ld/microsoft-project-rest-api-context.jsonld
      - type: Example
        url: examples/rest-api-project-example.json
        title: Project Example
      - type: Example
        url: examples/rest-api-task-example.json
        title: Task Example
      - type: Example
        url: examples/rest-api-enterprise-resource-example.json
        title: Enterprise Resource Example
      - type: Example
        url: examples/rest-api-assignment-example.json
        title: Assignment Example
      - type: Example
        url: examples/rest-api-calendar-example.json
        title: Calendar Example
      - type: Example
        url: examples/rest-api-custom-field-example.json
        title: Custom Field Example
      - type: Example
        url: examples/rest-api-time-sheet-example.json
        title: TimeSheet Example
  - aid: microsoft-project:csom-api
    name: Microsoft Project Online CSOM API
    description: Client-Side Object Model API for programmatic access to Project Online and Project Server. Provides .NET, Silverlight, Windows Phone, and JavaScript interfaces for CRUD operations on projects, tasks, resources, assignments, custom fields, lookup tables, and enterprise project types.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/office/client-developer/project/client-side-object-model-csom-for-project-2013
    baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer
    tags:
      - .NET
      - Client Library
      - CSOM
      - JavaScript
      - Projects
      - Resources
      - Tasks
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/client-developer/project/client-side-object-model-csom-for-project-2013
      - type: SDK
        url: https://www.nuget.org/packages/Microsoft.SharePointOnline.CSOM/
        title: .NET SDK
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/office/client-developer/project/getting-started-with-the-project-server-csom-and-.net
  - aid: microsoft-project:odata-reporting-api
    name: Microsoft Project OData Reporting API
    description: OData-based reporting feed for read-only access to Project Server and Project Online reporting data. Provides access to project, task, resource, assignment, and timesheet reporting tables and views via the ProjectData service endpoint.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/office/client-developer/project/project-server-2013-architecture
    baseURL: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectData
    tags:
      - OData
      - Projects
      - Reporting
      - Resources
      - Tasks
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/client-developer/project/project-server-2013-architecture
      - type: Authentication
        url: https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/authorization-and-authentication-of-sharepoint-add-ins
  - aid: microsoft-project:javascript-api
    name: Microsoft Project JavaScript API
    description: JavaScript API for building Office Add-ins that extend Microsoft Project desktop client. Enables reading task, resource, and view data from the active project within a task pane add-in.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/office/dev/add-ins/project/project-add-ins
    baseURL: https://appsforoffice.microsoft.com/lib/1/hosted/office.js
    tags:
      - Add-Ins
      - JavaScript
      - Office
      - Task Pane
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/project/project-add-ins
      - type: Quickstart
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/project-quickstart
      - type: APIReference
        url: https://learn.microsoft.com/en-us/javascript/api/office/office.context
      - type: CodeExamples
        url: https://developer.microsoft.com/en-us/microsoft-365/gallery/?filterBy=Project,Samples
common:
  - type: Portal
    url: https://developer.microsoft.com/en-us/microsoft-365
  - type: DeveloperPortal
    url: https://learn.microsoft.com/en-us/office/client-developer/project/project-programming-tasks
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/project-blog/bg-p/ProjectBlog
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Pricing
    url: https://www.microsoft.com/en-us/microsoft-365/project/compare-microsoft-project-management-software
  - type: Support
    url: https://support.microsoft.com/
  - type: GitHubRepository
    url: https://github.com/OfficeDev/Project-Samples
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/ms-project
  - type: Training
    url: https://support.microsoft.com/en-us/project
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/office/client-developer/project/getting-started-developing-project-server-workflows
  - type: GitHubOrganization
    url: https://github.com/OfficeDev
  - type: CodeExamples
    url: https://github.com/OfficeDev/Project-Accelerator
    title: Project Accelerator
  - type: CodeExamples
    url: https://github.com/OfficeDev/Project-Dataverse-Plugin-Sample
    title: Dataverse Plugin Sample
  - type: SpectralRules
    url: rules/microsoft-project-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/project-management.yaml
    title: Project Management Workflow
  - type: Vocabulary
    url: vocabulary/microsoft-project-vocabulary.yaml
  - type: Features
    data:
      - name: Gantt Charts
        description: Visual timeline charts for project scheduling with task dependencies, critical path analysis, and milestone tracking.
      - name: Task Management
        description: Create, assign, and track tasks with predecessors, successors, constraints, and deadlines.
      - name: Resource Management
        description: Assign resources to tasks, view workloads, and manage resource availability and capacity.
      - name: Portfolio Management
        description: Manage multiple projects as a portfolio with prioritization, budgeting, and resource allocation across projects.
      - name: Budgeting and Cost Tracking
        description: Track project costs, budgets, and earned value metrics for financial project management.
      - name: Scheduling Engine
        description: Automatic scheduling with task dependencies, resource leveling, and critical path calculation.
      - name: Timesheets
        description: Time tracking and approval workflows for resource hours and project progress reporting.
      - name: Custom Fields
        description: Define enterprise custom fields, lookup tables, and formulas for extended project metadata.
      - name: Reporting and Dashboards
        description: Pre-built and custom reports with Power BI integration for project, resource, and portfolio analytics.
      - name: Workflow Automation
        description: Demand management workflows for project proposals, approvals, and stage-gate governance.
      - name: Collaboration
        description: SharePoint-based project sites with document libraries, issue tracking, and team communication.
      - name: Power Platform Integration
        description: Integration with Power BI, Power Automate, and Power Apps for extended project management scenarios.
  - type: UseCases
    data:
      - name: IT Project Management
        description: Plan and track IT infrastructure, software development, and digital transformation projects.
      - name: Construction Project Planning
        description: Schedule construction phases, manage subcontractors, and track material costs.
      - name: Product Development
        description: Coordinate product development timelines, milestones, and cross-functional team resources.
      - name: Portfolio Optimization
        description: Evaluate and prioritize project portfolios based on strategic alignment, ROI, and resource constraints.
      - name: Resource Capacity Planning
        description: Forecast resource demand, identify bottlenecks, and optimize resource allocation across projects.
      - name: Program Management
        description: Manage interdependent projects as programs with shared resources and coordinated timelines.
      - name: Agile Project Tracking
        description: Track agile sprints, backlogs, and team velocity alongside traditional waterfall schedules.
      - name: Compliance Reporting
        description: Generate audit trails and compliance reports for project governance and regulatory requirements.
  - type: Integrations
    data:
      - name: Microsoft Teams
        description: View and manage project tasks directly within Microsoft Teams channels and tabs.
      - name: Power BI
        description: Connect to Project Online data for interactive dashboards and portfolio analytics.
      - name: SharePoint
        description: SharePoint-based project sites for document management, collaboration, and task synchronization.
      - name: Microsoft 365
        description: Deep integration with Outlook, Excel, Word, and other Microsoft 365 applications.
      - name: Power Automate
        description: Automate project workflows, notifications, and approvals using Power Automate flows.
      - name: Power Apps
        description: Build custom project management applications using Power Apps with Project data.
      - name: Azure DevOps
        description: Connect project schedules with Azure DevOps work items for software development projects.
      - name: Microsoft Planner
        description: Integrate lightweight task planning in Planner with enterprise project management in Project.
      - name: Dataverse
        description: Project for the web stores data in Microsoft Dataverse, enabling custom integrations and extensions.
      - name: Excel
        description: Export and import project data to Excel for custom analysis, reporting, and data manipulation.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
