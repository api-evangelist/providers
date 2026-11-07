---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amazon Cloudformation Agentic Access
  operation_count: 13
  slug: amazon-cloudformation-agentic-access
  summary_line: 13 operations
api_count: 1
apis:
- baseURL: https://cloudformation.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for managing stack resources
  name: Amazon CloudFormation Resources API
  slug: amazon-cloudformation-resources-api
- baseURL: https://cloudformation.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for managing CloudFormation stacks
  name: Amazon CloudFormation Stacks API
  slug: amazon-cloudformation-stacks-api
- baseURL: https://cloudformation.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for working with CloudFormation templates
  name: Amazon CloudFormation Templates API
  slug: amazon-cloudformation-templates-api
- baseURL: https://cloudformation.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for managing CloudFormation change sets
  name: Amazon CloudFormation Changesets API
  slug: amazon-cloudformation-changesets-api
- baseURL: https://cloudformation.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Cloudformation Generated Template API from Amazon CloudFormation — 6 operation(s) for cloudformation generated template.
  name: Amazon CloudFormation Cloudformation Generated Template API
  slug: amazon-cloudformation-generated-template-api
- baseURL: https://cloudformation.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Cloudformation Operations API from Amazon CloudFormation — 44 operation(s) for cloudformation operations.
  name: Amazon CloudFormation Cloudformation Operations API
  slug: amazon-cloudformation-operations-api
- baseURL: https://cloudformation.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Cloudformation Resource Scan API from Amazon CloudFormation — 3 operation(s) for cloudformation resource scan.
  name: Amazon CloudFormation Cloudformation Resource Scan API
  slug: amazon-cloudformation-resource-scan-api
- baseURL: https://cloudformation.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Cloudformation Stack Instance API from Amazon CloudFormation — 5 operation(s) for cloudformation stack instance.
  name: Amazon CloudFormation Cloudformation Stack Instance API
  slug: amazon-cloudformation-stack-instance-api
- baseURL: https://cloudformation.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Cloudformation Stack Refactor API from Amazon CloudFormation — 4 operation(s) for cloudformation stack refactor.
  name: Amazon CloudFormation Cloudformation Stack Refactor API
  slug: amazon-cloudformation-stack-refactor-api
- baseURL: https://cloudformation.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Cloudformation Stack Set API from Amazon CloudFormation — 5 operation(s) for cloudformation stack set.
  name: Amazon CloudFormation Cloudformation Stack Set API
  slug: amazon-cloudformation-stack-set-api
- baseURL: https://cloudformation.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Cloudformation Stack Set Operation API from Amazon CloudFormation — 3 operation(s) for cloudformation stack set operation.
  name: Amazon CloudFormation Cloudformation Stack Set Operation API
  slug: amazon-cloudformation-stack-set-operation-api
- baseURL: https://cloudformation.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Cloudformation Type API from Amazon CloudFormation — 5 operation(s) for cloudformation type.
  name: Amazon CloudFormation Cloudformation Type API
  slug: amazon-cloudformation-type-api
artifact_total: 88
collections:
- collection_type: open
  name: Amazon CloudFormation Change Sets API
  slug: open-amazon-cloudformation-change-sets-api
- collection_type: open
  name: Amazon CloudFormation Change Sets Resources API
  slug: open-amazon-cloudformation-resources-api
- collection_type: open
  name: Amazon CloudFormation Change Sets Stacks API
  slug: open-amazon-cloudformation-stacks-api
- collection_type: open
  name: Amazon CloudFormation Change Sets Templates API
  slug: open-amazon-cloudformation-templates-api
common:
- group: commercial
  href: https://artifacts.apis.io/amazon-cloudformation/plans/amazon-cloudformation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-cloudformation-plans-pricing.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-cloudformation/overview
- group: other
  href: https://artifacts.apis.io/amazon-cloudformation/capabilities/amazon-cloudformation-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-cloudformation-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/amazon-cloudformation/overlays/amazon-cloudformation-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amazon-cloudformation-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/awslabs/mcp/tree/main/src/aws-iac-mcp-server
- group: agent
  href: https://artifacts.apis.io/amazon-cloudformation/agentic-access/amazon-cloudformation-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-cloudformation-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-cloudformation/security/amazon-cloudformation-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-cloudformation-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-cloudformation/security/amazon-cloudformation-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-cloudformation-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-cloudformation/security/amazon-cloudformation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-cloudformation-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amazon-cloudformation/authentication/amazon-cloudformation-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-cloudformation-authentication.yml
- group: agent
  href: https://artifacts.apis.io/amazon-cloudformation/well-known/amazon-cloudformation-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazon-cloudformation-well-known.yml
- group: auth
  href: https://artifacts.apis.io/amazon-cloudformation/well-known/amazon-cloudformation-security.txt
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
  href: https://artifacts.apis.io/amazon-cloudformation/rules/amazon-cloudformation-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-cloudformation-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-cloudformation/vocabulary/amazon-cloudformation-vocabulary.yaml
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
finops:
- has_sources: true
  method: derived
  name: Amazon Cloudformation Finops
  primary_unit: handler operations
  service_category: ''
  slug: amazon-cloudformation-finops
  template: false
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
mcp_servers:
- description: ''
  name: AWS IaC MCP Server
  slug: aws-iac-mcp-server
- description: Local (stdio) MCP server; 8 tools listed.
  name: Amazon CloudFormation MCP Server
  slug: awslabs-cfn-mcp-server
modified: '2026-09-16'
name: Amazon CloudFormation
nav: Providers
network: true
overview: 'Amazon CloudFormation publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Resources API, Stacks API, Templates API, and 9 more. Tagged areas include Amazon Web Services, CloudFormation, Infrastructure as Code, DevOps, and IaC.


  The Amazon CloudFormation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon CloudFormation''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 22 more developer resources.'
plans:
- name: Amazon Cloudformation Plans Pricing
  plan_count: 3
  slug: amazon-cloudformation-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Amazon CloudFormation — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: amazon-cloudformation-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 65
  extends:
  - spectral:oas
  name: Amazon CloudFormation API Rules
  rule_count: 24
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 11
  slug: amazon-cloudformation-spectral-rules
score:
  band: exemplar
  composite: 69.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 81.0
    catalog_earned_first_party: 12.0
    catalog_gap: 34.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.7
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 70.0
    developer_ergonomics: 72.6
    discoverability: 71.7
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 67.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 66.7
      total: 12
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/amazon-cloudformation/amazon-cloudformation-2026-07-25T195946.png
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
- Amazon Web Services
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
