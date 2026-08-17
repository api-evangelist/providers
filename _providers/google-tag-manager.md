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
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Google Tag Manager Agentic Access
  operation_count: 44
  slug: google-tag-manager-agentic-access
  summary_line: 44 operations · 26 acting
api_count: 9
apis:
- description: The Server-side Tagging API provides APIs for building custom tags, clients, and variables that run in a server-side container, enabling server-to-server data collection and processing.
  name: Google Tag Manager Server-side Tagging API
  slug: google-tag-manager-server-side-tagging-api
- description: Operations for managing Google Tag Manager accounts.
  name: Google Tag Manager Accounts API
  slug: google-tag-manager-accounts-api
- description: Operations for managing containers within a Google Tag Manager account.
  name: Google Tag Manager Containers API
  slug: google-tag-manager-containers-api
- description: The Tagmanager API from Google Tag Manager — 3 operation(s) for tagmanager.
  name: Google Tag Manager Tagmanager API
  slug: google-tag-manager-tagmanager-api
- description: Operations for managing triggers within a workspace that control when tags fire.
  name: Google Tag Manager Triggers API
  slug: google-tag-manager-triggers-api
- description: Operations for managing user permissions on Google Tag Manager accounts.
  name: Google Tag Manager User Permissions API
  slug: google-tag-manager-user-permissions-api
- description: Operations for managing variables within a workspace that provide dynamic values to tags and triggers.
  name: Google Tag Manager Variables API
  slug: google-tag-manager-variables-api
- description: Operations for managing container versions, including publishing and rollback.
  name: Google Tag Manager Versions API
  slug: google-tag-manager-versions-api
- description: Operations for managing workspaces within a container, including version creation and conflict resolution.
  name: Google Tag Manager Workspaces API
  slug: google-tag-manager-workspaces-api
arazzos:
- description: List a container's version headers, then fetch the newest one in full.
  name: Google Tag Manager Audit Container Versions
  slug: google-tag-manager-audit-container-versions-workflow
- description: Create a container and workspace, cut a baseline version, and publish it.
  name: Google Tag Manager Bootstrap a Live Container
  slug: google-tag-manager-bootstrap-live-container-workflow
- description: Workspace, trigger, tag, version, and publish in a single release flow.
  name: Google Tag Manager Build and Publish a Tag End to End
  slug: google-tag-manager-build-and-publish-tag-workflow
- description: List account user permissions, then add a new user when not present.
  name: Google Tag Manager Grant a User Permission
  slug: google-tag-manager-grant-user-permission-workflow
- description: Resolve a container's live version, then fetch its full definition.
  name: Google Tag Manager Inspect the Live Container Version
  slug: google-tag-manager-inspect-live-version-workflow
- description: List the workspaces in a container, then fetch the first one in detail.
  name: Google Tag Manager List and Get a Workspace
  slug: google-tag-manager-list-and-get-workspace-workflow
- description: Create a container, open a workspace in it, and add a first tag.
  name: Google Tag Manager Provision a Tagged Container
  slug: google-tag-manager-provision-tagged-container-workflow
- description: Read a tag for its fingerprint, then update it with optimistic concurrency.
  name: Google Tag Manager Safely Update a Tag
  slug: google-tag-manager-safe-update-tag-workflow
- description: Check status, sync a workspace to the latest version, then cut a version.
  name: Google Tag Manager Sync and Version a Workspace
  slug: google-tag-manager-sync-and-version-workspace-workflow
- description: Create a workspace, create a trigger, then create a tag that fires on it.
  name: Google Tag Manager Wire a Trigger-Fired Tag
  slug: google-tag-manager-trigger-fired-tag-workflow
- description: Create a workspace, create a variable, then create a tag that consumes it.
  name: Google Tag Manager Build a Variable-Backed Tag
  slug: google-tag-manager-variable-backed-tag-workflow
- description: Freeze a workspace into a container version and publish it live.
  name: Google Tag Manager Version and Publish a Workspace
  slug: google-tag-manager-version-and-publish-workspace-workflow
artifact_total: 181
collections:
- collection_type: postman
  name: Google Tag Manager API
  slug: postman-google-tag-manager-api-v2
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Tag Manager Accounts API
  slug: open-google-tag-manager-accounts-api
- collection_type: open
  name: Google Tag Manager API
  slug: open-google-tag-manager-api-v2
- collection_type: open
  name: Google Tag Manager Accounts Containers API
  slug: open-google-tag-manager-containers-api
- collection_type: open
  name: Google Tag Manager Accounts Tagmanager API
  slug: open-google-tag-manager-tagmanager-api
- collection_type: open
  name: Google Tag Manager Accounts Triggers API
  slug: open-google-tag-manager-triggers-api
- collection_type: open
  name: Google Tag Manager Accounts User Permissions API
  slug: open-google-tag-manager-user-permissions-api
- collection_type: open
  name: Google Tag Manager Accounts Variables API
  slug: open-google-tag-manager-variables-api
- collection_type: open
  name: Google Tag Manager Accounts Versions API
  slug: open-google-tag-manager-versions-api
- collection_type: open
  name: Google Tag Manager Accounts Workspaces API
  slug: open-google-tag-manager-workspaces-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-tag-manager-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/google-tag-manager-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/google-tag-manager-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/google-tag-manager-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/google-tag-manager-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/google-tag-manager-sandbox.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/google-tag-manager-security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/google-tag-manager-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://support.google.com/marketingplatform/answer/9013962
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: commercial
  title: ''
  type: Plans
  url: plans/google-tag-manager-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/google-tag-manager-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://marketingplatform.google.com/about/tag-manager/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/tag-platform/tag-manager/api/reference/rest
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/google-tag-manager-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/google-tag-manager-accounts-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/google-tag-manager-containers-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/google-tag-manager-tagmanager-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/google-tag-manager-triggers-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/google-tag-manager-user-permissions-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/google-tag-manager-variables-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/google-tag-manager-versions-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/google-tag-manager-workspaces-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/google-tag-manager-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/google-tag-manager-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/google-tag-manager-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/google-tag-manager-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/google-tag-manager-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/google-tag-manager-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/google-tag-manager-changelog.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-tag-manager-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-tag-manager-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-tag-manager-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-tag-manager-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-tag-manager/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-tag-manager-audit-container-versions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-tag-manager-bootstrap-live-container-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-tag-manager-build-and-publish-tag-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-tag-manager-grant-user-permission-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-tag-manager-inspect-live-version-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-tag-manager-list-and-get-workspace-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-tag-manager-provision-tagged-container-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-tag-manager-safe-update-tag-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-tag-manager-sync-and-version-workspace-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-tag-manager-trigger-fired-tag-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-tag-manager-variable-backed-tag-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-tag-manager-version-and-publish-workspace-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/tag-platform
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/tag-platform/tag-manager/api/v2/devguide
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/tag-platform/tag-manager/api/v2/authorization
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/tag-platform/tag-manager
- group: company
  title: ''
  type: Blog
  url: https://blog.google/products/marketingplatform/
- group: build
  title: ''
  type: SDKs
  url: https://developers.google.com/tag-platform/tag-manager/api/v2/libraries
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/tagmanager
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: start
  title: ''
  type: Signup
  url: https://tagmanager.google.com/
- group: start
  title: ''
  type: Login
  url: https://tagmanager.google.com/
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.google.com/tag-platform/tag-manager/api/v2/limits-quotas
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.google.com/tagmanager/answer/4620708
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/google-tag-manager
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/googlemarketingplatform
- group: design
  title: ''
  type: SpectralRules
  url: rules/google-tag-manager-spectral-rules.yml
created: '2024-01-01'
description: 'Google Tag Manager is a tag management system that lets teams deploy and update measurement codes and related code fragments — collectively known as tags — on a website, mobile app, or server-side container without editing site code on every change. The Tag Manager API v2 exposes that configuration programmatically: accounts, containers, workspaces, tags, triggers, variables, container versions, and user permissions, across web, iOS, Android, AMP, and server-side usage contexts. Changes are staged in a workspace, frozen into an immutable container version, and then published to live traffic, with fingerprint-based optimistic concurrency guarding every write. Access is OAuth 2.0 only, with seven granular scopes separating read, edit, publish, and user-management rights.'
examples:
- key_count: 1
  name: Google Tag Manager V2 Account Access Example
  slug: google-tag-manager-v2-account-access-example
- key_count: 6
  name: Google Tag Manager V2 Account Example
  slug: google-tag-manager-v2-account-example
- key_count: 2
  name: Google Tag Manager V2 Account Features Example
  slug: google-tag-manager-v2-account-features-example
- key_count: 2
  name: Google Tag Manager V2 Condition Example
  slug: google-tag-manager-v2-condition-example
- key_count: 1
  name: Google Tag Manager V2 Consent Settings Example
  slug: google-tag-manager-v2-consent-settings-example
- key_count: 2
  name: Google Tag Manager V2 Container Access Example
  slug: google-tag-manager-v2-container-access-example
- key_count: 12
  name: Google Tag Manager V2 Container Example
  slug: google-tag-manager-v2-container-example
- key_count: 14
  name: Google Tag Manager V2 Container Features Example
  slug: google-tag-manager-v2-container-features-example
- key_count: 12
  name: Google Tag Manager V2 Container Version Example
  slug: google-tag-manager-v2-container-version-example
- key_count: 9
  name: Google Tag Manager V2 Container Version Header Example
  slug: google-tag-manager-v2-container-version-header-example
- key_count: 2
  name: Google Tag Manager V2 Create Container Version Request Version Options Example
  slug: google-tag-manager-v2-create-container-version-request-version-options-example
- key_count: 2
  name: Google Tag Manager V2 Create Container Version Response Example
  slug: google-tag-manager-v2-create-container-version-response-example
- key_count: 1
  name: Google Tag Manager V2 Entity Example
  slug: google-tag-manager-v2-entity-example
- key_count: 1
  name: Google Tag Manager V2 Format Value Example
  slug: google-tag-manager-v2-format-value-example
- key_count: 2
  name: Google Tag Manager V2 Get Workspace Status Response Example
  slug: google-tag-manager-v2-get-workspace-status-response-example
- key_count: 2
  name: Google Tag Manager V2 List Accounts Response Example
  slug: google-tag-manager-v2-list-accounts-response-example
- key_count: 2
  name: Google Tag Manager V2 List Container Versions Response Example
  slug: google-tag-manager-v2-list-container-versions-response-example
- key_count: 2
  name: Google Tag Manager V2 List Containers Response Example
  slug: google-tag-manager-v2-list-containers-response-example
- key_count: 2
  name: Google Tag Manager V2 List Tags Response Example
  slug: google-tag-manager-v2-list-tags-response-example
- key_count: 2
  name: Google Tag Manager V2 List Triggers Response Example
  slug: google-tag-manager-v2-list-triggers-response-example
- key_count: 2
  name: Google Tag Manager V2 List User Permissions Response Example
  slug: google-tag-manager-v2-list-user-permissions-response-example
- key_count: 2
  name: Google Tag Manager V2 List Variables Response Example
  slug: google-tag-manager-v2-list-variables-response-example
- key_count: 2
  name: Google Tag Manager V2 List Workspaces Response Example
  slug: google-tag-manager-v2-list-workspaces-response-example
- key_count: 0
  name: Google Tag Manager V2 Merge Conflict Example
  slug: google-tag-manager-v2-merge-conflict-example
- key_count: 6
  name: Google Tag Manager V2 Parameter Example
  slug: google-tag-manager-v2-parameter-example
- key_count: 1
  name: Google Tag Manager V2 Publish Container Version Response Example
  slug: google-tag-manager-v2-publish-container-version-response-example
- key_count: 0
  name: Google Tag Manager V2 Revert Tag Response Example
  slug: google-tag-manager-v2-revert-tag-response-example
- key_count: 0
  name: Google Tag Manager V2 Revert Trigger Response Example
  slug: google-tag-manager-v2-revert-trigger-response-example
- key_count: 0
  name: Google Tag Manager V2 Revert Variable Response Example
  slug: google-tag-manager-v2-revert-variable-response-example
- key_count: 2
  name: Google Tag Manager V2 Setup Tag Example
  slug: google-tag-manager-v2-setup-tag-example
- key_count: 2
  name: Google Tag Manager V2 Sync Status Example
  slug: google-tag-manager-v2-sync-status-example
- key_count: 1
  name: Google Tag Manager V2 Sync Workspace Response Example
  slug: google-tag-manager-v2-sync-workspace-response-example
- key_count: 22
  name: Google Tag Manager V2 Tag Example
  slug: google-tag-manager-v2-tag-example
- key_count: 2
  name: Google Tag Manager V2 Teardown Tag Example
  slug: google-tag-manager-v2-teardown-tag-example
- key_count: 15
  name: Google Tag Manager V2 Trigger Example
  slug: google-tag-manager-v2-trigger-example
- key_count: 4
  name: Google Tag Manager V2 User Permission Example
  slug: google-tag-manager-v2-user-permission-example
- key_count: 16
  name: Google Tag Manager V2 Variable Example
  slug: google-tag-manager-v2-variable-example
- key_count: 8
  name: Google Tag Manager V2 Workspace Example
  slug: google-tag-manager-v2-workspace-example
features:
- description: List and manage Google Tag Manager accounts with full access control.
  name: Account Management
- description: Create, update, delete, and configure containers for web, mobile, and server-side tagging.
  name: Container Management
- description: Create and manage workspaces for collaborative tag development with conflict resolution.
  name: Workspace Management
- description: Create, update, delete, and revert tags with full parameter and firing trigger configuration.
  name: Tag Configuration
- description: Define triggers that control when and how tags fire based on events and conditions.
  name: Trigger Configuration
- description: Create and manage variables that provide dynamic values to tags and triggers.
  name: Variable Management
- description: Create, publish, and manage container versions with rollback capabilities.
  name: Version Control
- description: Manage user access and permissions at the account and container level.
  name: User Permissions
- description: Build custom server-side tags, clients, and variables for server-to-server data collection.
  name: Server-Side Tagging
- description: Structured data layer for passing information between your website and Tag Manager.
  name: Data Layer
finops:
- name: Google Tag Manager Finops
  service_category: API
  slug: google-tag-manager-finops
image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_tag_manager.svg
integrations:
- description: Native integration with Google Analytics 4 for event tracking and measurement.
  name: Google Analytics
- description: Deploy Google Ads conversion tracking and remarketing tags with built-in templates.
  name: Google Ads
- description: Integrate with Campaign Manager, Display & Video 360, and Search Ads 360.
  name: Google Marketing Platform
- description: Deploy and manage Facebook Pixel tracking with community template support.
  name: Facebook Pixel
- description: Integrate with consent management platforms for privacy-compliant tag firing.
  name: Consent Management Platforms
json_schemas:
- name: Google Tag Manager Container
  property_count: 13
  slug: google-tag-manager-container
- name: AccountAccess
  property_count: 1
  slug: google-tag-manager-v2-account-access
- name: AccountFeatures
  property_count: 2
  slug: google-tag-manager-v2-account-features
- name: Account
  property_count: 6
  slug: google-tag-manager-v2-account
- name: Condition
  property_count: 2
  slug: google-tag-manager-v2-condition
- name: ConsentSettings
  property_count: 1
  slug: google-tag-manager-v2-consent-settings
- name: ContainerAccess
  property_count: 2
  slug: google-tag-manager-v2-container-access
- name: ContainerFeatures
  property_count: 14
  slug: google-tag-manager-v2-container-features
- name: Container
  property_count: 12
  slug: google-tag-manager-v2-container
- name: ContainerVersionHeader
  property_count: 9
  slug: google-tag-manager-v2-container-version-header
- name: ContainerVersion
  property_count: 12
  slug: google-tag-manager-v2-container-version
- name: CreateContainerVersionRequestVersionOptions
  property_count: 2
  slug: google-tag-manager-v2-create-container-version-request-version-options
- name: CreateContainerVersionResponse
  property_count: 2
  slug: google-tag-manager-v2-create-container-version-response
- name: Entity
  property_count: 1
  slug: google-tag-manager-v2-entity
- name: FormatValue
  property_count: 1
  slug: google-tag-manager-v2-format-value
- name: GetWorkspaceStatusResponse
  property_count: 2
  slug: google-tag-manager-v2-get-workspace-status-response
- name: ListAccountsResponse
  property_count: 2
  slug: google-tag-manager-v2-list-accounts-response
- name: ListContainerVersionsResponse
  property_count: 2
  slug: google-tag-manager-v2-list-container-versions-response
- name: ListContainersResponse
  property_count: 2
  slug: google-tag-manager-v2-list-containers-response
- name: ListTagsResponse
  property_count: 2
  slug: google-tag-manager-v2-list-tags-response
- name: ListTriggersResponse
  property_count: 2
  slug: google-tag-manager-v2-list-triggers-response
- name: ListUserPermissionsResponse
  property_count: 2
  slug: google-tag-manager-v2-list-user-permissions-response
- name: ListVariablesResponse
  property_count: 2
  slug: google-tag-manager-v2-list-variables-response
- name: ListWorkspacesResponse
  property_count: 2
  slug: google-tag-manager-v2-list-workspaces-response
- name: MergeConflict
  property_count: 0
  slug: google-tag-manager-v2-merge-conflict
- name: Parameter
  property_count: 6
  slug: google-tag-manager-v2-parameter
- name: PublishContainerVersionResponse
  property_count: 1
  slug: google-tag-manager-v2-publish-container-version-response
- name: RevertTagResponse
  property_count: 0
  slug: google-tag-manager-v2-revert-tag-response
- name: RevertTriggerResponse
  property_count: 0
  slug: google-tag-manager-v2-revert-trigger-response
- name: RevertVariableResponse
  property_count: 0
  slug: google-tag-manager-v2-revert-variable-response
- name: SetupTag
  property_count: 2
  slug: google-tag-manager-v2-setup-tag
- name: SyncStatus
  property_count: 2
  slug: google-tag-manager-v2-sync-status
- name: SyncWorkspaceResponse
  property_count: 1
  slug: google-tag-manager-v2-sync-workspace-response
- name: Tag
  property_count: 22
  slug: google-tag-manager-v2-tag
- name: TeardownTag
  property_count: 2
  slug: google-tag-manager-v2-teardown-tag
- name: Trigger
  property_count: 15
  slug: google-tag-manager-v2-trigger
- name: UserPermission
  property_count: 4
  slug: google-tag-manager-v2-user-permission
- name: Variable
  property_count: 16
  slug: google-tag-manager-v2-variable
- name: Workspace
  property_count: 8
  slug: google-tag-manager-v2-workspace
json_structures:
- name: Google Tag Manager V2 Account Access Structure
  property_count: 1
  slug: google-tag-manager-v2-account-access-structure
- name: Google Tag Manager V2 Account Features Structure
  property_count: 2
  slug: google-tag-manager-v2-account-features-structure
- name: Google Tag Manager V2 Account Structure
  property_count: 6
  slug: google-tag-manager-v2-account-structure
- name: Google Tag Manager V2 Condition Structure
  property_count: 2
  slug: google-tag-manager-v2-condition-structure
- name: Google Tag Manager V2 Consent Settings Structure
  property_count: 1
  slug: google-tag-manager-v2-consent-settings-structure
- name: Google Tag Manager V2 Container Access Structure
  property_count: 2
  slug: google-tag-manager-v2-container-access-structure
- name: Google Tag Manager V2 Container Features Structure
  property_count: 14
  slug: google-tag-manager-v2-container-features-structure
- name: Google Tag Manager V2 Container Structure
  property_count: 12
  slug: google-tag-manager-v2-container-structure
- name: Google Tag Manager V2 Container Version Header Structure
  property_count: 9
  slug: google-tag-manager-v2-container-version-header-structure
- name: Google Tag Manager V2 Container Version Structure
  property_count: 12
  slug: google-tag-manager-v2-container-version-structure
- name: Google Tag Manager V2 Create Container Version Request Version Options Structure
  property_count: 2
  slug: google-tag-manager-v2-create-container-version-request-version-options-structure
- name: Google Tag Manager V2 Create Container Version Response Structure
  property_count: 2
  slug: google-tag-manager-v2-create-container-version-response-structure
- name: Google Tag Manager V2 Entity Structure
  property_count: 1
  slug: google-tag-manager-v2-entity-structure
- name: Google Tag Manager V2 Format Value Structure
  property_count: 1
  slug: google-tag-manager-v2-format-value-structure
- name: Google Tag Manager V2 Get Workspace Status Response Structure
  property_count: 2
  slug: google-tag-manager-v2-get-workspace-status-response-structure
- name: Google Tag Manager V2 List Accounts Response Structure
  property_count: 2
  slug: google-tag-manager-v2-list-accounts-response-structure
- name: Google Tag Manager V2 List Container Versions Response Structure
  property_count: 2
  slug: google-tag-manager-v2-list-container-versions-response-structure
- name: Google Tag Manager V2 List Containers Response Structure
  property_count: 2
  slug: google-tag-manager-v2-list-containers-response-structure
- name: Google Tag Manager V2 List Tags Response Structure
  property_count: 2
  slug: google-tag-manager-v2-list-tags-response-structure
- name: Google Tag Manager V2 List Triggers Response Structure
  property_count: 2
  slug: google-tag-manager-v2-list-triggers-response-structure
- name: Google Tag Manager V2 List User Permissions Response Structure
  property_count: 2
  slug: google-tag-manager-v2-list-user-permissions-response-structure
- name: Google Tag Manager V2 List Variables Response Structure
  property_count: 2
  slug: google-tag-manager-v2-list-variables-response-structure
- name: Google Tag Manager V2 List Workspaces Response Structure
  property_count: 2
  slug: google-tag-manager-v2-list-workspaces-response-structure
- name: Google Tag Manager V2 Merge Conflict Structure
  property_count: 0
  slug: google-tag-manager-v2-merge-conflict-structure
- name: Google Tag Manager V2 Parameter Structure
  property_count: 6
  slug: google-tag-manager-v2-parameter-structure
- name: Google Tag Manager V2 Publish Container Version Response Structure
  property_count: 1
  slug: google-tag-manager-v2-publish-container-version-response-structure
- name: Google Tag Manager V2 Revert Tag Response Structure
  property_count: 0
  slug: google-tag-manager-v2-revert-tag-response-structure
- name: Google Tag Manager V2 Revert Trigger Response Structure
  property_count: 0
  slug: google-tag-manager-v2-revert-trigger-response-structure
- name: Google Tag Manager V2 Revert Variable Response Structure
  property_count: 0
  slug: google-tag-manager-v2-revert-variable-response-structure
- name: Google Tag Manager V2 Setup Tag Structure
  property_count: 2
  slug: google-tag-manager-v2-setup-tag-structure
- name: Google Tag Manager V2 Sync Status Structure
  property_count: 2
  slug: google-tag-manager-v2-sync-status-structure
- name: Google Tag Manager V2 Sync Workspace Response Structure
  property_count: 1
  slug: google-tag-manager-v2-sync-workspace-response-structure
- name: Google Tag Manager V2 Tag Structure
  property_count: 22
  slug: google-tag-manager-v2-tag-structure
- name: Google Tag Manager V2 Teardown Tag Structure
  property_count: 2
  slug: google-tag-manager-v2-teardown-tag-structure
- name: Google Tag Manager V2 Trigger Structure
  property_count: 15
  slug: google-tag-manager-v2-trigger-structure
- name: Google Tag Manager V2 User Permission Structure
  property_count: 4
  slug: google-tag-manager-v2-user-permission-structure
- name: Google Tag Manager V2 Variable Structure
  property_count: 16
  slug: google-tag-manager-v2-variable-structure
- name: Google Tag Manager V2 Workspace Structure
  property_count: 8
  slug: google-tag-manager-v2-workspace-structure
jsonld:
- class_count: 8
  name: Google Tag Manager Context
  property_count: 8
  slug: google-tag-manager-context
- class_count: 0
  name: Google Tag Manager V2 Context
  property_count: 0
  slug: google-tag-manager-v2-context
layout: provider
mcp_servers:
- description: ''
  name: google-tag-manager-mcp.yml
  slug: google-tag-manager-mcpyml
modified: '2026-08-13'
name: Google Tag Manager
nav: Providers
network: true
overview: 'Google Tag Manager publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Containers API, Tagmanager API, and 5 more. Tagged areas include Analytics, Conversion Tracking, Marketing, Tag Management, and Tracking.


  The Google Tag Manager catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Google Tag Manager''s developer surface includes sandbox, pricing, API reference, changelog, authentication, developer portal, getting-started guide, and 58 more developer resources.'
plans:
- name: Google Tag Manager Plans Pricing
  plan_count: 2
  slug: google-tag-manager-plans-pricing
random_paper: 135
rate_limits:
- limit_count: 2
  name: Google Tag Manager Rate Limits
  slug: google-tag-manager-rate-limits
rules:
- name: Google Tag Manager API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-tag-manager-jsonschema-spectral-rules
- name: Google Tag Manager API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 5
  slug: google-tag-manager-spectral-rules
scopes:
- name: Google Tag Manager Scopes
  scope_count: 7
  slug: google-tag-manager-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: exemplar
  composite: 72.0
  delta: 9.2
  facets:
    commercial_clarity: 73.7
    contract_quality: 73.9
    developer_ergonomics: 78.3
    discoverability: 100.0
    governance: 69.8
    operational_transparency: 36.8
  previous_composite: 62.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/google-tag-manager/refs/heads/main/screenshots/google-tag-manager-2026-06-20T182239.png
security:
- kind: authentication
  name: Google Tag Manager Authentication
  slug: google-tag-manager-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Tag Manager Domain Security
  slug: google-tag-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Tag Manager Vulnerability Disclosure
  slug: google-tag-manager-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Google Tag Manager Trust Center
  slug: google-tag-manager-trust-center
  summary_line: ISO/IEC 27001
slug: google-tag-manager
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
use_cases:
- description: Deploy and manage marketing and analytics tags without modifying website code.
  name: Marketing Tag Deployment
- description: Track conversions across multiple advertising platforms with centralized tag management.
  name: Conversion Tracking
- description: Implement consent-based tag firing and data collection policies for GDPR and CCPA compliance.
  name: Privacy Compliance
- description: Deploy and manage A/B testing tags and experiment configurations across web properties.
  name: A/B Testing
- description: Process data server-side for improved performance, accuracy, and privacy compliance.
  name: Server-Side Data Collection
website: https://developers.google.com/tag-platform
---
