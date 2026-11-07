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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 92
  human_in_the_loop: 1
  name: Gitlab Agentic Access
  operation_count: 167
  slug: gitlab-agentic-access
  summary_line: 167 operations · 92 acting · 1 human-in-the-loop
api_count: 14
apis:
- baseURL_template: https://{hostname}
  baseurl_source: spec_template
  description: GitLab Orbit knowledge graph gRPC service (package orbit.v1, OrbitService) that serves the Orbit dashboard, MCP agents and the glab CLI; published in GitLab's own gitlabhq/orbit-knowledge-graph reposi
  name: GitLab Orbit gRPC API
  slug: gitlab-orbit-api
- description: 'GraphQL is a query language for APIs. You can use it to request the exact data you need, and therefore limit the number of requests you need. GraphQL data is arranged in types, so your client can use '
  name: GitLab GraphQL API
  slug: gitlab-graphql-api
- baseURL: https://gitlab.com
  baseurl_source: declared
  description: The Applications API from GitLab — 2 operation(s) for applications.
  name: GitLab Applications API
  phrasing_intents:
  - id: postApiV4Applications
    intent: Register a new OAuth application
    question: How do I register an instance-wide OAuth app so I get a client ID and secret?
  - id: getApiV4Applications
    intent: List registered OAuth applications
    question: Which OAuth applications are registered on my GitLab instance?
  - id: deleteApiV4ApplicationsId
    intent: Delete an OAuth application
    question: How do I remove an OAuth application registered on the instance?
  phrasing_ops: 3
  slug: gitlab-applications-api
- baseURL: https://gitlab.com
  baseurl_source: declared
  description: Endpoints for initiating OAuth authorization flows.
  name: GitLab Authorization API
  phrasing_intents:
  - id: authorizeOAuth
    intent: Start the OAuth authorization code flow
    question: How do I send a user to GitLab to approve my app's access?
  - id: authorizeDevice
    intent: Start a device authorization grant
    question: How do I sign in a CLI or TV app that can't open a browser?
  phrasing_ops: 2
  slug: gitlab-authorization-api
- baseURL: https://gitlab.com
  baseurl_source: declared
  description: The Broadcast Messages API from GitLab — 2 operation(s) for broadcast messages.
  name: GitLab Broadcast Messages API
  phrasing_intents:
  - id: getApiV4BroadcastMessages
    intent: List all broadcast messages
    question: What announcement banners are configured on the instance?
  - id: postApiV4BroadcastMessages
    intent: Create a broadcast message
    question: How do I post a maintenance banner to all users of my GitLab instance?
  - id: getApiV4BroadcastMessagesId
    intent: Get a broadcast message
    question: How do I view one broadcast banner and its schedule?
  - id: putApiV4BroadcastMessagesId
    intent: Update a broadcast message
    question: How do I change the wording or end date of an existing announcement banner?
  - id: deleteApiV4BroadcastMessagesId
    intent: Delete a broadcast message
    question: How do I take down an announcement banner from my GitLab instance?
  phrasing_ops: 5
  slug: gitlab-broadcast-messages-api
- baseURL: https://gitlab.com
  baseurl_source: declared
  description: The Groups API from GitLab — 6 operation(s) for groups.
  name: GitLab Groups API
  slug: gitlab-groups-api
- baseURL: https://gitlab.com
  baseurl_source: declared
  description: The Metadata API from GitLab — 1 operation(s) for metadata.
  name: GitLab Metadata API
  phrasing_intents:
  - id: getApiV4Metadata
    intent: Get metadata about the GitLab instance
    question: What version and revision is this GitLab instance running?
  phrasing_ops: 1
  slug: gitlab-metadata-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Manage webhooks for a specific project.
  name: GitLab Project Webhooks API
  phrasing_intents:
  - id: listProjectWebhooks
    intent: List a project's webhooks
    question: Which webhooks are configured on my GitLab project?
  - id: addProjectWebhook
    intent: Add a webhook to a project
    question: How do I send a notification to my server whenever someone pushes to a project?
  - id: getProjectWebhook
    intent: Get a project webhook's configuration
    question: How do I check which events a specific webhook is subscribed to?
  - id: updateProjectWebhook
    intent: Update a project webhook
    question: How do I change the delivery URL of an existing project webhook?
  - id: deleteProjectWebhook
    intent: Delete a project webhook
    question: How do I stop a project webhook from receiving deliveries altogether?
  phrasing_ops: 5
  slug: gitlab-project-webhooks-api
- baseURL: https://gitlab.com
  baseurl_source: declared
  description: The Projects API from GitLab — 17 operation(s) for projects.
  name: GitLab Projects API
  slug: gitlab-projects-api
- baseURL: https://gitlab.com
  baseurl_source: declared
  description: Endpoints for exchanging, refreshing, and revoking OAuth tokens.
  name: GitLab Tokens API
  phrasing_intents:
  - id: exchangeToken
    intent: Exchange a code or refresh token for an access token
    question: How do I turn an OAuth authorization code into an access token?
  - id: revokeToken
    intent: Revoke an OAuth access or refresh token
    question: How do I invalidate an OAuth token when a user logs out?
  - id: getTokenInfo
    intent: Inspect the current OAuth token
    question: What scopes does my current OAuth token have?
  phrasing_ops: 3
  slug: gitlab-tokens-api
- baseURL: https://gitlab.com
  baseurl_source: declared
  description: Endpoints for retrieving authenticated user information via OAuth.
  name: GitLab User Info API
  phrasing_intents:
  - id: getUserInfo
    intent: Get the signed-in user's OpenID profile
    question: How do I get the name and email of the user who signed in with OpenID Connect?
  phrasing_ops: 1
  slug: gitlab-user-info-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Manage custom headers and URL variables for webhooks.
  name: GitLab Webhook Configuration API
  phrasing_intents:
  - id: setWebhookCustomHeader
    intent: Set a custom header on a webhook
    question: How do I add an authorization header to every delivery from a project webhook?
  - id: deleteWebhookCustomHeader
    intent: Remove a custom header from a webhook
    question: How do I stop a webhook from sending one of its custom headers?
  - id: setWebhookUrlVariable
    intent: Set a URL variable on a webhook
    question: How do I keep a secret out of a webhook URL by using a URL variable?
  - id: deleteWebhookUrlVariable
    intent: Remove a URL variable from a webhook
    question: How do I delete a URL variable I no longer substitute into a webhook URL?
  phrasing_ops: 4
  slug: gitlab-webhook-configuration-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Access webhook delivery history and resend events.
  name: GitLab Webhook Events API
  phrasing_intents:
  - id: listProjectWebhookEvents
    intent: List recent deliveries of a project webhook
    question: How do I see what a webhook sent and what my server answered over the last week?
  - id: resendWebhookEvent
    intent: Resend a past webhook delivery
    question: How do I retry a webhook delivery that failed?
  - id: testProjectWebhook
    intent: Send a test payload to a webhook
    question: How do I check my webhook endpoint is reachable before real events arrive?
  phrasing_ops: 3
  slug: gitlab-webhook-events-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with access requests for groups and projects.
  name: GitLab Access requests API
  slug: gitlab-access-requests-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to interact with access tokens including: - [Personal access tokens](https://docs.gitlab.com/user/profile/personal_access_tokens/). - [Group access tokens](https://docs.gitlab.com/user/gr'
  name: GitLab Access tokens API
  slug: gitlab-access-tokens-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to administer the ActiveContext indexing infrastructure, including its connections, collection options, the namespaces enabled for code indexing, and the dead queue. These endpoints requi
  name: GitLab Active context API
  slug: gitlab-active-context-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve, create, and update the [subscription add-on](https://docs.gitlab.com/subscriptions/subscription-add-ons/) purchases of a namespace.
  name: GitLab Add on purchases API
  slug: gitlab-add-on-purchases-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to control what percentage of namespaces are indexed for [advanced search](https://docs.gitlab.com/integration/advanced_search/elasticsearch/), rolling indexing forward or back.
  name: GitLab Advanced search rollout API
  slug: gitlab-advanced-search-rollout-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve the [GitLab agents for Kubernetes](https://docs.gitlab.com/user/clusters/agent/) that a CI/CD job is authorized to access.
  name: GitLab Agents API
  slug: gitlab-agents-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to ai agent audit events.
  name: GitLab Ai agent audit events API
  slug: gitlab-ai-agent-audit-events-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to register an external agent identity for a project, so that agent sessions can be attributed to a user and a machine. Registration returns the existing record if one already exists, or '
  name: GitLab Ai agent identities API
  slug: gitlab-ai-agent-identities-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to ai agent sessions.
  name: GitLab Ai agent sessions API
  slug: gitlab-ai-agent-sessions-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with metric images for [alerts](https://docs.gitlab.com/operations/incident_management/alerts/). Additional endpoints are available with the [GraphQL API](https://docs.gitlab.
  name: GitLab Alert management API
  slug: gitlab-alert-management-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve analytics about a group's activity, a project's deployment frequency, and product analytics data. For more information about the group metrics, see [group activity analytics](
  name: GitLab Analytics API
  slug: gitlab-analytics-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage the [merge request approval rules](https://docs.gitlab.com/user/project/merge_requests/approvals/rules/) defined for a project or a group, where the rules of a group apply to th
  name: GitLab Approval rules API
  slug: gitlab-approval-rules-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve and download [provenance attestations](https://docs.gitlab.com/ci/pipeline_security/slsa/level_3/provenance_v1/) for a project. > [!note] > The availability of these endpoints
  name: GitLab Attestations API
  slug: gitlab-attestations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to list and retrieve the [audit events](https://docs.gitlab.com/user/compliance/audit_events/) recorded for an instance or a group.
  name: GitLab Audit events API
  slug: gitlab-audit-events-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to authn.
  name: GitLab Authn API
  slug: gitlab-authn-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve and upload avatars for [users](https://docs.gitlab.com/user/profile/), [groups](https://docs.gitlab.com/user/group/), and [projects](https://docs.gitlab.com/user/project/).
  name: GitLab Avatars API
  slug: gitlab-avatars-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [emoji reactions](https://docs.gitlab.com/user/emoji_reactions/). GitLab objects that accept emoji reactions are called awardables. You can react with emoji on the following res
  name: GitLab Award emoji API
  slug: gitlab-award-emoji-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to manage badges for [projects](https://docs.gitlab.com/user/project/badges/) and [groups](https://docs.gitlab.com/user/project/badges/#group-badges). ## Placeholders Badges support place'
  name: GitLab Badges API
  slug: gitlab-badges-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to list, retrieve, pause, and resume the [batched background migrations](https://docs.gitlab.com/update/background_migrations/) running on an instance. These endpoints require administrat
  name: GitLab Batched background migrations API
  slug: gitlab-batched-background-migrations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to list, retrieve, restart, and stop the batched background operations running on an instance. These endpoints require administrator access to the instance.
  name: GitLab Batched background operations API
  slug: gitlab-batched-background-operations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [issue boards](https://docs.gitlab.com/user/project/issue_board/) and their lists, for both projects and [groups](https://docs.gitlab.com/user/project/issue_board/#group-issue-b
  name: GitLab Boards API
  slug: gitlab-boards-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [Git branches](https://docs.gitlab.com/user/project/repository/branches/). To change the branch protections configured for a project, use the [protected branches API](https://do
  name: GitLab Branches API
  slug: gitlab-branches-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to publish a release of a component project to the [CI/CD catalog](https://docs.gitlab.com/ci/components/). This endpoint is intended for CLI tooling and must be authenticated with a [job
  name: GitLab CI catalog API
  slug: gitlab-ci-catalog-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with [CI/CD jobs](https://docs.gitlab.com/ci/jobs/).
  name: GitLab CI jobs API
  slug: gitlab-ci-jobs-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to [validate a GitLab CI/CD configuration](https://docs.gitlab.com/ci/yaml/lint/). These endpoints take JSON-encoded YAML content. To preserve the formatting of your CI/CD configuration, '
  name: GitLab CI lint API
  slug: gitlab-ci-lint-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: '> [!warning] > These endpoints are [deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/515371) and were used > only by the GitLab subscription portal. Use this API to record a purchase of [comp'
  name: GitLab CI minutes API
  slug: gitlab-ci-minutes-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with [resource groups](https://docs.gitlab.com/ci/resource_groups/).
  name: GitLab CI resource groups API
  slug: gitlab-ci-resource-groups-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: '> [!warning] > Registering a runner with a registration token is > [deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/380872) and disabled by default in > GitLab 17.0 and later. Use this API t'
  name: GitLab CI runners API
  slug: gitlab-ci-runners-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to [trigger pipelines](https://docs.gitlab.com/ci/triggers/).
  name: GitLab CI triggers API
  slug: gitlab-ci-triggers-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage CI/CD variables for a [project](https://docs.gitlab.com/ci/variables/#for-a-project), a [group](https://docs.gitlab.com/ci/variables/#for-a-group), or an [instance](https://docs
  name: GitLab CI variables API
  slug: gitlab-ci-variables-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with the [GitLab agent for Kubernetes](https://docs.gitlab.com/user/clusters/agent/).
  name: GitLab Cluster agents API
  slug: gitlab-cluster-agents-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: '> [!warning] > These certificate-based cluster endpoints are [deprecated](https://gitlab.com/groups/gitlab-org/configure/-/work_items/8). Use this API to manage and discover the certificate-based Kube'
  name: GitLab Clusters API
  slug: gitlab-clusters-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve [code review analytics](https://docs.gitlab.com/user/analytics/code_review_analytics/) for a project.
  name: GitLab Code review analytics API
  slug: gitlab-code-review-analytics-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to administer the [Zoekt](https://docs.gitlab.com/integration/zoekt/) nodes that power [exact code search](https://docs.gitlab.com/user/search/exact_code_search/), including which namespa
  name: GitLab Code search API
  slug: gitlab-code-search-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to Code Suggestions.
  name: GitLab Code Suggestions API
  slug: gitlab-code-suggestions-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to list the statuses recorded against a [commit](https://docs.gitlab.com/user/project/repository/commits/), and to add or update the status that an external [CI/CD job](https://docs.gitla
  name: GitLab Commit statuses API
  slug: gitlab-commit-statuses-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [Git commits](https://docs.gitlab.com/user/project/repository/commits/).
  name: GitLab Commits API
  slug: gitlab-commits-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to manage the security policy settings for an instance, and to set the status of compliance controls that are evaluated by an external service. Managing security policy settings requires '
  name: GitLab Compliance policy settings API
  slug: gitlab-compliance-policy-settings-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to manage the [GitLab container registry](https://docs.gitlab.com/user/packages/container_registry/): list the registry repositories in a project or a group, retrieve or delete individual'
  name: GitLab Container registry API
  slug: gitlab-container-registry-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage the custom attributes set on users, groups, and projects. These endpoints require administrator access to the instance.
  name: GitLab Custom attributes API
  slug: gitlab-custom-attributes-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: '> [!note] > These endpoints are an [experiment](https://docs.gitlab.com/policy/development_stages_support/). Use this API to inspect and checksum the records that an instance stores for a given model.'
  name: GitLab Data management API
  slug: gitlab-data-management-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to list the tables in a GitLab database and retrieve the [database dictionary](https://docs.gitlab.com/development/database/database_dictionary/) entry for a single table. Retrieving the '
  name: GitLab Database dictionary API
  slug: gitlab-database-dictionary-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to retrieve a project''s dependencies and to export [dependency lists](https://docs.gitlab.com/user/application_security/dependency_list/) for a project, group, or pipeline. Every call to '
  name: GitLab Dependency management API
  slug: gitlab-dependency-management-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to purge the cache of a group's [dependency proxy](https://docs.gitlab.com/user/packages/dependency_proxy/).
  name: GitLab Dependency proxy API
  slug: gitlab-dependency-proxy-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [deploy keys](https://docs.gitlab.com/user/project/deploy_keys/), [deploy tokens](https://docs.gitlab.com/user/project/deploy_tokens/), and [code deployments](https://docs.gitla
  name: GitLab Deploy resources API
  slug: gitlab-deploy-resources-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [discussions](https://docs.gitlab.com/user/discussions/). This includes [comments, threads](https://docs.gitlab.com/user/discussions/), and system notes about changes to an obje
  name: GitLab Discussions API
  slug: gitlab-discussions-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve [DORA metrics](https://docs.gitlab.com/user/analytics/dora_metrics/) for groups and projects. Additional metrics are available through the [GraphQL API](https://docs.gitlab.co
  name: GitLab DORA metrics API
  slug: gitlab-dora-metrics-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage draft notes. These notes are pending, unpublished comments on merge requests. Draft notes can start a discussion, or continue an existing discussion as a reply. Before publishin
  name: GitLab Draft notes API
  slug: gitlab-draft-notes-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage the [enterprise users](https://docs.gitlab.com/user/enterprise_user/) of a top-level group, including disabling two-factor authentication for them. These endpoints work only for
  name: GitLab Enterprise users API
  slug: gitlab-enterprise-users-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with [GitLab environments](https://docs.gitlab.com/ci/environments/).
  name: GitLab Environments API
  slug: gitlab-environments-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: '> [!warning] > The Epics REST API was [deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/460668) in GitLab 17.0 > and is planned for removal in v5 of the API. From GitLab 17.4 to 18.0, if > [t'
  name: GitLab Epics API
  slug: gitlab-epics-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [error tracking](https://docs.gitlab.com/operations/error_tracking/) settings and client keys for a project. These endpoints require the Maintainer or Owner role.
  name: GitLab Error tracking API
  slug: gitlab-error-tracking-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to review event activity for a user, a project, or an instance. Events cover a wide range of actions, such as joining a project, commenting on an issue, pushing changes to a merge request
  name: GitLab Events API
  slug: gitlab-events-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve the A/B experiments running on an instance. This API is for internal use only, requires you to be a [GitLab team member](https://gitlab.com/groups/gitlab-com/-/group_members),
  name: GitLab Experiments API
  slug: gitlab-experiments-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [external status checks](https://docs.gitlab.com/user/project/merge_requests/status_checks/).
  name: GitLab External status checks API
  slug: gitlab-external-status-checks-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to manage a project''s [feature flags](https://docs.gitlab.com/operations/feature_flags/) and the [user lists](https://docs.gitlab.com/operations/feature_flags/#user-list) that scope them '
  name: GitLab Feature flags API
  slug: gitlab-feature-flags-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage the Flipper-based feature flags used in the development of GitLab itself. These endpoints support only boolean and percentage-of-time gate values, and require administrator auth
  name: GitLab Features API
  slug: gitlab-features-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [repository files](https://docs.gitlab.com/user/project/repository/). You can also [configure rate limits](https://docs.gitlab.com/administration/settings/files_api_rate_limits/
  name: GitLab Files API
  slug: gitlab-files-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with deployment [freeze periods](https://docs.gitlab.com/user/project/releases/#prevent-unintentional-releases-by-setting-a-deploy-freeze).
  name: GitLab Freeze periods API
  slug: gitlab-freeze-periods-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [Geo sites](https://docs.gitlab.com/administration/geo/). All of these endpoints require administrator access. > [!warning] > The Geo Nodes endpoints are [deprecated](https://gi
  name: GitLab Geo API
  slug: gitlab-geo-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to generate responses for [GitLab Duo Chat](https://docs.gitlab.com/user/gitlab_duo_chat/) and other GitLab Duo features. On GitLab.com, these endpoints are for internal use only. On GitL
  name: GitLab GitLab Duo API
  slug: gitlab-gitlab-duo-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to create and manage [flows](https://docs.gitlab.com/user/duo_agent_platform/flows/) in the [GitLab Duo Agent Platform](https://docs.gitlab.com/user/duo_agent_platform/). Flows are combin
  name: GitLab GitLab Duo workflows API
  slug: gitlab-gitlab-duo-workflows-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to [administer](https://docs.gitlab.com/administration/pages/) and [use](https://docs.gitlab.com/user/project/pages/) GitLab Pages, including managing [custom domains](https://docs.gitlab
  name: GitLab GitLab Pages API
  slug: gitlab-gitlab-pages-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to create and update the [subscription](https://docs.gitlab.com/subscriptions/) attached to a namespace.
  name: GitLab GitLab subscriptions API
  slug: gitlab-gitlab-subscriptions-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to execute [GitLab Query Language (GLQL)](https://docs.gitlab.com/user/glql/) queries programmatically. GLQL provides a simplified query language to search and filter [GitLab resources](h
  name: GitLab GLQL API
  slug: gitlab-glql-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage the credentials that members of a top-level group hold, including their personal access tokens, resource access tokens, and SSH keys. You can list these credentials, revoke them
  name: GitLab Group credentials inventory API
  slug: gitlab-group-credentials-inventory-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to [migrate a group structure](https://docs.gitlab.com/user/group/import/) by exporting and importing a file. When you use it with the [project import and export API](https://docs.gitlab.
  name: GitLab Group import and export API
  slug: gitlab-group-import-and-export-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to manage the hooks that GitLab uses to notify external services about events: - [Project webhooks](https://docs.gitlab.com/user/project/integrations/webhooks/) are limited to a single pr'
  name: GitLab Hooks API
  slug: gitlab-hooks-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to migrate groups and projects by using [direct transfer](https://docs.gitlab.com/user/group/import/direct_transfer_migrations/), and to [import repositories from external sources](https:'
  name: GitLab Imports API
  slug: gitlab-imports-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage an instance's [appearance](https://docs.gitlab.com/administration/appearance/) and [application settings](https://docs.gitlab.com/api/settings/#available-settings), and to retri
  name: GitLab Instance API
  slug: gitlab-instance-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [integrations](https://docs.gitlab.com/user/project/integrations/) for a project, or for a group and its subgroups. Managing integrations requires the Maintainer or Owner role f
  name: GitLab Integrations API
  slug: gitlab-integrations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: The Internal API from GitLab — 1 operation(s) for internal.
  name: GitLab Internal API
  slug: gitlab-internal-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to internal operations.
  name: GitLab Internal operations API
  slug: gitlab-internal-operations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage invitations and add users to a [group](https://docs.gitlab.com/user/group/#add-users-to-a-group) or [project](https://docs.gitlab.com/user/project/members/).
  name: GitLab Invitations API
  slug: gitlab-invitations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [issues](https://docs.gitlab.com/user/project/issues/), their [links to related issues](https://docs.gitlab.com/user/project/issues/related_issues/), and issue statistics. You c
  name: GitLab Issues API
  slug: gitlab-issues-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve [iterations](https://docs.gitlab.com/user/group/iterations/) for a group or a project. Projects no longer have their own iterations, but you can use the project endpoint to re
  name: GitLab Iterations API
  slug: gitlab-iterations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to subscribe a namespace to an installation of the [GitLab for Jira Cloud app](https://docs.gitlab.com/integration/jira/connect-app/).
  name: GitLab Jira Connect subscriptions API
  slug: gitlab-jira-connect-subscriptions-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to configure a GitLab for Jira (Forge) installation, by setting the GitLab instance URL it points to and registering the system token it uses to synchronize development information. For m
  name: GitLab Jira forge installation API
  slug: gitlab-jira-forge-installation-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to list, create, and delete the namespace subscriptions of a GitLab for Jira (Forge) installation. For more information, see the [Jira integrations](https://docs.gitlab.com/integration/ji
  name: GitLab Jira forge subscriptions API
  slug: gitlab-jira-forge-subscriptions-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to jira forge user delegation.
  name: GitLab Jira forge user delegation API
  slug: gitlab-jira-forge-user-delegation-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to download, keep, and delete [job artifacts](https://docs.gitlab.com/ci/jobs/job_artifacts/).
  name: GitLab Job artifacts API
  slug: gitlab-job-artifacts-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to run CI/CD jobs on a [runner](https://docs.gitlab.com/ci/runners/): request the next job, update its state, append to its log, and transfer its artifacts. GitLab Runner uses these endpo'
  name: GitLab Jobs API
  slug: gitlab-jobs-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve information about [SSH keys](https://docs.gitlab.com/user/ssh/), manage a user's SSH and [GPG keys](https://docs.gitlab.com/user/project/repository/signed_commits/gpg/), and m
  name: GitLab Keys API
  slug: gitlab-keys-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to list the namespaces enabled for the knowledge graph, and to enable or disable an individual namespace. These endpoints require administrator access to the instance.
  name: GitLab Knowledge graph API
  slug: gitlab-knowledge-graph-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [labels](https://docs.gitlab.com/user/project/labels/) for both projects and groups. For the difference between the two, see [types of labels](https://docs.gitlab.com/user/proje
  name: GitLab Labels API
  slug: gitlab-labels-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to search the LDAP groups available to an instance, and to [manage group memberships with LDAP](https://docs.gitlab.com/user/group/access_and_permissions/#manage-group-memberships-with-ld
  name: GitLab LDAP API
  slug: gitlab-ldap-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to add, retrieve, and delete the license that [activates GitLab Enterprise Edition](https://docs.gitlab.com/administration/license_file/). These endpoints require administrator access to '
  name: GitLab Licenses API
  slug: gitlab-licenses-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to render [Markdown](https://docs.gitlab.com/user/markdown/) content as HTML. All requests to this API must be [authenticated](https://docs.gitlab.com/api/rest/authentication/). > [!note]
  name: GitLab Markdown API
  slug: gitlab-markdown-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to connect Model Context Protocol (MCP) clients to the GitLab MCP server.
  name: GitLab MCP API
  slug: gitlab-mcp-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with member roles for your GitLab.com groups or entire GitLab Self-Managed instance.
  name: GitLab Member roles API
  slug: gitlab-member-roles-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage the [members](https://docs.gitlab.com/user/project/members/) of a group or a project, including inherited memberships, membership approvals, and the billable members of a group.
  name: GitLab Members API
  slug: gitlab-members-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [merge request approvals](https://docs.gitlab.com/user/project/merge_requests/approvals/) and the group and project [approval settings](https://docs.gitlab.com/user/project/merg
  name: GitLab Merge request approvals API
  slug: gitlab-merge-request-approvals-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to manage [merge requests](https://docs.gitlab.com/user/project/merge_requests/) in a project, and to list the merge requests across a group or an entire instance. You can: - Automate any'
  name: GitLab Merge requests API
  slug: gitlab-merge-requests-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve the [merge trains](https://docs.gitlab.com/ci/pipelines/merge_trains/) of a project. These endpoints require the Developer, Maintainer, or Owner role, and support [offset-base
  name: GitLab Merge trains API
  slug: gitlab-merge-trains-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to upload, list, update, and delete the metric images attached to an issue, such as the charts attached to an [incident](https://docs.gitlab.com/operations/incident_management/incidents/)
  name: GitLab Metric images API
  slug: gitlab-metric-images-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve the definitions of the metrics that GitLab collects for [Service Ping](https://docs.gitlab.com/development/internal_analytics/service_ping/).
  name: GitLab Metrics API
  slug: gitlab-metrics-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to mark GitLab database migrations as successful, so that a deployment can proceed without re-running them. These endpoints are available for GitLab Self-Managed and require administrator
  name: GitLab Migrations API
  slug: gitlab-migrations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [milestones](https://docs.gitlab.com/user/project/milestones/) for both projects and groups.
  name: GitLab Milestones API
  slug: gitlab-milestones-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to upload and download the files attached to a version of a machine learning model in the [model registry](https://docs.gitlab.com/user/project/ml/model_registry/). To create models and m
  name: GitLab ML Model Registry API
  slug: gitlab-ml-model-registry-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to track machine learning experiments, runs, and metrics, and to manage the [model registry](https://docs.gitlab.com/user/project/ml/model_registry/). These endpoints implement the MLflow
  name: GitLab ML Ops API
  slug: gitlab-mlops-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to mobile push subscriptions.
  name: GitLab Mobile push subscriptions API
  slug: gitlab-mobile-push-subscriptions-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to namespace projects.
  name: GitLab Namespace projects API
  slug: gitlab-namespace-projects-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to interact with namespaces, a special resource category used to organize users and groups. For more information, see [namespaces](https://docs.gitlab.com/user/namespace/). This API uses '
  name: GitLab Namespaces API
  slug: gitlab-namespaces-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to manage the comments and system records attached to GitLab content. You can: - Create and modify comments on issues, merge requests, epics, snippets, commits, and wiki pages. - Retrieve'
  name: GitLab Notes API
  slug: gitlab-notes-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve and update [notification settings](https://docs.gitlab.com/user/profile/notifications/) globally for your account, or for an individual group or project, which overrides the g
  name: GitLab Notification settings API
  slug: gitlab-notification-settings-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve the server configuration that the workspaces agent requires. This endpoint is internal and used by GitLab components.
  name: GitLab OAuth applications API
  slug: gitlab-oauth-applications-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to start and track offline transfer exports and imports, which migrate data between GitLab instances that cannot reach each other over a network.
  name: GitLab Offline transfers API
  slug: gitlab-offline-transfers-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to query [GitLab Orbit](https://docs.gitlab.com/orbit/), which indexes a group's software development lifecycle. > [!note] > The availability of these endpoints is controlled by a feature
  name: GitLab Orbit API
  slug: gitlab-orbit-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with GitLab organizations. For more information, see [organizations](https://docs.gitlab.com/user/organization/).
  name: GitLab Organizations API
  slug: gitlab-organizations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage the [packages](https://docs.gitlab.com/user/packages/package_registry/) stored in a project or a group.
  name: GitLab Packages API
  slug: gitlab-packages-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to interact with the Cargo package registry, including its sparse index, registry configuration, and crate downloads. Generally these endpoints are used by Cargo itself and are not meant '
  name: 'GitLab Packages: Cargo API'
  slug: gitlab-packages-cargo-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with the [Composer package manager client](https://docs.gitlab.com/user/packages/composer_repository/). > [!warning] > This API is used by the [Composer package manager client
  name: 'GitLab Packages: Composer API'
  slug: gitlab-packages-composer-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: '> [!warning] > The Conan registry is not FIPS compliant and is disabled when FIPS mode is enabled. These > endpoints all return `404 Not Found`. Use this API to interact with the Conan package manager'
  name: 'GitLab Packages: Conan API'
  slug: gitlab-packages-conan-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: '> [!warning] > These endpoints are under development and are not ready for production use due to limited > functionality. The package endpoints are used by Debian package clients such as > [dput](http'
  name: 'GitLab Packages: Debian API'
  slug: gitlab-packages-debian-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with [Helm package clients](https://docs.gitlab.com/user/packages/helm_repository/). > [!warning] > This API is used by the Helm-related package clients such as [Helm](https:/
  name: 'GitLab Packages: Helm API'
  slug: gitlab-packages-helm-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with the [npm package manager client](https://docs.gitlab.com/user/packages/npm_registry/). > [!warning] > This API is used by the [npm package manager client](https://docs.np
  name: 'GitLab Packages: NPM API'
  slug: gitlab-packages-npm-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with the [NuGet package manager client](https://docs.gitlab.com/user/packages/nuget_repository/). > [!warning] > This API is used by the [NuGet package manager client](https:/
  name: 'GitLab Packages: NuGet API'
  slug: gitlab-packages-nuget-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with the [PyPI package manager client](https://docs.gitlab.com/user/packages/pypi_repository/). > [!warning] > This API is used by the [PyPI package manager client](https://py
  name: 'GitLab Packages: PyPi API'
  slug: gitlab-packages-pypi-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to upload RPM packages to the [package registry](https://docs.gitlab.com/user/packages/package_registry/).
  name: 'GitLab Packages: RPM API'
  slug: gitlab-packages-rpm-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with the [Ruby gems and Bundler package manager clients](https://docs.gitlab.com/user/packages/rubygems_registry/). > [!warning] > This API is used by the Ruby gems and Bundle
  name: 'GitLab Packages: RubyGem API'
  slug: gitlab-packages-rubygem-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with [pipeline schedules](https://docs.gitlab.com/ci/pipelines/schedules/).
  name: GitLab Pipeline schedules API
  slug: gitlab-pipeline-schedules-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [CI/CD pipelines](https://docs.gitlab.com/ci/pipelines/) and the [jobs](https://docs.gitlab.com/ci/jobs/) they run.
  name: GitLab Pipelines API
  slug: gitlab-pipelines-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve and change the application limits of a subscription plan. The available plans depend on the GitLab edition. In the Community Edition, only the `default` plan exists. The Enter
  name: GitLab Plan limits API
  slug: gitlab-plan-limits-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [project aliases](https://docs.gitlab.com/user/project/working_with_projects/#project-aliases). After you create an alias for a project, users can clone the repository with that
  name: GitLab Project alias API
  slug: gitlab-project-alias-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve and change a project's [merge request approval configuration](https://docs.gitlab.com/user/project/merge_requests/approvals/settings/), such as the number of approvals a merge
  name: GitLab Project approvals API
  slug: gitlab-project-approvals-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with the Google Cloud integration. For more information, see [GitLab and Google Cloud integration](https://docs.gitlab.com/ci/gitlab_google_cloud_integration/).
  name: GitLab Project Google Cloud integration API
  slug: gitlab-project-google-cloud-integration-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to [import repositories from external sources](https://docs.gitlab.com/user/import/) and to [migrate a project](https://docs.gitlab.com/user/project/settings/import_export/) between GitLa
  name: GitLab Project import API
  slug: gitlab-project-import-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage project [pull mirroring](https://docs.gitlab.com/user/project/repository/mirror/pull/).
  name: GitLab Project mirrors API
  slug: gitlab-project-mirrors-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to download a snapshot of a project's repository, for use in salvaging a corrupt repository. These endpoints require administrator access to the instance.
  name: GitLab Project snapshots API
  slug: gitlab-project-snapshots-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to retrieve project-specific templates, in addition to the templates common to the entire instance: - [Dockerfile templates](https://docs.gitlab.com/api/templates/dockerfiles/) - [Gitigno'
  name: GitLab Project templates API
  slug: gitlab-project-templates-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with project topics. For more information, see [project topics](https://docs.gitlab.com/user/project/project_topics/).
  name: GitLab Project topics API
  slug: gitlab-project-topics-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to interact with [CI/CD job token](https://docs.gitlab.com/ci/jobs/ci_job_token/) scopes. > [!note] > All requests to the CI/CD job token scope API endpoint must be [authenticated](https:'
  name: GitLab Projects job token scope API
  slug: gitlab-projects-job-token-scope-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [protected branches](https://docs.gitlab.com/user/project/repository/branches/protected/) for a project, and the [protected branch settings](https://docs.gitlab.com/user/project
  name: GitLab Protected branches API
  slug: gitlab-protected-branches-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [protected environments](https://docs.gitlab.com/ci/environments/protected_environments/) for a project, and [protected environments for a group](https://docs.gitlab.com/ci/envi
  name: GitLab Protected environments API
  slug: gitlab-protected-environments-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [protected tags](https://docs.gitlab.com/user/project/protected_tags/).
  name: GitLab Protected tags API
  slug: gitlab-protected-tags-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to manage the SAML and SCIM identities linked to users in a group. Prerequisites for the SCIM endpoints: - You must enable [group SSO](https://docs.gitlab.com/user/group/saml_sso/). - You'
  name: GitLab Provider identities API
  slug: gitlab-provider-identities-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [push rules](https://docs.gitlab.com/user/project/repository/push_rules/) for a project, and [group push rules](https://docs.gitlab.com/user/project/repository/push_rules/#group
  name: GitLab Push rules API
  slug: gitlab-push-rules-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [releases](https://docs.gitlab.com/user/project/releases/) for a project, list the releases across a group, and manage the asset links attached to a release. Asset links support
  name: GitLab Releases API
  slug: gitlab-releases-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [remote mirrors](https://docs.gitlab.com/user/project/repository/mirror/push/). You can query and modify the state of these mirrors. For security reasons, the `url` attribute in
  name: GitLab Remote mirrors API
  slug: gitlab-remote-mirrors-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [Git repositories](https://docs.gitlab.com/user/project/repository/).
  name: GitLab Repositories API
  slug: gitlab-repositories-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to retrieve the events that track changes to issues, merge requests, and epics: - [Label](https://docs.gitlab.com/user/project/labels/) events record who added or removed a label, and whe'
  name: GitLab Resource events API
  slug: gitlab-resource-events-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to subscribe to and unsubscribe from [issues](https://docs.gitlab.com/user/project/issues/), [merge requests](https://docs.gitlab.com/user/project/merge_requests/), and [labels](https://d
  name: GitLab Resource subscriptions API
  slug: gitlab-resource-subscriptions-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to rollouts.
  name: GitLab Rollouts API
  slug: gitlab-rollouts-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to create, list, rotate, and revoke the authentication tokens that runner controllers use to authenticate with a GitLab instance and manage runners. These endpoints require administrator '
  name: GitLab Runner controller tokens API
  slug: gitlab-runner-controller-tokens-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage the runner controllers that handle CI/CD job admission control, and the scopes assigned to them. Runner controllers connect to the job router and evaluate jobs against custom po
  name: GitLab Runner controllers API
  slug: gitlab-runner-controllers-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage the [runners](https://docs.gitlab.com/ci/runners/) already registered to an instance, group, or project. To create a runner, use the [`POST /user/runners`](https://docs.gitlab.c
  name: GitLab Runners API
  slug: gitlab-runners-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage the [SAML group links](https://docs.gitlab.com/user/group/saml_sso/group_sync/) that map a group in your identity provider to a GitLab group, and to the role its members receive
  name: GitLab SAML group links API
  slug: gitlab-saml-group-links-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to [search across GitLab](https://docs.gitlab.com/user/search/) in an instance, a group, or a project, and to retrieve information about [advanced search migrations](https://docs.gitlab.c
  name: GitLab Search API
  slug: gitlab-search-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [secure files](https://docs.gitlab.com/ci/secure_files/) for a project.
  name: GitLab Secure files API
  slug: gitlab-secure-files-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to scan a single file for vulnerabilities and return the [SAST](https://docs.gitlab.com/user/application_security/sast/) results in real time.
  name: GitLab Security scans API
  slug: gitlab-security-scans-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to interact with [service accounts](https://docs.gitlab.com/user/profile/service_accounts/). The number of service accounts you can create depends on your subscription and offering: - On '
  name: GitLab Service accounts API
  slug: gitlab-service-accounts-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve information about the current state of Sidekiq, including its jobs, queues, and processes, and to delete jobs from a queue.
  name: GitLab Sidekiq API
  slug: gitlab-sidekiq-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage personal and project [snippets](https://docs.gitlab.com/user/snippets/). To move snippets between storages, use the [snippet repository storage moves API](https://docs.gitlab.co
  name: GitLab Snippets API
  slug: gitlab-snippets-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to upload the SBOM produced by a CI/CD job, download the resulting scan, and reuse a scan that already exists for the same SBOM.
  name: GitLab Software composition analysis API
  slug: gitlab-software-composition-analysis-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to schedule and track [repository storage moves](https://docs.gitlab.com/administration/operations/moving_repositories/) for groups, projects, and snippets. Project moves cover wiki and d
  name: GitLab Storage moves API
  slug: gitlab-storage-moves-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to update [Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).
  name: GitLab Submodules API
  slug: gitlab-submodules-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to manage [code suggestions](https://docs.gitlab.com/user/project/merge_requests/reviews/suggestions/). Suggestions provide a way to propose specific changes that can be directly applied '
  name: GitLab Suggestions API
  slug: gitlab-suggestions-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: The Swagger Doc API from GitLab — 2 operation(s) for swagger doc.
  name: GitLab Swagger Doc API
  slug: gitlab-swagger-doc-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [Git tags](https://docs.gitlab.com/user/project/repository/tags/). This API also returns X.509 signature information from signed tags.
  name: GitLab Tags API
  slug: gitlab-tags-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: 'Use this API to retrieve the file templates available to an entire instance: - [Dockerfile templates](https://gitlab.com/gitlab-org/gitlab-foss/-/tree/master/vendor/Dockerfile) - [`.gitignore` templat'
  name: GitLab Templates API
  slug: gitlab-templates-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with the [Terraform CLI](https://docs.gitlab.com/user/packages/terraform_module_registry/). > [!warning] > This API is used by the [Terraform CLI](https://developer.hashicorp.
  name: GitLab Terraform API
  slug: gitlab-terraform-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to list [to-do items](https://docs.gitlab.com/user/todos/), mark them as done, and create a to-do item for an issue or a merge request.
  name: GitLab To Dos API
  slug: gitlab-to-dos-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to exchange a token for a short-lived JWT that is scoped to a single GitLab service audience.
  name: GitLab Token exchange API
  slug: gitlab-token-exchange-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to serve [feature flags](https://docs.gitlab.com/operations/feature_flags/) to an Unleash-compatible client, and to register that client and receive its metrics. Generally these endpoints
  name: GitLab Unleash API
  slug: gitlab-unleash-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to track internal events and to retrieve the [Service Ping](https://docs.gitlab.com/development/internal_analytics/service_ping/) payload that GitLab collects, including its non-SQL metri
  name: GitLab Usage data API
  slug: gitlab-usage-data-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to interact with user accounts on GitLab. These endpoints can help manage [your account](https://docs.gitlab.com/user/profile/), manage [accounts for other users](https://docs.gitlab.com/
  name: GitLab Users API
  slug: gitlab-users-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to synchronize Visual Studio Code settings, so that a user's editor preferences follow them between VS Code and the [Web IDE](https://docs.gitlab.com/user/project/web_ide/).
  name: GitLab VS Code API
  slug: gitlab-vscode-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: '> [!warning] > These endpoints are in the process of being deprecated and are considered unstable. > The response payload may be subject to change or breakage across GitLab releases. Use the > [GraphQ'
  name: GitLab Vulnerabilities API
  slug: gitlab-vulnerabilities-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve the public key that GitLab uses to sign the commits created with the [web editor](https://docs.gitlab.com/user/project/repository/web_editor/).
  name: GitLab Web commits API
  slug: gitlab-web-commits-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to manage [group wikis](https://docs.gitlab.com/user/project/wiki/group/). An API for [project wikis](https://docs.gitlab.com/api/wikis/) is also available. Comments on a wiki page are ca
  name: GitLab Wikis API
  slug: gitlab-wikis-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Use this API to retrieve agent information and authorize user access for the agent that runs [workspaces](https://docs.gitlab.com/user/workspace/). These endpoints are internal and used by GitLab comp
  name: GitLab Workspaces API
  slug: gitlab-workspaces-api
- baseURL: https://www.gitlab.com/api/
  baseurl_source: declared
  description: The Admin API from GitLab — 11 operation(s) for admin.
  name: GitLab Admin API
  phrasing_intents:
  - id: getApiV4AdminBatchedBackgroundMigrationsId
    intent: Get a batched background migration
    question: How do I check the progress of one batched background migration on my instance?
  - id: getApiV4AdminBatchedBackgroundMigrations
    intent: List batched background migrations
    question: Which batched background migrations are running or queued on my self-managed GitLab?
  - id: putApiV4AdminBatchedBackgroundMigrationsIdResume
    intent: Resume a paused background migration
    question: How do I restart a batched background migration I paused?
  - id: putApiV4AdminBatchedBackgroundMigrationsIdPause
    intent: Pause a batched background migration
    question: How do I temporarily halt a batched background migration that is loading the database?
  - id: getApiV4AdminCiVariablesKey
    intent: Get an instance-level CI variable
    question: How do I read the value and settings of one instance-wide CI/CD variable?
  - id: putApiV4AdminCiVariablesKey
    intent: Update an instance-level CI variable
    question: How do I change the value of an existing instance-wide CI variable?
  - id: deleteApiV4AdminCiVariablesKey
    intent: Delete an instance-level CI variable
    question: How do I remove a CI/CD variable that applies to every project on the instance?
  - id: getApiV4AdminCiVariables
    intent: List instance-level CI variables
    question: What CI/CD variables are defined at the instance level?
  phrasing_ops: 16
  slug: gitlab-admin-api
- baseURL: https://www.gitlab.com/api/
  baseurl_source: declared
  description: The Application API from GitLab — 2 operation(s) for application.
  name: GitLab Application API
  phrasing_intents:
  - id: getApiV4ApplicationAppearance
    intent: Get the instance's appearance settings
    question: What title, logo and header message is my GitLab instance currently using?
  - id: putApiV4ApplicationAppearance
    intent: Change the instance's branding and appearance
    question: How do I set a custom logo and sign-in title for my self-managed GitLab?
  - id: getApiV4ApplicationPlanLimits
    intent: Get a plan's limits
    question: What limits apply to a plan on my GitLab instance, like max pipeline size?
  - id: putApiV4ApplicationPlanLimits
    intent: Change a plan's limits
    question: How do I raise the maximum npm package size for a plan?
  phrasing_ops: 4
  slug: gitlab-application-api
- baseURL: https://www.gitlab.com/api/
  baseurl_source: declared
  description: The Avatar API from GitLab — 1 operation(s) for avatar.
  name: GitLab Avatar API
  phrasing_intents:
  - id: getApiV4Avatar
    intent: Look up a user's avatar URL by email
    question: How do I get the profile picture URL for someone from their email address?
  phrasing_ops: 1
  slug: gitlab-avatar-api
- baseURL: https://www.gitlab.com/api/
  baseurl_source: declared
  description: Operations about bulk_imports
  name: GitLab Bulk Imports API
  phrasing_intents:
  - id: getApiV4BulkImportsImportIdEntitiesEntityId
    intent: Get one entity from a group migration
    question: How do I check the status of a single group or project inside a migration?
  - id: getApiV4BulkImportsImportIdEntities
    intent: List entities in one migration
    question: Which groups and projects are part of a specific migration?
  - id: getApiV4BulkImportsImportId
    intent: Get a group migration
    question: How do I check whether a GitLab-to-GitLab migration has finished?
  - id: getApiV4BulkImportsEntities
    intent: List entities across all migrations
    question: Can I see every group and project I've migrated, across all my imports?
  - id: getApiV4BulkImports
    intent: List all group migrations
    question: What GitLab migrations have I started?
  - id: postApiV4BulkImports
    intent: Start a group or project migration
    question: How do I migrate a group from another GitLab instance by direct transfer?
  phrasing_ops: 6
  slug: gitlab-bulk-imports-api
- baseURL: https://www.gitlab.com/api/
  baseurl_source: declared
  description: The Version API from GitLab — 1 operation(s) for version.
  name: GitLab Version API
  phrasing_intents:
  - id: getApiV4Version
    intent: Get the instance version (deprecated)
    question: Which GitLab version is my server on, using the older version endpoint?
  phrasing_ops: 1
  slug: gitlab-version-api
arazzos:
- description: Render a group badge preview, add it to the group, and confirm the list.
  name: GitLab Add and Preview a Group Badge
  slug: gitlab-add-group-badge-workflow
- description: Render a badge preview, then add it to a project and confirm the list.
  name: GitLab Add and Preview a Project Badge
  slug: gitlab-add-project-badge-workflow
- description: List a group's access requests and approve the first pending requester.
  name: GitLab Approve a Pending Group Access Request
  slug: gitlab-approve-group-access-request-workflow
- description: List a project's access requests and approve the first pending requester.
  name: GitLab Approve a Pending Project Access Request
  slug: gitlab-approve-project-access-request-workflow
- description: Authorize an upload, attach a metric image to an alert, then list images.
  name: GitLab Attach a Metric Image to an Alert
  slug: gitlab-attach-alert-metric-image-workflow
- description: Verify a branch has been merged, then unprotect and delete it.
  name: GitLab Clean Up a Merged Branch
  slug: gitlab-cleanup-merged-branch-workflow
- description: Cut a new branch from a ref and immediately apply push/merge protection.
  name: GitLab Create and Protect a Release Branch
  slug: gitlab-create-and-protect-branch-workflow
- description: Resolve the default branch tip and cut a new feature branch from it.
  name: GitLab Create a Feature Branch from the Default Branch
  slug: gitlab-create-branch-from-default-workflow
- description: Check whether a branch exists and create it from a ref only when missing.
  name: GitLab Ensure a Branch Exists
  slug: gitlab-ensure-branch-exists-workflow
- description: List project jobs, pick the first manual job, and trigger it.
  name: GitLab Find and Run a Pending Manual Job
  slug: gitlab-find-and-run-manual-job-workflow
- description: List failed jobs in a project and fetch full detail for the first one.
  name: GitLab Inspect a Failed CI Job
  slug: gitlab-inspect-failed-jobs-workflow
- description: Survey the branch list, then bulk-delete all merged branches.
  name: GitLab Prune Stale Merged Branches
  slug: gitlab-prune-stale-branches-workflow
- description: Create a broadcast banner, then read it back to confirm it was stored.
  name: GitLab Publish and Verify a Broadcast Message
  slug: gitlab-publish-broadcast-message-workflow
- description: Add an existing Kubernetes cluster, then confirm it in the cluster list.
  name: GitLab Register an Existing Instance Cluster
  slug: gitlab-register-instance-cluster-workflow
- description: Request access to a project, then approve that same requester.
  name: GitLab Request and Approve Project Access
  slug: gitlab-request-and-self-approve-project-access-workflow
- description: Confirm an instance CI variable exists, then delete it.
  name: GitLab Retire an Instance-Level CI Variable
  slug: gitlab-retire-instance-ci-variable-workflow
- description: Find a project badge by name and remove it when present.
  name: GitLab Retire a Project Badge by Name
  slug: gitlab-retire-project-badge-workflow
- description: Retire the current broadcast message and publish a replacement.
  name: GitLab Rotate the Active Broadcast Message
  slug: gitlab-rotate-broadcast-message-workflow
- description: Find an existing project badge by name and update its link and image.
  name: GitLab Rotate a Project Badge by Name
  slug: gitlab-rotate-project-badge-workflow
- description: Kick off a direct-transfer migration, then poll the import until it finishes.
  name: GitLab Start a Migration and Poll to Completion
  slug: gitlab-start-migration-and-poll-workflow
- description: Read a migration's summary, then drill into a specific entity's detail.
  name: GitLab Track a Migration's Entities
  slug: gitlab-track-migration-entities-workflow
- description: Start a manual CI job, then poll its status until it finishes.
  name: GitLab Trigger a Manual CI Job and Poll to Completion
  slug: gitlab-trigger-manual-job-and-poll-workflow
- description: Read an existing broadcast message, then update its window and text.
  name: GitLab Reschedule a Broadcast Message
  slug: gitlab-update-broadcast-message-workflow
- description: Look up an instance CI variable and update it or create it if missing.
  name: GitLab Upsert an Instance-Level CI Variable
  slug: gitlab-upsert-instance-ci-variable-workflow
artifact_total: 488
asyncapis:
- description: GitLab Webhooks deliver HTTP POST payloads to a configured URL whenever specified events occur in a GitLab project or group, such as pushes, merge requests, issues, pipeline status changes, and deploy
  name: GitLab Webhooks
  slug: gitlab-webhooks-asyncapi
collections:
- collection_type: postman
  name: GitLab api/v4/admin
  slug: postman-gitlab-api-v4-admin-openapi-original
- collection_type: postman
  name: GitLab api/v4/application
  slug: postman-gitlab-api-v4-application-openapi-original
- collection_type: postman
  name: GitLab api/v4/applications
  slug: postman-gitlab-api-v4-applications-openapi-original
- collection_type: postman
  name: GitLab api/v4/avatar
  slug: postman-gitlab-api-v4-avatar-openapi-original
- collection_type: postman
  name: GitLab api/v4/broadcast messages
  slug: postman-gitlab-api-v4-broadcast-messages-openapi-original
- collection_type: postman
  name: GitLab api/v4/bulk imports
  slug: postman-gitlab-api-v4-bulk-imports-openapi-original
- collection_type: postman
  name: GitLab api/v4/groups
  slug: postman-gitlab-api-v4-groups-openapi-original
- collection_type: postman
  name: GitLab api/v4/metadata
  slug: postman-gitlab-api-v4-metadata-openapi-original
- collection_type: postman
  name: GitLab api/v4/projects
  slug: postman-gitlab-api-v4-projects-openapi-original
- collection_type: postman
  name: GitLab api/v4/version
  slug: postman-gitlab-api-v4-version-openapi-original
- collection_type: postman
  name: GitLab OAuth 2.0 API
  slug: postman-gitlab-oauth2
- collection_type: postman
  name: GitLab API
  slug: postman-gitlab-openapi-original
- collection_type: postman
  name: GitLab Webhooks API
  slug: postman-gitlab-webhooks
- collection_type: open
  name: GitLab api/v4/ Admin API
  slug: open-gitlab-admin-api
- collection_type: open
  name: GitLab api/v4/ Admin Application API
  slug: open-gitlab-application-api
- collection_type: open
  name: GitLab api/v4/ Admin Applications API
  slug: open-gitlab-applications-api
- collection_type: open
  name: GitLab api/v4/ Admin Authorization API
  slug: open-gitlab-authorization-api
- collection_type: open
  name: GitLab api/v4/ Admin Avatar API
  slug: open-gitlab-avatar-api
- collection_type: open
  name: GitLab api/v4/ Admin Broadcast Messages API
  slug: open-gitlab-broadcast-messages-api
- collection_type: open
  name: GitLab api/v4/ Admin Bulk Imports API
  slug: open-gitlab-bulk-imports-api
- collection_type: open
  name: GitLab api/v4/ Admin Groups API
  slug: open-gitlab-groups-api
- collection_type: open
  name: GitLab api/v4/ Admin Metadata API
  slug: open-gitlab-metadata-api
- collection_type: open
  name: GitLab OAuth 2.0 API
  slug: open-gitlab-oauth2
- collection_type: open
  name: GitLab api/v4/ Admin Project Webhooks API
  slug: open-gitlab-project-webhooks-api
- collection_type: open
  name: GitLab api/v4/ Admin Projects API
  slug: open-gitlab-projects-api
- collection_type: open
  name: GitLab api/v4/ Admin Tokens API
  slug: open-gitlab-tokens-api
- collection_type: open
  name: GitLab api/v4/ Admin User Info API
  slug: open-gitlab-user-info-api
- collection_type: open
  name: GitLab api/v4/ Admin Version API
  slug: open-gitlab-version-api
- collection_type: open
  name: GitLab api/v4/ Admin Webhook Configuration API
  slug: open-gitlab-webhook-configuration-api
- collection_type: open
  name: GitLab api/v4/ Admin Webhook Events API
  slug: open-gitlab-webhook-events-api
- collection_type: open
  name: GitLab Webhooks API
  slug: open-gitlab-webhooks
common:
- group: design
  href: https://artifacts.apis.io/gitlab/conventions/gitlab-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/gitlab-conventions.yml
- group: agent
  href: https://artifacts.apis.io/gitlab/llms/gitlab-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gitlab-docs-llms.txt
- group: build
  href: https://artifacts.apis.io/gitlab/mcp/gitlab-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gitlab-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/gitlab/integrations/gitlab-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/gitlab-integration-edges.yml
- group: commercial
  href: https://artifacts.apis.io/gitlab/finops/gitlab-finops.yml
  title: ''
  type: FinOps
  url: finops/gitlab-finops.yml
- group: design
  href: https://artifacts.apis.io/gitlab/rules/gitlab-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/gitlab-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/gitlab/rules/gitlab-rules.yml
  title: ''
  type: Spectral
  url: rules/gitlab-rules.yml
- group: design
  href: https://artifacts.apis.io/gitlab/rules/gitlab-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/gitlab-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/gitlab/rules/gitlab-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/gitlab-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/gitlab/vocabulary/gitlab-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gitlab-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/gitlab/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gitlab/asyncapi/gitlab-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/gitlab-webhooks-asyncapi.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.gitlab.com/
- group: other
  href: https://artifacts.apis.io/gitlab/hosts/gitlab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gitlab-hosts.yml
- group: other
  href: https://artifacts.apis.io/gitlab/vendors/gitlab-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gitlab-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://docs.gitlab.com/user/project/integrations/webhooks/
- group: operate
  title: ''
  type: Roadmap
  url: https://handbook.gitlab.com/handbook/engineering/architecture/roadmap/
- group: company
  title: ''
  type: Newsroom
  url: https://about.gitlab.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://handbook.gitlab.com/handbook/leadership/
- group: operate
  href: https://artifacts.apis.io/gitlab/rate-limits/gitlab-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gitlab-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gitlab/plans/gitlab-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gitlab-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/gitlab/capabilities/gitlab-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gitlab-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/gitlab/overlays/gitlab-api-v4-admin-openapi-search.yml
  title: ''
  type: Overlay
  url: overlays/gitlab-api-v4-admin-openapi-search.yml
- group: agent
  href: https://artifacts.apis.io/gitlab/agentic-access/gitlab-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gitlab-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gitlab/security/gitlab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gitlab-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gitlab/security/gitlab-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gitlab-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/gitlab/security/gitlab-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gitlab-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gitlab/authentication/gitlab-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gitlab-authentication.yml
- group: auth
  href: https://artifacts.apis.io/gitlab/scopes/gitlab-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gitlab-scopes.yml
- group: build
  href: https://artifacts.apis.io/gitlab/packages/gitlab-packages.yml
  title: ''
  type: Packages
  url: packages/gitlab-packages.yml
- group: agent
  href: https://artifacts.apis.io/gitlab/well-known/gitlab-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gitlab-well-known.yml
- group: auth
  href: https://artifacts.apis.io/gitlab/well-known/gitlab-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gitlab-security.txt
- group: agent
  href: https://artifacts.apis.io/gitlab/mcp/gitlab-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gitlab-mcp.yml
- group: agent
  href: https://artifacts.apis.io/gitlab/llms/gitlab-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gitlab-llms.txt
- group: design
  href: https://artifacts.apis.io/gitlab/conformance/gitlab-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gitlab-conformance.yml
- group: design
  href: https://artifacts.apis.io/gitlab/errors/gitlab-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gitlab-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gitlab/lifecycle/gitlab-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gitlab-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gitlab/conventions/gitlab-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gitlab-conventions.yml
- group: operate
  href: https://artifacts.apis.io/gitlab/changelog/gitlab-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gitlab-changelog.yml
- group: build
  href: https://artifacts.apis.io/gitlab/cli/gitlab-cli.yml
  title: ''
  type: CLI
  url: cli/gitlab-cli.yml
- group: design
  href: https://artifacts.apis.io/gitlab/data-model/gitlab-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gitlab-data-model.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/gitlab/overview
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-add-group-badge-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-add-group-badge-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-add-project-badge-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-add-project-badge-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-approve-group-access-request-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-approve-group-access-request-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-approve-project-access-request-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-approve-project-access-request-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-attach-alert-metric-image-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-attach-alert-metric-image-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-cleanup-merged-branch-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-cleanup-merged-branch-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-create-and-protect-branch-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-create-and-protect-branch-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-create-branch-from-default-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-create-branch-from-default-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-ensure-branch-exists-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-ensure-branch-exists-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-find-and-run-manual-job-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-find-and-run-manual-job-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-inspect-failed-jobs-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-inspect-failed-jobs-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-prune-stale-branches-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-prune-stale-branches-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-publish-broadcast-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-publish-broadcast-message-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-register-instance-cluster-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-register-instance-cluster-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-request-and-self-approve-project-access-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-request-and-self-approve-project-access-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-retire-instance-ci-variable-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-retire-instance-ci-variable-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-retire-project-badge-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-retire-project-badge-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-rotate-broadcast-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-rotate-broadcast-message-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-rotate-project-badge-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-rotate-project-badge-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-start-migration-and-poll-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-start-migration-and-poll-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-track-migration-entities-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-track-migration-entities-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-trigger-manual-job-and-poll-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-trigger-manual-job-and-poll-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-update-broadcast-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-update-broadcast-message-workflow.yml
- group: design
  href: https://artifacts.apis.io/gitlab/arazzo/gitlab-upsert-instance-ci-variable-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gitlab-upsert-instance-ci-variable-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gitlab-com
- group: company
  title: ''
  type: Website
  url: https://about.gitlab.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.gitlab.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gitlab.com/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.gitlab.com/api/rest/authentication/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gitlabhq
- group: company
  title: ''
  type: Blog
  url: https://about.gitlab.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gitlab.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://about.gitlab.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://about.gitlab.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.gitlab.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://about.gitlab.com/company/contact/
- group: operate
  title: ''
  type: IDESupport
  url: https://docs.gitlab.com/ee/editor_extensions/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://about.gitlab.com/releases/categories/releases/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.gitlab.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://about.gitlab.com/get-started/
- group: start
  title: ''
  type: SignUp
  url: https://gitlab.com/users/sign_up
- group: operate
  title: ''
  type: Support
  url: https://about.gitlab.com/support/
- group: operate
  title: ''
  type: ChangeLog
  url: https://gitlab.com/gitlab-org/gitlab/blob/master/CHANGELOG.md
- group: build
  title: ''
  type: SDKs
  url: https://docs.gitlab.com/api/rest/third_party_clients/
- group: operate
  title: ''
  type: Support
  url: https://forum.gitlab.com/
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.gitlab.com/security/rate_limits/
- group: design
  href: https://artifacts.apis.io/gitlab/json-ld/gitlab-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gitlab-context.jsonld
- group: docs
  href: https://artifacts.apis.io/gitlab/json-schema/gitlab-project-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/gitlab-project-schema.json
- group: docs
  href: https://artifacts.apis.io/gitlab/json-schema/gitlab-merge-request-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/gitlab-merge-request-schema.json
- group: docs
  href: https://artifacts.apis.io/gitlab/json-schema/gitlab-issue-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/gitlab-issue-schema.json
- group: docs
  href: https://artifacts.apis.io/gitlab/json-schema/gitlab-pipeline-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/gitlab-pipeline-schema.json
- group: auth
  title: ''
  type: Security
  url: https://about.gitlab.com/security/
- group: auth
  title: ''
  type: Security
  url: https://about.gitlab.com/security/disclosure/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://about.gitlab.com/whats-new/
- group: company
  title: ''
  type: Partners
  url: https://about.gitlab.com/partners/technology-partners/
- group: docs
  title: ''
  type: Documentation
  url: https://about.gitlab.com/solutions/open-source/
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.gitlab.com/
- group: build
  title: ''
  type: Tools
  url: https://docs.gitlab.com/api/openapi/openapi_interactive/
- group: build
  title: ''
  type: GitHubRepository
  url: https://gitlab.com/gitlab-org/gitlab
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.gitlab.com/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gitlab.com/api/api_resources/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gitlab.com/api/rest/
created: '2023-11-10'
description: GitLab Inc. is an open-core company that develops GitLab, a DevOps software platform for building, securing, and managing applications. Created by Ukrainian developer Dmytro Zaporozhets and Dutch developer Sytse Sijbrandij, GitLab became the first partly-Ukrainian unicorn in 2018. Known for promoting remote work, it is one of the largest all-remote companies globally. GitLab has approximately 30 million registered users, including 1 million active licensed users.
examples:
- key_count: 6
  name: Gitlab Api V4 Admin Api_Entities_Batched Background Migration Example
  slug: gitlab-api-v4-admin-api_entities_batched-background-migration-example
- key_count: 7
  name: Gitlab Api V4 Admin Api_Entities_Ci_Variable Example
  slug: gitlab-api-v4-admin-api_entities_ci_variable-example
- key_count: 10
  name: Gitlab Api V4 Admin Api_Entities_Cluster Example
  slug: gitlab-api-v4-admin-api_entities_cluster-example
- key_count: 2
  name: Gitlab Api V4 Admin Api_Entities_Dictionary_Table Example
  slug: gitlab-api-v4-admin-api_entities_dictionary_table-example
- key_count: 10
  name: Gitlab Api V4 Application Api_Entities_Appearance Example
  slug: gitlab-api-v4-application-api_entities_appearance-example
- key_count: 6
  name: Gitlab Api V4 Application Api_Entities_Application With Secret Example
  slug: gitlab-api-v4-application-api_entities_application-with-secret-example
- key_count: 10
  name: Gitlab Api V4 Application Api_Entities_Plan Limit Example
  slug: gitlab-api-v4-application-api_entities_plan-limit-example
- key_count: 6
  name: Gitlab Api V4 Applications Api_Entities_Application With Secret Example
  slug: gitlab-api-v4-applications-api_entities_application-with-secret-example
- key_count: 1
  name: Gitlab Api V4 Avatar Api_Entities_Avatar Example
  slug: gitlab-api-v4-avatar-api_entities_avatar-example
- key_count: 10
  name: Gitlab Api V4 Broadcast Messages Api_Entities_Broadcast Message Example
  slug: gitlab-api-v4-broadcast-messages-api_entities_broadcast-message-example
- key_count: 5
  name: Gitlab Api V4 Bulk Imports Api_Entities_Bulk Import Example
  slug: gitlab-api-v4-bulk-imports-api_entities_bulk-import-example
- key_count: 10
  name: Gitlab Api V4 Bulk Imports Api_Entities_Bulk Imports Example
  slug: gitlab-api-v4-bulk-imports-api_entities_bulk-imports-example
- key_count: 10
  name: Gitlab Api V4 Groups Api_Entities_Access Requester Example
  slug: gitlab-api-v4-groups-api_entities_access-requester-example
- key_count: 7
  name: Gitlab Api V4 Groups Api_Entities_Badge Example
  slug: gitlab-api-v4-groups-api_entities_badge-example
- key_count: 5
  name: Gitlab Api V4 Groups Api_Entities_Basic Badge Details Example
  slug: gitlab-api-v4-groups-api_entities_basic-badge-details-example
- key_count: 4
  name: Gitlab Api V4 Metadata Api_Entities_Metadata Example
  slug: gitlab-api-v4-metadata-api_entities_metadata-example
- key_count: 10
  name: Gitlab Api V4 Projects Api_Entities_Access Requester Example
  slug: gitlab-api-v4-projects-api_entities_access-requester-example
- key_count: 7
  name: Gitlab Api V4 Projects Api_Entities_Badge Example
  slug: gitlab-api-v4-projects-api_entities_badge-example
- key_count: 5
  name: Gitlab Api V4 Projects Api_Entities_Basic Badge Details Example
  slug: gitlab-api-v4-projects-api_entities_basic-badge-details-example
- key_count: 9
  name: Gitlab Api V4 Projects Api_Entities_Branch Example
  slug: gitlab-api-v4-projects-api_entities_branch-example
- key_count: 10
  name: Gitlab Api V4 Projects Api_Entities_Job Example
  slug: gitlab-api-v4-projects-api_entities_job-example
- key_count: 6
  name: Gitlab Api V4 Projects Api_Entities_Metric Image Example
  slug: gitlab-api-v4-projects-api_entities_metric-image-example
- key_count: 4
  name: Gitlab Api V4 Version Api_Entities_Metadata Example
  slug: gitlab-api-v4-version-api_entities_metadata-example
- key_count: 10
  name: Gitlab Issue Example
  slug: gitlab-issue-example
- key_count: 10
  name: Gitlab Merge Request Example
  slug: gitlab-merge-request-example
- key_count: 2
  name: Gitlab Oauth2 Device Authorization Request Example
  slug: gitlab-oauth2-device-authorization-request-example
- key_count: 6
  name: Gitlab Oauth2 Device Authorization Response Example
  slug: gitlab-oauth2-device-authorization-response-example
- key_count: 3
  name: Gitlab Oauth2 Revoke Token Request Example
  slug: gitlab-oauth2-revoke-token-request-example
- key_count: 5
  name: Gitlab Oauth2 Token Info Example
  slug: gitlab-oauth2-token-info-example
- key_count: 10
  name: Gitlab Oauth2 Token Request Example
  slug: gitlab-oauth2-token-request-example
- key_count: 6
  name: Gitlab Oauth2 Token Response Example
  slug: gitlab-oauth2-token-response-example
- key_count: 8
  name: Gitlab Oauth2 User Info Example
  slug: gitlab-oauth2-user-info-example
- key_count: 10
  name: Gitlab Openapi Original Api_Entities_Access Requester Example
  slug: gitlab-openapi-original-api_entities_access-requester-example
- key_count: 7
  name: Gitlab Openapi Original Api_Entities_Badge Example
  slug: gitlab-openapi-original-api_entities_badge-example
- key_count: 5
  name: Gitlab Openapi Original Api_Entities_Basic Badge Details Example
  slug: gitlab-openapi-original-api_entities_basic-badge-details-example
- key_count: 6
  name: Gitlab Openapi Original Api_Entities_Batched Background Migration Example
  slug: gitlab-openapi-original-api_entities_batched-background-migration-example
- key_count: 9
  name: Gitlab Openapi Original Api_Entities_Branch Example
  slug: gitlab-openapi-original-api_entities_branch-example
- key_count: 7
  name: Gitlab Openapi Original Api_Entities_Ci_Variable Example
  slug: gitlab-openapi-original-api_entities_ci_variable-example
- key_count: 10
  name: Gitlab Openapi Original Api_Entities_Cluster Example
  slug: gitlab-openapi-original-api_entities_cluster-example
- key_count: 10
  name: Gitlab Openapi Original Api_Entities_Commit Example
  slug: gitlab-openapi-original-api_entities_commit-example
- key_count: 2
  name: Gitlab Openapi Original Api_Entities_Custom Attribute Example
  slug: gitlab-openapi-original-api_entities_custom-attribute-example
- key_count: 2
  name: Gitlab Openapi Original Api_Entities_Dictionary_Table Example
  slug: gitlab-openapi-original-api_entities_dictionary_table-example
- key_count: 6
  name: Gitlab Openapi Original Api_Entities_Metric Image Example
  slug: gitlab-openapi-original-api_entities_metric-image-example
- key_count: 4
  name: Gitlab Openapi Original Api_Entities_Platform_Kubernetes Example
  slug: gitlab-openapi-original-api_entities_platform_kubernetes-example
- key_count: 7
  name: Gitlab Openapi Original Api_Entities_Project Identity Example
  slug: gitlab-openapi-original-api_entities_project-identity-example
- key_count: 7
  name: Gitlab Openapi Original Api_Entities_Provider_Gcp Example
  slug: gitlab-openapi-original-api_entities_provider_gcp-example
- key_count: 9
  name: Gitlab Openapi Original Api_Entities_User Basic Example
  slug: gitlab-openapi-original-api_entities_user-basic-example
- key_count: 10
  name: Gitlab Pipeline Example
  slug: gitlab-pipeline-example
- key_count: 10
  name: Gitlab Project Example
  slug: gitlab-project-example
- key_count: 10
  name: Gitlab Webhooks Webhook Event Example
  slug: gitlab-webhooks-webhook-event-example
- key_count: 10
  name: Gitlab Webhooks Webhook Example
  slug: gitlab-webhooks-webhook-example
- key_count: 10
  name: Gitlab Webhooks Webhook Input Example
  slug: gitlab-webhooks-webhook-input-example
features:
- 'Free: 5 users, 400 compute minutes/mo, 10 GiB storage'
- 'Premium $29/user/mo: 10K compute minutes, $12 GitLab Credits/user'
- 'Ultimate custom: 50K compute minutes, $24 Credits/user, security testing'
- REST and GraphQL APIs
- 'Authenticated API: 2,000 req/min/user'
- 'Unauthenticated API: 500 req/min/IP'
- 'Search API: 30 req/min/user'
- Self-hosted Community Edition (free OSS)
- Self-hosted Enterprise Edition (paid)
- GitLab Runner for shared/dedicated runners
- OAuth 2.0 + personal access tokens + project access tokens
- Webhooks for project, group, and system events
- GitLab Duo AI assistant (separate add-on)
- Container Registry, Package Registry, Helm Chart Registry
- GitLab Pages static site hosting
- 'Application Security Testing (Ultimate): SAST, DAST, secret detection'
finops:
- has_sources: true
  method: derived
  name: Gitlab Finops
  primary_unit: user
  service_category: ''
  slug: gitlab-finops
  template: false
graphqls:
- description: 'GraphQL is a query language for APIs. You can use it to request the exact data you need, and therefore limit the number of requests you need. GraphQL data is arranged in types, so your client can use '
  name: GitLab GraphQL API
  slug: gitlab-graphql
image: /assets/icons/gitlab.png
json_schemas:
- name: API_Entities_AccessRequester
  property_count: 10
  slug: gitlab-api-entities-access-requester
- name: API_Entities_Appearance
  property_count: 16
  slug: gitlab-api-entities-appearance
- name: API_Entities_Application
  property_count: 5
  slug: gitlab-api-entities-application
- name: API_Entities_ApplicationWithSecret
  property_count: 6
  slug: gitlab-api-entities-application-with-secret
- name: API_Entities_Avatar
  property_count: 1
  slug: gitlab-api-entities-avatar
- name: API_Entities_Badge
  property_count: 7
  slug: gitlab-api-entities-badge
- name: API_Entities_BasicBadgeDetails
  property_count: 5
  slug: gitlab-api-entities-basic-badge-details
- name: API_Entities_BatchedBackgroundMigration
  property_count: 6
  slug: gitlab-api-entities-batched-background-migration
- name: API_Entities_Branch
  property_count: 9
  slug: gitlab-api-entities-branch
- name: API_Entities_BroadcastMessage
  property_count: 11
  slug: gitlab-api-entities-broadcast-message
- name: API_Entities_BulkImport
  property_count: 5
  slug: gitlab-api-entities-bulk-import
- name: API_Entities_BulkImports
  property_count: 16
  slug: gitlab-api-entities-bulk-imports
- name: API_Entities_Ci_Variable
  property_count: 7
  slug: gitlab-api-entities-ci-variable
- name: API_Entities_Cluster
  property_count: 15
  slug: gitlab-api-entities-cluster
- name: API_Entities_Dictionary_Table
  property_count: 2
  slug: gitlab-api-entities-dictionary-table
- name: API_Entities_Job
  property_count: 19
  slug: gitlab-api-entities-job
- name: API_Entities_Metadata
  property_count: 4
  slug: gitlab-api-entities-metadata
- name: API_Entities_MetricImage
  property_count: 6
  slug: gitlab-api-entities-metric-image
- name: API_Entities_PlanLimit
  property_count: 20
  slug: gitlab-api-entities-plan-limit
- name: API_Entities_BatchedBackgroundMigration
  property_count: 6
  slug: gitlab-api-v4-admin-api_entities_batched-background-migration
- name: API_Entities_Ci_Variable
  property_count: 7
  slug: gitlab-api-v4-admin-api_entities_ci_variable
- name: API_Entities_Cluster
  property_count: 15
  slug: gitlab-api-v4-admin-api_entities_cluster
- name: API_Entities_Dictionary_Table
  property_count: 2
  slug: gitlab-api-v4-admin-api_entities_dictionary_table
- name: API_Entities_Appearance
  property_count: 16
  slug: gitlab-api-v4-application-api_entities_appearance
- name: API_Entities_ApplicationWithSecret
  property_count: 6
  slug: gitlab-api-v4-application-api_entities_application-with-secret
- name: API_Entities_PlanLimit
  property_count: 20
  slug: gitlab-api-v4-application-api_entities_plan-limit
- name: API_Entities_ApplicationWithSecret
  property_count: 6
  slug: gitlab-api-v4-applications-api_entities_application-with-secret
- name: API_Entities_Avatar
  property_count: 1
  slug: gitlab-api-v4-avatar-api_entities_avatar
- name: API_Entities_BroadcastMessage
  property_count: 11
  slug: gitlab-api-v4-broadcast-messages-api_entities_broadcast-message
- name: API_Entities_BulkImport
  property_count: 5
  slug: gitlab-api-v4-bulk-imports-api_entities_bulk-import
- name: API_Entities_BulkImports
  property_count: 16
  slug: gitlab-api-v4-bulk-imports-api_entities_bulk-imports
- name: API_Entities_AccessRequester
  property_count: 10
  slug: gitlab-api-v4-groups-api_entities_access-requester
- name: API_Entities_Badge
  property_count: 7
  slug: gitlab-api-v4-groups-api_entities_badge
- name: API_Entities_BasicBadgeDetails
  property_count: 5
  slug: gitlab-api-v4-groups-api_entities_basic-badge-details
- name: API_Entities_Metadata
  property_count: 4
  slug: gitlab-api-v4-metadata-api_entities_metadata
- name: API_Entities_AccessRequester
  property_count: 10
  slug: gitlab-api-v4-projects-api_entities_access-requester
- name: API_Entities_Badge
  property_count: 7
  slug: gitlab-api-v4-projects-api_entities_badge
- name: API_Entities_BasicBadgeDetails
  property_count: 5
  slug: gitlab-api-v4-projects-api_entities_basic-badge-details
- name: API_Entities_Branch
  property_count: 9
  slug: gitlab-api-v4-projects-api_entities_branch
- name: API_Entities_Job
  property_count: 19
  slug: gitlab-api-v4-projects-api_entities_job
- name: API_Entities_MetricImage
  property_count: 6
  slug: gitlab-api-v4-projects-api_entities_metric-image
- name: API_Entities_Metadata
  property_count: 4
  slug: gitlab-api-v4-version-api_entities_metadata
- name: APIEntitiesApplicationSetting
  property_count: 690
  slug: gitlab-apientities-application-setting
- name: APIEntitiesGeoNodeStatus
  property_count: 605
  slug: gitlab-apientities-geo-node-status
- name: APIEntitiesGeoSiteStatus
  property_count: 605
  slug: gitlab-apientities-geo-site-status
- name: DeviceAuthorizationRequest
  property_count: 2
  slug: gitlab-device-authorization-request
- name: DeviceAuthorizationResponse
  property_count: 6
  slug: gitlab-device-authorization-response
- name: GitLab Issue
  property_count: 29
  slug: gitlab-issue
- name: GitLab Merge Request
  property_count: 33
  slug: gitlab-merge-request
- name: DeviceAuthorizationRequest
  property_count: 2
  slug: gitlab-oauth2-device-authorization-request
- name: DeviceAuthorizationResponse
  property_count: 6
  slug: gitlab-oauth2-device-authorization-response
- name: RevokeTokenRequest
  property_count: 3
  slug: gitlab-oauth2-revoke-token-request
- name: TokenInfo
  property_count: 5
  slug: gitlab-oauth2-token-info
- name: TokenRequest
  property_count: 10
  slug: gitlab-oauth2-token-request
- name: TokenResponse
  property_count: 6
  slug: gitlab-oauth2-token-response
- name: UserInfo
  property_count: 8
  slug: gitlab-oauth2-user-info
- name: API_Entities_AccessRequester
  property_count: 10
  slug: gitlab-openapi-original-api_entities_access-requester
- name: API_Entities_Badge
  property_count: 7
  slug: gitlab-openapi-original-api_entities_badge
- name: API_Entities_BasicBadgeDetails
  property_count: 5
  slug: gitlab-openapi-original-api_entities_basic-badge-details
- name: API_Entities_BatchedBackgroundMigration
  property_count: 6
  slug: gitlab-openapi-original-api_entities_batched-background-migration
- name: API_Entities_Branch
  property_count: 9
  slug: gitlab-openapi-original-api_entities_branch
- name: API_Entities_Ci_Variable
  property_count: 7
  slug: gitlab-openapi-original-api_entities_ci_variable
- name: API_Entities_Cluster
  property_count: 15
  slug: gitlab-openapi-original-api_entities_cluster
- name: API_Entities_Commit
  property_count: 14
  slug: gitlab-openapi-original-api_entities_commit
- name: API_Entities_CustomAttribute
  property_count: 2
  slug: gitlab-openapi-original-api_entities_custom-attribute
- name: API_Entities_Dictionary_Table
  property_count: 2
  slug: gitlab-openapi-original-api_entities_dictionary_table
- name: API_Entities_MetricImage
  property_count: 6
  slug: gitlab-openapi-original-api_entities_metric-image
- name: API_Entities_Platform_Kubernetes
  property_count: 4
  slug: gitlab-openapi-original-api_entities_platform_kubernetes
- name: API_Entities_ProjectIdentity
  property_count: 7
  slug: gitlab-openapi-original-api_entities_project-identity
- name: API_Entities_Provider_Gcp
  property_count: 7
  slug: gitlab-openapi-original-api_entities_provider_gcp
- name: API_Entities_UserBasic
  property_count: 9
  slug: gitlab-openapi-original-api_entities_user-basic
- name: GitLab Pipeline
  property_count: 22
  slug: gitlab-pipeline
- name: postApiV4GeoStatusRequest
  property_count: 1
  slug: gitlab-post-api-v4-geo-status-request
- name: GitLab Project
  property_count: 33
  slug: gitlab-project
- name: putApiV4ApplicationSettingsRequest
  property_count: 687
  slug: gitlab-put-api-v4-application-settings-request
- name: putApiV4ProjectsIdRequest
  property_count: 124
  slug: gitlab-put-api-v4-projects-id-request
- name: RevokeTokenRequest
  property_count: 3
  slug: gitlab-revoke-token-request
- name: TokenInfo
  property_count: 5
  slug: gitlab-token-info
- name: TokenRequest
  property_count: 10
  slug: gitlab-token-request
- name: TokenResponse
  property_count: 6
  slug: gitlab-token-response
- name: UserInfo
  property_count: 8
  slug: gitlab-user-info
- name: WebhookEvent
  property_count: 10
  slug: gitlab-webhook-event
- name: WebhookInput
  property_count: 19
  slug: gitlab-webhook-input
- name: Webhook
  property_count: 24
  slug: gitlab-webhook
- name: WebhookEvent
  property_count: 10
  slug: gitlab-webhooks-webhook-event
- name: WebhookInput
  property_count: 19
  slug: gitlab-webhooks-webhook-input
- name: Webhook
  property_count: 24
  slug: gitlab-webhooks-webhook
json_structures:
- name: Gitlab Api V4 Admin Api_Entities_Batched Background Migration Structure
  property_count: 6
  slug: gitlab-api-v4-admin-api_entities_batched-background-migration-structure
- name: Gitlab Api V4 Admin Api_Entities_Ci_Variable Structure
  property_count: 7
  slug: gitlab-api-v4-admin-api_entities_ci_variable-structure
- name: Gitlab Api V4 Admin Api_Entities_Cluster Structure
  property_count: 15
  slug: gitlab-api-v4-admin-api_entities_cluster-structure
- name: Gitlab Api V4 Admin Api_Entities_Dictionary_Table Structure
  property_count: 2
  slug: gitlab-api-v4-admin-api_entities_dictionary_table-structure
- name: Gitlab Api V4 Application Api_Entities_Appearance Structure
  property_count: 16
  slug: gitlab-api-v4-application-api_entities_appearance-structure
- name: Gitlab Api V4 Application Api_Entities_Application With Secret Structure
  property_count: 6
  slug: gitlab-api-v4-application-api_entities_application-with-secret-structure
- name: Gitlab Api V4 Application Api_Entities_Plan Limit Structure
  property_count: 20
  slug: gitlab-api-v4-application-api_entities_plan-limit-structure
- name: Gitlab Api V4 Applications Api_Entities_Application With Secret Structure
  property_count: 6
  slug: gitlab-api-v4-applications-api_entities_application-with-secret-structure
- name: Gitlab Api V4 Avatar Api_Entities_Avatar Structure
  property_count: 1
  slug: gitlab-api-v4-avatar-api_entities_avatar-structure
- name: Gitlab Api V4 Broadcast Messages Api_Entities_Broadcast Message Structure
  property_count: 11
  slug: gitlab-api-v4-broadcast-messages-api_entities_broadcast-message-structure
- name: Gitlab Api V4 Bulk Imports Api_Entities_Bulk Import Structure
  property_count: 5
  slug: gitlab-api-v4-bulk-imports-api_entities_bulk-import-structure
- name: Gitlab Api V4 Bulk Imports Api_Entities_Bulk Imports Structure
  property_count: 16
  slug: gitlab-api-v4-bulk-imports-api_entities_bulk-imports-structure
- name: Gitlab Api V4 Groups Api_Entities_Access Requester Structure
  property_count: 10
  slug: gitlab-api-v4-groups-api_entities_access-requester-structure
- name: Gitlab Api V4 Groups Api_Entities_Badge Structure
  property_count: 7
  slug: gitlab-api-v4-groups-api_entities_badge-structure
- name: Gitlab Api V4 Groups Api_Entities_Basic Badge Details Structure
  property_count: 5
  slug: gitlab-api-v4-groups-api_entities_basic-badge-details-structure
- name: Gitlab Api V4 Metadata Api_Entities_Metadata Structure
  property_count: 4
  slug: gitlab-api-v4-metadata-api_entities_metadata-structure
- name: Gitlab Api V4 Projects Api_Entities_Access Requester Structure
  property_count: 10
  slug: gitlab-api-v4-projects-api_entities_access-requester-structure
- name: Gitlab Api V4 Projects Api_Entities_Badge Structure
  property_count: 7
  slug: gitlab-api-v4-projects-api_entities_badge-structure
- name: Gitlab Api V4 Projects Api_Entities_Basic Badge Details Structure
  property_count: 5
  slug: gitlab-api-v4-projects-api_entities_basic-badge-details-structure
- name: Gitlab Api V4 Projects Api_Entities_Branch Structure
  property_count: 9
  slug: gitlab-api-v4-projects-api_entities_branch-structure
- name: Gitlab Api V4 Projects Api_Entities_Job Structure
  property_count: 19
  slug: gitlab-api-v4-projects-api_entities_job-structure
- name: Gitlab Api V4 Projects Api_Entities_Metric Image Structure
  property_count: 6
  slug: gitlab-api-v4-projects-api_entities_metric-image-structure
- name: Gitlab Api V4 Version Api_Entities_Metadata Structure
  property_count: 4
  slug: gitlab-api-v4-version-api_entities_metadata-structure
- name: Gitlab Issue Structure
  property_count: 29
  slug: gitlab-issue-structure
- name: Gitlab Merge Request Structure
  property_count: 33
  slug: gitlab-merge-request-structure
- name: Gitlab Oauth2 Device Authorization Request Structure
  property_count: 2
  slug: gitlab-oauth2-device-authorization-request-structure
- name: Gitlab Oauth2 Device Authorization Response Structure
  property_count: 6
  slug: gitlab-oauth2-device-authorization-response-structure
- name: Gitlab Oauth2 Revoke Token Request Structure
  property_count: 3
  slug: gitlab-oauth2-revoke-token-request-structure
- name: Gitlab Oauth2 Token Info Structure
  property_count: 5
  slug: gitlab-oauth2-token-info-structure
- name: Gitlab Oauth2 Token Request Structure
  property_count: 10
  slug: gitlab-oauth2-token-request-structure
- name: Gitlab Oauth2 Token Response Structure
  property_count: 6
  slug: gitlab-oauth2-token-response-structure
- name: Gitlab Oauth2 User Info Structure
  property_count: 8
  slug: gitlab-oauth2-user-info-structure
- name: Gitlab Openapi Original Api_Entities_Access Requester Structure
  property_count: 10
  slug: gitlab-openapi-original-api_entities_access-requester-structure
- name: Gitlab Openapi Original Api_Entities_Badge Structure
  property_count: 7
  slug: gitlab-openapi-original-api_entities_badge-structure
- name: Gitlab Openapi Original Api_Entities_Basic Badge Details Structure
  property_count: 5
  slug: gitlab-openapi-original-api_entities_basic-badge-details-structure
- name: Gitlab Openapi Original Api_Entities_Batched Background Migration Structure
  property_count: 6
  slug: gitlab-openapi-original-api_entities_batched-background-migration-structure
- name: Gitlab Openapi Original Api_Entities_Branch Structure
  property_count: 9
  slug: gitlab-openapi-original-api_entities_branch-structure
- name: Gitlab Openapi Original Api_Entities_Ci_Variable Structure
  property_count: 7
  slug: gitlab-openapi-original-api_entities_ci_variable-structure
- name: Gitlab Openapi Original Api_Entities_Cluster Structure
  property_count: 15
  slug: gitlab-openapi-original-api_entities_cluster-structure
- name: Gitlab Openapi Original Api_Entities_Commit Structure
  property_count: 14
  slug: gitlab-openapi-original-api_entities_commit-structure
- name: Gitlab Openapi Original Api_Entities_Custom Attribute Structure
  property_count: 2
  slug: gitlab-openapi-original-api_entities_custom-attribute-structure
- name: Gitlab Openapi Original Api_Entities_Dictionary_Table Structure
  property_count: 2
  slug: gitlab-openapi-original-api_entities_dictionary_table-structure
- name: Gitlab Openapi Original Api_Entities_Metric Image Structure
  property_count: 6
  slug: gitlab-openapi-original-api_entities_metric-image-structure
- name: Gitlab Openapi Original Api_Entities_Platform_Kubernetes Structure
  property_count: 4
  slug: gitlab-openapi-original-api_entities_platform_kubernetes-structure
- name: Gitlab Openapi Original Api_Entities_Project Identity Structure
  property_count: 7
  slug: gitlab-openapi-original-api_entities_project-identity-structure
- name: Gitlab Openapi Original Api_Entities_Provider_Gcp Structure
  property_count: 7
  slug: gitlab-openapi-original-api_entities_provider_gcp-structure
- name: Gitlab Openapi Original Api_Entities_User Basic Structure
  property_count: 9
  slug: gitlab-openapi-original-api_entities_user-basic-structure
- name: Gitlab Pipeline Structure
  property_count: 22
  slug: gitlab-pipeline-structure
- name: Gitlab Project Structure
  property_count: 33
  slug: gitlab-project-structure
- name: Gitlab Webhooks Webhook Event Structure
  property_count: 10
  slug: gitlab-webhooks-webhook-event-structure
- name: Gitlab Webhooks Webhook Input Structure
  property_count: 19
  slug: gitlab-webhooks-webhook-input-structure
- name: Gitlab Webhooks Webhook Structure
  property_count: 24
  slug: gitlab-webhooks-webhook-structure
jsonld:
- class_count: 38
  name: Gitlab Context
  property_count: 268
  slug: gitlab-context
layout: provider
mcp_servers:
- description: Remote MCP server at gitlab.com over HTTP requiring OAuth; 59 tools listed.
  name: GitLab MCP Server
  slug: gitlab
modified: '2026-11-05'
name: GitLab
nav: Providers
network: true
overview: 'GitLab publishes 189 API contracts indexed on the [APIs.io](https://apis.io/) network, including Orbit gRPC API, Applications API, Authorization API, and 186 more. Tagged areas include Code, Developer Tools, Platform, Software Development, and Version Control.


  The GitLab catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 4 Spectral governance rulesets.


  GitLab''s developer surface includes authentication, changelog, CLI, developer portal, documentation, engineering blog, pricing, and 97 more developer resources.'
plans:
- name: Gitlab Plans Pricing
  plan_count: 9
  slug: gitlab-plans-pricing
- name: Gitlab Price Estimates
  plan_count: 0
  slug: gitlab-price-estimates
random_paper: 3
rate_limits:
- limit_count: 67
  name: Gitlab Rate Limits
  slug: gitlab-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: GitLab — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: gitlab-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: GitLab — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: gitlab-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 118
  extends:
  - spectral:oas
  name: GitLab API Rules
  rule_count: 77
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 18
  slug: gitlab-rules
- authorship: generated
  effective_rule_count: 67
  extends:
  - spectral:oas
  name: GitLab API Rules
  rule_count: 26
  severity_counts:
    error: 14
    hint: 0
    info: 3
    warn: 9
  slug: gitlab-spectral-rules
scopes:
- name: Gitlab Scopes
  scope_count: 25
  slug: gitlab-scopes
  summary_line: 25 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: exemplar
  composite: 79.6
  coverage:
    artifact_dirs: 45
    catalog_earned: 91.0
    catalog_earned_first_party: 24.0
    catalog_gap: 24.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 89.5
    contract_governance: 45.5
    contract_quality: 75.1
    developer_ergonomics: 74.4
    discoverability: 73.3
    operational_transparency: 90.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 82.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 187
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 42.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gitlab/gitlab-2026-06-20T181844.png
security:
- kind: authentication
  name: Gitlab Authentication
  slug: gitlab-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Gitlab Domain Security
  slug: gitlab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gitlab Vulnerability Disclosure
  slug: gitlab-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Gitlab Trust Center
  slug: gitlab-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, GDPR, CSA STAR
skill_count: 7
skills:
- name: gitlab-commit-and-open-merge-request
  slug: gitlab-commit-and-open-merge-request
- name: gitlab-create-protect-branch
  slug: gitlab-create-protect-branch
- name: gitlab-debug-failed-pipeline
  slug: gitlab-debug-failed-pipeline
- name: gitlab-manage-group-badges
  slug: gitlab-manage-group-badges
- name: gitlab-manage-project-webhooks
  slug: gitlab-manage-project-webhooks
- name: gitlab-review-and-merge-merge-request
  slug: gitlab-review-and-merge-merge-request
- name: gitlab-run-manual-job
  slug: gitlab-run-manual-job
slug: gitlab
solutions:
- description: Core DevOps platform with unlimited repositories, CI/CD, issue tracking, and API access.
  name: GitLab Free
- description: Advanced DevOps with merge request approvals, code owners, and priority support.
  name: GitLab Premium
- description: Enterprise DevOps with security scanning, compliance, and advanced API features.
  name: GitLab Ultimate
- description: Single-tenant SaaS deployment with dedicated infrastructure and enhanced security.
  name: GitLab Dedicated
tags:
- Code
- Developer Tools
- Platform
- Software Development
- Version Control
- GitLab
use_cases:
- description: Automate CI/CD pipeline creation, runner management, and deployment workflows.
  name: DevOps Automation
- description: Programmatically manage issues, milestones, boards, and merge requests.
  name: Project Management
- description: Manage GitLab configuration, groups, projects, and settings through APIs.
  name: Infrastructure as Code
- description: Access vulnerability reports, security scan results, and compliance data.
  name: Security and Compliance
- description: Bulk import projects, users, and data from other platforms.
  name: Migration and Integration
- description: Build custom developer tools, dashboards, and bots for GitLab workflows.
  name: Custom Tooling
- description: Manage Docker images, Kubernetes clusters, and container deployments.
  name: Container Management
- description: Extract project analytics, contribution data, and productivity metrics.
  name: Analytics and Reporting
website: https://about.gitlab.com/
---
