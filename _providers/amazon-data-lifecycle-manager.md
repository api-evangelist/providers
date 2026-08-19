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
- acting_count: 5
  human_in_the_loop: 0
  name: Amazon Data Lifecycle Manager Agentic Access
  operation_count: 8
  slug: amazon-data-lifecycle-manager-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 2
apis:
- description: Operations for managing EBS snapshot and AMI lifecycle policies
  name: Amazon Data Lifecycle Manager Lifecycle Policies API
  slug: amazon-data-lifecycle-manager-lifecycle-policies-api
- description: Operations for managing resource tags
  name: Amazon Data Lifecycle Manager Tags API
  slug: amazon-data-lifecycle-manager-tags-api
arazzos:
- description: Retrieve a lifecycle policy, delete it, and confirm it no longer appears in the list.
  name: Amazon Data Lifecycle Manager Decommission Policy
  slug: amazon-data-lifecycle-manager-decommission-policy-workflow
- description: Disable a lifecycle policy and confirm the state change by reading it back.
  name: Amazon Data Lifecycle Manager Disable Policy
  slug: amazon-data-lifecycle-manager-disable-policy-workflow
- description: Create an EBS snapshot lifecycle policy, read it back, and confirm it in the policy list.
  name: Amazon Data Lifecycle Manager Provision Policy
  slug: amazon-data-lifecycle-manager-provision-policy-workflow
- description: Read a policy, re-enable and rewrite its snapshot schedule, then confirm the change.
  name: Amazon Data Lifecycle Manager Reconfigure Schedule
  slug: amazon-data-lifecycle-manager-reconfigure-schedule-workflow
- description: Add tags to a DLM resource and confirm them by listing the resource's tags.
  name: Amazon Data Lifecycle Manager Tag Policy Resource
  slug: amazon-data-lifecycle-manager-tag-policy-resource-workflow
- description: Remove tags from a DLM resource and confirm removal by listing the resource's tags.
  name: Amazon Data Lifecycle Manager Untag Policy Resource
  slug: amazon-data-lifecycle-manager-untag-policy-resource-workflow
artifact_total: 81
collections:
- collection_type: postman
  name: Amazon Data Lifecycle Manager API
  slug: postman-amazon-data-lifecycle-manager
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Data Lifecycle Manager Lifecycle Policies API
  slug: open-amazon-data-lifecycle-manager-lifecycle-policies-api
- collection_type: open
  name: Amazon Data Lifecycle Manager Lifecycle Policies Tags API
  slug: open-amazon-data-lifecycle-manager-tags-api
- collection_type: open
  name: Amazon Data Lifecycle Manager API
  slug: open-amazon-data-lifecycle-manager
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-data-lifecycle-manager-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-data-lifecycle-manager-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-data-lifecycle-manager-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-data-lifecycle-manager-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-data-lifecycle-manager-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-data-lifecycle-manager/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-lifecycle-manager-decommission-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-lifecycle-manager-disable-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-lifecycle-manager-provision-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-lifecycle-manager-reconfigure-schedule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-lifecycle-manager-tag-policy-resource-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-lifecycle-manager-untag-policy-resource-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/ebs/data-lifecycle-manager/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/ebs/data-lifecycle-manager/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/dlm/
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/ec2/v2/home#Lifecycle
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-data-lifecycle-manager-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-data-lifecycle-manager-vocabulary.yaml
created: '2026-03-16'
description: Amazon Data Lifecycle Manager provides an automated way to manage the lifecycle of your AWS resources. Using lifecycle policies, you can automate the creation, retention, and deletion of Amazon EBS snapshots and EBS-backed AMIs, reducing storage costs and simplifying backup management. Policies target EBS volumes and EC2 instances using tags, execute on configurable schedules, and apply flexible retention rules based on count or age.
examples:
- key_count: 4
  name: Create Lifecycle Policy Request Example
  slug: create-lifecycle-policy-request-example
- key_count: 1
  name: Create Lifecycle Policy Response Example
  slug: create-lifecycle-policy-response-example
- key_count: 3
  name: Create Rule Example
  slug: create-rule-example
- key_count: 3
  name: Error Example
  slug: error-example
- key_count: 1
  name: Get Lifecycle Policies Response Example
  slug: get-lifecycle-policies-response-example
- key_count: 1
  name: Get Lifecycle Policy Response Example
  slug: get-lifecycle-policy-response-example
- key_count: 5
  name: Lifecycle Policy Example
  slug: lifecycle-policy-example
- key_count: 4
  name: Lifecycle Policy Summary Example
  slug: lifecycle-policy-summary-example
- key_count: 1
  name: List Tags For Resource Response Example
  slug: list-tags-for-resource-response-example
- key_count: 3
  name: Policy Details Example
  slug: policy-details-example
- key_count: 1
  name: Retain Rule Example
  slug: retain-rule-example
- key_count: 4
  name: Schedule Example
  slug: schedule-example
- key_count: 2
  name: Tag Example
  slug: tag-example
- key_count: 1
  name: Tag Resource Request Example
  slug: tag-resource-request-example
- key_count: 2
  name: Update Lifecycle Policy Request Example
  slug: update-lifecycle-policy-request-example
features:
- description: Automatically create, copy, and delete EBS snapshots on configurable schedules using tag-based targeting of volumes across AWS accounts.
  name: EBS Snapshot Automation
- description: Automate the creation and deregistration of Amazon Machine Images from EC2 instances on schedules to maintain a library of AMIs.
  name: AMI Lifecycle Management
- description: Retain snapshots by count (keep the last N) or by age (keep for N days/weeks/months/years), automatically deleting older snapshots.
  name: Flexible Retention Rules
- description: Target EBS volumes or EC2 instances using resource tags for policy scope, enabling granular backup control without managing resource lists.
  name: Tag-Based Targeting
- description: Configure schedules to copy snapshots to other AWS regions for disaster recovery and geographic redundancy automatically.
  name: Cross-Region Copy
- description: Enable fast snapshot restore on snapshots created by DLM policies to dramatically reduce EBS volume initialization time.
  name: Fast Snapshot Restore
- description: Trigger snapshot sharing and copying workflows in response to CloudWatch Events for cross-account snapshot automation.
  name: Event-Based Policies
finops:
- name: Amazon Data Lifecycle Manager Finops
  service_category: API
  slug: amazon-data-lifecycle-manager-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-data-lifecycle-manager.png
json_schemas:
- name: Create Lifecycle Policy Request
  property_count: 5
  slug: create-lifecycle-policy-request
- name: Create Lifecycle Policy Response
  property_count: 1
  slug: create-lifecycle-policy-response
- name: Create Rule
  property_count: 4
  slug: create-rule
- name: Error
  property_count: 3
  slug: error
- name: Get Lifecycle Policies Response
  property_count: 1
  slug: get-lifecycle-policies-response
- name: Get Lifecycle Policy Response
  property_count: 1
  slug: get-lifecycle-policy-response
- name: Lifecycle Policy
  property_count: 7
  slug: lifecycle-policy
- name: Lifecycle Policy Summary
  property_count: 5
  slug: lifecycle-policy-summary
- name: List Tags for Resource Response
  property_count: 1
  slug: list-tags-for-resource-response
- name: Policy Details
  property_count: 4
  slug: policy-details
- name: Retain Rule
  property_count: 3
  slug: retain-rule
- name: Schedule
  property_count: 5
  slug: schedule
- name: Tag Resource Request
  property_count: 1
  slug: tag-resource-request
- name: Tag
  property_count: 2
  slug: tag
- name: Update Lifecycle Policy Request
  property_count: 4
  slug: update-lifecycle-policy-request
json_structures:
- name: Create Lifecycle Policy Request Structure
  property_count: 0
  slug: create-lifecycle-policy-request-structure
- name: Create Lifecycle Policy Response Structure
  property_count: 0
  slug: create-lifecycle-policy-response-structure
- name: Create Rule Structure
  property_count: 0
  slug: create-rule-structure
- name: Error Structure
  property_count: 0
  slug: error-structure
- name: Get Lifecycle Policies Response Structure
  property_count: 0
  slug: get-lifecycle-policies-response-structure
- name: Get Lifecycle Policy Response Structure
  property_count: 0
  slug: get-lifecycle-policy-response-structure
- name: Lifecycle Policy Structure
  property_count: 0
  slug: lifecycle-policy-structure
- name: Lifecycle Policy Summary Structure
  property_count: 0
  slug: lifecycle-policy-summary-structure
- name: List Tags For Resource Response Structure
  property_count: 0
  slug: list-tags-for-resource-response-structure
- name: Policy Details Structure
  property_count: 0
  slug: policy-details-structure
- name: Retain Rule Structure
  property_count: 0
  slug: retain-rule-structure
- name: Schedule Structure
  property_count: 0
  slug: schedule-structure
- name: Tag Resource Request Structure
  property_count: 0
  slug: tag-resource-request-structure
- name: Tag Structure
  property_count: 0
  slug: tag-structure
- name: Update Lifecycle Policy Request Structure
  property_count: 0
  slug: update-lifecycle-policy-request-structure
jsonld:
- class_count: 0
  name: Amazon Data Lifecycle Manager Context
  property_count: 34
  slug: amazon-data-lifecycle-manager-context
layout: provider
modified: '2026-05-19'
name: Amazon Data Lifecycle Manager
nav: Providers
network: true
overview: 'Amazon Data Lifecycle Manager publishes 2 APIs on the [APIs.io](https://apis.io/) network: Lifecycle Policies API and Tags API. Tagged areas include Backup, EBS Snapshots, Lifecycle Management, Storage, and Automation.


  The Amazon Data Lifecycle Manager catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Data Lifecycle Manager''s developer surface includes authentication, developer portal, documentation, support, developer console, signup flow, and 20 more developer resources.'
plans:
- name: Amazon Data Lifecycle Manager Plans Pricing
  plan_count: 3
  slug: amazon-data-lifecycle-manager-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Amazon Data Lifecycle Manager Rate Limits
  slug: amazon-data-lifecycle-manager-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Data Lifecycle Manager API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-data-lifecycle-manager-jsonschema-spectral-rules
- effective_rule_count: 68
  extends:
  - spectral:oas
  name: Amazon Data Lifecycle Manager API Rules
  rule_count: 27
  severity_counts:
    error: 13
    hint: 0
    info: 3
    warn: 11
  slug: amazon-data-lifecycle-manager-spectral-rules
score:
  band: developing
  composite: 52.4
  delta: -6.1
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 25.0
    contract_quality: 77.3
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 58.5
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
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-data-lifecycle-manager/refs/heads/main/screenshots/amazon-data-lifecycle-manager-2026-06-20T171613.png
security:
- kind: authentication
  name: Amazon Data Lifecycle Manager Authentication
  slug: amazon-data-lifecycle-manager-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Data Lifecycle Manager Domain Security
  slug: amazon-data-lifecycle-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Data Lifecycle Manager Vulnerability Disclosure
  slug: amazon-data-lifecycle-manager-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Data Lifecycle Manager Trust Center
  slug: amazon-data-lifecycle-manager-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-data-lifecycle-manager
tags:
- Backup
- EBS Snapshots
- Lifecycle Management
- Storage
- Automation
- Compliance
use_cases:
- description: Schedule daily EBS volume snapshots with automated retention of the last 7 or 30 days of backups without manual intervention.
  name: Automated Daily Backups
- description: Meet regulatory backup retention requirements by defining long-term retention policies (monthly/yearly) for compliance snapshots.
  name: Compliance and Audit Retention
- description: Automatically copy EBS snapshots to secondary AWS regions to enable cross-region disaster recovery with minimal RTO and RPO.
  name: Disaster Recovery
- description: Automate the creation of hardened EC2 AMI images from approved instances and manage their lifecycle for deployment fleets.
  name: Golden AMI Pipeline
- description: Reduce EBS snapshot storage costs by automatically deleting outdated snapshots based on configurable age or count retention rules.
  name: Storage Cost Optimization
website: https://aws.amazon.com/ebs/data-lifecycle-manager/
---
