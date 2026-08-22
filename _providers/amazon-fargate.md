---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 21
  human_in_the_loop: 1
  name: Amazon Fargate Agentic Access
  operation_count: 21
  slug: amazon-fargate-agentic-access
  summary_line: 21 operations · 21 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: Operations for managing account-level settings
  name: Amazon Fargate Account Settings API
  slug: amazon-fargate-account-settings-api
- description: Operations for creating and managing ECS clusters
  name: Amazon Fargate Clusters API
  slug: amazon-fargate-clusters-api
- description: Operations for deploying and managing long-running services
  name: Amazon Fargate Services API
  slug: amazon-fargate-services-api
- description: Operations for tagging ECS resources
  name: Amazon Fargate Tagging API
  slug: amazon-fargate-tagging-api
- description: Operations for registering and managing task definitions
  name: Amazon Fargate Task Definitions API
  slug: amazon-fargate-task-definitions-api
- description: Operations for running and managing Fargate tasks
  name: Amazon Fargate Tasks API
  slug: amazon-fargate-tasks-api
arazzos:
- description: Enumerate clusters, describe one, then list its services and running tasks.
  name: Amazon Fargate Cluster Inventory Audit
  slug: amazon-fargate-cluster-inventory-audit-workflow
- description: Scale a service to zero and delete it, then delete the cluster once it has no active services.
  name: Amazon Fargate Decommission a Cluster
  slug: amazon-fargate-decommission-cluster-workflow
- description: Register a task definition, create a Fargate service, and poll until the running count meets the desired count.
  name: Amazon Fargate Deploy a Service
  slug: amazon-fargate-deploy-service-workflow
- description: Create a cluster, register a Fargate task definition, run a task, and poll until it reaches RUNNING.
  name: Amazon Fargate Provision and Run a Task
  slug: amazon-fargate-provision-and-run-task-workflow
- description: Register a new task definition revision, update a service to it, and poll until the deployment is steady.
  name: Amazon Fargate Roll Out a Service Update
  slug: amazon-fargate-rolling-update-service-workflow
- description: Run a one-off Fargate task and poll DescribeTasks until it reaches STOPPED.
  name: Amazon Fargate Run a Batch Task to Completion
  slug: amazon-fargate-run-batch-task-to-completion-workflow
- description: Find the latest active revision of a task definition family, describe it, and run a task from it.
  name: Amazon Fargate Run the Latest Task Definition
  slug: amazon-fargate-run-latest-task-definition-workflow
- description: Find a running task in a cluster, stop it, and poll DescribeTasks until it is STOPPED.
  name: Amazon Fargate Stop a Task and Confirm
  slug: amazon-fargate-stop-task-and-confirm-workflow
- description: Scale a service to zero, wait for it to drain, then delete it.
  name: Amazon Fargate Tear Down a Service
  slug: amazon-fargate-teardown-service-workflow
artifact_total: 97
collections:
- collection_type: postman
  name: Amazon Fargate API
  slug: postman-amazon-fargate
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Fargate Account Settings API
  slug: open-amazon-fargate-account-settings-api
- collection_type: open
  name: Amazon Fargate Account Settings Clusters API
  slug: open-amazon-fargate-clusters-api
- collection_type: open
  name: Amazon Fargate Account Settings Services API
  slug: open-amazon-fargate-services-api
- collection_type: open
  name: Amazon Fargate Account Settings Tagging API
  slug: open-amazon-fargate-tagging-api
- collection_type: open
  name: Amazon Fargate Account Settings Task Definitions API
  slug: open-amazon-fargate-task-definitions-api
- collection_type: open
  name: Amazon Fargate Account Settings Tasks API
  slug: open-amazon-fargate-tasks-api
- collection_type: open
  name: Amazon Fargate API
  slug: open-amazon-fargate
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-fargate-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-fargate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-fargate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-fargate-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-fargate/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fargate-cluster-inventory-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fargate-decommission-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fargate-deploy-service-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fargate-provision-and-run-task-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fargate-rolling-update-service-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fargate-run-batch-task-to-completion-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fargate-run-latest-task-definition-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fargate-stop-task-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fargate-teardown-service-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://console.aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/fargate/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/containers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/ecs
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-fargate
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-fargate-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-fargate-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-fargate-context.jsonld
created: '2024-01-15'
description: Amazon Fargate is a serverless compute engine for containers that works with both Amazon ECS and Amazon EKS. Fargate removes the need to provision and manage servers, letting you specify and pay for resources per application, and improves security through application isolation by design.
examples:
- key_count: 3
  name: Amazon Fargate Account Setting Example
  slug: amazon-fargate-account-setting-example
- key_count: 3
  name: Amazon Fargate Aws Vpc Configuration Example
  slug: amazon-fargate-aws-vpc-configuration-example
- key_count: 9
  name: Amazon Fargate Cluster Example
  slug: amazon-fargate-cluster-example
- key_count: 2
  name: Amazon Fargate Cluster Setting Example
  slug: amazon-fargate-cluster-setting-example
- key_count: 8
  name: Amazon Fargate Container Definition Example
  slug: amazon-fargate-container-definition-example
- key_count: 12
  name: Amazon Fargate Example
  slug: amazon-fargate-example
- key_count: 3
  name: Amazon Fargate Failure Example
  slug: amazon-fargate-failure-example
- key_count: 2
  name: Amazon Fargate Key Value Pair Example
  slug: amazon-fargate-key-value-pair-example
- key_count: 4
  name: Amazon Fargate Load Balancer Example
  slug: amazon-fargate-load-balancer-example
- key_count: 2
  name: Amazon Fargate Log Configuration Example
  slug: amazon-fargate-log-configuration-example
- key_count: 1
  name: Amazon Fargate Network Configuration Example
  slug: amazon-fargate-network-configuration-example
- key_count: 3
  name: Amazon Fargate Port Mapping Example
  slug: amazon-fargate-port-mapping-example
- key_count: 13
  name: Amazon Fargate Service Example
  slug: amazon-fargate-service-example
- key_count: 2
  name: Amazon Fargate Tag Example
  slug: amazon-fargate-tag-example
- key_count: 11
  name: Amazon Fargate Task Definition Example
  slug: amazon-fargate-task-definition-example
- key_count: 14
  name: Amazon Fargate Task Example
  slug: amazon-fargate-task-example
features:
- description: Run containers without provisioning or managing servers. Fargate handles capacity, OS updates, and scaling automatically.
  name: Serverless Compute
- description: Works seamlessly with both Amazon ECS task definitions and Amazon EKS pods.
  name: ECS and EKS Integration
- description: Each task runs in its own dedicated single-tenant compute environment for improved security.
  name: Workload Isolation
- description: Tasks receive ENIs with full VPC networking support including security groups and VPC Flow Logs.
  name: VPC Networking
- description: Supports Application Auto Scaling with target tracking, step scaling, and scheduled scaling.
  name: Auto Scaling
- description: Integration with Amazon EFS for stateful workloads requiring persistent storage.
  name: Persistent Storage
- description: HIPAA, PCI, FedRAMP, and GovCloud (US) region support for regulated workloads.
  name: Compliance Support
- description: Built-in Container Insights for metrics, logs, and observability.
  name: CloudWatch Integration
- description: Run workloads on AWS Graviton processors for improved price-performance.
  name: ARM64/Graviton Support
- description: Run fault-tolerant workloads on Fargate Spot for significant cost savings.
  name: Spot Instances
finops:
- name: Amazon Fargate Finops
  service_category: API
  slug: amazon-fargate-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: AccountSetting
  property_count: 3
  slug: amazon-fargate-account-setting
- name: AwsVpcConfiguration
  property_count: 3
  slug: amazon-fargate-aws-vpc-configuration
- name: Cluster
  property_count: 9
  slug: amazon-fargate-cluster
- name: ClusterSetting
  property_count: 2
  slug: amazon-fargate-cluster-setting
- name: ContainerDefinition
  property_count: 8
  slug: amazon-fargate-container-definition
- name: Failure
  property_count: 3
  slug: amazon-fargate-failure
- name: KeyValuePair
  property_count: 2
  slug: amazon-fargate-key-value-pair
- name: LoadBalancer
  property_count: 4
  slug: amazon-fargate-load-balancer
- name: LogConfiguration
  property_count: 2
  slug: amazon-fargate-log-configuration
- name: NetworkConfiguration
  property_count: 1
  slug: amazon-fargate-network-configuration
- name: PortMapping
  property_count: 3
  slug: amazon-fargate-port-mapping
- name: Service
  property_count: 13
  slug: amazon-fargate-service
- name: Tag
  property_count: 2
  slug: amazon-fargate-tag
- name: TaskDefinition
  property_count: 11
  slug: amazon-fargate-task-definition
- name: Task
  property_count: 14
  slug: amazon-fargate-task
json_structures:
- name: Amazon Fargate Account Setting Structure
  property_count: 3
  slug: amazon-fargate-account-setting-structure
- name: Amazon Fargate Aws Vpc Configuration Structure
  property_count: 3
  slug: amazon-fargate-aws-vpc-configuration-structure
- name: Amazon Fargate Cluster Setting Structure
  property_count: 2
  slug: amazon-fargate-cluster-setting-structure
- name: Amazon Fargate Cluster Structure
  property_count: 9
  slug: amazon-fargate-cluster-structure
- name: Amazon Fargate Container Definition Structure
  property_count: 8
  slug: amazon-fargate-container-definition-structure
- name: Amazon Fargate Failure Structure
  property_count: 3
  slug: amazon-fargate-failure-structure
- name: Amazon Fargate Key Value Pair Structure
  property_count: 2
  slug: amazon-fargate-key-value-pair-structure
- name: Amazon Fargate Load Balancer Structure
  property_count: 4
  slug: amazon-fargate-load-balancer-structure
- name: Amazon Fargate Log Configuration Structure
  property_count: 2
  slug: amazon-fargate-log-configuration-structure
- name: Amazon Fargate Network Configuration Structure
  property_count: 1
  slug: amazon-fargate-network-configuration-structure
- name: Amazon Fargate Port Mapping Structure
  property_count: 3
  slug: amazon-fargate-port-mapping-structure
- name: Amazon Fargate Service Structure
  property_count: 13
  slug: amazon-fargate-service-structure
- name: Amazon Fargate Structure
  property_count: 12
  slug: amazon-fargate-structure
- name: Amazon Fargate Tag Structure
  property_count: 2
  slug: amazon-fargate-tag-structure
- name: Amazon Fargate Task Definition Structure
  property_count: 11
  slug: amazon-fargate-task-definition-structure
- name: Amazon Fargate Task Structure
  property_count: 14
  slug: amazon-fargate-task-structure
jsonld:
- class_count: 18
  name: Amazon Fargate Context
  property_count: 61
  slug: amazon-fargate-context
layout: provider
modified: '2026-05-19'
name: Amazon Fargate
nav: Providers
network: true
overview: 'Amazon Fargate publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account Settings API, Clusters API, Services API, and 3 more. Tagged areas include Compute, Containers, ECS, EKS, and Microservices.


  The Amazon Fargate catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Fargate''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 23 more developer resources.'
plans:
- name: Amazon Fargate Plans Pricing
  plan_count: 3
  slug: amazon-fargate-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Amazon Fargate Rate Limits
  slug: amazon-fargate-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Fargate API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-fargate-jsonschema-spectral-rules
- effective_rule_count: 74
  extends:
  - spectral:oas
  name: Amazon Fargate API Rules
  rule_count: 33
  severity_counts:
    error: 10
    hint: 0
    info: 5
    warn: 18
  slug: amazon-fargate-spectral-rules
score:
  band: developing
  composite: 42.2
  delta: -5.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 30.6
    developer_ergonomics: 50.0
    discoverability: 81.5
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 47.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-fargate/refs/heads/main/screenshots/amazon-fargate-2026-06-20T171646.png
security:
- kind: authentication
  name: Amazon Fargate Authentication
  slug: amazon-fargate-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Fargate Domain Security
  slug: amazon-fargate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Fargate Vulnerability Disclosure
  slug: amazon-fargate-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: amazon-fargate
tags:
- Compute
- Containers
- ECS
- EKS
- Microservices
- Serverless
use_cases:
- description: Deploy microservices-based web applications and REST APIs without infrastructure management.
  name: Web Applications and APIs
- description: Run parallel data processing jobs and ETL workloads using AWS Batch with Fargate.
  name: Batch Data Processing
- description: Lift-and-shift containerized workloads to serverless infrastructure for reduced operational burden.
  name: Application Modernization
- description: Run training, inference, and data preparation containers in flexible serverless environments.
  name: AI/ML Workloads
- description: Execute build, test, and deployment pipelines as ephemeral Fargate tasks.
  name: CI/CD Pipelines
- description: Run time-based container workloads using Amazon EventBridge and Fargate tasks.
  name: Scheduled Jobs
website: https://aws.amazon.com/fargate/
---
