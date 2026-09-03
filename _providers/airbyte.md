---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 53
  human_in_the_loop: 4
  name: Airbyte Agentic Access
  operation_count: 91
  slug: airbyte-agentic-access
  summary_line: 91 operations · 53 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public API from Airbyte — 47 operation(s) for public.
  name: Airbyte public API
  slug: airbyte-public-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_applications API from Airbyte — 3 operation(s) for public_applications.
  name: Airbyte public_applications API
  slug: airbyte-public-applications-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_connections API from Airbyte — 2 operation(s) for public_connections.
  name: Airbyte public_connections API
  slug: airbyte-public-connections-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_connector_definitions API from Airbyte — 1 operation(s) for public_connector_definitions.
  name: Airbyte public_connector_definitions API
  slug: airbyte-public-connector-definitions-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_dataplanes API from Airbyte — 2 operation(s) for public_dataplanes.
  name: Airbyte public_dataplanes API
  slug: airbyte-public-dataplanes-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_declarative_source_definitions API from Airbyte — 2 operation(s) for public_declarative_source_definitions.
  name: Airbyte public_declarative_source_definitions API
  slug: airbyte-public-declarative-source-definitions-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_destination_definitions API from Airbyte — 2 operation(s) for public_destination_definitions.
  name: Airbyte public_destination_definitions API
  slug: airbyte-public-destination-definitions-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_destinations API from Airbyte — 2 operation(s) for public_destinations.
  name: Airbyte public_destinations API
  slug: airbyte-public-destinations-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_group_members API from Airbyte — 2 operation(s) for public_group_members.
  name: Airbyte public_group_members API
  slug: airbyte-public-group-members-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_group_permissions API from Airbyte — 2 operation(s) for public_group_permissions.
  name: Airbyte public_group_permissions API
  slug: airbyte-public-group-permissions-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_groups API from Airbyte — 2 operation(s) for public_groups.
  name: Airbyte public_groups API
  slug: airbyte-public-groups-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_health API from Airbyte — 1 operation(s) for public_health.
  name: Airbyte public_health API
  slug: airbyte-public-health-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_jobs API from Airbyte — 2 operation(s) for public_jobs.
  name: Airbyte public_jobs API
  slug: airbyte-public-jobs-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_oauth API from Airbyte — 1 operation(s) for public_oauth.
  name: Airbyte public_oauth API
  slug: airbyte-public-oauth-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_organizations API from Airbyte — 3 operation(s) for public_organizations.
  name: Airbyte public_organizations API
  slug: airbyte-public-organizations-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_permissions API from Airbyte — 2 operation(s) for public_permissions.
  name: Airbyte public_permissions API
  slug: airbyte-public-permissions-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_regions API from Airbyte — 2 operation(s) for public_regions.
  name: Airbyte public_regions API
  slug: airbyte-public-regions-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_root API from Airbyte — 1 operation(s) for public_root.
  name: Airbyte public_root API
  slug: airbyte-public-root-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_source_definitions API from Airbyte — 2 operation(s) for public_source_definitions.
  name: Airbyte public_source_definitions API
  slug: airbyte-public-source-definitions-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_sources API from Airbyte — 3 operation(s) for public_sources.
  name: Airbyte public_sources API
  slug: airbyte-public-sources-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_streams API from Airbyte — 1 operation(s) for public_streams.
  name: Airbyte public_streams API
  slug: airbyte-public-streams-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_tags API from Airbyte — 2 operation(s) for public_tags.
  name: Airbyte public_tags API
  slug: airbyte-public-tags-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_users API from Airbyte — 1 operation(s) for public_users.
  name: Airbyte public_users API
  slug: airbyte-public-users-api
- baseURL: https://api.airbyte.com/v1
  baseurl_source: declared
  description: The public_workspaces API from Airbyte — 3 operation(s) for public_workspaces.
  name: Airbyte public_workspaces API
  slug: airbyte-public-workspaces-api
arazzos:
- description: Create an API application to mint client credentials, read it back, then exchange those credentials for a bearer access token.
  name: Airbyte Bootstrap an Application and Access Token
  slug: airbyte-application-token-bootstrap-workflow
- description: List the running jobs for a connection, branch on whether any are running, then cancel the first one and confirm the cancellation.
  name: Airbyte Find and Cancel a Running Job
  slug: airbyte-cancel-running-job-workflow
- description: Create a destination connector, read it back to confirm it persisted, and list the workspace's destinations to confirm it appears.
  name: Airbyte Create and Verify a Destination
  slug: airbyte-destination-create-verify-workflow
- description: List the connections in a workspace, branch on whether any exist, then trigger and confirm a sync for the first connection.
  name: Airbyte Find a Connection and Trigger Its Sync
  slug: airbyte-find-connection-and-sync-workflow
- description: Stand up a source, a destination, inspect the available streams, wire them into a connection, and kick off the first sync.
  name: Airbyte Provision a Full Data Pipeline
  slug: airbyte-provision-pipeline-workflow
- description: Trigger a reset job to clear destination data, poll it to completion, then branch into a fresh sync when the reset succeeds.
  name: Airbyte Reset a Connection and Re-Sync
  slug: airbyte-reset-and-resync-workflow
- description: Create a source connector, read it back to confirm it persisted, and list the workspace's sources to confirm it appears.
  name: Airbyte Create and Verify a Source
  slug: airbyte-source-create-verify-workflow
- description: Create an organizing tag in a workspace, find the first connection, and patch that connection to carry the new tag.
  name: Airbyte Create a Tag and Apply It to a Connection
  slug: airbyte-tag-connection-workflow
- description: Kick off a sync job for a connection and poll its status until it succeeds, fails, or is cancelled.
  name: Airbyte Trigger a Sync and Poll to Completion
  slug: airbyte-trigger-sync-and-poll-workflow
- description: Create a workspace, read it back, create an organizing tag inside it, and confirm the workspace starts empty of connections.
  name: Airbyte Bootstrap a Workspace
  slug: airbyte-workspace-bootstrap-workflow
artifact_total: 808
collections:
- collection_type: postman
  name: airbyte-api Applications API
  slug: postman-airbyte-applications-api
- collection_type: postman
  name: airbyte-api Applications Connections API
  slug: postman-airbyte-connections-api
- collection_type: postman
  name: airbyte-api Applications ConnectorDefinitions API
  slug: postman-airbyte-connectordefinitions-api
- collection_type: postman
  name: airbyte-api Applications Dataplanes API
  slug: postman-airbyte-dataplanes-api
- collection_type: postman
  name: airbyte-api Applications DeclarativeSourceDefinitions API
  slug: postman-airbyte-declarativesourcedefinitions-api
- collection_type: postman
  name: airbyte-api Applications DestinationDefinitions API
  slug: postman-airbyte-destinationdefinitions-api
- collection_type: postman
  name: airbyte-api Applications Destinations API
  slug: postman-airbyte-destinations-api
- collection_type: postman
  name: airbyte-api Applications embedded_widget API
  slug: postman-airbyte-embedded-widget-api
- collection_type: postman
  name: airbyte-api Applications Groups API
  slug: postman-airbyte-groups-api
- collection_type: postman
  name: airbyte-api Applications Jobs API
  slug: postman-airbyte-jobs-api
- collection_type: postman
  name: airbyte-api Applications OAuth API
  slug: postman-airbyte-oauth-api
- collection_type: postman
  name: airbyte-api Applications Organizations API
  slug: postman-airbyte-organizations-api
- collection_type: postman
  name: airbyte-api Applications Permissions API
  slug: postman-airbyte-permissions-api
- collection_type: postman
  name: airbyte-api Applications public API
  slug: postman-airbyte-public-api
- collection_type: postman
  name: airbyte-api Applications public_applications API
  slug: postman-airbyte-public-applications-api
- collection_type: postman
  name: airbyte-api Applications public_connections API
  slug: postman-airbyte-public-connections-api
- collection_type: postman
  name: airbyte-api Applications public_connector_definitions API
  slug: postman-airbyte-public-connector-definitions-api
- collection_type: postman
  name: airbyte-api Applications public_dataplanes API
  slug: postman-airbyte-public-dataplanes-api
- collection_type: postman
  name: airbyte-api Applications public_declarative_source_definitions API
  slug: postman-airbyte-public-declarative-source-definitions-api
- collection_type: postman
  name: airbyte-api Applications public_destination_definitions API
  slug: postman-airbyte-public-destination-definitions-api
- collection_type: postman
  name: airbyte-api Applications public_group_members API
  slug: postman-airbyte-public-group-members-api
- collection_type: postman
  name: airbyte-api Applications public_group_permissions API
  slug: postman-airbyte-public-group-permissions-api
- collection_type: postman
  name: airbyte-api Applications public_groups API
  slug: postman-airbyte-public-groups-api
- collection_type: postman
  name: airbyte-api Applications public_health API
  slug: postman-airbyte-public-health-api
- collection_type: postman
  name: airbyte-api Applications public_jobs API
  slug: postman-airbyte-public-jobs-api
- collection_type: postman
  name: airbyte-api Applications public_oauth API
  slug: postman-airbyte-public-oauth-api
- collection_type: postman
  name: airbyte-api Applications public_organizations API
  slug: postman-airbyte-public-organizations-api
- collection_type: postman
  name: airbyte-api Applications public_permissions API
  slug: postman-airbyte-public-permissions-api
- collection_type: postman
  name: airbyte-api Applications public_regions API
  slug: postman-airbyte-public-regions-api
- collection_type: postman
  name: airbyte-api Applications public_root API
  slug: postman-airbyte-public-root-api
- collection_type: postman
  name: airbyte-api Applications public_source_definitions API
  slug: postman-airbyte-public-source-definitions-api
- collection_type: postman
  name: airbyte-api Applications public_sources API
  slug: postman-airbyte-public-sources-api
- collection_type: postman
  name: airbyte-api Applications public_streams API
  slug: postman-airbyte-public-streams-api
- collection_type: postman
  name: airbyte-api Applications public_tags API
  slug: postman-airbyte-public-tags-api
- collection_type: postman
  name: airbyte-api Applications public_users API
  slug: postman-airbyte-public-users-api
- collection_type: postman
  name: airbyte-api Applications public_workspaces API
  slug: postman-airbyte-public-workspaces-api
- collection_type: postman
  name: airbyte-api Applications Regions API
  slug: postman-airbyte-regions-api
- collection_type: postman
  name: airbyte-api Applications SourceDefinitions API
  slug: postman-airbyte-sourcedefinitions-api
- collection_type: postman
  name: airbyte-api Applications Sources API
  slug: postman-airbyte-sources-api
- collection_type: postman
  name: airbyte-api Applications Streams API
  slug: postman-airbyte-streams-api
- collection_type: postman
  name: airbyte-api Applications Tags API
  slug: postman-airbyte-tags-api
- collection_type: postman
  name: airbyte-api Applications Users API
  slug: postman-airbyte-users-api
- collection_type: postman
  name: airbyte-api Applications Workspaces API
  slug: postman-airbyte-workspaces-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: airbyte-api Applications API
  slug: open-airbyte-applications-api
- collection_type: open
  name: airbyte-api Applications Connections API
  slug: open-airbyte-connections-api
- collection_type: open
  name: airbyte-api Applications ConnectorDefinitions API
  slug: open-airbyte-connectordefinitions-api
- collection_type: open
  name: airbyte-api Applications Dataplanes API
  slug: open-airbyte-dataplanes-api
- collection_type: open
  name: airbyte-api Applications DeclarativeSourceDefinitions API
  slug: open-airbyte-declarativesourcedefinitions-api
- collection_type: open
  name: airbyte-api Applications DestinationDefinitions API
  slug: open-airbyte-destinationdefinitions-api
- collection_type: open
  name: airbyte-api Applications Destinations API
  slug: open-airbyte-destinations-api
- collection_type: open
  name: airbyte-api Applications embedded_widget API
  slug: open-airbyte-embedded-widget-api
- collection_type: open
  name: airbyte-api Applications Groups API
  slug: open-airbyte-groups-api
- collection_type: open
  name: airbyte-api Applications Jobs API
  slug: open-airbyte-jobs-api
- collection_type: open
  name: airbyte-api Applications OAuth API
  slug: open-airbyte-oauth-api
- collection_type: open
  name: airbyte-api Applications Organizations API
  slug: open-airbyte-organizations-api
- collection_type: open
  name: airbyte-api Applications Permissions API
  slug: open-airbyte-permissions-api
- collection_type: open
  name: airbyte-api Applications public API
  slug: open-airbyte-public-api
- collection_type: open
  name: airbyte-api Applications public_applications API
  slug: open-airbyte-public-applications-api
- collection_type: open
  name: airbyte-api Applications public_connections API
  slug: open-airbyte-public-connections-api
- collection_type: open
  name: airbyte-api Applications public_connector_definitions API
  slug: open-airbyte-public-connector-definitions-api
- collection_type: open
  name: airbyte-api Applications public_dataplanes API
  slug: open-airbyte-public-dataplanes-api
- collection_type: open
  name: airbyte-api Applications public_declarative_source_definitions API
  slug: open-airbyte-public-declarative-source-definitions-api
- collection_type: open
  name: airbyte-api Applications public_destination_definitions API
  slug: open-airbyte-public-destination-definitions-api
- collection_type: open
  name: airbyte-api Applications public_destinations API
  slug: open-airbyte-public-destinations-api
- collection_type: open
  name: airbyte-api Applications public_group_members API
  slug: open-airbyte-public-group-members-api
- collection_type: open
  name: airbyte-api Applications public_group_permissions API
  slug: open-airbyte-public-group-permissions-api
- collection_type: open
  name: airbyte-api Applications public_groups API
  slug: open-airbyte-public-groups-api
- collection_type: open
  name: airbyte-api Applications public_health API
  slug: open-airbyte-public-health-api
- collection_type: open
  name: airbyte-api Applications public_jobs API
  slug: open-airbyte-public-jobs-api
- collection_type: open
  name: airbyte-api Applications public_oauth API
  slug: open-airbyte-public-oauth-api
- collection_type: open
  name: airbyte-api Applications public_organizations API
  slug: open-airbyte-public-organizations-api
- collection_type: open
  name: airbyte-api Applications public_permissions API
  slug: open-airbyte-public-permissions-api
- collection_type: open
  name: airbyte-api Applications public_regions API
  slug: open-airbyte-public-regions-api
- collection_type: open
  name: airbyte-api Applications public_root API
  slug: open-airbyte-public-root-api
- collection_type: open
  name: airbyte-api Applications public_source_definitions API
  slug: open-airbyte-public-source-definitions-api
- collection_type: open
  name: airbyte-api Applications public_sources API
  slug: open-airbyte-public-sources-api
- collection_type: open
  name: airbyte-api Applications public_streams API
  slug: open-airbyte-public-streams-api
- collection_type: open
  name: airbyte-api Applications public_tags API
  slug: open-airbyte-public-tags-api
- collection_type: open
  name: airbyte-api Applications public_users API
  slug: open-airbyte-public-users-api
- collection_type: open
  name: airbyte-api Applications public_workspaces API
  slug: open-airbyte-public-workspaces-api
- collection_type: open
  name: airbyte-api Applications Regions API
  slug: open-airbyte-regions-api
- collection_type: open
  name: airbyte-api Applications SourceDefinitions API
  slug: open-airbyte-sourcedefinitions-api
- collection_type: open
  name: airbyte-api Applications Sources API
  slug: open-airbyte-sources-api
- collection_type: open
  name: airbyte-api Applications Streams API
  slug: open-airbyte-streams-api
- collection_type: open
  name: airbyte-api Applications Tags API
  slug: open-airbyte-tags-api
- collection_type: open
  name: airbyte-api Applications Users API
  slug: open-airbyte-users-api
- collection_type: open
  name: airbyte-api Applications Workspaces API
  slug: open-airbyte-workspaces-api
- collection_type: open
  name: airbyte-api
  slug: open-airbyte
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/airbyte/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airbyte-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airbyte-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/airbyte-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/airbyte-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/airbyte-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/airbyte-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/airbyte-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/airbyte-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/airbyte-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/airbyte-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/airbyte-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airbyte-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/airbyte-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/airbyte-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/airbyte-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/airbyte-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/airbyte-cli.yml
- group: design
  title: ''
  type: Components
  url: components/airbyte-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/airbyte-data-model.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/airbyte-application-token-bootstrap-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/airbyte-cancel-running-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/airbyte-destination-create-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/airbyte-find-connection-and-sync-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/airbyte-provision-pipeline-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/airbyte-reset-and-resync-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/airbyte-source-create-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/airbyte-tag-connection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/airbyte-trigger-sync-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/airbyte-workspace-bootstrap-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airbytehq
- group: start
  title: ''
  type: Portal
  url: https://airbyte.com
- group: start
  title: ''
  type: Console
  url: https://cloud.airbyte.io
- group: start
  title: ''
  type: Signup
  url: https://cloud.airbyte.io
- group: commercial
  title: ''
  type: Pricing
  url: https://airbyte.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/airbytehq
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/airbytehq/airbyte
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.airbyte.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.airbyte.com
- group: company
  title: ''
  type: Blog
  url: https://airbyte.com/blog
- group: learn
  title: ''
  type: Tutorials
  url: https://airbyte.com/tutorials
- group: operate
  title: ''
  type: Support
  url: https://support.airbyte.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airbyte.com/company/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airbyte.com/company/terms
- group: company
  title: ''
  type: Newsletter
  url: https://airbyte.com/community/newsletter
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.airbyte.com/category/release-notes/
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/orgs/airbytehq/projects/37/views/1
- group: build
  title: PyAirbyte
  type: SDKs
  url: https://github.com/airbytehq/PyAirbyte
- group: build
  title: Airbyte CLI (abctl)
  type: CLI
  url: https://github.com/airbytehq/abctl
- group: build
  title: Python Connector CDK
  type: SDKs
  url: https://github.com/airbytehq/airbyte-python-cdk
- group: build
  title: Agent SDK
  type: SDKs
  url: https://github.com/airbytehq/airbyte-agent-sdk
- group: build
  title: Helm Chart
  type: SDKs
  url: https://artifacthub.io/packages/helm/airbyte/airbyte
- group: design
  title: Airbyte Spectral Rules
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/rules/airbyte-spectral-rules.yml
- group: design
  title: Airbyte Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/vocabulary/airbyte-vocabulary.yaml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/airbytehq/airbyte-claude-skills
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.airbyte.com/llms.txt
created: '2025-01-08'
description: Airbyte is an open-source data integration platform that enables businesses to easily and efficiently move and consolidate their data from various sources into one centralized location. With Airbyte, organizations can seamlessly connect and synchronize data from sources such as databases, APIs, and other third-party applications, allowing for real-time insights and analysis. Airbyte offers both self-hosted and cloud-hosted options, with a catalog of hundreds of pre-built connectors.
examples:
- key_count: 0
  name: Airbyte Actor Definition Id Example
  slug: airbyte-actor-definition-id-example
- key_count: 0
  name: Airbyte Actor Type Enum Example
  slug: airbyte-actor-type-enum-example
- key_count: 6
  name: Airbyte Addgroupmember Example
  slug: airbyte-addgroupmember-example
- key_count: 2
  name: Airbyte Airbyte Api Connection Schedule Example
  slug: airbyte-airbyte-api-connection-schedule-example
- key_count: 1
  name: Airbyte Application Create Example
  slug: airbyte-application-create-example
- key_count: 5
  name: Airbyte Application Read Example
  slug: airbyte-application-read-example
- key_count: 1
  name: Airbyte Application Read List Example
  slug: airbyte-application-read-list-example
- key_count: 3
  name: Airbyte Application Token Request With Grant Example
  slug: airbyte-application-token-request-with-grant-example
- key_count: 0
  name: Airbyte Auth Provider Example
  slug: airbyte-auth-provider-example
- key_count: 6
  name: Airbyte Canceljob Example
  slug: airbyte-canceljob-example
- key_count: 3
  name: Airbyte Configured Stream Mapper Example
  slug: airbyte-configured-stream-mapper-example
- key_count: 12
  name: Airbyte Connection Create Request Example
  slug: airbyte-connection-create-request-example
- key_count: 10
  name: Airbyte Connection Patch Request Example
  slug: airbyte-connection-patch-request-example
- key_count: 15
  name: Airbyte Connection Response Example
  slug: airbyte-connection-response-example
- key_count: 3
  name: Airbyte Connection Schedule Response Example
  slug: airbyte-connection-schedule-response-example
- key_count: 0
  name: Airbyte Connection Status Enum Example
  slug: airbyte-connection-status-enum-example
- key_count: 0
  name: Airbyte Connection Sync Mode Enum Example
  slug: airbyte-connection-sync-mode-enum-example
- key_count: 3
  name: Airbyte Connections Response Example
  slug: airbyte-connections-response-example
- key_count: 4
  name: Airbyte Connector Definition Response Example
  slug: airbyte-connector-definition-response-example
- key_count: 1
  name: Airbyte Connector Definitions Response Example
  slug: airbyte-connector-definitions-response-example
- key_count: 0
  name: Airbyte Connector Type Example
  slug: airbyte-connector-type-example
- key_count: 2
  name: Airbyte Create Declarative Source Definition Request Example
  slug: airbyte-create-declarative-source-definition-request-example
- key_count: 4
  name: Airbyte Create Definition Request Example
  slug: airbyte-create-definition-request-example
- key_count: 6
  name: Airbyte Createaccesstoken Example
  slug: airbyte-createaccesstoken-example
- key_count: 6
  name: Airbyte Createapplication Example
  slug: airbyte-createapplication-example
- key_count: 6
  name: Airbyte Createconnection Example
  slug: airbyte-createconnection-example
- key_count: 6
  name: Airbyte Createdataplane Example
  slug: airbyte-createdataplane-example
- key_count: 6
  name: Airbyte Createdeclarativesourcedefinition Example
  slug: airbyte-createdeclarativesourcedefinition-example
- key_count: 6
  name: Airbyte Createdestination Example
  slug: airbyte-createdestination-example
- key_count: 6
  name: Airbyte Createdestinationdefinition Example
  slug: airbyte-createdestinationdefinition-example
- key_count: 6
  name: Airbyte Creategroup Example
  slug: airbyte-creategroup-example
- key_count: 6
  name: Airbyte Creategrouppermission Example
  slug: airbyte-creategrouppermission-example
- key_count: 6
  name: Airbyte Createjob Example
  slug: airbyte-createjob-example
- key_count: 6
  name: Airbyte Createpermission Example
  slug: airbyte-createpermission-example
- key_count: 6
  name: Airbyte Createregion Example
  slug: airbyte-createregion-example
- key_count: 6
  name: Airbyte Createsource Example
  slug: airbyte-createsource-example
- key_count: 6
  name: Airbyte Createsourcedefinition Example
  slug: airbyte-createsourcedefinition-example
- key_count: 6
  name: Airbyte Createtag Example
  slug: airbyte-createtag-example
- key_count: 6
  name: Airbyte Createworkspace Example
  slug: airbyte-createworkspace-example
- key_count: 3
  name: Airbyte Dataplane Create Request Example
  slug: airbyte-dataplane-create-request-example
- key_count: 2
  name: Airbyte Dataplane Patch Request Example
  slug: airbyte-dataplane-patch-request-example
- key_count: 6
  name: Airbyte Dataplane Response Example
  slug: airbyte-dataplane-response-example
- key_count: 1
  name: Airbyte Dataplanes Response Example
  slug: airbyte-dataplanes-response-example
- key_count: 0
  name: Airbyte Declarative Manifest Example
  slug: airbyte-declarative-manifest-example
- key_count: 4
  name: Airbyte Declarative Source Definition Response Example
  slug: airbyte-declarative-source-definition-response-example
- key_count: 3
  name: Airbyte Declarative Source Definitions Response Example
  slug: airbyte-declarative-source-definitions-response-example
- key_count: 5
  name: Airbyte Definition Response Example
  slug: airbyte-definition-response-example
- key_count: 3
  name: Airbyte Definitions Response Example
  slug: airbyte-definitions-response-example
- key_count: 6
  name: Airbyte Deleteapplication Example
  slug: airbyte-deleteapplication-example
- key_count: 6
  name: Airbyte Deletedataplane Example
  slug: airbyte-deletedataplane-example
- key_count: 6
  name: Airbyte Deletedeclarativesourcedefinition Example
  slug: airbyte-deletedeclarativesourcedefinition-example
- key_count: 6
  name: Airbyte Deletedestinationdefinition Example
  slug: airbyte-deletedestinationdefinition-example
- key_count: 6
  name: Airbyte Deleteregion Example
  slug: airbyte-deleteregion-example
- key_count: 6
  name: Airbyte Deletesourcedefinition Example
  slug: airbyte-deletesourcedefinition-example
- key_count: 0
  name: Airbyte Destination Configuration Example
  slug: airbyte-destination-configuration-example
- key_count: 5
  name: Airbyte Destination Create Request Example
  slug: airbyte-destination-create-request-example
- key_count: 3
  name: Airbyte Destination Patch Request Example
  slug: airbyte-destination-patch-request-example
- key_count: 3
  name: Airbyte Destination Put Request Example
  slug: airbyte-destination-put-request-example
- key_count: 8
  name: Airbyte Destination Response Example
  slug: airbyte-destination-response-example
- key_count: 3
  name: Airbyte Destinations Response Example
  slug: airbyte-destinations-response-example
- key_count: 1
  name: Airbyte Email Notification Config Example
  slug: airbyte-email-notification-config-example
- key_count: 3
  name: Airbyte Embedded Organization List Item Example
  slug: airbyte-embedded-organization-list-item-example
- key_count: 1
  name: Airbyte Embedded Organizations List Example
  slug: airbyte-embedded-organizations-list-example
- key_count: 1
  name: Airbyte Embedded Scoped Token Request Example
  slug: airbyte-embedded-scoped-token-request-example
- key_count: 1
  name: Airbyte Embedded Scoped Token Response Example
  slug: airbyte-embedded-scoped-token-response-example
- key_count: 3
  name: Airbyte Embedded Widget Request Example
  slug: airbyte-embedded-widget-request-example
- key_count: 1
  name: Airbyte Embedded Widget Response Example
  slug: airbyte-embedded-widget-response-example
- key_count: 6
  name: Airbyte Encryption Mapper Aes Configuration Example
  slug: airbyte-encryption-mapper-aes-configuration-example
- key_count: 0
  name: Airbyte Encryption Mapper Algorithm Example
  slug: airbyte-encryption-mapper-algorithm-example
- key_count: 0
  name: Airbyte Encryption Mapper Configuration Example
  slug: airbyte-encryption-mapper-configuration-example
- key_count: 4
  name: Airbyte Encryption Mapper Rsa Configuration Example
  slug: airbyte-encryption-mapper-rsa-configuration-example
- key_count: 1
  name: Airbyte Field Filtering Mapper Configuration Example
  slug: airbyte-field-filtering-mapper-configuration-example
- key_count: 2
  name: Airbyte Field Renaming Mapper Configuration Example
  slug: airbyte-field-renaming-mapper-configuration-example
- key_count: 6
  name: Airbyte Generateembeddedscopedtoken Example
  slug: airbyte-generateembeddedscopedtoken-example
- key_count: 6
  name: Airbyte Getapplication Example
  slug: airbyte-getapplication-example
- key_count: 6
  name: Airbyte Getconnection Example
  slug: airbyte-getconnection-example
- key_count: 6
  name: Airbyte Getdataplane Example
  slug: airbyte-getdataplane-example
- key_count: 6
  name: Airbyte Getdeclarativesourcedefinition Example
  slug: airbyte-getdeclarativesourcedefinition-example
- key_count: 6
  name: Airbyte Getdestination Example
  slug: airbyte-getdestination-example
- key_count: 6
  name: Airbyte Getdestinationdefinition Example
  slug: airbyte-getdestinationdefinition-example
- key_count: 6
  name: Airbyte Getembeddedwidget Example
  slug: airbyte-getembeddedwidget-example
- key_count: 6
  name: Airbyte Getgroup Example
  slug: airbyte-getgroup-example
- key_count: 6
  name: Airbyte Getjob Example
  slug: airbyte-getjob-example
- key_count: 6
  name: Airbyte Getpermission Example
  slug: airbyte-getpermission-example
- key_count: 6
  name: Airbyte Getregion Example
  slug: airbyte-getregion-example
- key_count: 6
  name: Airbyte Getsource Example
  slug: airbyte-getsource-example
- key_count: 6
  name: Airbyte Getsourcedefinition Example
  slug: airbyte-getsourcedefinition-example
- key_count: 6
  name: Airbyte Getstreamproperties Example
  slug: airbyte-getstreamproperties-example
- key_count: 6
  name: Airbyte Gettag Example
  slug: airbyte-gettag-example
- key_count: 6
  name: Airbyte Getworkspace Example
  slug: airbyte-getworkspace-example
- key_count: 3
  name: Airbyte Group Create Request Example
  slug: airbyte-group-create-request-example
- key_count: 1
  name: Airbyte Group Member Add Request Example
  slug: airbyte-group-member-add-request-example
- key_count: 5
  name: Airbyte Group Member Response Example
  slug: airbyte-group-member-response-example
- key_count: 3
  name: Airbyte Group Members Response Example
  slug: airbyte-group-members-response-example
- key_count: 3
  name: Airbyte Group Permission Create Request Example
  slug: airbyte-group-permission-create-request-example
- key_count: 5
  name: Airbyte Group Permission Response Example
  slug: airbyte-group-permission-response-example
- key_count: 1
  name: Airbyte Group Permissions Response Example
  slug: airbyte-group-permissions-response-example
- key_count: 5
  name: Airbyte Group Response Example
  slug: airbyte-group-response-example
- key_count: 2
  name: Airbyte Group Update Request Example
  slug: airbyte-group-update-request-example
- key_count: 3
  name: Airbyte Groups Response Example
  slug: airbyte-groups-response-example
- key_count: 3
  name: Airbyte Hashing Mapper Configuration Example
  slug: airbyte-hashing-mapper-configuration-example
- key_count: 7
  name: Airbyte Initiate Oauth Request Example
  slug: airbyte-initiate-oauth-request-example
- key_count: 2
  name: Airbyte Job Create Request Example
  slug: airbyte-job-create-request-example
- key_count: 9
  name: Airbyte Job Response Example
  slug: airbyte-job-response-example
- key_count: 0
  name: Airbyte Job Status Enum Example
  slug: airbyte-job-status-enum-example
- key_count: 0
  name: Airbyte Job Type Enum Example
  slug: airbyte-job-type-enum-example
- key_count: 0
  name: Airbyte Job Type Example
  slug: airbyte-job-type-example
- key_count: 2
  name: Airbyte Job Type Resource Limit Example
  slug: airbyte-job-type-resource-limit-example
- key_count: 3
  name: Airbyte Jobs Response Example
  slug: airbyte-jobs-response-example
- key_count: 6
  name: Airbyte Listapplications Example
  slug: airbyte-listapplications-example
- key_count: 6
  name: Airbyte Listconnections Example
  slug: airbyte-listconnections-example
- key_count: 6
  name: Airbyte Listconnectordefinitions Example
  slug: airbyte-listconnectordefinitions-example
- key_count: 6
  name: Airbyte Listdataplanes Example
  slug: airbyte-listdataplanes-example
- key_count: 6
  name: Airbyte Listdeclarativesourcedefinitions Example
  slug: airbyte-listdeclarativesourcedefinitions-example
- key_count: 6
  name: Airbyte Listdestinationdefinitions Example
  slug: airbyte-listdestinationdefinitions-example
- key_count: 6
  name: Airbyte Listdestinations Example
  slug: airbyte-listdestinations-example
- key_count: 6
  name: Airbyte Listembeddedorganizationsbyuser Example
  slug: airbyte-listembeddedorganizationsbyuser-example
- key_count: 6
  name: Airbyte Listgroupmembers Example
  slug: airbyte-listgroupmembers-example
- key_count: 6
  name: Airbyte Listgrouppermissions Example
  slug: airbyte-listgrouppermissions-example
- key_count: 6
  name: Airbyte Listgroups Example
  slug: airbyte-listgroups-example
- key_count: 6
  name: Airbyte Listjobs Example
  slug: airbyte-listjobs-example
- key_count: 6
  name: Airbyte Listorganizationsforuser Example
  slug: airbyte-listorganizationsforuser-example
- key_count: 6
  name: Airbyte Listpermissions Example
  slug: airbyte-listpermissions-example
- key_count: 6
  name: Airbyte Listregions Example
  slug: airbyte-listregions-example
- key_count: 6
  name: Airbyte Listsourcedefinitions Example
  slug: airbyte-listsourcedefinitions-example
- key_count: 6
  name: Airbyte Listsources Example
  slug: airbyte-listsources-example
- key_count: 6
  name: Airbyte Listtags Example
  slug: airbyte-listtags-example
- key_count: 6
  name: Airbyte Listuserswithinanorganization Example
  slug: airbyte-listuserswithinanorganization-example
- key_count: 6
  name: Airbyte Listworkspaces Example
  slug: airbyte-listworkspaces-example
- key_count: 0
  name: Airbyte Manifest Version Example
  slug: airbyte-manifest-version-example
- key_count: 0
  name: Airbyte Mapper Configuration Example
  slug: airbyte-mapper-configuration-example
- key_count: 0
  name: Airbyte Namespace Definition Enum Example
  slug: airbyte-namespace-definition-enum-example
- key_count: 0
  name: Airbyte Namespace Definition Enum No Default Example
  slug: airbyte-namespace-definition-enum-no-default-example
- key_count: 0
  name: Airbyte Namespace Definition Type Example
  slug: airbyte-namespace-definition-type-example
- key_count: 0
  name: Airbyte Non Breaking Changes Preference Example
  slug: airbyte-non-breaking-changes-preference-example
- key_count: 0
  name: Airbyte Non Breaking Schema Updates Behavior Enum Example
  slug: airbyte-non-breaking-schema-updates-behavior-enum-example
- key_count: 0
  name: Airbyte Non Breaking Schema Updates Behavior Enum No Default Example
  slug: airbyte-non-breaking-schema-updates-behavior-enum-no-default-example
- key_count: 2
  name: Airbyte Notification Config Example
  slug: airbyte-notification-config-example
- key_count: 6
  name: Airbyte Notifications Config Example
  slug: airbyte-notifications-config-example
- key_count: 0
  name: Airbyte O Auth Configuration Example
  slug: airbyte-o-auth-configuration-example
- key_count: 0
  name: Airbyte O Auth Credentials Configuration Example
  slug: airbyte-o-auth-credentials-configuration-example
- key_count: 0
  name: Airbyte O Auth Input Configuration Example
  slug: airbyte-o-auth-input-configuration-example
- key_count: 0
  name: Airbyte Organization Id Example
  slug: airbyte-organization-id-example
- key_count: 3
  name: Airbyte Organization O Auth Credentials Request Example
  slug: airbyte-organization-o-auth-credentials-request-example
- key_count: 3
  name: Airbyte Organization Response Example
  slug: airbyte-organization-response-example
- key_count: 1
  name: Airbyte Organizations Response Example
  slug: airbyte-organizations-response-example
- key_count: 6
  name: Airbyte Patchconnection Example
  slug: airbyte-patchconnection-example
- key_count: 6
  name: Airbyte Patchdestination Example
  slug: airbyte-patchdestination-example
- key_count: 6
  name: Airbyte Patchsource Example
  slug: airbyte-patchsource-example
- key_count: 4
  name: Airbyte Permission Create Request Example
  slug: airbyte-permission-create-request-example
- key_count: 5
  name: Airbyte Permission Response Example
  slug: airbyte-permission-response-example
- key_count: 5
  name: Airbyte Permission Response Read Example
  slug: airbyte-permission-response-read-example
- key_count: 0
  name: Airbyte Permission Scope Example
  slug: airbyte-permission-scope-example
- key_count: 0
  name: Airbyte Permission Type Example
  slug: airbyte-permission-type-example
- key_count: 1
  name: Airbyte Permission Update Request Example
  slug: airbyte-permission-update-request-example
- key_count: 1
  name: Airbyte Permissions Response Example
  slug: airbyte-permissions-response-example
- key_count: 3
  name: Airbyte Public Access Token Response Example
  slug: airbyte-public-access-token-response-example
- key_count: 0
  name: Airbyte Public Permission Type Example
  slug: airbyte-public-permission-type-example
- key_count: 6
  name: Airbyte Putdestination Example
  slug: airbyte-putdestination-example
- key_count: 6
  name: Airbyte Putsource Example
  slug: airbyte-putsource-example
- key_count: 1
  name: Airbyte Redirect Url Response Example
  slug: airbyte-redirect-url-response-example
- key_count: 3
  name: Airbyte Region Create Request Example
  slug: airbyte-region-create-request-example
- key_count: 2
  name: Airbyte Region Patch Request Example
  slug: airbyte-region-patch-request-example
- key_count: 6
  name: Airbyte Region Response Example
  slug: airbyte-region-response-example
- key_count: 1
  name: Airbyte Regions Response Example
  slug: airbyte-regions-response-example
- key_count: 6
  name: Airbyte Resource Requirements Example
  slug: airbyte-resource-requirements-example
- key_count: 1
  name: Airbyte Row Filtering Mapper Configuration Example
  slug: airbyte-row-filtering-mapper-configuration-example
- key_count: 3
  name: Airbyte Row Filtering Operation Equal Example
  slug: airbyte-row-filtering-operation-equal-example
- key_count: 0
  name: Airbyte Row Filtering Operation Example
  slug: airbyte-row-filtering-operation-example
- key_count: 2
  name: Airbyte Row Filtering Operation Not Example
  slug: airbyte-row-filtering-operation-not-example
- key_count: 0
  name: Airbyte Row Filtering Operation Type Example
  slug: airbyte-row-filtering-operation-type-example
- key_count: 0
  name: Airbyte Schedule Type Enum Example
  slug: airbyte-schedule-type-enum-example
- key_count: 0
  name: Airbyte Schedule Type With Basic Enum Example
  slug: airbyte-schedule-type-with-basic-enum-example
- key_count: 2
  name: Airbyte Scoped Resource Requirements Example
  slug: airbyte-scoped-resource-requirements-example
- key_count: 1
  name: Airbyte Selected Field Info Example
  slug: airbyte-selected-field-info-example
- key_count: 0
  name: Airbyte Selected Fields Example
  slug: airbyte-selected-fields-example
- key_count: 0
  name: Airbyte Source Configuration Example
  slug: airbyte-source-configuration-example
- key_count: 6
  name: Airbyte Source Create Request Example
  slug: airbyte-source-create-request-example
- key_count: 0
  name: Airbyte Source Definition Specification Example
  slug: airbyte-source-definition-specification-example
- key_count: 5
  name: Airbyte Source Patch Request Example
  slug: airbyte-source-patch-request-example
- key_count: 3
  name: Airbyte Source Put Request Example
  slug: airbyte-source-put-request-example
- key_count: 8
  name: Airbyte Source Response Example
  slug: airbyte-source-response-example
- key_count: 3
  name: Airbyte Sources Response Example
  slug: airbyte-sources-response-example
- key_count: 0
  name: Airbyte Sso Config Status Example
  slug: airbyte-sso-config-status-example
- key_count: 9
  name: Airbyte Stream Configuration Example
  slug: airbyte-stream-configuration-example
- key_count: 1
  name: Airbyte Stream Configurations Example
  slug: airbyte-stream-configurations-example
- key_count: 0
  name: Airbyte Stream Mapper Type Example
  slug: airbyte-stream-mapper-type-example
- key_count: 7
  name: Airbyte Stream Properties Example
  slug: airbyte-stream-properties-example
- key_count: 0
  name: Airbyte Stream Properties Response Example
  slug: airbyte-stream-properties-response-example
- key_count: 3
  name: Airbyte Tag Create Request Example
  slug: airbyte-tag-create-request-example
- key_count: 4
  name: Airbyte Tag Example
  slug: airbyte-tag-example
- key_count: 0
  name: Airbyte Tag Id Example
  slug: airbyte-tag-id-example
- key_count: 2
  name: Airbyte Tag Patch Request Example
  slug: airbyte-tag-patch-request-example
- key_count: 4
  name: Airbyte Tag Response Example
  slug: airbyte-tag-response-example
- key_count: 1
  name: Airbyte Tags Response Example
  slug: airbyte-tags-response-example
- key_count: 1
  name: Airbyte Update Declarative Source Definition Request Example
  slug: airbyte-update-declarative-source-definition-request-example
- key_count: 2
  name: Airbyte Update Definition Request Example
  slug: airbyte-update-definition-request-example
- key_count: 6
  name: Airbyte Updatedataplane Example
  slug: airbyte-updatedataplane-example
- key_count: 6
  name: Airbyte Updatedeclarativesourcedefinition Example
  slug: airbyte-updatedeclarativesourcedefinition-example
- key_count: 6
  name: Airbyte Updatedestinationdefinition Example
  slug: airbyte-updatedestinationdefinition-example
- key_count: 6
  name: Airbyte Updategroup Example
  slug: airbyte-updategroup-example
- key_count: 6
  name: Airbyte Updatepermission Example
  slug: airbyte-updatepermission-example
- key_count: 6
  name: Airbyte Updateregion Example
  slug: airbyte-updateregion-example
- key_count: 6
  name: Airbyte Updatesourcedefinition Example
  slug: airbyte-updatesourcedefinition-example
- key_count: 6
  name: Airbyte Updatetag Example
  slug: airbyte-updatetag-example
- key_count: 6
  name: Airbyte Updateworkspace Example
  slug: airbyte-updateworkspace-example
- key_count: 0
  name: Airbyte User Id Example
  slug: airbyte-user-id-example
- key_count: 3
  name: Airbyte User Response Example
  slug: airbyte-user-response-example
- key_count: 0
  name: Airbyte User Status Example
  slug: airbyte-user-status-example
- key_count: 1
  name: Airbyte Users Response Example
  slug: airbyte-users-response-example
- key_count: 2
  name: Airbyte Webhook Notification Config Example
  slug: airbyte-webhook-notification-config-example
- key_count: 4
  name: Airbyte Workspace Create Request Example
  slug: airbyte-workspace-create-request-example
- key_count: 0
  name: Airbyte Workspace Id Example
  slug: airbyte-workspace-id-example
- key_count: 3
  name: Airbyte Workspace O Auth Credentials Request Example
  slug: airbyte-workspace-o-auth-credentials-request-example
- key_count: 4
  name: Airbyte Workspace Response Example
  slug: airbyte-workspace-response-example
- key_count: 3
  name: Airbyte Workspace Update Request Example
  slug: airbyte-workspace-update-request-example
- key_count: 3
  name: Airbyte Workspaces Response Example
  slug: airbyte-workspaces-response-example
features:
- 'Core: free open-source self-managed'
- 'Standard from $10/mo: fully managed, volume-based'
- 'Plus: bulk-credit discounts, accelerated support'
- 'Pro: Data Workers capacity pricing, SSO, RBAC'
- 'Enterprise Flex: custom limits, dedicated SA'
- 600+ pre-built connectors
- Public API at 60 req/min/workspace
- OAuth 2.0 + workspace API keys
- Webhooks for sync events
- Connector Builder for custom sources
- dbt Cloud integration for transformations
- Multiple workspaces (Pro+)
- SSO and RBAC (Pro+)
- Self-hosted Enterprise option
- Bring your own custom connector
- Data Activation (Reverse ETL) capabilities
finops:
- name: Airbyte Finops
  service_category: Data Integration
  slug: airbyte-finops
graphqls:
- description: Airbyte exposes a GraphQL endpoint at `https://api.airbyte.com/graphql`. The endpoint requires authentication and returns a 401 for unauthenticated requests, confirming a live GraphQL surface. The sch
  name: Airbyte GraphQL
  slug: airbyte-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airbyte.png
integrations:
- description: Orchestrate Airbyte syncs from Airflow DAGs.
  name: Apache Airflow
- description: Transform data after Airbyte syncs with dbt models.
  name: dbt
- description: Load data into Snowflake data warehouse.
  name: Snowflake
- description: Sync data to Google BigQuery.
  name: BigQuery
- description: Load data into Amazon Redshift.
  name: Redshift
- description: Ingest data into Databricks lakehouse.
  name: Databricks
- description: Infrastructure-as-code support for Airbyte resources.
  name: Terraform
- description: Deploy Airbyte on Kubernetes using official Helm charts.
  name: Kubernetes / Helm
json_schemas:
- name: ActorDefinitionId
  property_count: 0
  slug: airbyte-actor-definition-id
- name: ActorTypeEnum
  property_count: 0
  slug: airbyte-actor-type-enum
- name: ActorDefinitionId
  property_count: 0
  slug: airbyte-actordefinitionid
- name: ActorTypeEnum
  property_count: 0
  slug: airbyte-actortypeenum
- name: AirbyteApiConnectionSchedule
  property_count: 2
  slug: airbyte-airbyte-api-connection-schedule
- name: AirbyteApiConnectionSchedule
  property_count: 2
  slug: airbyte-airbyteapiconnectionschedule
- name: ApplicationCreate
  property_count: 1
  slug: airbyte-application-create
- name: ApplicationReadList
  property_count: 1
  slug: airbyte-application-read-list
- name: ApplicationRead
  property_count: 5
  slug: airbyte-application-read
- name: ApplicationTokenRequestWithGrant
  property_count: 3
  slug: airbyte-application-token-request-with-grant
- name: ApplicationCreate
  property_count: 1
  slug: airbyte-applicationcreate
- name: ApplicationRead
  property_count: 5
  slug: airbyte-applicationread
- name: ApplicationReadList
  property_count: 1
  slug: airbyte-applicationreadlist
- name: ApplicationTokenRequestWithGrant
  property_count: 3
  slug: airbyte-applicationtokenrequestwithgrant
- name: AuthProvider
  property_count: 0
  slug: airbyte-auth-provider
- name: AuthProvider
  property_count: 0
  slug: airbyte-authprovider
- name: ConfiguredStreamMapper
  property_count: 3
  slug: airbyte-configured-stream-mapper
- name: ConfiguredStreamMapper
  property_count: 3
  slug: airbyte-configuredstreammapper
- name: ConnectionCreateRequest
  property_count: 12
  slug: airbyte-connection-create-request
- name: ConnectionPatchRequest
  property_count: 10
  slug: airbyte-connection-patch-request
- name: ConnectionResponse
  property_count: 15
  slug: airbyte-connection-response
- name: ConnectionScheduleResponse
  property_count: 3
  slug: airbyte-connection-schedule-response
- name: ConnectionStatusEnum
  property_count: 0
  slug: airbyte-connection-status-enum
- name: ConnectionSyncModeEnum
  property_count: 0
  slug: airbyte-connection-sync-mode-enum
- name: ConnectionCreateRequest
  property_count: 12
  slug: airbyte-connectioncreaterequest
- name: ConnectionPatchRequest
  property_count: 10
  slug: airbyte-connectionpatchrequest
- name: Root Type for ConnectionResponse
  property_count: 15
  slug: airbyte-connectionresponse
- name: ConnectionsResponse
  property_count: 3
  slug: airbyte-connections-response
- name: ConnectionScheduleResponse
  property_count: 3
  slug: airbyte-connectionscheduleresponse
- name: Root Type for ConnectionsResponse
  property_count: 3
  slug: airbyte-connectionsresponse
- name: ConnectionStatusEnum
  property_count: 0
  slug: airbyte-connectionstatusenum
- name: ConnectionSyncModeEnum
  property_count: 0
  slug: airbyte-connectionsyncmodeenum
- name: ConnectorDefinitionResponse
  property_count: 4
  slug: airbyte-connector-definition-response
- name: ConnectorDefinitionsResponse
  property_count: 1
  slug: airbyte-connector-definitions-response
- name: ConnectorType
  property_count: 0
  slug: airbyte-connector-type
- name: Root Type for ConnectorDefinitionResponse
  property_count: 4
  slug: airbyte-connectordefinitionresponse
- name: Root Type for DefinitionsResponse
  property_count: 1
  slug: airbyte-connectordefinitionsresponse
- name: ConnectorType
  property_count: 0
  slug: airbyte-connectortype
- name: CreateDeclarativeSourceDefinitionRequest
  property_count: 2
  slug: airbyte-create-declarative-source-definition-request
- name: CreateDefinitionRequest
  property_count: 4
  slug: airbyte-create-definition-request
- name: CreateDeclarativeSourceDefinitionRequest
  property_count: 2
  slug: airbyte-createdeclarativesourcedefinitionrequest
- name: CreateDefinitionRequest
  property_count: 4
  slug: airbyte-createdefinitionrequest
- name: DataplaneCreateRequest
  property_count: 3
  slug: airbyte-dataplane-create-request
- name: DataplanePatchRequest
  property_count: 2
  slug: airbyte-dataplane-patch-request
- name: DataplaneResponse
  property_count: 6
  slug: airbyte-dataplane-response
- name: DataplaneCreateRequest
  property_count: 3
  slug: airbyte-dataplanecreaterequest
- name: DataplanePatchRequest
  property_count: 2
  slug: airbyte-dataplanepatchrequest
- name: DataplaneResponse
  property_count: 6
  slug: airbyte-dataplaneresponse
- name: DataplanesResponse
  property_count: 1
  slug: airbyte-dataplanes-response
- name: DataplanesResponse
  property_count: 1
  slug: airbyte-dataplanesresponse
- name: DeclarativeManifest
  property_count: 0
  slug: airbyte-declarative-manifest
- name: DeclarativeSourceDefinitionResponse
  property_count: 4
  slug: airbyte-declarative-source-definition-response
- name: DeclarativeSourceDefinitionsResponse
  property_count: 3
  slug: airbyte-declarative-source-definitions-response
- name: DeclarativeManifest
  property_count: 0
  slug: airbyte-declarativemanifest
- name: DeclarativeSourceDefinitionResponse
  property_count: 4
  slug: airbyte-declarativesourcedefinitionresponse
- name: Root Type for DeclarativeSourceDefinitionsResponse
  property_count: 3
  slug: airbyte-declarativesourcedefinitionsresponse
- name: DefinitionResponse
  property_count: 5
  slug: airbyte-definition-response
- name: Root Type for DefinitionResponse
  property_count: 5
  slug: airbyte-definitionresponse
- name: DefinitionsResponse
  property_count: 3
  slug: airbyte-definitions-response
- name: Root Type for DefinitionsResponse
  property_count: 3
  slug: airbyte-definitionsresponse
- name: DestinationConfiguration
  property_count: 0
  slug: airbyte-destination-configuration
- name: DestinationCreateRequest
  property_count: 5
  slug: airbyte-destination-create-request
- name: DestinationPatchRequest
  property_count: 3
  slug: airbyte-destination-patch-request
- name: DestinationPutRequest
  property_count: 3
  slug: airbyte-destination-put-request
- name: DestinationResponse
  property_count: 8
  slug: airbyte-destination-response
- name: DestinationConfiguration
  property_count: 0
  slug: airbyte-destinationconfiguration
- name: DestinationCreateRequest
  property_count: 5
  slug: airbyte-destinationcreaterequest
- name: DestinationPatchRequest
  property_count: 3
  slug: airbyte-destinationpatchrequest
- name: DestinationPutRequest
  property_count: 3
  slug: airbyte-destinationputrequest
- name: Root Type for DestinationResponse
  property_count: 8
  slug: airbyte-destinationresponse
- name: DestinationsResponse
  property_count: 3
  slug: airbyte-destinations-response
- name: Root Type for DestinationsResponse
  property_count: 3
  slug: airbyte-destinationsresponse
- name: EmailNotificationConfig
  property_count: 1
  slug: airbyte-email-notification-config
- name: EmailNotificationConfig
  property_count: 1
  slug: airbyte-emailnotificationconfig
- name: EmbeddedOrganizationListItem
  property_count: 3
  slug: airbyte-embedded-organization-list-item
- name: EmbeddedOrganizationsList
  property_count: 1
  slug: airbyte-embedded-organizations-list
- name: EmbeddedScopedTokenRequest
  property_count: 1
  slug: airbyte-embedded-scoped-token-request
- name: EmbeddedScopedTokenResponse
  property_count: 1
  slug: airbyte-embedded-scoped-token-response
- name: EmbeddedWidgetRequest
  property_count: 3
  slug: airbyte-embedded-widget-request
- name: EmbeddedWidgetResponse
  property_count: 1
  slug: airbyte-embedded-widget-response
- name: EmbeddedOrganizationListItem
  property_count: 3
  slug: airbyte-embeddedorganizationlistitem
- name: EmbeddedOrganizationsList
  property_count: 1
  slug: airbyte-embeddedorganizationslist
- name: EmbeddedScopedTokenRequest
  property_count: 1
  slug: airbyte-embeddedscopedtokenrequest
- name: EmbeddedScopedTokenResponse
  property_count: 1
  slug: airbyte-embeddedscopedtokenresponse
- name: EmbeddedWidgetRequest
  property_count: 3
  slug: airbyte-embeddedwidgetrequest
- name: EmbeddedWidgetResponse
  property_count: 1
  slug: airbyte-embeddedwidgetresponse
- name: EncryptionMapperAESConfiguration
  property_count: 6
  slug: airbyte-encryption-mapper-aes-configuration
- name: EncryptionMapperAlgorithm
  property_count: 0
  slug: airbyte-encryption-mapper-algorithm
- name: EncryptionMapperConfiguration
  property_count: 0
  slug: airbyte-encryption-mapper-configuration
- name: EncryptionMapperRSAConfiguration
  property_count: 4
  slug: airbyte-encryption-mapper-rsa-configuration
- name: Encryption - AES
  property_count: 6
  slug: airbyte-encryptionmapperaesconfiguration
- name: EncryptionMapperAlgorithm
  property_count: 0
  slug: airbyte-encryptionmapperalgorithm
- name: Encryption
  property_count: 0
  slug: airbyte-encryptionmapperconfiguration
- name: Encryption - RSA
  property_count: 4
  slug: airbyte-encryptionmapperrsaconfiguration
- name: FieldFilteringMapperConfiguration
  property_count: 1
  slug: airbyte-field-filtering-mapper-configuration
- name: FieldRenamingMapperConfiguration
  property_count: 2
  slug: airbyte-field-renaming-mapper-configuration
- name: Field Filtering
  property_count: 1
  slug: airbyte-fieldfilteringmapperconfiguration
- name: Field Renaming
  property_count: 2
  slug: airbyte-fieldrenamingmapperconfiguration
- name: GroupCreateRequest
  property_count: 3
  slug: airbyte-group-create-request
- name: GroupMemberAddRequest
  property_count: 1
  slug: airbyte-group-member-add-request
- name: GroupMemberResponse
  property_count: 5
  slug: airbyte-group-member-response
- name: GroupMembersResponse
  property_count: 3
  slug: airbyte-group-members-response
- name: GroupPermissionCreateRequest
  property_count: 3
  slug: airbyte-group-permission-create-request
- name: GroupPermissionResponse
  property_count: 5
  slug: airbyte-group-permission-response
- name: GroupPermissionsResponse
  property_count: 1
  slug: airbyte-group-permissions-response
- name: GroupResponse
  property_count: 5
  slug: airbyte-group-response
- name: GroupUpdateRequest
  property_count: 2
  slug: airbyte-group-update-request
- name: Root Type for GroupCreateRequest
  property_count: 3
  slug: airbyte-groupcreaterequest
- name: Root Type for GroupMemberAddRequest
  property_count: 1
  slug: airbyte-groupmemberaddrequest
- name: Root Type for GroupMemberResponse
  property_count: 5
  slug: airbyte-groupmemberresponse
- name: Root Type for GroupMembersResponse
  property_count: 3
  slug: airbyte-groupmembersresponse
- name: Root Type for GroupPermissionCreateRequest
  property_count: 3
  slug: airbyte-grouppermissioncreaterequest
- name: Root Type for GroupPermissionResponse
  property_count: 5
  slug: airbyte-grouppermissionresponse
- name: Root Type for GroupPermissionsResponse
  property_count: 1
  slug: airbyte-grouppermissionsresponse
- name: Root Type for GroupResponse
  property_count: 5
  slug: airbyte-groupresponse
- name: GroupsResponse
  property_count: 3
  slug: airbyte-groups-response
- name: Root Type for GroupsResponse
  property_count: 3
  slug: airbyte-groupsresponse
- name: Root Type for GroupUpdateRequest
  property_count: 2
  slug: airbyte-groupupdaterequest
- name: HashingMapperConfiguration
  property_count: 3
  slug: airbyte-hashing-mapper-configuration
- name: Hashing
  property_count: 3
  slug: airbyte-hashingmapperconfiguration
- name: InitiateOauthRequest
  property_count: 7
  slug: airbyte-initiate-oauth-request
- name: Root Type for initiate-oauth-post-body
  property_count: 7
  slug: airbyte-initiateoauthrequest
- name: JobCreateRequest
  property_count: 2
  slug: airbyte-job-create-request
- name: JobResponse
  property_count: 9
  slug: airbyte-job-response
- name: JobStatusEnum
  property_count: 0
  slug: airbyte-job-status-enum
- name: JobTypeEnum
  property_count: 0
  slug: airbyte-job-type-enum
- name: JobTypeResourceLimit
  property_count: 2
  slug: airbyte-job-type-resource-limit
- name: JobType
  property_count: 0
  slug: airbyte-job-type
- name: Root Type for JobCreate
  property_count: 2
  slug: airbyte-jobcreaterequest
- name: Root Type for JobResponse
  property_count: 9
  slug: airbyte-jobresponse
- name: JobsResponse
  property_count: 3
  slug: airbyte-jobs-response
- name: Root Type for JobsResponse
  property_count: 3
  slug: airbyte-jobsresponse
- name: JobStatusEnum
  property_count: 0
  slug: airbyte-jobstatusenum
- name: JobType
  property_count: 0
  slug: airbyte-jobtype
- name: JobTypeEnum
  property_count: 0
  slug: airbyte-jobtypeenum
- name: JobTypeResourceLimit
  property_count: 2
  slug: airbyte-jobtyperesourcelimit
- name: ManifestVersion
  property_count: 0
  slug: airbyte-manifest-version
- name: ManifestVersion
  property_count: 0
  slug: airbyte-manifestversion
- name: MapperConfiguration
  property_count: 0
  slug: airbyte-mapper-configuration
- name: MapperConfiguration
  property_count: 0
  slug: airbyte-mapperconfiguration
- name: NamespaceDefinitionEnumNoDefault
  property_count: 0
  slug: airbyte-namespace-definition-enum-no-default
- name: NamespaceDefinitionEnum
  property_count: 0
  slug: airbyte-namespace-definition-enum
- name: NamespaceDefinitionType
  property_count: 0
  slug: airbyte-namespace-definition-type
- name: NamespaceDefinitionEnum
  property_count: 0
  slug: airbyte-namespacedefinitionenum
- name: NamespaceDefinitionEnumNoDefault
  property_count: 0
  slug: airbyte-namespacedefinitionenumnodefault
- name: NamespaceDefinitionType
  property_count: 0
  slug: airbyte-namespacedefinitiontype
- name: NonBreakingChangesPreference
  property_count: 0
  slug: airbyte-non-breaking-changes-preference
- name: NonBreakingSchemaUpdatesBehaviorEnumNoDefault
  property_count: 0
  slug: airbyte-non-breaking-schema-updates-behavior-enum-no-default
- name: NonBreakingSchemaUpdatesBehaviorEnum
  property_count: 0
  slug: airbyte-non-breaking-schema-updates-behavior-enum
- name: NonBreakingChangesPreference
  property_count: 0
  slug: airbyte-nonbreakingchangespreference
- name: NonBreakingSchemaUpdatesBehaviorEnum
  property_count: 0
  slug: airbyte-nonbreakingschemaupdatesbehaviorenum
- name: NonBreakingSchemaUpdatesBehaviorEnumNoDefault
  property_count: 0
  slug: airbyte-nonbreakingschemaupdatesbehaviorenumnodefault
- name: NotificationConfig
  property_count: 2
  slug: airbyte-notification-config
- name: NotificationConfig
  property_count: 2
  slug: airbyte-notificationconfig
- name: NotificationsConfig
  property_count: 6
  slug: airbyte-notifications-config
- name: NotificationsConfig
  property_count: 6
  slug: airbyte-notificationsconfig
- name: OAuthConfiguration
  property_count: 0
  slug: airbyte-o-auth-configuration
- name: OAuthCredentialsConfiguration
  property_count: 0
  slug: airbyte-o-auth-credentials-configuration
- name: OAuthInputConfiguration
  property_count: 0
  slug: airbyte-o-auth-input-configuration
- name: OAuthConfiguration
  property_count: 0
  slug: airbyte-oauthconfiguration
- name: OAuthCredentialsConfiguration
  property_count: 0
  slug: airbyte-oauthcredentialsconfiguration
- name: OAuthInputConfiguration
  property_count: 0
  slug: airbyte-oauthinputconfiguration
- name: OrganizationId
  property_count: 0
  slug: airbyte-organization-id
- name: OrganizationOAuthCredentialsRequest
  property_count: 3
  slug: airbyte-organization-o-auth-credentials-request
- name: OrganizationResponse
  property_count: 3
  slug: airbyte-organization-response
- name: OrganizationId
  property_count: 0
  slug: airbyte-organizationid
- name: Root Type for OrganizationOAuthCredentials
  property_count: 3
  slug: airbyte-organizationoauthcredentialsrequest
- name: Root Type for OrganizationResponse
  property_count: 3
  slug: airbyte-organizationresponse
- name: OrganizationsResponse
  property_count: 1
  slug: airbyte-organizations-response
- name: Root Type for OrganizationsResponse
  property_count: 1
  slug: airbyte-organizationsresponse
- name: PermissionCreateRequest
  property_count: 4
  slug: airbyte-permission-create-request
- name: PermissionResponseRead
  property_count: 5
  slug: airbyte-permission-response-read
- name: PermissionResponse
  property_count: 5
  slug: airbyte-permission-response
- name: PermissionScope
  property_count: 0
  slug: airbyte-permission-scope
- name: PermissionType
  property_count: 0
  slug: airbyte-permission-type
- name: PermissionUpdateRequest
  property_count: 1
  slug: airbyte-permission-update-request
- name: PermissionCreateRequest
  property_count: 4
  slug: airbyte-permissioncreaterequest
- name: Root Type for PermissionResponse
  property_count: 5
  slug: airbyte-permissionresponse
- name: Root type for PermissionResponseRead
  property_count: 5
  slug: airbyte-permissionresponseread
- name: PermissionsResponse
  property_count: 1
  slug: airbyte-permissions-response
- name: PermissionScope
  property_count: 0
  slug: airbyte-permissionscope
- name: Root Type for PermissionsResponse
  property_count: 1
  slug: airbyte-permissionsresponse
- name: PermissionType
  property_count: 0
  slug: airbyte-permissiontype
- name: PermissionUpdateRequest
  property_count: 1
  slug: airbyte-permissionupdaterequest
- name: PublicAccessTokenResponse
  property_count: 3
  slug: airbyte-public-access-token-response
- name: PublicPermissionType
  property_count: 0
  slug: airbyte-public-permission-type
- name: PublicAccessTokenResponse
  property_count: 3
  slug: airbyte-publicaccesstokenresponse
- name: PublicPermissionType
  property_count: 0
  slug: airbyte-publicpermissiontype
- name: RedirectUrlResponse
  property_count: 1
  slug: airbyte-redirect-url-response
- name: Root Type for RedirectUrlResponse
  property_count: 1
  slug: airbyte-redirecturlresponse
- name: RegionCreateRequest
  property_count: 3
  slug: airbyte-region-create-request
- name: RegionPatchRequest
  property_count: 2
  slug: airbyte-region-patch-request
- name: RegionResponse
  property_count: 6
  slug: airbyte-region-response
- name: RegionCreateRequest
  property_count: 3
  slug: airbyte-regioncreaterequest
- name: RegionPatchRequest
  property_count: 2
  slug: airbyte-regionpatchrequest
- name: RegionResponse
  property_count: 6
  slug: airbyte-regionresponse
- name: RegionsResponse
  property_count: 1
  slug: airbyte-regions-response
- name: RegionsResponse
  property_count: 1
  slug: airbyte-regionsresponse
- name: ResourceRequirements
  property_count: 6
  slug: airbyte-resource-requirements
- name: ResourceRequirements
  property_count: 6
  slug: airbyte-resourcerequirements
- name: RowFilteringMapperConfiguration
  property_count: 1
  slug: airbyte-row-filtering-mapper-configuration
- name: RowFilteringOperationEqual
  property_count: 3
  slug: airbyte-row-filtering-operation-equal
- name: RowFilteringOperationNot
  property_count: 2
  slug: airbyte-row-filtering-operation-not
- name: RowFilteringOperation
  property_count: 0
  slug: airbyte-row-filtering-operation
- name: RowFilteringOperationType
  property_count: 0
  slug: airbyte-row-filtering-operation-type
- name: Row Filtering
  property_count: 1
  slug: airbyte-rowfilteringmapperconfiguration
- name: RowFilteringOperation
  property_count: 0
  slug: airbyte-rowfilteringoperation
- name: EQUAL
  property_count: 3
  slug: airbyte-rowfilteringoperationequal
- name: NOT
  property_count: 2
  slug: airbyte-rowfilteringoperationnot
- name: RowFilteringOperationType
  property_count: 0
  slug: airbyte-rowfilteringoperationtype
- name: ScheduleTypeEnum
  property_count: 0
  slug: airbyte-schedule-type-enum
- name: ScheduleTypeWithBasicEnum
  property_count: 0
  slug: airbyte-schedule-type-with-basic-enum
- name: ScheduleTypeEnum
  property_count: 0
  slug: airbyte-scheduletypeenum
- name: ScheduleTypeWithBasicEnum
  property_count: 0
  slug: airbyte-scheduletypewithbasicenum
- name: ScopedResourceRequirements
  property_count: 2
  slug: airbyte-scoped-resource-requirements
- name: ScopedResourceRequirements
  property_count: 2
  slug: airbyte-scopedresourcerequirements
- name: SelectedFieldInfo
  property_count: 1
  slug: airbyte-selected-field-info
- name: SelectedFields
  property_count: 0
  slug: airbyte-selected-fields
- name: SelectedFieldInfo
  property_count: 1
  slug: airbyte-selectedfieldinfo
- name: SelectedFields
  property_count: 0
  slug: airbyte-selectedfields
- name: SourceConfiguration
  property_count: 0
  slug: airbyte-source-configuration
- name: SourceCreateRequest
  property_count: 6
  slug: airbyte-source-create-request
- name: SourceDefinitionSpecification
  property_count: 0
  slug: airbyte-source-definition-specification
- name: SourcePatchRequest
  property_count: 5
  slug: airbyte-source-patch-request
- name: SourcePutRequest
  property_count: 3
  slug: airbyte-source-put-request
- name: SourceResponse
  property_count: 8
  slug: airbyte-source-response
- name: SourceConfiguration
  property_count: 0
  slug: airbyte-sourceconfiguration
- name: SourceCreateRequest
  property_count: 6
  slug: airbyte-sourcecreaterequest
- name: SourceDefinitionSpecification
  property_count: 0
  slug: airbyte-sourcedefinitionspecification
- name: SourcePatchRequest
  property_count: 5
  slug: airbyte-sourcepatchrequest
- name: SourcePutRequest
  property_count: 3
  slug: airbyte-sourceputrequest
- name: Root Type for SourceResponse
  property_count: 8
  slug: airbyte-sourceresponse
- name: SourcesResponse
  property_count: 3
  slug: airbyte-sources-response
- name: Root Type for SourcesResponse
  property_count: 3
  slug: airbyte-sourcesresponse
- name: SSOConfigStatus
  property_count: 0
  slug: airbyte-sso-config-status
- name: SSOConfigStatus
  property_count: 0
  slug: airbyte-ssoconfigstatus
- name: StreamConfiguration
  property_count: 9
  slug: airbyte-stream-configuration
- name: StreamConfigurations
  property_count: 1
  slug: airbyte-stream-configurations
- name: StreamMapperType
  property_count: 0
  slug: airbyte-stream-mapper-type
- name: StreamPropertiesResponse
  property_count: 0
  slug: airbyte-stream-properties-response
- name: StreamProperties
  property_count: 7
  slug: airbyte-stream-properties
- name: StreamConfiguration
  property_count: 9
  slug: airbyte-streamconfiguration
- name: StreamConfigurations
  property_count: 1
  slug: airbyte-streamconfigurations
- name: StreamMapperType
  property_count: 0
  slug: airbyte-streammappertype
- name: StreamProperties
  property_count: 7
  slug: airbyte-streamproperties
- name: StreamPropertiesResponse
  property_count: 0
  slug: airbyte-streampropertiesresponse
- name: TagCreateRequest
  property_count: 3
  slug: airbyte-tag-create-request
- name: TagId
  property_count: 0
  slug: airbyte-tag-id
- name: TagPatchRequest
  property_count: 2
  slug: airbyte-tag-patch-request
- name: TagResponse
  property_count: 4
  slug: airbyte-tag-response
- name: Tag
  property_count: 4
  slug: airbyte-tag
- name: TagCreateRequest
  property_count: 3
  slug: airbyte-tagcreaterequest
- name: TagId
  property_count: 0
  slug: airbyte-tagid
- name: TagPatchRequest
  property_count: 2
  slug: airbyte-tagpatchrequest
- name: Root Type for TagResponse
  property_count: 4
  slug: airbyte-tagresponse
- name: TagsResponse
  property_count: 1
  slug: airbyte-tags-response
- name: Root Type for TagsResponse
  property_count: 1
  slug: airbyte-tagsresponse
- name: UpdateDeclarativeSourceDefinitionRequest
  property_count: 1
  slug: airbyte-update-declarative-source-definition-request
- name: UpdateDefinitionRequest
  property_count: 2
  slug: airbyte-update-definition-request
- name: UpdateDeclarativeSourceDefinitionRequest
  property_count: 1
  slug: airbyte-updatedeclarativesourcedefinitionrequest
- name: UpdateDefinitionRequest
  property_count: 2
  slug: airbyte-updatedefinitionrequest
- name: UserId
  property_count: 0
  slug: airbyte-user-id
- name: UserResponse
  property_count: 3
  slug: airbyte-user-response
- name: UserStatus
  property_count: 0
  slug: airbyte-user-status
- name: UserId
  property_count: 0
  slug: airbyte-userid
- name: Root Type for UserResponse
  property_count: 3
  slug: airbyte-userresponse
- name: UsersResponse
  property_count: 1
  slug: airbyte-users-response
- name: Root Type for UsersResponse
  property_count: 1
  slug: airbyte-usersresponse
- name: UserStatus
  property_count: 0
  slug: airbyte-userstatus
- name: WebhookNotificationConfig
  property_count: 2
  slug: airbyte-webhook-notification-config
- name: WebhookNotificationConfig
  property_count: 2
  slug: airbyte-webhooknotificationconfig
- name: WorkspaceCreateRequest
  property_count: 4
  slug: airbyte-workspace-create-request
- name: WorkspaceId
  property_count: 0
  slug: airbyte-workspace-id
- name: WorkspaceOAuthCredentialsRequest
  property_count: 3
  slug: airbyte-workspace-o-auth-credentials-request
- name: WorkspaceResponse
  property_count: 4
  slug: airbyte-workspace-response
- name: WorkspaceUpdateRequest
  property_count: 3
  slug: airbyte-workspace-update-request
- name: WorkspaceCreateRequest
  property_count: 4
  slug: airbyte-workspacecreaterequest
- name: WorkspaceId
  property_count: 0
  slug: airbyte-workspaceid
- name: Root Type for WorkspaceOAuthCredentials
  property_count: 3
  slug: airbyte-workspaceoauthcredentialsrequest
- name: Root Type for WorkspaceResponse
  property_count: 4
  slug: airbyte-workspaceresponse
- name: WorkspacesResponse
  property_count: 3
  slug: airbyte-workspaces-response
- name: Root Type for WorkspacesResponse
  property_count: 3
  slug: airbyte-workspacesresponse
- name: WorkspaceUpdateRequest
  property_count: 3
  slug: airbyte-workspaceupdaterequest
json_structures:
- name: Airbyte Actor Definition Id Structure
  property_count: 0
  slug: airbyte-actor-definition-id-structure
- name: Airbyte Actor Type Enum Structure
  property_count: 0
  slug: airbyte-actor-type-enum-structure
- name: Airbyte Airbyte Api Connection Schedule Structure
  property_count: 2
  slug: airbyte-airbyte-api-connection-schedule-structure
- name: Airbyte Application Create Structure
  property_count: 1
  slug: airbyte-application-create-structure
- name: Airbyte Application Read List Structure
  property_count: 1
  slug: airbyte-application-read-list-structure
- name: Airbyte Application Read Structure
  property_count: 5
  slug: airbyte-application-read-structure
- name: Airbyte Application Token Request With Grant Structure
  property_count: 3
  slug: airbyte-application-token-request-with-grant-structure
- name: Airbyte Auth Provider Structure
  property_count: 0
  slug: airbyte-auth-provider-structure
- name: Airbyte Connection Create Request Structure
  property_count: 12
  slug: airbyte-connection-create-request-structure
- name: Airbyte Connection Patch Request Structure
  property_count: 10
  slug: airbyte-connection-patch-request-structure
- name: Airbyte Connection Response Structure
  property_count: 15
  slug: airbyte-connection-response-structure
- name: Airbyte Connection Schedule Response Structure
  property_count: 3
  slug: airbyte-connection-schedule-response-structure
- name: Airbyte Connection Status Enum Structure
  property_count: 0
  slug: airbyte-connection-status-enum-structure
- name: Airbyte Connection Sync Mode Enum Structure
  property_count: 0
  slug: airbyte-connection-sync-mode-enum-structure
- name: Airbyte Connections Response Structure
  property_count: 3
  slug: airbyte-connections-response-structure
- name: Airbyte Connector Definition Response Structure
  property_count: 4
  slug: airbyte-connector-definition-response-structure
- name: Airbyte Connector Definitions Response Structure
  property_count: 1
  slug: airbyte-connector-definitions-response-structure
- name: Airbyte Connector Type Structure
  property_count: 0
  slug: airbyte-connector-type-structure
- name: Airbyte Create Declarative Source Definition Request Structure
  property_count: 2
  slug: airbyte-create-declarative-source-definition-request-structure
- name: Airbyte Create Definition Request Structure
  property_count: 4
  slug: airbyte-create-definition-request-structure
- name: Airbyte Dataplane Create Request Structure
  property_count: 3
  slug: airbyte-dataplane-create-request-structure
- name: Airbyte Dataplane Patch Request Structure
  property_count: 2
  slug: airbyte-dataplane-patch-request-structure
- name: Airbyte Dataplane Response Structure
  property_count: 6
  slug: airbyte-dataplane-response-structure
- name: Airbyte Dataplanes Response Structure
  property_count: 1
  slug: airbyte-dataplanes-response-structure
- name: Airbyte Declarative Manifest Structure
  property_count: 0
  slug: airbyte-declarative-manifest-structure
- name: Airbyte Declarative Source Definition Response Structure
  property_count: 4
  slug: airbyte-declarative-source-definition-response-structure
- name: Airbyte Declarative Source Definitions Response Structure
  property_count: 3
  slug: airbyte-declarative-source-definitions-response-structure
- name: Airbyte Definition Response Structure
  property_count: 5
  slug: airbyte-definition-response-structure
- name: Airbyte Definitions Response Structure
  property_count: 3
  slug: airbyte-definitions-response-structure
- name: Airbyte Destination Configuration Structure
  property_count: 0
  slug: airbyte-destination-configuration-structure
- name: Airbyte Destination Create Request Structure
  property_count: 5
  slug: airbyte-destination-create-request-structure
- name: Airbyte Destination Patch Request Structure
  property_count: 3
  slug: airbyte-destination-patch-request-structure
- name: Airbyte Destination Put Request Structure
  property_count: 3
  slug: airbyte-destination-put-request-structure
- name: Airbyte Destination Response Structure
  property_count: 8
  slug: airbyte-destination-response-structure
- name: Airbyte Destinations Response Structure
  property_count: 3
  slug: airbyte-destinations-response-structure
- name: Airbyte Email Notification Config Structure
  property_count: 1
  slug: airbyte-email-notification-config-structure
- name: Airbyte Embedded Organization List Item Structure
  property_count: 3
  slug: airbyte-embedded-organization-list-item-structure
- name: Airbyte Embedded Organizations List Structure
  property_count: 1
  slug: airbyte-embedded-organizations-list-structure
- name: Airbyte Embedded Scoped Token Request Structure
  property_count: 1
  slug: airbyte-embedded-scoped-token-request-structure
- name: Airbyte Embedded Scoped Token Response Structure
  property_count: 1
  slug: airbyte-embedded-scoped-token-response-structure
- name: Airbyte Embedded Widget Request Structure
  property_count: 3
  slug: airbyte-embedded-widget-request-structure
- name: Airbyte Embedded Widget Response Structure
  property_count: 1
  slug: airbyte-embedded-widget-response-structure
- name: Airbyte Encryption Mapper Aes Configuration Structure
  property_count: 6
  slug: airbyte-encryption-mapper-aes-configuration-structure
- name: Airbyte Encryption Mapper Algorithm Structure
  property_count: 0
  slug: airbyte-encryption-mapper-algorithm-structure
- name: Airbyte Encryption Mapper Configuration Structure
  property_count: 0
  slug: airbyte-encryption-mapper-configuration-structure
- name: Airbyte Encryption Mapper Rsa Configuration Structure
  property_count: 4
  slug: airbyte-encryption-mapper-rsa-configuration-structure
- name: Airbyte Field Filtering Mapper Configuration Structure
  property_count: 1
  slug: airbyte-field-filtering-mapper-configuration-structure
- name: Airbyte Field Renaming Mapper Configuration Structure
  property_count: 2
  slug: airbyte-field-renaming-mapper-configuration-structure
- name: Airbyte Group Create Request Structure
  property_count: 3
  slug: airbyte-group-create-request-structure
- name: Airbyte Group Member Add Request Structure
  property_count: 1
  slug: airbyte-group-member-add-request-structure
- name: Airbyte Group Member Response Structure
  property_count: 5
  slug: airbyte-group-member-response-structure
- name: Airbyte Group Members Response Structure
  property_count: 3
  slug: airbyte-group-members-response-structure
- name: Airbyte Group Permission Create Request Structure
  property_count: 3
  slug: airbyte-group-permission-create-request-structure
- name: Airbyte Group Permission Response Structure
  property_count: 5
  slug: airbyte-group-permission-response-structure
- name: Airbyte Group Permissions Response Structure
  property_count: 1
  slug: airbyte-group-permissions-response-structure
- name: Airbyte Group Response Structure
  property_count: 5
  slug: airbyte-group-response-structure
- name: Airbyte Group Update Request Structure
  property_count: 2
  slug: airbyte-group-update-request-structure
- name: Airbyte Groups Response Structure
  property_count: 3
  slug: airbyte-groups-response-structure
- name: Airbyte Hashing Mapper Configuration Structure
  property_count: 3
  slug: airbyte-hashing-mapper-configuration-structure
- name: Airbyte Initiate Oauth Request Structure
  property_count: 7
  slug: airbyte-initiate-oauth-request-structure
- name: Airbyte Job Create Request Structure
  property_count: 2
  slug: airbyte-job-create-request-structure
- name: Airbyte Job Response Structure
  property_count: 9
  slug: airbyte-job-response-structure
- name: Airbyte Job Status Enum Structure
  property_count: 0
  slug: airbyte-job-status-enum-structure
- name: Airbyte Job Type Enum Structure
  property_count: 0
  slug: airbyte-job-type-enum-structure
- name: Airbyte Job Type Resource Limit Structure
  property_count: 2
  slug: airbyte-job-type-resource-limit-structure
- name: Airbyte Job Type Structure
  property_count: 0
  slug: airbyte-job-type-structure
- name: Airbyte Jobs Response Structure
  property_count: 3
  slug: airbyte-jobs-response-structure
- name: Airbyte Manifest Version Structure
  property_count: 0
  slug: airbyte-manifest-version-structure
- name: Airbyte Mapper Configuration Structure
  property_count: 0
  slug: airbyte-mapper-configuration-structure
- name: Airbyte Namespace Definition Enum No Default Structure
  property_count: 0
  slug: airbyte-namespace-definition-enum-no-default-structure
- name: Airbyte Namespace Definition Enum Structure
  property_count: 0
  slug: airbyte-namespace-definition-enum-structure
- name: Airbyte Namespace Definition Type Structure
  property_count: 0
  slug: airbyte-namespace-definition-type-structure
- name: Airbyte Non Breaking Changes Preference Structure
  property_count: 0
  slug: airbyte-non-breaking-changes-preference-structure
- name: Airbyte Non Breaking Schema Updates Behavior Enum No Default Structure
  property_count: 0
  slug: airbyte-non-breaking-schema-updates-behavior-enum-no-default-structure
- name: Airbyte Non Breaking Schema Updates Behavior Enum Structure
  property_count: 0
  slug: airbyte-non-breaking-schema-updates-behavior-enum-structure
- name: Airbyte Notification Config Structure
  property_count: 2
  slug: airbyte-notification-config-structure
- name: Airbyte Notifications Config Structure
  property_count: 6
  slug: airbyte-notifications-config-structure
- name: Airbyte O Auth Configuration Structure
  property_count: 0
  slug: airbyte-o-auth-configuration-structure
- name: Airbyte O Auth Credentials Configuration Structure
  property_count: 0
  slug: airbyte-o-auth-credentials-configuration-structure
- name: Airbyte O Auth Input Configuration Structure
  property_count: 0
  slug: airbyte-o-auth-input-configuration-structure
- name: Airbyte Organization Id Structure
  property_count: 0
  slug: airbyte-organization-id-structure
- name: Airbyte Organization O Auth Credentials Request Structure
  property_count: 3
  slug: airbyte-organization-o-auth-credentials-request-structure
- name: Airbyte Organization Response Structure
  property_count: 3
  slug: airbyte-organization-response-structure
- name: Airbyte Organizations Response Structure
  property_count: 1
  slug: airbyte-organizations-response-structure
- name: Airbyte Permission Create Request Structure
  property_count: 4
  slug: airbyte-permission-create-request-structure
- name: Airbyte Permission Response Read Structure
  property_count: 5
  slug: airbyte-permission-response-read-structure
- name: Airbyte Permission Response Structure
  property_count: 5
  slug: airbyte-permission-response-structure
- name: Airbyte Permission Scope Structure
  property_count: 0
  slug: airbyte-permission-scope-structure
- name: Airbyte Permission Type Structure
  property_count: 0
  slug: airbyte-permission-type-structure
- name: Airbyte Permission Update Request Structure
  property_count: 1
  slug: airbyte-permission-update-request-structure
- name: Airbyte Permissions Response Structure
  property_count: 1
  slug: airbyte-permissions-response-structure
- name: Airbyte Public Access Token Response Structure
  property_count: 3
  slug: airbyte-public-access-token-response-structure
- name: Airbyte Public Permission Type Structure
  property_count: 0
  slug: airbyte-public-permission-type-structure
- name: Airbyte Redirect Url Response Structure
  property_count: 1
  slug: airbyte-redirect-url-response-structure
- name: Airbyte Region Create Request Structure
  property_count: 3
  slug: airbyte-region-create-request-structure
- name: Airbyte Region Patch Request Structure
  property_count: 2
  slug: airbyte-region-patch-request-structure
- name: Airbyte Region Response Structure
  property_count: 6
  slug: airbyte-region-response-structure
- name: Airbyte Regions Response Structure
  property_count: 1
  slug: airbyte-regions-response-structure
- name: Airbyte Resource Requirements Structure
  property_count: 6
  slug: airbyte-resource-requirements-structure
- name: Airbyte Row Filtering Mapper Configuration Structure
  property_count: 1
  slug: airbyte-row-filtering-mapper-configuration-structure
- name: Airbyte Row Filtering Operation Structure
  property_count: 0
  slug: airbyte-row-filtering-operation-structure
- name: Airbyte Row Filtering Operation Type Structure
  property_count: 0
  slug: airbyte-row-filtering-operation-type-structure
- name: Airbyte Schedule Type Enum Structure
  property_count: 0
  slug: airbyte-schedule-type-enum-structure
- name: Airbyte Schedule Type With Basic Enum Structure
  property_count: 0
  slug: airbyte-schedule-type-with-basic-enum-structure
- name: Airbyte Scoped Resource Requirements Structure
  property_count: 2
  slug: airbyte-scoped-resource-requirements-structure
- name: Airbyte Selected Field Info Structure
  property_count: 1
  slug: airbyte-selected-field-info-structure
- name: Airbyte Selected Fields Structure
  property_count: 0
  slug: airbyte-selected-fields-structure
- name: Airbyte Source Configuration Structure
  property_count: 0
  slug: airbyte-source-configuration-structure
- name: Airbyte Source Create Request Structure
  property_count: 6
  slug: airbyte-source-create-request-structure
- name: Airbyte Source Definition Specification Structure
  property_count: 0
  slug: airbyte-source-definition-specification-structure
- name: Airbyte Source Patch Request Structure
  property_count: 5
  slug: airbyte-source-patch-request-structure
- name: Airbyte Source Put Request Structure
  property_count: 3
  slug: airbyte-source-put-request-structure
- name: Airbyte Source Response Structure
  property_count: 8
  slug: airbyte-source-response-structure
- name: Airbyte Sources Response Structure
  property_count: 3
  slug: airbyte-sources-response-structure
- name: Airbyte Sso Config Status Structure
  property_count: 0
  slug: airbyte-sso-config-status-structure
- name: Airbyte Stream Configuration Structure
  property_count: 9
  slug: airbyte-stream-configuration-structure
- name: Airbyte Stream Configurations Structure
  property_count: 1
  slug: airbyte-stream-configurations-structure
- name: Airbyte Stream Mapper Type Structure
  property_count: 0
  slug: airbyte-stream-mapper-type-structure
- name: Airbyte Stream Properties Response Structure
  property_count: 0
  slug: airbyte-stream-properties-response-structure
- name: Airbyte Stream Properties Structure
  property_count: 7
  slug: airbyte-stream-properties-structure
- name: Airbyte Structure
  property_count: 0
  slug: airbyte-structure
- name: Airbyte Tag Create Request Structure
  property_count: 3
  slug: airbyte-tag-create-request-structure
- name: Airbyte Tag Id Structure
  property_count: 0
  slug: airbyte-tag-id-structure
- name: Airbyte Tag Patch Request Structure
  property_count: 2
  slug: airbyte-tag-patch-request-structure
- name: Airbyte Tag Response Structure
  property_count: 4
  slug: airbyte-tag-response-structure
- name: Airbyte Tag Structure
  property_count: 4
  slug: airbyte-tag-structure
- name: Airbyte Tags Response Structure
  property_count: 1
  slug: airbyte-tags-response-structure
- name: Airbyte Update Declarative Source Definition Request Structure
  property_count: 1
  slug: airbyte-update-declarative-source-definition-request-structure
- name: Airbyte Update Definition Request Structure
  property_count: 2
  slug: airbyte-update-definition-request-structure
- name: Airbyte User Id Structure
  property_count: 0
  slug: airbyte-user-id-structure
- name: Airbyte User Response Structure
  property_count: 3
  slug: airbyte-user-response-structure
- name: Airbyte User Status Structure
  property_count: 0
  slug: airbyte-user-status-structure
- name: Airbyte Users Response Structure
  property_count: 1
  slug: airbyte-users-response-structure
- name: Airbyte Webhook Notification Config Structure
  property_count: 2
  slug: airbyte-webhook-notification-config-structure
- name: Airbyte Workspace Create Request Structure
  property_count: 4
  slug: airbyte-workspace-create-request-structure
- name: Airbyte Workspace Id Structure
  property_count: 0
  slug: airbyte-workspace-id-structure
- name: Airbyte Workspace O Auth Credentials Request Structure
  property_count: 3
  slug: airbyte-workspace-o-auth-credentials-request-structure
- name: Airbyte Workspace Response Structure
  property_count: 4
  slug: airbyte-workspace-response-structure
- name: Airbyte Workspace Update Request Structure
  property_count: 3
  slug: airbyte-workspace-update-request-structure
- name: Airbyte Workspaces Response Structure
  property_count: 3
  slug: airbyte-workspaces-response-structure
jsonld:
- class_count: 108
  name: Airbyte Context
  property_count: 129
  slug: airbyte-context
layout: provider
mcp_servers:
- description: ''
  name: Airbyte MCP Server
  slug: airbyte-mcp-server
modified: '2026-06-20'
name: Airbyte
nav: Providers
network: true
overview: 'Airbyte publishes 24 APIs on the [APIs.io](https://apis.io/) network, including public API, public_applications API, public_connections API, and 21 more. Tagged areas include Data Integration, ETL, ELT, Open-Source, and Data Pipeline.


  The Airbyte catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Airbyte''s developer surface includes authentication, changelog, CLI, developer portal, developer console, signup flow, pricing, and 49 more developer resources.'
plans:
- name: Airbyte Plans Pricing
  plan_count: 5
  slug: airbyte-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Airbyte Rate Limits
  slug: airbyte-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Airbyte API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: airbyte-jsonschema-spectral-rules
- effective_rule_count: 75
  extends:
  - spectral:oas
  name: Airbyte API Rules
  rule_count: 34
  severity_counts:
    error: 9
    hint: 0
    info: 8
    warn: 17
  slug: airbyte-spectral-rules
scopes:
- name: Airbyte Scopes
  scope_count: 2
  slug: airbyte-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: exemplar
  composite: 66.6
  coverage:
    artifact_dirs: 34
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 33.3
    contract_quality: 62.2
    developer_ergonomics: 96.4
    discoverability: 75.9
    governance: 33.3
    operational_transparency: 50.0
  previous_composite: 66.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/screenshots/airbyte-2026-06-20T171421.png
security:
- kind: authentication
  name: Airbyte Authentication
  slug: airbyte-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Airbyte Domain Security
  slug: airbyte-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Airbyte Vulnerability Disclosure
  slug: airbyte-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Airbyte Trust Center
  slug: airbyte-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: airbyte
tags:
- Data Integration
- ETL
- ELT
- Open-Source
- Data Pipeline
- Connectors
- Data
use_cases:
- description: Sync operational data to Snowflake, BigQuery, Redshift, or other warehouses.
  name: Data Warehouse Loading
- description: Land raw data into S3, GCS, or Azure data lakes.
  name: Data Lake Ingestion
- description: Build ELT pipelines for business intelligence and analytics.
  name: Analytics Pipelines
- description: Aggregate training data from multiple sources for machine learning.
  name: AI/ML Data Preparation
- description: Pull data from SaaS APIs (Salesforce, HubSpot, Stripe) into your data stack.
  name: API Data Sync
- description: Replicate relational databases with CDC change data capture.
  name: Database Replication
- description: Load and embed data into vector stores for AI search and retrieval.
  name: Vector Database Population
website: https://airbyte.com
---
