---
aid: github
url: https://raw.githubusercontent.com/api-search/code/main/_apis/github/apis.md
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
      - url: properties/github-app-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/apps
        type: Documentation
    description: >-
      The GitHub App API is the set of REST/GraphQL endpoints and webhooks that
      lets a GitHub App securely integrate with and automate work across GitHub.
      Apps authenticate with a shortlived JSON Web Token and exchange it for
      installation access tokens to act on specific repositories or
      organizations with finegrained, leastprivilege permissions, or use
      user-to-server OAuth to act on behalf of a user when needed. Through the
      API, an app can manage its installations, control which repositories it
      has access to, and read/write resources like issues, pull requests,
      commits, checks, deployments, and releases, as well as report status and
      check results. Webhooks deliver event payloads (for example, pushes and PR
      activity) so the app can react in real time, and app manifests enable
      streamlined, oneclick setup. In short, it provides the permissionscoped
      surface for building secure bots, CI/CD integrations, and other
      automations on GitHub.
  - aid: github:github-auth-api
    name: GitHub Authorization API
    tags:
      - Authorization
      - Authentication
    baseURL: https://api.github.com
    humanURL: >-
      https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28
    properties:
      - url: properties/github-auth-api-openapi.yml
        type: OpenAPI
      - url: >-

          https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api
        type: Documentation
    description: >-
      The GitHub Authorization (OAuth Authorizations) API historically let you
      programmatically create, list, inspect, and revoke access tokens for a
      user or OAuth applicationsetting scopes, verifying token validity,
      rotating or deleting tokens, and generally managing what an app could do
      on a users behalf. It was commonly used with basic authentication (and
      2FA) to mint personal access tokens and to manage OAuth app grants. For
      security reasons, these endpoints have been deprecated and disabled on
      GitHub.com; today, apps should use modern authorization flows (OAuth web
      or device flow) or GitHub Apps with finegrained permissions, and manage
      personal access tokens via the web UI or the current OAuth application
      endpoints for token verification and revocation.
  - aid: github:github-code-of-conduct-api
    name: GitHub Code of Conduct API
    tags:
      - Code of Conduct
    baseURL: https://api.github.com
    humanURL: >-
      https://docs.github.com/en/rest/codes-of-conduct/codes-of-conduct?apiVersion=2022-11-28
    properties:
      - url: properties/github-code-of-conduct-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/codes-of-conduct/codes-of-conduct
        type: Documentation
    description: >-
      GitHubs Code of Conduct API lets apps discover and retrieve the community
      codes of conduct that GitHub supports and see which one a repository has
      adopted. Through REST endpoints, clients can list available templates
      (like the Contributor Covenant), fetch a specific code by key, and read a
      repositorys code-of-conduct metadata and text, including fields such as
      name, key, URL, and body. This enables tooling to display community
      standards, audit or report adoption, and bootstrap repo files. Some
      endpoints are (or have been) in preview and may require a special Accept
      header, authentication is needed for private repositories, and updates are
      not done via the API but by committing the file to the repo.
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
    description: >-
      The GitHub Emojis API is a simple REST endpoint (GET /emojis or
      https://api.github.com/emojis) that returns a JSON dictionary mapping
      emoji shortcodes (like "smile" or "octocat") to the image URLs GitHub uses
      to render them. It covers both standard Unicode emoji and GitHub-specific
      custom ones, enabling clients to power emoji pickers, autocomplete for
      :shortcodes:, validation, or server-side rendering in apps that mirror
      GitHubs formatting. The endpoint is public and requires no auth, but
      using authentication increases rate limits; results change infrequently,
      so caching is recommended. Note that this list is broader than the
      specific set allowed for Reactions, which has its own constraints.
  - aid: github:github-events-api
    name: GitHub Events API
    tags:
      - Events
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/activity/events?apiVersion=2022-11-28
    properties:
      - url: properties/github-events-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Events API provides a read-only feed of recent activity on
      GitHub, exposing structured event objects you can poll to see what
      happened across the platform or within a specific repository,
      organization, or user account. It covers many event typessuch as pushes,
      pull requests, issues, comments, releases, stars, forks, and membership
      changeseach with consistent metadata (actor, repo, type, payload,
      timestamps, IDs). Endpoints like /events, /repos/{owner}/{repo}/events,
      /orgs/{org}/events, and user/received variants let you scope activity, and
      authenticated calls include private events youre authorized to view. Its
      useful for dashboards, analytics, and lightweight monitoring, but its not
      a streaming feed: events are transient, must be paginated and polled, are
      rate-limited, and arent guaranteed to be complete over long periods. For
      real-time reaction to changes, GitHub recommends Webhooks; for historical
      analyses, external archives or data exports are better suited.
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
      - url: properties/github-feeds-api-openapi.yml
        type: OpenAPI
    description: >-
      GitHubs Feeds API lets you programmatically discover the Atom feed URLs
      for GitHub activity thats relevant to you, such as the global timeline, a
      specific users activity, the authenticated users public and private
      activity, organization activity, and security advisories. It doesnt
      return events directly; instead, it provides the correct,
      authentication-aware links you can subscribe to with any RSS/Atom reader
      to receive updates like new issues, pull requests, comments, releases, and
      other public or authorized activity. Unauthenticated calls expose only
      public feeds, while authenticated calls include private feeds youre
      allowed to see. Clients typically fetch those feed URLs on an interval and
      use ETags for efficient polling, making it a simple way to integrate
      GitHub activity into dashboards, readers, or notification systems.
  - aid: github:github-gists-api
    name: GitHub Gists API
    tags:
      - Gists
      - Code
      - Artifacts
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/gists?apiVersion=2022-11-28
    properties:
      - url: properties/github-gists-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Gists API lets you programmatically manage gistslightweight
      code snippets and notesover HTTP. You can create gists (public or
      secret/unlisted), read individual gists, list public gists, your own, a
      users, and those youve starred, fetch raw file contents, view version
      history and commits, update gists by adding/renaming/removing files or
      changing descriptions, and delete them. It also supports forking,
      starring/un-starring and checking star status, plus full CRUD for gist
      comments. Responses include metadata such as owner, files, visibility,
      timestamps, and revision SHAs, with pagination and conditional requests
      available. Public gists are readable without authentication; modifying
      gists or accessing private data requires an access token with the gist
      scope, and standard GitHub REST rate limits apply.
  - aid: github:github-gitignore-templates-api
    name: GitHub Gitignore Templates API
    tags:
      - Templates
      - Gitignore
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/gitignore?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-gitignore-templates-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-gitignore-templates-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Gitignore Templates API is a REST interface that lets you
      discover and fetch canonical .gitignore templates maintained by GitHub, so
      you can programmatically create ignore files tailored to specific
      languages, frameworks, IDEs, or operating systems. It provides endpoints
      to list all available template names and to retrieve the full content of a
      chosen template (for example, Node, Python, macOS, or VisualStudio) via
      GET /gitignore/templates and GET /gitignore/templates/{name}. The
      responses include the templates name and the text to write into
      .gitignore, making it easy to scaffold new repositories, standardize
      ignore rules across teams, and prevent accidental commits of build
      artifacts, dependencies, or OS/IDE files; its accessible publicly, with
      authentication available for higher rate limits.
  - aid: github:github-installation-api
    name: GitHub Installation API
    tags:
      - Installations
    baseURL: https://api.github.com/
    properties:
      - url: properties/github-installation-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Installation API is part of the GitHub Apps platform and lets
      an app understand and manage where its installed and what it can access,
      and act on behalf of that installation. Using these endpoints, an app can
      list its installations, fetch details for a specific installation,
      enumerate the repositories granted to it, and (when the app is configured
      for selected repositories) add or remove repository access. Critically,
      it allows the app to exchange its JWT for shortlived installation access
      tokens that carry the installations permissions and repository scope;
      those tokens are then used to call GitHubs REST or GraphQL APIs or to
      perform Git operations over HTTPS. All actions are constrained by the
      permissions defined in the apps manifest and the repositories selected at
      install time, ensuring leastprivilege access. In short, this API is how a
      GitHub App securely discovers its tenants (user/org accounts), scopes its
      access, and performs work on their repositories without acting as an end
      user.
  - aid: github:github-issues-api
    name: GitHub Issues API
    tags:
      - Issues
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/issues?apiVersion=2022-11-28
    properties:
      - url: properties/github-issues-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Issues API lets you programmatically manage issue tracking on
      GitHub, enabling you to list and filter issues across repositories, create
      and edit issues, change their state (open/closed), and manage assignees,
      labels, and milestones. It supports adding, updating, and deleting
      comments; applying reactions; locking or unlocking conversations; and
      viewing issue events and timelines for auditing and automation. You can
      search issues, transfer them between repositories, and subscribe to
      notifications, and you can receive updates via webhooks. The API is
      available through both REST and GraphQL, with authentication and
      pagination/rate limiting, making it useful for building triage bots,
      dashboards, reports, and custom workflow automations.
  - aid: github:github-licenses-api
    name: GitHub Licenses API
    tags:
      - Licenses
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/licenses?apiVersion=2022-11-28
    properties:
      - url: properties/github-licenses-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Licenses API lets you programmatically discover and retrieve
      open source license information across GitHub. It provides endpoints to
      list the common licenses GitHub supports, get detailed metadata and the
      canonical text for a specific license (by its SPDX identifier), and fetch
      the detected license for a given repository. Responses include
      machine-readable fields such as name, key, spdx_id, description, and the
      permissions/conditions/limitations that summarize how a license can be
      used, plus the full license text/template you can render in your app. This
      makes it useful for compliance checks, inventory and reporting, helping
      users choose a license, and validating or displaying repository licensing
      in developer tools.
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
      - url: properties/github-manage-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Enterprise Management API lets administrators automate and
      integrate the operational and security management of their enterprise on
      GitHub. It covers tasks like provisioning and governing organizations,
      users, and teams; enforcing policies for repositories, security, and
      GitHub Actions; integrating identity and access management via SSO/SCIM;
      retrieving audit logs and usage data for compliance and billing; and
      managing self-hosted runners. For GitHub Enterprise Server, it also
      includes Management Console endpoints to configure instance settings (such
      as TLS, SMTP, and clustering), apply licenses, monitor health, and
      coordinate backups and restores. By exposing these controls via REST,
      GraphQL, and SCIM endpoints, the API enables large-scale automation and
      integration with ITSM, IdPs, and SIEM tools.
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
      - url: properties/github-markdown-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/markdown
        type: Documentation
    description: >-
      The GitHub Markdown API is a REST service that converts
      Markdownespecially GitHub Flavored Markdowninto the same HTML GitHub
      renders in READMEs, issues, and pull requests, so external apps can
      display content consistently with GitHub. You POST Markdown to its
      endpoints (/markdown or /markdown/raw) and get back HTML; you can choose
      standard markdown or gfm mode and optionally supply a repository
      context so shorthand references (like #123), commit SHAs, user mentions,
      emoji, task lists, tables, and other GFM features resolve as they do on
      GitHub. Its stateless and rate-limited, doesnt store your content, and
      returns HTML that your application should treat as untrusted and sanitize
      before inserting into a page.
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
      - url: properties/github-meta-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/meta
        type: Documentation
    description: |-

      Use the REST API to get meta information about GitHub, including the IP
      addresses of GitHub services.
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
      - url: properties/github-networks-api-openapi.yml
        type: OpenAPI
    description: >-
      GitHubs Networks API lets you retrieve a stream of public activity that
      occurs across a repositorys network, meaning the original repo and all
      of its forks. Exposed via the Events API (for example, listing events for
      /networks/{owner}/{repo}/events), it returns the same event types you see
      in other GitHub event feedspushes, pull requests, issues, releases, and
      moreaggregated across every repo in that fork family. This makes it
      useful for monitoring whats happening across forks, building dashboards
      or notifications that track downstream and upstream changes, and analyzing
      collaboration patterns. Results are read-only, public-only, paginated, and
      subject to standard GitHub API rate limits.
  - aid: github:github-notifications-api
    name: GitHub Notifications API
    tags:
      - Notifications
    baseURL: https://api.github.com/
    humanURL: >-

      https://docs.github.com/en/rest/activity/notifications?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-notifications-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-notifications-api-openapi.yml
        type: OpenAPI
    description: >-
      This GitHub REST API allows you to programmatically manage your GitHub
      notifications, which include updates on issues, pull requests, and
      commits. The API requires authentication via a personal access token
      (classic) and needs either the notifications or repo scope to function. 
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
      - url: properties/github-octocat-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Octocat API is a playful, non-functional endpoint in GitHubs
      REST API that returns an ASCII-art rendering of the Octocat mascot as
      plain text. Its primarily meant for fun and demospeople often use it to
      sanity-check connectivity, see how the API formats responses and headers,
      or showcase simple requests without touching real repository data. It
      doesnt manage or expose any GitHub resources, and in some clients you can
      even supply a short message that the Octocat says. Like other public
      endpoints, its accessible without authentication but still subject to
      GitHubs standard rate limits.
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
      - url: properties/github-org-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Organization API lets you programmatically administer and
      integrate with organizations on GitHub, spanning both REST and GraphQL. It
      covers core governance tasks such as reading and updating org settings and
      policies, managing members and outside collaborators, sending invitations
      and assigning roles, organizing teams and their permissions, and
      controlling repository access at scale. It also supports operational and
      security workflows, including organization webhooks, audit log retrieval,
      required security and compliance settings (e.g., Dependabot and secret
      scanning policies), finegrained personal access token and GitHub App
      installation approvals, and management of Actions resources like
      selfhosted runners. Where applicable, it integrates with SSO/SCIM
      provisioning and exposes usage/billing and installation dataenabling
      endtoend automation of org operations, security, and permissions.
  - aid: github:github-projects-api
    name: GitHub Projects API
    tags:
      - Projects
    baseURL: https://api.github.com/
    overlays:
      - url: overlays/github-projects-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-projects-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Projects API enables developers to programmatically create and
      manage GitHub Projects, which are flexible tools for planning and tracking
      work using customizable boards, tables, and roadmaps. Through these REST
      API endpoints, you can create projects at the repository, organization, or
      user level, add and organize items like issues and pull requests, manage
      project fields and views, update item statuses and metadata, and automate
      project workflows. This API is particularly useful for integrating project
      management functionality into custom applications, automating project
      updates based on repository events, building dashboards and reporting
      tools, or synchronizing GitHub project data with external project
      management systems.
  - aid: github:github-rate-limit-api
    name: GitHub Rate Limit API
    tags:
      - Rate Limits
    baseURL: https://api.github.com/
    humanURL: >-

      https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-rate-limit-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-rate-limit-openapi.yml
        type: OpenAPI
    description: >-
      GitHubs Rate Limit API lets you programmatically see how much API quota
      you have left and when it will reset, so you can avoid hitting API rate
      limit exceeded errors. By calling the /rate_limit endpoint (or by reading
      the X-RateLimit headers on any response), you get current limit,
      remaining, used, and reset time for different resource categories (for
      example, core REST, search, and GraphQL). The values are scoped to how you
      authenticate (unauthenticated IP, personal access token, OAuth app, or
      GitHub App installation) and can vary by resource type and plan. Apps
      typically use this information to throttle requests, prioritize work, or
      back off and retry after the reported reset time. Note that separate
      secondary/abuse protections may still apply and arent reflected by this
      endpoint.
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
      - url: properties/github-repos-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Repos API is a set of REST endpoints that let you
      programmatically create, read, update, and delete repositories and their
      resources, giving you control over a repos lifecycle and configuration.
      You can list and search repositories for users or organizations; retrieve
      metadata (visibility, default branch, license), topics, and languages;
      manage collaborators, teams, and permissions; create, archive, transfer,
      fork, star, and watch; manage branches and branch protection rules, tags,
      releases and assets; read and write repository contents (files,
      directories, blobs), commits, and compares; configure webhooks and deploy
      keys; and access traffic, vulnerabilities, and community health metrics.
      It uses token-based authentication with scopes (such as repo) and is
      rate-limited, making it suitable for automation, dashboards, and CI/CD
      integrations.
  - aid: github:github-scim-api
    name: GitHub SCIM API
    tags:
      - SCIM
    baseURL: https://api.github.com/
    humanURL: >-

      https://docs.github.com/en/enterprise-cloud@latest/rest/scim?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-scim-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-scim-openapi.yml
        type: OpenAPI
    description: >-
      GitHubs SCIM API implements the SCIM 2.0 standard to automate user
      lifecycle management from an identity provider (such as Entra ID/Azure AD,
      Okta, or OneLogin) to GitHub Enterprise Cloud. It lets you provision,
      update, suspend/reactivate, and deprovision users, keeping their GitHub
      access in sync with your IdP. For organizations that use SAML SSO, SCIM
      manages external identities and org membership; for enterprises using
      Enterprise Managed Users, it creates and maintains the managed user
      accounts themselves. Typical operations include creating users, updating
      profile attributes, and setting a users active state to revoke or restore
      access. SCIM complements SSO (authentication) by handling authorization
      and account lifecycle; it doesnt manage repositories or granular
      permissions beyond controlling whether a user exists and has access to the
      org or enterprise.
  - aid: github:github-search-api
    name: GitHub Search API
    tags:
      - Search
      - Discovery
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-search-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-search-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Search API lets you programmatically find and filter content
      across GitHubincluding repositories, code, issues and pull requests,
      commits, users, topics, and labelsusing a powerful query language with
      qualifiers (for example by language, stars, forks, org/user,
      path/filename, label, state, author, or committer). It returns ranked,
      paginated JSON results with total counts and optional sorting, so you can
      discover projects, locate code snippets, triage issues, or audit activity
      at scale. Authenticated requests enjoy higher rate limits and can search
      private resources the token can access, and the API returns only the first
      1,000 matching results for any query.
  - aid: github:github-setup-api
    name: GitHub Setup API
    tags:
      - Setup
    baseURL: https://api.github.com/
    humanURL: >-
      https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-setup-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-setup-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Setup API is the administrative interface for GitHub Enterprise
      Server that lets you automate tasks normally done in the Management
      Console during first-time and ongoing configuration. It provides endpoints
      to upload and apply your license, set the hostname and TLS certificates,
      configure system services like SMTP, create or reset the initial admin
      credentials, start and monitor reconfiguration runs, and query setup
      status and health. This API is intended for bootstrapping and repeatable
      provisioning (for example, cloud deployment or disaster recovery) and is
      restricted to authorized administrators. It is separate from the public
      GitHub REST and GraphQL APIs used for repositories, issues, and other
      developer workflows.
  - aid: github:github-teams-api
    name: GitHub Teams API
    tags:
      - Teams
    baseURL: https://api.github.com/
    overlays:
      - url: overlays/github-teams-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-teams-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Teams API lets you programmatically manage organization teams
      and the access they grant. With it, you can create, update, and delete
      teams; organize parent/child team hierarchies; add or remove members and
      maintainers; send and manage invitations; and list or audit team
      membership. It also lets you grant, adjust, or revoke a teams permissions
      to repositories (and, where applicable, projects), enabling consistent,
      leastprivilege access control at scale. For enterprise setups, it
      supports syncing teams with external identity provider groups. These
      capabilities are available via REST and GraphQL, and require appropriate
      organization admin or team maintainer permissions and token scopes.
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
    description: >-
      The GitHub Zen API is a playful REST endpoint that returns a random
      aphorism from the Zen of GitHub, such as Keep it logically awesome.
      Each request to GET https://api.github.com/zen responds with a single
      plain-text line, making it useful for quick connectivity checks, demoing
      HTTP calls, or verifying authentication. It doesnt require auth, but you
      can include a token to benefit from higher rate limits. Because it returns
      just a simple string with minimal structure, it serves as a lightweight
      sanity check and a fun Easter egg within the GitHub API.
  - aid: github:github-user-api
    name: GitHub User API
    tags:
      - Users
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/users?apiVersion=2022-11-28
    properties:
      - url: properties/github-users-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Users API (part of the REST API) lets applications read and,
      for the authenticated account, manage user-related data on GitHub. It can
      fetch public profiles for any user or the authenticated users private
      profile details, list a users public repositories and organizations, and
      view activity like followers and following. For the signed-in user it also
      supports actions such as updating profile metadata, following or
      unfollowing users, blocking users, and managing account artifacts like
      emails, SSH/GPG/signing keys, and linked social accounts. Endpoints honor
      pagination and conditional requests, and access to private data or write
      operations requires authentication with appropriate token scopes. This
      makes it useful for building integrations that personalize experiences,
      synchronize account data, or automate account settings.
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
modified: '2025-12-23'
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