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
  trial: false
  try_now: true
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
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 234
  human_in_the_loop: 33
  name: Statsig Agentic Access
  operation_count: 384
  slug: statsig-agentic-access
  summary_line: 384 operations · 234 acting · 33 human-in-the-loop
api_count: 4
apis:
- baseURL: https://events.statsigapi.net
  baseurl_source: declared
  description: The Statsig Events API handles the ingestion of event data from both client and server SDKs. It receives exposure events, custom events, and diagnostic data at the events.statsigapi.net endpoint. This
  name: Statsig Events API
  phrasing_intents:
  - id: logEvent
    intent: Log custom events for analytics
    question: How do I send custom events to Statsig for experiment analysis?
  - id: getConsoleV1Events
    intent: List recently logged events
    question: What events has my project received recently?
  - id: getConsoleV1EventsByEventName
    intent: See recent occurrences of one event
    question: Is a specific event like checkout_complete actually arriving?
  - id: getConsoleV1EventsByEventNameMetrics
    intent: Find metrics built on an event
    question: Which metrics are derived from a given event?
  phrasing_ops: 4
  slug: events-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Access audit log entries tracking changes made to project configuration through the console or API.
  name: statsig Audit Logs API
  phrasing_intents:
  - id: listAuditLogs
    intent: List audit log entries for project changes
    question: Who changed our feature flag and experiment configuration in Statsig recently?
  - id: getConsoleV1AuditLogs
    intent: Search audit logs by date, action or tag
    question: Can I filter the audit log to a date range?
  phrasing_ops: 2
  slug: statsig-audit-logs-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage autotune configurations that automatically optimize parameter values based on a target metric.
  name: statsig Autotunes API
  phrasing_intents:
  - id: listAutotunes
    intent: List autotune configurations
    question: Which autotunes are set up in my Statsig project?
  - id: createAutotune
    intent: Create an autotune that optimizes toward a metric
    question: How do I set up an autotune that automatically picks the best variant?
  - id: getConsoleV1Autotunes
    intent: Page through autotunes via the Console API
    question: Can I page through our autotune experiments through the Console API v1?
  - id: postConsoleV1Autotunes
    intent: Create an autotune that optimizes a success event
    question: Can I create an autotune that optimizes for an event such as a purchase?
  - id: getConsoleV1AutotunesById
    intent: Read one autotune
    question: What variants and success event is a particular autotune using?
  - id: postConsoleV1AutotunesById
    intent: Fully replace an autotune's settings
    question: Can I resend every setting of an autotune in one update?
  - id: patchConsoleV1AutotunesById
    intent: Change selected settings on an autotune
    question: Can I change just the winner threshold of a running autotune?
  - id: deleteConsoleV1AutotunesById
    intent: Delete an autotune
    question: Can I permanently remove an autotune I no longer need?
  phrasing_ops: 26
  slug: statsig-autotunes-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Endpoints for downloading full project configuration specs for server-side local evaluation.
  name: statsig Configuration API
  phrasing_intents:
  - id: downloadConfigSpecs
    intent: Download project config specs for local evaluation
    question: How does a server SDK get all gate, config, experiment and layer definitions for local evaluation?
  phrasing_ops: 1
  slug: statsig-configuration-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage dynamic configurations with full CRUD operations for server-driven configuration values.
  name: statsig Dynamic Configs API
  phrasing_intents:
  - id: listDynamicConfigs
    intent: List dynamic configs in the project
    question: Which dynamic configs exist in my Statsig project?
  - id: createDynamicConfig
    intent: Create a dynamic config
    question: How do I create a new dynamic config with default values?
  - id: getDynamicConfig
    intent: Get a dynamic config's full definition
    question: What default values and conditions does a particular dynamic config have?
  - id: partiallyUpdateDynamicConfig
    intent: Update fields on an existing dynamic config
    question: Can I turn off an existing dynamic config without changing its rules?
  - id: deleteDynamicConfig
    intent: Delete a dynamic config
    question: How do I permanently remove a dynamic config we no longer use?
  - id: getDynamicConfigRules
    intent: List the rules on a dynamic config
    question: What targeting rules are configured on a given dynamic config?
  - id: getConfig
    intent: Evaluate a dynamic config for a user
    question: What config values would a specific user receive from a dynamic config?
  - id: getConsoleV1DynamicConfigs
    intent: Filter dynamic configs by team, tag or lifecycle
    question: Which of our dynamic configs are flagged as stale by the nightly check?
  phrasing_ops: 31
  slug: statsig-dynamic-configs-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage A/B test experiments including creation, configuration, starting, resetting, and analysis.
  name: statsig Experiments API
  phrasing_intents:
  - id: listExperiments
    intent: List experiments and their status
    question: Which experiments are running or set up in my Statsig project?
  - id: createExperiment
    intent: Create an A/B experiment
    question: How do I set up a new A/B test with a hypothesis and groups?
  - id: getExperiment
    intent: Get an experiment's full setup
    question: What groups, parameters and hypothesis does a specific experiment have?
  - id: partiallyUpdateExperiment
    intent: Update fields on an existing experiment
    question: Can I change the allocation of an experiment that already exists?
  - id: deleteExperiment
    intent: Delete an experiment
    question: How do I permanently remove an experiment from the project?
  - id: startExperiment
    intent: Start an experiment
    question: How do I start an experiment so users begin getting assigned to groups?
  - id: resetExperiment
    intent: Reset an experiment and clear its data
    question: Can I wipe an experiment's collected data and start its assignments over?
  - id: postGetExperiment
    intent: Get a user's experiment group assignment
    question: Which experiment group is a particular user assigned to?
  phrasing_ops: 66
  slug: statsig-experiments-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Endpoints for evaluating feature gates for users, returning boolean pass/fail values along with rule identification.
  name: statsig Feature Gates API
  phrasing_intents:
  - id: checkGate
    intent: Check whether a user passes a feature gate
    question: Does a specific user pass a given feature gate?
  - id: checkGateMultiple
    intent: Check several feature gates for a user at once
    question: Can I evaluate several feature gates for one user in a single request?
  phrasing_ops: 2
  slug: statsig-feature-gates-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage feature gates including creation, updates, rules, overrides, enabling, disabling, launching, and archiving.
  name: statsig Gates API
  phrasing_intents:
  - id: listGates
    intent: List feature gates and their status
    question: Which feature gates exist in my Statsig project?
  - id: createGate
    intent: Create a feature gate
    question: How do I create a new feature flag?
  - id: getGate
    intent: Get a feature gate's full configuration
    question: What rules, conditions and overrides does a particular feature gate have?
  - id: partiallyUpdateGate
    intent: Update fields on an existing feature gate
    question: Can I change the description or tags on an existing feature gate?
  - id: deleteGate
    intent: Delete a feature gate
    question: Can a deleted feature gate be recovered afterward?
  - id: enableGate
    intent: Enable a feature gate
    question: How do I turn a feature gate back on so its rules are evaluated?
  - id: disableGate
    intent: Disable a feature gate
    question: Can I kill-switch a feature so the gate returns false for everyone?
  - id: launchGate
    intent: Mark a feature gate as fully launched
    question: How do I mark a feature as fully rolled out so its gate can be cleaned up?
  phrasing_ops: 56
  slug: statsig-gates-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage holdout groups that exclude users from receiving specific features for measuring long-term impact.
  name: statsig Holdouts API
  phrasing_intents:
  - id: listHoldouts
    intent: List holdout groups
    question: Which holdout groups are set up in my Statsig project?
  - id: createHoldout
    intent: Create a holdout group
    question: How do I hold back a group of users to measure the long-term impact of features?
  - id: getConsoleV1Holdouts
    intent: Filter and page through holdouts
    question: Can I filter holdouts by who created them or by tag?
  - id: postConsoleV1Holdouts
    intent: Create a holdout for a team and unit type
    question: Can I create a holdout keyed on a custom unit ID type instead of user ID?
  - id: getConsoleV1HoldoutsById
    intent: Get one holdout's details
    question: What gates and experiments does a given holdout apply to?
  - id: postConsoleV1HoldoutsById
    intent: Replace a holdout's full configuration
    question: How do I overwrite every setting on a holdout in one request?
  - id: patchConsoleV1HoldoutsById
    intent: Change selected holdout settings
    question: Can I change just the pass percentage on a holdout without resending everything?
  - id: deleteConsoleV1HoldoutsById
    intent: Delete a holdout
    question: Can I permanently remove a holdout we no longer need?
  phrasing_ops: 13
  slug: statsig-holdouts-api
- baseURL: https://api.statsig.com
  baseurl_source: declared
  description: Endpoints for initializing client SDKs with all evaluated feature gates, configs, experiments, and layers for a given user.
  name: statsig Initialization API
  phrasing_intents:
  - id: initialize
    intent: Get all evaluated flags and configs for a user
    question: How does a client SDK get every gate, config, experiment and layer value for a user at startup?
  phrasing_ops: 1
  slug: statsig-initialization-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage API keys for the project including server secret keys, client SDK keys, and console API keys.
  name: statsig Keys API
  phrasing_intents:
  - id: listKeys
    intent: List the project's API keys
    question: Which server secret, client SDK and console API keys does my Statsig project have?
  - id: getConsoleV1Keys
    intent: List keys by target app or environment
    question: Which keys are scoped to a given target app?
  - id: postConsoleV1Keys
    intent: Create an API key
    question: How do I generate a new server secret or client key?
  - id: getConsoleV1KeysById
    intent: Read one API key
    question: What scopes and environments does a specific key have?
  - id: patchConsoleV1KeysById
    intent: Update a key's scopes or environments
    question: Can I change the scopes on an existing key?
  - id: deleteConsoleV1KeysById
    intent: Delete an API key
    question: Can I permanently delete a key that leaked?
  - id: patchConsoleV1KeysByIdDeactivate
    intent: Deactivate an API key
    question: Can I switch off a key without deleting it?
  - id: patchConsoleV1KeysByIdRotate
    intent: Rotate an API key
    question: What's the process for rotating a key's secret value?
  phrasing_ops: 8
  slug: statsig-keys-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage layers that enable sharing parameters across multiple experiments while maintaining mutual exclusivity.
  name: statsig Layers API
  phrasing_intents:
  - id: listLayers
    intent: List layers in the project
    question: Which layers exist in my Statsig project?
  - id: createLayer
    intent: Create a layer for shared experiment parameters
    question: How do I create a layer so several experiments can share parameters?
  - id: getLayer
    intent: Get a layer's configuration
    question: What parameters and experiments are defined on a specific layer?
  - id: deleteLayer
    intent: Delete a layer
    question: How do I permanently remove a layer we no longer use?
  - id: listLayerExperiments
    intent: List the experiments in a layer
    question: Which experiments are running inside a particular layer?
  - id: postGetLayer
    intent: Get a user's parameter values from a layer
    question: What layer parameter values does a specific user receive?
  - id: getConsoleV1Layers
    intent: List layers via the Console API v1
    question: Can the Console API v1 list all layers in the project?
  - id: postConsoleV1Layers
    intent: Create a layer with an ID type
    question: Which ID type must I choose when creating a layer?
  phrasing_ops: 19
  slug: statsig-layers-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Access and manage metric definitions and metric sources used in experiment analysis.
  name: statsig Metrics API
  phrasing_intents:
  - id: listMetrics
    intent: List metric definitions
    question: Which metrics are defined in my Statsig project?
  - id: getMetric
    intent: Get a metric's definition
    question: How is a specific metric defined?
  - id: getConsoleV1Metrics
    intent: Read a metric's value for one day
    question: What was a metric's value on a specific date?
  - id: postConsoleV1Metrics
    intent: Create a metric
    question: Can I define a new ratio or funnel metric through the API?
  - id: getConsoleV1MetricsById
    intent: Read a metric definition via Console API v1
    question: Can the Console API v1 return a metric's full definition by its ID?
  - id: postConsoleV1MetricsById
    intent: Update a metric's definition
    question: Can I mark an existing metric as verified?
  - id: deleteConsoleV1MetricsById
    intent: Delete a metric
    question: Can I permanently delete a metric definition?
  - id: putConsoleV1MetricsByIdCancelArchive
    intent: Cancel a scheduled metric archive
    question: Can I stop a metric that's scheduled for archiving from being archived?
  phrasing_ops: 22
  slug: statsig-metrics-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage user segments for targeting rules across gates, configs, and experiments.
  name: statsig Segments API
  phrasing_intents:
  - id: listSegments
    intent: List user segments
    question: Which user segments exist in my Statsig project?
  - id: createSegment
    intent: Create a user segment
    question: How do I create a reusable user segment for targeting?
  - id: getSegment
    intent: Get a segment's configuration
    question: What rules define membership in a specific segment?
  - id: partiallyUpdateSegment
    intent: Update an existing user segment
    question: Can I change the membership rules of an existing segment?
  - id: deleteSegment
    intent: Delete a user segment
    question: How do I permanently remove a segment we no longer target?
  - id: getConsoleV1Segments
    intent: List segments via the Console API v1
    question: Can the Console API v1 list every segment in the project?
  - id: postConsoleV1Segments
    intent: Create a segment with an ID type and tags
    question: Can I set a custom ID for a new segment instead of using its name?
  - id: getConsoleV1SegmentsById
    intent: Get a segment via the Console API v1
    question: Can the Console API v1 return one segment's details?
  phrasing_ops: 20
  slug: statsig-segments-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Tags API from statsig — 1 operation(s) for tags.
  name: statsig Tags API
  phrasing_intents:
  - id: listTags
    intent: List tags used to organize the project
    question: Which tags are available for organizing gates and experiments in Statsig?
  - id: createTag
    intent: Create a tag
    question: How do I create a new tag for organizing gates and experiments?
  - id: getConsoleV1Tags
    intent: Page through tags
    question: Can I page through tags a few at a time?
  - id: postConsoleV1Tags
    intent: Create a tag with a description
    question: Can I mark a new tag as a core tag?
  - id: getConsoleV1TagsById
    intent: Read one tag
    question: Can I look a tag up by its name rather than its ID?
  - id: patchConsoleV1TagsById
    intent: Update a tag
    question: Can I rename an existing tag?
  - id: deleteConsoleV1TagsById
    intent: Delete a tag
    question: Can I delete a tag we stopped using?
  phrasing_ops: 7
  slug: statsig-tags-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage target application definitions that scope feature configurations to specific applications.
  name: statsig Target Apps API
  phrasing_intents:
  - id: listTargetApps
    intent: List target app definitions
    question: Which target apps are defined in my Statsig project?
  phrasing_ops: 1
  slug: statsig-target-apps-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: Manage user data and lookup user properties within the Statsig project.
  name: statsig Users API
  phrasing_intents:
  - id: listUsers
    intent: List users known to the project
    question: Which users does my Statsig project know about?
  - id: getConsoleV1Users
    intent: List company members, including stale ones
    question: Can I include former or stale members when listing users?
  - id: getConsoleV1UsersByEmail
    intent: Look up a user by email
    question: What role does a particular teammate have, given their email?
  - id: postConsoleV1UsersByEmail
    intent: Change a user's role or name
    question: How do I promote a teammate to Admin?
  - id: getConsoleV1UsersIdById
    intent: Look up a user by ID
    question: Which person does a given user ID in the audit trail belong to?
  - id: postConsoleV1UsersInvite
    intent: Invite users with a role and teams
    question: How do I invite several colleagues at once with the same role?
  - id: getConsoleV1UsersTeams
    intent: List teams
    question: What teams exist in our organization?
  - id: postConsoleV1UsersTeams
    intent: Create a team
    question: How do I set up a new team with members and admins?
  phrasing_ops: 11
  slug: statsig-users-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Alerts API from Statsig — 6 operation(s) for alerts.
  name: Statsig Alerts API
  phrasing_intents:
  - id: getConsoleV1Alerts
    intent: List topline alerts
    question: Which topline metric alerts are configured in my project?
  - id: postConsoleV1Alerts
    intent: Create a topline alert
    question: How do I get alerted when a topline metric moves?
  - id: getConsoleV1AlertsById
    intent: Read one topline alert
    question: What threshold and condition does a given alert use?
  - id: patchConsoleV1AlertsById
    intent: Update a topline alert's thresholds or routing
    question: How do I raise the threshold on an alert?
  - id: deleteConsoleV1AlertsById
    intent: Delete a topline alert
    question: Can I remove an alert that keeps firing for no reason?
  - id: getConsoleV1AlertsByIdEvents
    intent: List an alert's firing history
    question: When has a particular alert fired in the past?
  - id: getConsoleV1AlertsByIdEventsByEventId
    intent: Read one alert firing event
    question: What exactly happened during a specific alert firing?
  - id: postConsoleV1AlertsByIdMute
    intent: Mute a topline alert
    question: Can I silence an alert for a few hours during a planned launch?
  phrasing_ops: 9
  slug: statsig-alerts-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Change Validation API from Statsig — 2 operation(s) for change validation.
  name: Statsig Change Validation API
  phrasing_intents:
  - id: postConsoleV1ChangeValidation
    intent: Report a change validation result
    question: How can our CI pipeline mark a config review as validated?
  - id: patchConsoleV1ChangeValidationMessage
    intent: Update a change validation message
    question: Can I edit the message shown on a validation after it was posted?
  phrasing_ops: 2
  slug: statsig-change-validation-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Company API from Statsig — 1 operation(s) for company.
  name: Statsig Company API
  phrasing_intents:
  - id: getConsoleV1Company
    intent: Get company account info
    question: What company account is this API key tied to?
  phrasing_ops: 1
  slug: statsig-company-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Configs API from Statsig — 1 operation(s) for configs.
  name: Statsig Configs API
  phrasing_intents:
  - id: getConsoleV1ExposureCount
    intent: Count recent exposure events
    question: Is my new experiment receiving exposures yet?
  phrasing_ops: 1
  slug: statsig-configs-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Dashboards API from Statsig — 4 operation(s) for dashboards.
  name: Statsig Dashboards API
  phrasing_intents:
  - id: getConsoleV1Dashboards
    intent: List or search dashboards
    question: What dashboards do we have?
  - id: postConsoleV1Dashboards
    intent: Create a dashboard
    question: How do I build a new dashboard through the API?
  - id: getConsoleV1DashboardsById
    intent: Read a dashboard
    question: Which widgets are on a particular dashboard?
  - id: postConsoleV1DashboardsByIdWidgets
    intent: Add widgets to a dashboard
    question: How do I append a chart to an existing dashboard?
  - id: putConsoleV1DashboardsByIdWidgets
    intent: Replace all widgets on a dashboard
    question: Can I swap out every widget on a dashboard at once?
  - id: getConsoleV1DashboardsByIdWidgetsByWidgetIdResults
    intent: Get a dashboard widget's data
    question: Can I pull the numbers behind one dashboard chart?
  phrasing_ops: 6
  slug: statsig-dashboards-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Environments API from Statsig — 1 operation(s) for environments.
  name: Statsig Environments API
  phrasing_intents:
  - id: getConsoleV1Environments
    intent: List the project's environments
    question: Which environments like staging and production are defined?
  - id: postConsoleV1Environments
    intent: Update the project's environments
    question: How do I add a new environment such as QA?
  phrasing_ops: 2
  slug: statsig-environments-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Experiments (Warehouse Native) API from Statsig — 10 operation(s) for experiments (warehouse native).
  name: Statsig Experiments (Warehouse Native) API
  phrasing_intents:
  - id: getConsoleV1ExperimentsQualifyingEvents
    intent: List qualifying events
    question: Which qualifying events decide who counts in an experiment?
  - id: postConsoleV1ExperimentsQualifyingEvents
    intent: Create a qualifying event
    question: How do I define a qualifying event from a warehouse table or query?
  - id: getConsoleV1ExperimentsQualifyingEventsByName
    intent: Read a qualifying event
    question: What query defines a particular qualifying event?
  - id: postConsoleV1ExperimentsQualifyingEventsByName
    intent: Update a qualifying event
    question: How do I change the SQL behind a qualifying event?
  - id: deleteConsoleV1ExperimentsQualifyingEventsByName
    intent: Delete a qualifying event
    question: Can I remove a qualifying event we no longer use?
  phrasing_ops: 5
  slug: statsig-experiments-warehouse-native-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Ingestions API from Statsig — 9 operation(s) for ingestions.
  name: Statsig Ingestions API
  phrasing_intents:
  - id: getConsoleV1Ingestion
    intent: Read an ingestion source
    question: How is data ingestion configured for a given dataset?
  - id: postConsoleV1Ingestion
    intent: Create an ingestion source
    question: How do I start ingesting data from my warehouse?
  - id: patchConsoleV1Ingestion
    intent: Update an ingestion source
    question: Can I modify an existing ingestion source's configuration?
  - id: deleteConsoleV1Ingestion
    intent: Delete an ingestion source
    question: Can I stop and remove an ingestion source?
  - id: postConsoleV1IngestionBackfill
    intent: Backfill ingested data for a date range
    question: How do I re-ingest data for days that were missed?
  - id: postConsoleV1IngestionConnectionDatabricks
    intent: Connect Databricks for ingestion
    question: How do I connect a Databricks workspace as an ingestion source?
  - id: getConsoleV1IngestionEventsCount
    intent: Count ingested events over a date range
    question: How many events were ingested between two dates?
  - id: getConsoleV1IngestionEventsDelta
    intent: Get the ingestion event delta ledger
    question: What changed in ingested event volumes day over day?
  phrasing_ops: 13
  slug: statsig-ingestions-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Logs API from Statsig — 1 operation(s) for logs.
  name: Statsig Logs API
  phrasing_intents:
  - id: getConsoleV1Logs
    intent: Query recent events in the Logs Explorer
    question: Can I search recent logs with the same filter syntax as the console?
  phrasing_ops: 1
  slug: statsig-logs-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Overrides API from Statsig — 1 operation(s) for overrides.
  name: Statsig Overrides API
  phrasing_intents:
  - id: getConsoleV1Overrides
    intent: Audit overrides across the project
    question: Where is a specific user ID overridden across gates and experiments?
  phrasing_ops: 1
  slug: statsig-overrides-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Param Store API from Statsig — 2 operation(s) for param store.
  name: Statsig Param Store API
  phrasing_intents:
  - id: getConsoleV1ParamStores
    intent: List parameter stores
    question: Which parameter stores exist in my project?
  - id: postConsoleV1ParamStores
    intent: Create a parameter store
    question: How do I set up a new parameter store?
  - id: getConsoleV1ParamStoresByName
    intent: Get a parameter store
    question: What parameters are defined in a given param store?
  - id: postConsoleV1ParamStoresByName
    intent: Update a parameter store's parameters
    question: How do I change the parameters inside a param store?
  - id: deleteConsoleV1ParamStoresByName
    intent: Delete a parameter store
    question: Can I remove a param store we no longer use?
  phrasing_ops: 5
  slug: statsig-param-store-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Project API from Statsig — 1 operation(s) for project.
  name: Statsig Project API
  phrasing_intents:
  - id: getConsoleV1Project
    intent: Get project info
    question: Which project does my console key belong to?
  phrasing_ops: 1
  slug: statsig-project-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Prompts API from Statsig — 4 operation(s) for prompts.
  name: Statsig Prompts API
  phrasing_intents:
  - id: getConsoleV1Prompts
    intent: List prompts (AI Configs)
    question: What AI prompts are managed in my project?
  - id: postConsoleV1Prompts
    intent: Create a prompt (AI Config)
    question: How do I create a new managed prompt?
  - id: getConsoleV1PromptsById
    intent: Get a prompt
    question: What does a specific AI Config contain?
  - id: patchConsoleV1PromptsById
    intent: Update a prompt's description or ownership
    question: Can I change which team owns a prompt?
  - id: deleteConsoleV1PromptsById
    intent: Delete a prompt
    question: Can I delete a prompt we retired?
  - id: postConsoleV1PromptsByIdVersions
    intent: Add a new version to a prompt
    question: How do I save a new version of a prompt with a different model?
  - id: postConsoleV1PromptsByIdVersionsByVersionIdStartEvals
    intent: Start evals on a prompt version
    question: Can I kick off an evaluation run for one prompt version?
  phrasing_ops: 7
  slug: statsig-prompts-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Release Pipelines API from Statsig — 10 operation(s) for release pipelines.
  name: Statsig Release Pipelines API
  phrasing_intents:
  - id: getConsoleV1ReleasePipelineTriggers
    intent: List release pipeline runs
    question: Which release pipeline rollouts are in progress right now?
  - id: getConsoleV1ReleasePipelineTriggersById
    intent: Get a release pipeline run
    question: Which phase is a given rollout currently in?
  - id: putConsoleV1ReleasePipelineTriggersByIdAbort
    intent: Abort a release pipeline run
    question: How do I stop a bad rollout immediately?
  - id: putConsoleV1ReleasePipelineTriggersByIdApprove
    intent: Approve the next pipeline phase
    question: How do I sign off on a rollout phase that needs approval?
  - id: putConsoleV1ReleasePipelineTriggersByIdPause
    intent: Pause a release pipeline run
    question: Can I hold a rollout at its current phase while we investigate?
  - id: putConsoleV1ReleasePipelineTriggersByIdRollout
    intent: Fully roll out a pipeline run
    question: Can I skip the remaining phases and ship to everyone?
  - id: putConsoleV1ReleasePipelineTriggersByIdSkip
    intent: Skip to a pipeline phase
    question: Can I jump a rollout ahead to a later phase?
  - id: putConsoleV1ReleasePipelineTriggersByIdUnpause
    intent: Resume a paused pipeline run
    question: How do I resume a rollout I paused?
  phrasing_ops: 13
  slug: statsig-release-pipelines-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Reports API from Statsig — 1 operation(s) for reports.
  name: Statsig Reports API
  phrasing_intents:
  - id: getConsoleV1Reports
    intent: Get a report for a date
    question: Can I download a project report for a specific day?
  phrasing_ops: 1
  slug: statsig-reports-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Roles API from Statsig — 2 operation(s) for roles.
  name: Statsig Roles API
  phrasing_intents:
  - id: getConsoleV1Roles
    intent: List roles
    question: What custom roles are defined for our organization?
  - id: postConsoleV1Roles
    intent: Create a custom role
    question: How do I define a custom role with specific permissions?
  - id: getConsoleV1RolesById
    intent: Get a role's permissions
    question: What permissions does a particular role grant?
  - id: patchConsoleV1RolesById
    intent: Change a role's permissions
    question: How do I add a permission to an existing role?
  - id: deleteConsoleV1RolesById
    intent: Delete a role
    question: Can I delete a custom role nobody uses?
  phrasing_ops: 5
  slug: statsig-roles-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Settings API from Statsig — 4 operation(s) for settings.
  name: Statsig Settings API
  phrasing_intents:
  - id: getConsoleV1SettingsProject
    intent: Get project settings
    question: What is my project's visibility and default unit type?
  - id: postConsoleV1SettingsProject
    intent: Update project settings
    question: How do I rename the project or change its visibility?
  - id: getConsoleV1SettingsReviews
    intent: Get review requirement settings
    question: Are config and metric reviews required in my project?
  - id: postConsoleV1SettingsReviews
    intent: Update review requirement settings
    question: How do I require reviews on every config change?
  - id: getConsoleV1SettingsRoles
    intent: Get the default project role setting
    question: What role do new members get by default?
  - id: postConsoleV1SettingsRoles
    intent: Set the default project role
    question: How do I make new members start as Read Only?
  - id: getConsoleV1SettingsTeams
    intent: Get team requirement settings
    question: Is a team required on every new config?
  - id: postConsoleV1SettingsTeams
    intent: Require teams on new configs
    question: How do I force every new config to have an owning team?
  phrasing_ops: 8
  slug: statsig-settings-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Target App API from Statsig — 2 operation(s) for target app.
  name: Statsig Target App API
  phrasing_intents:
  - id: getConsoleV1TargetApp
    intent: List target apps
    question: Which target apps are defined in my project?
  - id: postConsoleV1TargetApp
    intent: Create a target app
    question: How do I create a target app so each SDK only downloads its own configs?
  - id: patchConsoleV1TargetApp
    intent: Bulk assign configs to target apps
    question: Can I assign many gates to several target apps in one call?
  - id: getConsoleV1TargetAppById
    intent: Read a target app
    question: What configs are assigned to a particular target app?
  - id: patchConsoleV1TargetAppById
    intent: Rename or redescribe a target app
    question: How do I rename a target app?
  - id: deleteConsoleV1TargetAppById
    intent: Delete a target app
    question: Can I remove a target app we retired?
  phrasing_ops: 6
  slug: statsig-target-app-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Unit ID Types API from Statsig — 2 operation(s) for unit id types.
  name: Statsig Unit ID Types API
  phrasing_intents:
  - id: getConsoleV1UnitIdTypes
    intent: List unit ID types
    question: Which unit ID types like userID or companyID are defined?
  - id: postConsoleV1UnitIdTypes
    intent: Create a custom unit ID type
    question: How do I randomize experiments by account instead of by user?
  - id: getConsoleV1UnitIdTypesById
    intent: Get a unit ID type
    question: What is a given unit ID type used for?
  - id: patchConsoleV1UnitIdTypesById
    intent: Update a unit ID type's description
    question: How do I change the description on a unit type?
  - id: deleteConsoleV1UnitIdTypesById
    intent: Delete a unit ID type
    question: Can I remove a custom unit type nobody uses?
  phrasing_ops: 5
  slug: statsig-unit-id-types-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Usage API from Statsig — 1 operation(s) for usage.
  name: Statsig Usage API
  phrasing_intents:
  - id: getConsoleV1ProjectUsageBillingReport
    intent: Download a usage billing report as CSV
    question: How much billable usage did my project generate last month?
  phrasing_ops: 1
  slug: statsig-usage-api
- baseURL: https://statsigapi.net
  baseurl_source: declared
  description: The Warehouse Connections API from Statsig — 1 operation(s) for warehouse connections.
  name: Statsig Warehouse Connections API
  phrasing_intents:
  - id: patchConsoleV1WhConnections
    intent: Update warehouse connection parameters
    question: Where do I update the credentials for our warehouse connection?
  phrasing_ops: 1
  slug: statsig-warehouse-connections-api
artifact_total: 89
asyncapis:
- description: 'Statsig''s webhook system provides real-time event-driven notifications for exposure events and configuration changes. Webhooks are triggered at runtime as users are assigned to gates and experiments, '
  name: Statsig Webhook Events
  slug: statsig-webhooks-asyncapi
collections:
- collection_type: open
  name: Statsig Client SDK Audit Logs API
  slug: open-statsig-audit-logs-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Autotunes API
  slug: open-statsig-autotunes-api
- collection_type: open
  name: Statsig Client SDK API
  slug: open-statsig-client-sdk-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Configuration API
  slug: open-statsig-configuration-api
- collection_type: open
  name: Statsig Console API
  slug: open-statsig-console-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Dynamic Configs API
  slug: open-statsig-dynamic-configs-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Events API
  slug: open-statsig-events-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Experiments API
  slug: open-statsig-experiments-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Feature Gates API
  slug: open-statsig-feature-gates-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Gates API
  slug: open-statsig-gates-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Holdouts API
  slug: open-statsig-holdouts-api
- collection_type: open
  name: Statsig HTTP API
  slug: open-statsig-http-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Initialization API
  slug: open-statsig-initialization-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Keys API
  slug: open-statsig-keys-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Layers API
  slug: open-statsig-layers-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Metrics API
  slug: open-statsig-metrics-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Segments API
  slug: open-statsig-segments-api
- collection_type: open
  name: Statsig Server SDK API
  slug: open-statsig-server-sdk-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Tags API
  slug: open-statsig-tags-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Target Apps API
  slug: open-statsig-target-apps-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Users API
  slug: open-statsig-users-api
- collection_type: open
  name: Statsig Client SDK Audit Logs Webhooks API
  slug: open-statsig-webhooks-api
common:
- group: other
  href: https://artifacts.apis.io/statsig/capabilities/statsig-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/statsig-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/statsig/overlays/statsig-console-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/statsig-console-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.statsig.com/
- group: agent
  href: https://artifacts.apis.io/statsig/agentic-access/statsig-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/statsig-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/statsig/security/statsig-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/statsig-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/statsig/security/statsig-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/statsig-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/statsig/authentication/statsig-authentication.yml
  title: ''
  type: Authentication
  url: authentication/statsig-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/statsig-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/statsig
- group: design
  href: https://artifacts.apis.io/statsig/json-ld/statsig-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/statsig-context.jsonld
- group: docs
  href: https://artifacts.apis.io/statsig/json-schema/statsig-feature-gate-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/statsig-feature-gate-schema.json
- group: docs
  href: https://artifacts.apis.io/statsig/json-schema/statsig-experiment-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/statsig-experiment-schema.json
- group: docs
  href: https://artifacts.apis.io/statsig/json-schema/statsig-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/statsig-event-schema.json
- group: design
  href: https://artifacts.apis.io/statsig/json-structure/statsig-feature-gate-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/statsig-feature-gate-structure.json
- group: design
  href: https://artifacts.apis.io/statsig/json-structure/statsig-experiment-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/statsig-experiment-structure.json
- group: design
  href: https://artifacts.apis.io/statsig/json-structure/statsig-event-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/statsig-event-structure.json
- group: design
  href: https://artifacts.apis.io/statsig/rules/statsig-rules.yml
  title: ''
  type: SpectralRules
  url: rules/statsig-rules.yml
- group: design
  href: https://artifacts.apis.io/statsig/vocabulary/statsig-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/statsig-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.statsig.com/llms.txt
- group: build
  href: https://artifacts.apis.io/statsig/packages/statsig-packages.yml
  title: ''
  type: Packages
  url: packages/statsig-packages.yml
- group: build
  href: https://artifacts.apis.io/statsig/packages/statsig-packages.yml
  title: ''
  type: SDKs
  url: packages/statsig-packages.yml
- group: agent
  href: https://artifacts.apis.io/statsig/mcp/statsig-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/statsig-mcp.yml
- group: build
  href: https://artifacts.apis.io/statsig/mcp/statsig-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/statsig-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/statsig/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/statsig/grpc/statsig-forward-proxy.proto
  title: ''
  type: Protobuf
  url: grpc/statsig-forward-proxy.proto
- group: agent
  href: https://artifacts.apis.io/statsig/well-known/statsig-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/statsig-well-known.yml
- group: design
  href: https://artifacts.apis.io/statsig/conformance/statsig-conformance.yml
  title: ''
  type: Conformance
  url: conformance/statsig-conformance.yml
- group: auth
  href: https://artifacts.apis.io/statsig/security/statsig-trust-center.yml
  title: ''
  type: Compliance
  url: security/statsig-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/statsig/security/statsig-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/statsig-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.statsig.com/legal/security
- group: design
  href: https://artifacts.apis.io/statsig/conventions/statsig-conventions.yml
  title: ''
  type: Conventions
  url: conventions/statsig-conventions.yml
- group: design
  href: https://artifacts.apis.io/statsig/errors/statsig-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/statsig-problem-types.yml
- group: design
  href: https://artifacts.apis.io/statsig/data-model/statsig-data-model.yml
  title: ''
  type: DataModel
  url: data-model/statsig-data-model.yml
- group: design
  href: https://artifacts.apis.io/statsig/lifecycle/statsig-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/statsig-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.statsig.com/
- group: operate
  href: https://artifacts.apis.io/statsig/changelog/statsig-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/statsig-changelog.yml
- group: build
  href: https://artifacts.apis.io/statsig/cli/statsig-cli.yml
  title: ''
  type: CLI
  url: cli/statsig-cli.yml
- group: commercial
  href: https://artifacts.apis.io/statsig/plans/statsig-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/statsig-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/statsig/rate-limits/statsig-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/statsig-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/statsig/finops/statsig-finops.yml
  title: ''
  type: FinOps
  url: finops/statsig-finops.yml
- group: build
  href: https://artifacts.apis.io/statsig/examples/statsig-check-gate-example.json
  title: ''
  type: Examples
  url: examples/statsig-check-gate-example.json
- group: design
  href: https://artifacts.apis.io/statsig/asyncapi/statsig-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/statsig-webhooks-asyncapi.yml
- group: docs
  href: https://artifacts.apis.io/statsig/asyncapi/statsig-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/statsig-webhooks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/statsig/llms/statsig-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/statsig-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.statsig.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.statsig.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.statsig.com/console-api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.statsig.com/sdks/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.statsig.com/contact
- group: operate
  title: ''
  type: Community
  url: https://www.statsig.com/slack
- group: company
  title: ''
  type: Blog
  url: https://www.statsig.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.statsig.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.statsig.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.statsig.com/terms
- group: operate
  title: ''
  type: FAQ
  url: https://docs.statsig.com/faq
created: '2026-05-04'
description: 'Statsig is a product development platform that combines feature management, experimentation and analytics in one system. Teams gate releases behind feature flags, run A/B, A/B/n, switchback, holdout and multi-armed-bandit experiments, and read the impact of every change against their own metrics — in Statsig Cloud, which ingests and stores the event data, or Warehouse Native, which runs the same analysis directly against the customer''s Snowflake, BigQuery, Databricks or Athena warehouse without moving user-level data out of it. Around that core it ships product analytics, web analytics, session replay, infra analytics, dynamic configs, parameter stores and 30+ SDKs. Its programmable surface is unusually complete: a first-party OpenAPI covering 324 Console API operations, a low-latency HTTP evaluation API, gRPC protobufs for the self-hosted Forward Proxy, an authenticated remote MCP server with OAuth, a public documentation MCP server, published Agent Skills, a Terraform provider
  and a CLI. Statsig is based in Bellevue, Washington.'
examples:
- key_count: 2
  name: Statsig Check Gate Example
  slug: statsig-check-gate-example
- key_count: 2
  name: Statsig Create Experiment Example
  slug: statsig-create-experiment-example
- key_count: 2
  name: Statsig Create Gate Example
  slug: statsig-create-gate-example
- key_count: 2
  name: Statsig List Gates Example
  slug: statsig-list-gates-example
- key_count: 2
  name: Statsig Log Events Example
  slug: statsig-log-events-example
finops:
- has_sources: true
  method: derived
  name: Statsig Finops
  primary_unit: subscription
  service_category: ''
  slug: statsig-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/statsig.png
json_schemas:
- name: Statsig Event
  property_count: 7
  slug: statsig-event
- name: Statsig Experiment
  property_count: 17
  slug: statsig-experiment
- name: Statsig Feature Gate
  property_count: 12
  slug: statsig-feature-gate
json_structures:
- name: Statsig Event Structure
  property_count: 0
  slug: statsig-event-structure
- name: Statsig Experiment Structure
  property_count: 0
  slug: statsig-experiment-structure
- name: Statsig Feature Gate Structure
  property_count: 0
  slug: statsig-feature-gate-structure
jsonld:
- class_count: 0
  name: Statsig Context
  property_count: 13
  slug: statsig-context
layout: provider
mcp_servers:
- description: Statsig ships TWO distinct remote MCP servers. The authenticated Statsig MCP server at https://api.statsig.com/v1/mcp exposes the Console API surface — gates, experiments, dynamic configs, segments, l
  name: Statsig MCP
  slug: statsig-mcp
modified: '2026-09-17'
name: Statsig
nav: Providers
network: true
overview: 'Statsig publishes 38 API contracts indexed on the [APIs.io](https://apis.io/) network, including Events API, Audit Logs API, Autotunes API, and 35 more. Tagged areas include Feature Flags, Experimentation, A/B Testing, Product Analytics, and Session Replay.


  The Statsig catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Statsig''s developer surface includes authentication, changelog, CLI, code examples, documentation, API reference, getting-started guide, and 48 more developer resources.'
plans:
- name: Statsig Plans Pricing
  plan_count: 3
  slug: statsig-plans-pricing
- name: Statsig Price Estimates
  plan_count: 0
  slug: statsig-price-estimates
random_paper: 23
rate_limits:
- limit_count: 5
  name: Statsig Rate Limits
  slug: statsig-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Statsig — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: statsig-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Statsig — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: statsig-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Statsig API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 3
    info: 0
    warn: 5
  slug: statsig-rules
score:
  band: exemplar
  composite: 76.8
  coverage:
    artifact_dirs: 37
    catalog_earned: 84.0
    catalog_earned_first_party: 24.0
    catalog_gap: 31.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 45.5
    contract_quality: 67.6
    developer_ergonomics: 78.6
    discoverability: 80.0
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 76.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 39
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/statsig/statsig-2026-06-20T194528.png
security:
- kind: authentication
  name: Statsig Authentication
  slug: statsig-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Statsig Domain Security
  slug: statsig-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Statsig Vulnerability Disclosure
  slug: statsig-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Statsig Trust Center
  slug: statsig-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR, HIPAA
skill_count: 3
skills:
- name: statsig-create-cloud-metric
  slug: statsig-create-cloud-metric
- name: statsig-dashboard
  slug: statsig-dashboard
- name: statsig
  slug: statsig
slug: statsig
tags:
- Feature Flags
- Experimentation
- A/B Testing
- Product Analytics
- Session Replay
- Developer Tools
- Data Warehouse
- Configuration Management
website: https://www.statsig.com/
---
