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
    idempotency: verified
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 49
  human_in_the_loop: 1
  name: Cloudformation Agentic Access
  operation_count: 49
  slug: cloudformation-agentic-access
  summary_line: 49 operations · 49 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: Operations for creating and managing change sets to preview stack changes.
  name: AWS CloudFormation Change Sets API
  slug: cloudformation-change-sets-api
- description: Operations for listing stack exports and imports.
  name: AWS CloudFormation Exports API
  slug: cloudformation-exports-api
- description: Operations for managing extension types in the CloudFormation Registry.
  name: AWS CloudFormation Registry API
  slug: cloudformation-registry-api
- description: Operations for tracking the status of asynchronous resource operations and cancelling in-progress requests.
  name: AWS CloudFormation Request Status API
  slug: cloudformation-request-status-api
- description: CRUDL operations for creating, reading, updating, deleting, and listing cloud resources through a uniform interface.
  name: AWS CloudFormation Resources API
  slug: cloudformation-resources-api
- description: Operations for detecting and describing configuration drift.
  name: AWS CloudFormation Stack Drift API
  slug: cloudformation-stack-drift-api
- description: Operations for retrieving stack-related events.
  name: AWS CloudFormation Stack Events API
  slug: cloudformation-stack-events-api
- description: Operations for managing stack instances within a stack set.
  name: AWS CloudFormation Stack Instances API
  slug: cloudformation-stack-instances-api
- description: Operations for getting and setting stack policies.
  name: AWS CloudFormation Stack Policies API
  slug: cloudformation-stack-policies-api
- description: Operations for describing resources within a stack.
  name: AWS CloudFormation Stack Resources API
  slug: cloudformation-stack-resources-api
- description: Operations for managing stack sets across multiple accounts and regions.
  name: AWS CloudFormation Stack Sets API
  slug: cloudformation-stack-sets-api
- description: Operations for creating, updating, deleting, and describing CloudFormation stacks.
  name: AWS CloudFormation Stacks API
  slug: cloudformation-stacks-api
- description: Operations for retrieving, validating, and summarizing templates.
  name: AWS CloudFormation Templates API
  slug: cloudformation-templates-api
arazzos:
- description: List the account's stack exports, then list the stacks that import a named export.
  name: CloudFormation Audit Cross-Stack Exports
  slug: cloudformation-audit-exports-workflow
- description: Create a change set, poll until CREATE_COMPLETE, execute it, then wait for the stack update to finish.
  name: CloudFormation Create and Execute a Change Set
  slug: cloudformation-change-set-deploy-workflow
- description: Create a stack set, roll out an instance to an account and region, then poll the instance until CURRENT.
  name: CloudFormation Deploy a Stack Set
  slug: cloudformation-deploy-stack-set-workflow
- description: Start drift detection, poll until detection completes, then list the drifted resources.
  name: CloudFormation Detect Stack Drift
  slug: cloudformation-detect-stack-drift-workflow
- description: Describe a single stack resource, then run targeted drift detection against just that resource.
  name: CloudFormation Inspect a Stack Resource
  slug: cloudformation-inspect-stack-resource-workflow
- description: Validate a template, create a stack, poll until CREATE_COMPLETE, then list its resources.
  name: CloudFormation Provision a Stack
  slug: cloudformation-provision-stack-workflow
- description: Create a change set, poll until it is computed, then branch — delete it when it contains no changes, otherwise keep it for review.
  name: CloudFormation Review and Clean Up a Change Set
  slug: cloudformation-review-change-set-workflow
- description: Summarize a template, update the stack, poll until UPDATE_COMPLETE, then pull the stack events.
  name: CloudFormation Safe Stack Update
  slug: cloudformation-safe-stack-update-workflow
- description: Disable termination protection, delete the stack, then poll until DELETE_COMPLETE.
  name: CloudFormation Tear Down a Stack
  slug: cloudformation-teardown-stack-workflow
artifact_total: 158
collections:
- collection_type: postman
  name: AWS Cloud Control API
  slug: postman-cloud-control-api
- collection_type: postman
  name: AWS CloudFormation API
  slug: postman-cloudformation-api
- collection_type: open
  name: AWS Cloud Control API
  slug: open-cloud-control-api
- collection_type: open
  name: AWS CloudFormation API
  slug: open-cloudformation-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudformation-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cloudformation-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudformation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudformation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudformation-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/aws-cloudformation/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cloudformation-audit-exports-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cloudformation-change-set-deploy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cloudformation-deploy-stack-set-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cloudformation-detect-stack-drift-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cloudformation-inspect-stack-resource-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cloudformation-provision-stack-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cloudformation-review-change-set-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cloudformation-safe-stack-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cloudformation-teardown-stack-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/cloudformation/resources/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/cloudformation/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/cloudformation/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/devops/category/management-tools/aws-cloudformation/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudformation/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws-cloudformation
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/aws-cloudformation/aws-cloudformation-templates
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-cloudformation
- group: build
  title: Python SDK (Boto3)
  type: SDKs
  url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html
- group: build
  title: JavaScript SDK v3
  type: SDKs
  url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/cloudformation-examples.html
- group: build
  title: Java SDK
  type: SDKs
  url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-cloudformation.html
- group: build
  title: Go SDK
  type: SDKs
  url: https://docs.aws.amazon.com/sdk-for-go/api/service/cloudformation/
- group: build
  title: AWS CLI - CloudFormation
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/cloudformation/
- group: build
  title: Rain - CloudFormation CLI
  type: CLI
  url: https://github.com/aws-cloudformation/rain
- group: docs
  title: Stack Schema
  type: JSONSchema
  url: json-schema/stack.json
- group: docs
  title: Template Schema
  type: JSONSchema
  url: json-schema/template.json
- group: docs
  title: Resource Schema
  type: JSONSchema
  url: json-schema/resource.json
- group: docs
  title: Change Set Schema
  type: JSONSchema
  url: json-schema/change-set.json
- group: docs
  title: Change Schema
  type: JSONSchema
  url: json-schema/cloudformation-change-schema.json
- group: docs
  title: Change Set Detail Schema
  type: JSONSchema
  url: json-schema/cloudformation-change-set-detail-schema.json
- group: docs
  title: Change Set Summary Schema
  type: JSONSchema
  url: json-schema/cloudformation-change-set-summary-schema.json
- group: docs
  title: Error Response Schema
  type: JSONSchema
  url: json-schema/cloudformation-error-response-schema.json
- group: docs
  title: Stack Detail Schema
  type: JSONSchema
  url: json-schema/cloudformation-stack-schema.json
- group: docs
  title: Stack Event Schema
  type: JSONSchema
  url: json-schema/cloudformation-stack-event-schema.json
- group: docs
  title: Stack Resource Schema
  type: JSONSchema
  url: json-schema/cloudformation-stack-resource-schema.json
- group: docs
  title: Stack Summary Schema
  type: JSONSchema
  url: json-schema/cloudformation-stack-summary-schema.json
- group: docs
  title: Tag Schema
  type: JSONSchema
  url: json-schema/cloudformation-tag-schema.json
- group: docs
  title: Cloud Control Progress Event Schema
  type: JSONSchema
  url: json-schema/cloud-control-progress-event-schema.json
- group: docs
  title: Cloud Control Resource Description Schema
  type: JSONSchema
  url: json-schema/cloud-control-resource-description-schema.json
- group: docs
  title: Cloud Control Error Response Schema
  type: JSONSchema
  url: json-schema/cloud-control-error-response-schema.json
- group: design
  title: JSON-LD Context
  type: JSONLD
  url: json-ld/context.jsonld
- group: design
  title: CloudFormation JSON-LD Context
  type: JSONLD
  url: json-ld/cloudformation-context.jsonld
- group: design
  title: Cloud Control JSON-LD Context
  type: JSONLD
  url: json-ld/cloud-control-context.jsonld
- group: design
  title: CloudFormation Vocabulary
  type: Vocabulary
  url: vocabulary/cloudformation-vocabulary.yaml
- group: design
  title: Spectral Rules
  type: Rules
  url: rules/cloudformation-spectral-rules.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://aws.amazon.com/blogs/devops/introducing-the-aws-infrastructure-as-code-mcp-server-ai-powered-cdk-and-cloudformation-assistance/
created: '2024'
description: A collection of APIs provided by AWS for infrastructure as code provisioning and management of AWS and third-party resources using CloudFormation templates and the Cloud Control API.
examples:
- key_count: 2
  name: Cloud Control Error Response Example
  slug: cloud-control-error-response-example
- key_count: 8
  name: Cloud Control Hook Progress Event Example
  slug: cloud-control-hook-progress-event-example
- key_count: 11
  name: Cloud Control Progress Event Example
  slug: cloud-control-progress-event-example
- key_count: 2
  name: Cloud Control Resource Description Example
  slug: cloud-control-resource-description-example
- key_count: 1
  name: Cloudformation Change Example
  slug: cloudformation-change-example
- key_count: 16
  name: Cloudformation Change Set Detail Example
  slug: cloudformation-change-set-detail-example
- key_count: 13
  name: Cloudformation Change Set Summary Example
  slug: cloudformation-change-set-summary-example
- key_count: 2
  name: Cloudformation Error Response Example
  slug: cloudformation-error-response-example
- key_count: 3
  name: Cloudformation Export Example
  slug: cloudformation-export-example
- key_count: 2
  name: Cloudformation Module Info Example
  slug: cloudformation-module-info-example
- key_count: 4
  name: Cloudformation Output Example
  slug: cloudformation-output-example
- key_count: 6
  name: Cloudformation Parameter Declaration Example
  slug: cloudformation-parameter-declaration-example
- key_count: 4
  name: Cloudformation Parameter Example
  slug: cloudformation-parameter-example
- key_count: 4
  name: Cloudformation Property Difference Example
  slug: cloudformation-property-difference-example
- key_count: 4
  name: Cloudformation Resource Change Detail Example
  slug: cloudformation-resource-change-detail-example
- key_count: 7
  name: Cloudformation Resource Change Example
  slug: cloudformation-resource-change-example
- key_count: 2
  name: Cloudformation Rollback Configuration Example
  slug: cloudformation-rollback-configuration-example
- key_count: 2
  name: Cloudformation Rollback Trigger Example
  slug: cloudformation-rollback-trigger-example
- key_count: 2
  name: Cloudformation Stack Drift Information Example
  slug: cloudformation-stack-drift-information-example
- key_count: 16
  name: Cloudformation Stack Event Example
  slug: cloudformation-stack-event-example
- key_count: 22
  name: Cloudformation Stack Example
  slug: cloudformation-stack-example
- key_count: 10
  name: Cloudformation Stack Instance Example
  slug: cloudformation-stack-instance-example
- key_count: 8
  name: Cloudformation Stack Instance Summary Example
  slug: cloudformation-stack-instance-summary-example
- key_count: 10
  name: Cloudformation Stack Resource Drift Example
  slug: cloudformation-stack-resource-drift-example
- key_count: 2
  name: Cloudformation Stack Resource Drift Information Example
  slug: cloudformation-stack-resource-drift-information-example
- key_count: 9
  name: Cloudformation Stack Resource Example
  slug: cloudformation-stack-resource-example
- key_count: 6
  name: Cloudformation Stack Resource Summary Example
  slug: cloudformation-stack-resource-summary-example
- key_count: 12
  name: Cloudformation Stack Set Example
  slug: cloudformation-stack-set-example
- key_count: 6
  name: Cloudformation Stack Set Operation Preferences Example
  slug: cloudformation-stack-set-operation-preferences-example
- key_count: 7
  name: Cloudformation Stack Set Summary Example
  slug: cloudformation-stack-set-summary-example
- key_count: 0
  name: Cloudformation Stack Status Example
  slug: cloudformation-stack-status-example
- key_count: 9
  name: Cloudformation Stack Summary Example
  slug: cloudformation-stack-summary-example
- key_count: 2
  name: Cloudformation Tag Example
  slug: cloudformation-tag-example
- key_count: 12
  name: Cloudformation Type Summary Example
  slug: cloudformation-type-summary-example
features:
- description: Define and provision AWS infrastructure using declarative JSON/YAML templates
  name: Infrastructure As Code
- description: Create, update, and delete collections of AWS resources as a single unit
  name: Stack Management
- description: Preview changes before applying them to running stacks
  name: Change Sets
- description: Detect when stack resources have been modified outside of CloudFormation
  name: Drift Detection
- description: Deploy stacks across multiple accounts and regions simultaneously
  name: Stack Sets
- description: Uniform interface for managing any resource in the CloudFormation Registry
  name: Cloud Control CRUDL
finops:
- name: Cloudformation Finops
  service_category: API
  slug: cloudformation-finops
image: https://aws.amazon.com/cloudformation/logo.png
integrations:
- description: Define cloud infrastructure using familiar programming languages that compile to CloudFormation
  name: AWS CDK
- description: Simplified syntax for serverless application deployment via CloudFormation
  name: AWS SAM
- description: Alternative IaC tool that can import/export CloudFormation templates
  name: Terraform
json_schemas:
- name: AWS CloudFormation Change Set
  property_count: 20
  slug: change-set
- name: ErrorResponse
  property_count: 2
  slug: cloud-control-error-response
- name: HookProgressEvent
  property_count: 8
  slug: cloud-control-hook-progress-event
- name: ProgressEvent
  property_count: 11
  slug: cloud-control-progress-event
- name: ResourceDescription
  property_count: 2
  slug: cloud-control-resource-description
- name: Change
  property_count: 1
  slug: cloudformation-change
- name: ChangeSetDetail
  property_count: 16
  slug: cloudformation-change-set-detail
- name: ChangeSetSummary
  property_count: 13
  slug: cloudformation-change-set-summary
- name: ErrorResponse
  property_count: 2
  slug: cloudformation-error-response
- name: Export
  property_count: 3
  slug: cloudformation-export
- name: ModuleInfo
  property_count: 2
  slug: cloudformation-module-info
- name: Output
  property_count: 4
  slug: cloudformation-output
- name: ParameterDeclaration
  property_count: 6
  slug: cloudformation-parameter-declaration
- name: Parameter
  property_count: 4
  slug: cloudformation-parameter
- name: PropertyDifference
  property_count: 4
  slug: cloudformation-property-difference
- name: ResourceChangeDetail
  property_count: 4
  slug: cloudformation-resource-change-detail
- name: ResourceChange
  property_count: 7
  slug: cloudformation-resource-change
- name: RollbackConfiguration
  property_count: 2
  slug: cloudformation-rollback-configuration
- name: RollbackTrigger
  property_count: 2
  slug: cloudformation-rollback-trigger
- name: StackDriftInformation
  property_count: 2
  slug: cloudformation-stack-drift-information
- name: StackEvent
  property_count: 16
  slug: cloudformation-stack-event
- name: StackInstance
  property_count: 10
  slug: cloudformation-stack-instance
- name: StackInstanceSummary
  property_count: 8
  slug: cloudformation-stack-instance-summary
- name: StackResourceDriftInformation
  property_count: 2
  slug: cloudformation-stack-resource-drift-information
- name: StackResourceDrift
  property_count: 10
  slug: cloudformation-stack-resource-drift
- name: StackResource
  property_count: 9
  slug: cloudformation-stack-resource
- name: StackResourceSummary
  property_count: 6
  slug: cloudformation-stack-resource-summary
- name: Stack
  property_count: 22
  slug: cloudformation-stack
- name: StackSetOperationPreferences
  property_count: 6
  slug: cloudformation-stack-set-operation-preferences
- name: StackSet
  property_count: 12
  slug: cloudformation-stack-set
- name: StackSetSummary
  property_count: 7
  slug: cloudformation-stack-set-summary
- name: StackStatus
  property_count: 0
  slug: cloudformation-stack-status
- name: StackSummary
  property_count: 9
  slug: cloudformation-stack-summary
- name: Tag
  property_count: 2
  slug: cloudformation-tag
- name: TypeSummary
  property_count: 12
  slug: cloudformation-type-summary
- name: AWS CloudFormation Stack Resource
  property_count: 11
  slug: resource
- name: AWS CloudFormation Stack
  property_count: 25
  slug: stack
- name: AWS CloudFormation Template
  property_count: 10
  slug: template
json_structures:
- name: Cloud Control Error Response Structure
  property_count: 2
  slug: cloud-control-error-response-structure
- name: Cloud Control Hook Progress Event Structure
  property_count: 8
  slug: cloud-control-hook-progress-event-structure
- name: Cloud Control Progress Event Structure
  property_count: 11
  slug: cloud-control-progress-event-structure
- name: Cloud Control Resource Description Structure
  property_count: 2
  slug: cloud-control-resource-description-structure
- name: Cloudformation Change Set Detail Structure
  property_count: 16
  slug: cloudformation-change-set-detail-structure
- name: Cloudformation Change Set Summary Structure
  property_count: 13
  slug: cloudformation-change-set-summary-structure
- name: Cloudformation Change Structure
  property_count: 1
  slug: cloudformation-change-structure
- name: Cloudformation Error Response Structure
  property_count: 2
  slug: cloudformation-error-response-structure
- name: Cloudformation Export Structure
  property_count: 3
  slug: cloudformation-export-structure
- name: Cloudformation Module Info Structure
  property_count: 2
  slug: cloudformation-module-info-structure
- name: Cloudformation Output Structure
  property_count: 4
  slug: cloudformation-output-structure
- name: Cloudformation Parameter Declaration Structure
  property_count: 6
  slug: cloudformation-parameter-declaration-structure
- name: Cloudformation Parameter Structure
  property_count: 4
  slug: cloudformation-parameter-structure
- name: Cloudformation Property Difference Structure
  property_count: 4
  slug: cloudformation-property-difference-structure
- name: Cloudformation Resource Change Detail Structure
  property_count: 4
  slug: cloudformation-resource-change-detail-structure
- name: Cloudformation Resource Change Structure
  property_count: 7
  slug: cloudformation-resource-change-structure
- name: Cloudformation Rollback Configuration Structure
  property_count: 2
  slug: cloudformation-rollback-configuration-structure
- name: Cloudformation Rollback Trigger Structure
  property_count: 2
  slug: cloudformation-rollback-trigger-structure
- name: Cloudformation Stack Drift Information Structure
  property_count: 2
  slug: cloudformation-stack-drift-information-structure
- name: Cloudformation Stack Event Structure
  property_count: 16
  slug: cloudformation-stack-event-structure
- name: Cloudformation Stack Instance Structure
  property_count: 10
  slug: cloudformation-stack-instance-structure
- name: Cloudformation Stack Instance Summary Structure
  property_count: 8
  slug: cloudformation-stack-instance-summary-structure
- name: Cloudformation Stack Resource Drift Information Structure
  property_count: 2
  slug: cloudformation-stack-resource-drift-information-structure
- name: Cloudformation Stack Resource Drift Structure
  property_count: 10
  slug: cloudformation-stack-resource-drift-structure
- name: Cloudformation Stack Resource Structure
  property_count: 9
  slug: cloudformation-stack-resource-structure
- name: Cloudformation Stack Resource Summary Structure
  property_count: 6
  slug: cloudformation-stack-resource-summary-structure
- name: Cloudformation Stack Set Operation Preferences Structure
  property_count: 6
  slug: cloudformation-stack-set-operation-preferences-structure
- name: Cloudformation Stack Set Structure
  property_count: 12
  slug: cloudformation-stack-set-structure
- name: Cloudformation Stack Set Summary Structure
  property_count: 7
  slug: cloudformation-stack-set-summary-structure
- name: Cloudformation Stack Status Structure
  property_count: 0
  slug: cloudformation-stack-status-structure
- name: Cloudformation Stack Structure
  property_count: 22
  slug: cloudformation-stack-structure
- name: Cloudformation Stack Summary Structure
  property_count: 9
  slug: cloudformation-stack-summary-structure
- name: Cloudformation Tag Structure
  property_count: 2
  slug: cloudformation-tag-structure
- name: Cloudformation Type Summary Structure
  property_count: 12
  slug: cloudformation-type-summary-structure
jsonld:
- class_count: 0
  name: Cloud Control Context
  property_count: 0
  slug: cloud-control-context
- class_count: 0
  name: Cloudformation Context
  property_count: 0
  slug: cloudformation-context
- class_count: 0
  name: context Context
  property_count: 8
  slug: context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: AWS CloudFormation
nav: Providers
network: true
overview: 'AWS CloudFormation publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Change Sets API, Exports API, Registry API, and 10 more. Tagged areas include Automation, Cloud Resources, IaC, Infrastructure As Code, and Stack Management.


  The AWS CloudFormation catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  AWS CloudFormation''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, engineering blog, developer console, and 49 more developer resources.'
plans:
- name: Cloudformation Plans Pricing
  plan_count: 3
  slug: cloudformation-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Cloudformation Rate Limits
  slug: cloudformation-rate-limits
rules:
- name: AWS CloudFormation API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: cloudformation-jsonschema-spectral-rules
- name: AWS CloudFormation API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 9
  slug: cloudformation-spectral-rules
score:
  band: exemplar
  composite: 72.6
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 72.1
    developer_ergonomics: 82.6
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 72.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudformation/refs/heads/main/screenshots/cloudformation-2026-06-20T174600.png
security:
- kind: authentication
  name: Cloudformation Authentication
  slug: cloudformation-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cloudformation Domain Security
  slug: cloudformation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cloudformation Vulnerability Disclosure
  slug: cloudformation-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cloudformation Trust Center
  slug: cloudformation-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: cloudformation
tags:
- Automation
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
use_cases:
- description: Deploy consistent infrastructure across multiple AWS accounts with Stack Sets
  name: Multi-Account Deployment
- description: Spin up identical dev, staging, and production environments from templates
  name: Environment Provisioning
- description: Detect configuration drift and enforce infrastructure compliance
  name: Compliance Auditing
website: https://aws.amazon.com/cloudformation/resources/
---
