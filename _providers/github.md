---
access_model:
  confidence: medium
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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 62.6
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 1717
  human_in_the_loop: 47
  name: Github Agentic Access
  operation_count: 3388
  slug: github-agentic-access
  summary_line: 3388 operations · 1717 acting · 47 human-in-the-loop
api_count: 38
apis:
- baseURL: https://api.github.com/
  baseurl_source: declared
  description: The GitHub Gists API lets you programmatically manage gistslightweight code snippets and notesover HTTP. You can create gists (public or secret/unlisted), read individual gists, list public gists, you
  name: GitHub Gists API
  phrasing_intents:
  - id: gists/list
    intent: List my gists
    question: Which gists have I created?
  - id: gists/create
    intent: Create a gist
    question: How do I share a code snippet as a new gist?
  - id: gists/list-public
    intent: List recent public gists from everyone
    question: What public gists have people shared most recently?
  - id: gists/list-starred
    intent: List gists I've starred
    question: Which gists have I starred?
  - id: gists/get
    intent: Get a gist and its files
    question: What files and content are inside a particular gist?
  - id: gists/update
    intent: Update a gist's description or files
    question: Can I edit the files in a gist I already posted?
  - id: gists/delete
    intent: Delete a gist
    question: How do I delete a gist I no longer need?
  - id: gists/list-comments
    intent: List comments on a gist
    question: What have people commented on a gist?
  phrasing_ops: 20
  slug: github-gists-api
- baseURL: https://api.github.com/
  baseurl_source: declared
  description: The GitHub Issues API lets you programmatically manage issue tracking on GitHub, enabling you to list and filter issues across repositories, create and edit issues, change their state (open/closed), a
  name: GitHub Issues API
  phrasing_intents:
  - id: issues/list
    intent: List my issues across every repository I can see
    question: What issues are assigned to me across all my repos, including organization repositories?
  - id: issues/list-for-org
    intent: List my issues in one organization
    question: Which issues in a single organization are assigned to me?
  - id: issues/list-assignees
    intent: List who can be assigned issues in a repository
    question: Who are the available assignees for issues in a repository?
  - id: issues/check-user-can-be-assigned
    intent: Check if a user can be assigned issues in a repo
    question: Does a given user have permission to be assigned issues in this repository at all?
  - id: issues/list-for-repo
    intent: List issues in a repository
    question: How do I list the open issues in one specific repository?
  - id: issues/create
    intent: Open a new issue in a repository
    question: How do I file a new issue in a repository through the API?
  - id: issues/list-comments-for-repo
    intent: List issue comments across a whole repository
    question: What comments have been left on issues and pull requests across an entire repository?
  - id: issues/get-comment
    intent: Get one issue comment by its id
    question: How can I look up a single issue comment when I only have its comment id?
  phrasing_ops: 40
  slug: github-issues-api
- baseURL: https://api.github.com/
  baseurl_source: declared
  description: The GitHub Licenses API lets you programmatically discover and retrieve open source license information across GitHub. It provides endpoints to list the common licenses GitHub supports, get detailed m
  name: GitHub Licenses API
  phrasing_intents:
  - id: licenses/get-all-commonly-used
    intent: List commonly used open source licenses
    question: Which open source licenses are most commonly used on GitHub?
  - id: licenses/get
    intent: Get the details of one license
    question: What permissions, conditions and limitations does a specific license like MIT carry?
  - id: licenses/get-for-repo
    intent: Get a repository's license
    question: Which license does a particular repository use?
  phrasing_ops: 3
  slug: github-licenses-api
- baseURL: https://api.github.com/
  baseurl_source: declared
  description: The GitHub Markdown API is a REST service that converts Markdownespecially GitHub Flavored Markdowninto the same HTML GitHub renders in READMEs, issues, and pull requests, so external apps can display
  name: GitHub Markdown API
  phrasing_intents:
  - id: markdown/render
    intent: Render Markdown to HTML
    question: How do I turn Markdown into HTML the same way GitHub displays it?
  - id: markdown/render-raw
    intent: Render plain-text Markdown like a README
    question: Can I send Markdown as plain text instead of JSON and get HTML back?
  phrasing_ops: 2
  slug: github-markdown-api
- baseURL: https://api.github.com/
  baseurl_source: declared
  description: Use the REST API to get meta information about GitHub, including the IP addresses of GitHub services.
  name: GitHub Meta API
  phrasing_intents:
  - id: meta/root
    intent: Discover the API's top-level resource links
    question: What resource URLs does the REST API root advertise?
  - id: meta/get
    intent: Get server meta information
    question: What meta information does my GitHub Enterprise Server instance publish about itself?
  - id: meta/get-octocat
    intent: Get the Octocat as ASCII art
    question: Can I get the Octocat drawn as ASCII art with my own message in a speech bubble?
  - id: meta/get-zen
    intent: Get a random Zen of GitHub saying
    question: What's a random line from the Zen of GitHub?
  phrasing_ops: 4
  slug: github-meta-api
- baseURL: https://api.github.com/
  baseurl_source: declared
  description: The GitHub Projects API enables developers to programmatically create and manage GitHub Projects, which are flexible tools for planning and tracking work using customizable boards, tables, and roadmap
  name: GitHub Projects API
  phrasing_intents:
  - id: projects/list-for-org
    intent: List an organization's project boards
    question: Which classic project boards does an organization have?
  - id: projects/create-for-org
    intent: Create an organization project board
    question: How do I create a new project board owned by an organization?
  - id: projects/get-card
    intent: Get a project card
    question: What's on a specific project card, and which column is it in?
  - id: projects/update-card
    intent: Edit or archive a project card
    question: How do I archive a project card without deleting it?
  - id: projects/delete-card
    intent: Delete a project card
    question: Can I permanently remove a card from a project board instead of archiving it?
  - id: projects/move-card
    intent: Move a card within or between project columns
    question: How do I move a project card to the top or bottom of a column?
  - id: projects/get-column
    intent: Get a project column
    question: What are the details of a specific column on a project board?
  - id: projects/update-column
    intent: Rename a project column
    question: How do I rename a column on a project board?
  phrasing_ops: 25
  slug: github-projects-api
- baseURL: https://api.github.com/
  baseurl_source: declared
  description: The GitHub Repos API is a set of REST endpoints that let you programmatically create, read, update, and delete repositories and their resources, giving you control over a repos lifecycle and configura
  name: GitHub Repos API
  phrasing_intents:
  - id: repos/list-for-org
    intent: List an organization's repositories
    question: What repositories does my GitHub organization own?
  - id: repos/create-in-org
    intent: Create a repository in an organization
    question: How do I create a new repository under my organization rather than my personal account?
  - id: repos/get
    intent: Get a repository's details
    question: Where can I see a repository's default branch, visibility and settings?
  - id: repos/update
    intent: Update a repository's settings
    question: Can I rename a repository or change its description through the API?
  - id: repos/delete
    intent: Delete a repository
    question: How do I permanently delete a GitHub repository?
  - id: repos/list-autolinks
    intent: List a repository's autolinks
    question: Which autolink references are configured on my repository?
  - id: repos/create-autolink
    intent: Create an autolink reference
    question: How do I make ticket IDs like JIRA-123 in commits link to our tracker automatically?
  - id: repos/get-autolink
    intent: Get one autolink reference
    question: What URL template does a specific autolink use?
  phrasing_ops: 163
  slug: github-repos-api
- baseURL: https://api.github.com/
  baseurl_source: declared
  description: The GitHub Search API lets you programmatically find and filter content across GitHubincluding repositories, code, issues and pull requests, commits, users, topics, and labelsusing a powerful query la
  name: GitHub Search API
  phrasing_intents:
  - id: search/code
    intent: Search for code inside files
    question: How do I find where a function is defined across GitHub repositories?
  - id: search/commits
    intent: Search commits on default branches
    question: How can I find commits whose message mentions a bug number?
  - id: search/issues-and-pull-requests
    intent: Search issues and pull requests
    question: How do I find open issues mentioning a keyword across repositories?
  - id: search/labels
    intent: Search labels in a repository
    question: How do I find issue labels in one repository by name or description?
  - id: search/repos
    intent: Search repositories
    question: What are the most-starred repositories for a given topic or language?
  - id: search/topics
    intent: Search repository topics
    question: Which repository topics exist that relate to a keyword?
  - id: search/users
    intent: Search users
    question: How do I find GitHub users by login, name or public email?
  phrasing_ops: 7
  slug: github-search-api
- baseURL: https://api.github.com/
  baseurl_source: declared
  description: The GitHub Users API (part of the REST API) lets applications read and, for the authenticated account, manage user-related data on GitHub. It can fetch public profiles for any user or the authenticate
  name: GitHub User API
  phrasing_intents:
  - id: users/get-authenticated
    intent: Get my own account profile
    question: Who am I signed in as, according to the token I'm using?
  - id: users/update-authenticated
    intent: Update my own profile
    question: Can I change my display name, bio or location on my profile through the API?
  - id: users/list-emails-for-authenticated-user
    intent: List all email addresses on my account
    question: Which email addresses are attached to my account, and which one is public?
  - id: users/add-email-for-authenticated-user
    intent: Add an email address to my account
    question: How do I add another email address to my account?
  - id: users/delete-email-for-authenticated-user
    intent: Remove an email address from my account
    question: Can I remove an old email address from my account?
  - id: users/list-followers-for-authenticated-user
    intent: List my followers
    question: Who follows me?
  - id: users/list-followed-by-authenticated-user
    intent: List the people I follow
    question: Which accounts am I following?
  - id: users/check-person-is-followed-by-authenticated
    intent: Check if I follow a user
    question: Am I already following a particular user?
  phrasing_ops: 36
  slug: github-user-api
- description: 'The GitHub Deployments API lets you create and manage deployments and deployment statuses for repositories. Deployments are requests to deploy a specific ref (branch, SHA, tag) to an environment, and '
  name: GitHub Deployments API
  slug: github-deployments-api
- description: The GitHub Releases API lets you create, edit, and delete releases for a repository, as well as upload and manage release assets (binaries, installers, archives). Releases are based on Git tags and pr
  name: GitHub Releases API
  slug: github-releases-api
- description: The GitHub Pages API lets you manage GitHub Pages sites for repositories, including creating, updating, and deleting sites, configuring custom domains and HTTPS enforcement, and triggering and monitor
  name: GitHub Pages API
  slug: github-pages-api
- description: The GitHub Git Database API provides low-level access to Git objects (blobs, commits, refs, tags, and trees) in a repository. It lets you read and write raw Git data directly, enabling operations like
  name: GitHub Git Database API
  slug: github-git-database-api
- description: The GitHub Codespaces API lets you create, manage, start, stop, and delete cloud development environments (codespaces) for repositories. It provides endpoints for managing codespace secrets, machine t
  name: GitHub Codespaces API
  slug: github-codespaces-api
- description: The GitHub Copilot API lets organization and enterprise owners manage GitHub Copilot seat assignments, retrieve usage metrics and billing information, and configure Copilot policies. It provides endpo
  name: GitHub Copilot API
  slug: github-copilot-api
- description: The GitHub Security Advisories API lets you view and manage security advisories for repositories and access the GitHub Advisory Database. It provides endpoints to create, update, and list repository s
  name: GitHub Security Advisories API
  slug: github-security-advisories-api
- description: The GitHub Commits API lets you list, retrieve, and compare commits in a repository, as well as manage commit comments and commit statuses. It provides endpoints for viewing commit details, listing pu
  name: GitHub Commits API
  slug: github-commits-api
- description: The GitHub Deploy Keys API lets you manage deploy keys for repositories. Deploy keys are SSH keys that grant read-only or read-write access to a single repository, commonly used for automated deployme
  name: GitHub Deploy Keys API
  slug: github-deploy-keys-api
- description: The GitHub Metrics API lets you access community profile and repository statistics, including contributor activity, commit frequency, code frequency, participation data, punch card data, and community
  name: GitHub Metrics API
  slug: github-metrics-api
- description: The GitHub Interactions API lets you temporarily restrict which users can comment, open issues, or create pull requests in public repositories. It supports setting interaction limits at the repository
  name: GitHub Interactions API
  slug: github-interactions-api
- description: The GitHub Models API provides access to the GitHub Models catalog, letting you list and retrieve details about AI models available on the GitHub platform. It supports browsing model metadata includin
  name: GitHub Models API
  slug: github-models-api
- description: The GitHub GraphQL API provides a flexible query language for accessing GitHub data, allowing clients to request exactly the fields they need in a single request. It supports queries, mutations, and s
  name: GitHub GraphQL API
  slug: github-graphql-api
- description: The GitHub Campaigns API lets organization owners and security managers create and manage security campaigns that coordinate remediation of code scanning alerts across multiple repositories. It provid
  name: GitHub Campaigns API
  slug: github-campaigns-api
- description: The GitHub Classroom API lets you programmatically interact with GitHub Classroom, providing endpoints to list classrooms, get classroom details, list assignments for a classroom, get assignment detai
  name: GitHub Classroom API
  slug: github-classroom-api
- description: The GitHub Code Security API lets organizations and enterprises create and manage reusable code security configurations that standardize security settings across repositories. It provides endpoints to
  name: GitHub Code Security API
  slug: github-code-security-api
- description: The GitHub Credentials API lets you programmatically manage authentication credentials, providing endpoints to revoke a list of credentials such as tokens and keys for security purposes. It enables au
  name: GitHub Credentials API
  slug: github-credentials-api
- description: 'The GitHub Enterprise Teams API lets enterprise owners create and manage enterprise-level teams. It provides endpoints to list, create, get, update, and delete teams, manage team membership including '
  name: GitHub Enterprise Teams API
  slug: github-enterprise-teams-api
- description: 'The GitHub Private Registries API lets organizations configure and manage private package registries. It provides endpoints to list, create, get, update, and delete private registry configurations at '
  name: GitHub Private Registries API
  slug: github-private-registries-api
- description: The GitHub Starring API lets you bookmark repositories and manage your starred list. It provides endpoints to list stargazers for a repository, list repositories starred by the authenticated user or a
  name: GitHub Starring API
  slug: github-starring-api
- description: The GitHub Watching API lets you subscribe to notifications for activity in a repository. It provides endpoints to list watchers of a repository, get and set a repository subscription, delete a subscr
  name: GitHub Watching API
  slug: github-watching-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage GitHub Actions using the REST API.
  name: GitHub Actions API
  phrasing_intents:
  - id: actions/get-actions-cache-usage-for-enterprise
    intent: Check Actions cache usage for an enterprise
    question: How much GitHub Actions cache storage is my whole enterprise using right now?
  - id: actions/get-actions-cache-usage-policy-for-enterprise
    intent: Get the enterprise Actions cache size policy
    question: What cache size limit do repos in my enterprise get for GitHub Actions by default?
  - id: actions/set-actions-cache-usage-policy-for-enterprise
    intent: Set the enterprise Actions cache size policy
    question: Can I raise the default Actions cache size limit for every repo in my enterprise?
  - id: actions/get-github-actions-default-workflow-permissions-enterprise
    intent: Get default GITHUB_TOKEN permissions for an enterprise
    question: What permissions does GITHUB_TOKEN get by default in workflows across my enterprise?
  - id: actions/set-github-actions-default-workflow-permissions-enterprise
    intent: Set default GITHUB_TOKEN permissions for an enterprise
    question: Can I make GITHUB_TOKEN read-only by default for every workflow in my enterprise?
  - id: actions/get-actions-cache-usage-for-org
    intent: Check Actions cache usage for an organization
    question: How much Actions cache storage is my organization using in total?
  - id: actions/get-actions-cache-usage-by-repo-for-org
    intent: List repos by Actions cache usage in an org
    question: Which repositories in my organization are using the most Actions cache?
  - id: actions/get-github-actions-permissions-organization
    intent: Get the Actions permissions policy for an org
    question: Which repositories in my organization are allowed to run GitHub Actions?
  phrasing_ops: 137
  slug: github-actions-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Activity API from GitHub — 25 operation(s) for activity.
  name: GitHub Activity API
  phrasing_intents:
  - id: activity/list-public-events
    intent: List recent public events across the server
    question: What public activity is happening across the whole GitHub instance right now?
  - id: activity/get-feeds
    intent: List the Atom feeds available to me
    question: Which Atom timeline feeds can I subscribe to as the signed-in user?
  - id: activity/list-public-events-for-repo-network
    intent: List public events for a repository's fork network
    question: What public activity is happening across a repository and all of its forks?
  - id: activity/list-notifications-for-authenticated-user
    intent: List my notifications
    question: What unread notifications do I have across all my repositories?
  - id: activity/mark-notifications-as-read
    intent: Mark all my notifications as read
    question: How do I clear every notification in my inbox at once?
  - id: activity/get-thread
    intent: Get one notification thread
    question: What is a particular notification thread about and why did I get it?
  - id: activity/mark-thread-as-read
    intent: Mark one notification thread as read
    question: Can I mark just a single notification as read without clearing the rest?
  - id: activity/get-thread-subscription-for-authenticated-user
    intent: Check my subscription to a notification thread
    question: Am I subscribed to a given notification thread, or have I ignored it?
  phrasing_ops: 31
  slug: github-activity-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Apps API from GitHub — 23 operation(s) for apps.
  name: GitHub Apps API
  phrasing_intents:
  - id: apps/get-authenticated
    intent: Get the GitHub App I'm authenticated as
    question: Which GitHub App do my current JWT credentials belong to?
  - id: apps/create-from-manifest
    intent: Finish creating an app from a manifest
    question: How do I complete the app manifest flow after the user is redirected back with a code?
  - id: apps/get-webhook-config-for-app
    intent: View my app's webhook configuration
    question: Where is my app sending its webhook payloads?
  - id: apps/update-webhook-config-for-app
    intent: Change my app's webhook settings
    question: Can I point my app's webhook at a new URL?
  - id: apps/list-webhook-deliveries
    intent: List my app's webhook deliveries
    question: Which webhook deliveries has my app sent recently?
  - id: apps/get-webhook-delivery
    intent: Inspect one webhook delivery for my app
    question: What request and response were recorded for one of my app's webhook deliveries?
  - id: apps/redeliver-webhook-delivery
    intent: Redeliver a webhook from my app
    question: Can I resend a webhook my app already delivered once?
  - id: apps/list-installation-requests-for-authenticated-app
    intent: List pending installation requests for my app
    question: Who has asked to install my app but is still waiting for approval?
  phrasing_ops: 29
  slug: github-apps-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The GitHub Billing API lets you view billing and usage information for organizations and enterprises, including Actions minutes, Packages storage and data transfer, Codespaces usage, and shared storag
  name: GitHub Billing API
  phrasing_intents:
  - id: billing/get-github-advanced-security-billing-ghe
    intent: Get Advanced Security committers for an enterprise
    question: How many Advanced Security seats is our whole enterprise consuming?
  - id: billing/get-github-advanced-security-billing-org
    intent: Get Advanced Security committers for an org
    question: How many Advanced Security seats is my organization using?
  phrasing_ops: 2
  slug: github-billing-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: 'The GitHub Checks API lets you create and manage check runs and check suites that report detailed status, annotations, and results for commits. It enables CI/CD tools and integrations to report build '
  name: GitHub Checks API
  phrasing_intents:
  - id: checks/create
    intent: Create a check run for a commit
    question: How does my app report a CI result against a specific commit?
  - id: checks/get
    intent: Get a check run
    question: What's the status and conclusion of a specific check run?
  - id: checks/update
    intent: Update or complete a check run
    question: How do I mark an in-progress check run as completed with a conclusion?
  - id: checks/list-annotations
    intent: List annotations on a check run
    question: What line-level warnings or failures did a check run annotate?
  - id: checks/rerequest-run
    intent: Re-run a single check run
    question: Can I re-run one failed check without pushing new code?
  - id: checks/create-suite
    intent: Create a check suite manually
    question: When would I need to create a check suite by hand instead of letting it happen automatically?
  - id: checks/set-suites-preferences
    intent: Change automatic check suite creation for a repo
    question: Can I stop check suites from being created automatically on every push?
  - id: checks/get-suite
    intent: Get a check suite
    question: What's the overall status and conclusion of a check suite?
  phrasing_ops: 12
  slug: github-checks-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Retrieve code scanning alerts from a repository.
  name: GitHub Code-Scanning API
  phrasing_intents:
  - id: code-scanning/list-alerts-for-enterprise
    intent: List code scanning alerts across an enterprise
    question: What code scanning alerts are open across every organization in our enterprise?
  - id: code-scanning/list-alerts-for-org
    intent: List code scanning alerts across an organization
    question: Which repositories in our organization have critical code scanning alerts on the default branch?
  - id: code-scanning/list-alerts-for-repo
    intent: List code scanning alerts in a repository
    question: What code scanning alerts does a repository have right now?
  - id: code-scanning/get-alert
    intent: Get one code scanning alert
    question: What rule triggered a specific code scanning alert and where in the code is it?
  - id: code-scanning/update-alert
    intent: Dismiss or reopen a code scanning alert
    question: How do I dismiss a code scanning alert as a false positive?
  - id: code-scanning/list-alert-instances
    intent: List where a code scanning alert occurs
    question: On which branches and files does a single code scanning alert show up?
  - id: code-scanning/list-recent-analyses
    intent: List code scanning analyses for a repository
    question: When did code scanning last analyze my repository, and with which tool?
  - id: code-scanning/get-analysis
    intent: Get one code scanning analysis
    question: What did a single code scanning analysis find, and can I download it as SARIF?
  phrasing_ops: 13
  slug: github-code-scanning-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Codes-Of-Conduct API from GitHub — 2 operation(s) for codes-of-conduct.
  name: GitHub Codes-Of-Conduct API
  phrasing_intents:
  - id: codes-of-conduct/get-all-codes-of-conduct
    intent: List all available codes of conduct
    question: Which codes of conduct does GitHub offer for projects?
  - id: codes-of-conduct/get-conduct-code
    intent: Get a single code of conduct by key
    question: What does the full text of the Contributor Covenant code of conduct say?
  phrasing_ops: 2
  slug: github-codes-of-conduct-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage Dependabot.
  name: GitHub Dependabot API
  phrasing_intents:
  - id: dependabot/list-alerts-for-enterprise
    intent: List Dependabot alerts across an enterprise
    question: Which vulnerable dependencies are open across every repo in our enterprise?
  - id: dependabot/list-alerts-for-org
    intent: List Dependabot alerts for an organization
    question: What Dependabot security alerts are open across my organization's repos?
  - id: dependabot/list-org-secrets
    intent: List an organization's Dependabot secrets
    question: What Dependabot secrets has my organization defined?
  - id: dependabot/get-org-public-key
    intent: Get the org key for encrypting Dependabot secrets
    question: Which public key do I encrypt an organization Dependabot secret with?
  - id: dependabot/get-org-secret
    intent: Get one organization Dependabot secret
    question: When was an org Dependabot secret last updated and who can use it?
  - id: dependabot/create-or-update-org-secret
    intent: Create or update an org Dependabot secret
    question: How do I add a private registry token as a Dependabot secret for my whole org?
  - id: dependabot/delete-org-secret
    intent: Delete an organization Dependabot secret
    question: How can I remove an organization-level Dependabot secret?
  - id: dependabot/list-selected-repos-for-org-secret
    intent: List repos allowed to use an org Dependabot secret
    question: Which repositories can use an org Dependabot secret set to selected visibility?
  phrasing_ops: 19
  slug: github-dependabot-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The GitHub Dependency Graph API lets you view and submit dependency information for a repository. It provides endpoints to export the software bill of materials (SBOM) for a repository and to submit d
  name: GitHub Dependency Graph API
  phrasing_intents:
  - id: dependency-graph/diff-range
    intent: Compare dependency changes between two commits
    question: Which dependencies were added or removed between two commits in my repo?
  - id: dependency-graph/export-sbom
    intent: Export a repository's SBOM
    question: How do I get a software bill of materials for my GitHub repository?
  - id: dependency-graph/create-repository-snapshot
    intent: Submit a dependency snapshot for a repository
    question: How do I submit dependencies my build detected to the dependency graph?
  phrasing_ops: 3
  slug: github-dependency-graph-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Emojis API from GitHub — 1 operation(s) for emojis.
  name: GitHub Emojis API
  phrasing_intents:
  - id: emojis/get
    intent: List the emojis available to use
    question: Which emoji shortcodes can I use in issues and comments on my Enterprise Server?
  phrasing_ops: 1
  slug: github-emojis-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Enterprise Administration
  name: GitHub Enterprise-Admin API
  phrasing_intents:
  - id: enterprise-admin/list-global-webhooks
    intent: List global webhooks on the instance
    question: Which global webhooks are configured on our GitHub Enterprise Server instance?
  - id: enterprise-admin/create-global-webhook
    intent: Create a global webhook
    question: How do I set up an instance-wide webhook that fires on user and organization events?
  - id: enterprise-admin/get-global-webhook
    intent: Get a global webhook's details
    question: What events and delivery URL is a particular global webhook configured with?
  - id: enterprise-admin/update-global-webhook
    intent: Update a global webhook
    question: How do I change which events an existing global webhook listens to?
  - id: enterprise-admin/delete-global-webhook
    intent: Delete a global webhook
    question: How do I remove an instance-wide webhook we no longer use?
  - id: enterprise-admin/ping-global-webhook
    intent: Send a test ping to a global webhook
    question: How can I test that a global webhook's endpoint is receiving deliveries?
  - id: enterprise-admin/list-public-keys
    intent: List SSH public keys across the instance
    question: Which user SSH public keys exist on our enterprise instance?
  - id: enterprise-admin/delete-public-key
    intent: Delete a user's SSH public key
    question: As a site admin, how do I revoke a compromised SSH public key for a user?
  phrasing_ops: 121
  slug: github-enterprise-admin-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Enterprise-Admin - Scim API from GitHub — 1 operation(s) for enterprise-admin - scim.
  name: GitHub Enterprise-Admin - Scim API
  phrasing_intents:
  - id: enterprise-admin/list-provisioned-groups-enterprise
    intent: List SCIM-provisioned groups in an enterprise
    question: Which groups has our identity provider provisioned into the enterprise over SCIM?
  phrasing_ops: 1
  slug: github-enterprise-admin-scim-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Raw Git functionality.
  name: GitHub Git API
  phrasing_intents:
  - id: git/create-blob
    intent: Create a Git blob in a repository
    question: How do I upload raw file content as a Git blob without cloning the repo?
  - id: git/get-blob
    intent: Get a Git blob by its SHA
    question: How can I read a file's contents from the Git database by its blob SHA?
  - id: git/create-commit
    intent: Create a Git commit object
    question: How do I create a commit directly through the Git database from a tree SHA?
  - id: git/get-commit
    intent: Get a Git commit object by SHA
    question: How do I look up the raw Git commit object, including its tree and parents, for a SHA?
  - id: git/list-matching-refs
    intent: List Git references matching a prefix
    question: How do I find all branches whose names start with feature/?
  - id: git/get-ref
    intent: Get a single Git reference
    question: What commit SHA does a specific branch point to right now?
  - id: git/create-ref
    intent: Create a branch or tag reference
    question: How do I create a new branch from a commit SHA through the API?
  - id: git/update-ref
    intent: Move a reference to a new commit
    question: How do I point an existing branch at a different commit?
  phrasing_ops: 13
  slug: github-git-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Gitignore API from GitHub — 2 operation(s) for gitignore.
  name: GitHub Gitignore API
  phrasing_intents:
  - id: gitignore/get-all-templates
    intent: List available gitignore templates
    question: Which .gitignore templates can I choose from when creating a GitHub repository?
  - id: gitignore/get-template
    intent: Get the contents of a gitignore template
    question: What does the Python .gitignore template actually contain?
  phrasing_ops: 2
  slug: github-gitignore-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The GitHub Migrations API lets you migrate data to and from GitHub. It supports organization migrations that export repositories and metadata as downloadable archives, source imports that convert repo
  name: GitHub Migrations API
  phrasing_intents:
  - id: migrations/list-for-org
    intent: List an organization's recent migrations
    question: What migrations have been run for my organization recently, exports and imports alike?
  - id: migrations/start-for-org
    intent: Start an organization migration export
    question: How do I export several of my organization's repositories into a migration archive?
  - id: migrations/get-status-for-org
    intent: Check an organization migration's status
    question: Has my organization's migration export finished yet, or is it still exporting?
  - id: migrations/download-archive-for-org
    intent: Download an organization migration archive
    question: Where do I download the archive once my organization migration is exported?
  - id: migrations/delete-archive-for-org
    intent: Delete an organization migration archive
    question: Can I delete an organization migration archive before the seven-day automatic cleanup?
  - id: migrations/unlock-repo-for-org
    intent: Unlock a repository locked for migration
    question: My repository is still locked after an organization migration; how do I unlock it?
  - id: migrations/list-repos-for-org
    intent: List repositories in an organization migration
    question: Which repositories are included in a given organization migration?
  - id: migrations/list-for-authenticated-user
    intent: List my user migrations
    question: What personal account migrations have I started?
  phrasing_ops: 11
  slug: github-migrations-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: OAuth Authorizations API
  name: GitHub Oauth-Authorizations API
  phrasing_intents:
  - id: oauth-authorizations/list-grants
    intent: List the OAuth apps I've granted access
    question: Which OAuth applications have I granted access to my account?
  - id: oauth-authorizations/get-grant
    intent: Get one OAuth grant
    question: What scopes did I grant a particular OAuth app?
  - id: oauth-authorizations/delete-grant
    intent: Revoke an OAuth grant and its tokens
    question: How do I cut off an OAuth app's access to my account entirely?
  - id: oauth-authorizations/list-authorizations
    intent: List my OAuth authorizations
    question: What OAuth tokens and authorizations exist on my account?
  - id: oauth-authorizations/create-authorization
    intent: Create a new OAuth authorization (deprecated)
    question: Can I still create a personal token through the OAuth Authorizations API?
  - id: oauth-authorizations/get-or-create-authorization-for-app
    intent: Get or create an authorization for an OAuth app
    question: Can I reuse an existing authorization for an OAuth app instead of making a duplicate?
  - id: oauth-authorizations/get-or-create-authorization-for-app-and-fingerprint
    intent: Get or create an app authorization by fingerprint
    question: Can I keep separate authorizations for the same app per device using a fingerprint?
  - id: oauth-authorizations/get-authorization
    intent: Get one OAuth authorization
    question: What scopes and note are attached to one of my authorizations?
  phrasing_ops: 10
  slug: github-oauth-authorizations-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Oidc API from GitHub — 1 operation(s) for oidc.
  name: GitHub Oidc API
  phrasing_intents:
  - id: oidc/get-oidc-custom-sub-template-for-org
    intent: Get an org's OIDC subject claim template
    question: Which claim keys make up the OIDC subject claim for my organization's Actions tokens?
  - id: oidc/update-oidc-custom-sub-template-for-org
    intent: Set an org's OIDC subject claim template
    question: Can I change which claims go into the OIDC subject claim for my org's workflows?
  phrasing_ops: 2
  slug: github-oidc-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Orgs API from GitHub — 30 operation(s) for orgs.
  name: GitHub Orgs API
  phrasing_intents:
  - id: orgs/list
    intent: List every organization on the server
    question: Can I get a list of all organizations on our GitHub Enterprise Server in the order they were created?
  - id: orgs/list-custom-roles
    intent: List custom repository roles (deprecated, by org ID)
    question: Is there an older endpoint that lists an organization's custom repository roles by numeric organization ID?
  - id: orgs/get
    intent: Get an organization's profile and settings
    question: What details can I pull about a GitHub organization, like its plan, billing email and settings?
  - id: orgs/update
    intent: Update an organization's profile and settings
    question: How do I change the billing email or public profile details of an organization?
  - id: orgs/delete
    intent: Delete an organization and all its repositories
    question: What happens to the repositories when I delete a whole organization?
  - id: announcement-banners/get-announcement-banner-for-org
    intent: Get an organization's announcement banner
    question: What announcement banner is currently showing to members of our organization?
  - id: announcement-banners/set-announcement-banner-for-org
    intent: Set an organization's announcement banner
    question: Can I post a banner message that every member of my organization sees?
  - id: announcement-banners/remove-announcement-banner-for-org
    intent: Remove an organization's announcement banner
    question: How do I take down the announcement banner from our organization?
  phrasing_ops: 49
  slug: github-orgs-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The GitHub Packages API lets you manage packages and package versions in GitHub Packages, a software package hosting service that supports npm, Maven, Gradle, RubyGems, NuGet, Docker, and other packag
  name: GitHub Packages API
  phrasing_intents:
  - id: packages/list-docker-migration-conflicting-packages-for-organization
    intent: List an org's packages that conflicted in Docker migration
    question: Which of our organization's packages ran into a conflict when migrating from the Docker registry?
  - id: packages/list-packages-for-organization
    intent: List an organization's packages
    question: What npm, Maven or container packages does our organization publish?
  - id: packages/get-package-for-organization
    intent: Get one package owned by an organization
    question: What are the details of a specific package our organization publishes, like visibility and version count?
  - id: packages/delete-package-for-org
    intent: Delete an entire organization package
    question: How do I delete a whole package, every version, from our organization?
  - id: packages/restore-package-for-org
    intent: Restore a deleted organization package
    question: Can I bring back a package our organization deleted a couple of weeks ago?
  - id: packages/get-all-package-versions-for-package-owned-by-org
    intent: List versions of an organization package
    question: Which versions of an organization's package have been published?
  - id: packages/get-package-version-for-organization
    intent: Get one version of an organization package
    question: What are the details of one specific version of an org package, like its tags and creation date?
  - id: packages/delete-package-version-for-org
    intent: Delete one version of an organization package
    question: Can I delete just one bad version of an org package and keep the rest?
  phrasing_ops: 27
  slug: github-packages-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Interact with GitHub Pull Requests.
  name: GitHub Pulls API
  phrasing_intents:
  - id: pulls/list
    intent: List pull requests in a repository
    question: What pull requests are open in a repository right now?
  - id: pulls/create
    intent: Open a pull request
    question: How do I open a pull request from my feature branch into main?
  - id: pulls/list-review-comments-for-repo
    intent: List review comments across all PRs in a repo
    question: What line-level code review comments have been left across every pull request in a repository?
  - id: pulls/get-review-comment
    intent: Get one pull request review comment
    question: What does a specific inline review comment on a pull request diff say?
  - id: pulls/update-review-comment
    intent: Edit a pull request review comment
    question: Can I edit the text of an inline review comment on a pull request?
  - id: pulls/delete-review-comment
    intent: Delete a pull request review comment
    question: Can I delete an inline code review comment I left on a pull request diff?
  - id: pulls/get
    intent: Get a pull request by number
    question: What's the status, branches and mergeability of a specific pull request?
  - id: pulls/update
    intent: Edit, close or retarget a pull request
    question: Can I change the base branch a pull request merges into?
  phrasing_ops: 27
  slug: github-pulls-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Check your current rate limit status
  name: GitHub Rate-Limit API
  phrasing_intents:
  - id: rate-limit/get
    intent: Check my remaining API rate limit
    question: How many API requests do I have left before I get rate limited?
  phrasing_ops: 1
  slug: github-rate-limit-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: 'The GitHub Reactions API lets you create, list, and delete emoji reactions on issues, pull requests, issue comments, pull request review comments, commit comments, release assets, and team discussion '
  name: GitHub Reactions API
  phrasing_intents:
  - id: reactions/list-for-team-discussion-comment-in-org
    intent: List reactions on a team discussion comment
    question: What emoji reactions has a reply on our team discussion received?
  - id: reactions/create-for-team-discussion-comment-in-org
    intent: React to a team discussion comment
    question: How do I add an emoji reaction to a reply in a team discussion?
  - id: reactions/delete-for-team-discussion-comment
    intent: Remove a reaction from a team discussion comment
    question: Can I take back an emoji reaction I left on a team discussion reply?
  - id: reactions/list-for-team-discussion-in-org
    intent: List reactions on a team discussion
    question: How are people reacting to a discussion post on our team page?
  - id: reactions/create-for-team-discussion-in-org
    intent: React to a team discussion
    question: Can I put an emoji reaction on a team discussion post itself?
  - id: reactions/delete-for-team-discussion
    intent: Remove a reaction from a team discussion
    question: How can I remove a reaction I put on a team discussion post?
  - id: reactions/list-for-commit-comment
    intent: List reactions on a commit comment
    question: What reactions has a comment on a commit gotten?
  - id: reactions/create-for-commit-comment
    intent: React to a commit comment
    question: How do I add an emoji reaction to a comment on a commit?
  phrasing_ops: 25
  slug: github-reactions-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The GitHub Secret Scanning API lets you retrieve and manage secret scanning alerts for repositories, organizations, and enterprises. Secret scanning detects tokens, keys, and other credentials acciden
  name: GitHub Secret Scanning API
  phrasing_intents:
  - id: secret-scanning/list-alerts-for-enterprise
    intent: List leaked-secret alerts across an enterprise
    question: Where have secrets been leaked across all the organizations in our enterprise?
  - id: secret-scanning/list-alerts-for-org
    intent: List leaked-secret alerts across an organization
    question: Which repositories in our organization have exposed credentials that are still open?
  - id: secret-scanning/list-alerts-for-repo
    intent: List leaked-secret alerts in a repository
    question: Has anyone committed an API key or token to this repository?
  - id: secret-scanning/get-alert
    intent: Get one secret scanning alert
    question: What kind of secret triggered a specific alert, and has it been resolved?
  - id: secret-scanning/update-alert
    intent: Resolve or reopen a secret scanning alert
    question: How do I close a secret scanning alert after I've rotated the leaked credential?
  - id: secret-scanning/list-locations-for-alert
    intent: List where a leaked secret was found
    question: In which files and commits was a leaked secret found?
  phrasing_ops: 6
  slug: github-secret-scanning-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Interact with GitHub Teams.
  name: GitHub Teams API
  phrasing_intents:
  - id: teams/external-idp-group-info-for-org
    intent: Look up an external identity provider group
    question: Which members and teams are tied to one of our external IdP groups?
  - id: teams/list-external-idp-groups-for-org
    intent: List external IdP groups in an organization
    question: What external identity provider groups are available to my organization?
  - id: teams/list
    intent: List the teams in an organization
    question: What teams exist in my organization?
  - id: teams/create
    intent: Create a team in an organization
    question: How do I create a new team in my GitHub organization?
  - id: teams/get-by-name
    intent: Get a team by its slug
    question: How can I look up a team's details from its slug?
  - id: teams/update-in-org
    intent: Update a team's settings
    question: Can I rename an existing team or change its description?
  - id: teams/delete-in-org
    intent: Delete a team from an organization
    question: What happens to child teams when I delete a parent team in my org?
  - id: teams/list-discussions-in-org
    intent: List discussions on a team's page
    question: What discussions have been posted on my team's page?
  phrasing_ops: 63
  slug: github-teams-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The GitHub V3 REST API API from GitHub — 0 operation(s) for github v3 rest api.
  name: GitHub V3 REST API
  slug: github-github-v3-rest-api-api
- baseURL: https://api.github.com/
  baseurl_source: declared
  description: The GitHub Application API API from GitHub — 0 operation(s) for github application api.
  name: GitHub GitHub Application API
  slug: github-github-application-api-api
arazzos:
- description: Branch off the default branch and commit a new file to that branch.
  name: GitHub Commit a File to a New Branch
  slug: github-commit-file-to-new-branch-workflow
- description: Ensure a triage label exists, open an issue, and apply the label to it.
  name: GitHub Create Label and Triage an Issue
  slug: github-create-label-and-triage-issue-workflow
- description: Create a milestone, then open an issue assigned to that milestone.
  name: GitHub Create a Milestone and Assign an Issue to It
  slug: github-create-milestone-and-issue-workflow
- description: Create a repository inside an organization and open its first tracking issue.
  name: GitHub Create Organization Repository and Open First Issue
  slug: github-create-org-repository-and-issue-workflow
- description: Create a repository for the authenticated user and open its first tracking issue.
  name: GitHub Create Repository and Open First Issue
  slug: github-create-repository-and-issue-workflow
- description: Trigger a workflow_dispatch event, locate the resulting run, and poll it to completion.
  name: GitHub Dispatch a Workflow and Poll the Run
  slug: github-dispatch-workflow-and-poll-run-workflow
- description: Fork a repository, resolve the fork's default branch tip, and create a working branch.
  name: GitHub Fork a Repository and Create a Working Branch
  slug: github-fork-and-branch-workflow
- description: Fork an existing gist into your account and leave a comment on the fork.
  name: GitHub Fork a Gist and Comment on the Fork
  slug: github-fork-gist-and-comment-workflow
- description: List a branch's commits, take the newest, then fetch that commit's full detail.
  name: GitHub Inspect the Latest Commit on a Branch
  slug: github-inspect-latest-commit-workflow
- description: Confirm an organization exists, then set a user's membership role in it.
  name: GitHub Onboard a Member into an Organization
  slug: github-onboard-org-member-workflow
- description: Open a pull request from an existing branch and immediately merge it.
  name: GitHub Open and Auto-Merge a Pull Request
  slug: github-open-and-merge-pull-request-workflow
- description: Open a pull request from a branch, then request reviewers on it.
  name: GitHub Open a Pull Request and Request Reviewers
  slug: github-open-pull-request-and-request-reviewers-workflow
- description: Branch, commit a file, and open a pull request back to the base branch.
  name: GitHub Propose a Change via Pull Request
  slug: github-propose-change-pull-request-workflow
- description: Create an organization repository, then register an organization-level webhook.
  name: GitHub Provision an Org Repository and Register an Org Webhook
  slug: github-provision-org-repo-with-webhook-workflow
- description: Create a tagged release, then upload a binary asset to it.
  name: GitHub Publish a Release and Upload an Asset
  slug: github-publish-release-with-asset-workflow
- description: Open a bug issue and immediately add a follow-up comment with reproduction detail.
  name: GitHub Report a Bug and Add Follow-up Detail
  slug: github-report-bug-issue-workflow
- description: Fetch a pull request, confirm it is mergeable, then merge it.
  name: GitHub Check Mergeability and Merge a Pull Request
  slug: github-review-and-merge-pull-request-workflow
- description: Star a gist to bookmark it, then post a feedback comment on it.
  name: GitHub Star a Gist and Leave Feedback
  slug: github-star-and-comment-gist-workflow
- description: Resolve a branch tip, create a tag reference there, then cut a release on that tag.
  name: GitHub Tag a Commit and Cut a Release
  slug: github-tag-commit-and-release-workflow
- description: Confirm a head branch exists, then merge it into a base branch.
  name: GitHub Verify a Branch and Merge It
  slug: github-verify-and-merge-branch-workflow
artifact_total: 1275
asyncapis:
- description: GitHub Webhooks deliver HTTP POST payloads to a configured URL whenever specified events occur on GitHub, such as pushes, pull requests, issues, releases, and more. Webhooks can be configured at the r
  name: GitHub Webhooks
  slug: github-webhooks-asyncapi
collections:
- collection_type: postman
  name: GitHub Application API
  slug: postman-github-app-api
- collection_type: postman
  name: GitHub Auth API
  slug: postman-github-auth-api
- collection_type: postman
  name: GitHub Code of Conduct API
  slug: postman-github-code-of-conduct-api
- collection_type: postman
  name: GitHub Emojis API
  slug: postman-github-emojis
- collection_type: postman
  name: GitHub Events API
  slug: postman-github-events-api
- collection_type: postman
  name: GitHub Issues API
  slug: postman-github-issues-api
- collection_type: postman
  name: github-repo-actions-api
  slug: postman-github-repo-actions-api
- collection_type: postman
  name: github-repos-api
  slug: postman-github-repo-autolinks-api
- collection_type: postman
  name: github-repos-api
  slug: postman-github-repo-branches-api
- collection_type: postman
  name: github-repos-api
  slug: postman-github-repo-code-scanning-api
- collection_type: postman
  name: github-repos-api
  slug: postman-github-repo-collaborators-api
- collection_type: postman
  name: github-repos-api
  slug: postman-github-repo-dependabot-api
- collection_type: postman
  name: github-repo-hooks-api
  slug: postman-github-repo-hooks-api
- collection_type: postman
  name: github-repos-api
  slug: postman-github-repo-invitations-api
- collection_type: postman
  name: github-repos-api
  slug: postman-github-repo-pulls-api
- collection_type: postman
  name: github-repos-api
  slug: postman-github-repo-tags-api
- collection_type: postman
  name: github-repos-api
  slug: postman-github-repos-api
- collection_type: postman
  name: GitHub SCIM API
  slug: postman-github-scim
- collection_type: postman
  name: GitHub Search API
  slug: postman-github-search-api
- collection_type: postman
  name: GitHub Setup API
  slug: postman-github-setup
- collection_type: postman
  name: GitHub Teams API
  slug: postman-github-teams
- collection_type: postman
  name: GitHub User API
  slug: postman-github-users-api
- collection_type: postman
  name: GitHub Zen API
  slug: postman-github-zen
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Github About API
  slug: open-github-about-api
- collection_type: open
  name: Github Access API
  slug: open-github-access-api
- collection_type: open
  name: GitHub Installation Accessible API
  slug: open-github-accessible-api
- collection_type: open
  name: Github Actions API
  slug: open-github-actions-api
- collection_type: open
  name: GitHub Org Active API
  slug: open-github-active-api
- collection_type: open
  name: Github Activity API
  slug: open-github-activity-api
- collection_type: open
  name: Github Add API
  slug: open-github-add-api
- collection_type: open
  name: github-repos-api Administrative API
  slug: open-github-administrative-api
- collection_type: open
  name: GitHub Org Advanced API
  slug: open-github-advanced-api
- collection_type: open
  name: Github Alerts API
  slug: open-github-alerts-api
- collection_type: open
  name: Github All API
  slug: open-github-all-api
- collection_type: open
  name: Github Allowed API
  slug: open-github-allowed-api
- collection_type: open
  name: github-repos-api Analysis API
  slug: open-github-analysis-api
- collection_type: open
  name: github-repos-api Annotations API
  slug: open-github-annotations-api
- collection_type: open
  name: GitHub Org Announcement API
  slug: open-github-announcement-api
- collection_type: open
  name: GitHub Application API
  slug: open-github-app-api
- collection_type: open
  name: Github Applications API
  slug: open-github-applications-api
- collection_type: open
  name: GitHub v3 REST Apps API
  slug: open-github-apps-api
- collection_type: open
  name: Github Archive API
  slug: open-github-archive-api
- collection_type: open
  name: github-repo-actions-api Artifacts API
  slug: open-github-artifacts-api
- collection_type: open
  name: github-repos-api Assets API
  slug: open-github-assets-api
- collection_type: open
  name: Github Assigned API
  slug: open-github-assigned-api
- collection_type: open
  name: Github Assignees API
  slug: open-github-assignees-api
- collection_type: open
  name: github-repos-api Associated API
  slug: open-github-associated-api
- collection_type: open
  name: github-repo-actions-api Attempts API
  slug: open-github-attempts-api
- collection_type: open
  name: GitHub SCIM Attribute API
  slug: open-github-attribute-api
- collection_type: open
  name: GitHub Org Audit API
  slug: open-github-audit-api
- collection_type: open
  name: GitHub Auth API
  slug: open-github-auth-api
- collection_type: open
  name: Github Authenticated API
  slug: open-github-authenticated-api
- collection_type: open
  name: Github Authorization API
  slug: open-github-authorization-api
- collection_type: open
  name: Github Authorized API
  slug: open-github-authorized-api
- collection_type: open
  name: github-repos-api Autolinks API
  slug: open-github-autolinks-api
- collection_type: open
  name: GitHub Org Banner API
  slug: open-github-banner-api
- collection_type: open
  name: Github Between API
  slug: open-github-between-api
- collection_type: open
  name: github-repos-api Bill API
  slug: open-github-bill-api
- collection_type: open
  name: GitHub v3 REST Billing API
  slug: open-github-billing-api
- collection_type: open
  name: github-repos-api Blobs API
  slug: open-github-blobs-api
- collection_type: open
  name: Github Branches API
  slug: open-github-branches-api
- collection_type: open
  name: github-repos-api Builds API
  slug: open-github-builds-api
- collection_type: open
  name: Github Cache API
  slug: open-github-cache-api
- collection_type: open
  name: github-repo-actions-api Caches API
  slug: open-github-caches-api
- collection_type: open
  name: github-repo-actions-api Cancel API
  slug: open-github-cancel-api
- collection_type: open
  name: GitHub Projects Card API
  slug: open-github-card-api
- collection_type: open
  name: GitHub Projects Cards API
  slug: open-github-cards-api
- collection_type: open
  name: github-repos-api Check API
  slug: open-github-check-api
- collection_type: open
  name: Github Checks API
  slug: open-github-checks-api
- collection_type: open
  name: Github Child API
  slug: open-github-child-api
- collection_type: open
  name: Github Claims API
  slug: open-github-claims-api
- collection_type: open
  name: Github Code API
  slug: open-github-code-api
- collection_type: open
  name: GitHub Code of Conduct API
  slug: open-github-code-of-conduct-api
- collection_type: open
  name: github-repos-api Code Owners API
  slug: open-github-code-owners-api
- collection_type: open
  name: GitHub v3 REST Code Scanning API
  slug: open-github-code-scanning-api
- collection_type: open
  name: Github Codes Of Conduct API
  slug: open-github-codes-of-conduct-api
- collection_type: open
  name: GitHub codes
  slug: open-github-codes
- collection_type: open
  name: Github Collaborators API
  slug: open-github-collaborators-api
- collection_type: open
  name: GitHub Projects Column API
  slug: open-github-column-api
- collection_type: open
  name: GitHub Projects Columns API
  slug: open-github-columns-api
- collection_type: open
  name: github-repos-api Combined API
  slug: open-github-combined-api
- collection_type: open
  name: Github Comment API
  slug: open-github-comment-api
- collection_type: open
  name: Github Comments API
  slug: open-github-comments-api
- collection_type: open
  name: Github Commits API
  slug: open-github-commits-api
- collection_type: open
  name: GitHub Org Committers API
  slug: open-github-committers-api
- collection_type: open
  name: github-repos-api Compare API
  slug: open-github-compare-api
- collection_type: open
  name: GitHub Code Conduct API
  slug: open-github-conduct-api
- collection_type: open
  name: Github Configuration API
  slug: open-github-configuration-api
- collection_type: open
  name: GitHub Org Conflicting API
  slug: open-github-conflicting-api
- collection_type: open
  name: Github Connection API
  slug: open-github-connection-api
- collection_type: open
  name: github-repos-api Content API
  slug: open-github-content-api
- collection_type: open
  name: github-repos-api Contexts API
  slug: open-github-contexts-api
- collection_type: open
  name: github-repos-api Contributor API
  slug: open-github-contributor-api
- collection_type: open
  name: github-repos-api Contributors API
  slug: open-github-contributors-api
- collection_type: open
  name: GitHub Org Convert API
  slug: open-github-convert-api
- collection_type: open
  name: github-repos-api Count API
  slug: open-github-count-api
- collection_type: open
  name: Github Create API
  slug: open-github-create-api
- collection_type: open
  name: Github Custom API
  slug: open-github-custom-api
- collection_type: open
  name: Github Customizations API
  slug: open-github-customizations-api
- collection_type: open
  name: github-repos-api Data API
  slug: open-github-data-api
- collection_type: open
  name: github-repos-api Day API
  slug: open-github-day-api
- collection_type: open
  name: Github Delete API
  slug: open-github-delete-api
- collection_type: open
  name: Github Deliveries API
  slug: open-github-deliveries-api
- collection_type: open
  name: Github Dependabot API
  slug: open-github-dependabot-api
- collection_type: open
  name: github-repos-api Dependencies API
  slug: open-github-dependencies-api
- collection_type: open
  name: GitHub v3 REST Dependency Graph API
  slug: open-github-dependency-graph-api
- collection_type: open
  name: github-repos-api Deploy API
  slug: open-github-deploy-api
- collection_type: open
  name: Github Deployments API
  slug: open-github-deployments-api
- collection_type: open
  name: github-repos-api Directories API
  slug: open-github-directories-api
- collection_type: open
  name: Github Disables API
  slug: open-github-disables-api
- collection_type: open
  name: Github Discussions API
  slug: open-github-discussions-api
- collection_type: open
  name: github-repos-api Dismiss API
  slug: open-github-dismiss-api
- collection_type: open
  name: Github Dispatch API
  slug: open-github-dispatch-api
- collection_type: open
  name: GitHub Org Docker API
  slug: open-github-docker-api
- collection_type: open
  name: GitHub Markdown Documents API
  slug: open-github-documents-api
- collection_type: open
  name: Github Download API
  slug: open-github-download-api
- collection_type: open
  name: GitHub Org During API
  slug: open-github-during-api
- collection_type: open
  name: Github Emojis API
  slug: open-github-emojis-api
- collection_type: open
  name: GitHub Emojis API
  slug: open-github-emojis
- collection_type: open
  name: Github Enabled API
  slug: open-github-enabled-api
- collection_type: open
  name: Github Enables API
  slug: open-github-enables-api
- collection_type: open
  name: Github Enforcement API
  slug: open-github-enforcement-api
- collection_type: open
  name: GitHub v3 REST Enterprise Admin API
  slug: open-github-enterprise-admin-api
- collection_type: open
  name: GitHub v3 REST Enterprise-Admin - Scim API
  slug: open-github-enterprise-admin-scim-api
- collection_type: open
  name: Github Enterprise API
  slug: open-github-enterprise-api
- collection_type: open
  name: github-repos-api Environments API
  slug: open-github-environments-api
- collection_type: open
  name: Github Event API
  slug: open-github-event-api
- collection_type: open
  name: Github Events API
  slug: open-github-events-api
- collection_type: open
  name: Github Existing API
  slug: open-github-existing-api
- collection_type: open
  name: github-repos-api Export API
  slug: open-github-export-api
- collection_type: open
  name: Github External API
  slug: open-github-external-api
- collection_type: open
  name: github-repo-actions-api Failed API
  slug: open-github-failed-api
- collection_type: open
  name: GitHub Org Feature API
  slug: open-github-feature-api
- collection_type: open
  name: GitHub Feeds API
  slug: open-github-feeds-api
- collection_type: open
  name: GitHub Feeds API
  slug: open-github-feeds
- collection_type: open
  name: Github Files API
  slug: open-github-files-api
- collection_type: open
  name: GitHub Org Fine Grained API
  slug: open-github-fine-grained-api
- collection_type: open
  name: GitHub Auth Fingerprint API
  slug: open-github-fingerprint-api
- collection_type: open
  name: Github Forks API
  slug: open-github-forks-api
- collection_type: open
  name: github-repos-api Generate API
  slug: open-github-generate-api
- collection_type: open
  name: Github Get API
  slug: open-github-get-api
- collection_type: open
  name: Github Gists API
  slug: open-github-gists-api
- collection_type: open
  name: GitHub Gists API
  slug: open-github-gists
- collection_type: open
  name: Github Git API
  slug: open-github-git-api
- collection_type: open
  name: GitHub Application GitHub Application API API
  slug: open-github-github-application-api-api
- collection_type: open
  name: GitHub Auth GitHub Auth API API
  slug: open-github-github-auth-api-api
- collection_type: open
  name: GitHub Code of Conduct GitHub Code Of Conduct API API
  slug: open-github-github-code-of-conduct-api-api
- collection_type: open
  name: GitHub Codes API
  slug: open-github-github-codes-api
- collection_type: open
  name: GitHub Emojis GitHub Emojis API API
  slug: open-github-github-emojis-api-api
- collection_type: open
  name: GitHub Feeds GitHub Feeds API API
  slug: open-github-github-feeds-api-api
- collection_type: open
  name: GitHub Gists GitHub Gists API API
  slug: open-github-github-gists-api-api
- collection_type: open
  name: GitHub Gitignore Templates GitHub Gitignore Templates API API
  slug: open-github-github-gitignore-templates-api-api
- collection_type: open
  name: GitHub Installation GitHub Installation API API
  slug: open-github-github-installation-api-api
- collection_type: open
  name: GitHub Licenses GitHub Licenses API API
  slug: open-github-github-licenses-api-api
- collection_type: open
  name: GitHub Manage GitHub Manage API API
  slug: open-github-github-manage-api-api
- collection_type: open
  name: GitHub Markdown GitHub Markdown API API
  slug: open-github-github-markdown-api-api
- collection_type: open
  name: GitHub Meta GitHub Meta API API
  slug: open-github-github-meta-api-api
- collection_type: open
  name: GitHub Networks GitHub Networks API API
  slug: open-github-github-networks-api-api
- collection_type: open
  name: GitHub Notifications GitHub Notifications API API
  slug: open-github-github-notifications-api-api
- collection_type: open
  name: GitHub Projects GitHub Projects API API
  slug: open-github-github-projects-api-api
- collection_type: open
  name: GitHub SCIM GitHub SCIM API API
  slug: open-github-github-scim-api-api
- collection_type: open
  name: GitHub v3 REST GitHub V3 REST API API
  slug: open-github-github-v3-rest-api-api
- collection_type: open
  name: GitHub v3 REST Gitignore API
  slug: open-github-gitignore-api
- collection_type: open
  name: GitHub Gitignore Templates API
  slug: open-github-gitignore-templates
- collection_type: open
  name: GitHub Application Grants API
  slug: open-github-grants-api
- collection_type: open
  name: Github Groups API
  slug: open-github-groups-api
- collection_type: open
  name: github-repos-api Head API
  slug: open-github-head-api
- collection_type: open
  name: Github History API
  slug: open-github-history-api
- collection_type: open
  name: Github Hook API
  slug: open-github-hook-api
- collection_type: open
  name: Github Hooks API
  slug: open-github-hooks-api
- collection_type: open
  name: github-repos-api Hourly API
  slug: open-github-hourly-api
- collection_type: open
  name: github-repo-actions-api Identifiers API
  slug: open-github-identifiers-api
- collection_type: open
  name: GitHub SCIM Identities API
  slug: open-github-identities-api
- collection_type: open
  name: GitHub Auth Impersonation API
  slug: open-github-impersonation-api
- collection_type: open
  name: Github Information API
  slug: open-github-information-api
- collection_type: open
  name: GitHub Installation API
  slug: open-github-installation
- collection_type: open
  name: Github Installations API
  slug: open-github-installations-api
- collection_type: open
  name: github-repos-api Instances API
  slug: open-github-instances-api
- collection_type: open
  name: github-repos-api Invitation API
  slug: open-github-invitation-api
- collection_type: open
  name: github-repos-api Invitations API
  slug: open-github-invitations-api
- collection_type: open
  name: Github Issues API
  slug: open-github-issues-api
- collection_type: open
  name: github-repo-actions-api Jobs API
  slug: open-github-jobs-api
- collection_type: open
  name: Github Keys API
  slug: open-github-keys-api
- collection_type: open
  name: github-repo-actions-api Label API
  slug: open-github-label-api
- collection_type: open
  name: Github Labels API
  slug: open-github-labels-api
- collection_type: open
  name: github-repos-api Languages API
  slug: open-github-languages-api
- collection_type: open
  name: github-repos-api Large File Storage API
  slug: open-github-large-file-storage-api
- collection_type: open
  name: github-repos-api Last API
  slug: open-github-last-api
- collection_type: open
  name: github-repos-api Latest API
  slug: open-github-latest-api
- collection_type: open
  name: GitHub Teams Ldap API
  slug: open-github-ldap-api
- collection_type: open
  name: Github Legacy API
  slug: open-github-legacy-api
- collection_type: open
  name: github-repo-actions-api Levels API
  slug: open-github-levels-api
- collection_type: open
  name: Github Licenses API
  slug: open-github-licenses-api
- collection_type: open
  name: GitHub Licenses API
  slug: open-github-licenses
- collection_type: open
  name: GitHub Rate Limit API
  slug: open-github-limit-api
- collection_type: open
  name: Github Lists API
  slug: open-github-lists-api
- collection_type: open
  name: github-repos-api Locks API
  slug: open-github-locks-api
- collection_type: open
  name: GitHub Org Log API
  slug: open-github-log-api
- collection_type: open
  name: github-repo-actions-api Logs API
  slug: open-github-logs-api
- collection_type: open
  name: GitHub Setup Maintenance API
  slug: open-github-maintenance-api
- collection_type: open
  name: GitHub Manage API
  slug: open-github-manage
- collection_type: open
  name: Github Manager API
  slug: open-github-manager-api
- collection_type: open
  name: GitHub Application Manifest API
  slug: open-github-manifest-api
- collection_type: open
  name: GitHub Teams Mapping API
  slug: open-github-mapping-api
- collection_type: open
  name: Github Mark API
  slug: open-github-mark-api
- collection_type: open
  name: Github Markdown API
  slug: open-github-markdown-api
- collection_type: open
  name: GitHub Markdown API
  slug: open-github-markdown
- collection_type: open
  name: github-repos-api Matching API
  slug: open-github-matching-api
- collection_type: open
  name: github-repos-api Materials API
  slug: open-github-materials-api
- collection_type: open
  name: Github Member API
  slug: open-github-member-api
- collection_type: open
  name: Github Members API
  slug: open-github-members-api
- collection_type: open
  name: GitHub Org Membership API
  slug: open-github-membership-api
- collection_type: open
  name: Github Memberships API
  slug: open-github-memberships-api
- collection_type: open
  name: Github Merge API
  slug: open-github-merge-api
- collection_type: open
  name: github-repos-api Merged API
  slug: open-github-merged-api
- collection_type: open
  name: Github Meta API
  slug: open-github-meta-api
- collection_type: open
  name: GitHub Meta API
  slug: open-github-meta
- collection_type: open
  name: Github Migrations API
  slug: open-github-migrations-api
- collection_type: open
  name: github-repos-api Milestones API
  slug: open-github-milestones-api
- collection_type: open
  name: GitHub Markdown Mode API
  slug: open-github-mode-api
- collection_type: open
  name: GitHub Setup Modes API
  slug: open-github-modes-api
- collection_type: open
  name: GitHub Projects Move API
  slug: open-github-move-api
- collection_type: open
  name: Github Name API
  slug: open-github-name-api
- collection_type: open
  name: GitHub Networks Network API
  slug: open-github-network-api
- collection_type: open
  name: GitHub Networks API
  slug: open-github-networks
- collection_type: open
  name: GitHub Manage Node API
  slug: open-github-node-api
- collection_type: open
  name: GitHub Manage Nodes API
  slug: open-github-nodes-api
- collection_type: open
  name: github-repos-api Notes API
  slug: open-github-notes-api
- collection_type: open
  name: github-repos-api Notifications API
  slug: open-github-notifications-api
- collection_type: open
  name: GitHub Notifications API
  slug: open-github-notifications
- collection_type: open
  name: GitHub Auth OAUTH API
  slug: open-github-oauth-api
- collection_type: open
  name: GitHub v3 REST OAUTH Authorizations API
  slug: open-github-oauth-authorizations-api
- collection_type: open
  name: github-repos-api Objects API
  slug: open-github-objects-api
- collection_type: open
  name: GitHub Octocat API
  slug: open-github-octocat-api
- collection_type: open
  name: GitHub Octocat API
  slug: open-github-octocat
- collection_type: open
  name: GitHub v3 REST Oidc API
  slug: open-github-oidc-api
- collection_type: open
  name: Github Openid Connect API
  slug: open-github-openid-connect-api
- collection_type: open
  name: Github Organizations API
  slug: open-github-organizations-api
- collection_type: open
  name: GitHub Org API
  slug: open-github-organizations
- collection_type: open
  name: GitHub v3 REST Orgs API
  slug: open-github-orgs-api
- collection_type: open
  name: Github Outside API
  slug: open-github-outside-api
- collection_type: open
  name: GitHub Org Owned API
  slug: open-github-owned-api
- collection_type: open
  name: GitHub Org Package API
  slug: open-github-package-api
- collection_type: open
  name: Github Packages API
  slug: open-github-packages-api
- collection_type: open
  name: github-repos-api Pages API
  slug: open-github-pages-api
- collection_type: open
  name: Github Pending API
  slug: open-github-pending-api
- collection_type: open
  name: GitHub Projects Permission API
  slug: open-github-permission-api
- collection_type: open
  name: Github Permissions API
  slug: open-github-permissions-api
- collection_type: open
  name: Github Ping API
  slug: open-github-ping-api
- collection_type: open
  name: Github Policies API
  slug: open-github-policies-api
- collection_type: open
  name: Github Pre Receive API
  slug: open-github-pre-receive-api
- collection_type: open
  name: github-repos-api Preferences API
  slug: open-github-preferences-api
- collection_type: open
  name: GitHub Setup Process API
  slug: open-github-process-api
- collection_type: open
  name: Github Project API
  slug: open-github-project-api
- collection_type: open
  name: Github Projects API
  slug: open-github-projects-api
- collection_type: open
  name: GitHub Projects API
  slug: open-github-projects
- collection_type: open
  name: Github Protected API
  slug: open-github-protected-api
- collection_type: open
  name: Github Protections API
  slug: open-github-protections-api
- collection_type: open
  name: GitHub SCIM Provision API
  slug: open-github-provision-api
- collection_type: open
  name: GitHub SCIM Provisioned API
  slug: open-github-provisioned-api
- collection_type: open
  name: GitHub SCIM Provisioning API
  slug: open-github-provisioning-api
- collection_type: open
  name: Github Public API
  slug: open-github-public-api
- collection_type: open
  name: Github Pull API
  slug: open-github-pull-api
- collection_type: open
  name: GitHub v3 REST Pulls API
  slug: open-github-pulls-api
- collection_type: open
  name: github-repo-hooks-api Push API
  slug: open-github-push-api
- collection_type: open
  name: GitHub Limit Rate API
  slug: open-github-rate-api
- collection_type: open
  name: GitHub Rate Limit API
  slug: open-github-rate-limit-
- collection_type: open
  name: GitHub v3 REST Rate Limit API
  slug: open-github-rate-limit-api
- collection_type: open
  name: GitHub Markdown Raw API
  slug: open-github-raw-api
- collection_type: open
  name: Github Re Deliver API
  slug: open-github-re-deliver-api
- collection_type: open
  name: github-repos-api Re Request API
  slug: open-github-re-request-api
- collection_type: open
  name: github-repo-actions-api Re Run API
  slug: open-github-re-run-api
- collection_type: open
  name: github-repos-api Reaction API
  slug: open-github-reaction-api
- collection_type: open
  name: Github Reactions API
  slug: open-github-reactions-api
- collection_type: open
  name: Github Read API
  slug: open-github-read-api
- collection_type: open
  name: github-repos-api Readme API
  slug: open-github-readme-api
- collection_type: open
  name: Github References API
  slug: open-github-references-api
- collection_type: open
  name: Github Registration API
  slug: open-github-registration-api
- collection_type: open
  name: Github Releases API
  slug: open-github-releases-api
- collection_type: open
  name: Github Remove API
  slug: open-github-remove-api
- collection_type: open
  name: github-repos-api Rename API
  slug: open-github-rename-api
- collection_type: open
  name: GitHub Markdown Render API
  slug: open-github-render-api
- collection_type: open
  name: github-repos-api Replace API
  slug: open-github-replace-api
- collection_type: open
  name: GitHub Manage Replicas API
  slug: open-github-replicas-api
- collection_type: open
  name: github-repos-api Replication API
  slug: open-github-replication-api
- collection_type: open
  name: github-repos-api Reply API
  slug: open-github-reply-api
- collection_type: open
  name: github-repo-actions-api
  slug: open-github-repo-actions-api
- collection_type: open
  name: github-repos-api
  slug: open-github-repo-autolinks-api
- collection_type: open
  name: github-repos-api
  slug: open-github-repo-branches-api
- collection_type: open
  name: github-repos-api
  slug: open-github-repo-code-scanning-api
- collection_type: open
  name: github-repos-api
  slug: open-github-repo-collaborators-api
- collection_type: open
  name: github-repos-api
  slug: open-github-repo-dependabot-api
- collection_type: open
  name: github-repo-hooks-api
  slug: open-github-repo-hooks-api
- collection_type: open
  name: github-repos-api
  slug: open-github-repo-invitations-api
- collection_type: open
  name: github-repos-api
  slug: open-github-repo-issues-api
- collection_type: open
  name: github-repos-api
  slug: open-github-repo-projects-api
- collection_type: open
  name: github-repos-api
  slug: open-github-repo-pulls-api
- collection_type: open
  name: github-repos-api
  slug: open-github-repo-subscription-api
- collection_type: open
  name: github-repos-api
  slug: open-github-repo-tags-api
- collection_type: open
  name: Github Repos API
  slug: open-github-repos-api
- collection_type: open
  name: Github Repositories API
  slug: open-github-repositories-api
- collection_type: open
  name: github-repos-api Requested API
  slug: open-github-requested-api
- collection_type: open
  name: Github Requests API
  slug: open-github-requests-api
- collection_type: open
  name: github-repos-api Rerequest API
  slug: open-github-rerequest-api
- collection_type: open
  name: GitHub Application Reset API
  slug: open-github-reset-api
- collection_type: open
  name: GitHub Org Restore API
  slug: open-github-restore-api
- collection_type: open
  name: Github Restrictions API
  slug: open-github-restrictions-api
- collection_type: open
  name: GitHub Installation Revoke API
  slug: open-github-revoke-api
- collection_type: open
  name: GitHub Org Role API
  slug: open-github-role-api
- collection_type: open
  name: GitHub Org Roles API
  slug: open-github-roles-api
- collection_type: open
  name: Github Runners API
  slug: open-github-runners-api
- collection_type: open
  name: GitHub Manage Running API
  slug: open-github-running-api
- collection_type: open
  name: Github Runs API
  slug: open-github-runs-api
- collection_type: open
  name: Github Scanning API
  slug: open-github-scanning-api
- collection_type: open
  name: GitHub SCIM API
  slug: open-github-scim-api
- collection_type: open
  name: GitHub SCIM API
  slug: open-github-scim
- collection_type: open
  name: GitHub Application Scoped API
  slug: open-github-scoped-api
- collection_type: open
  name: Github Search API
  slug: open-github-search-api
- collection_type: open
  name: GitHub v3 REST Secret Scanning API
  slug: open-github-secret-scanning-api
- collection_type: open
  name: Github Secrets API
  slug: open-github-secrets-api
- collection_type: open
  name: GitHub Teams Security API
  slug: open-github-security-api
- collection_type: open
  name: GitHub Org Selected API
  slug: open-github-selected-api
- collection_type: open
  name: Github Self Hosted API
  slug: open-github-self-hosted-api
- collection_type: open
  name: Github Servers API
  slug: open-github-servers-api
- collection_type: open
  name: Github Sets API
  slug: open-github-sets-api
- collection_type: open
  name: Github Settings API
  slug: open-github-settings-api
- collection_type: open
  name: Github Setup API
  slug: open-github-setup-api
- collection_type: open
  name: GitHub Setup API
  slug: open-github-setup
- collection_type: open
  name: github-repos-api Signatures API
  slug: open-github-signatures-api
- collection_type: open
  name: Github Single API
  slug: open-github-single-api
- collection_type: open
  name: github-repos-api Sites API
  slug: open-github-sites-api
- collection_type: open
  name: github-repos-api Software API
  slug: open-github-software-api
- collection_type: open
  name: Github Specific API
  slug: open-github-specific-api
- collection_type: open
  name: Github Ssh API
  slug: open-github-ssh-api
- collection_type: open
  name: GitHub Gists Star API
  slug: open-github-star-api
- collection_type: open
  name: github-repos-api Stargazers API
  slug: open-github-stargazers-api
- collection_type: open
  name: GitHub Gists Starred API
  slug: open-github-starred-api
- collection_type: open
  name: Github Start API
  slug: open-github-start-api
- collection_type: open
  name: github-repos-api State API
  slug: open-github-state-api
- collection_type: open
  name: github-repos-api States API
  slug: open-github-states-api
- collection_type: open
  name: github-repos-api Static Analysis Results Interchange Format API
  slug: open-github-static-analysis-results-interchange-format-api
- collection_type: open
  name: Github Status API
  slug: open-github-status-api
- collection_type: open
  name: github-repos-api Statuses API
  slug: open-github-statuses-api
- collection_type: open
  name: Github Subject API
  slug: open-github-subject-api
- collection_type: open
  name: github-repos-api Submit API
  slug: open-github-submit-api
- collection_type: open
  name: Github Subscriptions API
  slug: open-github-subscriptions-api
- collection_type: open
  name: github-repos-api Suites API
  slug: open-github-suites-api
- collection_type: open
  name: Github Suspend API
  slug: open-github-suspend-api
- collection_type: open
  name: Github Sync API
  slug: open-github-sync-api
- collection_type: open
  name: github-repos-api Tar API
  slug: open-github-tar-api
- collection_type: open
  name: Github Teams API
  slug: open-github-teams-api
- collection_type: open
  name: GitHub Teams API
  slug: open-github-teams
- collection_type: open
  name: Github Templates API
  slug: open-github-templates-api
- collection_type: open
  name: github-repo-hooks-api Tests API
  slug: open-github-tests-api
- collection_type: open
  name: GitHub Notifications Thread API
  slug: open-github-thread-api
- collection_type: open
  name: github-repos-api Timelines API
  slug: open-github-timelines-api
- collection_type: open
  name: Github Tokens API
  slug: open-github-tokens-api
- collection_type: open
  name: github-repos-api Topics API
  slug: open-github-topics-api
- collection_type: open
  name: github-repos-api Transfers API
  slug: open-github-transfers-api
- collection_type: open
  name: github-repos-api Trees API
  slug: open-github-trees-api
- collection_type: open
  name: Github Unlock API
  slug: open-github-unlock-api
- collection_type: open
  name: GitHub Gists Unstar API
  slug: open-github-unstar-api
- collection_type: open
  name: Github Unsuspend API
  slug: open-github-unsuspend-api
- collection_type: open
  name: Github Update API
  slug: open-github-update-api
- collection_type: open
  name: GitHub Setup Upgrade API
  slug: open-github-upgrade-api
- collection_type: open
  name: Github Upload API
  slug: open-github-upload-api
- collection_type: open
  name: github-repos-api Upstream API
  slug: open-github-upstream-api
- collection_type: open
  name: Github Usage API
  slug: open-github-usage-api
- collection_type: open
  name: Github Users API
  slug: open-github-users-api
- collection_type: open
  name: Github Variables API
  slug: open-github-variables-api
- collection_type: open
  name: Github Versions API
  slug: open-github-versions-api
- collection_type: open
  name: github-repos-api Vulnerabilities API
  slug: open-github-vulnerabilities-api
- collection_type: open
  name: github-repos-api Watchers API
  slug: open-github-watchers-api
- collection_type: open
  name: Github Webhooks API
  slug: open-github-webhooks-api
- collection_type: open
  name: github-repos-api Weekly API
  slug: open-github-weekly-api
- collection_type: open
  name: Github Workflows API
  slug: open-github-workflows-api
- collection_type: open
  name: github-repos-api Year API
  slug: open-github-year-api
- collection_type: open
  name: GitHub Zen API
  slug: open-github-zen-api
- collection_type: open
  name: GitHub Zen API
  slug: open-github-zen
- collection_type: open
  name: GitHub v3 REST API
  slug: open-github
- collection_type: open
  name: GitHub Repos API
  slug: open-temp
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/rate-limits/github-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/github-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/pricing
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/plans/github-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/github-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/capabilities/github-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/github-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/agentic-access/github-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/github-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/authentication/github-authentication.yml
  title: ''
  type: Authentication
  url: authentication/github-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://api.githubcopilot.com/mcp/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/github/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-commit-file-to-new-branch-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-commit-file-to-new-branch-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-create-label-and-triage-issue-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-create-label-and-triage-issue-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-create-milestone-and-issue-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-create-milestone-and-issue-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-create-org-repository-and-issue-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-create-org-repository-and-issue-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-create-repository-and-issue-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-create-repository-and-issue-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-dispatch-workflow-and-poll-run-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-dispatch-workflow-and-poll-run-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-fork-and-branch-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-fork-and-branch-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-fork-gist-and-comment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-fork-gist-and-comment-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-inspect-latest-commit-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-inspect-latest-commit-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-onboard-org-member-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-onboard-org-member-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-open-and-merge-pull-request-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-open-and-merge-pull-request-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-open-pull-request-and-request-reviewers-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-open-pull-request-and-request-reviewers-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-propose-change-pull-request-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-propose-change-pull-request-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-provision-org-repo-with-webhook-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-provision-org-repo-with-webhook-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-publish-release-with-asset-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-publish-release-with-asset-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-report-bug-issue-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-report-bug-issue-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-review-and-merge-pull-request-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-review-and-merge-pull-request-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-star-and-comment-gist-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-star-and-comment-gist-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-tag-commit-and-release-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-tag-commit-and-release-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/arazzo/github-verify-and-merge-branch-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/github-verify-and-merge-branch-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/github
- group: commercial
  title: ''
  type: Plans
  url: https://github.com/pricing
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/github/roadmap
- group: company
  title: ''
  type: About
  url: https://github.com/about
- group: docs
  title: ''
  type: Documentation
  url: https://docs.github.com/en/get-started/exploring-integrations/about-building-integrations
- group: operate
  title: ''
  type: StatusPage
  url: https://www.githubstatus.com/
- group: build
  title: ''
  type: CLI
  url: https://cli.github.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/github
- group: operate
  title: ''
  type: Support
  url: https://support.github.com/
- group: company
  title: ''
  type: Partners
  url: https://github.com/partners/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28
- group: design
  title: ''
  type: Pagination
  url: https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api?apiVersion=2022-11-28
- group: auth
  title: ''
  type: Authentication
  url: https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28
- group: build
  title: ''
  type: SDKs
  url: https://docs.github.com/en/rest/overview/libraries
- group: company
  title: ''
  type: Blog
  url: https://github.blog/
- group: company
  title: ''
  type: Website
  url: https://github.com
- group: start
  title: ''
  type: Login
  url: https://github.com/login
- group: start
  title: ''
  type: Signup
  url: https://github.com/signup
- group: start
  title: ''
  type: Portal
  url: https://docs.github.com/en/rest
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.blog/changelog/
- group: operate
  title: ''
  type: Community
  url: https://github.com/orgs/community/discussions
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/github-api
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/github
- group: auth
  title: ''
  type: Security
  url: https://github.com/security
- group: build
  title: ''
  type: DeveloperTools
  url: https://docs.github.com/en/graphql/overview/explorer
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/github/rest-api-description
- group: design
  title: ''
  type: Versioning
  url: https://docs.github.com/en/rest/about-the-rest-api/api-versions
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.github.com/en/rest/quickstart
- group: design
  title: ''
  type: Webhooks
  url: https://docs.github.com/en/webhooks
- group: other
  title: ''
  type: X
  url: https://x.com/github
- group: build
  title: ''
  type: SDKs
  url: https://github.com/octokit
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/json-schema/github-repository-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/github-repository-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/json-schema/github-issue-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/github-issue-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/json-schema/github-pull-request-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/github-pull-request-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/json-schema/github-user-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/github-user-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/json-schema/github-organization-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/github-organization-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/json-schema/github-commit-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/github-commit-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/json-schema/github-webhook-delivery-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/github-webhook-delivery-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/json-ld/github-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/github-context.jsonld
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/github/Skills-Based-Volunteering-Public
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.github.com/llms.txt
created: 2024/04/14
description: The GitHub REST API allows developers to programmatically interact with GitHub resources including repositories, users, organizations, pull requests, issues, and more.
examples:
- key_count: 7
  name: Github App Api Application Grant Example
  slug: github-app-api-application-grant-example
- key_count: 10
  name: Github App Api Authorization Example
  slug: github-app-api-authorization-example
- key_count: 10
  name: Github App Api Hook Delivery Example
  slug: github-app-api-hook-delivery-example
- key_count: 10
  name: Github App Api Installation Example
  slug: github-app-api-installation-example
- key_count: 10
  name: Github App Api Integration Example
  slug: github-app-api-integration-example
- key_count: 4
  name: Github App Api Webhook Config Example
  slug: github-app-api-webhook-config-example
- key_count: 10
  name: Github Auth Api Global Hook 2 Example
  slug: github-auth-api-global-hook-2-example
- key_count: 10
  name: Github Auth Api Global Hook Example
  slug: github-auth-api-global-hook-example
- key_count: 10
  name: Github Auth Api Ldap Mapping Team Example
  slug: github-auth-api-ldap-mapping-team-example
- key_count: 10
  name: Github Auth Api Ldap Mapping User Example
  slug: github-auth-api-ldap-mapping-user-example
- key_count: 10
  name: Github Auth Api Organization Simple Example
  slug: github-auth-api-organization-simple-example
- key_count: 9
  name: Github Auth Api Pre Receive Environment Example
  slug: github-auth-api-pre-receive-environment-example
- key_count: 10
  name: Github Auth Api Public Key Full Example
  slug: github-auth-api-public-key-full-example
- key_count: 10
  name: Github Auth Api Root Example
  slug: github-auth-api-root-example
- key_count: 5
  name: Github Code Of Conduct Api Code Of Conduct Example
  slug: github-code-of-conduct-api-code-of-conduct-example
- key_count: 7
  name: Github Code Of Conduct Api Webhook Branch Protection Rule Created Example
  slug: github-code-of-conduct-api-webhook-branch-protection-rule-created-example
- key_count: 7
  name: Github Code Of Conduct Api Webhook Branch Protection Rule Deleted Example
  slug: github-code-of-conduct-api-webhook-branch-protection-rule-deleted-example
- key_count: 8
  name: Github Code Of Conduct Api Webhook Branch Protection Rule Edited Example
  slug: github-code-of-conduct-api-webhook-branch-protection-rule-edited-example
- key_count: 9
  name: Github Code Of Conduct Api Webhook Cache Sync Example
  slug: github-code-of-conduct-api-webhook-cache-sync-example
- key_count: 6
  name: Github Code Of Conduct Api Webhook Check Run Completed Example
  slug: github-code-of-conduct-api-webhook-check-run-completed-example
- key_count: 1
  name: Github Code Of Conduct Api Webhook Check Run Completed Form Encoded Example
  slug: github-code-of-conduct-api-webhook-check-run-completed-form-encoded-example
- key_count: 6
  name: Github Code Of Conduct Api Webhook Check Run Created Example
  slug: github-code-of-conduct-api-webhook-check-run-created-example
- key_count: 5
  name: Github Codes Code Of Conduct Example
  slug: github-codes-code-of-conduct-example
- key_count: 10
  name: Github Commit Example
  slug: github-commit-example
- key_count: 7
  name: Github Emojis Webhook Branch Protection Rule Created Example
  slug: github-emojis-webhook-branch-protection-rule-created-example
- key_count: 7
  name: Github Emojis Webhook Branch Protection Rule Deleted Example
  slug: github-emojis-webhook-branch-protection-rule-deleted-example
- key_count: 8
  name: Github Emojis Webhook Branch Protection Rule Edited Example
  slug: github-emojis-webhook-branch-protection-rule-edited-example
- key_count: 9
  name: Github Emojis Webhook Cache Sync Example
  slug: github-emojis-webhook-cache-sync-example
- key_count: 6
  name: Github Emojis Webhook Check Run Completed Example
  slug: github-emojis-webhook-check-run-completed-example
- key_count: 1
  name: Github Emojis Webhook Check Run Completed Form Encoded Example
  slug: github-emojis-webhook-check-run-completed-form-encoded-example
- key_count: 10
  name: Github Events Api Global Hook 2 Example
  slug: github-events-api-global-hook-2-example
- key_count: 10
  name: Github Events Api Global Hook Example
  slug: github-events-api-global-hook-example
- key_count: 10
  name: Github Events Api Ldap Mapping Team Example
  slug: github-events-api-ldap-mapping-team-example
- key_count: 10
  name: Github Events Api Ldap Mapping User Example
  slug: github-events-api-ldap-mapping-user-example
- key_count: 10
  name: Github Events Api Organization Simple Example
  slug: github-events-api-organization-simple-example
- key_count: 9
  name: Github Events Api Pre Receive Environment Example
  slug: github-events-api-pre-receive-environment-example
- key_count: 10
  name: Github Events Api Public Key Full Example
  slug: github-events-api-public-key-full-example
- key_count: 10
  name: Github Events Api Root Example
  slug: github-events-api-root-example
- key_count: 10
  name: Github Feeds Feed Example
  slug: github-feeds-feed-example
- key_count: 7
  name: Github Feeds Webhook Branch Protection Rule Created Example
  slug: github-feeds-webhook-branch-protection-rule-created-example
- key_count: 7
  name: Github Feeds Webhook Branch Protection Rule Deleted Example
  slug: github-feeds-webhook-branch-protection-rule-deleted-example
- key_count: 8
  name: Github Feeds Webhook Branch Protection Rule Edited Example
  slug: github-feeds-webhook-branch-protection-rule-edited-example
- key_count: 9
  name: Github Feeds Webhook Cache Sync Example
  slug: github-feeds-webhook-cache-sync-example
- key_count: 6
  name: Github Feeds Webhook Check Run Completed Example
  slug: github-feeds-webhook-check-run-completed-example
- key_count: 10
  name: Github Gists Base Gist Example
  slug: github-gists-base-gist-example
- key_count: 4
  name: Github Gists Basic Error Example
  slug: github-gists-basic-error-example
- key_count: 8
  name: Github Gists Gist Comment Example
  slug: github-gists-gist-comment-example
- key_count: 5
  name: Github Gists Gist Commit Example
  slug: github-gists-gist-commit-example
- key_count: 10
  name: Github Gists Gist Simple Example
  slug: github-gists-gist-simple-example
- key_count: 10
  name: Github Gists Public User Example
  slug: github-gists-public-user-example
- key_count: 3
  name: Github Gists Validation Error Example
  slug: github-gists-validation-error-example
- key_count: 7
  name: Github Gists Webhook Branch Protection Rule Created Example
  slug: github-gists-webhook-branch-protection-rule-created-example
- key_count: 2
  name: Github Gitignore Templates Gitignore Template Example
  slug: github-gitignore-templates-gitignore-template-example
- key_count: 7
  name: Github Gitignore Templates Webhook Branch Protection Rule Created Example
  slug: github-gitignore-templates-webhook-branch-protection-rule-created-example
- key_count: 7
  name: Github Gitignore Templates Webhook Branch Protection Rule Deleted Example
  slug: github-gitignore-templates-webhook-branch-protection-rule-deleted-example
- key_count: 8
  name: Github Gitignore Templates Webhook Branch Protection Rule Edited Example
  slug: github-gitignore-templates-webhook-branch-protection-rule-edited-example
- key_count: 9
  name: Github Gitignore Templates Webhook Cache Sync Example
  slug: github-gitignore-templates-webhook-cache-sync-example
- key_count: 6
  name: Github Gitignore Templates Webhook Check Run Completed Example
  slug: github-gitignore-templates-webhook-check-run-completed-example
- key_count: 1
  name: Github Gitignore Templates Webhook Check Run Completed Form Encoded Example
  slug: github-gitignore-templates-webhook-check-run-completed-form-encoded-example
- key_count: 6
  name: Github Gitignore Templates Webhook Check Run Created Example
  slug: github-gitignore-templates-webhook-check-run-created-example
- key_count: 10
  name: Github Installation App Permissions Example
  slug: github-installation-app-permissions-example
- key_count: 4
  name: Github Installation Basic Error Example
  slug: github-installation-basic-error-example
- key_count: 10
  name: Github Installation Installation Example
  slug: github-installation-installation-example
- key_count: 8
  name: Github Installation Installation Token Example
  slug: github-installation-installation-token-example
- key_count: 5
  name: Github Installation Integration Installation Request Example
  slug: github-installation-integration-installation-request-example
- key_count: 3
  name: Github Installation Validation Error Example
  slug: github-installation-validation-error-example
- key_count: 7
  name: Github Installation Webhook Branch Protection Rule Created Example
  slug: github-installation-webhook-branch-protection-rule-created-example
- key_count: 7
  name: Github Installation Webhook Branch Protection Rule Deleted Example
  slug: github-installation-webhook-branch-protection-rule-deleted-example
- key_count: 10
  name: Github Issue Example
  slug: github-issue-example
- key_count: 10
  name: Github Issues Api Global Hook 2 Example
  slug: github-issues-api-global-hook-2-example
- key_count: 10
  name: Github Issues Api Global Hook Example
  slug: github-issues-api-global-hook-example
- key_count: 10
  name: Github Issues Api Ldap Mapping Team Example
  slug: github-issues-api-ldap-mapping-team-example
- key_count: 10
  name: Github Issues Api Ldap Mapping User Example
  slug: github-issues-api-ldap-mapping-user-example
- key_count: 10
  name: Github Issues Api Organization Simple Example
  slug: github-issues-api-organization-simple-example
- key_count: 9
  name: Github Issues Api Pre Receive Environment Example
  slug: github-issues-api-pre-receive-environment-example
- key_count: 10
  name: Github Issues Api Public Key Full Example
  slug: github-issues-api-public-key-full-example
- key_count: 10
  name: Github Issues Api Root Example
  slug: github-issues-api-root-example
- key_count: 4
  name: Github Licenses Basic Error Example
  slug: github-licenses-basic-error-example
- key_count: 10
  name: Github Licenses License Example
  slug: github-licenses-license-example
- key_count: 7
  name: Github Licenses Webhook Branch Protection Rule Created Example
  slug: github-licenses-webhook-branch-protection-rule-created-example
- key_count: 7
  name: Github Licenses Webhook Branch Protection Rule Deleted Example
  slug: github-licenses-webhook-branch-protection-rule-deleted-example
- key_count: 8
  name: Github Licenses Webhook Branch Protection Rule Edited Example
  slug: github-licenses-webhook-branch-protection-rule-edited-example
- key_count: 9
  name: Github Licenses Webhook Cache Sync Example
  slug: github-licenses-webhook-cache-sync-example
- key_count: 6
  name: Github Licenses Webhook Check Run Completed Example
  slug: github-licenses-webhook-check-run-completed-example
- key_count: 1
  name: Github Licenses Webhook Check Run Completed Form Encoded Example
  slug: github-licenses-webhook-check-run-completed-form-encoded-example
- key_count: 2
  name: Github Manage Ghes Config Nodes Example
  slug: github-manage-ghes-config-nodes-example
- key_count: 2
  name: Github Manage Ghes Replication Status Example
  slug: github-manage-ghes-replication-status-example
- key_count: 7
  name: Github Manage Webhook Branch Protection Rule Created Example
  slug: github-manage-webhook-branch-protection-rule-created-example
- key_count: 7
  name: Github Manage Webhook Branch Protection Rule Deleted Example
  slug: github-manage-webhook-branch-protection-rule-deleted-example
- key_count: 8
  name: Github Manage Webhook Branch Protection Rule Edited Example
  slug: github-manage-webhook-branch-protection-rule-edited-example
- key_count: 9
  name: Github Manage Webhook Cache Sync Example
  slug: github-manage-webhook-cache-sync-example
- key_count: 6
  name: Github Manage Webhook Check Run Completed Example
  slug: github-manage-webhook-check-run-completed-example
- key_count: 7
  name: Github Markdown Webhook Branch Protection Rule Created Example
  slug: github-markdown-webhook-branch-protection-rule-created-example
- key_count: 7
  name: Github Markdown Webhook Branch Protection Rule Deleted Example
  slug: github-markdown-webhook-branch-protection-rule-deleted-example
- key_count: 8
  name: Github Markdown Webhook Branch Protection Rule Edited Example
  slug: github-markdown-webhook-branch-protection-rule-edited-example
- key_count: 9
  name: Github Markdown Webhook Cache Sync Example
  slug: github-markdown-webhook-cache-sync-example
- key_count: 6
  name: Github Markdown Webhook Check Run Completed Example
  slug: github-markdown-webhook-check-run-completed-example
- key_count: 1
  name: Github Markdown Webhook Check Run Completed Form Encoded Example
  slug: github-markdown-webhook-check-run-completed-form-encoded-example
- key_count: 6
  name: Github Markdown Webhook Check Run Created Example
  slug: github-markdown-webhook-check-run-created-example
- key_count: 1
  name: Github Markdown Webhook Check Run Created Form Encoded Example
  slug: github-markdown-webhook-check-run-created-form-encoded-example
- key_count: 5
  name: Github Meta Api Overview Example
  slug: github-meta-api-overview-example
- key_count: 7
  name: Github Meta Webhook Branch Protection Rule Created Example
  slug: github-meta-webhook-branch-protection-rule-created-example
- key_count: 7
  name: Github Meta Webhook Branch Protection Rule Deleted Example
  slug: github-meta-webhook-branch-protection-rule-deleted-example
- key_count: 8
  name: Github Meta Webhook Branch Protection Rule Edited Example
  slug: github-meta-webhook-branch-protection-rule-edited-example
- key_count: 9
  name: Github Meta Webhook Cache Sync Example
  slug: github-meta-webhook-cache-sync-example
- key_count: 6
  name: Github Meta Webhook Check Run Completed Example
  slug: github-meta-webhook-check-run-completed-example
- key_count: 1
  name: Github Meta Webhook Check Run Completed Form Encoded Example
  slug: github-meta-webhook-check-run-completed-form-encoded-example
- key_count: 6
  name: Github Meta Webhook Check Run Created Example
  slug: github-meta-webhook-check-run-created-example
- key_count: 4
  name: Github Networks Basic Error Example
  slug: github-networks-basic-error-example
- key_count: 8
  name: Github Networks Event Example
  slug: github-networks-event-example
- key_count: 7
  name: Github Networks Webhook Branch Protection Rule Created Example
  slug: github-networks-webhook-branch-protection-rule-created-example
- key_count: 7
  name: Github Networks Webhook Branch Protection Rule Deleted Example
  slug: github-networks-webhook-branch-protection-rule-deleted-example
- key_count: 8
  name: Github Networks Webhook Branch Protection Rule Edited Example
  slug: github-networks-webhook-branch-protection-rule-edited-example
- key_count: 9
  name: Github Networks Webhook Cache Sync Example
  slug: github-networks-webhook-cache-sync-example
- key_count: 6
  name: Github Networks Webhook Check Run Completed Example
  slug: github-networks-webhook-check-run-completed-example
- key_count: 1
  name: Github Networks Webhook Check Run Completed Form Encoded Example
  slug: github-networks-webhook-check-run-completed-form-encoded-example
- key_count: 4
  name: Github Notifications Basic Error Example
  slug: github-notifications-basic-error-example
- key_count: 9
  name: Github Notifications Thread Example
  slug: github-notifications-thread-example
- key_count: 7
  name: Github Notifications Thread Subscription Example
  slug: github-notifications-thread-subscription-example
- key_count: 7
  name: Github Notifications Webhook Branch Protection Rule Created Example
  slug: github-notifications-webhook-branch-protection-rule-created-example
- key_count: 7
  name: Github Notifications Webhook Branch Protection Rule Deleted Example
  slug: github-notifications-webhook-branch-protection-rule-deleted-example
- key_count: 8
  name: Github Notifications Webhook Branch Protection Rule Edited Example
  slug: github-notifications-webhook-branch-protection-rule-edited-example
- key_count: 9
  name: Github Notifications Webhook Cache Sync Example
  slug: github-notifications-webhook-cache-sync-example
- key_count: 6
  name: Github Notifications Webhook Check Run Completed Example
  slug: github-notifications-webhook-check-run-completed-example
- key_count: 10
  name: Github Openapi Global Hook 2 Example
  slug: github-openapi-global-hook-2-example
- key_count: 10
  name: Github Openapi Global Hook Example
  slug: github-openapi-global-hook-example
- key_count: 10
  name: Github Openapi Ldap Mapping Team Example
  slug: github-openapi-ldap-mapping-team-example
- key_count: 10
  name: Github Openapi Ldap Mapping User Example
  slug: github-openapi-ldap-mapping-user-example
- key_count: 10
  name: Github Openapi Organization Simple Example
  slug: github-openapi-organization-simple-example
- key_count: 9
  name: Github Openapi Pre Receive Environment Example
  slug: github-openapi-pre-receive-environment-example
- key_count: 10
  name: Github Openapi Public Key Full Example
  slug: github-openapi-public-key-full-example
- key_count: 10
  name: Github Openapi Root Example
  slug: github-openapi-root-example
- key_count: 10
  name: Github Organization Example
  slug: github-organization-example
- key_count: 4
  name: Github Organizations Basic Error Example
  slug: github-organizations-basic-error-example
- key_count: 8
  name: Github Organizations Organization Custom Repository Role Example
  slug: github-organizations-organization-custom-repository-role-example
- key_count: 10
  name: Github Organizations Organization Full Example
  slug: github-organizations-organization-full-example
- key_count: 10
  name: Github Organizations Organization Simple Example
  slug: github-organizations-organization-simple-example
- key_count: 6
  name: Github Organizations Scim Error Example
  slug: github-organizations-scim-error-example
- key_count: 10
  name: Github Organizations Simple User Example
  slug: github-organizations-simple-user-example
- key_count: 3
  name: Github Organizations Validation Error Example
  slug: github-organizations-validation-error-example
- key_count: 3
  name: Github Organizations Validation Error Simple Example
  slug: github-organizations-validation-error-simple-example
- key_count: 4
  name: Github Projects Basic Error Example
  slug: github-projects-basic-error-example
- key_count: 10
  name: Github Projects Project Card Example
  slug: github-projects-project-card-example
- key_count: 2
  name: Github Projects Project Collaborator Permission Example
  slug: github-projects-project-collaborator-permission-example
- key_count: 8
  name: Github Projects Project Column Example
  slug: github-projects-project-column-example
- key_count: 10
  name: Github Projects Project Example
  slug: github-projects-project-example
- key_count: 10
  name: Github Projects Team Project Example
  slug: github-projects-team-project-example
- key_count: 3
  name: Github Projects Validation Error Example
  slug: github-projects-validation-error-example
- key_count: 3
  name: Github Projects Validation Error Simple Example
  slug: github-projects-validation-error-simple-example
- key_count: 10
  name: Github Pull Request Example
  slug: github-pull-request-example
- key_count: 4
  name: Github Rate Limit  Basic Error Example
  slug: github-rate-limit--basic-error-example
- key_count: 4
  name: Github Rate Limit  Rate Limit Example
  slug: github-rate-limit--rate-limit-example
- key_count: 2
  name: Github Rate Limit  Rate Limit Overview Example
  slug: github-rate-limit--rate-limit-overview-example
- key_count: 4
  name: Github Repo Actions Api Basic Error Example
  slug: github-repo-actions-api-basic-error-example
- key_count: 5
  name: Github Repo Actions Api Code Of Conduct Example
  slug: github-repo-actions-api-code-of-conduct-example
- key_count: 6
  name: Github Repo Actions Api Nullable License Simple Example
  slug: github-repo-actions-api-nullable-license-simple-example
- key_count: 10
  name: Github Repo Actions Api Nullable Simple User Example
  slug: github-repo-actions-api-nullable-simple-user-example
- key_count: 10
  name: Github Repo Actions Api Repository Example
  slug: github-repo-actions-api-repository-example
- key_count: 6
  name: Github Repo Actions Api Scim Error Example
  slug: github-repo-actions-api-scim-error-example
- key_count: 10
  name: Github Repo Actions Api Simple User Example
  slug: github-repo-actions-api-simple-user-example
- key_count: 3
  name: Github Repo Actions Api Validation Error Simple Example
  slug: github-repo-actions-api-validation-error-simple-example
- key_count: 4
  name: Github Repo Autolinks Api Autolink Example
  slug: github-repo-autolinks-api-autolink-example
- key_count: 4
  name: Github Repo Autolinks Api Basic Error Example
  slug: github-repo-autolinks-api-basic-error-example
- key_count: 3
  name: Github Repo Autolinks Api Validation Error Example
  slug: github-repo-autolinks-api-validation-error-example
- key_count: 4
  name: Github Repo Branches Api Basic Error Example
  slug: github-repo-branches-api-basic-error-example
- key_count: 10
  name: Github Repo Branches Api Integration Example
  slug: github-repo-branches-api-integration-example
- key_count: 10
  name: Github Repo Branches Api Nullable Simple User Example
  slug: github-repo-branches-api-nullable-simple-user-example
- key_count: 10
  name: Github Repo Branches Api Nullable Team Simple Example
  slug: github-repo-branches-api-nullable-team-simple-example
- key_count: 10
  name: Github Repo Branches Api Simple User Example
  slug: github-repo-branches-api-simple-user-example
- key_count: 3
  name: Github Repo Branches Api Validation Error Example
  slug: github-repo-branches-api-validation-error-example
- key_count: 3
  name: Github Repo Branches Api Validation Error Simple Example
  slug: github-repo-branches-api-validation-error-simple-example
- key_count: 4
  name: Github Repo Code Scanning Api Basic Error Example
  slug: github-repo-code-scanning-api-basic-error-example
- key_count: 10
  name: Github Repo Code Scanning Api Nullable Simple User Example
  slug: github-repo-code-scanning-api-nullable-simple-user-example
- key_count: 6
  name: Github Repo Code Scanning Api Scim Error Example
  slug: github-repo-code-scanning-api-scim-error-example
- key_count: 4
  name: Github Repo Collaborators Api Basic Error Example
  slug: github-repo-collaborators-api-basic-error-example
- key_count: 10
  name: Github Repo Collaborators Api Collaborator Example
  slug: github-repo-collaborators-api-collaborator-example
- key_count: 10
  name: Github Repo Collaborators Api Nullable Collaborator Example
  slug: github-repo-collaborators-api-nullable-collaborator-example
- key_count: 3
  name: Github Repo Collaborators Api Repository Collaborator Permission Example
  slug: github-repo-collaborators-api-repository-collaborator-permission-example
- key_count: 3
  name: Github Repo Collaborators Api Validation Error Example
  slug: github-repo-collaborators-api-validation-error-example
- key_count: 4
  name: Github Repo Dependabot Api Basic Error Example
  slug: github-repo-dependabot-api-basic-error-example
- key_count: 10
  name: Github Repo Dependabot Api Nullable Simple User Example
  slug: github-repo-dependabot-api-nullable-simple-user-example
- key_count: 6
  name: Github Repo Dependabot Api Scim Error Example
  slug: github-repo-dependabot-api-scim-error-example
- key_count: 3
  name: Github Repo Dependabot Api Validation Error Simple Example
  slug: github-repo-dependabot-api-validation-error-simple-example
- key_count: 4
  name: Github Repo Hooks Api Basic Error Example
  slug: github-repo-hooks-api-basic-error-example
- key_count: 10
  name: Github Repo Hooks Api Hook Delivery Item Example
  slug: github-repo-hooks-api-hook-delivery-item-example
- key_count: 6
  name: Github Repo Hooks Api Scim Error Example
  slug: github-repo-hooks-api-scim-error-example
- key_count: 4
  name: Github Repo Hooks Api Webhook Config Example
  slug: github-repo-hooks-api-webhook-config-example
- key_count: 5
  name: Github Repo Invitations Api Code Of Conduct Example
  slug: github-repo-invitations-api-code-of-conduct-example
- key_count: 10
  name: Github Repo Invitations Api Minimal Repository Example
  slug: github-repo-invitations-api-minimal-repository-example
- key_count: 10
  name: Github Repo Invitations Api Nullable Simple User Example
  slug: github-repo-invitations-api-nullable-simple-user-example
- key_count: 10
  name: Github Repo Invitations Api Repository Invitation Example
  slug: github-repo-invitations-api-repository-invitation-example
- key_count: 3
  name: Github Repo Invitations Api Security And Analysis Example
  slug: github-repo-invitations-api-security-and-analysis-example
- key_count: 10
  name: Github Repo Invitations Api Simple User Example
  slug: github-repo-invitations-api-simple-user-example
- key_count: 4
  name: Github Repo Issues Api Basic Error Example
  slug: github-repo-issues-api-basic-error-example
- key_count: 10
  name: Github Repo Issues Api Integration Example
  slug: github-repo-issues-api-integration-example
- key_count: 6
  name: Github Repo Issues Api Nullable License Simple Example
  slug: github-repo-issues-api-nullable-license-simple-example
- key_count: 10
  name: Github Repo Issues Api Nullable Simple User Example
  slug: github-repo-issues-api-nullable-simple-user-example
- key_count: 10
  name: Github Repo Issues Api Repository Example
  slug: github-repo-issues-api-repository-example
- key_count: 6
  name: Github Repo Issues Api Scim Error Example
  slug: github-repo-issues-api-scim-error-example
- key_count: 10
  name: Github Repo Issues Api Simple User Example
  slug: github-repo-issues-api-simple-user-example
- key_count: 3
  name: Github Repo Issues Api Validation Error Example
  slug: github-repo-issues-api-validation-error-example
- key_count: 4
  name: Github Repo Projects Api Basic Error Example
  slug: github-repo-projects-api-basic-error-example
- key_count: 10
  name: Github Repo Projects Api Nullable Simple User Example
  slug: github-repo-projects-api-nullable-simple-user-example
- key_count: 10
  name: Github Repo Projects Api Project Example
  slug: github-repo-projects-api-project-example
- key_count: 3
  name: Github Repo Projects Api Validation Error Simple Example
  slug: github-repo-projects-api-validation-error-simple-example
- key_count: 4
  name: Github Repo Pulls Api Basic Error Example
  slug: github-repo-pulls-api-basic-error-example
- key_count: 6
  name: Github Repo Pulls Api Nullable License Simple Example
  slug: github-repo-pulls-api-nullable-license-simple-example
- key_count: 10
  name: Github Repo Pulls Api Nullable Milestone Example
  slug: github-repo-pulls-api-nullable-milestone-example
- key_count: 10
  name: Github Repo Pulls Api Nullable Simple User Example
  slug: github-repo-pulls-api-nullable-simple-user-example
- key_count: 10
  name: Github Repo Pulls Api Repository Example
  slug: github-repo-pulls-api-repository-example
- key_count: 10
  name: Github Repo Pulls Api Simple User Example
  slug: github-repo-pulls-api-simple-user-example
- key_count: 3
  name: Github Repo Pulls Api Validation Error Example
  slug: github-repo-pulls-api-validation-error-example
- key_count: 3
  name: Github Repo Pulls Api Validation Error Simple Example
  slug: github-repo-pulls-api-validation-error-simple-example
- key_count: 4
  name: Github Repo Subscription Api Basic Error Example
  slug: github-repo-subscription-api-basic-error-example
- key_count: 6
  name: Github Repo Subscription Api Repository Subscription Example
  slug: github-repo-subscription-api-repository-subscription-example
- key_count: 10
  name: Github Repo Tags Api App Permissions Example
  slug: github-repo-tags-api-app-permissions-example
- key_count: 4
  name: Github Repo Tags Api Basic Error Example
  slug: github-repo-tags-api-basic-error-example
- key_count: 10
  name: Github Repo Tags Api Enterprise Example
  slug: github-repo-tags-api-enterprise-example
- key_count: 10
  name: Github Repo Tags Api Nullable Simple User Example
  slug: github-repo-tags-api-nullable-simple-user-example
- key_count: 6
  name: Github Repo Tags Api Scim Error Example
  slug: github-repo-tags-api-scim-error-example
- key_count: 10
  name: Github Repo Tags Api Simple User Example
  slug: github-repo-tags-api-simple-user-example
- key_count: 3
  name: Github Repo Tags Api Validation Error Example
  slug: github-repo-tags-api-validation-error-example
- key_count: 3
  name: Github Repo Tags Api Validation Error Simple Example
  slug: github-repo-tags-api-validation-error-simple-example
- key_count: 10
  name: Github Repos Api App Permissions Example
  slug: github-repos-api-app-permissions-example
- key_count: 4
  name: Github Repos Api Basic Error Example
  slug: github-repos-api-basic-error-example
- key_count: 10
  name: Github Repos Api Enterprise Example
  slug: github-repos-api-enterprise-example
- key_count: 10
  name: Github Repos Api Nullable Simple User Example
  slug: github-repos-api-nullable-simple-user-example
- key_count: 6
  name: Github Repos Api Scim Error Example
  slug: github-repos-api-scim-error-example
- key_count: 10
  name: Github Repos Api Simple User Example
  slug: github-repos-api-simple-user-example
- key_count: 3
  name: Github Repos Api Validation Error Example
  slug: github-repos-api-validation-error-example
- key_count: 3
  name: Github Repos Api Validation Error Simple Example
  slug: github-repos-api-validation-error-simple-example
- key_count: 10
  name: Github Repository Example
  slug: github-repository-example
- key_count: 4
  name: Github Scim Group Response Example
  slug: github-scim-group-response-example
- key_count: 4
  name: Github Scim Meta Example
  slug: github-scim-meta-example
- key_count: 6
  name: Github Scim Scim Error Example
  slug: github-scim-scim-error-example
- key_count: 4
  name: Github Scim User Name Response Example
  slug: github-scim-user-name-response-example
- key_count: 8
  name: Github Scim User Response Example
  slug: github-scim-user-response-example
- key_count: 2
  name: Github Setup Configuration Status Example
  slug: github-setup-configuration-status-example
- key_count: 2
  name: Github Setup Enterprise Settings Example
  slug: github-setup-enterprise-settings-example
- key_count: 3
  name: Github Setup Maintenance Status Example
  slug: github-setup-maintenance-status-example
- key_count: 2
  name: Github Setup Ssh Key Example
  slug: github-setup-ssh-key-example
- key_count: 4
  name: Github Teams Basic Error Example
  slug: github-teams-basic-error-example
- key_count: 10
  name: Github Teams Ldap Mapping Team Example
  slug: github-teams-ldap-mapping-team-example
- key_count: 5
  name: Github Teams Reaction Example
  slug: github-teams-reaction-example
- key_count: 10
  name: Github Teams Team Discussion Comment Example
  slug: github-teams-team-discussion-comment-example
- key_count: 10
  name: Github Teams Team Discussion Example
  slug: github-teams-team-discussion-example
- key_count: 10
  name: Github Teams Team Example
  slug: github-teams-team-example
- key_count: 10
  name: Github Teams Team Full Example
  slug: github-teams-team-full-example
- key_count: 3
  name: Github Teams Validation Error Example
  slug: github-teams-validation-error-example
- key_count: 10
  name: Github User Example
  slug: github-user-example
- key_count: 4
  name: Github Users Api Basic Error Example
  slug: github-users-api-basic-error-example
- key_count: 10
  name: Github Users Api Ldap Mapping User Example
  slug: github-users-api-ldap-mapping-user-example
- key_count: 10
  name: Github Users Api Public User Example
  slug: github-users-api-public-user-example
- key_count: 6
  name: Github Users Api Scim Error Example
  slug: github-users-api-scim-error-example
- key_count: 10
  name: Github Users Api Simple User Example
  slug: github-users-api-simple-user-example
- key_count: 2
  name: Github Users Api Starred Repository Example
  slug: github-users-api-starred-repository-example
- key_count: 3
  name: Github Users Api Validation Error Example
  slug: github-users-api-validation-error-example
- key_count: 3
  name: Github Users Api Validation Error Simple Example
  slug: github-users-api-validation-error-simple-example
- key_count: 10
  name: Github Webhook Delivery Example
  slug: github-webhook-delivery-example
features:
- REST API and GraphQL API for repositories, issues, PRs, releases, and Actions
- GitHub Apps with up to 15,000 requests/hour on Enterprise Cloud
- OAuth App authorization and fine-grained personal access tokens
- GitHub Actions workflow execution with self-hosted and GitHub-hosted runners
- GitHub Packages container, npm, Maven, NuGet, RubyGems, and Gradle registries
- GitHub Codespaces cloud development environments
- GitHub Copilot AI pair programmer (separate per-seat licensing)
- Audit log API and webhook event delivery
- Branch protection, required reviewers, code owners, environments
- 'Secondary rate limits: 100 concurrent / 900 points-per-minute / 80 content-generating-per-minute'
- Git LFS API at 3,000 requests/minute (authenticated)
- Conditional requests with ETag/If-None-Match return 304 without consuming rate limit
- OIDC token exchange for cloud provider federation
- SAML SSO, SCIM, and SSH certificate authority on Enterprise Cloud
- GitHub Marketplace for app distribution and billing
finops:
- name: Github Finops
  service_category: Developer Platform
  slug: github-finops
graphqls:
- description: The GitHub GraphQL API provides a flexible query language for accessing GitHub data, allowing clients to request exactly the fields they need in a single request. It supports queries, mutations, and s
  name: GitHub GraphQL API
  slug: github-graphql
image: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png
json_schemas:
- name: application-grant
  property_count: 7
  slug: github-app-api-application-grant
- name: authorization
  property_count: 15
  slug: github-app-api-authorization
- name: hook-delivery
  property_count: 14
  slug: github-app-api-hook-delivery
- name: installation
  property_count: 20
  slug: github-app-api-installation
- name: integration
  property_count: 17
  slug: github-app-api-integration
- name: webhook-config
  property_count: 4
  slug: github-app-api-webhook-config
- name: global-hook-2
  property_count: 10
  slug: github-auth-api-global-hook-2
- name: global-hook
  property_count: 10
  slug: github-auth-api-global-hook
- name: ldap-mapping-team
  property_count: 13
  slug: github-auth-api-ldap-mapping-team
- name: ldap-mapping-user
  property_count: 42
  slug: github-auth-api-ldap-mapping-user
- name: organization-simple
  property_count: 12
  slug: github-auth-api-organization-simple
- name: pre-receive-environment
  property_count: 9
  slug: github-auth-api-pre-receive-environment
- name: public-key-full
  property_count: 11
  slug: github-auth-api-public-key-full
- name: root
  property_count: 33
  slug: github-auth-api-root
- name: code-of-conduct
  property_count: 5
  slug: github-code-of-conduct-api-code-of-conduct
- name: webhook-branch-protection-rule-created
  property_count: 7
  slug: github-code-of-conduct-api-webhook-branch-protection-rule-created
- name: webhook-branch-protection-rule-deleted
  property_count: 7
  slug: github-code-of-conduct-api-webhook-branch-protection-rule-deleted
- name: webhook-branch-protection-rule-edited
  property_count: 8
  slug: github-code-of-conduct-api-webhook-branch-protection-rule-edited
- name: webhook-cache-sync
  property_count: 9
  slug: github-code-of-conduct-api-webhook-cache-sync
- name: webhook-check-run-completed-form-encoded
  property_count: 1
  slug: github-code-of-conduct-api-webhook-check-run-completed-form-encoded
- name: webhook-check-run-completed
  property_count: 6
  slug: github-code-of-conduct-api-webhook-check-run-completed
- name: webhook-check-run-created
  property_count: 6
  slug: github-code-of-conduct-api-webhook-check-run-created
- name: code-of-conduct
  property_count: 5
  slug: github-codes-code-of-conduct
- name: GitHub Commit
  property_count: 11
  slug: github-commit
- name: webhook-branch-protection-rule-created
  property_count: 7
  slug: github-emojis-webhook-branch-protection-rule-created
- name: webhook-branch-protection-rule-deleted
  property_count: 7
  slug: github-emojis-webhook-branch-protection-rule-deleted
- name: webhook-branch-protection-rule-edited
  property_count: 8
  slug: github-emojis-webhook-branch-protection-rule-edited
- name: webhook-cache-sync
  property_count: 9
  slug: github-emojis-webhook-cache-sync
- name: webhook-check-run-completed-form-encoded
  property_count: 1
  slug: github-emojis-webhook-check-run-completed-form-encoded
- name: webhook-check-run-completed
  property_count: 6
  slug: github-emojis-webhook-check-run-completed
- name: global-hook-2
  property_count: 10
  slug: github-events-api-global-hook-2
- name: global-hook
  property_count: 10
  slug: github-events-api-global-hook
- name: ldap-mapping-team
  property_count: 13
  slug: github-events-api-ldap-mapping-team
- name: ldap-mapping-user
  property_count: 42
  slug: github-events-api-ldap-mapping-user
- name: organization-simple
  property_count: 12
  slug: github-events-api-organization-simple
- name: pre-receive-environment
  property_count: 9
  slug: github-events-api-pre-receive-environment
- name: public-key-full
  property_count: 11
  slug: github-events-api-public-key-full
- name: root
  property_count: 33
  slug: github-events-api-root
- name: feed
  property_count: 11
  slug: github-feeds-feed
- name: webhook-branch-protection-rule-created
  property_count: 7
  slug: github-feeds-webhook-branch-protection-rule-created
- name: webhook-branch-protection-rule-deleted
  property_count: 7
  slug: github-feeds-webhook-branch-protection-rule-deleted
- name: webhook-branch-protection-rule-edited
  property_count: 8
  slug: github-feeds-webhook-branch-protection-rule-edited
- name: webhook-cache-sync
  property_count: 9
  slug: github-feeds-webhook-cache-sync
- name: webhook-check-run-completed
  property_count: 6
  slug: github-feeds-webhook-check-run-completed
- name: base-gist
  property_count: 20
  slug: github-gists-base-gist
- name: basic-error
  property_count: 4
  slug: github-gists-basic-error
- name: gist-comment
  property_count: 8
  slug: github-gists-gist-comment
- name: gist-commit
  property_count: 5
  slug: github-gists-gist-commit
- name: gist-simple
  property_count: 21
  slug: github-gists-gist-simple
- name: public-user
  property_count: 39
  slug: github-gists-public-user
- name: validation-error
  property_count: 3
  slug: github-gists-validation-error
- name: webhook-branch-protection-rule-created
  property_count: 7
  slug: github-gists-webhook-branch-protection-rule-created
- name: gitignore-template
  property_count: 2
  slug: github-gitignore-templates-gitignore-template
- name: webhook-branch-protection-rule-created
  property_count: 7
  slug: github-gitignore-templates-webhook-branch-protection-rule-created
- name: webhook-branch-protection-rule-deleted
  property_count: 7
  slug: github-gitignore-templates-webhook-branch-protection-rule-deleted
- name: webhook-branch-protection-rule-edited
  property_count: 8
  slug: github-gitignore-templates-webhook-branch-protection-rule-edited
- name: webhook-cache-sync
  property_count: 9
  slug: github-gitignore-templates-webhook-cache-sync
- name: webhook-check-run-completed-form-encoded
  property_count: 1
  slug: github-gitignore-templates-webhook-check-run-completed-form-encoded
- name: webhook-check-run-completed
  property_count: 6
  slug: github-gitignore-templates-webhook-check-run-completed
- name: webhook-check-run-created
  property_count: 6
  slug: github-gitignore-templates-webhook-check-run-created
- name: app-permissions
  property_count: 45
  slug: github-installation-app-permissions
- name: basic-error
  property_count: 4
  slug: github-installation-basic-error
- name: installation
  property_count: 20
  slug: github-installation-installation
- name: installation-token
  property_count: 8
  slug: github-installation-installation-token
- name: integration-installation-request
  property_count: 5
  slug: github-installation-integration-installation-request
- name: validation-error
  property_count: 3
  slug: github-installation-validation-error
- name: webhook-branch-protection-rule-created
  property_count: 7
  slug: github-installation-webhook-branch-protection-rule-created
- name: webhook-branch-protection-rule-deleted
  property_count: 7
  slug: github-installation-webhook-branch-protection-rule-deleted
- name: GitHub Issue
  property_count: 24
  slug: github-issue
- name: global-hook-2
  property_count: 10
  slug: github-issues-api-global-hook-2
- name: global-hook
  property_count: 10
  slug: github-issues-api-global-hook
- name: ldap-mapping-team
  property_count: 13
  slug: github-issues-api-ldap-mapping-team
- name: ldap-mapping-user
  property_count: 42
  slug: github-issues-api-ldap-mapping-user
- name: organization-simple
  property_count: 12
  slug: github-issues-api-organization-simple
- name: pre-receive-environment
  property_count: 9
  slug: github-issues-api-pre-receive-environment
- name: public-key-full
  property_count: 11
  slug: github-issues-api-public-key-full
- name: root
  property_count: 33
  slug: github-issues-api-root
- name: basic-error
  property_count: 4
  slug: github-licenses-basic-error
- name: license
  property_count: 13
  slug: github-licenses-license
- name: webhook-branch-protection-rule-created
  property_count: 7
  slug: github-licenses-webhook-branch-protection-rule-created
- name: webhook-branch-protection-rule-deleted
  property_count: 7
  slug: github-licenses-webhook-branch-protection-rule-deleted
- name: webhook-branch-protection-rule-edited
  property_count: 8
  slug: github-licenses-webhook-branch-protection-rule-edited
- name: webhook-cache-sync
  property_count: 9
  slug: github-licenses-webhook-cache-sync
- name: webhook-check-run-completed-form-encoded
  property_count: 1
  slug: github-licenses-webhook-check-run-completed-form-encoded
- name: webhook-check-run-completed
  property_count: 6
  slug: github-licenses-webhook-check-run-completed
- name: ghes-config-nodes
  property_count: 2
  slug: github-manage-ghes-config-nodes
- name: ghes-replication-status
  property_count: 2
  slug: github-manage-ghes-replication-status
- name: webhook-branch-protection-rule-created
  property_count: 7
  slug: github-manage-webhook-branch-protection-rule-created
- name: webhook-branch-protection-rule-deleted
  property_count: 7
  slug: github-manage-webhook-branch-protection-rule-deleted
- name: webhook-branch-protection-rule-edited
  property_count: 8
  slug: github-manage-webhook-branch-protection-rule-edited
- name: webhook-cache-sync
  property_count: 9
  slug: github-manage-webhook-cache-sync
- name: webhook-check-run-completed
  property_count: 6
  slug: github-manage-webhook-check-run-completed
- name: webhook-branch-protection-rule-created
  property_count: 7
  slug: github-markdown-webhook-branch-protection-rule-created
- name: webhook-branch-protection-rule-deleted
  property_count: 7
  slug: github-markdown-webhook-branch-protection-rule-deleted
- name: webhook-branch-protection-rule-edited
  property_count: 8
  slug: github-markdown-webhook-branch-protection-rule-edited
- name: webhook-cache-sync
  property_count: 9
  slug: github-markdown-webhook-cache-sync
- name: webhook-check-run-completed-form-encoded
  property_count: 1
  slug: github-markdown-webhook-check-run-completed-form-encoded
- name: webhook-check-run-completed
  property_count: 6
  slug: github-markdown-webhook-check-run-completed
- name: webhook-check-run-created-form-encoded
  property_count: 1
  slug: github-markdown-webhook-check-run-created-form-encoded
- name: webhook-check-run-created
  property_count: 6
  slug: github-markdown-webhook-check-run-created
- name: api-overview
  property_count: 5
  slug: github-meta-api-overview
- name: webhook-branch-protection-rule-created
  property_count: 7
  slug: github-meta-webhook-branch-protection-rule-created
- name: webhook-branch-protection-rule-deleted
  property_count: 7
  slug: github-meta-webhook-branch-protection-rule-deleted
- name: webhook-branch-protection-rule-edited
  property_count: 8
  slug: github-meta-webhook-branch-protection-rule-edited
- name: webhook-cache-sync
  property_count: 9
  slug: github-meta-webhook-cache-sync
- name: webhook-check-run-completed-form-encoded
  property_count: 1
  slug: github-meta-webhook-check-run-completed-form-encoded
- name: webhook-check-run-completed
  property_count: 6
  slug: github-meta-webhook-check-run-completed
- name: webhook-check-run-created
  property_count: 6
  slug: github-meta-webhook-check-run-created
- name: basic-error
  property_count: 4
  slug: github-networks-basic-error
- name: event
  property_count: 8
  slug: github-networks-event
- name: webhook-branch-protection-rule-created
  property_count: 7
  slug: github-networks-webhook-branch-protection-rule-created
- name: webhook-branch-protection-rule-deleted
  property_count: 7
  slug: github-networks-webhook-branch-protection-rule-deleted
- name: webhook-branch-protection-rule-edited
  property_count: 8
  slug: github-networks-webhook-branch-protection-rule-edited
- name: webhook-cache-sync
  property_count: 9
  slug: github-networks-webhook-cache-sync
- name: webhook-check-run-completed-form-encoded
  property_count: 1
  slug: github-networks-webhook-check-run-completed-form-encoded
- name: webhook-check-run-completed
  property_count: 6
  slug: github-networks-webhook-check-run-completed
- name: basic-error
  property_count: 4
  slug: github-notifications-basic-error
- name: thread
  property_count: 9
  slug: github-notifications-thread
- name: thread-subscription
  property_count: 7
  slug: github-notifications-thread-subscription
- name: webhook-branch-protection-rule-created
  property_count: 7
  slug: github-notifications-webhook-branch-protection-rule-created
- name: webhook-branch-protection-rule-deleted
  property_count: 7
  slug: github-notifications-webhook-branch-protection-rule-deleted
- name: webhook-branch-protection-rule-edited
  property_count: 8
  slug: github-notifications-webhook-branch-protection-rule-edited
- name: webhook-cache-sync
  property_count: 9
  slug: github-notifications-webhook-cache-sync
- name: webhook-check-run-completed
  property_count: 6
  slug: github-notifications-webhook-check-run-completed
- name: global-hook-2
  property_count: 10
  slug: github-openapi-global-hook-2
- name: global-hook
  property_count: 10
  slug: github-openapi-global-hook
- name: ldap-mapping-team
  property_count: 13
  slug: github-openapi-ldap-mapping-team
- name: ldap-mapping-user
  property_count: 42
  slug: github-openapi-ldap-mapping-user
- name: organization-simple
  property_count: 12
  slug: github-openapi-organization-simple
- name: pre-receive-environment
  property_count: 9
  slug: github-openapi-pre-receive-environment
- name: public-key-full
  property_count: 11
  slug: github-openapi-public-key-full
- name: root
  property_count: 33
  slug: github-openapi-root
- name: GitHub Organization
  property_count: 37
  slug: github-organization
- name: basic-error
  property_count: 4
  slug: github-organizations-basic-error
- name: organization-custom-repository-role
  property_count: 8
  slug: github-organizations-organization-custom-repository-role
- name: organization-full
  property_count: 56
  slug: github-organizations-organization-full
- name: organization-simple
  property_count: 12
  slug: github-organizations-organization-simple
- name: scim-error
  property_count: 6
  slug: github-organizations-scim-error
- name: simple-user
  property_count: 21
  slug: github-organizations-simple-user
- name: validation-error
  property_count: 3
  slug: github-organizations-validation-error
- name: validation-error-simple
  property_count: 3
  slug: github-organizations-validation-error-simple
- name: basic-error
  property_count: 4
  slug: github-projects-basic-error
- name: project-card
  property_count: 13
  slug: github-projects-project-card
- name: project-collaborator-permission
  property_count: 2
  slug: github-projects-project-collaborator-permission
- name: project-column
  property_count: 8
  slug: github-projects-project-column
- name: project
  property_count: 15
  slug: github-projects-project
- name: team-project
  property_count: 16
  slug: github-projects-team-project
- name: validation-error
  property_count: 3
  slug: github-projects-validation-error
- name: validation-error-simple
  property_count: 3
  slug: github-projects-validation-error-simple
- name: GitHub Pull Request
  property_count: 36
  slug: github-pull-request
- name: basic-error
  property_count: 4
  slug: github-rate-limit--basic-error
- name: rate-limit-overview
  property_count: 2
  slug: github-rate-limit--rate-limit-overview
- name: rate-limit
  property_count: 4
  slug: github-rate-limit--rate-limit
- name: basic-error
  property_count: 4
  slug: github-repo-actions-api-basic-error
- name: code-of-conduct
  property_count: 5
  slug: github-repo-actions-api-code-of-conduct
- name: nullable-license-simple
  property_count: 6
  slug: github-repo-actions-api-nullable-license-simple
- name: nullable-simple-user
  property_count: 21
  slug: github-repo-actions-api-nullable-simple-user
- name: repository
  property_count: 95
  slug: github-repo-actions-api-repository
- name: scim-error
  property_count: 6
  slug: github-repo-actions-api-scim-error
- name: simple-user
  property_count: 21
  slug: github-repo-actions-api-simple-user
- name: validation-error-simple
  property_count: 3
  slug: github-repo-actions-api-validation-error-simple
- name: autolink
  property_count: 4
  slug: github-repo-autolinks-api-autolink
- name: basic-error
  property_count: 4
  slug: github-repo-autolinks-api-basic-error
- name: validation-error
  property_count: 3
  slug: github-repo-autolinks-api-validation-error
- name: basic-error
  property_count: 4
  slug: github-repo-branches-api-basic-error
- name: integration
  property_count: 17
  slug: github-repo-branches-api-integration
- name: nullable-simple-user
  property_count: 21
  slug: github-repo-branches-api-nullable-simple-user
- name: nullable-team-simple
  property_count: 12
  slug: github-repo-branches-api-nullable-team-simple
- name: simple-user
  property_count: 21
  slug: github-repo-branches-api-simple-user
- name: validation-error
  property_count: 3
  slug: github-repo-branches-api-validation-error
- name: validation-error-simple
  property_count: 3
  slug: github-repo-branches-api-validation-error-simple
- name: basic-error
  property_count: 4
  slug: github-repo-code-scanning-api-basic-error
- name: nullable-simple-user
  property_count: 21
  slug: github-repo-code-scanning-api-nullable-simple-user
- name: scim-error
  property_count: 6
  slug: github-repo-code-scanning-api-scim-error
- name: basic-error
  property_count: 4
  slug: github-repo-collaborators-api-basic-error
- name: collaborator
  property_count: 22
  slug: github-repo-collaborators-api-collaborator
- name: nullable-collaborator
  property_count: 22
  slug: github-repo-collaborators-api-nullable-collaborator
- name: repository-collaborator-permission
  property_count: 3
  slug: github-repo-collaborators-api-repository-collaborator-permission
- name: validation-error
  property_count: 3
  slug: github-repo-collaborators-api-validation-error
- name: basic-error
  property_count: 4
  slug: github-repo-dependabot-api-basic-error
- name: nullable-simple-user
  property_count: 21
  slug: github-repo-dependabot-api-nullable-simple-user
- name: scim-error
  property_count: 6
  slug: github-repo-dependabot-api-scim-error
- name: validation-error-simple
  property_count: 3
  slug: github-repo-dependabot-api-validation-error-simple
- name: basic-error
  property_count: 4
  slug: github-repo-hooks-api-basic-error
- name: hook-delivery-item
  property_count: 12
  slug: github-repo-hooks-api-hook-delivery-item
- name: scim-error
  property_count: 6
  slug: github-repo-hooks-api-scim-error
- name: webhook-config
  property_count: 4
  slug: github-repo-hooks-api-webhook-config
- name: code-of-conduct
  property_count: 5
  slug: github-repo-invitations-api-code-of-conduct
- name: minimal-repository
  property_count: 87
  slug: github-repo-invitations-api-minimal-repository
- name: nullable-simple-user
  property_count: 21
  slug: github-repo-invitations-api-nullable-simple-user
- name: repository-invitation
  property_count: 10
  slug: github-repo-invitations-api-repository-invitation
- name: security-and-analysis
  property_count: 3
  slug: github-repo-invitations-api-security-and-analysis
- name: simple-user
  property_count: 21
  slug: github-repo-invitations-api-simple-user
- name: basic-error
  property_count: 4
  slug: github-repo-issues-api-basic-error
- name: integration
  property_count: 17
  slug: github-repo-issues-api-integration
- name: nullable-license-simple
  property_count: 6
  slug: github-repo-issues-api-nullable-license-simple
- name: nullable-simple-user
  property_count: 21
  slug: github-repo-issues-api-nullable-simple-user
- name: repository
  property_count: 95
  slug: github-repo-issues-api-repository
- name: scim-error
  property_count: 6
  slug: github-repo-issues-api-scim-error
- name: simple-user
  property_count: 21
  slug: github-repo-issues-api-simple-user
- name: validation-error
  property_count: 3
  slug: github-repo-issues-api-validation-error
- name: basic-error
  property_count: 4
  slug: github-repo-projects-api-basic-error
- name: nullable-simple-user
  property_count: 21
  slug: github-repo-projects-api-nullable-simple-user
- name: project
  property_count: 15
  slug: github-repo-projects-api-project
- name: validation-error-simple
  property_count: 3
  slug: github-repo-projects-api-validation-error-simple
- name: basic-error
  property_count: 4
  slug: github-repo-pulls-api-basic-error
- name: nullable-license-simple
  property_count: 6
  slug: github-repo-pulls-api-nullable-license-simple
- name: nullable-milestone
  property_count: 16
  slug: github-repo-pulls-api-nullable-milestone
- name: nullable-simple-user
  property_count: 21
  slug: github-repo-pulls-api-nullable-simple-user
- name: repository
  property_count: 95
  slug: github-repo-pulls-api-repository
- name: simple-user
  property_count: 21
  slug: github-repo-pulls-api-simple-user
- name: validation-error
  property_count: 3
  slug: github-repo-pulls-api-validation-error
- name: validation-error-simple
  property_count: 3
  slug: github-repo-pulls-api-validation-error-simple
- name: basic-error
  property_count: 4
  slug: github-repo-subscription-api-basic-error
- name: repository-subscription
  property_count: 6
  slug: github-repo-subscription-api-repository-subscription
- name: app-permissions
  property_count: 45
  slug: github-repo-tags-api-app-permissions
- name: basic-error
  property_count: 4
  slug: github-repo-tags-api-basic-error
- name: enterprise
  property_count: 10
  slug: github-repo-tags-api-enterprise
- name: nullable-simple-user
  property_count: 21
  slug: github-repo-tags-api-nullable-simple-user
- name: scim-error
  property_count: 6
  slug: github-repo-tags-api-scim-error
- name: simple-user
  property_count: 21
  slug: github-repo-tags-api-simple-user
- name: validation-error
  property_count: 3
  slug: github-repo-tags-api-validation-error
- name: validation-error-simple
  property_count: 3
  slug: github-repo-tags-api-validation-error-simple
- name: app-permissions
  property_count: 45
  slug: github-repos-api-app-permissions
- name: basic-error
  property_count: 4
  slug: github-repos-api-basic-error
- name: enterprise
  property_count: 10
  slug: github-repos-api-enterprise
- name: nullable-simple-user
  property_count: 21
  slug: github-repos-api-nullable-simple-user
- name: scim-error
  property_count: 6
  slug: github-repos-api-scim-error
- name: simple-user
  property_count: 21
  slug: github-repos-api-simple-user
- name: validation-error
  property_count: 3
  slug: github-repos-api-validation-error
- name: validation-error-simple
  property_count: 3
  slug: github-repos-api-validation-error-simple
- name: GitHub Repository
  property_count: 35
  slug: github-repository
- name: group-response
  property_count: 4
  slug: github-scim-group-response
- name: meta
  property_count: 4
  slug: github-scim-meta
- name: scim-error
  property_count: 6
  slug: github-scim-scim-error
- name: user-name-response
  property_count: 4
  slug: github-scim-user-name-response
- name: user-response
  property_count: 8
  slug: github-scim-user-response
- name: configuration-status
  property_count: 2
  slug: github-setup-configuration-status
- name: enterprise-settings
  property_count: 2
  slug: github-setup-enterprise-settings
- name: maintenance-status
  property_count: 3
  slug: github-setup-maintenance-status
- name: ssh-key
  property_count: 2
  slug: github-setup-ssh-key
- name: basic-error
  property_count: 4
  slug: github-teams-basic-error
- name: ldap-mapping-team
  property_count: 13
  slug: github-teams-ldap-mapping-team
- name: reaction
  property_count: 5
  slug: github-teams-reaction
- name: team-discussion-comment
  property_count: 13
  slug: github-teams-team-discussion-comment
- name: team-discussion
  property_count: 18
  slug: github-teams-team-discussion
- name: team-full
  property_count: 18
  slug: github-teams-team-full
- name: team
  property_count: 13
  slug: github-teams-team
- name: validation-error
  property_count: 3
  slug: github-teams-validation-error
- name: GitHub User
  property_count: 28
  slug: github-user
- name: basic-error
  property_count: 4
  slug: github-users-api-basic-error
- name: ldap-mapping-user
  property_count: 42
  slug: github-users-api-ldap-mapping-user
- name: public-user
  property_count: 39
  slug: github-users-api-public-user
- name: scim-error
  property_count: 6
  slug: github-users-api-scim-error
- name: simple-user
  property_count: 21
  slug: github-users-api-simple-user
- name: starred-repository
  property_count: 2
  slug: github-users-api-starred-repository
- name: validation-error
  property_count: 3
  slug: github-users-api-validation-error
- name: validation-error-simple
  property_count: 3
  slug: github-users-api-validation-error-simple
- name: GitHub Webhook Delivery
  property_count: 14
  slug: github-webhook-delivery
json_structures:
- name: Github App Api Application Grant Structure
  property_count: 7
  slug: github-app-api-application-grant-structure
- name: Github App Api Authorization Structure
  property_count: 15
  slug: github-app-api-authorization-structure
- name: Github App Api Hook Delivery Structure
  property_count: 14
  slug: github-app-api-hook-delivery-structure
- name: Github App Api Installation Structure
  property_count: 20
  slug: github-app-api-installation-structure
- name: Github App Api Integration Structure
  property_count: 17
  slug: github-app-api-integration-structure
- name: Github App Api Webhook Config Structure
  property_count: 4
  slug: github-app-api-webhook-config-structure
- name: Github Auth Api Global Hook 2 Structure
  property_count: 10
  slug: github-auth-api-global-hook-2-structure
- name: Github Auth Api Global Hook Structure
  property_count: 10
  slug: github-auth-api-global-hook-structure
- name: Github Auth Api Ldap Mapping Team Structure
  property_count: 13
  slug: github-auth-api-ldap-mapping-team-structure
- name: Github Auth Api Ldap Mapping User Structure
  property_count: 42
  slug: github-auth-api-ldap-mapping-user-structure
- name: Github Auth Api Organization Simple Structure
  property_count: 12
  slug: github-auth-api-organization-simple-structure
- name: Github Auth Api Pre Receive Environment Structure
  property_count: 9
  slug: github-auth-api-pre-receive-environment-structure
- name: Github Auth Api Public Key Full Structure
  property_count: 11
  slug: github-auth-api-public-key-full-structure
- name: Github Auth Api Root Structure
  property_count: 33
  slug: github-auth-api-root-structure
- name: Github Code Of Conduct Api Code Of Conduct Structure
  property_count: 5
  slug: github-code-of-conduct-api-code-of-conduct-structure
- name: Github Code Of Conduct Api Webhook Branch Protection Rule Created Structure
  property_count: 7
  slug: github-code-of-conduct-api-webhook-branch-protection-rule-created-structure
- name: Github Code Of Conduct Api Webhook Branch Protection Rule Deleted Structure
  property_count: 7
  slug: github-code-of-conduct-api-webhook-branch-protection-rule-deleted-structure
- name: Github Code Of Conduct Api Webhook Branch Protection Rule Edited Structure
  property_count: 8
  slug: github-code-of-conduct-api-webhook-branch-protection-rule-edited-structure
- name: Github Code Of Conduct Api Webhook Cache Sync Structure
  property_count: 9
  slug: github-code-of-conduct-api-webhook-cache-sync-structure
- name: Github Code Of Conduct Api Webhook Check Run Completed Form Encoded Structure
  property_count: 1
  slug: github-code-of-conduct-api-webhook-check-run-completed-form-encoded-structure
- name: Github Code Of Conduct Api Webhook Check Run Completed Structure
  property_count: 6
  slug: github-code-of-conduct-api-webhook-check-run-completed-structure
- name: Github Code Of Conduct Api Webhook Check Run Created Structure
  property_count: 6
  slug: github-code-of-conduct-api-webhook-check-run-created-structure
- name: Github Codes Code Of Conduct Structure
  property_count: 5
  slug: github-codes-code-of-conduct-structure
- name: Github Commit Structure
  property_count: 11
  slug: github-commit-structure
- name: Github Emojis Webhook Branch Protection Rule Created Structure
  property_count: 7
  slug: github-emojis-webhook-branch-protection-rule-created-structure
- name: Github Emojis Webhook Branch Protection Rule Deleted Structure
  property_count: 7
  slug: github-emojis-webhook-branch-protection-rule-deleted-structure
- name: Github Emojis Webhook Branch Protection Rule Edited Structure
  property_count: 8
  slug: github-emojis-webhook-branch-protection-rule-edited-structure
- name: Github Emojis Webhook Cache Sync Structure
  property_count: 9
  slug: github-emojis-webhook-cache-sync-structure
- name: Github Emojis Webhook Check Run Completed Form Encoded Structure
  property_count: 1
  slug: github-emojis-webhook-check-run-completed-form-encoded-structure
- name: Github Emojis Webhook Check Run Completed Structure
  property_count: 6
  slug: github-emojis-webhook-check-run-completed-structure
- name: Github Events Api Global Hook 2 Structure
  property_count: 10
  slug: github-events-api-global-hook-2-structure
- name: Github Events Api Global Hook Structure
  property_count: 10
  slug: github-events-api-global-hook-structure
- name: Github Events Api Ldap Mapping Team Structure
  property_count: 13
  slug: github-events-api-ldap-mapping-team-structure
- name: Github Events Api Ldap Mapping User Structure
  property_count: 42
  slug: github-events-api-ldap-mapping-user-structure
- name: Github Events Api Organization Simple Structure
  property_count: 12
  slug: github-events-api-organization-simple-structure
- name: Github Events Api Pre Receive Environment Structure
  property_count: 9
  slug: github-events-api-pre-receive-environment-structure
- name: Github Events Api Public Key Full Structure
  property_count: 11
  slug: github-events-api-public-key-full-structure
- name: Github Events Api Root Structure
  property_count: 33
  slug: github-events-api-root-structure
- name: Github Feeds Feed Structure
  property_count: 11
  slug: github-feeds-feed-structure
- name: Github Feeds Webhook Branch Protection Rule Created Structure
  property_count: 7
  slug: github-feeds-webhook-branch-protection-rule-created-structure
- name: Github Feeds Webhook Branch Protection Rule Deleted Structure
  property_count: 7
  slug: github-feeds-webhook-branch-protection-rule-deleted-structure
- name: Github Feeds Webhook Branch Protection Rule Edited Structure
  property_count: 8
  slug: github-feeds-webhook-branch-protection-rule-edited-structure
- name: Github Feeds Webhook Cache Sync Structure
  property_count: 9
  slug: github-feeds-webhook-cache-sync-structure
- name: Github Feeds Webhook Check Run Completed Structure
  property_count: 6
  slug: github-feeds-webhook-check-run-completed-structure
- name: Github Gists Base Gist Structure
  property_count: 20
  slug: github-gists-base-gist-structure
- name: Github Gists Basic Error Structure
  property_count: 4
  slug: github-gists-basic-error-structure
- name: Github Gists Gist Comment Structure
  property_count: 8
  slug: github-gists-gist-comment-structure
- name: Github Gists Gist Commit Structure
  property_count: 5
  slug: github-gists-gist-commit-structure
- name: Github Gists Gist Simple Structure
  property_count: 21
  slug: github-gists-gist-simple-structure
- name: Github Gists Public User Structure
  property_count: 39
  slug: github-gists-public-user-structure
- name: Github Gists Validation Error Structure
  property_count: 3
  slug: github-gists-validation-error-structure
- name: Github Gists Webhook Branch Protection Rule Created Structure
  property_count: 7
  slug: github-gists-webhook-branch-protection-rule-created-structure
- name: Github Gitignore Templates Gitignore Template Structure
  property_count: 2
  slug: github-gitignore-templates-gitignore-template-structure
- name: Github Gitignore Templates Webhook Branch Protection Rule Created Structure
  property_count: 7
  slug: github-gitignore-templates-webhook-branch-protection-rule-created-structure
- name: Github Gitignore Templates Webhook Branch Protection Rule Deleted Structure
  property_count: 7
  slug: github-gitignore-templates-webhook-branch-protection-rule-deleted-structure
- name: Github Gitignore Templates Webhook Branch Protection Rule Edited Structure
  property_count: 8
  slug: github-gitignore-templates-webhook-branch-protection-rule-edited-structure
- name: Github Gitignore Templates Webhook Cache Sync Structure
  property_count: 9
  slug: github-gitignore-templates-webhook-cache-sync-structure
- name: Github Gitignore Templates Webhook Check Run Completed Form Encoded Structure
  property_count: 1
  slug: github-gitignore-templates-webhook-check-run-completed-form-encoded-structure
- name: Github Gitignore Templates Webhook Check Run Completed Structure
  property_count: 6
  slug: github-gitignore-templates-webhook-check-run-completed-structure
- name: Github Gitignore Templates Webhook Check Run Created Structure
  property_count: 6
  slug: github-gitignore-templates-webhook-check-run-created-structure
- name: Github Installation App Permissions Structure
  property_count: 45
  slug: github-installation-app-permissions-structure
- name: Github Installation Basic Error Structure
  property_count: 4
  slug: github-installation-basic-error-structure
- name: Github Installation Installation Structure
  property_count: 20
  slug: github-installation-installation-structure
- name: Github Installation Installation Token Structure
  property_count: 8
  slug: github-installation-installation-token-structure
- name: Github Installation Integration Installation Request Structure
  property_count: 5
  slug: github-installation-integration-installation-request-structure
- name: Github Installation Validation Error Structure
  property_count: 3
  slug: github-installation-validation-error-structure
- name: Github Installation Webhook Branch Protection Rule Created Structure
  property_count: 7
  slug: github-installation-webhook-branch-protection-rule-created-structure
- name: Github Installation Webhook Branch Protection Rule Deleted Structure
  property_count: 7
  slug: github-installation-webhook-branch-protection-rule-deleted-structure
- name: Github Issue Structure
  property_count: 24
  slug: github-issue-structure
- name: Github Issues Api Global Hook 2 Structure
  property_count: 10
  slug: github-issues-api-global-hook-2-structure
- name: Github Issues Api Global Hook Structure
  property_count: 10
  slug: github-issues-api-global-hook-structure
- name: Github Issues Api Ldap Mapping Team Structure
  property_count: 13
  slug: github-issues-api-ldap-mapping-team-structure
- name: Github Issues Api Ldap Mapping User Structure
  property_count: 42
  slug: github-issues-api-ldap-mapping-user-structure
- name: Github Issues Api Organization Simple Structure
  property_count: 12
  slug: github-issues-api-organization-simple-structure
- name: Github Issues Api Pre Receive Environment Structure
  property_count: 9
  slug: github-issues-api-pre-receive-environment-structure
- name: Github Issues Api Public Key Full Structure
  property_count: 11
  slug: github-issues-api-public-key-full-structure
- name: Github Issues Api Root Structure
  property_count: 33
  slug: github-issues-api-root-structure
- name: Github Licenses Basic Error Structure
  property_count: 4
  slug: github-licenses-basic-error-structure
- name: Github Licenses License Structure
  property_count: 13
  slug: github-licenses-license-structure
- name: Github Licenses Webhook Branch Protection Rule Created Structure
  property_count: 7
  slug: github-licenses-webhook-branch-protection-rule-created-structure
- name: Github Licenses Webhook Branch Protection Rule Deleted Structure
  property_count: 7
  slug: github-licenses-webhook-branch-protection-rule-deleted-structure
- name: Github Licenses Webhook Branch Protection Rule Edited Structure
  property_count: 8
  slug: github-licenses-webhook-branch-protection-rule-edited-structure
- name: Github Licenses Webhook Cache Sync Structure
  property_count: 9
  slug: github-licenses-webhook-cache-sync-structure
- name: Github Licenses Webhook Check Run Completed Form Encoded Structure
  property_count: 1
  slug: github-licenses-webhook-check-run-completed-form-encoded-structure
- name: Github Licenses Webhook Check Run Completed Structure
  property_count: 6
  slug: github-licenses-webhook-check-run-completed-structure
- name: Github Manage Ghes Config Nodes Structure
  property_count: 2
  slug: github-manage-ghes-config-nodes-structure
- name: Github Manage Ghes Replication Status Structure
  property_count: 2
  slug: github-manage-ghes-replication-status-structure
- name: Github Manage Webhook Branch Protection Rule Created Structure
  property_count: 7
  slug: github-manage-webhook-branch-protection-rule-created-structure
- name: Github Manage Webhook Branch Protection Rule Deleted Structure
  property_count: 7
  slug: github-manage-webhook-branch-protection-rule-deleted-structure
- name: Github Manage Webhook Branch Protection Rule Edited Structure
  property_count: 8
  slug: github-manage-webhook-branch-protection-rule-edited-structure
- name: Github Manage Webhook Cache Sync Structure
  property_count: 9
  slug: github-manage-webhook-cache-sync-structure
- name: Github Manage Webhook Check Run Completed Structure
  property_count: 6
  slug: github-manage-webhook-check-run-completed-structure
- name: Github Markdown Webhook Branch Protection Rule Created Structure
  property_count: 7
  slug: github-markdown-webhook-branch-protection-rule-created-structure
- name: Github Markdown Webhook Branch Protection Rule Deleted Structure
  property_count: 7
  slug: github-markdown-webhook-branch-protection-rule-deleted-structure
- name: Github Markdown Webhook Branch Protection Rule Edited Structure
  property_count: 8
  slug: github-markdown-webhook-branch-protection-rule-edited-structure
- name: Github Markdown Webhook Cache Sync Structure
  property_count: 9
  slug: github-markdown-webhook-cache-sync-structure
- name: Github Markdown Webhook Check Run Completed Form Encoded Structure
  property_count: 1
  slug: github-markdown-webhook-check-run-completed-form-encoded-structure
- name: Github Markdown Webhook Check Run Completed Structure
  property_count: 6
  slug: github-markdown-webhook-check-run-completed-structure
- name: Github Markdown Webhook Check Run Created Form Encoded Structure
  property_count: 1
  slug: github-markdown-webhook-check-run-created-form-encoded-structure
- name: Github Markdown Webhook Check Run Created Structure
  property_count: 6
  slug: github-markdown-webhook-check-run-created-structure
- name: Github Meta Api Overview Structure
  property_count: 5
  slug: github-meta-api-overview-structure
- name: Github Meta Webhook Branch Protection Rule Created Structure
  property_count: 7
  slug: github-meta-webhook-branch-protection-rule-created-structure
- name: Github Meta Webhook Branch Protection Rule Deleted Structure
  property_count: 7
  slug: github-meta-webhook-branch-protection-rule-deleted-structure
- name: Github Meta Webhook Branch Protection Rule Edited Structure
  property_count: 8
  slug: github-meta-webhook-branch-protection-rule-edited-structure
- name: Github Meta Webhook Cache Sync Structure
  property_count: 9
  slug: github-meta-webhook-cache-sync-structure
- name: Github Meta Webhook Check Run Completed Form Encoded Structure
  property_count: 1
  slug: github-meta-webhook-check-run-completed-form-encoded-structure
- name: Github Meta Webhook Check Run Completed Structure
  property_count: 6
  slug: github-meta-webhook-check-run-completed-structure
- name: Github Meta Webhook Check Run Created Structure
  property_count: 6
  slug: github-meta-webhook-check-run-created-structure
- name: Github Networks Basic Error Structure
  property_count: 4
  slug: github-networks-basic-error-structure
- name: Github Networks Event Structure
  property_count: 8
  slug: github-networks-event-structure
- name: Github Networks Webhook Branch Protection Rule Created Structure
  property_count: 7
  slug: github-networks-webhook-branch-protection-rule-created-structure
- name: Github Networks Webhook Branch Protection Rule Deleted Structure
  property_count: 7
  slug: github-networks-webhook-branch-protection-rule-deleted-structure
- name: Github Networks Webhook Branch Protection Rule Edited Structure
  property_count: 8
  slug: github-networks-webhook-branch-protection-rule-edited-structure
- name: Github Networks Webhook Cache Sync Structure
  property_count: 9
  slug: github-networks-webhook-cache-sync-structure
- name: Github Networks Webhook Check Run Completed Form Encoded Structure
  property_count: 1
  slug: github-networks-webhook-check-run-completed-form-encoded-structure
- name: Github Networks Webhook Check Run Completed Structure
  property_count: 6
  slug: github-networks-webhook-check-run-completed-structure
- name: Github Notifications Basic Error Structure
  property_count: 4
  slug: github-notifications-basic-error-structure
- name: Github Notifications Thread Structure
  property_count: 9
  slug: github-notifications-thread-structure
- name: Github Notifications Thread Subscription Structure
  property_count: 7
  slug: github-notifications-thread-subscription-structure
- name: Github Notifications Webhook Branch Protection Rule Created Structure
  property_count: 7
  slug: github-notifications-webhook-branch-protection-rule-created-structure
- name: Github Notifications Webhook Branch Protection Rule Deleted Structure
  property_count: 7
  slug: github-notifications-webhook-branch-protection-rule-deleted-structure
- name: Github Notifications Webhook Branch Protection Rule Edited Structure
  property_count: 8
  slug: github-notifications-webhook-branch-protection-rule-edited-structure
- name: Github Notifications Webhook Cache Sync Structure
  property_count: 9
  slug: github-notifications-webhook-cache-sync-structure
- name: Github Notifications Webhook Check Run Completed Structure
  property_count: 6
  slug: github-notifications-webhook-check-run-completed-structure
- name: Github Openapi Global Hook 2 Structure
  property_count: 10
  slug: github-openapi-global-hook-2-structure
- name: Github Openapi Global Hook Structure
  property_count: 10
  slug: github-openapi-global-hook-structure
- name: Github Openapi Ldap Mapping Team Structure
  property_count: 13
  slug: github-openapi-ldap-mapping-team-structure
- name: Github Openapi Ldap Mapping User Structure
  property_count: 42
  slug: github-openapi-ldap-mapping-user-structure
- name: Github Openapi Organization Simple Structure
  property_count: 12
  slug: github-openapi-organization-simple-structure
- name: Github Openapi Pre Receive Environment Structure
  property_count: 9
  slug: github-openapi-pre-receive-environment-structure
- name: Github Openapi Public Key Full Structure
  property_count: 11
  slug: github-openapi-public-key-full-structure
- name: Github Openapi Root Structure
  property_count: 33
  slug: github-openapi-root-structure
- name: Github Organization Structure
  property_count: 37
  slug: github-organization-structure
- name: Github Organizations Basic Error Structure
  property_count: 4
  slug: github-organizations-basic-error-structure
- name: Github Organizations Organization Custom Repository Role Structure
  property_count: 8
  slug: github-organizations-organization-custom-repository-role-structure
- name: Github Organizations Organization Full Structure
  property_count: 56
  slug: github-organizations-organization-full-structure
- name: Github Organizations Organization Simple Structure
  property_count: 12
  slug: github-organizations-organization-simple-structure
- name: Github Organizations Scim Error Structure
  property_count: 6
  slug: github-organizations-scim-error-structure
- name: Github Organizations Simple User Structure
  property_count: 21
  slug: github-organizations-simple-user-structure
- name: Github Organizations Validation Error Simple Structure
  property_count: 3
  slug: github-organizations-validation-error-simple-structure
- name: Github Organizations Validation Error Structure
  property_count: 3
  slug: github-organizations-validation-error-structure
- name: Github Projects Basic Error Structure
  property_count: 4
  slug: github-projects-basic-error-structure
- name: Github Projects Project Card Structure
  property_count: 13
  slug: github-projects-project-card-structure
- name: Github Projects Project Collaborator Permission Structure
  property_count: 2
  slug: github-projects-project-collaborator-permission-structure
- name: Github Projects Project Column Structure
  property_count: 8
  slug: github-projects-project-column-structure
- name: Github Projects Project Structure
  property_count: 15
  slug: github-projects-project-structure
- name: Github Projects Team Project Structure
  property_count: 16
  slug: github-projects-team-project-structure
- name: Github Projects Validation Error Simple Structure
  property_count: 3
  slug: github-projects-validation-error-simple-structure
- name: Github Projects Validation Error Structure
  property_count: 3
  slug: github-projects-validation-error-structure
- name: Github Pull Request Structure
  property_count: 36
  slug: github-pull-request-structure
- name: Github Rate Limit  Basic Error Structure
  property_count: 4
  slug: github-rate-limit--basic-error-structure
- name: Github Rate Limit  Rate Limit Overview Structure
  property_count: 2
  slug: github-rate-limit--rate-limit-overview-structure
- name: Github Rate Limit  Rate Limit Structure
  property_count: 4
  slug: github-rate-limit--rate-limit-structure
- name: Github Repo Actions Api Basic Error Structure
  property_count: 4
  slug: github-repo-actions-api-basic-error-structure
- name: Github Repo Actions Api Code Of Conduct Structure
  property_count: 5
  slug: github-repo-actions-api-code-of-conduct-structure
- name: Github Repo Actions Api Nullable License Simple Structure
  property_count: 6
  slug: github-repo-actions-api-nullable-license-simple-structure
- name: Github Repo Actions Api Nullable Simple User Structure
  property_count: 21
  slug: github-repo-actions-api-nullable-simple-user-structure
- name: Github Repo Actions Api Repository Structure
  property_count: 95
  slug: github-repo-actions-api-repository-structure
- name: Github Repo Actions Api Scim Error Structure
  property_count: 6
  slug: github-repo-actions-api-scim-error-structure
- name: Github Repo Actions Api Simple User Structure
  property_count: 21
  slug: github-repo-actions-api-simple-user-structure
- name: Github Repo Actions Api Validation Error Simple Structure
  property_count: 3
  slug: github-repo-actions-api-validation-error-simple-structure
- name: Github Repo Autolinks Api Autolink Structure
  property_count: 4
  slug: github-repo-autolinks-api-autolink-structure
- name: Github Repo Autolinks Api Basic Error Structure
  property_count: 4
  slug: github-repo-autolinks-api-basic-error-structure
- name: Github Repo Autolinks Api Validation Error Structure
  property_count: 3
  slug: github-repo-autolinks-api-validation-error-structure
- name: Github Repo Branches Api Basic Error Structure
  property_count: 4
  slug: github-repo-branches-api-basic-error-structure
- name: Github Repo Branches Api Integration Structure
  property_count: 17
  slug: github-repo-branches-api-integration-structure
- name: Github Repo Branches Api Nullable Simple User Structure
  property_count: 21
  slug: github-repo-branches-api-nullable-simple-user-structure
- name: Github Repo Branches Api Nullable Team Simple Structure
  property_count: 12
  slug: github-repo-branches-api-nullable-team-simple-structure
- name: Github Repo Branches Api Simple User Structure
  property_count: 21
  slug: github-repo-branches-api-simple-user-structure
- name: Github Repo Branches Api Validation Error Simple Structure
  property_count: 3
  slug: github-repo-branches-api-validation-error-simple-structure
- name: Github Repo Branches Api Validation Error Structure
  property_count: 3
  slug: github-repo-branches-api-validation-error-structure
- name: Github Repo Code Scanning Api Basic Error Structure
  property_count: 4
  slug: github-repo-code-scanning-api-basic-error-structure
- name: Github Repo Code Scanning Api Nullable Simple User Structure
  property_count: 21
  slug: github-repo-code-scanning-api-nullable-simple-user-structure
- name: Github Repo Code Scanning Api Scim Error Structure
  property_count: 6
  slug: github-repo-code-scanning-api-scim-error-structure
- name: Github Repo Collaborators Api Basic Error Structure
  property_count: 4
  slug: github-repo-collaborators-api-basic-error-structure
- name: Github Repo Collaborators Api Collaborator Structure
  property_count: 22
  slug: github-repo-collaborators-api-collaborator-structure
- name: Github Repo Collaborators Api Nullable Collaborator Structure
  property_count: 22
  slug: github-repo-collaborators-api-nullable-collaborator-structure
- name: Github Repo Collaborators Api Repository Collaborator Permission Structure
  property_count: 3
  slug: github-repo-collaborators-api-repository-collaborator-permission-structure
- name: Github Repo Collaborators Api Validation Error Structure
  property_count: 3
  slug: github-repo-collaborators-api-validation-error-structure
- name: Github Repo Dependabot Api Basic Error Structure
  property_count: 4
  slug: github-repo-dependabot-api-basic-error-structure
- name: Github Repo Dependabot Api Nullable Simple User Structure
  property_count: 21
  slug: github-repo-dependabot-api-nullable-simple-user-structure
- name: Github Repo Dependabot Api Scim Error Structure
  property_count: 6
  slug: github-repo-dependabot-api-scim-error-structure
- name: Github Repo Dependabot Api Validation Error Simple Structure
  property_count: 3
  slug: github-repo-dependabot-api-validation-error-simple-structure
- name: Github Repo Hooks Api Basic Error Structure
  property_count: 4
  slug: github-repo-hooks-api-basic-error-structure
- name: Github Repo Hooks Api Hook Delivery Item Structure
  property_count: 12
  slug: github-repo-hooks-api-hook-delivery-item-structure
- name: Github Repo Hooks Api Scim Error Structure
  property_count: 6
  slug: github-repo-hooks-api-scim-error-structure
- name: Github Repo Hooks Api Webhook Config Structure
  property_count: 4
  slug: github-repo-hooks-api-webhook-config-structure
- name: Github Repo Invitations Api Code Of Conduct Structure
  property_count: 5
  slug: github-repo-invitations-api-code-of-conduct-structure
- name: Github Repo Invitations Api Minimal Repository Structure
  property_count: 87
  slug: github-repo-invitations-api-minimal-repository-structure
- name: Github Repo Invitations Api Nullable Simple User Structure
  property_count: 21
  slug: github-repo-invitations-api-nullable-simple-user-structure
- name: Github Repo Invitations Api Repository Invitation Structure
  property_count: 10
  slug: github-repo-invitations-api-repository-invitation-structure
- name: Github Repo Invitations Api Security And Analysis Structure
  property_count: 3
  slug: github-repo-invitations-api-security-and-analysis-structure
- name: Github Repo Invitations Api Simple User Structure
  property_count: 21
  slug: github-repo-invitations-api-simple-user-structure
- name: Github Repo Issues Api Basic Error Structure
  property_count: 4
  slug: github-repo-issues-api-basic-error-structure
- name: Github Repo Issues Api Integration Structure
  property_count: 17
  slug: github-repo-issues-api-integration-structure
- name: Github Repo Issues Api Nullable License Simple Structure
  property_count: 6
  slug: github-repo-issues-api-nullable-license-simple-structure
- name: Github Repo Issues Api Nullable Simple User Structure
  property_count: 21
  slug: github-repo-issues-api-nullable-simple-user-structure
- name: Github Repo Issues Api Repository Structure
  property_count: 95
  slug: github-repo-issues-api-repository-structure
- name: Github Repo Issues Api Scim Error Structure
  property_count: 6
  slug: github-repo-issues-api-scim-error-structure
- name: Github Repo Issues Api Simple User Structure
  property_count: 21
  slug: github-repo-issues-api-simple-user-structure
- name: Github Repo Issues Api Validation Error Structure
  property_count: 3
  slug: github-repo-issues-api-validation-error-structure
- name: Github Repo Projects Api Basic Error Structure
  property_count: 4
  slug: github-repo-projects-api-basic-error-structure
- name: Github Repo Projects Api Nullable Simple User Structure
  property_count: 21
  slug: github-repo-projects-api-nullable-simple-user-structure
- name: Github Repo Projects Api Project Structure
  property_count: 15
  slug: github-repo-projects-api-project-structure
- name: Github Repo Projects Api Validation Error Simple Structure
  property_count: 3
  slug: github-repo-projects-api-validation-error-simple-structure
- name: Github Repo Pulls Api Basic Error Structure
  property_count: 4
  slug: github-repo-pulls-api-basic-error-structure
- name: Github Repo Pulls Api Nullable License Simple Structure
  property_count: 6
  slug: github-repo-pulls-api-nullable-license-simple-structure
- name: Github Repo Pulls Api Nullable Milestone Structure
  property_count: 16
  slug: github-repo-pulls-api-nullable-milestone-structure
- name: Github Repo Pulls Api Nullable Simple User Structure
  property_count: 21
  slug: github-repo-pulls-api-nullable-simple-user-structure
- name: Github Repo Pulls Api Repository Structure
  property_count: 95
  slug: github-repo-pulls-api-repository-structure
- name: Github Repo Pulls Api Simple User Structure
  property_count: 21
  slug: github-repo-pulls-api-simple-user-structure
- name: Github Repo Pulls Api Validation Error Simple Structure
  property_count: 3
  slug: github-repo-pulls-api-validation-error-simple-structure
- name: Github Repo Pulls Api Validation Error Structure
  property_count: 3
  slug: github-repo-pulls-api-validation-error-structure
- name: Github Repo Subscription Api Basic Error Structure
  property_count: 4
  slug: github-repo-subscription-api-basic-error-structure
- name: Github Repo Subscription Api Repository Subscription Structure
  property_count: 6
  slug: github-repo-subscription-api-repository-subscription-structure
- name: Github Repo Tags Api App Permissions Structure
  property_count: 45
  slug: github-repo-tags-api-app-permissions-structure
- name: Github Repo Tags Api Basic Error Structure
  property_count: 4
  slug: github-repo-tags-api-basic-error-structure
- name: Github Repo Tags Api Enterprise Structure
  property_count: 10
  slug: github-repo-tags-api-enterprise-structure
- name: Github Repo Tags Api Nullable Simple User Structure
  property_count: 21
  slug: github-repo-tags-api-nullable-simple-user-structure
- name: Github Repo Tags Api Scim Error Structure
  property_count: 6
  slug: github-repo-tags-api-scim-error-structure
- name: Github Repo Tags Api Simple User Structure
  property_count: 21
  slug: github-repo-tags-api-simple-user-structure
- name: Github Repo Tags Api Validation Error Simple Structure
  property_count: 3
  slug: github-repo-tags-api-validation-error-simple-structure
- name: Github Repo Tags Api Validation Error Structure
  property_count: 3
  slug: github-repo-tags-api-validation-error-structure
- name: Github Repos Api App Permissions Structure
  property_count: 45
  slug: github-repos-api-app-permissions-structure
- name: Github Repos Api Basic Error Structure
  property_count: 4
  slug: github-repos-api-basic-error-structure
- name: Github Repos Api Enterprise Structure
  property_count: 10
  slug: github-repos-api-enterprise-structure
- name: Github Repos Api Nullable Simple User Structure
  property_count: 21
  slug: github-repos-api-nullable-simple-user-structure
- name: Github Repos Api Scim Error Structure
  property_count: 6
  slug: github-repos-api-scim-error-structure
- name: Github Repos Api Simple User Structure
  property_count: 21
  slug: github-repos-api-simple-user-structure
- name: Github Repos Api Validation Error Simple Structure
  property_count: 3
  slug: github-repos-api-validation-error-simple-structure
- name: Github Repos Api Validation Error Structure
  property_count: 3
  slug: github-repos-api-validation-error-structure
- name: Github Repository Structure
  property_count: 35
  slug: github-repository-structure
- name: Github Scim Group Response Structure
  property_count: 4
  slug: github-scim-group-response-structure
- name: Github Scim Meta Structure
  property_count: 4
  slug: github-scim-meta-structure
- name: Github Scim Scim Error Structure
  property_count: 6
  slug: github-scim-scim-error-structure
- name: Github Scim User Name Response Structure
  property_count: 4
  slug: github-scim-user-name-response-structure
- name: Github Scim User Response Structure
  property_count: 8
  slug: github-scim-user-response-structure
- name: Github Setup Configuration Status Structure
  property_count: 2
  slug: github-setup-configuration-status-structure
- name: Github Setup Enterprise Settings Structure
  property_count: 2
  slug: github-setup-enterprise-settings-structure
- name: Github Setup Maintenance Status Structure
  property_count: 3
  slug: github-setup-maintenance-status-structure
- name: Github Setup Ssh Key Structure
  property_count: 2
  slug: github-setup-ssh-key-structure
- name: Github Teams Basic Error Structure
  property_count: 4
  slug: github-teams-basic-error-structure
- name: Github Teams Ldap Mapping Team Structure
  property_count: 13
  slug: github-teams-ldap-mapping-team-structure
- name: Github Teams Reaction Structure
  property_count: 5
  slug: github-teams-reaction-structure
- name: Github Teams Team Discussion Comment Structure
  property_count: 13
  slug: github-teams-team-discussion-comment-structure
- name: Github Teams Team Discussion Structure
  property_count: 18
  slug: github-teams-team-discussion-structure
- name: Github Teams Team Full Structure
  property_count: 18
  slug: github-teams-team-full-structure
- name: Github Teams Team Structure
  property_count: 13
  slug: github-teams-team-structure
- name: Github Teams Validation Error Structure
  property_count: 3
  slug: github-teams-validation-error-structure
- name: Github User Structure
  property_count: 28
  slug: github-user-structure
- name: Github Users Api Basic Error Structure
  property_count: 4
  slug: github-users-api-basic-error-structure
- name: Github Users Api Ldap Mapping User Structure
  property_count: 42
  slug: github-users-api-ldap-mapping-user-structure
- name: Github Users Api Public User Structure
  property_count: 39
  slug: github-users-api-public-user-structure
- name: Github Users Api Scim Error Structure
  property_count: 6
  slug: github-users-api-scim-error-structure
- name: Github Users Api Simple User Structure
  property_count: 21
  slug: github-users-api-simple-user-structure
- name: Github Users Api Starred Repository Structure
  property_count: 2
  slug: github-users-api-starred-repository-structure
- name: Github Users Api Validation Error Simple Structure
  property_count: 3
  slug: github-users-api-validation-error-simple-structure
- name: Github Users Api Validation Error Structure
  property_count: 3
  slug: github-users-api-validation-error-structure
- name: Github Webhook Delivery Structure
  property_count: 14
  slug: github-webhook-delivery-structure
jsonld:
- class_count: 85
  name: Github Context
  property_count: 451
  slug: github-context
layout: provider
mcp_servers:
- description: GitHub's official MCP server connects AI tools to repositories, issues, pull requests, Actions, and code security; remote OAuth endpoint plus a local Docker image, with modular toolsets and a read-onl
  name: MCP Server
  slug: mcp-server
modified: '2026-09-16'
name: GitHub
nav: Providers
network: true
overview: 'GitHub publishes 35 APIs on the [APIs.io](https://apis.io/) network, including Gists API, Issues API, Licenses API, and 32 more. Tagged areas include Code, Developer Tools, Pipelines, Platform, and Software Development.


  The GitHub catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  GitHub''s developer surface includes pricing, authentication, documentation, CLI, support, getting-started guide, engineering blog, and 66 more developer resources.'
plans:
- name: Github Plans Pricing
  plan_count: 6
  slug: github-plans-pricing
- name: Github Price Estimates
  plan_count: 0
  slug: github-price-estimates
random_paper: 5
rate_limits:
- limit_count: 18
  name: Github Rate Limits
  slug: github-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: GitHub API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: github-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: GitHub API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: github-jsonschema-spectral-rules
- effective_rule_count: 20
  extends: []
  name: GitHub API Rules
  rule_count: 20
  severity_counts:
    error: 14
    hint: 0
    info: 3
    warn: 3
  slug: github-spectral-rules
score:
  band: exemplar
  composite: 77.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 74.5
    catalog_earned_first_party: 24.0
    catalog_gap: 40.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 13.6
    contract_quality: 74.7
    developer_ergonomics: 79.8
    discoverability: 66.7
    operational_transparency: 92.1
  previous_composite: 77.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 35
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/screenshots/github-2026-06-20T181834.png
security:
- kind: authentication
  name: Github Authentication
  slug: github-authentication
  summary_line: http · 1 scheme
slug: github
solutions:
- description: Free tier with unlimited public and private repos, Actions minutes, and Packages storage.
  name: GitHub Free
- description: Advanced tools for individual developers with more Actions minutes and Packages.
  name: GitHub Pro
- description: Collaboration features for teams with code owners, required reviews, and Pages.
  name: GitHub Team
- description: Enterprise features with SAML SSO, audit log streaming, and advanced security.
  name: GitHub Enterprise
tags:
- Code
- Developer Tools
- Pipelines
- Platform
- Software Development
- Source Control
- T1
- GitHub
use_cases:
- description: Automate build, test, and deployment pipelines with GitHub Actions API.
  name: CI/CD Automation
- description: Programmatically create, configure, and manage repositories and branches.
  name: Repository Management
- description: Create, update, and query issues, labels, milestones, and project boards.
  name: Issue and Project Tracking
- description: Automate pull request reviews, checks, and merge workflows.
  name: Code Review Automation
- description: Access Dependabot alerts, code scanning results, and secret scanning alerts.
  name: Security Scanning
- description: Build GitHub Apps, CLI extensions, and IDE integrations.
  name: Developer Tools
- description: Manage teams, members, permissions, and audit logs for organizations.
  name: Organization Management
- description: Publish and manage packages across multiple package registries.
  name: Package Publishing
---
