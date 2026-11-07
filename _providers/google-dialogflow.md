---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 277
  human_in_the_loop: 1
  name: Google Dialogflow Agentic Access
  operation_count: 437
  slug: google-dialogflow-agentic-access
  summary_line: 437 operations · 277 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: Natural Language Processing
  name: Dialogflow
  slug: dialogflow
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The agent API from Google Dialogflow — 14 operation(s) for agent.
  name: Google Dialogflow Agent API
  phrasing_intents:
  - id: dialogflow_projects_locations_agent_restore
    intent: Restore a regional ES agent from a ZIP
    question: Can I replace my regional ES agent entirely with one from a ZIP backup?
  - id: dialogflow_projects_locations_agent_updateFulfillment
    intent: Update a regional agent's fulfillment
    question: How do I point my regional ES agent's fulfillment at a new webhook service?
  - id: dialogflow_projects_locations_agent_getFulfillment
    intent: Get a regional agent's fulfillment
    question: Which webhook fulfillment is configured for my ES agent in a particular region?
  - id: dialogflow_projects_locations_agent_getValidationResult
    intent: Get validation errors for a regional agent
    question: Are there validation errors in my regional ES agent after training?
  - id: dialogflow_projects_locations_agent_search
    intent: Search ES agents in a regional location
    question: Which ES agents can I access across sub-projects in one location?
  - id: dialogflow_projects_locations_agent_export
    intent: Export a regional ES agent to a ZIP
    question: How do I back up my regional ES agent as a ZIP file?
  - id: dialogflow_projects_locations_agent_train
    intent: Train a regional ES agent
    question: How do I retrain my regional ES agent after changing intents?
  - id: dialogflow_projects_locations_agent_import
    intent: Import into a regional ES agent from a ZIP
    question: Can I merge intents and entities from a ZIP into my regional ES agent?
  phrasing_ops: 16
  slug: google-dialogflow-agent-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The agents API from Google Dialogflow — 7 operation(s) for agents.
  name: Google Dialogflow Agents API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_patch
    intent: Update a CX agent's settings
    question: How do I change my CX agent's time zone or supported languages?
  - id: dialogflow_projects_locations_agents_get
    intent: Retrieve a CX agent
    question: What are the default language, time zone and start flow of my Dialogflow CX agent?
  - id: dialogflow_projects_locations_agents_delete
    intent: Delete a CX agent
    question: Can I permanently delete a conversational agent I no longer use?
  - id: dialogflow_projects_locations_agents_getGenerativeSettings
    intent: Get a CX agent's generative AI settings
    question: Which LLM model and safety settings is my conversational agent using for generative features?
  - id: dialogflow_projects_locations_agents_updateGenerativeSettings
    intent: Update a CX agent's generative AI settings
    question: How do I change the LLM model my conversational agent uses?
  - id: dialogflow_projects_locations_agents_export
    intent: Export a CX agent
    question: How can I back up a whole conversational agent to Cloud Storage?
  - id: dialogflow_projects_locations_agents_validate
    intent: Validate a CX agent
    question: Can I check my conversational agent for configuration problems before deploying?
  - id: dialogflow_projects_locations_agents_getValidationResult
    intent: Get the latest validation result of a CX agent
    question: What issues did the last validation of my conversational agent find?
  phrasing_ops: 11
  slug: google-dialogflow-agents-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The answerRecords API from Google Dialogflow — 4 operation(s) for answerrecords.
  name: Google Dialogflow Answer Records API
  phrasing_intents:
  - id: dialogflow_projects_locations_answerRecords_list
    intent: List Agent Assist answer records in a region
    question: Which Agent Assist suggestions were shown to my agents in a particular region?
  - id: dialogflow_projects_locations_answerRecords_patch
    intent: Record feedback on a regional answer record
    question: How do I tell Dialogflow whether a suggestion shown to an agent in a specific region was useful?
  - id: dialogflow_projects_answerRecords_list
    intent: List Agent Assist answer records for a project
    question: What answer records has Agent Assist logged at the project level?
  - id: dialogflow_projects_answerRecords_patch
    intent: Record feedback on a project answer record
    question: Can I attach agent feedback to a project-level answer record?
  phrasing_ops: 4
  slug: google-dialogflow-answerrecords-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The changelogs API from Google Dialogflow — 2 operation(s) for changelogs.
  name: Google Dialogflow Changelogs API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_changelogs_list
    intent: List change logs for a CX agent
    question: Who changed what on my CX agent recently?
  - id: dialogflow_projects_locations_agents_changelogs_get
    intent: Get a single change log entry
    question: Can I see the details of one specific change made to my agent?
  phrasing_ops: 2
  slug: google-dialogflow-changelogs-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The contexts API from Google Dialogflow — 8 operation(s) for contexts.
  name: Google Dialogflow Contexts API
  phrasing_intents:
  - id: dialogflow_projects_locations_agent_sessions_contexts_create
    intent: Add a context to a regional session
    question: How do I set a context on a live session of my regional agent?
  - id: dialogflow_projects_locations_agent_sessions_contexts_list
    intent: List active contexts in a regional session
    question: Which contexts are currently active in a session on my regional ES agent?
  - id: dialogflow_projects_locations_agent_sessions_contexts_patch
    intent: Update a context in a regional session
    question: Can I change the lifespan of a context that is already active in a regional session?
  - id: dialogflow_projects_locations_agent_sessions_contexts_delete
    intent: Remove a context from a regional session
    question: Can I clear a single context from a session on my regional agent?
  - id: dialogflow_projects_locations_agent_sessions_contexts_get
    intent: Get a context from a regional session
    question: What parameters does a specific context hold in my regional session?
  - id: dialogflow_projects_locations_agent_environments_users_sessions_contexts_create
    intent: Add a context to a regional environment session
    question: How do I inject a context into an end user's session in a regional deployed environment?
  - id: dialogflow_projects_locations_agent_environments_users_sessions_contexts_list
    intent: List contexts in a regional environment session
    question: Which contexts are active for one user's session in a regional environment?
  - id: dialogflow_projects_locations_agent_environments_users_sessions_contexts_patch
    intent: Update a context in a regional environment session
    question: Can I extend a context's lifespan for one user in a regional deployed environment?
  phrasing_ops: 20
  slug: google-dialogflow-contexts-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The continuousTestResults API from Google Dialogflow — 1 operation(s) for continuoustestresults.
  name: Google Dialogflow Continuous Test Results API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_environments_continuousTestResults_list
    intent: List continuous test results for an environment
    question: Have the scheduled continuous tests on my environment been passing?
  phrasing_ops: 1
  slug: google-dialogflow-continuoustestresults-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The conversationDatasets API from Google Dialogflow — 6 operation(s) for conversationdatasets.
  name: Google Dialogflow Conversation Datasets API
  phrasing_intents:
  - id: dialogflow_projects_locations_conversationDatasets_importConversationData
    intent: Import transcripts into a regional conversation dataset
    question: How do I load conversation transcripts from Cloud Storage into a dataset in a specific region?
  - id: dialogflow_projects_locations_conversationDatasets_list
    intent: List conversation datasets in a region
    question: Which conversation datasets for model training do I have in a particular region?
  - id: dialogflow_projects_locations_conversationDatasets_create
    intent: Create a conversation dataset in a region
    question: How do I create a conversation dataset to train Agent Assist models in a specific region?
  - id: dialogflow_projects_locations_conversationDatasets_get
    intent: Get a regional conversation dataset
    question: How many conversations does one of my regional conversation datasets hold?
  - id: dialogflow_projects_locations_conversationDatasets_delete
    intent: Delete a regional conversation dataset
    question: How do I delete a conversation dataset I no longer need in a specific region?
  - id: dialogflow_projects_conversationDatasets_get
    intent: Get a project conversation dataset
    question: How do I view one conversation dataset at the global location of my project?
  - id: dialogflow_projects_conversationDatasets_list
    intent: List conversation datasets in a project
    question: What conversation datasets exist in my project without picking a region?
  - id: dialogflow_projects_conversationDatasets_importConversationData
    intent: Import transcripts into a project conversation dataset
    question: How do I import conversation transcripts into a global conversation dataset?
  phrasing_ops: 8
  slug: google-dialogflow-conversationdatasets-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The conversationModels API from Google Dialogflow — 8 operation(s) for conversationmodels.
  name: Google Dialogflow Conversation Models API
  phrasing_intents:
  - id: dialogflow_projects_locations_conversationModels_deploy
    intent: Deploy a regional conversation model
    question: How do I put a trained Agent Assist conversation model in a specific region into service?
  - id: dialogflow_projects_locations_conversationModels_create
    intent: Train a conversation model in a region
    question: How do I train a smart reply or article suggestion model on my conversation datasets in a given region?
  - id: dialogflow_projects_locations_conversationModels_list
    intent: List conversation models in a region
    question: Which conversation models have I trained in a particular location?
  - id: dialogflow_projects_locations_conversationModels_get
    intent: Retrieve a regional conversation model
    question: Is my regional conversation model still training or already deployed?
  - id: dialogflow_projects_locations_conversationModels_delete
    intent: Delete a regional conversation model
    question: Can I delete an Agent Assist model I trained in a specific region?
  - id: dialogflow_projects_locations_conversationModels_undeploy
    intent: Undeploy a regional conversation model
    question: How do I take a regional conversation model out of service without deleting it?
  - id: dialogflow_projects_conversationModels_undeploy
    intent: Undeploy a global conversation model
    question: Can I pause a project-level conversation model that is currently deployed?
  - id: dialogflow_projects_conversationModels_get
    intent: Retrieve a global conversation model
    question: What state is my project-level conversation model in?
  phrasing_ops: 12
  slug: google-dialogflow-conversationmodels-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The conversationProfiles API from Google Dialogflow — 8 operation(s) for conversationprofiles.
  name: Google Dialogflow Conversation Profiles API
  phrasing_intents:
  - id: dialogflow_projects_locations_conversationProfiles_delete
    intent: Delete a regional conversation profile
    question: Is there a way to delete a regional conversation profile I no longer use?
  - id: dialogflow_projects_locations_conversationProfiles_get
    intent: Get a regional conversation profile
    question: What settings does one regional Agent Assist conversation profile have?
  - id: dialogflow_projects_locations_conversationProfiles_patch
    intent: Update a regional conversation profile
    question: Can I change the language or time zone of an existing regional conversation profile?
  - id: dialogflow_projects_locations_conversationProfiles_create
    intent: Create a conversation profile in a region
    question: How do I create a conversation profile that ties a virtual agent and Agent Assist together in a specific region?
  - id: dialogflow_projects_locations_conversationProfiles_list
    intent: List conversation profiles in a region
    question: Which conversation profiles have I set up in a particular region?
  - id: dialogflow_projects_locations_conversationProfiles_setSuggestionFeatureConfig
    intent: Turn on a suggestion feature for a regional profile
    question: Which call turns on an Agent Assist suggestion feature like smart reply for a regional conversation profile?
  - id: dialogflow_projects_locations_conversationProfiles_clearSuggestionFeatureConfig
    intent: Turn off a suggestion feature on a regional profile
    question: Is it possible to switch off one Agent Assist suggestion type on a regional conversation profile?
  - id: dialogflow_projects_conversationProfiles_create
    intent: Create a conversation profile in a project
    question: How do I create a global conversation profile for Agent Assist in my project?
  phrasing_ops: 14
  slug: google-dialogflow-conversationprofiles-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The conversations API from Google Dialogflow — 7 operation(s) for conversations.
  name: Google Dialogflow Conversations API
  phrasing_intents:
  - id: dialogflow_projects_locations_conversations_get
    intent: Get a regional conversation
    question: Can I look up the state of one Agent Assist conversation stored in a specific region?
  - id: dialogflow_projects_locations_conversations_complete
    intent: Complete a regional conversation
    question: How do I end an Agent Assist conversation in a specific location?
  - id: dialogflow_projects_locations_conversations_create
    intent: Start a conversation in a region
    question: How do I start a new Agent Assist conversation in a particular location?
  - id: dialogflow_projects_locations_conversations_list
    intent: List conversations in a region
    question: Which conversations exist in one region of my project?
  - id: dialogflow_projects_locations_conversations_ingestContextReferences
    intent: Add context references to a conversation
    question: Can I attach extra context documents to a conversation for generators to use?
  - id: dialogflow_projects_conversations_complete
    intent: Complete a conversation
    question: Can I mark a conversation on the global endpoint as finished?
  - id: dialogflow_projects_conversations_list
    intent: List conversations in a project
    question: Which conversations does my project have at the global location?
  - id: dialogflow_projects_conversations_create
    intent: Start a conversation in a project
    question: How can I open a new conversation on the global endpoint?
  phrasing_ops: 9
  slug: google-dialogflow-conversations-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The deployments API from Google Dialogflow — 2 operation(s) for deployments.
  name: Google Dialogflow Deployments API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_environments_deployments_list
    intent: List deployments to an environment
    question: What has been deployed to one of my agent's environments over time?
  - id: dialogflow_projects_locations_agents_environments_deployments_get
    intent: Get a deployment
    question: Did a specific deployment to my environment succeed?
  phrasing_ops: 2
  slug: google-dialogflow-deployments-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The documents API from Google Dialogflow — 13 operation(s) for documents.
  name: Google Dialogflow Documents API
  phrasing_intents:
  - id: dialogflow_projects_knowledgeBases_documents_delete
    intent: Delete a document from a knowledge base
    question: Can I remove an outdated FAQ document from a project-level knowledge base?
  - id: dialogflow_projects_knowledgeBases_documents_get
    intent: Retrieve a document from a knowledge base
    question: How can I see the details of one document in a project-level Dialogflow knowledge base?
  - id: dialogflow_projects_knowledgeBases_documents_patch
    intent: Update a knowledge base document
    question: How do I rename a document in a project-level knowledge base?
  - id: dialogflow_projects_knowledgeBases_documents_reload
    intent: Reload a knowledge document from its source
    question: Can I make Dialogflow re-fetch a knowledge document after its source file changed?
  - id: dialogflow_projects_knowledgeBases_documents_list
    intent: List documents in a knowledge base
    question: What documents are loaded into my project-level knowledge base?
  - id: dialogflow_projects_knowledgeBases_documents_create
    intent: Add a document to a knowledge base
    question: How do I add an FAQ page or article to a project-level knowledge base?
  - id: dialogflow_projects_knowledgeBases_documents_export
    intent: Export a knowledge document to Cloud Storage
    question: Can I export a project-level knowledge document to a Cloud Storage bucket?
  - id: dialogflow_projects_knowledgeBases_documents_import
    intent: Bulk-import documents into a knowledge base
    question: How can I bulk-import many files from Cloud Storage into a project-level knowledge base?
  phrasing_ops: 22
  slug: google-dialogflow-documents-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The encryptionSpec API from Google Dialogflow — 1 operation(s) for encryptionspec.
  name: Google Dialogflow Encryption Spec API
  phrasing_intents:
  - id: dialogflow_projects_locations_encryptionSpec_initialize
    intent: Set up customer-managed encryption for a region
    question: Can I turn on customer-managed encryption keys for Dialogflow data in a region?
  phrasing_ops: 1
  slug: google-dialogflow-encryptionspec-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The entities API from Google Dialogflow — 6 operation(s) for entities.
  name: Google Dialogflow Entities API
  phrasing_intents:
  - id: dialogflow_projects_locations_agent_entityTypes_entities_batchDelete
    intent: Delete entity values in a regional entity type
    question: Can I remove several values from an entity type on my regional ES agent at once?
  - id: dialogflow_projects_locations_agent_entityTypes_entities_batchUpdate
    intent: Update entities in a regional entity type
    question: How do I update synonyms on many entities of a regional entity type in one call?
  - id: dialogflow_projects_locations_agent_entityTypes_entities_batchCreate
    intent: Add entities to a regional entity type
    question: Can I add a batch of new values to an entity type on my regional agent?
  - id: dialogflow_projects_agent_entityTypes_entities_batchDelete
    intent: Delete entity values in an entity type
    question: Can I delete many values from an entity type on my global ES agent?
  - id: dialogflow_projects_agent_entityTypes_entities_batchUpdate
    intent: Update entities in an entity type
    question: How do I bulk-edit entities on an entity type of my global ES agent?
  - id: dialogflow_projects_agent_entityTypes_entities_batchCreate
    intent: Add entities to an entity type
    question: Can I add many new values to an entity type on my global ES agent in one call?
  phrasing_ops: 6
  slug: google-dialogflow-entities-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The environments API from Google Dialogflow — 11 operation(s) for environments.
  name: Google Dialogflow Environments API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_environments_create
    intent: Create an environment for a CX agent
    question: How do I set up a new staging environment for my CX agent?
  - id: dialogflow_projects_locations_agents_environments_list
    intent: List environments of a CX agent
    question: What environments, like staging and production, does my Dialogflow CX agent have?
  - id: dialogflow_projects_locations_agents_environments_runContinuousTest
    intent: Run continuous tests on a CX environment
    question: Can I kick off the continuous test suite against a CX environment on demand?
  - id: dialogflow_projects_locations_agents_environments_lookupEnvironmentHistory
    intent: Look up the history of a CX environment
    question: How has a CX environment changed over time, version by version?
  - id: dialogflow_projects_locations_agents_environments_deployFlow
    intent: Deploy a flow version to a CX environment
    question: How do I promote a specific flow version into my CX production environment?
  - id: dialogflow_projects_locations_agents_environments_patch
    intent: Update a CX environment
    question: Can I change the description or test-case settings of an existing CX environment?
  - id: dialogflow_projects_locations_agents_environments_delete
    intent: Delete a CX environment
    question: Can I tear down a CX environment I no longer deploy to?
  - id: dialogflow_projects_locations_agents_environments_get
    intent: Retrieve a CX environment
    question: Which flow versions and webhook settings is a CX environment currently using?
  phrasing_ops: 20
  slug: google-dialogflow-environments-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The evaluations API from Google Dialogflow — 6 operation(s) for evaluations.
  name: Google Dialogflow Evaluations API
  phrasing_intents:
  - id: dialogflow_projects_locations_conversationModels_evaluations_list
    intent: List evaluations of a regional conversation model
    question: What evaluations have been run against my regional Agent Assist conversation model?
  - id: dialogflow_projects_locations_conversationModels_evaluations_create
    intent: Evaluate a regional conversation model
    question: How do I measure how well my regional smart reply model performs on held-out data?
  - id: dialogflow_projects_locations_conversationModels_evaluations_get
    intent: Retrieve a regional conversation model evaluation
    question: What scores did a specific evaluation of my regional conversation model produce?
  - id: dialogflow_projects_locations_generators_evaluations_get
    intent: Retrieve a generator evaluation
    question: What summarization metrics did an evaluation of my generator report?
  - id: dialogflow_projects_locations_generators_evaluations_delete
    intent: Delete a generator evaluation
    question: Can I delete an old evaluation run for one of my generators?
  - id: dialogflow_projects_locations_generators_evaluations_list
    intent: List evaluations of a generator
    question: Which evaluations have I run on a summarization generator?
  - id: dialogflow_projects_locations_generators_evaluations_create
    intent: Evaluate a generator
    question: How do I test the quality of a summarization generator before rolling it out?
  - id: dialogflow_projects_conversationModels_evaluations_list
    intent: List evaluations of a global conversation model
    question: Which evaluations exist for a project-level conversation model?
  phrasing_ops: 9
  slug: google-dialogflow-evaluations-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The examples API from Google Dialogflow — 2 operation(s) for examples.
  name: Google Dialogflow Examples API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_playbooks_examples_get
    intent: Retrieve a playbook example
    question: What conversation does one example in my Dialogflow playbook demonstrate?
  - id: dialogflow_projects_locations_agents_playbooks_examples_patch
    intent: Update a playbook example
    question: How do I fix the actions in an existing playbook example?
  - id: dialogflow_projects_locations_agents_playbooks_examples_delete
    intent: Delete a playbook example
    question: Can I remove a bad few-shot example from a playbook?
  - id: dialogflow_projects_locations_agents_playbooks_examples_list
    intent: List examples of a playbook
    question: Which examples have I given a playbook to learn from?
  - id: dialogflow_projects_locations_agents_playbooks_examples_create
    intent: Add an example to a playbook
    question: How do I teach a playbook with a sample conversation?
  phrasing_ops: 5
  slug: google-dialogflow-examples-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The experiments API from Google Dialogflow — 4 operation(s) for experiments.
  name: Google Dialogflow Experiments API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_environments_experiments_delete
    intent: Delete an experiment
    question: Can I delete an experiment I set up in an environment?
  - id: dialogflow_projects_locations_agents_environments_experiments_patch
    intent: Update an experiment
    question: How do I change the variants or rollout config of an existing experiment?
  - id: dialogflow_projects_locations_agents_environments_experiments_get
    intent: Get an experiment
    question: Can I see the results and state of one A/B experiment in an environment?
  - id: dialogflow_projects_locations_agents_environments_experiments_start
    intent: Start an experiment
    question: How do I begin sending traffic to an experiment's variants?
  - id: dialogflow_projects_locations_agents_environments_experiments_list
    intent: List experiments in an environment
    question: Which experiments are set up in one of my agent's environments?
  - id: dialogflow_projects_locations_agents_environments_experiments_create
    intent: Create an experiment in an environment
    question: How do I set up an A/B test between flow versions in an environment?
  - id: dialogflow_projects_locations_agents_environments_experiments_stop
    intent: Stop a running experiment
    question: Can I stop an experiment that is currently running?
  phrasing_ops: 7
  slug: google-dialogflow-experiments-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The flows API from Google Dialogflow — 7 operation(s) for flows.
  name: Google Dialogflow Flows API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_flows_list
    intent: List flows on a CX agent
    question: What flows make up my Dialogflow CX agent?
  - id: dialogflow_projects_locations_agents_flows_create
    intent: Create a flow on a CX agent
    question: How do I add a new conversation flow to my CX agent?
  - id: dialogflow_projects_locations_agents_flows_delete
    intent: Delete a flow
    question: Can I delete a flow that other pages still transition to?
  - id: dialogflow_projects_locations_agents_flows_get
    intent: Get a flow
    question: Can I see the transition routes and event handlers of one flow?
  - id: dialogflow_projects_locations_agents_flows_patch
    intent: Update a flow
    question: How do I rename a flow or change its routes?
  - id: dialogflow_projects_locations_agents_flows_import
    intent: Import a flow into a CX agent
    question: Can I import a flow from a file in Cloud Storage into my agent?
  - id: dialogflow_projects_locations_agents_flows_getValidationResult
    intent: Get a flow's latest validation result
    question: Which validation issues were found the last time my flow was validated?
  - id: dialogflow_projects_locations_agents_flows_validate
    intent: Validate a flow
    question: How do I check a flow for errors before I train or deploy it?
  phrasing_ops: 10
  slug: google-dialogflow-flows-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The generators API from Google Dialogflow — 5 operation(s) for generators.
  name: Google Dialogflow Generators API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_generators_create
    intent: Create a generator on a CX agent
    question: How do I add an LLM prompt generator to a CX agent?
  - id: dialogflow_projects_locations_agents_generators_list
    intent: List generators on a CX agent
    question: Which LLM generators are defined on my Dialogflow CX agent?
  - id: dialogflow_projects_locations_agents_generators_get
    intent: Get a CX agent generator
    question: Where can I read the prompt behind one of my CX agent's generators?
  - id: dialogflow_projects_locations_agents_generators_patch
    intent: Update a CX agent generator
    question: How do I change the prompt text of an existing CX generator?
  - id: dialogflow_projects_locations_agents_generators_delete
    intent: Delete a CX agent generator
    question: Can I delete a CX generator that pages still reference?
  - id: dialogflow_projects_locations_generators_create
    intent: Create an agent-assist generator in a region
    question: How do I create a summarization generator for Agent Assist in a specific location?
  - id: dialogflow_projects_locations_generators_list
    intent: List agent-assist generators in a region
    question: Which Agent Assist generators exist in a given region of my project?
  - id: dialogflow_projects_locations_generators_patch
    intent: Update an agent-assist generator in a region
    question: How do I change the trigger event on a regional Agent Assist generator?
  phrasing_ops: 12
  slug: google-dialogflow-generators-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The intents API from Google Dialogflow — 14 operation(s) for intents.
  name: Google Dialogflow Intents API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_intents_export
    intent: Export intents from a CX agent
    question: How can I export all the intents from my Dialogflow CX agent to a file?
  - id: dialogflow_projects_locations_agents_intents_patch
    intent: Update an intent on a CX agent
    question: How do I add more training phrases to an existing CX intent?
  - id: dialogflow_projects_locations_agents_intents_get
    intent: Retrieve one intent from a CX agent
    question: What training phrases and parameters does a particular CX agent intent have?
  - id: dialogflow_projects_locations_agents_intents_delete
    intent: Delete an intent from a CX agent
    question: Can I delete a single intent from my Dialogflow CX agent by its ID?
  - id: dialogflow_projects_locations_agents_intents_create
    intent: Create an intent on a CX agent
    question: How do I add a brand-new intent with training phrases to a CX agent?
  - id: dialogflow_projects_locations_agents_intents_list
    intent: List the intents of a CX agent
    question: Which intents does my CX agent currently have?
  - id: dialogflow_projects_locations_agents_intents_import
    intent: Import intents into a CX agent
    question: Can I bulk-load intents into a CX agent from a file in Cloud Storage?
  - id: dialogflow_projects_locations_agent_intents_delete
    intent: Delete an intent from a regional ES agent
    question: Can I delete one intent from an ES agent that lives in a non-global region?
  phrasing_ops: 23
  slug: google-dialogflow-intents-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The locations API from Google Dialogflow — 6 operation(s) for locations.
  name: Google Dialogflow Locations API
  phrasing_intents:
  - id: dialogflow_projects_locations_list
    intent: List regions available to Dialogflow CX
    question: Which regions can I host a Dialogflow CX agent in for my project?
  - id: dialogflow_projects_locations_get
    intent: Get a Dialogflow CX location
    question: What details can I get about one Dialogflow CX region like us-central1?
  - id: getV2ProjectsByProjectsIdLocationsByLocationsId
    intent: Get a Dialogflow ES location
    question: Can I look up one Dialogflow ES region for my project?
  - id: dialogflow_projects_locations_getAgent
    intent: Get the ES agent in a region
    question: How do I fetch the Dialogflow ES agent that lives in a specific region of my project?
  - id: dialogflow_projects_locations_setAgent
    intent: Create or update the ES agent in a region
    question: How do I create or update a Dialogflow ES agent in a specific region?
  - id: dialogflow_projects_locations_deleteAgent
    intent: Delete the ES agent in a region
    question: Can I delete the Dialogflow ES agent in one region of my project?
  - id: dialogflow_projects_locations_getEncryptionSpec
    intent: Get the encryption settings for a region
    question: Which customer-managed encryption key does Dialogflow use in a given region?
  - id: getV2ProjectsByProjectsIdLocations
    intent: List regions available to Dialogflow ES
    question: Which regions does Dialogflow ES support for my project?
  phrasing_ops: 8
  slug: google-dialogflow-locations-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The messages API from Google Dialogflow — 2 operation(s) for messages.
  name: Google Dialogflow Messages API
  phrasing_intents:
  - id: dialogflow_projects_locations_conversations_messages_list
    intent: List messages in a regional conversation
    question: How do I read the message transcript of a conversation hosted in a specific region?
  - id: dialogflow_projects_conversations_messages_list
    intent: List messages in a conversation
    question: Where can I pull the full transcript of a global Dialogflow conversation?
  phrasing_ops: 2
  slug: google-dialogflow-messages-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The operations API from Google Dialogflow — 12 operation(s) for operations.
  name: Google Dialogflow Operations API
  phrasing_intents:
  - id: dialogflow_projects_operations_get
    intent: Check a CX long-running operation
    question: How do I check whether a Dialogflow CX export or training job has finished?
  - id: dialogflow_projects_operations_cancel
    intent: Cancel a CX long-running operation
    question: How do I stop a Dialogflow CX import or export that is still running?
  - id: dialogflow_projects_operations_list
    intent: List CX long-running operations in a project
    question: Which Dialogflow CX background jobs are running or recently finished in my project?
  - id: dialogflow_projects_locations_operations_get
    intent: Check a regional CX long-running operation
    question: How do I check progress of a Dialogflow CX operation running in a specific region?
  - id: dialogflow_projects_locations_operations_cancel
    intent: Cancel a regional CX long-running operation
    question: How do I cancel a Dialogflow CX operation that is running in a particular region?
  - id: dialogflow_projects_locations_operations_list
    intent: List regional CX long-running operations
    question: What Dialogflow CX operations are in progress in a given region of my project?
  - id: postV2ProjectsByProjectsIdLocationsByLocationsIdOperations{operationsId}:cancel
    intent: Cancel a regional ES long-running operation
    question: How do I cancel a Dialogflow ES training or import job running in a specific region?
  - id: getV2ProjectsByProjectsIdLocationsByLocationsIdOperationsByOperationsId
    intent: Check a regional ES long-running operation
    question: How do I check whether a regional Dialogflow ES agent training job has finished?
  phrasing_ops: 12
  slug: google-dialogflow-operations-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The pages API from Google Dialogflow — 2 operation(s) for pages.
  name: Google Dialogflow Pages API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_flows_pages_get
    intent: Get a page in a CX flow
    question: What form, routes and entry fulfillment does a page in my Dialogflow CX flow have?
  - id: dialogflow_projects_locations_agents_flows_pages_delete
    intent: Delete a page from a CX flow
    question: Can I delete a page from a Dialogflow CX flow?
  - id: dialogflow_projects_locations_agents_flows_pages_patch
    intent: Update a page in a CX flow
    question: How do I change the form parameters or routes on an existing Dialogflow CX page?
  - id: dialogflow_projects_locations_agents_flows_pages_create
    intent: Create a page in a CX flow
    question: How do I add a new page to a Dialogflow CX flow?
  - id: dialogflow_projects_locations_agents_flows_pages_list
    intent: List pages in a CX flow
    question: What pages make up a given flow in my Dialogflow CX agent?
  phrasing_ops: 5
  slug: google-dialogflow-pages-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The participants API from Google Dialogflow — 6 operation(s) for participants.
  name: Google Dialogflow Participants API
  phrasing_intents:
  - id: dialogflow_projects_locations_conversations_participants_list
    intent: List participants in a regional conversation
    question: Who are the participants, like end user and human agent, in a conversation hosted in a specific region?
  - id: dialogflow_projects_locations_conversations_participants_create
    intent: Add a participant to a regional conversation
    question: How do I add a human agent or end user to a conversation in a specific region?
  - id: dialogflow_projects_locations_conversations_participants_patch
    intent: Update a participant in a regional conversation
    question: Can I change a participant's settings in a conversation hosted in a specific region?
  - id: dialogflow_projects_locations_conversations_participants_get
    intent: Get a participant in a regional conversation
    question: What role and details does one participant have in a regional conversation?
  - id: dialogflow_projects_locations_conversations_participants_analyzeContent
    intent: Analyze a participant message in a regional conversation
    question: How do I send what a participant said in a regional conversation to get virtual agent replies and suggestions?
  - id: dialogflow_projects_conversations_participants_create
    intent: Add a participant to a conversation
    question: How do I add an end user or human agent to a global Dialogflow conversation?
  - id: dialogflow_projects_conversations_participants_list
    intent: List participants in a conversation
    question: Who is taking part in a Dialogflow conversation at the global location?
  - id: dialogflow_projects_conversations_participants_get
    intent: Get a participant in a conversation
    question: Which call fetches one participant from a global Dialogflow conversation?
  phrasing_ops: 10
  slug: google-dialogflow-participants-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The playbooks API from Google Dialogflow — 4 operation(s) for playbooks.
  name: Google Dialogflow Playbooks API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_playbooks_list
    intent: List playbooks on a CX agent
    question: Which playbooks does my Dialogflow CX agent have?
  - id: dialogflow_projects_locations_agents_playbooks_create
    intent: Create a playbook on a CX agent
    question: How do I create a generative playbook with a goal and step-by-step instructions?
  - id: dialogflow_projects_locations_agents_playbooks_delete
    intent: Delete a playbook
    question: Can I remove a playbook from my CX agent?
  - id: dialogflow_projects_locations_agents_playbooks_patch
    intent: Update a playbook
    question: How do I rewrite the instructions of an existing playbook?
  - id: dialogflow_projects_locations_agents_playbooks_get
    intent: Retrieve a playbook
    question: What goal and instructions does one of my agent's playbooks contain?
  - id: dialogflow_projects_locations_agents_playbooks_import
    intent: Import a playbook into a CX agent
    question: Can I import a playbook I exported from another agent?
  - id: dialogflow_projects_locations_agents_playbooks_export
    intent: Export a playbook
    question: How do I export a single playbook to a file in Cloud Storage?
  phrasing_ops: 7
  slug: google-dialogflow-playbooks-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The projects API from Google Dialogflow — 1 operation(s) for projects.
  name: Google Dialogflow Projects API
  phrasing_intents:
  - id: dialogflow_projects_deleteAgent
    intent: Delete a project's ES agent
    question: Can I delete the Dialogflow ES agent from my project?
  - id: dialogflow_projects_setAgent
    intent: Create or update a project's ES agent
    question: How do I create or change the Dialogflow ES agent for my project?
  - id: dialogflow_projects_getAgent
    intent: Get a project's ES agent
    question: Which Dialogflow ES agent is attached to my Google Cloud project?
  phrasing_ops: 3
  slug: google-dialogflow-projects-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The results API from Google Dialogflow — 2 operation(s) for results.
  name: Google Dialogflow Results API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_testCases_results_get
    intent: Retrieve one test case run result
    question: Did a specific run of my Dialogflow CX test case pass or fail?
  - id: dialogflow_projects_locations_agents_testCases_results_list
    intent: List run results of a test case
    question: What is the pass/fail history of one of my CX agent's test cases?
  phrasing_ops: 2
  slug: google-dialogflow-results-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The sessions API from Google Dialogflow — 17 operation(s) for sessions.
  name: Google Dialogflow Sessions API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_sessions_detectIntent
    intent: Send a user turn to a CX agent session
    question: How do I send what a user typed to my Dialogflow CX agent and get the bot's reply back?
  - id: dialogflow_projects_locations_agents_sessions_serverStreamingDetectIntent
    intent: Stream a CX agent's reply to a user turn
    question: Can I get a Dialogflow CX agent's response streamed back in pieces instead of one final reply?
  - id: dialogflow_projects_locations_agents_sessions_matchIntent
    intent: Preview which intent a CX agent would match
    question: Which intent would my Dialogflow CX agent match for an utterance, without running fulfillment?
  - id: dialogflow_projects_locations_agents_sessions_fulfillIntent
    intent: Fulfill a chosen intent match in a CX session
    question: After matching intents in a CX session, how do I run fulfillment for the match I picked?
  - id: dialogflow_projects_locations_agents_sessions_submitAnswerFeedback
    intent: Rate an answer a CX agent gave
    question: Can I record whether a user found a Dialogflow CX agent's answer helpful?
  - id: dialogflow_projects_locations_agents_environments_sessions_serverStreamingDetectIntent
    intent: Stream a reply from a CX environment session
    question: Can I stream partial responses from a CX agent deployed to my production environment?
  - id: dialogflow_projects_locations_agents_environments_sessions_detectIntent
    intent: Send a user turn to a CX environment session
    question: How do I talk to the version of my CX agent deployed in a specific environment like production?
  - id: dialogflow_projects_locations_agents_environments_sessions_fulfillIntent
    intent: Fulfill an intent match in a CX environment session
    question: Can I run fulfillment for a matched intent in a session on a deployed CX environment?
  phrasing_ops: 17
  slug: google-dialogflow-sessions-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The statelessSuggestion API from Google Dialogflow — 1 operation(s) for statelesssuggestion.
  name: Google Dialogflow Stateless Suggestion API
  phrasing_intents:
  - id: dialogflow_projects_locations_statelessSuggestion_generate
    intent: Generate a suggestion without a stored conversation
    question: Can I run a generator on conversation context I pass in, without creating a conversation?
  phrasing_ops: 1
  slug: google-dialogflow-statelesssuggestion-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The suggestions API from Google Dialogflow — 18 operation(s) for suggestions.
  name: Google Dialogflow Suggestions API
  phrasing_intents:
  - id: dialogflow_projects_locations_suggestions_searchKnowledge
    intent: Search the knowledge base for a regional profile
    question: Can I query my agent-assist knowledge sources directly in a specific region without a conversation?
  - id: dialogflow_projects_locations_suggestions_generateStatelessSummary
    intent: Summarize a transcript in a region without storing it
    question: Can I get a summary of a conversation transcript I send inline, without creating a regional conversation?
  - id: dialogflow_projects_locations_conversations_participants_suggestions_suggestFaqAnswers
    intent: Suggest FAQ answers for a regional participant
    question: Can the assistant propose FAQ answers to an agent during a live conversation in a region?
  - id: dialogflow_projects_locations_conversations_participants_suggestions_suggestKnowledgeAssist
    intent: Get Knowledge Assist for a regional participant
    question: Can Knowledge Assist suggest a query and answer for a participant in a regional conversation?
  - id: dialogflow_projects_locations_conversations_participants_suggestions_suggestSmartReplies
    intent: Suggest smart replies for a regional participant
    question: Can I get smart reply suggestions while an agent is typing in a regional conversation?
  - id: dialogflow_projects_locations_conversations_participants_suggestions_suggestArticles
    intent: Suggest articles for a regional participant
    question: Can I surface knowledge articles to a human agent during a regional conversation?
  - id: dialogflow_projects_locations_conversations_suggestions_suggestConversationSummary
    intent: Summarize a regional conversation
    question: Can I get an AI summary of an ongoing conversation stored in a specific region?
  - id: dialogflow_projects_locations_conversations_suggestions_searchKnowledge
    intent: Search knowledge within a regional conversation
    question: Can a human agent search the knowledge base from inside a regional conversation?
  phrasing_ops: 18
  slug: google-dialogflow-suggestions-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The tools API from Google Dialogflow — 4 operation(s) for tools.
  name: Google Dialogflow Tools API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_tools_get
    intent: Retrieve a tool on a CX agent
    question: What OpenAPI spec or function definition backs a tool on my Dialogflow CX agent?
  - id: dialogflow_projects_locations_agents_tools_patch
    intent: Update a tool on a CX agent
    question: How do I swap the OpenAPI spec behind an existing CX agent tool?
  - id: dialogflow_projects_locations_agents_tools_delete
    intent: Delete a tool from a CX agent
    question: Can I delete a tool from my CX agent even if playbooks still reference it?
  - id: dialogflow_projects_locations_agents_tools_create
    intent: Add a tool to a CX agent
    question: How do I give my CX agent a tool that calls my own REST API?
  - id: dialogflow_projects_locations_agents_tools_list
    intent: List tools on a CX agent
    question: Which tools can my CX agent's playbooks call?
  - id: dialogflow_projects_locations_tools_create
    intent: Create an ES tool in a location
    question: How do I register a connector or extension tool at the project location level?
  - id: dialogflow_projects_locations_tools_list
    intent: List ES tools in a location
    question: Which v2 tools are defined in my project for a given location?
  - id: dialogflow_projects_locations_tools_delete
    intent: Delete an ES tool in a location
    question: Can I delete a location-level v2 tool I no longer need?
  phrasing_ops: 10
  slug: google-dialogflow-tools-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The transitionRouteGroups API from Google Dialogflow — 4 operation(s) for transitionroutegroups.
  name: Google Dialogflow Transition Route Groups API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_transitionRouteGroups_get
    intent: Get an agent-level transition route group
    question: What routes are inside a transition route group shared across my whole CX agent?
  - id: dialogflow_projects_locations_agents_transitionRouteGroups_delete
    intent: Delete an agent-level transition route group
    question: Can I delete a transition route group shared at the CX agent level?
  - id: dialogflow_projects_locations_agents_transitionRouteGroups_patch
    intent: Update an agent-level transition route group
    question: How do I change the routes in a transition route group shared across my CX agent?
  - id: dialogflow_projects_locations_agents_transitionRouteGroups_list
    intent: List agent-level transition route groups
    question: Which transition route groups are shared at the agent level on my Dialogflow CX agent?
  - id: dialogflow_projects_locations_agents_transitionRouteGroups_create
    intent: Create an agent-level transition route group
    question: How do I create a reusable transition route group that any flow in my CX agent can use?
  - id: dialogflow_projects_locations_agents_flows_transitionRouteGroups_get
    intent: Get a flow's transition route group
    question: What does a transition route group that belongs to one flow of my CX agent contain?
  - id: dialogflow_projects_locations_agents_flows_transitionRouteGroups_delete
    intent: Delete a flow's transition route group
    question: Can I delete a transition route group defined inside a single CX flow?
  - id: dialogflow_projects_locations_agents_flows_transitionRouteGroups_patch
    intent: Update a flow's transition route group
    question: How do I edit the routes in a transition route group that lives in one CX flow?
  phrasing_ops: 10
  slug: google-dialogflow-transitionroutegroups-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The versions API from Google Dialogflow — 14 operation(s) for versions.
  name: Google Dialogflow Versions API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_playbooks_versions_restore
    intent: Restore a playbook to a saved version
    question: Can I roll a Dialogflow CX playbook back to an earlier saved version?
  - id: dialogflow_projects_locations_agents_playbooks_versions_get
    intent: Get a saved playbook version
    question: Where can I see what a specific saved version of my playbook contains?
  - id: dialogflow_projects_locations_agents_playbooks_versions_delete
    intent: Delete a saved playbook version
    question: Can I remove a playbook version snapshot I no longer need?
  - id: dialogflow_projects_locations_agents_playbooks_versions_create
    intent: Save a new version of a playbook
    question: How do I snapshot a playbook before I start editing it?
  - id: dialogflow_projects_locations_agents_playbooks_versions_list
    intent: List saved versions of a playbook
    question: Which saved versions exist for one of my CX playbooks?
  - id: dialogflow_projects_locations_agents_tools_versions_delete
    intent: Delete a saved tool version
    question: Can I delete a tool version even if something still references it?
  - id: dialogflow_projects_locations_agents_tools_versions_get
    intent: Get a saved tool version
    question: Can I look at an earlier saved version of an agent tool's definition?
  - id: dialogflow_projects_locations_agents_tools_versions_list
    intent: List saved versions of a tool
    question: What versions have been saved for one of my agent's tools?
  phrasing_ops: 27
  slug: google-dialogflow-versions-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The webhooks API from Google Dialogflow — 2 operation(s) for webhooks.
  name: Google Dialogflow Webhooks API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_webhooks_patch
    intent: Update a CX webhook
    question: How do I change the endpoint URL of an existing webhook?
  - id: dialogflow_projects_locations_agents_webhooks_delete
    intent: Delete a CX webhook
    question: Can I delete a webhook that fulfillment still points to?
  - id: dialogflow_projects_locations_agents_webhooks_get
    intent: Get a CX webhook
    question: Can I see the URL and timeout configured for one of my CX webhooks?
  - id: dialogflow_projects_locations_agents_webhooks_create
    intent: Create a webhook on a CX agent
    question: How do I register a new webhook endpoint for my CX agent?
  - id: dialogflow_projects_locations_agents_webhooks_list
    intent: List webhooks on a CX agent
    question: Which webhooks are defined on my CX agent?
  phrasing_ops: 5
  slug: google-dialogflow-webhooks-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The Entity Types API from Google Dialogflow — 24 operation(s) for entity types.
  name: Google Dialogflow Entity Types API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_sessions_entityTypes_list
    intent: List session entity types in a CX session
    question: Which session-scoped entity type overrides are active in my Dialogflow CX conversation session?
  - id: dialogflow_projects_locations_agents_sessions_entityTypes_create
    intent: Add a session entity type to a CX session
    question: Can I give one Dialogflow CX conversation session its own extra entity values?
  - id: dialogflow_projects_locations_agents_sessions_entityTypes_get
    intent: Get a session entity type in a CX session
    question: What entity values does one specific session entity type hold in my CX conversation session?
  - id: dialogflow_projects_locations_agents_sessions_entityTypes_delete
    intent: Delete a session entity type from a CX session
    question: Is there a way to remove a session entity override from a live Dialogflow CX conversation session?
  - id: dialogflow_projects_locations_agents_sessions_entityTypes_patch
    intent: Update a session entity type in a CX session
    question: Can I change the entity values of a session entity type already attached to a CX conversation session?
  - id: dialogflow_projects_locations_agents_entityTypes_delete
    intent: Delete an entity type from a CX agent
    question: Which call deletes an entity type from my Dialogflow CX agent?
  - id: dialogflow_projects_locations_agents_entityTypes_patch
    intent: Update an entity type on a CX agent
    question: How do I add synonyms or rename an existing entity type on a Dialogflow CX agent?
  - id: dialogflow_projects_locations_agents_entityTypes_get
    intent: Get an entity type on a CX agent
    question: What definition and synonyms does one entity type on my Dialogflow CX agent have?
  phrasing_ops: 51
  slug: google-dialogflow-entity-types-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The Knowledge Bases API from Google Dialogflow — 6 operation(s) for knowledge bases.
  name: Google Dialogflow Knowledge Bases API
  phrasing_intents:
  - id: dialogflow_projects_knowledgeBases_delete
    intent: Delete a project-level knowledge base
    question: Can I delete a knowledge base that still has documents in it?
  - id: dialogflow_projects_knowledgeBases_get
    intent: Retrieve a project-level knowledge base
    question: What language and display name does one of my Dialogflow knowledge bases have?
  - id: dialogflow_projects_knowledgeBases_patch
    intent: Update a project-level knowledge base
    question: How do I rename a knowledge base in my project?
  - id: dialogflow_projects_knowledgeBases_create
    intent: Create a project-level knowledge base
    question: How do I create a new knowledge base to hold FAQ documents?
  - id: dialogflow_projects_knowledgeBases_list
    intent: List project-level knowledge bases
    question: Which knowledge bases exist in my Google Cloud project?
  - id: dialogflow_projects_locations_knowledgeBases_delete
    intent: Delete a regional knowledge base
    question: Can I delete a knowledge base hosted in a particular location?
  - id: dialogflow_projects_locations_knowledgeBases_get
    intent: Retrieve a regional knowledge base
    question: Can I look up a knowledge base that is stored in a specific region?
  - id: dialogflow_projects_locations_knowledgeBases_patch
    intent: Update a regional knowledge base
    question: How can I rename a knowledge base that lives in a specific region?
  phrasing_ops: 15
  slug: google-dialogflow-knowledge-bases-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The Security Settings API from Google Dialogflow — 2 operation(s) for security settings.
  name: Google Dialogflow Security Settings API
  phrasing_intents:
  - id: dialogflow_projects_locations_securitySettings_list
    intent: List security settings in a location
    question: Which Dialogflow CX security settings profiles exist in my project and region?
  - id: dialogflow_projects_locations_securitySettings_create
    intent: Create security settings for redaction and retention
    question: How do I make my conversational agents redact sensitive data from logs?
  - id: dialogflow_projects_locations_securitySettings_get
    intent: Retrieve security settings
    question: What redaction and retention rules does a security settings profile apply?
  - id: dialogflow_projects_locations_securitySettings_patch
    intent: Update security settings
    question: How do I shorten the retention period on existing security settings?
  - id: dialogflow_projects_locations_securitySettings_delete
    intent: Delete security settings
    question: Can I delete a security settings profile no agent uses anymore?
  phrasing_ops: 5
  slug: google-dialogflow-security-settings-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The SIP Trunks API from Google Dialogflow — 2 operation(s) for sip trunks.
  name: Google Dialogflow SIP Trunks API
  phrasing_intents:
  - id: dialogflow_projects_locations_sipTrunks_patch
    intent: Update a SIP trunk
    question: How do I change the peer hostnames allowed on an existing SIP trunk?
  - id: dialogflow_projects_locations_sipTrunks_get
    intent: Get a SIP trunk
    question: What hostnames and connection status does one SIP trunk connected to Dialogflow report?
  - id: dialogflow_projects_locations_sipTrunks_delete
    intent: Delete a SIP trunk
    question: Can I disconnect and delete a SIP trunk from Dialogflow?
  - id: dialogflow_projects_locations_sipTrunks_list
    intent: List SIP trunks
    question: Which SIP trunks have I connected to Dialogflow telephony in a region?
  - id: dialogflow_projects_locations_sipTrunks_create
    intent: Connect a new SIP trunk
    question: How do I connect my carrier's SIP trunk to Dialogflow for phone calls?
  phrasing_ops: 5
  slug: google-dialogflow-sip-trunks-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The Test Cases API from Google Dialogflow — 8 operation(s) for test cases.
  name: Google Dialogflow Test Cases API
  phrasing_intents:
  - id: dialogflow_projects_locations_agents_testCases_import
    intent: Import test cases into a CX agent
    question: Can I load conversation test cases from a file into my CX agent?
  - id: dialogflow_projects_locations_agents_testCases_patch
    intent: Update a test case
    question: How do I edit the expected turns of an existing test case?
  - id: dialogflow_projects_locations_agents_testCases_get
    intent: Get a test case
    question: Where can I see the turns and last result of one test case?
  - id: dialogflow_projects_locations_agents_testCases_run
    intent: Run a single test case
    question: Can I run one test case against a particular environment?
  - id: dialogflow_projects_locations_agents_testCases_list
    intent: List test cases on a CX agent
    question: Which test cases are defined for my CX agent?
  - id: dialogflow_projects_locations_agents_testCases_create
    intent: Create a test case
    question: How do I write a new conversation test case for my agent?
  - id: dialogflow_projects_locations_agents_testCases_calculateCoverage
    intent: Calculate test coverage for a CX agent
    question: How much of my agent's intents or transitions do my test cases cover?
  - id: dialogflow_projects_locations_agents_testCases_batchRun
    intent: Run several test cases at once
    question: Can I run a batch of test cases in a single request?
  phrasing_ops: 10
  slug: google-dialogflow-test-cases-api
artifact_total: 192
asyncapis:
- description: ''
  name: Google Dialogflow Webhooks
  slug: google-dialogflow-webhooks
collections:
- collection_type: open
  name: Dialogflow ES Projects API
  slug: open-google-dialogflow-projects-api
- collection_type: open
  name: Dialogflow ES API
  slug: open-google-dialogflow
common:
- group: design
  href: https://artifacts.apis.io/google-dialogflow/rules/google-dialogflow-rules.yml
  title: ''
  type: Spectral
  url: rules/google-dialogflow-rules.yml
- group: design
  href: https://artifacts.apis.io/google-dialogflow/json-ld/google-dialogflow-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/google-dialogflow-context.jsonld
- group: design
  href: https://artifacts.apis.io/google-dialogflow/vocabulary/google-dialogflow-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/google-dialogflow-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/google-dialogflow/hosts/google-dialogflow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/google-dialogflow-hosts.yml
- group: build
  href: https://artifacts.apis.io/google-dialogflow/integrations/google-dialogflow-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/google-dialogflow-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/google-dialogflow/capabilities/google-dialogflow-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-dialogflow-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/google-dialogflow/overlays/google-dialogflow-cx-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/google-dialogflow-cx-v3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/google-dialogflow/overlays/google-dialogflow-es-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/google-dialogflow-es-v2-overlay.yaml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Website
  url: https://cloud.google.com/dialogflow
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.google.com/dialogflow/docs
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/dialogflow/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cloud.google.com/dialogflow/docs/reference/rest
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/dialogflow/es/docs/quick/setup
- group: auth
  href: https://artifacts.apis.io/google-dialogflow/authentication/google-dialogflow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-dialogflow-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-dialogflow/scopes/google-dialogflow-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-dialogflow-scopes.yml
- group: agent
  href: https://artifacts.apis.io/google-dialogflow/agentic-access/google-dialogflow-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-dialogflow-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/google-dialogflow/packages/google-dialogflow-packages.yml
  title: ''
  type: Packages
  url: packages/google-dialogflow-packages.yml
- group: build
  href: https://artifacts.apis.io/google-dialogflow/packages/google-dialogflow-packages.yml
  title: ''
  type: SDKs
  url: packages/google-dialogflow-packages.yml
- group: build
  href: https://artifacts.apis.io/google-dialogflow/cli/google-dialogflow-cli.yml
  title: ''
  type: CLI
  url: cli/google-dialogflow-cli.yml
- group: design
  href: https://artifacts.apis.io/google-dialogflow/components/google-dialogflow-components.yml
  title: ''
  type: Components
  url: components/google-dialogflow-components.yml
- group: start
  href: https://artifacts.apis.io/google-dialogflow/sandbox/google-dialogflow-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/google-dialogflow-sandbox.yml
- group: design
  href: https://artifacts.apis.io/google-dialogflow/conventions/google-dialogflow-conventions.yml
  title: ''
  type: Conventions
  url: conventions/google-dialogflow-conventions.yml
- group: design
  href: https://artifacts.apis.io/google-dialogflow/data-model/google-dialogflow-data-model.yml
  title: ''
  type: DataModel
  url: data-model/google-dialogflow-data-model.yml
- group: design
  href: https://artifacts.apis.io/google-dialogflow/errors/google-dialogflow-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/google-dialogflow-problem-types.yml
- group: design
  href: https://artifacts.apis.io/google-dialogflow/lifecycle/google-dialogflow-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/google-dialogflow-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  href: https://artifacts.apis.io/google-dialogflow/lifecycle/google-dialogflow-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/google-dialogflow-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/google-dialogflow/changelog/google-dialogflow-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/google-dialogflow-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://cloud.google.com/dialogflow/docs/release-notes
- group: design
  href: https://artifacts.apis.io/google-dialogflow/conformance/google-dialogflow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-dialogflow-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cloud.google.com/dialogflow/docs/compliance-security-controls
- group: design
  href: https://artifacts.apis.io/google-dialogflow/asyncapi/google-dialogflow-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/google-dialogflow-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/google-dialogflow/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/google-dialogflow/llms/google-dialogflow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/google-dialogflow-llms.txt
- group: agent
  href: https://artifacts.apis.io/google-dialogflow/well-known/google-dialogflow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-dialogflow-well-known.yml
- group: auth
  href: https://artifacts.apis.io/google-dialogflow/well-known/google-dialogflow-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/google-dialogflow-security.txt
- group: auth
  href: https://artifacts.apis.io/google-dialogflow/security/google-dialogflow-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/google-dialogflow-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-dialogflow/security/google-dialogflow-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-dialogflow-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-dialogflow/security/google-dialogflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-dialogflow-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/google-dialogflow/plans/google-dialogflow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-dialogflow-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-dialogflow/rate-limits/google-dialogflow-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-dialogflow-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-dialogflow/finops/google-dialogflow-finops.yml
  title: ''
  type: FinOps
  url: finops/google-dialogflow-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/dialogflow/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.cloud.google.com/freetrial
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/dialogflow/docs/support
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/ai-machine-learning
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://cloud.google.com/dialogflow/sla
- group: operate
  title: ''
  type: Quotas
  url: https://cloud.google.com/dialogflow/quotas
created: '2024-01-01'
description: Google Dialogflow is Google Cloud's conversational-agent platform, shipped as two editions on one API host. Dialogflow ES (Essentials, API v2) builds intent-, entity- and context-driven agents with knowledge connectors and the Agent Assist surface for human contact-centre agents. Dialogflow CX — now branded Conversational Agents, API v3 — builds flow-based state-machine agents and generative playbook agents backed by Gemini models, data stores, generators and tool calling, with test cases, experiments, versions and environments as first-class API resources. Both are called at dialogflow.googleapis.com with a Google OAuth 2.0 bearer token; there is no API key. Google publishes no OpenAPI for Dialogflow — the first-party machine-readable contracts are the Google Discovery Documents served by the API host itself (279 operations on v2, 158 on v3) and the protobuf IDL in googleapis/googleapis (42 gRPC services, 267 RPCs).
finops:
- has_sources: true
  method: derived
  name: Google Dialogflow Finops
  primary_unit: count (request)
  service_category: ''
  slug: google-dialogflow-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-dialogflow.png
json_schemas:
- name: GoogleCloudDialogflowCxV3Agent
  property_count: 24
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-agent
- name: GoogleCloudDialogflowCxV3AgentValidationResult
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-agent-validation-result
- name: GoogleCloudDialogflowCxV3BatchRunTestCasesRequest
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-batch-run-test-cases-request
- name: GoogleCloudDialogflowCxV3CalculateCoverageResponse
  property_count: 4
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-calculate-coverage-response
- name: GoogleCloudDialogflowCxV3Changelog
  property_count: 8
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-changelog
- name: GoogleCloudDialogflowCxV3Deployment
  property_count: 6
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-deployment
- name: GoogleCloudDialogflowCxV3DetectIntentRequest
  property_count: 4
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-detect-intent-request
- name: GoogleCloudDialogflowCxV3DetectIntentResponse
  property_count: 6
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-detect-intent-response
- name: GoogleCloudDialogflowCxV3EntityType
  property_count: 8
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-entity-type
- name: GoogleCloudDialogflowCxV3Environment
  property_count: 7
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-environment
- name: GoogleCloudDialogflowCxV3Example
  property_count: 11
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-example
- name: GoogleCloudDialogflowCxV3Experiment
  property_count: 15
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-experiment
- name: GoogleCloudDialogflowCxV3ExportAgentRequest
  property_count: 5
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-export-agent-request
- name: GoogleCloudDialogflowCxV3ExportFlowRequest
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-export-flow-request
- name: GoogleCloudDialogflowCxV3ExportIntentsRequest
  property_count: 4
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-export-intents-request
- name: GoogleCloudDialogflowCxV3ExportPlaybookRequest
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-export-playbook-request
- name: GoogleCloudDialogflowCxV3ExportTestCasesRequest
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-export-test-cases-request
- name: GoogleCloudDialogflowCxV3Flow
  property_count: 13
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-flow
- name: GoogleCloudDialogflowCxV3FlowValidationResult
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-flow-validation-result
- name: GoogleCloudDialogflowCxV3FulfillIntentRequest
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-fulfill-intent-request
- name: GoogleCloudDialogflowCxV3GenerativeSettings
  property_count: 6
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-generative-settings
- name: GoogleCloudDialogflowCxV3Generator
  property_count: 6
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-generator
- name: GoogleCloudDialogflowCxV3ImportEntityTypesRequest
  property_count: 4
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-import-entity-types-request
- name: GoogleCloudDialogflowCxV3ImportFlowRequest
  property_count: 4
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-import-flow-request
- name: GoogleCloudDialogflowCxV3ImportIntentsRequest
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-import-intents-request
- name: GoogleCloudDialogflowCxV3ImportPlaybookRequest
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-import-playbook-request
- name: GoogleCloudDialogflowCxV3Intent
  property_count: 9
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-intent
- name: GoogleCloudDialogflowCxV3ListChangelogsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-changelogs-response
- name: GoogleCloudDialogflowCxV3ListContinuousTestResultsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-continuous-test-results-response
- name: GoogleCloudDialogflowCxV3ListDeploymentsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-deployments-response
- name: GoogleCloudDialogflowCxV3ListEnvironmentsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-environments-response
- name: GoogleCloudDialogflowCxV3ListExamplesResponse
  property_count: 1
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-examples-response
- name: GoogleCloudDialogflowCxV3ListExperimentsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-experiments-response
- name: GoogleCloudDialogflowCxV3ListFlowsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-flows-response
- name: GoogleCloudDialogflowCxV3ListGeneratorsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-generators-response
- name: GoogleCloudDialogflowCxV3ListPagesResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-pages-response
- name: GoogleCloudDialogflowCxV3ListPlaybookVersionsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-playbook-versions-response
- name: GoogleCloudDialogflowCxV3ListPlaybooksResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-playbooks-response
- name: GoogleCloudDialogflowCxV3ListSecuritySettingsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-security-settings-response
- name: GoogleCloudDialogflowCxV3ListTestCaseResultsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-test-case-results-response
- name: GoogleCloudDialogflowCxV3ListTestCasesResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-test-cases-response
- name: GoogleCloudDialogflowCxV3ListToolsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-tools-response
- name: GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-list-transition-route-groups-response
- name: GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-lookup-environment-history-response
- name: GoogleCloudDialogflowCxV3MatchIntentResponse
  property_count: 6
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-match-intent-response
- name: GoogleCloudDialogflowCxV3Page
  property_count: 10
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-page
- name: GoogleCloudDialogflowCxV3Playbook
  property_count: 17
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-playbook
- name: GoogleCloudDialogflowCxV3PlaybookVersion
  property_count: 4
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-playbook-version
- name: GoogleCloudDialogflowCxV3RestoreAgentRequest
  property_count: 4
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-restore-agent-request
- name: GoogleCloudDialogflowCxV3SecuritySettings
  property_count: 11
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-security-settings
- name: GoogleCloudDialogflowCxV3SessionEntityType
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-session-entity-type
- name: GoogleCloudDialogflowCxV3TestCaseResult
  property_count: 5
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-test-case-result
- name: GoogleCloudDialogflowCxV3TestCase
  property_count: 8
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-test-case
- name: GoogleCloudDialogflowCxV3Tool
  property_count: 7
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-tool
- name: GoogleCloudDialogflowCxV3ToolVersion
  property_count: 5
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-tool-version
- name: GoogleCloudDialogflowCxV3TransitionRouteGroup
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-transition-route-group
- name: GoogleCloudDialogflowCxV3Version
  property_count: 6
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-version
- name: GoogleCloudDialogflowCxV3Webhook
  property_count: 6
  slug: google-dialogflow-google-cloud-dialogflow-cx-v3-webhook
- name: GoogleCloudDialogflowV2Agent
  property_count: 12
  slug: google-dialogflow-google-cloud-dialogflow-v2-agent
- name: GoogleCloudDialogflowV2AnalyzeContentRequest
  property_count: 9
  slug: google-dialogflow-google-cloud-dialogflow-v2-analyze-content-request
- name: GoogleCloudDialogflowV2AnalyzeContentResponse
  property_count: 7
  slug: google-dialogflow-google-cloud-dialogflow-v2-analyze-content-response
- name: GoogleCloudDialogflowV2AnswerRecord
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-v2-answer-record
- name: GoogleCloudDialogflowV2BatchCreateEntitiesRequest
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-batch-create-entities-request
- name: GoogleCloudDialogflowV2BatchDeleteEntitiesRequest
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-batch-delete-entities-request
- name: GoogleCloudDialogflowV2BatchUpdateEntitiesRequest
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-v2-batch-update-entities-request
- name: GoogleCloudDialogflowV2BatchUpdateIntentsRequest
  property_count: 5
  slug: google-dialogflow-google-cloud-dialogflow-v2-batch-update-intents-request
- name: GoogleCloudDialogflowV2ClearSuggestionFeatureConfigRequest
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-clear-suggestion-feature-config-request
- name: GoogleCloudDialogflowV2CompleteConversationRequest
  property_count: 0
  slug: google-dialogflow-google-cloud-dialogflow-v2-complete-conversation-request
- name: GoogleCloudDialogflowV2Context
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-v2-context
- name: GoogleCloudDialogflowV2ConversationDataset
  property_count: 9
  slug: google-dialogflow-google-cloud-dialogflow-v2-conversation-dataset
- name: GoogleCloudDialogflowV2ConversationModelEvaluation
  property_count: 6
  slug: google-dialogflow-google-cloud-dialogflow-v2-conversation-model-evaluation
- name: GoogleCloudDialogflowV2ConversationModel
  property_count: 10
  slug: google-dialogflow-google-cloud-dialogflow-v2-conversation-model
- name: GoogleCloudDialogflowV2ConversationProfile
  property_count: 17
  slug: google-dialogflow-google-cloud-dialogflow-v2-conversation-profile
- name: GoogleCloudDialogflowV2Conversation
  property_count: 11
  slug: google-dialogflow-google-cloud-dialogflow-v2-conversation
- name: GoogleCloudDialogflowV2CreateConversationModelEvaluationRequest
  property_count: 1
  slug: google-dialogflow-google-cloud-dialogflow-v2-create-conversation-model-evaluation-request
- name: GoogleCloudDialogflowV2DeployConversationModelRequest
  property_count: 0
  slug: google-dialogflow-google-cloud-dialogflow-v2-deploy-conversation-model-request
- name: GoogleCloudDialogflowV2DetectIntentRequest
  property_count: 5
  slug: google-dialogflow-google-cloud-dialogflow-v2-detect-intent-request
- name: GoogleCloudDialogflowV2DetectIntentResponse
  property_count: 5
  slug: google-dialogflow-google-cloud-dialogflow-v2-detect-intent-response
- name: GoogleCloudDialogflowV2Document
  property_count: 10
  slug: google-dialogflow-google-cloud-dialogflow-v2-document
- name: GoogleCloudDialogflowV2EncryptionSpec
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-encryption-spec
- name: GoogleCloudDialogflowV2EntityType
  property_count: 6
  slug: google-dialogflow-google-cloud-dialogflow-v2-entity-type
- name: GoogleCloudDialogflowV2EnvironmentHistory
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-v2-environment-history
- name: GoogleCloudDialogflowV2Environment
  property_count: 7
  slug: google-dialogflow-google-cloud-dialogflow-v2-environment
- name: GoogleCloudDialogflowV2ExportDocumentRequest
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-v2-export-document-request
- name: GoogleCloudDialogflowV2Fulfillment
  property_count: 5
  slug: google-dialogflow-google-cloud-dialogflow-v2-fulfillment
- name: GoogleCloudDialogflowV2GenerateStatelessSuggestionRequest
  property_count: 6
  slug: google-dialogflow-google-cloud-dialogflow-v2-generate-stateless-suggestion-request
- name: GoogleCloudDialogflowV2GenerateStatelessSuggestionResponse
  property_count: 1
  slug: google-dialogflow-google-cloud-dialogflow-v2-generate-stateless-suggestion-response
- name: GoogleCloudDialogflowV2GenerateStatelessSummaryRequest
  property_count: 4
  slug: google-dialogflow-google-cloud-dialogflow-v2-generate-stateless-summary-request
- name: GoogleCloudDialogflowV2GenerateSuggestionsRequest
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-generate-suggestions-request
- name: GoogleCloudDialogflowV2GeneratorEvaluation
  property_count: 10
  slug: google-dialogflow-google-cloud-dialogflow-v2-generator-evaluation
- name: GoogleCloudDialogflowV2Generator
  property_count: 15
  slug: google-dialogflow-google-cloud-dialogflow-v2-generator
- name: GoogleCloudDialogflowV2ImportAgentRequest
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-import-agent-request
- name: GoogleCloudDialogflowV2ImportConversationDataRequest
  property_count: 1
  slug: google-dialogflow-google-cloud-dialogflow-v2-import-conversation-data-request
- name: GoogleCloudDialogflowV2ImportDocumentsRequest
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-v2-import-documents-request
- name: GoogleCloudDialogflowV2IngestContextReferencesRequest
  property_count: 1
  slug: google-dialogflow-google-cloud-dialogflow-v2-ingest-context-references-request
- name: GoogleCloudDialogflowV2IngestContextReferencesResponse
  property_count: 1
  slug: google-dialogflow-google-cloud-dialogflow-v2-ingest-context-references-response
- name: GoogleCloudDialogflowV2InitializeEncryptionSpecRequest
  property_count: 1
  slug: google-dialogflow-google-cloud-dialogflow-v2-initialize-encryption-spec-request
- name: GoogleCloudDialogflowV2Intent
  property_count: 20
  slug: google-dialogflow-google-cloud-dialogflow-v2-intent
- name: GoogleCloudDialogflowV2KnowledgeBase
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-v2-knowledge-base
- name: GoogleCloudDialogflowV2ListAnswerRecordsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-list-answer-records-response
- name: GoogleCloudDialogflowV2ListContextsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-list-contexts-response
- name: GoogleCloudDialogflowV2ListConversationDatasetsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-list-conversation-datasets-response
- name: GoogleCloudDialogflowV2ListConversationModelEvaluationsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-list-conversation-model-evaluations-response
- name: GoogleCloudDialogflowV2ListConversationModelsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-list-conversation-models-response
- name: GoogleCloudDialogflowV2ListConversationProfilesResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-list-conversation-profiles-response
- name: GoogleCloudDialogflowV2ListConversationsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-list-conversations-response
- name: GoogleCloudDialogflowV2ListDocumentsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-list-documents-response
- name: GoogleCloudDialogflowV2ListGeneratorEvaluationsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-list-generator-evaluations-response
- name: GoogleCloudDialogflowV2ListGeneratorsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-list-generators-response
- name: GoogleCloudDialogflowV2ListKnowledgeBasesResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-list-knowledge-bases-response
- name: GoogleCloudDialogflowV2ListMessagesResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-list-messages-response
- name: GoogleCloudDialogflowV2ListParticipantsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-list-participants-response
- name: GoogleCloudDialogflowV2ListSipTrunksResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-list-sip-trunks-response
- name: GoogleCloudDialogflowV2ListToolsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-list-tools-response
- name: GoogleCloudDialogflowV2Participant
  property_count: 6
  slug: google-dialogflow-google-cloud-dialogflow-v2-participant
- name: GoogleCloudDialogflowV2ReloadDocumentRequest
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-v2-reload-document-request
- name: GoogleCloudDialogflowV2RestoreAgentRequest
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-restore-agent-request
- name: GoogleCloudDialogflowV2SearchAgentsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-search-agents-response
- name: GoogleCloudDialogflowV2SearchKnowledgeRequest
  property_count: 10
  slug: google-dialogflow-google-cloud-dialogflow-v2-search-knowledge-request
- name: GoogleCloudDialogflowV2SearchKnowledgeResponse
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-v2-search-knowledge-response
- name: GoogleCloudDialogflowV2SessionEntityType
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-v2-session-entity-type
- name: GoogleCloudDialogflowV2SetSuggestionFeatureConfigRequest
  property_count: 2
  slug: google-dialogflow-google-cloud-dialogflow-v2-set-suggestion-feature-config-request
- name: GoogleCloudDialogflowV2SipTrunk
  property_count: 6
  slug: google-dialogflow-google-cloud-dialogflow-v2-sip-trunk
- name: GoogleCloudDialogflowV2SuggestKnowledgeAssistResponse
  property_count: 4
  slug: google-dialogflow-google-cloud-dialogflow-v2-suggest-knowledge-assist-response
- name: GoogleCloudDialogflowV2SuggestSmartRepliesResponse
  property_count: 3
  slug: google-dialogflow-google-cloud-dialogflow-v2-suggest-smart-replies-response
- name: GoogleCloudDialogflowV2Tool
  property_count: 13
  slug: google-dialogflow-google-cloud-dialogflow-v2-tool
- name: GoogleCloudDialogflowV2UndeployConversationModelRequest
  property_count: 0
  slug: google-dialogflow-google-cloud-dialogflow-v2-undeploy-conversation-model-request
- name: GoogleCloudDialogflowV2ValidationResult
  property_count: 1
  slug: google-dialogflow-google-cloud-dialogflow-v2-validation-result
- name: GoogleCloudDialogflowV2Version
  property_count: 5
  slug: google-dialogflow-google-cloud-dialogflow-v2-version
- name: GoogleCloudLocationListLocationsResponse
  property_count: 2
  slug: google-dialogflow-google-cloud-location-list-locations-response
- name: GoogleCloudLocationLocation
  property_count: 5
  slug: google-dialogflow-google-cloud-location-location
- name: GoogleLongrunningListOperationsResponse
  property_count: 3
  slug: google-dialogflow-google-longrunning-list-operations-response
- name: GoogleLongrunningOperation
  property_count: 5
  slug: google-dialogflow-google-longrunning-operation
- name: GoogleProtobufEmpty
  property_count: 0
  slug: google-dialogflow-google-protobuf-empty
jsonld:
- class_count: 120
  name: Google Dialogflow Context
  property_count: 296
  slug: google-dialogflow-context
layout: provider
modified: '2026-09-12'
name: Google Dialogflow
nav: Providers
network: true
overview: 'Google Dialogflow publishes 42 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Agents API, Answer Records API, and 39 more. Tagged areas include Agents, Artificial Intelligence, Chatbots, Conversational AI, and Google Cloud.


  The Google Dialogflow catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Google Dialogflow''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, sandbox, changelog, and 45 more developer resources.'
plans:
- name: Google Dialogflow Plans Pricing
  plan_count: 5
  slug: google-dialogflow-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 25
  name: Google Dialogflow Rate Limits
  slug: google-dialogflow-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Google Dialogflow API Rules
  rule_count: 68
  severity_counts:
    error: 58
    hint: 0
    info: 3
    warn: 7
  slug: google-dialogflow-rules
scopes:
- name: Google Dialogflow Scopes
  scope_count: 2
  slug: google-dialogflow-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: exemplar
  composite: 73.1
  coverage:
    artifact_dirs: 41
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.9
  facets:
    access_clarity: 78.9
    contract_governance: 35.6
    contract_quality: 67.7
    developer_ergonomics: 73.2
    discoverability: 66.1
    operational_transparency: 92.1
  previous_composite: 69.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 43
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 41.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-dialogflow/google-dialogflow-2026-06-20T182157.png
security:
- kind: authentication
  name: Google Dialogflow Authentication
  slug: google-dialogflow-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Google Dialogflow Domain Security
  slug: google-dialogflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Dialogflow Vulnerability Disclosure
  slug: google-dialogflow-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: google-dialogflow-detect-intent
  slug: google-dialogflow-detect-intent
- name: google-dialogflow-manage-intents
  slug: google-dialogflow-manage-intents
- name: google-dialogflow-webhook-fulfillment
  slug: google-dialogflow-webhook-fulfillment
slug: google-dialogflow
tags:
- Agents
- Artificial Intelligence
- Chatbots
- Conversational AI
- Google Cloud
- Machine Learning
- Natural Language Processing
- Speech Recognition
- Virtual Agents
- Voice Assistant
website: https://cloud.google.com/dialogflow
---
