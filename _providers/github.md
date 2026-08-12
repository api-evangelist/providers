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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 64.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 1203
  human_in_the_loop: 31
  name: Github Agentic Access
  operation_count: 2431
  slug: github-agentic-access
  summary_line: 2431 operations · 1203 acting · 31 human-in-the-loop
api_count: 350
apis:
- description: The GitHub Events API provides a read-only feed of recent activity on GitHub, exposing structured event objects you can poll to see what happened across the platform or within a specific repository, o
  name: GitHub Events API
  slug: github-events-api
- description: GitHubs Feeds API lets you programmatically discover the Atom feed URLs for GitHub activity thats relevant to you, such as the global timeline, a specific users activity, the authenticated users publi
  name: GitHub Feeds API
  slug: github-feeds-api
- description: The GitHub Gists API lets you programmatically manage gistslightweight code snippets and notesover HTTP. You can create gists (public or secret/unlisted), read individual gists, list public gists, you
  name: GitHub Gists API
  slug: github-gists-api
- description: The GitHub Issues API lets you programmatically manage issue tracking on GitHub, enabling you to list and filter issues across repositories, create and edit issues, change their state (open/closed), a
  name: GitHub Issues API
  slug: github-issues-api
- description: The GitHub Licenses API lets you programmatically discover and retrieve open source license information across GitHub. It provides endpoints to list the common licenses GitHub supports, get detailed m
  name: GitHub Licenses API
  slug: github-licenses-api
- description: The GitHub Markdown API is a REST service that converts Markdownespecially GitHub Flavored Markdowninto the same HTML GitHub renders in READMEs, issues, and pull requests, so external apps can display
  name: GitHub Markdown API
  slug: github-markdown-api
- description: Use the REST API to get meta information about GitHub, including the IP addresses of GitHub services.
  name: GitHub Meta API
  slug: github-meta-api
- description: This GitHub REST API allows you to programmatically manage your GitHub notifications, which include updates on issues, pull requests, and commits. The API requires authentication via a personal access
  name: GitHub Notifications API
  slug: github-notifications-api
- description: The GitHub Octocat API is a playful, non-functional endpoint in GitHubs REST API that returns an ASCII-art rendering of the Octocat mascot as plain text. Its primarily meant for fun and demospeople of
  name: GitHub Octocat API
  slug: github-octocat-api
- description: The GitHub Projects API enables developers to programmatically create and manage GitHub Projects, which are flexible tools for planning and tracking work using customizable boards, tables, and roadmap
  name: GitHub Projects API
  slug: github-projects-api
- description: The GitHub Repos API is a set of REST endpoints that let you programmatically create, read, update, and delete repositories and their resources, giving you control over a repos lifecycle and configura
  name: GitHub Repos API
  slug: github-repos-api
- description: The GitHub Search API lets you programmatically find and filter content across GitHubincluding repositories, code, issues and pull requests, commits, users, topics, and labelsusing a powerful query la
  name: GitHub Search API
  slug: github-search-api
- description: The GitHub Users API (part of the REST API) lets applications read and, for the authenticated account, manage user-related data on GitHub. It can fetch public profiles for any user or the authenticate
  name: GitHub User API
  slug: github-user-api
- description: 'The GitHub Checks API lets you create and manage check runs and check suites that report detailed status, annotations, and results for commits. It enables CI/CD tools and integrations to report build '
  name: GitHub Checks API
  slug: github-checks-api
- description: 'The GitHub Deployments API lets you create and manage deployments and deployment statuses for repositories. Deployments are requests to deploy a specific ref (branch, SHA, tag) to an environment, and '
  name: GitHub Deployments API
  slug: github-deployments-api
- description: The GitHub Releases API lets you create, edit, and delete releases for a repository, as well as upload and manage release assets (binaries, installers, archives). Releases are based on Git tags and pr
  name: GitHub Releases API
  slug: github-releases-api
- description: The GitHub Pages API lets you manage GitHub Pages sites for repositories, including creating, updating, and deleting sites, configuring custom domains and HTTPS enforcement, and triggering and monitor
  name: GitHub Pages API
  slug: github-pages-api
- description: The GitHub Packages API lets you manage packages and package versions in GitHub Packages, a software package hosting service that supports npm, Maven, Gradle, RubyGems, NuGet, Docker, and other packag
  name: GitHub Packages API
  slug: github-packages-api
- description: The GitHub Git Database API provides low-level access to Git objects (blobs, commits, refs, tags, and trees) in a repository. It lets you read and write raw Git data directly, enabling operations like
  name: GitHub Git Database API
  slug: github-git-database-api
- description: The GitHub Codespaces API lets you create, manage, start, stop, and delete cloud development environments (codespaces) for repositories. It provides endpoints for managing codespace secrets, machine t
  name: GitHub Codespaces API
  slug: github-codespaces-api
- description: The GitHub Copilot API lets organization and enterprise owners manage GitHub Copilot seat assignments, retrieve usage metrics and billing information, and configure Copilot policies. It provides endpo
  name: GitHub Copilot API
  slug: github-copilot-api
- description: The GitHub Billing API lets you view billing and usage information for organizations and enterprises, including Actions minutes, Packages storage and data transfer, Codespaces usage, and shared storag
  name: GitHub Billing API
  slug: github-billing-api
- description: The GitHub Migrations API lets you migrate data to and from GitHub. It supports organization migrations that export repositories and metadata as downloadable archives, source imports that convert repo
  name: GitHub Migrations API
  slug: github-migrations-api
- description: The GitHub Secret Scanning API lets you retrieve and manage secret scanning alerts for repositories, organizations, and enterprises. Secret scanning detects tokens, keys, and other credentials acciden
  name: GitHub Secret Scanning API
  slug: github-secret-scanning-api
- description: The GitHub Security Advisories API lets you view and manage security advisories for repositories and access the GitHub Advisory Database. It provides endpoints to create, update, and list repository s
  name: GitHub Security Advisories API
  slug: github-security-advisories-api
- description: The GitHub Commits API lets you list, retrieve, and compare commits in a repository, as well as manage commit comments and commit statuses. It provides endpoints for viewing commit details, listing pu
  name: GitHub Commits API
  slug: github-commits-api
- description: 'The GitHub Reactions API lets you create, list, and delete emoji reactions on issues, pull requests, issue comments, pull request review comments, commit comments, release assets, and team discussion '
  name: GitHub Reactions API
  slug: github-reactions-api
- description: The GitHub Deploy Keys API lets you manage deploy keys for repositories. Deploy keys are SSH keys that grant read-only or read-write access to a single repository, commonly used for automated deployme
  name: GitHub Deploy Keys API
  slug: github-deploy-keys-api
- description: The GitHub Dependency Graph API lets you view and submit dependency information for a repository. It provides endpoints to export the software bill of materials (SBOM) for a repository and to submit d
  name: GitHub Dependency Graph API
  slug: github-dependency-graph-api
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
- description: The About API from GitHub — 2 operation(s) for about.
  name: GitHub About API
  slug: github-about-api
- description: The Access API from GitHub — 12 operation(s) for access.
  name: GitHub Access API
  slug: github-access-api
- description: The Accessible API from GitHub — 3 operation(s) for accessible.
  name: GitHub Accessible API
  slug: github-accessible-api
- description: Endpoints to manage GitHub Actions using the REST API.
  name: GitHub Actions API
  slug: github-actions-api
- description: The Active API from GitHub — 1 operation(s) for active.
  name: GitHub Active API
  slug: github-active-api
- description: The Activity API from GitHub — 25 operation(s) for activity.
  name: GitHub Activity API
  slug: github-activity-api
- description: The Add API from GitHub — 27 operation(s) for add.
  name: GitHub Add API
  slug: github-add-api
- description: The Administrative API from GitHub — 1 operation(s) for administrative.
  name: GitHub Administrative API
  slug: github-administrative-api
- description: The Advanced API from GitHub — 1 operation(s) for advanced.
  name: GitHub Advanced API
  slug: github-advanced-api
- description: The Alerts API from GitHub — 11 operation(s) for alerts.
  name: GitHub Alerts API
  slug: github-alerts-api
- description: The All API from GitHub — 13 operation(s) for all.
  name: GitHub All API
  slug: github-all-api
- description: The Allowed API from GitHub — 2 operation(s) for allowed.
  name: GitHub Allowed API
  slug: github-allowed-api
- description: The Analysis API from GitHub — 3 operation(s) for analysis.
  name: GitHub Analysis API
  slug: github-analysis-api
- description: The Annotations API from GitHub — 1 operation(s) for annotations.
  name: GitHub Annotations API
  slug: github-annotations-api
- description: The Announcement API from GitHub — 1 operation(s) for announcement.
  name: GitHub Announcement API
  slug: github-announcement-api
- description: The Applications API from GitHub — 26 operation(s) for applications.
  name: GitHub Applications API
  slug: github-applications-api
- description: The Apps API from GitHub — 23 operation(s) for apps.
  name: GitHub Apps API
  slug: github-apps-api
- description: The Archive API from GitHub — 3 operation(s) for archive.
  name: GitHub Archive API
  slug: github-archive-api
- description: The Artifacts API from GitHub — 4 operation(s) for artifacts.
  name: GitHub Artifacts API
  slug: github-artifacts-api
- description: The Assets API from GitHub — 2 operation(s) for assets.
  name: GitHub Assets API
  slug: github-assets-api
- description: The Assigned API from GitHub — 4 operation(s) for assigned.
  name: GitHub Assigned API
  slug: github-assigned-api
- description: The Assignees API from GitHub — 3 operation(s) for assignees.
  name: GitHub Assignees API
  slug: github-assignees-api
- description: The Associated API from GitHub — 1 operation(s) for associated.
  name: GitHub Associated API
  slug: github-associated-api
- description: The Attempts API from GitHub — 3 operation(s) for attempts.
  name: GitHub Attempts API
  slug: github-attempts-api
- description: The Attribute API from GitHub — 2 operation(s) for attribute.
  name: GitHub Attribute API
  slug: github-attribute-api
- description: The Audit API from GitHub — 1 operation(s) for audit.
  name: GitHub Audit API
  slug: github-audit-api
- description: The Authenticated API from GitHub — 43 operation(s) for authenticated.
  name: GitHub Authenticated API
  slug: github-authenticated-api
- description: The Authorization API from GitHub — 5 operation(s) for authorization.
  name: GitHub Authorization API
  slug: github-authorization-api
- description: The Authorized API from GitHub — 1 operation(s) for authorized.
  name: GitHub Authorized API
  slug: github-authorized-api
- description: The Autolinks API from GitHub — 2 operation(s) for autolinks.
  name: GitHub Autolinks API
  slug: github-autolinks-api
- description: The Banner API from GitHub — 1 operation(s) for banner.
  name: GitHub Banner API
  slug: github-banner-api
- description: The Between API from GitHub — 2 operation(s) for between.
  name: GitHub Between API
  slug: github-between-api
- description: The Bill API from GitHub — 1 operation(s) for bill.
  name: GitHub Bill API
  slug: github-bill-api
- description: Monitor charges and usage from Actions and Packages.
  name: GitHub Billing API
  slug: github-billing-api
- description: The Blobs API from GitHub — 2 operation(s) for blobs.
  name: GitHub Blobs API
  slug: github-blobs-api
- description: The Branches API from GitHub — 14 operation(s) for branches.
  name: GitHub Branches API
  slug: github-branches-api
- description: The Builds API from GitHub — 3 operation(s) for builds.
  name: GitHub Builds API
  slug: github-builds-api
- description: The Cache API from GitHub — 7 operation(s) for cache.
  name: GitHub Cache API
  slug: github-cache-api
- description: The Caches API from GitHub — 1 operation(s) for caches.
  name: GitHub Caches API
  slug: github-caches-api
- description: The Cancel API from GitHub — 1 operation(s) for cancel.
  name: GitHub Cancel API
  slug: github-cancel-api
- description: The Card API from GitHub — 3 operation(s) for card.
  name: GitHub Card API
  slug: github-card-api
- description: The Cards API from GitHub — 1 operation(s) for cards.
  name: GitHub Cards API
  slug: github-cards-api
- description: The Check API from GitHub — 2 operation(s) for check.
  name: GitHub Check API
  slug: github-check-api
- description: The Checks API from GitHub — 28 operation(s) for checks.
  name: GitHub Checks API
  slug: github-checks-api
- description: The Child API from GitHub — 2 operation(s) for child.
  name: GitHub Child API
  slug: github-child-api
- description: The Claims API from GitHub — 2 operation(s) for claims.
  name: GitHub Claims API
  slug: github-claims-api
- description: The Code API from GitHub — 9 operation(s) for code.
  name: GitHub Code API
  slug: github-code-api
- description: The Code Owners API from GitHub — 1 operation(s) for code owners.
  name: GitHub Code Owners API
  slug: github-code-owners-api
- description: Retrieve code scanning alerts from a repository.
  name: GitHub Code-Scanning API
  slug: github-code-scanning-api
- description: The Codes-Of-Conduct API from GitHub — 2 operation(s) for codes-of-conduct.
  name: GitHub Codes-Of-Conduct API
  slug: github-codes-of-conduct-api
- description: The Collaborators API from GitHub — 6 operation(s) for collaborators.
  name: GitHub Collaborators API
  slug: github-collaborators-api
- description: The Column API from GitHub — 1 operation(s) for column.
  name: GitHub Column API
  slug: github-column-api
- description: The Columns API from GitHub — 2 operation(s) for columns.
  name: GitHub Columns API
  slug: github-columns-api
- description: The Combined API from GitHub — 1 operation(s) for combined.
  name: GitHub Combined API
  slug: github-combined-api
- description: The Comment API from GitHub — 15 operation(s) for comment.
  name: GitHub Comment API
  slug: github-comment-api
- description: The Comments API from GitHub — 18 operation(s) for comments.
  name: GitHub Comments API
  slug: github-comments-api
- description: The Commits API from GitHub — 24 operation(s) for commits.
  name: GitHub Commits API
  slug: github-commits-api
- description: The Committers API from GitHub — 1 operation(s) for committers.
  name: GitHub Committers API
  slug: github-committers-api
- description: The Compare API from GitHub — 1 operation(s) for compare.
  name: GitHub Compare API
  slug: github-compare-api
- description: The Conduct API from GitHub — 2 operation(s) for conduct.
  name: GitHub Conduct API
  slug: github-conduct-api
- description: The Configuration API from GitHub — 6 operation(s) for configuration.
  name: GitHub Configuration API
  slug: github-configuration-api
- description: The Conflicting API from GitHub — 3 operation(s) for conflicting.
  name: GitHub Conflicting API
  slug: github-conflicting-api
- description: The Connection API from GitHub — 1 operation(s) for connection.
  name: GitHub Connection API
  slug: github-connection-api
- description: The Content API from GitHub — 2 operation(s) for content.
  name: GitHub Content API
  slug: github-content-api
- description: The Contexts API from GitHub — 1 operation(s) for contexts.
  name: GitHub Contexts API
  slug: github-contexts-api
- description: The Contributor API from GitHub — 1 operation(s) for contributor.
  name: GitHub Contributor API
  slug: github-contributor-api
- description: The Contributors API from GitHub — 1 operation(s) for contributors.
  name: GitHub Contributors API
  slug: github-contributors-api
- description: The Convert API from GitHub — 1 operation(s) for convert.
  name: GitHub Convert API
  slug: github-convert-api
- description: The Count API from GitHub — 2 operation(s) for count.
  name: GitHub Count API
  slug: github-count-api
- description: The Create API from GitHub — 84 operation(s) for create.
  name: GitHub Create API
  slug: github-create-api
- description: The Custom API from GitHub — 7 operation(s) for custom.
  name: GitHub Custom API
  slug: github-custom-api
- description: The Customizations API from GitHub — 2 operation(s) for customizations.
  name: GitHub Customizations API
  slug: github-customizations-api
- description: The Data API from GitHub — 1 operation(s) for data.
  name: GitHub Data API
  slug: github-data-api
- description: The Day API from GitHub — 1 operation(s) for day.
  name: GitHub Day API
  slug: github-day-api
- description: The Delete API from GitHub — 86 operation(s) for delete.
  name: GitHub Delete API
  slug: github-delete-api
- description: The Deliveries API from GitHub — 9 operation(s) for deliveries.
  name: GitHub Deliveries API
  slug: github-deliveries-api
- description: Endpoints to manage Dependabot.
  name: GitHub Dependabot API
  slug: github-dependabot-api
- description: The Dependencies API from GitHub — 2 operation(s) for dependencies.
  name: GitHub Dependencies API
  slug: github-dependencies-api
- description: Endpoints to access Dependency Graph features.
  name: GitHub Dependency-Graph API
  slug: github-dependency-graph-api
- description: The Deploy API from GitHub — 2 operation(s) for deploy.
  name: GitHub Deploy API
  slug: github-deploy-api
- description: The Deployments API from GitHub — 8 operation(s) for deployments.
  name: GitHub Deployments API
  slug: github-deployments-api
- description: The Directories API from GitHub — 1 operation(s) for directories.
  name: GitHub Directories API
  slug: github-directories-api
- description: The Disables API from GitHub — 6 operation(s) for disables.
  name: GitHub Disables API
  slug: github-disables-api
- description: The Discussions API from GitHub — 14 operation(s) for discussions.
  name: GitHub Discussions API
  slug: github-discussions-api
- description: The Dismiss API from GitHub — 1 operation(s) for dismiss.
  name: GitHub Dismiss API
  slug: github-dismiss-api
- description: The Dispatch API from GitHub — 2 operation(s) for dispatch.
  name: GitHub Dispatch API
  slug: github-dispatch-api
- description: The Docker API from GitHub — 3 operation(s) for docker.
  name: GitHub Docker API
  slug: github-docker-api
- description: The Documents API from GitHub — 2 operation(s) for documents.
  name: GitHub Documents API
  slug: github-documents-api
- description: The Download API from GitHub — 7 operation(s) for download.
  name: GitHub Download API
  slug: github-download-api
- description: The During API from GitHub — 3 operation(s) for during.
  name: GitHub During API
  slug: github-during-api
- description: The Emojis API from GitHub — 1 operation(s) for emojis.
  name: GitHub Emojis API
  slug: github-emojis-api
- description: The Enabled API from GitHub — 2 operation(s) for enabled.
  name: GitHub Enabled API
  slug: github-enabled-api
- description: The Enables API from GitHub — 6 operation(s) for enables.
  name: GitHub Enables API
  slug: github-enables-api
- description: The Enforcement API from GitHub — 2 operation(s) for enforcement.
  name: GitHub Enforcement API
  slug: github-enforcement-api
- description: Enterprise Administration
  name: GitHub Enterprise-Admin API
  slug: github-enterprise-admin-api
- description: The Enterprise-Admin - Scim API from GitHub — 1 operation(s) for enterprise-admin - scim.
  name: GitHub Enterprise-Admin - Scim API
  slug: github-enterprise-admin-scim-api
- description: The Enterprise API from GitHub — 8 operation(s) for enterprise.
  name: GitHub Enterprise API
  slug: github-enterprise-api
- description: The Environments API from GitHub — 7 operation(s) for environments.
  name: GitHub Environments API
  slug: github-environments-api
- description: The Event API from GitHub — 2 operation(s) for event.
  name: GitHub Event API
  slug: github-event-api
- description: The Existing API from GitHub — 3 operation(s) for existing.
  name: GitHub Existing API
  slug: github-existing-api
- description: The Export API from GitHub — 1 operation(s) for export.
  name: GitHub Export API
  slug: github-export-api
- description: The External API from GitHub — 3 operation(s) for external.
  name: GitHub External API
  slug: github-external-api
- description: The Failed API from GitHub — 1 operation(s) for failed.
  name: GitHub Failed API
  slug: github-failed-api
- description: The Feature API from GitHub — 1 operation(s) for feature.
  name: GitHub Feature API
  slug: github-feature-api
- description: The Files API from GitHub — 2 operation(s) for files.
  name: GitHub Files API
  slug: github-files-api
- description: The Fine-Grained API from GitHub — 1 operation(s) for fine-grained.
  name: GitHub Fine-Grained API
  slug: github-fine-grained-api
- description: The Fingerprint API from GitHub — 1 operation(s) for fingerprint.
  name: GitHub Fingerprint API
  slug: github-fingerprint-api
- description: The Forks API from GitHub — 3 operation(s) for forks.
  name: GitHub Forks API
  slug: github-forks-api
- description: The Generate API from GitHub — 1 operation(s) for generate.
  name: GitHub Generate API
  slug: github-generate-api
- description: The Get API from GitHub — 181 operation(s) for get.
  name: GitHub Get API
  slug: github-get-api
- description: Raw Git functionality.
  name: GitHub Git API
  slug: github-git-api
- description: The Gitignore API from GitHub — 2 operation(s) for gitignore.
  name: GitHub Gitignore API
  slug: github-gitignore-api
- description: The Grants API from GitHub — 2 operation(s) for grants.
  name: GitHub Grants API
  slug: github-grants-api
- description: The Groups API from GitHub — 11 operation(s) for groups.
  name: GitHub Groups API
  slug: github-groups-api
- description: The Head API from GitHub — 1 operation(s) for head.
  name: GitHub Head API
  slug: github-head-api
- description: The History API from GitHub — 1 operation(s) for history.
  name: GitHub History API
  slug: github-history-api
- description: The Hook API from GitHub — 2 operation(s) for hook.
  name: GitHub Hook API
  slug: github-hook-api
- description: The Hooks API from GitHub — 2 operation(s) for hooks.
  name: GitHub Hooks API
  slug: github-hooks-api
- description: The Hourly API from GitHub — 1 operation(s) for hourly.
  name: GitHub Hourly API
  slug: github-hourly-api
- description: The Identifiers API from GitHub — 1 operation(s) for identifiers.
  name: GitHub Identifiers API
  slug: github-identifiers-api
- description: The Identities API from GitHub — 1 operation(s) for identities.
  name: GitHub Identities API
  slug: github-identities-api
- description: The Impersonation API from GitHub — 1 operation(s) for impersonation.
  name: GitHub Impersonation API
  slug: github-impersonation-api
- description: The Information API from GitHub — 6 operation(s) for information.
  name: GitHub Information API
  slug: github-information-api
- description: The Installations API from GitHub — 13 operation(s) for installations.
  name: GitHub Installations API
  slug: github-installations-api
- description: The Instances API from GitHub — 1 operation(s) for instances.
  name: GitHub Instances API
  slug: github-instances-api
- description: The Invitation API from GitHub — 2 operation(s) for invitation.
  name: GitHub Invitation API
  slug: github-invitation-api
- description: The Invitations API from GitHub — 2 operation(s) for invitations.
  name: GitHub Invitations API
  slug: github-invitations-api
- description: The Jobs API from GitHub — 6 operation(s) for jobs.
  name: GitHub Jobs API
  slug: github-jobs-api
- description: The Keys API from GitHub — 18 operation(s) for keys.
  name: GitHub Keys API
  slug: github-keys-api
- description: The Label API from GitHub — 1 operation(s) for label.
  name: GitHub Label API
  slug: github-label-api
- description: The Labels API from GitHub — 9 operation(s) for labels.
  name: GitHub Labels API
  slug: github-labels-api
- description: The Languages API from GitHub — 1 operation(s) for languages.
  name: GitHub Languages API
  slug: github-languages-api
- description: The Large File Storage API from GitHub — 1 operation(s) for large file storage.
  name: GitHub Large File Storage API
  slug: github-large-file-storage-api
- description: The Last API from GitHub — 1 operation(s) for last.
  name: GitHub Last API
  slug: github-last-api
- description: The Latest API from GitHub — 2 operation(s) for latest.
  name: GitHub Latest API
  slug: github-latest-api
- description: The Ldap API from GitHub — 4 operation(s) for ldap.
  name: GitHub Ldap API
  slug: github-ldap-api
- description: The Legacy API from GitHub — 15 operation(s) for legacy.
  name: GitHub Legacy API
  slug: github-legacy-api
- description: The Levels API from GitHub — 1 operation(s) for levels.
  name: GitHub Levels API
  slug: github-levels-api
- description: The Limit API from GitHub — 1 operation(s) for limit.
  name: GitHub Limit API
  slug: github-limit-api
- description: The Lists API from GitHub — 204 operation(s) for lists.
  name: GitHub Lists API
  slug: github-lists-api
- description: The Locks API from GitHub — 1 operation(s) for locks.
  name: GitHub Locks API
  slug: github-locks-api
- description: The Log API from GitHub — 1 operation(s) for log.
  name: GitHub Log API
  slug: github-log-api
- description: The Logs API from GitHub — 3 operation(s) for logs.
  name: GitHub Logs API
  slug: github-logs-api
- description: The Maintenance API from GitHub — 1 operation(s) for maintenance.
  name: GitHub Maintenance API
  slug: github-maintenance-api
- description: The Manager API from GitHub — 2 operation(s) for manager.
  name: GitHub Manager API
  slug: github-manager-api
- description: The Manifest API from GitHub — 1 operation(s) for manifest.
  name: GitHub Manifest API
  slug: github-manifest-api
- description: The Mapping API from GitHub — 4 operation(s) for mapping.
  name: GitHub Mapping API
  slug: github-mapping-api
- description: The Mark API from GitHub — 2 operation(s) for mark.
  name: GitHub Mark API
  slug: github-mark-api
- description: The Matching API from GitHub — 1 operation(s) for matching.
  name: GitHub Matching API
  slug: github-matching-api
- description: The Materials API from GitHub — 1 operation(s) for materials.
  name: GitHub Materials API
  slug: github-materials-api
- description: The Member API from GitHub — 3 operation(s) for member.
  name: GitHub Member API
  slug: github-member-api
- description: The Members API from GitHub — 4 operation(s) for members.
  name: GitHub Members API
  slug: github-members-api
- description: The Membership API from GitHub — 3 operation(s) for membership.
  name: GitHub Membership API
  slug: github-membership-api
- description: The Memberships API from GitHub — 4 operation(s) for memberships.
  name: GitHub Memberships API
  slug: github-memberships-api
- description: The Merge API from GitHub — 2 operation(s) for merge.
  name: GitHub Merge API
  slug: github-merge-api
- description: The Merged API from GitHub — 1 operation(s) for merged.
  name: GitHub Merged API
  slug: github-merged-api
- description: Move projects to or from GitHub.
  name: GitHub Migrations API
  slug: github-migrations-api
- description: The Milestones API from GitHub — 3 operation(s) for milestones.
  name: GitHub Milestones API
  slug: github-milestones-api
- description: The Mode API from GitHub — 1 operation(s) for mode.
  name: GitHub Mode API
  slug: github-mode-api
- description: The Modes API from GitHub — 1 operation(s) for modes.
  name: GitHub Modes API
  slug: github-modes-api
- description: The Move API from GitHub — 2 operation(s) for move.
  name: GitHub Move API
  slug: github-move-api
- description: The Name API from GitHub — 2 operation(s) for name.
  name: GitHub Name API
  slug: github-name-api
- description: The Network API from GitHub — 1 operation(s) for network.
  name: GitHub Network API
  slug: github-network-api
- description: The Node API from GitHub — 1 operation(s) for node.
  name: GitHub Node API
  slug: github-node-api
- description: The Nodes API from GitHub — 3 operation(s) for nodes.
  name: GitHub Nodes API
  slug: github-nodes-api
- description: The Notes API from GitHub — 1 operation(s) for notes.
  name: GitHub Notes API
  slug: github-notes-api
- description: The Oauth API from GitHub — 1 operation(s) for oauth.
  name: GitHub Oauth API
  slug: github-oauth-api
- description: OAuth Authorizations API
  name: GitHub Oauth-Authorizations API
  slug: github-oauth-authorizations-api
- description: The Objects API from GitHub — 2 operation(s) for objects.
  name: GitHub Objects API
  slug: github-objects-api
- description: The Oidc API from GitHub — 1 operation(s) for oidc.
  name: GitHub Oidc API
  slug: github-oidc-api
- description: The Openid Connect API from GitHub — 2 operation(s) for openid connect.
  name: GitHub Openid Connect API
  slug: github-openid-connect-api
- description: The Organizations API from GitHub — 89 operation(s) for organizations.
  name: GitHub Organizations API
  slug: github-organizations-api
- description: The Orgs API from GitHub — 30 operation(s) for orgs.
  name: GitHub Orgs API
  slug: github-orgs-api
- description: The Outside API from GitHub — 3 operation(s) for outside.
  name: GitHub Outside API
  slug: github-outside-api
- description: The Owned API from GitHub — 3 operation(s) for owned.
  name: GitHub Owned API
  slug: github-owned-api
- description: The Package API from GitHub — 10 operation(s) for package.
  name: GitHub Package API
  slug: github-package-api
- description: Manage packages for authenticated users and organizations.
  name: GitHub Packages API
  slug: github-packages-api
- description: The Pages API from GitHub — 5 operation(s) for pages.
  name: GitHub Pages API
  slug: github-pages-api
- description: The Pending API from GitHub — 2 operation(s) for pending.
  name: GitHub Pending API
  slug: github-pending-api
- description: The Permission API from GitHub — 1 operation(s) for permission.
  name: GitHub Permission API
  slug: github-permission-api
- description: The Permissions API from GitHub — 10 operation(s) for permissions.
  name: GitHub Permissions API
  slug: github-permissions-api
- description: The Ping API from GitHub — 2 operation(s) for ping.
  name: GitHub Ping API
  slug: github-ping-api
- description: The Policies API from GitHub — 3 operation(s) for policies.
  name: GitHub Policies API
  slug: github-policies-api
- description: The Pre-Receive API from GitHub — 4 operation(s) for pre-receive.
  name: GitHub Pre-Receive API
  slug: github-pre-receive-api
- description: The Preferences API from GitHub — 1 operation(s) for preferences.
  name: GitHub Preferences API
  slug: github-preferences-api
- description: The Process API from GitHub — 1 operation(s) for process.
  name: GitHub Process API
  slug: github-process-api
- description: The Project API from GitHub — 3 operation(s) for project.
  name: GitHub Project API
  slug: github-project-api
- description: The Protected API from GitHub — 3 operation(s) for protected.
  name: GitHub Protected API
  slug: github-protected-api
- description: The Protections API from GitHub — 7 operation(s) for protections.
  name: GitHub Protections API
  slug: github-protections-api
- description: The Provision API from GitHub — 2 operation(s) for provision.
  name: GitHub Provision API
  slug: github-provision-api
- description: The Provisioned API from GitHub — 4 operation(s) for provisioned.
  name: GitHub Provisioned API
  slug: github-provisioned-api
- description: The Provisioning API from GitHub — 2 operation(s) for provisioning.
  name: GitHub Provisioning API
  slug: github-provisioning-api
- description: The Public API from GitHub — 17 operation(s) for public.
  name: GitHub Public API
  slug: github-public-api
- description: The Pull API from GitHub — 19 operation(s) for pull.
  name: GitHub Pull API
  slug: github-pull-api
- description: Interact with GitHub Pull Requests.
  name: GitHub Pulls API
  slug: github-pulls-api
- description: The Push API from GitHub — 1 operation(s) for push.
  name: GitHub Push API
  slug: github-push-api
- description: The Rate API from GitHub — 1 operation(s) for rate.
  name: GitHub Rate API
  slug: github-rate-api
- description: Check your current rate limit status
  name: GitHub Rate-Limit API
  slug: github-rate-limit-api
- description: The Raw API from GitHub — 1 operation(s) for raw.
  name: GitHub Raw API
  slug: github-raw-api
- description: The Re-Deliver API from GitHub — 3 operation(s) for re-deliver.
  name: GitHub Re-Deliver API
  slug: github-re-deliver-api
- description: The Re-Request API from GitHub — 2 operation(s) for re-request.
  name: GitHub Re-Request API
  slug: github-re-request-api
- description: The Re-Run API from GitHub — 3 operation(s) for re-run.
  name: GitHub Re-Run API
  slug: github-re-run-api
- description: The Reaction API from GitHub — 1 operation(s) for reaction.
  name: GitHub Reaction API
  slug: github-reaction-api
- description: The Reactions API from GitHub — 16 operation(s) for reactions.
  name: GitHub Reactions API
  slug: github-reactions-api
- description: The Read API from GitHub — 2 operation(s) for read.
  name: GitHub Read API
  slug: github-read-api
- description: The Readme API from GitHub — 2 operation(s) for readme.
  name: GitHub Readme API
  slug: github-readme-api
- description: The References API from GitHub — 10 operation(s) for references.
  name: GitHub References API
  slug: github-references-api
- description: The Registration API from GitHub — 2 operation(s) for registration.
  name: GitHub Registration API
  slug: github-registration-api
- description: The Releases API from GitHub — 10 operation(s) for releases.
  name: GitHub Releases API
  slug: github-releases-api
- description: The Remove API from GitHub — 40 operation(s) for remove.
  name: GitHub Remove API
  slug: github-remove-api
- description: The Rename API from GitHub — 1 operation(s) for rename.
  name: GitHub Rename API
  slug: github-rename-api
- description: The Render API from GitHub — 2 operation(s) for render.
  name: GitHub Render API
  slug: github-render-api
- description: The Replace API from GitHub — 1 operation(s) for replace.
  name: GitHub Replace API
  slug: github-replace-api
- description: The Replicas API from GitHub — 2 operation(s) for replicas.
  name: GitHub Replicas API
  slug: github-replicas-api
- description: The Replication API from GitHub — 1 operation(s) for replication.
  name: GitHub Replication API
  slug: github-replication-api
- description: The Reply API from GitHub — 1 operation(s) for reply.
  name: GitHub Reply API
  slug: github-reply-api
- description: The Repositories API from GitHub — 123 operation(s) for repositories.
  name: GitHub Repositories API
  slug: github-repositories-api
- description: The Requested API from GitHub — 1 operation(s) for requested.
  name: GitHub Requested API
  slug: github-requested-api
- description: The Requests API from GitHub — 21 operation(s) for requests.
  name: GitHub Requests API
  slug: github-requests-api
- description: The Rerequest API from GitHub — 2 operation(s) for rerequest.
  name: GitHub Rerequest API
  slug: github-rerequest-api
- description: The Reset API from GitHub — 1 operation(s) for reset.
  name: GitHub Reset API
  slug: github-reset-api
- description: The Restore API from GitHub — 6 operation(s) for restore.
  name: GitHub Restore API
  slug: github-restore-api
- description: The Restrictions API from GitHub — 4 operation(s) for restrictions.
  name: GitHub Restrictions API
  slug: github-restrictions-api
- description: The Reviewers API from GitHub — 1 operation(s) for reviewers.
  name: GitHub Reviewers API
  slug: github-reviewers-api
- description: The Reviews API from GitHub — 13 operation(s) for reviews.
  name: GitHub Reviews API
  slug: github-reviews-api
- description: The Revoke API from GitHub — 1 operation(s) for revoke.
  name: GitHub Revoke API
  slug: github-revoke-api
- description: The Role API from GitHub — 2 operation(s) for role.
  name: GitHub Role API
  slug: github-role-api
- description: The Roles API from GitHub — 2 operation(s) for roles.
  name: GitHub Roles API
  slug: github-roles-api
- description: The Runners API from GitHub — 16 operation(s) for runners.
  name: GitHub Runners API
  slug: github-runners-api
- description: The Running API from GitHub — 1 operation(s) for running.
  name: GitHub Running API
  slug: github-running-api
- description: The Runs API from GitHub — 22 operation(s) for runs.
  name: GitHub Runs API
  slug: github-runs-api
- description: The Scanning API from GitHub — 11 operation(s) for scanning.
  name: GitHub Scanning API
  slug: github-scanning-api
- description: The Scim API from GitHub — 4 operation(s) for scim.
  name: GitHub Scim API
  slug: github-scim-api
- description: The Scoped API from GitHub — 1 operation(s) for scoped.
  name: GitHub Scoped API
  slug: github-scoped-api
- description: Retrieve secret scanning alerts from a repository.
  name: GitHub Secret-Scanning API
  slug: github-secret-scanning-api
- description: The Secrets API from GitHub — 19 operation(s) for secrets.
  name: GitHub Secrets API
  slug: github-secrets-api
- description: The Security API from GitHub — 1 operation(s) for security.
  name: GitHub Security API
  slug: github-security-api
- description: The Selected API from GitHub — 8 operation(s) for selected.
  name: GitHub Selected API
  slug: github-selected-api
- description: The Self-Hosted API from GitHub — 14 operation(s) for self-hosted.
  name: GitHub Self-Hosted API
  slug: github-self-hosted-api
- description: The Servers API from GitHub — 4 operation(s) for servers.
  name: GitHub Servers API
  slug: github-servers-api
- description: The Sets API from GitHub — 32 operation(s) for sets.
  name: GitHub Sets API
  slug: github-sets-api
- description: The Settings API from GitHub — 2 operation(s) for settings.
  name: GitHub Settings API
  slug: github-settings-api
- description: The Setup API from GitHub — 2 operation(s) for setup.
  name: GitHub Setup API
  slug: github-setup-api
- description: The Signatures API from GitHub — 1 operation(s) for signatures.
  name: GitHub Signatures API
  slug: github-signatures-api
- description: The Single API from GitHub — 2 operation(s) for single.
  name: GitHub Single API
  slug: github-single-api
- description: The Sites API from GitHub — 2 operation(s) for sites.
  name: GitHub Sites API
  slug: github-sites-api
- description: The Software API from GitHub — 1 operation(s) for software.
  name: GitHub Software API
  slug: github-software-api
- description: The Specific API from GitHub — 3 operation(s) for specific.
  name: GitHub Specific API
  slug: github-specific-api
- description: The Ssh API from GitHub — 6 operation(s) for ssh.
  name: GitHub Ssh API
  slug: github-ssh-api
- description: The Star API from GitHub — 2 operation(s) for star.
  name: GitHub Star API
  slug: github-star-api
- description: The Stargazers API from GitHub — 1 operation(s) for stargazers.
  name: GitHub Stargazers API
  slug: github-stargazers-api
- description: The Starred API from GitHub — 5 operation(s) for starred.
  name: GitHub Starred API
  slug: github-starred-api
- description: The Start API from GitHub — 3 operation(s) for start.
  name: GitHub Start API
  slug: github-start-api
- description: The State API from GitHub — 2 operation(s) for state.
  name: GitHub State API
  slug: github-state-api
- description: The States API from GitHub — 1 operation(s) for states.
  name: GitHub States API
  slug: github-states-api
- description: The Static Analysis Results Interchange Format API from GitHub — 2 operation(s) for static analysis results interchange format.
  name: GitHub Static Analysis Results Interchange Format API
  slug: github-static-analysis-results-interchange-format-api
- description: The Status API from GitHub — 11 operation(s) for status.
  name: GitHub Status API
  slug: github-status-api
- description: The Statuses API from GitHub — 2 operation(s) for statuses.
  name: GitHub Statuses API
  slug: github-statuses-api
- description: The Subject API from GitHub — 2 operation(s) for subject.
  name: GitHub Subject API
  slug: github-subject-api
- description: The Submit API from GitHub — 1 operation(s) for submit.
  name: GitHub Submit API
  slug: github-submit-api
- description: The Subscriptions API from GitHub — 2 operation(s) for subscriptions.
  name: GitHub Subscriptions API
  slug: github-subscriptions-api
- description: The Suites API from GitHub — 6 operation(s) for suites.
  name: GitHub Suites API
  slug: github-suites-api
- description: The Suspend API from GitHub — 2 operation(s) for suspend.
  name: GitHub Suspend API
  slug: github-suspend-api
- description: The Sync API from GitHub — 3 operation(s) for sync.
  name: GitHub Sync API
  slug: github-sync-api
- description: The Tar API from GitHub — 1 operation(s) for tar.
  name: GitHub Tar API
  slug: github-tar-api
- description: Interact with GitHub Teams.
  name: GitHub Teams API
  slug: github-teams-api
- description: The Templates API from GitHub — 4 operation(s) for templates.
  name: GitHub Templates API
  slug: github-templates-api
- description: The Tests API from GitHub — 1 operation(s) for tests.
  name: GitHub Tests API
  slug: github-tests-api
- description: The Thread API from GitHub — 2 operation(s) for thread.
  name: GitHub Thread API
  slug: github-thread-api
- description: The Timelines API from GitHub — 1 operation(s) for timelines.
  name: GitHub Timelines API
  slug: github-timelines-api
- description: The Tokens API from GitHub — 11 operation(s) for tokens.
  name: GitHub Tokens API
  slug: github-tokens-api
- description: The Topics API from GitHub — 2 operation(s) for topics.
  name: GitHub Topics API
  slug: github-topics-api
- description: The Transfers API from GitHub — 1 operation(s) for transfers.
  name: GitHub Transfers API
  slug: github-transfers-api
- description: The Trees API from GitHub — 2 operation(s) for trees.
  name: GitHub Trees API
  slug: github-trees-api
- description: The Unlock API from GitHub — 2 operation(s) for unlock.
  name: GitHub Unlock API
  slug: github-unlock-api
- description: The Unstar API from GitHub — 2 operation(s) for unstar.
  name: GitHub Unstar API
  slug: github-unstar-api
- description: The Unsuspend API from GitHub — 2 operation(s) for unsuspend.
  name: GitHub Unsuspend API
  slug: github-unsuspend-api
- description: The Update API from GitHub — 71 operation(s) for update.
  name: GitHub Update API
  slug: github-update-api
- description: The Upgrade API from GitHub — 1 operation(s) for upgrade.
  name: GitHub Upgrade API
  slug: github-upgrade-api
- description: The Upload API from GitHub — 3 operation(s) for upload.
  name: GitHub Upload API
  slug: github-upload-api
- description: The Upstream API from GitHub — 1 operation(s) for upstream.
  name: GitHub Upstream API
  slug: github-upstream-api
- description: The Usage API from GitHub — 4 operation(s) for usage.
  name: GitHub Usage API
  slug: github-usage-api
- description: The Variables API from GitHub — 9 operation(s) for variables.
  name: GitHub Variables API
  slug: github-variables-api
- description: The Versions API from GitHub — 10 operation(s) for versions.
  name: GitHub Versions API
  slug: github-versions-api
- description: The Vulnerabilities API from GitHub — 1 operation(s) for vulnerabilities.
  name: GitHub Vulnerabilities API
  slug: github-vulnerabilities-api
- description: The Watchers API from GitHub — 1 operation(s) for watchers.
  name: GitHub Watchers API
  slug: github-watchers-api
- description: The Webhooks API from GitHub — 19 operation(s) for webhooks.
  name: GitHub Webhooks API
  slug: github-webhooks-api
- description: The Weekly API from GitHub — 2 operation(s) for weekly.
  name: GitHub Weekly API
  slug: github-weekly-api
- description: The Workflows API from GitHub — 24 operation(s) for workflows.
  name: GitHub Workflows API
  slug: github-workflows-api
- description: The Year API from GitHub — 1 operation(s) for year.
  name: GitHub Year API
  slug: github-year-api
- description: The Zen API from GitHub — 1 operation(s) for zen.
  name: GitHub Zen API
  slug: github-zen-api
- description: The GitHub Application API API from GitHub — 0 operation(s) for github application api.
  name: GitHub GitHub Application API API
  slug: github-github-application-api-api
- description: The GitHub Auth API API from GitHub — 0 operation(s) for github auth api.
  name: GitHub GitHub Auth API API
  slug: github-github-auth-api-api
- description: The GitHub Code Of Conduct API API from GitHub — 0 operation(s) for github code of conduct api.
  name: GitHub GitHub Code Of Conduct API API
  slug: github-github-code-of-conduct-api-api
- description: The GitHub Codes API from GitHub — 0 operation(s) for github codes.
  name: GitHub GitHub Codes API
  slug: github-github-codes-api
- description: The GitHub Emojis API API from GitHub — 0 operation(s) for github emojis api.
  name: GitHub GitHub Emojis API API
  slug: github-github-emojis-api-api
- description: The GitHub Feeds API API from GitHub — 0 operation(s) for github feeds api.
  name: GitHub GitHub Feeds API API
  slug: github-github-feeds-api-api
- description: The GitHub Gists API API from GitHub — 0 operation(s) for github gists api.
  name: GitHub GitHub Gists API API
  slug: github-github-gists-api-api
- description: The GitHub Gitignore Templates API API from GitHub — 0 operation(s) for github gitignore templates api.
  name: GitHub GitHub Gitignore Templates API API
  slug: github-github-gitignore-templates-api-api
- description: The GitHub Installation API API from GitHub — 0 operation(s) for github installation api.
  name: GitHub GitHub Installation API API
  slug: github-github-installation-api-api
- description: The GitHub Licenses API API from GitHub — 0 operation(s) for github licenses api.
  name: GitHub GitHub Licenses API API
  slug: github-github-licenses-api-api
- description: The GitHub Manage API API from GitHub — 0 operation(s) for github manage api.
  name: GitHub GitHub Manage API API
  slug: github-github-manage-api-api
- description: The GitHub Markdown API API from GitHub — 0 operation(s) for github markdown api.
  name: GitHub GitHub Markdown API API
  slug: github-github-markdown-api-api
- description: The GitHub Meta API API from GitHub — 0 operation(s) for github meta api.
  name: GitHub GitHub Meta API API
  slug: github-github-meta-api-api
- description: The GitHub Networks API API from GitHub — 0 operation(s) for github networks api.
  name: GitHub GitHub Networks API API
  slug: github-github-networks-api-api
- description: The GitHub Notifications API API from GitHub — 0 operation(s) for github notifications api.
  name: GitHub GitHub Notifications API API
  slug: github-github-notifications-api-api
- description: The GitHub Projects API API from GitHub — 0 operation(s) for github projects api.
  name: GitHub GitHub Projects API API
  slug: github-github-projects-api-api
- description: The GitHub SCIM API API from GitHub — 0 operation(s) for github scim api.
  name: GitHub GitHub SCIM API API
  slug: github-github-scim-api-api
- description: The GitHub V3 REST API API from GitHub — 0 operation(s) for github v3 rest api.
  name: GitHub GitHub V3 REST API API
  slug: github-github-v3-rest-api-api
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
artifact_total: 1252
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
  name: GitHub Application API
  slug: open-github-app-api
- collection_type: open
  name: GitHub Auth API
  slug: open-github-auth-api
- collection_type: open
  name: GitHub Code of Conduct API
  slug: open-github-code-of-conduct-api
- collection_type: open
  name: GitHub codes
  slug: open-github-codes
- collection_type: open
  name: GitHub Emojis API
  slug: open-github-emojis
- collection_type: open
  name: GitHub Events API
  slug: open-github-events-api
- collection_type: open
  name: GitHub Feeds API
  slug: open-github-feeds
- collection_type: open
  name: GitHub Gists API
  slug: open-github-gists
- collection_type: open
  name: GitHub Gitignore Templates API
  slug: open-github-gitignore-templates
- collection_type: open
  name: GitHub Installation API
  slug: open-github-installation
- collection_type: open
  name: GitHub Issues API
  slug: open-github-issues-api
- collection_type: open
  name: GitHub Licenses API
  slug: open-github-licenses
- collection_type: open
  name: GitHub Manage API
  slug: open-github-manage
- collection_type: open
  name: GitHub Markdown API
  slug: open-github-markdown
- collection_type: open
  name: GitHub Meta API
  slug: open-github-meta
- collection_type: open
  name: GitHub Networks API
  slug: open-github-networks
- collection_type: open
  name: GitHub Notifications API
  slug: open-github-notifications
- collection_type: open
  name: GitHub Octocat API
  slug: open-github-octocat
- collection_type: open
  name: GitHub Org API
  slug: open-github-organizations
- collection_type: open
  name: GitHub Projects API
  slug: open-github-projects
- collection_type: open
  name: GitHub Rate Limit API
  slug: open-github-rate-limit-
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
  name: github-repos-api
  slug: open-github-repos-api
- collection_type: open
  name: GitHub SCIM API
  slug: open-github-scim
- collection_type: open
  name: GitHub Search API
  slug: open-github-search-api
- collection_type: open
  name: GitHub Setup API
  slug: open-github-setup
- collection_type: open
  name: GitHub Teams API
  slug: open-github-teams
- collection_type: open
  name: GitHub User API
  slug: open-github-users-api
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/github-agentic-access.yml
- group: auth
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
  title: ''
  type: Arazzo
  url: arazzo/github-commit-file-to-new-branch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-create-label-and-triage-issue-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-create-milestone-and-issue-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-create-org-repository-and-issue-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-create-repository-and-issue-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-dispatch-workflow-and-poll-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-fork-and-branch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-fork-gist-and-comment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-inspect-latest-commit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-onboard-org-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-open-and-merge-pull-request-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-open-pull-request-and-request-reviewers-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-propose-change-pull-request-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-provision-org-repo-with-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-publish-release-with-asset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-report-bug-issue-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-review-and-merge-pull-request-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-star-and-comment-gist-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-tag-commit-and-release-workflow.yml
- group: design
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
  title: ''
  type: JSONSchema
  url: json-schema/github-repository-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/github-issue-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/github-pull-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/github-user-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/github-organization-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/github-commit-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/github-webhook-delivery-schema.json
- group: design
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
modified: '2026-05-19'
name: GitHub
nav: Providers
network: true
overview: 'GitHub publishes 333 APIs on the [APIs.io](https://apis.io/) network, including Events API, Feeds API, Gists API, and 330 more. Tagged areas include Code, Pipelines, Platform, Software Development, and Source Control.


  The GitHub catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  GitHub''s developer surface includes authentication, documentation, CLI, support, getting-started guide, engineering blog, signup flow, and 62 more developer resources.'
plans:
- name: Github Plans Pricing
  plan_count: 3
  slug: github-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 8
  name: Github Rate Limits
  slug: github-rate-limits
rules:
- name: GitHub API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: github-asyncapi-spectral-rules
- name: GitHub API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: github-jsonschema-spectral-rules
- name: GitHub API Rules
  rule_count: 20
  severity_counts:
    error: 14
    hint: 0
    info: 3
    warn: 3
  slug: github-spectral-rules
score:
  band: exemplar
  composite: 66.2
  delta: -5.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 79.9
    developer_ergonomics: 78.3
    discoverability: 66.7
    governance: 41.7
    operational_transparency: 68.4
  previous_composite: 71.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 322
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
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
- Pipelines
- Platform
- Software Development
- Source Control
- T1
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
