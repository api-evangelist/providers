---
aid: github
url: https://raw.githubusercontent.com/api-search/code/main/_apis/github/apis.md
apis:
  - aid: github:github-graphql-api
    name: GitHub Graph API
    tags: []
    overlays: []
    description: |
      To create integrations, retrieve data, and automate your workflows, use
      the GitHub GraphQL API. The GitHub GraphQL API offers more precise and
      flexible queries than the GitHub REST API.
  - aid: github:github-admin-api
    name: GitHub Admin API
    tags:
      - Administrative
      - Hooks
      - Pings
      - Keys
      - Teams
      - Mapping
      - Sync
      - Users
      - Organizations
      - Pre
      - Receive
      - Environments
      - Downloads
      - Latest
      - Tokens
      - Authorization
    humanURL: >-

      https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-admin-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-admin-api-openapi.yml
        type: OpenAPI
      - url: >-

          https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin
        type: Documentation
    description: Use the REST API to administer your enterprise.
  - aid: github:github-app-api
    name: GitHub App API
    tags:
      - Applications
      - Manifests
      - Code
      - Conversions
      - Hook
      - Configurations
      - Deliveries
      - Attempts
      - Installation
      - Installations
      - Access_tokens
      - Suspended
      - Grants
      - Grants""
      - Token
      - Scoped
      - App_slug
      - Repositories
      - Owner
      - Actions
      - Runs
      - Approvals
      - Branches
      - Branch
      - Protection
      - Restrictions
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/apps?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-app-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-app-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/apps
        type: Documentation
    description: |-

      Use the REST API to retrieve information about GitHub Apps and GitHub App
      installations.
  - aid: github:github-auth-api
    name: GitHub Auth API
    tags:
      - Administrative
      - Users
      - User Names
      - Authorization
      - Clients
      - Fingerprint
      - Setup
      - Apis
      - Settings
      - Authorized
      - Keys
    baseURL: https://api.github.com
    humanURL: >-

      https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-auth-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-auth-api-openapi.yml
        type: OpenAPI
      - url: >-

          https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api
        type: Documentation
    description: |-

      You can authenticate to the REST API to access more endpoints and have a
      higher rate limit.
  - aid: github:github-code-of-conduct-api
    name: GitHub Code of Conduct API
    tags:
      - Keys
    baseURL: https://api.github.com
    humanURL: >-

      https://docs.github.com/en/rest/codes-of-conduct/codes-of-conduct?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-codes-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-code-of-conduct-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/codes-of-conduct/codes-of-conduct
        type: Documentation
    description: Use the REST API to get information about codes of conduct.
  - aid: github:github-emojis-api
    name: GitHub Emojis API
    tags: []
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/emojis?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-emojis--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-emojis--openapi-original.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/emojis
        type: Documentation
    description: |-

      Use the REST API to list and view all the available emojis to use on
      GitHub.
  - aid: github:github-enterprise-api
    name: GitHub Enterprise API
    tags: []
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin
    overlays:
      - url: overlays/github-enterprise-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-enterprise-openapi-original.yml
        type: OpenAPI
      - url: >-

          https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin
        type: Documentation
    description: |-

      Create integrations, retrieve data, and automate your workflows with the
      GitHub REST API.
  - aid: github:github-events-api
    name: GitHub Events API
    tags:
      - Authenticated
      - Events
      - Issues
      - Organizations
      - Owners
      - Public
      - Repositories
      - User Names
      - Users
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/activity/events?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-events--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-events--openapi-original.yml
        type: OpenAPI
    description: Use the REST API to interact with GitHub events.
  - aid: github:github-feeds-api
    name: GitHub Feeds API
    tags: []
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/activity/feeds?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-feeds--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-feeds--openapi-original.yml
        type: OpenAPI
    description: |-

      Use the REST API to interact with GitHub feeds. Lists the feeds available
      to the authenticated user. The response provides a URL for each feed. You
      can then get a specific feed by sending a request to one of the feed URLs.
  - aid: github:github-gists-api
    name: GitHub Gists API
    tags:
      - Checks
      - Comments
      - Commits
      - Fork
      - Forks
      - Gists
      - Public
      - Revisions
      - SHA
      - Star
      - Starred
      - Unstar
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/gists?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-gists--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-gists--openapi-original.yml
        type: OpenAPI
    description: |-

      Use the REST API to list, create, update and delete the public gists on
      GitHub.
  - aid: github:github-gitignore-templates-api
    name: GitHub Gitignore Templates API
    tags:
      - Git Ignore
      - Names
      - Templates
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/gitignore?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-gitignore-templates--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-gitignore-templates--openapi-original.yml
        type: OpenAPI
    description: |-

      Use the REST API to get .gitignore templates that can be used to ignore
      files and directories.
  - aid: github:github-installation-api
    name: GitHub Installation API
    tags:
      - Access
      - Accessible
      - Applications
      - Authenticated
      - Installations
      - Organizations
      - Owners
      - Repositories
      - Revoke
      - Suspend
      - Suspended
      - Tokens
      - Unsuspend
      - User Names
      - Users
    baseURL: https://api.github.com/
    overlays:
      - url: overlays/github-installation-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-installation-openapi-original.yml
        type: OpenAPI
    description: |-

      Use the REST API to get information about GitHub App installations and
      perform actions within those installations.
  - aid: github:github-issues-api
    name: GitHub Issues API
    tags:
      - Assigned
      - Assignee
      - Assignees
      - Checks
      - Comments
      - Events
      - Issues
      - Labels
      - Locks
      - Names
      - Numbers
      - Owners
      - Reactions
      - Repositories
      - Sets
      - Timeline
      - Unlock
      - Users
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/issues?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-issues--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-issues--openapi-original.yml
        type: OpenAPI
    description: |-

      Use the REST API to view and manage issues, including issue assignees,
      comments, labels, and milestones.
  - aid: github:github-licenses-api
    name: GitHub Licenses API
    tags:
      - Licenses
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/licenses?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-licenses--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-licenses--openapi-original.yml
        type: OpenAPI
    description: |-

      Use the REST API to retrieve popular open source licenses and information
      about a particular project's license file.
  - aid: github:github-manage-api
    name: GitHub Manage API
    tags:
      - Configurations
      - GHES
      - Manage
      - Metadata
      - Nodes
      - Releases
      - Replicas
      - Replication
      - Running
      - Services
      - Status
      - Versions
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-manage-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-manage-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: github:github-markdown-api
    name: GitHub Markdown API
    tags:
      - Documents
      - Markdown
      - Mode
      - Raw
      - Render
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/markdown?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-markdown--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-markdown--openapi-original.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/markdown
        type: Documentation
    description: |-

      Use the REST API to render a Markdown document as an HTML page or as raw
      text.
  - aid: github:github-meta-api
    name: GitHub Meta API
    tags: []
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/meta?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-meta--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-meta--openapi-original.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/meta
        type: Documentation
    description: |-

      Use the REST API to get meta information about GitHub, including the IP
      addresses of GitHub services.
  - aid: github:github-networks-api
    name: GitHub Networks API
    tags:
      - Events
      - Networks
      - Owners
      - Public
      - Repositories
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-networks-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-networks-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: github:github-notifications-api
    name: GitHub Notifications API
    tags:
      - Notifications
      - Threads
      - Mark
      - Read
      - Authenticated
      - Subscriptions
      - Users
      - Sets
    baseURL: https://api.github.com/
    humanURL: >-

      https://docs.github.com/en/rest/activity/notifications?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-notifications--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-notifications--openapi-original.yml
        type: OpenAPI
    description: |+

      Use the REST API to manage GitHub notifications.



  - aid: github:github-octocat-api
    name: GitHub Octocat API
    tags: []
    baseURL: https://api.github.com/
    humanURL: https://github.com/octokit/octokit.js
    overlays:
      - url: overlays/github-octocat--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-octocat--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: github:github-org-api
    name: GitHub Org API
    tags:
      - Access
      - Actions
      - Active
      - Administrative
      - Advanced
      - Alerts
      - Allowed
      - Announcement
      - Applications
      - Archive
      - Assigned
      - Attempts
      - Audit
      - Authenticated
      - Banner
      - Between
      - Billing
      - Cache
      - Checks
      - Child
      - Claim
      - Code
      - Collaborators
      - Comments
      - Committers
      - Configurations
      - Conflicting
      - Conflicts
      - Connections
      - Convert
      - Custom
      - Customizations
      - Default
      - Deliveries
      - Dependabot
      - Deprecated
      - Disable
      - Discussion
      - Discussions
      - Docker
      - Download
      - Downloads
      - During
      - Enable
      - Enabled
      - Enablement
      - Enforcement
      - Enterprise
      - Enterprises
      - Events
      - External
      - Feature
      - Fine
      - Fine Grained
      - Git
      - Grained
      - Groups
      - Hook
      - Hooks
      - Hub
      - Installations
      - Issues
      - Keys
      - Labels
      - Locks
      - Logs
      - Managers
      - Members
      - Memberships
      - Migrations
      - Names
      - Numbers
      - OIDC
      - Organizations
      - Outside
      - Owned
      - Owners
      - Packages
      - Permissions
      - Pings
      - Pre
      - Pre Receive
      - Products
      - Projects
      - Public
      - Reactions
      - Receive
      - Redeliver
      - Registrations
      - Repositories
      - Restore
      - Roles
      - Runners
      - Scanning
      - Secrets
      - Security
      - Selected
      - Self Hosted
      - Sets
      - Settings
      - Slug
      - Statistics
      - Status
      - Subjects
      - Teams
      - Templates
      - Tokens
      - Types
      - Unlock
      - Usage
      - User Names
      - Users
      - Variables
      - Versions
      - Webhooks
      - Workflows
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/orgs?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-org-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-org-openapi-original.yml
        type: OpenAPI
    description: Use the REST API to control and manage all your GitHub organizations.
  - aid: github:github-projects-api
    name: GitHub Projects API
    tags:
      - Cards
      - Checks
      - Collaborators
      - Columns
      - Existing
      - Move
      - Moves
      - Organizations
      - Owners
      - Permission
      - Permissions
      - Projects
      - Repositories
      - Slug
      - Teams
      - User Names
      - Users
    baseURL: https://api.github.com/
    overlays:
      - url: overlays/github-projects-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-projects-openapi-original.yml
        type: OpenAPI
    description: |-

      Use the REST API to create, list, update, delete and customize projects
      (classic).
  - aid: github:github-rate-limit-api
    name: GitHub Rate Limit API
    tags: []
    baseURL: https://api.github.com/
    humanURL: >-

      https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-rate-limit--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-rate-limit--openapi-original.yml
        type: OpenAPI
    description: |-

      Learn about REST API rate limits, how to avoid exceeding them, and what to
      do if you do exceed them.
  - aid: github:github-repos-api
    name: GitHub Repos API
    tags:
      - Enterprise
      - Repositories
      - Statistics
      - Accessible
      - Applications
      - Installations
      - Actions
      - Enabled
      - Git
      - Hub
      - Organizations
      - Permissions
      - Selected
      - Sets
      - Enable
      - Disable
      - Access
      - Groups
      - Runners
      - Self Hosted
      - Self Hosted
      - Self Hosted
      - Removes
      - Self Hosted
      - Names
      - Secrets
      - Variables
      - Dependabot
      - Locks
      - Migrations
      - Unlock
      - Fine
      - Fine Grained
      - Grained
      - Slug
      - Teams
      - Checks
      - Owners
      - Artifacts
      - Archive
      - Download
      - Format
      - Cache
      - Usage
      - Policies
      - Caches
      - (using
      - Keys
      - ID)
      - Jobs
      - Runs
      - Workflows
      - Logs
      - Re Run
      - Rerun
      - Claim
      - Customizations
      - OIDC
      - Subjects
      - Templates
      - Levels
      - Outside
      - Allowed
      - Default
      - Self Hosted
      - Downloads
      - Registrations
      - Tokens
      - Self Hosted
      - Self Hosted
      - Labels
      - Self Hosted
      - Custom
      - Self Hosted
      - Self Hosted
      - Self Hosted
      - Self Hosted
      - Approvals
      - History
      - Reviews
      - Attempt
      - Attempts
      - Numbers
      - Cancel
      - Deployments
      - Pending
      - Re Run
      - Failed
      - Re Run
      - Public
      - Dispatch
      - Dispatches
      - Events
      - Assignees
      - Assigned
      - Assignee
      - If
      - Users
      - Auto Links
      - Auto Link
      - References
      - Branches
      - Branch
      - Protection
      - Administrative
      - Administrator
      - Enforce
      - Pull
      - Required
      - Commit
      - Signatures
      - Status
      - Contexts
      - Restrictions
      - Protected
      - Rename
      - Annotations
      - Rerequest
      - Suites
      - Preferences
      - Alerts
      - Code
      - Scanning
      - Instances
      - Analysis
      - Configurations
      - Setup
      - Data
      - SARIF
      - Uploads
      - About
      - Information
      - Sarif
      - CODEOWNERS
      - Code Owners
      - Errors
      - Collaborators
      - Is
      - User Names
      - Permission
      - Comments
      - Reactions
      - Commits
      - HEAD
      - Head
      - SHA
      - Associated
      - Pulls
      - Combined
      - Specific
      - Statuses
      - Basehead
      - Compare
      - Content
      - Contents
      - Paths
      - Files
      - Contributors
      - Between
      - Dependencies
      - Difference
      - Graphs
      - (SBOM)
      - Bill
      - Exports
      - Materials
      - Software
      - Snapshots
      - Environments
      - Forks
      - Fork
      - Blobs
      - Objects
      - Matching
      - Tags
      - Trees
      - Hooks
      - Webhooks
      - Hook
      - Deliveries
      - Redeliver
      - Ping
      - Pings
      - Tests
      - Authenticated
      - Invitations
      - Invitation
      - Issues
      - Timeline
      - Deploy
      - Languages
      - LFS
      - Licenses
      - Merge
      - Sync
      - Upstream
      - Merges
      - Milestones
      - Notifications
      - Mark
      - Read
      - Pages
      - Servers
      - Sites
      - Builds
      - Build
      - Latest
      - Pre
      - Pre Receive
      - Receive
      - Pre Receive
      - Enforcement
      - Pre Receive
      - Pre Receive
      - Projects
      - Replies
      - Replies''
      - Merged
      - Requested
      - Reviewers
      - Dismiss
      - Dismissals
      - Submit
      - README
      - Readme
      - Directory
      - Releases
      - Assets
      - Generate
      - Notes
      - Replicas
      - Replication
      - Locations
      - Stargazers
      - Activity
      - Frequency
      - Weekly
      - Last
      - Years
      - Count
      - Participation
      - Cards
      - Days
      - Hourly
      - Punch
      - Subscribers
      - Watchers
      - Subscriptions
      - States
      - (tar)
      - Targets
      - Topics
      - Replace
      - Transfers
      - Vulnerabilities
      - (zip)
      - Using
      - Search
      - (Legacy)
      - Accept
      - Decline
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/repos?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-repos-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-repos-openapi-original.yml
        type: OpenAPI
    description: |-

      Use the REST API to create, manage and control the workflow of public and
      private GitHub repositories.
  - aid: github:github-scim-api
    name: GitHub SCIM API
    tags:
      - Attributes
      - Enterprise
      - Groups
      - Identities
      - Information
      - Provision
      - Provisioned
      - Provisioning
      - SCIM
      - Sets
      - Users
    baseURL: https://api.github.com/
    humanURL: >-

      https://docs.github.com/en/enterprise-cloud@latest/rest/scim?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-scim-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-scim-openapi-original.yml
        type: OpenAPI
    description: |-

      Use the REST API to control and manage your GitHub organization members'
      access with SCIM.
  - aid: github:github-search-api
    name: GitHub Search API
    tags:
      - Code
      - Search
      - Commits
      - Issues
      - Pull
      - Labels
      - Repositories
      - Topics
      - Users
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-search-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-search-openapi-original.yml
        type: OpenAPI
    description: Use the REST API to search for specific items on GitHub.
  - aid: github:github-setup-api
    name: GitHub Setup API
    tags:
      - Configuration Check
      - Configurations
      - Setup
      - Status
      - Configure
      - Process
      - Maintenance
      - Disable
      - Enable
      - Mode
      - Settings
      - Sets
      - Authorized
      - Keys
      - SSH
      - Removes
      - Git
      - Hub
      - Licenses
      - Upgrade
    baseURL: https://api.github.com/
    humanURL: >-
      https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-setup-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-setup-openapi-original.yml
        type: OpenAPI
    description: Use the REST API to create and manage teams in your GitHub organization.
  - aid: github:github-teams-api
    name: GitHub Teams API
    tags:
      - Administrative
      - LDAP
      - Mapping
      - Teams
      - Sync
      - Managers
      - Organizations
      - Security
      - Slug
      - Removes
      - Names
      - Discussions
      - Discussion
      - Numbers
      - Comments
      - Reactions
      - Between
      - Connections
      - External
      - Groups
      - Members
      - Memberships
      - User Names
      - Users
      - Projects
      - Checks
      - Permissions
      - Repositories
      - Owners
      - Child
      - Access
      - Branch
      - Branches
      - Protected
      - Protection
      - Restrictions
      - Sets
      - (Legacy)
      - Authenticated
    baseURL: https://api.github.com/
    overlays:
      - url: overlays/github-teams-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-teams-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: github:github-zen-api
    name: GitHub Zen API
    tags: []
    overlays:
      - url: overlays/github-zen--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-zen--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: github:github-user-api
    name: GitHub User API
    tags:
      - Administrative
      - LDAP
      - Mapping
      - User Names
      - Users
      - Sync
      - Authorization
      - Impersonation
      - OAuth
      - Tokens
      - Enterprise
      - Statistics
      - Access
      - Branch
      - Branches
      - Owners
      - Protected
      - Protection
      - Repositories
      - Restrictions
      - Sets
      - Removes
      - Search
      - Authenticated
      - Authenticated User
      - Conflicting
      - Conflicts
      - Docker
      - During
      - Migrations
      - Packages
      - Addresses
      - Emails
      - Followers
      - Following
      - Follows
      - People
      - Checks
      - Followed
      - If
      - Is
      - Person
      - Follow
      - Unfollowing
      - GPG
      - Gpg
      - Keys
      - Accessible
      - Applications
      - Installations
      - Accounts
      - Assigned
      - Issues
      - Public
      - SSH
      - Memberships
      - Organizations
      - Archive
      - Download
      - Namespaces
      - Names
      - Types
      - Restore
      - Owned
      - Versions
      - Projects
      - Invitations
      - Accept
      - Invitation
      - Decline
      - Social
      - Signing
      - Starred
      - Star
      - Unstar
      - Subscriptions
      - Watched
      - Teams
      - Events
      - Another
      - Targets
      - Gists
      - Contextual
      - Hovercard
      - Information
      - Received
      - Administrator
      - Promote
      - Sites
      - Demote
      - Suspend
      - Suspended
      - Unsuspend
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/users?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-user-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-user-openapi-original.yml
        type: OpenAPI
    description: |-

      Use the REST API to get public and private information about authenticated
      users.
name: GitHub
tags:
  - Code
  - Source Control
  - Software Development
type: Contract
access: 3rd-Party
created: 2024/04/14
modified: '2024-12-30'
position: Consuming
description: >-
  GitHub is a cloud-based platform for software development and version control,
  built on Git. It enables developers to store, manage, and collaborate on code.
  In addition to Gits distributed version control, GitHub offers access control,
  bug tracking, feature requests, task management, continuous integration, and
  wikis for projects. Headquartered in California, it has operated as a
  subsidiary of Microsoft since 2018.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'

---