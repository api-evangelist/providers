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
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Amazon Lambda Agentic Access
  operation_count: 11
  slug: amazon-lambda-agentic-access
  summary_line: 11 operations · 7 acting
api_count: 2
apis:
- description: Lambda event source mapping management
  name: Amazon Lambda Event Source Mappings API
  slug: amazon-lambda-event-source-mappings-api
- description: Lambda function management
  name: Amazon Lambda Functions API
  slug: amazon-lambda-functions-api
arazzos:
- description: Confirm a function exists, read its configuration, then delete it.
  name: Amazon Lambda Decommission Function
  slug: amazon-lambda-decommission-function-workflow
- description: Create a Lambda function, wait for it to become Active, then invoke it.
  name: Amazon Lambda Deploy and Invoke Function
  slug: amazon-lambda-deploy-and-invoke-function-workflow
- description: Create a function, wait until Active, attach an event source mapping, and wait until Enabled.
  name: Amazon Lambda Deploy Function With Event Source
  slug: amazon-lambda-deploy-with-event-source-workflow
- description: Create an event source mapping and poll it until it reaches the Enabled state.
  name: Amazon Lambda Provision Event Source Mapping
  slug: amazon-lambda-provision-event-source-mapping-workflow
- description: Change a function's runtime settings, wait for Active, then invoke to verify.
  name: Amazon Lambda Reconfigure Function
  slug: amazon-lambda-reconfigure-function-workflow
- description: List functions, select one by name, push new code, and wait until Active.
  name: Amazon Lambda Redeploy Discovered Function
  slug: amazon-lambda-redeploy-discovered-function-workflow
- description: Locate an event source mapping in the list, confirm its details, then delete it.
  name: Amazon Lambda Teardown Event Source Mapping
  slug: amazon-lambda-teardown-event-source-mapping-workflow
- description: Push new function code, wait for the update to settle, then invoke to verify.
  name: Amazon Lambda Update Code and Verify
  slug: amazon-lambda-update-code-and-verify-workflow
artifact_total: 50
collections:
- collection_type: postman
  name: Amazon Lambda API
  slug: postman-amazon-lambda
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Lambda Event Source Mappings API
  slug: open-amazon-lambda-event-source-mappings-api
- collection_type: open
  name: Amazon Lambda Event Source Mappings Functions API
  slug: open-amazon-lambda-functions-api
- collection_type: open
  name: Amazon Lambda API
  slug: open-amazon-lambda
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-lambda-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-lambda-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-lambda-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-lambda-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-lambda-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-lambda/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-lambda-decommission-function-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-lambda-deploy-and-invoke-function-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-lambda-deploy-with-event-source-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-lambda-provision-event-source-mapping-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-lambda-reconfigure-function-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-lambda-redeploy-discovered-function-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-lambda-teardown-event-source-mapping-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-lambda-update-code-and-verify-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/lambda/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/lambda/
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
  url: https://aws.amazon.com/blogs/compute/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/lambda/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: Knowledge Center
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-lambda
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-lambda-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-lambda-vocabulary.yaml
created: '2024-01-15'
description: AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers, automatically scaling and executing your code in response to events from over 200 AWS services and SaaS applications while you pay only for the compute time you consume.
examples:
- key_count: 5
  name: Amazon Lambda Event Source Mapping Example
  slug: amazon-lambda-event-source-mapping-example
- key_count: 12
  name: Amazon Lambda Function Example
  slug: amazon-lambda-function-example
features:
- description: Run code without provisioning or managing servers — Lambda handles all administration.
  name: Serverless Execution
- description: Automatically trigger code from over 200 AWS services and SaaS applications.
  name: Event-Driven Triggers
- description: Automatically scales to thousands of concurrent executions without configuration.
  name: Automatic Scaling
- description: Supports Node.js, Python, Java, Go, Ruby, .NET, and custom runtimes via Lambda layers.
  name: Multiple Runtimes
- description: Package and share code, libraries, and configurations across Lambda functions.
  name: Lambda Layers
- description: Deploy Lambda functions as container images up to 10 GB in size.
  name: Container Image Support
- description: Reduce cold starts for Java functions with Lambda SnapStart.
  name: SnapStart
finops:
- name: Amazon Lambda Finops
  service_category: API
  slug: amazon-lambda-finops
graphqls:
- description: ''
  name: Amazon Lambda GraphQL API
  slug: amazon-lambda-graphql
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Build REST and WebSocket APIs backed by Lambda functions.
  name: Amazon API Gateway
- description: Trigger Lambda from DynamoDB Streams for real-time data processing.
  name: Amazon DynamoDB
- description: Trigger Lambda on S3 object events for serverless file processing.
  name: Amazon S3
- description: Process Kinesis data streams with Lambda for real-time analytics.
  name: Amazon Kinesis
- description: Orchestrate Lambda functions in serverless workflows.
  name: AWS Step Functions
- description: Process SQS messages with Lambda for decoupled event processing.
  name: Amazon SQS
json_schemas:
- name: EventSourceMapping
  property_count: 5
  slug: amazon-lambda-event-source-mapping
- name: Function
  property_count: 12
  slug: amazon-lambda-function
json_structures:
- name: Amazon Lambda Event Source Mapping Structure
  property_count: 5
  slug: amazon-lambda-event-source-mapping-structure
- name: Amazon Lambda Function Structure
  property_count: 12
  slug: amazon-lambda-function-structure
jsonld:
- class_count: 2
  name: Amazon Lambda Context
  property_count: 7
  slug: amazon-lambda-context
layout: provider
modified: '2026-05-19'
name: Amazon Lambda
nav: Providers
network: true
overview: 'Amazon Lambda publishes 2 APIs on the [APIs.io](https://apis.io/) network: Event Source Mappings API and Functions API. Tagged areas include Compute, Event-Driven, FaaS, Functions, and Serverless.


  The Amazon Lambda catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Lambda''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 27 more developer resources.'
plans:
- name: Amazon Lambda Plans Pricing
  plan_count: 3
  slug: amazon-lambda-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Amazon Lambda Rate Limits
  slug: amazon-lambda-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Lambda API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-lambda-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: Amazon Lambda API Rules
  rule_count: 24
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 15
  slug: amazon-lambda-spectral-rules
score:
  band: strong
  composite: 54.5
  delta: -7.3
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 25.0
    contract_quality: 69.2
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 25.0
    operational_transparency: 36.8
  previous_composite: 61.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-lambda/refs/heads/main/screenshots/amazon-lambda-2026-06-20T171722.png
security:
- kind: authentication
  name: Amazon Lambda Authentication
  slug: amazon-lambda-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Lambda Domain Security
  slug: amazon-lambda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Lambda Vulnerability Disclosure
  slug: amazon-lambda-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Lambda Trust Center
  slug: amazon-lambda-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-lambda
tags:
- Compute
- Event-Driven
- FaaS
- Functions
- Serverless
use_cases:
- description: Build REST and GraphQL API backends with Lambda and API Gateway.
  name: API Backends
- description: Process S3 uploads, DynamoDB streams, and Kinesis records in real time.
  name: Data Processing
- description: Automate operational tasks triggered by CloudWatch events or schedules.
  name: Event Automation
- description: Run ML model inference on-demand without managing inference infrastructure.
  name: Machine Learning Inference
website: https://aws.amazon.com/
---
