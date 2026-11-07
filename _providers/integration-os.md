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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Manage connection access restrictions
  name: IntegrationOS Access API
  phrasing_intents:
  - id: revoke_project_connection_access
    intent: Clear all restrictions from a project key
    question: How do I remove every connection restriction from a project-level access key?
  - id: read_project_connection_access
    intent: View a project key's connection restrictions
    question: What connection restrictions are set on a project-level access key?
  - id: update_project_connection_access
    intent: Set connection restrictions on a project key
    question: How do I limit a project access key to certain connections or HTTP methods?
  - id: revoke_organization_connection_access
    intent: Clear all restrictions from an org key
    question: How do I strip every connection restriction from an organization-level key?
  - id: read_organization_connection_access
    intent: View an org key's connection restrictions
    question: Which connection restrictions apply to an organization-level access key?
  - id: update_organization_connection_access
    intent: Set connection restrictions on an org key
    question: How do I restrict an organization-level key to specific connections?
  - id: revoke_connection_access
    intent: Clear all restrictions from my personal key
    question: How do I give my own user key unrestricted access to every connection again?
  - id: read_connection_access
    intent: View my personal key's connection restrictions
    question: What restrictions are currently applied to my own user-level access key?
  phrasing_ops: 10
  slug: integration-os-access-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Search and list available actions for platforms
  name: IntegrationOS Actions API
  phrasing_intents:
  - id: search_actions
    intent: Search a platform's actions by keyword
    question: How do I find the action that sends an email or creates a contact on a connected platform?
  - id: list_actions
    intent: List the actions available on a platform
    question: What actions does a connected platform expose that I can run?
  phrasing_ops: 2
  slug: integration-os-actions-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: View cron run history for AI agents
  name: IntegrationOS AI Agent Cron Runs API
  phrasing_intents:
  - id: list_project_ai_agent_cron_runs
    intent: List a project agent's scheduled runs
    question: What has a project-scoped agent done on its schedule recently?
  - id: create_project_ai_agent_cron_run
    intent: Record a project agent's scheduled run
    question: How do I log a scheduled execution for an agent inside a project?
  - id: get_project_ai_agent_cron_run
    intent: Get one scheduled run of a project agent
    question: How do I inspect a single scheduled run of a project agent?
  - id: list_org_ai_agent_cron_runs
    intent: List an org agent's scheduled runs
    question: What scheduled runs has an organization-level agent made lately?
  - id: create_org_ai_agent_cron_run
    intent: Record an org agent's scheduled run
    question: How do I log a scheduled execution of an organization agent?
  - id: get_org_ai_agent_cron_run
    intent: Get one scheduled run of an org agent
    question: How can I look at one cron execution of an organization agent?
  - id: list_ai_agent_cron_runs
    intent: List my agent's scheduled runs
    question: What has my personal agent been doing on its schedule?
  - id: create_ai_agent_cron_run
    intent: Record my agent's scheduled run
    question: How is a scheduled run of my own agent recorded?
  phrasing_ops: 9
  slug: integration-os-ai-agent-cron-runs-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Manage AI agents for automation and orchestration
  name: IntegrationOS AI Agents API
  phrasing_intents:
  - id: list_ai_agents
    intent: List my AI agents
    question: Which AI agents do I have in my account?
  - id: create_ai_agent
    intent: Create an AI agent
    question: How do I create an AI agent in my own account with a chosen model and skills?
  - id: list_org_ai_agents
    intent: List an organization's AI agents
    question: What AI agents does my organization own?
  - id: create_org_ai_agent
    intent: Create an organization AI agent
    question: How do I create an agent that every project in my organization can see?
  - id: list_project_ai_agents
    intent: List a project's AI agents
    question: Which AI agents live inside a specific project?
  - id: create_project_ai_agent
    intent: Create a project AI agent
    question: How do I create an agent isolated to a single project?
  - id: delete_project_ai_agent
    intent: Delete a project AI agent
    question: How do I permanently delete an agent from a project?
  - id: get_project_ai_agent
    intent: Get a project AI agent's configuration
    question: How is a particular project agent configured?
  phrasing_ops: 15
  slug: integration-os-ai-agents-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Manage secrets for AI agent runner pods
  name: IntegrationOS AI Runner Secrets API
  phrasing_intents:
  - id: list_project_ai_runner_secrets
    intent: List a project agent's secrets
    question: Which secrets are stored for an AI agent that lives in a project?
  - id: create_project_ai_runner_secret
    intent: Add a secret to a project agent
    question: How do I give an AI agent in a project an API key it can use at runtime?
  - id: delete_project_ai_runner_secret
    intent: Delete a secret from a project agent
    question: How do I remove a stored secret from an AI agent in a project?
  - id: list_org_ai_runner_secrets
    intent: List an organization agent's secrets
    question: What secrets are configured on an AI agent owned by my organization?
  - id: create_org_ai_runner_secret
    intent: Add a secret to an organization agent
    question: How do I store a credential on an AI agent that belongs to the whole organization?
  - id: delete_org_ai_runner_secret
    intent: Delete a secret from an organization agent
    question: How do I delete a secret from an AI agent owned by my organization?
  - id: list_ai_runner_secrets
    intent: List my personal agent's secrets
    question: Which secrets have I stored on one of my own AI agents?
  - id: create_ai_runner_secret
    intent: Add a secret to my personal agent
    question: How do I give one of my own AI agents an API key to use when it runs?
  phrasing_ops: 9
  slug: integration-os-ai-runner-secrets-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Manage AI agent runner pods
  name: IntegrationOS AI Runners API
  phrasing_intents:
  - id: destroy_project_ai_runner
    intent: Tear down a project agent's runner
    question: How do I shut down and remove the runner for a project-scoped agent?
  - id: get_project_ai_runner_status
    intent: Check a project agent's runner status
    question: Is the runner behind my project-scoped AI agent up right now?
  - id: ensure_project_ai_runner
    intent: Start a project agent's runner if not running
    question: Can I make sure a project agent has a runner spun up before I send it work?
  - id: reveal_project_ai_runner_dashboard_password
    intent: Reveal a project runner's dashboard password
    question: Where do I find the dashboard password for a project agent's runner?
  - id: regenerate_project_ai_runner_dashboard_password
    intent: Rotate a project runner's dashboard password
    question: How can I rotate the runner dashboard password for a project-scoped agent?
  - id: proxy_project_ai_runner
    intent: Forward a request to a project agent's runner
    question: Can I send a request straight through to a project agent's runner?
  - id: destroy_org_ai_runner
    intent: Tear down an organization agent's runner
    question: How do I remove the runner hosting an organization-scoped agent?
  - id: get_org_ai_runner_status
    intent: Check an organization agent's runner status
    question: Is the runner for an organization-scoped AI agent currently running?
  phrasing_ops: 18
  slug: integration-os-ai-runners-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Manage AI skills with session or secret key authentication
  name: IntegrationOS AI Skills API
  phrasing_intents:
  - id: list_ai_skills
    intent: List the AI skills in my account
    question: Which AI skills are available in my personal account?
  - id: create_ai_skill
    intent: Create a personal AI skill
    question: How do I write a new AI skill for myself with its own prompt and allowed tools?
  - id: list_org_ai_skills
    intent: List an organization's AI skills
    question: Which AI skills are shared across every project in my organization?
  - id: create_org_ai_skill
    intent: Create an organization-wide AI skill
    question: How do I add an AI skill that every project in my organization can use?
  - id: list_project_ai_skills
    intent: List a project's AI skills
    question: What AI skills are isolated to one particular project?
  - id: create_project_ai_skill
    intent: Create an AI skill scoped to one project
    question: How do I create an AI skill that only one project can see?
  - id: delete_project_ai_skill
    intent: Delete a project AI skill and all versions
    question: How do I permanently delete a project skill along with every version?
  - id: get_project_ai_skill
    intent: Get a project AI skill's details
    question: What prompt, tools and live version does a project skill currently have?
  phrasing_ops: 27
  slug: integration-os-ai-skills-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: AuthKit initialization and token management
  name: IntegrationOS Auth Kit API
  phrasing_intents:
  - id: check_default_oauth
    intent: Check default OAuth setup for a connector
    question: Does a connector definition fall back to the default OAuth credentials in AuthKit?
  - id: init_authkit
    intent: Start an AuthKit session for an end user
    question: How do I launch the AuthKit connect flow for one of my end users?
  - id: init_authkit_dashboard
    intent: Open the AuthKit dashboard session
    question: How do I start an AuthKit session from the dashboard in my personal scope?
  - id: init_organization_authkit_dashboard
    intent: Open an org's AuthKit dashboard session
    question: How do I open an AuthKit dashboard session for my organization?
  - id: init_project_authkit_dashboard
    intent: Open a project's AuthKit dashboard session
    question: How do I start an AuthKit dashboard session scoped to one project?
  - id: generate_authkit_token
    intent: Generate an AuthKit token for an end user
    question: How do I mint an AuthKit token my frontend can use to open the connect UI?
  phrasing_ops: 6
  slug: integration-os-authkit-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: The Billing API from IntegrationOS — 1 operation(s) for billing.
  name: IntegrationOS Billing API
  phrasing_intents:
  - id: get_ai_agent_seat_trial
    intent: Check agent-seat free trial eligibility
    question: Am I still eligible for the free AI agent seat trial?
  - id: start_ai_agent_seat_trial
    intent: Start the free agent-seat trial
    question: How do I start the one-time free trial for an AI agent seat?
  phrasing_ops: 2
  slug: integration-os-billing-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: List and retrieve connection definitions
  name: IntegrationOS Connection Definitions API
  phrasing_intents:
  - id: list_connection_definitions
    intent: Browse the connectors available to connect
    question: Which platforms can I connect to, and what does each connector definition look like?
  - id: retrieve_connection_definition
    intent: Get one connector definition
    question: What are the details of a single connector definition, by its ID?
  phrasing_ops: 2
  slug: integration-os-connection-definitions-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: List and retrieve connection OAuth definitions
  name: IntegrationOS Connection OAuth Definitions API
  phrasing_intents:
  - id: list_connection_oauth_definitions
    intent: List connection OAuth definitions
    question: Which platforms have OAuth definitions set up for connections?
  - id: retrieve_connection_oauth_definition_by_id
    intent: Get a connection OAuth definition by id
    question: How do I fetch one connection OAuth definition when I have its id?
  - id: retrieve_connection_oauth_definition_by_platform
    intent: Get a platform's connection OAuth definition
    question: How is OAuth configured for connecting a specific platform?
  phrasing_ops: 3
  slug: integration-os-connection-oauth-definitions-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Manage connections
  name: IntegrationOS Connections API
  phrasing_intents:
  - id: list_connections
    intent: List my connections
    question: Which connected accounts do I have in my current scope?
  - id: get_connection_metrics
    intent: Get connection usage metrics
    question: How many connections do I have, and what do the connection metrics show?
  - id: list_organization_connections
    intent: List an organization's connections
    question: Which connections belong to a specific organization?
  - id: list_project_connections
    intent: List a project's connections
    question: What connections exist inside one project of my organization?
  - id: delete_project_connection
    intent: Delete a connection from a project
    question: How do I remove a connected account from one project?
  - id: retrieve_project_connection
    intent: Get a connection within a project
    question: How do I fetch one connection that belongs to a project by its ID?
  - id: update_project_connection_tags
    intent: Rename or retag a project connection
    question: Can I change the tags on a connection that lives in a project?
  - id: delete_organization_connection
    intent: Delete a connection from an organization
    question: How do I remove an organization-level connection?
  phrasing_ops: 14
  slug: integration-os-connections-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: List available connectors
  name: IntegrationOS Connectors API
  phrasing_intents:
  - id: list_connectors
    intent: Browse the connector catalog
    question: Which platforms can I integrate with through One?
  - id: list_connected_connectors
    intent: List connectors I have connected
    question: Which platforms have I actually connected in this environment?
  phrasing_ops: 2
  slug: integration-os-connectors-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: The Event Access API from IntegrationOS — 6 operation(s) for event access.
  name: IntegrationOS Event Access API
  phrasing_intents:
  - id: list_event_access
    intent: List my event access keys
    question: Which event access keys exist in my personal scope?
  - id: create_event_access
    intent: Create a personal event access key
    question: How do I create an event access key in my own account?
  - id: list_organization_event_access
    intent: List an organization's event access keys
    question: What event access keys belong to my organization?
  - id: create_organization_event_access
    intent: Create an organization event access key
    question: How do I create an event access key at the organization level?
  - id: list_project_event_access
    intent: List a project's event access keys
    question: Which event access keys are scoped to a single project?
  - id: create_project_event_access
    intent: Create a project event access key
    question: How do I create an event access key for one project?
  - id: delete_project_event_access
    intent: Delete a project event access key
    question: How do I revoke an event access key that belongs to a project?
  - id: delete_organization_event_access
    intent: Delete an organization event access key
    question: How do I revoke an organization-level event access key?
  phrasing_ops: 9
  slug: integration-os-event-access-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Search knowledge base
  name: IntegrationOS Knowledge API
  phrasing_intents:
  - id: list_knowledge
    intent: List action knowledge documents
    question: What per-action context does One use to ground LLM calls?
  phrasing_ops: 1
  slug: integration-os-knowledge-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: 'The live customer link: status, API-key rotation, and the customer-facing connect flow'
  name: IntegrationOS Link API
  phrasing_intents:
  - id: list_link_connections
    intent: List connections made through Link
    question: Which connections have my end users created through the Link flow?
  - id: init_link_connection
    intent: Start a Link session to connect an account
    question: How do I start the Link flow so an end user can connect their account?
  - id: retrieve_link
    intent: Get an organization's Link
    question: What are the settings of a specific Link in my organization?
  - id: rotate_link
    intent: Rotate an organization's Link
    question: How do I rotate a Link if I think it has been shared too widely?
  - id: resolve_link
    intent: Resolve the Link for the current caller
    question: Which Link applies to the credential I'm calling with?
  phrasing_ops: 5
  slug: integration-os-link-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: 'Agency-side lifecycle of customer link invitations: send, list, resend, revoke'
  name: IntegrationOS Link Invitations API
  phrasing_intents:
  - id: list_link_invitations
    intent: List customer link invitations
    question: Which customers have I sent connect-link invitations to?
  - id: send_link_invitation
    intent: Invite a customer to connect via a link
    question: How do I email a customer an invitation to connect their accounts?
  - id: revoke_link_invitation
    intent: Revoke a customer link invitation
    question: How do I cancel a connect-link invitation I sent to a customer?
  - id: resend_link_invitation
    intent: Resend a customer link invitation
    question: Can I resend a connect-link invitation a customer says they never got?
  phrasing_ops: 4
  slug: integration-os-link-invitations-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Agency-side templates that produce per-customer link invitations
  name: IntegrationOS Link Templates API
  phrasing_intents:
  - id: list_link_templates
    intent: List connect link templates
    question: Which link templates has my organization set up?
  - id: create_link_template
    intent: Create a connect link template
    question: How do I create a branded template for customer connect links?
  - id: delete_link_template
    intent: Delete a link template
    question: How do I remove a link template we no longer use?
  - id: retrieve_link_template
    intent: Get a link template
    question: How do I view the settings of one existing link template?
  - id: update_link_template
    intent: Update a link template
    question: Can I change the welcome message on a link template I already made?
  phrasing_ops: 5
  slug: integration-os-link-templates-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: The Marketplace API from IntegrationOS — 5 operation(s) for marketplace.
  name: IntegrationOS Marketplace API
  phrasing_intents:
  - id: search_marketplace_ai_skills
    intent: Search the AI skills marketplace
    question: Which public AI skills are published in the marketplace for a task I have in mind?
  - id: get_marketplace_ai_skill_latest
    intent: Get the latest version of a marketplace skill
    question: What does the newest release of a marketplace AI skill contain?
  - id: list_marketplace_ai_skill_versions
    intent: List a marketplace skill's released versions
    question: What versions of a marketplace AI skill have been released over time?
  - id: get_marketplace_ai_skill_version
    intent: Get a specific version of a marketplace skill
    question: Can I inspect an older pinned version of a marketplace skill rather than the latest?
  - id: export_marketplace_ai_skill_version
    intent: Export a marketplace skill version as a file
    question: How do I download a specific marketplace skill release to keep in my own repo?
  phrasing_ops: 5
  slug: integration-os-marketplace-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: The OAuth Authorizations API from IntegrationOS — 2 operation(s) for oauth authorizations.
  name: IntegrationOS OAuth Authorizations API
  phrasing_intents:
  - id: list_oauth_authorizations
    intent: List the OAuth apps I have authorized
    question: Which third-party OAuth apps have I granted access to my account?
  - id: revoke_oauth_authorization
    intent: Revoke an OAuth app's access to my account
    question: How do I remove an OAuth app's access to my account?
  - id: read_oauth_authorization
    intent: View my authorization for one OAuth app
    question: What access did I grant to a specific OAuth client?
  - id: edit_oauth_authorization
    intent: Change the access an authorized app has
    question: Can I narrow what an already-authorized OAuth app is allowed to reach?
  phrasing_ops: 4
  slug: integration-os-oauth-authorizations-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: The OAuth Clients API from IntegrationOS — 7 operation(s) for oauth clients.
  name: IntegrationOS OAuth Clients API
  phrasing_intents:
  - id: list_oauth_clients
    intent: List the OAuth clients I've registered
    question: Which OAuth client applications have I registered so far?
  - id: create_oauth_client
    intent: Register a new OAuth client app
    question: How do I register an app so it can request OAuth access on behalf of users?
  - id: delete_oauth_client
    intent: Delete a registered OAuth client
    question: How do I delete an OAuth client app I no longer use?
  - id: retrieve_oauth_client
    intent: Get an OAuth client's settings
    question: What redirect URIs and token lifetime are configured on one of my OAuth clients?
  - id: update_oauth_client
    intent: Update an OAuth client's settings
    question: Can I change the redirect URIs on an OAuth app I already registered?
  - id: list_permission_sets
    intent: List an OAuth client's permission sets
    question: Which permission sets are defined for one of my OAuth clients?
  - id: create_permission_set
    intent: Create a permission set for an OAuth client
    question: How do I define which connectors an OAuth app may request access to?
  - id: delete_permission_set
    intent: Delete a permission set from an OAuth client
    question: How do I remove a permission set an OAuth app no longer needs?
  phrasing_ops: 13
  slug: integration-os-oauth-clients-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Programmatically manage organizations, their members, invitations, AuthKit configuration, and API keys with a service-account API key
  name: IntegrationOS Organizations API
  phrasing_intents:
  - id: setup_organization
    intent: Create an organization with a service key
    question: How do I set up a new organization and get its service-account key in one step?
  - id: delete_organization
    intent: Delete an organization
    question: How do I delete an organization I no longer need?
  - id: get_organization
    intent: Get an organization's settings
    question: What members and projects does my organization have?
  - id: update_organization_settings
    intent: Rename or redescribe an organization
    question: How do I rename my organization?
  - id: upsert_organization_authkit
    intent: Configure organization-level embeddable auth
    question: How do I set up embeddable OAuth for a connector across my whole organization?
  - id: list_organization_invitations
    intent: List pending organization invitations
    question: Who has been invited to my organization but not joined yet?
  - id: create_organization_invitation
    intent: Invite someone to an organization
    question: How do I invite a teammate to my organization by email?
  - id: revoke_organization_invitation
    intent: Revoke an organization invitation
    question: How do I cancel an invitation to my organization before it is accepted?
  phrasing_ops: 16
  slug: integration-os-organizations-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Proxy requests to external APIs through configured connections
  name: IntegrationOS Passthrough API
  phrasing_intents:
  - id: passthrough
    intent: Delete on a platform via a raw DELETE
    question: Can I remove a record on a connected platform by forwarding a raw DELETE?
  - id: getV1PassthroughByKey
    intent: Read data from a platform via a raw GET
    question: How do I fetch a record from a connected platform when no ready-made action covers it?
  - id: headV1PassthroughByKey
    intent: Check a platform resource via a raw HEAD
    question: Can I check whether an upstream resource exists with a HEAD request, without pulling the body?
  - id: optionsV1PassthroughByKey
    intent: Probe a platform endpoint via raw OPTIONS
    question: How do I find which methods an upstream endpoint allows by forwarding an OPTIONS request?
  - id: patchV1PassthroughByKey
    intent: Partly update a platform record via raw PATCH
    question: How do I change just a few fields on a connected platform's record with a raw PATCH?
  - id: postV1PassthroughByKey
    intent: Create on a platform via a raw POST
    question: How do I create something on a connected platform through a raw POST when there's no built-in action?
  - id: putV1PassthroughByKey
    intent: Replace a platform record via a raw PUT
    question: Can I overwrite a whole record on a connected platform with a raw PUT call?
  phrasing_ops: 7
  slug: integration-os-passthrough-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Programmatically manage projects inside an organization — including members, invitations, and project-scoped API keys — with a service-account API key
  name: IntegrationOS Projects API
  phrasing_intents:
  - id: list_projects
    intent: List projects in an organization
    question: What projects exist in my organization?
  - id: create_project
    intent: Create a project
    question: How do I create a new project inside my organization?
  - id: delete_project
    intent: Delete a project
    question: How do I delete a project I am done with?
  - id: update_project
    intent: Rename or redescribe a project
    question: How do I rename a project?
  - id: upsert_project_authkit
    intent: Configure project-level embeddable auth
    question: Can I give one project its own embeddable OAuth settings, separate from the organization?
  - id: list_project_invitations
    intent: List pending project invitations
    question: Who has an open invitation to a particular project?
  - id: create_project_invitation
    intent: Invite someone to a project
    question: How do I invite a collaborator to only one project?
  - id: list_project_keys
    intent: List a project's API keys
    question: Which API keys are scoped to a given project?
  phrasing_ops: 14
  slug: integration-os-projects-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: User management
  name: IntegrationOS Users API
  phrasing_intents:
  - id: get_user_flags
    intent: Get my account's feature flags
    question: Which feature flags are switched on for my user account?
  phrasing_ops: 1
  slug: integration-os-users-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Manage vault connections with detailed views
  name: IntegrationOS Vault API
  phrasing_intents:
  - id: list_vault_connections
    intent: List the connections I can access
    question: Which connected accounts can my current key see in the vault?
  - id: delete_vault_connection
    intent: Delete a connection and its credentials
    question: How do I permanently remove a connected account and its stored credentials?
  - id: retrieve_vault_connection
    intent: Get one connection from the vault
    question: What are the details of a single connection stored in the vault?
  - id: update_vault_connection_tags
    intent: Rename or retag a vault connection
    question: Can I replace the tags on a vault connection, and are tags I leave out removed?
  - id: list_organization_vault_connections
    intent: List every connection in an organization
    question: As an admin, how do I see every connection across my organization regardless of project?
  - id: retrieve_organization_vault_connection
    intent: Get one connection in an organization
    question: What platform, identity and status does a particular organization connection have?
  - id: list_project_vault_connections
    intent: List the connections inside one project
    question: How do I narrow the vault to the connections of just one project?
  - id: retrieve_project_vault_connection
    intent: Get one connection inside a project
    question: What are the details of a specific connection that lives in a project?
  phrasing_ops: 8
  slug: integration-os-vault-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: The Webhook Events API from IntegrationOS — 2 operation(s) for webhook events.
  name: IntegrationOS Webhook Events API
  phrasing_intents:
  - id: list_org_webhook_events
    intent: List an organization's recent webhook events
    question: What webhook events were emitted across my whole organization recently?
  - id: list_project_webhook_events
    intent: List a project's recent webhook events
    question: Which webhook events has a single project emitted lately?
  phrasing_ops: 2
  slug: integration-os-webhook-events-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Manage webhook relay endpoints, events, and deliveries
  name: IntegrationOS Webhook Relay API
  phrasing_intents:
  - id: list_relay_endpoints
    intent: List my webhook relay endpoints
    question: Which webhook relay endpoints have been set up under my key?
  - id: create_relay_endpoint
    intent: Create a webhook relay endpoint on a connection
    question: How do I start receiving a connected platform's webhooks for one of my connections?
  - id: get_webhook_relay_config
    intent: Get webhook setup instructions for a connector
    question: What URL do I paste into the upstream platform to set up webhook relay for a connector?
  - id: list_webhook_relay_event_types
    intent: List the webhook event types a platform sends
    question: Which webhook event types can a given platform deliver through the relay?
  - id: list_relay_events
    intent: List inbound webhook events the relay received
    question: What webhook deliveries has the relay received from upstream platforms?
  - id: get_relay_event
    intent: Get one inbound webhook event and its payload
    question: How do I see the raw payload an upstream platform sent for a specific webhook event?
  - id: list_relay_event_deliveries
    intent: List delivery attempts for a relay event
    question: Why did a received webhook event not reach one of my endpoints?
  - id: receive_webhook_relay
    intent: Accept an inbound webhook from a platform
    question: What is the inbound URL upstream platforms post webhooks to for a connection?
  phrasing_ops: 16
  slug: integration-os-webhook-relay-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Manage webhook subscriptions and events
  name: IntegrationOS Webhook Subscriptions API
  phrasing_intents:
  - id: upsert_webhook_subscription
    intent: Create or reconcile a named webhook listener
    question: How can I register a webhook listener on every app boot without creating duplicates?
  - id: list_org_webhook_subscriptions
    intent: List organization webhook subscriptions
    question: Which webhook URLs are subscribed at the organization level?
  - id: create_org_webhook_subscription
    intent: Subscribe a URL to organization events
    question: How do I get webhooks for events across my whole organization?
  - id: list_project_webhook_subscriptions
    intent: List project webhook subscriptions
    question: Which webhooks are registered inside a specific project?
  - id: create_project_webhook_subscription
    intent: Subscribe a URL to project events
    question: How do I receive webhooks only for events inside one project?
  - id: delete_project_webhook_subscription
    intent: Delete a project webhook subscription
    question: How do I permanently remove a webhook from a project?
  - id: get_project_webhook_subscription
    intent: Get a project webhook subscription
    question: How is a particular project webhook configured?
  - id: update_project_webhook_subscription
    intent: Update a project webhook subscription
    question: Can I change the delivery URL of an existing project webhook?
  phrasing_ops: 13
  slug: integration-os-webhook-subscriptions-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: Identify the caller behind a secret key
  name: IntegrationOS Whoami API
  phrasing_intents:
  - id: whoami
    intent: Identify the owner of my API key
    question: Which user does this One secret key belong to?
  phrasing_ops: 1
  slug: integration-os-whoami-api
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: The OAuth API from IntegrationOS — 7 operation(s) for oauth.
  name: IntegrationOS O Auth API
  phrasing_intents:
  - id: oauth_authorize_actions
    intent: List a platform's actions for the consent card
    question: Which actions of a platform can the connect card offer in its custom picker?
  - id: oauth_authorize_actions_search
    intent: Search a platform's actions in the consent card
    question: Can the connect card search a platform's actions by text?
  - id: oauth_authorize_activate
    intent: Stand up an offered connector during consent
    question: What happens when an end user picks a connector that is offered but not yet set up?
  - id: oauth_authorize_connect
    intent: Start connecting a platform from the card
    question: Which platforms can a user still add from the OAuth connect card?
  - id: oauth_authorize_connections
    intent: List connections the user already holds
    question: Which of the requested connectors has the signed-in user already connected?
  - id: oauth_authorize_context
    intent: Load the context for a consent ceremony
    question: What does the connect card need to render an in-progress OAuth consent?
  - id: oauth_authorize_prior_grant
    intent: Read the user's prior grant for reconnect
    question: What did a user already grant this OAuth client, so a reconnect does not widen it?
  phrasing_ops: 7
  slug: integration-os-oauth-api
artifact_total: 44
asyncapis:
- description: ''
  name: Integration Os Webhooks
  slug: integration-os-webhooks
common:
- group: other
  href: https://artifacts.apis.io/integration-os/capabilities/integration-os-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/integration-os-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/integration-os/scopes/integration-os-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/integration-os-scopes.yml
- group: auth
  href: https://artifacts.apis.io/integration-os/authentication/integration-os-authentication.yml
  title: ''
  type: Authentication
  url: authentication/integration-os-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.withone.ai/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/withoneai/knowledge/issues
- group: other
  href: https://artifacts.apis.io/integration-os/a2a/integration-os-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/integration-os-a2a.yml
- group: auth
  href: https://artifacts.apis.io/integration-os/security/integration-os-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/integration-os-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/integrationos
- group: start
  title: ''
  type: Portal
  url: https://withone.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.withone.ai/docs/welcome
- group: company
  title: ''
  type: Blog
  url: https://www.withone.ai/blog
- group: other
  title: ''
  type: KnowledgeBase
  url: https://www.withone.ai/knowledge
- group: start
  title: ''
  type: Signup
  url: https://app.withone.ai
- group: start
  title: ''
  type: Login
  url: https://app.withone.ai
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/withoneai
- group: other
  title: ''
  type: HistoricalSite
  url: https://www.picaos.com/
- group: build
  title: ''
  type: HistoricalGitHub
  url: https://github.com/integration-os
- group: docs
  href: https://artifacts.apis.io/integration-os/openapi/_original/integration-os-one-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/integration-os-one-api-openapi.json
- group: agent
  href: https://artifacts.apis.io/integration-os/mcp/integration-os-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/integration-os-mcp.yml
- group: build
  href: https://artifacts.apis.io/integration-os/mcp/integration-os-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/integration-os-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/integration-os/asyncapi/integration-os-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/integration-os-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/integration-os/llms/integration-os-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/integration-os-llms.txt
- group: agent
  href: https://artifacts.apis.io/integration-os/well-known/integration-os-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/integration-os-well-known.yml
- group: agent
  href: https://artifacts.apis.io/integration-os/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/integration-os/packages/integration-os-packages.yml
  title: ''
  type: Packages
  url: packages/integration-os-packages.yml
- group: build
  href: https://artifacts.apis.io/integration-os/packages/integration-os-packages.yml
  title: ''
  type: SDKs
  url: packages/integration-os-packages.yml
- group: build
  href: https://artifacts.apis.io/integration-os/cli/integration-os-cli.yml
  title: ''
  type: CLI
  url: cli/integration-os-cli.yml
- group: design
  href: https://artifacts.apis.io/integration-os/components/integration-os-components.yml
  title: ''
  type: Components
  url: components/integration-os-components.yml
- group: start
  href: https://artifacts.apis.io/integration-os/sandbox/integration-os-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/integration-os-sandbox.yml
- group: design
  href: https://artifacts.apis.io/integration-os/conventions/integration-os-conventions.yml
  title: ''
  type: Conventions
  url: conventions/integration-os-conventions.yml
- group: design
  href: https://artifacts.apis.io/integration-os/conventions/integration-os-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/integration-os-conventions.yml
- group: design
  href: https://artifacts.apis.io/integration-os/errors/integration-os-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/integration-os-problem-types.yml
- group: design
  href: https://artifacts.apis.io/integration-os/data-model/integration-os-data-model.yml
  title: ''
  type: DataModel
  url: data-model/integration-os-data-model.yml
- group: design
  href: https://artifacts.apis.io/integration-os/conformance/integration-os-conformance.yml
  title: ''
  type: Conformance
  url: conformance/integration-os-conformance.yml
- group: design
  href: https://artifacts.apis.io/integration-os/lifecycle/integration-os-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/integration-os-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.withone.ai/
- group: operate
  href: https://artifacts.apis.io/integration-os/changelog/integration-os-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/integration-os-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/integration-os/plans/integration-os-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/integration-os-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/integration-os/rate-limits/integration-os-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/integration-os-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/integration-os/finops/integration-os-finops.yml
  title: ''
  type: FinOps
  url: finops/integration-os-finops.yml
- group: design
  href: https://artifacts.apis.io/integration-os/rules/integration-os-rules.yml
  title: ''
  type: Rules
  url: rules/integration-os-rules.yml
- group: other
  href: https://artifacts.apis.io/integration-os/overlays/integration-os-one-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/integration-os-one-api-overlay.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://www.withone.ai/docs/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://www.withone.ai/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.withone.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.withone.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.withone.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.withone.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withoneai
- group: operate
  title: ''
  type: Contact
  url: mailto:hello@withone.ai
created: '2026-03-27'
description: 'IntegrationOS was a unified API platform that let developers add third-party integrations to their products with a single API call. The company rebranded as Pica (picaos.com) and then, on 2026-03-25, as One (withone.ai) — the provider''s own changelog records the step as "Pica is now One". One is an agent infrastructure platform: authenticated access to 789 platforms and 111,176 actions through a unified CLI, managed OAuth (AuthKit), multi-step Flows, inbound webhook Relay, and both a hosted and a local Model Context Protocol server. This record preserves the IntegrationOS history and profiles the active successor''s published surface, including its OpenAPI 3.1.0 contract (248 operations), its four-tool MCP server, its llms.txt and its agent.json.'
finops:
- has_sources: true
  method: derived
  name: Integration Os Finops
  primary_unit: agent
  service_category: ''
  slug: integration-os-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: One ships BOTH a hosted remote MCP server and a local-stdio server, and the provider documents them as two ways to reach the same four tools. The remote endpoint is reachable and OAuth-gated; the loca
  name: IntegrationOS MCP Server
  slug: one
modified: '2026-09-16'
name: IntegrationOS
nav: Providers
network: true
overview: 'IntegrationOS publishes 31 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access API, Actions API, AI Agent Cron Runs API, and 28 more. Tagged areas include Agent Infrastructure, AI Agents, Connectors, Historical, and Integration.


  The IntegrationOS catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  IntegrationOS''s developer surface includes authentication, developer portal, documentation, engineering blog, signup flow, CLI, sandbox, and 43 more developer resources.'
plans:
- name: Integration Os Plans Pricing
  plan_count: 5
  slug: integration-os-plans-pricing
- name: Integration Os Price Estimates
  plan_count: 0
  slug: integration-os-price-estimates
random_paper: 19
rate_limits:
- limit_count: 4
  name: Integration Os Rate Limits
  slug: integration-os-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 0
  extends: []
  name: IntegrationOS API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: integration-os-rules
scopes:
- name: Integration Os Scopes
  scope_count: 38
  slug: integration-os-scopes
  summary_line: 38 scopes · authorizationCode
score:
  band: exemplar
  composite: 69.4
  coverage:
    artifact_dirs: 32
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 60.6
    developer_ergonomics: 85.0
    discoverability: 75.0
    operational_transparency: 65.8
  previous_composite: 68.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 31
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/integration-os/integration-os-2026-06-20T183438.png
security:
- kind: authentication
  name: Integration Os Authentication
  slug: integration-os-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Integration Os Domain Security
  slug: integration-os-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: one-connect-and-execute
  slug: integration-os-connect-and-execute
- name: integration-standards
  slug: integration-os-integration-standards
- name: one-scope-an-agent
  slug: integration-os-scope-an-agent
slug: integration-os
tags:
- Agent Infrastructure
- AI Agents
- Connectors
- Historical
- Integration
- iPaaS
- MCP
- Rebrand
- Unified API
- A2A
website: https://www.withone.ai/
---
