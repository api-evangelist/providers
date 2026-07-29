---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amazon Cloudformation Agentic Access
  operation_count: 13
  slug: amazon-cloudformation-agentic-access
  summary_line: 13 operations
api_count: 4
apis:
- description: Operations for managing CloudFormation change sets
  name: Amazon CloudFormation Change Sets API
  slug: amazon-cloudformation-change-sets-api
- description: Operations for managing stack resources
  name: Amazon CloudFormation Resources API
  slug: amazon-cloudformation-resources-api
- description: Operations for managing CloudFormation stacks
  name: Amazon CloudFormation Stacks API
  slug: amazon-cloudformation-stacks-api
- description: Operations for working with CloudFormation templates
  name: Amazon CloudFormation Templates API
  slug: amazon-cloudformation-templates-api
artifact_total: 72
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-cloudformation-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-cloudformation-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-cloudformation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-cloudformation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-cloudformation-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-cloudformation-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-cloudformation-security.txt
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/cloudformation/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/
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
  url: https://aws.amazon.com/blogs/devops/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudformation/
- group: start
  title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-cloudformation
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-cloudformation-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloudformation-vocabulary.yaml
created: '2024-01-01'
description: AWS CloudFormation is an infrastructure-as-code service that speeds up cloud provisioning by enabling developers to define and manage AWS resources programmatically through templates. Scale infrastructure globally and manage resources across all AWS accounts and regions through a single operation.
examples:
- key_count: 2
  name: Cloudformation Change Example
  slug: cloudformation-change-example
- key_count: 10
  name: Cloudformation Change Set Example
  slug: cloudformation-change-set-example
- key_count: 2
  name: Cloudformation Create Change Set Output Example
  slug: cloudformation-create-change-set-output-example
- key_count: 1
  name: Cloudformation Create Stack Output Example
  slug: cloudformation-create-stack-output-example
- key_count: 2
  name: Cloudformation Describe Stacks Output Example
  slug: cloudformation-describe-stacks-output-example
- key_count: 2
  name: Cloudformation List Stacks Output Example
  slug: cloudformation-list-stacks-output-example
- key_count: 4
  name: Cloudformation Output Example
  slug: cloudformation-output-example
- key_count: 4
  name: Cloudformation Parameter Example
  slug: cloudformation-parameter-example
- key_count: 2
  name: Cloudformation Rollback Configuration Example
  slug: cloudformation-rollback-configuration-example
- key_count: 2
  name: Cloudformation Stack Drift Information Example
  slug: cloudformation-stack-drift-information-example
- key_count: 20
  name: Cloudformation Stack Example
  slug: cloudformation-stack-example
- key_count: 2
  name: Cloudformation Stack Resource Drift Information Example
  slug: cloudformation-stack-resource-drift-information-example
- key_count: 10
  name: Cloudformation Stack Resource Example
  slug: cloudformation-stack-resource-example
- key_count: 2
  name: Cloudformation Tag Example
  slug: cloudformation-tag-example
- key_count: 1
  name: Cloudformation Update Stack Output Example
  slug: cloudformation-update-stack-output-example
features:
- description: Define AWS resources in JSON or YAML templates for repeatable, version-controlled deployments.
  name: Infrastructure as Code
- description: Deploy stacks across multiple AWS accounts and regions with a single operation.
  name: Multi-Account Stack Sets
- description: Preview changes to running stacks before executing them to avoid unintended updates.
  name: Change Sets
- description: Detect when deployed infrastructure has drifted from the CloudFormation template definition.
  name: Drift Detection
- description: Extend CloudFormation to manage third-party and community resources through the Registry.
  name: Registry Extensions
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-cloudformation.png
integrations:
- description: Automate CloudFormation deployments in CI/CD pipelines.
  name: AWS CodePipeline
- description: Track infrastructure changes and detect drift with Config integration.
  name: AWS Config
- description: Control who can create and update CloudFormation stacks.
  name: AWS IAM
- description: Publish approved CloudFormation templates as self-service products.
  name: AWS Service Catalog
- description: Receive stack event notifications via SNS topics.
  name: Amazon SNS
json_schemas:
- name: Amazon CloudFormation Stack
  property_count: 21
  slug: amazon-cloudformation-stack
- name: Change
  property_count: 2
  slug: cloudformation-change
- name: ChangeSet
  property_count: 10
  slug: cloudformation-change-set
- name: CreateChangeSetOutput
  property_count: 2
  slug: cloudformation-create-change-set-output
- name: CreateStackOutput
  property_count: 1
  slug: cloudformation-create-stack-output
- name: DescribeStacksOutput
  property_count: 2
  slug: cloudformation-describe-stacks-output
- name: ListStacksOutput
  property_count: 2
  slug: cloudformation-list-stacks-output
- name: Output
  property_count: 4
  slug: cloudformation-output
- name: Parameter
  property_count: 4
  slug: cloudformation-parameter
- name: RollbackConfiguration
  property_count: 2
  slug: cloudformation-rollback-configuration
- name: StackDriftInformation
  property_count: 2
  slug: cloudformation-stack-drift-information
- name: StackResourceDriftInformation
  property_count: 2
  slug: cloudformation-stack-resource-drift-information
- name: StackResource
  property_count: 10
  slug: cloudformation-stack-resource
- name: Stack
  property_count: 20
  slug: cloudformation-stack
- name: Tag
  property_count: 2
  slug: cloudformation-tag
- name: UpdateStackOutput
  property_count: 1
  slug: cloudformation-update-stack-output
json_structures:
- name: Cloudformation Change Set Structure
  property_count: 10
  slug: cloudformation-change-set-structure
- name: Cloudformation Change Structure
  property_count: 2
  slug: cloudformation-change-structure
- name: Cloudformation Create Change Set Output Structure
  property_count: 2
  slug: cloudformation-create-change-set-output-structure
- name: Cloudformation Create Stack Output Structure
  property_count: 1
  slug: cloudformation-create-stack-output-structure
- name: Cloudformation Describe Stacks Output Structure
  property_count: 2
  slug: cloudformation-describe-stacks-output-structure
- name: Cloudformation List Stacks Output Structure
  property_count: 2
  slug: cloudformation-list-stacks-output-structure
- name: Cloudformation Output Structure
  property_count: 4
  slug: cloudformation-output-structure
- name: Cloudformation Parameter Structure
  property_count: 4
  slug: cloudformation-parameter-structure
- name: Cloudformation Rollback Configuration Structure
  property_count: 2
  slug: cloudformation-rollback-configuration-structure
- name: Cloudformation Stack Drift Information Structure
  property_count: 2
  slug: cloudformation-stack-drift-information-structure
- name: Cloudformation Stack Resource Drift Information Structure
  property_count: 2
  slug: cloudformation-stack-resource-drift-information-structure
- name: Cloudformation Stack Resource Structure
  property_count: 10
  slug: cloudformation-stack-resource-structure
- name: Cloudformation Stack Structure
  property_count: 20
  slug: cloudformation-stack-structure
- name: Cloudformation Tag Structure
  property_count: 2
  slug: cloudformation-tag-structure
- name: Cloudformation Update Stack Output Structure
  property_count: 1
  slug: cloudformation-update-stack-output-structure
jsonld:
- class_count: 16
  name: Amazon Cloudformation Context
  property_count: 50
  slug: amazon-cloudformation-context
layout: provider
modified: '2026-06-20'
name: Amazon CloudFormation
nav: Providers
network: true
overview: 'Amazon CloudFormation publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Change Sets API, Resources API, Stacks API, and 1 more. Tagged areas include CloudFormation, Infrastructure as Code, DevOps, and IaC.


  The Amazon CloudFormation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon CloudFormation''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 17 more developer resources.'
random_paper: 68
rules:
- name: Amazon CloudFormation API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: amazon-cloudformation-jsonschema-spectral-rules
- name: Amazon CloudFormation API Rules
  rule_count: 24
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 11
  slug: amazon-cloudformation-spectral-rules
score:
  band: strong
  composite: 58.9
  delta: -1.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 79.7
    developer_ergonomics: 41.3
    discoverability: 83.3
    governance: 80.2
    operational_transparency: 21.1
  previous_composite: 59.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-cloudformation/refs/heads/main/screenshots/amazon-cloudformation-2026-07-25T195946.png
security:
- kind: authentication
  name: Amazon Cloudformation Authentication
  slug: amazon-cloudformation-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Cloudformation Domain Security
  slug: amazon-cloudformation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Cloudformation Vulnerability Disclosure
  slug: amazon-cloudformation-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Cloudformation Trust Center
  slug: amazon-cloudformation-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-cloudformation
tags:
- CloudFormation
- Infrastructure as Code
- DevOps
- IaC
use_cases:
- description: Automate infrastructure testing and deployment through CI/CD pipelines.
  name: DevOps Automation
- description: Deploy consistent infrastructure across multiple AWS regions.
  name: Multi-Region Deployment
- description: Enforce organizational infrastructure standards through template guardrails.
  name: Compliance Governance
- description: Rapidly rebuild infrastructure from templates after failures.
  name: Disaster Recovery
website: https://aws.amazon.com/cloudformation/
---
