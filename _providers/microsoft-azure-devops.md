---
access_model:
  confidence: medium
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://dev.azure.com'', ''status'': 302, ''note'': ''declared website redirects to https://azure.microsoft.com/en-us/products/devops/?nav=min — a different registrable domain (azure.com -> microsoft.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: true
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
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Microsoft Azure Devops Agentic Access
  operation_count: 93
  slug: microsoft-azure-devops-agentic-access
  summary_line: 93 operations · 43 acting
api_count: 11
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
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for work item attachments
  name: Azure DevOps Attachments API
  phrasing_intents:
  - id: attachments_get
    intent: Get a work item attachment's details
    question: Where do I find the download URL for a file attached to a work item?
  - id: attachments_upload
    intent: Upload a file as a work item attachment
    question: How do I upload a file so I can attach it to an Azure Boards work item?
  phrasing_ops: 2
  slug: microsoft-azure-devops-attachments-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for accessing build artifacts
  name: Azure DevOps Build Artifacts API
  phrasing_intents:
  - id: builds_listArtifacts
    intent: List the artifacts a build published
    question: Which artifacts did a particular build publish in Azure DevOps?
  phrasing_ops: 1
  slug: microsoft-azure-devops-build-artifacts-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing build pipeline definitions
  name: Azure DevOps Build Definitions API
  phrasing_intents:
  - id: definitions_list
    intent: List build definitions
    question: What build pipeline definitions exist in my Azure DevOps project?
  - id: definitions_create
    intent: Create a build definition
    question: How do I set up a new classic build definition with its repository, process and agent queue?
  - id: definitions_get
    intent: Get a build definition's configuration
    question: Where can I see the steps, triggers and variables configured on one build definition?
  - id: definitions_update
    intent: Replace a build definition
    question: How do I change the triggers or variables on an existing build definition?
  - id: definitions_delete
    intent: Delete a build definition
    question: Can I remove a build definition that I no longer use?
  phrasing_ops: 5
  slug: microsoft-azure-devops-build-definitions-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for accessing build logs and timelines
  name: Azure DevOps Build Logs API
  phrasing_intents:
  - id: builds_getLogs
    intent: List the log files of a build
    question: Where can I get the logs for each step of a build?
  - id: builds_getTimeline
    intent: Get a build's timeline of jobs and tasks
    question: Which task in a build failed and how long did each phase take?
  phrasing_ops: 2
  slug: microsoft-azure-devops-build-logs-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing and queuing builds
  name: Azure DevOps Builds API
  phrasing_intents:
  - id: builds_list
    intent: List builds
    question: Which builds failed on the main branch recently?
  - id: builds_queue
    intent: Queue a new build
    question: How do I kick off a build of a specific definition on a chosen branch?
  - id: builds_get
    intent: Get a build's status and result
    question: Did a particular build succeed, and how long did it take?
  - id: builds_delete
    intent: Delete a build
    question: Can I delete a build record together with its logs and artifacts?
  phrasing_ops: 4
  slug: microsoft-azure-devops-builds-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for work item comments
  name: Azure DevOps Comments API
  phrasing_intents:
  - id: workItems_listComments
    intent: List comments on a work item
    question: What discussion has happened on a bug or task in Azure Boards?
  - id: workItems_addComment
    intent: Add a comment to a work item
    question: How do I post a note to a work item's discussion?
  phrasing_ops: 2
  slug: microsoft-azure-devops-comments-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for accessing commits and commit history
  name: Azure DevOps Commits API
  phrasing_intents:
  - id: commits_list
    intent: List commits in a repository
    question: What commits were made to a repo between two dates?
  phrasing_ops: 1
  slug: microsoft-azure-devops-commits-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for listing consumers (webhook, service bus, etc.)
  name: Azure DevOps Consumers API
  phrasing_intents:
  - id: consumers_list
    intent: List service hook consumers
    question: What services can receive Azure DevOps service hook notifications?
  phrasing_ops: 1
  slug: microsoft-azure-devops-consumers-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing and monitoring deployments to environments
  name: Azure DevOps Deployments API
  phrasing_intents:
  - id: deployments_list
    intent: List release deployments
    question: Which deployments failed to a given environment last week?
  phrasing_ops: 1
  slug: microsoft-azure-devops-deployments-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing artifact feeds
  name: Azure DevOps Feeds API
  phrasing_intents:
  - id: feeds_list
    intent: List package feeds
    question: What Azure Artifacts feeds can I access in my organization?
  - id: feeds_create
    intent: Create a package feed
    question: How do I create a new artifact feed for our packages?
  - id: feeds_get
    intent: Get a feed's configuration
    question: Which upstream sources and visibility settings does a given feed have?
  - id: feeds_update
    intent: Update a feed's settings
    question: How do I rename an existing feed or change its description?
  - id: feeds_delete
    intent: Delete a package feed
    question: Does deleting a feed also remove every package in it?
  phrasing_ops: 5
  slug: microsoft-azure-devops-feeds-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for sending test notifications
  name: Azure DevOps Notifications API
  phrasing_intents:
  - id: notifications_sendTest
    intent: Send a test service hook notification
    question: How can I check that a service hook reaches its endpoint before relying on it?
  phrasing_ops: 1
  slug: microsoft-azure-devops-notifications-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing specific package versions
  name: Azure DevOps Package Versions API
  phrasing_intents:
  - id: packageVersions_delete
    intent: Delete a package version from a feed
    question: Can I remove one bad version of a package without deleting the whole package?
  phrasing_ops: 1
  slug: microsoft-azure-devops-package-versions-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for listing and managing packages within feeds
  name: Azure DevOps Packages API
  phrasing_intents:
  - id: packages_list
    intent: List packages in a feed
    question: What packages are published in one of my Azure Artifacts feeds?
  - id: packages_get
    intent: Get a package and its versions
    question: Which versions of a specific package exist in a feed?
  phrasing_ops: 2
  slug: microsoft-azure-devops-packages-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for accessing artifacts from pipeline runs
  name: Azure DevOps Pipeline Artifacts API
  phrasing_intents:
  - id: artifacts_list
    intent: List artifacts from a pipeline run
    question: What binaries or test results did a pipeline run publish?
  phrasing_ops: 1
  slug: microsoft-azure-devops-pipeline-artifacts-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for triggering and monitoring pipeline runs
  name: Azure DevOps Pipeline Runs API
  phrasing_intents:
  - id: runs_list
    intent: List a pipeline's runs
    question: What recent runs has a YAML pipeline had, and did they pass?
  - id: runs_run
    intent: Start a pipeline run
    question: How do I trigger a YAML pipeline with different template parameters?
  - id: runs_get
    intent: Get a pipeline run's details
    question: What state and result did a specific pipeline run end with?
  phrasing_ops: 3
  slug: microsoft-azure-devops-pipeline-runs-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing pipeline definitions
  name: Azure DevOps Pipelines API
  phrasing_intents:
  - id: pipelines_list
    intent: List pipelines
    question: What YAML pipelines are defined in my Azure DevOps project?
  - id: pipelines_create
    intent: Create a pipeline from a YAML file
    question: How do I register a YAML file in my repo as a new pipeline?
  - id: pipelines_get
    intent: Get a pipeline
    question: Which repository and YAML file does a pipeline point to?
  - id: listPipelines
    intent: List pipelines in a named project
    question: Which pipelines exist in one named project of an organization?
  - id: createPipeline
    intent: Create a pipeline in a named project
    question: How do I add a YAML pipeline to a specific project in a given organization?
  - id: getPipeline
    intent: Get a pipeline in a named project
    question: Where do I look up one pipeline when I know its organization, project and ID?
  phrasing_ops: 6
  slug: microsoft-azure-devops-pipelines-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for listing event publishers and their event types
  name: Azure DevOps Publishers API
  phrasing_intents:
  - id: publishers_list
    intent: List service hook publishers
    question: What event sources can I subscribe to with Azure DevOps service hooks?
  - id: publishers_listEventTypes
    intent: List a publisher's event types
    question: What events, like build completed or code pushed, can a publisher send?
  phrasing_ops: 2
  slug: microsoft-azure-devops-publishers-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for creating and managing pull requests
  name: Azure DevOps Pull Requests API
  phrasing_intents:
  - id: pullRequests_list
    intent: List pull requests in a repository
    question: Which pull requests are still open against main in a repository?
  - id: pullRequests_create
    intent: Open a pull request
    question: How do I open a pull request from my feature branch into main?
  - id: pullRequests_get
    intent: Get a pull request
    question: What is the merge status and reviewer vote on a specific pull request?
  - id: pullRequests_update
    intent: Update, complete or abandon a pull request
    question: How do I abandon or complete an existing pull request?
  - id: pullRequests_listThreads
    intent: List a pull request's comment threads
    question: What review comments have been left on a pull request?
  - id: pullRequests_addComment
    intent: Start a comment thread on a pull request
    question: How do I leave a review comment on a specific file in a pull request?
  phrasing_ops: 6
  slug: microsoft-azure-devops-pull-requests-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing pushes and commits
  name: Azure DevOps Pushes API
  phrasing_intents:
  - id: pushes_list
    intent: List pushes to a repository
    question: Who pushed to a branch and when?
  - id: pushes_create
    intent: Push commits with file changes
    question: How do I commit a file change to an Azure Repos branch without cloning it?
  phrasing_ops: 2
  slug: microsoft-azure-devops-pushes-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing branches and tags (refs)
  name: Azure DevOps Refs API
  phrasing_intents:
  - id: refs_list
    intent: List branches and tags
    question: What branches exist in an Azure Repos repository?
  phrasing_ops: 1
  slug: microsoft-azure-devops-refs-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing release pipeline definitions
  name: Azure DevOps Release Definitions API
  phrasing_intents:
  - id: releaseDefinitions_list
    intent: List release definitions
    question: What classic release pipelines are defined in my project?
  - id: releaseDefinitions_create
    intent: Create a release definition
    question: How do I set up a new classic release pipeline with its environments and artifacts?
  - id: releaseDefinitions_get
    intent: Get a release definition
    question: Which environments and artifact sources does a release definition use?
  - id: releaseDefinitions_update
    intent: Replace a release definition
    question: How do I change the environments of an existing release definition?
  - id: releaseDefinitions_delete
    intent: Delete a release definition
    question: Can I delete a release definition that still has releases?
  phrasing_ops: 5
  slug: microsoft-azure-devops-release-definitions-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing release instances
  name: Azure DevOps Releases API
  phrasing_intents:
  - id: releases_list
    intent: List releases
    question: Which releases were created for a release definition this month?
  - id: releases_create
    intent: Create a release
    question: How do I start a new release from a release definition?
  - id: releases_get
    intent: Get a release
    question: What is the deployment status of each environment in a release?
  - id: releases_update
    intent: Update a release
    question: How do I move a draft release to active?
  phrasing_ops: 4
  slug: microsoft-azure-devops-releases-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing Git repositories
  name: Azure DevOps Repositories API
  phrasing_intents:
  - id: repositories_list
    intent: List Git repositories
    question: What Git repositories are in my Azure DevOps project?
  - id: repositories_create
    intent: Create a Git repository
    question: How do I create a new Git repo in a project?
  - id: repositories_get
    intent: Get a repository
    question: What is the default branch and clone URL of a repository?
  - id: repositories_update
    intent: Rename or reconfigure a repository
    question: How do I rename a Git repository or change its default branch?
  - id: repositories_delete
    intent: Delete a repository
    question: Does deleting a repository also delete its pull requests?
  - id: items_list
    intent: Browse files and folders in a repository
    question: How do I see the files in a folder of a repo at a certain branch?
  phrasing_ops: 6
  slug: microsoft-azure-devops-repositories-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing service hook subscriptions
  name: Azure DevOps Subscriptions API
  phrasing_intents:
  - id: subscriptions_list
    intent: List service hook subscriptions
    question: What service hooks are set up in my Azure DevOps organization?
  - id: subscriptions_create
    intent: Create a service hook subscription
    question: How do I send a webhook to my endpoint whenever code is pushed?
  - id: subscriptions_get
    intent: Get a service hook subscription
    question: What endpoint and filters does a given service hook use?
  - id: subscriptions_update
    intent: Update a service hook subscription
    question: Can I change the URL an existing service hook posts to?
  - id: subscriptions_delete
    intent: Delete a service hook subscription
    question: How do I stop a service hook from sending notifications?
  phrasing_ops: 5
  slug: microsoft-azure-devops-subscriptions-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing test cases within test suites
  name: Azure DevOps Test Cases API
  phrasing_intents:
  - id: testCases_list
    intent: List test cases in a test suite
    question: Which test cases belong to a given test suite?
  - id: testCases_add
    intent: Add existing test cases to a suite
    question: How do I put existing Test Case work items into a test suite?
  phrasing_ops: 2
  slug: microsoft-azure-devops-test-cases-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing test plans
  name: Azure DevOps Test Plans API
  phrasing_intents:
  - id: testPlans_list
    intent: List test plans
    question: What test plans exist in my Azure DevOps project?
  - id: testPlans_create
    intent: Create a test plan
    question: How do I create a test plan for a sprint?
  - id: testPlans_get
    intent: Get a test plan
    question: Who owns a test plan and what iteration does it cover?
  - id: testPlans_update
    intent: Update a test plan
    question: How do I extend the end date of an existing test plan?
  - id: testPlans_delete
    intent: Delete a test plan
    question: Does deleting a test plan remove its suites too?
  phrasing_ops: 5
  slug: microsoft-azure-devops-test-plans-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing test suites within test plans
  name: Azure DevOps Test Suites API
  phrasing_intents:
  - id: testSuites_list
    intent: List test suites in a test plan
    question: What test suites are in a test plan?
  - id: testSuites_create
    intent: Create a test suite
    question: How do I add a requirement-based suite to a test plan?
  - id: testSuites_get
    intent: Get a test suite
    question: What type is a test suite and which suite is its parent?
  phrasing_ops: 3
  slug: microsoft-azure-devops-test-suites-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing wiki page content
  name: Azure DevOps Wiki Pages API
  phrasing_intents:
  - id: pages_get
    intent: Read a wiki page
    question: How do I get the Markdown of a wiki page by its path?
  - id: pages_createOrUpdate
    intent: Create or update a wiki page
    question: How do I publish a new page to a project wiki?
  - id: pages_delete
    intent: Delete a wiki page
    question: Can I remove a page from a wiki?
  phrasing_ops: 3
  slug: microsoft-azure-devops-wiki-pages-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing wiki instances
  name: Azure DevOps Wikis API
  phrasing_intents:
  - id: wikis_list
    intent: List wikis in a project
    question: What wikis does my Azure DevOps project have?
  - id: wikis_create
    intent: Create a wiki
    question: How do I publish a folder from a repo as a code wiki?
  - id: wikis_get
    intent: Get a wiki
    question: Which repository and mapped path back a given wiki?
  - id: wikis_update
    intent: Change a code wiki's branch
    question: How do I point a code wiki at a renamed main branch?
  - id: wikis_delete
    intent: Delete a wiki
    question: Does deleting a project wiki also delete its Git repository?
  phrasing_ops: 5
  slug: microsoft-azure-devops-wikis-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for querying and tracking work items using WIQL
  name: Azure DevOps Work Item Tracking API
  phrasing_intents:
  - id: workItems_queryByWiql
    intent: Run a WIQL query for work items
    question: What is the way to find work items with a query language in Azure Boards?
  phrasing_ops: 1
  slug: microsoft-azure-devops-work-item-tracking-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for work item type definitions and fields
  name: Azure DevOps Work Item Types API
  phrasing_intents:
  - id: workItemTypes_list
    intent: List work item types
    question: What work item types, like Bug or Epic, does my project use?
  - id: workItemTypes_get
    intent: Get a work item type's fields and states
    question: What states and transitions does the Bug type allow?
  - id: fields_list
    intent: List work item fields
    question: What custom fields exist for work items?
  phrasing_ops: 3
  slug: microsoft-azure-devops-work-item-types-api
- baseURL: https://dev.azure.com/{organization}
  baseurl_source: declared
  description: Operations for managing work items (Bugs, Tasks, User Stories, etc.)
  name: Azure DevOps Work Items API
  phrasing_intents:
  - id: workItems_list
    intent: Get several work items by ID
    question: How do I fetch a batch of work items when I know their IDs?
  - id: workItems_create
    intent: Create a work item
    question: How do I file a new bug in Azure Boards?
  - id: workItems_get
    intent: Get a work item
    question: What is the current state of a work item?
  - id: workItems_update
    intent: Update a work item
    question: How do I change a work item's state or assignee?
  - id: workItems_delete
    intent: Delete a work item
    question: Can a deleted work item be restored from the recycle bin?
  - id: getWorkItem
    intent: Get a work item in a project
    question: What is the status of a work item in a specific project?
  - id: updateWorkItem
    intent: Update a work item in a project
    question: How do I change fields or links on a work item?
  - id: createWorkItem
    intent: Create a work item in a project
    question: How do I create a new task in a specific project?
  phrasing_ops: 9
  slug: microsoft-azure-devops-work-items-api
- description: The Azure DevOps Artifacts API provides REST endpoints for managing package feeds including NuGet, npm, Maven, Python, and Universal Packages. APIs support feed creation, package publishing, version m
  name: Azure DevOps Artifacts API
  slug: azure-devops-artifacts-api
- description: The Azure DevOps Release API provides REST endpoints for managing release pipelines, deployments, and environments. APIs support release definition management, deployment approvals, environment config
  name: Azure DevOps Release API
  slug: azure-devops-release-api
- baseURL: https://vssps.dev.azure.com/{organization}/_apis/graph
  baseurl_source: declared
  description: Work item field definitions
  name: Azure DevOps Fields API
  phrasing_intents:
  - id: listWorkItemFields
    intent: List work item fields in a project
    question: What work item fields are defined in an Azure DevOps project?
  phrasing_ops: 1
  slug: microsoft-azure-devops-fields-api
- baseURL: https://vssps.dev.azure.com/{organization}/_apis/graph
  baseurl_source: declared
  description: Work item query execution
  name: Azure DevOps Queries API
  phrasing_intents:
  - id: queryWorkItemsByWiql
    intent: Find work items with a WIQL query
    question: How do I find all active bugs assigned to me in a project?
  phrasing_ops: 1
  slug: microsoft-azure-devops-queries-api
- baseURL: https://vssps.dev.azure.com/{organization}/_apis/graph
  baseurl_source: declared
  description: Pipeline run execution and monitoring
  name: Azure DevOps Runs API
  phrasing_intents:
  - id: listPipelineRuns
    intent: List runs of a pipeline
    question: What runs has a pipeline had in a given project?
  - id: runPipeline
    intent: Trigger a pipeline run
    question: How do I start a pipeline run with custom variables?
  - id: getPipelineRun
    intent: Get one pipeline run
    question: Did a specific pipeline run succeed?
  phrasing_ops: 3
  slug: microsoft-azure-devops-runs-api
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
artifact_total: 251
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
  name: API Collection
  slug: open-.refine-report
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
- collection_type: open
  name: Azure DevOps Artifacts Attachments API
  slug: open-microsoft-azure-devops-attachments-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Build Artifacts API
  slug: open-microsoft-azure-devops-build-artifacts-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Build Definitions API
  slug: open-microsoft-azure-devops-build-definitions-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Build Logs API
  slug: open-microsoft-azure-devops-build-logs-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Builds API
  slug: open-microsoft-azure-devops-builds-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Comments API
  slug: open-microsoft-azure-devops-comments-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Commits API
  slug: open-microsoft-azure-devops-commits-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Consumers API
  slug: open-microsoft-azure-devops-consumers-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Deployments API
  slug: open-microsoft-azure-devops-deployments-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Feeds API
  slug: open-microsoft-azure-devops-feeds-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Notifications API
  slug: open-microsoft-azure-devops-notifications-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Package Versions API
  slug: open-microsoft-azure-devops-package-versions-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Packages API
  slug: open-microsoft-azure-devops-packages-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Pipeline Artifacts API
  slug: open-microsoft-azure-devops-pipeline-artifacts-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Pipeline Runs API
  slug: open-microsoft-azure-devops-pipeline-runs-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Pipelines API
  slug: open-microsoft-azure-devops-pipelines-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Publishers API
  slug: open-microsoft-azure-devops-publishers-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Pull Requests API
  slug: open-microsoft-azure-devops-pull-requests-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Pushes API
  slug: open-microsoft-azure-devops-pushes-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Refs API
  slug: open-microsoft-azure-devops-refs-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Release Definitions API
  slug: open-microsoft-azure-devops-release-definitions-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Releases API
  slug: open-microsoft-azure-devops-releases-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Repositories API
  slug: open-microsoft-azure-devops-repositories-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Subscriptions API
  slug: open-microsoft-azure-devops-subscriptions-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Test Cases API
  slug: open-microsoft-azure-devops-test-cases-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Test Plans API
  slug: open-microsoft-azure-devops-test-plans-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Test Suites API
  slug: open-microsoft-azure-devops-test-suites-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Wiki Pages API
  slug: open-microsoft-azure-devops-wiki-pages-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Wikis API
  slug: open-microsoft-azure-devops-wikis-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Work Item Tracking API
  slug: open-microsoft-azure-devops-work-item-tracking-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Work Item Types API
  slug: open-microsoft-azure-devops-work-item-types-api
- collection_type: open
  name: Azure DevOps Artifacts Attachments Work Items API
  slug: open-microsoft-azure-devops-work-items-api
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/rate-limits/microsoft-azure-devops-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-devops-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/plans/microsoft-azure-devops-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-devops-plans-pricing.yml
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/azure-dev-ops/refs/heads/main/rules/azure-dev-ops-spectral-rules.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/security/microsoft-azure-devops-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-devops-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/scopes/microsoft-azure-devops-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-devops-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/microsoft-azure-devops
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.2
- group: build
  title: ''
  type: SDKs
  url: https://github.com/microsoft/azure-devops-node-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/microsoft/azure-devops-python-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/microsoft/azure-devops-go-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/microsoft/azure-devops-java-api
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/openapi/_original/microsoft-azure-devops-work-items-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/microsoft-azure-devops-work-items-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/openapi/_original/microsoft-azure-devops-pipelines-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/microsoft-azure-devops-pipelines-openapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/vocabulary/microsoft-azure-devops-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-devops-vocabulary.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/rules/microsoft-azure-devops-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/microsoft-azure-devops-spectral-rules.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/capabilities/microsoft-azure-devops-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-devops-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/microsoft/azure-devops-python-api/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/microsoft/azure-devops-python-api/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/microsoft/azure-devops-python-api/blob/dev/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/microsoft/.github/blob/main/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/microsoft/azure-devops-python-api/blob/dev/LICENSE
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/agentic-access/microsoft-azure-devops-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-devops-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/security/microsoft-azure-devops-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-devops-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/authentication/microsoft-azure-devops-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-devops-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-devops/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-board-bug-comment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-board-bug-comment-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-build-artifacts-retrieval-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-build-artifacts-retrieval-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-build-definition-provision-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-build-definition-provision-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-build-queue-monitor-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-build-queue-monitor-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-git-push-commit-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-git-push-commit-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-pipeline-create-run-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-pipeline-create-run-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-pipeline-run-monitor-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-pipeline-run-monitor-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-project-repository-inventory-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-project-repository-inventory-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-pull-request-complete-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-pull-request-complete-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-pull-request-create-comment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-pull-request-create-comment-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-pull-request-review-cycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-pull-request-review-cycle-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-release-create-monitor-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-release-create-monitor-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-release-definition-provision-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-release-definition-provision-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-release-from-definition-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-release-from-definition-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-repository-provision-init-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-repository-provision-init-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-work-item-bug-triage-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-work-item-bug-triage-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-work-item-create-linked-child-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-devops-work-item-create-linked-child-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/arazzo/microsoft-azure-devops-work-item-create-update-comment-workflow.yml
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
  type: Examples
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
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/json-schema/azure-devops-work-item-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/azure-devops-work-item-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/json-schema/azure-devops-pipeline-run-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/azure-devops-pipeline-run-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-devops/refs/heads/main/json-ld/azure-devops-context.jsonld
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
overview: 'Azure DevOps publishes 67 APIs on the [APIs.io](https://apis.io/) network, including Attachments API, Build Artifacts API, Build Definitions API, and 64 more. Tagged areas include Agile, CI/CD, Developer Tools, DevOps, and Project Management.


  The Azure DevOps catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Azure DevOps'' developer surface includes API reference, authentication, developer portal, documentation, getting-started guide, support, engineering blog, and 68 more developer resources.'
plans:
- name: Microsoft Azure Devops Plans Pricing
  plan_count: 7
  slug: microsoft-azure-devops-plans-pricing
- name: Microsoft Azure Devops Price Estimates
  plan_count: 0
  slug: microsoft-azure-devops-price-estimates
random_paper: 14
rate_limits:
- limit_count: 4
  name: Microsoft Azure Devops Rate Limits
  slug: microsoft-azure-devops-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Azure DevOps API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: microsoft-azure-devops-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Azure DevOps API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-azure-devops-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Azure DevOps API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 6
  slug: microsoft-azure-devops-spectral-rules
scopes:
- name: Microsoft Azure Devops Scopes
  scope_count: 4
  slug: microsoft-azure-devops-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 76.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 79.0
    catalog_earned_first_party: 24.0
    catalog_gap: 36.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 84.2
    contract_governance: 27.3
    contract_quality: 71.5
    developer_ergonomics: 82.1
    discoverability: 68.3
    operational_transparency: 76.3
  open_source:
    applies: true
    score: 75.0
  previous_composite: 76.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 22.2
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
- kind: vulnerability-disclosure
  name: Microsoft Azure Devops Vulnerability Disclosure
  slug: microsoft-azure-devops-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-azure-devops
tags:
- Agile
- CI/CD
- Developer Tools
- DevOps
- Project Management
- Version Control
website: https://www.microsoft.com/
---
