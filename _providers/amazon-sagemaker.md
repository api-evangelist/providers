---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Amazon Sagemaker Agentic Access
  operation_count: 13
  slug: amazon-sagemaker-agentic-access
  summary_line: 13 operations · 13 acting
api_count: 9
apis:
- description: The Amazon SageMaker AI runtime API for invoking deployed model endpoints to get real-time inference predictions.
  name: Amazon SageMaker Runtime API
  slug: amazon-sagemaker-runtime-api
- description: Data plane API operations for the Amazon SageMaker Feature Store supporting put, delete, and retrieve operations for ML features.
  name: Amazon SageMaker Feature Store Runtime API
  slug: amazon-sagemaker-feature-store-runtime-api
- description: Data plane API operations for Amazon SageMaker Metrics for putting and retrieving metrics related to training runs.
  name: Amazon SageMaker Metrics Service API
  slug: amazon-sagemaker-metrics-service-api
- description: APIs for creating and managing Amazon SageMaker geospatial capabilities including earth observation jobs and vector enrichment jobs.
  name: Amazon SageMaker Geospatial API
  slug: amazon-sagemaker-geospatial-api
- description: SageMaker Edge Manager dataplane service for communicating with active edge agents running ML models on edge devices.
  name: Amazon SageMaker Edge Manager API
  slug: amazon-sagemaker-edge-manager-api
- description: Operations for managing SageMaker endpoints.
  name: Amazon SageMaker Endpoints API
  slug: amazon-sagemaker-endpoints-api
- description: Operations for managing SageMaker models.
  name: Amazon SageMaker Models API
  slug: amazon-sagemaker-models-api
- description: Operations for managing SageMaker notebook instances.
  name: Amazon SageMaker Notebook Instances API
  slug: amazon-sagemaker-notebook-instances-api
- description: Operations for managing SageMaker training jobs.
  name: Amazon SageMaker Training Jobs API
  slug: amazon-sagemaker-training-jobs-api
arazzos:
- description: List hosted endpoints and describe the most recently created one in detail.
  name: Amazon SageMaker Audit Endpoint Fleet
  slug: amazon-sagemaker-audit-endpoint-fleet-workflow
- description: Verify an existing model, build an endpoint configuration for it, create an endpoint, and poll it to service.
  name: Amazon SageMaker Deploy Existing Model
  slug: amazon-sagemaker-deploy-existing-model-workflow
- description: Create a model, build an endpoint configuration, launch an endpoint, and poll it until it is in service.
  name: Amazon SageMaker Deploy Model to Endpoint
  slug: amazon-sagemaker-deploy-model-to-endpoint-workflow
- description: List registered models and describe the most recently created one in detail.
  name: Amazon SageMaker Inventory Models
  slug: amazon-sagemaker-inventory-models-workflow
- description: Create a SageMaker notebook instance and poll it until it is in service.
  name: Amazon SageMaker Provision Notebook Instance
  slug: amazon-sagemaker-provision-notebook-instance-workflow
- description: Find the most recent completed training job, read its artifacts, and register a model from them.
  name: Amazon SageMaker Register Latest Completed Training
  slug: amazon-sagemaker-register-latest-completed-training-workflow
- description: Start a SageMaker training job and poll its status until it reaches a terminal state.
  name: Amazon SageMaker Train Model and Poll Job
  slug: amazon-sagemaker-train-and-poll-job-workflow
- description: Train a model to completion, then register it from the produced artifacts and stand up a hosted endpoint.
  name: Amazon SageMaker Train Then Deploy
  slug: amazon-sagemaker-train-then-deploy-workflow
artifact_total: 87
collections:
- collection_type: postman
  name: Amazon SageMaker API
  slug: postman-amazon-sagemaker
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon SageMaker Endpoints API
  slug: open-amazon-sagemaker-endpoints-api
- collection_type: open
  name: Amazon SageMaker Endpoints Models API
  slug: open-amazon-sagemaker-models-api
- collection_type: open
  name: Amazon SageMaker Endpoints Notebook Instances API
  slug: open-amazon-sagemaker-notebook-instances-api
- collection_type: open
  name: Amazon SageMaker Endpoints Training Jobs API
  slug: open-amazon-sagemaker-training-jobs-api
- collection_type: open
  name: Amazon SageMaker API
  slug: open-amazon-sagemaker
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/aws/sagemaker-core/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/aws/sagemaker-core/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/aws/.github/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/aws/sagemaker-core/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/aws/sagemaker-core/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-sagemaker-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-sagemaker-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-sagemaker-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-sagemaker-domain-security.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-sagemaker/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-sagemaker-audit-endpoint-fleet-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-sagemaker-deploy-existing-model-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-sagemaker-deploy-model-to-endpoint-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-sagemaker-inventory-models-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-sagemaker-provision-notebook-instance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-sagemaker-register-latest-completed-training-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-sagemaker-train-and-poll-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-sagemaker-train-then-deploy-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/sagemaker/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/sagemaker/latest/dg/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/sagemaker/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/sagemaker/pricing/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/sagemaker/faqs/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/machine-learning/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: auth
  title: ''
  type: Security
  url: https://docs.aws.amazon.com/sagemaker/latest/dg/security.html
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-sagemaker
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: build
  title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/sagemaker/
- group: build
  title: SageMaker HyperPod CLI
  type: CLI
  url: https://github.com/aws/sagemaker-hyperpod-cli
- group: build
  title: Python SDK (GitHub)
  type: SDKs
  url: https://github.com/aws/sagemaker-python-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/aws/sagemaker-core
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/aws/sagemaker-distribution
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-sagemaker-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-sagemaker-vocabulary.yaml
- group: learn
  title: ''
  type: Training
  url: https://aws.amazon.com/training/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-sagemaker-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-sagemaker-tag-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-sagemaker-endpoint-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-sagemaker-model-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-sagemaker-notebook-instance-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-sagemaker-tag-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-sagemaker-training-job-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-sagemaker-endpoint-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-sagemaker-model-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-sagemaker-notebook-instance-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-sagemaker-tag-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-sagemaker-training-job-example.json
created: '2024-01-01'
description: Amazon SageMaker is a fully managed machine learning platform that enables developers and data scientists to build, train, and deploy machine learning models at scale. SageMaker removes the heavy lifting from each step of the machine learning process, providing built-in algorithms, managed Jupyter notebooks, distributed training, automatic model tuning, and one-click deployment to production endpoints with auto-scaling.
examples:
- key_count: 6
  name: Amazon Sagemaker Createendpoint Example
  slug: amazon-sagemaker-createendpoint-example
- key_count: 6
  name: Amazon Sagemaker Createendpointconfig Example
  slug: amazon-sagemaker-createendpointconfig-example
- key_count: 6
  name: Amazon Sagemaker Createmodel Example
  slug: amazon-sagemaker-createmodel-example
- key_count: 6
  name: Amazon Sagemaker Createnotebookinstance Example
  slug: amazon-sagemaker-createnotebookinstance-example
- key_count: 6
  name: Amazon Sagemaker Createtrainingjob Example
  slug: amazon-sagemaker-createtrainingjob-example
- key_count: 6
  name: Amazon Sagemaker Describeendpoint Example
  slug: amazon-sagemaker-describeendpoint-example
- key_count: 6
  name: Amazon Sagemaker Describemodel Example
  slug: amazon-sagemaker-describemodel-example
- key_count: 6
  name: Amazon Sagemaker Describenotebookinstance Example
  slug: amazon-sagemaker-describenotebookinstance-example
- key_count: 6
  name: Amazon Sagemaker Describetrainingjob Example
  slug: amazon-sagemaker-describetrainingjob-example
- key_count: 8
  name: Amazon Sagemaker Endpoint Example
  slug: amazon-sagemaker-endpoint-example
- key_count: 6
  name: Amazon Sagemaker Listendpoints Example
  slug: amazon-sagemaker-listendpoints-example
- key_count: 6
  name: Amazon Sagemaker Listmodels Example
  slug: amazon-sagemaker-listmodels-example
- key_count: 6
  name: Amazon Sagemaker Listnotebookinstances Example
  slug: amazon-sagemaker-listnotebookinstances-example
- key_count: 6
  name: Amazon Sagemaker Listtrainingjobs Example
  slug: amazon-sagemaker-listtrainingjobs-example
- key_count: 5
  name: Amazon Sagemaker Model Example
  slug: amazon-sagemaker-model-example
- key_count: 11
  name: Amazon Sagemaker Notebook Instance Example
  slug: amazon-sagemaker-notebook-instance-example
- key_count: 2
  name: Amazon Sagemaker Tag Example
  slug: amazon-sagemaker-tag-example
- key_count: 18
  name: Amazon Sagemaker Training Job Example
  slug: amazon-sagemaker-training-job-example
features:
- description: Fully integrated development environment for ML work with notebooks, debugging, and experiment tracking.
  name: SageMaker Studio
- description: Purpose-built infrastructure for distributed training that reduces foundation model training time by up to 40%.
  name: SageMaker HyperPod
- description: Hub providing access to foundation models, pre-built algorithms, and one-click deployment.
  name: SageMaker JumpStart
- description: Automated model creation with complete visibility and transparency.
  name: SageMaker Autopilot
- description: No-code visual interface for creating ML models without writing code.
  name: SageMaker Canvas
- description: Store, share, and manage features for machine learning models.
  name: SageMaker Feature Store
- description: Data preparation tool that reduces transformation workflow time significantly.
  name: SageMaker Data Wrangler
- description: Incorporates human feedback throughout the ML lifecycle for data labeling.
  name: SageMaker Ground Truth
- description: Purpose-built CI/CD service for machine learning workflows.
  name: SageMaker Pipelines
- description: Automatically detects concept drift and data quality issues in deployed models.
  name: SageMaker Model Monitor
- description: Provides machine learning explainability and bias detection.
  name: SageMaker Clarify
- description: Streamlines tracking and management of ML experiments.
  name: SageMaker Experiments
- description: Access controls and transparency across the full ML lifecycle with audit trails.
  name: ML Governance
finops:
- name: Amazon Sagemaker Finops
  service_category: AI / Machine Learning
  slug: amazon-sagemaker-finops
graphqls:
- description: 'This GraphQL schema provides a conceptual graph representation of the [Amazon SageMaker REST API](https://docs.aws.amazon.com/sagemaker/latest/APIReference/). SageMaker is a fully managed ML platform '
  name: Amazon SageMaker GraphQL Schema
  slug: amazon-sagemaker-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-sagemaker.png
json_schemas:
- name: Endpoint
  property_count: 8
  slug: amazon-sagemaker-endpoint
- name: Model
  property_count: 5
  slug: amazon-sagemaker-model
- name: NotebookInstance
  property_count: 11
  slug: amazon-sagemaker-notebook-instance
- name: NotebookInstance
  property_count: 11
  slug: amazon-sagemaker-notebookinstance
- name: Tag
  property_count: 2
  slug: amazon-sagemaker-tag
- name: TrainingJob
  property_count: 18
  slug: amazon-sagemaker-training-job
- name: TrainingJob
  property_count: 18
  slug: amazon-sagemaker-trainingjob
json_structures:
- name: Amazon Sagemaker Endpoint Structure
  property_count: 8
  slug: amazon-sagemaker-endpoint-structure
- name: Amazon Sagemaker Model Structure
  property_count: 5
  slug: amazon-sagemaker-model-structure
- name: Amazon Sagemaker Notebook Instance Structure
  property_count: 11
  slug: amazon-sagemaker-notebook-instance-structure
- name: Amazon Sagemaker Structure
  property_count: 0
  slug: amazon-sagemaker-structure
- name: Amazon Sagemaker Tag Structure
  property_count: 2
  slug: amazon-sagemaker-tag-structure
- name: Amazon Sagemaker Training Job Structure
  property_count: 18
  slug: amazon-sagemaker-training-job-structure
jsonld:
- class_count: 5
  name: Amazon Sagemaker Context
  property_count: 49
  slug: amazon-sagemaker-context
layout: provider
modified: '2026-05-19'
name: Amazon SageMaker
nav: Providers
network: true
overview: 'Amazon SageMaker publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Endpoints API, Models API, Notebook Instances API, and 1 more. Tagged areas include Artificial Intelligence, Inference, Machine-Learning, MLOps, and Training.


  The Amazon SageMaker catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon SageMaker''s developer surface includes developer portal, getting-started guide, documentation, API reference, developer console, signup flow, pricing, and 50 more developer resources.'
plans:
- name: Amazon Sagemaker Plans Pricing
  plan_count: 3
  slug: amazon-sagemaker-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Amazon Sagemaker Rate Limits
  slug: amazon-sagemaker-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon SageMaker API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-sagemaker-jsonschema-spectral-rules
- effective_rule_count: 67
  extends:
  - spectral:oas
  name: Amazon SageMaker API Rules
  rule_count: 26
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 14
  slug: amazon-sagemaker-spectral-rules
score:
  band: strong
  composite: 64.9
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 28.8
    contract_quality: 69.8
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 52.6
  previous_composite: 64.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-sagemaker/refs/heads/main/screenshots/amazon-sagemaker-2026-06-20T171815.png
security:
- kind: domain-security
  name: Amazon Sagemaker Domain Security
  slug: amazon-sagemaker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Sagemaker Vulnerability Disclosure
  slug: amazon-sagemaker-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Sagemaker Trust Center
  slug: amazon-sagemaker-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-sagemaker
tags:
- Artificial Intelligence
- Inference
- Machine-Learning
- MLOps
- Training
use_cases:
- description: Build custom generative AI applications using proprietary data with foundation model fine-tuning.
  name: Generative AI Applications
- description: Train and deploy ML models across the entire machine learning lifecycle from exploration to production.
  name: ML Model Development
- description: Query and analyze data across unified sources with built-in SQL analytics and data processing.
  name: Data Analytics
- description: Manage data and AI artifacts with fine-grained security controls and compliance tooling.
  name: Enterprise AI Governance
- description: Build and deploy computer vision models for image classification, object detection, and segmentation.
  name: Computer Vision
- description: Train and deploy NLP models for text classification, entity recognition, and language generation.
  name: Natural Language Processing
- description: Build real-time fraud detection models with low-latency inference endpoints.
  name: Fraud Detection
- description: Deploy ML models on edge devices for predictive maintenance use cases.
  name: Predictive Maintenance
website: https://aws.amazon.com/
---
