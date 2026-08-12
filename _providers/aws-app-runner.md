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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Aws App Runner Agentic Access
  operation_count: 20
  slug: aws-app-runner-agentic-access
  summary_line: 20 operations · 20 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: Manage auto scaling configurations
  name: AWS App Runner Auto Scaling API
  slug: aws-app-runner-auto-scaling-api
- description: The AWS App Runner API API from AWS App Runner — 1 operation(s) for aws app runner api.
  name: AWS App Runner AWS App Runner API API
  slug: aws-app-runner-aws-app-runner-api-api
- description: Manage source code provider connections
  name: AWS App Runner Connections API
  slug: aws-app-runner-connections-api
- description: Manage custom domain associations
  name: AWS App Runner Custom Domains API
  slug: aws-app-runner-custom-domains-api
- description: 'The #DeleteService API from AWS App Runner — 1 operation(s) for #deleteservice.'
  name: 'AWS App Runner #DeleteService API'
  slug: aws-app-runner-deleteservice-api
- description: Manage deployments and operations
  name: AWS App Runner Deployments API
  slug: aws-app-runner-deployments-api
- description: 'The #DescribeService API from AWS App Runner — 1 operation(s) for #describeservice.'
  name: 'AWS App Runner #DescribeService API'
  slug: aws-app-runner-describeservice-api
- description: 'The #ListServices API from AWS App Runner — 1 operation(s) for #listservices.'
  name: 'AWS App Runner #ListServices API'
  slug: aws-app-runner-listservices-api
- description: Manage observability configurations
  name: AWS App Runner Observability API
  slug: aws-app-runner-observability-api
- description: 'The #PauseService API from AWS App Runner — 1 operation(s) for #pauseservice.'
  name: 'AWS App Runner #PauseService API'
  slug: aws-app-runner-pauseservice-api
- description: 'The #ResumeService API from AWS App Runner — 1 operation(s) for #resumeservice.'
  name: 'AWS App Runner #ResumeService API'
  slug: aws-app-runner-resumeservice-api
- description: 'The #UpdateService API from AWS App Runner — 1 operation(s) for #updateservice.'
  name: 'AWS App Runner #UpdateService API'
  slug: aws-app-runner-updateservice-api
- description: Manage VPC connectors
  name: AWS App Runner VPC API
  slug: aws-app-runner-vpc-api
artifact_total: 102
collections:
- collection_type: postman
  name: AWS App Runner Auto Scaling API
  slug: postman-aws-app-runner-auto-scaling-api
- collection_type: postman
  name: AWS App Runner Auto Scaling AWS App Runner API API
  slug: postman-aws-app-runner-aws-app-runner-api-api
- collection_type: postman
  name: AWS App Runner Auto Scaling Connections API
  slug: postman-aws-app-runner-connections-api
- collection_type: postman
  name: AWS App Runner Auto Scaling Custom Domains API
  slug: postman-aws-app-runner-custom-domains-api
- collection_type: postman
  name: 'AWS App Runner Auto Scaling #DeleteService API'
  slug: postman-aws-app-runner-deleteservice-api
- collection_type: postman
  name: AWS App Runner Auto Scaling Deployments API
  slug: postman-aws-app-runner-deployments-api
- collection_type: postman
  name: 'AWS App Runner Auto Scaling #DescribeService API'
  slug: postman-aws-app-runner-describeservice-api
- collection_type: postman
  name: 'AWS App Runner Auto Scaling #ListServices API'
  slug: postman-aws-app-runner-listservices-api
- collection_type: postman
  name: AWS App Runner Auto Scaling Observability API
  slug: postman-aws-app-runner-observability-api
- collection_type: postman
  name: 'AWS App Runner Auto Scaling #PauseService API'
  slug: postman-aws-app-runner-pauseservice-api
- collection_type: postman
  name: 'AWS App Runner Auto Scaling #ResumeService API'
  slug: postman-aws-app-runner-resumeservice-api
- collection_type: postman
  name: 'AWS App Runner Auto Scaling #UpdateService API'
  slug: postman-aws-app-runner-updateservice-api
- collection_type: postman
  name: AWS App Runner Auto Scaling VPC API
  slug: postman-aws-app-runner-vpc-api
- collection_type: open
  name: AWS App Runner API
  slug: open-aws-app-runner
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/aws-app-runner/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-app-runner-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-app-runner-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-app-runner-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-app-runner-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-app-runner-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/apprunner/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/apprunner/pricing/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/apprunner/faqs/
- group: other
  title: ''
  type: Customers
  url: https://aws.amazon.com/apprunner/customers/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/apprunner/
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
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/containers/category/compute/aws-app-runner/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: design
  title: ''
  type: SpectralRules
  url: rules/aws-app-runner-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aws-app-runner-vocabulary.yaml
created: '2026-03-26'
description: AWS App Runner is a fully managed service that makes it easy to build, deploy, and run containerized web applications and APIs at scale. It automatically builds and deploys applications from container images or source code, load balances traffic with encryption, and scales to meet traffic needs without requiring infrastructure management. App Runner integrates with ECR, GitHub, Bitbucket, VPC, IAM, and CloudWatch for complete application delivery.
examples:
- key_count: 12
  name: App Runner Auto Scaling Configuration Example
  slug: app-runner-auto-scaling-configuration-example
- key_count: 7
  name: App Runner Auto Scaling Configuration Summary Example
  slug: app-runner-auto-scaling-configuration-summary-example
- key_count: 5
  name: App Runner Connection Example
  slug: app-runner-connection-example
- key_count: 5
  name: App Runner Connection Summary Example
  slug: app-runner-connection-summary-example
- key_count: 9
  name: App Runner Create Service Request Example
  slug: app-runner-create-service-request-example
- key_count: 4
  name: App Runner Custom Domain Example
  slug: app-runner-custom-domain-example
- key_count: 6
  name: App Runner Health Check Configuration Example
  slug: app-runner-health-check-configuration-example
- key_count: 3
  name: App Runner Instance Configuration Example
  slug: app-runner-instance-configuration-example
- key_count: 8
  name: App Runner Observability Configuration Example
  slug: app-runner-observability-configuration-example
- key_count: 7
  name: App Runner Operation Summary Example
  slug: app-runner-operation-summary-example
- key_count: 15
  name: App Runner Service Example
  slug: app-runner-service-example
- key_count: 7
  name: App Runner Service Summary Example
  slug: app-runner-service-summary-example
- key_count: 4
  name: App Runner Source Configuration Example
  slug: app-runner-source-configuration-example
- key_count: 2
  name: App Runner Tag Example
  slug: app-runner-tag-example
- key_count: 7
  name: App Runner Update Service Request Example
  slug: app-runner-update-service-request-example
- key_count: 8
  name: App Runner Vpc Connector Example
  slug: app-runner-vpc-connector-example
- key_count: 3
  name: App Runner Vpc Dns Target Example
  slug: app-runner-vpc-dns-target-example
features:
- description: Automatically builds container images from source code and deploys with zero configuration.
  name: Automatic Build and Deploy
- description: Scales automatically based on incoming request volume, with configurable min/max instances.
  name: Auto-Scaling
- description: Built-in load balancing with HTTPS encryption for all traffic to deployed services.
  name: Load Balancing
- description: Associate custom domain names with SSL/TLS certificates for branded endpoints.
  name: Custom Domains
- description: Connect to private VPC resources like RDS, ElastiCache, and internal services.
  name: VPC Integration
- description: Pause services to stop billing during idle periods and resume instantly when needed.
  name: Pause and Resume
- description: Integration with CloudWatch and X-Ray for metrics, logs, and distributed tracing.
  name: Observability
- description: Deploy directly from GitHub repositories or Amazon ECR container registries.
  name: GitHub and ECR Integration
finops:
- name: Aws App Runner Finops
  service_category: API
  slug: aws-app-runner-finops
graphqls:
- description: ''
  name: AWS App Runner GraphQL API
  slug: aws-app-runner-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-app-runner.png
json_schemas:
- name: AutoScalingConfiguration
  property_count: 12
  slug: app-runner-auto-scaling-configuration
- name: AutoScalingConfigurationSummary
  property_count: 7
  slug: app-runner-auto-scaling-configuration-summary
- name: Connection
  property_count: 5
  slug: app-runner-connection
- name: ConnectionSummary
  property_count: 5
  slug: app-runner-connection-summary
- name: CreateServiceRequest
  property_count: 9
  slug: app-runner-create-service-request
- name: CustomDomain
  property_count: 4
  slug: app-runner-custom-domain
- name: HealthCheckConfiguration
  property_count: 6
  slug: app-runner-health-check-configuration
- name: InstanceConfiguration
  property_count: 3
  slug: app-runner-instance-configuration
- name: ObservabilityConfiguration
  property_count: 8
  slug: app-runner-observability-configuration
- name: OperationSummary
  property_count: 7
  slug: app-runner-operation-summary
- name: Service
  property_count: 15
  slug: app-runner-service
- name: ServiceSummary
  property_count: 7
  slug: app-runner-service-summary
- name: SourceConfiguration
  property_count: 4
  slug: app-runner-source-configuration
- name: Tag
  property_count: 2
  slug: app-runner-tag
- name: UpdateServiceRequest
  property_count: 7
  slug: app-runner-update-service-request
- name: VpcConnector
  property_count: 8
  slug: app-runner-vpc-connector
- name: VpcDNSTarget
  property_count: 3
  slug: app-runner-vpc-dns-target
json_structures:
- name: App Runner Auto Scaling Configuration Structure
  property_count: 12
  slug: app-runner-auto-scaling-configuration-structure
- name: App Runner Auto Scaling Configuration Summary Structure
  property_count: 7
  slug: app-runner-auto-scaling-configuration-summary-structure
- name: App Runner Connection Structure
  property_count: 5
  slug: app-runner-connection-structure
- name: App Runner Connection Summary Structure
  property_count: 5
  slug: app-runner-connection-summary-structure
- name: App Runner Create Service Request Structure
  property_count: 9
  slug: app-runner-create-service-request-structure
- name: App Runner Custom Domain Structure
  property_count: 4
  slug: app-runner-custom-domain-structure
- name: App Runner Health Check Configuration Structure
  property_count: 6
  slug: app-runner-health-check-configuration-structure
- name: App Runner Instance Configuration Structure
  property_count: 3
  slug: app-runner-instance-configuration-structure
- name: App Runner Observability Configuration Structure
  property_count: 8
  slug: app-runner-observability-configuration-structure
- name: App Runner Operation Summary Structure
  property_count: 7
  slug: app-runner-operation-summary-structure
- name: App Runner Service Structure
  property_count: 15
  slug: app-runner-service-structure
- name: App Runner Service Summary Structure
  property_count: 7
  slug: app-runner-service-summary-structure
- name: App Runner Source Configuration Structure
  property_count: 4
  slug: app-runner-source-configuration-structure
- name: App Runner Tag Structure
  property_count: 2
  slug: app-runner-tag-structure
- name: App Runner Update Service Request Structure
  property_count: 7
  slug: app-runner-update-service-request-structure
- name: App Runner Vpc Connector Structure
  property_count: 8
  slug: app-runner-vpc-connector-structure
- name: App Runner Vpc Dns Target Structure
  property_count: 3
  slug: app-runner-vpc-dns-target-structure
jsonld:
- class_count: 12
  name: Aws App Runner Context
  property_count: 62
  slug: aws-app-runner-context
layout: provider
modified: '2026-05-19'
name: AWS App Runner
nav: Providers
network: true
overview: 'AWS App Runner publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Auto Scaling API, AWS App Runner API API, Connections API, and 10 more. Tagged areas include CI/CD, Containers, Deployment, Microservices, and Serverless.


  The AWS App Runner catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AWS App Runner''s developer surface includes authentication, documentation, pricing, FAQ, developer console, support, engineering blog, and 13 more developer resources.'
plans:
- name: Aws App Runner Plans Pricing
  plan_count: 3
  slug: aws-app-runner-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Aws App Runner Rate Limits
  slug: aws-app-runner-rate-limits
rules:
- name: AWS App Runner API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: aws-app-runner-jsonschema-spectral-rules
- name: AWS App Runner API Rules
  rule_count: 20
  severity_counts:
    error: 12
    hint: 0
    info: 0
    warn: 8
  slug: aws-app-runner-spectral-rules
score:
  band: developing
  composite: 55.6
  delta: -8.5
  facets:
    commercial_clarity: 55.3
    contract_quality: 70.9
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 28.9
  previous_composite: 64.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-app-runner/refs/heads/main/screenshots/aws-app-runner-2026-06-20T172739.png
security:
- kind: authentication
  name: Aws App Runner Authentication
  slug: aws-app-runner-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws App Runner Domain Security
  slug: aws-app-runner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws App Runner Vulnerability Disclosure
  slug: aws-app-runner-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws App Runner Trust Center
  slug: aws-app-runner-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-app-runner
tags:
- CI/CD
- Containers
- Deployment
- Microservices
- Serverless
use_cases:
- description: Deploy containerized web applications without managing servers, load balancers, or scaling.
  name: Web Application Deployment
- description: Host REST or GraphQL API backends with automatic scaling and HTTPS termination.
  name: API Backend Deployment
- description: Deploy individual microservices with isolated scaling and custom domain routing.
  name: Microservices Hosting
- description: Quickly spin up and tear down environments using pause/resume to minimize costs.
  name: Development and Staging Environments
website: https://aws.amazon.com/apprunner/
---
