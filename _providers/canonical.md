---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 413
  human_in_the_loop: 3
  name: Canonical Agentic Access
  operation_count: 812
  slug: canonical-agentic-access
  summary_line: 812 operations · 413 acting · 3 human-in-the-loop
api_count: 13
apis:
- description: The public Snap Store Device API (api.snapcraft.io) serves information about snaps, revisions, channels, tracks, assertions, and refresh state to snap clients. The Snapcraft Dashboard API (dashboard.s
  name: Snap Store API
  slug: snap-store-api
- description: Developer-facing REST API for Charmhub, Canonical's marketplace for charms (Kubernetes and machine operators). Supports charm discovery, publishing, release channels, and token exchange — macaroons is
  name: Charmhub API
  slug: charmhub-api
- description: The RESTful API for MAAS (Metal as a Service). Everything the MAAS UI can do — commissioning, allocation, deployment, DHCP/DNS, tags, zones, pools, users, machines — is available through the API, maki
  name: MAAS API
  slug: maas-api
- description: Juju is Canonical's open-source orchestration engine for deploying, integrating, scaling, and managing applications on clouds, MAAS, LXD, and Kubernetes via charms. Juju clients communicate with a con
  name: Juju Client / Controller API
  slug: juju-api
- description: Launchpad exposes a RESTful Web Services API over its project hosting, bug tracking, code, builds, translations, and distribution data. The API is authenticated with OAuth; anonymous access gives read
  name: Launchpad Web Services API
  slug: launchpad-api
- description: The Ubuntu Pro client exposes a local API/CLI for managing Ubuntu Pro subscription services on a host — enabling, disabling, and inspecting Extended Security Maintenance (ESM), Livepatch, FIPS, compli
  name: Ubuntu Pro Client API
  slug: ubuntu-pro-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Assertions API from Canonical — 1 operation(s) for assertions.
  name: Canonical Assertions API
  phrasing_intents:
  - id: listAssertionTypes
    intent: List known assertion types
    question: Which assertion types does snapd know about?
  - id: addAssertion
    intent: Add or replace a signed assertion
    question: How do I add a signed assertion to the system's assertion database?
  - id: getAssertionsByType
    intent: Get assertions of a given type
    question: How do I fetch all assertions of one type, such as account-key?
  - id: getModelAssertion
    intent: Get the device's model assertion
    question: Which model assertion describes this snap-based device?
  - id: setModelAssertion
    intent: Remodel the device with a new model assertion
    question: How do I remodel a device by supplying a new model assertion?
  - id: getSerialAssertion
    intent: Get the device's serial assertion
    question: What serial assertion binds this device's identity to its key?
  - id: setSerialAssertion
    intent: Forget the device's serial registration
    question: How do I make a device forget its serial and register again?
  - id: getV2AssertionsByTypeByPrimaryKey
    intent: Fetch one assertion by its primary key
    question: Can I fetch a single signed assertion if I know its type and primary key?
  phrasing_ops: 8
  slug: canonical-assertions-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Search API from Canonical — 1 operation(s) for search.
  name: Canonical Search API
  phrasing_intents:
  - id: getApiV1Search
    intent: Search the store (legacy v1)
    question: Can I still search the Snap Store through the old v1 search endpoint?
  phrasing_ops: 1
  slug: canonical-search-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Snaps API from Canonical — 10 operation(s) for snaps.
  name: Canonical Snaps API
  phrasing_intents:
  - id: getV2SnapsInfoByName
    intent: Get snap details
    question: Which channels and revisions are published for a snap?
  - id: getV2SnapsFind
    intent: Find snaps
    question: How do I search the Snap Store by keyword?
  - id: postV2SnapsRefresh
    intent: Check which snaps need refreshing
    question: Which of my installed snaps have newer revisions available?
  - id: getApiV1SnapsSearch
    intent: Search snaps (legacy v1)
    question: Does the older v1 snaps search endpoint still work?
  - id: getApiV1SnapsNames
    intent: List snap names for autocomplete
    question: Can I get every snap name to drive autocomplete?
  - id: getApiV1SnapsSections
    intent: List store sections
    question: What sections or categories does the store group snaps into?
  - id: postApiV1SnapsAuthNonces
    intent: Request a device nonce
    question: How does a device get a nonce before authenticating to the store?
  - id: postApiV1SnapsAuthSessions
    intent: Create a device session
    question: How does a device open an authenticated session with the store?
  phrasing_ops: 10
  slug: canonical-snaps-api
- description: MicroCeph is Canonical's opinionated, snap-delivered Ceph distribution. It publishes a small OpenAPI 3.1.0 contract for its cluster REST surface. Recorded here because it is a real published first-par
  name: MicroCeph REST API
  phrasing_intents:
  - id: setLogLevel
    intent: Set the MicroCeph log level
    question: How do I turn up debug logging for the MicroCeph daemon?
  - id: getLogLevel
    intent: Get the MicroCeph log level
    question: What logging level is the MicroCeph daemon currently using?
  phrasing_ops: 2
  slug: microceph-api
- description: The AppAuthorizationService API from Canonical — 3 operation(s) for appauthorizationservice.
  name: Canonical App Authorization Service API
  phrasing_intents:
  - id: AppAuthorizationService_RemoveAllowedGroupsForApp
    intent: Remove an app from every group
    question: How do I revoke an app's access from all groups at once?
  - id: AppAuthorizationService_GetAllowedGroupsForApp
    intent: List groups an app is allowed in
    question: Which groups is a given OAuth app allowed to be used in?
  - id: AppAuthorizationService_RemoveAllowedAppsFromGroup
    intent: Remove all apps from a group
    question: Can I clear a group's entire allowed-apps list in one go?
  - id: AppAuthorizationService_GetAllowedAppsInGroup
    intent: List apps allowed in a group
    question: Which apps are members of a group's allowed list?
  - id: AppAuthorizationService_AddAllowedAppToGroup
    intent: Allow an app in a group
    question: How do I authorize a client app for a group?
  - id: AppAuthorizationService_RemoveAllowedAppFromGroup
    intent: Remove one app from a group
    question: How do I take a single app off a group's allowed list?
  phrasing_ops: 6
  slug: canonical-appauthorizationservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The application API from Canonical — 1 operation(s) for application.
  name: Canonical Application API
  phrasing_intents:
  - id: handle-get-applications
    intent: List streaming-enabled applications
    question: Which AMS applications can I stream to users?
  phrasing_ops: 1
  slug: canonical-application-api
- description: The applications API from Canonical — 20 operation(s) for applications.
  name: Canonical Applications API
  phrasing_intents:
  - id: applications_get
    intent: List Android applications in AMS
    question: Which Android applications are stored in my Anbox Management Service?
  - id: application_post
    intent: Create an application from a package
    question: How do I upload a new Android app package with a manifest.yaml to AMS?
  - id: applications_delete
    intent: Delete several applications at once
    question: Can I remove a batch of AMS applications in one request?
  - id: application_get
    intent: Get details of one AMS application
    question: Where can I see the details stored for a single Anbox application?
  - id: application_delete
    intent: Delete an application and all its versions
    question: How do I remove a single Anbox application along with every version of it?
  - id: application_patch_upload
    intent: Replace an application's package
    question: Can I push a new bzip2 or zip package to an existing AMS application?
  - id: application_patch_meta
    intent: Update an application's metadata only
    question: Which AMS application metadata changes create a new application version?
  - id: application_manifest_get
    intent: Download an application's latest manifest
    question: Can I download the latest manifest.yaml of an AMS application?
  phrasing_ops: 45
  slug: canonical-applications-api
- baseURL: unix:///run/snapd.socket
  baseurl_source: spec
  description: The Apps API from Canonical — 2 operation(s) for apps.
  name: Canonical Apps API
  phrasing_intents:
  - id: getAliases
    intent: List snap app aliases
    question: Which command aliases are set up for snap apps on this system?
  - id: modifyAliases
    intent: Alias, unalias or prefer snap aliases
    question: How do I create a command alias for an app inside a snap?
  - id: listApps
    intent: List apps from installed snaps
    question: Which applications and services do my installed snaps provide?
  - id: modifyApps
    intent: Start, stop or restart snap services
    question: How do I restart a service that runs from a snap?
  phrasing_ops: 4
  slug: canonical-apps-api
- description: The artefact-builds API from Canonical — 1 operation(s) for artefact-builds.
  name: Canonical Artefact Builds API
  phrasing_intents:
  - id: get_artefact_builds_v1_artefacts__artefact_id__builds_get
    intent: Get an artefact's builds with test executions
    question: What builds does an artefact have and which tests ran on each?
  phrasing_ops: 1
  slug: canonical-artefact-builds-api
- description: The artefact-matching-rules API from Canonical — 2 operation(s) for artefact-matching-rules.
  name: Canonical Artefact Matching Rules API
  phrasing_intents:
  - id: create_artefact_matching_rule_v1_artefact_matching_rules_post
    intent: Create an artefact matching rule
    question: How do I route artefacts of a given family to my team for review?
  - id: get_artefact_matching_rules_v1_artefact_matching_rules_get
    intent: List artefact matching rules
    question: Which rules decide which team reviews an artefact in Test Observer?
  - id: get_artefact_matching_rule_v1_artefact_matching_rules__rule_id__get
    intent: Get an artefact matching rule
    question: What criteria and teams does a particular matching rule have?
  - id: update_artefact_matching_rule_v1_artefact_matching_rules__rule_id__patch
    intent: Update an artefact matching rule
    question: How do I change which teams an existing matching rule assigns?
  - id: delete_artefact_matching_rule_v1_artefact_matching_rules__rule_id__delete
    intent: Delete an artefact matching rule
    question: How do I remove an artefact matching rule?
  phrasing_ops: 5
  slug: canonical-artefact-matching-rules-api
- description: The artefacts API from Canonical — 8 operation(s) for artefacts.
  name: Canonical Artefacts API
  phrasing_intents:
  - id: get_artefacts_v1_artefacts_get
    intent: List the latest test artefacts
    question: Which artefacts are currently under test in Test Observer?
  - id: search_artefacts_v1_artefacts_search_get
    intent: Search artefact names
    question: Is there an artefact whose name contains a given word?
  - id: get_artefact_history_v1_artefacts_history_get
    intent: Get an artefact's version history
    question: What versions of a snap have been through testing, and when were they created?
  - id: get_artefact_v1_artefacts__artefact_id__get
    intent: Get one artefact
    question: What's the current status and stage of a specific artefact?
  - id: patch_artefact_v1_artefacts__artefact_id__patch
    intent: Update an artefact's status, stage or reviewers
    question: How do I approve or reject an artefact after testing?
  - id: get_artefact_versions_v1_artefacts__artefact_id__versions_get
    intent: List other versions of an artefact
    question: What other versions exist alongside a given artefact?
  - id: get_environment_reviews_v1_artefacts__artefact_id__environment_reviews_get
    intent: List an artefact's environment reviews
    question: Which test environments have been reviewed for an artefact?
  - id: bulk_update_environment_reviews_v1_artefacts__artefact_id__environment_reviews_patch
    intent: Update many environment reviews at once
    question: Can I mark all environment reviews for an artefact in a single request?
  phrasing_ops: 10
  slug: canonical-artefacts-api
- baseURL: unix:///run/snapd.socket
  baseurl_source: spec
  description: Return the reference to a change that will occur in the background.
  name: Canonical Asynchronous API
  phrasing_intents:
  - id: getConfdb
    intent: Read configuration values from confdb
    question: How do I read values from a confdb view on a snapd device?
  - id: setConfdb
    intent: Write configuration values to confdb
    question: How do I set configuration values through a confdb view?
  - id: postInterfaces
    intent: Connect or disconnect snap interfaces
    question: How do I connect a snap's plug to a slot?
  - id: manageQuotaGroups
    intent: Create, change or remove a quota group
    question: How do I limit the resources a group of snaps can use?
  - id: manageSnaps
    intent: Install, refresh or remove several snaps
    question: How do I install or refresh several snaps in one request?
  - id: manageSnapByName
    intent: Install, refresh or remove one snap
    question: How do I install a single snap from a specific channel?
  - id: setSnapConfig
    intent: Set an installed snap's configuration
    question: How do I change configuration options of an installed snap?
  - id: manageSnapshots
    intent: Restore, check, forget or import snapshots
    question: How do I restore a saved snapshot set of my snaps' data?
  phrasing_ops: 8
  slug: canonical-asynchronous-api
- description: The auth_groups API from Canonical — 3 operation(s) for auth_groups.
  name: Canonical Auth Groups API
  phrasing_intents:
  - id: auth_groups_get
    intent: List authorization group URLs
    question: Which authorization groups exist on my LXD server?
  - id: auth_groups_post
    intent: Create an authorization group
    question: How do I create a new group of permissions in LXD?
  - id: auth_group_delete
    intent: Delete an authorization group
    question: How do I remove an auth group I no longer need?
  - id: auth_group_get
    intent: Get one authorization group
    question: What permissions does a particular auth group hold?
  - id: auth_group_patch
    intent: Partially update an authorization group
    question: Can I update just the description of an auth group?
  - id: auth_group_post
    intent: Rename an authorization group
    question: How do I rename an authorization group?
  - id: auth_group_put
    intent: Replace an authorization group's permissions
    question: Can I replace the entire permission list of an auth group?
  - id: auth_groups_get_recursion1
    intent: List authorization groups with details
    question: Can I list every auth group together with its permissions?
  phrasing_ops: 8
  slug: canonical-auth-groups-api
- description: The authentication API from Canonical — 4 operation(s) for authentication.
  name: Canonical Authentication API
  phrasing_intents:
  - id: saml_login_v1_auth_saml_login_get
    intent: Start a SAML single sign-on login
    question: How do I sign in with SAML single sign-on?
  - id: saml_logout_v1_auth_saml_logout_get
    intent: Start a SAML logout
    question: How do I log out of a SAML session?
  - id: saml_login_callback_v1_auth_saml_acs_post
    intent: Receive the SAML login assertion
    question: Which endpoint is the SAML assertion consumer service?
  - id: saml_logout_callback_v1_auth_saml_sls_get
    intent: Handle a SAML logout redirect
    question: Which URL handles a SAML single logout redirect?
  - id: saml_logout_callback_v1_auth_saml_sls_post
    intent: Handle a posted SAML logout response
    question: Can the identity provider post the SAML logout response instead of redirecting?
  phrasing_ops: 5
  slug: canonical-authentication-api
- baseURL: unix:///run/snapd.socket
  baseurl_source: spec
  description: Access is restricted to the root user.
  name: Canonical Authentication Required API
  phrasing_intents:
  - id: getChanges
    intent: List snapd changes in progress or completed
    question: What installs, refreshes and other changes is snapd running right now?
  - id: getChangeById
    intent: Check the status of one snapd change
    question: Has a specific snapd background change finished yet?
  - id: abortChangeById
    intent: Abort a snapd change in progress
    question: Can I stop a snap operation that's still running?
  - id: createCohorts
    intent: Create cohort keys for snaps
    question: How do I generate cohort keys so several devices get the same snap revision?
  - id: findSnaps
    intent: Search the store for snaps
    question: Which snaps in the store match a search term and work on this machine?
  - id: loginUser
    intent: Log in to snapd and the store
    question: How do I sign in to snapd with my store account?
  - id: logoutUser
    intent: Log out of snapd and the store
    question: How do I sign the current user out of snapd?
  - id: getLogs
    intent: Read snap service logs
    question: Where can I read the logs for my snap services?
  phrasing_ops: 20
  slug: canonical-authenticationrequired-api
- description: The AuthzGroupsService API from Canonical — 5 operation(s) for authzgroupsservice.
  name: Canonical Authz Groups Service API
  phrasing_intents:
  - id: AuthzGroupsService_ListGroups
    intent: List authorization groups
    question: Which authorization groups are defined in the identity platform admin?
  - id: AuthzGroupsService_CreateGroup
    intent: Create an authorization group
    question: How do I create a new group for granting permissions?
  - id: AuthzGroupsService_RemoveGroup
    intent: Delete an authorization group
    question: How do I delete an authorization group entirely?
  - id: AuthzGroupsService_GetGroup
    intent: Get an authorization group
    question: What are the name and type of a specific authorization group?
  - id: AuthzGroupsService_UpdateGroup
    intent: Update an authorization group
    question: How do I rename an authorization group or change its description?
  - id: AuthzGroupsService_ListUsersInGroup
    intent: List the users in an authorization group
    question: Who are the members of a given authorization group?
  - id: AuthzGroupsService_AddUsersToGroup
    intent: Add users to an authorization group
    question: How do I add several people to one authorization group at once?
  - id: AuthzGroupsService_RemoveUserFromGroup
    intent: Remove a user from an authorization group
    question: How do I take one person out of an authorization group?
  phrasing_ops: 10
  slug: canonical-authzgroupsservice-api
- description: The certificates API from Canonical — 4 operation(s) for certificates.
  name: Canonical Certificates API
  phrasing_intents:
  - id: certificates_get
    intent: List trusted client certificates
    question: Which client certificates are trusted by this server?
  - id: certificates_post
    intent: Trust a new client certificate
    question: How do I add a new trusted client by its certificate?
  - id: certificate_get
    intent: Get a trusted certificate
    question: What details are stored for a trusted certificate?
  - id: certificate_delete
    intent: Remove a trusted certificate
    question: How do I revoke a client's trust on this server?
  - id: certificate_patch
    intent: Update some fields of a trusted certificate
    question: Can I just rename a trusted certificate without changing anything else?
  - id: certificate_put
    intent: Replace a trusted certificate's configuration
    question: How do I overwrite all settings of a trusted certificate?
  - id: certificates_get_recursion1
    intent: List trusted certificates with details
    question: Can I list trusted certificates with all their fields expanded?
  - id: certificates_post_untrusted
    intent: Add a certificate as an untrusted client
    question: How does a client that isn't trusted yet add itself using a token?
  phrasing_ops: 8
  slug: canonical-certificates-api
- description: The certification API from Canonical — 1 operation(s) for certification.
  name: Canonical Certification API
  phrasing_intents:
  - id: check_certification_v1_certification_status_post
    intent: Check whether a system is Ubuntu certified
    question: Is my laptop model certified for Ubuntu?
  phrasing_ops: 1
  slug: canonical-certification-api
- description: The changes and tasks API from Canonical — 4 operation(s) for changes and tasks.
  name: Canonical changes and tasks API
  phrasing_intents:
  - id: getV1Changes
    intent: List changes
    question: Which changes are still in progress on my Pebble daemon?
  - id: getV1ChangesById
    intent: Get a specific change
    question: What is the status of a particular change and its tasks?
  - id: postV1ChangesById
    intent: Abort a change
    question: How do I abort a change that is still running?
  - id: getV1ChangesByIdWait
    intent: Wait for a change to finish
    question: Can I block until a change completes instead of polling it?
  - id: getV1TasksByTaskIdWebsocketByWebsocketId
    intent: Connect to a task's websocket
    question: How do I attach to the websocket of a running exec task?
  phrasing_ops: 5
  slug: canonical-changes-and-tasks-api
- description: The checks API from Canonical — 2 operation(s) for checks.
  name: Canonical Checks API
  phrasing_intents:
  - id: getV1Checks
    intent: List health checks
    question: Which Pebble health checks are failing right now?
  - id: postV1Checks
    intent: Start or stop health checks
    question: How do I stop a health check from running?
  - id: postV1ChecksRefresh
    intent: Run a health check immediately
    question: Can I force a check to run now instead of waiting for its period?
  phrasing_ops: 3
  slug: canonical-checks-api
- description: The ClientsService API from Canonical — 2 operation(s) for clientsservice.
  name: Canonical Clients Service API
  phrasing_intents:
  - id: ClientsService_ListClients
    intent: List OAuth clients
    question: Which OAuth clients are registered in the Identity Platform?
  - id: ClientsService_CreateClient
    intent: Register an OAuth client
    question: How do I register a new OAuth client application?
  - id: ClientsService_RemoveClient
    intent: Delete an OAuth client
    question: How do I delete an OAuth client application?
  - id: ClientsService_GetClient
    intent: Get an OAuth client
    question: What redirect URIs and grant types does a particular client have?
  - id: ClientsService_UpdateClient
    intent: Update an OAuth client
    question: How do I change the redirect URIs of an existing OAuth client?
  phrasing_ops: 5
  slug: canonical-clientsservice-api
- description: The cluster API from Canonical — 7 operation(s) for cluster.
  name: Canonical Cluster API
  phrasing_intents:
  - id: cluster_get
    intent: Get the LXD cluster configuration
    question: Is clustering enabled on my LXD server and what is its configuration?
  - id: cluster_put
    intent: Replace the LXD cluster configuration
    question: How do I enable clustering on an LXD server or join it to an existing cluster?
  - id: clustering_update_cert
    intent: Replace the cluster certificate
    question: How do I rotate the TLS certificate used by my whole LXD cluster?
  - id: cluster_groups_post
    intent: Create a cluster group
    question: Can I group some LXD cluster members together for placement?
  - id: cluster_members_get
    intent: List cluster member URLs
    question: Which servers are members of my LXD cluster?
  - id: cluster_members_post
    intent: Request a join token for a new member
    question: How do I get a join token so a new server can join the LXD cluster?
  - id: cluster_member_delete
    intent: Remove a member from the cluster
    question: How do I remove a server from my LXD cluster?
  - id: cluster_member_get
    intent: Get one cluster member
    question: Can I see the roles and failure domain of a single LXD cluster member?
  phrasing_ops: 14
  slug: canonical-cluster-api
- description: The cluster-groups API from Canonical — 3 operation(s) for cluster-groups.
  name: Canonical Cluster Groups API
  phrasing_intents:
  - id: cluster_groups_get
    intent: List cluster group URLs
    question: Which cluster groups are defined in my LXD cluster?
  - id: cluster_group_delete
    intent: Delete a cluster group
    question: How do I remove a cluster group?
  - id: cluster_group_get
    intent: Get one cluster group
    question: Which members belong to a specific cluster group?
  - id: cluster_group_patch
    intent: Update part of a cluster group
    question: Can I change only a cluster group's description?
  - id: cluster_group_post
    intent: Rename a cluster group
    question: How do I rename a cluster group?
  - id: cluster_group_put
    intent: Replace a cluster group's members
    question: Can I replace the whole member list of a cluster group?
  - id: cluster_groups_get_recursion1
    intent: List cluster groups with members
    question: Can I list every cluster group along with its members in one call?
  phrasing_ops: 7
  slug: canonical-cluster-groups-api
- description: The cluster-links API from Canonical — 4 operation(s) for cluster-links.
  name: Canonical Cluster Links API
  phrasing_intents:
  - id: cluster_links_get
    intent: List cluster link URLs
    question: Which other LXD clusters is this cluster linked to?
  - id: cluster_links_post
    intent: Link to another LXD cluster
    question: How do I link this LXD cluster to a remote cluster?
  - id: cluster_link_delete
    intent: Remove a cluster link
    question: How do I unlink a remote LXD cluster?
  - id: cluster_link_get
    intent: Get one cluster link
    question: What settings does a particular cluster link have?
  - id: cluster_link_patch
    intent: Change some cluster link settings
    question: Can I update just one setting on a cluster link?
  - id: cluster_link_post
    intent: Rename a cluster link
    question: How do I rename an existing cluster link?
  - id: cluster_link_put
    intent: Replace a cluster link's configuration
    question: How do I overwrite a cluster link's whole configuration?
  - id: cluster_link_state_get
    intent: Check a cluster link's state
    question: Is a cluster link currently healthy and reachable?
  phrasing_ops: 9
  slug: canonical-cluster-links-api
- description: The config API from Canonical — 1 operation(s) for config.
  name: Canonical Config API
  phrasing_intents:
  - id: config_get
    intent: Show the AMS service configuration
    question: What configuration values is the Anbox Management Service currently using?
  - id: config_patch
    intent: Change an AMS service setting
    question: How do I change a configuration item on the Anbox Management Service?
  phrasing_ops: 2
  slug: canonical-config-api
- description: The containers API from Canonical — 6 operation(s) for containers.
  name: Canonical Containers API
  phrasing_intents:
  - id: containers_get
    intent: List container endpoints
    question: Which Anbox containers are running, as a list of endpoint URLs?
  - id: containers_post
    intent: Launch a new Android container
    question: How do I launch an Android container from an application in Anbox Cloud?
  - id: containers_delete
    intent: Delete several containers at once
    question: How do I delete a batch of containers in one request?
  - id: container_get
    intent: Get one container's details
    question: What status and node is a specific Anbox container on?
  - id: container_delete
    intent: Delete a container
    question: How do I delete a single Anbox container?
  - id: container_patch
    intent: Start or stop a container
    question: How do I stop a running container or start a stopped one?
  - id: container_exec_post
    intent: Run a command inside a container
    question: How do I run a shell command inside an Android container?
  - id: container_logs_get
    intent: List a container's collected logs
    question: Which log files did AMS collect for a container that went into error?
  phrasing_ops: 10
  slug: canonical-containers-api
- description: The devices API from Canonical — 3 operation(s) for devices.
  name: Canonical Devices API
  phrasing_intents:
  - id: devices_list
    intent: List registered devices
    question: Which devices are registered right now?
  - id: devices_create
    intent: Register a new device
    question: How do I register a new device with its address and certificate?
  - id: devices_retrieve
    intent: Get a device by ID
    question: How do I look up everything stored about one device?
  - id: devices_update
    intent: Replace all of a device's fields
    question: Can I overwrite every field of a registered device at once?
  - id: devices_partial_update
    intent: Change some fields of a device
    question: Can I change only a device's address?
  - id: devices_destroy
    intent: Delete a registered device
    question: How do I unregister a device?
  - id: devices_certificate_retrieve
    intent: Check a device's certificate signing status
    question: Has my device's certificate request been signed yet?
  - id: devices_certificate_create
    intent: Submit a certificate signing request
    question: How do I submit a CSR for a device?
  phrasing_ops: 9
  slug: canonical-devices-api
- description: The environment-reviews API from Canonical — 2 operation(s) for environment-reviews.
  name: Canonical Environment Reviews API
  phrasing_intents:
  - id: get_environment_reviews_v1_artefacts__artefact_id__environment_reviews_get
    intent: List environment reviews for an artefact
    question: What review decisions have been made for each environment an artefact was tested on?
  - id: bulk_update_environment_reviews_v1_artefacts__artefact_id__environment_reviews_patch
    intent: Update many environment reviews at once
    question: Can I approve several environment reviews of an artefact in one request?
  - id: update_environment_review_v1_artefacts__artefact_id__environment_reviews__review_id__patch
    intent: Record a decision on one environment review
    question: How do I approve or reject a single environment's test results for an artefact?
  phrasing_ops: 3
  slug: canonical-environment-reviews-api
- description: The environments API from Canonical — 3 operation(s) for environments.
  name: Canonical Environments API
  phrasing_intents:
  - id: get_reported_issues_v1_environments_reported_issues_get
    intent: List issues reported against environments
    question: Which test environments have known reported issues?
  - id: create_reported_issue_v1_environments_reported_issues_post
    intent: Report an issue with a test environment
    question: How do I flag a problem with a specific test environment?
  - id: update_reported_issue_v1_environments_reported_issues__issue_id__put
    intent: Update a reported environment issue
    question: Can I mark a reported environment issue as confirmed later?
  - id: delete_reported_issue_v1_environments_reported_issues__issue_id__delete
    intent: Delete a reported environment issue
    question: How do I remove an environment issue that was reported by mistake?
  - id: get_environments_v1_environments_get
    intent: List environments used in test runs
    question: Which environments have been used in test executions?
  phrasing_ops: 5
  slug: canonical-environments-api
- description: The events API from Canonical — 1 operation(s) for events.
  name: Canonical Events API
  phrasing_intents:
  - id: events_get
    intent: Subscribe to AMS change events over a websocket
    question: Can I get live notifications when things change in AMS?
  phrasing_ops: 1
  slug: canonical-events-api
- description: The exec API from Canonical — 1 operation(s) for exec.
  name: Canonical Exec API
  phrasing_intents:
  - id: postV1Exec
    intent: Execute a command
    question: How do I run a command inside a Pebble-managed container?
  phrasing_ops: 1
  slug: canonical-exec-api
- description: The execution-metadata API from Canonical — 1 operation(s) for execution-metadata.
  name: Canonical Execution Metadata API
  phrasing_intents:
  - id: get_execution_metadata_v1_execution_metadata_get
    intent: Get test execution metadata
    question: What metadata categories are recorded on test executions in Test Observer?
  phrasing_ops: 1
  slug: canonical-execution-metadata-api
- baseURL: unix:///run/snapd.socket
  baseurl_source: spec
  description: Interact with experimental features.
  name: Canonical Experimental API
  phrasing_intents:
  - id: postConfdbControl
    intent: Delegate or withdraw remote confdb management
    question: How do I let an operator remotely manage confdb values on my device?
  - id: getPrompts
    intent: List outstanding access prompts
    question: Which snap permission prompts are waiting for a reply?
  - id: getPromptById
    intent: Get one access prompt
    question: What exactly is a particular pending prompt asking permission for?
  - id: replyToPrompt
    intent: Allow or deny an access prompt
    question: How do I allow or deny a snap's pending access request?
  - id: getRules
    intent: List access prompting rules
    question: What prompting rules have been saved for my snaps?
  - id: manageRules
    intent: Create an access rule or remove rules by selector
    question: How do I add a new access rule without waiting for a prompt?
  - id: getRuleById
    intent: Get one access rule
    question: What does a specific prompting rule allow or deny?
  - id: updateRuleById
    intent: Patch or remove one access rule
    question: Can I edit an existing prompting rule by ID?
  phrasing_ops: 8
  slug: canonical-experimental-api
- description: The files API from Canonical — 1 operation(s) for files.
  name: Canonical Files API
  phrasing_intents:
  - id: getV1Files
    intent: Read or list files
    question: How do I read a file from the remote system?
  - id: postV1Files
    intent: Write, create or remove files
    question: Can I upload file contents to a path on the remote system?
  phrasing_ops: 2
  slug: canonical-files-api
- description: The GroupsService API from Canonical — 8 operation(s) for groupsservice.
  name: Canonical Groups Service API
  phrasing_intents:
  - id: GroupsService_ListGroups
    intent: List identity platform groups
    question: What groups exist in the identity platform admin?
  - id: GroupsService_CreateGroup
    intent: Create a group
    question: How do I add a new group in the identity admin?
  - id: GroupsService_RemoveGroup
    intent: Delete a group
    question: How do I delete a group I no longer need?
  - id: GroupsService_GetGroup
    intent: Get a group
    question: What are the details of a particular group?
  - id: GroupsService_UpdateGroup
    intent: Rename or update a group
    question: Can I rename an existing group?
  - id: GroupsService_ListGroupEntitlements
    intent: List a group's entitlements
    question: What entitlements has a group been granted?
  - id: GroupsService_UpdateGroupEntitlements
    intent: Grant or change a group's entitlements
    question: How do I give a group new entitlements?
  - id: GroupsService_RemoveGroupEntitlement
    intent: Remove one entitlement from a group
    question: How do I revoke a single entitlement from a group?
  phrasing_ops: 14
  slug: canonical-groupsservice-api
- description: The Hardware API (hwapi) API from Canonical — 1 operation(s) for hardware api (hwapi).
  name: Canonical Hardware API (hwapi) API
  phrasing_intents:
  - id: root__get
    intent: Check the hardware API root
    question: Is the hardware certification API up and responding?
  phrasing_ops: 1
  slug: canonical-hardware-api-hwapi-api
- description: The health API from Canonical — 4 operation(s) for health.
  name: Canonical Health API
  phrasing_intents:
  - id: health_retrieve
    intent: Check the API health endpoint
    question: Is the v1 API reporting itself healthy?
  - id: getV1Health
    intent: Get health of Pebble checks
    question: Are my Pebble health checks reporting healthy at the ready level?
  - id: live_health_live_get
    intent: Run the liveness probe
    question: Is the application process up and answering requests?
  - id: ready_health_ready_get
    intent: Run the readiness probe
    question: Is the application ready to serve traffic, including its database connection?
  phrasing_ops: 4
  slug: canonical-health-api
- description: The identities API from Canonical — 15 operation(s) for identities.
  name: Canonical Identities API
  phrasing_intents:
  - id: identities_get
    intent: List URLs of all identities across auth methods
    question: Where can I get the URLs of every identity LXD knows about, whatever the auth method?
  - id: identities_get_bearer
    intent: List URLs of bearer identities
    question: Which bearer-token identities exist on my LXD server, as a list of links?
  - id: identities_post_bearer
    intent: Create a bearer identity
    question: How do I add a new bearer-token identity to LXD?
  - id: identity_delete_bearer_token
    intent: Revoke a bearer identity's token
    question: How can I revoke the token of a bearer identity without deleting the identity itself?
  - id: identity_post_bearer_token
    intent: Issue a new token for a bearer identity
    question: How do I generate a fresh token for an existing bearer identity?
  - id: identity_delete_bearer
    intent: Delete a bearer identity
    question: How do I remove a bearer identity from LXD completely?
  - id: identity_get_bearer
    intent: Get one bearer identity
    question: What groups is a particular bearer identity in?
  - id: identity_patch_bearer
    intent: Partially update a bearer identity
    question: Can I change only some fields of a bearer identity and leave the rest alone?
  phrasing_ops: 28
  slug: canonical-identities-api
- description: The IdentitiesService API from Canonical — 2 operation(s) for identitiesservice.
  name: Canonical Identities Service API
  phrasing_intents:
  - id: IdentitiesService_ListIdentities
    intent: List user identities
    question: Which user identities exist in the identity platform?
  - id: IdentitiesService_CreateIdentity
    intent: Create a user identity
    question: How do I create a new user identity with traits like email and name?
  - id: IdentitiesService_RemoveIdentity
    intent: Delete a user identity
    question: How do I permanently delete a user identity?
  - id: IdentitiesService_GetIdentity
    intent: Get a user identity
    question: What traits and state does a particular identity have?
  - id: IdentitiesService_UpdateIdentity
    intent: Update a user identity
    question: How do I change a user's traits or deactivate their identity?
  phrasing_ops: 5
  slug: canonical-identitiesservice-api
- description: The identity_provider_groups API from Canonical — 3 operation(s) for identity_provider_groups.
  name: Canonical Identity Provider Groups API
  phrasing_intents:
  - id: identity_provider_groups_get
    intent: List identity provider groups as URLs
    question: Which identity provider groups are mapped in LXD?
  - id: identity_provider_groups_post
    intent: Create an identity provider group mapping
    question: How do I map a group from my identity provider onto LXD groups?
  - id: identity_provider_group_delete
    intent: Delete an identity provider group
    question: How do I remove an IdP group mapping from LXD?
  - id: identity_provider_group_get
    intent: Get an identity provider group
    question: Which LXD groups is a particular IdP group mapped to?
  - id: identity_provider_group_patch
    intent: Add groups to an IdP group mapping
    question: Can I add one more LXD group to an existing IdP mapping without replacing it?
  - id: identity_provider_group_post
    intent: Rename an identity provider group
    question: Can I rename an identity provider group mapping in LXD?
  - id: identity_provider_group_put
    intent: Replace an IdP group's mapped groups
    question: How do I overwrite the full list of LXD groups an IdP group maps to?
  - id: identity_provider_groups_get_recursion1
    intent: List identity provider groups with mappings
    question: How do I see every IdP group together with the LXD groups it maps to?
  phrasing_ops: 8
  slug: canonical-identity-provider-groups-api
- description: The IdpsService API from Canonical — 2 operation(s) for idpsservice.
  name: Canonical Idps Service API
  phrasing_intents:
  - id: IdpsService_ListIdps
    intent: List configured identity providers
    question: Which external identity providers are set up for sign-in?
  - id: IdpsService_CreateIdp
    intent: Add an identity provider
    question: How do I connect a new OIDC identity provider for sign-in?
  - id: IdpsService_RemoveIdp
    intent: Remove an identity provider
    question: How do I disconnect a login provider users should no longer sign in with?
  - id: IdpsService_GetIdp
    intent: Get one identity provider
    question: What client ID and issuer is a particular identity provider using?
  - id: IdpsService_UpdateIdp
    intent: Update an identity provider
    question: How do I rotate the client secret on an existing identity provider?
  phrasing_ops: 5
  slug: canonical-idpsservice-api
- description: The images API from Canonical — 19 operation(s) for images.
  name: Canonical Images API
  phrasing_intents:
  - id: images_get
    intent: List images in the Anbox cluster
    question: Which Android images are available in my AMS cluster?
  - id: image_post_import
    intent: Import an image from an image server into AMS
    question: How do I pull an Anbox image into AMS from an image server by name?
  - id: image_post_upload
    intent: Upload a package to create a new AMS image
    question: How do I create an Anbox image in AMS by uploading a gzip, bzip2 or xz package?
  - id: image_get
    intent: Get details of an AMS image by id or name
    question: Can I look up an AMS image using either its id or its name?
  - id: image_delete
    intent: Delete an image stored in AMS
    question: Is there a way to remove an Android image from my AMS cluster entirely?
  - id: image_patch_upload
    intent: Upload a new package version to an existing AMS image
    question: How do I push a new package version to an image that already exists in AMS?
  - id: image_patch_meta
    intent: Update an AMS image's metadata
    question: Can I change an AMS image's settings without re-uploading its package?
  - id: image_version_delete
    intent: Delete one version of an AMS image
    question: How do I delete a single old version of an AMS image and keep the rest?
  phrasing_ops: 31
  slug: canonical-images-api
- description: The instances API from Canonical — 29 operation(s) for instances.
  name: Canonical Instances API
  phrasing_intents:
  - id: instances_get
    intent: List Anbox instances as endpoint URLs
    question: How do I get the URLs of every Anbox instance in AMS?
  - id: instances_post
    intent: Launch a new Anbox instance from an app or image
    question: How do I launch a new Android instance in AMS from an application?
  - id: instances_delete
    intent: Delete several Anbox instances at once
    question: Can I delete a batch of AMS instances by their IDs in one call?
  - id: instances_put
    intent: Change the running state of all instances
    question: Can I stop every instance at once instead of one by one?
  - id: instance_get
    intent: Get details of one Anbox instance
    question: How can I look up a single AMS instance by its ID or name?
  - id: instance_delete
    intent: Delete one Anbox instance
    question: How do I remove a single Anbox instance from AMS?
  - id: instance_patch
    intent: Start or stop one Anbox instance
    question: How do I stop a single Anbox instance without deleting it?
  - id: instance_exec_post
    intent: Run a command inside an Anbox instance
    question: Can I run a shell command inside an Android instance managed by AMS?
  phrasing_ops: 58
  slug: canonical-instances-api
- baseURL: unix:///run/snapd.socket
  baseurl_source: spec
  description: Display and manage interactions between snaps.
  name: Canonical Interfaces API
  phrasing_intents:
  - id: getConnections
    intent: List interface connections
    question: Which plugs and slots are currently connected on this system?
  - id: getInterfaces
    intent: List available interfaces
    question: What snap interfaces are available on this device?
  phrasing_ops: 2
  slug: canonical-interfaces-api
- description: The internal API from Canonical — 1 operation(s) for internal.
  name: Canonical Internal API
  phrasing_intents:
  - id: TenantService_LookupTenants
    intent: Look up tenants for a user
    question: Which tenants does a user with a given email belong to?
  phrasing_ops: 1
  slug: canonical-internal-api
- description: The issues API from Canonical — 6 operation(s) for issues.
  name: Canonical Issues API
  phrasing_intents:
  - id: add_issue_attachments_v1_issues__issue_id__attach_post
    intent: Attach test results to an issue
    question: How do I link failing test results to a known issue?
  - id: remove_issue_attachments_v1_issues__issue_id__detach_post
    intent: Detach test results from an issue
    question: Can I unlink test results that were wrongly attached to an issue?
  - id: post_attachment_rule_v1_issues__issue_id__attachment_rules_post
    intent: Create an auto-attachment rule for an issue
    question: Can new test results be attached to an issue automatically when they match certain criteria?
  - id: patch_attachment_rule_v1_issues__issue_id__attachment_rules__attachment_rule_id__patch
    intent: Enable or disable an attachment rule
    question: Can I temporarily pause an issue's attachment rule without deleting it?
  - id: delete_attachment_rule_v1_issues__issue_id__attachment_rules__attachment_rule_id__delete
    intent: Delete an issue attachment rule
    question: How do I remove an automatic attachment rule from an issue?
  - id: get_issues_v1_issues_get
    intent: List tracked issues
    question: Which known issues are being tracked against test results?
  - id: create_or_update_issue_v1_issues_put
    intent: Create or update an issue by URL
    question: How do I register a bug tracker issue so test results can be linked to it?
  - id: get_issue_v1_issues__issue_id__get
    intent: Get one issue
    question: Where can I see a tracked issue and its attached test results?
  phrasing_ops: 9
  slug: canonical-issues-api
- description: The layers API from Canonical — 1 operation(s) for layers.
  name: Canonical Layers API
  phrasing_intents:
  - id: postV1Layers
    intent: Add a layer to the plan
    question: How do I add a configuration layer to the Pebble plan at runtime?
  phrasing_ops: 1
  slug: canonical-layers-api
- description: Manages local repositories.
  name: Canonical Local Service API
  phrasing_intents:
  - id: LocalService_ListLocals
    intent: List local Debian repositories
    question: Which local package repositories have been set up in debarchive?
  - id: LocalService_CreateLocal
    intent: Create a local Debian repository
    question: How do I create a new local repository for my own packages?
  - id: LocalService_GetLocal
    intent: Get a local repository
    question: What distribution and component is a given local repository set to?
  - id: LocalService_DeleteLocal
    intent: Delete a local repository
    question: How do I delete a local repository I no longer need?
  - id: LocalService_UpdateLocal
    intent: Update a local repository
    question: How do I rename a local repository or change its default distribution?
  - id: LocalService_ListLocalPackages
    intent: List packages in a local repository
    question: Which packages are available in one of my local repositories?
  - id: LocalService_ImportLocalPackages
    intent: Import packages into a local repository
    question: How do I import packages into a local repo from a package index URL?
  - id: LocalService_BatchGetLocals
    intent: Fetch several local repositories by name
    question: Can I retrieve several local repositories by name in one call?
  phrasing_ops: 8
  slug: canonical-localservice-api
- description: The logs API from Canonical — 1 operation(s) for logs.
  name: Canonical Logs API
  phrasing_intents:
  - id: getV1Logs
    intent: Get service logs
    question: How do I see the recent log output of a Pebble service?
  phrasing_ops: 1
  slug: canonical-logs-api
- description: The Metadata API from Canonical — 1 operation(s) for metadata.
  name: Canonical Metadata API
  phrasing_intents:
  - id: metadata_configuration_get
    intent: Get LXD metadata configuration
    question: Where can I get the generated metadata describing all LXD configuration keys?
  phrasing_ops: 1
  slug: canonical-metadata-api
- description: The metrics API from Canonical — 2 operation(s) for metrics.
  name: Canonical Metrics API
  phrasing_intents:
  - id: metrics_get
    intent: Get instance metrics
    question: How much CPU and memory are my instances using?
  - id: getV1Metrics
    intent: Get Pebble service and check metrics
    question: Can I scrape Pebble service and health check metrics in OpenMetrics format?
  phrasing_ops: 2
  slug: canonical-metrics-api
- description: The MetricsService API from Canonical — 1 operation(s) for metricsservice.
  name: Canonical Metrics Service API
  phrasing_intents:
  - id: MetricsService_ListMetrics
    intent: List identity platform metrics
    question: What metrics does the identity platform admin service expose?
  phrasing_ops: 1
  slug: canonical-metricsservice-api
- description: Methods for managing repository mirrors.
  name: Canonical Mirror Service API
  phrasing_intents:
  - id: MirrorService_ListMirrors
    intent: List package mirrors
    question: Which package mirrors have I set up?
  - id: MirrorService_CreateMirror
    intent: Create a Debian archive mirror
    question: How do I set up a mirror of an upstream Debian or Ubuntu archive?
  - id: MirrorService_GetMirror
    intent: Get a mirror's details
    question: When did a mirror last download from upstream?
  - id: MirrorService_DeleteMirror
    intent: Delete a mirror
    question: How do I remove a mirror I no longer need?
  - id: MirrorService_UpdateMirror
    intent: Change a mirror's upstream settings
    question: Can I add architectures or components to an existing mirror?
  - id: MirrorService_ListMirrorPackages
    intent: List packages in a mirror
    question: Which packages are available in my mirror?
  - id: MirrorService_SyncMirror
    intent: Sync a mirror with its upstream
    question: How do I pull the latest packages into a mirror?
  - id: MirrorService_BatchGetMirrors
    intent: Look up several mirrors by name
    question: Can I fetch several mirrors in one request by name?
  phrasing_ops: 8
  slug: canonical-mirrorservice-api
- description: The network-acls API from Canonical — 4 operation(s) for network-acls.
  name: Canonical Network Acls API
  phrasing_intents:
  - id: network_acls_get
    intent: List URLs of network ACLs
    question: Which network ACLs are defined in a project, as links?
  - id: network_acls_post
    intent: Create a network ACL
    question: How do I create a firewall ACL for LXD networks?
  - id: network_acl_delete
    intent: Delete a network ACL
    question: How do I remove a network ACL I no longer need?
  - id: network_acl_get
    intent: Get one network ACL
    question: What rules does a specific network ACL have?
  - id: network_acl_patch
    intent: Change part of a network ACL
    question: Can I update only an ACL's description or config keys?
  - id: network_acl_post
    intent: Rename a network ACL
    question: Can I rename a network ACL?
  - id: network_acl_put
    intent: Replace a network ACL's full rule set
    question: How do I replace all of an ACL's rules at once?
  - id: network_acl_log_get
    intent: Read a network ACL's log
    question: Which traffic did a network ACL block or allow?
  phrasing_ops: 9
  slug: canonical-network-acls-api
- description: The network-allocations API from Canonical — 1 operation(s) for network-allocations.
  name: Canonical Network Allocations API
  phrasing_intents:
  - id: network_allocations_get
    intent: List IP and network allocations in use
    question: Which addresses are in use by networks, forwards, load balancers and instances?
  phrasing_ops: 1
  slug: canonical-network-allocations-api
- description: The network-forwards API from Canonical — 3 operation(s) for network-forwards.
  name: Canonical Network Forwards API
  phrasing_intents:
  - id: network_forwards_get
    intent: List network address forward URLs
    question: Which address forwards are set up on an LXD network?
  - id: network_forwards_post
    intent: Create a network address forward
    question: How do I forward an external listen address to an instance on an LXD network?
  - id: network_forward_delete
    intent: Delete a network address forward
    question: How do I stop forwarding a listen address on an LXD network?
  - id: network_forward_get
    intent: Get a network address forward
    question: What ports and target does a specific address forward use?
  - id: network_forward_patch
    intent: Partially update a network address forward
    question: Can I change just the description of an address forward?
  - id: network_forward_put
    intent: Replace a network address forward
    question: How do I overwrite all port rules of an address forward?
  - id: network_forward_get_recursion1
    intent: List network forwards with details
    question: Can I get every network forward with its ports and config expanded?
  phrasing_ops: 7
  slug: canonical-network-forwards-api
- description: The network-load-balancer-pools API from Canonical — 3 operation(s) for network-load-balancer-pools.
  name: Canonical Network Load Balancer Pools API
  phrasing_intents:
  - id: network_load_balancer_pools_get
    intent: List a network's load balancer pools
    question: Which load balancer pools exist on one of my LXD networks?
  - id: network_load_balancer_pools_post
    intent: Create a network load balancer pool
    question: How do I group instances into a load balancer pool?
  - id: network_load_balancer_pool_delete
    intent: Delete a network load balancer pool
    question: How do I remove a load balancer pool from a network?
  - id: network_load_balancer_pool_get
    intent: Get a network load balancer pool
    question: Which instances belong to a particular load balancer pool?
  - id: network_load_balancer_pool_put
    intent: Update a network load balancer pool
    question: How do I change which instances are in a load balancer pool?
  - id: network_load_balancer_pool_state_get
    intent: Get the state of a load balancer pool
    question: Are the members of my load balancer pool healthy right now?
  phrasing_ops: 6
  slug: canonical-network-load-balancer-pools-api
- description: The network-load-balancers API from Canonical — 3 operation(s) for network-load-balancers.
  name: Canonical Network Load Balancers API
  phrasing_intents:
  - id: network_load_balancers_get
    intent: List a network's load balancers as URLs
    question: Which load balancers are defined on one of my LXD networks?
  - id: network_load_balancers_post
    intent: Create a network load balancer
    question: How do I create a load balancer on an LXD network listening on an address?
  - id: network_load_balancer_delete
    intent: Delete a network load balancer
    question: Is there a way to remove a load balancer from an LXD network?
  - id: network_load_balancer_get
    intent: Get a network load balancer
    question: What backends and ports does a specific load balancer use?
  - id: network_load_balancer_patch
    intent: Partially update a network load balancer
    question: Can I change only the description of a network load balancer?
  - id: network_load_balancer_put
    intent: Replace a network load balancer's configuration
    question: How do I overwrite all backends and ports on a load balancer?
  - id: network_load_balancer_get_recursion1
    intent: List a network's load balancers with details
    question: How do I get every load balancer on a network with backends and ports in one call?
  phrasing_ops: 7
  slug: canonical-network-load-balancers-api
- description: The network-peers API from Canonical — 3 operation(s) for network-peers.
  name: Canonical Network Peers API
  phrasing_intents:
  - id: network_peers_get
    intent: List URLs of a network's peerings
    question: Which peerings does an OVN network have, as links?
  - id: network_peers_post
    intent: Create a network peering
    question: How do I peer two LXD networks so they can route to each other?
  - id: network_peer_delete
    intent: Delete a network peering
    question: How do I remove the peering between two networks?
  - id: network_peer_get
    intent: Get one network peering
    question: What's the status of a specific network peering?
  - id: network_peer_patch
    intent: Change part of a peering's configuration
    question: Can I change just a peering's description?
  - id: network_peer_put
    intent: Replace a peering's configuration
    question: How do I overwrite a peering's whole configuration?
  - id: network_peer_get_recursion1
    intent: List a network's peerings with full details
    question: Can I see every peering's target network and status in one call?
  phrasing_ops: 7
  slug: canonical-network-peers-api
- description: The network-zones API from Canonical — 6 operation(s) for network-zones.
  name: Canonical Network Zones API
  phrasing_intents:
  - id: network_zones_get
    intent: List network zones as URLs
    question: Which DNS network zones are defined on my LXD server?
  - id: network_zones_post
    intent: Create a network zone
    question: How do I create a new DNS zone for my LXD networks?
  - id: network_zone_delete
    intent: Delete a network zone
    question: Can I remove a DNS network zone I no longer use?
  - id: network_zone_get
    intent: Get a network zone
    question: What configuration does a particular network zone have?
  - id: network_zone_patch
    intent: Partially update a network zone
    question: Can I change only the description of a network zone?
  - id: network_zone_put
    intent: Replace a network zone's configuration
    question: How do I overwrite a network zone's entire config at once?
  - id: network_zone_records_get
    intent: List records in a network zone as URLs
    question: Which DNS records exist in one of my network zones?
  - id: network_zone_records_post
    intent: Add a DNS record to a network zone
    question: How do I add a custom DNS record to an LXD network zone?
  phrasing_ops: 14
  slug: canonical-network-zones-api
- description: The networks API from Canonical — 5 operation(s) for networks.
  name: Canonical Networks API
  phrasing_intents:
  - id: networks_get
    intent: List network URLs
    question: Which networks are defined on my LXD server?
  - id: networks_post
    intent: Create a network
    question: How do I create a new bridge network in LXD?
  - id: network_delete
    intent: Delete a network
    question: How do I remove a network I no longer use?
  - id: network_get
    intent: Get one network's configuration
    question: How do I see the configuration of a specific network?
  - id: network_patch
    intent: Change some settings of a network
    question: Can I change one key like ipv4.address without resending the full config?
  - id: network_post
    intent: Rename a network
    question: How do I rename an existing network?
  - id: network_put
    intent: Replace a network's configuration
    question: Can I replace every setting of a network in one go?
  - id: networks_leases_get
    intent: List a network's DHCP leases
    question: Which IP addresses has a network's DHCP server handed out?
  phrasing_ops: 10
  slug: canonical-networks-api
- description: The nodes API from Canonical — 3 operation(s) for nodes.
  name: Canonical Nodes API
  phrasing_intents:
  - id: nodes_get
    intent: List Anbox nodes
    question: Which nodes does AMS know about in my Anbox Cloud cluster?
  - id: node_post
    intent: Add a node to AMS
    question: How do I add a new LXD node to Anbox Cloud?
  - id: node_get
    intent: Get one Anbox node
    question: What resources does a specific AMS node have?
  - id: node_delete
    intent: Delete an Anbox node
    question: How do I remove a node from AMS?
  - id: node_patch
    intent: Update an Anbox node
    question: How do I stop new containers from being scheduled on a node?
  - id: nodes_get_recursion1
    intent: List Anbox nodes with full details
    question: Can I get every node's CPU, memory and GPU slots in one call?
  phrasing_ops: 6
  slug: canonical-nodes-api
- baseURL: unix:///run/snapd.socket
  baseurl_source: spec
  description: The notices API from Canonical — 4 operation(s) for notices.
  name: Canonical Notices API
  phrasing_intents:
  - id: getV1Notices
    intent: List Pebble notices
    question: Which notices has the Pebble daemon recorded?
  - id: postV1Notices
    intent: Record a custom Pebble notice
    question: How do I record my own custom notice in Pebble?
  - id: getV1NoticesById
    intent: Get one Pebble notice
    question: What does a single Pebble notice contain?
  - id: getNotices
    intent: List system notices
    question: What notices has snapd recorded for me recently?
  - id: postNotices
    intent: Create a snap-run-inhibit notice
    question: Can I create a notice through the API, and which types are allowed?
  - id: getNoticeByID
    intent: Get one notice
    question: What does a specific notice contain?
  phrasing_ops: 6
  slug: canonical-notices-api
- description: The notifications API from Canonical — 6 operation(s) for notifications.
  name: Canonical Notifications API
  phrasing_intents:
  - id: get_own_notifications_v1_users_me_notifications_get
    intent: List my Test Observer notifications
    question: What notifications do I have waiting in Test Observer?
  - id: get_own_notification_count_v1_users_me_notifications_count_get
    intent: Count my notifications
    question: How many notifications do I have?
  - id: mark_own_notification_as_read_v1_users_me_notifications__notification_id__dismiss_post
    intent: Dismiss one of my notifications
    question: How do I mark one of my own notifications as read?
  - id: get_notifications_v1_users__user_id__notifications_get
    intent: List another user's notifications
    question: Can I view the notifications of a specific Test Observer user?
  - id: get_notification_count_v1_users__user_id__notifications_count_get
    intent: Count a user's notifications
    question: How many notifications does a given user have?
  - id: mark_notification_as_read_v1_users__user_id__notifications__notification_id__dismiss_post
    intent: Dismiss a notification for a user
    question: Can I mark a notification as read on behalf of another user?
  phrasing_ops: 6
  slug: canonical-notifications-api
- baseURL: https://testflinger.ps7.canonical.com/
  baseurl_source: declared
  description: The Oidc_Api API from Canonical — 2 operation(s) for oidc_api.
  name: Canonical Oidc API
  phrasing_intents:
  - id: postOidcAuthInit
    intent: Start an OIDC sign-in
    question: How does a client begin authenticating through the OIDC provider?
  - id: postOidcAuthPollByRequestId
    intent: Poll for an OIDC sign-in result
    question: Has my OIDC login finished yet?
  phrasing_ops: 2
  slug: canonical-oidc-api-api
- description: The oidc_sessions API from Canonical — 3 operation(s) for oidc_sessions.
  name: Canonical Oidc Sessions API
  phrasing_intents:
  - id: oidc_sessions_get
    intent: List OIDC session URLs
    question: Which OIDC login sessions are open on my LXD server, as links?
  - id: oidc_session_delete
    intent: End an OIDC session
    question: How do I force a user's OIDC session to end?
  - id: oidc_session_get
    intent: Get one OIDC session
    question: What are the details of a specific OIDC session?
  - id: oidc_sessions_get_recursion1
    intent: List OIDC sessions with full details
    question: Can I see full details of every OIDC session, like when each expires?
  phrasing_ops: 4
  slug: canonical-oidc-sessions-api
- description: The operations API from Canonical — 10 operation(s) for operations.
  name: Canonical Operations API
  phrasing_intents:
  - id: operations_get
    intent: List running and queued AMS operations
    question: Which background operations are in progress or queued on my Anbox Management Service?
  - id: operation_get
    intent: Check the status of an AMS operation
    question: What is the current status of an AMS operation I started?
  - id: operation_delete
    intent: Cancel an AMS operation
    question: How do I cancel a long-running AMS operation?
  - id: operation_wait_get
    intent: Wait for an AMS operation to finish
    question: Can I block until an AMS operation reaches a final status?
  - id: operation_websocket_get
    intent: Open a websocket to an AMS operation
    question: How do I attach to the stdin and stdout of an AMS exec operation?
  - id: operations_get_recursion1
    intent: List AMS operations with full details
    question: How do I see the status and progress of every queued AMS operation in one call?
  - id: delete10OperationsById
    intent: Cancel an LXD operation
    question: How do I cancel a running LXD operation?
  - id: get10OperationsById
    intent: Get the state of an LXD operation
    question: What state is a background LXD operation in right now?
  phrasing_ops: 12
  slug: canonical-operations-api
- description: Manages long-running operations.
  name: Canonical Operation Service API
  phrasing_intents:
  - id: OperationService_GetOperation
    intent: Get the state of a long-running operation
    question: Has my long-running operation finished yet?
  - id: OperationService_BatchGetOperations
    intent: Get several long-running operations at once
    question: Can I check the status of many operations in one request?
  phrasing_ops: 2
  slug: canonical-operationservice-api
- description: The permissions API from Canonical — 3 operation(s) for permissions.
  name: Canonical Permissions API
  phrasing_intents:
  - id: permissions_get
    intent: List available LXD permissions
    question: Which permissions can I grant on LXD entities?
  - id: permissions_get_recursion1
    intent: List LXD permissions with the groups holding them
    question: Which groups hold each LXD permission?
  - id: get_permissions_v1_permissions_get
    intent: Get my permissions in the v1 service
    question: What permissions does my account have in the v1 service?
  phrasing_ops: 3
  slug: canonical-permissions-api
- description: The placement-groups API from Canonical — 3 operation(s) for placement-groups.
  name: Canonical Placement Groups API
  phrasing_intents:
  - id: placement_groups_get
    intent: List placement group URLs
    question: Which placement groups exist in my LXD project?
  - id: placement_groups_post
    intent: Create a placement group
    question: How do I add a placement group to an LXD project?
  - id: placement_group_delete
    intent: Delete a placement group
    question: How do I remove a placement group I no longer need?
  - id: placement_group_get
    intent: Get a placement group
    question: What is configured on a specific placement group?
  - id: placement_group_patch
    intent: Partially update a placement group
    question: Is it possible to change only some of a placement group's settings?
  - id: placement_group_post
    intent: Rename a placement group
    question: Can I rename an existing placement group?
  - id: placement_group_put
    intent: Replace a placement group
    question: How do I overwrite a placement group's full configuration?
  - id: placement_groups_get_recursion1
    intent: List placement groups with details
    question: Can I list placement groups with their full configuration expanded?
  phrasing_ops: 8
  slug: canonical-placement-groups-api
- description: The plan API from Canonical — 1 operation(s) for plan.
  name: Canonical Plan API
  phrasing_intents:
  - id: getV1Plan
    intent: Get the current plan
    question: What does the combined Pebble plan currently look like?
  phrasing_ops: 1
  slug: canonical-plan-api
- description: The profiles API from Canonical — 3 operation(s) for profiles.
  name: Canonical Profiles API
  phrasing_intents:
  - id: profiles_get
    intent: List URLs of LXD profiles
    question: Which instance profiles exist in a project, as links?
  - id: profiles_post
    intent: Create an instance profile
    question: How do I create a reusable profile for LXD instances?
  - id: profile_delete
    intent: Delete an instance profile
    question: How do I remove a profile I no longer use?
  - id: profile_get
    intent: Get one instance profile
    question: What config and devices does a particular profile set?
  - id: profile_patch
    intent: Change some of a profile's settings
    question: Can I tweak one profile key without resending the whole profile?
  - id: profile_post
    intent: Rename an instance profile
    question: Can I rename an LXD profile?
  - id: profile_put
    intent: Replace a profile's entire configuration
    question: How do I overwrite a profile's config and devices completely?
  - id: profiles_get_recursion1
    intent: List LXD profiles with full config
    question: Can I see every profile's devices and config in one call?
  phrasing_ops: 8
  slug: canonical-profiles-api
- description: The projects API from Canonical — 4 operation(s) for projects.
  name: Canonical Projects API
  phrasing_intents:
  - id: projects_get
    intent: List URLs of LXD projects
    question: Which projects exist on my LXD server, as a list of links?
  - id: projects_post
    intent: Create an LXD project
    question: How do I create a new project to isolate instances in LXD?
  - id: project_delete
    intent: Delete an LXD project
    question: How do I remove a project from LXD?
  - id: project_get
    intent: Get one LXD project
    question: What's the configuration of a particular project?
  - id: project_patch
    intent: Change some of a project's settings
    question: Can I change one project setting without resending the rest?
  - id: project_post
    intent: Rename an LXD project
    question: Can I rename an existing LXD project?
  - id: project_put
    intent: Replace a project's entire configuration
    question: How do I overwrite a project's whole configuration?
  - id: project_state_get
    intent: Get a project's resource usage
    question: How much CPU, memory and disk is a project consuming?
  phrasing_ops: 10
  slug: canonical-projects-api
- description: Manages the publication of Debian artifacts.
  name: Canonical Publication Service API
  phrasing_intents:
  - id: PublicationService_ListPublications
    intent: List publications
    question: Which repository publications have I configured?
  - id: PublicationService_CreatePublication
    intent: Create a repository publication
    question: How do I define a publication that pushes a package source to a target?
  - id: PublicationService_GetPublication
    intent: Get a publication
    question: How do I look up one publication's settings?
  - id: PublicationService_DeletePublication
    intent: Delete a publication
    question: How do I remove a publication?
  - id: PublicationService_UpdatePublication
    intent: Change a publication's settings
    question: Can I change a publication's target or source?
  - id: PublicationService_PublishPublication
    intent: Publish a publication to its target
    question: How do I push a publication out to its target now?
  phrasing_ops: 6
  slug: canonical-publicationservice-api
- description: Manages the storage destinations for publishing Debian archives.
  name: Canonical Publication Target Service API
  phrasing_intents:
  - id: PublicationTargetService_ListPublicationTargets
    intent: List publication targets
    question: Which publication targets are configured for my mirrors?
  - id: PublicationTargetService_CreatePublicationTarget
    intent: Create a publication target
    question: How do I add a new place to publish artifacts, such as S3, Swift or a filesystem path?
  - id: PublicationTargetService_GetPublicationTarget
    intent: Get a publication target
    question: What storage backend does a given publication target use?
  - id: PublicationTargetService_DeletePublicationTarget
    intent: Delete a publication target
    question: Does deleting a publication target also remove the artifacts already published there?
  - id: PublicationTargetService_UpdatePublicationTarget
    intent: Update a publication target
    question: Can I rename a publication target or change its backend?
  - id: PublicationTargetService_BatchGetPublicationTargets
    intent: Fetch several publication targets by name
    question: Can I retrieve a handful of publication targets by name in a single request?
  phrasing_ops: 6
  slug: canonical-publicationtargetservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The region API from Canonical — 1 operation(s) for region.
  name: Canonical Region API
  phrasing_intents:
  - id: handle-get-regions
    intent: List Anbox Cloud streaming regions
    question: Which Anbox Cloud regions can I stream Android containers from?
  phrasing_ops: 1
  slug: canonical-region-api
- description: The replicators API from Canonical — 4 operation(s) for replicators.
  name: Canonical Replicators API
  phrasing_intents:
  - id: replicators_get
    intent: List replicators as URLs
    question: Which replicators are configured on my LXD cluster?
  - id: replicators_post
    intent: Create a replicator
    question: How do I set up a new replicator for a project?
  - id: replicator_delete
    intent: Delete a replicator
    question: How do I remove a replicator I no longer need?
  - id: replicator_get
    intent: Get a replicator
    question: What configuration does a particular replicator have?
  - id: replicator_patch
    intent: Partially update a replicator
    question: Can I change just the description of a replicator?
  - id: replicator_post
    intent: Rename a replicator
    question: Is it possible to rename an existing replicator?
  - id: replicator_put
    intent: Replace a replicator's configuration
    question: How do I overwrite a replicator's full configuration?
  - id: replicator_state_get
    intent: Get a replicator's current state
    question: Is my replicator currently running, and what did its last run do?
  phrasing_ops: 10
  slug: canonical-replicators-api
- description: The reports API from Canonical — 2 operation(s) for reports.
  name: Canonical Reports API
  phrasing_intents:
  - id: get_testresults_report_v1_reports_test_results_get
    intent: Export a CSV of artefacts with test results
    question: Can I download a CSV of every artefact and its test results for a date range?
  - id: get_test_execution_reports_v1_reports_test_executions_get
    intent: Export a CSV of test executions with environments
    question: Can I get a CSV of all test executions with their environment details?
  phrasing_ops: 2
  slug: canonical-reports-api
- description: The RolesService API from Canonical — 5 operation(s) for rolesservice.
  name: Canonical Roles Service API
  phrasing_intents:
  - id: RolesService_ListRoles
    intent: List roles
    question: Which roles exist in the identity platform admin?
  - id: RolesService_CreateRole
    intent: Create a role
    question: How do I define a new role for access control?
  - id: RolesService_RemoveRole
    intent: Delete a role
    question: How do I delete a role I no longer use?
  - id: RolesService_GetRole
    intent: Get a role
    question: What is the name of the role with a given id?
  - id: RolesService_UpdateRole
    intent: Rename a role
    question: Can I rename an existing role?
  - id: RolesService_ListRoleEntitlements
    intent: List a role's entitlements
    question: Which permissions does a particular role grant?
  - id: RolesService_UpdateRoleEntitlements
    intent: Add or change a role's entitlements
    question: How do I grant extra permissions to a role?
  - id: RolesService_RemoveRoleEntitlement
    intent: Remove an entitlement from a role
    question: How do I revoke a single permission from a role?
  phrasing_ops: 9
  slug: canonical-rolesservice-api
- baseURL: unix:///run/snapd.socket
  baseurl_source: spec
  description: Requires the user to authenticate with root access.
  name: Canonical Root API
  phrasing_intents:
  - id: getUsers
    intent: List user accounts on the system
    question: Which user accounts exist on this system?
  - id: manageUsers
    intent: Create or remove a local user
    question: How do I create a local user from a store account email?
  phrasing_ops: 2
  slug: canonical-root-api
- description: The schema API from Canonical — 1 operation(s) for schema.
  name: Canonical Schema API
  phrasing_intents:
  - id: schema_retrieve
    intent: Download the API's OpenAPI schema
    question: Can I download the OpenAPI 3 schema for this API?
  phrasing_ops: 1
  slug: canonical-schema-api
- description: The SchemasService API from Canonical — 3 operation(s) for schemasservice.
  name: Canonical Schemas Service API
  phrasing_intents:
  - id: SchemasService_ListSchemas
    intent: List identity schemas
    question: Which identity schemas are defined in the Identity Platform?
  - id: SchemasService_CreateSchema
    intent: Create an identity schema
    question: How do I add a new identity schema that defines user traits?
  - id: SchemasService_RemoveSchema
    intent: Delete an identity schema
    question: How do I delete an identity schema that's no longer used?
  - id: SchemasService_GetSchema
    intent: Get an identity schema
    question: What traits does a particular identity schema define?
  - id: SchemasService_UpdateSchema
    intent: Update an identity schema
    question: How do I change the definition of an existing identity schema?
  - id: SchemasService_GetDefaultSchema
    intent: Get the default identity schema
    question: Which identity schema is used by default for new identities?
  - id: SchemasService_UpdateDefaultSchema
    intent: Change the default identity schema
    question: How do I switch which identity schema is the default?
  phrasing_ops: 7
  slug: canonical-schemasservice-api
- description: The Security API from Canonical — 15 operation(s) for security.
  name: Canonical Security API
  phrasing_intents:
  - id: getSecurityCompatNoticesJson
    intent: List security notices (compat format)
    question: Is there a backward-compatible feed of Ubuntu security notices?
  - id: getSecurityCompatNotices{noticeId}Json
    intent: Get one security notice (compat format)
    question: Can I fetch a single USN in the older compat format?
  - id: getSecurityCvesJson
    intent: Search CVEs
    question: Which CVEs affect a given Ubuntu package?
  - id: getSecurityCves{cveId}Json
    intent: Get one CVE
    question: What is Ubuntu's status and priority for a specific CVE?
  - id: getSecurityNoticesJson
    intent: List Ubuntu security notices
    question: Which Ubuntu Security Notices were published for noble?
  - id: getSecurityNotices{noticeId}Json
    intent: Get one Ubuntu security notice
    question: What does a specific USN fix and which packages does it update?
  - id: getSecurityPageNoticesJson
    intent: List notices for the security web page
    question: Is there a notices listing shaped for the security notices web page?
  - id: getSecurityReleasesJson
    intent: List Ubuntu releases
    question: Which Ubuntu releases does the security tracker cover?
  phrasing_ops: 17
  slug: canonical-security-api
- description: The Sentry Debug API from Canonical — 1 operation(s) for sentry debug.
  name: Canonical Sentry Debug API
  phrasing_intents:
  - id: trigger_error_sentry_debug_get
    intent: Trigger a test error for error monitoring
    question: Is error reporting wired up correctly on this service?
  phrasing_ops: 1
  slug: canonical-sentry-debug-api
- description: The server API from Canonical — 5 operation(s) for server.
  name: Canonical Server API
  phrasing_intents:
  - id: api_get
    intent: List supported API versions
    question: Which API versions does this LXD server support?
  - id: server_get
    intent: Get the server environment and config
    question: How do I see the full LXD server configuration and environment?
  - id: server_patch
    intent: Change some server settings
    question: How do I set one server option like core.https_address?
  - id: server_put
    intent: Replace the server configuration
    question: Can I replace the entire LXD server configuration at once?
  - id: events_get
    intent: Stream server events
    question: How do I subscribe to live LXD events over a websocket?
  - id: resources_get
    intent: Get the server's hardware inventory
    question: What CPUs, memory and GPUs does my LXD host have?
  - id: server_get_untrusted
    intent: Get public server info for untrusted clients
    question: What server details can an unauthenticated client see?
  phrasing_ops: 7
  slug: canonical-server-api
- description: The service API from Canonical — 2 operation(s) for service.
  name: Canonical Service API
  phrasing_intents:
  - id: service_get
    intent: Check AMS status and supported extensions
    question: Is the Anbox Management Service up, and which API extensions does it support?
  - id: version_get
    intent: Get the running AMS version
    question: What version of the Anbox Management Service is running?
  phrasing_ops: 2
  slug: canonical-service-api
- description: The services API from Canonical — 1 operation(s) for services.
  name: Canonical Services API
  phrasing_intents:
  - id: getV1Services
    intent: List services
    question: Which Pebble services are running and which are stopped?
  - id: postV1Services
    intent: Start, stop or restart services
    question: How do I restart a service managed by Pebble?
  phrasing_ops: 2
  slug: canonical-services-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The session API from Canonical — 8 operation(s) for session.
  name: Canonical Session API
  phrasing_intents:
  - id: handle-adb-connect-session
    intent: Attach to a streaming session as an ADB client
    question: How do I connect ADB to a running Anbox streaming session?
  - id: handle-master-connect-session
    intent: Attach to a streaming session as master
    question: What websocket does the master client use to drive a streaming session?
  - id: handle-slave-connect-session
    intent: Attach to a streaming session as a secondary client
    question: How does a secondary viewer connect to someone else's streaming session?
  - id: handle-get-sessions
    intent: List streaming sessions
    question: How do I see all the Anbox streaming sessions currently running?
  - id: handle-new-session
    intent: Start a new streaming session for an app
    question: How do I start streaming an Android app to a user?
  - id: handle-delete-sessions
    intent: Delete several streaming sessions at once
    question: Can I end a batch of streaming sessions in one call?
  - id: handle-get-session
    intent: Get a streaming session by ID
    question: How do I check the status of one streaming session?
  - id: handle-delete-session
    intent: End and delete one streaming session
    question: How do I stop and remove a single streaming session?
  phrasing_ops: 11
  slug: canonical-session-api
- description: The signals API from Canonical — 1 operation(s) for signals.
  name: Canonical Signals API
  phrasing_intents:
  - id: postV1Signals
    intent: Send a signal to services
    question: How do I send SIGHUP to a service so it reloads its config?
  phrasing_ops: 1
  slug: canonical-signals-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The status API from Canonical — 1 operation(s) for status.
  name: Canonical Status API
  phrasing_intents:
  - id: handle-get-status
    intent: Check Anbox Stream Gateway health
    question: Is the Anbox Stream Gateway healthy right now?
  phrasing_ops: 1
  slug: canonical-status-api
- description: The StatusService API from Canonical — 2 operation(s) for statusservice.
  name: Canonical Status Service API
  phrasing_intents:
  - id: StatusService_GetStatus
    intent: Check service status
    question: Is the service up and healthy right now?
  - id: StatusService_GetVersion
    intent: Get the running service version
    question: Which version of the service is deployed?
  phrasing_ops: 2
  slug: canonical-statusservice-api
- description: The storage API from Canonical — 29 operation(s) for storage.
  name: Canonical Storage API
  phrasing_intents:
  - id: storage_pools_get
    intent: List storage pool URLs
    question: Which storage pools exist on my LXD server, just as a list of URLs?
  - id: storage_pools_post
    intent: Create a storage pool
    question: How do I add a new storage pool to LXD with a specific driver like zfs or btrfs?
  - id: storage_pool_bucket_delete
    intent: Delete a storage bucket
    question: How do I remove an object storage bucket from a pool?
  - id: storage_pool_bucket_patch
    intent: Change some bucket settings
    question: Can I change only a bucket's size limit without touching other settings?
  - id: storage_pool_bucket_put
    intent: Replace a bucket's configuration
    question: How do I overwrite all of a bucket's settings at once?
  - id: storage_pool_bucket_key_delete
    intent: Revoke a bucket access key
    question: How do I revoke an access key so it can no longer reach the bucket?
  - id: storage_pool_bucket_key_put
    intent: Update a bucket access key
    question: How do I change the role on an existing bucket key?
  - id: storage_pool_resources
    intent: Check storage pool usage
    question: How much space is used and free in a storage pool?
  phrasing_ops: 52
  slug: canonical-storage-api
- description: The system info API from Canonical — 1 operation(s) for system info.
  name: Canonical system info API
  phrasing_intents:
  - id: getV1SystemInfo
    intent: Get Pebble system information
    question: Which version of Pebble is running?
  phrasing_ops: 1
  slug: canonical-system-info-api
- description: The tasks API from Canonical — 1 operation(s) for tasks.
  name: Canonical Tasks API
  phrasing_intents:
  - id: tasks_get
    intent: List AMS tasks
    question: Which background tasks is AMS running?
  phrasing_ops: 1
  slug: canonical-tasks-api
- description: The teams API from Canonical — 3 operation(s) for teams.
  name: Canonical Teams API
  phrasing_intents:
  - id: get_teams_v1_teams_get
    intent: List teams
    question: Which teams are set up in Test Observer?
  - id: create_team_v1_teams_post
    intent: Create a team
    question: How do I create a new review team?
  - id: get_team_v1_teams__team_id__get
    intent: Get a team
    question: Who is on a particular team and what can they do?
  - id: update_team_v1_teams__team_id__patch
    intent: Update a team's permissions or matching rules
    question: Can I change the permissions of an existing team?
  - id: add_team_member_v1_teams__team_id__members__user_id__post
    intent: Add a user to a team
    question: How do I add a reviewer to a team?
  - id: remove_team_member_v1_teams__team_id__members__user_id__delete
    intent: Remove a user from a team
    question: How do I take someone off a team?
  phrasing_ops: 6
  slug: canonical-teams-api
- description: The TenantService API from Canonical — 8 operation(s) for tenantservice.
  name: Canonical Tenant Service API
  phrasing_intents:
  - id: TenantService_ListMyTenants
    intent: List the tenants I belong to
    question: Which tenants is my own account a member of?
  - id: TenantService_ListTenants
    intent: List all tenants as an admin
    question: As an administrator, how do I list every tenant in the system?
  - id: TenantService_CreateTenant
    intent: Create a tenant
    question: How do I create a new tenant?
  - id: TenantService_DeleteTenant
    intent: Delete a tenant
    question: Can I permanently remove a tenant?
  - id: TenantService_UpdateTenant
    intent: Update a tenant
    question: How do I rename or disable an existing tenant?
  - id: TenantService_InviteMember
    intent: Invite someone to a tenant
    question: How do I invite a colleague by email to join a tenant?
  - id: TenantService_ListTenantUsers
    intent: List users in a tenant
    question: Who are the users in a given tenant?
  - id: TenantService_ProvisionUser
    intent: Add a user directly to a tenant
    question: Can I add a user to a tenant straight away without sending an invite?
  phrasing_ops: 11
  slug: canonical-tenantservice-api
- description: The test-cases API from Canonical — 3 operation(s) for test-cases.
  name: Canonical Test Cases API
  phrasing_intents:
  - id: get_reported_issues_v1_test_cases_reported_issues_get
    intent: List issues reported against test cases
    question: Which known issues are linked to a test case?
  - id: create_reported_issue_v1_test_cases_reported_issues_post
    intent: Report an issue for a test case
    question: How do I link a bug report to a failing test case?
  - id: update_reported_issue_v1_test_cases_reported_issues__issue_id__put
    intent: Update a reported test case issue
    question: Can I change the bug link on an issue I already reported?
  - id: delete_reported_issue_v1_test_cases_reported_issues__issue_id__delete
    intent: Delete a reported test case issue
    question: How do I remove an issue report once the bug is fixed?
  - id: get_test_cases_v1_test_cases_get
    intent: Search test cases and their templates
    question: Which test cases exist for disk tests?
  phrasing_ops: 5
  slug: canonical-test-cases-api
- description: The test-executions API from Canonical — 10 operation(s) for test-executions.
  name: Canonical Test Executions API
  phrasing_intents:
  - id: end_test_execution_v1_test_executions_end_test_put
    intent: Finish a test execution and submit its results
    question: How do I close out a test run and report its results to Test Observer?
  - id: get_test_results_v1_test_executions__id__test_results_get
    intent: Get the test results of a test execution
    question: Which individual test cases passed or failed in a given test execution?
  - id: post_results_v1_test_executions__id__test_results_post
    intent: Add test results to a test execution
    question: How do I upload test case results to a test execution that is still running?
  - id: post_link_v1_test_executions__id__links_post
    intent: Attach a labelled link to a test execution
    question: How do I add a link, like a log or dashboard URL, to a test execution?
  - id: delete_link_v1_test_executions__id__links__link_id__delete
    intent: Remove a link from a test execution
    question: How do I delete an outdated link from a test run?
  - id: create_rerun_requests_v1_test_executions_reruns_post
    intent: Request reruns of test executions
    question: How do I ask for failed test executions to be run again?
  - id: get_rerun_requests_v1_test_executions_reruns_get
    intent: List pending test execution rerun requests
    question: Which test executions have been asked to run again?
  - id: delete_rerun_requests_v1_test_executions_reruns_delete
    intent: Cancel rerun requests for test executions
    question: How do I withdraw a rerun I requested by mistake?
  phrasing_ops: 16
  slug: canonical-test-executions-api
- description: The Test Observer API from Canonical — 1 operation(s) for test observer.
  name: Canonical Test Observer API
  phrasing_intents:
  - id: root__get
    intent: Check the Test Observer API is reachable
    question: Is the Test Observer API up and responding?
  phrasing_ops: 1
  slug: canonical-test-observer-api
- description: The test-plans API from Canonical — 1 operation(s) for test-plans.
  name: Canonical Test Plans API
  phrasing_intents:
  - id: get_test_plans_v1_test_plans_get
    intent: List test plan names
    question: Which test plans have been used in test executions?
  phrasing_ops: 1
  slug: canonical-test-plans-api
- description: The test-results API from Canonical — 1 operation(s) for test-results.
  name: Canonical Test Results API
  phrasing_intents:
  - id: search_test_results_v1_test_results_get
    intent: Search test results across artefacts
    question: Which test cases failed across all my artefacts last week?
  phrasing_ops: 1
  slug: canonical-test-results-api
- description: The users API from Canonical — 3 operation(s) for users.
  name: Canonical Users API
  phrasing_intents:
  - id: get_authenticated_user_v1_users_me_get
    intent: Get my own user profile
    question: Which Test Observer user am I signed in as?
  - id: get_users_v1_users_get
    intent: List or search users
    question: Who are the users registered in Test Observer?
  - id: get_user_v1_users__user_id__get
    intent: Get a user
    question: What are the details of a specific Test Observer user?
  - id: delete_user_v1_users__user_id__delete
    intent: Delete a user
    question: How do I remove a user from Test Observer?
  - id: update_user_v1_users__user_id__patch
    intent: Grant or revoke admin for a user
    question: How do I make a user an admin?
  phrasing_ops: 5
  slug: canonical-users-api
- description: The Version API from Canonical — 1 operation(s) for version.
  name: Canonical Version API
  phrasing_intents:
  - id: get_version_v1_version_get
    intent: Get the Test Observer version
    question: Which version of Test Observer is the server running?
  phrasing_ops: 1
  slug: canonical-version-api
- description: The warnings API from Canonical — 3 operation(s) for warnings.
  name: Canonical Warnings API
  phrasing_intents:
  - id: warnings_get
    intent: List warnings as URLs
    question: Are there any warnings raised on my LXD server, as a list of links?
  - id: warning_delete
    intent: Delete a warning
    question: How do I remove a warning from LXD entirely?
  - id: warning_get
    intent: Get one warning
    question: What is a specific warning about and when did it last occur?
  - id: warning_patch
    intent: Partially update a warning's status
    question: Is there a partial update I can use to change just a warning's status?
  - id: warning_put
    intent: Set a warning's status
    question: How do I acknowledge an LXD warning so it stops showing as new?
  - id: warnings_get_recursion1
    intent: List warnings with full details
    question: What do all the current LXD warnings actually say?
  phrasing_ops: 6
  slug: canonical-warnings-api
- baseURL: https://testflinger.ps7.canonical.com/
  baseurl_source: declared
  description: The Agents API from Canonical — 6 operation(s) for agents.
  name: Canonical Agents API
  phrasing_intents:
  - id: getV1AgentsData
    intent: List data for all test agents
    question: Which Testflinger agents are registered and what state is each one in?
  - id: getV1AgentsQueues
    intent: List advertised queues
    question: Which queues does this server advertise as valid to submit to?
  - id: postV1AgentsQueues
    intent: Advertise the queues an agent services
    question: How does an agent tell the server which queues it listens on?
  - id: postV1AgentsImages
    intent: Publish known images for a queue
    question: How do I record which provisioning images are available on a queue?
  - id: getV1AgentsImagesByQueue
    intent: Get known images for a queue
    question: Which images can I provision on a particular queue?
  - id: getV1AgentsDataByAgentName
    intent: Get one agent's information
    question: What state is a specific agent in right now?
  - id: postV1AgentsDataByAgentName
    intent: Update an agent's reported status
    question: How does an agent report its state and location back to the server?
  - id: postV1AgentsProvisionLogsByAgentName
    intent: Post an agent's provision log
    question: How do I record whether provisioning succeeded on an agent?
  phrasing_ops: 8
  slug: canonical-agents-api
- baseURL: https://testflinger.ps7.canonical.com/
  baseurl_source: declared
  description: The Client Permissions API from Canonical — 2 operation(s) for client permissions.
  name: Canonical Client Permissions API
  phrasing_intents:
  - id: getV1ClientPermissions
    intent: List all client permissions
    question: Which clients have permissions on the Testflinger server?
  - id: getV1ClientPermissionsByClientId
    intent: Get one client's permissions
    question: What is the maximum priority a particular client may use?
  - id: putV1ClientPermissionsByClientId
    intent: Create or update client permissions
    question: How do I grant a client a higher job priority?
  - id: deleteV1ClientPermissionsByClientId
    intent: Delete a client and its permissions
    question: How do I remove a client ID entirely?
  phrasing_ops: 4
  slug: canonical-client-permissions-api
- baseURL: https://testflinger.ps7.canonical.com/
  baseurl_source: declared
  description: The Job API from Canonical — 7 operation(s) for job.
  name: Canonical Job API
  phrasing_intents:
  - id: getV1Job
    intent: Pick up the next job from a queue
    question: How does an agent ask the server for the next job on its queues?
  - id: postV1Job
    intent: Submit a test job
    question: How do I submit a test job to a Testflinger queue?
  - id: getV1JobSearch
    intent: Search jobs by tag
    question: Can I find all jobs carrying a certain tag?
  - id: getV1JobByJobId
    intent: Get a job's definition
    question: What did I submit as the definition of a job that already ran?
  - id: postV1JobByJobIdAction
    intent: Take an action on a job
    question: How do I change the status of a job that is queued or running?
  - id: postV1JobByJobIdEvents
    intent: Forward job status events to a webhook
    question: How does an agent push job status events to the webhook the user registered?
  - id: getV1JobByJobIdPosition
    intent: Get a job's place in the queue
    question: How many jobs are ahead of mine in the queue?
  - id: getV1JobByJobIdAttachments
    intent: Download a job's attachments
    question: Where can an agent download the files attached to a job?
  phrasing_ops: 9
  slug: canonical-job-api
- baseURL: https://testflinger.ps7.canonical.com/
  baseurl_source: declared
  description: The Oauth2 API from Canonical — 3 operation(s) for oauth2.
  name: Canonical Oauth2 API
  phrasing_intents:
  - id: postV1Oauth2Token
    intent: Issue access and refresh tokens
    question: How does a client get a JWT carrying its queue and priority permissions?
  - id: postV1Oauth2Revoke
    intent: Revoke a refresh token
    question: How can an admin revoke a client's refresh token?
  - id: postV1Oauth2Refresh
    intent: Refresh an access token
    question: My access token expired; can I get a new one without logging in again?
  phrasing_ops: 3
  slug: canonical-oauth2-api
- baseURL: https://testflinger.ps7.canonical.com/
  baseurl_source: declared
  description: The Queues API from Canonical — 3 operation(s) for queues.
  name: Canonical Queues API
  phrasing_intents:
  - id: getV1QueuesWaitTimes
    intent: Get queue wait times
    question: How long do jobs typically wait before they start on each queue?
  - id: getV1QueuesByQueueNameJobs
    intent: List jobs in a queue
    question: Which jobs are sitting in a particular queue and what state are they in?
  - id: getV1QueuesByQueueNameAgents
    intent: List agents serving a queue
    question: Which agents are listening on a particular queue?
  phrasing_ops: 3
  slug: canonical-queues-api
- baseURL: https://testflinger.ps7.canonical.com/
  baseurl_source: declared
  description: The Restricted Queues API from Canonical — 2 operation(s) for restricted queues.
  name: Canonical Restricted Queues API
  phrasing_intents:
  - id: getV1RestrictedQueues
    intent: List restricted queues and owners
    question: Which queues are restricted, and who owns them?
  - id: getV1RestrictedQueuesByQueueName
    intent: Get a restricted queue's owners
    question: Who is allowed to use a particular restricted queue?
  - id: postV1RestrictedQueuesByQueueName
    intent: Add an owner to a restricted queue
    question: How do I give a client access to a restricted queue?
  - id: deleteV1RestrictedQueuesByQueueName
    intent: Remove an owner from a restricted queue
    question: How do I take a client's access away from a restricted queue?
  phrasing_ops: 4
  slug: canonical-restricted-queues-api
- baseURL: https://testflinger.ps7.canonical.com/
  baseurl_source: declared
  description: The Result API from Canonical — 4 operation(s) for result.
  name: Canonical Result API
  phrasing_intents:
  - id: getV1ResultByJobId
    intent: Get a job's full results
    question: How do I see the output and exit status of every phase of a finished job?
  - id: postV1ResultByJobId
    intent: Post a job's results
    question: How does an agent report the final status of a job?
  - id: getV1ResultByJobIdStatus
    intent: Get a job's state and exit codes only
    question: Is there a lightweight way to check a job's state without pulling its logs?
  - id: getV1ResultByJobIdArtifact
    intent: Download a job's artifact bundle
    question: Where do I download the artifacts my test job produced?
  - id: postV1ResultByJobIdArtifact
    intent: Upload a job's artifact bundle
    question: How does an agent upload artifacts produced by a test run?
  - id: getV1ResultByJobIdLogByLogType
    intent: Get a job's logs by type
    question: Can I read a job's serial log separately from its output log?
  - id: postV1ResultByJobIdLogByLogType
    intent: Stream a log fragment for a job
    question: How does an agent stream log data for a running job?
  phrasing_ops: 7
  slug: canonical-result-api
- baseURL: https://testflinger.ps7.canonical.com/
  baseurl_source: declared
  description: The Secrets API from Canonical — 1 operation(s) for secrets.
  name: Canonical Secrets API
  phrasing_intents:
  - id: putV1SecretsByClientIdByPath
    intent: Store a secret
    question: How do I store a secret that my test jobs can use?
  - id: deleteV1SecretsByClientIdByPath
    intent: Remove a secret
    question: How do I delete a secret I stored for my client?
  phrasing_ops: 2
  slug: canonical-secrets-api
- baseURL: https://testflinger.ps7.canonical.com/
  baseurl_source: declared
  description: The Testflinger API API from Canonical — 1 operation(s) for testflinger api.
  name: Canonical Testflinger API
  phrasing_intents:
  - id: getV1
    intent: Identify the server
    question: Is this endpoint a Testflinger server?
  phrasing_ops: 1
  slug: canonical-testflinger-api-api
- description: The Add Ons API from Canonical — 4 operation(s) for add ons.
  name: Canonical Add Ons API
  phrasing_intents:
  - id: addons_get
    intent: List addons in AMS
    question: Which addons are installed in my Anbox Management Service?
  - id: addons_post
    intent: Create an addon by uploading a package
    question: How do I upload a new addon with its manifest and hooks to AMS?
  - id: addon_get
    intent: Get an addon
    question: What versions exist for a particular AMS addon?
  - id: addon_delete
    intent: Delete an addon
    question: How do I remove an addon and all its versions from AMS?
  - id: addon_patch
    intent: Upload a new version of an addon
    question: How do I ship an updated package for an existing addon?
  - id: addon_version_delete
    intent: Delete one version of an addon
    question: Can I delete one broken version of an addon and keep the others?
  - id: addons_get_recursion1
    intent: List addons with full details
    question: Can I get every addon with its versions in one call?
  phrasing_ops: 7
  slug: canonical-add-ons-api
- description: The Authentication Service API from Canonical — 4 operation(s) for authentication service.
  name: Canonical Authentication Service API
  phrasing_intents:
  - id: AuthenticationService_Login
    intent: Start a login to the identity platform admin
    question: How do I sign in to the identity platform admin UI?
  - id: AuthenticationService_Callback
    intent: Complete the login callback
    question: What handles the authorization code returned after sign-in?
  - id: AuthenticationService_Logout
    intent: Log out of the identity platform admin
    question: How do I sign out of the admin session?
  - id: AuthenticationService_Me
    intent: Get the signed-in user's profile
    question: Who am I signed in as?
  phrasing_ops: 4
  slug: canonical-authentication-service-api
- baseURL: unix:///run/snapd.socket
  baseurl_source: spec
  description: Do not require the user to authenticate.
  name: Canonical Open Access API
  phrasing_intents:
  - id: getSnapIcon
    intent: Get an installed snap's icon
    question: Can I fetch the icon file of a snap installed on this machine?
  - id: getQuotaGroups
    intent: List snap quota groups
    question: Which quota groups exist on this system and what limits do they set?
  - id: getQuotaGroupByName
    intent: Get one snap quota group
    question: What limits does a particular quota group enforce?
  - id: getStoreSections
    intent: List Snap Store sections
    question: Which sections or categories are available in the Snap Store?
  - id: listInstalledSnaps
    intent: List installed snaps
    question: Which snaps are installed on this system, with their components?
  - id: getInstalledSnapByName
    intent: Get details of an installed snap
    question: What version and channel is a specific installed snap on?
  - id: listSnapshots
    intent: List snap snapshots
    question: Which snapshot sets of snap data are stored on this system?
  - id: getSystems
    intent: List recovery systems
    question: Which recovery systems are available on this device?
  phrasing_ops: 10
  slug: canonical-open-access-api
artifact_total: 375
asyncapis:
- description: ''
  name: Canonical Launchpad Webhooks
  slug: canonical-launchpad-webhooks
collections:
- collection_type: open
  name: Canonical Snap Store Device Assertions API
  slug: open-canonical-assertions-api
- collection_type: open
  name: Canonical Snap Store Device Assertions Search API
  slug: open-canonical-search-api
- collection_type: open
  name: Canonical Snap Store Device Assertions Snaps API
  slug: open-canonical-snaps-api
- collection_type: open
  name: Canonical Snap Store Device API
  slug: open-canonical
common:
- group: commercial
  href: https://artifacts.apis.io/canonical/finops/canonical-finops.yml
  title: ''
  type: FinOps
  url: finops/canonical-finops.yml
- group: design
  href: https://artifacts.apis.io/canonical/rules/canonical-rules.yml
  title: ''
  type: Spectral
  url: rules/canonical-rules.yml
- group: design
  href: https://artifacts.apis.io/canonical/json-ld/canonical-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/canonical-context.jsonld
- group: design
  href: https://artifacts.apis.io/canonical/vocabulary/canonical-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/canonical-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/canonical/hosts/canonical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canonical-hosts.yml
- group: other
  href: https://artifacts.apis.io/canonical/vendors/canonical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canonical-vendors.yml
- group: agent
  href: https://artifacts.apis.io/canonical/skills/canonical-snapd-manage-snap.md
  title: ''
  type: AgentSkill
  url: skills/canonical-snapd-manage-snap.md
- group: other
  href: https://artifacts.apis.io/canonical/overlays/canonical-lxd-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-lxd-rest-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/canonical/skills/canonical-lxd-provision-instance.md
  title: ''
  type: AgentSkill
  url: skills/canonical-lxd-provision-instance.md
- group: other
  href: https://artifacts.apis.io/canonical/overlays/canonical-ubuntu-security-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-ubuntu-security-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/canonical/skills/canonical-ubuntu-security-cve-lookup.md
  title: ''
  type: AgentSkill
  url: skills/canonical-ubuntu-security-cve-lookup.md
- group: other
  href: https://artifacts.apis.io/canonical/overlays/canonical-pebble-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-pebble-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/canonical/overlays/canonical-testflinger-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-testflinger-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/canonical/overlays/canonical-hardware-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-hardware-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/canonical/overlays/canonical-identity-platform-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-identity-platform-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/canonical/overlays/canonical-test-observer-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-test-observer-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/canonical/overlays/canonical-anbox-cloud-ams-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-anbox-cloud-ams-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/canonical/overlays/canonical-anbox-stream-gateway-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-anbox-stream-gateway-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/canonical/overlays/canonical-cos-registration-server-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-cos-registration-server-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/canonical/scopes/canonical-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/canonical-scopes.yml
- group: auth
  href: https://artifacts.apis.io/canonical/authentication/canonical-authentication.yml
  title: ''
  type: Authentication
  url: authentication/canonical-authentication.yml
- group: agent
  href: https://artifacts.apis.io/canonical/agentic-access/canonical-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/canonical-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/canonical/security/canonical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canonical-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canonical
- group: company
  title: ''
  type: Website
  url: https://canonical.com/
- group: company
  title: ''
  type: UbuntuWebsite
  url: https://ubuntu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.ubuntu.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/canonical
- group: other
  title: ''
  type: SnapStore
  url: https://snapcraft.io/
- group: other
  title: ''
  type: Charmhub
  url: https://charmhub.io/
- group: other
  title: ''
  type: Launchpad
  url: https://launchpad.net/
- group: learn
  title: ''
  type: DiscourseForum
  url: https://discourse.ubuntu.com/
- group: commercial
  title: ''
  type: DataPrivacy
  url: https://ubuntu.com/legal/data-privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ubuntu.com/legal/terms
- group: company
  title: ''
  type: Blog
  url: https://canonical.com/blog/feed/
- group: build
  href: https://artifacts.apis.io/canonical/packages/canonical-packages.yml
  title: ''
  type: Packages
  url: packages/canonical-packages.yml
- group: build
  href: https://artifacts.apis.io/canonical/packages/canonical-packages.yml
  title: ''
  type: SDKs
  url: packages/canonical-packages.yml
- group: build
  href: https://artifacts.apis.io/canonical/cli/canonical-cli.yml
  title: ''
  type: CLI
  url: cli/canonical-cli.yml
- group: design
  href: https://artifacts.apis.io/canonical/components/canonical-components.yml
  title: ''
  type: Components
  url: components/canonical-components.yml
- group: design
  href: https://artifacts.apis.io/canonical/conventions/canonical-conventions.yml
  title: ''
  type: Conventions
  url: conventions/canonical-conventions.yml
- group: design
  href: https://artifacts.apis.io/canonical/conventions/canonical-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/canonical-conventions.yml
- group: design
  href: https://artifacts.apis.io/canonical/errors/canonical-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/canonical-problem-types.yml
- group: design
  href: https://artifacts.apis.io/canonical/data-model/canonical-data-model.yml
  title: ''
  type: DataModel
  url: data-model/canonical-data-model.yml
- group: design
  href: https://artifacts.apis.io/canonical/lifecycle/canonical-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/canonical-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/canonical/lifecycle/canonical-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/canonical-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.canonical.com/
- group: operate
  href: https://artifacts.apis.io/canonical/changelog/canonical-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/canonical-changelog.yml
- group: design
  href: https://artifacts.apis.io/canonical/conformance/canonical-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canonical-conformance.yml
- group: auth
  href: https://artifacts.apis.io/canonical/security/canonical-trust-center.yml
  title: ''
  type: Compliance
  url: security/canonical-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/canonical/security/canonical-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/canonical-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/canonical/security/canonical-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/canonical-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/canonical/security/canonical-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/canonical-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/canonical/well-known/canonical-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canonical-well-known.yml
- group: auth
  href: https://artifacts.apis.io/canonical/well-known/canonical-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/canonical-security.txt
- group: agent
  href: https://artifacts.apis.io/canonical/llms/canonical-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canonical-llms.txt
- group: design
  href: https://artifacts.apis.io/canonical/asyncapi/canonical-launchpad-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/canonical-launchpad-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/canonical/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/canonical/overlays/canonical-landscape-debarchive-provider-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-landscape-debarchive-provider-overlay.yaml
- group: commercial
  href: https://artifacts.apis.io/canonical/plans/canonical-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canonical-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/canonical/rate-limits/canonical-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/canonical-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://ubuntu.com/pricing/pro
- group: start
  title: ''
  type: SignUp
  url: https://ubuntu.com/pro/subscribe
- group: start
  title: ''
  type: Login
  url: https://login.ubuntu.com/
- group: operate
  title: ''
  type: Support
  url: https://ubuntu.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ubuntu.com/legal/data-privacy
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.ubuntu.com/lxd/latest/rest-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://ubuntu.com/tutorials
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/canonical
created: '2026-03-16'
description: Canonical is the company behind Ubuntu, the world's most popular open source operating system for cloud, servers, desktops, IoT, and Kubernetes. Canonical publishes a broad set of developer APIs spanning the Ubuntu and Canonical ecosystem — the Snap Store and Snapcraft, the Charmhub charm marketplace, LXD system containers, MAAS bare-metal provisioning, Juju orchestration, Launchpad project hosting, Ubuntu Pro subscription services, and Landscape systems management — most of which are RESTful, open, and well documented.
finops:
- has_sources: true
  method: derived
  name: Canonical Finops
  primary_unit: physical server
  service_category: ''
  slug: canonical-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canonical.png
json_schemas:
- name: api.ApplicationsGetResponse
  property_count: 5
  slug: canonical-api-applications-get-response
- name: apiauthz_groupsCreateGroupResp
  property_count: 3
  slug: canonical-apiauthz-groups-create-group-resp
- name: apiauthz_groupsGetGroupResp
  property_count: 3
  slug: canonical-apiauthz-groups-get-group-resp
- name: apiauthz_groupsListGroupsResp
  property_count: 4
  slug: canonical-apiauthz-groups-list-groups-resp
- name: apiauthz_groupsUpdateGroupResp
  property_count: 3
  slug: canonical-apiauthz-groups-update-group-resp
- name: apigroupsCreateGroupResp
  property_count: 4
  slug: canonical-apigroups-create-group-resp
- name: apigroupsGetGroupResp
  property_count: 4
  slug: canonical-apigroups-get-group-resp
- name: apigroupsListGroupsResp
  property_count: 4
  slug: canonical-apigroups-list-groups-resp
- name: AppActionRestart
  property_count: 5
  slug: canonical-app-action-restart
- name: AppActionStart
  property_count: 5
  slug: canonical-app-action-start
- name: AppActionStop
  property_count: 5
  slug: canonical-app-action-stop
- name: App
  property_count: 8
  slug: canonical-app
- name: ApplicationPatch
  property_count: 16
  slug: canonical-application-patch
- name: ApplicationResponse
  property_count: 4
  slug: canonical-application-response
- name: Application
  property_count: 18
  slug: canonical-application
- name: ApplicationsDelete
  property_count: 2
  slug: canonical-applications-delete
- name: ArtefactBuildEnvironmentReviewResponse
  property_count: 6
  slug: canonical-artefact-build-environment-review-response
- name: ArtefactBuildResponse
  property_count: 4
  slug: canonical-artefact-build-response
- name: ArtefactMatchingRulePatch
  property_count: 12
  slug: canonical-artefact-matching-rule-patch
- name: ArtefactMatchingRuleRequest
  property_count: 12
  slug: canonical-artefact-matching-rule-request
- name: ArtefactMatchingRuleResponse
  property_count: 13
  slug: canonical-artefact-matching-rule-response
- name: ArtefactPatch
  property_count: 10
  slug: canonical-artefact-patch
- name: ArtefactResponse
  property_count: 28
  slug: canonical-artefact-response
- name: ArtefactSearchResponse
  property_count: 4
  slug: canonical-artefact-search-response
- name: AssertionResult
  property_count: 4
  slug: canonical-assertion-result
- name: AuthGroupPost is used for renaming a group.
  property_count: 1
  slug: canonical-auth-group-post
- name: AuthGroupPut contains the editable fields of a group.
  property_count: 2
  slug: canonical-auth-group-put
- name: AuthGroup is the type for a LXD group.
  property_count: 6
  slug: canonical-auth-group
- name: AuthGroupsPost is used for creating a new group.
  property_count: 3
  slug: canonical-auth-groups-post
- name: authorizationAddAllowedAppToGroupResp
  property_count: 2
  slug: canonical-authorization-add-allowed-app-to-group-resp
- name: authorizationGetAllowedAppsInGroupResp
  property_count: 3
  slug: canonical-authorization-get-allowed-apps-in-group-resp
- name: authorizationGetAllowedGroupsForAppResp
  property_count: 3
  slug: canonical-authorization-get-allowed-groups-for-app-resp
- name: authorizationRemoveAllowedAppFromGroupResp
  property_count: 2
  slug: canonical-authorization-remove-allowed-app-from-group-resp
- name: authorizationRemoveAllowedAppsFromGroupResp
  property_count: 2
  slug: canonical-authorization-remove-allowed-apps-from-group-resp
- name: authorizationRemoveAllowedGroupsForAppResp
  property_count: 2
  slug: canonical-authorization-remove-allowed-groups-for-app-resp
- name: authz_groupsListUserGroupsResp
  property_count: 4
  slug: canonical-authz-groups-list-user-groups-resp
- name: authz_groupsListUsersInGroupResp
  property_count: 4
  slug: canonical-authz-groups-list-users-in-group-resp
- name: BaseResponse
  property_count: 3
  slug: canonical-base-response
- name: BatchGetLocalsRequest
  property_count: 2
  slug: canonical-batch-get-locals-request
- name: BatchGetLocalsResponse
  property_count: 2
  slug: canonical-batch-get-locals-response
- name: BatchGetMirrorsRequest
  property_count: 2
  slug: canonical-batch-get-mirrors-request
- name: BatchGetMirrorsResponse
  property_count: 2
  slug: canonical-batch-get-mirrors-response
- name: BatchGetOperationsRequest
  property_count: 2
  slug: canonical-batch-get-operations-request
- name: BatchGetOperationsResponse
  property_count: 2
  slug: canonical-batch-get-operations-response
- name: CertificatePut
  property_count: 5
  slug: canonical-certificate-put
- name: Certificate
  property_count: 2
  slug: canonical-certificate
- name: CertificatesPost_2
  property_count: 8
  slug: canonical-certificates-post-2
- name: CertificatesPost
  property_count: 2
  slug: canonical-certificates-post
- name: CertificationStatusRequest
  property_count: 10
  slug: canonical-certification-status-request
- name: CertifiedImageExistsResponse
  property_count: 7
  slug: canonical-certified-image-exists-response
- name: CertifiedResponse
  property_count: 7
  slug: canonical-certified-response
- name: Change
  property_count: 11
  slug: canonical-change
- name: CheckActionResponse
  property_count: 4
  slug: canonical-check-action-response
- name: clientsClient
  property_count: 47
  slug: canonical-clients-client
- name: clientsCreateClientResp
  property_count: 3
  slug: canonical-clients-create-client-resp
- name: clientsGetClientResp
  property_count: 3
  slug: canonical-clients-get-client-resp
- name: clientsListClientsResp
  property_count: 4
  slug: canonical-clients-list-clients-resp
- name: clientsRemoveClientResp
  property_count: 2
  slug: canonical-clients-remove-client-resp
- name: clientsUpdateClientResp
  property_count: 3
  slug: canonical-clients-update-client-resp
- name: ClusterGroupPost represents the fields required to rename a cluster group.
  property_count: 1
  slug: canonical-cluster-group-post
- name: ClusterGroupPut represents the modifiable fields of a cluster group.
  property_count: 2
  slug: canonical-cluster-group-put
- name: ClusterGroup represents a cluster group.
  property_count: 4
  slug: canonical-cluster-group
- name: ClusterGroupsPost represents the fields available for a new cluster group.
  property_count: 3
  slug: canonical-cluster-groups-post
- name: ClusterLinkPost represents the fields available for renaming a cluster link.
  property_count: 1
  slug: canonical-cluster-link-post
- name: ClusterLinkPut represents the modifiable fields of a cluster link.
  property_count: 2
  slug: canonical-cluster-link-put
- name: ClusterLink represents high-level information about a cluster link.
  property_count: 6
  slug: canonical-cluster-link
- name: ClusterLinkState represents the state of a linked cluster.
  property_count: 1
  slug: canonical-cluster-link-state
- name: ClusterLinksPost represents the fields available for a new cluster link.
  property_count: 9
  slug: canonical-cluster-links-post
- name: ClusterMemberPut
  property_count: 5
  slug: canonical-cluster-member-put
- name: ClusterMember represents the a LXD node in the cluster.
  property_count: 11
  slug: canonical-cluster-member
- name: ClusterMemberStatePost represents the fields required to evacuate a cluster member.
  property_count: 3
  slug: canonical-cluster-member-state-post
- name: ClusterPut
  property_count: 7
  slug: canonical-cluster-put
- name: Cluster represents high-level information about a LXD cluster.
  property_count: 3
  slug: canonical-cluster
- name: CollectionResponse
  property_count: 5
  slug: canonical-collection-response
- name: ConfdbControlAction
  property_count: 4
  slug: canonical-confdb-control-action
- name: ConfigPost
  property_count: 2
  slug: canonical-config-post
- name: ConnectionStatus
  property_count: 4
  slug: canonical-connection-status
- name: ContainerExecPost
  property_count: 5
  slug: canonical-container-exec-post
- name: Container
  property_count: 21
  slug: canonical-container
- name: ContainersDelete
  property_count: 2
  slug: canonical-containers-delete
- name: ContainersPost
  property_count: 17
  slug: canonical-containers-post
- name: DeviceCertificate
  property_count: 7
  slug: canonical-device-certificate
- name: Device
  property_count: 9
  slug: canonical-device
- name: EnvironmentReportedIssueRequest
  property_count: 4
  slug: canonical-environment-reported-issue-request
- name: EnvironmentReportedIssueResponse
  property_count: 7
  slug: canonical-environment-reported-issue-response
- name: EnvironmentReviewPatch
  property_count: 3
  slug: canonical-environment-review-patch
- name: EnvironmentsResponse
  property_count: 4
  slug: canonical-environments-response
- name: Event
  property_count: 3
  slug: canonical-event
- name: ExecutionMetadataGetResponse
  property_count: 1
  slug: canonical-execution-metadata-get-response
- name: FindResults
  property_count: 1
  slug: canonical-find-results
- name: GetChangeByIDResponse
  property_count: 4
  slug: canonical-get-change-by-idresponse
- name: GetChangesResponse
  property_count: 4
  slug: canonical-get-changes-response
- name: GetChecksResponse
  property_count: 4
  slug: canonical-get-checks-response
- name: GetHealthOKResponse
  property_count: 4
  slug: canonical-get-health-okresponse
- name: GetNoticeByIDResponse
  property_count: 4
  slug: canonical-get-notice-by-idresponse
- name: GetNoticesResponse
  property_count: 4
  slug: canonical-get-notices-response
- name: GetPlanResponse
  property_count: 4
  slug: canonical-get-plan-response
- name: groupsGetGroupIdentitiesResp
  property_count: 4
  slug: canonical-groups-get-group-identities-resp
- name: IdentitiesBearerPost contains required information for the creation of a token identity.
  property_count: 3
  slug: canonical-identities-bearer-post
- name: identitiesCreateIdentityBody
  property_count: 9
  slug: canonical-identities-create-identity-body
- name: identitiesCreateIdentityResp
  property_count: 4
  slug: canonical-identities-create-identity-resp
- name: identitiesGetIdentityResp
  property_count: 4
  slug: canonical-identities-get-identity-resp
- name: identitiesListIdentitiesResp
  property_count: 4
  slug: canonical-identities-list-identities-resp
- name: IdentitiesTLSPost contains required information for the creation of a TLS identity.
  property_count: 5
  slug: canonical-identities-tlspost
- name: identitiesUpdateIdentityBody
  property_count: 7
  slug: canonical-identities-update-identity-body
- name: identitiesUpdateIdentityResp
  property_count: 4
  slug: canonical-identities-update-identity-resp
- name: IdentityInfo expands an Identity to include effective group membership and effective permissions.
  property_count: 11
  slug: canonical-identity-info
- name: IdentityProviderGroupPost is used for renaming an IdentityProviderGroup.
  property_count: 1
  slug: canonical-identity-provider-group-post
- name: IdentityProviderGroupPut contains the editable fields of an IdentityProviderGroup.
  property_count: 1
  slug: canonical-identity-provider-group-put
- name: IdentityProviderGroup represents a mapping between LXD groups and groups defined by an identity provider.
  property_count: 3
  slug: canonical-identity-provider-group
- name: IdentityProviderGroupsPost is used for creating an IdentityProviderGroup.
  property_count: 2
  slug: canonical-identity-provider-groups-post
- name: IdentityPut contains the editable fields of an IdentityInfo.
  property_count: 2
  slug: canonical-identity-put
- name: Identity is the type for an authenticated party that can make requests to the HTTPS API.
  property_count: 8
  slug: canonical-identity
- name: idpsCreateIdpBody
  property_count: 16
  slug: canonical-idps-create-idp-body
- name: idpsCreateIdpResp
  property_count: 3
  slug: canonical-idps-create-idp-resp
- name: idpsGetIdpResp
  property_count: 3
  slug: canonical-idps-get-idp-resp
- name: idpsListIdpsResp
  property_count: 3
  slug: canonical-idps-list-idps-resp
- name: idpsUpdateIdpBody
  property_count: 16
  slug: canonical-idps-update-idp-body
- name: idpsUpdateIdpResp
  property_count: 3
  slug: canonical-idps-update-idp-resp
- name: Image_2
  property_count: 20
  slug: canonical-image-2
- name: ImageAliasesPost
  property_count: 5
  slug: canonical-image-aliases-post
- name: ImageExportPost
  property_count: 6
  slug: canonical-image-export-post
- name: ImagePut
  property_count: 5
  slug: canonical-image-put
- name: Image
  property_count: 10
  slug: canonical-image
- name: ImagesPost_2
  property_count: 9
  slug: canonical-images-post-2
- name: ImportLocalPackagesRequest
  property_count: 3
  slug: canonical-import-local-packages-request
- name: Instance represents a LXD instance.
  property_count: 18
  slug: canonical-instance-2
- name: InstanceFull is a combination of Instance, InstanceBackup, InstanceState and InstanceSnapshot.
  property_count: 21
  slug: canonical-instance-full
- name: InstancePost represents the fields required to rename/move a LXD instance.
  property_count: 13
  slug: canonical-instance-post
- name: Instance
  property_count: 23
  slug: canonical-instance
- name: InstanceSnapshot represents a LXD instance snapshot.
  property_count: 13
  slug: canonical-instance-snapshot
- name: InstancesPost
  property_count: 14
  slug: canonical-instances-post
- name: IssueAttachmentRequest
  property_count: 3
  slug: canonical-issue-attachment-request
- name: IssuePutRequest
  property_count: 4
  slug: canonical-issue-put-request
- name: IssueResponse
  property_count: 10
  slug: canonical-issue-response
- name: IssueTestResultAttachmentRulePostRequest
  property_count: 12
  slug: canonical-issue-test-result-attachment-rule-post-request
- name: IssuesGetResponse
  property_count: 4
  slug: canonical-issues-get-response
- name: LegacyInterfaceObject
  property_count: 2
  slug: canonical-legacy-interface-object
- name: Level
  property_count: 0
  slug: canonical-level
- name: ListFilesResponse
  property_count: 4
  slug: canonical-list-files-response
- name: ListLocalPackagesResponse
  property_count: 2
  slug: canonical-list-local-packages-response
- name: ListMirrorPackagesResponse
  property_count: 2
  slug: canonical-list-mirror-packages-response
- name: Local
  property_count: 8
  slug: canonical-local
- name: logs
  property_count: 3
  slug: canonical-logs
- name: MetadataConfiguration contains metadata about the LXD server configuration options.
  property_count: 2
  slug: canonical-metadata-configuration
- name: MinimalIssueTestResultAttachmentRuleResponse
  property_count: 13
  slug: canonical-minimal-issue-test-result-attachment-rule-response
- name: Mirror
  property_count: 20
  slug: canonical-mirror
- name: ModernInterfaceObject
  property_count: 0
  slug: canonical-modern-interface-object
- name: NetworkACL used for displaying an ACL.
  property_count: 8
  slug: canonical-network-acl
- name: NetworkAllocations
  property_count: 6
  slug: canonical-network-allocations
- name: NetworkForwardPut
  property_count: 3
  slug: canonical-network-forward-put
- name: NetworkForward used for displaying an network address forward.
  property_count: 5
  slug: canonical-network-forward
- name: NetworkForwardsPost
  property_count: 4
  slug: canonical-network-forwards-post
- name: NetworkLease
  property_count: 6
  slug: canonical-network-lease
- name: NetworkLoadBalancerPoolPut represents the modifiable fields of a LXD network load balancer pool.
  property_count: 3
  slug: canonical-network-load-balancer-pool-put
- name: NetworkLoadBalancerPool used for displaying a network load balancer pool.
  property_count: 5
  slug: canonical-network-load-balancer-pool
- name: NetworkLoadBalancerPoolState represents the state of a network load balancer pool.
  property_count: 1
  slug: canonical-network-load-balancer-pool-state
- name: NetworkLoadBalancerPoolsPost represents the fields of a new LXD network load balancer pool.
  property_count: 4
  slug: canonical-network-load-balancer-pools-post
- name: NetworkLoadBalancerPut
  property_count: 4
  slug: canonical-network-load-balancer-put
- name: NetworkLoadBalancer
  property_count: 6
  slug: canonical-network-load-balancer
- name: NetworkLoadBalancersPost
  property_count: 5
  slug: canonical-network-load-balancers-post
- name: NetworkPeerPut
  property_count: 2
  slug: canonical-network-peer-put
- name: NetworkPeer used for displaying a LXD network peering.
  property_count: 7
  slug: canonical-network-peer
- name: NetworkPeersPost
  property_count: 5
  slug: canonical-network-peers-post
- name: NetworkPost
  property_count: 1
  slug: canonical-network-post
- name: NetworkPut
  property_count: 2
  slug: canonical-network-put
- name: Network
  property_count: 10
  slug: canonical-network
- name: NetworkState
  property_count: 10
  slug: canonical-network-state
- name: NetworkZonePut
  property_count: 2
  slug: canonical-network-zone-put
- name: NetworkZoneRecordPut
  property_count: 3
  slug: canonical-network-zone-record-put
- name: NetworkZoneRecord represents a network zone (DNS) record.
  property_count: 4
  slug: canonical-network-zone-record
- name: NetworkZoneRecordsPost
  property_count: 4
  slug: canonical-network-zone-records-post
- name: NetworkZone represents a network zone (DNS).
  property_count: 6
  slug: canonical-network-zone
- name: NetworkZonesPost
  property_count: 3
  slug: canonical-network-zones-post
- name: NetworksPost
  property_count: 4
  slug: canonical-networks-post
- name: NoMetaSyncResponse
  property_count: 4
  slug: canonical-no-meta-sync-response
- name: NodeDelete
  property_count: 2
  slug: canonical-node-delete
- name: NodePatch
  property_count: 12
  slug: canonical-node-patch
- name: Node
  property_count: 22
  slug: canonical-node
- name: NodesPost
  property_count: 18
  slug: canonical-nodes-post
- name: NotCertifiedResponse
  property_count: 1
  slug: canonical-not-certified-response
- name: Notice
  property_count: 11
  slug: canonical-notice
- name: NotificationResponse
  property_count: 6
  slug: canonical-notification-response
- name: NotificationsResponse
  property_count: 4
  slug: canonical-notifications-response
- name: OIDCSession contains session details for a current login.
  property_count: 7
  slug: canonical-oidcsession
- name: Operation_2
  property_count: 15
  slug: canonical-operation-2
- name: OperationResponse
  property_count: 5
  slug: canonical-operation-response
- name: Operation
  property_count: 5
  slug: canonical-operation
- name: PatchedDeviceCertificate
  property_count: 7
  slug: canonical-patched-device-certificate
- name: PatchedDevice
  property_count: 9
  slug: canonical-patched-device
- name: PermissionInfo expands a Permission to include any groups that may have the specified Permission.
  property_count: 4
  slug: canonical-permission-info
- name: Permission represents a permission that may be granted to a group.
  property_count: 3
  slug: canonical-permission
- name: PlacementGroupPut
  property_count: 0
  slug: canonical-placement-group-put
- name: PlacementGroup
  property_count: 0
  slug: canonical-placement-group
- name: PlacementGroupsPost
  property_count: 0
  slug: canonical-placement-groups-post
- name: Plug
  property_count: 7
  slug: canonical-plug
- name: PostExecRequest
  property_count: 14
  slug: canonical-post-exec-request
- name: PostExecResponse
  property_count: 5
  slug: canonical-post-exec-response
- name: PostFilesMakeDirsRequest
  property_count: 2
  slug: canonical-post-files-make-dirs-request
- name: PostFilesRemovePathsRequest
  property_count: 2
  slug: canonical-post-files-remove-paths-request
- name: PostFilesResponse
  property_count: 4
  slug: canonical-post-files-response
- name: PostLayersResponse
  property_count: 4
  slug: canonical-post-layers-response
- name: PostNoticesResponse
  property_count: 4
  slug: canonical-post-notices-response
- name: ProfilePost
  property_count: 1
  slug: canonical-profile-post
- name: ProfilePut
  property_count: 3
  slug: canonical-profile-put
- name: Profile
  property_count: 7
  slug: canonical-profile
- name: ProfilesPost
  property_count: 4
  slug: canonical-profiles-post
- name: ProjectPost
  property_count: 1
  slug: canonical-project-post
- name: ProjectPut
  property_count: 2
  slug: canonical-project-put
- name: Project
  property_count: 6
  slug: canonical-project
- name: ProjectStatePut
  property_count: 1
  slug: canonical-project-state-put
- name: ProjectState
  property_count: 1
  slug: canonical-project-state
- name: ProjectsPost
  property_count: 5
  slug: canonical-projects-post
- name: PromptingPrompt
  property_count: 5
  slug: canonical-prompting-prompt
- name: PromptingReply
  property_count: 4
  slug: canonical-prompting-reply
- name: PromptingRuleActionAdd
  property_count: 2
  slug: canonical-prompting-rule-action-add
- name: PromptingRuleActionRemove
  property_count: 2
  slug: canonical-prompting-rule-action-remove
- name: PromptingRule
  property_count: 6
  slug: canonical-prompting-rule
- name: QuotaGroup
  property_count: 7
  slug: canonical-quota-group
- name: ReadFilesResponse
  property_count: 2
  slug: canonical-read-files-response
- name: RefreshCheckResponse
  property_count: 4
  slug: canonical-refresh-check-response
- name: RefreshRequest
  property_count: 2
  slug: canonical-refresh-request
- name: RefreshResponse
  property_count: 1
  slug: canonical-refresh-response
- name: RelatedCertifiedSystemExistsResponse
  property_count: 14
  slug: canonical-related-certified-system-exists-response
- name: Slot
  property_count: 7
  slug: canonical-slot
- name: SnapInfo
  property_count: 4
  slug: canonical-snap-info
- name: Snap
  property_count: 26
  slug: canonical-snap
- name: SyncMirrorRequest
  property_count: 6
  slug: canonical-sync-mirror-request
- name: SystemActionCreate
  property_count: 6
  slug: canonical-system-action-create
- name: SystemActionInstall
  property_count: 2
  slug: canonical-system-action-install
- name: SystemDetails
  property_count: 8
  slug: canonical-system-details
- name: tenantLookupTenantsResponse
  property_count: 1
  slug: canonical-tenant-lookup-tenants-response
- name: ValidationSet
  property_count: 6
  slug: canonical-validation-set
jsonld:
- class_count: 120
  name: Canonical Context
  property_count: 234
  slug: canonical-context
layout: provider
modified: '2026-09-05'
name: Canonical
nav: Providers
network: true
overview: 'Canonical publishes 122 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assertions API, Search API, Snaps API, and 119 more. Tagged areas include Canonical, Cloud, Linux, Open Source, and Ubuntu.


  The Canonical catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Canonical''s developer surface includes authentication, documentation, engineering blog, CLI, changelog, pricing, signup flow, and 61 more developer resources.'
plans:
- name: Canonical Plans Pricing
  plan_count: 14
  slug: canonical-plans-pricing
- name: Canonical Price Estimates
  plan_count: 0
  slug: canonical-price-estimates
random_paper: 0
rate_limits:
- limit_count: 0
  name: Canonical Rate Limits
  slug: canonical-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Canonical API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 4
  slug: canonical-rules
scopes:
- name: Canonical Scopes
  scope_count: 3
  slug: canonical-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: exemplar
  composite: 76.4
  coverage:
    artifact_dirs: 37
    catalog_earned: 75.8
    catalog_earned_first_party: 12.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 35.6
    contract_quality: 66.6
    developer_ergonomics: 73.2
    discoverability: 69.6
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 76.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 12.0
      derived: 3
      marker_coverage: 2.6
      total: 117
    mcp: derived
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
screenshot: https://apis.io/screenshots/canonical/canonical-2026-06-20T173927.png
security:
- kind: authentication
  name: Canonical Authentication
  slug: canonical-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Canonical Domain Security
  slug: canonical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Canonical Vulnerability Disclosure
  slug: canonical-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Canonical Trust Center
  slug: canonical-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: canonical-lxd-provision-instance
  slug: canonical-lxd-provision-instance
- name: canonical-snapd-manage-snap
  slug: canonical-snapd-manage-snap
- name: canonical-ubuntu-security-cve-lookup
  slug: canonical-ubuntu-security-cve-lookup
slug: canonical
tags:
- Canonical
- Cloud
- Linux
- Open Source
- Ubuntu
- Containers
- Bare Metal
- Charms
- Identity
website: https://canonical.com/
---
