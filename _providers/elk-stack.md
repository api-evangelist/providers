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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: derived
    mcp_server: templated
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.4
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 1137
  human_in_the_loop: 57
  name: Elk Stack Agentic Access
  operation_count: 1873
  slug: elk-stack-agentic-access
  summary_line: 1873 operations · 1137 acting · 57 human-in-the-loop
api_count: 19
apis:
- baseURL: https://api.elastic-cloud.com/api/v1
  baseurl_source: declared
  description: The Elastic Cloud control-plane API creates, scales, upgrades and deletes Elasticsearch and Kibana deployments, and manages accounts, organizations, IAM, traffic filters, extensions, deployment templa
  name: Elastic Cloud API
  slug: elastic-cloud-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Accounts API from Elastic Stack (ELK Stack) — 1 operation(s) for accounts.
  name: Elastic Stack (ELK Stack) Accounts API
  phrasing_intents:
  - id: get-current-account
    intent: View the current Elastic Cloud account
    question: How do I see the details of the account I'm signed in to on Elastic Cloud Enterprise?
  - id: update-current-account
    intent: Replace the current account's trust settings
    question: Can I change which clusters my account trusts by sending a full account update?
  - id: patch-current-account
    intent: Partially update the current account
    question: Is there a way to patch just part of my account settings rather than replacing them?
  phrasing_ops: 3
  slug: elk-stack-accounts-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Actions API from Elastic Stack (ELK Stack) — 1 operation(s) for actions.
  name: Elastic Stack (ELK Stack) Actions API
  phrasing_intents:
  - id: get-actions-connector-oauth-callback-script
    intent: Get the connector OAuth callback script
    question: Where do I get the script used for a connector's OAuth callback?
  phrasing_ops: 1
  slug: elk-stack-actions-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Agent Builder is a set of AI-powered capabilities for developing and interacting with agents that work with your Elasticsearch data. Most users will probably want to integrate with Agent Builder using
  name: Elastic Stack (ELK Stack) agent builder API
  phrasing_intents:
  - id: post-agent-builder-a2a-agentid
    intent: Send an A2A protocol task to an agent
    question: Can an external A2A client hand a task to one of my Agent Builder agents?
  - id: get-agent-builder-a2a-agentid.json
    intent: Get an agent's A2A discovery card
    question: Where do I find the A2A agent card that advertises an Agent Builder agent for discovery?
  - id: get-agent-builder-agents
    intent: List Agent Builder agents
    question: Which agents are defined in my Kibana Agent Builder?
  - id: post-agent-builder-agents
    intent: Create an Agent Builder agent
    question: How do I create a new custom agent in Elastic Agent Builder?
  - id: post-agent-builder-agents-agent-id-consumption
    intent: Get an agent's token consumption per conversation
    question: How many LLM tokens has a given agent used in each conversation?
  - id: delete-agent-builder-agents-id
    intent: Delete an agent
    question: Is deleting an Agent Builder agent permanent?
  - id: get-agent-builder-agents-id
    intent: Get one agent's full definition
    question: What configuration and tool assignments does a specific agent have?
  - id: put-agent-builder-agents-id
    intent: Update an existing agent
    question: Can I change the instructions or tools of an agent I already created?
  phrasing_ops: 41
  slug: elk-stack-agent-builder-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Alerting enables you to define rules, which detect complex conditions within your data. When a condition is met, the rule tracks it as an alert and runs the actions that are defined in the rule. Actio
  name: Elastic Stack (ELK Stack) Alerting API
  phrasing_intents:
  - id: getAlertingHealth
    intent: Check alerting framework health
    question: Is the Kibana alerting framework healthy and able to run rules?
  - id: getRuleTypes
    intent: List available rule types
    question: Which kinds of alerting rules can I create with my privileges?
  - id: delete-alerting-rule-id
    intent: Delete a rule
    question: How do I permanently delete an alerting rule?
  - id: get-alerting-rule-id
    intent: Get a rule's details
    question: What schedule, params and actions does a particular rule have?
  - id: post-alerting-rule-id
    intent: Create a rule
    question: How do I create a new alerting rule under an ID I pick?
  - id: put-alerting-rule-id
    intent: Update an existing rule
    question: How do I change the name, schedule or actions on an existing rule?
  - id: post-alerting-rule-id-disable
    intent: Disable a rule
    question: How do I turn off a rule without deleting it?
  - id: post-alerting-rule-id-enable
    intent: Enable a rule
    question: How do I turn a disabled rule back on?
  phrasing_ops: 23
  slug: elk-stack-alerting-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Alerting V2 is an ES|QL-first alerting API for managing rules, alert actions, and action policies. Use these endpoints to create and manage detection rules, act on alerts, and control when and how not
  name: Elastic Stack (ELK Stack) Alerting V2 API
  phrasing_intents:
  - id: get-alerting-v2-action-policies
    intent: List alerting action policies
    question: Which action policies are set up to route my Kibana alerts to destinations?
  - id: post-alerting-v2-action-policies
    intent: Create an action policy with a generated ID
    question: How do I create a new action policy that sends matching alerts to a destination?
  - id: post-alerting-v2-action-policies-bulk-delete
    intent: Delete several action policies at once
    question: Can I remove a batch of action policies in one request instead of one by one?
  - id: post-alerting-v2-action-policies-bulk-disable
    intent: Disable several action policies at once
    question: Is there a way to turn off a whole set of action policies in a single call?
  - id: post-alerting-v2-action-policies-bulk-enable
    intent: Enable several action policies at once
    question: Can I switch a group of disabled action policies back on together?
  - id: post-alerting-v2-action-policies-bulk-snooze
    intent: Snooze several action policies until a time
    question: Can I silence many action policies until a maintenance window ends?
  - id: post-alerting-v2-action-policies-bulk-unsnooze
    intent: Cancel the snooze on several action policies
    question: Can I end the snooze early on a batch of action policies?
  - id: post-alerting-v2-action-policies-bulk-update-api-key
    intent: Rotate API keys for several action policies
    question: Can I rotate the API keys of many action policies in one request?
  phrasing_ops: 52
  slug: elk-stack-alerting-v2-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The analytics API from Elastic Stack (ELK Stack) — 3 operation(s) for analytics.
  name: Elastic Stack (ELK Stack) Analytics API
  phrasing_intents:
  - id: search-application-get-behavioral-analytics-1
    intent: Get a named behavioral analytics collection
    question: How do I look up one behavioral analytics collection by name?
  - id: search-application-put-behavioral-analytics
    intent: Create a behavioral analytics collection
    question: How do I start tracking search behavior with a new analytics collection?
  - id: search-application-delete-behavioral-analytics
    intent: Delete a behavioral analytics collection
    question: Does deleting an analytics collection also delete its data stream?
  - id: search-application-get-behavioral-analytics
    intent: List all behavioral analytics collections
    question: Which behavioral analytics collections exist on my cluster?
  - id: search-application-post-behavioral-analytics-event
    intent: Record a search behavior event
    question: How do I send a search or click event into an analytics collection?
  phrasing_ops: 5
  slug: elk-stack-analytics-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Adjust APM agent configuration without need to redeploy your application.
  name: Elastic Stack (ELK Stack) APM agent configuration API
  phrasing_intents:
  - id: deleteAgentConfiguration
    intent: Delete an APM agent configuration
    question: How do I remove the central agent configuration for a service?
  - id: getAgentConfigurations
    intent: List all APM agent configurations
    question: How do I see every APM agent configuration defined in Kibana?
  - id: createUpdateAgentConfiguration
    intent: Create or update an APM agent configuration
    question: How do I centrally change settings like sample rate for an APM agent on one service?
  - id: getAgentNameForService
    intent: Find which APM agent a service uses
    question: Which APM agent language is instrumenting a given service?
  - id: getEnvironmentsForService
    intent: List environments available for a service
    question: What environments can I target when configuring an agent for a service?
  - id: searchSingleConfiguration
    intent: Look up an agent's config and mark it applied
    question: How does an APM agent fetch its configuration and report that it applied it?
  - id: getSingleAgentConfiguration
    intent: Get the agent configuration for a service
    question: How do I view the agent settings configured for one service in a specific environment?
  phrasing_ops: 7
  slug: elk-stack-apm-agent-configuration-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Configure APM agent keys to authorize requests from APM agents to the APM Server.
  name: Elastic Stack (ELK Stack) APM agent keys API
  phrasing_intents:
  - id: createAgentKey
    intent: Create an APM agent API key
    question: What's needed to create an API key my APM agents can use to send data?
  phrasing_ops: 1
  slug: elk-stack-apm-agent-keys-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Annotate visualizations in the APM app with significant events. Annotations enable you to easily see how events are impacting the performance of your applications.
  name: Elastic Stack (ELK Stack) APM annotations API
  phrasing_intents:
  - id: createAnnotation
    intent: Annotate an APM service
    question: How do I mark a deployment on an APM service's charts?
  - id: getAnnotation
    intent: Search an APM service's annotations
    question: What deployment annotations exist for an APM service?
  phrasing_ops: 2
  slug: elk-stack-apm-annotations-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Create APM fleet server schema.
  name: Elastic Stack (ELK Stack) APM server schema API
  phrasing_intents:
  - id: saveApmServerSchema
    intent: Save the APM Server schema for Fleet
    question: How do I store the APM Server configuration schema used by the Fleet APM integration?
  phrasing_ops: 1
  slug: elk-stack-apm-server-schema-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Configure APM source maps. A source map allows minified files to be mapped back to original source code--allowing you to maintain the speed advantage of minified code, without losing the ability to qu
  name: Elastic Stack (ELK Stack) APM sourcemaps API
  phrasing_intents:
  - id: getSourceMaps
    intent: List uploaded APM source maps
    question: Which source maps have I already uploaded to APM?
  - id: uploadSourceMap
    intent: Upload a source map for a service version
    question: How do I upload a JavaScript source map so APM can un-minify my RUM stack traces?
  - id: deleteSourceMap
    intent: Delete an uploaded source map
    question: How do I remove a source map I uploaded to APM by mistake?
  phrasing_ops: 3
  slug: elk-stack-apm-sourcemaps-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Authentication API from Elastic Stack (ELK Stack) — 12 operation(s) for authentication.
  name: Elastic Stack (ELK Stack) Authentication API
  phrasing_intents:
  - id: get-authentication-info
    intent: Get my authentication info
    question: Am I currently holding elevated permissions in Elastic Cloud Enterprise?
  - id: login
    intent: Log in with a username and password
    question: How do I sign in to ECE with a username and password?
  - id: logout
    intent: Log out of the current session
    question: How do I end my current ECE session?
  - id: refresh-token
    intent: Refresh my authentication token
    question: Can I get a new auth token before the current one expires?
  - id: get-api-keys
    intent: List API keys I can see
    question: Which API keys exist that I am allowed to view?
  - id: create-api-key
    intent: Create an API key
    question: How do I create a new API key for automation?
  - id: delete-api-keys
    intent: Delete several of my API keys
    question: Can I revoke a batch of API keys in one call?
  - id: get-users-api-keys
    intent: List API keys of all users (deprecated)
    question: Can an admin see the API keys belonging to every user?
  phrasing_ops: 18
  slug: elk-stack-authentication-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The BillingCostsAnalysis API from Elastic Stack (ELK Stack) — 6 operation(s) for billingcostsanalysis.
  name: Elastic Stack (ELK Stack) Billing Costs Analysis API
  phrasing_intents:
  - id: get-costs-overview
    intent: Get an organization's cost overview
    question: How much has my Elastic Cloud organization spent so far?
  - id: get-costs-charts
    intent: Get an organization's usage charts
    question: What does our organization-wide usage look like over time?
  - id: get-costs-deployments
    intent: Get costs broken down by deployment
    question: Which of our deployments costs the most?
  - id: get-costs-charts-by-deployment
    intent: Get usage charts for one deployment
    question: How has usage for a single deployment trended over time?
  - id: get-costs-items-by-deployment
    intent: Get itemized costs for one deployment
    question: What line items make up the bill for one deployment?
  - id: get-costs-items
    intent: Get itemized costs for an organization
    question: What individual line items make up our organization's bill?
  phrasing_ops: 6
  slug: elk-stack-billingcostsanalysis-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: 'Cases are used to open and track issues. You can add assignees and tags to your cases, set their severity and status, and add alerts, comments, and visualizations. You can also send cases to external '
  name: Elastic Stack (ELK Stack) Cases API
  phrasing_intents:
  - id: deleteCaseDefaultSpace
    intent: Delete one or more cases
    question: How do I permanently delete several Kibana cases at once?
  - id: updateCaseDefaultSpace
    intent: Update fields on existing cases
    question: How do I close a case or change its status programmatically?
  - id: createCaseDefaultSpace
    intent: Open a new case
    question: How do I open a new security or observability case in Kibana from a script?
  - id: findCasesDefaultSpace
    intent: Search and filter cases
    question: Which open cases are assigned to me?
  - id: getCaseDefaultSpace
    intent: Get a case's details
    question: What's the current status and description of a specific case?
  - id: getCaseAlertsDefaultSpace
    intent: List alerts attached to a case
    question: Which detection alerts have been attached to this case?
  - id: deleteCaseCommentsDefaultSpace
    intent: Delete every comment and alert on a case
    question: How do I wipe all comments and attached alerts from a case in one go?
  - id: updateCaseCommentDefaultSpace
    intent: Edit an existing case comment or alert
    question: How do I fix a typo in a comment I already posted on a case?
  phrasing_ops: 29
  slug: elk-stack-cases-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The cat API from Elastic Stack (ELK Stack) — 45 operation(s) for cat.
  name: Elastic Stack (ELK Stack) Cat API
  phrasing_intents:
  - id: cat-aliases
    intent: List all index aliases in the cluster
    question: What index aliases exist across my Elasticsearch cluster?
  - id: cat-aliases-1
    intent: Show details for specific index aliases
    question: Which indices does a particular alias point to?
  - id: cat-allocation
    intent: Show shard allocation and disk use per node
    question: How many shards are allocated to each data node right now?
  - id: cat-allocation-1
    intent: Show shard allocation for specific nodes
    question: How much disk does one particular node use for its shards?
  - id: cat-circuit-breaker
    intent: Show circuit breaker statistics
    question: Are any circuit breakers tripping in my cluster?
  - id: cat-circuit-breaker-1
    intent: Show stats for matching circuit breakers
    question: Can I look at only the request or fielddata circuit breaker?
  - id: cat-component-templates
    intent: List component templates in the cluster
    question: Which component templates are defined in my cluster?
  - id: cat-component-templates-1
    intent: Show component templates matching a name
    question: Is there a component template with a particular name?
  phrasing_ops: 47
  slug: elk-stack-cat-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The ccr API from Elastic Stack (ELK Stack) — 12 operation(s) for ccr.
  name: Elastic Stack (ELK Stack) Ccr API
  phrasing_intents:
  - id: ccr-get-auto-follow-pattern-1
    intent: View one auto-follow pattern
    question: What settings does a specific cross-cluster replication auto-follow pattern use?
  - id: ccr-put-auto-follow-pattern
    intent: Create or update an auto-follow pattern
    question: How do I automatically replicate new indices from a remote cluster as they get created?
  - id: ccr-delete-auto-follow-pattern
    intent: Delete an auto-follow pattern
    question: How do I remove an auto-follow pattern I no longer need for cross-cluster replication?
  - id: ccr-follow
    intent: Create a follower index for a leader index
    question: How do I start replicating one specific index from a remote Elasticsearch cluster?
  - id: ccr-follow-info
    intent: Get follower index configuration and status
    question: Is my follower index currently active or paused, and which leader does it track?
  - id: ccr-follow-stats
    intent: Get shard-level stats for a follower index
    question: How far behind the leader is my follower index on each shard?
  - id: ccr-forget-follower
    intent: Remove follower retention leases from a leader
    question: How do I clean up retention leases a follower left on the leader index after unfollowing failed?
  - id: ccr-get-auto-follow-pattern
    intent: List all auto-follow patterns
    question: Which auto-follow patterns are configured on this cluster?
  phrasing_ops: 14
  slug: elk-stack-ccr-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The cluster API from Elastic Stack (ELK Stack) — 35 operation(s) for cluster.
  name: Elastic Stack (ELK Stack) Cluster API
  phrasing_intents:
  - id: cluster-allocation-explain
    intent: Explain why a shard is unassigned or placed
    question: Why is one of my Elasticsearch shards stuck unassigned?
  - id: cluster-allocation-explain-1
    intent: Explain a shard allocation with a request body
    question: How do I send the index and shard number in a JSON body to get an allocation explanation?
  - id: cluster-post-voting-config-exclusions
    intent: Exclude master nodes from voting
    question: How do I safely remove master-eligible nodes from the voting configuration before shutting them down?
  - id: cluster-delete-voting-config-exclusions
    intent: Clear the voting configuration exclusion list
    question: How do I clear the voting exclusions after I've finished removing master nodes?
  - id: cluster-get-settings
    intent: Get cluster-wide settings
    question: What persistent and transient settings have been set on my cluster?
  - id: cluster-put-settings
    intent: Update dynamic cluster settings
    question: How do I change a dynamic cluster setting without restarting nodes?
  - id: cluster-health
    intent: Check overall cluster health
    question: Is my Elasticsearch cluster green, yellow or red right now?
  - id: cluster-health-1
    intent: Check health of specific indices or data streams
    question: What's the health status of just one index or data stream rather than the whole cluster?
  phrasing_ops: 40
  slug: elk-stack-cluster-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Comments API from Elastic Stack (ELK Stack) — 2 operation(s) for comments.
  name: Elastic Stack (ELK Stack) Comments API
  phrasing_intents:
  - id: list-comment
    intent: List comments on a resource
    question: What comments have been left on a deployment or other resource?
  - id: create-comment
    intent: Post a comment on a resource
    question: How do I leave a note on a platform resource for my team?
  - id: get-comment
    intent: Get a single comment
    question: How do I read one specific comment on a resource?
  - id: update-comment
    intent: Edit a comment
    question: How do I change the text of a comment I already posted?
  - id: delete-comment
    intent: Delete a comment
    question: How do I remove a comment from a resource?
  phrasing_ops: 5
  slug: elk-stack-comments-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The connector API from Elastic Stack (ELK Stack) — 24 operation(s) for connector.
  name: Elastic Stack (ELK Stack) Connector API
  phrasing_intents:
  - id: connector-check-in
    intent: Record a connector heartbeat
    question: How does a self-managed connector tell Elasticsearch it is still alive?
  - id: connector-get
    intent: Get a connector's details
    question: What configuration, status and index does a particular connector have?
  - id: connector-put
    intent: Create or update a connector with a chosen ID
    question: Can I create a connector under an ID I pick myself, or overwrite the one at that ID?
  - id: connector-delete
    intent: Delete a connector
    question: Does deleting a connector also remove its data index and API keys?
  - id: connector-list
    intent: List connectors
    question: What connectors are configured in my Elasticsearch cluster?
  - id: connector-put-1
    intent: Create or update a connector via PUT without an ID
    question: Can I PUT a connector to the collection path and let Elasticsearch generate its ID?
  - id: connector-post
    intent: Create a connector with a generated ID
    question: How do I add a new connector that syncs third-party content into an Elasticsearch index?
  - id: connector-sync-job-cancel
    intent: Cancel a connector sync job
    question: How can I stop a connector sync that is currently running?
  phrasing_ops: 30
  slug: elk-stack-connector-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Connectors provide a central place to store connection information for services and integrations with Elastic or third party systems. Alerting rules can use connectors to run actions when rule conditi
  name: Elastic Stack (ELK Stack) Connectors API
  phrasing_intents:
  - id: get-actions-connector-types
    intent: List available connector types
    question: What kinds of connectors can I set up in Kibana?
  - id: get-actions-connector-oauth-callback
    intent: Complete a connector's OAuth callback
    question: How does a connector exchange the OAuth authorization code for tokens?
  - id: get-actions-connector-connectorid-oauth-start
    intent: Start OAuth authorization for a connector
    question: How do I kick off the OAuth sign-in for a connector?
  - id: delete-actions-connector-id
    intent: Delete a connector
    question: How do I delete a connector I no longer use?
  - id: get-actions-connector-id
    intent: Get a connector's details
    question: How do I look up the configuration of one connector?
  - id: post-actions-connector-id
    intent: Create a connector with a chosen ID
    question: How do I create a new connector in Kibana with my own ID?
  - id: put-actions-connector-id
    intent: Update a connector
    question: How do I rename or reconfigure an existing connector?
  - id: post-actions-connector-id-execute
    intent: Run a connector
    question: How do I test a connector by running it?
  phrasing_ops: 9
  slug: elk-stack-connectors-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: '> This documentation is temporarily hosted at a separate location. > > **[View the full Dashboards API reference →](https://elastic.github.io/dashboards-api-spec/dashboards#tag/Dashboards)**'
  name: Elastic Stack (ELK Stack) Dashboards API
  phrasing_intents:
  - id: search-dashboards
    intent: Search Kibana dashboards
    question: What dashboards do I have in Kibana?
  - id: create-dashboard
    intent: Create a new dashboard
    question: How do I create a new Kibana dashboard through the API?
  - id: get-dashboard
    intent: Get a dashboard
    question: How do I fetch the definition of a single dashboard?
  - id: upsert-dashboard
    intent: Create or replace a dashboard by ID
    question: How do I update an existing dashboard or create it if the ID is new?
  - id: delete-dashboard
    intent: Delete a dashboard
    question: How do I delete a dashboard I no longer need?
  phrasing_ops: 5
  slug: elk-stack-dashboards-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The data stream API from Elastic Stack (ELK Stack) — 14 operation(s) for data stream.
  name: Elastic Stack (ELK Stack) data stream API
  phrasing_intents:
  - id: indices-get-data-stream-1
    intent: Get details of named data streams
    question: What backing indices and template does a particular data stream use?
  - id: indices-create-data-stream
    intent: Create a data stream
    question: How do I create a data stream by hand instead of waiting for the first document?
  - id: indices-delete-data-stream
    intent: Delete data streams and their backing indices
    question: How do I delete a data stream along with all its backing indices?
  - id: indices-data-streams-stats
    intent: Get stats for all data streams
    question: How much storage are my data streams using overall?
  - id: indices-data-streams-stats-1
    intent: Get stats for specific data streams
    question: How big is one particular data stream and how many backing indices does it have?
  - id: indices-get-data-lifecycle
    intent: Get a data stream's lifecycle settings
    question: What retention period is configured on a data stream's lifecycle?
  - id: indices-put-data-lifecycle
    intent: Set retention and downsampling on a data stream
    question: How do I keep only 30 days of data in a data stream?
  - id: indices-get-data-stream-options
    intent: Get a data stream's options
    question: Is the failure store enabled on my data stream?
  phrasing_ops: 21
  slug: elk-stack-data-stream-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Data stream APIs enable you to manage data streams, which are collections of indices that share the same index template and are managed as a single unit for time-series data.
  name: Elastic Stack (ELK Stack) Data streams API
  phrasing_intents:
  - id: get-fleet-data-streams
    intent: List Fleet-managed data streams
    question: Which data streams is Fleet managing and how large are they?
  - id: get-fleet-epm-data-streams
    intent: List data streams from installed integration packages
    question: What data streams did my installed integration packages create?
  phrasing_ops: 2
  slug: elk-stack-data-streams-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Data view APIs enable you to manage data views, formerly known as Kibana index patterns.
  name: Elastic Stack (ELK Stack) data views API
  phrasing_intents:
  - id: getAllDataViewsDefault
    intent: List all data views in a Kibana space
    question: What data views are available in my Kibana space?
  - id: createDataViewDefaultw
    intent: Create a data view
    question: How do I create a data view over my logs indices in Kibana?
  - id: deleteDataViewDefault
    intent: Delete a data view
    question: Can a deleted data view be recovered?
  - id: getDataViewDefault
    intent: Get a data view
    question: What index pattern and fields does a particular data view use?
  - id: updateDataViewDefault
    intent: Update a data view
    question: Can I change the index pattern of an existing data view?
  - id: updateFieldsMetadataDefault
    intent: Set labels and formats on data view fields
    question: Can I give a field a custom label or description in a data view?
  - id: createRuntimeFieldDefault
    intent: Add a new runtime field to a data view
    question: How do I add a computed field to a data view without reindexing?
  - id: createUpdateRuntimeFieldDefault
    intent: Create or replace a runtime field
    question: Can I upsert a runtime field so it's replaced if it already exists?
  phrasing_ops: 15
  slug: elk-stack-data-views-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Deployments API from Elastic Stack (ELK Stack) — 58 operation(s) for deployments.
  name: Elastic Stack (ELK Stack) Deployments API
  phrasing_intents:
  - id: list-deployments
    intent: List all deployments
    question: What deployments do I have running in Elastic Cloud Enterprise?
  - id: create-deployment
    intent: Create a new deployment
    question: How do I spin up a new Elastic deployment?
  - id: resync-deployments
    intent: Resync the search index for all deployments
    question: How do I rebuild the deployment search index across every deployment?
  - id: search-deployments
    intent: Search deployments with a query
    question: How do I find deployments that match a specific query?
  - id: search-eligible-remote-clusters
    intent: Find deployments eligible as remote clusters
    question: Which deployments can serve as remote clusters for a given Elasticsearch version?
  - id: get-deployment
    intent: Get a deployment's details
    question: How do I look up the full details of one deployment?
  - id: update-deployment
    intent: Update a deployment's configuration
    question: How do I change the configuration of an existing deployment?
  - id: delete-deployment
    intent: Delete a deployment and its resources
    question: How do I permanently delete a deployment along with all its resources?
  phrasing_ops: 72
  slug: elk-stack-deployments-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The DeploymentsTrafficFilter API from Elastic Stack (ELK Stack) — 8 operation(s) for deploymentstrafficfilter.
  name: Elastic Stack (ELK Stack) Deployments Traffic Filter API
  phrasing_intents:
  - id: get-traffic-filter-deployment-ruleset-associations
    intent: List rulesets applied to a deployment
    question: Which traffic filter rulesets are attached to my Elastic Cloud deployment?
  - id: get-traffic-filter-claimed-link-ids
    intent: List claimed private link IDs
    question: Which private link IDs has my organization claimed for traffic filtering?
  - id: claim-traffic-filter-link-id
    intent: Claim a private link ID
    question: How do I claim ownership of a private link endpoint ID for my organization?
  - id: unclaim-traffic-filter-link-id
    intent: Release a claimed private link ID
    question: How do I give up ownership of a link ID I claimed earlier?
  - id: get-traffic-filter-rulesets
    intent: List traffic filter rulesets
    question: What IP and private link traffic filter rulesets do I have in Elastic Cloud?
  - id: create-traffic-filter-ruleset
    intent: Create a traffic filter ruleset
    question: How do I restrict access to my deployments to a set of allowed IP addresses?
  - id: get-traffic-filter-ruleset
    intent: Get a traffic filter ruleset
    question: How do I see the rules inside one traffic filter ruleset?
  - id: update-traffic-filter-ruleset
    intent: Update a traffic filter ruleset
    question: How do I add a new allowed IP range to an existing ruleset?
  phrasing_ops: 12
  slug: elk-stack-deploymentstrafficfilter-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The DeploymentTemplates API from Elastic Stack (ELK Stack) — 2 operation(s) for deploymenttemplates.
  name: Elastic Stack (ELK Stack) Deployment Templates API
  phrasing_intents:
  - id: get-deployment-templates-v2
    intent: List deployment templates in a region
    question: What deployment templates are available in a region?
  - id: create-deployment-template-v2
    intent: Create a deployment template
    question: How do I create a new deployment template?
  - id: get-deployment-template-v2
    intent: Get a deployment template
    question: What does a particular deployment template define?
  - id: set-deployment-template-v2
    intent: Create or update a deployment template by ID
    question: Can I overwrite an existing deployment template by its ID?
  - id: delete-deployment-template-v2
    intent: Delete a deployment template
    question: How do I remove a deployment template I no longer offer?
  phrasing_ops: 5
  slug: elk-stack-deploymenttemplates-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The document API from Elastic Stack (ELK Stack) — 19 operation(s) for document.
  name: Elastic Stack (ELK Stack) Document API
  phrasing_intents:
  - id: bulk-1
    intent: Run bulk document actions via PUT on any index
    question: Can I send a PUT to the cluster-wide bulk endpoint with actions naming their own indices?
  - id: bulk
    intent: Bulk index, update or delete documents
    question: How do I index thousands of documents in one request instead of one call each?
  - id: bulk-3
    intent: Run bulk document actions via PUT on one index
    question: Can I PUT a bulk batch scoped to one index so the actions don't repeat the index name?
  - id: bulk-2
    intent: Bulk write documents into a single index
    question: How do I bulk load documents into one specific index without naming it on every line?
  - id: create
    intent: Create a document only if its ID is new (PUT)
    question: How do I add a document with a specific ID and fail if that ID already exists?
  - id: create-1
    intent: Create a document only if its ID is new (POST)
    question: Can I POST to the _create endpoint so a duplicate document ID is rejected rather than overwritten?
  - id: get
    intent: Get a document by its ID
    question: How do I fetch a single document and its source when I know the index and ID?
  - id: index
    intent: Index or replace a document with PUT
    question: How do I save a JSON document under my own ID, overwriting it if it exists?
  phrasing_ops: 33
  slug: elk-stack-document-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Elastic Agent actions APIs enable you to manage actions performed on Elastic Agents, including agent reassignment, diagnostics collection, enrollment management, upgrades, and bulk operations for agen
  name: Elastic Stack (ELK Stack) Elastic Agent actions API
  phrasing_intents:
  - id: post-fleet-agents-agentid-actions
    intent: Send a custom action to one Fleet agent
    question: Can I push a custom action to a single Elastic Agent?
  - id: post-fleet-agents-agentid-reassign
    intent: Move one agent to another policy
    question: How do I move a single Elastic Agent to a different agent policy?
  - id: post-fleet-agents-agentid-remove-collector
    intent: Remove one OpAMP collector from Fleet
    question: How do I take a single OpAMP collector off the Fleet agents list?
  - id: post-fleet-agents-agentid-request-diagnostics
    intent: Request diagnostics from one agent
    question: How do I collect a diagnostics bundle from a misbehaving Elastic Agent?
  - id: post-fleet-agents-agentid-rollback
    intent: Roll back one agent to its previous version
    question: Can I undo an Elastic Agent upgrade on one host?
  - id: post-fleet-agents-agentid-unenroll
    intent: Unenroll one agent from Fleet
    question: How do I unenroll a single Elastic Agent from Fleet?
  - id: post-fleet-agents-agentid-upgrade
    intent: Upgrade one agent to a new version
    question: How do I upgrade a single Elastic Agent to a specific version?
  - id: get-fleet-agents-action-status
    intent: Check progress of recent agent actions
    question: Did my recent Fleet upgrade or reassign actions finish successfully?
  phrasing_ops: 16
  slug: elk-stack-elastic-agent-actions-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Elastic Agent binary download sources APIs enable you to manage download sources for Elastic Agent binaries, including creating, updating, and deleting custom download sources for agent binaries.
  name: Elastic Stack (ELK Stack) Elastic Agent binary download sources API
  phrasing_intents:
  - id: get-fleet-agent-download-sources
    intent: List Elastic Agent binary download sources
    question: Where does Fleet download Elastic Agent binaries from?
  - id: post-fleet-agent-download-sources
    intent: Add an agent binary download source
    question: Can I point Fleet at our own mirror for agent binaries in an air-gapped network?
  - id: delete-fleet-agent-download-sources-sourceid
    intent: Delete an agent binary download source
    question: How do I remove a download source we no longer use?
  - id: get-fleet-agent-download-sources-sourceid
    intent: Get one agent binary download source
    question: What host and proxy does a particular download source use?
  - id: put-fleet-agent-download-sources-sourceid
    intent: Update an agent binary download source
    question: Can I change the host URL of an existing download source?
  phrasing_ops: 5
  slug: elk-stack-elastic-agent-binary-download-sources-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Elastic Agent policies APIs enable you to manage agent policies, including creating, updating, and deleting policies, as well as to retrieve agent policy outputs, manifests, and auto-upgrade status in
  name: Elastic Stack (ELK Stack) Elastic Agent policies API
  phrasing_intents:
  - id: get-fleet-agent-policies
    intent: List Fleet agent policies
    question: How do I list all the agent policies in Fleet?
  - id: post-fleet-agent-policies
    intent: Create a Fleet agent policy
    question: How do I create a new agent policy in Fleet?
  - id: post-fleet-agent-policies-bulk-get
    intent: Fetch several agent policies by ID at once
    question: Can I retrieve a batch of agent policies in one call by their IDs?
  - id: get-fleet-agent-policies-agentpolicyid
    intent: Get one agent policy
    question: How do I look up a single Fleet agent policy by its ID?
  - id: put-fleet-agent-policies-agentpolicyid
    intent: Update an agent policy
    question: How do I rename an existing agent policy or move it to another namespace?
  - id: get-fleet-agent-policies-agentpolicyid-auto-upgrade-agents-status
    intent: Check auto-upgrade status of a policy's agents
    question: How far along is the automatic upgrade of agents on one policy?
  - id: post-fleet-agent-policies-agentpolicyid-copy
    intent: Duplicate an agent policy
    question: Can I clone an existing agent policy under a new name?
  - id: get-fleet-agent-policies-agentpolicyid-download
    intent: Download an agent policy file
    question: How do I download an agent policy as a file for a standalone Elastic Agent?
  phrasing_ops: 14
  slug: elk-stack-elastic-agent-policies-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Enables you to retrieve status information about Elastic Agents, including health summaries and operational status.
  name: Elastic Stack (ELK Stack) Elastic Agent status API
  phrasing_intents:
  - id: get-fleet-agent-status
    intent: Summarize agent statuses for a policy
    question: How many of my Elastic Agents are online, offline or unhealthy?
  phrasing_ops: 1
  slug: elk-stack-elastic-agent-status-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Elastic Agents APIs enable you to manage Elastic Agents, including retrieving agent information, managing agent lifecycle, handling file uploads, and initiating agent setup.
  name: Elastic Stack (ELK Stack) Elastic Agents API
  phrasing_intents:
  - id: get-fleet-agent-status-data
    intent: Check which data streams agents are sending to
    question: Is my newly enrolled agent actually sending data yet?
  - id: get-fleet-agents
    intent: List Fleet agents
    question: Which Elastic Agents are enrolled in Fleet?
  - id: post-fleet-agents
    intent: Find agents by action IDs
    question: Which agents were targeted by a particular Fleet action?
  - id: delete-fleet-agents-agentid
    intent: Delete a Fleet agent
    question: How do I remove an agent record from Fleet?
  - id: get-fleet-agents-agentid
    intent: Get a Fleet agent
    question: What status and policy does a specific agent have?
  - id: put-fleet-agents-agentid
    intent: Update an agent's tags or metadata
    question: Can I add tags to an enrolled agent?
  - id: get-fleet-agents-agentid-effective-config
    intent: Get an agent's effective configuration
    question: What configuration is an agent actually running with?
  - id: post-fleet-agents-agentid-migrate
    intent: Migrate one agent to another cluster
    question: Can I move a single agent to a different Fleet cluster?
  phrasing_ops: 18
  slug: elk-stack-elastic-agents-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Elastic Package Manager (EPM) APIs enable you to manage packages and integrations, including installing, updating, and uninstalling packages, managing custom integrations, and handling package assets.
  name: Elastic Stack (ELK Stack) Elastic Package Manager (EPM) API
  phrasing_intents:
  - id: post-fleet-epm-bulk-assets
    intent: Fetch several Kibana saved objects by asset ID
    question: Can I pull the definitions of several integration assets like dashboards and visualizations in one call?
  - id: get-fleet-epm-categories
    intent: List integration categories
    question: What categories are Fleet integrations grouped into, like security or observability?
  - id: post-fleet-epm-custom-integrations
    intent: Create a custom integration
    question: How do I build my own custom Fleet integration with its own datasets?
  - id: put-fleet-epm-custom-integrations-pkgname
    intent: Update a custom integration's readme and categories
    question: Can I change the README text of a custom integration I already built?
  - id: get-fleet-epm-packages
    intent: Browse available integration packages
    question: What integrations are available in the Fleet package registry?
  - id: post-fleet-epm-packages
    intent: Install an integration from an uploaded archive
    question: How do I install an integration package from a zip file I have locally instead of the registry?
  - id: post-fleet-epm-packages-bulk
    intent: Install several integration packages at once
    question: Can I install a whole list of integrations from the registry in a single request?
  - id: post-fleet-epm-packages-bulk-namespace-customization
    intent: Toggle namespace customization for many packages
    question: Can I turn on namespace-level customization for several integrations at once?
  phrasing_ops: 36
  slug: elk-stack-elastic-package-manager-epm-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The enrich API from Elastic Stack (ELK Stack) — 4 operation(s) for enrich.
  name: Elastic Stack (ELK Stack) Enrich API
  phrasing_intents:
  - id: enrich-get-policy
    intent: Get an enrich policy by name
    question: What match fields and source indices does a particular enrich policy use?
  - id: enrich-put-policy
    intent: Create an enrich policy
    question: How do I create an enrich policy to add lookup data to incoming documents?
  - id: enrich-delete-policy
    intent: Delete an enrich policy and its index
    question: How do I remove an enrich policy I no longer use?
  - id: enrich-execute-policy
    intent: Run an enrich policy to build its index
    question: How do I build or refresh the enrich index after creating an enrich policy?
  - id: enrich-get-policy-1
    intent: List all enrich policies
    question: Which enrich policies exist on my cluster?
  - id: enrich-stats
    intent: Get enrich coordinator stats
    question: Which enrich policies are executing right now?
  phrasing_ops: 6
  slug: elk-stack-enrich-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The eql API from Elastic Stack (ELK Stack) — 3 operation(s) for eql.
  name: Elastic Stack (ELK Stack) Eql API
  phrasing_intents:
  - id: eql-get
    intent: Get results of an async EQL search
    question: How do I fetch the results of an EQL search that ran asynchronously?
  - id: eql-delete
    intent: Delete an async EQL search and its results
    question: How do I cancel and clean up an async EQL search?
  - id: eql-get-status
    intent: Check the status of an async EQL search
    question: Is my async EQL search still running?
  - id: eql-search
    intent: Run an EQL query (GET)
    question: How do I run an Event Query Language query over an index with a GET request?
  - id: eql-search-1
    intent: Run an EQL query (POST)
    question: What is the POST form of an EQL search for detecting event sequences?
  phrasing_ops: 5
  slug: elk-stack-eql-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The esql API from Elastic Stack (ELK Stack) — 12 operation(s) for esql.
  name: Elastic Stack (ELK Stack) Esql API
  phrasing_intents:
  - id: esql-async-query
    intent: Run an ES|QL query asynchronously
    question: How do I run a long ES|QL query in the background and fetch results later?
  - id: esql-async-query-get
    intent: Get results of an async ES|QL query
    question: Has my async ES|QL query finished yet?
  - id: esql-async-query-delete
    intent: Cancel or delete an async ES|QL query
    question: How do I cancel an async ES|QL query that's still running?
  - id: esql-async-query-stop
    intent: Stop an async ES|QL query and keep partial results
    question: Can I stop an async ES|QL query and get whatever results it has so far?
  - id: esql-get-data-source-1
    intent: Get ES|QL data sources by name
    question: How do I look up a specific ES|QL federation data source by name?
  - id: esql-put-data-source
    intent: Create or update an ES|QL data source
    question: How do I register an external data source for ES|QL data federation?
  - id: esql-delete-data-source
    intent: Delete ES|QL data sources
    question: How do I remove an ES|QL federation data source?
  - id: esql-get-dataset-1
    intent: Get ES|QL datasets by name
    question: How do I look up a particular ES|QL dataset by name?
  phrasing_ops: 19
  slug: elk-stack-esql-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Extensions API from Elastic Stack (ELK Stack) — 2 operation(s) for extensions.
  name: Elastic Stack (ELK Stack) Extensions API
  phrasing_intents:
  - id: list-extensions
    intent: List available deployment extensions
    question: Which plugins and bundles have been registered as extensions for my deployments?
  - id: create-extension
    intent: Register a new deployment extension
    question: How do I register a custom plugin or bundle for my Elasticsearch deployments?
  - id: get-extension
    intent: Get a deployment extension
    question: How do I see the details of one extension I registered?
  - id: update-extension
    intent: Update an extension's details
    question: Can I change the name, description or download URL of an existing extension?
  - id: upload-extension
    intent: Upload the archive for an extension
    question: How do I upload the zip file for an extension I already created?
  - id: delete-extension
    intent: Delete a deployment extension
    question: How do I remove an extension I no longer need?
  phrasing_ops: 6
  slug: elk-stack-extensions-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The features API from Elastic Stack (ELK Stack) — 2 operation(s) for features.
  name: Elastic Stack (ELK Stack) Features API
  phrasing_intents:
  - id: features-get-features
    intent: List features that can be snapshotted
    question: Which feature states can I include in a snapshot?
  - id: features-reset-features
    intent: Reset all feature system indices
    question: How do I wipe the state stored in system indices on a test cluster?
  phrasing_ops: 2
  slug: elk-stack-features-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Fleet agentless policies API from Elastic Stack (ELK Stack) — 4 operation(s) for fleet agentless policies.
  name: Elastic Stack (ELK Stack) Fleet agentless policies API
  phrasing_intents:
  - id: get-fleet-agentless-policies
    intent: List managed integrations (deprecated endpoint)
    question: Which agentless managed integrations are running in Fleet, via the old agentless_policies endpoint?
  - id: post-fleet-agentless-policies
    intent: Create an agentless policy (deprecated endpoint)
    question: How do I create an agentless integration through the legacy agentless_policies route?
  - id: post-fleet-agentless-policies-upgrade
    intent: Bulk upgrade agentless policies (deprecated)
    question: How do I upgrade several agentless integrations to their installed package version at once?
  - id: post-fleet-agentless-policies-upgrade-dryrun
    intent: Preview an agentless policy upgrade (deprecated)
    question: Can I preview what an agentless integration upgrade would change without applying it?
  - id: delete-fleet-agentless-policies-policyid
    intent: Delete an agentless policy (deprecated endpoint)
    question: How do I remove an agentless integration using the deprecated agentless_policies path?
  - id: get-fleet-agentless-policies-policyid
    intent: Get one agentless policy (deprecated endpoint)
    question: How do I view a single agentless integration through the legacy agentless_policies route?
  - id: put-fleet-agentless-policies-policyid
    intent: Replace an agentless policy (deprecated endpoint)
    question: Does updating an agentless policy clear optional fields I leave out of the request?
  phrasing_ops: 7
  slug: elk-stack-fleet-agentless-policies-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The fleet API from Elastic Stack (ELK Stack) — 4 operation(s) for fleet.
  name: Elastic Stack (ELK Stack) Fleet API
  phrasing_intents:
  - id: fleet-global-checkpoints
    intent: Get an index's global checkpoints
    question: What are the current global checkpoints for an index Fleet server reads from?
  - id: fleet-msearch
    intent: Run a Fleet multi search via GET, no index
    question: Can I send several Fleet searches in one GET request without naming an index in the path?
  - id: fleet-msearch-1
    intent: Run a Fleet multi search via POST, no index
    question: How do I POST a batch of Fleet searches without an index in the URL?
  - id: fleet-msearch-2
    intent: Run a Fleet multi search via GET on an index
    question: Can I run several Fleet searches against one default index using GET?
  - id: fleet-msearch-3
    intent: Run a Fleet multi search via POST on an index
    question: How do I POST a batch of Fleet searches against a specific index?
  - id: fleet-search
    intent: Run a Fleet search via GET
    question: Can I run a GET search that only executes after a given checkpoint is visible?
  - id: fleet-search-1
    intent: Run a Fleet search via POST
    question: How do I POST a Fleet search with a Query DSL body that waits for a checkpoint?
  phrasing_ops: 7
  slug: elk-stack-fleet-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet cloud connectors APIs enable you to manage Fleet cloud connectors, including creating, updating, and deleting cloud connector configurations for Fleet integrations.
  name: Elastic Stack (ELK Stack) Fleet cloud connectors API
  phrasing_intents:
  - id: get-fleet-cloud-connectors
    intent: List Fleet cloud connectors
    question: Which cloud connectors are set up in Fleet?
  - id: post-fleet-cloud-connectors
    intent: Create a Fleet cloud connector
    question: How do I connect Fleet to my AWS or Azure account with a cloud connector?
  - id: delete-fleet-cloud-connectors-cloudconnectorid
    intent: Delete a Fleet cloud connector
    question: How do I remove a cloud connector I no longer use?
  - id: get-fleet-cloud-connectors-cloudconnectorid
    intent: Get a Fleet cloud connector
    question: How do I look up the configuration of one cloud connector?
  - id: put-fleet-cloud-connectors-cloudconnectorid
    intent: Update a Fleet cloud connector
    question: How do I rename an existing cloud connector?
  - id: get-fleet-cloud-connectors-cloudconnectorid-usage
    intent: See which policies use a cloud connector
    question: Which package policies depend on a given cloud connector?
  phrasing_ops: 6
  slug: elk-stack-fleet-cloud-connectors-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet enrollment API keys APIs enable you to manage enrollment API keys for Fleet, including creating, retrieving, and revoking API keys used for agent enrollment.
  name: Elastic Stack (ELK Stack) Fleet enrollment API keys API
  phrasing_intents:
  - id: get-fleet-enrollment-api-keys
    intent: List Fleet enrollment API keys
    question: Which enrollment tokens exist for enrolling Elastic Agents?
  - id: post-fleet-enrollment-api-keys
    intent: Create a Fleet enrollment API key
    question: How do I create an enrollment token so new agents join a specific policy?
  - id: post-fleet-enrollment-api-keys-bulk-delete
    intent: Bulk revoke or delete enrollment API keys
    question: How do I revoke many Fleet enrollment tokens at once?
  - id: delete-fleet-enrollment-api-keys-keyid
    intent: Revoke or delete one enrollment API key
    question: How do I revoke a single leaked enrollment token?
  - id: get-fleet-enrollment-api-keys-keyid
    intent: Get a Fleet enrollment API key
    question: What policy is a particular enrollment token tied to?
  phrasing_ops: 5
  slug: elk-stack-fleet-enrollment-api-keys-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet internals APIs enable you to manage Fleet internal operations, including checking permissions, monitoring Fleet Server health, managing settings, and initiating Fleet setup.
  name: Elastic Stack (ELK Stack) Fleet internals API
  phrasing_intents:
  - id: get-fleet-check-permissions
    intent: Check the current user's Fleet permissions
    question: Do I have the privileges needed to use Fleet?
  - id: post-fleet-health-check
    intent: Check a Fleet Server's health
    question: Is my Fleet Server instance healthy and reachable?
  - id: get-fleet-settings
    intent: Get global Fleet settings
    question: What are the current global Fleet settings?
  - id: put-fleet-settings
    intent: Update global Fleet settings
    question: How do I allow prerelease integrations in Fleet?
  - id: post-fleet-setup
    intent: Initialize Fleet
    question: How do I set up Fleet and create the Elasticsearch resources it needs?
  - id: get-fleet-space-settings
    intent: Get Fleet settings for the current space
    question: What Fleet settings apply to this particular Kibana space?
  - id: put-fleet-space-settings
    intent: Set Fleet settings for the current space
    question: How do I restrict which namespace prefixes a Kibana space can use in Fleet?
  phrasing_ops: 7
  slug: elk-stack-fleet-internals-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Fleet managed integrations API from Elastic Stack (ELK Stack) — 4 operation(s) for fleet managed integrations.
  name: Elastic Stack (ELK Stack) Fleet managed integrations API
  phrasing_intents:
  - id: get-fleet-managed-integrations
    intent: List managed integrations
    question: Which managed integrations are set up in Fleet?
  - id: post-fleet-managed-integrations
    intent: Create a managed integration
    question: How do I set up a new managed integration for a package?
  - id: post-fleet-managed-integrations-upgrade
    intent: Upgrade managed integrations in bulk
    question: Can I upgrade several managed integrations to the installed package version at once?
  - id: post-fleet-managed-integrations-upgrade-dryrun
    intent: Preview a managed integration upgrade
    question: What would change if I upgraded my managed integrations?
  - id: delete-fleet-managed-integrations-policyid
    intent: Delete a managed integration
    question: How do I remove a managed integration from Fleet?
  - id: get-fleet-managed-integrations-policyid
    intent: Get a managed integration
    question: What settings does one managed integration have?
  - id: put-fleet-managed-integrations-policyid
    intent: Replace a managed integration's configuration
    question: Does updating a managed integration clear fields I leave out?
  phrasing_ops: 7
  slug: elk-stack-fleet-managed-integrations-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet outputs APIs enable you to manage Fleet outputs, including creating, updating, and deleting output configurations, generating Logstash API keys, and monitoring output health.
  name: Elastic Stack (ELK Stack) Fleet outputs API
  phrasing_intents:
  - id: post-fleet-logstash-api-keys
    intent: Generate a Logstash API key for Fleet
    question: How do I get an API key so Logstash can receive data from a Fleet output?
  - id: get-fleet-outputs
    intent: List Fleet outputs
    question: Where are my Elastic Agents configured to ship data?
  - id: post-fleet-outputs
    intent: Create a Fleet output
    question: How do I add a new output, like Elasticsearch, Kafka or Logstash, for agents to send data to?
  - id: delete-fleet-outputs-outputid
    intent: Delete a Fleet output
    question: How do I remove a Fleet output I no longer use?
  - id: get-fleet-outputs-outputid
    intent: Get a Fleet output
    question: What hosts and settings does a specific Fleet output use?
  - id: put-fleet-outputs-outputid
    intent: Update a Fleet output
    question: Can I change the hosts of an existing Fleet output?
  - id: get-fleet-outputs-outputid-health
    intent: Check a Fleet output's health
    question: Is my Fleet output healthy and receiving data?
  phrasing_ops: 7
  slug: elk-stack-fleet-outputs-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet package policies APIs enable you to manage Fleet package policies, including creating, updating, and deleting policies, performing bulk operations, and managing policy upgrades.
  name: Elastic Stack (ELK Stack) Fleet package policies API
  phrasing_intents:
  - id: get-fleet-package-policies
    intent: List Fleet package policies
    question: Which integration package policies are configured in Fleet?
  - id: post-fleet-package-policies
    intent: Create a package policy on an agent policy
    question: How do I add an integration to an agent policy in Fleet?
  - id: post-fleet-package-policies-bulk-get
    intent: Fetch several package policies by ID
    question: Can I fetch several package policies in one request?
  - id: delete-fleet-package-policies-packagepolicyid
    intent: Delete a package policy
    question: How do I remove one integration from an agent policy?
  - id: get-fleet-package-policies-packagepolicyid
    intent: Get a package policy
    question: What inputs and variables does a specific package policy have?
  - id: put-fleet-package-policies-packagepolicyid
    intent: Update a package policy
    question: How do I change the settings of an integration already on an agent policy?
  - id: post-fleet-package-policies-delete
    intent: Delete several package policies
    question: Can I remove many integrations from agent policies in one call?
  - id: post-fleet-package-policies-upgrade
    intent: Upgrade package policies to a newer version
    question: How do I move integrations onto the latest package version?
  phrasing_ops: 9
  slug: elk-stack-fleet-package-policies-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet proxies APIs enable you to manage Fleet proxies, including creating, updating, and deleting proxy configurations for Fleet agent communication.
  name: Elastic Stack (ELK Stack) Fleet proxies API
  phrasing_intents:
  - id: get-fleet-proxies
    intent: List Fleet proxies
    question: Which proxies are configured for Fleet and Elastic Agents?
  - id: post-fleet-proxies
    intent: Create a Fleet proxy
    question: How do I route Elastic Agent traffic through a proxy in Fleet?
  - id: delete-fleet-proxies-itemid
    intent: Delete a Fleet proxy
    question: How do I remove a proxy from Fleet settings?
  - id: get-fleet-proxies-itemid
    intent: Get a Fleet proxy
    question: What URL and certificates does a specific Fleet proxy use?
  - id: put-fleet-proxies-itemid
    intent: Update a Fleet proxy
    question: How do I change the URL of an existing Fleet proxy?
  phrasing_ops: 5
  slug: elk-stack-fleet-proxies-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: 'Use the Fleet remote synced integrations API to check the status of the automatic integrations synchronization on a remote cluster: * Use the `/api/fleet/remote_synced_integrations/{outputId}/remote_s'
  name: Elastic Stack (ELK Stack) Fleet remote synced integrations API
  phrasing_intents:
  - id: get-fleet-remote-synced-integrations-outputid-remote-status
    intent: Check integration sync status for one output
    question: Are integrations syncing correctly to the remote cluster behind a specific Fleet output?
  - id: get-fleet-remote-synced-integrations-status
    intent: Check overall remote integration sync status
    question: Are my Fleet integrations synced across all remote clusters?
  phrasing_ops: 2
  slug: elk-stack-fleet-remote-synced-integrations-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet Server hosts APIs enable you to manage Fleet Server hosts, including creating, updating, and deleting Fleet Server host configurations.
  name: Elastic Stack (ELK Stack) Fleet Server hosts API
  phrasing_intents:
  - id: get-fleet-fleet-server-hosts
    intent: List Fleet Server hosts
    question: Which Fleet Server hosts are configured in Fleet?
  - id: post-fleet-fleet-server-hosts
    intent: Add a Fleet Server host
    question: How do I register a new Fleet Server host that Elastic Agents can enroll through?
  - id: delete-fleet-fleet-server-hosts-itemid
    intent: Delete a Fleet Server host
    question: How do I remove a Fleet Server host from Fleet?
  - id: get-fleet-fleet-server-hosts-itemid
    intent: Get a Fleet Server host
    question: What URLs and SSL settings does a specific Fleet Server host have?
  - id: put-fleet-fleet-server-hosts-itemid
    intent: Update a Fleet Server host
    question: How do I change the URLs of an existing Fleet Server host?
  phrasing_ops: 5
  slug: elk-stack-fleet-server-hosts-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Enables you to create tokens for Fleet service authentication and authorization.
  name: Elastic Stack (ELK Stack) Fleet service tokens API
  phrasing_intents:
  - id: post-fleet-service-tokens
    intent: Create a Fleet Server service token
    question: How do I generate the service token a Fleet Server needs to enroll?
  phrasing_ops: 1
  slug: elk-stack-fleet-service-tokens-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Fleet uninstall tokens APIs enable you to manage Fleet uninstall tokens, including retrieving metadata and decrypted tokens for agent uninstallation.
  name: Elastic Stack (ELK Stack) Fleet uninstall tokens API
  phrasing_intents:
  - id: get-fleet-uninstall-tokens
    intent: List latest uninstall tokens per agent policy
    question: Which agent policies have uninstall tokens for tamper-protected Elastic Agents?
  - id: post-fleet-uninstall-tokens-agentpolicyid-rotate
    intent: Rotate an agent policy's uninstall token
    question: How do I rotate the uninstall token after it was shared too widely?
  - id: get-fleet-uninstall-tokens-uninstalltokenid
    intent: Get a decrypted uninstall token
    question: What is the actual uninstall token value I need to remove a protected agent?
  phrasing_ops: 3
  slug: elk-stack-fleet-uninstall-tokens-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The graph API from Elastic Stack (ELK Stack) — 1 operation(s) for graph.
  name: Elastic Stack (ELK Stack) Graph API
  phrasing_intents:
  - id: graph-explore
    intent: Explore term connections via GET
    question: Can I find related terms in an index with a GET graph explore request?
  - id: graph-explore-1
    intent: Explore term connections via POST
    question: How do I POST a graph exploration to discover how terms in my data relate?
  phrasing_ops: 2
  slug: elk-stack-graph-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The health_report API from Elastic Stack (ELK Stack) — 2 operation(s) for health_report.
  name: Elastic Stack (ELK Stack) Health Report API
  phrasing_intents:
  - id: health-report
    intent: Get the full cluster health report
    question: Is my Elasticsearch cluster healthy, and which indicators are yellow or red?
  - id: health-report-1
    intent: Get the health of one cluster feature
    question: How do I check the health of just one area, like shard availability or disk?
  phrasing_ops: 2
  slug: elk-stack-health-report-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The IamService API from Elastic Stack (ELK Stack) — 31 operation(s) for iamservice.
  name: Elastic Stack (ELK Stack) Iam Service API
  phrasing_intents:
  - id: list-organizations
    intent: List organizations I belong to
    question: Which Elastic Cloud organizations can my user see?
  - id: get-organization-invitation
    intent: Look up an organization invitation by token
    question: What organization does this invitation token belong to?
  - id: get-organization
    intent: Get an organization's details
    question: How do I fetch the details of a single organization by its id?
  - id: update-organization
    intent: Update an organization's settings
    question: Can I rename my organization or change its billing contacts?
  - id: domain-claim-get-domain-claims
    intent: List an organization's claimed domains
    question: Which email domains has my organization claimed?
  - id: domain-claim-delete
    intent: Remove a domain claim from an organization
    question: How do I drop a domain my organization no longer owns?
  - id: domain-claim-generate-verification-code
    intent: Generate a domain ownership verification code
    question: How do I get the verification code to prove my organization owns a domain?
  - id: domain-claim-verify-domain
    intent: Verify a domain claim challenge
    question: I published the verification code, how do I complete the domain claim?
  phrasing_ops: 50
  slug: elk-stack-iamservice-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The ilm API from Elastic Stack (ELK Stack) — 10 operation(s) for ilm.
  name: Elastic Stack (ELK Stack) Ilm API
  phrasing_intents:
  - id: ilm-get-lifecycle
    intent: Get a specific lifecycle policy
    question: How do I see the phases and actions of one index lifecycle policy?
  - id: ilm-put-lifecycle
    intent: Create or update a lifecycle policy
    question: How do I create a policy that rolls over indices and deletes them after 30 days?
  - id: ilm-delete-lifecycle
    intent: Delete a lifecycle policy
    question: How do I delete an ILM policy I no longer need?
  - id: ilm-explain-lifecycle
    intent: Explain an index's lifecycle state
    question: What phase and step is my index in right now?
  - id: ilm-get-lifecycle-1
    intent: List all lifecycle policies
    question: Which index lifecycle policies exist on my cluster?
  - id: ilm-get-status
    intent: Get the ILM status
    question: Is index lifecycle management currently running or stopped?
  - id: ilm-migrate-to-data-tiers
    intent: Migrate indices and policies to data tiers
    question: How do I switch from custom node attributes to data tier allocation?
  - id: ilm-move-to-step
    intent: Manually move an index to a lifecycle step
    question: Can I force an index into a different ILM phase or step?
  phrasing_ops: 12
  slug: elk-stack-ilm-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The indices API from Elastic Stack (ELK Stack) — 63 operation(s) for indices.
  name: Elastic Stack (ELK Stack) Indices API
  phrasing_intents:
  - id: cluster-get-component-template-1
    intent: Get a named component template
    question: What mappings and settings does one specific component template define?
  - id: cluster-put-component-template
    intent: Create or update a component template (PUT)
    question: How do I define a reusable component template with shared mappings using a PUT request?
  - id: cluster-put-component-template-1
    intent: Create or update a component template (POST)
    question: Is there a POST variant for saving a component template's mappings and settings?
  - id: cluster-delete-component-template
    intent: Delete component templates
    question: How do I remove a component template that no index template uses any more?
  - id: cluster-exists-component-template
    intent: Check whether a component template exists
    question: Is there a quick way to test whether a component template exists without downloading it?
  - id: cluster-get-component-template
    intent: List all component templates
    question: Which component templates are defined on my cluster?
  - id: dangling-indices-import-dangling-index
    intent: Import a dangling index
    question: How do I recover a dangling index that is missing from the cluster state?
  - id: dangling-indices-delete-dangling-index
    intent: Delete a dangling index
    question: How do I permanently discard a dangling index I do not want to recover?
  phrasing_ops: 104
  slug: elk-stack-indices-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The inference API from Elastic Stack (ELK Stack) — 40 operation(s) for inference.
  name: Elastic Stack (ELK Stack) Inference API
  phrasing_intents:
  - id: inference-chat-completion-unified
    intent: Stream a chat completion from an inference endpoint
    question: Can I stream a multi-turn chat conversation through an Elasticsearch chat_completion endpoint?
  - id: inference-completion
    intent: Get a text completion from an inference endpoint
    question: How do I get a non-streaming text completion from a completion inference endpoint?
  - id: inference-get-1
    intent: Look up an inference endpoint by ID
    question: What service and settings is a given inference endpoint configured with?
  - id: inference-put
    intent: Create an inference endpoint without a task type
    question: Can I create an inference endpoint just by ID, letting the service determine the task type?
  - id: inference-inference
    intent: Run inference against an endpoint by ID
    question: Can I send input to an inference endpoint by ID and let it perform whatever task it was configured for?
  - id: inference-delete
    intent: Delete an inference endpoint by ID
    question: How do I remove an inference endpoint I no longer need?
  - id: inference-get-2
    intent: Look up an inference endpoint by task type and ID
    question: Can I fetch an inference endpoint scoped to a specific task type like text_embedding?
  - id: inference-put-1
    intent: Create an inference endpoint for a task type
    question: How do I create an inference endpoint for a specific task type such as sparse_embedding or completion?
  phrasing_ops: 48
  slug: elk-stack-inference-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The info API from Elastic Stack (ELK Stack) — 1 operation(s) for info.
  name: Elastic Stack (ELK Stack) Info API
  phrasing_intents:
  - id: info
    intent: Get cluster build and version info
    question: What version of Elasticsearch is my cluster running?
  phrasing_ops: 1
  slug: elk-stack-info-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The ingest API from Elastic Stack (ELK Stack) — 12 operation(s) for ingest.
  name: Elastic Stack (ELK Stack) Ingest API
  phrasing_intents:
  - id: ingest-get-geoip-database-1
    intent: Get a specific GeoIP database configuration
    question: How do I see the settings of one GeoIP database configuration by ID?
  - id: ingest-put-geoip-database
    intent: Create or update a GeoIP database configuration
    question: How do I register a MaxMind GeoIP database for the geoip processor to download?
  - id: ingest-delete-geoip-database
    intent: Delete a GeoIP database configuration
    question: How do I remove a GeoIP database configuration I no longer need?
  - id: ingest-get-ip-location-database-1
    intent: Get a specific IP location database configuration
    question: How do I view one IP location database configuration by its ID?
  - id: ingest-put-ip-location-database
    intent: Create or update an IP location database config
    question: How do I add an IPinfo or MaxMind database for the ip_location processor?
  - id: ingest-delete-ip-location-database
    intent: Delete an IP location database configuration
    question: How do I remove an IP location database configuration?
  - id: ingest-get-pipeline-1
    intent: Get a specific ingest pipeline
    question: How do I see the processors defined in one ingest pipeline?
  - id: ingest-put-pipeline
    intent: Create or update an ingest pipeline
    question: How do I create an ingest pipeline that transforms documents before they are indexed?
  phrasing_ops: 22
  slug: elk-stack-ingest-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The license API from Elastic Stack (ELK Stack) — 5 operation(s) for license.
  name: Elastic Stack (ELK Stack) License API
  phrasing_intents:
  - id: license-get
    intent: Get the cluster license
    question: What type of Elastic license is my cluster running?
  - id: license-post
    intent: Install a license with a PUT request
    question: Can I install a new license with PUT without restarting nodes?
  - id: license-post-1
    intent: Install a license with a POST request
    question: Is there a POST form of the update license call?
  - id: license-delete
    intent: Delete the cluster license
    question: What happens to my subscription level if I delete the license?
  - id: license-get-basic-status
    intent: Check if a basic license can be started
    question: Is my cluster eligible to start a basic license?
  - id: license-get-trial-status
    intent: Check if a trial license can be started
    question: Is my cluster still eligible for a free trial?
  - id: license-post-start-basic
    intent: Start a basic license
    question: How do I move my cluster onto an indefinite basic license?
  - id: license-post-start-trial
    intent: Start a 30-day trial license
    question: Can I start a 30-day trial of all subscription features?
  phrasing_ops: 8
  slug: elk-stack-license-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Links API from Elastic Stack (ELK Stack) — 2 operation(s) for links.
  name: Elastic Stack (ELK Stack) Links API
  phrasing_intents:
  - id: get-links
    intent: List links library items in Kibana
    question: How do I see all the saved links panels in my Kibana library?
  - id: post-links
    intent: Create a links library item
    question: How do I save a new set of dashboard links to the Kibana library?
  - id: delete-links-id
    intent: Delete a links library item
    question: How do I remove a links panel from the Kibana library for good?
  - id: get-links-id
    intent: Get a links library item by ID
    question: How do I look up one specific links panel from the library by its ID?
  - id: put-links-id
    intent: Create or replace a links library item by ID
    question: Can I upsert a links library item at an ID I choose?
  phrasing_ops: 5
  slug: elk-stack-links-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The logstash API from Elastic Stack (ELK Stack) — 4 operation(s) for logstash.
  name: Elastic Stack (ELK Stack) Logstash API
  phrasing_intents:
  - id: logstash-get-pipeline-1
    intent: Get a Logstash pipeline from Elasticsearch
    question: Can I read a centrally managed Logstash pipeline straight from the Elasticsearch _logstash API?
  - id: logstash-put-pipeline
    intent: Store a Logstash pipeline in Elasticsearch
    question: What fields does the Elasticsearch _logstash API require to save a pipeline, like username and last_modified?
  - id: logstash-delete-pipeline
    intent: Delete a Logstash pipeline from Elasticsearch
    question: Can I delete a centrally managed pipeline directly through the Elasticsearch _logstash API?
  - id: logstash-get-pipeline
    intent: List Logstash pipelines in Elasticsearch
    question: Which Logstash pipelines are stored in Elasticsearch for central management?
  - id: delete-logstash-pipeline
    intent: Delete a Logstash pipeline in Kibana
    question: How do I remove a centrally managed pipeline using Kibana?
  - id: get-logstash-pipeline
    intent: Get a Logstash pipeline from Kibana
    question: How do I view a centrally managed Logstash pipeline through the Kibana API?
  - id: put-logstash-pipeline
    intent: Create or update a Logstash pipeline in Kibana
    question: How do I create a centrally managed Logstash pipeline from Kibana?
  - id: get-logstash-pipelines
    intent: List all Logstash pipelines in Kibana
    question: What Logstash pipelines does Kibana central management know about?
  phrasing_ops: 8
  slug: elk-stack-logstash-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: You can schedule single or recurring maintenance windows to temporarily reduce rule notifications. For example, a maintenance window prevents false alarms during planned outages.
  name: Elastic Stack (ELK Stack) Maintenance Window API
  phrasing_intents:
  - id: post-maintenance-window
    intent: Create a maintenance window
    question: How do I silence alert notifications during a planned deployment?
  - id: get-maintenance-window-find
    intent: Search maintenance windows
    question: Which maintenance windows are running right now?
  - id: delete-maintenance-window-id
    intent: Delete a maintenance window
    question: How do I permanently delete a maintenance window?
  - id: get-maintenance-window-id
    intent: Get a maintenance window
    question: When does a particular maintenance window start and end?
  - id: patch-maintenance-window-id
    intent: Edit a maintenance window
    question: How do I extend or reschedule an existing maintenance window?
  - id: post-maintenance-window-id-archive
    intent: Archive a maintenance window
    question: How do I end a maintenance window early by archiving it?
  - id: post-maintenance-window-id-unarchive
    intent: Restore an archived maintenance window
    question: How do I bring back a maintenance window that was archived?
  phrasing_ops: 7
  slug: elk-stack-maintenance-window-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Markdowns API from Elastic Stack (ELK Stack) — 2 operation(s) for markdowns.
  name: Elastic Stack (ELK Stack) Markdowns API
  phrasing_intents:
  - id: get-markdowns
    intent: List markdown library items
    question: What markdown items are saved in my Kibana markdown library?
  - id: post-markdowns
    intent: Create a markdown library item
    question: How do I add a new reusable markdown snippet to the Kibana library?
  - id: delete-markdowns-id
    intent: Delete a markdown library item
    question: How do I permanently remove a markdown snippet from the library?
  - id: get-markdowns-id
    intent: Get a markdown library item's full content
    question: How do I read the full markdown content of one saved library item?
  - id: put-markdowns-id
    intent: Replace or upsert a markdown library item
    question: How do I update the text of an existing markdown library item?
  phrasing_ops: 5
  slug: elk-stack-markdowns-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Enables you to rotate message signing key pairs for secure Fleet communication.
  name: Elastic Stack (ELK Stack) Message Signing Service API
  phrasing_intents:
  - id: post-fleet-message-signing-service-rotate-key-pair
    intent: Rotate the Fleet message signing key pair
    question: How do I rotate the key pair Fleet uses to sign messages sent to Elastic Agents?
  phrasing_ops: 1
  slug: elk-stack-message-signing-service-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The migration API from Elastic Stack (ELK Stack) — 7 operation(s) for migration.
  name: Elastic Stack (ELK Stack) Migration API
  phrasing_intents:
  - id: indices-cancel-migrate-reindex
    intent: Cancel a migration reindex
    question: How do I stop an in-progress upgrade reindex of a data stream?
  - id: indices-create-from
    intent: Create an index from a source index (PUT)
    question: How do I create a new index copying another index's mappings and settings with PUT?
  - id: indices-create-from-1
    intent: Create an index from a source index (POST)
    question: How do I copy an index's mappings and settings into a new index with POST?
  - id: indices-get-migrate-reindex-status
    intent: Check migration reindex progress
    question: How far along is the upgrade reindex of my data stream?
  - id: indices-migrate-reindex
    intent: Reindex a data stream's legacy backing indices
    question: How do I upgrade old backing indices of a data stream before a major version upgrade?
  - id: migration-deprecations
    intent: List deprecated features in use cluster-wide
    question: Which deprecated settings is my cluster using before I upgrade?
  - id: migration-deprecations-1
    intent: List deprecations for a specific index
    question: Does one particular index use any deprecated settings?
  - id: migration-get-feature-upgrade-status
    intent: Check which system features need migration
    question: Which system features must be migrated before I upgrade?
  phrasing_ops: 9
  slug: elk-stack-migration-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The ml anomaly API from Elastic Stack (ELK Stack) — 45 operation(s) for ml anomaly.
  name: Elastic Stack (ELK Stack) ml anomaly API
  phrasing_intents:
  - id: ml-close-job
    intent: Close an anomaly detection job
    question: Can I still look at results after I close an anomaly detection job?
  - id: ml-get-calendars-2
    intent: Get one ML calendar's configuration
    question: What jobs are attached to a specific machine learning calendar?
  - id: ml-put-calendar
    intent: Create an ML calendar
    question: How do I create a calendar for planned downtime in Elastic machine learning?
  - id: ml-get-calendars-3
    intent: Get one ML calendar via POST body paging
    question: Can I fetch a specific ML calendar using a POST request with paging in the body?
  - id: ml-delete-calendar
    intent: Delete an ML calendar
    question: Does deleting a machine learning calendar also remove its scheduled events?
  - id: ml-delete-calendar-event
    intent: Delete a scheduled event from a calendar
    question: Can I remove one scheduled event from an ML calendar without deleting the calendar?
  - id: ml-put-calendar-job
    intent: Add an anomaly job to a calendar
    question: How do I make an existing anomaly job respect a calendar's scheduled events?
  - id: ml-delete-calendar-job
    intent: Remove an anomaly job from a calendar
    question: Can I detach a job from a calendar without deleting the calendar itself?
  phrasing_ops: 70
  slug: elk-stack-ml-anomaly-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The ml API from Elastic Stack (ELK Stack) — 7 operation(s) for ml.
  name: Elastic Stack (ELK Stack) Ml API
  phrasing_intents:
  - id: ml-get-memory-stats
    intent: Get ML memory usage across all nodes
    question: How much memory are my machine learning jobs and models using across the cluster?
  - id: ml-get-memory-stats-1
    intent: Get ML memory usage for one node
    question: How much memory is machine learning using on a specific node?
  - id: ml-info
    intent: Get machine learning defaults and limits
    question: What are the default settings and limits for machine learning jobs?
  - id: ml-set-upgrade-mode
    intent: Toggle ML upgrade mode
    question: How do I pause all machine learning jobs before upgrading my cluster?
  - id: mlSync
    intent: Sync ML saved objects in the default space
    question: How do I fix machine learning jobs that are missing from Kibana's saved objects?
  - id: mlUpdateJobsSpaces
    intent: Change which spaces ML jobs belong to
    question: How do I share a machine learning job with another Kibana space?
  - id: mlUpdateTrainedModelsSpaces
    intent: Change which spaces trained models belong to
    question: How do I make a trained model available in another Kibana space?
  phrasing_ops: 7
  slug: elk-stack-ml-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The ml data frame API from Elastic Stack (ELK Stack) — 12 operation(s) for ml data frame.
  name: Elastic Stack (ELK Stack) ml data frame API
  phrasing_intents:
  - id: ml-get-data-frame-analytics
    intent: Get data frame analytics job configs by ID
    question: What source, destination and analysis is a specific data frame analytics job configured with?
  - id: ml-put-data-frame-analytics
    intent: Create a data frame analytics job
    question: How do I set up outlier detection, regression or classification on an index?
  - id: ml-delete-data-frame-analytics
    intent: Delete a data frame analytics job
    question: How do I remove a data frame analytics job I no longer need?
  - id: ml-evaluate-data-frame
    intent: Evaluate data frame analytics results
    question: How accurate is my classification model compared with the ground truth in its results index?
  - id: ml-explain-data-frame-analytics
    intent: Explain an unsaved analytics config via GET
    question: Before creating a job, which fields would a draft data frame analytics config include or skip, using the GET form?
  - id: ml-explain-data-frame-analytics-1
    intent: Explain an unsaved analytics config via POST
    question: Can I POST a draft analytics config and get back which fields it would analyze?
  - id: ml-explain-data-frame-analytics-2
    intent: Explain an existing analytics job via GET
    question: Why were certain fields left out of an existing data frame analytics job, checked with GET?
  - id: ml-explain-data-frame-analytics-3
    intent: Explain an existing analytics job via POST
    question: Can I POST to explain an existing analytics job, overriding some of its settings in the body?
  phrasing_ops: 18
  slug: elk-stack-ml-data-frame-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The ml trained model API from Elastic Stack (ELK Stack) — 12 operation(s) for ml trained model.
  name: Elastic Stack (ELK Stack) ml trained model API
  phrasing_intents:
  - id: ml-clear-trained-model-deployment-cache
    intent: Clear a trained model deployment's inference cache
    question: Can I clear the inference cache of a deployed model without restarting the deployment?
  - id: ml-get-trained-models
    intent: Get trained model configs by ID
    question: What inference config and metadata does a particular trained model have?
  - id: ml-put-trained-model
    intent: Upload a trained model
    question: How do I bring in a model that wasn't created by data frame analytics?
  - id: ml-delete-trained-model
    intent: Delete an unreferenced trained model
    question: How do I delete a trained model that no ingest pipeline uses anymore?
  - id: ml-put-trained-model-alias
    intent: Create or reassign a trained model alias
    question: Can I give a trained model a friendly alias to use in inference processors?
  - id: ml-delete-trained-model-alias
    intent: Delete a trained model alias
    question: How do I remove an alias from a trained model?
  - id: ml-get-trained-models-1
    intent: List all trained models
    question: What trained models are available on my cluster?
  - id: ml-get-trained-models-stats
    intent: Get usage stats for specific trained models
    question: How many inference calls has a specific trained model served?
  phrasing_ops: 15
  slug: elk-stack-ml-trained-model-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Interact with the Observability AI Assistant resources.
  name: Elastic Stack (ELK Stack) Observability AI Assistant API
  phrasing_intents:
  - id: observability-ai-assistant-chat-complete
    intent: Get a chat completion from the AI Assistant
    question: How do I ask the Observability AI Assistant a question through the API?
  phrasing_ops: 1
  slug: elk-stack-observability-ai-assistant-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Organizations API from Elastic Stack (ELK Stack) — 15 operation(s) for organizations.
  name: Elastic Stack (ELK Stack) Organizations API
  phrasing_intents:
  - id: list-organizations
    intent: List the organizations I belong to
    question: Which Elastic Cloud organizations does my user have access to?
  - id: get-organization-invitation
    intent: Look up an organization invitation by token
    question: What organization does this invitation token belong to?
  - id: get-organization
    intent: Get an organization's details
    question: How do I fetch the name and settings of one organization by its id?
  - id: update-organization
    intent: Update an organization's name and contacts
    question: Can I rename my organization or change its billing contacts?
  - id: domain-claim-get-domain-claims
    intent: List an organization's claimed domains
    question: Which email domains has my organization already claimed?
  - id: domain-claim-delete
    intent: Remove a claimed domain from an organization
    question: How do I give up a domain my organization previously claimed?
  - id: domain-claim-generate-verification-code
    intent: Generate a domain verification code
    question: How do I get the verification code I need to prove we own a domain?
  - id: domain-claim-verify-domain
    intent: Verify a domain claim challenge
    question: Once the verification code is published, how do I complete the domain claim?
  phrasing_ops: 23
  slug: elk-stack-organizations-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Platform API from Elastic Stack (ELK Stack) — 3 operation(s) for platform.
  name: Elastic Stack (ELK Stack) Platform API
  phrasing_intents:
  - id: get-platform
    intent: Get platform information
    question: What version and details does my Elastic platform installation report?
  - id: get-extra-certificates
    intent: List extra trusted certificates
    question: Which extra certificates are configured on the platform?
  - id: get-extra-certificate
    intent: Read one extra certificate
    question: How do I view a specific extra certificate?
  - id: set-extra-certificate
    intent: Add or update an extra certificate
    question: How do I add a custom certificate to the platform's trust configuration?
  - id: delete-extra-certificate
    intent: Delete an extra certificate
    question: How do I remove an extra certificate from the platform?
  phrasing_ops: 5
  slug: elk-stack-platform-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The PlatformConfigurationInstances API from Elastic Stack (ELK Stack) — 2 operation(s) for platformconfigurationinstances.
  name: Elastic Stack (ELK Stack) Platform Configuration Instances API
  phrasing_intents:
  - id: get-instance-configurations
    intent: List instance configurations
    question: What instance configurations are available on my Elastic platform?
  - id: create-instance-configuration
    intent: Create an instance configuration
    question: How do I define a new instance configuration with its allowed sizes?
  - id: get-instance-configuration
    intent: Get an instance configuration
    question: What sizes and node types does a specific instance configuration allow?
  - id: set-instance-configuration
    intent: Create or replace an instance configuration by ID
    question: How do I overwrite an existing instance configuration with a known ID?
  - id: delete-instance-configuration
    intent: Delete an instance configuration
    question: How do I delete an instance configuration I no longer use?
  phrasing_ops: 5
  slug: elk-stack-platformconfigurationinstances-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The PlatformConfigurationNetworking API from Elastic Stack (ELK Stack) — 2 operation(s) for platformconfigurationnetworking.
  name: Elastic Stack (ELK Stack) Platform Configuration Networking API
  phrasing_intents:
  - id: get-default-deployment-domain-name
    intent: Get the default deployment domain name
    question: What default domain name are my ECE deployments published under?
  - id: set-default-deployment-domain-name
    intent: Set the default deployment domain name
    question: How do I change the default domain name used for deployment endpoints?
  - id: get-resource-kind-deployment-domain-name
    intent: Get the deployment domain for a resource kind
    question: What domain name is used for Kibana or Elasticsearch resources specifically?
  - id: set-resource-kind-deployment-domain-name
    intent: Set the deployment domain for a resource kind
    question: How do I give one resource kind its own deployment domain name?
  phrasing_ops: 4
  slug: elk-stack-platformconfigurationnetworking-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The PlatformConfigurationSecurity API from Elastic Stack (ELK Stack) — 12 operation(s) for platformconfigurationsecurity.
  name: Elastic Stack (ELK Stack) Platform Configuration Security API
  phrasing_intents:
  - id: get-security-deployment
    intent: View the platform security deployment
    question: What does the current security deployment for my Elastic Cloud Enterprise platform look like?
  - id: create-security-deployment
    intent: Create the platform security deployment
    question: How do I set up a security deployment for the first time on my platform?
  - id: update-security-deployment
    intent: Update the platform security deployment
    question: Can I change the version or topology of the existing security deployment?
  - id: get-enrollment-tokens
    intent: List active enrollment tokens
    question: Which enrollment tokens are currently active for adding hosts to the platform?
  - id: create-enrollment-token
    intent: Create an enrollment token
    question: How do I generate a token so a new host can join my installation with certain roles?
  - id: delete-enrollment-token
    intent: Revoke an enrollment token
    question: How can I revoke an enrollment token that leaked?
  - id: get-security-realm-configurations
    intent: List security realm configurations
    question: Which authentication realms, like LDAP, SAML or Active Directory, are configured?
  - id: reorder-security-realms
    intent: Reorder security realms
    question: Can I change which authentication realm is tried first?
  phrasing_ops: 22
  slug: elk-stack-platformconfigurationsecurity-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The PlatformConfigurationSnapshots API from Elastic Stack (ELK Stack) — 2 operation(s) for platformconfigurationsnapshots.
  name: Elastic Stack (ELK Stack) Platform Configuration Snapshots API
  phrasing_intents:
  - id: get-snapshot-repositories
    intent: List snapshot repository configurations
    question: Which snapshot repositories are configured for the platform?
  - id: get-snapshot-repository
    intent: Get a snapshot repository configuration
    question: What type and settings does a particular snapshot repository have?
  - id: set-snapshot-repository
    intent: Create or update a snapshot repository
    question: How do I add an S3 snapshot repository to the platform?
  - id: delete-snapshot-repository
    intent: Delete a snapshot repository configuration
    question: How do I remove a snapshot repository from the platform?
  phrasing_ops: 4
  slug: elk-stack-platformconfigurationsnapshots-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The PlatformConfigurationTemplates API from Elastic Stack (ELK Stack) — 1 operation(s) for platformconfigurationtemplates.
  name: Elastic Stack (ELK Stack) Platform Configuration Templates API
  phrasing_intents:
  - id: get-global-deployment-templates
    intent: List deployment templates across all regions
    question: Which deployment templates are available across every region?
  phrasing_ops: 1
  slug: elk-stack-platformconfigurationtemplates-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The PlatformConfigurationTrustRelationships API from Elastic Stack (ELK Stack) — 2 operation(s) for platformconfigurationtrustrelationships.
  name: Elastic Stack (ELK Stack) Platform Configuration Trust Relationships API
  phrasing_intents:
  - id: get-trust-relationships
    intent: List trust relationships
    question: Which environments does my installation have trust relationships with?
  - id: create-trust-relationship
    intent: Create a trust relationship
    question: How do I set up trust with another environment so its deployments can connect to mine?
  - id: get-trust-relationship
    intent: Get a trust relationship
    question: What are the settings of one specific trust relationship?
  - id: update-trust-relationship
    intent: Update a trust relationship
    question: Can I rotate the CA certificate on an existing trust relationship?
  - id: delete-trust-relationship
    intent: Delete a trust relationship
    question: How do I remove trust with another environment?
  phrasing_ops: 5
  slug: elk-stack-platformconfigurationtrustrelationships-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The PlatformInfrastructure API from Elastic Stack (ELK Stack) — 51 operation(s) for platforminfrastructure.
  name: Elastic Stack (ELK Stack) Platform Infrastructure API
  phrasing_intents:
  - id: get-api-base-url
    intent: Get the platform API base URL
    question: What API base URL is configured for my Elastic Cloud Enterprise platform?
  - id: set-api-base-url
    intent: Set the platform API base URL
    question: How do I change the API base URL for my ECE installation?
  - id: list-config-store-option
    intent: List Config Store options
    question: What options are stored in the platform Config Store?
  - id: get-config-store-option
    intent: Get a Config Store option by name
    question: How do I read the value of one Config Store option?
  - id: create-config-store-option
    intent: Create a new Config Store option
    question: How do I add a brand-new option to the platform Config Store?
  - id: put-config-store-option
    intent: Update an existing Config Store option
    question: How do I change the value of a Config Store option that already exists?
  - id: delete-config-store-option
    intent: Delete a Config Store option
    question: How do I remove an option from the Config Store?
  - id: get-adminconsoles
    intent: List adminconsoles
    question: What adminconsole instances are running in my ECE installation?
  phrasing_ops: 83
  slug: elk-stack-platforminfrastructure-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The query_rules API from Elastic Stack (ELK Stack) — 4 operation(s) for query_rules.
  name: Elastic Stack (ELK Stack) Query Rules API
  phrasing_intents:
  - id: query-rules-get-rule
    intent: Get a query rule
    question: How do I see the criteria and actions of one rule inside a ruleset?
  - id: query-rules-put-rule
    intent: Create or update a single query rule
    question: How do I pin specific documents to the top when a query matches certain criteria?
  - id: query-rules-delete-rule
    intent: Delete a query rule
    question: How do I remove one rule from a query ruleset?
  - id: query-rules-get-ruleset
    intent: Get a query ruleset
    question: What rules are in a given query ruleset?
  - id: query-rules-put-ruleset
    intent: Create or replace a query ruleset
    question: How many rules can one query ruleset hold?
  - id: query-rules-delete-ruleset
    intent: Delete a query ruleset
    question: How do I delete an entire query ruleset and everything in it?
  - id: query-rules-list-rulesets
    intent: List query rulesets
    question: Which query rulesets exist on my cluster?
  - id: query-rules-test
    intent: Test which query rules would match
    question: Which rules in my ruleset would fire for a given user query?
  phrasing_ops: 8
  slug: elk-stack-query-rules-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The reindex API from Elastic Stack (ELK Stack) — 3 operation(s) for reindex.
  name: Elastic Stack (ELK Stack) Reindex API
  phrasing_intents:
  - id: cancel-reindex
    intent: Cancel a running reindex task
    question: How do I cancel a reindex that's taking too long?
  - id: get-reindex
    intent: Get a reindex task's status and progress
    question: How far along is my reindex task?
  - id: list-reindex
    intent: List running reindex tasks
    question: Which reindex jobs are running on my cluster right now?
  phrasing_ops: 3
  slug: elk-stack-reindex-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Manage the roles that grant Elasticsearch and Kibana privileges.
  name: Elastic Stack (ELK Stack) Roles API
  phrasing_intents:
  - id: get-security-role
    intent: List all Kibana roles
    question: What roles are defined in Kibana?
  - id: delete-security-role-name
    intent: Delete a Kibana role
    question: How do I delete a Kibana role by name?
  - id: get-security-role-name
    intent: Get a Kibana role
    question: How do I see the privileges granted by one Kibana role?
  - id: put-security-role-name
    intent: Create or update a Kibana role
    question: How do I create a role granting read access to certain indices and Kibana features?
  - id: post-security-roles
    intent: Create or update several Kibana roles at once
    question: Can I create or update multiple roles in a single request?
  phrasing_ops: 5
  slug: elk-stack-roles-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The rollup API from Elastic Stack (ELK Stack) — 8 operation(s) for rollup.
  name: Elastic Stack (ELK Stack) Rollup API
  phrasing_intents:
  - id: rollup-get-jobs
    intent: Get one rollup job's config and stats
    question: What is the status and configuration of a specific rollup job?
  - id: rollup-put-job
    intent: Create a rollup job
    question: How do I summarize old time series data into a smaller rollup index on a schedule?
  - id: rollup-delete-job
    intent: Delete a rollup job
    question: Can I delete a rollup job that is still started?
  - id: rollup-get-jobs-1
    intent: List all rollup jobs
    question: Which rollup jobs are active on my cluster?
  - id: rollup-get-rollup-caps
    intent: Get rollup capabilities for an index pattern
    question: Which fields and aggregations are rolled up for a given source index pattern?
  - id: rollup-get-rollup-caps-1
    intent: Get rollup capabilities for all indices
    question: What rollup capabilities exist across every source index in the cluster?
  - id: rollup-get-rollup-index-caps
    intent: Get capabilities of a rollup index
    question: What jobs and aggregations are stored inside a particular rollup index?
  - id: rollup-rollup-search
    intent: Search rolled-up data with GET
    question: Can I query rollup indices with a GET request and normal Query DSL?
  phrasing_ops: 11
  slug: elk-stack-rollup-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Export sets of saved objects that you want to import into Kibana, resolve import errors, and rotate an encryption key for encrypted saved objects with the saved objects APIs. To manage a specific type
  name: Elastic Stack (ELK Stack) saved objects API
  phrasing_intents:
  - id: rotateEncryptionKey
    intent: Rotate the encryption key for saved objects
    question: How do I re-encrypt Kibana saved objects with the current primary key?
  - id: post-saved-objects-bulk-create
    intent: Create many saved objects at once (legacy)
    question: How do I create several Kibana saved objects in a single request?
  - id: post-saved-objects-bulk-delete
    intent: Delete many saved objects at once (legacy)
    question: How do I delete a batch of Kibana saved objects in one call?
  - id: post-saved-objects-bulk-get
    intent: Fetch many saved objects by type and ID
    question: How do I fetch several saved objects by type and ID at once?
  - id: post-saved-objects-bulk-resolve
    intent: Resolve many saved objects via legacy aliases
    question: How do I look up several saved objects whose IDs may have changed after an upgrade?
  - id: put-saved-objects-bulk-update
    intent: Update many saved objects at once (legacy)
    question: How do I update several saved objects in one request?
  - id: post-saved-objects-export
    intent: Export saved objects to a file
    question: How do I back up my Kibana dashboards to a file?
  - id: get-saved-objects-find
    intent: Search saved objects
    question: How do I find saved objects of a given type by title?
  phrasing_ops: 16
  slug: elk-stack-saved-objects-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The script API from Elastic Stack (ELK Stack) — 5 operation(s) for script.
  name: Elastic Stack (ELK Stack) Script API
  phrasing_intents:
  - id: get-script
    intent: Get a stored script or search template
    question: How can I see the source of a stored Painless script?
  - id: put-script
    intent: Store a script with PUT
    question: How do I save a Painless script in the cluster state with a PUT request?
  - id: put-script-1
    intent: Store a script with POST
    question: Can I create or update a stored script with POST instead of PUT?
  - id: delete-script
    intent: Delete a stored script or search template
    question: How do I remove a stored script from the cluster?
  - id: get-script-context
    intent: List supported script contexts
    question: Which script contexts does Elasticsearch support, and what methods do they have?
  - id: get-script-languages
    intent: List available script languages
    question: Which scripting languages are enabled on my cluster?
  - id: put-script-2
    intent: Store a script for a context with PUT
    question: Can I compile and store a script against a specific context in the URL path using PUT?
  - id: put-script-3
    intent: Store a script for a context with POST
    question: Can I POST a stored script to a path that names its context?
  phrasing_ops: 10
  slug: elk-stack-script-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The search API from Elastic Stack (ELK Stack) — 29 operation(s) for search.
  name: Elastic Stack (ELK Stack) Search API
  phrasing_intents:
  - id: async-search-get
    intent: Get the results of an async search
    question: How do I retrieve the hits from an async search I submitted earlier?
  - id: async-search-delete
    intent: Cancel or delete an async search
    question: How do I cancel an async search that is still running?
  - id: async-search-status
    intent: Check an async search's status
    question: Is my async search still running, without pulling back its hits?
  - id: async-search-submit
    intent: Start an async search across all indices
    question: How do I run a long search in the background across the whole cluster?
  - id: async-search-submit-1
    intent: Start an async search on specific indices
    question: How do I launch an asynchronous search limited to one index or data stream?
  - id: scroll
    intent: Get the next scroll batch via GET
    question: How do I fetch the next page of a scrolling search using a GET request?
  - id: scroll-1
    intent: Get the next scroll batch via POST
    question: Can I POST a scroll ID in the body to retrieve the next batch of hits?
  - id: clear-scroll
    intent: Clear scroll contexts named in the body
    question: How do I free the resources held by open scroll contexts?
  phrasing_ops: 55
  slug: elk-stack-search-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The search_application API from Elastic Stack (ELK Stack) — 4 operation(s) for search_application.
  name: Elastic Stack (ELK Stack) Search Application API
  phrasing_intents:
  - id: search-application-get
    intent: Get a search application
    question: Which indices and template does a particular search application use?
  - id: search-application-put
    intent: Create or update a search application
    question: How do I set up a search application over several indices?
  - id: search-application-delete
    intent: Delete a search application
    question: Are the indices removed when I delete a search application?
  - id: search-application-list
    intent: List search applications
    question: What search applications exist in my cluster?
  - id: search-application-render-query
    intent: Render a search application's query
    question: Can I see the Elasticsearch query a search application would generate without running it?
  - id: search-application-search
    intent: Run a search application search
    question: How do I run a search through a search application's template?
  - id: search-application-search-1
    intent: Run a search application search via POST
    question: Can I run a search application query with a POST request body?
  phrasing_ops: 7
  slug: elk-stack-search-application-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The searchable_snapshots API from Elastic Stack (ELK Stack) — 7 operation(s) for searchable_snapshots.
  name: Elastic Stack (ELK Stack) Searchable Snapshots API
  phrasing_intents:
  - id: searchable-snapshots-cache-stats
    intent: Get shared cache stats across all nodes
    question: How full is the shared cache for partially mounted indices across my cluster?
  - id: searchable-snapshots-cache-stats-1
    intent: Get shared cache stats for specific nodes
    question: What does the searchable snapshot cache look like on one particular node?
  - id: searchable-snapshots-clear-cache
    intent: Clear the searchable snapshot cache everywhere
    question: Can I flush the shared cache for all partially mounted indices?
  - id: searchable-snapshots-clear-cache-1
    intent: Clear the searchable snapshot cache for an index
    question: How do I clear cached data for just one mounted index or data stream?
  - id: searchable-snapshots-mount
    intent: Mount a snapshot as a searchable index
    question: How do I make an index inside a snapshot searchable without restoring it fully?
  - id: searchable-snapshots-stats
    intent: Get searchable snapshot stats for all indices
    question: What are the searchable snapshot statistics across the whole cluster?
  - id: searchable-snapshots-stats-1
    intent: Get searchable snapshot stats for an index
    question: How is one mounted searchable snapshot index performing?
  phrasing_ops: 7
  slug: elk-stack-searchable-snapshots-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Manage and interact with Security Assistant resources.
  name: Elastic Stack (ELK Stack) Security AI Assistant API
  phrasing_intents:
  - id: PerformAnonymizationFieldsBulkAction
    intent: Bulk create, update or delete anonymization fields
    question: Can I change which fields the Security AI Assistant anonymizes in one batch?
  - id: FindAnonymizationFields
    intent: List anonymization fields
    question: Which fields does the security AI assistant anonymize before sending to the model?
  - id: ChatComplete
    intent: Get a model response from the security assistant
    question: How do I send messages to the Elastic Security AI Assistant and get an answer back?
  - id: DeleteAllConversations
    intent: Delete all my assistant conversations
    question: Can I clear my entire security assistant chat history?
  - id: CreateConversation
    intent: Start a new assistant conversation
    question: Can I create a saved conversation with the security AI assistant ahead of time?
  - id: FindConversations
    intent: Search my assistant conversations
    question: What conversations have I had with the security AI assistant?
  - id: DeleteConversation
    intent: Delete one assistant conversation
    question: Can I delete a single chat with the security assistant?
  - id: ReadConversation
    intent: Get an assistant conversation
    question: Can I pull up the full message history of one assistant conversation?
  phrasing_ops: 21
  slug: elk-stack-security-ai-assistant-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The security API from Elastic Stack (ELK Stack) — 64 operation(s) for security.
  name: Elastic Stack (ELK Stack) Security API
  phrasing_intents:
  - id: encryption-reset
    intent: Reset the project encryption key
    question: How do I recover when the project encryption key can no longer be read from disk?
  - id: security-activate-user-profile
    intent: Activate a user profile for another user
    question: How does Kibana create or refresh a user profile on behalf of a user who just logged in?
  - id: security-authenticate
    intent: See who I'm authenticated as
    question: Which user and roles is my current Elasticsearch credential authenticated as?
  - id: security-get-role-1
    intent: List all native realm roles
    question: Which roles are defined in the native realm?
  - id: security-bulk-put-role
    intent: Create or update many roles at once
    question: How do I create several native realm roles in a single request?
  - id: security-bulk-delete-role
    intent: Delete many roles at once
    question: How do I delete several native realm roles in one call?
  - id: security-bulk-update-api-keys
    intent: Update multiple API keys at once
    question: How do I apply the same metadata or expiration to many API keys in one request?
  - id: security-change-password
    intent: Change a user's password (PUT)
    question: How do I reset the password of a specific native realm user?
  phrasing_ops: 100
  slug: elk-stack-security-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Use the Attack discovery APIs to generate and manage Attack discoveries. Attack Discovery leverages large language models (LLMs) to analyze alerts in your environment and identify threats. Each "disco
  name: Elastic Stack (ELK Stack) Security Attack discovery API
  phrasing_intents:
  - id: PostAttackDiscoveryBulk
    intent: Bulk update Attack discoveries
    question: Can I change the workflow status of many Attack discoveries at once?
  - id: AttackDiscoveryFind
    intent: Search Attack discoveries
    question: Which Attack discoveries were found in the last day?
  - id: PostAttackDiscoveryGenerate
    intent: Generate attack discoveries from alerts with AI
    question: How do I have an AI connector analyse my security alerts for attack chains?
  - id: GetAttackDiscoveryGenerations
    intent: List my recent Attack Discovery generations
    question: What is the status of my recent Attack Discovery runs?
  - id: GetAttackDiscoveryGeneration
    intent: Get one Attack Discovery generation
    question: Which attack discoveries did a particular generation run produce?
  - id: PostAttackDiscoveryGenerationsDismiss
    intent: Dismiss an Attack Discovery generation
    question: How do I stop a finished generation from showing in the UI?
  - id: CreateAttackDiscoverySchedules
    intent: Create an Attack Discovery schedule
    question: Can Attack Discovery run automatically on an interval?
  - id: BulkDeleteAttackDiscoverySchedules
    intent: Delete several Attack Discovery schedules
    question: Can I delete multiple Attack Discovery schedules at once?
  phrasing_ops: 16
  slug: elk-stack-security-attack-discovery-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Use the detections APIs to create and manage detection rules. Detection rules search events and external alerts sent to Elastic Security and generate detection alerts from any hits. Alerts are display
  name: Elastic Stack (ELK Stack) Security Detections API
  phrasing_intents:
  - id: SetAttacksAssignees
    intent: Assign users to attack discovery alerts
    question: How do I assign an analyst to an attack discovery?
  - id: SearchAttacks
    intent: Search and aggregate attack discoveries
    question: Which attack discoveries in this space match my query?
  - id: SetAttacksStatus
    intent: Change the workflow status of attack discoveries
    question: How do I mark an attack discovery as acknowledged or closed?
  - id: SetAttacksTags
    intent: Tag or untag attack discoveries
    question: Can I add and remove tags on attack discoveries in a single request?
  - id: DeleteAlertsIndex
    intent: Delete the security alerts index
    question: What happens to stored alerts if I delete the alerts backing index?
  - id: ReadAlertsIndex
    intent: Check the security alerts index
    question: Which Elasticsearch index backs Elastic Security detection alerts in my space?
  - id: CreateAlertsIndex
    intent: Create the security alerts index
    question: Do I need to create an alerts index before detection rules can generate alerts?
  - id: ReadPrivileges
    intent: Check my security detection privileges
    question: Do I have the index privileges needed to create the security alerts index?
  phrasing_ops: 29
  slug: elk-stack-security-detections-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Endpoint Exceptions API allows you to manage detection rule endpoint exceptions to prevent a rule from generating an alert from incoming events even when the rule's other criteria are met.
  name: Elastic Stack (ELK Stack) Security Endpoint Exceptions API
  phrasing_intents:
  - id: CreateEndpointList
    intent: Create the Elastic Endpoint exception list
    question: How do I set up the exception list that Elastic Endpoint rules use?
  - id: DeleteEndpointListItem
    intent: Delete an Endpoint exception item
    question: How can I remove an Endpoint exception so those events alert again?
  - id: ReadEndpointListItem
    intent: Get an Endpoint exception item
    question: What conditions does a specific Endpoint exception item contain?
  - id: CreateEndpointListItem
    intent: Add an Endpoint exception item
    question: How do I stop Elastic Endpoint from alerting on a trusted process?
  - id: UpdateEndpointListItem
    intent: Update an Endpoint exception item
    question: How do I edit the entries of an existing Endpoint exception?
  - id: FindEndpointListItems
    intent: List Endpoint exception items
    question: Which exceptions are currently on the Elastic Endpoint list?
  phrasing_ops: 6
  slug: elk-stack-security-endpoint-exceptions-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Interact with and manage endpoints running the Elastic Defend integration.
  name: Elastic Stack (ELK Stack) Security Endpoint Management API
  phrasing_intents:
  - id: EndpointGetActionsList
    intent: List endpoint response actions
    question: What response actions have been run against my endpoints?
  - id: EndpointGetActionsStatus
    intent: Get pending response action status for agents
    question: Do any of my agents have response actions still pending?
  - id: EndpointGetActionsDetails
    intent: Get details of a response action
    question: Did a specific response action complete successfully?
  - id: EndpointFileInfo
    intent: Get info about a response action file
    question: What file was collected by a get-file response action, and how big is it?
  - id: EndpointFileDownload
    intent: Download a file from a response action
    question: How can I download a file that was pulled from an endpoint?
  - id: CancelAction
    intent: Cancel a pending response action
    question: Can I cancel a response action that is still pending on a host?
  - id: EndpointExecuteAction
    intent: Run a shell command on an endpoint
    question: Can I run a shell command remotely on a compromised host?
  - id: EndpointGetFileAction
    intent: Retrieve a file from an endpoint
    question: Can I pull a suspicious file off a host for analysis?
  phrasing_ops: 29
  slug: elk-stack-security-endpoint-management-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Use the Security entity analytics APIs to manage entity analytics and risk scoring, including asset criticality, privileged user monitoring, and entity engines.
  name: Elastic Stack (ELK Stack) Security Entity Analytics API
  phrasing_intents:
  - id: DeleteAssetCriticalityRecord
    intent: Remove an entity's asset criticality record
    question: How can I clear the criticality level I assigned to a user?
  - id: GetAssetCriticalityRecord
    intent: Get an entity's asset criticality record
    question: What asset criticality level is assigned to a particular host or user?
  - id: CreateAssetCriticalityRecord
    intent: Set asset criticality for a single entity
    question: How do I mark one host as high impact so its risk score is weighted more?
  - id: BulkUpsertAssetCriticalityRecords
    intent: Bulk set asset criticality for many entities
    question: Can I assign criticality levels to hundreds of hosts and users in one call?
  - id: FindAssetCriticalityRecords
    intent: List asset criticality records
    question: Which entities have been given an asset criticality level?
  - id: DeleteMonitoringEngine
    intent: Delete the Privilege Monitoring Engine
    question: How do I tear down the Privilege Monitoring Engine completely?
  - id: DisableMonitoringEngine
    intent: Disable the Privilege Monitoring Engine
    question: Can I pause privileged user monitoring without losing the data it has collected?
  - id: InitMonitoringEngine
    intent: Initialize the Privilege Monitoring Engine
    question: How do I turn on Privilege Monitoring for the first time?
  phrasing_ops: 29
  slug: elk-stack-security-entity-analytics-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Security entity store API from Elastic Stack (ELK Stack) — 16 operation(s) for security entity store.
  name: Elastic Stack (ELK Stack) Security entity store API
  phrasing_intents:
  - id: put-security-entity-store
    intent: Change Entity Store log extraction settings
    question: Can I adjust how the Entity Store extracts entities from logs after it is installed?
  - id: get-security-entity-store-entities
    intent: List entities in the Entity Store
    question: Which hosts, users and services has the Entity Store recorded?
  - id: delete-security-entity-store-entities
    intent: Delete an entity record
    question: How can I remove a single host or user entity from the Entity Store?
  - id: post-security-entity-store-entities-entitytype
    intent: Create an entity record
    question: How do I add a new user or host entity to the Entity Store by hand?
  - id: put-security-entity-store-entities-entitytype
    intent: Update one entity record
    question: Can I edit fields on an existing host or user entity?
  - id: put-security-entity-store-entities-bulk
    intent: Update many entity records at once
    question: Can I update a batch of entity records in a single request?
  - id: post-security-entity-store-install
    intent: Install the Entity Store
    question: How do I turn on the Entity Store for hosts and users in Elastic Security?
  - id: get-security-entity-store-resolution-group
    intent: Show an entity's resolution group
    question: Which other entities have been linked to this one as the same identity?
  phrasing_ops: 17
  slug: elk-stack-security-entity-store-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Exceptions are associated with detection and endpoint rules, and are used to prevent a rule from generating an alert from incoming events, even when the rule's other criteria are met. They can help re
  name: Elastic Stack (ELK Stack) Security Exceptions API
  phrasing_intents:
  - id: CreateRuleExceptionListItems
    intent: Add exception items to a detection rule
    question: How do I add an exception directly to one detection rule so it stops alerting on known-good activity?
  - id: DeleteExceptionList
    intent: Delete an exception list
    question: How do I permanently delete an exception list?
  - id: ReadExceptionList
    intent: Get an exception list's details
    question: What are the details of a specific exception list?
  - id: CreateExceptionList
    intent: Create an exception list
    question: How do I create a new exception list for my detection rules?
  - id: UpdateExceptionList
    intent: Update an exception list
    question: How do I rename an existing exception list or change its description?
  - id: DuplicateExceptionList
    intent: Duplicate an exception list
    question: Can I make a copy of an existing exception list?
  - id: ExportExceptionList
    intent: Export an exception list to a file
    question: How do I export an exception list and its items as NDJSON?
  - id: FindExceptionLists
    intent: Search and list exception lists
    question: Which exception lists exist in my Kibana space?
  phrasing_ops: 16
  slug: elk-stack-security-exceptions-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: 'Lists can be used with detection rule exceptions to define values that prevent a rule from generating alerts. Lists are made up of: * **List containers**: A container for values of the same Elasticsea'
  name: Elastic Stack (ELK Stack) Security Lists API
  phrasing_intents:
  - id: DeleteList
    intent: Delete a value list and its items
    question: Does deleting a value list also delete all of its items?
  - id: ReadList
    intent: Get a value list's details
    question: Can I look up one value list by its ID?
  - id: PatchList
    intent: Change specific fields of a value list
    question: Can I change just the name of a value list without replacing the rest?
  - id: CreateList
    intent: Create a value list
    question: How do I create a new value list of IP addresses for exceptions?
  - id: UpdateList
    intent: Replace a value list's name and description
    question: Can I fully replace a value list, knowing unspecified fields get deleted?
  - id: FindLists
    intent: Browse and filter value lists
    question: What value lists exist in this Kibana space?
  - id: DeleteListIndex
    intent: Delete the value list data streams
    question: How do I remove the .lists and .items data streams entirely?
  - id: ReadListIndex
    intent: Check that value list data streams exist
    question: Do the .lists and .items data streams exist in this space?
  phrasing_ops: 18
  slug: elk-stack-security-lists-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Run live queries, manage packs and saved queries.
  name: Elastic Stack (ELK Stack) Security Osquery API
  phrasing_intents:
  - id: OsqueryGetUnifiedHistory
    intent: View combined osquery execution history
    question: Can I see live, rule-triggered and scheduled osquery runs in one timeline?
  - id: OsqueryFindLiveQueries
    intent: List live osquery queries
    question: Which live queries have been run against my hosts?
  - id: OsqueryCreateLiveQuery
    intent: Run a live osquery query on hosts
    question: How do I run an osquery SQL query on my endpoints right now?
  - id: OsqueryGetLiveQueryDetails
    intent: Get a live query's details
    question: What queries and agents were part of a specific live query run?
  - id: OsqueryGetLiveQueryResults
    intent: Get the result rows of a live query
    question: Where do I see the rows my live osquery query returned?
  - id: OsqueryExportLiveQueryResults
    intent: Download live query results as a file
    question: Can I download a live query's results as a file?
  - id: OsqueryFindPacks
    intent: List osquery packs
    question: What osquery query packs do I have?
  - id: OsqueryCreatePacks
    intent: Create an osquery pack
    question: How do I bundle several scheduled osquery queries into a pack?
  phrasing_ops: 21
  slug: elk-stack-security-osquery-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Use the initialization API to set up the assets Elastic Security needs to operate in a Kibana space. A single request can run one or more initialization flows. Each flow provisions a specific set of a
  name: Elastic Stack (ELK Stack) Security Solution Initialization API
  phrasing_intents:
  - id: InitializeSecuritySolution
    intent: Run Security Solution initialization flows
    question: How do I provision prebuilt detection rules and security data views for a new space?
  phrasing_ops: 1
  slug: elk-stack-security-solution-initialization-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: You can create Timelines and Timeline templates via the API, as well as import new Timelines from an ndjson file.
  name: Elastic Stack (ELK Stack) Security Timeline API
  phrasing_intents:
  - id: DeleteNote
    intent: Delete one or more Timeline notes
    question: How do I remove a note I left on a Timeline investigation?
  - id: GetNotes
    intent: List investigation notes
    question: What notes have analysts left on a particular alert or event document?
  - id: PersistNoteRoute
    intent: Add or edit a note on a Timeline or event
    question: How do I add a note to a Timeline or to an event in it?
  - id: PersistPinnedEventRoute
    intent: Pin or unpin an event in a Timeline
    question: How do I pin an important event so it stays at the top of a Timeline?
  - id: DeleteTimelines
    intent: Delete Timelines or templates
    question: How do I delete old Timeline investigations I no longer need?
  - id: GetTimeline
    intent: Get a saved Timeline or template
    question: How do I load a saved Timeline investigation by its ID?
  - id: PatchTimeline
    intent: Update an existing Timeline
    question: How do I change the title or query of a Timeline I already saved?
  - id: CreateTimelines
    intent: Create a Timeline or Timeline template
    question: How do I create a new Timeline for a security investigation?
  phrasing_ops: 17
  slug: elk-stack-security-timeline-api-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Manage Kibana short URLs.
  name: Elastic Stack (ELK Stack) short url API
  phrasing_intents:
  - id: post-url
    intent: Create a Kibana short URL
    question: How do I make a short, shareable link to a Kibana view?
  - id: resolve-url
    intent: Resolve a short URL by its slug
    question: Where does a Kibana short link slug point to?
  - id: delete-url
    intent: Delete a short URL
    question: How do I remove a Kibana short link?
  - id: get-url
    intent: Get a short URL by ID
    question: What locator and params are stored in one short URL?
  phrasing_ops: 4
  slug: elk-stack-short-url-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The significant_events API from Elastic Stack (ELK Stack) — 4 operation(s) for significant_events.
  name: Elastic Stack (ELK Stack) Significant Events API
  phrasing_intents:
  - id: get-streams-name-queries
    intent: List significant-event queries on a stream
    question: Which significant-event queries are attached to a stream?
  - id: post-streams-name-queries-bulk
    intent: Bulk add and remove stream queries
    question: How do I add and delete several significant-event queries on a stream in one call?
  - id: delete-streams-name-queries-queryid
    intent: Remove a significant-event query from a stream
    question: How do I remove a detection query from a stream?
  - id: put-streams-name-queries-queryid
    intent: Add a significant-event query to a stream
    question: How do I add an ES|QL query that flags significant events on a stream?
  - id: get-streams-name-significant-events
    intent: Read a stream's significant events over time
    question: What significant events happened on a stream during a time range?
  phrasing_ops: 5
  slug: elk-stack-significant-events-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The slm API from Elastic Stack (ELK Stack) — 8 operation(s) for slm.
  name: Elastic Stack (ELK Stack) Slm API
  phrasing_intents:
  - id: slm-get-lifecycle
    intent: Get a snapshot lifecycle policy
    question: When did my nightly snapshot policy last succeed or fail?
  - id: slm-put-lifecycle
    intent: Create or update a snapshot policy
    question: How do I schedule automatic nightly snapshots of my cluster?
  - id: slm-delete-lifecycle
    intent: Delete a snapshot lifecycle policy
    question: How do I stop a snapshot policy from taking any more snapshots?
  - id: slm-execute-lifecycle
    intent: Take a snapshot now using a policy
    question: Can I take a snapshot immediately before an upgrade instead of waiting for the schedule?
  - id: slm-execute-retention
    intent: Delete expired snapshots now
    question: How do I force snapshot retention to run and delete expired snapshots right away?
  - id: slm-get-lifecycle-1
    intent: List all snapshot lifecycle policies
    question: What snapshot policies are set up in my cluster?
  - id: slm-get-stats
    intent: Get snapshot lifecycle statistics
    question: How many snapshots has SLM taken, failed or deleted in total?
  - id: slm-get-status
    intent: Check whether snapshot lifecycle is running
    question: Is snapshot lifecycle management running or stopped?
  phrasing_ops: 10
  slug: elk-stack-slm-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: SLO APIs enable you to define, manage and track service-level objectives
  name: Elastic Stack (ELK Stack) Slo API
  phrasing_intents:
  - id: findSlosOp
    intent: List and search SLOs
    question: Which service level objectives are defined in my Kibana space?
  - id: createSloOp
    intent: Create a service level objective
    question: How do I define a new SLO with a target and time window?
  - id: bulkDeleteOp
    intent: Bulk delete SLO definitions
    question: How do I delete many SLOs and their summary and rollup data at once?
  - id: bulkDeleteStatusOp
    intent: Check the status of a bulk SLO deletion
    question: Has my bulk SLO deletion finished yet?
  - id: deleteRollupDataOp
    intent: Purge SLO rollup and summary data
    question: Can I purge old rollup data for SLOs while keeping the definitions?
  - id: bulkSnapshotOp
    intent: Compute summaries for many SLO instances at once
    question: How do I get the status of up to 100 SLO instances as of a past moment?
  - id: deleteSloInstancesOp
    intent: Delete data for specific SLO instances
    question: How do I remove the rollup and summary data for particular SLO instance IDs?
  - id: deleteSloOp
    intent: Delete an SLO
    question: How do I delete a single SLO I no longer need?
  phrasing_ops: 15
  slug: elk-stack-slo-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The snapshot API from Elastic Stack (ELK Stack) — 12 operation(s) for snapshot.
  name: Elastic Stack (ELK Stack) Snapshot API
  phrasing_intents:
  - id: snapshot-cleanup-repository
    intent: Clean up stale data in a snapshot repository
    question: How do I delete leftover files in a snapshot repository that no snapshot references anymore?
  - id: snapshot-clone
    intent: Clone a snapshot within the same repository
    question: Can I copy some indices from an existing snapshot into a new snapshot?
  - id: snapshot-get
    intent: Get information about snapshots
    question: How do I list the snapshots stored in a repository?
  - id: snapshot-create
    intent: Take a snapshot (PUT form)
    question: How do I back up my cluster's indices to a snapshot repository with a PUT request?
  - id: snapshot-create-1
    intent: Take a snapshot (POST form)
    question: Is there a POST variant for creating a snapshot of data streams and indices?
  - id: snapshot-delete
    intent: Delete snapshots
    question: How do I delete old snapshots from a repository?
  - id: snapshot-get-repository-1
    intent: Get settings of named snapshot repositories
    question: How do I see the type and settings of one specific snapshot repository?
  - id: snapshot-create-repository
    intent: Register or update a snapshot repository (PUT)
    question: How do I register a new snapshot repository with a PUT request?
  phrasing_ops: 18
  slug: elk-stack-snapshot-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Spaces API from Elastic Stack (ELK Stack) — 7 operation(s) for spaces.
  name: Elastic Stack (ELK Stack) Spaces API
  phrasing_intents:
  - id: post-spaces-resolve-copy-saved-objects-errors
    intent: Resolve conflicts from copying saved objects
    question: What do I do when copying a dashboard to another space fails with conflicts?
  - id: post-spaces-copy-saved-objects
    intent: Copy saved objects to other spaces
    question: How do I copy a Kibana dashboard into another space?
  - id: post-spaces-disable-legacy-url-aliases
    intent: Disable legacy URL aliases
    question: Can I stop old saved object URLs from redirecting to their new targets?
  - id: post-spaces-get-shareable-references
    intent: Collect shareable references for saved objects
    question: Which related objects and spaces would be involved if I share a saved object?
  - id: post-spaces-update-objects-spaces
    intent: Share or unshare saved objects across spaces
    question: Can I share one saved object into multiple spaces without copying it?
  - id: get-spaces-space
    intent: List Kibana spaces
    question: Which Kibana spaces can I access?
  - id: post-spaces-space
    intent: Create a Kibana space
    question: How do I create a new Kibana space for my team?
  - id: delete-spaces-space-id
    intent: Delete a Kibana space
    question: Does deleting a space also delete its dashboards and other saved objects?
  phrasing_ops: 10
  slug: elk-stack-spaces-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The sql API from Elastic Stack (ELK Stack) — 6 operation(s) for sql.
  name: Elastic Stack (ELK Stack) Sql API
  phrasing_intents:
  - id: sql-clear-cursor
    intent: Close an SQL search cursor
    question: How do I release an SQL pagination cursor I'm done with?
  - id: sql-delete-async
    intent: Delete or cancel an async SQL search
    question: How do I cancel an async SQL search that is still running?
  - id: sql-get-async
    intent: Get results of an async SQL search
    question: How do I fetch the results of an async SQL query I started earlier?
  - id: sql-get-async-status
    intent: Check the status of an async SQL search
    question: Is my async SQL search still running or has it completed?
  - id: sql-query-1
    intent: Run an SQL query with a GET request
    question: Can I send an SQL query to Elasticsearch using a GET request with a body?
  - id: sql-query
    intent: Run an SQL query against Elasticsearch
    question: How do I query my Elasticsearch indices with SQL?
  - id: sql-translate-1
    intent: Translate SQL into Query DSL via GET
    question: Can I use a GET request to see the Query DSL that an SQL statement becomes?
  - id: sql-translate
    intent: Translate SQL into Elasticsearch Query DSL
    question: How do I convert an SQL statement into the equivalent Elasticsearch search request?
  phrasing_ops: 8
  slug: elk-stack-sql-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Stack API from Elastic Stack (ELK Stack) — 3 operation(s) for stack.
  name: Elastic Stack (ELK Stack) Stack API
  phrasing_intents:
  - id: get-instance-types
    intent: List instance types (deprecated)
    question: Which instance types are available for deployments?
  - id: get-version-stacks
    intent: List available Elastic Stack versions
    question: Which Elastic Stack versions can I deploy?
  - id: update-stack-packs
    intent: Upload an Elastic Stack pack
    question: How do I upload a new stack pack so a version becomes available?
  - id: get-version-stack
    intent: Get an Elastic Stack version
    question: How do I see the template and details of one stack version?
  - id: update-version-stack
    intent: Update an Elastic Stack version configuration
    question: How do I change the Elasticsearch and Kibana settings of a stack version?
  - id: delete-version-stack
    intent: Remove an Elastic Stack version from the list
    question: How do I hide a stack version from the available versions?
  phrasing_ops: 6
  slug: elk-stack-stack-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The streams API from Elastic Stack (ELK Stack) — 16 operation(s) for streams.
  name: Elastic Stack (ELK Stack) Streams API
  phrasing_intents:
  - id: streams-logs-disable
    intent: Turn off a named stream type on the cluster
    question: How do I switch off the logs stream feature at the Elasticsearch cluster level?
  - id: streams-logs-enable
    intent: Turn on a named stream type on the cluster
    question: How do I turn on the logs stream feature directly in Elasticsearch?
  - id: streams-status
    intent: Check which stream types are enabled
    question: Are logs streams currently enabled on my Elasticsearch cluster?
  - id: get-streams
    intent: List all streams
    question: What streams exist in my Kibana space?
  - id: post-streams-disable
    intent: Disable wired streams in Kibana
    question: What happens to my data if I disable wired streams in Kibana?
  - id: post-streams-enable
    intent: Enable wired streams in Kibana
    question: How do I turn on wired streams from Kibana?
  - id: post-streams-resync
    intent: Resync streams with Elasticsearch assets
    question: How do I make sure the Elasticsearch assets behind my streams are up to date?
  - id: delete-streams-name
    intent: Delete a stream and its data stream
    question: How do I delete a stream along with its underlying data stream?
  phrasing_ops: 21
  slug: elk-stack-streams-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The synonyms API from Elastic Stack (ELK Stack) — 3 operation(s) for synonyms.
  name: Elastic Stack (ELK Stack) Synonyms API
  phrasing_intents:
  - id: synonyms-get-synonym
    intent: Get the rules in a synonym set
    question: What synonym rules are in a particular synonym set?
  - id: synonyms-put-synonym
    intent: Create or replace a synonym set
    question: How do I create a synonym set for my search analyzer?
  - id: synonyms-delete-synonym
    intent: Delete a synonym set
    question: How do I delete a synonym set?
  - id: synonyms-get-synonym-rule
    intent: Get a single synonym rule
    question: What does one specific rule in a synonym set say?
  - id: synonyms-put-synonym-rule
    intent: Create or update a single synonym rule
    question: How do I add or change one synonym rule without resending the whole set?
  - id: synonyms-delete-synonym-rule
    intent: Delete a single synonym rule
    question: How do I remove one rule from a synonym set?
  - id: synonyms-get-synonyms-sets
    intent: List all synonym sets
    question: Which synonym sets are defined in my cluster?
  phrasing_ops: 7
  slug: elk-stack-synonyms-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Synthetics APIs enable you to check the status of your services and applications.
  name: Elastic Stack (ELK Stack) Synthetics API
  phrasing_intents:
  - id: post-synthetics-monitor-test
    intent: Run an on-demand test of a monitor
    question: Can I trigger a synthetic monitor to run right now instead of waiting for its schedule?
  - id: get-synthetic-monitors
    intent: List synthetic monitors
    question: Which uptime and synthetic monitors do I have configured?
  - id: post-synthetic-monitors
    intent: Create a synthetic monitor
    question: How do I set up a new HTTP uptime check for my site?
  - id: delete-synthetic-monitors
    intent: Delete several monitors at once
    question: How do I remove a batch of synthetic monitors in one request?
  - id: delete-synthetic-monitor
    intent: Delete a synthetic monitor
    question: How do I remove a single monitor from the Synthetics app?
  - id: get-synthetic-monitor
    intent: Get a synthetic monitor
    question: How do I view the full configuration of a single monitor?
  - id: put-synthetic-monitor
    intent: Update a synthetic monitor
    question: Can I change just one field of a monitor, like its schedule, without resending everything?
  - id: get-parameters
    intent: List Synthetics parameters
    question: What global parameters are defined for my synthetic monitors?
  phrasing_ops: 18
  slug: elk-stack-synthetics-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Get information about the system status, resource usage, features, and installed plugins.
  name: Elastic Stack (ELK Stack) System API
  phrasing_intents:
  - id: get-features
    intent: List Kibana features
    question: Which Kibana features can I grant or hide in spaces and roles?
  - id: get-status
    intent: Check Kibana's health status
    question: Is Kibana up and healthy right now?
  phrasing_ops: 2
  slug: elk-stack-system-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Tags API from Elastic Stack (ELK Stack) — 2 operation(s) for tags.
  name: Elastic Stack (ELK Stack) Tags API
  phrasing_intents:
  - id: get-tags
    intent: Search Kibana tags
    question: What tags have been created in Kibana?
  - id: post-tags
    intent: Create a tag
    question: How do I create a new tag for organizing dashboards?
  - id: delete-tags-id
    intent: Delete a tag
    question: How do I remove a tag I no longer use?
  - id: get-tags-id
    intent: Get a tag
    question: What name and color does a specific tag have?
  - id: put-tags-id
    intent: Create or update a tag by ID
    question: Can I rename or recolor a tag I already have?
  phrasing_ops: 5
  slug: elk-stack-tags-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Task manager APIs enable you to check the health of the Kibana task manager, which is used by features such as alerting, actions, and reporting to run mission critical work as persistent background ta
  name: Elastic Stack (ELK Stack) task manager API
  phrasing_intents:
  - id: task-manager-health
    intent: Check Kibana task manager health
    question: Is the Kibana task manager healthy and keeping up with its workload?
  phrasing_ops: 1
  slug: elk-stack-task-manager-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The tasks API from Elastic Stack (ELK Stack) — 4 operation(s) for tasks.
  name: Elastic Stack (ELK Stack) Tasks API
  phrasing_intents:
  - id: tasks-cancel
    intent: Cancel tasks matching filters
    question: How do I cancel every running reindex task across the cluster at once?
  - id: tasks-cancel-1
    intent: Cancel a specific task by ID
    question: How do I cancel one long-running Elasticsearch task when I know its ID?
  - id: tasks-get
    intent: Get information about a task
    question: What is the progress of a specific running task in my cluster?
  - id: tasks-list
    intent: List running tasks in the cluster
    question: Which tasks are currently running on my Elasticsearch nodes?
  phrasing_ops: 4
  slug: elk-stack-tasks-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Telemetry API from Elastic Stack (ELK Stack) — 1 operation(s) for telemetry.
  name: Elastic Stack (ELK Stack) Telemetry API
  phrasing_intents:
  - id: get-telemetry-config
    intent: Check whether ECE telemetry is enabled
    question: Is my Elastic Cloud Enterprise installation sending telemetry?
  - id: set-telemetry-config
    intent: Turn ECE telemetry on or off
    question: Can I opt out of ECE telemetry?
  phrasing_ops: 2
  slug: elk-stack-telemetry-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The text_structure API from Elastic Stack (ELK Stack) — 4 operation(s) for text_structure.
  name: Elastic Stack (ELK Stack) Text Structure API
  phrasing_intents:
  - id: text-structure-find-field-structure
    intent: Detect the structure of an indexed text field
    question: Can Elasticsearch work out the format of log lines already in an index?
  - id: text-structure-find-message-structure
    intent: Detect the structure of text messages via GET
    question: Can I infer the format of a list of log messages before ingesting them?
  - id: text-structure-find-message-structure-1
    intent: Detect the structure of text messages via POST
    question: What ingest pipeline would suit a batch of sample messages?
  - id: text-structure-find-structure
    intent: Detect the structure of a text file
    question: Can Elasticsearch figure out the format of a CSV or log file for me?
  - id: text-structure-test-grok-pattern
    intent: Test a Grok pattern via GET
    question: Does my Grok pattern match these log lines?
  - id: text-structure-test-grok-pattern-1
    intent: Test a Grok pattern via POST
    question: Can I POST a Grok pattern and see match offsets for each line?
  phrasing_ops: 6
  slug: elk-stack-text-structure-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The transform API from Elastic Stack (ELK Stack) — 13 operation(s) for transform.
  name: Elastic Stack (ELK Stack) Transform API
  phrasing_intents:
  - id: transform-get-transform
    intent: Get a transform's configuration
    question: What source, destination and pivot does a particular transform use?
  - id: transform-put-transform
    intent: Create a transform
    question: How do I pivot raw events into an entity-centric summary index?
  - id: transform-delete-transform
    intent: Delete a transform
    question: Can I delete a transform and its destination index together?
  - id: transform-get-node-stats
    intent: Get transform usage per node
    question: How are transforms distributed across my cluster's nodes?
  - id: transform-get-transform-1
    intent: List all transforms
    question: Which transforms exist in my cluster?
  - id: transform-get-transform-stats
    intent: Get a transform's stats
    question: Is my transform running, and how many documents has it processed?
  - id: transform-preview-transform
    intent: Preview an existing transform's output
    question: What results would an existing transform produce right now?
  - id: transform-preview-transform-1
    intent: Preview an existing transform via POST
    question: Can I preview a saved transform using a POST request?
  phrasing_ops: 17
  slug: elk-stack-transform-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The TrustedEnvironments API from Elastic Stack (ELK Stack) — 1 operation(s) for trustedenvironments.
  name: Elastic Stack (ELK Stack) Trusted Environments API
  phrasing_intents:
  - id: get-trusted-envs
    intent: List an organization's trusted environments
    question: Which environments does my organization trust for cross-cluster connections?
  phrasing_ops: 1
  slug: elk-stack-trustedenvironments-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: 'The Kibana Upgrade Assistant API helps you prepare for the next major Elasticsearch release. > warn > This is a Kibana REST API (not an Elasticsearch API) and requests must target your Kibana URL: > *'
  name: Elastic Stack (ELK Stack) Upgrade API
  phrasing_intents:
  - id: get-upgrade-status
    intent: Check cluster upgrade readiness
    question: Is my cluster ready to upgrade to the next major version?
  phrasing_ops: 1
  slug: elk-stack-upgrade-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Uptime APIs enable you to view and update uptime monitoring settings.
  name: Elastic Stack (ELK Stack) Uptime API
  phrasing_intents:
  - id: get-uptime-settings
    intent: Get uptime monitoring settings
    question: What certificate expiration threshold is uptime monitoring using?
  - id: put-uptime-settings
    intent: Update uptime monitoring settings
    question: How do I get warned earlier before TLS certificates expire?
  phrasing_ops: 2
  slug: elk-stack-uptime-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Enables you to invalidate user sessions for security and session management purposes.
  name: Elastic Stack (ELK Stack) user session API
  phrasing_intents:
  - id: post-security-session-invalidate
    intent: Invalidate Kibana user sessions
    question: Can I force-log-out users by invalidating their Kibana sessions?
  phrasing_ops: 1
  slug: elk-stack-user-session-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The UserRoleAssignments API from Elastic Stack (ELK Stack) — 1 operation(s) for userroleassignments.
  name: Elastic Stack (ELK Stack) User Role Assignments API
  phrasing_intents:
  - id: add-role-assignments
    intent: Grant role assignments to a user
    question: How do I give a user a deployment-scoped role in Elastic Cloud?
  - id: remove-role-assignments
    intent: Revoke role assignments from a user
    question: How do I take a deployment role away from a user?
  phrasing_ops: 2
  slug: elk-stack-userroleassignments-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The Users API from Elastic Stack (ELK Stack) — 3 operation(s) for users.
  name: Elastic Stack (ELK Stack) Users API
  phrasing_intents:
  - id: get-current-user
    intent: Get my own user information
    question: Which user am I logged in as, and what are my details?
  - id: update-current-user
    intent: Update my own user profile
    question: How do I change my own full name or email?
  - id: get-users
    intent: List all users
    question: Who has a user account on the platform?
  - id: create-user
    intent: Create a new user
    question: How do I add a new user with a password and roles?
  - id: get-user
    intent: Get a single user by name
    question: What roles and details does a particular user have?
  - id: delete-user
    intent: Delete a user
    question: How do I remove a user account permanently?
  - id: update-user
    intent: Update another user's account
    question: How do I change the roles or email of another user?
  phrasing_ops: 7
  slug: elk-stack-users-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: '> This documentation is temporarily hosted at a separate location. > > **[View the full Visualizations API reference →](https://elastic.github.io/dashboards-api-spec/visualizations#tag/Visualizations)'
  name: Elastic Stack (ELK Stack) Visualizations API
  phrasing_intents:
  - id: search-visualizations
    intent: Search visualizations
    question: Which saved visualizations exist in Kibana?
  - id: create-visualization
    intent: Create a visualization
    question: How do I create a new Kibana visualization programmatically?
  - id: get-visualization
    intent: Get a visualization
    question: Where can I fetch the definition of one visualization?
  - id: upsert-visualization
    intent: Create or replace a visualization by ID
    question: Can I create or overwrite a visualization at a known ID in one call?
  - id: delete-visualization
    intent: Delete a visualization
    question: Is there a way to delete a visualization I no longer need?
  phrasing_ops: 5
  slug: elk-stack-visualizations-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The watcher API from Elastic Stack (ELK Stack) — 13 operation(s) for watcher.
  name: Elastic Stack (ELK Stack) Watcher API
  phrasing_intents:
  - id: watcher-ack-watch
    intent: Acknowledge all actions of a watch (PUT)
    question: How do I acknowledge a watch with a PUT request so its actions stop firing?
  - id: watcher-ack-watch-1
    intent: Acknowledge all actions of a watch (POST)
    question: How do I acknowledge an entire watch using a POST request?
  - id: watcher-ack-watch-2
    intent: Acknowledge one action of a watch (PUT)
    question: Can I acknowledge just one action of a watch with a PUT request?
  - id: watcher-ack-watch-3
    intent: Acknowledge one action of a watch (POST)
    question: How do I acknowledge a single named action of a watch using POST?
  - id: watcher-activate-watch
    intent: Activate a watch (PUT)
    question: How do I turn an inactive watch back on with a PUT request?
  - id: watcher-activate-watch-1
    intent: Activate a watch (POST)
    question: How do I activate a watch with a POST request?
  - id: watcher-deactivate-watch
    intent: Deactivate a watch (PUT)
    question: How do I pause a watch with a PUT request without deleting it?
  - id: watcher-deactivate-watch-1
    intent: Deactivate a watch (POST)
    question: How do I deactivate a watch with a POST request?
  phrasing_ops: 24
  slug: elk-stack-watcher-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: Workflows enable you to automate multi-step processes directly in Kibana. Define sequences of steps in YAML to transform data insights into automated actions and outcomes, without needing external aut
  name: Elastic Stack (ELK Stack) Workflows API
  phrasing_intents:
  - id: delete-workflows
    intent: Delete several workflows at once
    question: How do I delete a batch of workflows by their IDs in one call?
  - id: get-workflows
    intent: List and search workflows
    question: How do I list the automation workflows defined in my Kibana space?
  - id: post-workflows
    intent: Create several workflows at once
    question: Can I import a batch of workflow definitions in a single request?
  - id: get-workflows-aggs
    intent: Aggregate workflows by field
    question: How many workflows do I have per tag or per creator?
  - id: get-workflows-connectors
    intent: List connectors available to workflows
    question: Which connectors can my workflow steps call?
  - id: get-workflows-executions-executionid
    intent: Get a workflow execution
    question: How do I check the status of one workflow run?
  - id: post-workflows-executions-executionid-cancel
    intent: Cancel a workflow execution
    question: How do I stop a single workflow run that's stuck or running too long?
  - id: get-workflows-executions-executionid-children
    intent: List child executions of a workflow run
    question: Which sub-workflow runs did a parent workflow execution spawn?
  phrasing_ops: 31
  slug: elk-stack-workflows-api
- baseURL: https://{elasticsearch_endpoint}
  baseurl_source: declared
  description: The xpack API from Elastic Stack (ELK Stack) — 2 operation(s) for xpack.
  name: Elastic Stack (ELK Stack) Xpack API
  phrasing_intents:
  - id: xpack-info
    intent: Get build, license and feature info
    question: Which license is installed on my cluster and which features does it enable?
  - id: xpack-usage
    intent: Get feature usage statistics
    question: How much are the licensed features on my cluster actually being used?
  phrasing_ops: 2
  slug: elk-stack-xpack-api
- baseURL: https://api.elastic-cloud.com/api/v1
  baseurl_source: declared
  description: The Index API from Elastic Stack — 3 operation(s) for index.
  name: Elastic Stack Index API
  slug: elk-stack-index-api
artifact_total: 152
asyncapis:
- description: ''
  name: Elk Stack Webhooks
  slug: elk-stack-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Elasticsearch REST Cat API
  slug: open-elk-stack-cat-api
- collection_type: open
  name: Elasticsearch REST Cat Cluster API
  slug: open-elk-stack-cluster-api
- collection_type: open
  name: Elasticsearch REST Cat Document API
  slug: open-elk-stack-document-api
- collection_type: open
  name: Elasticsearch REST Cat Index API
  slug: open-elk-stack-index-api
- collection_type: open
  name: Elasticsearch REST Cat Ingest API
  slug: open-elk-stack-ingest-api
- collection_type: open
  name: Elasticsearch REST Cat Search API
  slug: open-elk-stack-search-api
- collection_type: open
  name: Elasticsearch REST Cat Snapshot API
  slug: open-elk-stack-snapshot-api
- collection_type: open
  name: Elasticsearch REST API
  slug: open-elk-stack
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/elastic/elasticsearch-specification/blob/main/LICENSE
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/capabilities/elk-stack-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/elk-stack-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/overlays/elk-stack-elasticsearch-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elk-stack-elasticsearch-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/overlays/elk-stack-kibana-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elk-stack-kibana-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.elastic.co/elastic-stack/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.elastic.co/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.elastic.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.elastic.co/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.elastic.co/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.elastic.co/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://discuss.elastic.co/
- group: company
  title: ''
  type: Blog
  url: https://www.elastic.co/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elastic
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elastic.co/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.elastic.co/cloud/elasticsearch-service/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elastic.co/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elastic.co/legal/privacy-statement
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elastic-co
- group: operate
  title: ''
  type: StatusPage
  url: https://status.elastic.co/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/llms/elk-stack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elk-stack-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/packages/elk-stack-packages.yml
  title: ''
  type: Packages
  url: packages/elk-stack-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/packages/elk-stack-packages.yml
  title: ''
  type: SDKs
  url: packages/elk-stack-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/cli/elk-stack-cli.yml
  title: ''
  type: CLI
  url: cli/elk-stack-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/components/elk-stack-components.yml
  title: ''
  type: Components
  url: components/elk-stack-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/well-known/elk-stack-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elk-stack-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/well-known/elk-stack-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/elk-stack-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/mcp/elk-stack-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/elk-stack-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/mcp/elk-stack-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/elk-stack-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/asyncapi/elk-stack-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/elk-stack-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/conformance/elk-stack-conformance.yml
  title: ''
  type: Conformance
  url: conformance/elk-stack-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/security/elk-stack-trust-center.yml
  title: ''
  type: Compliance
  url: security/elk-stack-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/errors/elk-stack-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/elk-stack-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/lifecycle/elk-stack-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/elk-stack-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/lifecycle/elk-stack-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/elk-stack-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/changelog/elk-stack-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/elk-stack-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/conventions/elk-stack-conventions.yml
  title: ''
  type: Conventions
  url: conventions/elk-stack-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/conventions/elk-stack-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/elk-stack-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/data-model/elk-stack-data-model.yml
  title: ''
  type: DataModel
  url: data-model/elk-stack-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/sandbox/elk-stack-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/elk-stack-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/plans/elk-stack-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elk-stack-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/rate-limits/elk-stack-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/elk-stack-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/authentication/elk-stack-authentication.yml
  title: ''
  type: Authentication
  url: authentication/elk-stack-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/security/elk-stack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elk-stack-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/security/elk-stack-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/elk-stack-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/security/elk-stack-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/elk-stack-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/security/elk-stack-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/elk-stack-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/agentic-access/elk-stack-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/elk-stack-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/finops/elk-stack-finops.yml
  title: ''
  type: FinOps
  url: finops/elk-stack-finops.yml
created: '2024-01-01'
description: 'The Elastic Stack (formerly known as the ELK Stack) is the collection of open-source products from Elastic — Elasticsearch, Logstash, Kibana, and Beats/Elastic Agent — designed for taking data from any source, in any format, and searching, analyzing, and visualizing it in real time. It is widely used for log management, observability, security analytics (SIEM), and increasingly as a vector database and retrieval layer for RAG and agentic AI applications. Elastic publishes machine-readable OpenAPI descriptions for all three of its programmable surfaces: the Elasticsearch REST API, the Kibana APIs, and the Elastic Cloud control-plane API. The stack is deployment-hosted — self-managed, Elastic Cloud Hosted, or Elastic Cloud Serverless — so the Elasticsearch and Kibana base URLs are always specific to the customer''s own cluster or project.'
finops:
- name: Elk Stack Finops
  service_category: API
  slug: elk-stack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elk-stack.png
layout: provider
mcp_servers:
- description: Remote MCP server at {kibana_url} requiring an API key; 6 tools listed.
  name: Elastic Stack MCP Server
  slug: elk-stack-mcp-yml
modified: '2026-08-27'
name: Elastic Stack
nav: Providers
network: true
overview: 'Elastic Stack publishes 133 APIs on the [APIs.io](https://apis.io/) network, including Elastic Cloud API, (ELK Stack) Accounts API, (ELK Stack) Actions API, and 130 more. Tagged areas include Analytics, Logging, Monitoring, Observability, and Search.


  The Elastic Stack catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Elastic Stack''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 42 more developer resources.'
plans:
- name: Elk Stack Plans Pricing
  plan_count: 4
  slug: elk-stack-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Elk Stack Rate Limits
  slug: elk-stack-rate-limits
score:
  band: exemplar
  composite: 78.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 56.6
    developer_ergonomics: 80.4
    discoverability: 75.0
    operational_transparency: 60.5
  previous_composite: 76.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 132
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 100.0
screenshot: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/screenshots/elk-stack-2026-06-20T180610.png
security:
- kind: authentication
  name: Elk Stack Authentication
  slug: elk-stack-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Elk Stack Domain Security
  slug: elk-stack-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Elk Stack Vulnerability Disclosure
  slug: elk-stack-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Elk Stack Trust Center
  slug: elk-stack-trust-center
  summary_line: FedRAMP High, FedRAMP Moderate, PCI DSS (Level 1 Service Provider), CSA STAR, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, SOC 2, SOC 3, TISAX, HIPAA, Cyber Essentials Plus, IRAP Assessed — Protected B, GDPR
slug: elk-stack
tags:
- Analytics
- Logging
- Monitoring
- Observability
- Search
- Security
- Vector Database
- SIEM
- Machine Learning
- Vector Search
website: https://www.elastic.co/elastic-stack/
---
