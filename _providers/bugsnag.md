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
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 93
  human_in_the_loop: 2
  name: Bugsnag Agentic Access
  operation_count: 193
  slug: bugsnag-agentic-access
  summary_line: 193 operations · 93 acting · 2 human-in-the-loop
api_count: 5
apis:
- baseURL: https://build.bugsnag.com
  baseurl_source: declared
  description: Notify Bugsnag about application builds and deployments. Build notifications are used to track releases, identify regressions, and associate source control information with error data.
  name: bugsnag Builds API
  phrasing_intents:
  - id: createBuild
    intent: Report a new build or release
    question: How do I tell BugSnag which release introduced an error?
  phrasing_ops: 1
  slug: bugsnag-builds-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Manage collaborators within an organization or project. Collaborators are users who have access to view and manage Bugsnag data.
  name: bugsnag Collaborators API
  phrasing_intents:
  - id: listOrganizationCollaborators
    intent: List an organization's collaborators
    question: Who has access to my BugSnag organization?
  - id: inviteOrganizationCollaborator
    intent: Invite a collaborator by email
    question: How do I invite a teammate to my organization by email?
  - id: getOrganizationCollaborator
    intent: Get a collaborator's role and access
    question: What role and project access does a specific collaborator have?
  - id: updateOrganizationCollaborator
    intent: Change a collaborator's permissions
    question: Can I promote an existing collaborator to admin?
  - id: removeOrganizationCollaborator
    intent: Remove a collaborator from an organization
    question: How do I revoke someone's access to every project in my organization?
  phrasing_ops: 5
  slug: bugsnag-collaborators-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Manage comments on errors. Comments allow team members to discuss and annotate specific errors.
  name: bugsnag Comments API
  phrasing_intents:
  - id: listErrorComments
    intent: List comments on an error
    question: What has my team said about this error?
  - id: createErrorComment
    intent: Comment on an error
    question: How do I leave a note on an error for my teammates?
  - id: getComment
    intent: Get a single error comment
    question: How do I fetch one specific comment on an error?
  - id: updateComment
    intent: Edit a comment on a project's error
    question: How do I fix a typo in a comment I left on an error?
  - id: deleteComment
    intent: Delete a comment on a project's error
    question: Can I permanently remove a comment I posted on an error?
  phrasing_ops: 5
  slug: bugsnag-comments-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access and manage errors within projects. Errors represent groups of similar events that have been detected by Bugsnag.
  name: bugsnag Errors API
  phrasing_intents:
  - id: listProjectErrors
    intent: List a project's errors
    question: What errors are currently open in my project?
  - id: bulkUpdateErrors
    intent: Update many errors at once
    question: How do I resolve or ignore a batch of errors in one go?
  - id: deleteAllErrorsInProject
    intent: Wipe all errors and events in a project
    question: Can I clear out every error and event in a project at once?
  - id: getError
    intent: Get one error's details
    question: How many users has a specific error affected?
  - id: updateError
    intent: Resolve, snooze or reassign one error
    question: How do I mark a single error as resolved?
  - id: deleteError
    intent: Delete a single error
    question: Can I permanently delete one error along with its events?
  - id: deleteEventById
    intent: Delete one event
    question: Can I delete a single event that captured sensitive data?
  - id: viewLatestEventOnError
    intent: View an error's latest event
    question: What does the most recent occurrence of an error look like when I only have the error ID?
  phrasing_ops: 16
  slug: bugsnag-errors-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access event field definitions for projects. Event fields describe the available data dimensions for filtering and searching events.
  name: bugsnag EventFields API
  phrasing_intents:
  - id: listEventFields
    intent: List a project's event fields
    question: Which fields can I filter or pivot errors on in my project?
  phrasing_ops: 1
  slug: bugsnag-eventfields-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access individual error events. Events represent individual occurrences of an error within a project.
  name: bugsnag Events API
  phrasing_intents:
  - id: listErrorEvents
    intent: List occurrences of an error
    question: How can I see every individual occurrence of an error?
  - id: getLatestEvent
    intent: Get the most recent occurrence of an error
    question: What did the most recent occurrence of this error look like?
  - id: getEvent
    intent: Get a specific event by ID
    question: How do I pull the full details of one event I have the ID for?
  phrasing_ops: 3
  slug: bugsnag-events-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access and manage organizations. An organization is the top-level entity in Bugsnag that contains projects and collaborators.
  name: bugsnag Organizations API
  phrasing_intents:
  - id: listOrganizations
    intent: List my organizations
    question: Which BugSnag organizations do I belong to?
  - id: getOrganization
    intent: Get an organization's billing email and slug
    question: What billing email and slug are set on my organization?
  - id: createOrganization
    intent: Create an organization
    question: How do I start a brand-new BugSnag organization?
  - id: getOrganizationById
    intent: View an organization record by ID
    question: How do I pull up an organization's complete record by its ID?
  - id: updateOrganizationById
    intent: Update organization name and billing
    question: How do I change my organization's billing emails or invoice address?
  - id: deleteOrganization
    intent: Delete an organization
    question: Can I shut down and delete an entire BugSnag organization?
  - id: revokeOrganizationApiKey
    intent: Regenerate an organization's API key
    question: How do I rotate my organization's API key if it leaked?
  - id: revokeOrganizationAuthToken
    intent: Regenerate the deprecated organization auth token
    question: Can I still regenerate the old organization-level data access auth token?
  phrasing_ops: 41
  slug: bugsnag-organizations-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access pivot data for errors. Pivots allow you to group and analyze error data by various dimensions such as browser, device, or location.
  name: bugsnag Pivots API
  phrasing_intents:
  - id: listProjectPivots
    intent: List a project's pivot dimensions
    question: Which dimensions like browser or OS can I group my project's errors by?
  - id: listPivotValues
    intent: List values seen for a pivot
    question: Which browser names or OS versions have shown up in my errors?
  phrasing_ops: 2
  slug: bugsnag-pivots-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access and manage projects within an organization. Projects represent individual applications being monitored by Bugsnag.
  name: bugsnag Projects API
  phrasing_intents:
  - id: listOrganizationProjects
    intent: List an organization's projects
    question: What projects are in my BugSnag organization?
  - id: createProject
    intent: Create a project
    question: How do I create a new project and get its API key?
  - id: getProject
    intent: Get a project's settings
    question: What is the notifier API key for my project?
  - id: updateProject
    intent: Update a project's settings
    question: How do I rename a project?
  - id: deleteProject
    intent: Delete a project
    question: Can I delete a project and everything in it?
  - id: regenerateProjectApiKey
    intent: Regenerate a project's notifier API key
    question: How do I rotate my project's API key after it was exposed?
  - id: regenerateProjectUploadApiKey
    intent: Regenerate a project's upload API key
    question: How do I rotate the key used for uploading source maps and ProGuard files?
  - id: createProjectEventField
    intent: Create a custom event field
    question: How do I make a custom metadata value filterable in my project?
  phrasing_ops: 47
  slug: bugsnag-projects-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access release information for projects. Releases represent deployed versions of your application and their associated error data.
  name: bugsnag Releases API
  phrasing_intents:
  - id: listProjectReleases
    intent: List a project's releases
    question: Which versions of my app have been deployed in this project?
  - id: getRelease
    intent: Get one release's details
    question: What source control and builder info was recorded for a particular release?
  phrasing_ops: 2
  slug: bugsnag-releases-api
- baseURL: https://sessions.bugsnag.com
  baseurl_source: declared
  description: Report session data to Bugsnag for stability score calculations. Sessions represent periods of user activity and are used to compute crash-free session and user percentages.
  name: bugsnag Sessions API
  phrasing_intents:
  - id: sendSessions
    intent: Send session tracking data
    question: How do I report sessions so BugSnag can calculate crash-free percentages?
  phrasing_ops: 1
  slug: bugsnag-sessions-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access stability metrics for projects. Stability data provides crash-free session and user percentages across releases.
  name: bugsnag Stability API
  phrasing_intents:
  - id: getProjectStabilityTrend
    intent: Get a project's stability trend
    question: How has my app's crash-free session rate changed across releases?
  phrasing_ops: 1
  slug: bugsnag-stability-api
- baseURL: https://otlp.bugsnag.com
  baseurl_source: declared
  description: Send OpenTelemetry trace data to Bugsnag for performance monitoring. Spans represent individual operations and are assembled into traces that visualize request flow and latency.
  name: bugsnag Traces API
  phrasing_intents:
  - id: sendTraces
    intent: Send OpenTelemetry trace spans
    question: Can I send OpenTelemetry spans to BugSnag over OTLP HTTP?
  - id: postTracesV1
    intent: Send a sampled trace report to a project
    question: How do I post a trace report to BugSnag's /traces/v1 endpoint with my project API key?
  phrasing_ops: 2
  slug: bugsnag-traces-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access trend data for errors and projects. Trends provide time-series data showing how error rates and stability change over time.
  name: bugsnag Trends API
  phrasing_intents:
  - id: getErrorTrend
    intent: Get one error's frequency trend
    question: Is a particular error happening more or less often over time?
  - id: getProjectTrend
    intent: Get a project's overall error trend
    question: How is the overall error rate for my whole project trending?
  phrasing_ops: 2
  slug: bugsnag-trends-api
- baseURL: https://api.bugsnag.com
  baseurl_source: declared
  description: Access information about the currently authenticated user.
  name: Bugsnag Current User API
  phrasing_intents:
  - id: listProjectSavedSearches
    intent: List a project's saved searches
    question: What saved error searches exist on my project?
  - id: createSavedSearch
    intent: Save an error search
    question: How do I save a set of error filters so I can reuse it?
  - id: getSavedSearchById
    intent: Get a saved search
    question: What filters and sort order does a particular saved search use?
  - id: updateSavedSearchById
    intent: Update a saved search
    question: Can I rename a saved search or change its filters?
  - id: deleteSavedSearchById
    intent: Delete a saved search
    question: Can I get rid of a saved search nobody uses anymore?
  - id: getSavedSearchUsageSummary
    intent: Get usage summary of a saved search
    question: Is a saved search being used anywhere before I delete it?
  - id: getCurrentUser
    intent: Get the signed-in user's profile
    question: Who am I authenticated as with this BugSnag token?
  phrasing_ops: 7
  slug: bugsnag-current-user-api
- baseURL: https://build.bugsnag.com
  baseurl_source: declared
  description: ProGuard/DexGuard/R8 mappings for obfuscated Java/Kotlin and NDK symbol files for shared object (.so) files
  name: Bugsnag Android API
  phrasing_intents:
  - id: uploadNdkSymbol
    intent: Upload Android NDK shared object symbols
    question: How do I get readable native stack traces for my Android NDK crashes?
  - id: uploadProguard
    intent: Upload an Android ProGuard mapping file
    question: How do I deobfuscate Java stack traces from a minified Android build?
  phrasing_ops: 2
  slug: bugsnag-android-api
- baseURL: https://build.bugsnag.com
  baseurl_source: declared
  description: Debug symbol (.dSYM) files for release builds
  name: Bugsnag Apple API
  phrasing_intents:
  - id: uploadDsym
    intent: Upload Apple dSYM debug symbols
    question: How do I symbolicate iOS crash reports so I see function names and line numbers?
  phrasing_ops: 1
  slug: bugsnag-apple-api
- baseURL: https://build.bugsnag.com
  baseurl_source: declared
  description: Symbol files for split debug Dart builds
  name: Bugsnag Dart API
  phrasing_intents:
  - id: uploadDartSymbol
    intent: Upload Flutter Dart symbol files
    question: How do I see readable Dart stack traces when I build Flutter with --strip-debug-info?
  phrasing_ops: 1
  slug: bugsnag-dart-api
- baseURL: https://build.bugsnag.com
  baseurl_source: declared
  description: The Integrations API from Bugsnag — 8 operation(s) for integrations.
  name: Bugsnag Integrations API
  phrasing_intents:
  - id: getIntegrations
    intent: List supported integration types
    question: Which integrations does BugSnag support?
  - id: integrationsTest
    intent: Test integration settings before saving
    question: Can I try out integration credentials before I actually configure them?
  - id: configuredIntegrations
    intent: Get a configured integration
    question: What are the full settings of an integration already set up on a project?
  - id: configuredIntegrationsUpdate
    intent: Update a configured integration
    question: Can I change the settings of an integration I already set up?
  - id: configuredIntegrationsDelete
    intent: Delete a configured integration
    question: How do I disconnect an integration from a project?
  - id: updateConfiguredIntegrationsTriggerConfig
    intent: Set an integration's automatic trigger
    question: Can I make an integration act automatically when a certain condition is met?
  - id: configuredIntegrationTest
    intent: Send a test through a saved integration
    question: How do I check that an integration I already configured is working?
  - id: projectConfiguredIntegrations
    intent: Add an integration to a project
    question: How do I connect an issue tracker to my project?
  phrasing_ops: 10
  slug: bugsnag-integrations-api
- baseURL: https://build.bugsnag.com
  baseurl_source: declared
  description: Source maps for minified JavaScript
  name: Bugsnag JavaScript API
  phrasing_intents:
  - id: uploadReactNativeSourcemap
    intent: Upload a React Native source map
    question: How do I get readable React Native JavaScript stack traces on BugSnag?
  - id: uploadSourcemap
    intent: Upload a browser JavaScript source map
    question: How do I de-minify browser JavaScript errors on my BugSnag dashboard?
  phrasing_ops: 2
  slug: bugsnag-javascript-api
- baseURL: https://build.bugsnag.com
  baseurl_source: declared
  description: Symbol files for shared object (.so) files
  name: Bugsnag Linux API
  phrasing_intents:
  - id: uploadLinux
    intent: Upload Linux shared object symbols
    question: How do I get human-readable stack traces for a Linux native app?
  phrasing_ops: 1
  slug: bugsnag-linux-api
- baseURL: https://build.bugsnag.com
  baseurl_source: declared
  description: Upload minidump files and optional associated event data. The minidump file must be included in the request as the `upload_file_minidump` request part. Include the `event` part to associate additional
  name: Bugsnag Minidump API
  phrasing_intents:
  - id: uploadMinidumps
    intent: Upload a crash minidump
    question: How do I send a Breakpad or Crashpad minidump to BugSnag as a crash report?
  phrasing_ops: 1
  slug: bugsnag-minidump-api
- baseURL: https://build.bugsnag.com
  baseurl_source: declared
  description: Breakpad symbol files for Minidumps
  name: Bugsnag Minidumps API
  phrasing_intents:
  - id: uploadBreakpadSymbol
    intent: Upload Breakpad symbol files
    question: How do I symbolicate minidumps from Electron or Crashpad crashes?
  phrasing_ops: 1
  slug: bugsnag-minidumps-api
- baseURL: https://build.bugsnag.com
  baseurl_source: declared
  description: Symbol files for Nintendo Switch
  name: Bugsnag Nintendo API
  phrasing_intents:
  - id: uploadNintendoSwitchSymbol
    intent: Upload Nintendo Switch symbol files
    question: How do I see file names and line numbers in crashes from my Nintendo Switch game?
  phrasing_ops: 1
  slug: bugsnag-nintendo-api
- baseURL: https://build.bugsnag.com
  baseurl_source: declared
  description: The SCIM API from Bugsnag — 4 operation(s) for scim.
  name: Bugsnag SCIM API
  phrasing_intents:
  - id: listScimCollaborators
    intent: List SCIM-provisioned users
    question: How does my identity provider list the users provisioned in BugSnag via SCIM?
  - id: createScimCollaborator
    intent: Provision a user via SCIM
    question: How do I provision a new user into BugSnag from my identity provider?
  - id: getScimCollaborator
    intent: Get a SCIM-provisioned user
    question: How do I fetch one SCIM user record by its ID?
  - id: updateScimCollaborator
    intent: Replace a SCIM user's details
    question: How do I update a provisioned user's name and email through SCIM?
  - id: patchScimCollaborator
    intent: Deactivate or re-add a SCIM user
    question: Can I toggle the active flag to remove and later re-add a provisioned user?
  - id: deleteScimCollaborator
    intent: Deprovision a SCIM user
    question: How does my identity provider remove a user from BugSnag via SCIM?
  - id: listScimGroups
    intent: List SCIM groups
    question: Which SCIM groups are synced into my BugSnag organization?
  - id: createScimGroup
    intent: Create a SCIM group
    question: How do I push a new group from my identity provider into BugSnag?
  phrasing_ops: 11
  slug: bugsnag-scim-api
- baseURL: https://build.bugsnag.com
  baseurl_source: declared
  description: IL2CPP mapping files for Unity
  name: Bugsnag Unity API
  phrasing_intents:
  - id: uploadUnityLineMappings
    intent: Upload Unity IL2CPP line mappings
    question: How do I get C# line numbers in native crashes from a Unity IL2CPP build?
  phrasing_ops: 1
  slug: bugsnag-unity-api
artifact_total: 127
asyncapis:
- description: 'Bugsnag webhooks deliver real-time notifications about error events to a configured callback URL via HTTP POST. The webhook integration sends JSON payloads containing information about the triggering '
  name: Bugsnag Webhook Events
  slug: bugsnag-webhooks-asyncapi
collections:
- collection_type: open
  name: Bugsnag Build API
  slug: open-bugsnag-build
- collection_type: open
  name: Bugsnag Build Builds API
  slug: open-bugsnag-builds-api
- collection_type: open
  name: Bugsnag Build Builds Collaborators API
  slug: open-bugsnag-collaborators-api
- collection_type: open
  name: Bugsnag Build Builds Comments API
  slug: open-bugsnag-comments-api
- collection_type: open
  name: Bugsnag Build Builds CurrentUser API
  slug: open-bugsnag-currentuser-api
- collection_type: open
  name: Bugsnag Data Access API
  slug: open-bugsnag-data-access
- collection_type: open
  name: Bugsnag Error Reporting API
  slug: open-bugsnag-error-reporting
- collection_type: open
  name: Bugsnag Build Builds Errors API
  slug: open-bugsnag-errors-api
- collection_type: open
  name: Bugsnag Build Builds EventFields API
  slug: open-bugsnag-eventfields-api
- collection_type: open
  name: Bugsnag Build Builds Events API
  slug: open-bugsnag-events-api
- collection_type: open
  name: Bugsnag Build Builds Notifications API
  slug: open-bugsnag-notifications-api
- collection_type: open
  name: Bugsnag Build Builds Organizations API
  slug: open-bugsnag-organizations-api
- collection_type: open
  name: Bugsnag Build Builds Pivots API
  slug: open-bugsnag-pivots-api
- collection_type: open
  name: Bugsnag Build Builds Projects API
  slug: open-bugsnag-projects-api
- collection_type: open
  name: Bugsnag Build Builds Releases API
  slug: open-bugsnag-releases-api
- collection_type: open
  name: Bugsnag Session Tracking API
  slug: open-bugsnag-session-tracking
- collection_type: open
  name: Bugsnag Build Builds Sessions API
  slug: open-bugsnag-sessions-api
- collection_type: open
  name: Bugsnag Build Builds Stability API
  slug: open-bugsnag-stability-api
- collection_type: open
  name: Bugsnag Trace API
  slug: open-bugsnag-trace
- collection_type: open
  name: Bugsnag Build Builds Traces API
  slug: open-bugsnag-traces-api
- collection_type: open
  name: Bugsnag Build Builds Trends API
  slug: open-bugsnag-trends-api
common:
- group: commercial
  href: https://artifacts.apis.io/bugsnag/finops/bugsnag-finops.yml
  title: ''
  type: FinOps
  url: finops/bugsnag-finops.yml
- group: other
  href: https://artifacts.apis.io/bugsnag/capabilities/bugsnag-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bugsnag-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://bugsnag.com
- group: agent
  href: https://artifacts.apis.io/bugsnag/agentic-access/bugsnag-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bugsnag-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bugsnag/security/bugsnag-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bugsnag-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bugsnag/security/bugsnag-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bugsnag-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/bugsnag/authentication/bugsnag-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bugsnag-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bugsnag
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bugsnag2
- group: build
  href: https://artifacts.apis.io/bugsnag/packages/bugsnag-packages.yml
  title: ''
  type: Packages
  url: packages/bugsnag-packages.yml
- group: build
  href: https://artifacts.apis.io/bugsnag/packages/bugsnag-packages.yml
  title: ''
  type: SDKs
  url: packages/bugsnag-packages.yml
- group: build
  href: https://artifacts.apis.io/bugsnag/cli/bugsnag-cli.yml
  title: ''
  type: CLI
  url: cli/bugsnag-cli.yml
- group: agent
  href: https://artifacts.apis.io/bugsnag/mcp/bugsnag-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bugsnag-mcp.yml
- group: build
  href: https://artifacts.apis.io/bugsnag/mcp/bugsnag-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bugsnag-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bugsnag/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/bugsnag/llms/bugsnag-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bugsnag-llms.txt
- group: agent
  href: https://artifacts.apis.io/bugsnag/well-known/bugsnag-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bugsnag-well-known.yml
- group: design
  href: https://artifacts.apis.io/bugsnag/conformance/bugsnag-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bugsnag-conformance.yml
- group: auth
  href: https://artifacts.apis.io/bugsnag/conformance/bugsnag-conformance.yml
  title: ''
  type: Compliance
  url: conformance/bugsnag-conformance.yml
- group: design
  href: https://artifacts.apis.io/bugsnag/errors/bugsnag-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bugsnag-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bugsnag/lifecycle/bugsnag-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bugsnag-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bugsnag.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.smartbear.com/bugsnag/docs/data-access-versioning
- group: auth
  href: https://artifacts.apis.io/bugsnag/scopes/bugsnag-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bugsnag-scopes.yml
- group: design
  href: https://artifacts.apis.io/bugsnag/conventions/bugsnag-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bugsnag-conventions.yml
- group: operate
  href: https://artifacts.apis.io/bugsnag/changelog/bugsnag-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bugsnag-changelog.yml
- group: design
  href: https://artifacts.apis.io/bugsnag/data-model/bugsnag-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bugsnag-data-model.yml
- group: other
  href: https://artifacts.apis.io/bugsnag/overlays/bugsnag-data-access-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bugsnag-data-access-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/bugsnag/security/bugsnag-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bugsnag-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bugsnag/security/bugsnag-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bugsnag-trust-center.yml
- group: design
  title: ''
  type: Webhooks
  url: https://docs.bugsnag.com/product/integrations/data-forwarding/webhook/
- group: commercial
  href: https://artifacts.apis.io/bugsnag/plans/bugsnag-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bugsnag-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bugsnag/rate-limits/bugsnag-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bugsnag-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/bugsnag/vocabulary/bugsnag-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bugsnag-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bugsnag/json-structure/bugsnag-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/bugsnag-structure.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.smartbear.com/bugsnag
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bugsnag.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.smartbear.com/bugsnag
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.smartbear.com/bugsnag/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.bugsnag.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bugsnag.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.bugsnag.com/user/new/
- group: start
  title: ''
  type: Login
  url: https://app.bugsnag.com/user/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smartbear.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smartbear.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://smartbear.com/blog/
- group: docs
  href: https://artifacts.apis.io/bugsnag/asyncapi/bugsnag-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/bugsnag-webhooks-asyncapi.yml
- group: docs
  href: https://artifacts.apis.io/bugsnag/json-schema/bugsnag-error-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/bugsnag-error-event-schema.json
- group: docs
  href: https://artifacts.apis.io/bugsnag/json-schema/bugsnag-build-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/bugsnag-build-schema.json
- group: design
  href: https://artifacts.apis.io/bugsnag/json-ld/bugsnag-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bugsnag-context.jsonld
created: 2024/04/14
description: 'BugSnag is an application stability monitoring platform from SmartBear that helps software teams detect, diagnose and fix errors in web, mobile, desktop and back-end applications. It combines error monitoring, real user monitoring and end-to-end distributed tracing behind a stability score that tells a team whether a release is safe to ship. BugSnag publishes six OpenAPI 3.0 definitions on SwaggerHub under the smartbear-public organization: a 141-operation Data Access API on api.bugsnag.com (errors, events, projects, releases, span groups, traces, feature flags and a full SCIM 2.0 provisioning surface), plus ingest and build-time APIs for error reporting (notify.bugsnag.com), session tracking (sessions.bugsnag.com), OTLP trace ingest (otlp.bugsnag.com), build notification (build.bugsnag.com) and symbol/source-map upload (upload.bugsnag.com). Agent access is first class: SmartBear runs a hosted MCP server at bugsnag.mcp.smartbear.com behind OAuth 2.1, and ships the same 19 BugSnag
  tools in the local @smartbear/mcp npm package.'
features:
- 'Free: 7.5K events + 1M spans/mo, 1 user'
- 'Select: 50K-3M events tiers, unlimited users, SAML SSO'
- 'Preferred: 100K-3M events, premium support, dedicated CSM'
- 'Enterprise: custom allowances, on-prem option, named CSM'
- Notify API for event ingest from any platform
- Data API at 60 req/min for issue queries
- 50+ platform SDKs (Node, Ruby, Python, JS, mobile, game engines)
- Stability scores and crash benchmarks
- End-to-end distributed tracing
- Auto error prioritization (Select+)
- Auto error assignment (Preferred+)
- Feature flags & experiments (Preferred+)
- On-prem deployment option (Preferred+)
- Sensitive data filtering
- 30+ integrations (Slack, Jira, GitHub, etc.)
- Source map upload for minified JS/native crashes
finops:
- has_sources: true
  method: derived
  name: Bugsnag Finops
  primary_unit: subscription
  service_category: ''
  slug: bugsnag-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bugsnag.png
json_schemas:
- name: ApplicationInfo
  property_count: 5
  slug: bugsnag-applicationinfo
- name: Breadcrumb
  property_count: 4
  slug: bugsnag-breadcrumb
- name: BreadcrumbPayload
  property_count: 4
  slug: bugsnag-breadcrumbpayload
- name: Bugsnag Build
  property_count: 9
  slug: bugsnag-build
- name: BuildPayload
  property_count: 9
  slug: bugsnag-buildpayload
- name: BuildResponse
  property_count: 2
  slug: bugsnag-buildresponse
- name: Collaborator
  property_count: 8
  slug: bugsnag-collaborator
- name: CollaboratorInvite
  property_count: 3
  slug: bugsnag-collaboratorinvite
- name: CollaboratorUpdate
  property_count: 2
  slug: bugsnag-collaboratorupdate
- name: Comment
  property_count: 6
  slug: bugsnag-comment
- name: CommentCreate
  property_count: 1
  slug: bugsnag-commentcreate
- name: DeviceInfo
  property_count: 6
  slug: bugsnag-deviceinfo
- name: Bugsnag Error Event
  property_count: 14
  slug: bugsnag-error-event
- name: Error
  property_count: 1
  slug: bugsnag-error
- name: ErrorItem
  property_count: 21
  slug: bugsnag-erroritem
- name: ErrorResponse
  property_count: 1
  slug: bugsnag-errorresponse
- name: ErrorUpdate
  property_count: 3
  slug: bugsnag-errorupdate
- name: Event
  property_count: 17
  slug: bugsnag-event
- name: EventField
  property_count: 3
  slug: bugsnag-eventfield
- name: EventPayload
  property_count: 14
  slug: bugsnag-eventpayload
- name: Exception
  property_count: 3
  slug: bugsnag-exception
- name: ExceptionPayload
  property_count: 4
  slug: bugsnag-exceptionpayload
- name: ExportTraceServiceRequest
  property_count: 1
  slug: bugsnag-exporttraceservicerequest
- name: ExportTraceServiceResponse
  property_count: 1
  slug: bugsnag-exporttraceserviceresponse
- name: KeyValue
  property_count: 2
  slug: bugsnag-keyvalue
- name: NotificationPayload
  property_count: 4
  slug: bugsnag-notificationpayload
- name: Notifier
  property_count: 3
  slug: bugsnag-notifier
- name: Organization
  property_count: 8
  slug: bugsnag-organization
- name: Pivot
  property_count: 4
  slug: bugsnag-pivot
- name: PivotValue
  property_count: 4
  slug: bugsnag-pivotvalue
- name: Project
  property_count: 22
  slug: bugsnag-project
- name: ProjectCreate
  property_count: 2
  slug: bugsnag-projectcreate
- name: ProjectUpdate
  property_count: 5
  slug: bugsnag-projectupdate
- name: Release
  property_count: 14
  slug: bugsnag-release
- name: ResourceSpans
  property_count: 2
  slug: bugsnag-resourcespans
- name: ScopeSpans
  property_count: 2
  slug: bugsnag-scopespans
- name: SessionCount
  property_count: 3
  slug: bugsnag-sessioncount
- name: SessionPayload
  property_count: 4
  slug: bugsnag-sessionpayload
- name: Span
  property_count: 10
  slug: bugsnag-span
- name: StabilityTrend
  property_count: 1
  slug: bugsnag-stabilitytrend
- name: StackFrame
  property_count: 6
  slug: bugsnag-stackframe
- name: StackFramePayload
  property_count: 6
  slug: bugsnag-stackframepayload
- name: ThreadPayload
  property_count: 4
  slug: bugsnag-threadpayload
- name: Trend
  property_count: 1
  slug: bugsnag-trend
- name: User
  property_count: 5
  slug: bugsnag-user
json_structures:
- name: Bugsnag Structure
  property_count: 0
  slug: bugsnag-structure
jsonld:
- class_count: 0
  name: Bugsnag Context
  property_count: 7
  slug: bugsnag-context
layout: provider
mcp_servers:
- description: 'SmartBear publishes a first-party Model Context Protocol server for BugSnag. It is available two ways: a hosted remote server an MCP client can POST to directly over OAuth, and a local stdio server di'
  name: BugSnag MCP (SmartBear MCP Server)
  slug: bugsnag-mcp-smartbear-mcp-server
modified: '2026-09-17'
name: Bugsnag
nav: Providers
network: true
overview: 'Bugsnag publishes 26 API contracts indexed on the [APIs.io](https://apis.io/) network, including Builds API, Collaborators API, Comments API, and 23 more. Tagged areas include Monitoring, Observability, Error Monitoring, Application Performance Monitoring, and Distributed Tracing.


  The Bugsnag catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Bugsnag''s developer surface includes authentication, CLI, changelog, documentation, API reference, getting-started guide, support, and 43 more developer resources.'
plans:
- name: Bugsnag Plans Pricing
  plan_count: 4
  slug: bugsnag-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 2
  name: Bugsnag Rate Limits
  slug: bugsnag-rate-limits
rules:
- authorship: generated
  effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Bugsnag — asyncapi rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: bugsnag-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Bugsnag — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: bugsnag-jsonschema-spectral-rules
scopes:
- name: Bugsnag Scopes
  scope_count: 3
  slug: bugsnag-scopes
  summary_line: 3 scopes · authorization_code/refresh_token
score:
  band: exemplar
  composite: 78.5
  coverage:
    artifact_dirs: 37
    catalog_earned: 77.0
    catalog_earned_first_party: 20.0
    catalog_gap: 38.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 62.1
    developer_ergonomics: 73.2
    discoverability: 73.3
    operational_transparency: 81.6
  previous_composite: 78.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
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
    score: 11.1
screenshot: https://apis.io/screenshots/bugsnag/bugsnag-2026-06-20T173757.png
security:
- kind: authentication
  name: Bugsnag Authentication
  slug: bugsnag-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Bugsnag Domain Security
  slug: bugsnag-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bugsnag Vulnerability Disclosure
  slug: bugsnag-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Bugsnag Trust Center
  slug: bugsnag-trust-center
  summary_line: SOC 2, ISO/IEC 27001, NIST CSF
skill_count: 4
skills:
- name: bugsnag-performance-investigation
  slug: bugsnag-performance-investigation
- name: bugsnag-provision-collaborators-scim
  slug: bugsnag-provision-collaborators-scim
- name: bugsnag-release-health
  slug: bugsnag-release-health
- name: bugsnag-triage-errors
  slug: bugsnag-triage-errors
slug: bugsnag
tags:
- Monitoring
- Observability
- Error Monitoring
- Application Performance Monitoring
- Distributed Tracing
- Developer Tools
- SmartBear
website: https://bugsnag.com
---
