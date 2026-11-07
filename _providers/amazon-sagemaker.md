---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Amazon Sagemaker Agentic Access
  operation_count: 13
  slug: amazon-sagemaker-agentic-access
  summary_line: 13 operations · 9 acting
api_count: 1
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
- baseURL: https://api.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: Operations for managing SageMaker endpoints.
  name: Amazon SageMaker Endpoints API
  phrasing_intents:
  - id: CreateEndpoint
    intent: Deploy a model to a live hosting endpoint
    question: How do I put a trained model behind a live SageMaker endpoint for real-time predictions?
  - id: DescribeEndpoint
    intent: Check the details and status of one endpoint
    question: Is my inference endpoint finished provisioning and ready to take traffic?
  - id: ListEndpoints
    intent: List hosting endpoints in the account
    question: Which inference endpoints do I have running in my account right now?
  phrasing_ops: 3
  slug: amazon-sagemaker-endpoints-api
- baseURL: https://api.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: Operations for managing SageMaker models.
  name: Amazon SageMaker Models API
  phrasing_intents:
  - id: CreateModel
    intent: Register a model with its inference container
    question: How do I register my model artifacts and inference code so SageMaker can host them?
  - id: DescribeModel
    intent: Look up one registered model
    question: What container image and execution role is a given model set up with?
  - id: ListModels
    intent: List registered models
    question: Which models have I registered in SageMaker so far?
  phrasing_ops: 3
  slug: amazon-sagemaker-models-api
- baseURL: https://api.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: Operations for managing SageMaker notebook instances.
  name: Amazon SageMaker Notebook Instances API
  phrasing_intents:
  - id: CreateNotebookInstance
    intent: Launch a Jupyter notebook instance
    question: How do I spin up a hosted Jupyter notebook in SageMaker for exploring data?
  - id: DescribeNotebookInstance
    intent: Get the status and settings of one notebook
    question: Is my Jupyter notebook instance running or stopped right now?
  - id: ListNotebookInstances
    intent: List notebook instances in the account
    question: Which Jupyter notebook instances exist in my account?
  phrasing_ops: 3
  slug: amazon-sagemaker-notebook-instances-api
- baseURL: https://api.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: Operations for managing SageMaker training jobs.
  name: Amazon SageMaker Training Jobs API
  phrasing_intents:
  - id: CreateTrainingJob
    intent: Start a model training job
    question: How do I kick off training a model on my own data in SageMaker?
  - id: DescribeTrainingJob
    intent: Check the progress of one training job
    question: Has my training job finished, and did it succeed or fail?
  - id: ListTrainingJobs
    intent: List training jobs
    question: Which training jobs have I run recently?
  phrasing_ops: 3
  slug: amazon-sagemaker-training-jobs-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Action API from Amazon SageMaker — 5 operation(s) for sagemaker action.
  name: Amazon SageMaker Sagemaker Action API
  slug: amazon-sagemaker-action-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Ai Benchmark Job API from Amazon SageMaker — 5 operation(s) for sagemaker ai benchmark job.
  name: Amazon SageMaker Sagemaker Ai Benchmark Job API
  slug: amazon-sagemaker-ai-benchmark-job-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Ai Recommendation Job API from Amazon SageMaker — 5 operation(s) for sagemaker ai recommendation job.
  name: Amazon SageMaker Sagemaker Ai Recommendation Job API
  slug: amazon-sagemaker-ai-recommendation-job-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Ai Workload Config API from Amazon SageMaker — 4 operation(s) for sagemaker ai workload config.
  name: Amazon SageMaker Sagemaker Ai Workload Config API
  slug: amazon-sagemaker-ai-workload-config-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Algorithm API from Amazon SageMaker — 4 operation(s) for sagemaker algorithm.
  name: Amazon SageMaker Sagemaker Algorithm API
  slug: amazon-sagemaker-algorithm-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker App API from Amazon SageMaker — 4 operation(s) for sagemaker app.
  name: Amazon SageMaker Sagemaker App API
  slug: amazon-sagemaker-app-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker App Image Config API from Amazon SageMaker — 5 operation(s) for sagemaker app image config.
  name: Amazon SageMaker Sagemaker App Image Config API
  slug: amazon-sagemaker-app-image-config-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Artifact API from Amazon SageMaker — 5 operation(s) for sagemaker artifact.
  name: Amazon SageMaker Sagemaker Artifact API
  slug: amazon-sagemaker-artifact-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Association API from Amazon SageMaker — 3 operation(s) for sagemaker association.
  name: Amazon SageMaker Sagemaker Association API
  slug: amazon-sagemaker-association-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Auto Ml Job API from Amazon SageMaker — 4 operation(s) for sagemaker auto ml job.
  name: Amazon SageMaker Sagemaker Auto Ml Job API
  slug: amazon-sagemaker-auto-ml-job-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Cluster API from Amazon SageMaker — 5 operation(s) for sagemaker cluster.
  name: Amazon SageMaker Sagemaker Cluster API
  slug: amazon-sagemaker-cluster-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Cluster Node API from Amazon SageMaker — 4 operation(s) for sagemaker cluster node.
  name: Amazon SageMaker Sagemaker Cluster Node API
  slug: amazon-sagemaker-cluster-node-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Cluster Scheduler Config API from Amazon SageMaker — 5 operation(s) for sagemaker cluster scheduler config.
  name: Amazon SageMaker Sagemaker Cluster Scheduler Config API
  slug: amazon-sagemaker-cluster-scheduler-config-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Code Repository API from Amazon SageMaker — 5 operation(s) for sagemaker code repository.
  name: Amazon SageMaker Sagemaker Code Repository API
  slug: amazon-sagemaker-code-repository-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Compilation Job API from Amazon SageMaker — 5 operation(s) for sagemaker compilation job.
  name: Amazon SageMaker Sagemaker Compilation Job API
  slug: amazon-sagemaker-compilation-job-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Compute Quota API from Amazon SageMaker — 5 operation(s) for sagemaker compute quota.
  name: Amazon SageMaker Sagemaker Compute Quota API
  slug: amazon-sagemaker-compute-quota-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Context API from Amazon SageMaker — 5 operation(s) for sagemaker context.
  name: Amazon SageMaker Sagemaker Context API
  slug: amazon-sagemaker-context-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Data Quality Job Definition API from Amazon SageMaker — 4 operation(s) for sagemaker data quality job definition.
  name: Amazon SageMaker Sagemaker Data Quality Job Definition API
  slug: amazon-sagemaker-data-quality-job-definition-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Device API from Amazon SageMaker — 5 operation(s) for sagemaker device.
  name: Amazon SageMaker Sagemaker Device API
  slug: amazon-sagemaker-device-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Device Fleet API from Amazon SageMaker — 5 operation(s) for sagemaker device fleet.
  name: Amazon SageMaker Sagemaker Device Fleet API
  slug: amazon-sagemaker-device-fleet-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Domain API from Amazon SageMaker — 5 operation(s) for sagemaker domain.
  name: Amazon SageMaker Sagemaker Domain API
  slug: amazon-sagemaker-domain-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Edge Deployment Plan API from Amazon SageMaker — 4 operation(s) for sagemaker edge deployment plan.
  name: Amazon SageMaker Sagemaker Edge Deployment Plan API
  slug: amazon-sagemaker-edge-deployment-plan-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Edge Deployment Stage API from Amazon SageMaker — 4 operation(s) for sagemaker edge deployment stage.
  name: Amazon SageMaker Sagemaker Edge Deployment Stage API
  slug: amazon-sagemaker-edge-deployment-stage-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Edge Packaging Job API from Amazon SageMaker — 4 operation(s) for sagemaker edge packaging job.
  name: Amazon SageMaker Sagemaker Edge Packaging Job API
  slug: amazon-sagemaker-edge-packaging-job-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Endpoint Config API from Amazon SageMaker — 4 operation(s) for sagemaker endpoint config.
  name: Amazon SageMaker Sagemaker Endpoint Config API
  slug: amazon-sagemaker-endpoint-config-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Experiment API from Amazon SageMaker — 5 operation(s) for sagemaker experiment.
  name: Amazon SageMaker Sagemaker Experiment API
  slug: amazon-sagemaker-experiment-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Feature Group API from Amazon SageMaker — 5 operation(s) for sagemaker feature group.
  name: Amazon SageMaker Sagemaker Feature Group API
  slug: amazon-sagemaker-feature-group-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Flow Definition API from Amazon SageMaker — 4 operation(s) for sagemaker flow definition.
  name: Amazon SageMaker Sagemaker Flow Definition API
  slug: amazon-sagemaker-flow-definition-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Hub API from Amazon SageMaker — 5 operation(s) for sagemaker hub.
  name: Amazon SageMaker Sagemaker Hub API
  slug: amazon-sagemaker-hub-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Hub Content API from Amazon SageMaker — 5 operation(s) for sagemaker hub content.
  name: Amazon SageMaker Sagemaker Hub Content API
  slug: amazon-sagemaker-hub-content-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Hub Content Reference API from Amazon SageMaker — 3 operation(s) for sagemaker hub content reference.
  name: Amazon SageMaker Sagemaker Hub Content Reference API
  slug: amazon-sagemaker-hub-content-reference-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Human Task Ui API from Amazon SageMaker — 4 operation(s) for sagemaker human task ui.
  name: Amazon SageMaker Sagemaker Human Task Ui API
  slug: amazon-sagemaker-human-task-ui-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Hyper Parameter Tuning Job API from Amazon SageMaker — 5 operation(s) for sagemaker hyper parameter tuning job.
  name: Amazon SageMaker Sagemaker Hyper Parameter Tuning Job API
  slug: amazon-sagemaker-hyper-parameter-tuning-job-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Image API from Amazon SageMaker — 5 operation(s) for sagemaker image.
  name: Amazon SageMaker Sagemaker Image API
  slug: amazon-sagemaker-image-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Image Version API from Amazon SageMaker — 5 operation(s) for sagemaker image version.
  name: Amazon SageMaker Sagemaker Image Version API
  slug: amazon-sagemaker-image-version-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Inference Component API from Amazon SageMaker — 5 operation(s) for sagemaker inference component.
  name: Amazon SageMaker Sagemaker Inference Component API
  slug: amazon-sagemaker-inference-component-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Inference Experiment API from Amazon SageMaker — 7 operation(s) for sagemaker inference experiment.
  name: Amazon SageMaker Sagemaker Inference Experiment API
  slug: amazon-sagemaker-inference-experiment-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Inference Recommendations Job API from Amazon SageMaker — 4 operation(s) for sagemaker inference recommendations job.
  name: Amazon SageMaker Sagemaker Inference Recommendations Job API
  slug: amazon-sagemaker-inference-recommendations-job-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Job API from Amazon SageMaker — 5 operation(s) for sagemaker job.
  name: Amazon SageMaker Sagemaker Job API
  slug: amazon-sagemaker-job-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Labeling Job API from Amazon SageMaker — 5 operation(s) for sagemaker labeling job.
  name: Amazon SageMaker Sagemaker Labeling Job API
  slug: amazon-sagemaker-labeling-job-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Mlflow App API from Amazon SageMaker — 5 operation(s) for sagemaker mlflow app.
  name: Amazon SageMaker Sagemaker Mlflow App API
  slug: amazon-sagemaker-mlflow-app-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Mlflow Tracking Server API from Amazon SageMaker — 7 operation(s) for sagemaker mlflow tracking server.
  name: Amazon SageMaker Sagemaker Mlflow Tracking Server API
  slug: amazon-sagemaker-mlflow-tracking-server-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Model Bias Job Definition API from Amazon SageMaker — 4 operation(s) for sagemaker model bias job definition.
  name: Amazon SageMaker Sagemaker Model Bias Job Definition API
  slug: amazon-sagemaker-model-bias-job-definition-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Model Card API from Amazon SageMaker — 5 operation(s) for sagemaker model card.
  name: Amazon SageMaker Sagemaker Model Card API
  slug: amazon-sagemaker-model-card-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Model Card Export Job API from Amazon SageMaker — 3 operation(s) for sagemaker model card export job.
  name: Amazon SageMaker Sagemaker Model Card Export Job API
  slug: amazon-sagemaker-model-card-export-job-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Model Explainability Job Definition API from Amazon SageMaker — 4 operation(s) for sagemaker model explainability job definition.
  name: Amazon SageMaker Sagemaker Model Explainability Job Definition API
  slug: amazon-sagemaker-model-explainability-job-definition-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Model Package API from Amazon SageMaker — 6 operation(s) for sagemaker model package.
  name: Amazon SageMaker Sagemaker Model Package API
  slug: amazon-sagemaker-model-package-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Model Package Group API from Amazon SageMaker — 4 operation(s) for sagemaker model package group.
  name: Amazon SageMaker Sagemaker Model Package Group API
  slug: amazon-sagemaker-model-package-group-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Model Package Group Policy API from Amazon SageMaker — 3 operation(s) for sagemaker model package group policy.
  name: Amazon SageMaker Sagemaker Model Package Group Policy API
  slug: amazon-sagemaker-model-package-group-policy-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Model Quality Job Definition API from Amazon SageMaker — 4 operation(s) for sagemaker model quality job definition.
  name: Amazon SageMaker Sagemaker Model Quality Job Definition API
  slug: amazon-sagemaker-model-quality-job-definition-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Monitoring Schedule API from Amazon SageMaker — 7 operation(s) for sagemaker monitoring schedule.
  name: Amazon SageMaker Sagemaker Monitoring Schedule API
  slug: amazon-sagemaker-monitoring-schedule-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Notebook Instance Lifecycle Config API from Amazon SageMaker — 5 operation(s) for sagemaker notebook instance lifecycle config.
  name: Amazon SageMaker Sagemaker Notebook Instance Lifecycle Config API
  slug: amazon-sagemaker-notebook-instance-lifecycle-config-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Operations API from Amazon SageMaker — 63 operation(s) for sagemaker operations.
  name: Amazon SageMaker Sagemaker Operations API
  slug: amazon-sagemaker-operations-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Optimization Job API from Amazon SageMaker — 5 operation(s) for sagemaker optimization job.
  name: Amazon SageMaker Sagemaker Optimization Job API
  slug: amazon-sagemaker-optimization-job-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Partner App API from Amazon SageMaker — 5 operation(s) for sagemaker partner app.
  name: Amazon SageMaker Sagemaker Partner App API
  slug: amazon-sagemaker-partner-app-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Pipeline API from Amazon SageMaker — 5 operation(s) for sagemaker pipeline.
  name: Amazon SageMaker Sagemaker Pipeline API
  slug: amazon-sagemaker-pipeline-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Pipeline Execution API from Amazon SageMaker — 5 operation(s) for sagemaker pipeline execution.
  name: Amazon SageMaker Sagemaker Pipeline Execution API
  slug: amazon-sagemaker-pipeline-execution-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Processing Job API from Amazon SageMaker — 5 operation(s) for sagemaker processing job.
  name: Amazon SageMaker Sagemaker Processing Job API
  slug: amazon-sagemaker-processing-job-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Project API from Amazon SageMaker — 5 operation(s) for sagemaker project.
  name: Amazon SageMaker Sagemaker Project API
  slug: amazon-sagemaker-project-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Space API from Amazon SageMaker — 5 operation(s) for sagemaker space.
  name: Amazon SageMaker Sagemaker Space API
  slug: amazon-sagemaker-space-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Studio Lifecycle Config API from Amazon SageMaker — 4 operation(s) for sagemaker studio lifecycle config.
  name: Amazon SageMaker Sagemaker Studio Lifecycle Config API
  slug: amazon-sagemaker-studio-lifecycle-config-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Tag API from Amazon SageMaker — 3 operation(s) for sagemaker tag.
  name: Amazon SageMaker Sagemaker Tag API
  slug: amazon-sagemaker-tag-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Training Plan API from Amazon SageMaker — 3 operation(s) for sagemaker training plan.
  name: Amazon SageMaker Sagemaker Training Plan API
  slug: amazon-sagemaker-training-plan-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Training Session API from Amazon SageMaker — 5 operation(s) for sagemaker training session.
  name: Amazon SageMaker Sagemaker Training Session API
  slug: amazon-sagemaker-training-session-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Transform Job API from Amazon SageMaker — 4 operation(s) for sagemaker transform job.
  name: Amazon SageMaker Sagemaker Transform Job API
  slug: amazon-sagemaker-transform-job-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Trial API from Amazon SageMaker — 5 operation(s) for sagemaker trial.
  name: Amazon SageMaker Sagemaker Trial API
  slug: amazon-sagemaker-trial-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Trial Component API from Amazon SageMaker — 7 operation(s) for sagemaker trial component.
  name: Amazon SageMaker Sagemaker Trial Component API
  slug: amazon-sagemaker-trial-component-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker User Profile API from Amazon SageMaker — 5 operation(s) for sagemaker user profile.
  name: Amazon SageMaker Sagemaker User Profile API
  slug: amazon-sagemaker-user-profile-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Workforce API from Amazon SageMaker — 5 operation(s) for sagemaker workforce.
  name: Amazon SageMaker Sagemaker Workforce API
  slug: amazon-sagemaker-workforce-api
- baseURL: https://runtime.sagemaker.{region}.amazonaws.com
  baseurl_source: declared
  description: The Sagemaker Workteam API from Amazon SageMaker — 5 operation(s) for sagemaker workteam.
  name: Amazon SageMaker Sagemaker Workteam API
  slug: amazon-sagemaker-workteam-api
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
artifact_total: 156
collections:
- collection_type: postman
  name: Amazon SageMaker API
  slug: postman-amazon-sagemaker
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
  href: https://artifacts.apis.io/amazon-sagemaker/rate-limits/amazon-sagemaker-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-sagemaker-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-sagemaker/finops/amazon-sagemaker-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-sagemaker-finops.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-sagemaker/plans/amazon-sagemaker-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-sagemaker-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/sagemaker/
- group: other
  href: https://artifacts.apis.io/amazon-sagemaker/capabilities/amazon-sagemaker-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-sagemaker-capability-edges.yml
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
  href: https://artifacts.apis.io/amazon-sagemaker/agentic-access/amazon-sagemaker-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-sagemaker-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-sagemaker/security/amazon-sagemaker-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-sagemaker-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-sagemaker/security/amazon-sagemaker-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-sagemaker-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-sagemaker/security/amazon-sagemaker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-sagemaker-domain-security.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-sagemaker/overview
- group: design
  href: https://artifacts.apis.io/amazon-sagemaker/arazzo/amazon-sagemaker-audit-endpoint-fleet-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-sagemaker-audit-endpoint-fleet-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-sagemaker/arazzo/amazon-sagemaker-deploy-existing-model-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-sagemaker-deploy-existing-model-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-sagemaker/arazzo/amazon-sagemaker-deploy-model-to-endpoint-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-sagemaker-deploy-model-to-endpoint-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-sagemaker/arazzo/amazon-sagemaker-inventory-models-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-sagemaker-inventory-models-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-sagemaker/arazzo/amazon-sagemaker-provision-notebook-instance-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-sagemaker-provision-notebook-instance-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-sagemaker/arazzo/amazon-sagemaker-register-latest-completed-training-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-sagemaker-register-latest-completed-training-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-sagemaker/arazzo/amazon-sagemaker-train-and-poll-job-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-sagemaker-train-and-poll-job-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-sagemaker/arazzo/amazon-sagemaker-train-then-deploy-workflow.yml
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
  href: https://artifacts.apis.io/amazon-sagemaker/rules/amazon-sagemaker-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-sagemaker-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-sagemaker/vocabulary/amazon-sagemaker-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-sagemaker-vocabulary.yaml
- group: learn
  title: ''
  type: Training
  url: https://aws.amazon.com/training/
- group: design
  href: https://artifacts.apis.io/amazon-sagemaker/json-ld/amazon-sagemaker-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-sagemaker-context.jsonld
- group: docs
  href: https://artifacts.apis.io/amazon-sagemaker/json-schema/amazon-sagemaker-tag-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-sagemaker-tag-schema.json
- group: design
  href: https://artifacts.apis.io/amazon-sagemaker/json-structure/amazon-sagemaker-endpoint-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-sagemaker-endpoint-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-sagemaker/json-structure/amazon-sagemaker-model-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-sagemaker-model-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-sagemaker/json-structure/amazon-sagemaker-notebook-instance-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-sagemaker-notebook-instance-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-sagemaker/json-structure/amazon-sagemaker-tag-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-sagemaker-tag-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-sagemaker/json-structure/amazon-sagemaker-training-job-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-sagemaker-training-job-structure.json
- group: build
  href: https://artifacts.apis.io/amazon-sagemaker/examples/amazon-sagemaker-endpoint-example.json
  title: ''
  type: Examples
  url: examples/amazon-sagemaker-endpoint-example.json
- group: build
  href: https://artifacts.apis.io/amazon-sagemaker/examples/amazon-sagemaker-model-example.json
  title: ''
  type: Examples
  url: examples/amazon-sagemaker-model-example.json
- group: build
  href: https://artifacts.apis.io/amazon-sagemaker/examples/amazon-sagemaker-notebook-instance-example.json
  title: ''
  type: Examples
  url: examples/amazon-sagemaker-notebook-instance-example.json
- group: build
  href: https://artifacts.apis.io/amazon-sagemaker/examples/amazon-sagemaker-tag-example.json
  title: ''
  type: Examples
  url: examples/amazon-sagemaker-tag-example.json
- group: build
  href: https://artifacts.apis.io/amazon-sagemaker/examples/amazon-sagemaker-training-job-example.json
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
- has_sources: true
  method: derived
  name: Amazon Sagemaker Finops
  primary_unit: credit
  service_category: ''
  slug: amazon-sagemaker-finops
  template: false
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
modified: '2026-09-16'
name: Amazon SageMaker
nav: Providers
network: true
overview: 'Amazon SageMaker publishes 79 API contracts indexed on the [APIs.io](https://apis.io/) network, including Endpoints API, Models API, Notebook Instances API, and 76 more. Tagged areas include Artificial Intelligence, Amazon Web Services, Inference, Machine Learning, and MLOps.


  The Amazon SageMaker catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon SageMaker''s developer surface includes developer portal, getting-started guide, documentation, API reference, developer console, signup flow, pricing, and 55 more developer resources.'
plans:
- name: Amazon Sagemaker Plans Pricing
  plan_count: 6
  slug: amazon-sagemaker-plans-pricing
- name: Amazon Sagemaker Price Estimates
  plan_count: 0
  slug: amazon-sagemaker-price-estimates
random_paper: 3
rate_limits:
- limit_count: 5
  name: Amazon Sagemaker Rate Limits
  slug: amazon-sagemaker-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Amazon SageMaker — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-sagemaker-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 67
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
  band: exemplar
  composite: 71.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 81.0
    catalog_earned_first_party: 12.0
    catalog_gap: 34.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 100.0
    contract_governance: 27.3
    contract_quality: 75.7
    developer_ergonomics: 67.9
    discoverability: 67.9
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  open_source:
    applies: true
    score: 65.0
  previous_composite: 69.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 74
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/amazon-sagemaker/amazon-sagemaker-2026-06-20T171815.png
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
- Amazon Web Services
- Inference
- Machine Learning
- MLOps
- Training
- Model Training
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
website: https://aws.amazon.com/sagemaker/
---
