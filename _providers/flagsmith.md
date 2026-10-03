---
access_model:
  confidence: high
  label: Freemium · Self-serve signup · 14-day trial on paid tiers
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.2
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 401
  human_in_the_loop: 8
  name: Flagsmith Agentic Access
  operation_count: 650
  slug: flagsmith-agentic-access
  summary_line: 650 operations · 401 acting · 8 human-in-the-loop
api_count: 2
apis:
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: The Flagsmith Flags API is the public-facing REST API that client-side and server-side SDKs use to retrieve feature flag values and remote configuration for environments and users. It uses a non-secre
  name: Flagsmith Flags API
  phrasing_intents:
  - id: listFlags
    intent: Get all flags for an environment
    question: How does a client SDK fetch every flag and its value for an environment in Flagsmith?
  phrasing_ops: 1
  slug: flags-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Manage environments within a project. Environments represent deployment stages such as development, staging, and production.
  name: flagsmith Environments API
  phrasing_intents:
  - id: listEnvironments
    intent: List environments I can access
    question: Which Flagsmith environments do I have access to?
  - id: getEnvironment
    intent: Get an environment (unversioned path)
    question: What project and feature states belong to an environment, from the unversioned endpoint?
  - id: updateEnvironment
    intent: Update an environment (unversioned path)
    question: Can I rename an environment through the unversioned update endpoint?
  - id: api_v1_environments_create
    intent: Create an environment in a project
    question: How do I add a new staging environment to my project?
  - id: api_v1_environments_retrieve
    intent: Get an environment's settings (v1)
    question: What settings like banner text or versioning does an environment have in the v1 API?
  - id: api_v1_environments_update
    intent: Replace an environment's settings (v1)
    question: How do I fully replace an environment's configuration with the v1 API?
  - id: api_v1_environments_partial_update
    intent: Change individual environment settings
    question: Can I just set a banner colour on an environment without touching other settings?
  - id: api_v1_environments_destroy
    intent: Delete an environment
    question: How do I remove an environment I no longer use?
  phrasing_ops: 61
  slug: flagsmith-environments-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Manage feature flags within a project. Features can be toggled on or off and can have remote configuration values.
  name: flagsmith Features API
  phrasing_intents:
  - id: listFeatures
    intent: List a project's feature flags
    question: What feature flags are defined in my Flagsmith project?
  - id: createFeature
    intent: Create a feature flag
    question: How do I add a new feature flag that shows up in every environment?
  - id: getFeature
    intent: Get a feature flag's details
    question: How is a specific feature flag configured, including its multivariate options?
  - id: updateFeature
    intent: Replace a feature flag (unversioned path)
    question: How do I rename a feature flag or change its type with a full update?
  - id: deleteFeature
    intent: Delete a feature flag (unversioned path)
    question: How do I permanently remove a feature flag from all environments using the unversioned route?
  - id: listFeatureStates
    intent: List feature states in an environment
    question: Which flags are on or off in my production environment and with what values?
  - id: updateFeatureState
    intent: Toggle a flag or change its value in an environment
    question: How do I turn a flag on in just one environment?
  - id: api_v1_environments_features_versions_destroy
    intent: Delete a feature version in an environment
    question: Can I delete a specific version of a feature's state in an environment?
  phrasing_ops: 41
  slug: flagsmith-features-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Manage user identities within an environment. Identities represent individual users and their associated traits.
  name: flagsmith Identities API
  phrasing_intents:
  - id: listIdentities
    intent: List identities in an environment
    question: Which users have identities in this environment, via the endpoint without the /api/v1 prefix?
  - id: getIdentity
    intent: Get an identity and its traits
    question: What traits does a given identity have, fetched from the non-v1 identity path?
  - id: deleteIdentity
    intent: Permanently delete an identity
    question: Does deleting an identity also wipe its traits and flag overrides?
  - id: api_v1_environments_edge_identities_list
    intent: List edge identities in an environment
    question: Which edge identities exist in an environment?
  - id: api_v1_environments_edge_identities_create
    intent: Create an edge identity
    question: Can I create an edge identity with a friendly dashboard alias?
  - id: api_v1_environments_edge_identities_edge_featurestates_list
    intent: List an edge identity's flag overrides
    question: Which flags have been overridden for a specific edge identity?
  - id: api_v1_environments_edge_identities_edge_featurestates_create
    intent: Override a flag for an edge identity
    question: How do I give one edge identity its own value for a flag?
  - id: api_v1_environments_edge_identities_edge_featurestates_retrieve
    intent: Get one edge identity flag override
    question: What value does a specific edge identity override currently hold?
  phrasing_ops: 47
  slug: flagsmith-identities-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Manage organisations within Flagsmith. Organisations are the top-level container for projects, users, and billing.
  name: flagsmith Organisations API
  phrasing_intents:
  - id: listOrganisations
    intent: List the organisations I belong to
    question: Which Flagsmith organisations does my account have access to?
  - id: getOrganisation
    intent: Get an organisation's plan and usage limits
    question: What subscription plan and feature usage limits does my organisation have?
  - id: api_v1_organisations_create
    intent: Create a new organisation
    question: How do I create a brand-new organisation under my account?
  - id: api_v1_organisations_licence_update
    intent: Upload or replace an organisation's licence
    question: Where do I apply a self-hosted licence to my organisation?
  - id: api_v1_organisations_api_usage_notification_list
    intent: List API usage notifications for an organisation
    question: Has my organisation been warned about approaching its API request limit?
  - id: api_v1_organisations_github_create_cleanup_issue_create
    intent: Open a GitHub issue to clean up stale flags
    question: Can Flagsmith open a GitHub issue reminding us to remove an old flag from code?
  - id: api_v1_organisations_github_issues_retrieve
    intent: List GitHub issues from the linked integration
    question: Which GitHub issues can I link to a feature flag?
  - id: api_v1_organisations_github_pulls_retrieve
    intent: List GitHub pull requests from the integration
    question: What pull requests from our GitHub repos can be linked to a flag?
  phrasing_ops: 106
  slug: flagsmith-organisations-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Manage projects within an organisation. Projects contain environments and feature flags.
  name: flagsmith Projects API
  phrasing_intents:
  - id: listProjects
    intent: List projects I can access across organisations
    question: Which Flagsmith projects do I have access to across all my organisations?
  - id: createProject
    intent: Create a project with just a name and organisation
    question: What is the minimum I need to create a project that will hold environments and flags?
  - id: getProject
    intent: Get a project's details
    question: How do I see a project's name, organisation and environments?
  - id: updateProject
    intent: Rename or replace a project's details
    question: How do I rename an existing project?
  - id: deleteProject
    intent: Permanently delete a project and everything in it
    question: What gets wiped when I permanently delete a project and all its environments and flags?
  - id: api_v1_projects_list
    intent: List projects via the v1 API
    question: How do I list projects through the versioned v1 projects API?
  - id: api_v1_projects_create
    intent: Create a project with its settings
    question: Can I create a project that enforces lower-case feature names or a naming regex?
  - id: api_v1_projects_partial_update
    intent: Change a project's settings
    question: How do I change the stale flag threshold on a project?
  phrasing_ops: 46
  slug: flagsmith-projects-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Manage segments within a project. Segments define groups of users based on traits and rules for targeted flag delivery.
  name: flagsmith Segments API
  phrasing_intents:
  - id: listSegments
    intent: List a project's segments
    question: Which user segments are defined in my project?
  - id: createSegment
    intent: Create a segment from trait rules
    question: How do I create a segment of users based on trait rules for targeted flags?
  - id: getSegment
    intent: Get a segment's rules and conditions
    question: What rules and conditions make up a particular segment?
  - id: updateSegment
    intent: Replace a segment's name, description and rules
    question: How do I rewrite the full rule set of an existing segment?
  - id: deleteSegment
    intent: Permanently delete a segment
    question: What happens to segment overrides when I delete a segment?
  - id: api_v1_projects_segments_partial_update
    intent: Change some fields on a segment
    question: Can I change just a segment's description without resending its rules?
  - id: api_v1_projects_segments_destroy
    intent: Delete a segment via the v1 project endpoint
    question: Is there a v1 API path under /api/v1/projects for deleting a segment?
  - id: api_v1_projects_segments_associated_features_retrieve
    intent: See which features a segment is used by
    question: Which features have overrides that depend on this segment?
  phrasing_ops: 11
  slug: flagsmith-segments-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Manage organisation users and their permissions within Flagsmith.
  name: flagsmith Users API
  phrasing_intents:
  - id: listOrganisationUsers
    intent: List users in an organisation
    question: Who are the members of my Flagsmith organisation?
  phrasing_ops: 1
  slug: flagsmith-users-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Configure webhooks for environments and organisations to receive notifications about flag changes and audit log events.
  name: flagsmith Webhooks API
  phrasing_intents:
  - id: listEnvironmentWebhooks
    intent: List environment webhooks (unversioned path)
    question: Which webhooks receive flag evaluation data for identified users in my environment, via the unversioned path?
  - id: createEnvironmentWebhook
    intent: Add an environment webhook (unversioned path)
    question: How can I get flag evaluation data POSTed to my URL whenever identities are evaluated?
  - id: listOrganisationWebhooks
    intent: List organisation audit webhooks (unversioned)
    question: Which webhooks receive audit log events for my whole organisation, from the unversioned path?
  - id: createOrganisationWebhook
    intent: Add an organisation audit webhook (unversioned)
    question: How do I stream audit log events for changes across my organisation to my own URL?
  - id: api_v1_cb_webhook_create
    intent: Receive Chargebee subscription webhooks
    question: What endpoint handles incoming Chargebee billing webhooks for subscription changes?
  - id: api_v1_cohort_sync_mixpanel_webhook_create
    intent: Receive a Mixpanel cohort sync
    question: How does Mixpanel push cohort membership into Flagsmith each sync cycle?
  - id: api_v1_cohort_sync_webhook_cohorts_members_add_create
    intent: Add members to a CSV cohort
    question: How do I add identities to an existing CSV cohort without re-uploading the file?
  - id: api_v1_cohort_sync_webhook_cohorts_members_remove_create
    intent: Remove members from a CSV cohort
    question: How can I take specific identities out of a CSV cohort?
  phrasing_ops: 21
  slug: flagsmith-webhooks-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Platform hub admin dashboard endpoints.
  name: Flagsmith Admin dashboard API
  phrasing_intents:
  - id: api_v1_admin_dashboard_organisations_retrieve
    intent: Review organisations on the admin dashboard
    question: Which organisations exist on my self-hosted Flagsmith instance?
  - id: api_v1_admin_dashboard_release_pipelines_retrieve
    intent: Review release pipelines on the admin dashboard
    question: What release pipelines are configured across the whole instance?
  - id: api_v1_admin_dashboard_stale_flags_retrieve
    intent: Find stale flags across the instance
    question: Which feature flags have gone stale and could be cleaned up?
  - id: api_v1_admin_dashboard_summary_retrieve
    intent: Get the admin dashboard summary
    question: What are the headline numbers for my Flagsmith instance?
  - id: api_v1_admin_dashboard_usage_trends_retrieve
    intent: See usage trends on the admin dashboard
    question: How has API usage on the instance trended over time?
  phrasing_ops: 5
  slug: flagsmith-admin-dashboard-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: SDK analytics and telemetry.
  name: Flagsmith Analytics API
  phrasing_intents:
  - id: api_v1_analytics_flags_create
    intent: Report flag evaluation analytics (v1)
    question: Where does an SDK send flag analytics events on the original v1 endpoint?
  - id: api_v1_analytics_telemetry_create
    intent: Send self-hosted installation telemetry
    question: How does a self-hosted Flagsmith install report its telemetry?
  - id: api_v2_analytics_flags_create
    intent: Report flag evaluations (v2)
    question: Can I submit a list of flag evaluations to the v2 analytics endpoint?
  phrasing_ops: 3
  slug: flagsmith-analytics-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Access audit logs.
  name: Flagsmith Audit API
  phrasing_intents:
  - id: api_v1_audit_list
    intent: Search the audit log across everything I can see
    question: Who changed what across all my Flagsmith projects recently?
  - id: api_v1_audit_retrieve
    intent: Get one audit log entry by ID
    question: Can I pull up the full detail of a single audit log record?
  - id: api_v1_organisations_audit_list
    intent: List an organisation's audit log
    question: How do I see the audit trail for everything in one organisation?
  - id: api_v1_organisations_audit_retrieve
    intent: Get an audit entry within an organisation
    question: Can I look up one audit record scoped to a specific organisation?
  - id: api_v1_projects_audit_list
    intent: List a project's audit log
    question: What changes have been made inside one project lately?
  - id: api_v1_projects_audit_retrieve
    intent: Get an audit entry within a project
    question: How do I open a single audit record that belongs to one project?
  phrasing_ops: 6
  slug: flagsmith-audit-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Authentication, MFA, OAuth, and token management.
  name: Flagsmith Authentication API
  phrasing_intents:
  - id: api_v1_auth_activate_create
    intent: Start enabling a two-factor method
    question: How do I begin turning on two-factor authentication for my account?
  - id: api_v1_auth_activate_confirm_create
    intent: Confirm a two-factor method setup
    question: What is the final step to finish enabling two-factor authentication?
  - id: api_v1_auth_deactivate_create
    intent: Turn off a two-factor method
    question: Can I disable two-factor authentication on my account?
  - id: api_v1_auth_login_create
    intent: Log in with email and password
    question: How do I get an auth token by logging in with my email and password?
  - id: api_v1_auth_login_code_create
    intent: Complete login with a two-factor code
    question: After my password, where do I submit the second-factor login code?
  - id: api_v1_auth_logout_create
    intent: Log out and remove my auth token
    question: How do I log out so my auth token stops working?
  - id: api_v1_auth_mfa_user_active_methods_retrieve
    intent: List my active two-factor methods
    question: Which two-factor methods are currently switched on for my account?
  - id: api_v1_auth_oauth_github_create
    intent: Sign in with GitHub
    question: Can I log in or sign up using my GitHub account?
  phrasing_ops: 59
  slug: flagsmith-authentication-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Experimental endpoints subject to change.
  name: Flagsmith Experimental API
  phrasing_intents:
  - id: api___future___environments_features_retrieve
    intent: See what a flag serves in an environment
    question: What value and on/off state does a flag currently serve in production?
  - id: api___future___environments_features_update
    intent: Replace a flag's environment configuration
    question: Can I reset a flag's whole setup in an environment, dropping overrides I don't resend?
  - id: api___future___environments_features_partial_update
    intent: Adjust part of a flag's environment configuration
    question: Can I change only a flag's environment default and keep its segment overrides as they are?
  - id: api___future___environments_features_segment_overrides_destroy
    intent: Remove a flag's override for one segment
    question: How do I drop one segment's special value for a flag without touching the rest?
  - id: api_experiments_environments_delete_segment_override_create
    intent: Delete a segment override via the experimental endpoint
    question: Can I delete a segment override by passing the feature name instead of its id?
  - id: api_experiments_environments_update_flag_v1_create
    intent: Update a single feature state
    question: How can I switch one flag on and set its value in an environment in a single call?
  - id: api_experiments_environments_update_flag_v2_create
    intent: Configure a flag's default and overrides at once
    question: Can I set a flag's environment default and all its segment overrides in one request?
  phrasing_ops: 7
  slug: flagsmith-experimental-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Manage feature states and feature versioning.
  name: Flagsmith Feature states API
  phrasing_intents:
  - id: api_v1_environment_feature_versions_retrieve
    intent: Get an environment feature version by ID
    question: Can I look up a feature version without knowing its environment or feature?
  - id: api_v1_environments_featurestates_list
    intent: List feature states in an environment
    question: How do I see every flag state set in one environment using its environment key?
  - id: api_v1_environments_featurestates_create
    intent: Create a feature state via the deprecated environment path
    question: Is there still an environment-scoped endpoint for creating feature states, even though it is deprecated?
  - id: api_v1_environments_featurestates_retrieve
    intent: Get one feature state in an environment
    question: How do I read a single feature state inside an environment by its ID?
  - id: api_v1_environments_featurestates_partial_update
    intent: Toggle a feature state in an environment
    question: How do I switch a flag on or off in an environment using its environment key?
  - id: api_v1_environments_featurestates_destroy
    intent: Delete a feature state from an environment
    question: How do I remove a feature state from an environment by its environment key?
  - id: api_v1_environments_features_versions_featurestates_partial_update
    intent: Edit a feature state inside a feature version
    question: How do I change the value of a feature state within a versioned feature change?
  - id: api_v1_environments_features_versions_featurestates_destroy
    intent: Delete a feature state from a feature version
    question: How do I remove a feature state from a specific versioned change of a feature?
  phrasing_ops: 17
  slug: flagsmith-feature-states-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Configure third-party integrations (Amplitude, DataDog, Slack, etc.).
  name: Flagsmith Integrations API
  phrasing_intents:
  - id: api_v1_admin_dashboard_integrations_retrieve
    intent: See integration usage on the admin dashboard
    question: Which third-party integrations are switched on across my whole Flagsmith instance?
  - id: api_v1_environments_integrations_amplitude_list
    intent: List Amplitude integrations for an environment
    question: Is Amplitude already connected to this environment?
  - id: api_v1_environments_integrations_amplitude_create
    intent: Connect Amplitude to an environment
    question: How do I send flag data from an environment into Amplitude?
  - id: api_v1_environments_integrations_amplitude_retrieve
    intent: Get one Amplitude integration's settings
    question: What base URL is my Amplitude integration currently sending to?
  - id: api_v1_environments_integrations_amplitude_update
    intent: Replace an Amplitude integration's settings
    question: Can I overwrite the full Amplitude config, key and URL together, in one call?
  - id: api_v1_environments_integrations_amplitude_partial_update
    intent: Change one Amplitude integration setting
    question: Can I rotate just the Amplitude API key without touching anything else?
  - id: api_v1_environments_integrations_amplitude_destroy
    intent: Disconnect Amplitude from an environment
    question: How can I stop an environment from sending data to Amplitude?
  - id: api_v1_environments_integrations_dynatrace_list
    intent: List Dynatrace integrations for an environment
    question: Does this environment already push flag changes to Dynatrace?
  phrasing_ops: 107
  slug: flagsmith-integrations-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: MCP-compatible endpoints.
  name: Flagsmith MCP API
  phrasing_intents:
  - id: list_environments
    intent: List environments I can access
    question: Which Flagsmith environments does my account have access to?
  - id: create_environment_feature_change_request
    intent: Open a change request for flag changes
    question: How do I propose a flag change for approval instead of applying it directly?
  - id: list_metrics
    intent: List experiment metrics in an environment
    question: What experiment metrics are defined for this environment?
  - id: create_metric
    intent: Define a new experiment metric
    question: How do I define a metric to measure an experiment against?
  - id: get_metric
    intent: Get an experiment metric's details
    question: Which experiments are using a particular metric?
  - id: update_metric
    intent: Update an experiment metric
    question: Can I change the event definition of an existing experiment metric?
  - id: list_experiments
    intent: List experiments in an environment
    question: Which experiments are currently running in this environment?
  - id: create_experiment
    intent: Start an experiment on a multivariate feature
    question: How do I set up an A/B experiment on a multivariate flag?
  phrasing_ops: 54
  slug: flagsmith-mcp-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Manage metadata fields and model configuration.
  name: Flagsmith Metadata API
  phrasing_intents:
  - id: api_v1_auth_saml_metadata_retrieve
    intent: Download SAML service provider metadata
    question: Where do I get the SAML metadata to give my identity provider?
  - id: api_v1_metadata_fields_list
    intent: List an organisation's custom metadata fields
    question: What custom metadata fields has my organisation defined?
  - id: api_v1_metadata_fields_create
    intent: Define a new custom metadata field
    question: How do I add a custom field such as a Jira ticket URL to my flags?
  - id: api_v1_metadata_fields_retrieve
    intent: Get one metadata field definition
    question: What type and description does a given metadata field have?
  - id: api_v1_metadata_fields_update
    intent: Replace a metadata field definition
    question: Can I redefine a metadata field completely in one update?
  - id: api_v1_metadata_fields_partial_update
    intent: Edit part of a metadata field
    question: Can I just rename a metadata field?
  - id: api_v1_metadata_fields_destroy
    intent: Delete a metadata field
    question: How do I remove a custom metadata field we no longer use?
  - id: api_v1_projects_metadata_fields_list
    intent: List metadata fields available to a project
    question: Which custom fields can I fill in on a project's features?
  phrasing_ops: 9
  slug: flagsmith-metadata-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: The o API from Flagsmith — 1 operation(s) for o.
  name: Flagsmith O API
  phrasing_intents:
  - id: o_register_create
    intent: Register an OAuth client dynamically
    question: Does Flagsmith support RFC 7591 dynamic client registration for OAuth?
  phrasing_ops: 1
  slug: flagsmith-o-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Onboarding flows.
  name: Flagsmith Onboarding API
  phrasing_intents:
  - id: api_v1_onboarding_request_receive_create
    intent: Submit an onboarding request
    question: Can I ask the Flagsmith team for onboarding help through the API?
  phrasing_ops: 1
  slug: flagsmith-onboarding-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Other endpoints.
  name: Flagsmith Other API
  phrasing_intents:
  - id: api_v1_cohort_sync_amplitude_lists_create
    intent: Create a cohort list for an Amplitude cohort sync
    question: How does an Amplitude cohort sync get a list ID in Flagsmith when it is first set up?
  - id: api_v1_cohort_sync_amplitude_lists_add_create
    intent: Add users to a synced Amplitude cohort list
    question: How do users get added to a cohort that is synced from Amplitude?
  - id: api_v1_cohort_sync_amplitude_lists_remove_create
    intent: Remove users from a synced Amplitude cohort list
    question: How are users taken out of a cohort that is synced from Amplitude?
  - id: api_v1_gitlab_webhook_create
    intent: Receive a GitLab webhook event
    question: Where does GitLab send webhook events for the Flagsmith GitLab integration?
  - id: api_v1_oauth_authorize_retrieve
    intent: Validate an OAuth authorisation request
    question: How do I check that an OAuth authorisation request is valid before showing a consent screen?
  - id: api_v1_oauth_authorize_create
    intent: Submit an OAuth consent decision
    question: How do I record a user's approval or denial on the OAuth consent screen?
  phrasing_ops: 6
  slug: flagsmith-other-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Manage user and group permissions across organisations, projects, and environments.
  name: Flagsmith Permissions API
  phrasing_intents:
  - id: api_v1_environments_user_group_permissions_list
    intent: List group permissions on an environment
    question: Which user groups have access to this environment?
  - id: api_v1_environments_user_group_permissions_create
    intent: Grant a group access to an environment
    question: How do I give a whole team permissions on one environment?
  - id: api_v1_environments_user_group_permissions_retrieve
    intent: Get one group's environment permission grant
    question: What exactly can a given group do in this environment?
  - id: api_v1_environments_user_group_permissions_update
    intent: Replace a group's environment permissions
    question: Can I overwrite the full set of rights a team has on an environment?
  - id: api_v1_environments_user_group_permissions_partial_update
    intent: Adjust part of a group's environment grant
    question: Can I just toggle admin on a group's environment grant?
  - id: api_v1_environments_user_group_permissions_destroy
    intent: Revoke a group's environment access
    question: How do I take a team's access away from an environment?
  - id: api_v1_environments_user_permissions_list
    intent: List user permissions on an environment
    question: Which individual users have direct access to this environment?
  - id: api_v1_environments_user_permissions_create
    intent: Grant a user access to an environment
    question: How do I give one person permissions on a single environment?
  phrasing_ops: 34
  slug: flagsmith-permissions-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: The processor API from Flagsmith — 1 operation(s) for processor.
  name: Flagsmith Processor API
  phrasing_intents:
  - id: processor_monitoring_retrieve
    intent: Check the task processor's monitoring status
    question: Is the Flagsmith background task processor healthy right now?
  phrasing_ops: 1
  slug: flagsmith-processor-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: SDK endpoints for flags, identities, and traits.
  name: Flagsmith SDK API
  phrasing_intents:
  - id: sdk_v1_environment_document
    intent: Download the environment document for local evaluation
    question: How do I get the full environment document my SDK needs for local evaluation mode?
  - id: sdk_v1_flags
    intent: Get the feature flags for an environment
    question: Which feature flags are on in this environment right now?
  - id: sdk_v1_flags_2
    intent: Get flags for an identifier (deprecated path)
    question: Can I still fetch flags with the identifier in the URL path of the flags endpoint?
  - id: sdk_v1_get_identities
    intent: Get an identity's flags and traits
    question: How do I read the flags and traits a specific user sees without changing anything?
  - id: sdk_v1_post_identities
    intent: Identify a user, set traits and get their flags
    question: Can I set a user's traits and get their flags back in the same call?
  phrasing_ops: 5
  slug: flagsmith-sdk-api
artifact_total: 50
asyncapis:
- description: Flagsmith provides two types of webhooks for receiving event notifications. Environment webhooks automatically send flag evaluations for identified users whenever an identity's flags are evaluated via
  name: Flagsmith Webhook Events
  slug: flagsmith-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flagsmith Admin API
  slug: open-flagsmith-admin-api
- collection_type: open
  name: Flagsmith Admin Environments API
  slug: open-flagsmith-environments-api
- collection_type: open
  name: Flagsmith Admin Environments Features API
  slug: open-flagsmith-features-api
- collection_type: open
  name: Flagsmith Admin Environments Flags API
  slug: open-flagsmith-flags-api
- collection_type: open
  name: Flagsmith Admin Environments Identities API
  slug: open-flagsmith-identities-api
- collection_type: open
  name: Flagsmith Admin Environments Organisations API
  slug: open-flagsmith-organisations-api
- collection_type: open
  name: Flagsmith Admin Environments Projects API
  slug: open-flagsmith-projects-api
- collection_type: open
  name: Flagsmith Admin Environments Segments API
  slug: open-flagsmith-segments-api
- collection_type: open
  name: Flagsmith Admin Environments Users API
  slug: open-flagsmith-users-api
- collection_type: open
  name: Flagsmith Admin Environments Webhooks API
  slug: open-flagsmith-webhooks-api
common:
- group: company
  title: ''
  type: Website
  url: https://flagsmith.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/agentic-access/flagsmith-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flagsmith-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/security/flagsmith-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flagsmith-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/authentication/flagsmith-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flagsmith-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Flagsmith
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flagsmith
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/json-ld/flagsmith-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/flagsmith-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/json-schema/flagsmith-feature-flag-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/flagsmith-feature-flag-schema.json
- group: company
  title: ''
  type: Blog
  url: https://flagsmith.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.flagsmith.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flagsmith.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.flagsmith.com/integrating-with-flagsmith/flagsmith-api-overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.flagsmith.com/getting-started/quick-start
- group: operate
  title: ''
  type: Support
  url: https://docs.flagsmith.com/support/faq
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/hFhxNtXzgm
- group: commercial
  title: ''
  type: Pricing
  url: https://flagsmith.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.flagsmith.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flagsmith.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flagsmith.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/flagsmith/workspace/flagsmith/overview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flagsmith.com
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/changelog/flagsmith-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/flagsmith-changelog.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/lifecycle/flagsmith-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/flagsmith-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/lifecycle/flagsmith-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/flagsmith-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/packages/flagsmith-packages.yml
  title: ''
  type: Packages
  url: packages/flagsmith-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/packages/flagsmith-packages.yml
  title: ''
  type: SDKs
  url: packages/flagsmith-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/cli/flagsmith-cli.yml
  title: ''
  type: CLI
  url: cli/flagsmith-cli.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/sandbox/flagsmith-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/flagsmith-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/mcp/flagsmith-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/flagsmith-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/mcp/flagsmith-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/flagsmith-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/llms/flagsmith-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flagsmith-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/well-known/flagsmith-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flagsmith-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/scopes/flagsmith-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/flagsmith-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/conventions/flagsmith-conventions.yml
  title: ''
  type: Conventions
  url: conventions/flagsmith-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/errors/flagsmith-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/flagsmith-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/rate-limits/flagsmith-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/flagsmith-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/plans/flagsmith-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flagsmith-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/data-model/flagsmith-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flagsmith-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/conformance/flagsmith-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flagsmith-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/security/flagsmith-trust-center.yml
  title: ''
  type: Compliance
  url: security/flagsmith-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/security/flagsmith-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/flagsmith-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/security/flagsmith-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/flagsmith-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/security/flagsmith-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/flagsmith-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/asyncapi/flagsmith-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/flagsmith-webhooks-asyncapi.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/finops/flagsmith-finops.yml
  title: ''
  type: FinOps
  url: finops/flagsmith-finops.yml
created: '2026-05-03'
description: 'Flagsmith is an open-source feature flag, remote configuration and experimentation platform built by Bullet Train Ltd. Teams use it to release features safely, run A/B and multivariate tests, and segment users without redeploying code, across web, mobile and server-side applications. It ships as a hosted cloud service on a global low-latency Edge API, as a private cloud deployment, or self-hosted on the customer''s own infrastructure, with the core product open source under BSD-3-Clause. Two public API surfaces back it: a non-secret SDK/Flags API for evaluating flags, and a 615-operation Management API that does everything the dashboard does. Flagsmith is OpenFeature compatible, publishes first-party SDKs for thirteen language ecosystems, and operates a remote MCP server exposing 54 tools to AI agents over OAuth.'
finops:
- name: Flagsmith Finops
  service_category: API
  slug: flagsmith-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flagsmith.png
json_schemas:
- name: Flagsmith Feature Flag
  property_count: 12
  slug: flagsmith-feature-flag
jsonld:
- class_count: 0
  name: Flagsmith Context
  property_count: 9
  slug: flagsmith-context
layout: provider
mcp_servers:
- description: ''
  name: Flagsmith MCP Server
  slug: flagsmith-mcp-server
modified: '2026-09-17'
name: Flagsmith
nav: Providers
network: true
overview: 'Flagsmith publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Flags API, Environments API, Features API, and 21 more. Tagged areas include Feature Flags, Remote Config, Release Management, A/B Testing, and Experimentation.


  The Flagsmith catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Flagsmith''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, pricing, and 39 more developer resources.'
plans:
- name: Flagsmith Plans Pricing
  plan_count: 4
  slug: flagsmith-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Flagsmith Rate Limits
  slug: flagsmith-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Flagsmith API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: flagsmith-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Flagsmith API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: flagsmith-jsonschema-spectral-rules
scopes:
- name: Flagsmith Scopes
  scope_count: 0
  slug: flagsmith-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 78.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 73.5
    catalog_earned_first_party: 24.0
    catalog_gap: 41.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 56.9
    developer_ergonomics: 79.2
    discoverability: 75.0
    operational_transparency: 92.1
  previous_composite: 80.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 37.5
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/screenshots/flagsmith-2026-06-20T181306.png
security:
- kind: authentication
  name: Flagsmith Authentication
  slug: flagsmith-authentication
  summary_line: apiKey/http/oauth2 · 7 schemes
- kind: domain-security
  name: Flagsmith Domain Security
  slug: flagsmith-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flagsmith Vulnerability Disclosure
  slug: flagsmith-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Flagsmith Trust Center
  slug: flagsmith-trust-center
  summary_line: read, note, how_to_verify
slug: flagsmith
tags:
- Feature Flags
- Remote Config
- Release Management
- A/B Testing
- Experimentation
- Segmentation
- Developer Tools
- DevOps
- Open Source
- Software-as-a-Service
- MCP
- Agent Ready
website: https://flagsmith.com
---
