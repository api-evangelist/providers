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
  - sandbox
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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: templated
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 62
  human_in_the_loop: 21
  name: Dynatrace Agentic Access
  operation_count: 133
  slug: dynatrace-agentic-access
  summary_line: 133 operations · 62 acting · 21 human-in-the-loop
api_count: 7
apis:
- description: The Dynatrace Environment API provides access to monitoring data and configuration settings for a specific Dynatrace environment. It includes endpoints for metrics, problems, events, logs, entities, s
  name: Dynatrace Environment API
  slug: dynatrace-environment-api
- description: The Dynatrace Synthetic API v2 provides programmatic access to synthetic monitoring resources including browser monitors, HTTP monitors, and clickpaths. It allows you to create, update, delete, and re
  name: Dynatrace Synthetic API v2
  slug: dynatrace-synthetic-api-v2
- description: The Dynatrace Configuration API provides access to environment-level configuration settings including alerting profiles, anomaly detection rules, application detection rules, and data privacy settings
  name: Dynatrace Configuration API
  slug: dynatrace-configuration-api
- description: The Dynatrace OpenPipeline API enables configuration of data ingestion pipelines that handle observability, security, and business data from any source or format. It provides endpoints for managing pi
  name: Dynatrace OpenPipeline API
  slug: dynatrace-openpipeline-api
- description: The Dynatrace Automation API provides access to the Workflows automation engine, allowing you to create, manage, and execute automated workflows within Dynatrace. It supports orchestrating remediation
  name: Dynatrace Automation API
  slug: dynatrace-automation-api
- description: The Dynatrace Settings API 2.0 is the modern, schema-driven configuration API for managing Dynatrace environment settings objects. It replaces portions of the Configuration API v1 and provides a unifi
  name: Dynatrace Settings API 2.0
  slug: dynatrace-settings-api-v2
- description: The Dynatrace Extensions API 2.0 provides endpoints for managing monitoring extensions including uploading, activating, configuring, and removing extensions within a Dynatrace environment. It supports
  name: Dynatrace Extensions API 2.0
  slug: dynatrace-extensions-api-v2
- description: The Dynatrace DQL/Grail Query API enables execution of DQL (Dynatrace Query Language) queries against the Grail data lakehouse via REST. Queries execute asynchronously using a POST to initiate and GET
  name: Dynatrace DQL/Grail Query API
  slug: dynatrace-grail-dql-api
- description: 'The Dynatrace Access Tokens API v2 allows you to create, list, update, and delete API access tokens and ActiveGate tokens within a Dynatrace environment. It provides fine-grained scope management for '
  name: Dynatrace Access Tokens API v2
  slug: dynatrace-access-tokens-api-v2
- description: The Dynatrace Service-Level Objectives API is a management API for creating, editing, listing, deleting, and evaluating SLOs and SLO templates within a Dynatrace environment. It enables programmatic d
  name: Dynatrace Service-Level Objectives API
  slug: dynatrace-slo-api
- description: The Dynatrace Releases API provides an overview of releases deployed in your monitored environment. It allows you to retrieve information about software releases, deployment versions, and release stag
  name: Dynatrace Releases API
  slug: dynatrace-releases-api
- description: The Dynatrace Network Zones API enables you to manage network zones within a Dynatrace environment. It provides endpoints for listing all network zones, retrieving zone details including OneAgent coun
  name: Dynatrace Network Zones API
  slug: dynatrace-network-zones-api
- description: The Dynatrace Deployment API provides endpoints for downloading OneAgent and ActiveGate installers, listing available installer versions, and retrieving ActiveGate endpoint information. It enables aut
  name: Dynatrace Deployment API
  slug: dynatrace-deployment-api
- description: The Dynatrace Audit Logs API provides access to audit-related events within a Dynatrace environment including logins, logouts, configuration changes, and API token modifications. Audit logs are retain
  name: Dynatrace Audit Logs API
  slug: dynatrace-audit-logs-api
- description: The Dynatrace Business Events API v2 enables ingestion of business event data in JSON format into Dynatrace via the bizevents/ingest endpoint. It supports business-grade reporting and analytics throug
  name: Dynatrace Business Events API v2
  slug: dynatrace-business-events-api-v2
- description: The Dynatrace Application Security API provides endpoints for querying vulnerabilities, vulnerability details, remediation items, vulnerable functions, and security attacks within a Dynatrace environm
  name: Dynatrace Application Security API
  slug: dynatrace-application-security-api
- description: 'The Dynatrace Custom Tags API allows you to manage custom tags on monitored entities within a Dynatrace environment. It provides endpoints for reading, adding, and removing tags from entities such as '
  name: Dynatrace Custom Tags API
  slug: dynatrace-custom-tags-api
- description: The Dynatrace ActiveGate API enables you to view and manage ActiveGate configurations within a Dynatrace environment. It provides endpoints for listing ActiveGates, retrieving ActiveGate details, mana
  name: Dynatrace ActiveGate API
  slug: dynatrace-activegate-api
- description: 'The Dynatrace Credential Vault API enables management of credentials used for synthetic browser and HTTP monitors within a Dynatrace environment. It supports creating, listing, updating, and deleting '
  name: Dynatrace Credential Vault API
  slug: dynatrace-credential-vault-api
- description: The Dynatrace Document API provides a platform service for creating, managing, and sharing documents such as dashboards, notebooks, and launchpads within Dynatrace. It persists content-agnostic docume
  name: Dynatrace Document API
  slug: dynatrace-document-api
- description: The Dynatrace Grail Bucket Management API provides a public API for managing storage buckets within the Grail data lakehouse. It supports creating, updating, deleting, and truncating buckets for organ
  name: Dynatrace Grail Bucket Management API
  slug: dynatrace-grail-bucket-management-api
- description: 'The Dynatrace Davis AI API provides access to the Davis predictive and causal AI platform service for customized AI/ML analysis. It delivers time series forecasting, anomaly detection model training, '
  name: Dynatrace Davis AI API
  slug: dynatrace-davis-ai-api
- description: 'The Dynatrace Hub API provides programmatic access to the Dynatrace Hub catalog content including apps, extensions, and technologies in the context of the current environment. It supports listing and '
  name: Dynatrace Hub API
  slug: dynatrace-hub-api
- description: The Dynatrace OneAgent on a Host API enables you to check the configuration and status of OneAgent instances deployed on your hosts. It provides endpoints for listing hosts with OneAgent details, retr
  name: Dynatrace OneAgent on a Host API
  slug: dynatrace-oneagent-on-host-api
- description: 'The Dynatrace Platform Management API provides basic read-only information about the currently logged-in environment including environment settings, license information, and permissions. It is a core '
  name: Dynatrace Platform Management API
  slug: dynatrace-platform-management-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Operations for querying monitored entities and entity types
  name: Dynatrace Entities API
  phrasing_intents:
  - id: listEntities
    intent: List monitored entities matching a selector
    question: Which hosts or services is Dynatrace currently monitoring?
  - id: getEntity
    intent: Get a monitored entity's details
    question: What properties and relationships does a specific service or host have?
  - id: listEntityTypes
    intent: List available entity types
    question: What kinds of entities can Dynatrace monitor, like SERVICE or HOST?
  - id: getEntityType
    intent: Get an entity type's definition
    question: Which properties and relationships are available on the PROCESS_GROUP type?
  - id: lookupEntity
    intent: Look up an entity ID by display name
    question: I know a service's name, how do I get its entity ID?
  phrasing_ops: 5
  slug: dynatrace-entities-api
- baseURL: https://api.dynatrace.com
  baseurl_source: declared
  description: Operations for listing environments in the account
  name: Dynatrace Environments API
  phrasing_intents:
  - id: listEnvironments
    intent: List environments with their names and URLs
    question: What are the names and URLs of all environments in my account?
  phrasing_ops: 1
  slug: dynatrace-environments-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Operations for querying and ingesting custom events
  name: Dynatrace Events API
  phrasing_intents:
  - id: listEvents
    intent: List events in the environment
    question: Which deployment or configuration events happened in the last hour?
  - id: getEvent
    intent: Get an event's details
    question: What exactly happened in a particular event?
  - id: ingestEvent
    intent: Send a custom event such as a deployment
    question: How do I mark a deployment on the Dynatrace timeline?
  phrasing_ops: 3
  slug: dynatrace-events-api
- baseURL: https://api.dynatrace.com
  baseurl_source: declared
  description: Operations for managing user groups and group membership
  name: Dynatrace Groups API
  phrasing_intents:
  - id: listGroups
    intent: List user groups in an account
    question: Which groups control access and permissions in my account?
  - id: createGroup
    intent: Create a user group
    question: How do I create a new group so I can grant a team access?
  - id: getGroup
    intent: Get a group's details and permissions
    question: What permissions has a specific group been assigned?
  - id: updateGroup
    intent: Update a group's name and description
    question: Can I change a group's description without touching its permissions?
  - id: deleteGroup
    intent: Permanently delete a group
    question: Do users lose access when their group is permanently deleted?
  phrasing_ops: 5
  slug: dynatrace-groups-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Operations for ingesting, searching, aggregating, and exporting log records
  name: Dynatrace Logs API
  phrasing_intents:
  - id: searchLogs
    intent: Search log records
    question: How do I find error logs from the past hour in Grail?
  - id: ingestLogs
    intent: Send log records into Grail
    question: Can I push my application's log lines straight into Dynatrace?
  - id: aggregateLogs
    intent: Aggregate log records by fields
    question: How many errors did each service log today?
  - id: exportLogs
    intent: Export log records in bulk
    question: What's the best way to bulk-export logs to a SIEM or archive?
  phrasing_ops: 4
  slug: dynatrace-logs-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Operations for querying, managing, and ingesting time-series metrics
  name: Dynatrace Metrics API
  phrasing_intents:
  - id: listMetrics
    intent: List available metrics
    question: What metrics are available in my environment?
  - id: getMetricDescriptor
    intent: Get a metric's descriptor
    question: What unit and aggregations does a given metric support?
  - id: deleteCustomMetric
    intent: Delete a custom metric
    question: How do I get rid of a custom metric I no longer send?
  - id: queryMetricData
    intent: Query metric data points
    question: What was average CPU on my hosts over the last day?
  - id: ingestCustomMetrics
    intent: Send custom metric data points
    question: How do I push my own metric values using the line protocol?
  phrasing_ops: 5
  slug: dynatrace-metrics-api
- baseURL: https://api.dynatrace.com
  baseurl_source: declared
  description: Operations for querying account-level permissions
  name: Dynatrace Permissions API
  phrasing_intents:
  - id: listPermissions
    intent: List permissions defined for an account
    question: Which permissions can groups be granted in my account?
  phrasing_ops: 1
  slug: dynatrace-permissions-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Operations for querying and managing detected problems
  name: Dynatrace Problems API
  phrasing_intents:
  - id: listProblems
    intent: List detected problems
    question: What problems is Dynatrace reporting right now?
  - id: getProblem
    intent: Get a problem's details and root cause
    question: What is the root cause and impact of a specific problem?
  - id: closeProblem
    intent: Close an open problem
    question: How do I manually close a problem once it's resolved?
  - id: listProblemComments
    intent: List comments on a problem
    question: What investigation notes has the team left on a problem?
  - id: createProblemComment
    intent: Add a comment to a problem
    question: Can I attach a ticket reference to a problem as a comment?
  - id: getProblemComment
    intent: Get one comment on a problem
    question: Can I read a single problem comment by its ID?
  - id: updateProblemComment
    intent: Edit a comment on a problem
    question: Can I fix a typo in a comment I already left on a problem?
  - id: deleteProblemComment
    intent: Delete a comment from a problem
    question: How do I remove a comment posted on the wrong problem?
  phrasing_ops: 8
  slug: dynatrace-problems-api
- baseURL: https://api.dynatrace.com
  baseurl_source: declared
  description: Operations for managing account users
  name: Dynatrace Users API
  phrasing_intents:
  - id: listUsers
    intent: List users with profiles and memberships
    question: Which people are in my account and what groups are they in?
  - id: createUser
    intent: Create a user and send an invitation
    question: How do I invite a new user with their first and last name?
  - id: getUser
    intent: Get a user's profile
    question: What profile information do we hold for a particular user?
  - id: updateUser
    intent: Replace a user's profile and groups
    question: Can I correct a user's name and reset their groups in one update?
  - id: deleteUser
    intent: Permanently delete a user
    question: Does deleting a user cut off their access to every environment immediately?
  phrasing_ops: 5
  slug: dynatrace-users-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Access account-level audit logs.
  name: Dynatrace Account Audits API
  phrasing_intents:
  - id: AuditsController_listAuditsByAccount
    intent: List account-level audit log entries
    question: Who changed settings in my Dynatrace account last week?
  phrasing_ops: 1
  slug: dynatrace-account-audits-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Retrieve the limits configured for an account.
  name: Dynatrace Account limits API
  phrasing_intents:
  - id: getLimitsForAccount
    intent: Show the limits defined for an account
    question: What limits apply to my Dynatrace account?
  phrasing_ops: 1
  slug: dynatrace-account-limits-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Manage account settings such as cost-center and product field values.
  name: Dynatrace Account Settings API
  phrasing_intents:
  - id: AccountsController_listCostcenterCostAllocationValues
    intent: List allowed cost center values
    question: Which cost center values can I allocate Dynatrace spend to?
  - id: AccountsController_createCostcenterCostAllocationValues
    intent: Add new cost center values
    question: Can I add a few new cost centers without touching the existing ones?
  - id: AccountsController_replaceCostcenterCostAllocationValues
    intent: Replace the full set of cost center values
    question: How do I overwrite all my cost centers with a new list at once?
  - id: AccountsController_deleteCostcenterCostAllocationValue
    intent: Delete one cost center value
    question: How do I remove a single cost center that we no longer use?
  - id: AccountsController_listProductCostAllocationValues
    intent: List allowed product allocation values
    question: Which product values are set up for cost allocation on my account?
  - id: AccountsController_createProductCostAllocationValues
    intent: Add new product allocation values
    question: Can I add another product for cost allocation while keeping the current ones?
  - id: AccountsController_replaceProductCostAllocationValues
    intent: Replace the full set of product values
    question: How do I overwrite the product allocation list with a fresh set?
  - id: AccountsController_deleteProductCostAllocationValue
    intent: Delete one product allocation value
    question: How do I remove a product we stopped allocating costs to?
  phrasing_ops: 8
  slug: dynatrace-account-settings-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: View platform subscriptions and their usage, cost, forecast, and rate-card data.
  name: Dynatrace Dynatrace Platform Subscription API
  phrasing_intents:
  - id: SubscriptionsController_listSubscriptions
    intent: List an account's subscriptions
    question: Which Dynatrace Platform Subscriptions does my account have?
  - id: SubscriptionsController_getForecast
    intent: Forecast usage by end of annual commitment
    question: Will we overrun our annual commitment before the term ends?
  - id: SubscriptionsController_getSubscription
    intent: Get one subscription's details
    question: What are the terms and budget of a specific subscription?
  - id: getEnvironmentUsage
    intent: Get per-environment usage (deprecated v2)
    question: Is the older v2 per-environment usage endpoint still available?
  - id: SubscriptionsController_getTotalSubscriptionUsage
    intent: Get a subscription's usage by date
    question: How much of my subscription have we consumed each day?
  - id: SubscriptionsController_getTotalSubscriptionCost
    intent: Get a subscription's aggregated cost by date
    question: What has my subscription cost us day by day?
  - id: getEnvironmentCost
    intent: Get per-environment cost (deprecated v2)
    question: Where is the old v2 report of SaaS costs per environment?
  - id: getEnvironmentCostV3
    intent: Get subscription cost broken down by environment
    question: Which environment is driving most of our subscription cost?
  phrasing_ops: 11
  slug: dynatrace-dynatrace-platform-subscription-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: List environments and clusters and manage their IP allowlist configuration.
  name: Dynatrace Environment management API
  phrasing_intents:
  - id: EnvironmentResourcesController_getEnvironmentResources
    intent: List environments and management zones
    question: Which management zones exist in each of my environments?
  - id: EnvironmentResourcesController_getEnvironments
    intent: List environments in an account (v2)
    question: What environments does my account currently have, using the v2 listing?
  - id: EnvironmentResourcesController_getClusters
    intent: List clusters in a managed account
    question: Which Managed clusters belong to my account?
  - id: EnvironmentResourcesController_getConfig
    intent: Get an environment's IP allowlist
    question: Which IP addresses are allowed to reach my environment?
  - id: EnvironmentResourcesController_setConfig
    intent: Set an environment's IP allowlist
    question: How do I restrict access to my tenant to specific IP ranges?
  phrasing_ops: 5
  slug: dynatrace-environment-management-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Create and manage user groups and their members.
  name: Dynatrace Group management API
  phrasing_intents:
  - id: GroupsController_getGroups
    intent: List an account's user groups
    question: What user groups are defined in my Dynatrace account?
  - id: GroupsController_createGroups
    intent: Create several user groups at once
    question: Can I create multiple user groups in a single request?
  - id: GroupsController_getUsersForGroup
    intent: List the members of a group
    question: Who belongs to a particular user group?
  - id: GroupsController_editGroup
    intent: Edit a group's name, description or SAML values
    question: Can I change the federated attribute values that map SSO users to a group?
  - id: GroupsController_deleteGroup
    intent: Delete a user group
    question: What happens to members when I delete a user group?
  phrasing_ops: 5
  slug: dynatrace-group-management-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Manage notifications for an account.
  name: Dynatrace Notifications API
  phrasing_intents:
  - id: listNotifications
    intent: List account notifications (deprecated v1)
    question: Is the older v1 notifications search still supported, and until when?
  - id: listNotificationsV2
    intent: List account notifications
    question: What budget or usage alerts has my account received recently?
  phrasing_ops: 2
  slug: dynatrace-notifications-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Manage group permissions (deprecated; use policy management instead).
  name: Dynatrace Permission management API
  phrasing_intents:
  - id: PermissionsController_getGroupPermissions
    intent: List a group's role-based permissions
    question: What legacy role-based permissions does a group currently have?
  - id: PermissionsController_addGroupPermissions
    intent: Add role-based permissions to a group
    question: Can I grant extra permissions to a group while keeping what it has?
  - id: PermissionsController_overwriteGroupPermissions
    intent: Overwrite a group's role-based permissions
    question: How do I replace a group's entire permission set in one go?
  - id: PermissionsController_removeGroupPermissions
    intent: Remove a permission from a group
    question: How do I revoke one permission from a group for a single environment?
  phrasing_ops: 4
  slug: dynatrace-permission-management-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Manage platform tokens for account users.
  name: Dynatrace Platform tokens API
  phrasing_intents:
  - id: getPlatformTokensForAccount
    intent: List platform tokens in an account
    question: Which platform tokens exist in my account and who owns them?
  - id: generatePlatformToken
    intent: Create a platform token for a user
    question: How do I generate a platform token with specific scopes for a user?
  - id: deletePlatformToken
    intent: Delete a platform token
    question: How do I permanently delete a leaked platform token?
  - id: updatePlatformTokenExpirationDate
    intent: Change a platform token's expiration date
    question: Can I extend a platform token before it expires?
  - id: updatePlatformTokenStatus
    intent: Enable or disable a platform token
    question: Can I temporarily disable a platform token without deleting it?
  phrasing_ops: 5
  slug: dynatrace-platform-tokens-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Manage IAM policies, policy bindings, and permission boundaries.
  name: Dynatrace Policy management API
  phrasing_intents:
  - id: validateNewLevelPolicy
    intent: Validate a new policy draft (deprecated)
    question: Can I dry-run a brand-new IAM policy statement before creating it?
  - id: validateLevelPolicy
    intent: Validate changes to an existing policy (deprecated)
    question: Can I check an edit to an existing policy is valid before saving it?
  - id: getEffectivePermissions
    intent: Get effective permissions for a user or group
    question: What can a given user actually do once all their policies are combined?
  - id: getPolicyOverviewList
    intent: List policies for a level including inherited ones
    question: Which policies apply to an environment, including ones inherited from the account?
  - id: getLevelPolicies
    intent: List policies defined natively on a level
    question: Which policies were created directly on this level, not inherited?
  - id: createLevelPolicy
    intent: Create an IAM policy
    question: How do I write a new IAM policy with my own statement?
  - id: getLevelPolicy
    intent: Get one policy's statement and details
    question: What statement does a specific policy contain?
  - id: updateLevelPolicy
    intent: Update or create a policy by UUID
    question: How do I change the statement of an existing policy?
  phrasing_ops: 27
  slug: dynatrace-policy-management-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Look up reference data such as time zones, regions, and available permissions.
  name: Dynatrace Reference data API
  phrasing_intents:
  - id: ReferenceDataController_
    intent: List available time zones
    question: Which time zones does Dynatrace account management accept?
  - id: getRefV1Regions
    intent: List available regions
    question: Which regions can an environment be hosted in?
  - id: ReferenceDataController_getPermissions
    intent: List all permissions that exist
    question: What is the full catalog of permission names I can assign?
  phrasing_ops: 3
  slug: dynatrace-reference-data-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Manage service users within an account.
  name: Dynatrace Service user management API
  phrasing_intents:
  - id: ServiceUsersController_createServiceUserForAccount
    intent: Create a service user
    question: How do I create a service user for an automation or CI pipeline?
  - id: ServiceUsersController_getServiceUsersFromAccount
    intent: List service users in an account
    question: Which non-human service users exist in my account?
  - id: ServiceUsersController_updateServiceUserForAccount
    intent: Rename or redescribe a service user
    question: Can I rename a service user after creating it?
  - id: ServiceUsersController_getServiceUser
    intent: Get a service user
    question: What are the details of a specific service user?
  - id: ServiceUsersController_deleteUser
    intent: Remove a service user
    question: How do I delete a service user we no longer use?
  phrasing_ops: 5
  slug: dynatrace-service-user-management-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Manage users in an account and their group memberships.
  name: Dynatrace User management API
  phrasing_intents:
  - id: UsersController_getUsers
    intent: List users of an account
    question: Who has access to my Dynatrace account?
  - id: UsersController_createUserForAccount
    intent: Invite a user to an account by email
    question: How do I add a colleague to the account using just their email?
  - id: UsersController_getUserGroups
    intent: List the groups a user belongs to
    question: Which groups is a given person a member of?
  - id: UsersController_addUserToGroups
    intent: Add a user to more groups
    question: Can I add someone to extra groups without dropping their current ones?
  - id: UsersController_removeUserFromAccount
    intent: Remove a user from an account
    question: How do I offboard someone from the account entirely?
  - id: UsersController_replaceUserGroups
    intent: Set a user's group membership exactly
    question: Can I overwrite a user's groups so they belong only to the ones I specify?
  - id: UsersController_removeUserFromGroups
    intent: Remove a user from specific groups
    question: How do I take someone out of one group but keep them in the account?
  phrasing_ops: 7
  slug: dynatrace-user-management-api
- baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  baseurl_source: declared
  description: Manage workload identity federation trust policies and their service-user mappings.
  name: Dynatrace Workload Identity Federation API
  phrasing_intents:
  - id: listWifTrustPolicies
    intent: List workload identity trust policies
    question: Which external identity providers are trusted for workload identity federation?
  - id: createWifTrustPolicy
    intent: Create a workload identity trust policy
    question: How do I let CI jobs authenticate with OIDC tokens instead of secrets?
  - id: getWifTrustPolicy
    intent: Get a workload identity trust policy
    question: What issuer and audience does a specific trust policy accept?
  - id: updateWifTrustPolicy
    intent: Update a workload identity trust policy
    question: Can I change the issuer or audience on an existing trust policy?
  - id: deleteWifTrustPolicy
    intent: Delete a workload identity trust policy
    question: How do I stop trusting an identity provider permanently?
  - id: patchWifTrustPolicyStatus
    intent: Enable or disable a trust policy
    question: Can I temporarily switch off a trust policy without deleting it?
  - id: listWifServiceUserMappings
    intent: List service user mappings for a trust policy
    question: Which service users can federated workloads assume under a trust policy?
  - id: createWifServiceUserMapping
    intent: Map federated identities to a service user
    question: How do I map claims from an external token to a service user and scopes?
  phrasing_ops: 12
  slug: dynatrace-workload-identity-federation-api
arazzos:
- description: Enumerate users, groups, and permissions across a Dynatrace account for an access review.
  name: Dynatrace Audit Account Access
  slug: dynatrace-account-access-audit-workflow
- description: Resolve a service by name, push a deployment event onto its timeline, and verify it.
  name: Dynatrace Annotate a Deployment with a Custom Event
  slug: dynatrace-annotate-deployment-event-workflow
- description: List entities matching a selector and expand the top match with its relationships.
  name: Dynatrace Map an Entity's Dependencies
  slug: dynatrace-entity-dependency-map-workflow
- description: List entity types, read one type definition, and list a sample of entities of that type.
  name: Dynatrace Discover an Entity Type and Sample Its Entities
  slug: dynatrace-entity-type-discovery-workflow
- description: Aggregate error logs by source, pull the matching records, and raise an error event.
  name: Dynatrace Investigate Error Logs and Annotate
  slug: dynatrace-error-log-investigation-workflow
- description: Aggregate logs to size the export, then bulk-export the matching records page by page.
  name: Dynatrace Export Logs for SIEM Forwarding
  slug: dynatrace-export-logs-for-siem-workflow
- description: Stream log records into Grail and immediately search them back to confirm ingestion.
  name: Dynatrace Ingest Log Records and Search Them Back
  slug: dynatrace-ingest-and-search-logs-workflow
- description: Push custom metric data via MINT, confirm the metric is registered, and query it back.
  name: Dynatrace Ingest a Custom Metric and Verify It
  slug: dynatrace-ingest-and-verify-metric-workflow
- description: Confirm a metric exists, query its data points, and raise a custom alert event.
  name: Dynatrace Query a Metric and Raise an Alert Event
  slug: dynatrace-metric-threshold-alert-workflow
- description: Create a group, invite a user assigned to that group, and confirm the membership.
  name: Dynatrace Onboard a User into a New Group
  slug: dynatrace-onboard-account-user-workflow
- description: Add a comment to a problem, read it back, and update its content.
  name: Dynatrace Manage a Problem Comment Lifecycle
  slug: dynatrace-problem-comment-lifecycle-workflow
- description: Confirm a problem, post a collaboration comment, and list the full comment thread.
  name: Dynatrace Add a Comment to a Problem and Read the Thread
  slug: dynatrace-problem-comment-thread-workflow
- description: List open problems, inspect the top one, annotate it, and close it.
  name: Dynatrace Triage and Close a Problem
  slug: dynatrace-problem-triage-and-close-workflow
- description: Resolve a service, read a key metric, and list its open problems and recent events.
  name: Dynatrace Service Health Snapshot
  slug: dynatrace-service-health-snapshot-workflow
- description: Resolve a service by name, read its details, and list problems impacting it.
  name: Dynatrace Find Problems Affecting a Named Service
  slug: dynatrace-service-problem-lookup-workflow
artifact_total: 594
asyncapis:
- description: Dynatrace delivers problem lifecycle notifications to client-provided webhook endpoints via HTTP POST. When a problem is opened, updated, merged, or resolved, Dynatrace sends a notification payload to
  name: Dynatrace Problem Notifications API
  slug: dynatrace-problems-asyncapi
collections:
- collection_type: postman
  name: Dynatrace Account Management API
  slug: postman-dynatrace-account-management-api
- collection_type: postman
  name: Dynatrace Entities API v2
  slug: postman-dynatrace-entities-api-v2
- collection_type: postman
  name: Dynatrace Events API v2
  slug: postman-dynatrace-events-api-v2
- collection_type: postman
  name: Dynatrace Log Monitoring API v2
  slug: postman-dynatrace-log-monitoring-api-v2
- collection_type: postman
  name: Dynatrace Metrics API v2
  slug: postman-dynatrace-metrics-api-v2
- collection_type: postman
  name: Dynatrace Problems API v2
  slug: postman-dynatrace-problems-api-v2
- collection_type: open
  name: Dynatrace Account Management API
  slug: open-dynatrace-account-management-api
- collection_type: open
  name: Dynatrace Entities API v2
  slug: open-dynatrace-entities-api-v2
- collection_type: open
  name: Dynatrace Account Management Entities API
  slug: open-dynatrace-entities-api
- collection_type: open
  name: Dynatrace Account Management Entities Environments API
  slug: open-dynatrace-environments-api
- collection_type: open
  name: Dynatrace Events API v2
  slug: open-dynatrace-events-api-v2
- collection_type: open
  name: Dynatrace Account Management Entities Events API
  slug: open-dynatrace-events-api
- collection_type: open
  name: Dynatrace Account Management Entities Groups API
  slug: open-dynatrace-groups-api
- collection_type: open
  name: Dynatrace Log Monitoring API v2
  slug: open-dynatrace-log-monitoring-api-v2
- collection_type: open
  name: Dynatrace Account Management Entities Logs API
  slug: open-dynatrace-logs-api
- collection_type: open
  name: Dynatrace Metrics API v2
  slug: open-dynatrace-metrics-api-v2
- collection_type: open
  name: Dynatrace Account Management Entities Metrics API
  slug: open-dynatrace-metrics-api
- collection_type: open
  name: Dynatrace Account Management Entities Permissions API
  slug: open-dynatrace-permissions-api
- collection_type: open
  name: Dynatrace Problems API v2
  slug: open-dynatrace-problems-api-v2
- collection_type: open
  name: Dynatrace Account Management Entities Problems API
  slug: open-dynatrace-problems-api
- collection_type: open
  name: Dynatrace Account Management Entities Users API
  slug: open-dynatrace-users-api
common:
- group: design
  href: https://artifacts.apis.io/dynatrace/rules/dynatrace-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/dynatrace-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/rules/dynatrace-rules.yml
  title: ''
  type: Spectral
  url: rules/dynatrace-rules.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/rules/dynatrace-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/dynatrace-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/rules/dynatrace-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/dynatrace-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-problems-v2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-problems-v2-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-metrics-v2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-metrics-v2-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-log-monitoring-v2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-log-monitoring-v2-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-events-v2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-events-v2-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-entities-v2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-entities-v2-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-account-management-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-account-management-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/vocabulary/dynatrace-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dynatrace-vocabulary.yml
- group: start
  href: https://artifacts.apis.io/dynatrace/sandbox/dynatrace-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/dynatrace-sandbox.yml
- group: other
  href: https://artifacts.apis.io/dynatrace/hosts/dynatrace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dynatrace-hosts.yml
- group: other
  href: https://artifacts.apis.io/dynatrace/vendors/dynatrace-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dynatrace-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.dynatrace.com/signup/playground/infrastructure/
- group: company
  title: ''
  type: Newsroom
  url: https://www.dynatrace.com/news/tag/business-observability/
- group: company
  title: ''
  type: Website
  url: https://www.dynatrace.com/
- group: other
  href: https://artifacts.apis.io/dynatrace/capabilities/dynatrace-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/dynatrace-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/dynatrace/agentic-access/dynatrace-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dynatrace-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/dynatrace/security/dynatrace-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dynatrace-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dynatrace/security/dynatrace-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dynatrace-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dynatrace/security/dynatrace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dynatrace-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/dynatrace/authentication/dynatrace-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dynatrace-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dynatrace/scopes/dynatrace-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/dynatrace-scopes.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/Dynatrace/dynatrace-for-ai
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dynatrace/overview
- group: design
  href: https://artifacts.apis.io/dynatrace/arazzo/dynatrace-account-access-audit-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dynatrace-account-access-audit-workflow.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/arazzo/dynatrace-annotate-deployment-event-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dynatrace-annotate-deployment-event-workflow.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/arazzo/dynatrace-entity-dependency-map-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dynatrace-entity-dependency-map-workflow.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/arazzo/dynatrace-entity-type-discovery-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dynatrace-entity-type-discovery-workflow.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/arazzo/dynatrace-error-log-investigation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dynatrace-error-log-investigation-workflow.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/arazzo/dynatrace-export-logs-for-siem-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dynatrace-export-logs-for-siem-workflow.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/arazzo/dynatrace-ingest-and-search-logs-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dynatrace-ingest-and-search-logs-workflow.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/arazzo/dynatrace-ingest-and-verify-metric-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dynatrace-ingest-and-verify-metric-workflow.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/arazzo/dynatrace-metric-threshold-alert-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dynatrace-metric-threshold-alert-workflow.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/arazzo/dynatrace-onboard-account-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dynatrace-onboard-account-user-workflow.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/arazzo/dynatrace-problem-comment-lifecycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dynatrace-problem-comment-lifecycle-workflow.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/arazzo/dynatrace-problem-comment-thread-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dynatrace-problem-comment-thread-workflow.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/arazzo/dynatrace-problem-triage-and-close-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dynatrace-problem-triage-and-close-workflow.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/arazzo/dynatrace-service-health-snapshot-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dynatrace-service-health-snapshot-workflow.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/arazzo/dynatrace-service-problem-lookup-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/dynatrace-service-problem-lookup-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dynatrace
- group: start
  title: ''
  type: Portal
  url: https://www.dynatrace.com/support/help/dynatrace-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dynatrace.com/docs/dynatrace-api
- group: auth
  title: ''
  type: Authentication
  url: https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dynatrace.com/support/help/dynatrace-api/basics
- group: docs
  title: ''
  type: APIReference
  url: https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-response-codes
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.dynatrace.com/docs/whats-new/dynatrace-api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dynatrace.com/company/trust-center/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dynatrace.com/company/trust-center/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.dynatrace.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dynatrace.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.dynatrace.com/signup/
- group: operate
  title: ''
  type: Support
  url: https://community.dynatrace.com/
- group: company
  title: ''
  type: Blog
  url: https://community.dynatrace.com/t5/Developer-Blog/bg-p/dev_blog
- group: operate
  title: ''
  type: StatusPage
  url: https://dynatrace.status.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Dynatrace
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dynatrace.com/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/dynatrace
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/dynatrace
- group: docs
  href: https://artifacts.apis.io/dynatrace/json-schema/dynatrace-metric-series-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/dynatrace-metric-series-schema.json
- group: docs
  href: https://artifacts.apis.io/dynatrace/json-schema/dynatrace-problem-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/dynatrace-problem-schema.json
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-context.jsonld
- group: build
  title: ''
  type: SDKs
  url: https://developer.dynatrace.com/develop/sdks/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.dynatrace.com/develop/access-platform-apis-from-outside/
- group: auth
  title: ''
  type: Security
  url: https://docs.dynatrace.com/docs/manage/identity-access-management
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Dynatrace/dynatrace-api
- group: other
  title: ''
  type: Marketplace
  url: https://www.dynatrace.com/hub/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/basics/deprecation-migration-guides
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dynatrace.com/plan/platform-services/
- group: build
  title: Configuration as Code CLI
  type: CLI
  url: https://github.com/Dynatrace/dynatrace-configuration-as-code
- group: build
  title: Java OneAgent SDK
  type: SDKs
  url: https://github.com/Dynatrace/OneAgent-SDK-for-Java
- group: build
  title: Python OneAgent SDK
  type: SDKs
  url: https://github.com/Dynatrace/OneAgent-SDK-for-Python
- group: build
  title: Node.js OneAgent SDK
  type: SDKs
  url: https://github.com/Dynatrace/OneAgent-SDK-for-NodeJs
- group: build
  title: .NET OneAgent SDK
  type: SDKs
  url: https://github.com/Dynatrace/OneAgent-SDK-for-dotnet
- group: build
  title: C OneAgent SDK
  type: SDKs
  url: https://github.com/Dynatrace/OneAgent-SDK-for-C
- group: build
  title: Swift Mobile SDK
  type: SDKs
  url: https://github.com/Dynatrace/swift-mobile-sdk
- group: build
  title: Workflow Samples
  type: CodeExamples
  url: https://github.com/Dynatrace/Dynatrace-workflow-samples
- group: build
  title: Code Snippets
  type: CodeExamples
  url: https://github.com/Dynatrace/snippets
- group: build
  title: Community Examples
  type: CodeExamples
  url: https://github.com/Dynatrace/community-examples
- group: learn
  title: Tutorials
  type: Tutorials
  url: https://github.com/Dynatrace/Dynatrace-Tutorial
- group: design
  href: https://artifacts.apis.io/dynatrace/rules/dynatrace-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/dynatrace-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/vocabulary/dynatrace-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/dynatrace-vocabulary.yaml
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-account-management-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-account-management-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-dynatrace-metric-series-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-dynatrace-metric-series-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-dynatrace-problem-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-dynatrace-problem-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-entities-api-v2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-entities-api-v2-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-events-api-v2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-events-api-v2-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-log-monitoring-api-v2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-log-monitoring-api-v2-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-metrics-api-v2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-metrics-api-v2-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-problems-api-v2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-problems-api-v2-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-problems-entity-ref-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-problems-entity-ref-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-problems-impacted-entity-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-problems-impacted-entity-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-problems-problem-details-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-problems-problem-details-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-problems-problem-notification-payload-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-problems-problem-notification-payload-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-problems-webhook-header-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-problems-webhook-header-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynatrace/json-ld/dynatrace-problems-webhook-notification-config-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynatrace-problems-webhook-notification-config-context.jsonld
- group: build
  href: https://artifacts.apis.io/dynatrace/packages/dynatrace-packages.yml
  title: ''
  type: Packages
  url: packages/dynatrace-packages.yml
- group: build
  href: https://artifacts.apis.io/dynatrace/packages/dynatrace-packages.yml
  title: ''
  type: SDKs
  url: packages/dynatrace-packages.yml
- group: agent
  href: https://artifacts.apis.io/dynatrace/well-known/dynatrace-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dynatrace-well-known.yml
- group: auth
  href: https://artifacts.apis.io/dynatrace/well-known/dynatrace-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dynatrace-security.txt
- group: other
  href: https://artifacts.apis.io/dynatrace/well-known/dynatrace-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/dynatrace-openid-configuration.json
- group: agent
  href: https://artifacts.apis.io/dynatrace/mcp/dynatrace-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dynatrace-mcp.yml
- group: build
  href: https://artifacts.apis.io/dynatrace/mcp/dynatrace-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dynatrace-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dynatrace/llms/dynatrace-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dynatrace-llms.txt
- group: design
  href: https://artifacts.apis.io/dynatrace/conformance/dynatrace-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dynatrace-conformance.yml
- group: auth
  href: https://artifacts.apis.io/dynatrace/security/dynatrace-trust-center.yml
  title: ''
  type: Compliance
  url: security/dynatrace-trust-center.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/errors/dynatrace-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dynatrace-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/lifecycle/dynatrace-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dynatrace-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/basics/deprecation-migration-guides
- group: design
  href: https://artifacts.apis.io/dynatrace/conventions/dynatrace-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dynatrace-conventions.yml
- group: operate
  href: https://artifacts.apis.io/dynatrace/changelog/dynatrace-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dynatrace-changelog.yml
- group: build
  href: https://artifacts.apis.io/dynatrace/cli/dynatrace-cli.yml
  title: ''
  type: CLI
  url: cli/dynatrace-cli.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/components/dynatrace-components.yml
  title: ''
  type: Components
  url: components/dynatrace-components.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/data-model/dynatrace-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dynatrace-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/dynatrace/plans/dynatrace-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dynatrace-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dynatrace/rate-limits/dynatrace-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dynatrace-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dynatrace/finops/dynatrace-finops.yml
  title: ''
  type: FinOps
  url: finops/dynatrace-finops.yml
- group: design
  href: https://artifacts.apis.io/dynatrace/asyncapi/dynatrace-problems-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/dynatrace-problems-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/dynatrace/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/dynatrace/skills/dynatrace-triage-problem.md
  title: ''
  type: AgentSkill
  url: skills/dynatrace-triage-problem.md
- group: agent
  href: https://artifacts.apis.io/dynatrace/skills/dynatrace-ingest-telemetry.md
  title: ''
  type: AgentSkill
  url: skills/dynatrace-ingest-telemetry.md
- group: agent
  href: https://artifacts.apis.io/dynatrace/skills/dynatrace-manage-account-access.md
  title: ''
  type: AgentSkill
  url: skills/dynatrace-manage-account-access.md
- group: other
  title: ''
  type: Marketplace
  url: https://www.dynatrace.com/hub/detail/dynatrace-mcp-server/
- group: other
  href: https://artifacts.apis.io/dynatrace/overlays/dynatrace-entities-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dynatrace-entities-overlay.yaml
- group: other
  href: https://artifacts.apis.io/dynatrace/overlays/dynatrace-environments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dynatrace-environments-overlay.yaml
- group: other
  href: https://artifacts.apis.io/dynatrace/overlays/dynatrace-events-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dynatrace-events-overlay.yaml
- group: other
  href: https://artifacts.apis.io/dynatrace/overlays/dynatrace-groups-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dynatrace-groups-overlay.yaml
- group: other
  href: https://artifacts.apis.io/dynatrace/overlays/dynatrace-logs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dynatrace-logs-overlay.yaml
- group: other
  href: https://artifacts.apis.io/dynatrace/overlays/dynatrace-metrics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dynatrace-metrics-overlay.yaml
- group: other
  href: https://artifacts.apis.io/dynatrace/overlays/dynatrace-permissions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dynatrace-permissions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/dynatrace/overlays/dynatrace-problems-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dynatrace-problems-overlay.yaml
- group: other
  href: https://artifacts.apis.io/dynatrace/overlays/dynatrace-users-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dynatrace-users-overlay.yaml
- group: start
  title: ''
  type: SignUp
  url: https://www.dynatrace.com/signup/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/kinlaneapi/dynatrace/overview
- group: start
  title: ''
  type: Trial
  url: https://www.dynatrace.com/trial/
- group: docs
  href: https://artifacts.apis.io/dynatrace/openapi/dynatrace-account-management-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/dynatrace-account-management-api-openapi.json
created: '2025-01-08'
description: Dynatrace is a software intelligence platform that provides application performance monitoring, artificial intelligence for operations, cloud infrastructure monitoring, and digital experience management.
examples:
- key_count: 3
  name: Account Management Api Environment Collection Example
  slug: account-management-api-environment-collection-example
- key_count: 4
  name: Account Management Api Environment Example
  slug: account-management-api-environment-example
- key_count: 3
  name: Account Management Api Group Collection Example
  slug: account-management-api-group-collection-example
- key_count: 2
  name: Account Management Api Group Create Request Example
  slug: account-management-api-group-create-request-example
- key_count: 6
  name: Account Management Api Group Example
  slug: account-management-api-group-example
- key_count: 1
  name: Account Management Api Permission Collection Example
  slug: account-management-api-permission-collection-example
- key_count: 4
  name: Account Management Api Permission Example
  slug: account-management-api-permission-example
- key_count: 3
  name: Account Management Api User Collection Example
  slug: account-management-api-user-collection-example
- key_count: 4
  name: Account Management Api User Create Request Example
  slug: account-management-api-user-create-request-example
- key_count: 6
  name: Account Management Api User Example
  slug: account-management-api-user-example
- key_count: 3
  name: Dynatrace Account Management Environment Collection Example
  slug: dynatrace-account-management-environment-collection-example
- key_count: 4
  name: Dynatrace Account Management Environment Example
  slug: dynatrace-account-management-environment-example
- key_count: 1
  name: Dynatrace Account Management Error Envelope Example
  slug: dynatrace-account-management-error-envelope-example
- key_count: 2
  name: Dynatrace Account Management Error Example
  slug: dynatrace-account-management-error-example
- key_count: 3
  name: Dynatrace Account Management Group Collection Example
  slug: dynatrace-account-management-group-collection-example
- key_count: 2
  name: Dynatrace Account Management Group Create Request Example
  slug: dynatrace-account-management-group-create-request-example
- key_count: 6
  name: Dynatrace Account Management Group Example
  slug: dynatrace-account-management-group-example
- key_count: 1
  name: Dynatrace Account Management Permission Collection Example
  slug: dynatrace-account-management-permission-collection-example
- key_count: 4
  name: Dynatrace Account Management Permission Example
  slug: dynatrace-account-management-permission-example
- key_count: 3
  name: Dynatrace Account Management User Collection Example
  slug: dynatrace-account-management-user-collection-example
- key_count: 4
  name: Dynatrace Account Management User Create Request Example
  slug: dynatrace-account-management-user-create-request-example
- key_count: 6
  name: Dynatrace Account Management User Example
  slug: dynatrace-account-management-user-example
- key_count: 4
  name: Dynatrace Entities V2 Constraint Violation Example
  slug: dynatrace-entities-v2-constraint-violation-example
- key_count: 4
  name: Dynatrace Entities V2 Entity Collection Example
  slug: dynatrace-entities-v2-entity-collection-example
- key_count: 10
  name: Dynatrace Entities V2 Entity Example
  slug: dynatrace-entities-v2-entity-example
- key_count: 2
  name: Dynatrace Entities V2 Entity Lookup Request Example
  slug: dynatrace-entities-v2-entity-lookup-request-example
- key_count: 4
  name: Dynatrace Entities V2 Entity Tag Example
  slug: dynatrace-entities-v2-entity-tag-example
- key_count: 3
  name: Dynatrace Entities V2 Entity Type Collection Example
  slug: dynatrace-entities-v2-entity-type-collection-example
- key_count: 6
  name: Dynatrace Entities V2 Entity Type Example
  slug: dynatrace-entities-v2-entity-type-example
- key_count: 3
  name: Dynatrace Entities V2 Entity Type Property Example
  slug: dynatrace-entities-v2-entity-type-property-example
- key_count: 2
  name: Dynatrace Entities V2 Entity Type Relationship Example
  slug: dynatrace-entities-v2-entity-type-relationship-example
- key_count: 1
  name: Dynatrace Entities V2 Error Envelope Example
  slug: dynatrace-entities-v2-error-envelope-example
- key_count: 3
  name: Dynatrace Entities V2 Error Example
  slug: dynatrace-entities-v2-error-example
- key_count: 2
  name: Dynatrace Entities V2 Management Zone Example
  slug: dynatrace-entities-v2-management-zone-example
- key_count: 4
  name: Dynatrace Events V2 Constraint Violation Example
  slug: dynatrace-events-v2-constraint-violation-example
- key_count: 3
  name: Dynatrace Events V2 Entity Stub Example
  slug: dynatrace-events-v2-entity-stub-example
- key_count: 1
  name: Dynatrace Events V2 Error Envelope Example
  slug: dynatrace-events-v2-error-envelope-example
- key_count: 3
  name: Dynatrace Events V2 Error Example
  slug: dynatrace-events-v2-error-example
- key_count: 4
  name: Dynatrace Events V2 Event Collection Example
  slug: dynatrace-events-v2-event-collection-example
- key_count: 8
  name: Dynatrace Events V2 Event Example
  slug: dynatrace-events-v2-event-example
- key_count: 7
  name: Dynatrace Events V2 Event Ingest Payload Example
  slug: dynatrace-events-v2-event-ingest-payload-example
- key_count: 2
  name: Dynatrace Events V2 Event Ingest Result Example
  slug: dynatrace-events-v2-event-ingest-result-example
- key_count: 2
  name: Dynatrace Events V2 Event Ingest Result Item Example
  slug: dynatrace-events-v2-event-ingest-result-item-example
- key_count: 4
  name: Dynatrace Log Monitoring V2 Constraint Violation Example
  slug: dynatrace-log-monitoring-v2-constraint-violation-example
- key_count: 1
  name: Dynatrace Log Monitoring V2 Error Envelope Example
  slug: dynatrace-log-monitoring-v2-error-envelope-example
- key_count: 3
  name: Dynatrace Log Monitoring V2 Error Example
  slug: dynatrace-log-monitoring-v2-error-example
- key_count: 2
  name: Dynatrace Log Monitoring V2 Log Aggregate Group Example
  slug: dynatrace-log-monitoring-v2-log-aggregate-group-example
- key_count: 1
  name: Dynatrace Log Monitoring V2 Log Aggregate Result Example
  slug: dynatrace-log-monitoring-v2-log-aggregate-result-example
- key_count: 2
  name: Dynatrace Log Monitoring V2 Log Export Result Example
  slug: dynatrace-log-monitoring-v2-log-export-result-example
- key_count: 5
  name: Dynatrace Log Monitoring V2 Log Ingest Record Example
  slug: dynatrace-log-monitoring-v2-log-ingest-record-example
- key_count: 6
  name: Dynatrace Log Monitoring V2 Log Record Example
  slug: dynatrace-log-monitoring-v2-log-record-example
- key_count: 2
  name: Dynatrace Log Monitoring V2 Log Record Search Result Example
  slug: dynatrace-log-monitoring-v2-log-record-search-result-example
- key_count: 2
  name: Dynatrace Metric Series Example
  slug: dynatrace-metric-series-example
- key_count: 4
  name: Dynatrace Metrics V2 Constraint Violation Example
  slug: dynatrace-metrics-v2-constraint-violation-example
- key_count: 1
  name: Dynatrace Metrics V2 Error Envelope Example
  slug: dynatrace-metrics-v2-error-envelope-example
- key_count: 3
  name: Dynatrace Metrics V2 Error Example
  slug: dynatrace-metrics-v2-error-example
- key_count: 4
  name: Dynatrace Metrics V2 Metric Data Example
  slug: dynatrace-metrics-v2-metric-data-example
- key_count: 2
  name: Dynatrace Metrics V2 Metric Default Aggregation Example
  slug: dynatrace-metrics-v2-metric-default-aggregation-example
- key_count: 4
  name: Dynatrace Metrics V2 Metric Descriptor Collection Example
  slug: dynatrace-metrics-v2-metric-descriptor-collection-example
- key_count: 12
  name: Dynatrace Metrics V2 Metric Descriptor Example
  slug: dynatrace-metrics-v2-metric-descriptor-example
- key_count: 4
  name: Dynatrace Metrics V2 Metric Dimension Definition Example
  slug: dynatrace-metrics-v2-metric-dimension-definition-example
- key_count: 2
  name: Dynatrace Metrics V2 Metric Series Collection Example
  slug: dynatrace-metrics-v2-metric-series-collection-example
- key_count: 4
  name: Dynatrace Metrics V2 Metric Series Example
  slug: dynatrace-metrics-v2-metric-series-example
- key_count: 14
  name: Dynatrace Problem Example
  slug: dynatrace-problem-example
- key_count: 2
  name: Dynatrace Problems V2 Alerting Profile Stub Example
  slug: dynatrace-problems-v2-alerting-profile-stub-example
- key_count: 3
  name: Dynatrace Problems V2 Comment Collection Example
  slug: dynatrace-problems-v2-comment-collection-example
- key_count: 5
  name: Dynatrace Problems V2 Comment Example
  slug: dynatrace-problems-v2-comment-example
- key_count: 2
  name: Dynatrace Problems V2 Comment Request Body Example
  slug: dynatrace-problems-v2-comment-request-body-example
- key_count: 4
  name: Dynatrace Problems V2 Constraint Violation Example
  slug: dynatrace-problems-v2-constraint-violation-example
- key_count: 3
  name: Dynatrace Problems V2 Entity Stub Example
  slug: dynatrace-problems-v2-entity-stub-example
- key_count: 1
  name: Dynatrace Problems V2 Error Envelope Example
  slug: dynatrace-problems-v2-error-envelope-example
- key_count: 3
  name: Dynatrace Problems V2 Error Example
  slug: dynatrace-problems-v2-error-example
- key_count: 2
  name: Dynatrace Problems V2 Management Zone Example
  slug: dynatrace-problems-v2-management-zone-example
- key_count: 1
  name: Dynatrace Problems V2 Problem Close Request Example
  slug: dynatrace-problems-v2-problem-close-request-example
- key_count: 2
  name: Dynatrace Problems V2 Problem Close Result Example
  slug: dynatrace-problems-v2-problem-close-result-example
- key_count: 4
  name: Dynatrace Problems V2 Problem Collection Example
  slug: dynatrace-problems-v2-problem-collection-example
- key_count: 12
  name: Dynatrace Problems V2 Problem Example
  slug: dynatrace-problems-v2-problem-example
- key_count: 4
  name: Entities Api V2 Constraint Violation Example
  slug: entities-api-v2-constraint-violation-example
- key_count: 4
  name: Entities Api V2 Entity Collection Example
  slug: entities-api-v2-entity-collection-example
- key_count: 10
  name: Entities Api V2 Entity Example
  slug: entities-api-v2-entity-example
- key_count: 2
  name: Entities Api V2 Entity Lookup Request Example
  slug: entities-api-v2-entity-lookup-request-example
- key_count: 4
  name: Entities Api V2 Entity Tag Example
  slug: entities-api-v2-entity-tag-example
- key_count: 3
  name: Entities Api V2 Entity Type Collection Example
  slug: entities-api-v2-entity-type-collection-example
- key_count: 6
  name: Entities Api V2 Entity Type Example
  slug: entities-api-v2-entity-type-example
- key_count: 3
  name: Entities Api V2 Entity Type Property Example
  slug: entities-api-v2-entity-type-property-example
- key_count: 2
  name: Entities Api V2 Entity Type Relationship Example
  slug: entities-api-v2-entity-type-relationship-example
- key_count: 2
  name: Entities Api V2 Management Zone Example
  slug: entities-api-v2-management-zone-example
- key_count: 4
  name: Events Api V2 Constraint Violation Example
  slug: events-api-v2-constraint-violation-example
- key_count: 3
  name: Events Api V2 Entity Stub Example
  slug: events-api-v2-entity-stub-example
- key_count: 4
  name: Events Api V2 Event Collection Example
  slug: events-api-v2-event-collection-example
- key_count: 8
  name: Events Api V2 Event Example
  slug: events-api-v2-event-example
- key_count: 7
  name: Events Api V2 Event Ingest Payload Example
  slug: events-api-v2-event-ingest-payload-example
- key_count: 2
  name: Events Api V2 Event Ingest Result Example
  slug: events-api-v2-event-ingest-result-example
- key_count: 2
  name: Events Api V2 Event Ingest Result Item Example
  slug: events-api-v2-event-ingest-result-item-example
- key_count: 4
  name: Log Monitoring Api V2 Constraint Violation Example
  slug: log-monitoring-api-v2-constraint-violation-example
- key_count: 2
  name: Log Monitoring Api V2 Log Aggregate Group Example
  slug: log-monitoring-api-v2-log-aggregate-group-example
- key_count: 1
  name: Log Monitoring Api V2 Log Aggregate Result Example
  slug: log-monitoring-api-v2-log-aggregate-result-example
- key_count: 2
  name: Log Monitoring Api V2 Log Export Result Example
  slug: log-monitoring-api-v2-log-export-result-example
- key_count: 5
  name: Log Monitoring Api V2 Log Ingest Record Example
  slug: log-monitoring-api-v2-log-ingest-record-example
- key_count: 6
  name: Log Monitoring Api V2 Log Record Example
  slug: log-monitoring-api-v2-log-record-example
- key_count: 2
  name: Log Monitoring Api V2 Log Record Search Result Example
  slug: log-monitoring-api-v2-log-record-search-result-example
- key_count: 4
  name: Metrics Api V2 Constraint Violation Example
  slug: metrics-api-v2-constraint-violation-example
- key_count: 4
  name: Metrics Api V2 Metric Data Example
  slug: metrics-api-v2-metric-data-example
- key_count: 2
  name: Metrics Api V2 Metric Default Aggregation Example
  slug: metrics-api-v2-metric-default-aggregation-example
- key_count: 4
  name: Metrics Api V2 Metric Descriptor Collection Example
  slug: metrics-api-v2-metric-descriptor-collection-example
- key_count: 12
  name: Metrics Api V2 Metric Descriptor Example
  slug: metrics-api-v2-metric-descriptor-example
- key_count: 4
  name: Metrics Api V2 Metric Dimension Definition Example
  slug: metrics-api-v2-metric-dimension-definition-example
- key_count: 2
  name: Metrics Api V2 Metric Series Collection Example
  slug: metrics-api-v2-metric-series-collection-example
- key_count: 4
  name: Metrics Api V2 Metric Series Example
  slug: metrics-api-v2-metric-series-example
- key_count: 2
  name: Problems Api V2 Alerting Profile Stub Example
  slug: problems-api-v2-alerting-profile-stub-example
- key_count: 3
  name: Problems Api V2 Comment Collection Example
  slug: problems-api-v2-comment-collection-example
- key_count: 5
  name: Problems Api V2 Comment Example
  slug: problems-api-v2-comment-example
- key_count: 2
  name: Problems Api V2 Comment Request Body Example
  slug: problems-api-v2-comment-request-body-example
- key_count: 4
  name: Problems Api V2 Constraint Violation Example
  slug: problems-api-v2-constraint-violation-example
- key_count: 3
  name: Problems Api V2 Entity Stub Example
  slug: problems-api-v2-entity-stub-example
- key_count: 2
  name: Problems Api V2 Management Zone Example
  slug: problems-api-v2-management-zone-example
- key_count: 1
  name: Problems Api V2 Problem Close Request Example
  slug: problems-api-v2-problem-close-request-example
- key_count: 2
  name: Problems Api V2 Problem Close Result Example
  slug: problems-api-v2-problem-close-result-example
- key_count: 4
  name: Problems Api V2 Problem Collection Example
  slug: problems-api-v2-problem-collection-example
- key_count: 12
  name: Problems Api V2 Problem Example
  slug: problems-api-v2-problem-example
- key_count: 3
  name: Problems Entity Ref Example
  slug: problems-entity-ref-example
- key_count: 2
  name: Problems Impacted Entity Example
  slug: problems-impacted-entity-example
- key_count: 7
  name: Problems Problem Details Example
  slug: problems-problem-details-example
- key_count: 10
  name: Problems Problem Notification Payload Example
  slug: problems-problem-notification-payload-example
- key_count: 2
  name: Problems Webhook Header Example
  slug: problems-webhook-header-example
- key_count: 8
  name: Problems Webhook Notification Config Example
  slug: problems-webhook-notification-config-example
features:
- description: End-to-end monitoring of applications, infrastructure, and digital experiences with automatic discovery and AI-powered root cause analysis.
  name: Full-Stack Observability
- description: Deterministic AI engine that automatically detects anomalies, identifies root causes, and provides precise answers about performance issues without manual configuration.
  name: Davis AI Engine
- description: Unified data store that combines logs, metrics, traces, events, and business data in a single analytics platform with unlimited retention and DQL query language.
  name: Grail Data Lakehouse
- description: Real-time topology mapping and dependency analysis across distributed systems with automatic baselining and smart alerting.
  name: Software Intelligence
- description: Automated workflows, remediation, and orchestration capabilities that integrate with CI/CD pipelines and IT service management tools.
  name: Cloud Automation
- description: Runtime application security with vulnerability detection, attack protection, and security analytics built into the observability platform.
  name: Application Security
- description: Real user monitoring, session replay, and synthetic monitoring for web and mobile applications to optimize user experience.
  name: Digital Experience Monitoring
- description: Flexible data ingestion framework supporting any data source and format with configurable routing, processing, and enrichment pipelines.
  name: OpenPipeline Data Ingestion
- description: Extensible monitoring platform with 600+ out-of-the-box integrations and a framework for building custom data collection extensions.
  name: Extensions Framework
- description: Automated SLO tracking and evaluation with burn rate alerting and reliability scoring based on real monitoring data.
  name: Service Level Objectives
finops:
- has_sources: true
  method: derived
  name: Dynatrace Finops
  primary_unit: host
  service_category: ''
  slug: dynatrace-finops
  template: false
image: https://www.dynatrace.com/logo.png
integrations:
- description: Native integration with AWS services for monitoring EC2, Lambda, RDS, and other AWS resources with automatic tagging and topology mapping.
  name: AWS CloudWatch
- description: Deep integration with Microsoft Azure for monitoring Azure App Services, AKS, Functions, and other Azure platform services.
  name: Azure Monitor
- description: Integration with GCP services including GKE, Cloud Run, Cloud Functions, and BigQuery for comprehensive cloud monitoring.
  name: Google Cloud Platform
- description: Full-stack Kubernetes monitoring with automatic pod, node, and cluster discovery, resource utilization tracking, and workload health analysis.
  name: Kubernetes
- description: Bidirectional integration with ServiceNow for automated incident creation, enrichment, and resolution based on Dynatrace problem detection.
  name: ServiceNow
- description: Integration with PagerDuty for intelligent alert routing, incident management, and on-call notification based on Dynatrace AI-detected problems.
  name: PagerDuty
- description: Notification integration with Slack channels for real-time alerts on performance issues, deployments, and problem resolution updates.
  name: Slack
- description: Integration with Atlassian Jira for automated issue creation and tracking based on detected performance problems and vulnerabilities.
  name: Jira
- description: Terraform provider for infrastructure-as-code management of Dynatrace monitoring configuration, dashboards, and alerting profiles.
  name: Terraform
- description: Ansible collection for automated deployment and configuration of Dynatrace OneAgent and environment settings across infrastructure.
  name: Ansible
json_schemas:
- name: EnvironmentCollection
  property_count: 3
  slug: account-management-api-environment-collection
- name: Environment
  property_count: 4
  slug: account-management-api-environment
- name: GroupCollection
  property_count: 3
  slug: account-management-api-group-collection
- name: GroupCreateRequest
  property_count: 2
  slug: account-management-api-group-create-request
- name: Group
  property_count: 6
  slug: account-management-api-group
- name: PermissionCollection
  property_count: 1
  slug: account-management-api-permission-collection
- name: Permission
  property_count: 4
  slug: account-management-api-permission
- name: UserCollection
  property_count: 3
  slug: account-management-api-user-collection
- name: UserCreateRequest
  property_count: 4
  slug: account-management-api-user-create-request
- name: User
  property_count: 6
  slug: account-management-api-user
- name: AccountLimitsPage
  property_count: 4
  slug: dynatrace-account-limits-page
- name: EnvironmentCollection
  property_count: 3
  slug: dynatrace-account-management-environment-collection
- name: Environment
  property_count: 4
  slug: dynatrace-account-management-environment
- name: ErrorEnvelope
  property_count: 1
  slug: dynatrace-account-management-error-envelope
- name: Error
  property_count: 2
  slug: dynatrace-account-management-error
- name: GroupCollection
  property_count: 3
  slug: dynatrace-account-management-group-collection
- name: GroupCreateRequest
  property_count: 2
  slug: dynatrace-account-management-group-create-request
- name: Group
  property_count: 6
  slug: dynatrace-account-management-group
- name: PermissionCollection
  property_count: 1
  slug: dynatrace-account-management-permission-collection
- name: Permission
  property_count: 4
  slug: dynatrace-account-management-permission
- name: UserCollection
  property_count: 3
  slug: dynatrace-account-management-user-collection
- name: UserCreateRequest
  property_count: 4
  slug: dynatrace-account-management-user-create-request
- name: User
  property_count: 6
  slug: dynatrace-account-management-user
- name: AppendLevelPolicyBindingForGroupDto
  property_count: 3
  slug: dynatrace-append-level-policy-binding-for-group-dto
- name: AuditsByAccountDto
  property_count: 2
  slug: dynatrace-audits-by-account-dto
- name: ClusterListDto
  property_count: 1
  slug: dynatrace-cluster-list-dto
- name: CreateOrUpdateLevelPolicyRequestDto
  property_count: 4
  slug: dynatrace-create-or-update-level-policy-request-dto
- name: ConstraintViolation
  property_count: 4
  slug: dynatrace-entities-v2-constraint-violation
- name: EntityCollection
  property_count: 4
  slug: dynatrace-entities-v2-entity-collection
- name: EntityLookupRequest
  property_count: 2
  slug: dynatrace-entities-v2-entity-lookup-request
- name: Entity
  property_count: 10
  slug: dynatrace-entities-v2-entity
- name: EntityTag
  property_count: 4
  slug: dynatrace-entities-v2-entity-tag
- name: EntityTypeCollection
  property_count: 3
  slug: dynatrace-entities-v2-entity-type-collection
- name: EntityTypeProperty
  property_count: 3
  slug: dynatrace-entities-v2-entity-type-property
- name: EntityTypeRelationship
  property_count: 2
  slug: dynatrace-entities-v2-entity-type-relationship
- name: EntityType
  property_count: 6
  slug: dynatrace-entities-v2-entity-type
- name: ErrorEnvelope
  property_count: 1
  slug: dynatrace-entities-v2-error-envelope
- name: Error
  property_count: 3
  slug: dynatrace-entities-v2-error
- name: ManagementZone
  property_count: 2
  slug: dynatrace-entities-v2-management-zone
- name: EnvironmentListDto
  property_count: 1
  slug: dynatrace-environment-list-dto
- name: EnvironmentResourceDto
  property_count: 2
  slug: dynatrace-environment-resource-dto
- name: ConstraintViolation
  property_count: 4
  slug: dynatrace-events-v2-constraint-violation
- name: EntityStub
  property_count: 3
  slug: dynatrace-events-v2-entity-stub
- name: ErrorEnvelope
  property_count: 1
  slug: dynatrace-events-v2-error-envelope
- name: Error
  property_count: 3
  slug: dynatrace-events-v2-error
- name: EventCollection
  property_count: 4
  slug: dynatrace-events-v2-event-collection
- name: EventIngestPayload
  property_count: 7
  slug: dynatrace-events-v2-event-ingest-payload
- name: EventIngestResultItem
  property_count: 2
  slug: dynatrace-events-v2-event-ingest-result-item
- name: EventIngestResult
  property_count: 2
  slug: dynatrace-events-v2-event-ingest-result
- name: Event
  property_count: 8
  slug: dynatrace-events-v2-event
- name: ExternalServiceUserWithGroupUuidDto
  property_count: 7
  slug: dynatrace-external-service-user-with-group-uuid-dto
- name: ExternalServiceUsersPageDto
  property_count: 3
  slug: dynatrace-external-service-users-page-dto
- name: FieldValuesRequestDto
  property_count: 1
  slug: dynatrace-field-values-request-dto
- name: Forecast
  property_count: 7
  slug: dynatrace-forecast
- name: GeneratePlatformTokenForm
  property_count: 6
  slug: dynatrace-generate-platform-token-form
- name: GetGroupDto
  property_count: 7
  slug: dynatrace-get-group-dto
- name: GroupListDto
  property_count: 2
  slug: dynatrace-group-list-dto
- name: GroupUserDto
  property_count: 7
  slug: dynatrace-group-user-dto
- name: GroupUserListDto
  property_count: 2
  slug: dynatrace-group-user-list-dto
- name: InsertGroupDto
  property_count: 4
  slug: dynatrace-insert-group-dto
- name: IpConfigDto
  property_count: 3
  slug: dynatrace-ip-config-dto
- name: LevelLimitsDto
  property_count: 3
  slug: dynatrace-level-limits-dto
- name: LevelPolicyDto
  property_count: 6
  slug: dynatrace-level-policy-dto
- name: ConstraintViolation
  property_count: 4
  slug: dynatrace-log-monitoring-v2-constraint-violation
- name: ErrorEnvelope
  property_count: 1
  slug: dynatrace-log-monitoring-v2-error-envelope
- name: Error
  property_count: 3
  slug: dynatrace-log-monitoring-v2-error
- name: LogAggregateGroup
  property_count: 2
  slug: dynatrace-log-monitoring-v2-log-aggregate-group
- name: LogAggregateResult
  property_count: 1
  slug: dynatrace-log-monitoring-v2-log-aggregate-result
- name: LogExportResult
  property_count: 2
  slug: dynatrace-log-monitoring-v2-log-export-result
- name: LogIngestRecord
  property_count: 5
  slug: dynatrace-log-monitoring-v2-log-ingest-record
- name: LogRecord
  property_count: 6
  slug: dynatrace-log-monitoring-v2-log-record
- name: LogRecordSearchResult
  property_count: 2
  slug: dynatrace-log-monitoring-v2-log-record-search-result
- name: Dynatrace Metric Series
  property_count: 2
  slug: dynatrace-metric-series
- name: ConstraintViolation
  property_count: 4
  slug: dynatrace-metrics-v2-constraint-violation
- name: ErrorEnvelope
  property_count: 1
  slug: dynatrace-metrics-v2-error-envelope
- name: Error
  property_count: 3
  slug: dynatrace-metrics-v2-error
- name: MetricData
  property_count: 4
  slug: dynatrace-metrics-v2-metric-data
- name: MetricDefaultAggregation
  property_count: 2
  slug: dynatrace-metrics-v2-metric-default-aggregation
- name: MetricDescriptorCollection
  property_count: 4
  slug: dynatrace-metrics-v2-metric-descriptor-collection
- name: MetricDescriptor
  property_count: 12
  slug: dynatrace-metrics-v2-metric-descriptor
- name: MetricDimensionDefinition
  property_count: 4
  slug: dynatrace-metrics-v2-metric-dimension-definition
- name: MetricSeriesCollection
  property_count: 2
  slug: dynatrace-metrics-v2-metric-series-collection
- name: MetricSeries
  property_count: 4
  slug: dynatrace-metrics-v2-metric-series
- name: NotificationListDto
  property_count: 3
  slug: dynatrace-notification-list-dto
- name: NotificationQueryParamsDto
  property_count: 9
  slug: dynatrace-notification-query-params-dto
- name: NotificationV2ListDto
  property_count: 4
  slug: dynatrace-notification-v2-list-dto
- name: PaginatedEnvironmentBreakdownDto
  property_count: 4
  slug: dynatrace-paginated-environment-breakdown-dto
- name: PaginatedFieldValueDto
  property_count: 2
  slug: dynatrace-paginated-field-value-dto
- name: PermissionDto
  property_count: 2
  slug: dynatrace-permission-dto
- name: PermissionsDto
  property_count: 5
  slug: dynatrace-permissions-dto
- name: PermissionsGroupDto
  property_count: 8
  slug: dynatrace-permissions-group-dto
- name: PlatformTokenExpirationDateDto
  property_count: 1
  slug: dynatrace-platform-token-expiration-date-dto
- name: PlatformTokenPageDto
  property_count: 4
  slug: dynatrace-platform-token-page-dto
- name: PlatformTokenSecret
  property_count: 3
  slug: dynatrace-platform-token-secret
- name: PlatformTokenStatusUpdateDto
  property_count: 1
  slug: dynatrace-platform-token-status-update-dto
- name: PolicyBoundaryDto
  property_count: 3
  slug: dynatrace-policy-boundary-dto
- name: PolicyBoundaryOverview
  property_count: 7
  slug: dynatrace-policy-boundary-overview
- name: Dynatrace Problem
  property_count: 14
  slug: dynatrace-problem
- name: AlertingProfileStub
  property_count: 2
  slug: dynatrace-problems-v2-alerting-profile-stub
- name: CommentCollection
  property_count: 3
  slug: dynatrace-problems-v2-comment-collection
- name: CommentRequestBody
  property_count: 2
  slug: dynatrace-problems-v2-comment-request-body
- name: Comment
  property_count: 5
  slug: dynatrace-problems-v2-comment
- name: ConstraintViolation
  property_count: 4
  slug: dynatrace-problems-v2-constraint-violation
- name: EntityStub
  property_count: 3
  slug: dynatrace-problems-v2-entity-stub
- name: ErrorEnvelope
  property_count: 1
  slug: dynatrace-problems-v2-error-envelope
- name: Error
  property_count: 3
  slug: dynatrace-problems-v2-error
- name: ManagementZone
  property_count: 2
  slug: dynatrace-problems-v2-management-zone
- name: ProblemCloseRequest
  property_count: 1
  slug: dynatrace-problems-v2-problem-close-request
- name: ProblemCloseResult
  property_count: 2
  slug: dynatrace-problems-v2-problem-close-result
- name: ProblemCollection
  property_count: 4
  slug: dynatrace-problems-v2-problem-collection
- name: Problem
  property_count: 12
  slug: dynatrace-problems-v2-problem
- name: PutGroupDto
  property_count: 4
  slug: dynatrace-put-group-dto
- name: RateCardSummaryDto
  property_count: 5
  slug: dynatrace-rate-card-summary-dto
- name: RegionDto
  property_count: 1
  slug: dynatrace-region-dto
- name: RestWifServiceUserMappingForm
  property_count: 4
  slug: dynatrace-rest-wif-service-user-mapping-form
- name: RestWifServiceUserMappingList
  property_count: 4
  slug: dynatrace-rest-wif-service-user-mapping-list
- name: RestWifServiceUserMapping
  property_count: 8
  slug: dynatrace-rest-wif-service-user-mapping
- name: RestWifTrustPolicyForm
  property_count: 5
  slug: dynatrace-rest-wif-trust-policy-form
- name: RestWifTrustPolicyList
  property_count: 4
  slug: dynatrace-rest-wif-trust-policy-list
- name: RestWifTrustPolicy
  property_count: 11
  slug: dynatrace-rest-wif-trust-policy
- name: ServiceUserDto
  property_count: 2
  slug: dynatrace-service-user-dto
- name: SubscriptionDto
  property_count: 12
  slug: dynatrace-subscription-dto
- name: SubscriptionEnvironmentCostListV3Dto
  property_count: 3
  slug: dynatrace-subscription-environment-cost-list-v3-dto
- name: SubscriptionEnvironmentUsageListV3Dto
  property_count: 3
  slug: dynatrace-subscription-environment-usage-list-v3-dto
- name: TimeZoneDto
  property_count: 2
  slug: dynatrace-time-zone-dto
- name: UserEmailDto
  property_count: 1
  slug: dynatrace-user-email-dto
- name: UserListDto
  property_count: 2
  slug: dynatrace-user-list-dto
- name: ConstraintViolation
  property_count: 4
  slug: entities-api-v2-constraint-violation
- name: EntityCollection
  property_count: 4
  slug: entities-api-v2-entity-collection
- name: EntityLookupRequest
  property_count: 2
  slug: entities-api-v2-entity-lookup-request
- name: Entity
  property_count: 10
  slug: entities-api-v2-entity
- name: EntityTag
  property_count: 4
  slug: entities-api-v2-entity-tag
- name: EntityTypeCollection
  property_count: 3
  slug: entities-api-v2-entity-type-collection
- name: EntityTypeProperty
  property_count: 3
  slug: entities-api-v2-entity-type-property
- name: EntityTypeRelationship
  property_count: 2
  slug: entities-api-v2-entity-type-relationship
- name: EntityType
  property_count: 6
  slug: entities-api-v2-entity-type
- name: ManagementZone
  property_count: 2
  slug: entities-api-v2-management-zone
- name: ConstraintViolation
  property_count: 4
  slug: events-api-v2-constraint-violation
- name: EntityStub
  property_count: 3
  slug: events-api-v2-entity-stub
- name: EventCollection
  property_count: 4
  slug: events-api-v2-event-collection
- name: EventIngestPayload
  property_count: 7
  slug: events-api-v2-event-ingest-payload
- name: EventIngestResultItem
  property_count: 2
  slug: events-api-v2-event-ingest-result-item
- name: EventIngestResult
  property_count: 2
  slug: events-api-v2-event-ingest-result
- name: Event
  property_count: 8
  slug: events-api-v2-event
- name: ConstraintViolation
  property_count: 4
  slug: log-monitoring-api-v2-constraint-violation
- name: LogAggregateGroup
  property_count: 2
  slug: log-monitoring-api-v2-log-aggregate-group
- name: LogAggregateResult
  property_count: 1
  slug: log-monitoring-api-v2-log-aggregate-result
- name: LogExportResult
  property_count: 2
  slug: log-monitoring-api-v2-log-export-result
- name: LogIngestRecord
  property_count: 5
  slug: log-monitoring-api-v2-log-ingest-record
- name: LogRecord
  property_count: 6
  slug: log-monitoring-api-v2-log-record
- name: LogRecordSearchResult
  property_count: 2
  slug: log-monitoring-api-v2-log-record-search-result
- name: ConstraintViolation
  property_count: 4
  slug: metrics-api-v2-constraint-violation
- name: MetricData
  property_count: 4
  slug: metrics-api-v2-metric-data
- name: MetricDefaultAggregation
  property_count: 2
  slug: metrics-api-v2-metric-default-aggregation
- name: MetricDescriptorCollection
  property_count: 4
  slug: metrics-api-v2-metric-descriptor-collection
- name: MetricDescriptor
  property_count: 12
  slug: metrics-api-v2-metric-descriptor
- name: MetricDimensionDefinition
  property_count: 4
  slug: metrics-api-v2-metric-dimension-definition
- name: MetricSeriesCollection
  property_count: 2
  slug: metrics-api-v2-metric-series-collection
- name: MetricSeries
  property_count: 4
  slug: metrics-api-v2-metric-series
- name: AlertingProfileStub
  property_count: 2
  slug: problems-api-v2-alerting-profile-stub
- name: CommentCollection
  property_count: 3
  slug: problems-api-v2-comment-collection
- name: CommentRequestBody
  property_count: 2
  slug: problems-api-v2-comment-request-body
- name: Comment
  property_count: 5
  slug: problems-api-v2-comment
- name: ConstraintViolation
  property_count: 4
  slug: problems-api-v2-constraint-violation
- name: EntityStub
  property_count: 3
  slug: problems-api-v2-entity-stub
- name: ManagementZone
  property_count: 2
  slug: problems-api-v2-management-zone
- name: ProblemCloseRequest
  property_count: 1
  slug: problems-api-v2-problem-close-request
- name: ProblemCloseResult
  property_count: 2
  slug: problems-api-v2-problem-close-result
- name: ProblemCollection
  property_count: 4
  slug: problems-api-v2-problem-collection
- name: Problem
  property_count: 12
  slug: problems-api-v2-problem
- name: EntityRef
  property_count: 3
  slug: problems-entity-ref
- name: ImpactedEntity
  property_count: 2
  slug: problems-impacted-entity
- name: ProblemDetails
  property_count: 7
  slug: problems-problem-details
- name: ProblemNotificationPayload
  property_count: 10
  slug: problems-problem-notification-payload
- name: WebhookHeader
  property_count: 2
  slug: problems-webhook-header
- name: WebhookNotificationConfig
  property_count: 8
  slug: problems-webhook-notification-config
json_structures:
- name: Account Management Api Environment Collection Structure
  property_count: 3
  slug: account-management-api-environment-collection-structure
- name: Account Management Api Environment Structure
  property_count: 4
  slug: account-management-api-environment-structure
- name: Account Management Api Group Collection Structure
  property_count: 3
  slug: account-management-api-group-collection-structure
- name: Account Management Api Group Create Request Structure
  property_count: 2
  slug: account-management-api-group-create-request-structure
- name: Account Management Api Group Structure
  property_count: 6
  slug: account-management-api-group-structure
- name: Account Management Api Permission Collection Structure
  property_count: 1
  slug: account-management-api-permission-collection-structure
- name: Account Management Api Permission Structure
  property_count: 4
  slug: account-management-api-permission-structure
- name: Account Management Api User Collection Structure
  property_count: 3
  slug: account-management-api-user-collection-structure
- name: Account Management Api User Create Request Structure
  property_count: 4
  slug: account-management-api-user-create-request-structure
- name: Account Management Api User Structure
  property_count: 6
  slug: account-management-api-user-structure
- name: Dynatrace Account Management Environment Collection Structure
  property_count: 3
  slug: dynatrace-account-management-environment-collection-structure
- name: Dynatrace Account Management Environment Structure
  property_count: 4
  slug: dynatrace-account-management-environment-structure
- name: Dynatrace Account Management Error Envelope Structure
  property_count: 1
  slug: dynatrace-account-management-error-envelope-structure
- name: Dynatrace Account Management Error Structure
  property_count: 2
  slug: dynatrace-account-management-error-structure
- name: Dynatrace Account Management Group Collection Structure
  property_count: 3
  slug: dynatrace-account-management-group-collection-structure
- name: Dynatrace Account Management Group Create Request Structure
  property_count: 2
  slug: dynatrace-account-management-group-create-request-structure
- name: Dynatrace Account Management Group Structure
  property_count: 6
  slug: dynatrace-account-management-group-structure
- name: Dynatrace Account Management Permission Collection Structure
  property_count: 1
  slug: dynatrace-account-management-permission-collection-structure
- name: Dynatrace Account Management Permission Structure
  property_count: 4
  slug: dynatrace-account-management-permission-structure
- name: Dynatrace Account Management User Collection Structure
  property_count: 3
  slug: dynatrace-account-management-user-collection-structure
- name: Dynatrace Account Management User Create Request Structure
  property_count: 4
  slug: dynatrace-account-management-user-create-request-structure
- name: Dynatrace Account Management User Structure
  property_count: 6
  slug: dynatrace-account-management-user-structure
- name: Dynatrace Entities V2 Constraint Violation Structure
  property_count: 4
  slug: dynatrace-entities-v2-constraint-violation-structure
- name: Dynatrace Entities V2 Entity Collection Structure
  property_count: 4
  slug: dynatrace-entities-v2-entity-collection-structure
- name: Dynatrace Entities V2 Entity Lookup Request Structure
  property_count: 2
  slug: dynatrace-entities-v2-entity-lookup-request-structure
- name: Dynatrace Entities V2 Entity Structure
  property_count: 10
  slug: dynatrace-entities-v2-entity-structure
- name: Dynatrace Entities V2 Entity Tag Structure
  property_count: 4
  slug: dynatrace-entities-v2-entity-tag-structure
- name: Dynatrace Entities V2 Entity Type Collection Structure
  property_count: 3
  slug: dynatrace-entities-v2-entity-type-collection-structure
- name: Dynatrace Entities V2 Entity Type Property Structure
  property_count: 3
  slug: dynatrace-entities-v2-entity-type-property-structure
- name: Dynatrace Entities V2 Entity Type Relationship Structure
  property_count: 2
  slug: dynatrace-entities-v2-entity-type-relationship-structure
- name: Dynatrace Entities V2 Entity Type Structure
  property_count: 6
  slug: dynatrace-entities-v2-entity-type-structure
- name: Dynatrace Entities V2 Error Envelope Structure
  property_count: 1
  slug: dynatrace-entities-v2-error-envelope-structure
- name: Dynatrace Entities V2 Error Structure
  property_count: 3
  slug: dynatrace-entities-v2-error-structure
- name: Dynatrace Entities V2 Management Zone Structure
  property_count: 2
  slug: dynatrace-entities-v2-management-zone-structure
- name: Dynatrace Events V2 Constraint Violation Structure
  property_count: 4
  slug: dynatrace-events-v2-constraint-violation-structure
- name: Dynatrace Events V2 Entity Stub Structure
  property_count: 3
  slug: dynatrace-events-v2-entity-stub-structure
- name: Dynatrace Events V2 Error Envelope Structure
  property_count: 1
  slug: dynatrace-events-v2-error-envelope-structure
- name: Dynatrace Events V2 Error Structure
  property_count: 3
  slug: dynatrace-events-v2-error-structure
- name: Dynatrace Events V2 Event Collection Structure
  property_count: 4
  slug: dynatrace-events-v2-event-collection-structure
- name: Dynatrace Events V2 Event Ingest Payload Structure
  property_count: 7
  slug: dynatrace-events-v2-event-ingest-payload-structure
- name: Dynatrace Events V2 Event Ingest Result Item Structure
  property_count: 2
  slug: dynatrace-events-v2-event-ingest-result-item-structure
- name: Dynatrace Events V2 Event Ingest Result Structure
  property_count: 2
  slug: dynatrace-events-v2-event-ingest-result-structure
- name: Dynatrace Events V2 Event Structure
  property_count: 8
  slug: dynatrace-events-v2-event-structure
- name: Dynatrace Log Monitoring V2 Constraint Violation Structure
  property_count: 4
  slug: dynatrace-log-monitoring-v2-constraint-violation-structure
- name: Dynatrace Log Monitoring V2 Error Envelope Structure
  property_count: 1
  slug: dynatrace-log-monitoring-v2-error-envelope-structure
- name: Dynatrace Log Monitoring V2 Error Structure
  property_count: 3
  slug: dynatrace-log-monitoring-v2-error-structure
- name: Dynatrace Log Monitoring V2 Log Aggregate Group Structure
  property_count: 2
  slug: dynatrace-log-monitoring-v2-log-aggregate-group-structure
- name: Dynatrace Log Monitoring V2 Log Aggregate Result Structure
  property_count: 1
  slug: dynatrace-log-monitoring-v2-log-aggregate-result-structure
- name: Dynatrace Log Monitoring V2 Log Export Result Structure
  property_count: 2
  slug: dynatrace-log-monitoring-v2-log-export-result-structure
- name: Dynatrace Log Monitoring V2 Log Ingest Record Structure
  property_count: 5
  slug: dynatrace-log-monitoring-v2-log-ingest-record-structure
- name: Dynatrace Log Monitoring V2 Log Record Search Result Structure
  property_count: 2
  slug: dynatrace-log-monitoring-v2-log-record-search-result-structure
- name: Dynatrace Log Monitoring V2 Log Record Structure
  property_count: 6
  slug: dynatrace-log-monitoring-v2-log-record-structure
- name: Dynatrace Metric Series Structure
  property_count: 2
  slug: dynatrace-metric-series-structure
- name: Dynatrace Metrics V2 Constraint Violation Structure
  property_count: 4
  slug: dynatrace-metrics-v2-constraint-violation-structure
- name: Dynatrace Metrics V2 Error Envelope Structure
  property_count: 1
  slug: dynatrace-metrics-v2-error-envelope-structure
- name: Dynatrace Metrics V2 Error Structure
  property_count: 3
  slug: dynatrace-metrics-v2-error-structure
- name: Dynatrace Metrics V2 Metric Data Structure
  property_count: 4
  slug: dynatrace-metrics-v2-metric-data-structure
- name: Dynatrace Metrics V2 Metric Default Aggregation Structure
  property_count: 2
  slug: dynatrace-metrics-v2-metric-default-aggregation-structure
- name: Dynatrace Metrics V2 Metric Descriptor Collection Structure
  property_count: 4
  slug: dynatrace-metrics-v2-metric-descriptor-collection-structure
- name: Dynatrace Metrics V2 Metric Descriptor Structure
  property_count: 12
  slug: dynatrace-metrics-v2-metric-descriptor-structure
- name: Dynatrace Metrics V2 Metric Dimension Definition Structure
  property_count: 4
  slug: dynatrace-metrics-v2-metric-dimension-definition-structure
- name: Dynatrace Metrics V2 Metric Series Collection Structure
  property_count: 2
  slug: dynatrace-metrics-v2-metric-series-collection-structure
- name: Dynatrace Metrics V2 Metric Series Structure
  property_count: 4
  slug: dynatrace-metrics-v2-metric-series-structure
- name: Dynatrace Problem Structure
  property_count: 14
  slug: dynatrace-problem-structure
- name: Dynatrace Problems V2 Alerting Profile Stub Structure
  property_count: 2
  slug: dynatrace-problems-v2-alerting-profile-stub-structure
- name: Dynatrace Problems V2 Comment Collection Structure
  property_count: 3
  slug: dynatrace-problems-v2-comment-collection-structure
- name: Dynatrace Problems V2 Comment Request Body Structure
  property_count: 2
  slug: dynatrace-problems-v2-comment-request-body-structure
- name: Dynatrace Problems V2 Comment Structure
  property_count: 5
  slug: dynatrace-problems-v2-comment-structure
- name: Dynatrace Problems V2 Constraint Violation Structure
  property_count: 4
  slug: dynatrace-problems-v2-constraint-violation-structure
- name: Dynatrace Problems V2 Entity Stub Structure
  property_count: 3
  slug: dynatrace-problems-v2-entity-stub-structure
- name: Dynatrace Problems V2 Error Envelope Structure
  property_count: 1
  slug: dynatrace-problems-v2-error-envelope-structure
- name: Dynatrace Problems V2 Error Structure
  property_count: 3
  slug: dynatrace-problems-v2-error-structure
- name: Dynatrace Problems V2 Management Zone Structure
  property_count: 2
  slug: dynatrace-problems-v2-management-zone-structure
- name: Dynatrace Problems V2 Problem Close Request Structure
  property_count: 1
  slug: dynatrace-problems-v2-problem-close-request-structure
- name: Dynatrace Problems V2 Problem Close Result Structure
  property_count: 2
  slug: dynatrace-problems-v2-problem-close-result-structure
- name: Dynatrace Problems V2 Problem Collection Structure
  property_count: 4
  slug: dynatrace-problems-v2-problem-collection-structure
- name: Dynatrace Problems V2 Problem Structure
  property_count: 12
  slug: dynatrace-problems-v2-problem-structure
- name: Entities Api V2 Constraint Violation Structure
  property_count: 4
  slug: entities-api-v2-constraint-violation-structure
- name: Entities Api V2 Entity Collection Structure
  property_count: 4
  slug: entities-api-v2-entity-collection-structure
- name: Entities Api V2 Entity Lookup Request Structure
  property_count: 2
  slug: entities-api-v2-entity-lookup-request-structure
- name: Entities Api V2 Entity Structure
  property_count: 10
  slug: entities-api-v2-entity-structure
- name: Entities Api V2 Entity Tag Structure
  property_count: 4
  slug: entities-api-v2-entity-tag-structure
- name: Entities Api V2 Entity Type Collection Structure
  property_count: 3
  slug: entities-api-v2-entity-type-collection-structure
- name: Entities Api V2 Entity Type Property Structure
  property_count: 3
  slug: entities-api-v2-entity-type-property-structure
- name: Entities Api V2 Entity Type Relationship Structure
  property_count: 2
  slug: entities-api-v2-entity-type-relationship-structure
- name: Entities Api V2 Entity Type Structure
  property_count: 6
  slug: entities-api-v2-entity-type-structure
- name: Entities Api V2 Management Zone Structure
  property_count: 2
  slug: entities-api-v2-management-zone-structure
- name: Events Api V2 Constraint Violation Structure
  property_count: 4
  slug: events-api-v2-constraint-violation-structure
- name: Events Api V2 Entity Stub Structure
  property_count: 3
  slug: events-api-v2-entity-stub-structure
- name: Events Api V2 Event Collection Structure
  property_count: 4
  slug: events-api-v2-event-collection-structure
- name: Events Api V2 Event Ingest Payload Structure
  property_count: 7
  slug: events-api-v2-event-ingest-payload-structure
- name: Events Api V2 Event Ingest Result Item Structure
  property_count: 2
  slug: events-api-v2-event-ingest-result-item-structure
- name: Events Api V2 Event Ingest Result Structure
  property_count: 2
  slug: events-api-v2-event-ingest-result-structure
- name: Events Api V2 Event Structure
  property_count: 8
  slug: events-api-v2-event-structure
- name: Log Monitoring Api V2 Constraint Violation Structure
  property_count: 4
  slug: log-monitoring-api-v2-constraint-violation-structure
- name: Log Monitoring Api V2 Log Aggregate Group Structure
  property_count: 2
  slug: log-monitoring-api-v2-log-aggregate-group-structure
- name: Log Monitoring Api V2 Log Aggregate Result Structure
  property_count: 1
  slug: log-monitoring-api-v2-log-aggregate-result-structure
- name: Log Monitoring Api V2 Log Export Result Structure
  property_count: 2
  slug: log-monitoring-api-v2-log-export-result-structure
- name: Log Monitoring Api V2 Log Ingest Record Structure
  property_count: 5
  slug: log-monitoring-api-v2-log-ingest-record-structure
- name: Log Monitoring Api V2 Log Record Search Result Structure
  property_count: 2
  slug: log-monitoring-api-v2-log-record-search-result-structure
- name: Log Monitoring Api V2 Log Record Structure
  property_count: 6
  slug: log-monitoring-api-v2-log-record-structure
- name: Metrics Api V2 Constraint Violation Structure
  property_count: 4
  slug: metrics-api-v2-constraint-violation-structure
- name: Metrics Api V2 Metric Data Structure
  property_count: 4
  slug: metrics-api-v2-metric-data-structure
- name: Metrics Api V2 Metric Default Aggregation Structure
  property_count: 2
  slug: metrics-api-v2-metric-default-aggregation-structure
- name: Metrics Api V2 Metric Descriptor Collection Structure
  property_count: 4
  slug: metrics-api-v2-metric-descriptor-collection-structure
- name: Metrics Api V2 Metric Descriptor Structure
  property_count: 12
  slug: metrics-api-v2-metric-descriptor-structure
- name: Metrics Api V2 Metric Dimension Definition Structure
  property_count: 4
  slug: metrics-api-v2-metric-dimension-definition-structure
- name: Metrics Api V2 Metric Series Collection Structure
  property_count: 2
  slug: metrics-api-v2-metric-series-collection-structure
- name: Metrics Api V2 Metric Series Structure
  property_count: 4
  slug: metrics-api-v2-metric-series-structure
- name: Problems Api V2 Alerting Profile Stub Structure
  property_count: 2
  slug: problems-api-v2-alerting-profile-stub-structure
- name: Problems Api V2 Comment Collection Structure
  property_count: 3
  slug: problems-api-v2-comment-collection-structure
- name: Problems Api V2 Comment Request Body Structure
  property_count: 2
  slug: problems-api-v2-comment-request-body-structure
- name: Problems Api V2 Comment Structure
  property_count: 5
  slug: problems-api-v2-comment-structure
- name: Problems Api V2 Constraint Violation Structure
  property_count: 4
  slug: problems-api-v2-constraint-violation-structure
- name: Problems Api V2 Entity Stub Structure
  property_count: 3
  slug: problems-api-v2-entity-stub-structure
- name: Problems Api V2 Management Zone Structure
  property_count: 2
  slug: problems-api-v2-management-zone-structure
- name: Problems Api V2 Problem Close Request Structure
  property_count: 1
  slug: problems-api-v2-problem-close-request-structure
- name: Problems Api V2 Problem Close Result Structure
  property_count: 2
  slug: problems-api-v2-problem-close-result-structure
- name: Problems Api V2 Problem Collection Structure
  property_count: 4
  slug: problems-api-v2-problem-collection-structure
- name: Problems Api V2 Problem Structure
  property_count: 12
  slug: problems-api-v2-problem-structure
- name: Problems Entity Ref Structure
  property_count: 3
  slug: problems-entity-ref-structure
- name: Problems Impacted Entity Structure
  property_count: 2
  slug: problems-impacted-entity-structure
- name: Problems Problem Details Structure
  property_count: 7
  slug: problems-problem-details-structure
- name: Problems Problem Notification Payload Structure
  property_count: 10
  slug: problems-problem-notification-payload-structure
- name: Problems Webhook Header Structure
  property_count: 2
  slug: problems-webhook-header-structure
- name: Problems Webhook Notification Config Structure
  property_count: 8
  slug: problems-webhook-notification-config-structure
jsonld:
- class_count: 10
  name: Dynatrace Account Management Api Context
  property_count: 23
  slug: dynatrace-account-management-api-context
- class_count: 0
  name: Dynatrace Account Management Context
  property_count: 12
  slug: dynatrace-account-management-context
- class_count: 7
  name: Dynatrace Context
  property_count: 28
  slug: dynatrace-context
- class_count: 1
  name: Dynatrace Dynatrace Metric Series Context
  property_count: 2
  slug: dynatrace-dynatrace-metric-series-context
- class_count: 1
  name: Dynatrace Dynatrace Problem Context
  property_count: 14
  slug: dynatrace-dynatrace-problem-context
- class_count: 10
  name: Dynatrace Entities Api V2 Context
  property_count: 27
  slug: dynatrace-entities-api-v2-context
- class_count: 0
  name: Dynatrace Entities V2 Context
  property_count: 12
  slug: dynatrace-entities-v2-context
- class_count: 7
  name: Dynatrace Events Api V2 Context
  property_count: 22
  slug: dynatrace-events-api-v2-context
- class_count: 0
  name: Dynatrace Events V2 Context
  property_count: 9
  slug: dynatrace-events-v2-context
- class_count: 7
  name: Dynatrace Log Monitoring Api V2 Context
  property_count: 14
  slug: dynatrace-log-monitoring-api-v2-context
- class_count: 0
  name: Dynatrace Log Monitoring V2 Context
  property_count: 9
  slug: dynatrace-log-monitoring-v2-context
- class_count: 8
  name: Dynatrace Metrics Api V2 Context
  property_count: 30
  slug: dynatrace-metrics-api-v2-context
- class_count: 0
  name: Dynatrace Metrics V2 Context
  property_count: 10
  slug: dynatrace-metrics-v2-context
- class_count: 11
  name: Dynatrace Problems Api V2 Context
  property_count: 30
  slug: dynatrace-problems-api-v2-context
- class_count: 1
  name: Dynatrace Problems Entity Ref Context
  property_count: 3
  slug: dynatrace-problems-entity-ref-context
- class_count: 1
  name: Dynatrace Problems Impacted Entity Context
  property_count: 2
  slug: dynatrace-problems-impacted-entity-context
- class_count: 1
  name: Dynatrace Problems Problem Details Context
  property_count: 7
  slug: dynatrace-problems-problem-details-context
- class_count: 1
  name: Dynatrace Problems Problem Notification Payload Context
  property_count: 10
  slug: dynatrace-problems-problem-notification-payload-context
- class_count: 0
  name: Dynatrace Problems V2 Context
  property_count: 13
  slug: dynatrace-problems-v2-context
- class_count: 1
  name: Dynatrace Problems Webhook Header Context
  property_count: 2
  slug: dynatrace-problems-webhook-header-context
- class_count: 1
  name: Dynatrace Problems Webhook Notification Config Context
  property_count: 8
  slug: dynatrace-problems-webhook-notification-config-context
layout: provider
mcp_servers:
- description: Dynatrace ships an officially supported REMOTE Model Context Protocol server named `dynatrace-mcp`, hosted inside each customer's own Dynatrace SaaS environment and reached over Streamable HTTP at a p
  name: Dynatrace MCP Server
  slug: dynatrace-mcp-server
modified: '2026-08-29'
name: Dynatrace
nav: Providers
network: true
overview: 'Dynatrace publishes 48 API contracts indexed on the [APIs.io](https://apis.io/) network, including Entities API, Environments API, Events API, and 45 more. Tagged areas include AI Operations, Analytics, APM, Application Performance Monitoring, and Application Security.


  The Dynatrace catalog on APIs.io includes 1 event-driven AsyncAPI specification, 21 JSON-LD contexts, and 4 Spectral governance rulesets.


  Dynatrace''s developer surface includes sandbox, authentication, developer portal, documentation, getting-started guide, API reference, changelog, and 130 more developer resources.'
plans:
- name: Dynatrace Plans Pricing
  plan_count: 19
  slug: dynatrace-plans-pricing
- name: Dynatrace Price Estimates
  plan_count: 0
  slug: dynatrace-price-estimates
random_paper: 19
rate_limits:
- limit_count: 8
  name: Dynatrace Rate Limits
  slug: dynatrace-rate-limits
rules:
- authorship: generated
  effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Dynatrace — asyncapi rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: dynatrace-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Dynatrace — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: dynatrace-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Dynatrace API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: dynatrace-rules
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: Dynatrace API Rules
  rule_count: 30
  severity_counts:
    error: 19
    hint: 0
    info: 3
    warn: 8
  slug: dynatrace-spectral-rules
scopes:
- name: Dynatrace Scopes
  scope_count: 3
  slug: dynatrace-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: exemplar
  composite: 84.1
  coverage:
    artifact_dirs: 43
    catalog_earned: 87.0
    catalog_earned_first_party: 24.0
    catalog_gap: 28.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 67.2
    developer_ergonomics: 80.4
    discoverability: 74.2
    operational_transparency: 94.7
  previous_composite: 86.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 50.0
      total: 28
    mcp: first-party
    skills: first-party
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
screenshot: https://apis.io/screenshots/dynatrace/dynatrace-2026-06-20T180345.png
security:
- kind: authentication
  name: Dynatrace Authentication
  slug: dynatrace-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Dynatrace Domain Security
  slug: dynatrace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dynatrace Vulnerability Disclosure
  slug: dynatrace-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dynatrace Trust Center
  slug: dynatrace-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
skill_count: 17
skills:
- name: dt-alerting
  slug: dt-alerting
- name: dt-app-dashboards
  slug: dt-app-dashboards
- name: dt-app-notebooks
  slug: dt-app-notebooks
- name: dt-dql-essentials
  slug: dt-dql-essentials
- name: dt-js-runtime
  slug: dt-js-runtime
- name: dt-migration
  slug: dt-migration
- name: dt-obs-aws
  slug: dt-obs-aws
- name: dt-obs-azure
  slug: dt-obs-azure
- name: dt-obs-frontends
  slug: dt-obs-frontends
- name: dt-obs-gcp
  slug: dt-obs-gcp
- name: dt-obs-hosts
  slug: dt-obs-hosts
- name: dt-obs-kubernetes
  slug: dt-obs-kubernetes
- name: dt-obs-logs
  slug: dt-obs-logs
- name: dt-obs-predictive-analytics
  slug: dt-obs-predictive-analytics
- name: dt-obs-problems
  slug: dt-obs-problems
- name: dt-obs-services
  slug: dt-obs-services
- name: dt-obs-tracing
  slug: dt-obs-tracing
slug: dynatrace
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
- Monitoring
use_cases:
- description: Monitor hosts, containers, and cloud infrastructure with automatic discovery, health metrics, and capacity planning across hybrid and multi-cloud environments.
  name: Infrastructure Monitoring
- description: Trace distributed transactions end-to-end, identify bottlenecks, and optimize application performance with code-level visibility and AI-powered insights.
  name: Application Performance Management
- description: Ingest, search, and analyze log data at scale using the Grail data lakehouse with DQL queries for troubleshooting and compliance.
  name: Log Analytics and Management
- description: Track application health and performance during cloud migration with automatic dependency mapping and impact analysis.
  name: Cloud Migration Monitoring
- description: Integrate observability into CI/CD pipelines with automated quality gates, deployment validation, and incident response workflows.
  name: DevOps and SRE Automation
- description: Correlate business events with technical performance data to measure revenue impact and optimize digital business outcomes.
  name: Business Analytics
- description: Detect runtime vulnerabilities, monitor attack attempts, and assess application security posture with integrated security analytics.
  name: Security Posture Management
- description: Proactively monitor application availability and performance with browser-based and HTTP synthetic tests from global locations.
  name: Synthetic Testing
website: https://www.dynatrace.com/
---
