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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Amazon Serverless Application Repository Agentic Access
  operation_count: 10
  slug: amazon-serverless-application-repository-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 4
apis:
- description: Serverless application management
  name: Amazon Serverless Application Repository Applications API
  slug: amazon-serverless-application-repository-applications-api
- description: CloudFormation changeset management
  name: Amazon Serverless Application Repository Changesets API
  slug: amazon-serverless-application-repository-changesets-api
- description: Application policy management
  name: Amazon Serverless Application Repository Policies API
  slug: amazon-serverless-application-repository-policies-api
- description: Application version management
  name: Amazon Serverless Application Repository Versions API
  slug: amazon-serverless-application-repository-versions-api
arazzos:
- description: List owned applications, inspect the first one in detail, and enumerate its published versions.
  name: AWS SAR Browse And Inspect Applications
  slug: amazon-serverless-application-repository-browse-applications-workflow
- description: Confirm an application exists by reading it, then delete it to decommission it.
  name: AWS SAR Decommission Application
  slug: amazon-serverless-application-repository-decommission-application-workflow
- description: Publish an application version, then create a CloudFormation change set to deploy it into a stack.
  name: AWS SAR Deploy Application Via Change Set
  slug: amazon-serverless-application-repository-deploy-via-change-set-workflow
- description: Create an application, publish a version, grant deploy permissions, and create a deploy change set.
  name: AWS SAR Provision And Share Application
  slug: amazon-serverless-application-repository-provision-and-share-workflow
- description: Create a new serverless application, add a version to it, then confirm the published result.
  name: AWS SAR Publish Application
  slug: amazon-serverless-application-repository-publish-application-workflow
- description: Create an application and publish two sequential semantic versions, then list all versions.
  name: AWS SAR Publish Multiple Versions
  slug: amazon-serverless-application-repository-publish-multiple-versions-workflow
- description: Create an application, attach a sharing permission policy to it, then read the policy back.
  name: AWS SAR Set Application Policy
  slug: amazon-serverless-application-repository-set-application-policy-workflow
- description: Read an application, update its descriptive metadata, then read it back to confirm the changes.
  name: AWS SAR Update Application Metadata
  slug: amazon-serverless-application-repository-update-application-metadata-workflow
artifact_total: 51
collections:
- collection_type: postman
  name: Amazon Serverless Application Repository API
  slug: postman-amazon-serverless-application-repository
- collection_type: open
  name: Amazon Serverless Application Repository API
  slug: open-amazon-serverless-application-repository
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-serverless-application-repository-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-serverless-application-repository-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-serverless-application-repository-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-serverless-application-repository-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-serverless-application-repository-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-serverless-application-repository/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-serverless-application-repository-browse-applications-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-serverless-application-repository-decommission-application-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-serverless-application-repository-deploy-via-change-set-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-serverless-application-repository-provision-and-share-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-serverless-application-repository-publish-application-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-serverless-application-repository-publish-multiple-versions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-serverless-application-repository-set-application-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-serverless-application-repository-update-application-metadata-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/serverless/serverlessrepo/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/serverless/serverlessrepo/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/serverlessrepo/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/serverlessrepo/latest/devguide/appendix-api-reference.html
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/serverlessrepo/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/serverless/serverlessrepo/pricing/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/serverless/serverlessrepo/faqs/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/compute/tag/serverless-application-repository/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
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
  url: https://stackoverflow.com/questions/tagged/serverless-application-repository
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-serverless-application-repository-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-serverless-application-repository-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-serverless-application-repository-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-serverless-application-repository-application-policy-statement-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-serverless-application-repository-application-summary-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-serverless-application-repository-application-policy-statement-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-serverless-application-repository-application-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-serverless-application-repository-application-summary-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-serverless-application-repository-version-summary-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-serverless-application-repository-application-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-serverless-application-repository-application-policy-statement-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-serverless-application-repository-application-summary-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-serverless-application-repository-version-summary-example.json
created: '2026-03-16'
description: The AWS Serverless Application Repository enables teams, organizations, and individual developers to find, deploy, and publish serverless applications. It enables you to quickly deploy code samples, components, and complete applications for common use cases such as web and mobile backends, data processing, and IoT applications using AWS SAM templates.
examples:
- key_count: 11
  name: Amazon Serverless Application Repository Application Example
  slug: amazon-serverless-application-repository-application-example
- key_count: 3
  name: Amazon Serverless Application Repository Application Policy Statement Example
  slug: amazon-serverless-application-repository-application-policy-statement-example
- key_count: 6
  name: Amazon Serverless Application Repository Application Summary Example
  slug: amazon-serverless-application-repository-application-summary-example
- key_count: 4
  name: Amazon Serverless Application Repository Version Summary Example
  slug: amazon-serverless-application-repository-version-summary-example
features:
- description: Deploy pre-built serverless applications with a single click from the SAR console.
  name: One-Click Deployment
- description: Publish applications as AWS SAM templates with full CloudFormation resource support.
  name: SAM Template Support
- description: Manage multiple application versions using semantic versioning for controlled updates.
  name: Semantic Versioning
- description: Share applications publicly to the entire AWS community or privately within your organization.
  name: Public and Private Sharing
- description: Compose complex serverless architectures using nested SAM application references.
  name: Nested Applications
- description: Control who can deploy your application using resource-based policies.
  name: Policy Sharing
- description: Attach open source licenses to applications using SPDX license identifiers.
  name: License Management
- description: Deploy applications through CloudFormation changesets for full infrastructure-as-code support.
  name: CloudFormation Integration
finops:
- name: Amazon Serverless Application Repository Finops
  service_category: API
  slug: amazon-serverless-application-repository-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-serverless-application-repository.png
json_schemas:
- name: ApplicationPolicyStatement
  property_count: 3
  slug: amazon-serverless-application-repository-application-policy-statement
- name: Application
  property_count: 11
  slug: amazon-serverless-application-repository-application
- name: ApplicationSummary
  property_count: 6
  slug: amazon-serverless-application-repository-application-summary
- name: VersionSummary
  property_count: 4
  slug: amazon-serverless-application-repository-version-summary
json_structures:
- name: Amazon Serverless Application Repository Application Policy Statement Structure
  property_count: 3
  slug: amazon-serverless-application-repository-application-policy-statement-structure
- name: Amazon Serverless Application Repository Application Structure
  property_count: 11
  slug: amazon-serverless-application-repository-application-structure
- name: Amazon Serverless Application Repository Application Summary Structure
  property_count: 6
  slug: amazon-serverless-application-repository-application-summary-structure
- name: Amazon Serverless Application Repository Version Summary Structure
  property_count: 4
  slug: amazon-serverless-application-repository-version-summary-structure
jsonld:
- class_count: 7
  name: Amazon Serverless Application Repository Context
  property_count: 13
  slug: amazon-serverless-application-repository-context
layout: provider
modified: '2026-05-19'
name: Amazon Serverless Application Repository
nav: Providers
network: true
overview: 'Amazon Serverless Application Repository publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Changesets API, Policies API, and 1 more. Tagged areas include Application Repository, Lambda, SAM, and Serverless.


  The Amazon Serverless Application Repository catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Serverless Application Repository''s developer surface includes authentication, developer portal, getting-started guide, documentation, API reference, developer console, signup flow, and 37 more developer resources.'
plans:
- name: Amazon Serverless Application Repository Plans Pricing
  plan_count: 3
  slug: amazon-serverless-application-repository-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Amazon Serverless Application Repository Rate Limits
  slug: amazon-serverless-application-repository-rate-limits
rules:
- name: Amazon Serverless Application Repository API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-serverless-application-repository-jsonschema-spectral-rules
- name: Amazon Serverless Application Repository API Rules
  rule_count: 26
  severity_counts:
    error: 8
    hint: 0
    info: 4
    warn: 14
  slug: amazon-serverless-application-repository-spectral-rules
score:
  band: exemplar
  composite: 67.6
  delta: -6.7
  facets:
    commercial_clarity: 78.9
    contract_quality: 67.6
    developer_ergonomics: 63.0
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 74.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-serverless-application-repository/refs/heads/main/screenshots/amazon-serverless-application-repository-2026-06-20T171819.png
security:
- kind: authentication
  name: Amazon Serverless Application Repository Authentication
  slug: amazon-serverless-application-repository-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Serverless Application Repository Domain Security
  slug: amazon-serverless-application-repository-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Serverless Application Repository Vulnerability Disclosure
  slug: amazon-serverless-application-repository-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Serverless Application Repository Trust Center
  slug: amazon-serverless-application-repository-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-serverless-application-repository
tags:
- Application Repository
- Lambda
- SAM
- Serverless
use_cases:
- description: Quickly deploy serverless application templates for common patterns like APIs, data processing, and IoT.
  name: Rapid Prototyping
- description: Share production-ready serverless building blocks across teams within your organization.
  name: Internal Application Sharing
- description: Publish open source serverless applications to the public SAR catalog.
  name: Open Source Distribution
- description: Distribute serverless integration patterns to AWS partner customers.
  name: Partner Integration Patterns
- description: Package and share reusable microservice patterns as deployable SAR applications.
  name: Microservice Templates
- description: Automate deployment of pre-vetted serverless infrastructure patterns via CI/CD pipelines.
  name: DevOps Automation
website: https://aws.amazon.com/serverless/serverlessrepo/
---
