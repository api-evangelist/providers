---
aid: microsoft-planner
name: Microsoft Planner
description: Microsoft Planner is a task management tool that helps teams organize work, assign tasks, share files, and collaborate on projects within Microsoft 365.
image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
tags:
  - Collaboration
  - Microsoft 365
  - Productivity
  - Project Management
  - Task Management
created: '2024-01-01'
modified: '2026-04-18'
url: https://raw.githubusercontent.com/api-evangelist/microsoft-planner/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - name: Microsoft Planner API
    description: RESTful API for accessing and managing tasks, plans, and buckets in Microsoft Planner through Microsoft Graph.
    image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
    humanURL: https://developer.microsoft.com/en-us/graph/docs/api-reference/v1.0/resources/planner_overview
    baseURL: https://graph.microsoft.com/v1.0/planner
    tags:
      - Assignments
      - Buckets
      - Microsoft Graph
      - Plans
      - Tasks
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview
      - type: OpenAPI
        url: openapi/microsoft-planner-openapi.yml
      - type: JSONSchema
        url: json-schema/microsoft-planner-task-schema.json
      - type: JSONLD
        url: json-ld/microsoft-planner-context.jsonld
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: Pricing
        url: https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft365-plans-and-pricing
      - type: RateLimits
        url: https://learn.microsoft.com/en-us/graph/throttling
      - type: SDK
        url: https://github.com/microsoftgraph/msgraph-sdk-dotnet
        title: .NET SDK
      - type: SDK
        url: https://github.com/microsoftgraph/msgraph-sdk-javascript
        title: JavaScript SDK
      - type: SDK
        url: https://github.com/microsoftgraph/msgraph-sdk-python
        title: Python SDK
      - type: SDK
        url: https://github.com/microsoftgraph/msgraph-sdk-java
        title: Java SDK
      - type: SDK
        url: https://github.com/microsoftgraph/msgraph-sdk-go
        title: Go SDK
      - type: SDK
        url: https://github.com/microsoftgraph/msgraph-sdk-php
        title: PHP SDK
      - type: Support
        url: https://developer.microsoft.com/en-us/graph/support
      - type: ChangeLog
        url: https://developer.microsoft.com/en-us/graph/changelog
      - type: Sandbox
        url: https://developer.microsoft.com/en-us/graph/graph-explorer
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/planner-concept-overview
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview?view=graph-rest-1.0
      - type: Quickstart
        url: https://developer.microsoft.com/en-us/graph/quick-start
    contact:
      - FN: Microsoft Graph Support
        url: https://developer.microsoft.com/en-us/graph/support
        email: graphsdksupport@microsoft.com
  - name: Microsoft Graph Plans API
    description: API for creating, reading, updating, and deleting plans in Microsoft Planner through Microsoft Graph. Plans are the containers for tasks and are owned by groups or other containers.
    image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/plannerplan?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0/planner/plans
    tags:
      - Microsoft Graph
      - Planner
      - Plans
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/plannerplan?view=graph-rest-1.0
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/planner-post-plans?view=graph-rest-1.0
      - type: OpenAPI
        url: openapi/microsoft-planner-openapi.yml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/planner-concept-overview
      - type: Sandbox
        url: https://developer.microsoft.com/en-us/graph/graph-explorer
    contact:
      - FN: Microsoft Graph Support
        url: https://developer.microsoft.com/en-us/graph/support
        email: graphsdksupport@microsoft.com
  - name: Microsoft Graph Tasks API
    description: API for creating, reading, updating, and deleting tasks in Microsoft Planner through Microsoft Graph. Tasks are contained in plans and can be assigned to buckets and users.
    image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/plannertask?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0/planner/tasks
    tags:
      - Assignments
      - Microsoft Graph
      - Planner
      - Tasks
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/plannertask?view=graph-rest-1.0
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/planner-post-tasks?view=graph-rest-1.0
      - type: OpenAPI
        url: openapi/microsoft-planner-openapi.yml
      - type: JSONSchema
        url: json-schema/microsoft-planner-task-schema.json
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/planner-concept-overview
      - type: Sandbox
        url: https://developer.microsoft.com/en-us/graph/graph-explorer
    contact:
      - FN: Microsoft Graph Support
        url: https://developer.microsoft.com/en-us/graph/support
        email: graphsdksupport@microsoft.com
  - name: Microsoft Graph Buckets API
    description: API for creating, reading, updating, and deleting buckets in Microsoft Planner through Microsoft Graph. Buckets represent custom columns for organizing tasks within a plan.
    image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/plannerbucket?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0/planner/buckets
    tags:
      - Buckets
      - Microsoft Graph
      - Organization
      - Planner
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/plannerbucket?view=graph-rest-1.0
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/planner-post-buckets?view=graph-rest-1.0
      - type: OpenAPI
        url: openapi/microsoft-planner-openapi.yml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/planner-concept-overview
      - type: Sandbox
        url: https://developer.microsoft.com/en-us/graph/graph-explorer
    contact:
      - FN: Microsoft Graph Support
        url: https://developer.microsoft.com/en-us/graph/support
        email: graphsdksupport@microsoft.com
  - name: Microsoft Graph Planner API (Beta)
    description: Beta version of the Planner API in Microsoft Graph providing access to preview features including plannerRoster resources, business scenarios integration, and expanded container type support.
    image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview?view=graph-rest-beta
    baseURL: https://graph.microsoft.com/beta/planner
    tags:
      - Beta
      - Microsoft Graph
      - Planner
      - Preview
      - Rosters
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview?view=graph-rest-beta
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview?view=graph-rest-beta
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/planner-concept-overview
      - type: Sandbox
        url: https://developer.microsoft.com/en-us/graph/graph-explorer
    contact:
      - FN: Microsoft Graph Support
        url: https://developer.microsoft.com/en-us/graph/support
        email: graphsdksupport@microsoft.com
  - name: Microsoft Graph Business Scenarios Planner API (Beta)
    description: Beta API for integrating external business processes with Microsoft Planner through business scenarios, allowing creation of scenario-controlled Planner tasks and plans.
    image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/businessscenario-planner-overview?view=graph-rest-beta
    baseURL: https://graph.microsoft.com/beta/solutions/businessScenarios
    tags:
      - Beta
      - Business Scenarios
      - Integration
      - Microsoft Graph
      - Planner
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/businessscenario-planner-overview?view=graph-rest-beta
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/businessscenario-overview?view=graph-rest-beta
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: Sandbox
        url: https://developer.microsoft.com/en-us/graph/graph-explorer
    contact:
      - FN: Microsoft Graph Support
        url: https://developer.microsoft.com/en-us/graph/support
        email: graphsdksupport@microsoft.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
common:
  - type: Portal
    url: https://developer.microsoft.com/en-us/graph
  - type: TermsOfService
    url: https://docs.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/graph/planner-concept-overview
  - type: Blog
    url: https://developer.microsoft.com/en-us/graph/blogs/
  - type: StatusPage
    url: https://developer.microsoft.com/en-us/graph/status
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview
  - type: Login
    url: https://planner.cloud.microsoft
  - type: Support
    url: https://support.microsoft.com/en-us/planner
  - type: FAQ
    url: https://support.microsoft.com/en-us/office/frequently-asked-questions-about-microsoft-planner-d1a2d4e6-a4d7-408c-a48a-31caaa267de5
  - type: GitHubOrganization
    url: https://github.com/microsoftgraph
  - type: ChangeLog
    url: https://developer.microsoft.com/en-us/graph/changelog
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: SDK
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: SignUp
    url: https://developer.microsoft.com/en-us/microsoft-365/dev-program
  - type: Sandbox
    url: https://developer.microsoft.com/en-us/graph/graph-explorer
  - type: RateLimits
    url: https://learn.microsoft.com/en-us/graph/throttling
  - type: OpenAPI
    url: openapi/microsoft-planner-openapi.yml
  - type: JSONSchema
    url: json-schema/microsoft-planner-task-schema.json
  - type: JSONLD
    url: json-ld/microsoft-planner-context.jsonld
  - type: SpectralRules
    url: rules/microsoft-planner-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/microsoft-planner-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/task-management.yaml
  - type: Features
    data:
      - Visual task boards with drag-and-drop organization
      - Plan creation tied to Microsoft 365 Groups
      - Task assignment with due dates and priorities
      - Bucket-based task categorization and organization
      - Checklist subtasks within individual tasks
      - File attachment and external reference linking
      - Progress tracking with charts and status views
      - Microsoft Teams integration for collaborative planning
      - Category labels for cross-cutting task classification
      - Microsoft Graph API for programmatic access
  - type: UseCases
    data:
      - Project management for team-based work coordination
      - Sprint planning and agile task tracking
      - Onboarding workflows for new employees
      - Event planning with task delegation and deadlines
      - Content publishing calendars and editorial workflows
      - IT helpdesk ticket organization and tracking
      - Marketing campaign task management
      - Cross-functional team collaboration on initiatives
  - type: Integrations
    data:
      - Microsoft Teams for in-chat task management
      - Microsoft To Do for personal task sync
      - Power Automate for workflow automation
      - SharePoint for document-linked tasks
      - Outlook for email-to-task conversion
      - Excel for data export and reporting
      - Power BI for advanced analytics dashboards
      - Azure DevOps for development task bridging
---
