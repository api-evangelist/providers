---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Microsoft Azure Devops Agentic Access
  operation_count: 93
  slug: microsoft-azure-devops-agentic-access
  summary_line: 93 operations · 43 acting
api_count: 62
apis:
- description: API for managing users, groups, and memberships within an Azure DevOps organization. Enables programmatic administration of identities and group membership.
  name: Azure DevOps Graph API
  slug: azure-devops-graph-api
- description: API for managing Azure DevOps projects, teams, and team members. Provides foundational access to the organizational structure of an Azure DevOps organization.
  name: Azure DevOps Core API
  slug: azure-devops-core-api
- description: API for managing security namespaces, access control lists, and access control entries in Azure DevOps. Used to programmatically set and evaluate permissions on resources.
  name: Azure DevOps Security API
  slug: azure-devops-security-api
- description: API for managing notification subscriptions for users and teams. Enables programmatic creation and management of email and other notification channels for Azure DevOps events such as work item changes
  name: Azure DevOps Notifications API
  slug: azure-devops-notifications-api
- description: API for querying and downloading the Azure DevOps audit log. Provides access to auditable events within an organization for security reviews and compliance reporting.
  name: Azure DevOps Audit API
  slug: azure-devops-audit-api
- description: API for searching code, work items, and wiki pages across all projects and repositories within an Azure DevOps organization. Supports full-text and filtered search results.
  name: Azure DevOps Search API
  slug: azure-devops-search-api
- description: API for managing code policy configurations and policy types in Azure Repos. Used to define and enforce branch policies such as required reviewers, status checks, and merge strategies.
  name: Azure DevOps Policy API
  slug: azure-devops-policy-api
- description: API for managing the pipeline agent infrastructure including agent pools, queues, agents, environments, deployment groups, and task groups. Provides programmatic control over the compute resources use
  name: Azure DevOps Distributed Task API
  slug: azure-devops-distributed-task-api
- description: OData-based API providing access to the Azure DevOps Analytics service for reporting and querying historical and real-time project data. Supports queries across work items, pipelines, and test plans f
  name: Azure DevOps Analytics OData API
  slug: azure-devops-analytics-odata-api
- description: API for managing extensions installed in an Azure DevOps organization. Enables programmatic listing, installing, updating, and removing of Marketplace extensions, as well as reading extension data and
  name: Azure DevOps Extension Management API
  slug: azure-devops-extension-management-api
- description: API for managing service connections that connect Azure DevOps pipelines to external services such as GitHub, Docker, Azure, and other third-party providers. Supports creating, updating, and sharing s
  name: Azure DevOps Service Endpoint API
  slug: azure-devops-service-endpoint-api
- description: API for accessing Team Foundation Version Control (TFVC) repositories within Azure DevOps. Provides programmatic access to TFVC items, changesets, shelvesets, labels, and branches for organizations us
  name: Azure DevOps TFVC API
  slug: azure-devops-tfvc-api
- description: API for organization administrators to retrieve and revoke OAuth authorizations including personal access tokens and session tokens for users in their organizations. Enables centralized token governan
  name: Azure DevOps Token Administration API
  slug: azure-devops-token-administration-api
- description: API for listing the Azure DevOps organizations that the authenticated user has access to. Each person using Azure DevOps Services has access to one or more organization accounts.
  name: Azure DevOps Accounts API
  slug: azure-devops-accounts-api
- description: API for managing pipeline approvals and checks on resources such as environments, service connections, agent pools, variable groups, and secure files. Enables programmatic creation and modification of
  name: Azure DevOps Approvals and Checks API
  slug: azure-devops-approvals-and-checks-api
- description: API for managing specific package types within Azure Artifacts feeds including NuGet, npm, Maven, Python, and Universal Packages. Provides package-type-specific operations beyond the general Artifacts
  name: Azure DevOps Artifacts Package Types API
  slug: azure-devops-artifacts-package-types-api
- description: API for creating and managing team dashboards and widgets in Azure DevOps. Each team can have one or more dashboards, and each dashboard contains a set of configurable widgets with multi-user concurre
  name: Azure DevOps Dashboard API
  slug: azure-devops-dashboard-api
- description: API for managing user favorites in Azure DevOps. Enables programmatic creation, retrieval, and deletion of favorite items such as queries, builds, repositories, and other artifacts scoped to individua
  name: Azure DevOps Favorites API
  slug: azure-devops-favorites-api
- description: API for finding legacy identity descriptors for users and groups in Azure DevOps. Identities can be searched by name, email, ID, identity descriptor, and subject descriptor. Legacy identity descriptor
  name: Azure DevOps Identities API
  slug: azure-devops-identities-api
- description: API for managing member entitlements in Azure DevOps organizations. A member is a user or group added to an account. Enables programmatic management of licenses, extensions, and project or team member
  name: Azure DevOps Member Entitlement Management API
  slug: azure-devops-member-entitlement-management-api
- description: API for generating and downloading permissions reports that help administrators determine the effective permissions of users and groups on securable resources in Azure DevOps. Reports list effective p
  name: Azure DevOps Permissions Report API
  slug: azure-devops-permissions-report-api
- description: API for retrieving the authenticated user's profile information in Azure DevOps. Each person using Azure DevOps Services has a profile containing their identity and preference data.
  name: Azure DevOps Profile API
  slug: azure-devops-profile-api
- description: API for managing security role definitions and role assignments on Azure DevOps resources. Enables listing role definitions, assigning roles to identities on specific resources, removing role assignme
  name: Azure DevOps Security Roles API
  slug: azure-devops-security-roles-api
- description: API for querying the health and status of Azure DevOps services. Provides the ability to query status information for Azure DevOps all-up, or scoped to a specific service and geography. Results are ca
  name: Azure DevOps Status API
  slug: azure-devops-status-api
- description: API for working with the Azure DevOps managed Symbol Service. Supports creating and managing symbol requests, updating debug entries, querying symbols via the Microsoft SymSrv protocol, and checking s
  name: Azure DevOps Symbol API
  slug: azure-devops-symbol-api
- description: API for managing modern test plans, test suites, test cases, test points, and test configurations in Azure DevOps. Provides programmatic access to test plan management operations including cloning, re
  name: Azure DevOps Test Plan API
  slug: azure-devops-test-plan-api
- description: API for managing test results, code coverage data, test run logs, and test result metrics in Azure DevOps. Supports publishing test result documents, querying results by build or pipeline, and retriev
  name: Azure DevOps Test Results API
  slug: azure-devops-test-results-api
- description: 'API for users to manage the lifecycle of their own personal access tokens (PATs) in Azure DevOps. Supports creating, listing, updating, and revoking PATs programmatically. Requires authorization with '
  name: Azure DevOps Token Lifecycle Management API
  slug: azure-devops-token-lifecycle-management-api
- description: 'API for managing board configurations, team settings, iterations, capacities, and process configuration in Azure Boards. Provides programmatic access to board columns, rows, card styling rules, chart '
  name: Azure DevOps Work API
  slug: azure-devops-work-api
- description: API for managing work item tracking process customizations in Azure DevOps. Enables programmatic management of inherited processes, work item types, fields, states, rules, behaviors, layouts, and pick
  name: Azure DevOps Work Item Tracking Process API
  slug: azure-devops-work-item-tracking-process-api
- description: Operations for work item attachments
  name: Azure DevOps Attachments API
  slug: microsoft-azure-devops-attachments-api
- description: Operations for accessing build artifacts
  name: Azure DevOps Build Artifacts API
  slug: microsoft-azure-devops-build-artifacts-api
- description: Operations for managing build pipeline definitions
  name: Azure DevOps Build Definitions API
  slug: microsoft-azure-devops-build-definitions-api
- description: Operations for accessing build logs and timelines
  name: Azure DevOps Build Logs API
  slug: microsoft-azure-devops-build-logs-api
- description: Operations for managing and queuing builds
  name: Azure DevOps Builds API
  slug: microsoft-azure-devops-builds-api
- description: Operations for work item comments
  name: Azure DevOps Comments API
  slug: microsoft-azure-devops-comments-api
- description: Operations for accessing commits and commit history
  name: Azure DevOps Commits API
  slug: microsoft-azure-devops-commits-api
- description: Operations for listing consumers (webhook, service bus, etc.)
  name: Azure DevOps Consumers API
  slug: microsoft-azure-devops-consumers-api
- description: Operations for managing and monitoring deployments to environments
  name: Azure DevOps Deployments API
  slug: microsoft-azure-devops-deployments-api
- description: Operations for managing artifact feeds
  name: Azure DevOps Feeds API
  slug: microsoft-azure-devops-feeds-api
- description: Operations for sending test notifications
  name: Azure DevOps Notifications API
  slug: microsoft-azure-devops-notifications-api
- description: Operations for managing specific package versions
  name: Azure DevOps Package Versions API
  slug: microsoft-azure-devops-package-versions-api
- description: Operations for listing and managing packages within feeds
  name: Azure DevOps Packages API
  slug: microsoft-azure-devops-packages-api
- description: Operations for accessing artifacts from pipeline runs
  name: Azure DevOps Pipeline Artifacts API
  slug: microsoft-azure-devops-pipeline-artifacts-api
- description: Operations for triggering and monitoring pipeline runs
  name: Azure DevOps Pipeline Runs API
  slug: microsoft-azure-devops-pipeline-runs-api
- description: Operations for managing pipeline definitions
  name: Azure DevOps Pipelines API
  slug: microsoft-azure-devops-pipelines-api
- description: Operations for listing event publishers and their event types
  name: Azure DevOps Publishers API
  slug: microsoft-azure-devops-publishers-api
- description: Operations for creating and managing pull requests
  name: Azure DevOps Pull Requests API
  slug: microsoft-azure-devops-pull-requests-api
- description: Operations for managing pushes and commits
  name: Azure DevOps Pushes API
  slug: microsoft-azure-devops-pushes-api
- description: Operations for managing branches and tags (refs)
  name: Azure DevOps Refs API
  slug: microsoft-azure-devops-refs-api
- description: Operations for managing release pipeline definitions
  name: Azure DevOps Release Definitions API
  slug: microsoft-azure-devops-release-definitions-api
- description: Operations for managing release instances
  name: Azure DevOps Releases API
  slug: microsoft-azure-devops-releases-api
- description: Operations for managing Git repositories
  name: Azure DevOps Repositories API
  slug: microsoft-azure-devops-repositories-api
- description: Operations for managing service hook subscriptions
  name: Azure DevOps Subscriptions API
  slug: microsoft-azure-devops-subscriptions-api
- description: Operations for managing test cases within test suites
  name: Azure DevOps Test Cases API
  slug: microsoft-azure-devops-test-cases-api
- description: Operations for managing test plans
  name: Azure DevOps Test Plans API
  slug: microsoft-azure-devops-test-plans-api
- description: Operations for managing test suites within test plans
  name: Azure DevOps Test Suites API
  slug: microsoft-azure-devops-test-suites-api
- description: Operations for managing wiki page content
  name: Azure DevOps Wiki Pages API
  slug: microsoft-azure-devops-wiki-pages-api
- description: Operations for managing wiki instances
  name: Azure DevOps Wikis API
  slug: microsoft-azure-devops-wikis-api
- description: Operations for querying and tracking work items using WIQL
  name: Azure DevOps Work Item Tracking API
  slug: microsoft-azure-devops-work-item-tracking-api
- description: Operations for work item type definitions and fields
  name: Azure DevOps Work Item Types API
  slug: microsoft-azure-devops-work-item-types-api
- description: Operations for managing work items (Bugs, Tasks, User Stories, etc.)
  name: Azure DevOps Work Items API
  slug: microsoft-azure-devops-work-items-api
arazzos:
- description: Query a board column with WIQL, fetch the work item type, and acknowledge the top bug.
  name: Azure DevOps Board Bug Acknowledgement
  slug: microsoft-azure-devops-board-bug-comment-workflow
- description: Find the latest succeeded build for a definition, confirm it, and list its artifacts.
  name: Azure DevOps Retrieve Artifacts of the Latest Successful Build
  slug: microsoft-azure-devops-build-artifacts-retrieval-workflow
- description: Create a build definition, confirm it, and queue its first build.
  name: Azure DevOps Provision a Build Definition and Run It
  slug: microsoft-azure-devops-build-definition-provision-workflow
- description: Queue a build, poll until it completes, and fetch its timeline.
  name: Azure DevOps Queue and Monitor a Build
  slug: microsoft-azure-devops-build-queue-monitor-workflow
- description: Resolve the tip of a branch, push a new commit, and confirm the push.
  name: Azure DevOps Commit a File via a Git Push
  slug: microsoft-azure-devops-git-push-commit-workflow
- description: Create a YAML pipeline from a repo file, confirm it, and trigger a run.
  name: Azure DevOps Create a YAML Pipeline and Start Its First Run
  slug: microsoft-azure-devops-pipeline-create-run-workflow
- description: Run a YAML pipeline, poll the run until it finishes, and list its artifacts.
  name: Azure DevOps Run and Monitor a Pipeline
  slug: microsoft-azure-devops-pipeline-run-monitor-workflow
- description: List a project's repositories, pick the first, and inventory its branches and pull requests.
  name: Azure DevOps Project Repository Inventory
  slug: microsoft-azure-devops-project-repository-inventory-workflow
- description: Fetch a pull request, verify it can merge, and complete it.
  name: Azure DevOps Complete a Pull Request
  slug: microsoft-azure-devops-pull-request-complete-workflow
- description: Create a pull request, confirm it, and add an opening review comment thread.
  name: Azure DevOps Open a Pull Request and Start a Review Thread
  slug: microsoft-azure-devops-pull-request-create-comment-workflow
- description: List active pull requests, open the oldest, and add a review comment.
  name: Azure DevOps Review the Oldest Active Pull Request
  slug: microsoft-azure-devops-pull-request-review-cycle-workflow
- description: Create a release from a definition, poll it active, and fetch environments.
  name: Azure DevOps Create and Monitor a Release
  slug: microsoft-azure-devops-release-create-monitor-workflow
- description: Create a release definition, confirm it, and create a first release from it.
  name: Azure DevOps Provision a Release Definition and Cut a Release
  slug: microsoft-azure-devops-release-definition-provision-workflow
- description: Read a release definition, create a release from it, and confirm the release.
  name: Azure DevOps Inspect a Release Definition and Cut a Release
  slug: microsoft-azure-devops-release-from-definition-workflow
- description: Create a Git repository, confirm it, and list its branches.
  name: Azure DevOps Provision and Inspect a Git Repository
  slug: microsoft-azure-devops-repository-provision-init-workflow
- description: Find open bugs with a WIQL query, fetch the top result, and triage it.
  name: Azure DevOps Bug Triage by WIQL Query
  slug: microsoft-azure-devops-work-item-bug-triage-workflow
- description: Create a parent work item, create a child, and link them hierarchically.
  name: Azure DevOps Create a Parent and Linked Child Work Item
  slug: microsoft-azure-devops-work-item-create-linked-child-workflow
- description: Create a work item, transition its state, and append a comment in one flow.
  name: Azure DevOps Create, Update, and Comment on a Work Item
  slug: microsoft-azure-devops-work-item-create-update-comment-workflow
artifact_total: 209
asyncapis:
- description: AsyncAPI specification for Azure DevOps Service Hooks (webhooks and event subscriptions). Azure DevOps delivers event notifications via HTTP POST requests to subscriber endpoints when events occur suc
  name: Azure DevOps Service Hooks AsyncAPI
  slug: azure-devops-service-hooks-asyncapi
collections:
- collection_type: postman
  name: Azure DevOps Artifacts API
  slug: postman-azure-devops-artifacts-api
- collection_type: postman
  name: Azure DevOps Builds API
  slug: postman-azure-devops-builds-api
- collection_type: postman
  name: Azure DevOps Git Repositories API
  slug: postman-azure-devops-git-api
- collection_type: postman
  name: Azure DevOps Pipelines API
  slug: postman-azure-devops-pipelines-api
- collection_type: postman
  name: Azure DevOps Releases API
  slug: postman-azure-devops-releases-api
- collection_type: postman
  name: Azure DevOps Service Hooks API
  slug: postman-azure-devops-service-hooks-api
- collection_type: postman
  name: Azure DevOps Test Plans API
  slug: postman-azure-devops-test-plans-api
- collection_type: postman
  name: Azure DevOps Wiki API
  slug: postman-azure-devops-wiki-api
- collection_type: postman
  name: Azure DevOps Work Items API
  slug: postman-azure-devops-work-items-api
- collection_type: open
  name: Azure DevOps Artifacts API
  slug: open-azure-devops-artifacts-api
- collection_type: open
  name: Azure DevOps Builds API
  slug: open-azure-devops-builds-api
- collection_type: open
  name: Azure DevOps Git Repositories API
  slug: open-azure-devops-git-api
- collection_type: open
  name: Azure DevOps Pipelines API
  slug: open-azure-devops-pipelines-api
- collection_type: open
  name: Azure DevOps Releases API
  slug: open-azure-devops-releases-api
- collection_type: open
  name: Azure DevOps Service Hooks API
  slug: open-azure-devops-service-hooks-api
- collection_type: open
  name: Azure DevOps Test Plans API
  slug: open-azure-devops-test-plans-api
- collection_type: open
  name: Azure DevOps Wiki API
  slug: open-azure-devops-wiki-api
- collection_type: open
  name: Azure DevOps Work Items API
  slug: open-azure-devops-work-items-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-devops-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-devops-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-devops-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-devops/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-board-bug-comment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-build-artifacts-retrieval-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-build-definition-provision-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-build-queue-monitor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-git-push-commit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-pipeline-create-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-pipeline-run-monitor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-project-repository-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-pull-request-complete-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-pull-request-create-comment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-pull-request-review-cycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-release-create-monitor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-release-definition-provision-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-release-from-definition-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-repository-provision-init-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-work-item-bug-triage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-work-item-create-linked-child-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-work-item-create-update-comment-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://dev.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/devops/?view=azure-devops
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance
- group: build
  title: ''
  type: Client Libraries
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/dotnet-client-libraries?view=azure-devops
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/rate-limits
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dev.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/devops/
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/devops/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/services/devops/
- group: operate
  title: ''
  type: Community
  url: https://developercommunity.visualstudio.com/AzureDevOps
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-devops
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/devops/release-notes/
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.visualstudio.com/azuredevops
- group: build
  title: ''
  type: Extensions
  url: https://learn.microsoft.com/en-us/azure/devops/extend/overview?view=azure-devops
- group: build
  title: ''
  type: CLI
  url: https://learn.microsoft.com/en-us/azure/devops/cli/?view=azure-devops
- group: design
  title: ''
  type: Versioning
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/rest-api-versioning?view=azure-devops
- group: build
  title: ''
  type: Samples
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/rest/samples?view=azure-devops
- group: other
  title: ''
  type: Best Practices
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/integration-bestpractices?view=azure-devops
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/azure-devops-python-api
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/azure-devops-node-api
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/azure-devops-extension-sdk
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/azure-devops-work-item-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/azure-devops-pipeline-run-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/azure-devops-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/microsoft/azure-devops-mcp
created: '2024-01-01'
description: Azure DevOps provides developer services for support teams to plan work, collaborate on code development, and build and deploy applications.
examples:
- key_count: 6
  name: Microsoft Azure Devops Builds Queue Example
  slug: microsoft-azure-devops-builds-queue-example
- key_count: 6
  name: Microsoft Azure Devops Feeds Create Example
  slug: microsoft-azure-devops-feeds-create-example
- key_count: 6
  name: Microsoft Azure Devops Notifications Sendtest Example
  slug: microsoft-azure-devops-notifications-sendtest-example
- key_count: 6
  name: Microsoft Azure Devops Pages Createorupdate Example
  slug: microsoft-azure-devops-pages-createorupdate-example
- key_count: 6
  name: Microsoft Azure Devops Pipelines Create Example
  slug: microsoft-azure-devops-pipelines-create-example
- key_count: 6
  name: Microsoft Azure Devops Pullrequests Addcomment Example
  slug: microsoft-azure-devops-pullrequests-addcomment-example
- key_count: 6
  name: Microsoft Azure Devops Pullrequests Create Example
  slug: microsoft-azure-devops-pullrequests-create-example
- key_count: 6
  name: Microsoft Azure Devops Releases Create Example
  slug: microsoft-azure-devops-releases-create-example
- key_count: 6
  name: Microsoft Azure Devops Runs Run Example
  slug: microsoft-azure-devops-runs-run-example
- key_count: 6
  name: Microsoft Azure Devops Subscriptions Create Example
  slug: microsoft-azure-devops-subscriptions-create-example
- key_count: 6
  name: Microsoft Azure Devops Testcases Add Example
  slug: microsoft-azure-devops-testcases-add-example
- key_count: 6
  name: Microsoft Azure Devops Testplans Create Example
  slug: microsoft-azure-devops-testplans-create-example
- key_count: 6
  name: Microsoft Azure Devops Testsuites Create Example
  slug: microsoft-azure-devops-testsuites-create-example
- key_count: 6
  name: Microsoft Azure Devops Wikis Create Example
  slug: microsoft-azure-devops-wikis-create-example
- key_count: 6
  name: Microsoft Azure Devops Wikis Update Example
  slug: microsoft-azure-devops-wikis-update-example
- key_count: 6
  name: Microsoft Azure Devops Workitems Addcomment Example
  slug: microsoft-azure-devops-workitems-addcomment-example
- key_count: 6
  name: Microsoft Azure Devops Workitems Create Example
  slug: microsoft-azure-devops-workitems-create-example
- key_count: 6
  name: Microsoft Azure Devops Workitems Querybywiql Example
  slug: microsoft-azure-devops-workitems-querybywiql-example
- key_count: 6
  name: Microsoft Azure Devops Workitems Update Example
  slug: microsoft-azure-devops-workitems-update-example
finops:
- name: Microsoft Azure Devops Finops
  service_category: DevOps / Developer Tools
  slug: microsoft-azure-devops-finops
image: https://azure.microsoft.com/svghandler/devops/
json_schemas:
- name: Azure DevOps Pipeline Run
  property_count: 12
  slug: azure-devops-pipeline-run
- name: Azure DevOps Work Item
  property_count: 6
  slug: azure-devops-work-item
- name: ApiError
  property_count: 6
  slug: microsoft-azure-devops-apierror
- name: Artifact
  property_count: 4
  slug: microsoft-azure-devops-artifact
- name: AttachmentReference
  property_count: 2
  slug: microsoft-azure-devops-attachmentreference
- name: Build
  property_count: 22
  slug: microsoft-azure-devops-build
- name: BuildArtifact
  property_count: 4
  slug: microsoft-azure-devops-buildartifact
- name: BuildDefinition
  property_count: 17
  slug: microsoft-azure-devops-builddefinition
- name: BuildDefinitionCreateRequest
  property_count: 8
  slug: microsoft-azure-devops-builddefinitioncreaterequest
- name: BuildDefinitionReference
  property_count: 5
  slug: microsoft-azure-devops-builddefinitionreference
- name: BuildLog
  property_count: 6
  slug: microsoft-azure-devops-buildlog
- name: BuildQueueRequest
  property_count: 7
  slug: microsoft-azure-devops-buildqueuerequest
- name: BuildRepository
  property_count: 8
  slug: microsoft-azure-devops-buildrepository
- name: Comment
  property_count: 11
  slug: microsoft-azure-devops-comment
- name: ConfigurationVariableValue
  property_count: 3
  slug: microsoft-azure-devops-configurationvariablevalue
- name: Consumer
  property_count: 8
  slug: microsoft-azure-devops-consumer
- name: ConsumerAction
  property_count: 6
  slug: microsoft-azure-devops-consumeraction
- name: CreatePipelineParameters
  property_count: 3
  slug: microsoft-azure-devops-createpipelineparameters
- name: Deployment
  property_count: 21
  slug: microsoft-azure-devops-deployment
- name: EventType
  property_count: 6
  slug: microsoft-azure-devops-eventtype
- name: EventTypeReference
  property_count: 2
  slug: microsoft-azure-devops-eventtypereference
- name: Feed
  property_count: 13
  slug: microsoft-azure-devops-feed
- name: FeedCreateRequest
  property_count: 6
  slug: microsoft-azure-devops-feedcreaterequest
- name: FeedUpdateRequest
  property_count: 6
  slug: microsoft-azure-devops-feedupdaterequest
- name: FeedView
  property_count: 5
  slug: microsoft-azure-devops-feedview
- name: GitCommitRef
  property_count: 9
  slug: microsoft-azure-devops-gitcommitref
- name: GitItem
  property_count: 10
  slug: microsoft-azure-devops-gititem
- name: GitPullRequest
  property_count: 23
  slug: microsoft-azure-devops-gitpullrequest
- name: GitPullRequestCommentThread
  property_count: 9
  slug: microsoft-azure-devops-gitpullrequestcommentthread
- name: GitPullRequestCommentThreadCreateRequest
  property_count: 3
  slug: microsoft-azure-devops-gitpullrequestcommentthreadcreaterequest
- name: GitPullRequestCreateRequest
  property_count: 8
  slug: microsoft-azure-devops-gitpullrequestcreaterequest
- name: GitPush
  property_count: 7
  slug: microsoft-azure-devops-gitpush
- name: GitPushCreateRequest
  property_count: 2
  slug: microsoft-azure-devops-gitpushcreaterequest
- name: GitRef
  property_count: 5
  slug: microsoft-azure-devops-gitref
- name: GitRefUpdate
  property_count: 4
  slug: microsoft-azure-devops-gitrefupdate
- name: GitRepository
  property_count: 13
  slug: microsoft-azure-devops-gitrepository
- name: GitUserDate
  property_count: 4
  slug: microsoft-azure-devops-gituserdate
- name: IdentityRef
  property_count: 6
  slug: microsoft-azure-devops-identityref
- name: IdentityRefWithVote
  property_count: 5
  slug: microsoft-azure-devops-identityrefwithvote
- name: InputDescriptor
  property_count: 8
  slug: microsoft-azure-devops-inputdescriptor
- name: JsonPatchOperation
  property_count: 4
  slug: microsoft-azure-devops-jsonpatchoperation
- name: NotificationResult
  property_count: 7
  slug: microsoft-azure-devops-notificationresult
- name: Package
  property_count: 7
  slug: microsoft-azure-devops-package
- name: PackageVersion
  property_count: 11
  slug: microsoft-azure-devops-packageversion
- name: Pipeline
  property_count: 7
  slug: microsoft-azure-devops-pipeline
- name: PipelineConfiguration
  property_count: 3
  slug: microsoft-azure-devops-pipelineconfiguration
- name: Publisher
  property_count: 6
  slug: microsoft-azure-devops-publisher
- name: Release
  property_count: 20
  slug: microsoft-azure-devops-release
- name: ReleaseApproval
  property_count: 13
  slug: microsoft-azure-devops-releaseapproval
- name: ReleaseCreateRequest
  property_count: 7
  slug: microsoft-azure-devops-releasecreaterequest
- name: ReleaseDefinition
  property_count: 18
  slug: microsoft-azure-devops-releasedefinition
- name: ReleaseDefinitionEnvironment
  property_count: 10
  slug: microsoft-azure-devops-releasedefinitionenvironment
- name: ReleaseDefinitionShallowReference
  property_count: 5
  slug: microsoft-azure-devops-releasedefinitionshallowreference
- name: ReleaseEnvironment
  property_count: 14
  slug: microsoft-azure-devops-releaseenvironment
- name: Run
  property_count: 12
  slug: microsoft-azure-devops-run
- name: RunPipelineParameters
  property_count: 4
  slug: microsoft-azure-devops-runpipelineparameters
- name: Subscription
  property_count: 15
  slug: microsoft-azure-devops-subscription
- name: SubscriptionCreateRequest
  property_count: 7
  slug: microsoft-azure-devops-subscriptioncreaterequest
- name: TeamProjectReference
  property_count: 7
  slug: microsoft-azure-devops-teamprojectreference
- name: TestCase
  property_count: 4
  slug: microsoft-azure-devops-testcase
- name: TestPlan
  property_count: 19
  slug: microsoft-azure-devops-testplan
- name: TestPlanCreateParams
  property_count: 9
  slug: microsoft-azure-devops-testplancreateparams
- name: TestPlanUpdateParams
  property_count: 11
  slug: microsoft-azure-devops-testplanupdateparams
- name: TestSuite
  property_count: 17
  slug: microsoft-azure-devops-testsuite
- name: TestSuiteCreateParams
  property_count: 6
  slug: microsoft-azure-devops-testsuitecreateparams
- name: TestSuiteReference
  property_count: 3
  slug: microsoft-azure-devops-testsuitereference
- name: Timeline
  property_count: 6
  slug: microsoft-azure-devops-timeline
- name: TimelineRecord
  property_count: 18
  slug: microsoft-azure-devops-timelinerecord
- name: UpstreamSource
  property_count: 7
  slug: microsoft-azure-devops-upstreamsource
- name: WikiCreateParametersV2
  property_count: 6
  slug: microsoft-azure-devops-wikicreateparametersv2
- name: WikiPage
  property_count: 11
  slug: microsoft-azure-devops-wikipage
- name: WikiUpdateParameters
  property_count: 1
  slug: microsoft-azure-devops-wikiupdateparameters
- name: WikiV2
  property_count: 10
  slug: microsoft-azure-devops-wikiv2
- name: WorkItem
  property_count: 6
  slug: microsoft-azure-devops-workitem
- name: WorkItemComment
  property_count: 9
  slug: microsoft-azure-devops-workitemcomment
- name: WorkItemField
  property_count: 12
  slug: microsoft-azure-devops-workitemfield
- name: WorkItemQueryResult
  property_count: 5
  slug: microsoft-azure-devops-workitemqueryresult
- name: WorkItemRelation
  property_count: 3
  slug: microsoft-azure-devops-workitemrelation
- name: WorkItemType
  property_count: 12
  slug: microsoft-azure-devops-workitemtype
- name: WorkItemTypeFieldInstance
  property_count: 8
  slug: microsoft-azure-devops-workitemtypefieldinstance
json_structures:
- name: Microsoft Azure Devops Structure
  property_count: 0
  slug: microsoft-azure-devops-structure
jsonld:
- class_count: 0
  name: Azure Devops Context
  property_count: 15
  slug: azure-devops-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Azure DevOps
nav: Providers
network: true
overview: 'Azure DevOps publishes 32 APIs on the [APIs.io](https://apis.io/) network, including Attachments API, Build Artifacts API, Build Definitions API, and 29 more. Tagged areas include Agile, CI/CD, DevOps, Project Management, and Version Control.


  The Azure DevOps catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Azure DevOps'' developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, pricing, and 45 more developer resources.'
plans:
- name: Microsoft Azure Devops Plans Pricing
  plan_count: 6
  slug: microsoft-azure-devops-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 3
  name: Microsoft Azure Devops Rate Limits
  slug: microsoft-azure-devops-rate-limits
rules:
- name: Azure DevOps API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: microsoft-azure-devops-asyncapi-spectral-rules
- name: Azure DevOps API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-azure-devops-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 69.0
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 81.6
    developer_ergonomics: 65.2
    discoverability: 66.7
    governance: 47.9
    operational_transparency: 68.4
  previous_composite: 69.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 32
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/screenshots/microsoft-azure-devops-2026-06-20T185413.png
security:
- kind: authentication
  name: Microsoft Azure Devops Authentication
  slug: microsoft-azure-devops-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Microsoft Azure Devops Domain Security
  slug: microsoft-azure-devops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-devops
tags:
- Agile
- CI/CD
- DevOps
- Project Management
- Version Control
website: https://dev.azure.com
---
