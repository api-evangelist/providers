---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 90
  human_in_the_loop: 0
  name: Sentry System Agentic Access
  operation_count: 200
  slug: sentry-system-agentic-access
  summary_line: 200 operations · 90 acting
api_count: 21
apis:
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage alerts (beta)
  name: Sentry Alerts API
  phrasing_intents:
  - id: fetchAlerts
    intent: List an organization's alerts
    question: Which alerts are set up across my Sentry organization?
  - id: createAlert
    intent: Create an organization alert
    question: How can I add a new alert to my organization?
  - id: mutateOrganizationAlerts
    intent: Bulk update alert status
    question: How do I change the status of several alerts at once?
  - id: bulkDeleteAlerts
    intent: Delete several alerts at once
    question: Can I remove multiple alerts in a single request?
  - id: fetchAlert
    intent: Get one alert's details
    question: What is configured on a specific alert?
  - id: updateAlert
    intent: Rename or update an alert
    question: How do I rename an existing alert?
  - id: deleteAlert
    intent: Delete a single alert
    question: How do I get rid of one alert I no longer need?
  phrasing_ops: 7
  slug: sentry-system-alerts-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: View monitor check-in history
  name: Sentry Check-Ins API
  phrasing_intents:
  - id: listMonitorCheckIns
    intent: List a cron monitor's check-ins
    question: How can I see every check-in a cron monitor has recorded?
  - id: listMonitorCheckInsForProject
    intent: List a monitor's check-ins within a project
    question: Can I pull a monitor's check-ins scoped to one project?
  phrasing_ops: 2
  slug: sentry-system-check-ins-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage project client keys (DSNs)
  name: Sentry Client Keys API
  phrasing_intents:
  - id: listProjectClientKeys
    intent: List a project's client keys (DSNs)
    question: Where do I find the DSN keys for my project?
  - id: createProjectClientKey
    intent: Create a new client key
    question: How do I generate an additional DSN for a project?
  - id: retrieveProjectClientKey
    intent: Get a single client key
    question: What are the details of one specific client key?
  - id: updateProjectClientKey
    intent: Rename or disable a client key
    question: Can I deactivate a DSN without deleting it?
  - id: deleteProjectClientKey
    intent: Delete a client key
    question: What happens to events sent with a DSN after I delete its key?
  phrasing_ops: 5
  slug: sentry-system-client-keys-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage commits associated with releases
  name: Sentry Commits API
  phrasing_intents:
  - id: listOrganizationReleaseCommits
    intent: List commits in a release
    question: Which commits went into a particular release?
  - id: listReleaseCommitFiles
    intent: List files changed in a release
    question: What files were changed by the commits in a release?
  phrasing_ops: 2
  slug: sentry-system-commits-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage custom integrations
  name: Sentry Custom Integrations API
  phrasing_intents:
  - id: listOrganizationCustomIntegrations
    intent: List an org's custom integrations
    question: Which custom integrations (Sentry Apps) has my organization built?
  - id: retrieveCustomIntegration
    intent: Get a custom integration's details
    question: What scopes and webhook URL does a given Sentry App use?
  - id: updateCustomIntegration
    intent: Update a custom integration
    question: Can I change the webhook URL of my Sentry App?
  - id: deleteCustomIntegration
    intent: Delete a custom integration
    question: How do I remove a Sentry App we no longer use?
  phrasing_ops: 4
  slug: sentry-system-custom-integrations-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage custom dashboards and their widgets
  name: Sentry Dashboards API
  phrasing_intents:
  - id: listOrganizationDashboards
    intent: List custom dashboards
    question: Which custom dashboards exist in my organization?
  - id: createOrganizationDashboard
    intent: Create a custom dashboard
    question: How do I create a new dashboard with widgets?
  - id: retrieveOrganizationDashboard
    intent: Get a dashboard and its widgets
    question: What widgets are on a particular dashboard?
  - id: editOrganizationDashboard
    intent: Edit a custom dashboard
    question: How do I retitle an existing dashboard?
  - id: deleteOrganizationDashboard
    intent: Delete a custom dashboard
    question: How do I delete a dashboard nobody uses?
  phrasing_ops: 5
  slug: sentry-system-dashboards-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage data forwarding configurations
  name: Sentry Data Forwarders API
  phrasing_intents:
  - id: listDataForwarders
    intent: List data forwarders
    question: Which data forwarders are configured for my organization?
  - id: createDataForwarder
    intent: Create a data forwarder
    question: How do I set up a new data forwarder?
  - id: updateDataForwarder
    intent: Update a data forwarder
    question: Can I rename an existing data forwarder?
  - id: deleteDataForwarder
    intent: Delete a data forwarder
    question: How do I stop forwarding data by removing a forwarder?
  phrasing_ops: 4
  slug: sentry-system-data-forwarders-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage debug information files
  name: Sentry Debug Files API
  phrasing_intents:
  - id: listProjectDebugFiles
    intent: List a project's debug information files
    question: Which dSYM and debug symbol files have been uploaded for my project?
  phrasing_ops: 1
  slug: sentry-system-debug-files-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage deployments of releases
  name: Sentry Deploys API
  phrasing_intents:
  - id: listReleaseDeploys
    intent: List a release's deploys
    question: Where has a given release been deployed?
  - id: createReleaseDeploy
    intent: Record a deploy of a release
    question: How do I tell Sentry a release was deployed to production?
  phrasing_ops: 2
  slug: sentry-system-deploys-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage saved Discover queries
  name: Sentry Discover API
  phrasing_intents:
  - id: listDiscoverSavedQueries
    intent: List saved Discover queries
    question: Which Discover queries has my team saved?
  - id: createDiscoverSavedQuery
    intent: Save a new Discover query
    question: How do I save a Discover query so I can reuse it?
  - id: retrieveDiscoverSavedQuery
    intent: Get a saved Discover query
    question: What columns and filters does a saved query use?
  - id: editDiscoverSavedQuery
    intent: Edit a saved Discover query
    question: How do I change the filter on a query I saved earlier?
  - id: deleteDiscoverSavedQuery
    intent: Delete a saved Discover query
    question: How do I remove a saved query from Discover?
  phrasing_ops: 5
  slug: sentry-system-discover-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage project and organization environments
  name: Sentry Environments API
  phrasing_intents:
  - id: listOrganizationEnvironments
    intent: List an organization's environments
    question: Which environments exist across my whole organization?
  - id: listProjectEnvironments
    intent: List a project's environments
    question: What environments does a single project report from?
  - id: retrieveProjectEnvironment
    intent: Get a project environment
    question: Is a particular environment hidden in my project?
  - id: updateProjectEnvironment
    intent: Hide or show a project environment
    question: Can I hide a noisy environment from a project's views?
  phrasing_ops: 4
  slug: sentry-system-environments-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Access and manage error and transaction events
  name: Sentry Events API
  phrasing_intents:
  - id: listIssueEvents
    intent: List events for an issue
    question: What individual events make up an issue?
  - id: listProjectEvents
    intent: List a project's error events
    question: Which error events came into a project recently?
  - id: retrieveProjectEvent
    intent: Get an event from a project
    question: How can I read the full payload of one event in a project?
  - id: retrieveIssueEvent
    intent: Get a specific event of an issue
    question: Can I pull one event by ID through its issue?
  - id: debugSourceMaps
    intent: Troubleshoot source maps for an event
    question: Why is my JavaScript stack trace still minified?
  phrasing_ops: 5
  slug: sentry-system-events-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Query and analyze event data
  name: Sentry Explore API
  phrasing_intents:
  - id: queryExploreEventsTable
    intent: Query events as a table
    question: How do I slice my events by fields and aggregates in a table?
  - id: queryExploreEventsTimeseries
    intent: Query events as a time series
    question: Can I chart an event metric over time?
  phrasing_ops: 2
  slug: sentry-system-explore-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage external issue links
  name: Sentry External Issues API
  phrasing_intents:
  - id: createExternalIssue
    intent: Link a Sentry issue to an external issue
    question: How can my integration link a Sentry issue to a ticket in our tracker?
  - id: deleteExternalIssue
    intent: Unlink an external issue
    question: Can I remove a tracker link from a Sentry issue?
  - id: listIssueExternalLinks
    intent: List external links on an issue
    question: Which tracker tickets are linked to a Sentry issue?
  phrasing_ops: 3
  slug: sentry-system-external-issues-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage external team mappings
  name: Sentry External Teams API
  phrasing_intents:
  - id: createExternalTeam
    intent: Map a team to an external service team
    question: How do I link a Sentry team to a team in our chat or code hosting tool?
  - id: updateExternalTeam
    intent: Update an external team mapping
    question: Can I change the external name a team is mapped to?
  - id: deleteExternalTeam
    intent: Remove an external team mapping
    question: How do I unlink a Sentry team from its external team?
  phrasing_ops: 3
  slug: sentry-system-external-teams-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage external user mappings
  name: Sentry External Users API
  phrasing_intents:
  - id: createExternalUser
    intent: Map a member to an external service user
    question: How do I link a Sentry member to their username in an external tool?
  - id: updateExternalUser
    intent: Update an external user mapping
    question: Can I correct the external username a member is mapped to?
  - id: deleteExternalUser
    intent: Remove an external user mapping
    question: How do I unlink a member from their external account?
  phrasing_ops: 3
  slug: sentry-system-external-users-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage inbound data filters
  name: Sentry Filters API
  phrasing_intents:
  - id: listProjectFilters
    intent: List a project's inbound data filters
    question: Which inbound filters are active on my project?
  - id: updateProjectFilter
    intent: Turn an inbound data filter on or off
    question: How do I enable a filter to drop unwanted events before ingestion?
  phrasing_ops: 2
  slug: sentry-system-filters-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage integration installations
  name: Sentry Installations API
  phrasing_intents:
  - id: listOrganizationInstallations
    intent: List Integration Platform installations
    question: Which Sentry Apps are installed in my organization?
  phrasing_ops: 1
  slug: sentry-system-installations-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage third-party integrations
  name: Sentry Integrations API
  phrasing_intents:
  - id: listOrganizationIntegrations
    intent: List an organization's integrations
    question: Which integrations are configured for my organization?
  - id: retrieveOrganizationIntegration
    intent: Get an installed integration
    question: What are the details of one installed integration?
  - id: deleteOrganizationIntegration
    intent: Uninstall an integration
    question: How do I remove an integration from my organization?
  - id: getIntegrationProviderInfo
    intent: List available integration providers
    question: Which integration providers can I install in Sentry?
  phrasing_ops: 4
  slug: sentry-system-integrations-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: View user interactions within replays
  name: Sentry Interactions API
  phrasing_intents:
  - id: listOrganizationSelectors
    intent: List DOM selectors seen in replays
    question: Which page elements do users click on most across replays?
  - id: listClickedNodes
    intent: List nodes clicked in a replay
    question: What did a user click on during a session replay?
  phrasing_ops: 2
  slug: sentry-system-interactions-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage issue alert rules at the project level
  name: Sentry Issue Alerts API
  phrasing_intents:
  - id: listIssueAlertRules
    intent: List a project's issue alert rules
    question: Which issue alert rules are set on my project?
  - id: createIssueAlertRule
    intent: Create an issue alert rule
    question: How do I get notified when a new issue is created in a project?
  - id: retrieveIssueAlertRule
    intent: Get an issue alert rule
    question: What conditions and actions does a specific issue alert use?
  - id: updateIssueAlertRule
    intent: Update an issue alert rule
    question: How can I change the actions on an existing issue alert?
  - id: deleteIssueAlertRule
    intent: Delete an issue alert rule
    question: How do I stop an issue alert from firing permanently?
  phrasing_ops: 5
  slug: sentry-system-issue-alerts-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage error issues
  name: Sentry Issues API
  phrasing_intents:
  - id: listOrganizationIssues
    intent: Search issues across an organization
    question: How do I find unresolved issues across all my projects?
  - id: bulkMutateOrganizationIssues
    intent: Bulk update issues across an org
    question: Can I resolve many issues across different projects at once?
  - id: bulkRemoveOrganizationIssues
    intent: Bulk delete issues across an org
    question: Can I permanently delete several issues from different projects at once?
  - id: retrieveIssue
    intent: Get an issue's details
    question: What is the status and assignee of a particular issue?
  - id: updateIssue
    intent: Resolve, assign or update one issue
    question: How do I mark a single issue as resolved?
  - id: removeIssue
    intent: Delete a single issue
    question: How do I delete one issue entirely?
  - id: listProjectIssues
    intent: List a project's issues
    question: Which issues are open in one project?
  - id: bulkMutateProjectIssues
    intent: Bulk update issues in a project
    question: Can I resolve a list of issues within a single project at once?
  phrasing_ops: 12
  slug: sentry-system-issues-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage organization members and their roles
  name: Sentry Members API
  phrasing_intents:
  - id: listOrganizationMembers
    intent: List organization members
    question: Who are the members of my Sentry organization?
  - id: addOrganizationMember
    intent: Invite a member by email
    question: How do I invite a new person to my organization?
  - id: retrieveOrganizationMember
    intent: Get an organization member
    question: What role does a specific member have?
  - id: updateOrganizationMemberRoles
    intent: Change a member's org role or teams
    question: How do I promote a member to admin?
  - id: deleteOrganizationMember
    intent: Remove a member from the organization
    question: How do I remove someone who left the company?
  - id: listTeamMembers
    intent: List a team's members
    question: Who belongs to a particular team?
  - id: addMemberToTeam
    intent: Add a member to a team
    question: How do I put an existing member on a team?
  - id: removeMemberFromTeam
    intent: Remove a member from a team
    question: How do I take someone off a team but keep them in the org?
  phrasing_ops: 10
  slug: sentry-system-members-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage metric alert rules at the organization level
  name: Sentry Metric Alerts API
  phrasing_intents:
  - id: listMetricAlertRules
    intent: List metric alert rules
    question: Which metric alerts watch error rates or latency in my org?
  - id: createMetricAlertRule
    intent: Create a metric alert rule
    question: How do I alert when p95 latency crosses a threshold?
  - id: retrieveMetricAlertRule
    intent: Get a metric alert rule
    question: What thresholds does a particular metric alert use?
  - id: updateMetricAlertRule
    intent: Update a metric alert rule
    question: How do I change the threshold on an existing metric alert?
  - id: deleteMetricAlertRule
    intent: Delete a metric alert rule
    question: How do I remove a metric alert that's too noisy?
  phrasing_ops: 5
  slug: sentry-system-metric-alerts-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Analyze mobile application build artifacts
  name: Sentry Mobile Builds API
  phrasing_intents:
  - id: retrieveArtifactInstallInfo
    intent: Get install links for a mobile build
    question: How can testers install a mobile build I uploaded?
  - id: retrieveArtifactSizeAnalysis
    intent: Get size analysis for a mobile build
    question: What is making my app binary so large?
  phrasing_ops: 2
  slug: sentry-system-mobile-builds-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage cron job monitors
  name: Sentry Monitors API
  phrasing_intents:
  - id: listOrganizationMonitors
    intent: List an organization's monitors
    question: Which cron monitors does my organization have?
  - id: createMonitor
    intent: Create a cron monitor
    question: How do I start monitoring a scheduled job?
  - id: mutateOrganizationMonitors
    intent: Bulk update monitor status
    question: Can I disable several monitors at once?
  - id: bulkDeleteMonitors
    intent: Delete several monitors at once
    question: Can I remove many monitors in one request?
  - id: retrieveMonitor
    intent: Get a cron monitor across the org
    question: What schedule and status does a monitor have?
  - id: updateMonitor
    intent: Update a cron monitor at org level
    question: How do I change the schedule of a cron monitor by its slug?
  - id: deleteMonitor
    intent: Delete a cron monitor or its environments
    question: Can I delete just one environment from a cron monitor?
  - id: retrieveMonitorForProject
    intent: Get a monitor within a project
    question: How can I view a monitor through the project it belongs to?
  phrasing_ops: 14
  slug: sentry-system-monitors-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage Sentry organizations
  name: Sentry Organizations API
  phrasing_intents:
  - id: listOrganizations
    intent: List organizations I can access
    question: Which Sentry organizations does my token have access to?
  - id: retrieveOrganization
    intent: Get an organization's details
    question: What settings does my organization have?
  - id: updateOrganization
    intent: Rename or update an organization
    question: How do I rename my organization?
  - id: listOrganizationProjects
    intent: List an organization's projects
    question: Which projects exist under my org?
  - id: resolveShortId
    intent: Resolve an issue short ID
    question: How do I turn a short ID like PROJ-123 into an issue?
  - id: resolveEventId
    intent: Find the issue for an event ID
    question: Which project and issue does an event ID belong to?
  - id: retrieveEventCounts
    intent: Get event counts for an organization
    question: How many events did my org send in the last 30 days?
  - id: listOrganizationTrustedRelays
    intent: List trusted Relays
    question: Which trusted Relays are registered for my org?
  phrasing_ops: 9
  slug: sentry-system-organizations-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage projects within organizations
  name: Sentry Projects API
  phrasing_intents:
  - id: listOrganizationProjects
    intent: List an organization's projects
    question: Which projects exist in my Sentry organization?
  - id: retrieveProject
    intent: Get a project's details
    question: What platform and settings does a project have?
  - id: updateProject
    intent: Update a project's settings
    question: How do I rename a project or change its platform?
  - id: deleteProject
    intent: Delete a project
    question: Is deleting a project reversible?
  - id: createProject
    intent: Create a project for a team
    question: How do I create a new project owned by a team?
  - id: listProjectUsers
    intent: List users seen in a project
    question: Which end users have been seen in my app's project?
  - id: addTeamToProject
    intent: Give a team access to a project
    question: How do I grant another team access to a project?
  - id: removeTeamFromProject
    intent: Revoke a team's project access
    question: How do I take a team's access away from a project?
  phrasing_ops: 8
  slug: sentry-system-projects-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Access replay recording segments
  name: Sentry Recording Segments API
  phrasing_intents:
  - id: listRecordingSegments
    intent: List a replay's recording segments
    question: How do I download the raw recording data of a replay?
  - id: retrieveRecordingSegment
    intent: Get one recording segment
    question: Can I fetch a single segment of a replay recording?
  phrasing_ops: 2
  slug: sentry-system-recording-segments-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage files associated with releases
  name: Sentry Release Files API
  phrasing_intents:
  - id: listOrganizationReleaseFiles
    intent: List a release's uploaded files
    question: Which source maps and artifacts were uploaded for a release?
  - id: uploadOrganizationReleaseFile
    intent: Upload a file to a release
    question: How do I upload a source map to a release?
  - id: retrieveOrganizationReleaseFile
    intent: Get a release file
    question: Can I check one file attached to a release?
  - id: updateOrganizationReleaseFile
    intent: Rename a release file
    question: How do I fix the name of a source map I uploaded to a release?
  - id: deleteOrganizationReleaseFile
    intent: Delete a release file
    question: How do I remove a wrong source map from a release?
  phrasing_ops: 5
  slug: sentry-system-release-files-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage software releases
  name: Sentry Releases API
  phrasing_intents:
  - id: listOrganizationReleases
    intent: List an organization's releases
    question: Which releases have been created in my org?
  - id: createOrganizationRelease
    intent: Create a release
    question: How do I tell Sentry about a new version I'm shipping?
  - id: retrieveOrganizationRelease
    intent: Get a release
    question: What are the details of a specific version?
  - id: updateOrganizationRelease
    intent: Update a release
    question: How do I mark a release as released with a date?
  - id: deleteOrganizationRelease
    intent: Delete a release
    question: How do I delete a release I created by mistake?
  - id: listReleaseThresholdStatuses
    intent: Check release threshold statuses
    question: Are my releases passing their health thresholds?
  phrasing_ops: 6
  slug: sentry-system-releases-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage session replays
  name: Sentry Replays API
  phrasing_intents:
  - id: listOrganizationReplays
    intent: List session replays
    question: How do I find session replays from the last day?
  - id: retrieveReplay
    intent: Get a session replay
    question: What happened during a specific session replay?
  - id: deleteReplay
    intent: Delete a session replay
    question: How do I delete a replay that captured sensitive data?
  - id: listReplayViewers
    intent: List who viewed a replay
    question: Who on my team has already watched this replay?
  - id: getReplayCount
    intent: Count replays for issues or transactions
    question: How many replays are attached to an issue?
  phrasing_ops: 5
  slug: sentry-system-replays-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage organization repositories
  name: Sentry Repositories API
  phrasing_intents:
  - id: listOrganizationRepositories
    intent: List connected code repositories
    question: Which code repositories are connected to my org for commit tracking?
  - id: listRepositoryCommits
    intent: List a repository's commits
    question: What commits has Sentry recorded for one repository?
  - id: listRepositories
    intent: List Prevent repositories for an owner
    question: Which repositories does Prevent track for my organization?
  - id: retrieveRepository
    intent: Get a Prevent repository
    question: What does Prevent know about one of my repositories?
  - id: listRepositoryBranches
    intent: List a repository's branches
    question: Which branches exist on a Prevent repository?
  - id: syncRepositories
    intent: Sync repositories from the integrated org
    question: How do I pull newly created repositories into Prevent?
  - id: getSyncStatus
    intent: Check repository sync status
    question: Is the repository sync still running?
  phrasing_ops: 7
  slug: sentry-system-repositories-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Provision and manage organization members via SCIM
  name: Sentry SCIM Members API
  phrasing_intents:
  - id: listScimMembers
    intent: List members via SCIM
    question: How does my identity provider list Sentry members over SCIM?
  - id: provisionScimMember
    intent: Provision a member via SCIM
    question: How do I auto-provision a new user into Sentry from our IdP?
  - id: queryScimMember
    intent: Get a member via SCIM
    question: Can I look up one SCIM user's record?
  - id: updateScimMember
    intent: Deactivate a member via SCIM patch
    question: Can I deactivate a user through SCIM without deleting them?
  - id: deleteScimMember
    intent: Deprovision a member via SCIM
    question: How does offboarding in our IdP remove someone from Sentry?
  phrasing_ops: 5
  slug: sentry-system-scim-members-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Provision and manage teams via SCIM
  name: Sentry SCIM Teams API
  phrasing_intents:
  - id: listScimTeams
    intent: List teams via SCIM
    question: How does my IdP see Sentry teams as SCIM groups?
  - id: provisionScimTeam
    intent: Provision a team via SCIM
    question: How do I create a Sentry team from an IdP group?
  - id: queryScimTeam
    intent: Get a team via SCIM
    question: Can I read one team's SCIM group record?
  - id: updateScimTeam
    intent: Update a team or its members via SCIM
    question: How do I sync group membership changes into a Sentry team?
  - id: deleteScimTeam
    intent: Delete a team via SCIM
    question: What happens in Sentry when an IdP group is deleted?
  phrasing_ops: 5
  slug: sentry-system-scim-teams-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: AI-powered issue analysis and fix suggestions
  name: Sentry Seer API
  phrasing_intents:
  - id: listSeerModels
    intent: List Seer AI models
    question: Which AI models can Seer use to analyze issues?
  - id: startSeerIssueFix
    intent: Start a Seer AI fix for an issue
    question: Can Seer suggest a code fix for an issue automatically?
  - id: retrieveSeerIssueFixState
    intent: Check a Seer autofix's progress
    question: Has Seer finished its fix analysis for my issue?
  phrasing_ops: 3
  slug: sentry-system-seer-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage project service hooks
  name: Sentry Service Hooks API
  phrasing_intents:
  - id: listProjectServiceHooks
    intent: List a project's service hooks
    question: Which webhooks are registered as service hooks on my project?
  - id: createProjectServiceHook
    intent: Register a service hook
    question: How do I send project events to my own webhook URL?
  - id: retrieveProjectServiceHook
    intent: Get a service hook
    question: What URL and events does a service hook have?
  - id: updateProjectServiceHook
    intent: Update a service hook
    question: How do I change where a service hook sends events?
  - id: deleteProjectServiceHook
    intent: Remove a service hook
    question: How do I stop a service hook from sending events?
  phrasing_ops: 5
  slug: sentry-system-service-hooks-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Retrieve release health session statistics
  name: Sentry Sessions API
  phrasing_intents:
  - id: retrieveReleaseHealthSessions
    intent: Get release health session stats
    question: What is my crash-free session rate?
  phrasing_ops: 1
  slug: sentry-system-sessions-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage spike protection notification actions
  name: Sentry Spike Protection API
  phrasing_intents:
  - id: listSpikeProtectionNotifications
    intent: List spike protection notifications
    question: Who gets notified when spike protection kicks in?
  - id: createSpikeProtectionNotification
    intent: Add a spike protection notification
    question: How do I get alerted when a project hits a spike?
  phrasing_ops: 2
  slug: sentry-system-spike-protection-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage teams within organizations
  name: Sentry Teams API
  phrasing_intents:
  - id: listOrganizationTeams
    intent: List an organization's teams
    question: Which teams exist in my organization?
  - id: createTeam
    intent: Create a team
    question: How do I create a new team?
  - id: retrieveTeam
    intent: Get a team's details
    question: What are the details of a particular team?
  - id: updateTeam
    intent: Rename a team
    question: How do I rename a team?
  - id: deleteTeam
    intent: Delete a team
    question: What happens to a team's projects when I delete the team?
  - id: listTeamProjects
    intent: List a team's projects
    question: Which projects does a team own?
  - id: listProjectTeams
    intent: List teams with access to a project
    question: Which teams have access to a given project?
  phrasing_ops: 7
  slug: sentry-system-teams-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Retrieve test result metrics and test suites
  name: Sentry Test Results API
  phrasing_intents:
  - id: listTestResults
    intent: List test results
    question: Which tests failed recently in my repository?
  - id: retrieveTestResultMetrics
    intent: Get aggregated test metrics
    question: How flaky is my test suite overall?
  - id: listTestSuites
    intent: List test suites for a repository
    question: Which test suites appear in my repository's results?
  phrasing_ops: 3
  slug: sentry-system-test-results-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage repository upload tokens
  name: Sentry Tokens API
  phrasing_intents:
  - id: listRepositoryTokens
    intent: List repository upload tokens
    question: Where do I find the upload token for each repository?
  - id: regenerateToken
    intent: Regenerate a repository upload token
    question: How do I rotate a leaked repository upload token?
  phrasing_ops: 2
  slug: sentry-system-tokens-api
- baseURL: https://sentry.io/api/0
  baseurl_source: declared
  description: Manage user feedback submissions
  name: Sentry User Feedback API
  phrasing_intents:
  - id: listProjectUserFeedback
    intent: List a project's user feedback
    question: What feedback have users submitted for my app?
  - id: submitProjectUserFeedback
    intent: Submit user feedback for an event
    question: How do I attach a user's comments to an error event?
  phrasing_ops: 2
  slug: sentry-system-user-feedback-api
- description: 'Sentry provides official SDKs for 22+ platforms including JavaScript, Python, PHP, .NET, Java, Go, Ruby, Rust, Android, Apple, React Native, Unity, and Unreal Engine. Each SDK provides error capture, '
  name: Sentry SDK API
  slug: sentry-sdk-api
- description: 'The Sentry Integration Platform API enables building public and internal integrations with Sentry. Supports OAuth2 with PKCE, device authorization flow for CLI/CI environments, webhook notifications, '
  name: Sentry Integration Platform API
  slug: sentry-integration-platform-api
arazzos:
- description: Find a recent project event, attach user feedback to it, and confirm the feedback was recorded.
  name: Sentry Capture User Feedback for an Event
  slug: sentry-system-capture-user-feedback-workflow
- description: Create a cron-job monitor for an organization, confirm it, and list its check-ins.
  name: Sentry Create a Cron Monitor and Verify Check-ins
  slug: sentry-system-create-cron-monitor-workflow
- description: Create a metric alert rule for an organization, retrieve it, and confirm it appears in the rule list.
  name: Sentry Create a Metric Alert Rule
  slug: sentry-system-create-metric-alert-workflow
- description: Create a team, confirm it, add an existing organization member, and verify the team roster.
  name: Sentry Create a Team and Add a Member
  slug: sentry-system-create-team-add-member-workflow
- description: Create an organization release, confirm it, record a deploy to an environment, and list its deploys.
  name: Sentry Cut a Release and Record a Deploy
  slug: sentry-system-cut-release-deploy-workflow
- description: Confirm a project, grant a team access to it, and verify the team appears on the project.
  name: Sentry Grant a Team Access to a Project
  slug: sentry-system-grant-team-project-access-workflow
- description: Find an issue, inspect a tag's distribution and values, then bookmark and assign it for follow-up.
  name: Sentry Investigate an Issue's Tags
  slug: sentry-system-investigate-issue-tags-workflow
- description: Invite a new member to an organization, confirm the invite, add them to a team, and verify the roster.
  name: Sentry Invite a Member and Onboard to a Team
  slug: sentry-system-invite-member-onboard-team-workflow
- description: Create a new project under a team, confirm it, and mint a client key (DSN) for the SDK.
  name: Sentry Provision a Project and Client Key
  slug: sentry-system-provision-project-key-workflow
- description: List available Seer models, start an AI autofix for an issue, then poll until the fix completes.
  name: Sentry Run a Seer AI Autofix on an Issue
  slug: sentry-system-seer-autofix-issue-workflow
- description: Trigger a Prevent repository sync from GitHub, poll until it finishes, then list the synced repositories.
  name: Sentry Sync Prevent Repositories
  slug: sentry-system-sync-prevent-repos-workflow
- description: Find a high-priority unresolved issue in an organization, inspect it, then assign and resolve it.
  name: Sentry Triage and Resolve an Issue
  slug: sentry-system-triage-resolve-issue-workflow
artifact_total: 218
asyncapis:
- description: ''
  name: Sentry System Webhooks
  slug: sentry-system-webhooks
collections:
- collection_type: postman
  name: Sentry Alerts API
  slug: postman-sentry-alerts
- collection_type: postman
  name: Sentry API
  slug: postman-sentry-api
- collection_type: postman
  name: Sentry Crons API
  slug: postman-sentry-crons
- collection_type: postman
  name: Sentry Dashboards API
  slug: postman-sentry-dashboards
- collection_type: postman
  name: Sentry Discover API
  slug: postman-sentry-discover
- collection_type: postman
  name: Sentry Environments API
  slug: postman-sentry-environments
- collection_type: postman
  name: Sentry Events and Issues API
  slug: postman-sentry-events-issues
- collection_type: postman
  name: Sentry Explore API
  slug: postman-sentry-explore
- collection_type: postman
  name: Sentry Integration Platform API
  slug: postman-sentry-integration-platform
- collection_type: postman
  name: Sentry Integrations API
  slug: postman-sentry-integrations
- collection_type: postman
  name: Sentry Mobile Builds API
  slug: postman-sentry-mobile-builds
- collection_type: postman
  name: Sentry Monitors API
  slug: postman-sentry-monitors
- collection_type: postman
  name: Sentry Organizations API
  slug: postman-sentry-organizations
- collection_type: postman
  name: Sentry Prevent API
  slug: postman-sentry-prevent
- collection_type: postman
  name: Sentry Projects API
  slug: postman-sentry-projects
- collection_type: postman
  name: Sentry Releases API
  slug: postman-sentry-releases
- collection_type: postman
  name: Sentry Replays API
  slug: postman-sentry-replays
- collection_type: postman
  name: Sentry SCIM API
  slug: postman-sentry-scim
- collection_type: postman
  name: Sentry Seer API
  slug: postman-sentry-seer
- collection_type: postman
  name: Sentry Teams API
  slug: postman-sentry-teams
- collection_type: postman
  name: Sentry Users API
  slug: postman-sentry-users
- collection_type: open
  name: Sentry Alerts API
  slug: open-sentry-alerts
- collection_type: open
  name: Sentry API
  slug: open-sentry-api
- collection_type: open
  name: Sentry Crons API
  slug: open-sentry-crons
- collection_type: open
  name: Sentry Dashboards API
  slug: open-sentry-dashboards
- collection_type: open
  name: Sentry Discover API
  slug: open-sentry-discover
- collection_type: open
  name: Sentry Environments API
  slug: open-sentry-environments
- collection_type: open
  name: Sentry Events and Issues API
  slug: open-sentry-events-issues
- collection_type: open
  name: Sentry Explore API
  slug: open-sentry-explore
- collection_type: open
  name: Sentry Integration Platform API
  slug: open-sentry-integration-platform
- collection_type: open
  name: Sentry Integrations API
  slug: open-sentry-integrations
- collection_type: open
  name: Sentry Mobile Builds API
  slug: open-sentry-mobile-builds
- collection_type: open
  name: Sentry Monitors API
  slug: open-sentry-monitors
- collection_type: open
  name: Sentry Organizations API
  slug: open-sentry-organizations
- collection_type: open
  name: Sentry Prevent API
  slug: open-sentry-prevent
- collection_type: open
  name: Sentry Projects API
  slug: open-sentry-projects
- collection_type: open
  name: Sentry Releases API
  slug: open-sentry-releases
- collection_type: open
  name: Sentry Replays API
  slug: open-sentry-replays
- collection_type: open
  name: Sentry SCIM API
  slug: open-sentry-scim
- collection_type: open
  name: Sentry Seer API
  slug: open-sentry-seer
- collection_type: open
  name: Sentry Alerts API
  slug: open-sentry-system-alerts-api
- collection_type: open
  name: Sentry Alerts Check-Ins API
  slug: open-sentry-system-check-ins-api
- collection_type: open
  name: Sentry Alerts Client Keys API
  slug: open-sentry-system-client-keys-api
- collection_type: open
  name: Sentry Alerts Commits API
  slug: open-sentry-system-commits-api
- collection_type: open
  name: Sentry Alerts Custom Integrations API
  slug: open-sentry-system-custom-integrations-api
- collection_type: open
  name: Sentry Alerts Dashboards API
  slug: open-sentry-system-dashboards-api
- collection_type: open
  name: Sentry Alerts Data Forwarders API
  slug: open-sentry-system-data-forwarders-api
- collection_type: open
  name: Sentry Alerts Debug Files API
  slug: open-sentry-system-debug-files-api
- collection_type: open
  name: Sentry Alerts Deploys API
  slug: open-sentry-system-deploys-api
- collection_type: open
  name: Sentry Alerts Discover API
  slug: open-sentry-system-discover-api
- collection_type: open
  name: Sentry Alerts Environments API
  slug: open-sentry-system-environments-api
- collection_type: open
  name: Sentry Alerts Events API
  slug: open-sentry-system-events-api
- collection_type: open
  name: Sentry Alerts Explore API
  slug: open-sentry-system-explore-api
- collection_type: open
  name: Sentry Alerts External Issues API
  slug: open-sentry-system-external-issues-api
- collection_type: open
  name: Sentry Alerts External Teams API
  slug: open-sentry-system-external-teams-api
- collection_type: open
  name: Sentry Alerts External Users API
  slug: open-sentry-system-external-users-api
- collection_type: open
  name: Sentry Alerts Filters API
  slug: open-sentry-system-filters-api
- collection_type: open
  name: Sentry Alerts Installations API
  slug: open-sentry-system-installations-api
- collection_type: open
  name: Sentry Alerts Integrations API
  slug: open-sentry-system-integrations-api
- collection_type: open
  name: Sentry Alerts Interactions API
  slug: open-sentry-system-interactions-api
- collection_type: open
  name: Sentry Alerts Issue Alerts API
  slug: open-sentry-system-issue-alerts-api
- collection_type: open
  name: Sentry Alerts Issues API
  slug: open-sentry-system-issues-api
- collection_type: open
  name: Sentry Alerts Members API
  slug: open-sentry-system-members-api
- collection_type: open
  name: Sentry Alerts Metric Alerts API
  slug: open-sentry-system-metric-alerts-api
- collection_type: open
  name: Sentry Alerts Mobile Builds API
  slug: open-sentry-system-mobile-builds-api
- collection_type: open
  name: Sentry Alerts Monitors API
  slug: open-sentry-system-monitors-api
- collection_type: open
  name: Sentry Alerts Organizations API
  slug: open-sentry-system-organizations-api
- collection_type: open
  name: Sentry Alerts Projects API
  slug: open-sentry-system-projects-api
- collection_type: open
  name: Sentry Alerts Recording Segments API
  slug: open-sentry-system-recording-segments-api
- collection_type: open
  name: Sentry Alerts Release Files API
  slug: open-sentry-system-release-files-api
- collection_type: open
  name: Sentry Alerts Releases API
  slug: open-sentry-system-releases-api
- collection_type: open
  name: Sentry Alerts Replays API
  slug: open-sentry-system-replays-api
- collection_type: open
  name: Sentry Alerts Repositories API
  slug: open-sentry-system-repositories-api
- collection_type: open
  name: Sentry Alerts SCIM Members API
  slug: open-sentry-system-scim-members-api
- collection_type: open
  name: Sentry Alerts SCIM Teams API
  slug: open-sentry-system-scim-teams-api
- collection_type: open
  name: Sentry Alerts Seer API
  slug: open-sentry-system-seer-api
- collection_type: open
  name: Sentry Alerts Service Hooks API
  slug: open-sentry-system-service-hooks-api
- collection_type: open
  name: Sentry Alerts Sessions API
  slug: open-sentry-system-sessions-api
- collection_type: open
  name: Sentry Alerts Spike Protection API
  slug: open-sentry-system-spike-protection-api
- collection_type: open
  name: Sentry Alerts Teams API
  slug: open-sentry-system-teams-api
- collection_type: open
  name: Sentry Alerts Test Results API
  slug: open-sentry-system-test-results-api
- collection_type: open
  name: Sentry Alerts Tokens API
  slug: open-sentry-system-tokens-api
- collection_type: open
  name: Sentry Alerts User Feedback API
  slug: open-sentry-system-user-feedback-api
- collection_type: open
  name: Sentry Alerts Users API
  slug: open-sentry-system-users-api
- collection_type: open
  name: Sentry Teams API
  slug: open-sentry-teams
- collection_type: open
  name: Sentry Users API
  slug: open-sentry-users
common:
- group: commercial
  href: https://artifacts.apis.io/sentry-system/finops/sentry-system-finops.yml
  title: ''
  type: FinOps
  url: finops/sentry-system-finops.yml
- group: operate
  href: https://artifacts.apis.io/sentry-system/rate-limits/sentry-system-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sentry-system-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sentry-system/plans/sentry-system-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sentry-system-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/sentry-system/capabilities/sentry-system-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sentry-system-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/sentry-system/overlays/sentry-system-alerts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sentry-system-alerts-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/sentry-system/agentic-access/sentry-system-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sentry-system-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/sentry-system/security/sentry-system-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sentry-system-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sentry-system/security/sentry-system-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sentry-system-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/sentry-system/security/sentry-system-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sentry-system-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sentry-system/authentication/sentry-system-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sentry-system-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sentry-system/scopes/sentry-system-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sentry-system-scopes.yml
- group: agent
  href: https://artifacts.apis.io/sentry-system/well-known/sentry-system-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sentry-system-well-known.yml
- group: auth
  href: https://artifacts.apis.io/sentry-system/well-known/sentry-system-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sentry-system-security.txt
- group: build
  href: https://artifacts.apis.io/sentry-system/packages/sentry-system-packages.yml
  title: ''
  type: Packages
  url: packages/sentry-system-packages.yml
- group: agent
  href: https://artifacts.apis.io/sentry-system/mcp/sentry-system-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sentry-system-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sentry-system/llms/sentry-system-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sentry-system-llms.txt
- group: build
  href: https://artifacts.apis.io/sentry-system/cli/sentry-system-cli.yml
  title: ''
  type: CLI
  url: cli/sentry-system-cli.yml
- group: operate
  href: https://artifacts.apis.io/sentry-system/changelog/sentry-system-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sentry-system-changelog.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/errors/sentry-system-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sentry-system-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/lifecycle/sentry-system-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sentry-system-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/conformance/sentry-system-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sentry-system-conformance.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/conventions/sentry-system-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sentry-system-conventions.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/data-model/sentry-system-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sentry-system-data-model.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/components/sentry-system-components.yml
  title: ''
  type: Components
  url: components/sentry-system-components.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/asyncapi/sentry-system-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sentry-system-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/sentry-system/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/sentry-system/mcp/sentry-system-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/sentry-system-tool-crosswalk.yml
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.sentry.io/
- group: start
  href: https://artifacts.apis.io/sentry-system/sandbox/sentry-system-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/sentry-system-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://sentry.io/security/
- group: other
  title: ''
  type: APICatalog
  url: https://sentry.io/.well-known/api-catalog
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@sentry/node
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/sentry-sdk/
- group: build
  title: ''
  type: SDKs
  url: https://central.sonatype.com/artifact/io.sentry/sentry
- group: build
  title: ''
  type: SDKs
  url: https://pkg.go.dev/github.com/getsentry/sentry-go
- group: build
  title: ''
  type: SDKs
  url: https://packagist.org/packages/sentry/sentry
- group: build
  title: ''
  type: SDKs
  url: https://www.nuget.org/packages/Sentry
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sentry/overview
- group: design
  href: https://artifacts.apis.io/sentry-system/arazzo/sentry-system-capture-user-feedback-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-capture-user-feedback-workflow.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/arazzo/sentry-system-create-cron-monitor-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-create-cron-monitor-workflow.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/arazzo/sentry-system-create-metric-alert-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-create-metric-alert-workflow.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/arazzo/sentry-system-create-team-add-member-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-create-team-add-member-workflow.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/arazzo/sentry-system-cut-release-deploy-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-cut-release-deploy-workflow.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/arazzo/sentry-system-grant-team-project-access-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-grant-team-project-access-workflow.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/arazzo/sentry-system-investigate-issue-tags-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-investigate-issue-tags-workflow.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/arazzo/sentry-system-invite-member-onboard-team-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-invite-member-onboard-team-workflow.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/arazzo/sentry-system-provision-project-key-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-provision-project-key-workflow.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/arazzo/sentry-system-seer-autofix-issue-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-seer-autofix-issue-workflow.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/arazzo/sentry-system-sync-prevent-repos-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-sync-prevent-repos-workflow.yml
- group: design
  href: https://artifacts.apis.io/sentry-system/arazzo/sentry-system-triage-resolve-issue-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-triage-resolve-issue-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://sentry.io/
- group: company
  title: ''
  type: Website
  url: https://sentry.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sentry.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sentry.io/product/sentry-basics/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.sentry.io/api/auth/
- group: commercial
  title: ''
  type: Pricing
  url: https://sentry.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://blog.sentry.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getsentry
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/sentry
- group: start
  title: ''
  type: Signup
  url: https://sentry.io/signup/
- group: start
  title: ''
  type: Login
  url: https://sentry.io/auth/login/
- group: operate
  title: ''
  type: Support
  url: https://sentry.zendesk.com/hc/en-us/
- group: operate
  title: ''
  type: ChangeLog
  url: https://sentry.io/changelog/
- group: auth
  title: ''
  type: Security
  url: https://sentry.io/security/
- group: operate
  title: ''
  type: Community
  url: https://sentry.io/community/
- group: other
  title: ''
  type: Self-Hosted
  url: https://docs.sentry.io/server/
- group: docs
  title: ''
  type: Documentation
  url: https://develop.sentry.dev/
- group: build
  title: ''
  type: CLI
  url: https://docs.sentry.io/cli/
- group: build
  title: ''
  type: SDKs
  url: https://docs.sentry.io/platforms/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sentry.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sentry.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sentry.io/privacy/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.sentry.io/llms.txt
- group: start
  title: ''
  type: Portal
  url: https://docs.sentry.io/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sentry.io/api/
created: '2024-01-15'
description: Sentry is an open-source error tracking and performance monitoring platform that helps developers identify, triage, and resolve issues in their applications in real-time. Its Web API at https://sentry.io/api/0 covers issues and events, releases and deploys, alerting, dashboards and Discover queries, session replays, cron and uptime monitors, mobile build size analysis, SCIM 2.0 provisioning, and the Seer AI agent that root-causes an issue and can open a pull request. Sentry also runs a first-party remote MCP server at https://mcp.sentry.dev/mcp and ships official SDKs for 20+ platforms.
finops:
- has_sources: true
  method: derived
  name: Sentry System Finops
  primary_unit: subscription
  service_category: ''
  slug: sentry-system-finops
  template: false
image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
json_schemas:
- name: Sentry Alert Rule
  property_count: 12
  slug: sentry-alert-rule
- name: Sentry Event
  property_count: 14
  slug: sentry-event
- name: Sentry Issue
  property_count: 19
  slug: sentry-issue
- name: Sentry Monitor
  property_count: 9
  slug: sentry-monitor
- name: Sentry Organization
  property_count: 9
  slug: sentry-organization
- name: Sentry Project
  property_count: 14
  slug: sentry-project
- name: Sentry Release
  property_count: 14
  slug: sentry-release
- name: Sentry Replay
  property_count: 17
  slug: sentry-replay
- name: CheckIn
  property_count: 5
  slug: sentry-system-checkin
- name: ClientKey
  property_count: 9
  slug: sentry-system-clientkey
- name: Commit
  property_count: 5
  slug: sentry-system-commit
- name: Dashboard
  property_count: 5
  slug: sentry-system-dashboard
- name: DashboardSummary
  property_count: 5
  slug: sentry-system-dashboardsummary
- name: DataForwarder
  property_count: 3
  slug: sentry-system-dataforwarder
- name: DebugFile
  property_count: 8
  slug: sentry-system-debugfile
- name: Deploy
  property_count: 6
  slug: sentry-system-deploy
- name: Environment
  property_count: 4
  slug: sentry-system-environment
- name: Event
  property_count: 11
  slug: sentry-system-event
- name: ExternalIssue
  property_count: 5
  slug: sentry-system-externalissue
- name: Installation
  property_count: 5
  slug: sentry-system-installation
- name: Integration
  property_count: 8
  slug: sentry-system-integration
- name: Issue
  property_count: 15
  slug: sentry-system-issue
- name: IssueAlertRule
  property_count: 11
  slug: sentry-system-issuealertrule
- name: MetricAlertRule
  property_count: 12
  slug: sentry-system-metricalertrule
- name: Monitor
  property_count: 9
  slug: sentry-system-monitor
- name: MonitorAlert
  property_count: 4
  slug: sentry-system-monitoralert
- name: Organization
  property_count: 7
  slug: sentry-system-organization
- name: OrganizationDetail
  property_count: 9
  slug: sentry-system-organizationdetail
- name: OrganizationMember
  property_count: 10
  slug: sentry-system-organizationmember
- name: PreventRepository
  property_count: 5
  slug: sentry-system-preventrepository
- name: Project
  property_count: 12
  slug: sentry-system-project
- name: ProjectDetail
  property_count: 14
  slug: sentry-system-projectdetail
- name: RecordingSegment
  property_count: 4
  slug: sentry-system-recordingsegment
- name: Release
  property_count: 9
  slug: sentry-system-release
- name: ReleaseFile
  property_count: 7
  slug: sentry-system-releasefile
- name: Replay
  property_count: 17
  slug: sentry-system-replay
- name: Repository
  property_count: 7
  slug: sentry-system-repository
- name: SavedQuery
  property_count: 12
  slug: sentry-system-savedquery
- name: ScimGroup
  property_count: 5
  slug: sentry-system-scimgroup
- name: ScimListResponse
  property_count: 5
  slug: sentry-system-scimlistresponse
- name: ScimUser
  property_count: 7
  slug: sentry-system-scimuser
- name: SeerAutofixState
  property_count: 5
  slug: sentry-system-seerautofixstate
- name: SeerModel
  property_count: 4
  slug: sentry-system-seermodel
- name: SentryApp
  property_count: 11
  slug: sentry-system-sentryapp
- name: ServiceHook
  property_count: 6
  slug: sentry-system-servicehook
- name: SpikeProtectionAction
  property_count: 3
  slug: sentry-system-spikeprotectionaction
- name: Team
  property_count: 7
  slug: sentry-system-team
- name: TeamDetail
  property_count: 9
  slug: sentry-system-teamdetail
- name: TeamMember
  property_count: 8
  slug: sentry-system-teammember
- name: TestResult
  property_count: 6
  slug: sentry-system-testresult
- name: UptimeMonitor
  property_count: 7
  slug: sentry-system-uptimemonitor
- name: UserFeedback
  property_count: 6
  slug: sentry-system-userfeedback
- name: Widget
  property_count: 6
  slug: sentry-system-widget
- name: Sentry Team
  property_count: 9
  slug: sentry-team
json_structures:
- name: Sentry System Structure
  property_count: 0
  slug: sentry-system-structure
jsonld:
- class_count: 0
  name: Sentry Context
  property_count: 15
  slug: sentry-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.sentry.dev over HTTP; 12 tools listed.
  name: Sentry MCP Server
  slug: sentry
modified: '2026-09-18'
name: Sentry
nav: Providers
network: true
overview: 'Sentry publishes 45 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, Check-Ins API, Client Keys API, and 42 more. Tagged areas include APM, Application Monitoring, Bug Tracking, Developer Tools, and Error Tracking.


  The Sentry catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Sentry''s developer surface includes authentication, CLI, changelog, sandbox, developer portal, documentation, getting-started guide, and 68 more developer resources.'
plans:
- name: Sentry System Plans Pricing
  plan_count: 4
  slug: sentry-system-plans-pricing
- name: Sentry System Price Estimates
  plan_count: 0
  slug: sentry-system-price-estimates
random_paper: 7
rate_limits:
- limit_count: 0
  name: Sentry System Rate Limits
  slug: sentry-system-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Sentry — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sentry-system-jsonschema-spectral-rules
scopes:
- name: Sentry System Scopes
  scope_count: 26
  slug: sentry-system-scopes
  summary_line: 26 scopes · authorizationCode
score:
  band: exemplar
  composite: 80.6
  coverage:
    artifact_dirs: 40
    catalog_earned: 75.3
    catalog_earned_first_party: 12.0
    catalog_gap: 39.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 28.0
    contract_quality: 70.2
    developer_ergonomics: 92.3
    discoverability: 96.7
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 80.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 43
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/sentry-system/sentry-system-2026-06-20T193714.png
security:
- kind: authentication
  name: Sentry System Authentication
  slug: sentry-system-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Sentry System Domain Security
  slug: sentry-system-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sentry System Vulnerability Disclosure
  slug: sentry-system-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Sentry System Trust Center
  slug: sentry-system-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, ISO 27001, HIPAA
skill_count: 6
skills:
- name: sentry-create-cron-monitor
  slug: sentry-system-create-cron-monitor
- name: sentry-cut-release-and-record-deploy
  slug: sentry-system-cut-release-and-record-deploy
- name: sentry-invite-member-and-onboard
  slug: sentry-system-invite-member-and-onboard
- name: sentry-provision-project-and-key
  slug: sentry-system-provision-project-and-key
- name: sentry-run-seer-autofix
  slug: sentry-system-run-seer-autofix
- name: sentry-triage-and-resolve-issue
  slug: sentry-system-triage-and-resolve-issue
slug: sentry-system
tags:
- APM
- Application Monitoring
- Bug Tracking
- Developer Tools
- Error Tracking
- Observability
- Performance Monitoring
- Real-Time Monitoring
- Monitoring
website: https://sentry.io/
---
