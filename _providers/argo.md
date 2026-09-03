---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 29
  human_in_the_loop: 2
  name: Argo Agentic Access
  operation_count: 48
  slug: argo-agentic-access
  summary_line: 48 operations · 29 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: Kubernetes-native API for the Argo Events event-driven automation framework. Exposes CRD-based resources including EventSource, EventBus, and Sensor for triggering Argo Workflows and Kubernetes action
  name: Argo Events API
  slug: argo-events-api
- description: Kubernetes CRD-based API for Argo Rollouts progressive delivery controller. Provides Rollout and AnalysisTemplate resources for managing canary and blue-green deployment strategies with automated anal
  name: Argo Rollouts API
  slug: argo-rollouts-api
- baseURL: https://localhost:2746/api/v1
  baseurl_source: declared
  description: Operations for creating, querying, syncing, and deleting Argo CD GitOps applications.
  name: Argo Applications API
  slug: argo-applications-api
- baseURL: https://localhost:2746/api/v1
  baseurl_source: declared
  description: Operations for registering and managing target Kubernetes clusters for application deployment.
  name: Argo Clusters API
  slug: argo-clusters-api
- baseURL: https://localhost:2746/api/v1
  baseurl_source: declared
  description: Operations for managing scheduled cron workflows
  name: Argo Cron Workflows API
  slug: argo-cron-workflows-api
- baseURL: https://localhost:2746/api/v1
  baseurl_source: declared
  description: Server information and version endpoints
  name: Argo Info API
  slug: argo-info-api
- baseURL: https://localhost:2746/api/v1
  baseurl_source: declared
  description: Operations for managing Argo CD projects that provide governance and access control for applications.
  name: Argo Projects API
  slug: argo-projects-api
- baseURL: https://localhost:2746/api/v1
  baseurl_source: declared
  description: Operations for registering and managing Git and Helm chart repositories used as application sources.
  name: Argo Repositories API
  slug: argo-repositories-api
- baseURL: https://localhost:2746/api/v1
  baseurl_source: declared
  description: Authentication operations for obtaining and invalidating bearer tokens.
  name: Argo Session API
  slug: argo-session-api
- baseURL: https://localhost:2746/api/v1
  baseurl_source: declared
  description: Operations for reading Argo CD server configuration and settings.
  name: Argo Settings API
  slug: argo-settings-api
- baseURL: https://localhost:2746/api/v1
  baseurl_source: declared
  description: Server version information endpoint.
  name: Argo Version API
  slug: argo-version-api
- baseURL: https://localhost:2746/api/v1
  baseurl_source: declared
  description: Operations for accessing archived workflow records
  name: Argo Workflow Archives API
  slug: argo-workflow-archives-api
- baseURL: https://localhost:2746/api/v1
  baseurl_source: declared
  description: Operations for managing reusable workflow templates
  name: Argo Workflow Templates API
  slug: argo-workflow-templates-api
- baseURL: https://localhost:2746/api/v1
  baseurl_source: declared
  description: Operations for managing workflow executions
  name: Argo Workflows API
  slug: argo-workflows-api
artifact_total: 213
asyncapis:
- description: Argo Events is a Kubernetes-native event-driven automation framework that listens to over 20 event sources and triggers Argo Workflows, Kubernetes objects, HTTP requests, and other actions in response
  name: Argo Events
  slug: argo-events-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Argo CD Applications API
  slug: open-argo-applications-api
- collection_type: open
  name: Argo CD API
  slug: open-argo-cd
- collection_type: open
  name: Argo CD Applications Clusters API
  slug: open-argo-clusters-api
- collection_type: open
  name: Argo CD Applications Cron Workflows API
  slug: open-argo-cron-workflows-api
- collection_type: open
  name: Argo CD Applications Info API
  slug: open-argo-info-api
- collection_type: open
  name: Argo CD Applications Projects API
  slug: open-argo-projects-api
- collection_type: open
  name: Argo CD Applications Repositories API
  slug: open-argo-repositories-api
- collection_type: open
  name: Argo CD Applications Session API
  slug: open-argo-session-api
- collection_type: open
  name: Argo CD Applications Settings API
  slug: open-argo-settings-api
- collection_type: open
  name: Argo CD Applications Version API
  slug: open-argo-version-api
- collection_type: open
  name: Argo CD Applications Workflow Archives API
  slug: open-argo-workflow-archives-api
- collection_type: open
  name: Argo CD Applications Workflow Templates API
  slug: open-argo-workflow-templates-api
- collection_type: open
  name: Argo CD Applications Workflows API
  slug: open-argo-workflows-api
- collection_type: open
  name: Argo Workflows API
  slug: open-argo-workflows
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/argoproj/argo-events/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/argoproj/argo-events/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/argoproj/argo-events/blob/master/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/argoproj/argo-events/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/argoproj/argo-events/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/argo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/argo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/argo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/argo-ai
- group: company
  title: ''
  type: Website
  url: https://argoproj.github.io/
- group: docs
  title: ''
  type: Documentation
  url: https://argoproj.github.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/argoproj
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/argoproj/argoproj
- group: company
  title: ''
  type: Blog
  url: https://blog.argoproj.io/
- group: operate
  title: ''
  type: Support
  url: https://github.com/argoproj/argo-workflows/issues
- group: design
  title: ''
  type: JSONLD
  url: json-ld/argo-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/argo-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/argo-vocabulary.yaml
created: '2025-01-01'
description: Argo is a collection of open-source Kubernetes-native tools for workflows, events, CI/CD, and progressive delivery. The project includes Argo Workflows (container-native workflow engine), Argo CD (declarative GitOps continuous delivery), Argo Events (event-driven automation framework), and Argo Rollouts (progressive delivery with canary and blue-green strategies). Argo is a CNCF graduated project governed by the Linux Foundation.
examples:
- key_count: 4
  name: Argo Application Example
  slug: argo-application-example
- key_count: 2
  name: Argo Cd App Project Example
  slug: argo-cd-app-project-example
- key_count: 3
  name: Argo Cd Application Destination Example
  slug: argo-cd-application-destination-example
- key_count: 5
  name: Argo Cd Application Example
  slug: argo-cd-application-example
- key_count: 1
  name: Argo Cd Application List Example
  slug: argo-cd-application-list-example
- key_count: 6
  name: Argo Cd Application Source Example
  slug: argo-cd-application-source-example
- key_count: 5
  name: Argo Cd Application Spec Example
  slug: argo-cd-application-spec-example
- key_count: 3
  name: Argo Cd Application Status Example
  slug: argo-cd-application-status-example
- key_count: 4
  name: Argo Cd Cluster Example
  slug: argo-cd-cluster-example
- key_count: 1
  name: Argo Cd Cluster List Example
  slug: argo-cd-cluster-list-example
- key_count: 1
  name: Argo Cd Project List Example
  slug: argo-cd-project-list-example
- key_count: 4
  name: Argo Cd Repository Example
  slug: argo-cd-repository-example
- key_count: 1
  name: Argo Cd Repository List Example
  slug: argo-cd-repository-list-example
- key_count: 6
  name: Argo Cd Settings Example
  slug: argo-cd-settings-example
- key_count: 3
  name: Argo Cd Sync Policy Example
  slug: argo-cd-sync-policy-example
- key_count: 5
  name: Argo Cd Sync Request Example
  slug: argo-cd-sync-request-example
- key_count: 5
  name: Argo Cd Version Message Example
  slug: argo-cd-version-message-example
- key_count: 5
  name: Argo Rollout Example
  slug: argo-rollout-example
- key_count: 4
  name: Argo Workflow Example
  slug: argo-workflow-example
- key_count: 2
  name: Argo Workflows Arguments Example
  slug: argo-workflows-arguments-example
- key_count: 7
  name: Argo Workflows Artifact Example
  slug: argo-workflows-artifact-example
- key_count: 3
  name: Argo Workflows Cron Workflow Create Request Example
  slug: argo-workflows-cron-workflow-create-request-example
- key_count: 5
  name: Argo Workflows Cron Workflow Example
  slug: argo-workflows-cron-workflow-example
- key_count: 3
  name: Argo Workflows Cron Workflow List Example
  slug: argo-workflows-cron-workflow-list-example
- key_count: 9
  name: Argo Workflows Cron Workflow Spec Example
  slug: argo-workflows-cron-workflow-spec-example
- key_count: 3
  name: Argo Workflows Cron Workflow Status Example
  slug: argo-workflows-cron-workflow-status-example
- key_count: 3
  name: Argo Workflows Cron Workflow Update Request Example
  slug: argo-workflows-cron-workflow-update-request-example
- key_count: 8
  name: Argo Workflows Dag Task Example
  slug: argo-workflows-dag-task-example
- key_count: 2
  name: Argo Workflows Info Response Example
  slug: argo-workflows-info-response-example
- key_count: 2
  name: Argo Workflows Inputs Example
  slug: argo-workflows-inputs-example
- key_count: 2
  name: Argo Workflows Log Entry Example
  slug: argo-workflows-log-entry-example
- key_count: 12
  name: Argo Workflows Node Status Example
  slug: argo-workflows-node-status-example
- key_count: 9
  name: Argo Workflows Object Meta Example
  slug: argo-workflows-object-meta-example
- key_count: 4
  name: Argo Workflows Outputs Example
  slug: argo-workflows-outputs-example
- key_count: 6
  name: Argo Workflows Parameter Example
  slug: argo-workflows-parameter-example
- key_count: 3
  name: Argo Workflows Retry Strategy Example
  slug: argo-workflows-retry-strategy-example
- key_count: 13
  name: Argo Workflows Template Example
  slug: argo-workflows-template-example
- key_count: 8
  name: Argo Workflows Version Example
  slug: argo-workflows-version-example
- key_count: 4
  name: Argo Workflows Workflow Create Request Example
  slug: argo-workflows-workflow-create-request-example
- key_count: 5
  name: Argo Workflows Workflow Example
  slug: argo-workflows-workflow-example
- key_count: 3
  name: Argo Workflows Workflow List Example
  slug: argo-workflows-workflow-list-example
- key_count: 3
  name: Argo Workflows Workflow Resubmit Request Example
  slug: argo-workflows-workflow-resubmit-request-example
- key_count: 3
  name: Argo Workflows Workflow Resume Request Example
  slug: argo-workflows-workflow-resume-request-example
- key_count: 5
  name: Argo Workflows Workflow Retry Request Example
  slug: argo-workflows-workflow-retry-request-example
- key_count: 16
  name: Argo Workflows Workflow Spec Example
  slug: argo-workflows-workflow-spec-example
- key_count: 11
  name: Argo Workflows Workflow Status Example
  slug: argo-workflows-workflow-status-example
- key_count: 7
  name: Argo Workflows Workflow Step Example
  slug: argo-workflows-workflow-step-example
- key_count: 4
  name: Argo Workflows Workflow Stop Request Example
  slug: argo-workflows-workflow-stop-request-example
- key_count: 3
  name: Argo Workflows Workflow Template Create Request Example
  slug: argo-workflows-workflow-template-create-request-example
- key_count: 4
  name: Argo Workflows Workflow Template Example
  slug: argo-workflows-workflow-template-example
- key_count: 3
  name: Argo Workflows Workflow Template List Example
  slug: argo-workflows-workflow-template-list-example
- key_count: 3
  name: Argo Workflows Workflow Template Update Request Example
  slug: argo-workflows-workflow-template-update-request-example
features:
- description: Container-native workflow engine for orchestrating parallel jobs and ML pipelines on Kubernetes.
  name: Argo Workflows
- description: Declarative GitOps continuous delivery tool that syncs Kubernetes application state from Git.
  name: Argo CD
- description: Event-driven automation framework supporting 20+ event sources to trigger Kubernetes workflows.
  name: Argo Events
- description: Progressive delivery controller with canary, blue-green, and experiment strategies for Kubernetes.
  name: Argo Rollouts
- description: All four Argo projects are CNCF graduated, ensuring production-quality governance and stability.
  name: CNCF Graduated
- description: All tools are implemented as Kubernetes CRDs and controllers, integrating natively with the platform.
  name: Kubernetes-Native
finops:
- name: Argo Finops
  service_category: API
  slug: argo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/argo.png
integrations:
- description: Argo CD natively renders Helm charts; Argo Workflows can execute Helm operations as steps.
  name: Helm
- description: Argo CD supports Kustomize overlays for environment-specific application configuration.
  name: Kustomize
- description: All Argo tools expose Prometheus metrics for monitoring workflow and deployment health.
  name: Prometheus
- description: Argo CD and Argo Workflows support Slack notifications for deployment and workflow events.
  name: Slack
- description: Deep integration with GitHub webhooks for triggering workflows and CD syncs.
  name: GitHub
- description: Argo Workflows uses S3 as an artifact repository for passing data between workflow steps.
  name: Amazon S3
json_schemas:
- name: Argo CD Application Spec
  property_count: 4
  slug: argo-application
- name: AppProject
  property_count: 2
  slug: argo-cd-app-project
- name: ApplicationDestination
  property_count: 3
  slug: argo-cd-application-destination
- name: ApplicationList
  property_count: 1
  slug: argo-cd-application-list
- name: Application
  property_count: 5
  slug: argo-cd-application
- name: ApplicationSource
  property_count: 6
  slug: argo-cd-application-source
- name: ApplicationSpec
  property_count: 5
  slug: argo-cd-application-spec
- name: ApplicationStatus
  property_count: 3
  slug: argo-cd-application-status
- name: ClusterList
  property_count: 1
  slug: argo-cd-cluster-list
- name: Cluster
  property_count: 4
  slug: argo-cd-cluster
- name: ProjectList
  property_count: 1
  slug: argo-cd-project-list
- name: RepositoryList
  property_count: 1
  slug: argo-cd-repository-list
- name: Repository
  property_count: 4
  slug: argo-cd-repository
- name: Settings
  property_count: 6
  slug: argo-cd-settings
- name: SyncPolicy
  property_count: 3
  slug: argo-cd-sync-policy
- name: SyncRequest
  property_count: 5
  slug: argo-cd-sync-request
- name: VersionMessage
  property_count: 5
  slug: argo-cd-version-message
- name: Argo Rollout Spec
  property_count: 5
  slug: argo-rollout
- name: Argo Workflow Spec
  property_count: 4
  slug: argo-workflow
- name: Arguments
  property_count: 2
  slug: argo-workflows-arguments
- name: Artifact
  property_count: 7
  slug: argo-workflows-artifact
- name: CronWorkflowCreateRequest
  property_count: 3
  slug: argo-workflows-cron-workflow-create-request
- name: CronWorkflowList
  property_count: 3
  slug: argo-workflows-cron-workflow-list
- name: CronWorkflow
  property_count: 5
  slug: argo-workflows-cron-workflow
- name: CronWorkflowSpec
  property_count: 9
  slug: argo-workflows-cron-workflow-spec
- name: CronWorkflowStatus
  property_count: 3
  slug: argo-workflows-cron-workflow-status
- name: CronWorkflowUpdateRequest
  property_count: 3
  slug: argo-workflows-cron-workflow-update-request
- name: DAGTask
  property_count: 8
  slug: argo-workflows-dag-task
- name: InfoResponse
  property_count: 2
  slug: argo-workflows-info-response
- name: Inputs
  property_count: 2
  slug: argo-workflows-inputs
- name: LogEntry
  property_count: 2
  slug: argo-workflows-log-entry
- name: NodeStatus
  property_count: 12
  slug: argo-workflows-node-status
- name: ObjectMeta
  property_count: 9
  slug: argo-workflows-object-meta
- name: Outputs
  property_count: 4
  slug: argo-workflows-outputs
- name: Parameter
  property_count: 6
  slug: argo-workflows-parameter
- name: RetryStrategy
  property_count: 3
  slug: argo-workflows-retry-strategy
- name: Template
  property_count: 13
  slug: argo-workflows-template
- name: Version
  property_count: 8
  slug: argo-workflows-version
- name: WorkflowCreateRequest
  property_count: 4
  slug: argo-workflows-workflow-create-request
- name: WorkflowList
  property_count: 3
  slug: argo-workflows-workflow-list
- name: WorkflowResubmitRequest
  property_count: 3
  slug: argo-workflows-workflow-resubmit-request
- name: WorkflowResumeRequest
  property_count: 3
  slug: argo-workflows-workflow-resume-request
- name: WorkflowRetryRequest
  property_count: 5
  slug: argo-workflows-workflow-retry-request
- name: Workflow
  property_count: 5
  slug: argo-workflows-workflow
- name: WorkflowSpec
  property_count: 16
  slug: argo-workflows-workflow-spec
- name: WorkflowStatus
  property_count: 11
  slug: argo-workflows-workflow-status
- name: WorkflowStep
  property_count: 7
  slug: argo-workflows-workflow-step
- name: WorkflowStopRequest
  property_count: 4
  slug: argo-workflows-workflow-stop-request
- name: WorkflowTemplateCreateRequest
  property_count: 3
  slug: argo-workflows-workflow-template-create-request
- name: WorkflowTemplateList
  property_count: 3
  slug: argo-workflows-workflow-template-list
- name: WorkflowTemplate
  property_count: 4
  slug: argo-workflows-workflow-template
- name: WorkflowTemplateUpdateRequest
  property_count: 3
  slug: argo-workflows-workflow-template-update-request
json_structures:
- name: Argo Application Structure
  property_count: 4
  slug: argo-application-structure
- name: Argo Cd App Project Structure
  property_count: 2
  slug: argo-cd-app-project-structure
- name: Argo Cd Application Destination Structure
  property_count: 3
  slug: argo-cd-application-destination-structure
- name: Argo Cd Application List Structure
  property_count: 1
  slug: argo-cd-application-list-structure
- name: Argo Cd Application Source Structure
  property_count: 6
  slug: argo-cd-application-source-structure
- name: Argo Cd Application Spec Structure
  property_count: 5
  slug: argo-cd-application-spec-structure
- name: Argo Cd Application Status Structure
  property_count: 3
  slug: argo-cd-application-status-structure
- name: Argo Cd Application Structure
  property_count: 5
  slug: argo-cd-application-structure
- name: Argo Cd Cluster List Structure
  property_count: 1
  slug: argo-cd-cluster-list-structure
- name: Argo Cd Cluster Structure
  property_count: 4
  slug: argo-cd-cluster-structure
- name: Argo Cd Project List Structure
  property_count: 1
  slug: argo-cd-project-list-structure
- name: Argo Cd Repository List Structure
  property_count: 1
  slug: argo-cd-repository-list-structure
- name: Argo Cd Repository Structure
  property_count: 4
  slug: argo-cd-repository-structure
- name: Argo Cd Settings Structure
  property_count: 6
  slug: argo-cd-settings-structure
- name: Argo Cd Sync Policy Structure
  property_count: 3
  slug: argo-cd-sync-policy-structure
- name: Argo Cd Sync Request Structure
  property_count: 5
  slug: argo-cd-sync-request-structure
- name: Argo Cd Version Message Structure
  property_count: 5
  slug: argo-cd-version-message-structure
- name: Argo Rollout Structure
  property_count: 5
  slug: argo-rollout-structure
- name: Argo Workflow Structure
  property_count: 4
  slug: argo-workflow-structure
- name: Argo Workflows Arguments Structure
  property_count: 2
  slug: argo-workflows-arguments-structure
- name: Argo Workflows Artifact Structure
  property_count: 7
  slug: argo-workflows-artifact-structure
- name: Argo Workflows Cron Workflow Create Request Structure
  property_count: 3
  slug: argo-workflows-cron-workflow-create-request-structure
- name: Argo Workflows Cron Workflow List Structure
  property_count: 3
  slug: argo-workflows-cron-workflow-list-structure
- name: Argo Workflows Cron Workflow Spec Structure
  property_count: 9
  slug: argo-workflows-cron-workflow-spec-structure
- name: Argo Workflows Cron Workflow Status Structure
  property_count: 3
  slug: argo-workflows-cron-workflow-status-structure
- name: Argo Workflows Cron Workflow Structure
  property_count: 5
  slug: argo-workflows-cron-workflow-structure
- name: Argo Workflows Cron Workflow Update Request Structure
  property_count: 3
  slug: argo-workflows-cron-workflow-update-request-structure
- name: Argo Workflows Dag Task Structure
  property_count: 8
  slug: argo-workflows-dag-task-structure
- name: Argo Workflows Info Response Structure
  property_count: 2
  slug: argo-workflows-info-response-structure
- name: Argo Workflows Inputs Structure
  property_count: 2
  slug: argo-workflows-inputs-structure
- name: Argo Workflows Log Entry Structure
  property_count: 2
  slug: argo-workflows-log-entry-structure
- name: Argo Workflows Node Status Structure
  property_count: 12
  slug: argo-workflows-node-status-structure
- name: Argo Workflows Object Meta Structure
  property_count: 9
  slug: argo-workflows-object-meta-structure
- name: Argo Workflows Outputs Structure
  property_count: 4
  slug: argo-workflows-outputs-structure
- name: Argo Workflows Parameter Structure
  property_count: 6
  slug: argo-workflows-parameter-structure
- name: Argo Workflows Retry Strategy Structure
  property_count: 3
  slug: argo-workflows-retry-strategy-structure
- name: Argo Workflows Template Structure
  property_count: 13
  slug: argo-workflows-template-structure
- name: Argo Workflows Version Structure
  property_count: 8
  slug: argo-workflows-version-structure
- name: Argo Workflows Workflow Create Request Structure
  property_count: 4
  slug: argo-workflows-workflow-create-request-structure
- name: Argo Workflows Workflow List Structure
  property_count: 3
  slug: argo-workflows-workflow-list-structure
- name: Argo Workflows Workflow Resubmit Request Structure
  property_count: 3
  slug: argo-workflows-workflow-resubmit-request-structure
- name: Argo Workflows Workflow Resume Request Structure
  property_count: 3
  slug: argo-workflows-workflow-resume-request-structure
- name: Argo Workflows Workflow Retry Request Structure
  property_count: 5
  slug: argo-workflows-workflow-retry-request-structure
- name: Argo Workflows Workflow Spec Structure
  property_count: 16
  slug: argo-workflows-workflow-spec-structure
- name: Argo Workflows Workflow Status Structure
  property_count: 11
  slug: argo-workflows-workflow-status-structure
- name: Argo Workflows Workflow Step Structure
  property_count: 7
  slug: argo-workflows-workflow-step-structure
- name: Argo Workflows Workflow Stop Request Structure
  property_count: 4
  slug: argo-workflows-workflow-stop-request-structure
- name: Argo Workflows Workflow Structure
  property_count: 5
  slug: argo-workflows-workflow-structure
- name: Argo Workflows Workflow Template Create Request Structure
  property_count: 3
  slug: argo-workflows-workflow-template-create-request-structure
- name: Argo Workflows Workflow Template List Structure
  property_count: 3
  slug: argo-workflows-workflow-template-list-structure
- name: Argo Workflows Workflow Template Structure
  property_count: 4
  slug: argo-workflows-workflow-template-structure
- name: Argo Workflows Workflow Template Update Request Structure
  property_count: 3
  slug: argo-workflows-workflow-template-update-request-structure
jsonld:
- class_count: 4
  name: Argo Context
  property_count: 37
  slug: argo-context
layout: provider
modified: '2026-05-19'
name: Argo
nav: Providers
network: true
overview: 'Argo publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Events API, Applications API, Clusters API, and 10 more. Tagged areas include CNCF, CI/CD, GitOps, Kubernetes, and Open-Source.


  The Argo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Argo''s developer surface includes authentication, documentation, engineering blog, support, and 14 more developer resources.'
plans:
- name: Argo Plans Pricing
  plan_count: 3
  slug: argo-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Argo Rate Limits
  slug: argo-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Argo API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 7
  slug: argo-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Argo API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: argo-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Argo API Rules
  rule_count: 16
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 7
  slug: argo-spectral-rules
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 68.2
    developer_ergonomics: 47.6
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 85.0
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/argo/refs/heads/main/screenshots/argo-2026-06-20T172416.png
security:
- kind: authentication
  name: Argo Authentication
  slug: argo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Argo Domain Security
  slug: argo-domain-security
  summary_line: TLSv1.3 · HSTS
slug: argo
tags:
- CNCF
- CI/CD
- GitOps
- Kubernetes
- Open-Source
- Progressive Delivery
- Workflow Engine
use_cases:
- description: Combine Argo CD and Argo Workflows for a complete Git-driven DevOps platform on Kubernetes.
  name: GitOps Platform
- description: Use Argo Workflows to orchestrate multi-step ML training, evaluation, and deployment pipelines.
  name: Machine Learning Pipelines
- description: Use Argo Events to trigger workflows based on webhooks, schedules, messaging, and cloud events.
  name: Event-Driven Automation
- description: Use Argo Rollouts for safe canary and blue-green deployments with automated analysis and rollback.
  name: Progressive Delivery
- description: Build complete CI/CD pipelines natively on Kubernetes using Argo Workflows and Argo CD together.
  name: CI/CD on Kubernetes
website: https://argoproj.github.io/
---
