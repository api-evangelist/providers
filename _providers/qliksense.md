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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: templated
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.6
  scored_at: '2026-11-06'
api_count: 78
apis:
- description: JSON-RPC WebSocket API for interacting with the Qlik Associative Engine, creating and manipulating apps, and building visualizations.
  name: Qlik Engine API
  slug: engine-api
- description: gRPC/protobuf contract for extending the Qlik Associative Engine with external compute. A plugin implements the qlik.sse.Connector service and the engine calls out to it for scalar, aggregation and te
  name: Qlik Server-Side Extension Protocol
  slug: server-side-extension
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/webhooks
  baseurl_source: declared
  description: 'The Qlik Cloud tenant event surface: 29 AsyncAPI 3.0.0 documents covering 102 message definitions across apps, reloads, spaces, tenants, users, roles, licenses, quotas, OAuth clients, data-integration'
  name: Qlik Cloud System Events
  slug: system-events
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/ai/mcp
  baseurl_source: declared
  description: Qlik's first-party remote Model Context Protocol server, generally available since 2026-02-10 and included from the Starter plan up. It exposes Qlik Cloud analytics — datasets and data quality, data p
  name: Qlik MCP Server
  slug: mcp-server
- description: WebSocket-based API for interacting with the Qlik Associative Engine, including data modeling, selections, and visualizations.
  name: Qlik Sense Engine API
  slug: qlik-sense-engine-api
- description: REST API for managing Qlik Sense repository objects including apps, streams, users, and security rules.
  name: Qlik Sense Repository API
  slug: qlik-sense-repository-api
- description: REST API for session management and authentication through the Qlik Sense Proxy Service.
  name: Qlik Sense Proxy API
  slug: qlik-sense-proxy-api
- description: REST API for managing data integration tasks, connections, and data pipelines.
  name: Qlik Data Integration API
  slug: qlik-data-integration-api
- description: JavaScript API for embedding Qlik Sense visualizations and mashups into web applications.
  name: Qlik Embedding API
  slug: qlik-embedding-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The alerting actions API from Qlik Sense — 2 operation(s) for alerting actions.
  name: Qlik Sense alerting actions API
  phrasing_intents:
  - id: alertingActionsTriggerCreate
    intent: Trigger a data alert task
    question: How do I fire a data alert task manually?
  - id: alertingTaskActionsValidate
    intent: Validate a data alert before creating it
    question: Can I check that alert recipients are valid before creating the alert?
  phrasing_ops: 2
  slug: qliksense-alerting-actions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The alerting settings API from Qlik Sense — 1 operation(s) for alerting settings.
  name: Qlik Sense alerting settings API
  phrasing_intents:
  - id: alertingSettingsGet
    intent: Get data alert settings
    question: Is data alerting turned on for my tenant?
  - id: alertingSettingsUpload
    intent: Enable or disable data alerting
    question: How do I switch data alerting on or off for the tenant?
  phrasing_ops: 2
  slug: qliksense-alerting-settings-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The alerting tasks API from Qlik Sense — 4 operation(s) for alerting tasks.
  name: Qlik Sense alerting tasks API
  phrasing_intents:
  - id: alertingTasksList
    intent: List data alerts
    question: Which data alerts exist in Qlik Cloud for a given app?
  - id: alertingTasksCreate
    intent: Create a data alert
    question: How do I set up a data alert that notifies people when a condition is met?
  - id: alertingTasksIDGet
    intent: Get a data alert
    question: How do I see the full settings of one data alert?
  - id: alertingTasksUpdate
    intent: Update a data alert
    question: Can I disable a data alert without deleting it?
  - id: alertingTasksDelete
    intent: Delete a data alert
    question: How do I delete a data alert I no longer want?
  - id: alertingConditionGet
    intent: Get a data alert's condition
    question: What condition triggers a particular data alert?
  - id: alertingRecipientStatsGet
    intent: Get data alert recipient stats
    question: How many recipients are subscribed to a data alert?
  phrasing_ops: 7
  slug: qliksense-alerting-tasks-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The alerting tasks executions API from Qlik Sense — 4 operation(s) for alerting tasks executions.
  name: Qlik Sense alerting tasks executions API
  phrasing_intents:
  - id: alertingExecutionsIDGet
    intent: Get a data alert execution
    question: How do I see the details of one run of a data alert?
  - id: alertingExecutionsDelete
    intent: Delete a data alert execution
    question: Can I delete a single execution record from a data alert's history?
  - id: alertingExecutionsList
    intent: List a data alert's executions
    question: What is the run history of a data alert?
  - id: alertingExecutionsEvaluationGet
    intent: Get a data alert execution evaluation
    question: What did the condition evaluate to during a specific alert run?
  - id: alertingExecutionsEvaluationStats
    intent: Get data alert execution stats
    question: How often has a data alert run and triggered over a period?
  phrasing_ops: 5
  slug: qliksense-alerting-tasks-executions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The aliases API from Qlik Sense — 2 operation(s) for aliases.
  name: Qlik Sense Aliases API
  phrasing_intents:
  - id: getAliases
    intent: List aliases on a deployment
    question: What aliases exist for my ML deployment?
  - id: postAlias
    intent: Create an alias for a deployment
    question: How do I create an alias pointing to a model in a deployment?
  - id: getAlias
    intent: Get a deployment alias
    question: Which model does a particular alias point to?
  - id: updateAliases
    intent: Update a deployment alias
    question: Can I repoint an alias to a different model?
  - id: deleteAlias
    intent: Delete a deployment alias
    question: How do I remove an alias from a deployment?
  phrasing_ops: 5
  slug: qliksense-aliases-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The Analytics API from Qlik Sense — 1 operation(s) for analytics.
  name: Qlik Sense Analytics API
  phrasing_intents:
  - id: restoreApp
    intent: Restore a deleted analytics app
    question: How do I recover an app I accidentally deleted?
  phrasing_ops: 1
  slug: qliksense-analytics-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The api-keys API from Qlik Sense — 2 operation(s) for api-keys.
  name: Qlik Sense API Keys API
  phrasing_intents:
  - id: getApiKeys
    intent: List API keys
    question: Which API keys exist in my Qlik tenant?
  - id: createApiKey
    intent: Create an API key
    question: How do I generate a new API key for myself?
  - id: getApiKeyById
    intent: Get an API key
    question: Where can I see the details of one API key?
  - id: updateApiKey
    intent: Update an API key's description
    question: Can I rename or re-describe an existing API key?
  - id: deleteApiKeyById
    intent: Delete or revoke an API key
    question: Can a tenant admin revoke someone else's API key?
  phrasing_ops: 5
  slug: qliksense-api-keys-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The api-keys configurations API from Qlik Sense — 1 operation(s) for api-keys configurations.
  name: Qlik Sense api-keys configurations API
  phrasing_intents:
  - id: getApiKeysConfiguration
    intent: Get a tenant's API key configuration
    question: Are API keys enabled for my tenant, and what limits apply?
  - id: updateApiKeyConfiguration
    intent: Update a tenant's API key configuration
    question: Can I change the API key policy for a tenant?
  phrasing_ops: 2
  slug: qliksense-api-keys-configurations-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The api settings API from Qlik Sense — 1 operation(s) for api settings.
  name: Qlik Sense api settings API
  phrasing_intents:
  - id: ConditionManagerAPISettingsGet
    intent: Get condition manager settings
    question: Are the condition manager API endpoints enabled for my tenant?
  - id: conditionManagerAPISettingsUpload
    intent: Enable or disable condition manager endpoints
    question: How do I turn the condition manager API on or off?
  phrasing_ops: 2
  slug: qliksense-api-settings-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The Apps API from Qlik Sense — 23 operation(s) for apps.
  name: Qlik Sense Apps API
  phrasing_intents:
  - id: getAppsV2
    intent: List ODAG apps by type
    question: Which apps are set up as ODAG selection or template apps?
  - id: postApiV1Apps
    intent: Create a new Qlik Sense app
    question: Can I create a brand-new empty analytics app through the API?
  - id: getApiV1AppsByAppId
    intent: Get details of an app
    question: Where can I see the name, owner and attributes of one specific app?
  - id: putApiV1AppsByAppId
    intent: Update an app's attributes
    question: Can I rename an existing app or change its description?
  - id: deleteApiV1AppsByAppId
    intent: Delete an app
    question: Can I permanently remove an analytics app I no longer need?
  - id: postApiV1AppsByAppIdCopy
    intent: Duplicate an app
    question: Can I make a copy of an existing app to experiment on?
  - id: getApiV1AppsByAppIdDataLineage
    intent: Get the data lineage of an app
    question: Which sources feed the data loaded into a given app?
  - id: getApiV1AppsByAppIdDataMetadata
    intent: Get an app's data model metadata
    question: Where do I find the tables, fields and reload statistics of an app's data model?
  phrasing_ops: 34
  slug: qliksense-apps-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The assignments API from Qlik Sense — 2 operation(s) for assignments.
  name: Qlik Sense Assignments API
  phrasing_intents:
  - id: getSpaceAssignments
    intent: List users and groups assigned to a space
    question: Who has access to a Qlik Cloud space, and with which roles?
  - id: createSpaceAssignment
    intent: Give a user or group roles in a space
    question: How do I give a colleague access to a shared space?
  - id: getSpaceAssignmentById
    intent: Get one space assignment
    question: What roles does a specific assignment grant in a space?
  - id: updateSpaceAssignmentById
    intent: Change the roles on a space assignment
    question: How do I change the roles an existing member has in a space?
  - id: deleteSpaceAssignmentById
    intent: Remove a user or group from a space
    question: How do I revoke someone's access to a space?
  phrasing_ops: 5
  slug: qliksense-assignments-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The assistants API from Qlik Sense — 4 operation(s) for assistants.
  name: Qlik Sense Assistants API
  phrasing_intents:
  - id: getApiV1Assistants
    intent: List AI assistants
    question: Which Qlik Answers assistants exist in my tenant?
  - id: postApiV1Assistants
    intent: Create an AI assistant
    question: Can I set up a new assistant backed by my knowledge bases?
  - id: getApiV1AssistantsByAssistantIdFeedback
    intent: Get an assistant's feedback summary
    question: Are users giving my assistant thumbs up or thumbs down?
  - id: postApiV1AssistantsByAssistantIdSourcesPlaintexts
    intent: Fetch source chunk text for an assistant
    question: Can I see the original source text behind the chunks an assistant cited?
  - id: getApiV1AssistantsById
    intent: Get an assistant
    question: Can I view the configuration of one specific assistant?
  - id: patchApiV1AssistantsById
    intent: Update an assistant's properties
    question: Can I change an assistant's title or system message after creating it?
  - id: deleteApiV1AssistantsById
    intent: Delete an assistant
    question: Can I remove an assistant I no longer use?
  phrasing_ops: 7
  slug: qliksense-assistants-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The async actions API from Qlik Sense — 1 operation(s) for async actions.
  name: Qlik Sense async actions API
  phrasing_intents:
  - id: get_async_action_status
    intent: Check an asynchronous data integration action
    question: Has my long-running data integration action finished yet?
  phrasing_ops: 1
  slug: qliksense-async-actions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The audits API from Qlik Sense — 7 operation(s) for audits.
  name: Qlik Sense Audits API
  phrasing_intents:
  - id: audits
    intent: List recent audit events
    question: Who did what in my Qlik tenant over the last few weeks?
  - id: audit
    intent: Get an audit event
    question: How do I see the full details of one audit event?
  - id: fetch-consumption-app
    intent: Export the consumption usage app
    question: How do I get a usage report app for my capacity subscription?
  - id: archive
    intent: List archived audit events for a date
    question: Where can I find audit events older than 90 days?
  - id: getSettings
    intent: Get audit service settings
    question: How is the audit service configured on my tenant?
  - id: sources
    intent: List audit event sources
    question: Which services can produce audit events?
  - id: eventTypes
    intent: List audit event types
    question: What kinds of audit events can occur in my tenant?
  phrasing_ops: 7
  slug: qliksense-audits-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The automation-connections API from Qlik Sense — 10 operation(s) for automation-connections.
  name: Qlik Sense Automation Connections API
  phrasing_intents:
  - id: getAutomationConnections
    intent: List automation connections (v1 path)
    question: What automation connections does the v1 automation-connections endpoint return for me?
  - id: createAutomationConnection
    intent: Create an automation connection (v1 path)
    question: How do I create an automation connection with the v1 automation-connections endpoint?
  - id: getAutomationConnection
    intent: Get an automation connection (v1 path)
    question: How do I fetch a single automation connection from the v1 endpoint?
  - id: updateAutomationConnection
    intent: Update an automation connection (v1 path)
    question: How do I rename an automation connection with the v1 endpoint?
  - id: deleteAutomationConnection
    intent: Delete an automation connection (v1 path)
    question: How do I remove an automation connection using the v1 endpoint?
  - id: automationConnectionChangeOwner
    intent: Change connection owner (v1 path)
    question: How do I transfer ownership of an automation connection with the v1 endpoint?
  - id: automationConnectionChangeSpace
    intent: Move a connection to a space (v1 path)
    question: How do I change the space of an automation connection with the v1 endpoint?
  - id: checkAutomationConnection
    intent: Test an automation connection (v1 path)
    question: How do I validate an automation connection with the v1 check action?
  phrasing_ops: 16
  slug: qliksense-automation-connections-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The automation-connectors API from Qlik Sense — 4 operation(s) for automation-connectors.
  name: Qlik Sense Automation Connectors API
  phrasing_intents:
  - id: getAutomationConnectors
    intent: List automation connectors (v1 endpoint)
    question: Which automation connectors does the v1 connectors endpoint list?
  - id: getApiWorkflowsAutomationConnectors
    intent: List automation connectors (workflows endpoint)
    question: Which connectors are available to automations in the workflows API?
  - id: getAutomationConnector
    intent: Get an automation connector's details
    question: What blocks and snippets does a given automation connector provide?
  - id: getConnectorWebhookConfiguration
    intent: Get a connector's webhook configuration
    question: Which webhook events can an automation connector trigger on?
  phrasing_ops: 4
  slug: qliksense-automation-connectors-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The automations API from Qlik Sense — 30 operation(s) for automations.
  name: Qlik Sense Automations API
  phrasing_intents:
  - id: getAutomations
    intent: List automations (v1 endpoint)
    question: Which Qlik automations can I see through the v1 automations endpoint?
  - id: createAutomation
    intent: Create an automation (v1 endpoint)
    question: How do I create a new automation with the v1 automations endpoint?
  - id: getAutomation
    intent: Get an automation's definition (v1 endpoint)
    question: Where can I read the full definition of one automation from the v1 API?
  - id: updateAutomation
    intent: Update an automation (v1 endpoint)
    question: Can I change an existing automation's schedules through the v1 API?
  - id: deleteAutomation
    intent: Delete an automation (v1 endpoint)
    question: How do I permanently delete an automation using the v1 API?
  - id: automationChangeOwner
    intent: Change an automation's owner (v1 change-owner action)
    question: Can I hand an automation to another user with the v1 change-owner action?
  - id: automationChangeSpace
    intent: Move an automation to another space (v1 endpoint)
    question: Can I move an automation into a different space with the v1 API?
  - id: copyAutomation
    intent: Duplicate an automation (v1 endpoint)
    question: Is there a v1 action to duplicate an existing automation?
  phrasing_ops: 39
  slug: qliksense-automations-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The automl-deployments API from Qlik Sense — 1 operation(s) for automl-deployments.
  name: Qlik Sense Automl Deployments API
  phrasing_intents:
  - id: postRealtimePredictions
    intent: Generate real-time AutoML predictions
    question: How do I get predictions from a deployed AutoML model in real time?
  phrasing_ops: 1
  slug: qliksense-automl-deployments-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The automl-predictions API from Qlik Sense — 6 operation(s) for automl-predictions.
  name: Qlik Sense Automl Predictions API
  phrasing_intents:
  - id: getCoordinateShapForPrediction
    intent: Download SHAP values in coordinate form
    question: Can I get a prediction's Shapley values in coordinate (long) form?
  - id: getPredictionJobs
    intent: List jobs for an AutoML prediction
    question: Which jobs ran for one of my AutoML predictions?
  - id: getErrorsForPrediction
    intent: Download rows that could not be predicted
    question: Which rows failed to get a prediction, and why?
  - id: getConfigurationsForPrediction
    intent: Download predicted values
    question: How do I get the file of predicted values from an AutoML prediction?
  - id: getShapForPrediction
    intent: Download SHAP values for a prediction
    question: Can I see which features drove each prediction through its Shapley values?
  - id: getSourceForPrediction
    intent: Download a prediction's source values
    question: Can I get the input rows a prediction was made on, with an index field?
  phrasing_ops: 6
  slug: qliksense-automl-predictions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The banner API from Qlik Sense — 2 operation(s) for banner.
  name: Qlik Sense Banner API
  phrasing_intents:
  - id: getBanner
    intent: Get the announcement banner
    question: What announcement banner is currently configured for the tenant?
  - id: upsertBanner
    intent: Set the announcement banner
    question: How do I post a maintenance announcement across the top of Qlik Cloud?
  phrasing_ops: 2
  slug: qliksense-banner-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The brands API from Qlik Sense — 6 operation(s) for brands.
  name: Qlik Sense Brands API
  phrasing_intents:
  - id: getBrands
    intent: List brands
    question: Which custom brands are defined on my Qlik tenant?
  - id: postBrands
    intent: Create a brand
    question: How do I add a custom brand with my own logo?
  - id: getBrandsByBrandId
    intent: Get a brand
    question: Where can I see the details of a specific brand?
  - id: patchBrandsByBrandId
    intent: Update a brand
    question: Can I change the name or description of an existing brand?
  - id: deleteBrandsByBrandId
    intent: Delete a brand
    question: What happens if I delete the brand that is currently active?
  - id: postBrandsByBrandIdActionsActivate
    intent: Activate a brand
    question: How do I make a custom brand the one users see?
  - id: postBrandsByBrandIdActionsDeactivate
    intent: Deactivate a brand
    question: How do I go back to the Qlik default brand?
  - id: getBrandsByBrandIdFilesByBrandFileId
    intent: Download a brand file
    question: How do I download the logo or favicon file from a brand?
  phrasing_ops: 12
  slug: qliksense-brands-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The categories API from Qlik Sense — 2 operation(s) for categories.
  name: Qlik Sense Categories API
  phrasing_intents:
  - id: getApiV1GlossariesByIdCategories
    intent: List categories in a glossary
    question: Which categories are defined in a business glossary?
  - id: postApiV1GlossariesByIdCategories
    intent: Create a glossary category
    question: Can I add a new category to organise terms in a glossary?
  - id: getApiV1GlossariesByIdCategoriesByCategoryId
    intent: Get a glossary category
    question: Can I view the details of one category in a glossary?
  - id: patchApiV1GlossariesByIdCategoriesByCategoryId
    intent: Patch individual category properties
    question: Can I change just one property of a glossary category with JSON Patch?
  - id: putApiV1GlossariesByIdCategoriesByCategoryId
    intent: Replace a glossary category
    question: Can I fully rewrite a category's name, parent and stewards in one call?
  - id: deleteApiV1GlossariesByIdCategoriesByCategoryId
    intent: Delete a glossary category
    question: Can I remove a category from a glossary?
  phrasing_ops: 6
  slug: qliksense-categories-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The change-stores API from Qlik Sense — 2 operation(s) for change-stores.
  name: Qlik Sense Change Stores API
  phrasing_intents:
  - id: listChangeStores
    intent: List change stores in a space
    question: Which change stores exist in a space?
  - id: getChangeStoreById
    intent: Get a change store
    question: Which charts are connected to a particular change store?
  phrasing_ops: 2
  slug: qliksense-change-stores-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The changes API from Qlik Sense — 2 operation(s) for changes.
  name: Qlik Sense Changes API
  phrasing_intents:
  - id: listChanges
    intent: List changes in a change store
    question: What write-back changes have been recorded in a change store?
  - id: getTabularViewChanges
    intent: View changed rows as a table
    question: Can I see a change store's edits as modified rows in a table?
  phrasing_ops: 2
  slug: qliksense-changes-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The chat API from Qlik Sense — 2 operation(s) for chat.
  name: Qlik Sense Chat API
  phrasing_intents:
  - id: postApiV1AssistantsByAssistantIdThreadsByThreadIdActionsInvoke
    intent: Ask an assistant and wait for the full answer
    question: Can I send a prompt to an assistant and get the whole answer in one response?
  - id: postApiV1AssistantsByAssistantIdThreadsByThreadIdActionsStream
    intent: Stream an assistant's answer
    question: Can I stream an assistant's answer token by token as it is generated?
  phrasing_ops: 2
  slug: qliksense-chat-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The collections API from Qlik Sense — 5 operation(s) for collections.
  name: Qlik Sense Collections API
  phrasing_intents:
  - id: collections#listCollections
    intent: List collections
    question: Which collections and tags do I have access to in Qlik Cloud?
  - id: collections#createCollection
    intent: Create a collection
    question: How do I create a new collection to group apps and items?
  - id: collections#getCollection
    intent: Get a collection
    question: How do I look up one collection by its ID?
  - id: collections#PatchCollection
    intent: Publish or unpublish a collection
    question: How do I publish a private collection as a public governed collection?
  - id: collections#updateCollection
    intent: Rename or redescribe a collection
    question: Can I replace a collection's name and description in one call?
  - id: collections#deleteCollection
    intent: Delete a collection
    question: What happens to the items when I delete a collection?
  - id: collections#listCollectionItems
    intent: List items in a collection
    question: What apps and items are inside a particular collection?
  - id: collections#addCollectionItem
    intent: Add an item to a collection
    question: How do I add an app or other item to a collection?
  phrasing_ops: 11
  slug: qliksense-collections-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The computation API from Qlik Sense — 5 operation(s) for computation.
  name: Qlik Sense Computation API
  phrasing_intents:
  - id: getBatchComputationStatus
    intent: Check a batch data quality computation
    question: How do I track a batch data quality computation across several datasets?
  - id: requestDataQualityComputation
    intent: Run data quality via the data-governance path
    question: How do I trigger a data quality computation through the data-governance endpoint?
  - id: getDataQualityComputation
    intent: Check computation status via data-governance path
    question: How do I poll a data quality computation on the data-governance path?
  - id: postApiV1DataQualitiesComputations
    intent: Run data quality via the v1 path
    question: How do I trigger a data quality computation on the v1 data-qualities endpoint?
  - id: getApiV1DataQualitiesComputationsByComputationId
    intent: Check computation status via the v1 path
    question: How do I poll a v1 data quality computation until it finishes?
  phrasing_ops: 5
  slug: qliksense-computation-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The condition preview API from Qlik Sense — 2 operation(s) for condition preview.
  name: Qlik Sense condition preview API
  phrasing_intents:
  - id: conditionsPreview
    intent: Preview a condition before saving it
    question: Can I test what a condition would evaluate to before I save it?
  - id: conditionsPreviewGet
    intent: Get a condition preview result
    question: What did my condition preview return?
  phrasing_ops: 2
  slug: qliksense-condition-preview-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The conditions API from Qlik Sense — 2 operation(s) for conditions.
  name: Qlik Sense Conditions API
  phrasing_intents:
  - id: createCondition
    intent: Create an alert condition
    question: How do I define a condition based on the data in an app?
  - id: getCondition
    intent: Get a saved condition
    question: What does a saved condition check for?
  - id: updateCondition
    intent: Update a saved condition
    question: Can I change the values in an existing condition?
  - id: deleteCondition
    intent: Delete a condition
    question: How do I remove a condition I no longer need?
  phrasing_ops: 4
  slug: qliksense-conditions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The Consumption API from Qlik Sense — 1 operation(s) for consumption.
  name: Qlik Sense Consumption API
  phrasing_intents:
  - id: GetExecutionsByTenantId
    intent: List consumption execution records
    question: How many executions has my tenant consumed?
  phrasing_ops: 1
  slug: qliksense-consumption-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The csp-origins API from Qlik Sense — 3 operation(s) for csp-origins.
  name: Qlik Sense Csp Origins API
  phrasing_intents:
  - id: listCSPEntries
    intent: List content security policy origins
    question: Which origins are allowed by my tenant's content security policy?
  - id: createCSPEntry
    intent: Add a CSP origin
    question: How do I allow an external origin to embed Qlik content?
  - id: getCSPEntry
    intent: Get a CSP origin
    question: How do I see the directives set on one CSP entry?
  - id: updateCSPEntry
    intent: Update a CSP origin
    question: Can I change which directives an existing CSP origin allows?
  - id: deleteCSPEntry
    intent: Delete a CSP origin
    question: How do I stop allowing an origin in the content security policy?
  - id: getCSPHeader
    intent: Generate the tenant CSP header
    question: What does the full Content-Security-Policy header for my tenant look like?
  phrasing_ops: 6
  slug: qliksense-csp-origins-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The csrf API from Qlik Sense — 1 operation(s) for csrf.
  name: Qlik Sense Csrf API
  phrasing_intents:
  - id: getApiV1CsrfToken
    intent: Get a CSRF token
    question: Where do I get a CSRF token for browser requests to Qlik Cloud?
  phrasing_ops: 1
  slug: qliksense-csrf-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data-asset API from Qlik Sense — 2 operation(s) for data-asset.
  name: Qlik Sense Data Asset API
  phrasing_intents:
  - id: saveDataAsset
    intent: Register a new data asset
    question: How do I save a new data asset?
  - id: batchDeleteDataAssets
    intent: Delete data assets in bulk
    question: Can I delete many data assets at once?
  - id: getDataAsset
    intent: Get a data asset
    question: How do I look up a data asset by its ID?
  - id: patchDataAsset
    intent: Partially update a data asset
    question: How do I change only a few fields on a data asset?
  - id: updateDataAsset
    intent: Replace a data asset's definition
    question: Can I overwrite every field on a data asset?
  phrasing_ops: 5
  slug: qliksense-data-asset-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data-connections API from Qlik Sense — 5 operation(s) for data-connections.
  name: Qlik Sense Data Connections API
  phrasing_intents:
  - id: getApiV1DataConnections
    intent: List data connections
    question: Which data connections can I see in my tenant?
  - id: postApiV1DataConnections
    intent: Create a data connection
    question: Can I create a new connection to a database or file source?
  - id: getApiV1DataConnectionsByQID
    intent: Get a data connection
    question: Can I look up a single data connection by its ID or name?
  - id: patchApiV1DataConnectionsByQID
    intent: Patch a data connection
    question: Can I change just one property of a data connection?
  - id: putApiV1DataConnectionsByQID
    intent: Replace a data connection
    question: Can I rewrite a data connection's connect statement and credentials?
  - id: deleteApiV1DataConnectionsByQID
    intent: Delete a data connection
    question: Can I remove a single data connection I no longer use?
  - id: postApiV1DataConnectionsActionsDelete
    intent: Bulk delete data connections
    question: Can an admin delete many data connections in a single request?
  - id: postApiV1DataConnectionsActionsDuplicate
    intent: Duplicate a data connection
    question: Can I clone an existing data connection?
  phrasing_ops: 9
  slug: qliksense-data-connections-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data-credentials API from Qlik Sense — 2 operation(s) for data-credentials.
  name: Qlik Sense Data Credentials API
  phrasing_intents:
  - id: getApiV1DataCredentialsByQID
    intent: Get a data credential
    question: Can I look up a stored data credential by ID or by name?
  - id: patchApiV1DataCredentialsByQID
    intent: Patch a data credential
    question: Can I change one field of a data credential without resending all of it?
  - id: putApiV1DataCredentialsByQID
    intent: Replace a data credential
    question: Can I rotate the username and password stored in a data credential?
  - id: deleteApiV1DataCredentialsByQID
    intent: Delete a data credential
    question: Can I remove a stored data credential?
  - id: postApiV1DataCredentialsActionsFilterOrphan
    intent: Find orphaned data credentials
    question: Which data credentials are no longer attached to any connection?
  phrasing_ops: 5
  slug: qliksense-data-credentials-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data-product-activation API from Qlik Sense — 2 operation(s) for data-product-activation.
  name: Qlik Sense Data Product Activation API
  phrasing_intents:
  - id: activateDataProduct
    intent: Activate a data product
    question: How do I make a data product discoverable to consumers?
  - id: deactivateDataProduct
    intent: Deactivate a data product
    question: How do I stop a data product from being consumed?
  phrasing_ops: 2
  slug: qliksense-data-product-activation-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data-product API from Qlik Sense — 4 operation(s) for data-product.
  name: Qlik Sense Data Product API
  phrasing_intents:
  - id: createDataProduct
    intent: Create a data product
    question: How do I package related datasets into a governed data product?
  - id: getDataProduct
    intent: Get a data product
    question: What datasets and contacts belong to a data product?
  - id: patchDataProduct
    intent: Update a data product
    question: Can I add datasets or change tags on an existing data product?
  - id: deleteDataProduct
    intent: Delete a data product
    question: Does deleting a data product also delete its datasets?
  - id: getDataProductDoc
    intent: Export data product documentation
    question: How do I export a data product's documentation as Markdown?
  - id: moveDataProduct
    intent: Move a data product to another space
    question: How do I move a data product into a different space?
  phrasing_ops: 6
  slug: qliksense-data-product-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data-product-changelog API from Qlik Sense — 1 operation(s) for data-product-changelog.
  name: Qlik Sense Data Product Changelog API
  phrasing_intents:
  - id: getDataProductChangelog
    intent: Get a data product's change history
    question: What changes have been made to a data product over time?
  phrasing_ops: 1
  slug: qliksense-data-product-changelog-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data-product-data-quality API from Qlik Sense — 1 operation(s) for data-product-data-quality.
  name: Qlik Sense Data Product Data Quality API
  phrasing_intents:
  - id: requestDataQualityComputation
    intent: Compute data quality for a data product
    question: How do I run a data quality assessment across every dataset in a data product?
  phrasing_ops: 1
  slug: qliksense-data-product-data-quality-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data-product-generate-provider-url API from Qlik Sense — 1 operation(s) for data-product-generate-provider-url.
  name: Qlik Sense Data Product Generate Provider URL API
  phrasing_intents:
  - id: generateProviderUiUrl
    intent: Generate a provider UI URL for a dataset
    question: How do I get a link to the third-party provider's interface for a data product dataset?
  phrasing_ops: 1
  slug: qliksense-data-product-generate-provider-url-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data project actions API from Qlik Sense — 2 operation(s) for data project actions.
  name: Qlik Sense data project actions API
  phrasing_intents:
  - id: prepare_project
    intent: Prepare a data integration project
    question: How do I get a data integration project ready to run?
  - id: validate_project
    intent: Validate a data integration project
    question: Are there errors in my data integration project before I run it?
  phrasing_ops: 2
  slug: qliksense-data-project-actions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data project API from Qlik Sense — 2 operation(s) for data project.
  name: Qlik Sense data project API
  phrasing_intents:
  - id: list_projects
    intent: List data integration projects
    question: Which data integration projects exist in my Qlik tenant?
  - id: create_project
    intent: Create a data integration project
    question: How do I start a new data integration project in a space?
  - id: get_project
    intent: Get a data integration project
    question: Where can I see the settings of one data integration project?
  phrasing_ops: 3
  slug: qliksense-data-project-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data project deployment API from Qlik Sense — 5 operation(s) for data project deployment.
  name: Qlik Sense data project deployment API
  phrasing_intents:
  - id: export_project
    intent: Export a data integration project
    question: How do I export a data integration project to move it to another tenant?
  - id: import_project
    intent: Import a legacy JSON project zip synchronously
    question: Can I import a legacy JSON-format project zip and wait for it to finish?
  - id: import_project_async
    intent: Import a project zip in the background
    question: What is the recommended way to import a YAML-based data integration project?
  - id: get_project_export_variables
    intent: Get a project's export variables
    question: Which export variables (bindings) does a data integration project have?
  - id: update_project_export_variables
    intent: Update a project's export variables
    question: Can I change the binding values a project uses when exported?
  - id: validate_project_definitions
    intent: Validate project definition files before import
    question: Can I check a project zip for errors before importing it?
  phrasing_ops: 6
  slug: qliksense-data-project-deployment-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data-quality API from Qlik Sense — 4 operation(s) for data-quality.
  name: Qlik Sense Data Quality API
  phrasing_intents:
  - id: getFieldQualitiesFiltered
    intent: Get field-level quality for many datasets
    question: Can I get per-field data quality metrics for up to 100 datasets at once?
  - id: getDataQualityGlobalResults
    intent: Get a dataset's global quality (data-governance path)
    question: How many valid, invalid and empty cells does one dataset have on the data-governance quality endpoint?
  - id: getDataQualityGlobalResultsFiltered
    intent: Get global quality for many datasets
    question: Can I compare overall data quality across a list of datasets in one call?
  - id: getApiV1DataQualitiesGlobalResults
    intent: Get a dataset's global quality (v1 path)
    question: Where is the v1 endpoint for a single dataset's global quality counts?
  phrasing_ops: 4
  slug: qliksense-data-quality-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data-sources API from Qlik Sense — 4 operation(s) for data-sources.
  name: Qlik Sense Data Sources API
  phrasing_intents:
  - id: getDataSources
    intent: List available data sources
    question: Which data source connectors are available in my Qlik Cloud tenant?
  - id: getApiV1DataSourcesByDataSourceIdApiSpecs
    intent: Get connection properties of a data source
    question: Which connection properties does a given data source connector require?
  - id: getApiV1DataSourcesByDataSourceIdGateways
    intent: List gateways for a data source
    question: Which data gateways can I use to reach a particular data source?
  - id: getDataSourceSettings
    intent: Get data source settings
    question: Is a particular data source enabled or disabled?
  - id: updateDataSourceSettings
    intent: Enable or disable a data source
    question: How do I disable a data source for everyone in the tenant?
  phrasing_ops: 5
  slug: qliksense-data-sources-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data task actions API from Qlik Sense — 4 operation(s) for data task actions.
  name: Qlik Sense data task actions API
  phrasing_intents:
  - id: prepare_task
    intent: Prepare a data task for running
    question: How do I prepare a data integration task before running it?
  - id: recreate_task_datasets
    intent: Recreate a data task's datasets
    question: How do I rebuild the datasets of a data task from scratch?
  - id: reload_task
    intent: Request a dataset reload for a data task
    question: Does requesting a reload run immediately or on the task's next run?
  - id: validate_task
    intent: Validate a data task
    question: How do I check that a data integration task is valid before running it?
  phrasing_ops: 4
  slug: qliksense-data-task-actions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data task API from Qlik Sense — 2 operation(s) for data task.
  name: Qlik Sense data task API
  phrasing_intents:
  - id: list_project_tasks
    intent: List data tasks in a project
    question: Which data tasks belong to a data integration project?
  - id: get_data_task
    intent: Get a data task in a project
    question: Can I look up one specific data task within a project?
  phrasing_ops: 2
  slug: qliksense-data-task-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The data task runtime API from Qlik Sense — 4 operation(s) for data task runtime.
  name: Qlik Sense data task runtime API
  phrasing_intents:
  - id: start_data_task
    intent: Start a data integration task
    question: How do I start a data task in a data integration project?
  - id: stop_data_task
    intent: Stop a data integration task
    question: How do I stop a running data task?
  - id: get_data_task_runtime_state
    intent: Get a data task's runtime state
    question: Is my data task running right now?
  - id: list_data_task_datasets
    intent: List dataset runtime states for a task
    question: Which datasets in my data task are loading or failing?
  phrasing_ops: 4
  slug: qliksense-data-task-runtime-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The datafiles API from Qlik Sense — 9 operation(s) for datafiles.
  name: Qlik Sense Datafiles API
  phrasing_intents:
  - id: getApiV1DataFiles
    intent: List data files and folders
    question: Which data files have been uploaded to my tenant?
  - id: postApiV1DataFiles
    intent: Upload a data file or create a folder
    question: Can I upload a CSV or Excel file for apps to load?
  - id: getApiV1DataFilesById
    intent: Get a data file's details
    question: Can I see the size and owner of one uploaded data file?
  - id: putApiV1DataFilesById
    intent: Re-upload a data file or update a folder
    question: Can I overwrite an existing data file with a newer version?
  - id: deleteApiV1DataFilesById
    intent: Delete a data file or folder
    question: Can I delete one uploaded data file?
  - id: postApiV1DataFilesByIdActionsChangeOwner
    intent: Change a data file's owner
    question: Can an admin reassign a data file to another user?
  - id: postApiV1DataFilesByIdActionsChangeSpace
    intent: Move one data file to another space
    question: Can I move a single data file into a shared space?
  - id: postApiV1DataFilesActionsChangeSpace
    intent: Move many data files between spaces
    question: Can I move a whole batch of data files to another space in one call?
  phrasing_ops: 12
  slug: qliksense-datafiles-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The deliveries API from Qlik Sense — 3 operation(s) for deliveries.
  name: Qlik Sense Deliveries API
  phrasing_intents:
  - id: getWebhookDeliveryList
    intent: List deliveries for a webhook
    question: Which webhook deliveries failed recently?
  - id: getWebhookDelivery
    intent: Get a webhook delivery
    question: What payload and response did a specific webhook delivery have?
  - id: resendDelivery
    intent: Resend a webhook delivery
    question: Can I retry a failed webhook delivery?
  phrasing_ops: 3
  slug: qliksense-deliveries-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The deployments API from Qlik Sense — 6 operation(s) for deployments.
  name: Qlik Sense Deployments API
  phrasing_intents:
  - id: getDeployments
    intent: List ML deployments
    question: Which AutoML deployments exist in my Qlik tenant?
  - id: postDeployment
    intent: Create an ML deployment
    question: How do I create a new machine learning deployment?
  - id: getDeployment
    intent: Get an ML deployment
    question: Where can I see the details of one ML deployment?
  - id: patchDeployment
    intent: Update an ML deployment
    question: Can I edit properties of an existing ML deployment?
  - id: deleteDeployment
    intent: Delete an ML deployment
    question: Can I delete an ML deployment I no longer need?
  - id: activateDeploymentModels
    intent: Activate a deployment's model
    question: How do I turn on the model behind an ML deployment for predictions?
  - id: deactivateDeploymentModels
    intent: Deactivate a deployment's model
    question: Can I temporarily switch off the model of an ML deployment?
  - id: addDeployedModels
    intent: Add models to an ML deployment
    question: Can one ML deployment serve more than one model?
  phrasing_ops: 9
  slug: qliksense-deployments-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The direct-access-agent-benchmarking API from Qlik Sense — 3 operation(s) for direct-access-agent-benchmarking.
  name: Qlik Sense Direct Access Agent Benchmarking API
  phrasing_intents:
  - id: runBenchmark
    intent: Start a Direct Access agent benchmark
    question: How do I measure the throughput and latency of a Direct Access agent?
  - id: getBenchmarkStatus
    intent: Check a benchmark's status and results
    question: Is my Direct Access agent benchmark still running?
  - id: cancelBenchmark
    intent: Cancel a running benchmark
    question: Can I stop a Direct Access agent benchmark that is taking too long?
  phrasing_ops: 3
  slug: qliksense-direct-access-agent-benchmarking-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The direct-access-agent-configuration API from Qlik Sense — 7 operation(s) for direct-access-agent-configuration.
  name: Qlik Sense Direct Access Agent Configuration API
  phrasing_intents:
  - id: restartConnectorAgentServiceAsync
    intent: Restart a Direct Access Gateway agent
    question: How do I restart a Direct Access Gateway agent remotely?
  - id: getConnectorAgentConfigAsync
    intent: Get a gateway agent configuration
    question: Where can I read the local configuration of a Direct Access Gateway agent?
  - id: patchConnectorAgentConfigurationAsync
    intent: Patch a gateway agent configuration
    question: How do I change a setting in a gateway agent's local configuration with JSON Patch?
  - id: getConnectorFileListAsync
    intent: List a connector's configuration files
    question: Which configuration files does a given connector have on a gateway agent?
  - id: getConnectorFlatFileConfigurationAsync
    intent: Read a connector configuration file
    question: How can I read the items inside a connector's flat configuration file?
  - id: putConnectorFlatFileConfigurationAsync
    intent: Replace a connector configuration file
    question: How do I overwrite a connector's flat configuration file on the gateway agent?
  - id: getApiV1DirectAccessAgentsByAgentIdConnectorsFileConnectorFilesAllowedPaths
    intent: Get File Connector allowed paths
    question: Which folders is the File Connector allowed to read on my gateway agent?
  - id: putApiV1DirectAccessAgentsByAgentIdConnectorsFileConnectorFilesAllowedPaths
    intent: Set File Connector allowed paths
    question: How do I change which paths the File Connector may access?
  phrasing_ops: 12
  slug: qliksense-direct-access-agent-configuration-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The editable-columns API from Qlik Sense — 1 operation(s) for editable-columns.
  name: Qlik Sense Editable Columns API
  phrasing_intents:
  - id: listEditableColumns
    intent: List editable columns in a change store
    question: Which columns can users edit in a change store?
  phrasing_ops: 1
  slug: qliksense-editable-columns-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The email-config-actions API from Qlik Sense — 3 operation(s) for email-config-actions.
  name: Qlik Sense Email Config Actions API
  phrasing_intents:
  - id: sendTestEmailAction
    intent: Send a test email
    question: How can I confirm my tenant's email setup actually delivers mail?
  - id: validateAction
    intent: Check whether the email config is valid
    question: Is my saved email configuration marked valid, without contacting the server?
  - id: verifyConnectionAction
    intent: Verify the email server connection
    question: Can I test that the mail server is reachable and the credentials work without sending an email?
  phrasing_ops: 3
  slug: qliksense-email-config-actions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The email-config API from Qlik Sense — 1 operation(s) for email-config.
  name: Qlik Sense Email Config API
  phrasing_intents:
  - id: getEmailConfig
    intent: Get the tenant's email configuration
    question: How is outgoing email configured for my Qlik Cloud tenant?
  - id: patchEmailConfig
    intent: Patch the email configuration (deprecated)
    question: Can I still partially update the email configuration with the deprecated patch call?
  - id: putEmailConfig
    intent: Set or replace the email configuration
    question: How do I set up the mail server the tenant uses to send email?
  - id: deleteEmailConfig
    intent: Delete the email configuration
    question: How do I remove the tenant's email server settings?
  phrasing_ops: 4
  slug: qliksense-email-config-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The evaluation API from Qlik Sense — 10 operation(s) for evaluation.
  name: Qlik Sense Evaluation API
  phrasing_intents:
  - id: getEvaluations
    intent: List an app's performance evaluations
    question: Which performance evaluations have been run on my Qlik Sense app over time?
  - id: queueEvaluation
    intent: Queue a performance evaluation for an app
    question: How do I measure an app's object response times, CPU usage and data model size?
  - id: compareTwo
    intent: Compare two app evaluations for regressions
    question: Did my app get slower after the last change, comparing a baseline evaluation to a new one?
  - id: downloadCompareTwo
    intent: Download a comparison log of two evaluations
    question: Where can I download the comparison log between a baseline and a new app evaluation as a file?
  - id: getOneEvaluation
    intent: Get one app evaluation's results
    question: What were the results of one specific app evaluation?
  - id: downloadOneEvaluation
    intent: Download an app evaluation log
    question: How do I download the log file for a single app evaluation?
  - id: evaluation#getEvaluations
    intent: List app evaluations via the older v1 endpoint
    question: How do I list an app's evaluations with the legacy /api/v1/apps endpoint?
  - id: evaluation#queueEvaluation
    intent: Queue an app evaluation via the older v1 endpoint
    question: Can I still queue an app evaluation through the legacy v1 apps endpoint?
  phrasing_ops: 12
  slug: qliksense-evaluation-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The evaluations API from Qlik Sense — 2 operation(s) for evaluations.
  name: Qlik Sense Evaluations API
  phrasing_intents:
  - id: executeCondition
    intent: Evaluate an alert condition
    question: Can I trigger evaluation of an alerting condition on demand?
  - id: getApiV1ConditionsByIdEvaluationsByEvaluationId
    intent: Get a condition evaluation result
    question: Can I look up the result of one past evaluation of an alert condition?
  - id: deleteApiV1ConditionsByIdEvaluationsByEvaluationId
    intent: Delete a condition evaluation
    question: Can I remove an old evaluation record from an alert condition?
  phrasing_ops: 3
  slug: qliksense-evaluations-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The experiments API from Qlik Sense — 7 operation(s) for experiments.
  name: Qlik Sense Experiments API
  phrasing_intents:
  - id: getExperiments
    intent: List ML experiments
    question: Which AutoML experiments exist in my Qlik tenant?
  - id: postExperiment
    intent: Create an ML experiment
    question: How do I start a new AutoML experiment?
  - id: getExperiment
    intent: Get an ML experiment
    question: Where can I see the details of one particular experiment?
  - id: patchExperiment
    intent: Update an ML experiment
    question: Can I rename or edit an existing experiment?
  - id: deleteExperiment
    intent: Delete an ML experiment
    question: How do I remove an experiment I no longer need?
  - id: postExperimentRecommendModels
    intent: Get model recommendations for an experiment
    question: Which model in my experiment is the most accurate or the fastest?
  - id: getExperimentModels
    intent: List models trained in an experiment
    question: What models were trained in my experiment?
  - id: getExperimentModel
    intent: Get a trained model from an experiment
    question: How do I look up one trained model's details?
  phrasing_ops: 13
  slug: qliksense-experiments-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The extensions API from Qlik Sense — 4 operation(s) for extensions.
  name: Qlik Sense Extensions API
  phrasing_intents:
  - id: getExtensions
    intent: List imported extensions
    question: Which visualization extensions have been imported into my tenant?
  - id: createExtension
    intent: Import a new extension
    question: How do I upload a new extension to the tenant?
  - id: getExtensionById
    intent: Get an extension's details
    question: Can I look up an extension by its name rather than its ID?
  - id: updateExtensionById
    intent: Update an existing extension
    question: Can I replace an installed extension with a newer file?
  - id: deleteExtensionById
    intent: Delete an extension
    question: How do I remove an extension from the tenant?
  - id: getExtensionArchive
    intent: Download an extension as a zip
    question: Can I download all of an extension's files as a zip archive?
  - id: getFileFromExtensionArchive
    intent: Download one file from an extension
    question: Can I fetch a single file out of an imported extension?
  phrasing_ops: 7
  slug: qliksense-extensions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The filters API from Qlik Sense — 3 operation(s) for filters.
  name: Qlik Sense Filters API
  phrasing_intents:
  - id: filtersList
    intent: List report filters in an app
    question: Which report filters are defined in my Qlik Sense app?
  - id: filtersCreate
    intent: Create a report filter in an app
    question: How do I save a set of selections as a filter to reapply to report output?
  - id: filtersGet
    intent: Get one report filter
    question: What field definitions are in a particular report filter?
  - id: filtersUpdate
    intent: Update a report filter
    question: Can I change the name or definition of an existing report filter?
  - id: filtersDelete
    intent: Delete a report filter
    question: How do I remove a report filter from an app?
  - id: filtersCount
    intent: Count report filters in an app
    question: How many report filters does my app have?
  phrasing_ops: 6
  slug: qliksense-filters-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The glossaries API from Qlik Sense — 4 operation(s) for glossaries.
  name: Qlik Sense Glossaries API
  phrasing_intents:
  - id: getApiV1Glossaries
    intent: List business glossaries
    question: Which business glossaries exist in my tenant?
  - id: postApiV1Glossaries
    intent: Create a business glossary
    question: Can I start a new business glossary for my team?
  - id: getApiV1GlossariesById
    intent: Get a glossary
    question: Can I see the overview and description of one glossary?
  - id: patchApiV1GlossariesById
    intent: Patch glossary properties
    question: Can I change just one property of a glossary with JSON Patch?
  - id: putApiV1GlossariesById
    intent: Replace a glossary
    question: Can I rewrite a glossary's name, overview and description all at once?
  - id: deleteApiV1GlossariesById
    intent: Delete a glossary and its terms
    question: Can I delete an entire glossary?
  - id: getApiV1GlossariesByIdActionsExport
    intent: Export a glossary
    question: Can I export a glossary with its categories and terms to a file?
  - id: postApiV1GlossariesActionsImport
    intent: Import a glossary from a file
    question: Can I import a glossary definition file with its terms and categories?
  phrasing_ops: 8
  slug: qliksense-glossaries-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The groups API from Qlik Sense — 3 operation(s) for groups.
  name: Qlik Sense Groups API
  phrasing_intents:
  - id: getGroups
    intent: List groups
    question: Which user groups exist in my Qlik Cloud tenant?
  - id: postGroups
    intent: Create a group
    question: How do I create a new user group?
  - id: getGroupById
    intent: Get a group
    question: How do I look up one group by its ID?
  - id: updateGroupById
    intent: Update a group
    question: Can I change the roles or status of an existing group?
  - id: deleteGroupById
    intent: Delete a group
    question: How do I delete a user group?
  - id: groups_api_actions_filter
    intent: Filter groups with an advanced query
    question: Can I search groups with an advanced query string in the request body?
  phrasing_ops: 6
  slug: qliksense-groups-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The groups-settings API from Qlik Sense — 1 operation(s) for groups-settings.
  name: Qlik Sense Groups Settings API
  phrasing_intents:
  - id: groups_api_get_settings
    intent: Get the tenant's group settings
    question: Is automatic group creation from the identity provider enabled for my tenant?
  - id: patchSettings
    intent: Update the tenant's group settings
    question: How do I turn off IdP group synchronization?
  phrasing_ops: 2
  slug: qliksense-groups-settings-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The iam-resources API from Qlik Sense — 3 operation(s) for iam-resources.
  name: Qlik Sense Iam Resources API
  phrasing_intents:
  - id: getAuthSettings
    intent: Get tenant session and auth settings
    question: What is my tenant's session inactivity timeout and maximum session lifespan?
  - id: updateAuthSettings
    intent: Change tenant session timeouts
    question: How do I shorten the idle session timeout for users in my tenant?
  - id: getIPPolicies
    intent: List IP allowlist policies
    question: Which IP allowlist policies exist in my Qlik Cloud tenant?
  - id: createIPPolicy
    intent: Create an IP allowlist policy
    question: How do I restrict tenant access to my office IP ranges?
  - id: getIPPolicyByID
    intent: Get an IP policy's details
    question: What addresses does a particular IP policy allow?
  - id: updateIPPolicyByID
    intent: Update an IP allowlist policy
    question: How do I add another CIDR range to an existing IP policy?
  - id: deleteIPPolicyByID
    intent: Delete an IP allowlist policy
    question: What happens to IP allowlisting if I delete the last enabled policy?
  phrasing_ops: 7
  slug: qliksense-iam-resources-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The idp API from Qlik Sense — 5 operation(s) for idp.
  name: Qlik Sense Idp API
  phrasing_intents:
  - id: getIdps
    intent: List identity providers
    question: Which identity providers are registered on my Qlik Cloud tenant?
  - id: createIdp
    intent: Register an identity provider
    question: How do I add a SAML or OIDC identity provider to my tenant?
  - id: getWellKnownMetaData
    intent: Get tenant IdP configuration metadata
    question: What IdP configuration metadata does the tenant publish in its well-known file?
  - id: getIdp
    intent: Get an identity provider
    question: How do I view the configuration of one identity provider?
  - id: updateIdp
    intent: Update an identity provider
    question: How do I change the configuration of an existing IdP?
  - id: deleteIdp
    intent: Delete an identity provider
    question: How do I remove an identity provider from my tenant?
  - id: getMeMeta
    intent: Get active interactive IdP metadata
    question: What IdP metadata is used when no interactive IdP is enabled?
  - id: getStatus
    intent: Check IdP configuration statuses
    question: Are all my identity provider configurations healthy?
  phrasing_ops: 8
  slug: qliksense-idp-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The impact API from Qlik Sense — 4 operation(s) for impact.
  name: Qlik Sense Impact API
  phrasing_intents:
  - id: getApiV1LineageGraphsImpactByIdActionsExpand
    intent: Expand a node in an impact analysis graph
    question: Can I drill into one node of an impact analysis graph to see the next level down?
  - id: getApiV1LineageGraphsImpactByIdActionsSearch
    intent: Search labels in an impact graph
    question: Can I search a downstream impact graph for a field or table by name?
  - id: getApiV1LineageGraphsImpactByIdOverview
    intent: See which resources a change would impact
    question: If I change this table, which apps and datasets downstream are affected?
  - id: getApiV1LineageGraphsImpactByIdSource
    intent: Get the levels of an impact root node
    question: Can I get the field, table and resource levels of the node I am running impact analysis on?
  phrasing_ops: 4
  slug: qliksense-impact-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The insight-analyses API from Qlik Sense — 3 operation(s) for insight-analyses.
  name: Qlik Sense Insight Analyses API
  phrasing_intents:
  - id: getAnalyses
    intent: List supported insight analyses for an app
    question: Which analysis types does Insight Advisor support for my app?
  - id: getRecommendations
    intent: Recommend analyses for a question
    question: Can I get chart recommendations from a natural language question about my app?
  - id: getBusinessModel
    intent: Get an app's logical business model
    question: Which fields and master items does Insight Advisor use for my app?
  phrasing_ops: 3
  slug: qliksense-insight-analyses-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The invite API from Qlik Sense — 1 operation(s) for invite.
  name: Qlik Sense Invite API
  phrasing_intents:
  - id: inviteUsers
    intent: Invite users by email
    question: How do I invite new people to my Qlik Cloud tenant by email?
  phrasing_ops: 1
  slug: qliksense-invite-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The items API from Qlik Sense — 4 operation(s) for items.
  name: Qlik Sense Items API
  phrasing_intents:
  - id: items#listItems
    intent: List items I can access
    question: Which apps and other items can I access in Qlik Cloud?
  - id: items#getItem
    intent: Get an item
    question: How do I look up one item's metadata?
  - id: items#updateItem
    intent: Update an item
    question: Can I rename an item or change its description?
  - id: items#deleteItem
    intent: Delete an item
    question: Does deleting an item remove it from collections too?
  - id: items#listItemCollections
    intent: List collections an item belongs to
    question: Which collections and tags is an item in?
  - id: items#listPublishedItems
    intent: List published copies of an item
    question: Where are the published copies of my app?
  phrasing_ops: 6
  slug: qliksense-items-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The items-settings API from Qlik Sense — 1 operation(s) for items-settings.
  name: Qlik Sense Items Settings API
  phrasing_intents:
  - id: items#GetSettings
    intent: Get items settings
    question: Are usage metrics enabled for items in my tenant?
  - id: items#PatchSettings
    intent: Update items settings
    question: How do I turn usage metrics on or off for items?
  phrasing_ops: 2
  slug: qliksense-items-settings-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The jobs API from Qlik Sense — 1 operation(s) for jobs.
  name: Qlik Sense Jobs API
  phrasing_intents:
  - id: cancelJobs
    intent: Cancel ML jobs
    question: How do I cancel the jobs for an AutoML experiment version?
  phrasing_ops: 1
  slug: qliksense-jobs-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The licenses API from Qlik Sense — 8 operation(s) for licenses.
  name: Qlik Sense Licenses API
  phrasing_intents:
  - id: getApiV1LicensesAssignments
    intent: List license assignments
    question: Which users have a professional or analyzer license assigned?
  - id: postApiV1LicensesAssignmentsActionsAdd
    intent: Assign licenses to users
    question: Can I give several users a license in one request?
  - id: postApiV1LicensesAssignmentsActionsDelete
    intent: Remove licenses from users
    question: Can I free up licenses by removing them from departed users?
  - id: postApiV1LicensesAssignmentsActionsUpdate
    intent: Change users' license type
    question: Can I change the license access a user already has?
  - id: getApiV1LicensesConsumption
    intent: Get license consumption
    question: How much of our license has the tenant consumed so far?
  - id: getApiV1LicensesOverview
    intent: Get the tenant license overview
    question: What license is applied to my tenant and how many seats does it include?
  - id: getApiV1LicensesSettings
    intent: Get license auto-assign settings
    question: Are new users automatically given a license in my tenant?
  - id: putApiV1LicensesSettings
    intent: Set license auto-assign settings
    question: Can I turn on automatic license assignment for new users?
  phrasing_ops: 9
  slug: qliksense-licenses-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The lineage-graphs API from Qlik Sense — 4 operation(s) for lineage-graphs.
  name: Qlik Sense Lineage Graphs API
  phrasing_intents:
  - id: getApiV1LineageGraphsNodesById
    intent: Get the lineage graph of a node
    question: Where does the data in this field or table come from upstream?
  - id: getApiV1LineageGraphsNodesByIdActionsExpand
    intent: Expand a node in a lineage graph
    question: Can I expand one node of an upstream lineage graph to see its edges?
  - id: getApiV1LineageGraphsNodesByIdActionsSearch
    intent: Search labels in a lineage graph
    question: Can I search an upstream lineage graph for a source by name?
  - id: postApiV1LineageGraphsNodesByIdOverview
    intent: Get a direct upstream lineage overview
    question: Which datasets or apps directly feed each field of a resource?
  phrasing_ops: 4
  slug: qliksense-lineage-graphs-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The Link API from Qlik Sense — 4 operation(s) for link.
  name: Qlik Sense Link API
  phrasing_intents:
  - id: linksGetV2
    intent: List ODAG links
    question: Which on-demand app generation links exist in my tenant?
  - id: linkCreateV2
    intent: Create an ODAG link
    question: How do I set up on-demand app generation between a selection app and a template app?
  - id: linkGetV2
    intent: Get an ODAG link's details
    question: Where can I review the bindings and status of one ODAG link?
  - id: linkUpdateV2
    intent: Update an ODAG link
    question: Can I change the template app or bindings on an existing ODAG link?
  - id: linkCanCreateV2
    intent: Check permission to create ODAG links
    question: Am I allowed to create new ODAG links?
  - id: syncAppLinkUsagesV2
    intent: Register ODAG links used by a selection app
    question: Which ODAG links referenced by a selection app can I actually access?
  phrasing_ops: 6
  slug: qliksense-link-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The links API from Qlik Sense — 1 operation(s) for links.
  name: Qlik Sense Links API
  phrasing_intents:
  - id: getApiV1GlossariesByIdTermsByTermIdLinks
    intent: List resources linked to a glossary term
    question: Which apps or datasets are linked to a business glossary term?
  - id: postApiV1GlossariesByIdTermsByTermIdLinks
    intent: Link a resource to a glossary term
    question: Can I link an app or dataset to a business term?
  phrasing_ops: 2
  slug: qliksense-links-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The login API from Qlik Sense — 1 operation(s) for login.
  name: Qlik Sense Login API
  phrasing_intents:
  - id: getLogin
    intent: Start an interactive login
    question: Where do I send a user to sign in with my tenant's identity provider?
  phrasing_ops: 1
  slug: qliksense-login-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The notifications API from Qlik Sense — 1 operation(s) for notifications.
  name: Qlik Sense Notifications API
  phrasing_intents:
  - id: NotificationRequest
    intent: List supported notifications
    question: What notification types can users subscribe to?
  phrasing_ops: 1
  slug: qliksense-notifications-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The oauth-clients API from Qlik Sense — 6 operation(s) for oauth-clients.
  name: Qlik Sense OAUTH Clients API
  phrasing_intents:
  - id: readAllOAuthClients
    intent: List OAuth clients in the tenant
    question: Which OAuth clients are registered in my Qlik Cloud tenant?
  - id: createOAuthClient
    intent: Register a new OAuth client
    question: How do I register an OAuth client for a web app or SPA to connect to my tenant?
  - id: readOAuthClient
    intent: Get an OAuth client's details
    question: What redirect URIs and scopes does a particular OAuth client have?
  - id: patchOAuthClient
    intent: Update an OAuth client's settings
    question: Can I add client_secret as an auth method on an existing OAuth client and get a secret back?
  - id: deleteOAuthClient
    intent: Delete an OAuth client
    question: What confirmation header do I need to delete an OAuth client?
  - id: publishOAuthClient
    intent: Publish an OAuth client to all tenants in a region
    question: How can a third-party app use the same client ID across every Qlik Cloud tenant in a region?
  - id: createOAuthClientSecret
    intent: Generate a new OAuth client secret
    question: How many client secrets can one OAuth client hold at once?
  - id: deleteOAuthClientSecret
    intent: Revoke an OAuth client secret
    question: How do I revoke one old secret on an OAuth client without deleting the client?
  phrasing_ops: 11
  slug: qliksense-oauth-clients-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The oauth-tokens API from Qlik Sense — 2 operation(s) for oauth-tokens.
  name: Qlik Sense OAUTH Tokens API
  phrasing_intents:
  - id: getApiV1OauthTokens
    intent: List OAuth tokens
    question: Which OAuth tokens have been issued to users in my tenant?
  - id: deleteApiV1OauthTokensByTokenId
    intent: Revoke an OAuth token
    question: Can I revoke an OAuth token that may have leaked?
  phrasing_ops: 2
  slug: qliksense-oauth-tokens-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The outputs API from Qlik Sense — 1 operation(s) for outputs.
  name: Qlik Sense Outputs API
  phrasing_intents:
  - id: getOutputs
    intent: List a report request's outputs
    question: Which files has my report request produced so far?
  phrasing_ops: 1
  slug: qliksense-outputs-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The owl API from Qlik Sense — 1 operation(s) for owl.
  name: Qlik Sense Owl API
  phrasing_intents:
  - id: getAdaptiveCards
    intent: List Adaptive Cards for app metrics
    question: Which metric insight cards has the discovery agent produced for my apps?
  phrasing_ops: 1
  slug: qliksense-owl-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The pinned links API from Qlik Sense — 4 operation(s) for pinned links.
  name: Qlik Sense pinned links API
  phrasing_intents:
  - id: getPinnedLinks
    intent: List pinned links
    question: Which pinned navigation links are set up in the tenant?
  - id: createPinnedLink
    intent: Create a pinned link
    question: How do I pin a link to the Qlik Cloud navigation for all users?
  - id: getPinnedLink
    intent: Get a pinned link
    question: How do I look up one pinned link by its ID?
  - id: patchPinnedLink
    intent: Update a pinned link
    question: Can I rename or change the URL of an existing pinned link?
  - id: deletePinnedLink
    intent: Delete a pinned link
    question: How do I unpin a single navigation link?
  - id: postPinnedLinksBulkCreate
    intent: Create several pinned links at once
    question: Can I add multiple pinned links in one request?
  - id: postPinnedLinksDeleteAll
    intent: Delete all pinned links
    question: How do I clear every pinned link in the tenant at once?
  phrasing_ops: 7
  slug: qliksense-pinned-links-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The predictions API from Qlik Sense — 6 operation(s) for predictions.
  name: Qlik Sense Predictions API
  phrasing_intents:
  - id: predictRealtimeWithAlias
    intent: Get real-time predictions via a deployment alias
    question: Can I call a deployed model through an alias to get instant predictions?
  - id: getBatchPredictions
    intent: List batch prediction configurations
    question: What batch prediction jobs are set up for my deployment?
  - id: postBatchPrediction
    intent: Create a batch prediction configuration
    question: How do I set up a batch prediction job for a deployed model?
  - id: getBatchPrediction
    intent: Get a batch prediction
    question: Where can I see the configuration and status of one batch prediction?
  - id: patchBatchPrediction
    intent: Update a batch prediction
    question: Can I change the settings of an existing batch prediction?
  - id: deleteBatchPrediction
    intent: Delete a batch prediction
    question: How do I remove a batch prediction job I no longer need?
  - id: predictBatchPrediction
    intent: Run a batch prediction now
    question: How do I trigger a batch prediction to run immediately?
  - id: getBatchPredictionSchedule
    intent: Get a batch prediction schedule
    question: When is my batch prediction scheduled to run?
  phrasing_ops: 12
  slug: qliksense-predictions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The profile API from Qlik Sense — 1 operation(s) for profile.
  name: Qlik Sense Profile API
  phrasing_intents:
  - id: getDataSetProfiles
    intent: Get a dataset's profile
    question: Has a profile already been computed for my dataset?
  phrasing_ops: 1
  slug: qliksense-profile-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The profile-insights API from Qlik Sense — 2 operation(s) for profile-insights.
  name: Qlik Sense Profile Insights API
  phrasing_intents:
  - id: postProfileInsights
    intent: Start generating profile insights
    question: How do I profile a dataset before building an ML experiment?
  - id: getProfileInsights
    intent: Get profile insights for a dataset
    question: Are the profile insights for my dataset ready yet?
  phrasing_ops: 2
  slug: qliksense-profile-insights-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The questions API from Qlik Sense — 2 operation(s) for questions.
  name: Qlik Sense Questions API
  phrasing_intents:
  - id: postApiV1QuestionsActionsAsk
    intent: Ask a natural-language question of your data
    question: Can I ask a plain-English question about my data and get an answer back?
  - id: filterMetrics
    intent: Find natural-language metrics for apps
    question: What natural-language metrics are available for my apps?
  phrasing_ops: 2
  slug: qliksense-questions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The quotas API from Qlik Sense — 2 operation(s) for quotas.
  name: Qlik Sense Quotas API
  phrasing_intents:
  - id: quotas
    intent: List tenant quotas
    question: What quotas apply to my Qlik tenant?
  - id: quota
    intent: Get one tenant quota
    question: How close am I to a specific quota limit?
  phrasing_ops: 2
  slug: qliksense-quotas-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The reload-tasks API from Qlik Sense — 2 operation(s) for reload-tasks.
  name: Qlik Sense Reload Tasks API
  phrasing_intents:
  - id: getApiV1ReloadTasks
    intent: List scheduled reload tasks
    question: Which scheduled reload tasks do I have access to?
  - id: postApiV1ReloadTasks
    intent: Schedule recurring reloads for an app
    question: Can I set an app to reload on a recurring schedule?
  - id: getApiV1ReloadTasksByTaskId
    intent: Get a reload task
    question: Can I see the schedule and state of one reload task?
  - id: putApiV1ReloadTasksByTaskId
    intent: Change a reload task schedule
    question: Can I change how often a scheduled reload runs?
  - id: deleteApiV1ReloadTasksByTaskId
    intent: Delete a reload task
    question: Can I remove a scheduled reload I no longer need?
  phrasing_ops: 5
  slug: qliksense-reload-tasks-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The reloads API from Qlik Sense — 3 operation(s) for reloads.
  name: Qlik Sense Reloads API
  phrasing_intents:
  - id: getApiV1Reloads
    intent: List reloads of an app
    question: Which reloads have run for a given app and did they succeed?
  - id: postApiV1Reloads
    intent: Reload an app now
    question: Can I trigger an app reload right away instead of waiting for the schedule?
  - id: getApiV1ReloadsByReloadId
    intent: Get a reload record
    question: Is a reload I started still running, or has it finished?
  - id: postApiV1ReloadsByReloadIdActionsCancel
    intent: Cancel a reload
    question: Can I stop a reload that is queued or taking too long?
  phrasing_ops: 4
  slug: qliksense-reloads-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The report-templates API from Qlik Sense — 3 operation(s) for report-templates.
  name: Qlik Sense Report Templates API
  phrasing_intents:
  - id: getReportTemplates
    intent: List report templates
    question: Which report templates are available to me?
  - id: createReportTemplate
    intent: Create a report template
    question: How do I add a new report template from an uploaded file?
  - id: getReportTemplate
    intent: Get a report template
    question: Where can I see info about one report template?
  - id: patchReportTemplate
    intent: Patch a report template
    question: Can I change just the name or description of a report template?
  - id: updateReportTemplate
    intent: Replace a report template
    question: How do I replace the file behind an existing report template?
  - id: deleteReportTemplate
    intent: Delete a report template
    question: How do I remove a report template?
  - id: downloadReportTemplate
    intent: Download a report template file
    question: How do I download the file behind a report template?
  phrasing_ops: 7
  slug: qliksense-report-templates-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The reports API from Qlik Sense — 1 operation(s) for reports.
  name: Qlik Sense Reports API
  phrasing_intents:
  - id: postReports
    intent: Queue a report generation request
    question: How do I generate a PDF or PowerPoint report from a Qlik Sense app?
  phrasing_ops: 1
  slug: qliksense-reports-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The Request API from Qlik Sense — 6 operation(s) for request.
  name: Qlik Sense Request API
  phrasing_intents:
  - id: linkRequestsGetV2
    intent: List on-demand app requests for an ODAG link
    question: Which on-demand app generation requests have been made through one ODAG link?
  - id: linkRequestCreateV2
    intent: Request a new on-demand app from an ODAG link
    question: How do I generate an on-demand app from my current selections in a selection app?
  - id: requestGetV2
    intent: Check the status of an ODAG request
    question: Is my on-demand app request still queued, loading, succeeded or failed?
  - id: requestActionV2
    intent: Pause, resume or cancel an ODAG request
    question: Can I cancel an on-demand app request once its data has started loading?
  - id: deleteAppV2
    intent: Delete an app generated by an ODAG request
    question: Who is allowed to delete an app that an on-demand request generated?
  - id: reloadAppV2
    intent: Reload data in an ODAG-generated app
    question: Can I refresh the data in an on-demand generated app from its sources?
  - id: renameAppV2
    intent: Rename an ODAG-generated app
    question: How do I give an on-demand generated app a better name?
  - id: getSelectionsV2
    intent: Get the selections behind an ODAG request
    question: Which field values were selected when an on-demand app request was submitted?
  phrasing_ops: 8
  slug: qliksense-request-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The roles API from Qlik Sense — 2 operation(s) for roles.
  name: Qlik Sense Roles API
  phrasing_intents:
  - id: getRoles
    intent: List roles in the tenant
    question: Which roles exist in my Qlik Cloud tenant, including custom ones?
  - id: createRole
    intent: Create a custom role
    question: How do I create a custom role with a specific set of scopes?
  - id: getRoleById
    intent: Get a role's details
    question: What scopes does a particular role grant?
  - id: updateRoleById
    intent: Update a custom role
    question: How do I change the scopes on a custom role I created?
  - id: deleteRoleById
    intent: Delete a custom role
    question: Can I delete a custom role that is still assigned to users?
  phrasing_ops: 5
  slug: qliksense-roles-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The search API from Qlik Sense — 2 operation(s) for search.
  name: Qlik Sense Search API
  phrasing_intents:
  - id: searchAssistants
    intent: Search an assistant's knowledge
    question: How do I run a semantic search over the content behind one of my assistants?
  - id: postApiV1KnowledgebasesByIdActionsSearch
    intent: Search chunks in a knowledge base
    question: Can I run a semantic search directly against one knowledge base?
  phrasing_ops: 2
  slug: qliksense-search-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The setting API from Qlik Sense — 1 operation(s) for setting.
  name: Qlik Sense Setting API
  phrasing_intents:
  - id: notesConfigGet
    intent: Check whether notes are enabled
    question: Is the notes feature turned on for my tenant and user?
  - id: updateNoteSettingsConfig
    intent: Turn the notes feature on or off
    question: How do I enable notes for the whole tenant?
  phrasing_ops: 2
  slug: qliksense-setting-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The Settings API from Qlik Sense — 2 operation(s) for settings.
  name: Qlik Sense Settings API
  phrasing_intents:
  - id: getV2
    intent: Get ODAG settings
    question: Is on-demand app generation enabled on my tenant?
  - id: updateV2
    intent: Update ODAG settings
    question: How do I turn on-demand app generation on or off?
  - id: canUpdateV2
    intent: Check permission to change ODAG settings
    question: Am I allowed to change the ODAG settings?
  phrasing_ops: 3
  slug: qliksense-settings-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The shares API from Qlik Sense — 2 operation(s) for shares.
  name: Qlik Sense Shares API
  phrasing_intents:
  - id: getSpaceShares
    intent: List shares in a space
    question: Who has resources in a space shared with them?
  - id: createSpaceShare
    intent: Share a resource in a space
    question: How do I share an item in a space with a user or group?
  - id: getSpaceShareById
    intent: Get a space share
    question: How do I look up one share in a space?
  - id: patchShareById
    intent: Update a space share
    question: Can I change the roles on an existing space share?
  - id: deleteSpaceShareById
    intent: Revoke a space share
    question: How do I stop sharing a resource with someone in a space?
  phrasing_ops: 5
  slug: qliksense-shares-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The sharing settings API from Qlik Sense — 1 operation(s) for sharing settings.
  name: Qlik Sense sharing settings API
  phrasing_intents:
  - id: sharingSettingsGet
    intent: Get sharing settings
    question: Is sharing of tasks and reports enabled in my tenant?
  - id: sharingSettingsPatch
    intent: Toggle individual sharing settings
    question: Can I flip one sharing toggle without resending the whole configuration?
  - id: sharingAPISettingsUpload
    intent: Replace sharing settings
    question: Can a tenant admin turn sharing on and cap the number of recipients?
  phrasing_ops: 3
  slug: qliksense-sharing-settings-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The sharing tasks actions API from Qlik Sense — 2 operation(s) for sharing tasks actions.
  name: Qlik Sense sharing tasks actions API
  phrasing_intents:
  - id: sharingTasksActionsCancel
    intent: Cancel a sharing task run
    question: How do I stop a recurring sharing task that is currently running?
  - id: sharingTasksActionsRecurring
    intent: Run a sharing task now
    question: Can I trigger a recurring sharing task immediately instead of waiting for its schedule?
  phrasing_ops: 2
  slug: qliksense-sharing-tasks-actions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The sharing tasks API from Qlik Sense — 2 operation(s) for sharing tasks.
  name: Qlik Sense sharing tasks API
  phrasing_intents:
  - id: sharingTasksList
    intent: List sharing tasks
    question: Which report sharing tasks are set up?
  - id: sharingTasksCreateRecurring
    intent: Create a recurring sharing task
    question: How do I schedule a report to be emailed to people regularly?
  - id: sharingTasksIDGet
    intent: Get a sharing task
    question: What are the settings of one sharing task?
  - id: sharingTasksUpdate
    intent: Update a sharing task
    question: Can I change the recipients or schedule of a sharing task?
  - id: sharingTasksDelete
    intent: Delete a sharing task
    question: How do I stop and remove a scheduled report share?
  phrasing_ops: 5
  slug: qliksense-sharing-tasks-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The sharing tasks executions API from Qlik Sense — 3 operation(s) for sharing tasks executions.
  name: Qlik Sense sharing tasks executions API
  phrasing_intents:
  - id: SharingExecutionsList
    intent: List executions of a sharing task
    question: When has one of my sharing tasks run, and did each run succeed?
  - id: sharingExecutionsIDGet
    intent: Get one sharing task execution
    question: What happened in the latest run of a sharing task?
  - id: sharingExecutionsFilesAliasGet
    intent: Download a file from a sharing task execution
    question: How do I download the report file a sharing task produced?
  phrasing_ops: 3
  slug: qliksense-sharing-tasks-executions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The spaces API from Qlik Sense — 3 operation(s) for spaces.
  name: Qlik Sense Spaces API
  phrasing_intents:
  - id: getSpaces
    intent: List spaces
    question: Which spaces do I have access to in Qlik Cloud?
  - id: createSpace
    intent: Create a space
    question: How do I create a new shared or managed space?
  - id: getSpaceById
    intent: Get a space
    question: Where do I see the details of a single space?
  - id: patchSpaceById
    intent: Change individual space properties
    question: Can I change just one property of a space without resending the rest?
  - id: updateSpaceById
    intent: Replace a space's name, owner and description
    question: Can I update all of a space's properties in one full replace?
  - id: deleteSpaceById
    intent: Delete a space
    question: What happens to content if I delete a space before emptying it?
  - id: getTypes
    intent: List available space types
    question: Which space types are available in my tenant?
  phrasing_ops: 7
  slug: qliksense-spaces-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The starters API from Qlik Sense — 3 operation(s) for starters.
  name: Qlik Sense Starters API
  phrasing_intents:
  - id: getApiV1AssistantsByAssistantIdStarters
    intent: List an assistant's starter questions
    question: Which starter questions does an assistant suggest to users?
  - id: postApiV1AssistantsByAssistantIdStarters
    intent: Add a starter question to an assistant
    question: Can I add a suggested starter question to an assistant?
  - id: getApiV1AssistantsByAssistantIdStartersByStarterId
    intent: Get a starter question
    question: Can I view one starter question and its follow-ups?
  - id: putApiV1AssistantsByAssistantIdStartersByStarterId
    intent: Update a starter question
    question: Can I reword a starter question or its recommended answer?
  - id: deleteApiV1AssistantsByAssistantIdStartersByStarterId
    intent: Delete a starter question
    question: Can I remove a starter question from an assistant?
  - id: putApiV1AssistantsByAssistantIdStartersByStarterIdFollowupsByFollowupId
    intent: Update a starter follow-up
    question: Can I edit a follow-up question attached to a starter?
  - id: deleteApiV1AssistantsByAssistantIdStartersByStarterIdFollowupsByFollowupId
    intent: Delete a starter follow-up
    question: Can I remove one follow-up while keeping its starter question?
  phrasing_ops: 7
  slug: qliksense-starters-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The status API from Qlik Sense — 1 operation(s) for status.
  name: Qlik Sense Status API
  phrasing_intents:
  - id: getStatus
    intent: Check a report request's status
    question: Is my report request finished processing?
  phrasing_ops: 1
  slug: qliksense-status-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The task API from Qlik Sense — 14 operation(s) for task.
  name: Qlik Sense Task API
  phrasing_intents:
  - id: listTasks
    intent: List scheduled tasks I can access
    question: Which scheduling tasks can I see in my Qlik Cloud tenant, and when did each last run?
  - id: createTask
    intent: Create a scheduled workflow task
    question: How do I create a new scheduled task with a Serverless Workflow definition?
  - id: getTask
    intent: Get a scheduled task's full definition
    question: What trigger and state definitions does one of my scheduling tasks have?
  - id: patchTask
    intent: Partially update a scheduled task
    question: Can I change just one field of a scheduling task with a JSON Patch instead of resending the whole thing?
  - id: updateTask
    intent: Replace a scheduled task's whole definition
    question: What happens to fields I leave out when I replace a scheduling task's full definition?
  - id: deleteTask
    intent: Delete a scheduled task and cancel its runs
    question: Does deleting a scheduling task also cancel its pending runs?
  - id: startTask
    intent: Run a scheduled task immediately
    question: Can I trigger a scheduling task right now outside its normal schedule?
  - id: getTaskRuns
    intent: List the run history of a scheduled task
    question: When did one of my scheduling tasks run, and who triggered each run?
  phrasing_ops: 21
  slug: qliksense-task-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The task-graph API from Qlik Sense — 5 operation(s) for task-graph.
  name: Qlik Sense Task Graph API
  phrasing_intents:
  - id: listAncestorTasks
    intent: Get a task's upstream ancestor graph
    question: Which upstream tasks must run before a given scheduled task, several levels up?
  - id: listChildTasks
    intent: List a task's direct child tasks
    question: Which tasks are triggered directly when a given task succeeds?
  - id: listDescendantTasks
    intent: Get a task's downstream descendant graph
    question: What is the full chain of downstream tasks a task will eventually trigger?
  - id: listParentTasks
    intent: List a task's direct parent tasks
    question: Which tasks directly trigger a given task when they complete?
  - id: listTaskSubgraph
    intent: Get a task's full dependency subgraph
    question: Can I see both upstream and downstream dependencies of a task in one graph?
  phrasing_ops: 5
  slug: qliksense-task-graph-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The task run history API from Qlik Sense — 3 operation(s) for task run history.
  name: Qlik Sense task run history API
  phrasing_intents:
  - id: get_task_run_state
    intent: Get the state of a data task run
    question: What happened during a specific past run of a data task?
  - id: list_task_run_datasets
    intent: List dataset states for a task run
    question: How did each dataset fare in a particular task run?
  - id: search_task_runs
    intent: Search a data task's run history
    question: How do I look through the run history of a data task?
  phrasing_ops: 3
  slug: qliksense-task-run-history-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The Temporary contents API from Qlik Sense — 5 operation(s) for temporary contents.
  name: Qlik Sense Temporary contents API
  phrasing_intents:
  - id: TempContentsPost
    intent: Upload a temporary file
    question: How do I upload a file that only needs to live for a short time?
  - id: TempContentsGet
    intent: Download a temporary file
    question: Can I download just a byte range of a temporary file?
  - id: TempContentsDetails
    intent: Get a temporary file's metadata
    question: What is the name, size and expiry of a temporary file?
  - id: postTus
    intent: Start a resumable upload (tus)
    question: How do I start a resumable upload for a large file using the tus protocol?
  - id: patchTus
    intent: Send a chunk of a resumable upload (tus)
    question: How do I send the next chunk of a resumable tus upload?
  phrasing_ops: 5
  slug: qliksense-temporary-contents-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The tenant key migration information API from Qlik Sense — 1 operation(s) for tenant key migration information.
  name: Qlik Sense tenant key migration information API
  phrasing_intents:
  - id: getApiV1EncryptionKeyprovidersMigrationActionsDetails
    intent: Check encryption key migration progress
    question: Is my tenant's encryption key migration still running?
  phrasing_ops: 1
  slug: qliksense-tenant-key-migration-information-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The tenant key provider management API from Qlik Sense — 3 operation(s) for tenant key provider management.
  name: Qlik Sense tenant key provider management API
  phrasing_intents:
  - id: getApiV1EncryptionKeyproviders
    intent: List AWS KMS key providers
    question: Which customer-managed AWS KMS keys are registered for my tenant?
  - id: postApiV1EncryptionKeyproviders
    intent: Register an AWS KMS key
    question: Can I bring my own multi-region AWS KMS key to encrypt tenant data?
  - id: getApiV1EncryptionKeyprovidersActionsList
    intent: List all key providers including default
    question: Can I see every key provider on the tenant, including the Qlik default?
  - id: postApiV1EncryptionKeyprovidersActionsResetToDefaultProvider
    intent: Revert to the Qlik managed encryption key
    question: Can I switch my tenant back to the default Qlik managed key?
  phrasing_ops: 4
  slug: qliksense-tenant-key-provider-management-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The tenant key provider operations API from Qlik Sense — 3 operation(s) for tenant key provider operations.
  name: Qlik Sense tenant key provider operations API
  phrasing_intents:
  - id: getApiV1EncryptionKeyprovidersByArnFingerPrint
    intent: Get a key provider by fingerprint
    question: Can I look up one registered key using its ARN fingerprint?
  - id: patchApiV1EncryptionKeyprovidersByArnFingerPrint
    intent: Rename or redescribe a key provider
    question: Can I change the name or description of a registered key?
  - id: deleteApiV1EncryptionKeyprovidersByArnFingerPrint
    intent: Delete a key provider
    question: Can I remove a KMS key that is no longer in use?
  - id: postApiV1EncryptionKeyprovidersByArnFingerPrintActionsMigrate
    intent: Migrate tenant encryption to a key
    question: Can I move my tenant's encryption over to a newly registered key?
  - id: postApiV1EncryptionKeyprovidersByArnFingerPrintActionsTest
    intent: Test access to an AWS KMS key
    question: Does Qlik Cloud still have the access it needs to my KMS key?
  phrasing_ops: 5
  slug: qliksense-tenant-key-provider-operations-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The tenant-settings API from Qlik Sense — 4 operation(s) for tenant-settings.
  name: Qlik Sense Tenant Settings API
  phrasing_intents:
  - id: getTenantSettings
    intent: Get the tenant's settings
    question: What settings are currently saved for my Qlik Cloud tenant?
  - id: createTenantSettings
    intent: Create the tenant settings entry
    question: How do I set a preferred start page when the tenant has no settings yet?
  - id: updateTenantSettings
    intent: Update existing tenant settings
    question: Can I change the tenant's existing settings without recreating them?
  - id: deleteTenantSettings
    intent: Delete the tenant settings
    question: How do I remove all saved tenant settings?
  - id: toggleCrossRegionalDataProcessing
    intent: Turn cross-region data processing on or off
    question: Can I allow my tenant's data to be processed in another region?
  - id: toggleCrossRegionInference
    intent: Turn cross-region AI inference on or off
    question: How do I let my tenant run AI inference in another region?
  - id: getTenantSettingsStartPages
    intent: List available start pages
    question: Which start pages can I choose from for the tenant?
  phrasing_ops: 7
  slug: qliksense-tenant-settings-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The tenants API from Qlik Sense — 5 operation(s) for tenants.
  name: Qlik Sense Tenants API
  phrasing_intents:
  - id: createTenant
    intent: Create a Qlik Cloud tenant
    question: How do I create a new Qlik Cloud tenant from a license key?
  - id: getTenantById
    intent: Get a tenant
    question: How do I look up a tenant's details by ID?
  - id: updateTenantById
    intent: Update a tenant
    question: Can I change a tenant's properties after it is created?
  - id: deactivateTenantById
    intent: Deactivate a tenant
    question: What happens to a tenant after I deactivate it?
  - id: reactivateTenantById
    intent: Reactivate a tenant
    question: Can I bring back a tenant I deactivated before it is purged?
  - id: getApiV1TenantsMe
    intent: Get the tenant I am signed in to
    question: Which tenant am I currently signed in to?
  phrasing_ops: 6
  slug: qliksense-tenants-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The terms API from Qlik Sense — 4 operation(s) for terms.
  name: Qlik Sense Terms API
  phrasing_intents:
  - id: getApiV1GlossariesByIdTerms
    intent: List terms in a glossary
    question: Which business terms are defined in a glossary?
  - id: postApiV1GlossariesByIdTerms
    intent: Create a glossary term
    question: Can I add a new business term to a glossary?
  - id: getApiV1GlossariesByIdTermsByTermId
    intent: Get a glossary term
    question: What does a particular business term mean in our glossary?
  - id: patchApiV1GlossariesByIdTermsByTermId
    intent: Patch glossary term properties
    question: Can I change just one property of a term with JSON Patch?
  - id: putApiV1GlossariesByIdTermsByTermId
    intent: Replace a glossary term
    question: Can I rewrite a term's name, description and categories in one call?
  - id: deleteApiV1GlossariesByIdTermsByTermId
    intent: Delete a glossary term
    question: Can I remove an obsolete term from a glossary?
  - id: postApiV1GlossariesByIdTermsByTermIdActionsChangeStatus
    intent: Change a term's status
    question: Can I mark a glossary term as verified?
  - id: getApiV1GlossariesByIdTermsByTermIdRevisions
    intent: List revisions of a term
    question: Can I see how a glossary term has changed over time?
  phrasing_ops: 8
  slug: qliksense-terms-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The themes API from Qlik Sense — 4 operation(s) for themes.
  name: Qlik Sense Themes API
  phrasing_intents:
  - id: getThemes
    intent: List themes
    question: Which custom themes are imported into my tenant?
  - id: createTheme
    intent: Import a new theme
    question: How do I upload a custom theme to the tenant?
  - id: getThemeById
    intent: Get a theme
    question: How do I fetch a theme by its ID or name?
  - id: updateThemeById
    intent: Update a theme
    question: Can I replace an existing theme with a new file?
  - id: deleteThemeById
    intent: Delete a theme
    question: How do I remove a theme from the tenant?
  - id: getThemeArchive
    intent: Download a theme as a zip
    question: How do I download all of a theme's files as a zip archive?
  - id: getFileFromThemeArchive
    intent: Download one file from a theme
    question: Can I download a single file, like the CSS, from a theme?
  phrasing_ops: 7
  slug: qliksense-themes-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The threads API from Qlik Sense — 7 operation(s) for threads.
  name: Qlik Sense Threads API
  phrasing_intents:
  - id: getApiV1AssistantsByAssistantIdThreads
    intent: List conversation threads of an assistant
    question: Which conversation threads exist on an assistant?
  - id: postApiV1AssistantsByAssistantIdThreads
    intent: Start a new conversation thread
    question: Can I start a fresh conversation thread with an assistant?
  - id: getApiV1AssistantsByAssistantidThreadsByThreadid
    intent: Get a conversation thread
    question: Can I view the details of one conversation thread?
  - id: patchApiV1AssistantsByAssistantidThreadsByThreadid
    intent: Update a conversation thread
    question: Can I rename a conversation thread?
  - id: deleteApiV1AssistantsByAssistantidThreadsByThreadid
    intent: Delete a conversation thread
    question: Can I delete a whole conversation thread with an assistant?
  - id: getApiV1AssistantsByAssistantIdThreadsByThreadIdInteractions
    intent: List interactions in a thread
    question: Can I see every question and answer exchanged in a thread?
  - id: postApiV1AssistantsByAssistantIdThreadsByThreadIdInteractions
    intent: Record an interaction in a thread
    question: Can I save a question, answer and its sources as an interaction in a thread?
  - id: getApiV1AssistantsByAssistantIdThreadsByThreadIdInteractionsByInteractionId
    intent: Get one interaction
    question: Can I look up a single question and answer from a thread?
  phrasing_ops: 12
  slug: qliksense-threads-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The tokens API from Qlik Sense — 1 operation(s) for tokens.
  name: Qlik Sense Tokens API
  phrasing_intents:
  - id: postLoginJwtSession
    intent: Exchange a JWT for a session cookie
    question: Can I sign a user into Qlik Cloud with a JWT I issue?
  phrasing_ops: 1
  slug: qliksense-tokens-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The trust-score-result API from Qlik Sense — 1 operation(s) for trust-score-result.
  name: Qlik Sense Trust Score Result API
  phrasing_intents:
  - id: filterDatasetsTrustScore
    intent: Get Trust Scores for datasets in bulk
    question: How trustworthy are my datasets according to their Trust Score?
  phrasing_ops: 1
  slug: qliksense-trust-score-result-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The users API from Qlik Sense — 5 operation(s) for users.
  name: Qlik Sense Users API
  phrasing_intents:
  - id: getUsers
    intent: List users
    question: Who are the users in my Qlik tenant?
  - id: createUser
    intent: Invite a new user
    question: How do I invite someone to my tenant?
  - id: getUserById
    intent: Get a user
    question: Where can I see one user's profile and roles?
  - id: updateUserById
    intent: Update a user
    question: Can I change a user's roles or status?
  - id: deleteUserById
    intent: Delete a user
    question: How do I remove a user from my tenant?
  - id: countUsers
    intent: Count users in the tenant
    question: How many users does my tenant have?
  - id: users_api_actions_filter
    intent: Search users with an advanced filter
    question: Can I search users with a complex query instead of a simple filter?
  - id: getApiV1UsersMe
    intent: Get my own user profile
    question: Who am I signed in as right now?
  phrasing_ops: 8
  slug: qliksense-users-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The web-integrations API from Qlik Sense — 2 operation(s) for web-integrations.
  name: Qlik Sense Web Integrations API
  phrasing_intents:
  - id: getWebIntegrations
    intent: List web integrations
    question: Which web integrations are configured for embedding?
  - id: createWebIntegration
    intent: Create a web integration
    question: How do I allow my website origin to embed Qlik content?
  - id: getWebIntegrationById
    intent: Get a web integration
    question: Which origins does a particular web integration allow?
  - id: updateWebIntegrationById
    intent: Update a web integration
    question: Can I add a new origin to an existing web integration?
  - id: deleteWebIntegrationById
    intent: Delete a web integration
    question: How do I remove a web integration?
  phrasing_ops: 5
  slug: qliksense-web-integrations-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The web-notifications API from Qlik Sense — 3 operation(s) for web-notifications.
  name: Qlik Sense Web Notifications API
  phrasing_intents:
  - id: getNotifications
    intent: List my in-app notifications
    question: What unread notifications do I have in Qlik Cloud?
  - id: getNotification
    intent: Get a single notification
    question: What does one particular notification say?
  - id: updateNotification
    intent: Mark one notification read or unread
    question: Can I mark a single notification as read?
  - id: deleteNotification
    intent: Delete one notification
    question: How do I dismiss a single notification for good?
  - id: updateNotifications
    intent: Mark all notifications as read
    question: Can I mark every notification as read in one go?
  - id: deleteNotifications
    intent: Delete all my notifications
    question: How do I clear out every notification at once?
  phrasing_ops: 6
  slug: qliksense-web-notifications-api
- baseURL: https://{tenant}.{region}.qlikcloud.com
  baseurl_source: declared
  description: The webhooks API from Qlik Sense — 3 operation(s) for webhooks.
  name: Qlik Sense Webhooks API
  phrasing_intents:
  - id: listWebhookEntries
    intent: List webhooks
    question: Which webhooks are configured in my Qlik tenant?
  - id: createWebhook
    intent: Create a webhook
    question: How do I subscribe a URL to tenant events with a webhook?
  - id: getWebhook
    intent: Get a webhook
    question: Where can I see one webhook's settings and target URL?
  - id: patchWebhook
    intent: Change selected webhook properties
    question: Can I just toggle a webhook on or off without resending everything?
  - id: updateWebhook
    intent: Replace all of a webhook's properties
    question: Does a full webhook update clear the fields I leave out?
  - id: deleteWebhook
    intent: Delete a webhook
    question: Can I delete a webhook I no longer need?
  - id: listEventTypes
    intent: List subscribable webhook event types
    question: Which event types can a webhook subscribe to?
  phrasing_ops: 7
  slug: qliksense-webhooks-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The Dataset API from Qlik Sense — 2 operation(s) for dataset.
  name: Qlik Sense Dataset API
  phrasing_intents:
  - id: saveDataSet
    intent: Save a new data set
    question: How do I register a new data set in the catalog?
  - id: batchDeleteDataSets
    intent: Delete several data sets at once
    question: Can I delete multiple data sets in one request?
  - id: getDataSet
    intent: Get a data set
    question: Where can I see one data set's schema and properties?
  - id: patchDataSet
    intent: Patch a data set with JSON Patch
    question: Can I change just one field of a data set using JSON Patch operations?
  - id: updateDataSet
    intent: Fully replace a data set
    question: Can I replace every attribute of a data set, including its owner?
  phrasing_ops: 5
  slug: qliksense-dataset-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The Datastore API from Qlik Sense — 4 operation(s) for datastore.
  name: Qlik Sense Datastore API
  phrasing_intents:
  - id: getDataStores
    intent: List data stores
    question: Which data stores are registered in my tenant?
  - id: saveDataStore
    intent: Register a new data store
    question: How do I register a new data store?
  - id: batchDeleteDataStores
    intent: Delete empty data stores in bulk
    question: Can I delete several data stores at once?
  - id: getDataStore
    intent: Get a data store
    question: How do I look up a single data store by its ID?
  - id: patchDataStore
    intent: Partially update a data store
    question: Can I change just one field on a data store?
  - id: updateDataStore
    intent: Replace a data store's definition
    question: How do I fully overwrite a data store's definition?
  - id: getDataAssets
    intent: List data assets in data stores
    question: What data assets belong to a data store?
  - id: deleteDataAssetByDataStoreId
    intent: Delete all data assets in data stores
    question: How do I clear out every data asset in a data store?
  phrasing_ops: 10
  slug: qliksense-datastore-api
- baseURL: wss://your-tenant.qlikcloud.com/app/
  baseurl_source: declared
  description: The Knowledge Bases API from Qlik Sense — 11 operation(s) for knowledge bases.
  name: Qlik Sense Knowledge Bases API
  phrasing_intents:
  - id: getApiV1Knowledgebases
    intent: List knowledge bases
    question: Which knowledge bases do I have access to?
  - id: postApiV1Knowledgebases
    intent: Create a knowledge base
    question: Can I create a new knowledge base to feed an assistant?
  - id: getApiV1KnowledgebasesById
    intent: Get a knowledge base
    question: Can I view the details and datasources of one knowledge base?
  - id: patchApiV1KnowledgebasesById
    intent: Update a knowledge base
    question: Can I rename a knowledge base or change its description?
  - id: deleteApiV1KnowledgebasesById
    intent: Delete a knowledge base
    question: Can I delete a whole knowledge base?
  - id: postApiV1KnowledgebasesByIdDatasources
    intent: Add a datasource to a knowledge base
    question: Can I add a folder of documents as a source for a knowledge base?
  - id: putApiV1KnowledgebasesByIdDatasourcesByDatasourceId
    intent: Update a knowledge base datasource
    question: Can I change the chunking or file settings of an existing knowledge base source?
  - id: deleteApiV1KnowledgebasesByIdDatasourcesByDatasourceId
    intent: Remove a datasource from a knowledge base
    question: Can I remove one source from a knowledge base without deleting the whole thing?
  phrasing_ops: 17
  slug: qliksense-knowledge-bases-api
artifact_total: 209
asyncapis:
- description: ''
  name: Qliksense Asyncapi Index
  slug: qliksense-asyncapi-index
- description: ''
  name: Qliksense Webhooks
  slug: qliksense-webhooks
common:
- group: other
  href: https://artifacts.apis.io/qliksense/capabilities/qliksense-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/qliksense-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-analytics-apps-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-analytics-apps-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-analytics-change-stores-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-analytics-change-stores-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-analytics-discovery-agent-adaptive-cards-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-analytics-discovery-agent-adaptive-cards-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-analytics-odag-apps-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-analytics-odag-apps-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-analytics-odag-links-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-analytics-odag-links-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-analytics-odag-requests-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-analytics-odag-requests-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-analytics-odag-settings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-analytics-odag-settings-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-api-keys-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-api-keys-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-apps-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-apps-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-assistants-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-assistants-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-audits-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-audits-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-automation-connections-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-automation-connections-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-automation-connectors-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-automation-connectors-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-automations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-automations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-automl-deployments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-automl-deployments-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-automl-predictions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-automl-predictions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-banners-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-banners-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-brands-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-brands-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-collections-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-collections-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-conditions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-conditions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-consumption-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-consumption-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-core-auth-settings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-core-auth-settings-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-core-ip-policies-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-core-ip-policies-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-csp-origins-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-csp-origins-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-csrf-token-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-csrf-token-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-data-alerts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-alerts-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-data-assets-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-assets-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-data-connections-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-connections-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-data-credentials-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-credentials-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-data-files-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-files-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-data-governance-data-products-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-governance-data-products-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-data-governance-data-qualities-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-governance-data-qualities-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-data-governance-trust-scores-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-governance-trust-scores-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-data-qualities-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-qualities-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-data-sets-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-sets-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-data-sources-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-sources-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-data-stores-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-data-stores-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-di-projects-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-di-projects-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-direct-access-agents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-direct-access-agents-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-encryption-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-encryption-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-extensions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-extensions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-glossaries-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-glossaries-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-groups-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-groups-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-identity-providers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-identity-providers-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-items-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-items-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-knowledgebases-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-knowledgebases-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-licenses-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-licenses-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-lineage-graphs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-lineage-graphs-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-login-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-login-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-ml-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-ml-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-notes-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-notes-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-notifications-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-notifications-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-oauth-clients-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-oauth-clients-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-oauth-tokens-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-oauth-tokens-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-questions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-questions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-quotas-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-quotas-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-reload-tasks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-reload-tasks-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-reloads-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-reloads-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-report-templates-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-report-templates-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-reports-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-reports-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-roles-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-roles-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-scheduling-tasks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-scheduling-tasks-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-sharing-tasks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-sharing-tasks-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-spaces-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-spaces-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-tasks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-tasks-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-temp-contents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-temp-contents-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-tenant-settings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-tenant-settings-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-tenants-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-tenants-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-themes-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-themes-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-transports-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-transports-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-ui-config-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-ui-config-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-users-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-users-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-web-integrations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-web-integrations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-web-notifications-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-web-notifications-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-webhooks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-webhooks-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-workflows-automation-connections-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-workflows-automation-connections-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-workflows-automation-connectors-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-workflows-automation-connectors-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qliksense/overlays/qliksense-workflows-automations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qliksense-workflows-automations-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/qlik-oss/server-side-extension/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.qlik.com/us/products/qlik-sense
- group: start
  title: ''
  type: DeveloperPortal
  url: https://qlik.dev/
- group: start
  title: ''
  type: Portal
  url: https://qlik.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://qlik.dev/apis/
- group: docs
  title: ''
  type: APIReference
  url: https://qlik.dev/apis/rest/
- group: start
  title: ''
  type: GettingStarted
  url: https://qlik.dev/manage/get-started-first-api-call/
- group: auth
  title: ''
  type: Authentication
  url: https://qlik.dev/authenticate
- group: operate
  title: ''
  type: Support
  url: https://support.qlik.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.qlik.com/
- group: company
  title: ''
  type: Blog
  url: https://www.qlik.com/us/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qlik-oss
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qlik.com/us/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.qlik.com/us/trial/qlik-cloud-analytics
- group: start
  title: ''
  type: Login
  url: https://login.qlik.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qlik.com/us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qlik.com/us/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qlikcloud.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://qlik.dev/changelog/
- group: other
  title: ''
  type: RSS
  url: https://qlik.dev/rss.xml
- group: build
  title: ''
  type: CLI
  url: https://qlik.dev/toolkits/qlik-cli/
- group: build
  href: https://artifacts.apis.io/qliksense/packages/qliksense-packages.yml
  title: ''
  type: SDKs
  url: packages/qliksense-packages.yml
- group: build
  href: https://artifacts.apis.io/qliksense/packages/qliksense-packages.yml
  title: ''
  type: Packages
  url: packages/qliksense-packages.yml
- group: agent
  href: https://artifacts.apis.io/qliksense/mcp/qliksense-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/qliksense-mcp.yml
- group: build
  href: https://artifacts.apis.io/qliksense/mcp/qliksense-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/qliksense-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/qliksense/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/qliksense/llms/qliksense-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qliksense-llms.txt
- group: docs
  href: https://artifacts.apis.io/qliksense/asyncapi/qliksense-asyncapi-index.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/qliksense-asyncapi-index.yml
- group: design
  href: https://artifacts.apis.io/qliksense/asyncapi/qliksense-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/qliksense-webhooks.yml
- group: other
  href: https://artifacts.apis.io/qliksense/grpc/qliksense-server-side-extension.proto
  title: ''
  type: Protobuf
  url: grpc/qliksense-server-side-extension.proto
- group: other
  href: https://artifacts.apis.io/qliksense/json-rpc/qliksense-qix-openrpc.json
  title: ''
  type: OpenRPC
  url: json-rpc/qliksense-qix-openrpc.json
- group: docs
  href: https://artifacts.apis.io/qliksense/json-schema/qliksense-qtcp-project.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/qliksense-qtcp-project.schema.json
- group: design
  href: https://artifacts.apis.io/qliksense/conformance/qliksense-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qliksense-conformance.yml
- group: auth
  href: https://artifacts.apis.io/qliksense/security/qliksense-trust-center.yml
  title: ''
  type: Compliance
  url: security/qliksense-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/qliksense/security/qliksense-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/qliksense-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/qliksense/security/qliksense-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/qliksense-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/qliksense/security/qliksense-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/qliksense-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/qliksense/security/qliksense-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qliksense-domain-security.yml
- group: design
  href: https://artifacts.apis.io/qliksense/errors/qliksense-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/qliksense-problem-types.yml
- group: design
  href: https://artifacts.apis.io/qliksense/lifecycle/qliksense-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/qliksense-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/qliksense/lifecycle/qliksense-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/qliksense-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/qliksense/scopes/qliksense-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/qliksense-scopes.yml
- group: auth
  href: https://artifacts.apis.io/qliksense/authentication/qliksense-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qliksense-authentication.yml
- group: design
  href: https://artifacts.apis.io/qliksense/conventions/qliksense-conventions.yml
  title: ''
  type: Conventions
  url: conventions/qliksense-conventions.yml
- group: operate
  href: https://artifacts.apis.io/qliksense/changelog/qliksense-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/qliksense-changelog.yml
- group: build
  href: https://artifacts.apis.io/qliksense/cli/qliksense-cli.yml
  title: ''
  type: CLI
  url: cli/qliksense-cli.yml
- group: design
  href: https://artifacts.apis.io/qliksense/components/qliksense-components.yml
  title: ''
  type: Components
  url: components/qliksense-components.yml
- group: design
  href: https://artifacts.apis.io/qliksense/data-model/qliksense-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qliksense-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/qliksense/plans/qliksense-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qliksense-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/qliksense/rate-limits/qliksense-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/qliksense-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/qliksense/finops/qliksense-finops.yml
  title: ''
  type: FinOps
  url: finops/qliksense-finops.yml
created: '2024-01-15'
description: 'Qlik Sense and Qlik Cloud from Qlik Parent, Inc. — a business intelligence, data integration and AI analytics platform. Qlik publishes one of the broadest machine-readable API surfaces in the analytics market: 78 OpenAPI 3.0.0 documents covering 681 REST operations, 29 AsyncAPI 3.0.0 event documents carrying CloudEvents 1.0 payloads, an OpenRPC 1.0.0 document for the QIX Associative Engine WebSocket API, 39 JSON Schemas for Qlik Talend Cloud declarative pipelines, and a proto3 gRPC contract for the engine''s Server-Side Extension protocol. It also ships a generally-available remote MCP server at <tenant>/api/ai/mcp and maintains a public Agent Skills hub. Every API is tenant-scoped to https://{tenant}.{region}.qlikcloud.com and authenticated with an API key, an OAuth 2.0 token or a signed JWT.'
features:
- description: Qlik's unique Associative Engine enables dynamic data exploration without predefined queries or drill paths.
  name: Associative Engine
- description: Comprehensive REST API coverage for all Qlik Cloud resources including apps, data, users, and automation.
  name: 50+ REST APIs
- description: AutoML, natural language queries, and AI assistants for data-driven insights.
  name: AI-Powered Analytics
- description: Build automation workflows connecting Qlik with external applications without coding.
  name: No-Code Automation
- description: Event-driven architecture with webhooks for real-time notifications on platform events.
  name: Real-Time Webhooks
- description: Deploy Qlik Cloud across AWS, Azure, and GCP regions with global availability.
  name: Multi-Cloud Deployment
finops:
- has_sources: true
  method: derived
  name: Qliksense Finops
  primary_unit: 10 users, billed annually
  service_category: ''
  slug: qliksense-finops
  template: false
image: /assets/icons/qliksense.png
integrations:
- description: Direct connectivity for analytics on Snowflake cloud data warehouse.
  name: Snowflake
- description: Integration with Databricks lakehouse for large-scale analytics workloads.
  name: Databricks
- description: Enterprise data connectivity for SAP ERP, BW, and HANA data sources.
  name: SAP
- description: CRM data integration for sales analytics and pipeline management.
  name: Salesforce
- description: Collaboration integration for sharing analytics insights and alerts in Slack.
  name: Slack
- description: Embed analytics and receive notifications within Microsoft Teams.
  name: Microsoft Teams
json_schemas:
- name: New Task Defaults Configuration
  property_count: 14
  slug: qliksense-qtcp-newtaskdefaults.schema
- name: Common Task Settings Definitions
  property_count: 0
  slug: qliksense-qtcp-newtaskdefaults.settings.common.schema
- name: Defaults for new Datamart Task
  property_count: 8
  slug: qliksense-qtcp-newtaskdefaults.settings.datamart.schema
- name: Defaults for new File Based Knowledge Mart Task
  property_count: 7
  slug: qliksense-qtcp-newtaskdefaults.settings.filebasedknowledgemart.schema
- name: Defaults for new Knowledge Mart Task
  property_count: 9
  slug: qliksense-qtcp-newtaskdefaults.settings.knowledgemart.schema
- name: Defaults for new Lakehouse Storage Task
  property_count: 5
  slug: qliksense-qtcp-newtaskdefaults.settings.lakehousestorage.schema
- name: Defaults for new Lake Landing Task
  property_count: 3
  slug: qliksense-qtcp-newtaskdefaults.settings.lakelanding.schema
- name: Defaults for new Landing Task
  property_count: 5
  slug: qliksense-qtcp-newtaskdefaults.settings.landing.schema
- name: Defaults for new QVD Storage Task
  property_count: 2
  slug: qliksense-qtcp-newtaskdefaults.settings.qvdstorage.schema
- name: Defaults for new Registered Data Task
  property_count: 4
  slug: qliksense-qtcp-newtaskdefaults.settings.registereddata.schema
- name: Defaults for new Replicate Landing Task
  property_count: 3
  slug: qliksense-qtcp-newtaskdefaults.settings.replicatelanding.schema
- name: Defaults for new Storage Task
  property_count: 8
  slug: qliksense-qtcp-newtaskdefaults.settings.storage.schema
- name: Defaults for new Streaming Lake Landing Task
  property_count: 4
  slug: qliksense-qtcp-newtaskdefaults.settings.streaminglakelanding.schema
- name: Defaults for new Streaming Transform Task
  property_count: 5
  slug: qliksense-qtcp-newtaskdefaults.settings.streamingtransform.schema
- name: Defaults for new Transform Task
  property_count: 9
  slug: qliksense-qtcp-newtaskdefaults.settings.transform.schema
- name: Project Configuration
  property_count: 2
  slug: qliksense-qtcp-project.schema
- name: Task Dataset Configuration
  property_count: 4
  slug: qliksense-qtcp-task.dataset.schema
- name: Task Model Configuration
  property_count: 2
  slug: qliksense-qtcp-task.model.schema
- name: Task Schedule Configuration
  property_count: 2
  slug: qliksense-qtcp-task.schedule.schema
- name: Task Configuration
  property_count: 0
  slug: qliksense-qtcp-task.schema
- name: Common Task Settings Definitions
  property_count: 0
  slug: qliksense-qtcp-task.settings.common.schema
- name: Datamart Task Settings
  property_count: 7
  slug: qliksense-qtcp-task.settings.datamart.schema
- name: File Based Knowledge Mart Task Settings
  property_count: 14
  slug: qliksense-qtcp-task.settings.filebasedknowledgemart.schema
- name: Knowledge Mart Task Settings
  property_count: 15
  slug: qliksense-qtcp-task.settings.knowledgemart.schema
- name: Lakehouse Mirror Task Settings
  property_count: 6
  slug: qliksense-qtcp-task.settings.lakehousemirror.schema
- name: Lakehouse Storage Task Settings
  property_count: 6
  slug: qliksense-qtcp-task.settings.lakehousestorage.schema
- name: Lake Landing Task Configuration (Replication)
  property_count: 21
  slug: qliksense-qtcp-task.settings.lakelanding.schema
- name: Landing Task Settings
  property_count: 19
  slug: qliksense-qtcp-task.settings.landing.schema
- name: QVD Storage Task Settings
  property_count: 3
  slug: qliksense-qtcp-task.settings.qvdstorage.schema
- name: Registered Data Task Settings
  property_count: 9
  slug: qliksense-qtcp-task.settings.registereddata.schema
- name: Replicate Landing Task Settings
  property_count: 2
  slug: qliksense-qtcp-task.settings.replicatelanding.schema
- name: Replication Task Configuration (Replication)
  property_count: 17
  slug: qliksense-qtcp-task.settings.replication.schema
- name: Storage Task Settings
  property_count: 8
  slug: qliksense-qtcp-task.settings.storage.schema
- name: Streaming Lake Landing Task Settings
  property_count: 3
  slug: qliksense-qtcp-task.settings.streaminglakelanding.schema
- name: Streaming Transform Task Settings
  property_count: 5
  slug: qliksense-qtcp-task.settings.streamingtransform.schema
- name: Transform Task Settings
  property_count: 7
  slug: qliksense-qtcp-task.settings.transform.schema
- name: Task SourceSelection Configuration
  property_count: 6
  slug: qliksense-qtcp-task.sourceselection.schema
- name: Task transformation data flow Configuration
  property_count: 6
  slug: qliksense-qtcp-task.transformationdataflow.schema
- name: Task transformation Configuration
  property_count: 2
  slug: qliksense-qtcp-task.transformationrules.schema
layout: provider
mcp_servers:
- description: Qlik ships a first-party REMOTE MCP server as part of Qlik Cloud. It reached general availability on 2026-02-10 and is listed as an included capability from the Starter plan upward on https://www.qlik
  name: Qlik MCP Server
  slug: qlik-mcp-server
modified: '2026-09-15'
name: Qlik Sense
nav: Providers
network: true
overview: 'Qlik Sense publishes 135 API contracts indexed on the [APIs.io](https://apis.io/) network, including Qlik Cloud System Events, Qlik MCP Server, alerting actions API, and 132 more. Tagged areas include Agents, Analytics, Artificial Intelligence, Business Intelligence, and Cloud.


  The Qlik Sense catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 1 Spectral governance ruleset.


  Qlik Sense''s developer surface includes developer portal, documentation, API reference, getting-started guide, authentication, support, engineering blog, and 123 more developer resources.'
plans:
- name: Qliksense Plans Pricing
  plan_count: 4
  slug: qliksense-plans-pricing
- name: Qliksense Price Estimates
  plan_count: 0
  slug: qliksense-price-estimates
random_paper: 15
rate_limits:
- limit_count: 3
  name: Qliksense Rate Limits
  slug: qliksense-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Qlik Sense API Rules
  rule_count: 50
  severity_counts:
    error: 24
    hint: 0
    info: 9
    warn: 17
  slug: qliksense-rules
scopes:
- name: Qliksense Scopes
  scope_count: 225
  slug: qliksense-scopes
  summary_line: 225 scopes
score:
  band: exemplar
  composite: 74.2
  coverage:
    artifact_dirs: 32
    catalog_earned: 66.5
    catalog_earned_first_party: 24.0
    catalog_gap: 48.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 51.6
    developer_ergonomics: 78.6
    discoverability: 58.3
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 74.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 126
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/qliksense/qliksense-2026-06-20T192343.png
security:
- kind: authentication
  name: Qliksense Authentication
  slug: qliksense-authentication
  summary_line: 8 schemes
- kind: domain-security
  name: Qliksense Domain Security
  slug: qliksense-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Qliksense Vulnerability Disclosure
  slug: qliksense-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Qliksense Trust Center
  slug: qliksense-trust-center
  summary_line: qlik, qlik_cloud_government, talend_cloud
skill_count: 5
skills:
- name: qlik-ai-readiness-optimizer
  slug: qliksense-ai-readiness-optimizer
- name: qlik-load-script
  slug: qliksense-load-script
- name: qliksense-onboard-user-to-space
  slug: qliksense-onboard-user-to-space
- name: qliksense-reload-an-app
  slug: qliksense-reload-an-app
- name: qliksense-subscribe-to-events
  slug: qliksense-subscribe-to-events
slug: qliksense
tags:
- Agents
- Analytics
- Artificial Intelligence
- Business Intelligence
- Cloud
- Data Integration
- Data Visualization
- Embedded Analytics
- Enterprise
- Machine Learning
use_cases:
- description: Embed interactive Qlik visualizations and dashboards in custom web applications.
  name: Embedded Analytics
- description: Automate data integration and transformation workflows using APIs and automation connectors.
  name: Data Pipeline Automation
- description: Enable business users to create and share analytics apps through the platform APIs.
  name: Self-Service BI
- description: Generate predictive analytics and natural language insights using ML and NLP APIs.
  name: AI-Powered Insights
- description: Manage multiple Qlik Cloud tenants programmatically for SaaS and enterprise deployments.
  name: Multi-Tenant Management
website: https://www.qlik.com/us/products/qlik-sense
---
