---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Scale Ai Agentic Access
  operation_count: 14
  slug: scale-ai-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 9
apis:
- description: The Scale REST API is the unified programmatic surface for Scale's data engine. It is built on REST principles with resource-oriented URLs, form-encoded request bodies, JSON responses, and standard HT
  name: Scale REST API
  slug: scale-rest-api
- description: The GenAI Data Engine is Scale's product surface for generating, curating, and reviewing data used to train and tune generative-AI foundation models, including RLHF, SFT, evaluation, and red-team data
  name: Scale GenAI Data Engine
  slug: scale-genai-data-engine
- description: Scale's Automotive Data Engine covers autonomy-grade data needs including LiDAR labeling, sensor fusion, multi-stage annotation, the customer dashboard, data hosting, and Nucleus for dataset managemen
  name: Scale Automotive Data Engine
  slug: scale-automotive-data-engine
- description: Nucleus is Scale's dataset management product for browsing, querying, and curating ML datasets at scale.
  name: Scale Nucleus
  slug: scale-nucleus
- description: Donovan is Scale's AI platform for defense and public-sector use cases, delivering decision-support and analytic capabilities to U.S. and allied government customers.
  name: Scale Donovan
  slug: scale-donovan
- baseURL: https://api.scale.com
  baseurl_source: declared
  description: The Batches API from Scale AI — 4 operation(s) for batches.
  name: Scale AI Batches API
  slug: scale-ai-batches-api
- baseURL: https://api.scale.com
  baseurl_source: declared
  description: The Projects API from Scale AI — 3 operation(s) for projects.
  name: Scale AI Projects API
  slug: scale-ai-projects-api
- baseURL: https://api.scale.com
  baseurl_source: declared
  description: The Tasks API from Scale AI — 5 operation(s) for tasks.
  name: Scale AI Tasks API
  slug: scale-ai-tasks-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The account groups API from Scale AI — 1 operation(s) for account groups.
  name: Scale AI account groups API
  slug: scale-ai-account-groups-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Accounts API from Scale AI — 1 operation(s) for accounts.
  name: Scale AI Accounts API
  slug: scale-ai-accounts-api
- baseURL: https://agentex.sgp.scale.com
  baseurl_source: declared
  description: The Agent APIKeys API from Scale AI — 5 operation(s) for agent apikeys.
  name: Scale AI Agent APIKeys API
  slug: scale-ai-agent-apikeys-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Agent Configs API from Scale AI — 3 operation(s) for agent configs.
  name: Scale AI Agent Configs API
  slug: scale-ai-agent-configs-api
- baseURL: https://agentex.sgp.scale.com
  baseurl_source: declared
  description: The Agent Task Tracker API from Scale AI — 2 operation(s) for agent task tracker.
  name: Scale AI Agent Task Tracker API
  slug: scale-ai-agent-task-tracker-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Agentex Agent API from Scale AI — 1 operation(s) for agentex agent.
  name: Scale AI Agentex Agent API
  slug: scale-ai-agentex-agent-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Agentex Cloud Build API from Scale AI — 5 operation(s) for agentex cloud build.
  name: Scale AI Agentex Cloud Build API
  slug: scale-ai-agentex-cloud-build-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Agentex Cloud Deploy API from Scale AI — 3 operation(s) for agentex cloud deploy.
  name: Scale AI Agentex Cloud Deploy API
  slug: scale-ai-agentex-cloud-deploy-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Agents API from Scale AI — 11 operation(s) for agents.
  name: Scale AI Agents API
  slug: scale-ai-agents-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Annotation Tasks API from Scale AI — 1 operation(s) for annotation tasks.
  name: Scale AI Annotation Tasks API
  slug: scale-ai-annotation-tasks-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Application Specs API from Scale AI — 2 operation(s) for application specs.
  name: Scale AI Application Specs API
  slug: scale-ai-application-specs-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Applications API from Scale AI — 19 operation(s) for applications.
  name: Scale AI Applications API
  slug: scale-ai-applications-api
- baseURL: https://api.spellbook.scale.com/llm-engine
  baseurl_source: declared
  description: The Async Tasks API from Scale AI — 2 operation(s) for async tasks.
  name: Scale AI Async Tasks API
  slug: scale-ai-async-tasks-api
- baseURL: https://api.spellbook.scale.com/llm-engine
  baseurl_source: declared
  description: The Batch Completions API from Scale AI — 3 operation(s) for batch completions.
  name: Scale AI Batch Completions API
  slug: scale-ai-batch-completions-api
- baseURL: https://api.spellbook.scale.com/llm-engine
  baseurl_source: declared
  description: The Batch Jobs API from Scale AI — 2 operation(s) for batch jobs.
  name: Scale AI Batch Jobs API
  slug: scale-ai-batch-jobs-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Beta API from Scale AI — 5 operation(s) for beta.
  name: Scale AI Beta API
  slug: scale-ai-beta-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Chat Completions API from Scale AI — 1 operation(s) for chat completions.
  name: Scale AI Chat Completions API
  slug: scale-ai-chat-completions-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Chat Themes API from Scale AI — 2 operation(s) for chat themes.
  name: Scale AI Chat Themes API
  slug: scale-ai-chat-themes-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The ChatThreads API from Scale AI — 5 operation(s) for chatthreads.
  name: Scale AI Chat Threads API
  slug: scale-ai-chatthreads-api
- baseURL: https://agentex.sgp.scale.com
  baseurl_source: declared
  description: The Checkpoints API from Scale AI — 5 operation(s) for checkpoints.
  name: Scale AI Checkpoints API
  slug: scale-ai-checkpoints-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Chunks API from Scale AI — 1 operation(s) for chunks.
  name: Scale AI Chunks API
  slug: scale-ai-chunks-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Completions API from Scale AI — 2 operation(s) for completions.
  name: Scale AI Completions API
  slug: scale-ai-completions-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Credentials API from Scale AI — 5 operation(s) for credentials.
  name: Scale AI Credentials API
  slug: scale-ai-credentials-api
- baseURL: https://dex.sgp.scale.com
  baseurl_source: declared
  description: Project-scoped integration with the Data Sources service
  name: Scale AI Data sources API
  slug: scale-ai-data-sources-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Dataset Items API from Scale AI — 3 operation(s) for dataset items.
  name: Scale AI Dataset Items API
  slug: scale-ai-dataset-items-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Datasets API from Scale AI — 2 operation(s) for datasets.
  name: Scale AI Datasets API
  slug: scale-ai-datasets-api
- baseURL: https://agentex.sgp.scale.com
  baseurl_source: declared
  description: The Deployment History API from Scale AI — 2 operation(s) for deployment history.
  name: Scale AI Deployment History API
  slug: scale-ai-deployment-history-api
- baseURL: https://agentex.sgp.scale.com
  baseurl_source: declared
  description: The Deployments API from Scale AI — 4 operation(s) for deployments.
  name: Scale AI Deployments API
  slug: scale-ai-deployments-api
- baseURL: https://api.spellbook.scale.com/llm-engine
  baseurl_source: declared
  description: The Docker Image Batch Job Bundles API from Scale AI — 3 operation(s) for docker image batch job bundles.
  name: Scale AI Docker Image Batch Job Bundles API
  slug: scale-ai-docker-image-batch-job-bundles-api
- baseURL: https://api.spellbook.scale.com/llm-engine
  baseurl_source: declared
  description: The Docker Image Batch Jobs API from Scale AI — 2 operation(s) for docker image batch jobs.
  name: Scale AI Docker Image Batch Jobs API
  slug: scale-ai-docker-image-batch-jobs-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Evaluation Charts API from Scale AI — 2 operation(s) for evaluation charts.
  name: Scale AI Evaluation Charts API
  slug: scale-ai-evaluation-charts-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Evaluation Configs API from Scale AI — 2 operation(s) for evaluation configs.
  name: Scale AI Evaluation Configs API
  slug: scale-ai-evaluation-configs-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Evaluation Dashboards API from Scale AI — 4 operation(s) for evaluation dashboards.
  name: Scale AI Evaluation Dashboards API
  slug: scale-ai-evaluation-dashboards-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Evaluation Datasets API from Scale AI — 19 operation(s) for evaluation datasets.
  name: Scale AI Evaluation Datasets API
  slug: scale-ai-evaluation-datasets-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Evaluation Groups API from Scale AI — 3 operation(s) for evaluation groups.
  name: Scale AI Evaluation Groups API
  slug: scale-ai-evaluation-groups-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Evaluation Items API from Scale AI — 3 operation(s) for evaluation items.
  name: Scale AI Evaluation Items API
  slug: scale-ai-evaluation-items-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Evaluations API from Scale AI — 25 operation(s) for evaluations.
  name: Scale AI Evaluations API
  slug: scale-ai-evaluations-api
- baseURL: https://agentex.sgp.scale.com
  baseurl_source: declared
  description: The Events API from Scale AI — 2 operation(s) for events.
  name: Scale AI Events API
  slug: scale-ai-events-api
- baseURL: https://dex.sgp.scale.com
  baseurl_source: declared
  description: Operations related to starting extract jobs and accessing their results
  name: Scale AI Extract API
  slug: scale-ai-extract-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: Operations related to file upload and access
  name: Scale AI Files API
  slug: scale-ai-files-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Fine Tuning Jobs V3 (Beta) API from Scale AI — 3 operation(s) for fine tuning jobs v3 (beta).
  name: Scale AI Fine Tuning Jobs V3 (Beta) API
  slug: scale-ai-fine-tuning-jobs-v3-beta-api
- baseURL: https://api.spellbook.scale.com/llm-engine
  baseurl_source: declared
  description: The Healthz API from Scale AI — 1 operation(s) for healthz.
  name: Scale AI Healthz API
  slug: scale-ai-healthz-api
- baseURL: https://dex.sgp.scale.com
  baseurl_source: declared
  description: The Indexes API from Scale AI — 5 operation(s) for indexes.
  name: Scale AI Indexes API
  slug: scale-ai-indexes-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Inference API from Scale AI — 5 operation(s) for inference.
  name: Scale AI Inference API
  slug: scale-ai-inference-api
- baseURL: https://agentex.sgp.scale.com
  baseurl_source: declared
  description: The Integrations API from Scale AI — 1 operation(s) for integrations.
  name: Scale AI Integrations API
  slug: scale-ai-integrations-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Interactions API from Scale AI — 2 operation(s) for interactions.
  name: Scale AI Interactions API
  slug: scale-ai-interactions-api
- baseURL: https://dex.sgp.scale.com
  baseurl_source: declared
  description: Operations related to monitoring jobs and their status
  name: Scale AI Jobs API
  slug: scale-ai-jobs-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Knowledge Base Data Sources API from Scale AI — 2 operation(s) for knowledge base data sources.
  name: Scale AI Knowledge Base Data Sources API
  slug: scale-ai-knowledge-base-data-sources-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Knowledge Bases API from Scale AI — 19 operation(s) for knowledge bases.
  name: Scale AI Knowledge Bases API
  slug: scale-ai-knowledge-bases-api
- baseURL: https://agentex.sgp.scale.com
  baseurl_source: declared
  description: The Linear API from Scale AI — 1 operation(s) for linear.
  name: Scale AI Linear API
  slug: scale-ai-linear-api
- baseURL: https://api.spellbook.scale.com/llm-engine
  baseurl_source: declared
  description: The Llm API from Scale AI — 10 operation(s) for llm.
  name: Scale AI Llm API
  slug: scale-ai-llm-api
- baseURL: https://agentex.sgp.scale.com
  baseurl_source: declared
  description: The Messages API from Scale AI — 4 operation(s) for messages.
  name: Scale AI Messages API
  slug: scale-ai-messages-api
- baseURL: https://api.spellbook.scale.com/llm-engine
  baseurl_source: declared
  description: The Model Bundles API from Scale AI — 8 operation(s) for model bundles.
  name: Scale AI Model Bundles API
  slug: scale-ai-model-bundles-api
- baseURL: https://api.spellbook.scale.com/llm-engine
  baseurl_source: declared
  description: The Model Endpoints Api API from Scale AI — 1 operation(s) for model endpoints api.
  name: Scale AI Model Endpoints API
  slug: scale-ai-model-endpoints-api-api
- baseURL: https://api.spellbook.scale.com/llm-engine
  baseurl_source: declared
  description: The Model Endpoints API from Scale AI — 3 operation(s) for model endpoints.
  name: Scale AI Model Endpoints API
  slug: scale-ai-model-endpoints-api
- baseURL: https://api.spellbook.scale.com/llm-engine
  baseurl_source: declared
  description: The Model Endpoints Schema.json API from Scale AI — 1 operation(s) for model endpoints schema.json.
  name: Scale AI Model Endpoints Schema.json API
  slug: scale-ai-model-endpoints-schema-json-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Model server API from Scale AI — 10 operation(s) for model server.
  name: Scale AI Model server API
  slug: scale-ai-model-server-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Model Templates V3 (Beta) API from Scale AI — 2 operation(s) for model templates v3 (beta).
  name: Scale AI Model Templates V3 (Beta) API
  slug: scale-ai-model-templates-v3-beta-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: Model API.
  name: Scale AI Models API
  slug: scale-ai-models-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The MonitoringDashboard API from Scale AI — 3 operation(s) for monitoringdashboard.
  name: Scale AI Monitoring Dashboard API
  slug: scale-ai-monitoringdashboard-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Organizations API from Scale AI — 1 operation(s) for organizations.
  name: Scale AI Organizations API
  slug: scale-ai-organizations-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The package deployments API from Scale AI — 4 operation(s) for package deployments.
  name: Scale AI package deployments API
  slug: scale-ai-package-deployments-api
- baseURL: https://dex.sgp.scale.com
  baseurl_source: declared
  description: Operations related to starting parse jobs and accessing their results
  name: Scale AI Parse API
  slug: scale-ai-parse-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Question Sets API from Scale AI — 2 operation(s) for question sets.
  name: Scale AI Question Sets API
  slug: scale-ai-question-sets-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Questions API from Scale AI — 5 operation(s) for questions.
  name: Scale AI Questions API
  slug: scale-ai-questions-api
- baseURL: https://api.spellbook.scale.com/llm-engine
  baseurl_source: declared
  description: The Readyz API from Scale AI — 1 operation(s) for readyz.
  name: Scale AI Readyz API
  slug: scale-ai-readyz-api
- baseURL: https://dex.sgp.scale.com
  baseurl_source: declared
  description: Dex Research agent kickoff and results.
  name: Scale AI Research API
  slug: scale-ai-research-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Rubrics API from Scale AI — 5 operation(s) for rubrics.
  name: Scale AI Rubrics API
  slug: scale-ai-rubrics-api
- baseURL: https://agentex.sgp.scale.com
  baseurl_source: declared
  description: The Schedules API from Scale AI — 11 operation(s) for schedules.
  name: Scale AI Schedules API
  slug: scale-ai-schedules-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Serving API from Scale AI — 3 operation(s) for serving.
  name: Scale AI Serving API
  slug: scale-ai-serving-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Sessions API from Scale AI — 2 operation(s) for sessions.
  name: Scale AI Sessions API
  slug: scale-ai-sessions-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The SGP Cloud Secrets API from Scale AI — 2 operation(s) for sgp cloud secrets.
  name: Scale AI SGP Cloud Secrets API
  slug: scale-ai-sgp-cloud-secrets-api
- baseURL: https://agentex.sgp.scale.com
  baseurl_source: declared
  description: The Slack API from Scale AI — 3 operation(s) for slack.
  name: Scale AI Slack API
  slug: scale-ai-slack-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Span Assessment API from Scale AI — 2 operation(s) for span assessment.
  name: Scale AI Span Assessment API
  slug: scale-ai-span-assessment-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Spans API from Scale AI — 14 operation(s) for spans.
  name: Scale AI Spans API
  slug: scale-ai-spans-api
- baseURL: https://agentex.sgp.scale.com
  baseurl_source: declared
  description: The States API from Scale AI — 2 operation(s) for states.
  name: Scale AI States API
  slug: scale-ai-states-api
- baseURL: https://api.spellbook.scale.com/llm-engine
  baseurl_source: declared
  description: The Streaming Tasks API from Scale AI — 1 operation(s) for streaming tasks.
  name: Scale AI Streaming Tasks API
  slug: scale-ai-streaming-tasks-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Studio Projects API from Scale AI — 2 operation(s) for studio projects.
  name: Scale AI Studio Projects API
  slug: scale-ai-studio-projects-api
- baseURL: https://api.spellbook.scale.com/llm-engine
  baseurl_source: declared
  description: The Sync Tasks API from Scale AI — 1 operation(s) for sync tasks.
  name: Scale AI Sync Tasks API
  slug: scale-ai-sync-tasks-api
- baseURL: https://agentex.sgp.scale.com
  baseurl_source: declared
  description: The task-retention API from Scale AI — 3 operation(s) for task-retention.
  name: Scale AI Task Retention API
  slug: scale-ai-task-retention-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Training Datasets V3 (Beta) API from Scale AI — 3 operation(s) for training datasets v3 (beta).
  name: Scale AI Training Datasets V3 (Beta) API
  slug: scale-ai-training-datasets-v3-beta-api
- baseURL: https://api.spellbook.scale.com/llm-engine
  baseurl_source: declared
  description: The Triggers API from Scale AI — 2 operation(s) for triggers.
  name: Scale AI Triggers API
  slug: scale-ai-triggers-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: The Users API from Scale AI — 3 operation(s) for users.
  name: Scale AI Users API
  slug: scale-ai-users-api
- baseURL: https://api.egp.scale.com
  baseurl_source: declared
  description: Operations related to vector store creation and management
  name: Scale AI Vector Stores API
  slug: scale-ai-vector-stores-api
- baseURL: https://dex.sgp.scale.com
  baseurl_source: declared
  description: Callbacks from external services
  name: Scale AI Webhooks API
  slug: scale-ai-webhooks-api
- baseURL: https://api.scale.com
  baseurl_source: declared
  description: The Health Check API from Scale AI — 1 operation(s) for health check.
  name: Scale AI Health Check API
  slug: scale-ai-health-check-api
artifact_total: 172
collections:
- collection_type: open
  name: Scale AI REST Batches API
  slug: open-scale-ai-batches-api
- collection_type: open
  name: Scale AI REST Batches Projects API
  slug: open-scale-ai-projects-api
- collection_type: open
  name: Scale AI REST Batches Tasks API
  slug: open-scale-ai-tasks-api
- collection_type: open
  name: Scale AI REST API
  slug: open-scale-ai
common:
- group: other
  href: https://artifacts.apis.io/scale-ai/capabilities/scale-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/scale-ai-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/scale-ai/well-known/scale-ai-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scale-ai-status-security.txt
- group: design
  href: https://artifacts.apis.io/scale-ai/rules/scale-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/scale-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/scale-ai/json-ld/scale-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/scale-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/scale-ai/vocabulary/scale-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/scale-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/scale-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/scale-ai/data-model/scale-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scale-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/scale-ai/conventions/scale-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/scale-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/scale-ai/conventions/scale-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/scale-ai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://scale.com/security
- group: operate
  href: https://artifacts.apis.io/scale-ai/lifecycle/scale-ai-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/scale-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/scale-ai/lifecycle/scale-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/scale-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/scale-ai/errors/scale-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scale-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/scale-ai/conformance/scale-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scale-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/scale-ai/overlays/scale-ai-agentex-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scale-ai-agentex-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/scale-ai/llms/scale-ai-sgp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scale-ai-sgp-llms.txt
- group: agent
  href: https://artifacts.apis.io/scale-ai/llms/scale-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scale-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/scale-ai/a2a/scale-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/scale-ai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/scale-ai/well-known/scale-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scale-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/scale-ai/well-known/scale-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scale-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/scale-ai/hosts/scale-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scale-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/scale-ai/integrations/scale-ai-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/scale-ai-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/scale-ai/vendors/scale-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scale-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/scale-ai/packages/scale-ai-packages.yml
  title: ''
  type: Packages
  url: packages/scale-ai-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://scale.com/pricing
- group: operate
  href: https://artifacts.apis.io/scale-ai/rate-limits/scale-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/scale-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/scale-ai/finops/scale-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/scale-ai-finops.yml
- group: company
  title: ''
  type: Website
  url: https://scale.com/
- group: agent
  href: https://artifacts.apis.io/scale-ai/agentic-access/scale-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/scale-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/scale-ai/security/scale-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/scale-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/scale-ai/security/scale-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/scale-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/scale-ai/security/scale-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scale-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/scale-ai/authentication/scale-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scale-ai-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://scale.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://scale.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api-reference.scale.com
- group: start
  title: ''
  type: GettingStarted
  url: https://api-reference.scale.com/docs/api-reference/introduction-to-scale-api.md
- group: auth
  title: ''
  type: Authentication
  url: https://api-reference.scale.com/docs/api-reference/authentication.md
- group: company
  title: ''
  type: Blog
  url: https://scale.com/blog
- group: start
  title: ''
  type: Login
  url: https://dashboard.scale.com/login
- group: start
  title: ''
  type: Console
  url: https://dashboard.scale.com
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/scaleapi/
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/scaleapi
- group: operate
  title: ''
  type: Support
  url: https://scale.com/docs/customer-support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scaleapi
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scale.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scale.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.scale.com/
- group: auth
  title: ''
  type: Security
  url: https://scale.com/security
- group: company
  title: ''
  type: Twitter
  url: https://x.com/scale_ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scaleai
created: '2026-05-23'
description: Scale AI is the data engine for AI. The company turns raw data into training data by combining ML-powered pre-labeling with multi-tier human review, and ships an extensive REST API and SDKs for managing labeling, evaluation, and generative-AI data pipelines. The product portfolio spans the Scale Data Engine (foundational labeling and review), the GenAI Data Engine (data for foundation-model training and tuning), the Scale GenAI Platform (deployment and orchestration for generative AI), the Automotive Data Engine (LiDAR, sensor fusion, customer dashboards, Nucleus), and Donovan (Scale's defense / public-sector AI product). The REST API lives at api.scale.com/v1, supports live and sandbox modes, and is wrapped by official Python (scaleapi) and JavaScript (scaleapi) SDKs. The company serves enterprise, insurance, healthcare, and U.S. and global public-sector verticals.
features:
- description: Resource-oriented REST API with JSON responses, live and sandbox modes, and versioned v1 endpoints.
  name: REST API at api.scale.com/v1
- description: Create, retrieve, cancel, and tag individual labeling tasks with unique identifiers and metadata.
  name: Tasks API
- description: Create, finalize, prioritize, list, and retrieve status for batches of tasks.
  name: Batches API
- description: Create and manage labeling projects, including taxonomy service management.
  name: Projects API
- description: Image and video, sensor fusion, LiDAR, and multi-stage annotation task types.
  name: Specialized Annotation
- description: RLHF, SFT, evaluation, and red-team data for generative AI foundation models.
  name: GenAI Data Engine
- description: Deployment and orchestration product for enterprise and public-sector generative-AI workflows.
  name: GenAI Platform
- description: Scale's defense and public-sector AI product line.
  name: Donovan
- description: Dataset management for browsing, querying, and curating ML datasets.
  name: Nucleus
- description: Integrates with AWS S3, Azure, and Google Cloud Storage for data ingest and delivery.
  name: Cloud Storage Integration
- description: Asynchronous task completion callbacks and secure result URLs.
  name: Callbacks
finops:
- has_sources: false
  method: generated
  name: Scale Ai Finops
  primary_unit: ''
  service_category: API
  slug: scale-ai-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scale-ai.png
integrations:
- description: Cloud storage ingest and delivery for labeling jobs.
  name: AWS S3, Azure Blob, Google Cloud Storage
- description: Official Python client published on PyPI.
  name: Python SDK (scaleapi)
- description: Official Node.js client published on npm.
  name: JavaScript SDK (scaleapi)
- description: Test integrations safely against a sandbox environment that mirrors live behavior.
  name: Sandbox Mode
json_schemas:
- name: AgentRunScheduleResponse
  property_count: 23
  slug: scale-ai-agent-run-schedule-response
- name: ChatCompletionRequest
  property_count: 29
  slug: scale-ai-chat-completion-request
- name: ChatCompletionV2Request
  property_count: 58
  slug: scale-ai-chat-completion-v2-request
- name: CompletionRequestV2
  property_count: 15
  slug: scale-ai-completion-request-v2
- name: CompletionV2Request
  property_count: 38
  slug: scale-ai-completion-v2-request
- name: CreateAgentRunScheduleRequest
  property_count: 11
  slug: scale-ai-create-agent-run-schedule-request
- name: CreateBatchCompletionsV1Request
  property_count: 15
  slug: scale-ai-create-batch-completions-v1-request
- name: CreateBatchCompletionsV2Request
  property_count: 15
  slug: scale-ai-create-batch-completions-v2-request
- name: CreateChatCompletionRequest
  property_count: 8
  slug: scale-ai-create-chat-completion-request
- name: CreateModelEndpointV1Request
  property_count: 26
  slug: scale-ai-create-model-endpoint-v1-request
- name: CreateSpanRequest
  property_count: 10
  slug: scale-ai-create-span-request
- name: DataSourceEntity
  property_count: 16
  slug: scale-ai-data-source-entity
- name: DeleteResponse
  property_count: 2
  slug: scale-ai-delete-response
- name: ChatCompletionRequest
  property_count: 29
  slug: scale-ai-egp-api-backend-server-api-apps-public-routers-inference-inference-model-models-chat-completion-request
- name: ChatCompletionRequest
  property_count: 16
  slug: scale-ai-egp-api-backend-server-utils-model-schemas-completions-chat-completion-request
- name: ExecuteAgentRequest
  property_count: 6
  slug: scale-ai-execute-agent-request
- name: FileEntity
  property_count: 17
  slug: scale-ai-file-entity
- name: JobEntity
  property_count: 14
  slug: scale-ai-job-entity
- name: LegacyEvaluationResponseWithViews
  property_count: 24
  slug: scale-ai-legacy-evaluation-response-with-views
- name: MaybePaginatedListResponse[ProjectEntity]
  property_count: 0
  slug: scale-ai-maybe-paginated-list-response-project-entity
- name: ParseResultEntity
  property_count: 12
  slug: scale-ai-parse-result-entity
- name: ProjectCreateRequest
  property_count: 2
  slug: scale-ai-project-create-request
- name: ProjectEntity
  property_count: 7
  slug: scale-ai-project-entity
- name: ProjectUpdateRequest
  property_count: 3
  slug: scale-ai-project-update-request
- name: RegisterAgentResponse
  property_count: 13
  slug: scale-ai-register-agent-response
- name: ResearchJobRequest
  property_count: 8
  slug: scale-ai-research-job-request
- name: ResponseObject
  property_count: 32
  slug: scale-ai-response-object
- name: ResponseRequest
  property_count: 17
  slug: scale-ai-response-request
- name: SGPVectorStoreCreateRequestBase
  property_count: 5
  slug: scale-ai-sgpvector-store-create-request-base
- name: Span
  property_count: 10
  slug: scale-ai-span
- name: SpansBySpanMetricsRequest
  property_count: 22
  slug: scale-ai-spans-by-span-metrics-request
- name: SpansExportRequest
  property_count: 23
  slug: scale-ai-spans-export-request
- name: SpansMetricsRequest
  property_count: 21
  slug: scale-ai-spans-metrics-request
- name: TaskResponse
  property_count: 10
  slug: scale-ai-task-response
- name: Task
  property_count: 9
  slug: scale-ai-task
- name: TaskStatusReasonRequest
  property_count: 1
  slug: scale-ai-task-status-reason-request
- name: TaskSummary
  property_count: 9
  slug: scale-ai-task-summary
- name: UpdateAgentRunScheduleRequest
  property_count: 11
  slug: scale-ai-update-agent-run-schedule-request
- name: UpdateModelEndpointV1Request
  property_count: 23
  slug: scale-ai-update-model-endpoint-v1-request
- name: UpdateTaskRequest
  property_count: 2
  slug: scale-ai-update-task-request
jsonld:
- class_count: 120
  name: Scale Ai Context
  property_count: 183
  slug: scale-ai-context
layout: provider
modified: '2026-10-27'
name: Scale AI
nav: Providers
network: true
overview: 'Scale AI publishes 94 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batches API, Projects API, Tasks API, and 91 more. Tagged areas include Data Engine, Labeling, RLHF, GenAI Platform, and Donovan.


  The Scale AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Scale AI''s developer surface includes pricing, authentication, developer portal, documentation, API reference, getting-started guide, engineering blog, and 44 more developer resources.'
plans:
- name: Scale Ai Plans Pricing
  plan_count: 0
  slug: scale-ai-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Scale Ai Rate Limits
  slug: scale-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Scale AI API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 4
  slug: scale-ai-rules
scopes:
- name: Scale Ai Scopes
  scope_count: 0
  slug: scale-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.0
  coverage:
    artifact_dirs: 37
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 62.9
    developer_ergonomics: 63.7
    discoverability: 69.6
    operational_transparency: 55.3
  previous_composite: 69.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 59.1
      derived: 0
      marker_coverage: 0.0
      total: 89
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/scale-ai/scale-ai-2026-06-20T193601.png
security:
- kind: authentication
  name: Scale Ai Authentication
  slug: scale-ai-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Scale Ai Domain Security
  slug: scale-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Scale Ai Vulnerability Disclosure
  slug: scale-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Scale Ai Trust Center
  slug: scale-ai-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP
skill_count: 3
skills:
- name: scale-ai-manage-tasks
  slug: scale-ai-manage-tasks
- name: scale-ai-set-up-project
  slug: scale-ai-set-up-project
- name: scale-ai-submit-labeling-batch
  slug: scale-ai-submit-labeling-batch
slug: scale-ai
tags:
- Data Engine
- Labeling
- RLHF
- GenAI Platform
- Donovan
- Defense AI
- LiDAR
- Sensor Fusion
- REST API
use_cases:
- description: RLHF, SFT, evaluation, and red-team datasets for frontier model labs.
  name: Foundation Model Training Data
- description: LiDAR, camera, and sensor-fusion labeling for AV programs.
  name: Autonomous Vehicle Data
- description: Build and deploy generative-AI applications on the GenAI Platform.
  name: Enterprise GenAI Deployment
- description: Deliver Donovan-based analytic and decision-support workflows to defense and government customers.
  name: Public Sector Decision Support
- description: Browse, query, and curate ML datasets at scale with Nucleus.
  name: Dataset Curation
website: https://scale.com/
---
