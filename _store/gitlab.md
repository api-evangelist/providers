---
aid: gitlab
url: https://raw.githubusercontent.com/api-search/code/main/_apis/gitlab/apis.md
apis:
  - aid: gitlab:gitlab-graphql-api
    name: GitLab GraphQL API
    tags:
      - Data
      - GraphQL
      - Query Language
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/graphql
    humanURL: https://docs.gitlab.com/ee/api/graphql/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/ee/api/graphql/
        type: Documentation
      - url: https://docs.gitlab.com/ee/api/graphql/#deprecation-and-removal-process
        type: Deprecation
      - url: https://docs.gitlab.com/ee/api/graphql/#deprecation-and-removal-process
        type: Documentation
      - url: https://docs.gitlab.com/ee/api/graphql/#limits
        type: RateLimits
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
      - url: https://docs.gitlab.com/api/graphql/reference/
        type: APIReference
      - url: https://docs.gitlab.com/api/graphql/getting_started/
        type: GettingStarted
    description: GraphQL is a query language for APIs. You can use it to request the exact data you need, and therefore limit the number of requests you need. GraphQL data is arranged in types, so your client can use client-side GraphQL libraries to consume the API and avoid manual parsing. There are no fixed endpoints and no data model, so you can add to the API without creating breaking changes. This enables us to have a versionless API.
  - aid: gitlab:apiv4groups
    name: GitLab Groups API
    tags:
      - Access Control
      - Groups
      - Organizations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/groups/
    overlays:
      - url: overlays/gitlab-api-v4-groups-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-groups-openapi-original.yml
        type: OpenAPI
      - url: https://docs.gitlab.com/api/groups/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Groups API allows you to create, read, update, and delete groups and subgroups. Groups are used to manage access control and organize projects within a GitLab instance, enabling teams to collaborate with shared access permissions and settings.
  - aid: gitlab:apiv4projects
    name: GitLab Projects API
    tags:
      - Projects
      - Repositories
      - Source Control
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/projects/
    overlays:
      - url: overlays/gitlab-api-v4-projects-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-projects-openapi-original.yml
        type: OpenAPI
      - url: https://docs.gitlab.com/api/projects/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Projects API provides programmatic access to GitLab projects, enabling you to create, list, update, and delete projects. It supports managing project settings, members, forks, stars, and other project-level resources across GitLab.com and self-managed instances.
  - aid: gitlab:apiv4admin
    name: GitLab Admin API
    tags:
      - Admin
      - Administration
      - Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/admin/
    overlays:
      - url: overlays/gitlab-api-v4-admin-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-admin-openapi-original.yml
        type: OpenAPI
      - url: https://docs.gitlab.com/api/admin/
        type: Documentation
    description: The GitLab Admin API provides administrative endpoints for managing a GitLab instance. It includes operations for managing runners, CI/CD variables, Sidekiq queues, and other instance-level administrative tasks that require administrator privileges.
  - aid: gitlab:apiv4applications
    name: GitLab Applications API
    tags:
      - Applications
      - Authentication
      - OAuth
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/applications/
    overlays:
      - url: overlays/gitlab-api-v4-applications-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-applications-openapi-original.yml
        type: OpenAPI
      - url: https://docs.gitlab.com/api/applications/
        type: Documentation
    description: The GitLab Applications API allows you to manage OAuth applications registered in GitLab. You can create, list, and delete OAuth applications that enable third-party services to access GitLab resources on behalf of users using the OAuth 2.0 protocol.
  - aid: gitlab:apiv4avatar
    name: GitLab Avatar API
    tags:
      - Avatars
      - Profile
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/avatar/
    overlays:
      - url: overlays/gitlab-api-v4-avatar-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-avatar-openapi-original.yml
        type: OpenAPI
      - url: https://docs.gitlab.com/api/avatar/
        type: Documentation
    description: The GitLab Avatar API allows you to retrieve avatar images for users and groups. It returns avatar URLs based on user email addresses, enabling applications to display profile images for GitLab users without requiring authentication.
  - aid: gitlab:apiv4broadcast-messages
    name: GitLab Broadcast Messages API
    tags:
      - Administration
      - Broadcast Messages
      - Notifications
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/broadcast_messages/
    overlays:
      - url: overlays/gitlab-api-v4-broadcast-messages-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-broadcast-messages-openapi-original.yml
        type: OpenAPI
      - url: https://docs.gitlab.com/api/broadcast_messages/
        type: Documentation
    description: The GitLab Broadcast Messages API allows administrators to create and manage broadcast messages that appear as banners across all GitLab pages. These messages are used to communicate announcements, maintenance notices, and other important information to all users of a GitLab instance.
  - aid: gitlab:apiv4bulk-imports
    name: GitLab Bulk Imports API
    tags:
      - Bulk Imports
      - Data Transfer
      - Migration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/bulk_imports/
    overlays:
      - url: overlays/gitlab-api-v4-bulk-imports-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-bulk-imports-openapi-original.yml
        type: OpenAPI
      - url: https://docs.gitlab.com/api/bulk_imports/
        type: Documentation
    description: The GitLab Bulk Imports API enables migration of groups and projects between GitLab instances. It provides endpoints for initiating bulk import operations and tracking their progress, facilitating large-scale data migrations between GitLab environments.
  - aid: gitlab:apiv4application
    name: GitLab Application Settings API
    tags:
      - Administration
      - Application Settings
      - Configuration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/settings/
    overlays:
      - url: overlays/gitlab-api-v4-application-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-application-openapi-original.yml
        type: OpenAPI
      - url: https://docs.gitlab.com/api/settings/
        type: Documentation
    description: The GitLab Application Settings API provides access to instance-wide configuration settings for a GitLab installation. Administrators can retrieve and modify application settings such as sign-up restrictions, default project visibility, and other instance-level preferences.
  - aid: gitlab:apiv4metadata
    name: GitLab Metadata API
    tags:
      - Instance Information
      - Metadata
      - System
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/metadata/
    overlays:
      - url: overlays/gitlab-api-v4-metadata-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-metadata-openapi-original.yml
        type: OpenAPI
      - url: https://docs.gitlab.com/api/metadata/
        type: Documentation
    description: The GitLab Metadata API provides information about the GitLab instance, including the version, revision, and other metadata about the running installation. It is useful for verifying connectivity and identifying the version of a GitLab instance programmatically.
  - aid: gitlab:apiv4version
    name: GitLab Version API
    tags:
      - Instance Information
      - System
      - Version
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/version/
    overlays:
      - url: overlays/gitlab-api-v4-version-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-version-openapi-original.yml
        type: OpenAPI
      - url: https://docs.gitlab.com/api/version/
        type: Documentation
    description: The GitLab Version API returns version and revision information for the GitLab instance. This endpoint is useful for verifying what version of GitLab is running and for checking compatibility with specific API features before making requests.
  - aid: gitlab:gitlab-rest-api
    name: GitLab REST API
    tags:
      - DevOps
      - Integration
      - REST
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/rest/
    overlays: []
    properties:
      - url: openapi/gitlab-openapi-original.yml
        type: OpenAPI
      - url: https://docs.gitlab.com/api/rest/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
      - url: https://docs.gitlab.com/api/rest/third_party_clients/
        type: SDK
      - url: https://docs.gitlab.com/api/api_resources/
        type: APIReference
      - url: https://docs.gitlab.com/security/rate_limits/
        type: RateLimits
      - url: https://docs.gitlab.com/api/openapi/openapi_interactive/
        type: Interactive Documentation
    description: The GitLab REST API provides programmatic access to GitLab resources, enabling you to build integrations, automate repetitive tasks, and extract data for custom reports. The API supports projects, groups, issues, merge requests, CI/CD pipelines, and many other GitLab features through standard HTTP methods and JSON responses.
  - aid: gitlab:gitlab-oauth2-api
    name: GitLab OAuth 2.0 API
    tags:
      - Authentication
      - Authorization
      - OAuth
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com
    humanURL: https://docs.gitlab.com/api/oauth2/
    overlays: []
    properties:
      - url: openapi/gitlab-oauth2-openapi.yml
        type: OpenAPI
      - url: https://docs.gitlab.com/api/oauth2/
        type: Documentation
      - url: https://docs.gitlab.com/integration/oauth_provider/
        type: Authentication
    description: The GitLab OAuth 2.0 API enables third-party services to access GitLab resources on behalf of users using the OAuth 2.0 protocol. It supports authorization code with PKCE, device authorization grant, and resource owner password credentials flows, allowing secure delegation of access to GitLab resources.
  - aid: gitlab:gitlab-webhooks
    name: GitLab Webhooks
    tags:
      - Events
      - Integrations
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/user/project/integrations/webhooks.html
    overlays: []
    properties:
      - url: openapi/gitlab-webhooks-openapi.yml
        type: OpenAPI
      - url: asyncapi/gitlab-webhooks-asyncapi.yml
        type: AsyncAPI
      - url: https://docs.gitlab.com/user/project/integrations/webhooks.html
        type: Documentation
      - url: https://docs.gitlab.com/api/project_webhooks/
        type: APIReference
    description: GitLab Webhooks allow you to receive real-time HTTP POST notifications when events occur in GitLab projects or groups. Webhooks can be configured to trigger on events such as push events, merge requests, issues, comments, and pipeline status changes, enabling integrations with external systems.
  - aid: gitlab:apiv4issues
    name: GitLab Issues API
    tags:
      - Bug Tracking
      - Issues
      - Project Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/issues/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/issues/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Issues API provides programmatic access to manage issues across projects and groups. It supports creating, listing, updating, and deleting issues, as well as managing issue assignments, labels, milestones, and related metadata for tracking work in GitLab.
  - aid: gitlab:apiv4merge-requests
    name: GitLab Merge Requests API
    tags:
      - Code Review
      - Collaboration
      - Merge Requests
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/merge_requests/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/merge_requests/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Merge Requests API enables programmatic management of merge requests across projects and groups. It supports creating, listing, updating, approving, and merging merge requests, as well as managing reviewers, assignees, and merge request metadata for code review workflows.
  - aid: gitlab:apiv4pipelines
    name: GitLab Pipelines API
    tags:
      - CI/CD
      - Continuous Integration
      - Pipelines
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/pipelines/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/pipelines/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Pipelines API provides programmatic access to CI/CD pipelines in GitLab projects. It supports listing, creating, retrying, and canceling pipelines, as well as retrieving pipeline details and variables for automating continuous integration and delivery workflows.
  - aid: gitlab:apiv4jobs
    name: GitLab Jobs API
    tags:
      - Build
      - CI/CD
      - Jobs
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/jobs/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/jobs/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Jobs API allows you to interact with CI/CD jobs in GitLab projects. It supports listing, retrieving, canceling, retrying, and erasing jobs, as well as downloading job artifacts and viewing job logs for build and deployment automation.
  - aid: gitlab:apiv4runners
    name: GitLab Runners API
    tags:
      - CI/CD
      - Infrastructure
      - Runners
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/runners/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/runners/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Runners API provides endpoints for managing CI/CD runners registered to a GitLab instance. It supports listing, registering, updating, and deleting runners, as well as managing runner configurations and viewing jobs assigned to specific runners.
  - aid: gitlab:apiv4users
    name: GitLab Users API
    tags:
      - Access Management
      - Identity
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/users/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/users/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Users API provides programmatic access to manage user accounts on a GitLab instance. It supports listing, creating, updating, and deleting users, managing SSH keys and GPG keys, viewing user activity, and administering user-level settings and permissions.
  - aid: gitlab:apiv4repositories
    name: GitLab Repositories API
    tags:
      - Git
      - Repositories
      - Source Control
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/repositories/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/repositories/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Repositories API provides access to Git repository data within GitLab projects. It supports listing repository tree structures, retrieving file contents, comparing branches and tags, downloading archives, and accessing contributor statistics.
  - aid: gitlab:apiv4commits
    name: GitLab Commits API
    tags:
      - Commits
      - Git
      - Source Control
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/commits/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/commits/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Commits API provides programmatic access to Git commits within GitLab projects. It supports listing, creating, and retrieving commits, viewing commit diffs and comments, cherry-picking commits, and accessing commit status information for CI/CD integration.
  - aid: gitlab:apiv4branches
    name: GitLab Branches API
    tags:
      - Branches
      - Git
      - Source Control
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/branches/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/branches/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Branches API enables programmatic management of Git branches within GitLab projects. It supports listing, creating, and deleting branches, as well as retrieving branch details including the latest commit and protection status.
  - aid: gitlab:apiv4tags
    name: GitLab Tags API
    tags:
      - Git
      - Source Control
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/tags/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/tags/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Tags API provides programmatic access to manage Git tags within GitLab projects. It supports listing, creating, and deleting tags, as well as retrieving tag details for version management and release workflows.
  - aid: gitlab:apiv4releases
    name: GitLab Releases API
    tags:
      - Distribution
      - Releases
      - Versioning
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/releases/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/releases/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Releases API enables programmatic management of project releases. It supports creating, listing, updating, and deleting releases, as well as managing release assets and links for distributing software versions and release notes.
  - aid: gitlab:apiv4environments
    name: GitLab Environments API
    tags:
      - CI/CD
      - Deployments
      - Environments
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/environments/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/environments/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Environments API provides programmatic access to manage deployment environments within GitLab projects. It supports creating, listing, updating, stopping, and deleting environments used to track deployments across different stages such as staging and production.
  - aid: gitlab:apiv4deployments
    name: GitLab Deployments API
    tags:
      - CI/CD
      - Deployments
      - Release Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/deployments/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/deployments/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Deployments API enables programmatic access to deployment records in GitLab projects. It supports listing, creating, and updating deployments, as well as retrieving deployment details and merge requests associated with specific deployments.
  - aid: gitlab:apiv4pipeline-schedules
    name: GitLab Pipeline Schedules API
    tags:
      - Automation
      - CI/CD
      - Pipeline Schedules
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/pipeline_schedules/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/pipeline_schedules/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Pipeline Schedules API provides programmatic access to manage scheduled CI/CD pipelines. It supports creating, listing, updating, and deleting pipeline schedules, as well as managing schedule variables and triggering scheduled pipeline runs.
  - aid: gitlab:apiv4labels
    name: GitLab Labels API
    tags:
      - Labels
      - Organization
      - Project Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/labels/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/labels/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Labels API provides programmatic access to manage project labels. It supports creating, listing, updating, deleting, and subscribing to labels used for categorizing issues, merge requests, and other project resources.
  - aid: gitlab:apiv4milestones
    name: GitLab Milestones API
    tags:
      - Milestones
      - Planning
      - Project Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/milestones/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/milestones/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Milestones API provides programmatic access to manage project milestones. It supports creating, listing, updating, and deleting milestones, as well as retrieving issues and merge requests associated with specific milestones for sprint and release planning.
  - aid: gitlab:apiv4notes
    name: GitLab Notes API
    tags:
      - Collaboration
      - Comments
      - Notes
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/notes/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/notes/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Notes API provides programmatic access to manage comments and system notes on issues, merge requests, epics, and snippets. It supports creating, listing, updating, and deleting notes for collaboration and discussion within GitLab resources.
  - aid: gitlab:apiv4snippets
    name: GitLab Snippets API
    tags:
      - Code Sharing
      - Collaboration
      - Snippets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/snippets/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/snippets/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Snippets API provides programmatic access to manage code snippets. It supports creating, listing, updating, and deleting both personal and project snippets, enabling sharing of code fragments and configuration examples across teams and projects.
  - aid: gitlab:apiv4packages
    name: GitLab Packages API
    tags:
      - Artifacts
      - Package Registry
      - Packages
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/packages/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/packages/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Packages API provides programmatic access to the GitLab Package Registry. It supports listing, retrieving, and deleting packages across projects and groups, with support for multiple package formats including NPM, Maven, PyPI, NuGet, Conan, Helm, and more.
  - aid: gitlab:apiv4container-registry
    name: GitLab Container Registry API
    tags:
      - Container Registry
      - Containers
      - Docker
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/container_registry/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/container_registry/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Container Registry API provides programmatic access to manage container images stored in the GitLab Container Registry. It supports listing repositories and tags, deleting images, and managing registry visibility settings for containerized application deployments.
  - aid: gitlab:apiv4vulnerabilities
    name: GitLab Vulnerabilities API
    tags:
      - DevSecOps
      - Security
      - Vulnerabilities
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/vulnerabilities/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/vulnerabilities/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Vulnerabilities API provides programmatic access to manage security vulnerabilities detected in GitLab projects. It supports retrieving, confirming, resolving, and dismissing vulnerabilities found by SAST, DAST, container scanning, and dependency scanning tools.
  - aid: gitlab:apiv4deploy-keys
    name: GitLab Deploy Keys API
    tags:
      - Deploy Keys
      - Security
      - SSH
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/deploy_keys/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/deploy_keys/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Deploy Keys API provides programmatic access to manage deploy keys for GitLab projects. It supports listing, creating, updating, and deleting SSH deploy keys that grant read-only or read-write access to repositories for automated deployment workflows.
  - aid: gitlab:apiv4protected-branches
    name: GitLab Protected Branches API
    tags:
      - Access Control
      - Protected Branches
      - Source Control
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/protected_branches/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/protected_branches/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Protected Branches API provides programmatic access to manage branch protection rules. It supports listing, creating, updating, and removing protection settings that control who can push, merge, and force push to specific branches in a project.
  - aid: gitlab:apiv4wikis
    name: GitLab Wikis API
    tags:
      - Documentation
      - Knowledge Base
      - Wikis
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/wikis/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/wikis/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Wikis API provides programmatic access to manage project wiki pages. It supports listing, creating, updating, and deleting wiki pages, as well as uploading attachments, enabling teams to maintain project documentation programmatically.
  - aid: gitlab:apiv4events
    name: GitLab Events API
    tags:
      - Activity
      - Audit
      - Events
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/events/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/events/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Events API provides programmatic access to review event activity across GitLab. It supports listing all events, retrieving user contribution events, and viewing project-specific events such as pushes, comments, issue updates, and merge request actions.
  - aid: gitlab:apiv4search
    name: GitLab Search API
    tags:
      - Discovery
      - Query
      - Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/search/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/search/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Search API enables programmatic search across a GitLab instance, group, or project. It supports searching for projects, issues, merge requests, milestones, code blobs, commits, notes, wiki pages, and users with scope-based filtering.
  - aid: gitlab:apiv4namespaces
    name: GitLab Namespaces API
    tags:
      - Namespaces
      - Organization
      - Structure
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gitlab.com/api/v4
    humanURL: https://docs.gitlab.com/api/namespaces/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/api/namespaces/
        type: Documentation
      - url: https://docs.gitlab.com/api/rest/authentication/
        type: Authentication
    description: The GitLab Namespaces API provides programmatic access to manage namespaces in GitLab. It supports listing namespaces, retrieving namespace details, and verifying namespace existence, which is essential for organizing projects and groups within the GitLab hierarchy.
name: GitLab
tags:
  - Code
  - Platform
  - Software Development
  - Source Control
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - type: Website
    url: https://about.gitlab.com/
  - type: Portal
    url: https://docs.gitlab.com/api/
  - type: Documentation
    url: https://docs.gitlab.com/
  - type: Authentication
    url: https://docs.gitlab.com/api/rest/authentication/
  - type: GitHubOrganization
    url: https://github.com/gitlabhq
  - type: Blog
    url: https://about.gitlab.com/blog/
  - type: StatusPage
    url: https://status.gitlab.com/
  - type: Pricing
    url: https://about.gitlab.com/pricing/
  - url: https://about.gitlab.com/terms/
    type: TermsOfService
  - url: https://about.gitlab.com/privacy/
    type: PrivacyPolicy
  - url: https://about.gitlab.com/company/contact/
    type: Support
  - url: https://docs.gitlab.com/ee/editor_extensions/
    type: IDESupport
  - url: https://about.gitlab.com/releases/categories/releases/
    type: ReleaseNotes
  - url: https://developer.gitlab.com/
    type: Portal
  - url: https://docs.gitlab.com/
    type: Documentation
  - url: https://about.gitlab.com/get-started/
    type: GettingStarted
  - url: https://status.gitlab.com/
    type: StatusPage
  - url: https://gitlab.com/users/sign_up
    type: SignUp
  - url: https://about.gitlab.com/blog/
    type: Blog
  - url: https://about.gitlab.com/support/
    type: Support
  - url: https://gitlab.com/gitlab-org/gitlab/blob/master/CHANGELOG.md
    type: ChangeLog
  - url: https://docs.gitlab.com/api/rest/authentication/
    type: Authentication
  - url: https://docs.gitlab.com/api/rest/third_party_clients/
    type: SDK
  - url: https://forum.gitlab.com/
    type: Support
  - url: https://docs.gitlab.com/security/rate_limits/
    type: RateLimits
  - url: json-ld/gitlab-context.jsonld
    type: JSONLD
  - url: json-schema/gitlab-project-schema.json
    type: JSONSchema
  - url: json-schema/gitlab-merge-request-schema.json
    type: JSONSchema
  - url: json-schema/gitlab-issue-schema.json
    type: JSONSchema
  - url: json-schema/gitlab-pipeline-schema.json
    type: JSONSchema
  - url: https://about.gitlab.com/pricing/
    type: Pricing
  - url: https://about.gitlab.com/security/
    type: Security
  - url: https://about.gitlab.com/security/disclosure/
    type: Security
  - url: https://about.gitlab.com/direction/
    type: Documentation
  - url: https://about.gitlab.com/integrations/
    type: Integrations
  - url: https://about.gitlab.com/partners/technology-partners/
    type: Partners
  - url: https://about.gitlab.com/solutions/open-source/
    type: Documentation
  - url: https://marketplace.gitlab.com/
    type: Marketplace
  - url: https://docs.gitlab.com/api/openapi/openapi_interactive/
    type: Tools
  - url: https://gitlab.com/gitlab-org/gitlab
    type: GitHubRepository
  - type: Features
    data:
      - 'Free: 5 users, 400 compute minutes/mo, 10 GiB storage'
      - 'Premium $29/user/mo: 10K compute minutes, $12 GitLab Credits/user'
      - 'Ultimate custom: 50K compute minutes, $24 Credits/user, security testing'
      - REST and GraphQL APIs
      - 'Authenticated API: 2,000 req/min/user'
      - 'Unauthenticated API: 500 req/min/IP'
      - 'Search API: 30 req/min/user'
      - Self-hosted Community Edition (free OSS)
      - Self-hosted Enterprise Edition (paid)
      - GitLab Runner for shared/dedicated runners
      - OAuth 2.0 + personal access tokens + project access tokens
      - Webhooks for project, group, and system events
      - GitLab Duo AI assistant (separate add-on)
      - Container Registry, Package Registry, Helm Chart Registry
      - GitLab Pages static site hosting
      - 'Application Security Testing (Ultimate): SAST, DAST, secret detection'
    sources:
      - https://about.gitlab.com/pricing/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: DevOps Automation
        description: Automate CI/CD pipeline creation, runner management, and deployment workflows.
      - name: Project Management
        description: Programmatically manage issues, milestones, boards, and merge requests.
      - name: Infrastructure as Code
        description: Manage GitLab configuration, groups, projects, and settings through APIs.
      - name: Security and Compliance
        description: Access vulnerability reports, security scan results, and compliance data.
      - name: Migration and Integration
        description: Bulk import projects, users, and data from other platforms.
      - name: Custom Tooling
        description: Build custom developer tools, dashboards, and bots for GitLab workflows.
      - name: Container Management
        description: Manage Docker images, Kubernetes clusters, and container deployments.
      - name: Analytics and Reporting
        description: Extract project analytics, contribution data, and productivity metrics.
  - type: Solutions
    data:
      - name: GitLab Free
        description: Core DevOps platform with unlimited repositories, CI/CD, issue tracking, and API access.
      - name: GitLab Premium
        description: Advanced DevOps with merge request approvals, code owners, and priority support.
      - name: GitLab Ultimate
        description: Enterprise DevOps with security scanning, compliance, and advanced API features.
      - name: GitLab Dedicated
        description: Single-tenant SaaS deployment with dedicated infrastructure and enhanced security.
created: 2023/11/10
modified: '2026-05-04'
position: Consuming
description: GitLab Inc. is an open-core company that develops GitLab, a DevOps software platform for building, securing, and managing applications. Created by Ukrainian developer Dmytro Zaporozhets and Dutch developer Sytse Sijbrandij, GitLab became the first partly-Ukrainian unicorn in 2018. Known for promoting remote work, it is one of the largest all-remote companies globally. GitLab has approximately 30 million registered users, including 1 million active licensed users.
maintainers:
  - FN: Kin Lane
    url: http://apievangelist.com
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
