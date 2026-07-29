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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 63.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 92
  human_in_the_loop: 1
  name: Gitlab Agentic Access
  operation_count: 167
  slug: gitlab-agentic-access
  summary_line: 167 operations · 92 acting · 1 human-in-the-loop
api_count: 44
apis:
- description: 'GraphQL is a query language for APIs. You can use it to request the exact data you need, and therefore limit the number of requests you need. GraphQL data is arranged in types, so your client can use '
  name: GitLab GraphQL API
  slug: gitlab-graphql-api
- description: The GitLab Issues API provides programmatic access to manage issues across projects and groups. It supports creating, listing, updating, and deleting issues, as well as managing issue assignments, lab
  name: GitLab Issues API
  slug: apiv4issues
- description: The GitLab Merge Requests API enables programmatic management of merge requests across projects and groups. It supports creating, listing, updating, approving, and merging merge requests, as well as m
  name: GitLab Merge Requests API
  slug: apiv4merge-requests
- description: The GitLab Pipelines API provides programmatic access to CI/CD pipelines in GitLab projects. It supports listing, creating, retrying, and canceling pipelines, as well as retrieving pipeline details an
  name: GitLab Pipelines API
  slug: apiv4pipelines
- description: 'The GitLab Jobs API allows you to interact with CI/CD jobs in GitLab projects. It supports listing, retrieving, canceling, retrying, and erasing jobs, as well as downloading job artifacts and viewing '
  name: GitLab Jobs API
  slug: apiv4jobs
- description: The GitLab Runners API provides endpoints for managing CI/CD runners registered to a GitLab instance. It supports listing, registering, updating, and deleting runners, as well as managing runner confi
  name: GitLab Runners API
  slug: apiv4runners
- description: The GitLab Users API provides programmatic access to manage user accounts on a GitLab instance. It supports listing, creating, updating, and deleting users, managing SSH keys and GPG keys, viewing use
  name: GitLab Users API
  slug: apiv4users
- description: The GitLab Repositories API provides access to Git repository data within GitLab projects. It supports listing repository tree structures, retrieving file contents, comparing branches and tags, downlo
  name: GitLab Repositories API
  slug: apiv4repositories
- description: The GitLab Commits API provides programmatic access to Git commits within GitLab projects. It supports listing, creating, and retrieving commits, viewing commit diffs and comments, cherry-picking comm
  name: GitLab Commits API
  slug: apiv4commits
- description: The GitLab Branches API enables programmatic management of Git branches within GitLab projects. It supports listing, creating, and deleting branches, as well as retrieving branch details including the
  name: GitLab Branches API
  slug: apiv4branches
- description: The GitLab Tags API provides programmatic access to manage Git tags within GitLab projects. It supports listing, creating, and deleting tags, as well as retrieving tag details for version management a
  name: GitLab Tags API
  slug: apiv4tags
- description: The GitLab Releases API enables programmatic management of project releases. It supports creating, listing, updating, and deleting releases, as well as managing release assets and links for distributi
  name: GitLab Releases API
  slug: apiv4releases
- description: 'The GitLab Environments API provides programmatic access to manage deployment environments within GitLab projects. It supports creating, listing, updating, stopping, and deleting environments used to '
  name: GitLab Environments API
  slug: apiv4environments
- description: The GitLab Deployments API enables programmatic access to deployment records in GitLab projects. It supports listing, creating, and updating deployments, as well as retrieving deployment details and m
  name: GitLab Deployments API
  slug: apiv4deployments
- description: The GitLab Pipeline Schedules API provides programmatic access to manage scheduled CI/CD pipelines. It supports creating, listing, updating, and deleting pipeline schedules, as well as managing schedu
  name: GitLab Pipeline Schedules API
  slug: apiv4pipeline-schedules
- description: 'The GitLab Labels API provides programmatic access to manage project labels. It supports creating, listing, updating, deleting, and subscribing to labels used for categorizing issues, merge requests, '
  name: GitLab Labels API
  slug: apiv4labels
- description: The GitLab Milestones API provides programmatic access to manage project milestones. It supports creating, listing, updating, and deleting milestones, as well as retrieving issues and merge requests a
  name: GitLab Milestones API
  slug: apiv4milestones
- description: The GitLab Notes API provides programmatic access to manage comments and system notes on issues, merge requests, epics, and snippets. It supports creating, listing, updating, and deleting notes for co
  name: GitLab Notes API
  slug: apiv4notes
- description: The GitLab Snippets API provides programmatic access to manage code snippets. It supports creating, listing, updating, and deleting both personal and project snippets, enabling sharing of code fragmen
  name: GitLab Snippets API
  slug: apiv4snippets
- description: The GitLab Packages API provides programmatic access to the GitLab Package Registry. It supports listing, retrieving, and deleting packages across projects and groups, with support for multiple packag
  name: GitLab Packages API
  slug: apiv4packages
- description: The GitLab Container Registry API provides programmatic access to manage container images stored in the GitLab Container Registry. It supports listing repositories and tags, deleting images, and manag
  name: GitLab Container Registry API
  slug: apiv4container-registry
- description: The GitLab Vulnerabilities API provides programmatic access to manage security vulnerabilities detected in GitLab projects. It supports retrieving, confirming, resolving, and dismissing vulnerabilitie
  name: GitLab Vulnerabilities API
  slug: apiv4vulnerabilities
- description: The GitLab Deploy Keys API provides programmatic access to manage deploy keys for GitLab projects. It supports listing, creating, updating, and deleting SSH deploy keys that grant read-only or read-wr
  name: GitLab Deploy Keys API
  slug: apiv4deploy-keys
- description: The GitLab Protected Branches API provides programmatic access to manage branch protection rules. It supports listing, creating, updating, and removing protection settings that control who can push, m
  name: GitLab Protected Branches API
  slug: apiv4protected-branches
- description: The GitLab Wikis API provides programmatic access to manage project wiki pages. It supports listing, creating, updating, and deleting wiki pages, as well as uploading attachments, enabling teams to ma
  name: GitLab Wikis API
  slug: apiv4wikis
- description: The GitLab Events API provides programmatic access to review event activity across GitLab. It supports listing all events, retrieving user contribution events, and viewing project-specific events such
  name: GitLab Events API
  slug: apiv4events
- description: 'The GitLab Search API enables programmatic search across a GitLab instance, group, or project. It supports searching for projects, issues, merge requests, milestones, code blobs, commits, notes, wiki '
  name: GitLab Search API
  slug: apiv4search
- description: The GitLab Namespaces API provides programmatic access to manage namespaces in GitLab. It supports listing namespaces, retrieving namespace details, and verifying namespace existence, which is essenti
  name: GitLab Namespaces API
  slug: apiv4namespaces
- description: The Admin API from GitLab — 11 operation(s) for admin.
  name: GitLab Admin API
  slug: gitlab-admin-api
- description: The Application API from GitLab — 2 operation(s) for application.
  name: GitLab Application API
  slug: gitlab-application-api
- description: The Applications API from GitLab — 2 operation(s) for applications.
  name: GitLab Applications API
  slug: gitlab-applications-api
- description: Endpoints for initiating OAuth authorization flows.
  name: GitLab Authorization API
  slug: gitlab-authorization-api
- description: The Avatar API from GitLab — 1 operation(s) for avatar.
  name: GitLab Avatar API
  slug: gitlab-avatar-api
- description: The Broadcast Messages API from GitLab — 2 operation(s) for broadcast messages.
  name: GitLab Broadcast Messages API
  slug: gitlab-broadcast-messages-api
- description: The Bulk Imports API from GitLab — 5 operation(s) for bulk imports.
  name: GitLab Bulk Imports API
  slug: gitlab-bulk-imports-api
- description: The Groups API from GitLab — 6 operation(s) for groups.
  name: GitLab Groups API
  slug: gitlab-groups-api
- description: The Metadata API from GitLab — 1 operation(s) for metadata.
  name: GitLab Metadata API
  slug: gitlab-metadata-api
- description: Manage webhooks for a specific project.
  name: GitLab Project Webhooks API
  slug: gitlab-project-webhooks-api
- description: The Projects API from GitLab — 17 operation(s) for projects.
  name: GitLab Projects API
  slug: gitlab-projects-api
- description: Endpoints for exchanging, refreshing, and revoking OAuth tokens.
  name: GitLab Tokens API
  slug: gitlab-tokens-api
- description: Endpoints for retrieving authenticated user information via OAuth.
  name: GitLab User Info API
  slug: gitlab-user-info-api
- description: The Version API from GitLab — 1 operation(s) for version.
  name: GitLab Version API
  slug: gitlab-version-api
- description: Manage custom headers and URL variables for webhooks.
  name: GitLab Webhook Configuration API
  slug: gitlab-webhook-configuration-api
- description: Access webhook delivery history and resend events.
  name: GitLab Webhook Events API
  slug: gitlab-webhook-events-api
arazzos:
- description: Render a group badge preview, add it to the group, and confirm the list.
  name: GitLab Add and Preview a Group Badge
  slug: gitlab-add-group-badge-workflow
- description: Render a badge preview, then add it to a project and confirm the list.
  name: GitLab Add and Preview a Project Badge
  slug: gitlab-add-project-badge-workflow
- description: List a group's access requests and approve the first pending requester.
  name: GitLab Approve a Pending Group Access Request
  slug: gitlab-approve-group-access-request-workflow
- description: List a project's access requests and approve the first pending requester.
  name: GitLab Approve a Pending Project Access Request
  slug: gitlab-approve-project-access-request-workflow
- description: Authorize an upload, attach a metric image to an alert, then list images.
  name: GitLab Attach a Metric Image to an Alert
  slug: gitlab-attach-alert-metric-image-workflow
- description: Verify a branch has been merged, then unprotect and delete it.
  name: GitLab Clean Up a Merged Branch
  slug: gitlab-cleanup-merged-branch-workflow
- description: Cut a new branch from a ref and immediately apply push/merge protection.
  name: GitLab Create and Protect a Release Branch
  slug: gitlab-create-and-protect-branch-workflow
- description: Resolve the default branch tip and cut a new feature branch from it.
  name: GitLab Create a Feature Branch from the Default Branch
  slug: gitlab-create-branch-from-default-workflow
- description: Check whether a branch exists and create it from a ref only when missing.
  name: GitLab Ensure a Branch Exists
  slug: gitlab-ensure-branch-exists-workflow
- description: List project jobs, pick the first manual job, and trigger it.
  name: GitLab Find and Run a Pending Manual Job
  slug: gitlab-find-and-run-manual-job-workflow
- description: List failed jobs in a project and fetch full detail for the first one.
  name: GitLab Inspect a Failed CI Job
  slug: gitlab-inspect-failed-jobs-workflow
- description: Survey the branch list, then bulk-delete all merged branches.
  name: GitLab Prune Stale Merged Branches
  slug: gitlab-prune-stale-branches-workflow
- description: Create a broadcast banner, then read it back to confirm it was stored.
  name: GitLab Publish and Verify a Broadcast Message
  slug: gitlab-publish-broadcast-message-workflow
- description: Add an existing Kubernetes cluster, then confirm it in the cluster list.
  name: GitLab Register an Existing Instance Cluster
  slug: gitlab-register-instance-cluster-workflow
- description: Request access to a project, then approve that same requester.
  name: GitLab Request and Approve Project Access
  slug: gitlab-request-and-self-approve-project-access-workflow
- description: Confirm an instance CI variable exists, then delete it.
  name: GitLab Retire an Instance-Level CI Variable
  slug: gitlab-retire-instance-ci-variable-workflow
- description: Find a project badge by name and remove it when present.
  name: GitLab Retire a Project Badge by Name
  slug: gitlab-retire-project-badge-workflow
- description: Retire the current broadcast message and publish a replacement.
  name: GitLab Rotate the Active Broadcast Message
  slug: gitlab-rotate-broadcast-message-workflow
- description: Find an existing project badge by name and update its link and image.
  name: GitLab Rotate a Project Badge by Name
  slug: gitlab-rotate-project-badge-workflow
- description: Kick off a direct-transfer migration, then poll the import until it finishes.
  name: GitLab Start a Migration and Poll to Completion
  slug: gitlab-start-migration-and-poll-workflow
- description: Read a migration's summary, then drill into a specific entity's detail.
  name: GitLab Track a Migration's Entities
  slug: gitlab-track-migration-entities-workflow
- description: Start a manual CI job, then poll its status until it finishes.
  name: GitLab Trigger a Manual CI Job and Poll to Completion
  slug: gitlab-trigger-manual-job-and-poll-workflow
- description: Read an existing broadcast message, then update its window and text.
  name: GitLab Reschedule a Broadcast Message
  slug: gitlab-update-broadcast-message-workflow
- description: Look up an instance CI variable and update it or create it if missing.
  name: GitLab Upsert an Instance-Level CI Variable
  slug: gitlab-upsert-instance-ci-variable-workflow
artifact_total: 283
asyncapis:
- description: GitLab Webhooks deliver HTTP POST payloads to a configured URL whenever specified events occur in a GitLab project or group, such as pushes, merge requests, issues, pipeline status changes, and deploy
  name: GitLab Webhooks
  slug: gitlab-webhooks-asyncapi
collections:
- collection_type: postman
  name: GitLab api/v4/admin
  slug: postman-gitlab-api-v4-admin-openapi-original
- collection_type: postman
  name: GitLab api/v4/application
  slug: postman-gitlab-api-v4-application-openapi-original
- collection_type: postman
  name: GitLab api/v4/applications
  slug: postman-gitlab-api-v4-applications-openapi-original
- collection_type: postman
  name: GitLab api/v4/avatar
  slug: postman-gitlab-api-v4-avatar-openapi-original
- collection_type: postman
  name: GitLab api/v4/broadcast messages
  slug: postman-gitlab-api-v4-broadcast-messages-openapi-original
- collection_type: postman
  name: GitLab api/v4/bulk imports
  slug: postman-gitlab-api-v4-bulk-imports-openapi-original
- collection_type: postman
  name: GitLab api/v4/groups
  slug: postman-gitlab-api-v4-groups-openapi-original
- collection_type: postman
  name: GitLab api/v4/metadata
  slug: postman-gitlab-api-v4-metadata-openapi-original
- collection_type: postman
  name: GitLab api/v4/projects
  slug: postman-gitlab-api-v4-projects-openapi-original
- collection_type: postman
  name: GitLab api/v4/version
  slug: postman-gitlab-api-v4-version-openapi-original
- collection_type: postman
  name: GitLab OAuth 2.0 API
  slug: postman-gitlab-oauth2
- collection_type: postman
  name: GitLab API
  slug: postman-gitlab-openapi-original
- collection_type: postman
  name: GitLab Webhooks API
  slug: postman-gitlab-webhooks
- collection_type: open
  name: GitLab OAuth 2.0 API
  slug: open-gitlab-oauth2
- collection_type: open
  name: GitLab Webhooks API
  slug: open-gitlab-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gitlab-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gitlab-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gitlab-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gitlab-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gitlab-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gitlab-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/gitlab-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gitlab-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gitlab-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gitlab-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gitlab-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/gitlab-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gitlab-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gitlab-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gitlab-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gitlab-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/gitlab-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gitlab-data-model.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/gitlab/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-add-group-badge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-add-project-badge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-approve-group-access-request-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-approve-project-access-request-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-attach-alert-metric-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-cleanup-merged-branch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-create-and-protect-branch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-create-branch-from-default-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-ensure-branch-exists-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-find-and-run-manual-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-inspect-failed-jobs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-prune-stale-branches-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-publish-broadcast-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-register-instance-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-request-and-self-approve-project-access-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-retire-instance-ci-variable-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-retire-project-badge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-rotate-broadcast-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-rotate-project-badge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-start-migration-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-track-migration-entities-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-trigger-manual-job-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-update-broadcast-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitlab-upsert-instance-ci-variable-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gitlab-com
- group: company
  title: ''
  type: Website
  url: https://about.gitlab.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.gitlab.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gitlab.com/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.gitlab.com/api/rest/authentication/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gitlabhq
- group: company
  title: ''
  type: Blog
  url: https://about.gitlab.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gitlab.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://about.gitlab.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://about.gitlab.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.gitlab.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://about.gitlab.com/company/contact/
- group: operate
  title: ''
  type: IDESupport
  url: https://docs.gitlab.com/ee/editor_extensions/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://about.gitlab.com/releases/categories/releases/
- group: start
  title: ''
  type: Portal
  url: https://developer.gitlab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gitlab.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://about.gitlab.com/get-started/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gitlab.com/
- group: start
  title: ''
  type: Signup
  url: https://gitlab.com/users/sign_up
- group: company
  title: ''
  type: Blog
  url: https://about.gitlab.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://about.gitlab.com/support/
- group: operate
  title: ''
  type: ChangeLog
  url: https://gitlab.com/gitlab-org/gitlab/blob/master/CHANGELOG.md
- group: auth
  title: ''
  type: Authentication
  url: https://docs.gitlab.com/api/rest/authentication/
- group: build
  title: ''
  type: SDKs
  url: https://docs.gitlab.com/api/rest/third_party_clients/
- group: operate
  title: ''
  type: Support
  url: https://forum.gitlab.com/
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.gitlab.com/security/rate_limits/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/gitlab-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gitlab-project-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gitlab-merge-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gitlab-issue-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gitlab-pipeline-schema.json
- group: commercial
  title: ''
  type: Pricing
  url: https://about.gitlab.com/pricing/
- group: auth
  title: ''
  type: Security
  url: https://about.gitlab.com/security/
- group: auth
  title: ''
  type: Security
  url: https://about.gitlab.com/security/disclosure/
- group: docs
  title: ''
  type: Documentation
  url: https://about.gitlab.com/direction/
- group: company
  title: ''
  type: Partners
  url: https://about.gitlab.com/partners/technology-partners/
- group: docs
  title: ''
  type: Documentation
  url: https://about.gitlab.com/solutions/open-source/
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.gitlab.com/
- group: build
  title: ''
  type: Tools
  url: https://docs.gitlab.com/api/openapi/openapi_interactive/
- group: build
  title: ''
  type: GitHubRepository
  url: https://gitlab.com/gitlab-org/gitlab
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.gitlab.com/llms.txt
created: 2023/11/10
description: GitLab Inc. is an open-core company that develops GitLab, a DevOps software platform for building, securing, and managing applications. Created by Ukrainian developer Dmytro Zaporozhets and Dutch developer Sytse Sijbrandij, GitLab became the first partly-Ukrainian unicorn in 2018. Known for promoting remote work, it is one of the largest all-remote companies globally. GitLab has approximately 30 million registered users, including 1 million active licensed users.
examples:
- key_count: 6
  name: Gitlab Api V4 Admin Api_Entities_Batched Background Migration Example
  slug: gitlab-api-v4-admin-api_entities_batched-background-migration-example
- key_count: 7
  name: Gitlab Api V4 Admin Api_Entities_Ci_Variable Example
  slug: gitlab-api-v4-admin-api_entities_ci_variable-example
- key_count: 10
  name: Gitlab Api V4 Admin Api_Entities_Cluster Example
  slug: gitlab-api-v4-admin-api_entities_cluster-example
- key_count: 2
  name: Gitlab Api V4 Admin Api_Entities_Dictionary_Table Example
  slug: gitlab-api-v4-admin-api_entities_dictionary_table-example
- key_count: 10
  name: Gitlab Api V4 Application Api_Entities_Appearance Example
  slug: gitlab-api-v4-application-api_entities_appearance-example
- key_count: 6
  name: Gitlab Api V4 Application Api_Entities_Application With Secret Example
  slug: gitlab-api-v4-application-api_entities_application-with-secret-example
- key_count: 10
  name: Gitlab Api V4 Application Api_Entities_Plan Limit Example
  slug: gitlab-api-v4-application-api_entities_plan-limit-example
- key_count: 6
  name: Gitlab Api V4 Applications Api_Entities_Application With Secret Example
  slug: gitlab-api-v4-applications-api_entities_application-with-secret-example
- key_count: 1
  name: Gitlab Api V4 Avatar Api_Entities_Avatar Example
  slug: gitlab-api-v4-avatar-api_entities_avatar-example
- key_count: 10
  name: Gitlab Api V4 Broadcast Messages Api_Entities_Broadcast Message Example
  slug: gitlab-api-v4-broadcast-messages-api_entities_broadcast-message-example
- key_count: 5
  name: Gitlab Api V4 Bulk Imports Api_Entities_Bulk Import Example
  slug: gitlab-api-v4-bulk-imports-api_entities_bulk-import-example
- key_count: 10
  name: Gitlab Api V4 Bulk Imports Api_Entities_Bulk Imports Example
  slug: gitlab-api-v4-bulk-imports-api_entities_bulk-imports-example
- key_count: 10
  name: Gitlab Api V4 Groups Api_Entities_Access Requester Example
  slug: gitlab-api-v4-groups-api_entities_access-requester-example
- key_count: 7
  name: Gitlab Api V4 Groups Api_Entities_Badge Example
  slug: gitlab-api-v4-groups-api_entities_badge-example
- key_count: 5
  name: Gitlab Api V4 Groups Api_Entities_Basic Badge Details Example
  slug: gitlab-api-v4-groups-api_entities_basic-badge-details-example
- key_count: 4
  name: Gitlab Api V4 Metadata Api_Entities_Metadata Example
  slug: gitlab-api-v4-metadata-api_entities_metadata-example
- key_count: 10
  name: Gitlab Api V4 Projects Api_Entities_Access Requester Example
  slug: gitlab-api-v4-projects-api_entities_access-requester-example
- key_count: 7
  name: Gitlab Api V4 Projects Api_Entities_Badge Example
  slug: gitlab-api-v4-projects-api_entities_badge-example
- key_count: 5
  name: Gitlab Api V4 Projects Api_Entities_Basic Badge Details Example
  slug: gitlab-api-v4-projects-api_entities_basic-badge-details-example
- key_count: 9
  name: Gitlab Api V4 Projects Api_Entities_Branch Example
  slug: gitlab-api-v4-projects-api_entities_branch-example
- key_count: 10
  name: Gitlab Api V4 Projects Api_Entities_Job Example
  slug: gitlab-api-v4-projects-api_entities_job-example
- key_count: 6
  name: Gitlab Api V4 Projects Api_Entities_Metric Image Example
  slug: gitlab-api-v4-projects-api_entities_metric-image-example
- key_count: 4
  name: Gitlab Api V4 Version Api_Entities_Metadata Example
  slug: gitlab-api-v4-version-api_entities_metadata-example
- key_count: 10
  name: Gitlab Issue Example
  slug: gitlab-issue-example
- key_count: 10
  name: Gitlab Merge Request Example
  slug: gitlab-merge-request-example
- key_count: 2
  name: Gitlab Oauth2 Device Authorization Request Example
  slug: gitlab-oauth2-device-authorization-request-example
- key_count: 6
  name: Gitlab Oauth2 Device Authorization Response Example
  slug: gitlab-oauth2-device-authorization-response-example
- key_count: 3
  name: Gitlab Oauth2 Revoke Token Request Example
  slug: gitlab-oauth2-revoke-token-request-example
- key_count: 5
  name: Gitlab Oauth2 Token Info Example
  slug: gitlab-oauth2-token-info-example
- key_count: 10
  name: Gitlab Oauth2 Token Request Example
  slug: gitlab-oauth2-token-request-example
- key_count: 6
  name: Gitlab Oauth2 Token Response Example
  slug: gitlab-oauth2-token-response-example
- key_count: 8
  name: Gitlab Oauth2 User Info Example
  slug: gitlab-oauth2-user-info-example
- key_count: 10
  name: Gitlab Openapi Original Api_Entities_Access Requester Example
  slug: gitlab-openapi-original-api_entities_access-requester-example
- key_count: 7
  name: Gitlab Openapi Original Api_Entities_Badge Example
  slug: gitlab-openapi-original-api_entities_badge-example
- key_count: 5
  name: Gitlab Openapi Original Api_Entities_Basic Badge Details Example
  slug: gitlab-openapi-original-api_entities_basic-badge-details-example
- key_count: 6
  name: Gitlab Openapi Original Api_Entities_Batched Background Migration Example
  slug: gitlab-openapi-original-api_entities_batched-background-migration-example
- key_count: 9
  name: Gitlab Openapi Original Api_Entities_Branch Example
  slug: gitlab-openapi-original-api_entities_branch-example
- key_count: 7
  name: Gitlab Openapi Original Api_Entities_Ci_Variable Example
  slug: gitlab-openapi-original-api_entities_ci_variable-example
- key_count: 10
  name: Gitlab Openapi Original Api_Entities_Cluster Example
  slug: gitlab-openapi-original-api_entities_cluster-example
- key_count: 10
  name: Gitlab Openapi Original Api_Entities_Commit Example
  slug: gitlab-openapi-original-api_entities_commit-example
- key_count: 2
  name: Gitlab Openapi Original Api_Entities_Custom Attribute Example
  slug: gitlab-openapi-original-api_entities_custom-attribute-example
- key_count: 2
  name: Gitlab Openapi Original Api_Entities_Dictionary_Table Example
  slug: gitlab-openapi-original-api_entities_dictionary_table-example
- key_count: 6
  name: Gitlab Openapi Original Api_Entities_Metric Image Example
  slug: gitlab-openapi-original-api_entities_metric-image-example
- key_count: 4
  name: Gitlab Openapi Original Api_Entities_Platform_Kubernetes Example
  slug: gitlab-openapi-original-api_entities_platform_kubernetes-example
- key_count: 7
  name: Gitlab Openapi Original Api_Entities_Project Identity Example
  slug: gitlab-openapi-original-api_entities_project-identity-example
- key_count: 7
  name: Gitlab Openapi Original Api_Entities_Provider_Gcp Example
  slug: gitlab-openapi-original-api_entities_provider_gcp-example
- key_count: 9
  name: Gitlab Openapi Original Api_Entities_User Basic Example
  slug: gitlab-openapi-original-api_entities_user-basic-example
- key_count: 10
  name: Gitlab Pipeline Example
  slug: gitlab-pipeline-example
- key_count: 10
  name: Gitlab Project Example
  slug: gitlab-project-example
- key_count: 10
  name: Gitlab Webhooks Webhook Event Example
  slug: gitlab-webhooks-webhook-event-example
- key_count: 10
  name: Gitlab Webhooks Webhook Example
  slug: gitlab-webhooks-webhook-example
- key_count: 10
  name: Gitlab Webhooks Webhook Input Example
  slug: gitlab-webhooks-webhook-input-example
features:
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
finops:
- name: Gitlab Finops
  service_category: DevOps Platform
  slug: gitlab-finops
graphqls:
- description: 'GraphQL is a query language for APIs. You can use it to request the exact data you need, and therefore limit the number of requests you need. GraphQL data is arranged in types, so your client can use '
  name: GitLab GraphQL API
  slug: gitlab-graphql
image: /assets/icons/gitlab.png
json_schemas:
- name: API_Entities_BatchedBackgroundMigration
  property_count: 6
  slug: gitlab-api-v4-admin-api_entities_batched-background-migration
- name: API_Entities_Ci_Variable
  property_count: 7
  slug: gitlab-api-v4-admin-api_entities_ci_variable
- name: API_Entities_Cluster
  property_count: 15
  slug: gitlab-api-v4-admin-api_entities_cluster
- name: API_Entities_Dictionary_Table
  property_count: 2
  slug: gitlab-api-v4-admin-api_entities_dictionary_table
- name: API_Entities_Appearance
  property_count: 16
  slug: gitlab-api-v4-application-api_entities_appearance
- name: API_Entities_ApplicationWithSecret
  property_count: 6
  slug: gitlab-api-v4-application-api_entities_application-with-secret
- name: API_Entities_PlanLimit
  property_count: 20
  slug: gitlab-api-v4-application-api_entities_plan-limit
- name: API_Entities_ApplicationWithSecret
  property_count: 6
  slug: gitlab-api-v4-applications-api_entities_application-with-secret
- name: API_Entities_Avatar
  property_count: 1
  slug: gitlab-api-v4-avatar-api_entities_avatar
- name: API_Entities_BroadcastMessage
  property_count: 11
  slug: gitlab-api-v4-broadcast-messages-api_entities_broadcast-message
- name: API_Entities_BulkImport
  property_count: 5
  slug: gitlab-api-v4-bulk-imports-api_entities_bulk-import
- name: API_Entities_BulkImports
  property_count: 16
  slug: gitlab-api-v4-bulk-imports-api_entities_bulk-imports
- name: API_Entities_AccessRequester
  property_count: 10
  slug: gitlab-api-v4-groups-api_entities_access-requester
- name: API_Entities_Badge
  property_count: 7
  slug: gitlab-api-v4-groups-api_entities_badge
- name: API_Entities_BasicBadgeDetails
  property_count: 5
  slug: gitlab-api-v4-groups-api_entities_basic-badge-details
- name: API_Entities_Metadata
  property_count: 4
  slug: gitlab-api-v4-metadata-api_entities_metadata
- name: API_Entities_AccessRequester
  property_count: 10
  slug: gitlab-api-v4-projects-api_entities_access-requester
- name: API_Entities_Badge
  property_count: 7
  slug: gitlab-api-v4-projects-api_entities_badge
- name: API_Entities_BasicBadgeDetails
  property_count: 5
  slug: gitlab-api-v4-projects-api_entities_basic-badge-details
- name: API_Entities_Branch
  property_count: 9
  slug: gitlab-api-v4-projects-api_entities_branch
- name: API_Entities_Job
  property_count: 19
  slug: gitlab-api-v4-projects-api_entities_job
- name: API_Entities_MetricImage
  property_count: 6
  slug: gitlab-api-v4-projects-api_entities_metric-image
- name: API_Entities_Metadata
  property_count: 4
  slug: gitlab-api-v4-version-api_entities_metadata
- name: GitLab Issue
  property_count: 29
  slug: gitlab-issue
- name: GitLab Merge Request
  property_count: 33
  slug: gitlab-merge-request
- name: DeviceAuthorizationRequest
  property_count: 2
  slug: gitlab-oauth2-device-authorization-request
- name: DeviceAuthorizationResponse
  property_count: 6
  slug: gitlab-oauth2-device-authorization-response
- name: RevokeTokenRequest
  property_count: 3
  slug: gitlab-oauth2-revoke-token-request
- name: TokenInfo
  property_count: 5
  slug: gitlab-oauth2-token-info
- name: TokenRequest
  property_count: 10
  slug: gitlab-oauth2-token-request
- name: TokenResponse
  property_count: 6
  slug: gitlab-oauth2-token-response
- name: UserInfo
  property_count: 8
  slug: gitlab-oauth2-user-info
- name: API_Entities_AccessRequester
  property_count: 10
  slug: gitlab-openapi-original-api_entities_access-requester
- name: API_Entities_Badge
  property_count: 7
  slug: gitlab-openapi-original-api_entities_badge
- name: API_Entities_BasicBadgeDetails
  property_count: 5
  slug: gitlab-openapi-original-api_entities_basic-badge-details
- name: API_Entities_BatchedBackgroundMigration
  property_count: 6
  slug: gitlab-openapi-original-api_entities_batched-background-migration
- name: API_Entities_Branch
  property_count: 9
  slug: gitlab-openapi-original-api_entities_branch
- name: API_Entities_Ci_Variable
  property_count: 7
  slug: gitlab-openapi-original-api_entities_ci_variable
- name: API_Entities_Cluster
  property_count: 15
  slug: gitlab-openapi-original-api_entities_cluster
- name: API_Entities_Commit
  property_count: 14
  slug: gitlab-openapi-original-api_entities_commit
- name: API_Entities_CustomAttribute
  property_count: 2
  slug: gitlab-openapi-original-api_entities_custom-attribute
- name: API_Entities_Dictionary_Table
  property_count: 2
  slug: gitlab-openapi-original-api_entities_dictionary_table
- name: API_Entities_MetricImage
  property_count: 6
  slug: gitlab-openapi-original-api_entities_metric-image
- name: API_Entities_Platform_Kubernetes
  property_count: 4
  slug: gitlab-openapi-original-api_entities_platform_kubernetes
- name: API_Entities_ProjectIdentity
  property_count: 7
  slug: gitlab-openapi-original-api_entities_project-identity
- name: API_Entities_Provider_Gcp
  property_count: 7
  slug: gitlab-openapi-original-api_entities_provider_gcp
- name: API_Entities_UserBasic
  property_count: 9
  slug: gitlab-openapi-original-api_entities_user-basic
- name: GitLab Pipeline
  property_count: 22
  slug: gitlab-pipeline
- name: GitLab Project
  property_count: 33
  slug: gitlab-project
- name: WebhookEvent
  property_count: 10
  slug: gitlab-webhooks-webhook-event
- name: WebhookInput
  property_count: 19
  slug: gitlab-webhooks-webhook-input
- name: Webhook
  property_count: 24
  slug: gitlab-webhooks-webhook
json_structures:
- name: Gitlab Api V4 Admin Api_Entities_Batched Background Migration Structure
  property_count: 6
  slug: gitlab-api-v4-admin-api_entities_batched-background-migration-structure
- name: Gitlab Api V4 Admin Api_Entities_Ci_Variable Structure
  property_count: 7
  slug: gitlab-api-v4-admin-api_entities_ci_variable-structure
- name: Gitlab Api V4 Admin Api_Entities_Cluster Structure
  property_count: 15
  slug: gitlab-api-v4-admin-api_entities_cluster-structure
- name: Gitlab Api V4 Admin Api_Entities_Dictionary_Table Structure
  property_count: 2
  slug: gitlab-api-v4-admin-api_entities_dictionary_table-structure
- name: Gitlab Api V4 Application Api_Entities_Appearance Structure
  property_count: 16
  slug: gitlab-api-v4-application-api_entities_appearance-structure
- name: Gitlab Api V4 Application Api_Entities_Application With Secret Structure
  property_count: 6
  slug: gitlab-api-v4-application-api_entities_application-with-secret-structure
- name: Gitlab Api V4 Application Api_Entities_Plan Limit Structure
  property_count: 20
  slug: gitlab-api-v4-application-api_entities_plan-limit-structure
- name: Gitlab Api V4 Applications Api_Entities_Application With Secret Structure
  property_count: 6
  slug: gitlab-api-v4-applications-api_entities_application-with-secret-structure
- name: Gitlab Api V4 Avatar Api_Entities_Avatar Structure
  property_count: 1
  slug: gitlab-api-v4-avatar-api_entities_avatar-structure
- name: Gitlab Api V4 Broadcast Messages Api_Entities_Broadcast Message Structure
  property_count: 11
  slug: gitlab-api-v4-broadcast-messages-api_entities_broadcast-message-structure
- name: Gitlab Api V4 Bulk Imports Api_Entities_Bulk Import Structure
  property_count: 5
  slug: gitlab-api-v4-bulk-imports-api_entities_bulk-import-structure
- name: Gitlab Api V4 Bulk Imports Api_Entities_Bulk Imports Structure
  property_count: 16
  slug: gitlab-api-v4-bulk-imports-api_entities_bulk-imports-structure
- name: Gitlab Api V4 Groups Api_Entities_Access Requester Structure
  property_count: 10
  slug: gitlab-api-v4-groups-api_entities_access-requester-structure
- name: Gitlab Api V4 Groups Api_Entities_Badge Structure
  property_count: 7
  slug: gitlab-api-v4-groups-api_entities_badge-structure
- name: Gitlab Api V4 Groups Api_Entities_Basic Badge Details Structure
  property_count: 5
  slug: gitlab-api-v4-groups-api_entities_basic-badge-details-structure
- name: Gitlab Api V4 Metadata Api_Entities_Metadata Structure
  property_count: 4
  slug: gitlab-api-v4-metadata-api_entities_metadata-structure
- name: Gitlab Api V4 Projects Api_Entities_Access Requester Structure
  property_count: 10
  slug: gitlab-api-v4-projects-api_entities_access-requester-structure
- name: Gitlab Api V4 Projects Api_Entities_Badge Structure
  property_count: 7
  slug: gitlab-api-v4-projects-api_entities_badge-structure
- name: Gitlab Api V4 Projects Api_Entities_Basic Badge Details Structure
  property_count: 5
  slug: gitlab-api-v4-projects-api_entities_basic-badge-details-structure
- name: Gitlab Api V4 Projects Api_Entities_Branch Structure
  property_count: 9
  slug: gitlab-api-v4-projects-api_entities_branch-structure
- name: Gitlab Api V4 Projects Api_Entities_Job Structure
  property_count: 19
  slug: gitlab-api-v4-projects-api_entities_job-structure
- name: Gitlab Api V4 Projects Api_Entities_Metric Image Structure
  property_count: 6
  slug: gitlab-api-v4-projects-api_entities_metric-image-structure
- name: Gitlab Api V4 Version Api_Entities_Metadata Structure
  property_count: 4
  slug: gitlab-api-v4-version-api_entities_metadata-structure
- name: Gitlab Issue Structure
  property_count: 29
  slug: gitlab-issue-structure
- name: Gitlab Merge Request Structure
  property_count: 33
  slug: gitlab-merge-request-structure
- name: Gitlab Oauth2 Device Authorization Request Structure
  property_count: 2
  slug: gitlab-oauth2-device-authorization-request-structure
- name: Gitlab Oauth2 Device Authorization Response Structure
  property_count: 6
  slug: gitlab-oauth2-device-authorization-response-structure
- name: Gitlab Oauth2 Revoke Token Request Structure
  property_count: 3
  slug: gitlab-oauth2-revoke-token-request-structure
- name: Gitlab Oauth2 Token Info Structure
  property_count: 5
  slug: gitlab-oauth2-token-info-structure
- name: Gitlab Oauth2 Token Request Structure
  property_count: 10
  slug: gitlab-oauth2-token-request-structure
- name: Gitlab Oauth2 Token Response Structure
  property_count: 6
  slug: gitlab-oauth2-token-response-structure
- name: Gitlab Oauth2 User Info Structure
  property_count: 8
  slug: gitlab-oauth2-user-info-structure
- name: Gitlab Openapi Original Api_Entities_Access Requester Structure
  property_count: 10
  slug: gitlab-openapi-original-api_entities_access-requester-structure
- name: Gitlab Openapi Original Api_Entities_Badge Structure
  property_count: 7
  slug: gitlab-openapi-original-api_entities_badge-structure
- name: Gitlab Openapi Original Api_Entities_Basic Badge Details Structure
  property_count: 5
  slug: gitlab-openapi-original-api_entities_basic-badge-details-structure
- name: Gitlab Openapi Original Api_Entities_Batched Background Migration Structure
  property_count: 6
  slug: gitlab-openapi-original-api_entities_batched-background-migration-structure
- name: Gitlab Openapi Original Api_Entities_Branch Structure
  property_count: 9
  slug: gitlab-openapi-original-api_entities_branch-structure
- name: Gitlab Openapi Original Api_Entities_Ci_Variable Structure
  property_count: 7
  slug: gitlab-openapi-original-api_entities_ci_variable-structure
- name: Gitlab Openapi Original Api_Entities_Cluster Structure
  property_count: 15
  slug: gitlab-openapi-original-api_entities_cluster-structure
- name: Gitlab Openapi Original Api_Entities_Commit Structure
  property_count: 14
  slug: gitlab-openapi-original-api_entities_commit-structure
- name: Gitlab Openapi Original Api_Entities_Custom Attribute Structure
  property_count: 2
  slug: gitlab-openapi-original-api_entities_custom-attribute-structure
- name: Gitlab Openapi Original Api_Entities_Dictionary_Table Structure
  property_count: 2
  slug: gitlab-openapi-original-api_entities_dictionary_table-structure
- name: Gitlab Openapi Original Api_Entities_Metric Image Structure
  property_count: 6
  slug: gitlab-openapi-original-api_entities_metric-image-structure
- name: Gitlab Openapi Original Api_Entities_Platform_Kubernetes Structure
  property_count: 4
  slug: gitlab-openapi-original-api_entities_platform_kubernetes-structure
- name: Gitlab Openapi Original Api_Entities_Project Identity Structure
  property_count: 7
  slug: gitlab-openapi-original-api_entities_project-identity-structure
- name: Gitlab Openapi Original Api_Entities_Provider_Gcp Structure
  property_count: 7
  slug: gitlab-openapi-original-api_entities_provider_gcp-structure
- name: Gitlab Openapi Original Api_Entities_User Basic Structure
  property_count: 9
  slug: gitlab-openapi-original-api_entities_user-basic-structure
- name: Gitlab Pipeline Structure
  property_count: 22
  slug: gitlab-pipeline-structure
- name: Gitlab Project Structure
  property_count: 33
  slug: gitlab-project-structure
- name: Gitlab Webhooks Webhook Event Structure
  property_count: 10
  slug: gitlab-webhooks-webhook-event-structure
- name: Gitlab Webhooks Webhook Input Structure
  property_count: 19
  slug: gitlab-webhooks-webhook-input-structure
- name: Gitlab Webhooks Webhook Structure
  property_count: 24
  slug: gitlab-webhooks-webhook-structure
jsonld:
- class_count: 38
  name: Gitlab Context
  property_count: 268
  slug: gitlab-context
layout: provider
mcp_servers:
- description: ''
  name: gitlab-mcp.yml
  slug: gitlab-mcpyml
modified: '2026-06-20'
name: GitLab
nav: Providers
network: true
overview: 'GitLab publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Application API, Applications API, and 13 more. Tagged areas include Code, Platform, Software Development, and Source Control.


  The GitLab catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  GitLab''s developer surface includes authentication, changelog, CLI, developer portal, documentation, engineering blog, pricing, and 77 more developer resources.'
plans:
- name: Gitlab Plans Pricing
  plan_count: 3
  slug: gitlab-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Gitlab Rate Limits
  slug: gitlab-rate-limits
rules:
- name: GitLab API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: gitlab-asyncapi-spectral-rules
- name: GitLab API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: gitlab-jsonschema-spectral-rules
- name: GitLab API Rules
  rule_count: 27
  severity_counts:
    error: 15
    hint: 0
    info: 3
    warn: 9
  slug: gitlab-spectral-rules
scopes:
- name: Gitlab Scopes
  scope_count: 25
  slug: gitlab-scopes
  summary_line: 25 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: exemplar
  composite: 73.7
  delta: 0.8
  facets:
    commercial_clarity: 78.9
    contract_quality: 72.2
    developer_ergonomics: 71.7
    discoverability: 77.8
    governance: 62.5
    operational_transparency: 78.9
  previous_composite: 72.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gitlab/refs/heads/main/screenshots/gitlab-2026-06-20T181844.png
security:
- kind: authentication
  name: Gitlab Authentication
  slug: gitlab-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Gitlab Domain Security
  slug: gitlab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gitlab Vulnerability Disclosure
  slug: gitlab-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Gitlab Trust Center
  slug: gitlab-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, GDPR, CSA STAR
slug: gitlab
solutions:
- description: Core DevOps platform with unlimited repositories, CI/CD, issue tracking, and API access.
  name: GitLab Free
- description: Advanced DevOps with merge request approvals, code owners, and priority support.
  name: GitLab Premium
- description: Enterprise DevOps with security scanning, compliance, and advanced API features.
  name: GitLab Ultimate
- description: Single-tenant SaaS deployment with dedicated infrastructure and enhanced security.
  name: GitLab Dedicated
tags:
- Code
- Platform
- Software Development
- Source Control
use_cases:
- description: Automate CI/CD pipeline creation, runner management, and deployment workflows.
  name: DevOps Automation
- description: Programmatically manage issues, milestones, boards, and merge requests.
  name: Project Management
- description: Manage GitLab configuration, groups, projects, and settings through APIs.
  name: Infrastructure as Code
- description: Access vulnerability reports, security scan results, and compliance data.
  name: Security and Compliance
- description: Bulk import projects, users, and data from other platforms.
  name: Migration and Integration
- description: Build custom developer tools, dashboards, and bots for GitLab workflows.
  name: Custom Tooling
- description: Manage Docker images, Kubernetes clusters, and container deployments.
  name: Container Management
- description: Extract project analytics, contribution data, and productivity metrics.
  name: Analytics and Reporting
website: https://about.gitlab.com/
---
