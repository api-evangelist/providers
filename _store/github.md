---
aid: github
url: https://raw.githubusercontent.com/api-search/code/main/_apis/github/apis.md
apis:
  - aid: github:github-graphql-api
    name: GitHub Graph API
    tags:
      - GraphQL
    overlays: []
    description: |
      To create integrations, retrieve data, and automate your workflows, use
      the GitHub GraphQL API. The GitHub GraphQL API offers more precise and
      flexible queries than the GitHub REST API.
  - aid: github:github-admin-api
    name: GitHub Admin API
    tags:
      - Administrative
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
      - url: properties/github-events-api-openapi.yml
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
      - url: properties/github-issues-api-openapi.yml
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
      - ' Repositories'
      - Repos
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/repos?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-repos-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-repos-api-openapi.yml
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
      - url: properties/github-search-api-openapi.yml
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
      - ' LDAP'
      - ' Mapping'
      - ' User Names'
      - ' Users'
      - ' Sync'
      - ' Authorization'
      - ' Impersonation'
      - ' OAuth'
      - ' Tokens'
      - ' Enterprise'
      - ' Statistics'
      - ' Access'
      - ' Branch'
      - ' Branches'
      - ' Owners'
      - ' Protected'
      - ' Protection'
      - ' Repositories'
      - ' Restrictions'
      - ' Sets'
      - ' Removes'
      - ' Search'
      - ' Authenticated'
      - ' Authenticated User'
      - ' Conflicting'
      - ' Conflicts'
      - ' Docker'
      - ' During'
      - ' Migrations'
      - ' Packages'
      - ' Addresses'
      - ' Emails'
      - ' Followers'
      - ' Following'
      - ' Follows'
      - ' People'
      - ' Checks'
      - ' Followed'
      - ' Person'
      - ' Follow'
      - ' Unfollowing'
      - ' GPG'
      - ' Gpg'
      - ' Keys'
      - ' Accessible'
      - ' Applications'
      - ' Installations'
      - ' Accounts'
      - ' Assigned'
      - ' Issues'
      - ' Public'
      - ' SSH'
      - ' Memberships'
      - ' Organizations'
      - ' Archive'
      - ' Download'
      - ' Namespaces'
      - ' Names'
      - ' Types'
      - ' Restore'
      - ' Owned'
      - ' Versions'
      - ' Projects'
      - ' Invitations'
      - ' Accept'
      - ' Invitation'
      - ' Decline'
      - ' Social'
      - ' Signing'
      - ' Starred'
      - ' Star'
      - ' Unstar'
      - ' Subscriptions'
      - ' Watched'
      - ' Teams'
      - ' Events'
      - ' Another'
      - ' Targets'
      - ' Gists'
      - ' Contextual'
      - ' Hovercard'
      - ' Information'
      - ' Received'
      - ' Administrator'
      - ' Promote'
      - ' Sites'
      - ' Demote'
      - ' Suspend'
      - ' Suspended'
      - ' Unsuspend'
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/users?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-user-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-user-api-openapi.yml
        type: OpenAPI
    description: |-

      Use the REST API to get public and private information about authenticated
      users.
name: GitHub
tags:
  - Code
  - Source Control
  - Software Development
  - Platform
  - Pipelines
  - T1
type: Contract
access: 3rd-Party
common:
  - url: https://github.com/pricing
    data:
      - id: free
        name: Free
        addOns:
          - name: GitHub Copilot Access
            description: >-
              With GitHub Copilot, get suggestions for whole lines or entire
              functionsright inside your editor.
          - name: GitHub Codespaces Access
            description: >-
              With GitHub Codespaces, get an instant dev environment in the
              cloud, so you can code anywhere on any device.
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Free
            metric: user
            timeFrame: month
            description: Usage based pricing.
          - geo: US
            unit: 1
            label: CI/CD Minutes
            limit: 2000
            price: Free
            metric: ci-cd-minute
            timeFrame: minutes
            description: CI/CD minutes usage.
          - geo: US
            unit: 1
            label: Package Storage
            limit: 500
            price: Free
            metric: mb
            description: The amount of package storage.
        elements:
          - name: Unlimited Public Repositories
            description: >-
              Host open source projects in public GitHub repositories,
              accessible via web or command line. Public repositories are
              accessible to anyone at GitHub.com.
          - name: Unlimited Private Repositories
            description: >-
              Host open source projects in public GitHub repositories,
              accessible via web or command line. Public repositories are
              accessible to anyone at GitHub.com.
          - name: Dependabot Security Updates
            description: >-
              Keep projects secure by automatically opening pull requests to
              update vulnerable dependencies and keep them up to date.
          - name: Dependabot Version Updates
            description: >-
              Keep projects secure by automatically opening pull requests to
              update vulnerable dependencies and keep them up to date.
          - name: Issues
            description: >-
              Give your developers flexible features for project management that
              adapts to any team, project, and workflow  all alongside your
              code.
          - name: Projects
            description: >-
              Give your developers flexible features for project management that
              adapts to any team, project, and workflow  all alongside your
              code.
          - name: Community Support
            description: >-
              Get help with most of your GitHub questions and issues in our
              Community Forum.
        description: The basics for individuals and organizations
      - id: team
        name: Team
        addOns:
          - name: GitHub Secret Protection
            description: >-
              Ensure your secrets stay secure. Mitigate risk associated with
              exposed secrets in your repositories, while preventing new leaks
              before they happen with push protection.
          - name: GitHub Code Security
            description: >-
              Find and fix vulnerabilities in your code before they reach
              production. Prioritize your Dependabot alerts with automated
              triage rules.
        entries:
          - geo: US
            unit: 1
            label: User
            price: '4.00'
            metric: user
            timeFrame: month
            description: Usage based pricing.
          - geo: US
            unit: 1
            label: CI/CD Minutes
            limit: 2000
            price: Free
            metric: ci-cd-minute
            timeFrame: minutes
            description: CI/CD minutes usage.
          - geo: US
            unit: 1
            label: Package Storage
            limit: 500
            price: Free
            metric: mb
            description: The amount of package storage.
        elements:
          - name: Unlimited Public Repositories
            description: >-
              Host open source projects in public GitHub repositories,
              accessible via web or command line. Public repositories are
              accessible to anyone at GitHub.com.
          - name: Unlimited Private Repositories
            description: >-
              Host open source projects in public GitHub repositories,
              accessible via web or command line. Public repositories are
              accessible to anyone at GitHub.com.
          - name: Dependabot Security Updates
            description: >-
              Keep projects secure by automatically opening pull requests to
              update vulnerable dependencies and keep them up to date.
          - name: Dependabot Version Updates
            description: >-
              Keep projects secure by automatically opening pull requests to
              update vulnerable dependencies and keep them up to date.
          - name: Issues
            description: >-
              Give your developers flexible features for project management that
              adapts to any team, project, and workflow  all alongside your
              code.
          - name: Projects
            description: >-
              Give your developers flexible features for project management that
              adapts to any team, project, and workflow  all alongside your
              code.
          - name: Community Support
            description: >-
              Get help with most of your GitHub questions and issues in our
              Community Forum.
          - name: Access to GitHub Codespaces
            description: >-
              Blazing fast cloud developer environments with flexible compute
              and pre-configured containers, developers can code, collaborate,
              and debug from any browser. Pay only for what you use with compute
              fees starting at $0.18/hr and storage fees at $0.07/GB per month.
          - name: Protected Branches
            description: >-
              Enforce restrictions on how code branches are merged, including
              requiring reviews by selected collaborators, or allowing only
              specific contributors to work on a particular branch.
          - name: Multiple Reviewers in Pull Requests
            description: Assign multiple users or a team to review a pull request.
          - name: Draft Pull Requests
            description: >-
              Easily discuss and collaborate on pull requests before submitting
              to formal review.
          - name: Code Owners
            description: >-
              Automatically request reviewsor require approvalby selected
              contributors when changes are made to sections of code that they
              own.
          - name: Required Reviewers
            description: >-
              Ensure that pull requests have a specific number of approving
              reviews before collaborators can make changes to a protected
              branch.
          - name: Pages & Wikis
            description: >-
              Host documentation and simple websites for your project in a wiki
              format that contributors can easily edit either on the web or
              command line.
          - name: Environmental Deployment Branches and Secrets
            description: >-
              A job cannot access secrets that are defined in an environment
              unless it is running on the specified branch.
          - name: Web Based Support
            description: >-
              GitHub Support can help you troubleshoot issues you run into while
              using GitHub.
        description: Advanced collaboration for individuals and organizations.
      - id: enterprise
        name: Enterprise
        addOns:
          - name: Premium Support
            description: >-
              With Premium, get a 30-minute SLA on Urgent tickets and 24/7 web
              and phone support via callback request. With Premium Plus, get
              everything in Premium, assigned Customer Reliability Engineer and
              more.
        entries:
          - geo: US
            unit: 1
            label: User
            price: '21.00'
            metric: user
            timeFrame: month
            description: Usage based pricing.
          - geo: US
            unit: 1
            label: CI/CD Minutes
            limit: 50000
            price: Free
            metric: ci-cd-minute
            timeFrame: minutes
            description: CI/CD minutes usage.
          - geo: US
            unit: 1
            label: Package Storage
            limit: 50
            price: Free
            metric: gb
            description: The amount of package storage.
        elements:
          - name: Unlimited Public Repositories
            description: >-
              Host open source projects in public GitHub repositories,
              accessible via web or command line. Public repositories are
              accessible to anyone at GitHub.com.
          - name: Unlimited Private Repositories
            description: >-
              Host open source projects in public GitHub repositories,
              accessible via web or command line. Public repositories are
              accessible to anyone at GitHub.com.
          - name: Dependabot Security Updates
            description: >-
              Keep projects secure by automatically opening pull requests to
              update vulnerable dependencies and keep them up to date.
          - name: Dependabot Version Updates
            description: >-
              Keep projects secure by automatically opening pull requests to
              update vulnerable dependencies and keep them up to date.
          - name: Issues
            description: >-
              Give your developers flexible features for project management that
              adapts to any team, project, and workflow  all alongside your
              code.
          - name: Projects
            description: >-
              Give your developers flexible features for project management that
              adapts to any team, project, and workflow  all alongside your
              code.
          - name: Community Support
            description: >-
              Get help with most of your GitHub questions and issues in our
              Community Forum.
          - name: Access to GitHub Codespaces
            description: >-
              Blazing fast cloud developer environments with flexible compute
              and pre-configured containers, developers can code, collaborate,
              and debug from any browser. Pay only for what you use with compute
              fees starting at $0.18/hr and storage fees at $0.07/GB per month.
          - name: Protected Branches
            description: >-
              Enforce restrictions on how code branches are merged, including
              requiring reviews by selected collaborators, or allowing only
              specific contributors to work on a particular branch.
          - name: Multiple Reviewers in Pull Requests
            description: Assign multiple users or a team to review a pull request.
          - name: Draft Pull Requests
            description: >-
              Easily discuss and collaborate on pull requests before submitting
              to formal review.
          - name: Code Owners
            description: >-
              Automatically request reviewsor require approvalby selected
              contributors when changes are made to sections of code that they
              own.
          - name: Required Reviewers
            description: >-
              Ensure that pull requests have a specific number of approving
              reviews before collaborators can make changes to a protected
              branch.
          - name: Pages & Wikis
            description: >-
              Host documentation and simple websites for your project in a wiki
              format that contributors can easily edit either on the web or
              command line.
          - name: Environmental Deployment Branches and Secrets
            description: >-
              A job cannot access secrets that are defined in an environment
              unless it is running on the specified branch.
          - name: Data Residency
            description: >-
              GitHub Enterprise Cloud offers a multi-tenant enterprise SaaS
              solution on Microsoft Azure, allowing you to choose a regional
              cloud deployment for data residency, so your in-scope data is
              stored at rest in a designated location. Start a free 30 day trial
              today or contact our sales team for more information.
          - name: Managed Users
            description: >-
              Own and control the user accounts of your enterprise members
              through your identity provider (IdP).
          - name: User Provisioning Through SCIM
            description: >-
              Automatically invite members to join your organization when you
              grant access on your IdP. If you remove a member's access to your
              GitHub organization on your SAML IdP, the member will be
              automatically removed from the GitHub organization.
          - name: Centrall Manage Multiple Organizations
            description: >-
              GitHub Enterprise Cloud includes the option to create an
              enterprise account, which enables collaboration between multiple
              organizations, gives administrators a single point of visibility
              and management and brings license cost savings for identical users
              in multiple organizations
          - name: Environment Protection Rules
            description: >-
              When a workflow job references an environment, the job won't start
              until all of the environment's protection rules pass.
          - name: Repository Rules
            description: >-
              Enforce branch and tag restrictions across your organization,
              ensuring branch and tag protection across your repositories.
              Evaluate rules to assess impact before enforcement.
          - name: Audit Log API
            description: >-
              As a GitHub Enterprise Cloud organization administrator, you can
              now access log events using our GraphQL API and monitor the
              activity in your organization.
          - name: Annual SOC Reports
            description: >-
              GitHub offers AICPA System and Organization Controls (SOC) 1 Type
              2 and SOC 2 Type 2 reports with IAASB International Standards on
              Assurance Engagements, ISAE 3000, and ISAE 3402.
          - name: FedRAMP
            description: >-
              Government users can host projects on GitHub Enterprise Cloud with
              the confidence that our platform meets the low impact
              software-as-a-service (SaaS) baseline of security standards set by
              our U.S. federal government partners.
          - name: SAML Single Sign-On
            description: >-
              Use an identity provider to manage the identities of GitHub users
              and applications.
          - name: Advanced Auditing
            description: >-
              Quickly review the actions performed by members of your
              organization. Keep copies of audit log data to ensure secure IP
              and maintain compliance for your organization.
          - name: GitHub Connect
            description: >-
              Share features and workflows between your GitHub Enterprise Server
              instance and GitHub Enterprise Cloud.
        description: Security, compliance, and flexible deployment
    name: Plans
    type: Plans
  - url: https://github.com/github/roadmap
    name: Road Map
    type: RoadMap
  - url: https://github.com/about
    name: About GitHub
    type: About
  - url: >-
      https://docs.github.com/en/get-started/exploring-integrations/about-building-integrations
    name: About building integrations - GitHub Docs
    type: Documentation
  - url: https://www.githubstatus.com/
    name: Status
    type: Status
  - url: https://cli.github.com/
    name: GitHub CLI | Take GitHub to the command line
    type: CLI
  - url: https://github.com/github
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://support.github.com/
    name: GitHub Support
    type: Support
  - url: https://github.com/partners/
    name: GitHub  Where software is built
    type: Partners
  - url: https://github.com/partners/
    name: GitHub  Where software is built
    type: Partners
  - url: >-
      https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
    name: GitHub Terms of Service - GitHub Docs
    type: TermsOfService
  - url: >-
      https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
    name: GitHub General Privacy Statement - GitHub Docs
    type: PrivacyPolicy
  - url: >-
      https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
    name: GitHub General Privacy Statement - GitHub Docs
    type: PrivacyPolicy
  - url: >-
      https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28
    name: Rate limits for the REST API - GitHub Docs
    type: RateLimits
  - url: >-
      https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api?apiVersion=2022-11-28
    name: Using pagination in the REST API - GitHub Docs
    type: Pagination
  - url: >-
      https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28
    name: Authenticating to the REST API - GitHub Docs
    type: Authentication
  - url: >-
      https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28
    name: Getting started with the REST API - GitHub Docs
    type: GettingStarted
created: 2024/04/14
modified: '2025-12-21'
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