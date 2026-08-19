---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Replicate Agentic Access
  operation_count: 27
  slug: replicate-agentic-access
  summary_line: 27 operations · 12 acting
api_count: 16
apis:
- description: The Accounts API from Replicate — 1 operation(s) for accounts.
  name: Replicate Accounts API
  slug: replicate-accounts-api
- description: The Cancel API from Replicate — 2 operation(s) for cancel.
  name: Replicate Cancel API
  slug: replicate-cancel-api
- description: The Collections API from Replicate — 2 operation(s) for collections.
  name: Replicate Collections API
  slug: replicate-collections-api
- description: The Deployments API from Replicate — 3 operation(s) for deployments.
  name: Replicate Deployments API
  slug: replicate-deployments-api
- description: The Hardware API from Replicate — 1 operation(s) for hardware.
  name: Replicate Hardware API
  slug: replicate-hardware-api
- description: The Model API from Replicate — 5 operation(s) for model.
  name: Replicate Model API
  slug: replicate-model-api
- description: The Models API from Replicate — 1 operation(s) for models.
  name: Replicate Models API
  slug: replicate-models-api
- description: The Name API from Replicate — 7 operation(s) for name.
  name: Replicate Name API
  slug: replicate-name-api
- description: The Owner API from Replicate — 7 operation(s) for owner.
  name: Replicate Owner API
  slug: replicate-owner-api
- description: The Predictions API from Replicate — 5 operation(s) for predictions.
  name: Replicate Predictions API
  slug: replicate-predictions-api
- description: The Secrets API from Replicate — 1 operation(s) for secrets.
  name: Replicate Secrets API
  slug: replicate-secrets-api
- description: The Slug API from Replicate — 1 operation(s) for slug.
  name: Replicate Slug API
  slug: replicate-slug-api
- description: The Training API from Replicate — 2 operation(s) for training.
  name: Replicate Training API
  slug: replicate-training-api
- description: The Trainings API from Replicate — 1 operation(s) for trainings.
  name: Replicate Trainings API
  slug: replicate-trainings-api
- description: The Version API from Replicate — 2 operation(s) for version.
  name: Replicate Version API
  slug: replicate-version-api
- description: The Webhooks API from Replicate — 1 operation(s) for webhooks.
  name: Replicate Webhooks API
  slug: replicate-webhooks-api
arazzos:
- description: Read a curated collection, confirm a chosen model, run its latest version, and poll the prediction.
  name: Replicate Pick a Model from a Collection and Predict
  slug: replicate-collection-predict-workflow
- description: Pick hardware, create a deployment for a model version, then run a prediction via the deployment.
  name: Replicate Create a Deployment and Run a Prediction Through It
  slug: replicate-deploy-and-predict-workflow
- description: Look up a model, pick its latest version, run a prediction, and poll to completion.
  name: Replicate Resolve Latest Version and Predict
  slug: replicate-model-version-predict-workflow
- description: Run a prediction against an official model by name, then poll until complete.
  name: Replicate Run an Official Model and Poll
  slug: replicate-official-model-predict-workflow
- description: Run a model version, then poll the prediction until it reaches a terminal state.
  name: Replicate Create Prediction and Poll Until Complete
  slug: replicate-predict-and-poll-workflow
- description: Create a prediction, poll a bounded number of times, and cancel it if it has not finished.
  name: Replicate Run a Prediction with Bounded Wait and Cancel
  slug: replicate-predict-with-timeout-cancel-workflow
- description: Read a deployment, update its version and instance bounds, then run a prediction through it.
  name: Replicate Scale a Deployment and Run a Prediction
  slug: replicate-scale-deployment-and-predict-workflow
- description: Search public models by query, run a prediction on the top match's latest version, and poll it.
  name: Replicate Search for a Model and Run a Prediction
  slug: replicate-search-model-and-predict-workflow
- description: Start a fine-tuning run from a base model version, then poll until the training finishes.
  name: Replicate Start a Training and Poll Until Complete
  slug: replicate-train-model-and-poll-workflow
- description: Retrieve the default webhook signing secret, then create a prediction that posts to a webhook.
  name: Replicate Fetch Webhook Secret and Run a Webhook Prediction
  slug: replicate-webhook-secured-predict-workflow
artifact_total: 90
asyncapis:
- description: 'AsyncAPI definition for Replicate''s event-driven surfaces: - Server-Sent Events (SSE) stream returned for predictions where the model supports streaming output. The stream URL is published by the Pred'
  name: Replicate Streaming and Webhooks API
  slug: replicate-asyncapi
collections:
- collection_type: postman
  name: Replicate
  slug: postman-replicate
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Replicate Accounts API
  slug: open-replicate-accounts-api
- collection_type: open
  name: Replicate Accounts Cancel API
  slug: open-replicate-cancel-api
- collection_type: open
  name: Replicate Accounts Collections API
  slug: open-replicate-collections-api
- collection_type: open
  name: Replicate Accounts Deployments API
  slug: open-replicate-deployments-api
- collection_type: open
  name: Replicate Accounts Hardware API
  slug: open-replicate-hardware-api
- collection_type: open
  name: Replicate Accounts Model API
  slug: open-replicate-model-api
- collection_type: open
  name: Replicate Accounts Models API
  slug: open-replicate-models-api
- collection_type: open
  name: Replicate Accounts Name API
  slug: open-replicate-name-api
- collection_type: open
  name: Replicate Accounts Owner API
  slug: open-replicate-owner-api
- collection_type: open
  name: Replicate Accounts Predictions API
  slug: open-replicate-predictions-api
- collection_type: open
  name: Replicate Accounts Secrets API
  slug: open-replicate-secrets-api
- collection_type: open
  name: Replicate Accounts Slug API
  slug: open-replicate-slug-api
- collection_type: open
  name: Replicate Accounts Training API
  slug: open-replicate-training-api
- collection_type: open
  name: Replicate Accounts Trainings API
  slug: open-replicate-trainings-api
- collection_type: open
  name: Replicate Accounts Version API
  slug: open-replicate-version-api
- collection_type: open
  name: Replicate Accounts Webhooks API
  slug: open-replicate-webhooks-api
- collection_type: open
  name: Replicate
  slug: open-replicate
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/replicate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/replicate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/replicate-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/replicate/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/replicate-collection-predict-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/replicate-deploy-and-predict-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/replicate-model-version-predict-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/replicate-official-model-predict-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/replicate-predict-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/replicate-predict-with-timeout-cancel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/replicate-scale-deployment-and-predict-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/replicate-search-model-and-predict-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/replicate-train-model-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/replicate-webhook-secured-predict-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/replicate
- group: company
  title: ''
  type: Website
  url: https://replicate.com
- group: docs
  title: ''
  type: Documentation
  url: https://replicate.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://replicate.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://replicate.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://replicate.com/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://replicate.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://replicate.com/privacy
- group: start
  title: ''
  type: Signup
  url: https://replicate.com/signin?next=/docs
- group: start
  title: ''
  type: Login
  url: https://replicate.com/signin
- group: other
  title: ''
  type: Playground
  url: https://replicate.com/explore
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/replicate
- group: build
  title: ''
  type: SDKs
  url: https://replicate.com/docs/reference/client-libraries
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/replicate/replicate-python
- group: build
  title: ''
  type: Node.js SDK
  url: https://github.com/replicate/replicate-javascript
- group: build
  title: ''
  type: Go SDK
  url: https://github.com/replicate/replicate-go
- group: build
  title: ''
  type: Swift SDK
  url: https://github.com/replicate/replicate-swift
- group: other
  title: ''
  type: Cog
  url: https://github.com/replicate/cog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.replicate.com
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/replicate/replicate-mcp-code-mode
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/replicate/skills
- group: agent
  title: ''
  type: LlmsText
  url: https://replicate.com/llms.txt
created: '2024-11-13'
description: Replicate lets you run machine learning models in the cloud with a simple API. Thousands of open-source models are available, and you can run your own custom models at scale. Run image generation, language models, audio synthesis, video generation, and more with a few lines of code. Replicate makes AI accessible to every software engineer.
examples:
- key_count: 4
  name: Replicate Create Prediction Example
  slug: replicate-create-prediction-example
- key_count: 4
  name: Replicate List Models Example
  slug: replicate-list-models-example
features:
- T4 GPU at $0.000225/sec (cheapest)
- L40S GPU at $0.000975/sec
- A100 80GB at $0.00140/sec
- H100 at $0.001525/sec (highest performance)
- Pay only for execution time (per second)
- Default 10 predictions/sec; can be raised to 100 on paid
- 'Other endpoints: 60 req/sec'
- Public model library with thousands of models
- Cog framework for packaging your own models
- Deployments for low-latency inference (charges idle time)
- Webhooks for prediction completion
- OAuth 2.0 and API tokens
- Streaming output for LLM models
- Files input via signed URLs
- Training service for fine-tuning
- Trainings billed at hardware rate
finops:
- name: Replicate Finops
  service_category: ML Inference
  slug: replicate-finops
graphqls:
- description: Replicate does not currently expose a public GraphQL endpoint. The platform's primary API is a REST HTTP API available at `https://api.replicate.com/v1`. This GraphQL schema is a conceptual representa
  name: Replicate GraphQL
  slug: replicate-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/replicate.png
json_schemas:
- name: Replicate Model
  property_count: 14
  slug: replicate-model
- name: Replicate Prediction
  property_count: 16
  slug: replicate-prediction
- name: schemas_prediction_request
  property_count: 4
  slug: replicate-schemas-prediction-request
- name: schemas_training_request
  property_count: 4
  slug: replicate-schemas-training-request
- name: schemas_version_prediction_request
  property_count: 5
  slug: replicate-schemas-version-prediction-request
json_structures:
- name: Replicate Prediction Structure
  property_count: 0
  slug: replicate-prediction-structure
- name: Replicate Structure
  property_count: 0
  slug: replicate-structure
jsonld:
- class_count: 2
  name: Replicate Context
  property_count: 32
  slug: replicate-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-29'
name: Replicate
nav: Providers
network: true
overview: 'Replicate publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Cancel API, Collections API, and 13 more. Tagged areas include Artificial Intelligence, Machine Learning, Image Generation, Language Models, and Model Deployment.


  The Replicate catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Replicate''s developer surface includes authentication, documentation, pricing, engineering blog, changelog, signup flow, and 30 more developer resources.'
plans:
- name: Replicate Plans Pricing
  plan_count: 4
  slug: replicate-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 4
  name: Replicate Rate Limits
  slug: replicate-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Replicate API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: replicate-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Replicate API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: replicate-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Replicate API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 2
    info: 0
    warn: 6
  slug: replicate-rules
score:
  band: strong
  composite: 54.4
  delta: -7.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 11.4
    contract_quality: 73.6
    developer_ergonomics: 56.0
    discoverability: 72.2
    governance: 11.4
    operational_transparency: 42.1
  previous_composite: 61.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/replicate/refs/heads/main/screenshots/replicate-2026-06-20T192926.png
security:
- kind: authentication
  name: Replicate Authentication
  slug: replicate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Replicate Domain Security
  slug: replicate-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 7
skills:
- name: build-models
  slug: build-models
- name: compare-models
  slug: compare-models
- name: find-models
  slug: find-models
- name: prompt-images
  slug: prompt-images
- name: prompt-videos
  slug: prompt-videos
- name: publish-models
  slug: publish-models
- name: run-models
  slug: run-models
slug: replicate
tags:
- Artificial Intelligence
- Machine Learning
- Image Generation
- Language Models
- Model Deployment
website: https://replicate.com
---
