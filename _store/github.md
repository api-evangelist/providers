---
aid: github
url: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/apis.yml
apis:
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
      - url: openapi/github-app-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/apps
        type: Documentation
    description: The GitHub App API is the set of REST/GraphQL endpoints and webhooks that lets a GitHub App securely integrate with and automate work across GitHub. Apps authenticate with a shortlived JSON Web Token and exchange it for installation access tokens to act on specific repositories or organizations with finegrained, leastprivilege permissions, or use user-to-server OAuth to act on behalf of a user when needed.
  - aid: github:github-auth-api
    name: GitHub Authorization API
    tags:
      - Authentication
      - Authorization
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28
    properties:
      - url: openapi/github-auth-api-openapi.yml
        type: OpenAPI
      - url: |-

          https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api
        type: Documentation
    description: The GitHub Authorization (OAuth Authorizations) API historically let you programmatically create, list, inspect, and revoke access tokens for a user or OAuth applicationsetting scopes, verifying token validity, rotating or deleting tokens, and generally managing what an app could do on a users behalf. It was commonly used with basic authentication (and 2FA) to mint personal access tokens and to manage OAuth app grants.
  - aid: github:github-code-of-conduct-api
    name: GitHub Code of Conduct API
    tags:
      - Code of Conduct
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/codes-of-conduct/codes-of-conduct?apiVersion=2022-11-28
    properties:
      - url: openapi/github-code-of-conduct-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/codes-of-conduct/codes-of-conduct
        type: Documentation
    description: GitHubs Code of Conduct API lets apps discover and retrieve the community codes of conduct that GitHub supports and see which one a repository has adopted. Through REST endpoints, clients can list available templates (like the Contributor Covenant), fetch a specific code by key, and read a repositorys code-of-conduct metadata and text, including fields such as name, key, URL, and body. This enables tooling to display community standards, audit or report adoption, and bootstrap repo files.
  - aid: github:github-emojis-api
    name: GitHub Emojis API
    tags:
      - Emojis
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/emojis?apiVersion=2022-11-28
    properties:
      - url: openapi/github-emojis-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/emojis
        type: Documentation
    description: The GitHub Emojis API is a simple REST endpoint (GET /emojis or https://api.github.com/emojis) that returns a JSON dictionary mapping emoji shortcodes (like "smile" or "octocat") to the image URLs GitHub uses to render them. It covers both standard Unicode emoji and GitHub-specific custom ones, enabling clients to power emoji pickers, autocomplete for :shortcodes:, validation, or server-side rendering in apps that mirror GitHubs formatting.
  - aid: github:github-events-api
    name: GitHub Events API
    tags:
      - Events
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/activity/events?apiVersion=2022-11-28
    properties:
      - url: openapi/github-events-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/activity/events
        type: Documentation
    description: The GitHub Events API provides a read-only feed of recent activity on GitHub, exposing structured event objects you can poll to see what happened across the platform or within a specific repository, organization, or user account. It covers many event typessuch as pushes, pull requests, issues, comments, releases, stars, forks, and membership changeseach with consistent metadata (actor, repo, type, payload, timestamps, IDs).
  - aid: github:github-feeds-api
    name: GitHub Feeds API
    tags:
      - Feeds
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/activity/feeds?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-feeds-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-feeds-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/activity/feeds
        type: Documentation
    description: GitHubs Feeds API lets you programmatically discover the Atom feed URLs for GitHub activity thats relevant to you, such as the global timeline, a specific users activity, the authenticated users public and private activity, organization activity, and security advisories.
  - aid: github:github-gists-api
    name: GitHub Gists API
    tags:
      - Artifacts
      - Code
      - Gists
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/gists?apiVersion=2022-11-28
    properties:
      - url: openapi/github-gists-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/gists
        type: Documentation
    description: The GitHub Gists API lets you programmatically manage gistslightweight code snippets and notesover HTTP. You can create gists (public or secret/unlisted), read individual gists, list public gists, your own, a users, and those youve starred, fetch raw file contents, view version history and commits, update gists by adding/renaming/removing files or changing descriptions, and delete them. It also supports forking, starring/un-starring and checking star status, plus full CRUD for gist comments.
  - aid: github:github-gitignore-templates-api
    name: GitHub Gitignore Templates API
    tags:
      - Gitignore
      - Templates
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/gitignore?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-gitignore-templates-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-gitignore-templates-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/gitignore
        type: Documentation
    description: The GitHub Gitignore Templates API is a REST interface that lets you discover and fetch canonical .gitignore templates maintained by GitHub, so you can programmatically create ignore files tailored to specific languages, frameworks, IDEs, or operating systems. It provides endpoints to list all available template names and to retrieve the full content of a chosen template (for example, Node, Python, macOS, or VisualStudio) via GET /gitignore/templates and GET /gitignore/templates/{name}.
  - aid: github:github-installation-api
    name: GitHub Installation API
    tags:
      - Installations
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/apps/installations?apiVersion=2022-11-28
    properties:
      - url: openapi/github-installation-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/apps/installations
        type: Documentation
    description: The GitHub Installation API is part of the GitHub Apps platform and lets an app understand and manage where its installed and what it can access, and act on behalf of that installation. Using these endpoints, an app can list its installations, fetch details for a specific installation, enumerate the repositories granted to it, and (when the app is configured for selected repositories ) add or remove repository access.
  - aid: github:github-issues-api
    name: GitHub Issues API
    tags:
      - Issues
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/issues?apiVersion=2022-11-28
    properties:
      - url: openapi/github-issues-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/issues
        type: Documentation
    description: The GitHub Issues API lets you programmatically manage issue tracking on GitHub, enabling you to list and filter issues across repositories, create and edit issues, change their state (open/closed), and manage assignees, labels, and milestones. It supports adding, updating, and deleting comments; applying reactions; locking or unlocking conversations; and viewing issue events and timelines for auditing and automation.
  - aid: github:github-licenses-api
    name: GitHub Licenses API
    tags:
      - Licenses
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/licenses?apiVersion=2022-11-28
    properties:
      - url: openapi/github-licenses-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/licenses
        type: Documentation
    description: The GitHub Licenses API lets you programmatically discover and retrieve open source license information across GitHub. It provides endpoints to list the common licenses GitHub supports, get detailed metadata and the canonical text for a specific license (by its SPDX identifier), and fetch the detected license for a given repository.
  - aid: github:github-manage-api
    name: GitHub Enterprise Management API
    tags:
      - Management
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-manage-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-manage-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/enterprise-admin
        type: Documentation
    description: The GitHub Enterprise Management API lets administrators automate and integrate the operational and security management of their enterprise on GitHub. It covers tasks like provisioning and governing organizations, users, and teams; enforcing policies for repositories, security, and GitHub Actions; integrating identity and access management via SSO/SCIM; retrieving audit logs and usage data for compliance and billing; and managing self-hosted runners.
  - aid: github:github-markdown-api
    name: GitHub Markdown API
    tags:
      - Markdown
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/markdown?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-markdown-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-markdown-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/markdown
        type: Documentation
    description: The GitHub Markdown API is a REST service that converts Markdownespecially GitHub Flavored Markdowninto the same HTML GitHub renders in READMEs, issues, and pull requests, so external apps can display content consistently with GitHub.
  - aid: github:github-meta-api
    name: GitHub Meta API
    tags:
      - Metadata
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/meta?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-meta-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-meta-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/meta
        type: Documentation
    description: Use the REST API to get meta information about GitHub, including the IP addresses of GitHub services.
  - aid: github:github-networks-api
    name: GitHub Networks API
    tags:
      - Networks
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-networks-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-networks-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/activity/events
        type: Documentation
    description: GitHubs Networks API lets you retrieve a stream of public activity that occurs across a repositorys network, meaning the original repo and all of its forks. Exposed via the Events API (for example, listing events for /networks/{owner}/{repo}/events), it returns the same event types you see in other GitHub event feedspushes, pull requests, issues, releases, and moreaggregated across every repo in that fork family.
  - aid: github:github-notifications-api
    name: GitHub Notifications API
    tags:
      - Notifications
    baseURL: https://api.github.com/
    humanURL: |-

      https://docs.github.com/en/rest/activity/notifications?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-notifications-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-notifications-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/activity/notifications
        type: Documentation
    description: This GitHub REST API allows you to programmatically manage your GitHub notifications, which include updates on issues, pull requests, and commits. The API requires authentication via a personal access token (classic) and needs either the notifications or repo scope to function.
  - aid: github:github-octocat-api
    name: GitHub Octocat API
    tags:
      - Octocat
    baseURL: https://api.github.com/
    humanURL: https://github.com/octokit/octokit.js
    overlays:
      - url: overlays/github-octocat-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-octocat-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/meta/meta
        type: Documentation
    description: The GitHub Octocat API is a playful, non-functional endpoint in GitHubs REST API that returns an ASCII-art rendering of the Octocat mascot as plain text. Its primarily meant for fun and demospeople often use it to sanity-check connectivity, see how the API formats responses and headers, or showcase simple requests without touching real repository data. It doesnt manage or expose any GitHub resources, and in some clients you can even supply a short message that the Octocat says.
  - aid: github:github-org-api
    name: GitHub Organization API
    tags:
      - Organizations
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/orgs?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-org-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-org-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/orgs
        type: Documentation
    description: The GitHub Organization API lets you programmatically administer and integrate with organizations on GitHub, spanning both REST and GraphQL. It covers core governance tasks such as reading and updating org settings and policies, managing members and outside collaborators, sending invitations and assigning roles, organizing teams and their permissions, and controlling repository access at scale.
  - aid: github:github-projects-api
    name: GitHub Projects API
    tags:
      - Projects
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/projects?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-projects-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-projects-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/projects
        type: Documentation
    description: The GitHub Projects API enables developers to programmatically create and manage GitHub Projects, which are flexible tools for planning and tracking work using customizable boards, tables, and roadmaps. Through these REST API endpoints, you can create projects at the repository, organization, or user level, add and organize items like issues and pull requests, manage project fields and views, update item statuses and metadata, and automate project workflows.
  - aid: github:github-rate-limit-api
    name: GitHub Rate Limit API
    tags:
      - Rate Limits
    baseURL: https://api.github.com/
    humanURL: |-

      https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-rate-limit-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-rate-limit-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/rate-limit
        type: Documentation
    description: GitHubs Rate Limit API lets you programmatically see how much API quota you have left and when it will reset, so you can avoid hitting API rate limit exceeded errors. By calling the /rate_limit endpoint (or by reading the X-RateLimit headers on any response), you get current limit, remaining, used, and reset time for different resource categories (for example, core REST, search, and GraphQL).
  - aid: github:github-repos-api
    name: GitHub Repos API
    tags:
      - Repos
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/repos?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-repos-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-repos-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/repos
        type: Documentation
    description: The GitHub Repos API is a set of REST endpoints that let you programmatically create, read, update, and delete repositories and their resources, giving you control over a repos lifecycle and configuration.
  - aid: github:github-scim-api
    name: GitHub SCIM API
    tags:
      - SCIM
    baseURL: https://api.github.com/
    humanURL: |-

      https://docs.github.com/en/enterprise-cloud@latest/rest/scim?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-scim-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-scim-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/enterprise-cloud@latest/rest/scim
        type: Documentation
    description: GitHubs SCIM API implements the SCIM 2.0 standard to automate user lifecycle management from an identity provider (such as Entra ID/Azure AD, Okta, or OneLogin) to GitHub Enterprise Cloud. It lets you provision, update, suspend/reactivate, and deprovision users, keeping their GitHub access in sync with your IdP.
  - aid: github:github-search-api
    name: GitHub Search API
    tags:
      - Discovery
      - Search
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-search-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-search-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/search
        type: Documentation
    description: The GitHub Search API lets you programmatically find and filter content across GitHubincluding repositories, code, issues and pull requests, commits, users, topics, and labelsusing a powerful query language with qualifiers (for example by language, stars, forks, org/user, path/filename, label, state, author, or committer).
  - aid: github:github-setup-api
    name: GitHub Setup API
    tags:
      - Setup
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-setup-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-setup-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api
        type: Documentation
    description: The GitHub Setup API is the administrative interface for GitHub Enterprise Server that lets you automate tasks normally done in the Management Console during first-time and ongoing configuration. It provides endpoints to upload and apply your license, set the hostname and TLS certificates, configure system services like SMTP, create or reset the initial admin credentials, start and monitor reconfiguration runs, and query setup status and health.
  - aid: github:github-teams-api
    name: GitHub Teams API
    tags:
      - Teams
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/teams?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-teams-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-teams-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/teams
        type: Documentation
    description: The GitHub Teams API lets you programmatically manage organization teams and the access they grant. With it, you can create, update, and delete teams; organize parent/child team hierarchies; add or remove members and maintainers; send and manage invitations; and list or audit team membership. It also lets you grant, adjust, or revoke a teams permissions to repositories (and, where applicable, projects), enabling consistent, leastprivilege access control at scale.
  - aid: github:github-zen-api
    name: GitHub Zen API
    tags:
      - Zen
    overlays:
      - url: overlays/github-zen-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-zen-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/meta/meta
        type: Documentation
    description: The GitHub Zen API is a playful REST endpoint that returns a random aphorism from the Zen of GitHub, such as Keep it logically awesome. Each request to GET https://api.github.com/zen responds with a single plain-text line, making it useful for quick connectivity checks, demoing HTTP calls, or verifying authentication. It doesnt require auth, but you can include a token to benefit from higher rate limits.
  - aid: github:github-user-api
    name: GitHub User API
    tags:
      - Users
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/users?apiVersion=2022-11-28
    properties:
      - url: openapi/github-users-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/users
        type: Documentation
    description: The GitHub Users API (part of the REST API) lets applications read and, for the authenticated account, manage user-related data on GitHub. It can fetch public profiles for any user or the authenticated users private profile details, list a users public repositories and organizations, and view activity like followers and following.
  - aid: github:github-actions-api
    name: GitHub Actions API
    tags:
      - Actions
      - Automation
      - CI/CD
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/actions?apiVersion=2022-11-28
    properties:
      - url: openapi/github-repo-actions-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/actions
        type: Documentation
    description: The GitHub Actions API lets you manage and automate GitHub Actions workflows, including creating and managing workflow runs, jobs, artifacts, caches, secrets, variables, self-hosted runners, and runner groups. It provides endpoints for triggering workflow dispatches, downloading logs and artifacts, reviewing and approving deployments, managing OIDC subject claims, and configuring permissions and allowed actions at the organization and repository level.
  - aid: github:github-branches-api
    name: GitHub Branches API
    tags:
      - Branches
      - Source Control
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/branches?apiVersion=2022-11-28
    properties:
      - url: openapi/github-repo-branches-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/branches
        type: Documentation
    description: The GitHub Branches API lets you list, create, and manage branches in a repository, including configuring branch protection rules that enforce required status checks, pull request reviews, signed commits, and restrictions on who can push. It also supports managing branch protection settings for admins and teams.
  - aid: github:github-code-scanning-api
    name: GitHub Code Scanning API
    tags:
      - Analysis
      - Code Scanning
      - Security
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/code-scanning?apiVersion=2022-11-28
    properties:
      - url: openapi/github-repo-code-scanning-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/code-scanning
        type: Documentation
    description: The GitHub Code Scanning API lets you retrieve and manage code scanning alerts for a repository. Code scanning uses CodeQL or third-party analysis tools to find potential security vulnerabilities and coding errors. The API provides endpoints to list, get, update, and dismiss alerts, as well as manage analyses and upload SARIF results.
  - aid: github:github-collaborators-api
    name: GitHub Collaborators API
    tags:
      - Access Control
      - Collaborators
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/collaborators?apiVersion=2022-11-28
    properties:
      - url: openapi/github-repo-collaborators-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/collaborators
        type: Documentation
    description: The GitHub Collaborators API lets you manage access to repositories by adding, removing, and listing collaborators, checking permissions, and managing repository invitations. It supports fine-grained permission levels including read, triage, write, maintain, and admin access for individual users on a repository.
  - aid: github:github-dependabot-api
    name: GitHub Dependabot API
    tags:
      - Dependabot
      - Dependencies
      - Security
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/dependabot?apiVersion=2022-11-28
    properties:
      - url: openapi/github-repo-dependabot-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/dependabot
        type: Documentation
    description: The GitHub Dependabot API lets you manage Dependabot alerts and secrets for repositories and organizations. It provides endpoints to list, get, and update Dependabot alerts for vulnerable dependencies, as well as create, update, and delete encrypted secrets that Dependabot uses to access private registries during version updates.
  - aid: github:github-webhooks-api
    name: GitHub Webhooks API
    tags:
      - Automation
      - Events
      - Webhooks
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/webhooks?apiVersion=2022-11-28
    properties:
      - url: openapi/github-repo-hooks-api-openapi.yml
        type: OpenAPI
      - url: asyncapi/github-webhooks-asyncapi.yml
        type: AsyncAPI
      - url: https://docs.github.com/en/rest/webhooks
        type: Documentation
      - url: https://docs.github.com/en/webhooks/webhook-events-and-payloads
        type: Reference
    description: The GitHub Webhooks API lets you create and manage webhooks for repositories and organizations. Webhooks deliver HTTP POST payloads to a configured URL whenever specified events occur, such as pushes, pull requests, issues, and releases. The API supports creating, updating, deleting, and testing webhooks, as well as listing and redelivering webhook deliveries.
  - aid: github:github-pull-requests-api
    name: GitHub Pull Requests API
    tags:
      - Code Review
      - Pull Requests
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/pulls?apiVersion=2022-11-28
    properties:
      - url: openapi/github-repo-pulls-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/pulls
        type: Documentation
    description: The GitHub Pull Requests API lets you create, list, update, and merge pull requests in a repository. It provides endpoints for managing pull request reviews, review comments, review requests, and merge operations. You can also check mergeability, list commits and changed files, and manage draft pull requests.
  - aid: github:github-tags-api
    name: GitHub Tags API
    tags:
      - Releases
      - Source Control
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/git/tags?apiVersion=2022-11-28
    properties:
      - url: openapi/github-repo-tags-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/git/tags
        type: Documentation
    description: The GitHub Tags API lets you create and manage Git tag objects in a repository. Tags are references that point to specific commits, commonly used to mark release points. The API supports creating annotated tags with messages and tagger information, as well as retrieving tag data including the tagged object, tag name, and message.
  - aid: github:github-checks-api
    name: GitHub Checks API
    tags:
      - Checks
      - CI/CD
      - Status
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/checks?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/checks
        type: Documentation
    description: The GitHub Checks API lets you create and manage check runs and check suites that report detailed status, annotations, and results for commits. It enables CI/CD tools and integrations to report build and test results directly on pull requests with rich output including summaries, text, images, and per-line annotations.
  - aid: github:github-deployments-api
    name: GitHub Deployments API
    tags:
      - Deployments
      - Releases
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/deployments?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/deployments
        type: Documentation
    description: The GitHub Deployments API lets you create and manage deployments and deployment statuses for repositories. Deployments are requests to deploy a specific ref (branch, SHA, tag) to an environment, and deployment statuses track the progress of that deployment. The API also supports managing deployment environments, environment protection rules, and deployment branch policies.
  - aid: github:github-releases-api
    name: GitHub Releases API
    tags:
      - Distribution
      - Releases
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/releases?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/releases
        type: Documentation
    description: The GitHub Releases API lets you create, edit, and delete releases for a repository, as well as upload and manage release assets (binaries, installers, archives). Releases are based on Git tags and provide a way to package and distribute software versions with release notes, pre-release flags, and downloadable assets.
  - aid: github:github-pages-api
    name: GitHub Pages API
    tags:
      - Hosting
      - Pages
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/pages?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/pages
        type: Documentation
    description: The GitHub Pages API lets you manage GitHub Pages sites for repositories, including creating, updating, and deleting sites, configuring custom domains and HTTPS enforcement, and triggering and monitoring Pages builds. GitHub Pages hosts static websites directly from a repository branch or GitHub Actions workflow.
  - aid: github:github-packages-api
    name: GitHub Packages API
    tags:
      - Packages
      - Registry
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/packages?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/packages
        type: Documentation
    description: The GitHub Packages API lets you manage packages and package versions in GitHub Packages, a software package hosting service that supports npm, Maven, Gradle, RubyGems, NuGet, Docker, and other package formats. The API provides endpoints to list, get, delete, and restore packages and their versions at the user, organization, and repository level.
  - aid: github:github-git-database-api
    name: GitHub Git Database API
    tags:
      - Database
      - Git
      - Source Control
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/git?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/git
        type: Documentation
    description: The GitHub Git Database API provides low-level access to Git objects (blobs, commits, refs, tags, and trees) in a repository. It lets you read and write raw Git data directly, enabling operations like creating commits programmatically, building trees, reading blob contents, and managing references without using the higher-level repository content endpoints.
  - aid: github:github-codespaces-api
    name: GitHub Codespaces API
    tags:
      - Codespaces
      - Development Environments
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/codespaces?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/codespaces
        type: Documentation
    description: The GitHub Codespaces API lets you create, manage, start, stop, and delete cloud development environments (codespaces) for repositories. It provides endpoints for managing codespace secrets, machine types, dev container configurations, and organization-level codespace policies and billing.
  - aid: github:github-copilot-api
    name: GitHub Copilot API
    tags:
      - AI
      - Copilot
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/copilot?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/copilot
        type: Documentation
    description: The GitHub Copilot API lets organization and enterprise owners manage GitHub Copilot seat assignments, retrieve usage metrics and billing information, and configure Copilot policies. It provides endpoints to add and remove Copilot seats for members, list assigned seats, and access Copilot usage data for reporting and administration.
  - aid: github:github-billing-api
    name: GitHub Billing API
    tags:
      - Billing
      - Usage
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/billing?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/billing
        type: Documentation
    description: The GitHub Billing API lets you view billing and usage information for organizations and enterprises, including Actions minutes, Packages storage and data transfer, Codespaces usage, and shared storage consumption. It provides endpoints for retrieving current usage summaries and managing billing budgets and thresholds.
  - aid: github:github-migrations-api
    name: GitHub Migrations API
    tags:
      - Export
      - Import
      - Migrations
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/migrations?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/migrations
        type: Documentation
    description: The GitHub Migrations API lets you migrate data to and from GitHub. It supports organization migrations that export repositories and metadata as downloadable archives, source imports that convert repositories from Subversion, Mercurial, or TFS to Git, and user migrations for moving personal repositories between accounts or platforms.
  - aid: github:github-secret-scanning-api
    name: GitHub Secret Scanning API
    tags:
      - Secret Scanning
      - Security
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/secret-scanning?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/secret-scanning
        type: Documentation
    description: The GitHub Secret Scanning API lets you retrieve and manage secret scanning alerts for repositories, organizations, and enterprises. Secret scanning detects tokens, keys, and other credentials accidentally committed to repositories. The API provides endpoints to list, get, and update alert statuses, as well as manage push protection bypass requests and list alert locations.
  - aid: github:github-security-advisories-api
    name: GitHub Security Advisories API
    tags:
      - Advisories
      - Security
      - Vulnerabilities
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/security-advisories?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/security-advisories
        type: Documentation
    description: The GitHub Security Advisories API lets you view and manage security advisories for repositories and access the GitHub Advisory Database. It provides endpoints to create, update, and list repository security advisories, request CVE identifiers, and query the global advisory database for known vulnerabilities across the open source ecosystem.
  - aid: github:github-commits-api
    name: GitHub Commits API
    tags:
      - Commits
      - Source Control
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/commits?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/commits
        type: Documentation
    description: The GitHub Commits API lets you list, retrieve, and compare commits in a repository, as well as manage commit comments and commit statuses. It provides endpoints for viewing commit details, listing pull requests associated with a commit, getting the combined status for a ref, and creating status checks that report build or test results.
  - aid: github:github-reactions-api
    name: GitHub Reactions API
    tags:
      - Reactions
      - Social
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/reactions?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/reactions
        type: Documentation
    description: The GitHub Reactions API lets you create, list, and delete emoji reactions on issues, pull requests, issue comments, pull request review comments, commit comments, release assets, and team discussion posts. Supported reaction types include thumbs up/down, laugh, confused, heart, hooray, rocket, and eyes.
  - aid: github:github-deploy-keys-api
    name: GitHub Deploy Keys API
    tags:
      - Deploy Keys
      - Security
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/deploy-keys?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/deploy-keys
        type: Documentation
    description: The GitHub Deploy Keys API lets you manage deploy keys for repositories. Deploy keys are SSH keys that grant read-only or read-write access to a single repository, commonly used for automated deployment systems and CI/CD pipelines that need to clone or push to a specific repository without using a personal account.
  - aid: github:github-dependency-graph-api
    name: GitHub Dependency Graph API
    tags:
      - Dependencies
      - Security
      - Supply Chain
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/dependency-graph?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/dependency-graph
        type: Documentation
    description: The GitHub Dependency Graph API lets you view and submit dependency information for a repository. It provides endpoints to export the software bill of materials (SBOM) for a repository and to submit dependency snapshots from build tools or package managers, enabling GitHub to generate Dependabot alerts for vulnerable dependencies.
  - aid: github:github-metrics-api
    name: GitHub Metrics API
    tags:
      - Analytics
      - Metrics
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/metrics?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/metrics
        type: Documentation
    description: The GitHub Metrics API lets you access community profile and repository statistics, including contributor activity, commit frequency, code frequency, participation data, punch card data, and community health metrics. It helps developers and maintainers understand project activity patterns and community engagement.
  - aid: github:github-interactions-api
    name: GitHub Interactions API
    tags:
      - Interactions
      - Moderation
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/interactions?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/interactions
        type: Documentation
    description: The GitHub Interactions API lets you temporarily restrict which users can comment, open issues, or create pull requests in public repositories. It supports setting interaction limits at the repository, organization, or authenticated user level, restricting interactions to existing users, contributors, or collaborators for a specified duration.
  - aid: github:github-models-api
    name: GitHub Models API
    tags:
      - AI
      - Machine Learning
      - Models
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/models?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/models
        type: Documentation
    description: The GitHub Models API provides access to the GitHub Models catalog, letting you list and retrieve details about AI models available on the GitHub platform. It supports browsing model metadata including names, descriptions, publishers, and capabilities, enabling integration with AI model discovery and selection workflows.
  - aid: github:github-graphql-api
    name: GitHub GraphQL API
    tags:
      - GraphQL
      - Query Language
    baseURL: https://api.github.com/graphql
    humanURL: https://docs.github.com/en/graphql
    properties:
      - url: https://docs.github.com/en/graphql
        type: Documentation
      - url: https://docs.github.com/en/graphql/reference
        type: Reference
    description: The GitHub GraphQL API provides a flexible query language for accessing GitHub data, allowing clients to request exactly the fields they need in a single request. It supports queries, mutations, and subscriptions across all GitHub resources including repositories, issues, pull requests, users, organizations, and projects, and is the recommended API for new integrations that need precise data fetching.
  - aid: github:github-campaigns-api
    name: GitHub Campaigns API
    tags:
      - Campaigns
      - Security
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/campaigns?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/campaigns
        type: Documentation
    description: The GitHub Campaigns API lets organization owners and security managers create and manage security campaigns that coordinate remediation of code scanning alerts across multiple repositories. It provides endpoints to list, create, get, update, and delete campaigns, each of which tracks alert statistics including open, closed, and in-progress items, and supports assigning campaign managers from both users and teams.
  - aid: github:github-classroom-api
    name: GitHub Classroom API
    tags:
      - Classroom
      - Education
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/classroom?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/classroom
        type: Documentation
    description: The GitHub Classroom API lets you programmatically interact with GitHub Classroom, providing endpoints to list classrooms, get classroom details, list assignments for a classroom, get assignment details, list accepted assignments for students, and retrieve assignment grades. It is useful for educational administrators and tooling that needs to manage or report on classroom data and student submissions.
  - aid: github:github-code-security-api
    name: GitHub Code Security API
    tags:
      - Code Security
      - Configurations
      - Security
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/code-security?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/code-security
        type: Documentation
    description: The GitHub Code Security API lets organizations and enterprises create and manage reusable code security configurations that standardize security settings across repositories. It provides endpoints to create, retrieve, update, and delete configurations, set defaults, and attach or detach configurations from repositories at both the organization and enterprise level.
  - aid: github:github-credentials-api
    name: GitHub Credentials API
    tags:
      - Authentication
      - Credentials
      - Security
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/credentials?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/credentials
        type: Documentation
    description: The GitHub Credentials API lets you programmatically manage authentication credentials, providing endpoints to revoke a list of credentials such as tokens and keys for security purposes. It enables automated credential lifecycle management and bulk revocation when credentials need to be invalidated.
  - aid: github:github-enterprise-teams-api
    name: GitHub Enterprise Teams API
    tags:
      - Enterprise
      - Teams
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/enterprise-teams?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/enterprise-teams
        type: Documentation
    description: The GitHub Enterprise Teams API lets enterprise owners create and manage enterprise-level teams. It provides endpoints to list, create, get, update, and delete teams, manage team membership including bulk additions and removals, and assign teams to specific organizations within the enterprise.
  - aid: github:github-private-registries-api
    name: GitHub Private Registries API
    tags:
      - Packages
      - Registries
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/private-registries?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/private-registries
        type: Documentation
    description: The GitHub Private Registries API lets organizations configure and manage private package registries. It provides endpoints to list, create, get, update, and delete private registry configurations at the organization level, as well as retrieve the public key used for private registry encryption.
  - aid: github:github-autolinks-api
    name: GitHub Autolinks API
    tags:
      - Autolinks
      - Repositories
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/repos/autolinks?apiVersion=2022-11-28
    properties:
      - url: openapi/github-repo-autolinks-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/repos/autolinks
        type: Documentation
    description: The GitHub Autolinks API lets repository administrators manage autolink references that automatically link issues, pull requests, commit messages, and release descriptions to external third-party services like JIRA or Zendesk. It provides endpoints to list, create, get, and delete autolink references defined by a reference prefix and target URL.
  - aid: github:github-starring-api
    name: GitHub Starring API
    tags:
      - Activity
      - Starring
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/activity/starring?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/activity/starring
        type: Documentation
    description: The GitHub Starring API lets you bookmark repositories and manage your starred list. It provides endpoints to list stargazers for a repository, list repositories starred by the authenticated user or a specific user, check if a repository is starred, and star or unstar a repository. It supports a custom media type that includes a timestamp of when the star was created.
  - aid: github:github-watching-api
    name: GitHub Watching API
    tags:
      - Activity
      - Notifications
      - Watching
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/activity/watching?apiVersion=2022-11-28
    properties:
      - url: https://docs.github.com/en/rest/activity/watching
        type: Documentation
    description: The GitHub Watching API lets you subscribe to notifications for activity in a repository. It provides endpoints to list watchers of a repository, get and set a repository subscription, delete a subscription, and list repositories watched by the authenticated user or a specific user. Watching a repository means you receive notifications for new issues, pull requests, and other activity.
  - aid: github:github-repository-invitations-api
    name: GitHub Repository Invitations API
    tags:
      - Collaborators
      - Invitations
      - Repositories
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/collaborators/invitations?apiVersion=2022-11-28
    properties:
      - url: openapi/github-repo-invitations-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/collaborators/invitations
        type: Documentation
    description: The GitHub Repository Invitations API lets you manage repository collaboration invitations. It provides endpoints to list repository invitations, update an invitation, delete an invitation, list invitations for the authenticated user, and accept or decline a repository invitation.
name: GitHub
tags:
  - Code
  - Pipelines
  - Platform
  - Software Development
  - Source Control
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
            description: With GitHub Copilot, get suggestions for whole lines or entire functionsright inside your editor.
          - name: GitHub Codespaces Access
            description: With GitHub Codespaces, get an instant dev environment in the cloud, so you can code anywhere on any device.
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
            description: Host open source projects in public GitHub repositories, accessible via web or command line. Public repositories are accessible to anyone at GitHub.com.
          - name: Unlimited Private Repositories
            description: Host open source projects in public GitHub repositories, accessible via web or command line. Public repositories are accessible to anyone at GitHub.com.
          - name: Dependabot Security Updates
            description: Keep projects secure by automatically opening pull requests to update vulnerable dependencies and keep them up to date.
          - name: Dependabot Version Updates
            description: Keep projects secure by automatically opening pull requests to update vulnerable dependencies and keep them up to date.
          - name: Issues
            description: Give your developers flexible features for project management that adapts to any team, project, and workflow  all alongside your code.
          - name: Projects
            description: Give your developers flexible features for project management that adapts to any team, project, and workflow  all alongside your code.
          - name: Community Support
            description: Get help with most of your GitHub questions and issues in our Community Forum.
        description: The basics for individuals and organizations
      - id: team
        name: Team
        addOns:
          - name: GitHub Secret Protection
            description: Ensure your secrets stay secure. Mitigate risk associated with exposed secrets in your repositories, while preventing new leaks before they happen with push protection.
          - name: GitHub Code Security
            description: Find and fix vulnerabilities in your code before they reach production. Prioritize your Dependabot alerts with automated triage rules.
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
            description: Host open source projects in public GitHub repositories, accessible via web or command line. Public repositories are accessible to anyone at GitHub.com.
          - name: Unlimited Private Repositories
            description: Host open source projects in public GitHub repositories, accessible via web or command line. Public repositories are accessible to anyone at GitHub.com.
          - name: Dependabot Security Updates
            description: Keep projects secure by automatically opening pull requests to update vulnerable dependencies and keep them up to date.
          - name: Dependabot Version Updates
            description: Keep projects secure by automatically opening pull requests to update vulnerable dependencies and keep them up to date.
          - name: Issues
            description: Give your developers flexible features for project management that adapts to any team, project, and workflow  all alongside your code.
          - name: Projects
            description: Give your developers flexible features for project management that adapts to any team, project, and workflow  all alongside your code.
          - name: Community Support
            description: Get help with most of your GitHub questions and issues in our Community Forum.
          - name: Access to GitHub Codespaces
            description: Blazing fast cloud developer environments with flexible compute and pre-configured containers, developers can code, collaborate, and debug from any browser. Pay only for what you use with compute fees starting at $0.18/hr and storage fees at $0.07/GB per month.
          - name: Protected Branches
            description: Enforce restrictions on how code branches are merged, including requiring reviews by selected collaborators, or allowing only specific contributors to work on a particular branch.
          - name: Multiple Reviewers in Pull Requests
            description: Assign multiple users or a team to review a pull request.
          - name: Draft Pull Requests
            description: Easily discuss and collaborate on pull requests before submitting to formal review.
          - name: Code Owners
            description: Automatically request reviewsor require approvalby selected contributors when changes are made to sections of code that they own.
          - name: Required Reviewers
            description: Ensure that pull requests have a specific number of approving reviews before collaborators can make changes to a protected branch.
          - name: Pages & Wikis
            description: Host documentation and simple websites for your project in a wiki format that contributors can easily edit either on the web or command line.
          - name: Environmental Deployment Branches and Secrets
            description: A job cannot access secrets that are defined in an environment unless it is running on the specified branch.
          - name: Web Based Support
            description: GitHub Support can help you troubleshoot issues you run into while using GitHub.
        description: Advanced collaboration for individuals and organizations.
      - id: enterprise
        name: Enterprise
        addOns:
          - name: Premium Support
            description: With Premium, get a 30-minute SLA on Urgent tickets and 24/7 web and phone support via callback request. With Premium Plus, get everything in Premium, assigned Customer Reliability Engineer and more.
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
            description: Host open source projects in public GitHub repositories, accessible via web or command line. Public repositories are accessible to anyone at GitHub.com.
          - name: Unlimited Private Repositories
            description: Host open source projects in public GitHub repositories, accessible via web or command line. Public repositories are accessible to anyone at GitHub.com.
          - name: Dependabot Security Updates
            description: Keep projects secure by automatically opening pull requests to update vulnerable dependencies and keep them up to date.
          - name: Dependabot Version Updates
            description: Keep projects secure by automatically opening pull requests to update vulnerable dependencies and keep them up to date.
          - name: Issues
            description: Give your developers flexible features for project management that adapts to any team, project, and workflow  all alongside your code.
          - name: Projects
            description: Give your developers flexible features for project management that adapts to any team, project, and workflow  all alongside your code.
          - name: Community Support
            description: Get help with most of your GitHub questions and issues in our Community Forum.
          - name: Access to GitHub Codespaces
            description: Blazing fast cloud developer environments with flexible compute and pre-configured containers, developers can code, collaborate, and debug from any browser. Pay only for what you use with compute fees starting at $0.18/hr and storage fees at $0.07/GB per month.
          - name: Protected Branches
            description: Enforce restrictions on how code branches are merged, including requiring reviews by selected collaborators, or allowing only specific contributors to work on a particular branch.
          - name: Multiple Reviewers in Pull Requests
            description: Assign multiple users or a team to review a pull request.
          - name: Draft Pull Requests
            description: Easily discuss and collaborate on pull requests before submitting to formal review.
          - name: Code Owners
            description: Automatically request reviewsor require approvalby selected contributors when changes are made to sections of code that they own.
          - name: Required Reviewers
            description: Ensure that pull requests have a specific number of approving reviews before collaborators can make changes to a protected branch.
          - name: Pages & Wikis
            description: Host documentation and simple websites for your project in a wiki format that contributors can easily edit either on the web or command line.
          - name: Environmental Deployment Branches and Secrets
            description: A job cannot access secrets that are defined in an environment unless it is running on the specified branch.
          - name: Data Residency
            description: GitHub Enterprise Cloud offers a multi-tenant enterprise SaaS solution on Microsoft Azure, allowing you to choose a regional cloud deployment for data residency, so your in-scope data is stored at rest in a designated location. Start a free 30 day trial today or contact our sales team for more information.
          - name: Managed Users
            description: Own and control the user accounts of your enterprise members through your identity provider (IdP).
          - name: User Provisioning Through SCIM
            description: Automatically invite members to join your organization when you grant access on your IdP. If you remove a member's access to your GitHub organization on your SAML IdP, the member will be automatically removed from the GitHub organization.
          - name: Centrall Manage Multiple Organizations
            description: GitHub Enterprise Cloud includes the option to create an enterprise account, which enables collaboration between multiple organizations, gives administrators a single point of visibility and management and brings license cost savings for identical users in multiple organizations
          - name: Environment Protection Rules
            description: When a workflow job references an environment, the job won't start until all of the environment's protection rules pass.
          - name: Repository Rules
            description: Enforce branch and tag restrictions across your organization, ensuring branch and tag protection across your repositories. Evaluate rules to assess impact before enforcement.
          - name: Audit Log API
            description: As a GitHub Enterprise Cloud organization administrator, you can now access log events using our GraphQL API and monitor the activity in your organization.
          - name: Annual SOC Reports
            description: GitHub offers AICPA System and Organization Controls (SOC) 1 Type 2 and SOC 2 Type 2 reports with IAASB International Standards on Assurance Engagements, ISAE 3000, and ISAE 3402.
          - name: FedRAMP
            description: Government users can host projects on GitHub Enterprise Cloud with the confidence that our platform meets the low impact software-as-a-service (SaaS) baseline of security standards set by our U.S. federal government partners.
          - name: SAML Single Sign-On
            description: Use an identity provider to manage the identities of GitHub users and applications.
          - name: Advanced Auditing
            description: Quickly review the actions performed by members of your organization. Keep copies of audit log data to ensure secure IP and maintain compliance for your organization.
          - name: GitHub Connect
            description: Share features and workflows between your GitHub Enterprise Server instance and GitHub Enterprise Cloud.
        description: Security, compliance, and flexible deployment
    name: Plans
    type: Plans
  - url: https://github.com/github/roadmap
    name: Road Map
    type: RoadMap
  - url: https://github.com/about
    name: About GitHub
    type: About
  - url: https://docs.github.com/en/get-started/exploring-integrations/about-building-integrations
    name: About building integrations - GitHub Docs
    type: Documentation
  - url: https://www.githubstatus.com/
    name: Status
    type: StatusPage
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
    name: GitHub Partners
    type: Partners
  - url: https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
    name: GitHub Terms of Service - GitHub Docs
    type: TermsOfService
  - url: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
    name: GitHub General Privacy Statement - GitHub Docs
    type: PrivacyPolicy
  - url: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28
    name: Rate limits for the REST API - GitHub Docs
    type: RateLimits
  - url: https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api?apiVersion=2022-11-28
    name: Using pagination in the REST API - GitHub Docs
    type: Pagination
  - url: https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28
    name: Authenticating to the REST API - GitHub Docs
    type: Authentication
  - url: https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28
    name: Getting started with the REST API - GitHub Docs
    type: GettingStarted
  - url: https://docs.github.com/en/rest/overview/libraries
    type: sdks
  - url: https://github.blog/
    type: Blog
  - url: https://github.com
    name: GitHub
    type: Website
  - url: https://github.com/login
    name: GitHub Login
    type: Login
  - url: https://github.com/signup
    name: GitHub Sign Up
    type: SignUp
  - url: https://docs.github.com/en/rest
    name: GitHub REST API Documentation
    type: Portal
  - url: https://github.blog/changelog/
    name: GitHub Changelog
    type: ChangeLog
  - url: https://github.com/orgs/community/discussions
    name: GitHub Community
    type: Community
  - url: https://stackoverflow.com/questions/tagged/github-api
    name: GitHub API on Stack Overflow
    type: StackOverflow
  - url: https://www.youtube.com/github
    name: GitHub YouTube
    type: YouTube
  - url: https://github.com/security
    name: GitHub Security
    type: Security
  - url: https://docs.github.com/en/graphql/overview/explorer
    name: GitHub GraphQL API Explorer
    type: DeveloperTools
  - url: https://github.com/github/rest-api-description
    name: GitHub REST API OpenAPI Description
    type: OpenAPI
  - url: https://docs.github.com/en/rest/about-the-rest-api/api-versions
    name: API Versions - GitHub Docs
    type: Versioning
  - url: https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api
    name: Troubleshooting the REST API - GitHub Docs
    type: Errors
  - url: https://docs.github.com/en/rest/quickstart
    name: Quickstart for GitHub REST API - GitHub Docs
    type: Quickstart
  - url: https://docs.github.com/en/webhooks
    name: GitHub Webhooks Documentation
    type: Webhooks
  - url: https://x.com/github
    name: GitHub on X
    type: X
  - url: https://github.com/octokit
    name: Octokit - Official GitHub SDK Libraries
    type: SDKs
  - url: json-schema/github-repository-schema.json
    name: GitHub Repository Schema
    type: JSONSchema
  - url: json-schema/github-issue-schema.json
    name: GitHub Issue Schema
    type: JSONSchema
  - url: json-schema/github-pull-request-schema.json
    name: GitHub Pull Request Schema
    type: JSONSchema
  - url: json-schema/github-user-schema.json
    name: GitHub User Schema
    type: JSONSchema
  - url: json-schema/github-organization-schema.json
    name: GitHub Organization Schema
    type: JSONSchema
  - url: json-schema/github-commit-schema.json
    name: GitHub Commit Schema
    type: JSONSchema
  - url: json-schema/github-webhook-delivery-schema.json
    name: GitHub Webhook Delivery Schema
    type: JSONSchema
  - url: json-ld/github-context.jsonld
    name: GitHub JSON-LD Context
    type: JSON-LD
  - type: Features
    data:
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
    sources:
      - https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
      - https://github.com/pricing
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: CI/CD Automation
        description: Automate build, test, and deployment pipelines with GitHub Actions API.
      - name: Repository Management
        description: Programmatically create, configure, and manage repositories and branches.
      - name: Issue and Project Tracking
        description: Create, update, and query issues, labels, milestones, and project boards.
      - name: Code Review Automation
        description: Automate pull request reviews, checks, and merge workflows.
      - name: Security Scanning
        description: Access Dependabot alerts, code scanning results, and secret scanning alerts.
      - name: Developer Tools
        description: Build GitHub Apps, CLI extensions, and IDE integrations.
      - name: Organization Management
        description: Manage teams, members, permissions, and audit logs for organizations.
      - name: Package Publishing
        description: Publish and manage packages across multiple package registries.
  - type: Integrations
    data:
      - name: VS Code
        description: GitHub integration in Visual Studio Code with Copilot, PR reviews, and Codespaces.
      - name: Slack
        description: GitHub notifications, deployments, and actions in Slack channels.
      - name: Jira
        description: Link GitHub commits and PRs to Jira issues for project tracking.
      - name: Terraform
        description: Manage GitHub repositories, teams, and settings as infrastructure code.
      - name: Azure DevOps
        description: Cross-platform CI/CD with GitHub repos and Azure Pipelines.
  - type: Solutions
    data:
      - name: GitHub Free
        description: Free tier with unlimited public and private repos, Actions minutes, and Packages storage.
      - name: GitHub Pro
        description: Advanced tools for individual developers with more Actions minutes and Packages.
      - name: GitHub Team
        description: Collaboration features for teams with code owners, required reviews, and Pages.
      - name: GitHub Enterprise
        description: Enterprise features with SAML SSO, audit log streaming, and advanced security.
created: 2024/04/14
modified: '2026-05-04'
position: Consuming
description: The GitHub REST API allows developers to programmatically interact with GitHub resources including repositories, users, organizations, pull requests, issues, and more.
maintainers:
  - name: Kin Lane
    url: http://apievangelist.com
    email: kin@apievangelist.com
  - name: GitHub
    email: support@github.com
    url: https://github.com
specificationVersion: '0.19'
image: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png
---
