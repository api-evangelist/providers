---
name: Azure DevOps
description: Azure DevOps provides developer services for support teams to plan work, collaborate on code development, and build and deploy applications.
image: https://azure.microsoft.com/svghandler/devops/
tags:
  - Agile
  - CI/CD
  - DevOps
  - Project Management
  - Version Control
created: '2024-01-01'
modified: '2026-04-28'
url: https://dev.azure.com
specificationVersion: '0.18'
apis:
  - name: Azure DevOps Services REST API
    description: REST API for Azure DevOps Services providing programmatic access to work items, builds, releases, repositories, and more.
    image: https://azure.microsoft.com/svghandler/devops/
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/
    baseURL: https://dev.azure.com/{organization}
    tags:
      - DevOps
      - REST
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/
      - type: OpenAPI
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance
      - type: Client Libraries
        url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/dotnet-client-libraries?view=azure-devops
    contact:
      - type: Support
        url: https://azure.microsoft.com/en-us/support/devops/
  - name: Azure DevOps Boards API
    description: API for managing work items, boards, backlogs, sprints, and queries in Azure Boards. Enables programmatic access to agile planning and tracking resources.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/
    baseURL: https://dev.azure.com/{organization}/{project}/_apis/wit
    tags:
      - Agile
      - Boards
      - Work Items
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/
      - type: OpenAPI
        url: openapi/azure-devops-work-items-api-openapi.yml
  - name: Azure DevOps Repos API
    description: API for managing Git repositories, pull requests, commits, branches, and pushes in Azure Repos. Supports full programmatic control over source code hosted in Azure DevOps.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/git/
    baseURL: https://dev.azure.com/{organization}/{project}/_apis/git
    tags:
      - Git
      - Repositories
      - Source Control
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/git/
      - type: OpenAPI
        url: openapi/azure-devops-git-api-openapi.yml
  - name: Azure DevOps Pipelines API
    description: API for managing build and release pipelines, pipeline runs, and pipeline artifacts. Provides programmatic access to create, trigger, and monitor CI/CD pipelines.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/pipelines/
    baseURL: https://dev.azure.com/{organization}/{project}/_apis/pipelines
    tags:
      - Builds
      - CI/CD
      - Releases
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/pipelines/
      - type: OpenAPI
        url: openapi/azure-devops-pipelines-api-openapi.yml
  - name: Azure DevOps Build API
    description: API for managing build definitions, queuing builds, and accessing build results and logs. Supports the full lifecycle of continuous integration builds in Azure DevOps.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/build/
    baseURL: https://dev.azure.com/{organization}/{project}/_apis/build
    tags:
      - Automation
      - Build
      - CI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/build/
      - type: OpenAPI
        url: openapi/azure-devops-builds-api-openapi.yml
  - name: Azure DevOps Release API
    description: API for managing release definitions, deployments, and approvals in Azure Pipelines. Enables programmatic control over continuous delivery and release orchestration.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/release/
    baseURL: https://vsrm.dev.azure.com/{organization}/{project}/_apis/release
    tags:
      - CD
      - Deployment
      - Release
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/release/
      - type: OpenAPI
        url: openapi/azure-devops-releases-api-openapi.yml
  - name: Azure DevOps Test Plans API
    description: API for managing test plans, test suites, test cases, and test runs in Azure Test Plans. Provides programmatic access to quality assurance and testing workflows.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/test/
    baseURL: https://dev.azure.com/{organization}/{project}/_apis/test
    tags:
      - QA
      - Test Plans
      - Testing
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/test/
      - type: OpenAPI
        url: openapi/azure-devops-test-plans-api-openapi.yml
  - name: Azure DevOps Artifacts API
    description: API for managing packages, feeds, and artifact dependencies in Azure Artifacts. Supports NuGet, npm, Maven, Python, and Universal packages in private or public feeds.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/artifacts/
    baseURL: https://feeds.dev.azure.com/{organization}/_apis/packaging
    tags:
      - Artifacts
      - Dependencies
      - Packages
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/artifacts/
      - type: OpenAPI
        url: openapi/azure-devops-artifacts-api-openapi.yml
  - name: Azure DevOps Graph API
    description: API for managing users, groups, and memberships within an Azure DevOps organization. Enables programmatic administration of identities and group membership.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/graph/
    baseURL: https://vssps.dev.azure.com/{organization}/_apis/graph
    tags:
      - Groups
      - Permissions
      - Users
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/graph/
  - name: Azure DevOps Core API
    description: API for managing Azure DevOps projects, teams, and team members. Provides foundational access to the organizational structure of an Azure DevOps organization.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/core/
    baseURL: https://dev.azure.com/{organization}/_apis
    tags:
      - Organization
      - Projects
      - Teams
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/core/
  - name: Azure DevOps Security API
    description: API for managing security namespaces, access control lists, and access control entries in Azure DevOps. Used to programmatically set and evaluate permissions on resources.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/security/
    baseURL: https://dev.azure.com/{organization}/_apis/accesscontrollists
    tags:
      - Access Control
      - Permissions
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/security/
  - name: Azure DevOps Service Hooks API
    description: API for managing service hook subscriptions, publishers, and consumers. Enables event-driven integrations by configuring webhooks and other notification mechanisms when Azure DevOps events occur.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/hooks/
    baseURL: https://dev.azure.com/{organization}/_apis/hooks
    tags:
      - Events
      - Integrations
      - Webhooks
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/hooks/
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/devops/service-hooks/overview?view=azure-devops
      - type: OpenAPI
        url: openapi/azure-devops-service-hooks-api-openapi.yml
      - type: AsyncAPI
        url: asyncapi/azure-devops-service-hooks-asyncapi.yml
  - name: Azure DevOps Notifications API
    description: API for managing notification subscriptions for users and teams. Enables programmatic creation and management of email and other notification channels for Azure DevOps events such as work item changes, build results, and pull requests.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/notification/
    baseURL: https://dev.azure.com/{organization}/_apis/notification
    tags:
      - Alerts
      - Notifications
      - Subscriptions
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/notification/
  - name: Azure DevOps Audit API
    description: API for querying and downloading the Azure DevOps audit log. Provides access to auditable events within an organization for security reviews and compliance reporting.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/audit/
    baseURL: https://auditservice.dev.azure.com/{organization}/_apis/audit
    tags:
      - Audit
      - Compliance
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/audit/
  - name: Azure DevOps Search API
    description: API for searching code, work items, and wiki pages across all projects and repositories within an Azure DevOps organization. Supports full-text and filtered search results.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/search/
    baseURL: https://almsearch.dev.azure.com/{organization}/_apis/search
    tags:
      - Code
      - Search
      - Work Items
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/search/
  - name: Azure DevOps Policy API
    description: API for managing code policy configurations and policy types in Azure Repos. Used to define and enforce branch policies such as required reviewers, status checks, and merge strategies.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/policy/
    baseURL: https://dev.azure.com/{organization}/{project}/_apis/policy
    tags:
      - Branch Protection
      - Code Review
      - Policy
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/policy/
  - name: Azure DevOps Distributed Task API
    description: API for managing the pipeline agent infrastructure including agent pools, queues, agents, environments, deployment groups, and task groups. Provides programmatic control over the compute resources used to run pipelines.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/distributedtask/
    baseURL: https://dev.azure.com/{organization}/_apis/distributedtask
    tags:
      - Agents
      - Pipelines
      - Pools
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/distributedtask/
  - name: Azure DevOps Analytics OData API
    description: OData-based API providing access to the Azure DevOps Analytics service for reporting and querying historical and real-time project data. Supports queries across work items, pipelines, and test plans for Power BI and custom reporting scenarios.
    humanURL: https://learn.microsoft.com/en-us/azure/devops/report/extend-analytics/quick-ref?view=azure-devops
    baseURL: https://analytics.dev.azure.com/{organization}/{project}/_odata
    tags:
      - Analytics
      - OData
      - Reporting
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/devops/report/extend-analytics/quick-ref?view=azure-devops
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/devops/report/extend-analytics/odata-api-version?view=azure-devops
  - name: Azure DevOps Wiki API
    description: API for creating and managing wikis and wiki pages within Azure DevOps projects. Every wiki is backed by a Git repository and supports creating, reading, updating, and deleting wikis and pages programmatically.
    image: https://azure.microsoft.com/svghandler/devops/
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/wiki/
    baseURL: https://dev.azure.com/{organization}/{project}/_apis/wiki
    tags:
      - Documentation
      - Pages
      - Wiki
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/wiki/
      - type: OpenAPI
        url: openapi/azure-devops-wiki-api-openapi.yml
  - name: Azure DevOps Extension Management API
    description: API for managing extensions installed in an Azure DevOps organization. Enables programmatic listing, installing, updating, and removing of Marketplace extensions, as well as reading extension data and settings.
    image: https://azure.microsoft.com/svghandler/devops/
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/extensionmanagement/
    baseURL: https://extmgmt.dev.azure.com/{organization}/_apis/extensionmanagement
    tags:
      - Extensions
      - Marketplace
      - Plugins
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/extensionmanagement/
  - name: Azure DevOps Service Endpoint API
    description: API for managing service connections that connect Azure DevOps pipelines to external services such as GitHub, Docker, Azure, and other third-party providers. Supports creating, updating, and sharing service endpoints across projects.
    image: https://azure.microsoft.com/svghandler/devops/
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/
    baseURL: https://dev.azure.com/{organization}/{project}/_apis/serviceendpoint
    tags:
      - Integrations
      - Pipelines
      - Service Connections
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/
  - name: Azure DevOps TFVC API
    description: API for accessing Team Foundation Version Control (TFVC) repositories within Azure DevOps. Provides programmatic access to TFVC items, changesets, shelvesets, labels, and branches for organizations using centralized version control.
    image: https://azure.microsoft.com/svghandler/devops/
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/tfvc/
    baseURL: https://dev.azure.com/{organization}/{project}/_apis/tfvc
    tags:
      - Source Control
      - TFVC
      - Version Control
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/tfvc/
  - name: Azure DevOps Token Administration API
    description: API for organization administrators to retrieve and revoke OAuth authorizations including personal access tokens and session tokens for users in their organizations. Enables centralized token governance and security oversight.
    image: https://azure.microsoft.com/svghandler/devops/
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/tokenadmin/
    baseURL: https://vssps.dev.azure.com/{organization}/_apis/tokenadmin
    tags:
      - Access Control
      - Security
      - Token Administration
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/tokenadmin/
  - name: Azure DevOps Accounts API
    description: API for listing the Azure DevOps organizations that the authenticated user has access to. Each person using Azure DevOps Services has access to one or more organization accounts.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/account/
    baseURL: https://app.vssps.visualstudio.com/_apis/accounts
    tags:
      - Accounts
      - Administration
      - Organizations
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/account/
  - name: Azure DevOps Approvals and Checks API
    description: API for managing pipeline approvals and checks on resources such as environments, service connections, agent pools, variable groups, and secure files. Enables programmatic creation and modification of checks, management of approvals, and querying of check evaluation details.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/approvalsandchecks/
    baseURL: https://dev.azure.com/{organization}/{project}/_apis/pipelines/checks
    tags:
      - Approvals
      - Checks
      - Pipelines
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/approvalsandchecks/
  - name: Azure DevOps Artifacts Package Types API
    description: API for managing specific package types within Azure Artifacts feeds including NuGet, npm, Maven, Python, and Universal Packages. Provides package-type-specific operations beyond the general Artifacts feed management API.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/artifactspackagetypes/
    baseURL: https://pkgs.dev.azure.com/{organization}/_apis/packaging
    tags:
      - Maven
      - Npm
      - NuGet
      - Packages
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/artifactspackagetypes/
  - name: Azure DevOps Dashboard API
    description: API for creating and managing team dashboards and widgets in Azure DevOps. Each team can have one or more dashboards, and each dashboard contains a set of configurable widgets with multi-user concurrency support via eTag versioning.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/dashboard/
    baseURL: https://dev.azure.com/{organization}/{project}/{team}/_apis/dashboard
    tags:
      - Dashboards
      - Reporting
      - Widgets
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/dashboard/
  - name: Azure DevOps Favorites API
    description: API for managing user favorites in Azure DevOps. Enables programmatic creation, retrieval, and deletion of favorite items such as queries, builds, repositories, and other artifacts scoped to individual users or teams.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/favorite/
    baseURL: https://dev.azure.com/{organization}/_apis/favorite
    tags:
      - Bookmarks
      - Favorites
      - User Preferences
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/favorite/
  - name: Azure DevOps Identities API
    description: API for finding legacy identity descriptors for users and groups in Azure DevOps. Identities can be searched by name, email, ID, identity descriptor, and subject descriptor. Legacy identity descriptors are used by systems that rely on the identity management service, such as the security APIs for permissions management.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/ims/
    baseURL: https://vssps.dev.azure.com/{organization}/_apis/identities
    tags:
      - Groups
      - Identities
      - Users
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/ims/
  - name: Azure DevOps Member Entitlement Management API
    description: API for managing member entitlements in Azure DevOps organizations. A member is a user or group added to an account. Enables programmatic management of licenses, extensions, and project or team memberships for users and groups.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/memberentitlementmanagement/
    baseURL: https://vsaex.dev.azure.com/{organization}/_apis/userentitlements
    tags:
      - Entitlements
      - Licensing
      - User Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/memberentitlementmanagement/
  - name: Azure DevOps Permissions Report API
    description: API for generating and downloading permissions reports that help administrators determine the effective permissions of users and groups on securable resources in Azure DevOps. Reports list effective permissions for each user and group in the organization, accounting for directly assigned, group hierarchy inherited, and resource hierarchy inherited permissions.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/permissionsreport/
    baseURL: https://dev.azure.com/{organization}/_apis/permissionsreport
    tags:
      - Compliance
      - Permissions
      - Reports
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/permissionsreport/
  - name: Azure DevOps Profile API
    description: API for retrieving the authenticated user's profile information in Azure DevOps. Each person using Azure DevOps Services has a profile containing their identity and preference data.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/profile/
    baseURL: https://app.vssps.visualstudio.com/_apis/profile/profiles
    tags:
      - Identity
      - Profile
      - Users
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/profile/
  - name: Azure DevOps Security Roles API
    description: API for managing security role definitions and role assignments on Azure DevOps resources. Enables listing role definitions, assigning roles to identities on specific resources, removing role assignments, and managing permission inheritance.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/securityroles/
    baseURL: https://dev.azure.com/{organization}/_apis/securityroles
    tags:
      - Access Control
      - Role Assignments
      - Security Roles
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/securityroles/
  - name: Azure DevOps Status API
    description: API for querying the health and status of Azure DevOps services. Provides the ability to query status information for Azure DevOps all-up, or scoped to a specific service and geography. Results are cached for 60 seconds.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/status/
    baseURL: https://status.dev.azure.com/_apis/status
    tags:
      - Health
      - Monitoring
      - Status
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/status/
  - name: Azure DevOps Symbol API
    description: API for working with the Azure DevOps managed Symbol Service. Supports creating and managing symbol requests, updating debug entries, querying symbols via the Microsoft SymSrv protocol, and checking service availability. Used to publish and consume debug symbols for builds.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/symbol/
    baseURL: https://artifacts.dev.azure.com/{organization}/_apis/symbol
    tags:
      - Artifacts
      - Debugging
      - Symbols
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/symbol/
  - name: Azure DevOps Test Plan API
    description: API for managing modern test plans, test suites, test cases, test points, and test configurations in Azure DevOps. Provides programmatic access to test plan management operations including cloning, recycle bin operations, and test suite organization.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/testplan/
    baseURL: https://dev.azure.com/{organization}/{project}/_apis/testplan
    tags:
      - Test Cases
      - Test Plans
      - Test Suites
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/testplan/
  - name: Azure DevOps Test Results API
    description: API for managing test results, code coverage data, test run logs, and test result metrics in Azure DevOps. Supports publishing test result documents, querying results by build or pipeline, and retrieving detailed test result group information.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/testresults/
    baseURL: https://vstmr.dev.azure.com/{organization}/{project}/_apis/testresults
    tags:
      - Code Coverage
      - Test Results
      - Test Runs
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/testresults/
  - name: Azure DevOps Token Lifecycle Management API
    description: API for users to manage the lifecycle of their own personal access tokens (PATs) in Azure DevOps. Supports creating, listing, updating, and revoking PATs programmatically. Requires authorization with Microsoft Entra ID access tokens.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/tokens/
    baseURL: https://vssps.dev.azure.com/{organization}/_apis/tokens
    tags:
      - Authentication
      - Personal Access Tokens
      - Tokens
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/tokens/
  - name: Azure DevOps Work API
    description: API for managing board configurations, team settings, iterations, capacities, and process configuration in Azure Boards. Provides programmatic access to board columns, rows, card styling rules, chart settings, team field values, backlog settings, and sprint capacity planning.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/work/
    baseURL: https://dev.azure.com/{organization}/{project}/{team}/_apis/work
    tags:
      - Boards
      - Capacity
      - Sprints
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/work/
  - name: Azure DevOps Work Item Tracking Process API
    description: API for managing work item tracking process customizations in Azure DevOps. Enables programmatic management of inherited processes, work item types, fields, states, rules, behaviors, layouts, and picklist values for customizing Azure Boards experiences.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/processes/
    baseURL: https://dev.azure.com/{organization}/_apis/work/processes
    tags:
      - Customization
      - Processes
      - Work Item Types
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/processes/
common:
  - type: Portal
    url: https://dev.azure.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/devops/?view=azure-devops
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance
  - type: Client Libraries
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/dotnet-client-libraries?view=azure-devops
  - type: Rate Limits
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/rate-limits
  - type: Status
    url: https://status.dev.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/devops/
  - type: Blog
    url: https://devblogs.microsoft.com/devops/
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/services/devops/
  - type: Community
    url: https://developercommunity.visualstudio.com/AzureDevOps
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/azure-devops
  - type: Change Log
    url: https://learn.microsoft.com/en-us/azure/devops/release-notes/
  - type: Marketplace
    url: https://marketplace.visualstudio.com/azuredevops
  - type: Extensions
    url: https://learn.microsoft.com/en-us/azure/devops/extend/overview?view=azure-devops
  - type: CLI
    url: https://learn.microsoft.com/en-us/azure/devops/cli/?view=azure-devops
  - type: Versioning
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/rest-api-versioning?view=azure-devops
  - type: Samples
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/rest/samples?view=azure-devops
  - type: Best Practices
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/integration-bestpractices?view=azure-devops
  - type: GitHub Organization
    url: https://github.com/microsoft
  - type: GitHubRepository
    url: https://github.com/microsoft/azure-devops-python-api
  - type: GitHubRepository
    url: https://github.com/microsoft/azure-devops-node-api
  - type: GitHubRepository
    url: https://github.com/microsoft/azure-devops-extension-sdk
  - type: JSONSchema
    url: json-schema/azure-devops-work-item-schema.json
  - type: JSONSchema
    url: json-schema/azure-devops-pipeline-run-schema.json
  - type: JSON-LD
    url: json-ld/azure-devops-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
