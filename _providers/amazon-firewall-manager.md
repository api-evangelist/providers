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
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Amazon Firewall Manager Agentic Access
  operation_count: 13
  slug: amazon-firewall-manager-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 5
apis:
- description: Firewall Manager administrator account management
  name: Amazon Firewall Manager Admin Accounts API
  slug: amazon-firewall-manager-admin-accounts-api
- description: Compliance status and violations
  name: Amazon Firewall Manager Compliance API
  slug: amazon-firewall-manager-compliance-api
- description: Member account association
  name: Amazon Firewall Manager Member Accounts API
  slug: amazon-firewall-manager-member-accounts-api
- description: Firewall Manager security policies
  name: Amazon Firewall Manager Policies API
  slug: amazon-firewall-manager-policies-api
- description: Resource sets and tags
  name: Amazon Firewall Manager Resources API
  slug: amazon-firewall-manager-resources-api
arazzos:
- description: Resolve a policy, enumerate member accounts, and pull compliance detail for a chosen account.
  name: Amazon Firewall Manager Audit Policy Compliance
  slug: amazon-firewall-manager-audit-policy-compliance-workflow
- description: Create or update a resource set and apply tags to the resulting resource set ARN.
  name: Amazon Firewall Manager Create And Tag Resource Set
  slug: amazon-firewall-manager-create-and-tag-resource-set-workflow
- description: Create or update a Firewall Manager policy and confirm it persisted by reading it back.
  name: Amazon Firewall Manager Create And Verify Policy
  slug: amazon-firewall-manager-create-and-verify-policy-workflow
- description: Confirm a policy exists, then delete it and all of its managed resources.
  name: Amazon Firewall Manager Decommission Policy
  slug: amazon-firewall-manager-decommission-policy-workflow
- description: Find a policy in the policy list and apply governance tags to its ARN when it exists.
  name: Amazon Firewall Manager Find And Tag Policy
  slug: amazon-firewall-manager-find-and-tag-policy-workflow
- description: List resource sets, read one back by id, and apply an ownership tag to it.
  name: Amazon Firewall Manager Inventory And Tag Resource Set
  slug: amazon-firewall-manager-inventory-and-tag-resource-set-workflow
- description: Set the Firewall Manager administrator account and confirm its association and role status.
  name: Amazon Firewall Manager Onboard Admin Account
  slug: amazon-firewall-manager-onboard-admin-account-workflow
- description: Create a resource set and then create a policy scoped to the same resource type.
  name: Amazon Firewall Manager Resource Set Driven Policy
  slug: amazon-firewall-manager-resource-set-driven-policy-workflow
artifact_total: 54
collections:
- collection_type: postman
  name: AWS Firewall Manager API
  slug: postman-amazon-firewall-manager
- collection_type: open
  name: AWS Firewall Manager API
  slug: open-amazon-firewall-manager
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-firewall-manager-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-firewall-manager-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-firewall-manager-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-firewall-manager-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-firewall-manager-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-firewall-manager/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-firewall-manager-audit-policy-compliance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-firewall-manager-create-and-tag-resource-set-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-firewall-manager-create-and-verify-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-firewall-manager-decommission-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-firewall-manager-find-and-tag-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-firewall-manager-inventory-and-tag-resource-set-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-firewall-manager-onboard-admin-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-firewall-manager-resource-set-driven-policy-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/firewall-manager/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/firewall-manager/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html
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
  url: https://aws.amazon.com/blogs/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/wafv2/fmsv2/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
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
  url: https://stackoverflow.com/questions/tagged/aws-firewall-manager
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-firewall-manager-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-firewall-manager-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-firewall-manager-context.jsonld
created: '2026-03-16'
description: AWS Firewall Manager is a security management service that allows you to centrally configure and manage firewall rules across your accounts and applications in AWS Organizations. It makes it easier to bring new applications and resources into compliance with security policies.
examples:
- key_count: 4
  name: Amazon Firewall Manager Compliance Violator Example
  slug: amazon-firewall-manager-compliance-violator-example
- key_count: 10
  name: Amazon Firewall Manager Policy Example
  slug: amazon-firewall-manager-policy-example
- key_count: 7
  name: Amazon Firewall Manager Resource Set Example
  slug: amazon-firewall-manager-resource-set-example
- key_count: 2
  name: Amazon Firewall Manager Security Service Policy Data Example
  slug: amazon-firewall-manager-security-service-policy-data-example
- key_count: 2
  name: Amazon Firewall Manager Tag Example
  slug: amazon-firewall-manager-tag-example
features:
- description: Define and enforce WAF, Shield Advanced, Network Firewall, and security group policies from a single pane of glass across all AWS accounts.
  name: Centralized Policy Management
- description: Automatically remediate non-compliant resources so that new accounts and resources are always protected.
  name: Automatic Remediation
- description: Manage security policies across hundreds of AWS accounts within an AWS Organization.
  name: Multi-Account Support
- description: View policy compliance status per account and resource with detailed violation reports.
  name: Compliance Visibility
- description: Group AWS resources by type for targeted policy application and management.
  name: Resource Sets
- description: Apply policies to resources based on AWS resource tags for fine-grained scope control.
  name: Tag-Based Targeting
- description: Deploy and manage third-party firewall appliances through AWS Marketplace with Firewall Manager.
  name: Third-Party Firewall Support
finops:
- name: Amazon Firewall Manager Finops
  service_category: API
  slug: amazon-firewall-manager-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-firewall-manager.png
json_schemas:
- name: ComplianceViolator
  property_count: 3
  slug: amazon-firewall-manager-compliance-violator
- name: Policy
  property_count: 8
  slug: amazon-firewall-manager-policy
- name: ResourceSet
  property_count: 6
  slug: amazon-firewall-manager-resource-set
- name: SecurityServicePolicyData
  property_count: 2
  slug: amazon-firewall-manager-security-service-policy-data
- name: Tag
  property_count: 2
  slug: amazon-firewall-manager-tag
json_structures:
- name: Amazon Firewall Manager Compliance Violator Structure
  property_count: 0
  slug: amazon-firewall-manager-compliance-violator-structure
- name: Amazon Firewall Manager Policy Structure
  property_count: 0
  slug: amazon-firewall-manager-policy-structure
- name: Amazon Firewall Manager Resource Set Structure
  property_count: 0
  slug: amazon-firewall-manager-resource-set-structure
- name: Amazon Firewall Manager Security Service Policy Data Structure
  property_count: 0
  slug: amazon-firewall-manager-security-service-policy-data-structure
- name: Amazon Firewall Manager Tag Structure
  property_count: 0
  slug: amazon-firewall-manager-tag-structure
jsonld:
- class_count: 5
  name: Amazon Firewall Manager Context
  property_count: 14
  slug: amazon-firewall-manager-context
layout: provider
modified: '2026-05-19'
name: Amazon Firewall Manager
nav: Providers
network: true
overview: 'Amazon Firewall Manager publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Admin Accounts API, Compliance API, Member Accounts API, and 2 more. Tagged areas include Compliance, Firewall, Network Security, and Security.


  The Amazon Firewall Manager catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Firewall Manager''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 23 more developer resources.'
plans:
- name: Amazon Firewall Manager Plans Pricing
  plan_count: 3
  slug: amazon-firewall-manager-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 5
  name: Amazon Firewall Manager Rate Limits
  slug: amazon-firewall-manager-rate-limits
rules:
- name: Amazon Firewall Manager API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-firewall-manager-jsonschema-spectral-rules
- name: Amazon Firewall Manager API Rules
  rule_count: 35
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 24
  slug: amazon-firewall-manager-spectral-rules
score:
  band: strong
  composite: 65.0
  delta: -4.4
  facets:
    commercial_clarity: 68.4
    contract_quality: 82.3
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 69.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-firewall-manager/refs/heads/main/screenshots/amazon-firewall-manager-2026-06-20T171659.png
security:
- kind: authentication
  name: Amazon Firewall Manager Authentication
  slug: amazon-firewall-manager-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Firewall Manager Domain Security
  slug: amazon-firewall-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Firewall Manager Vulnerability Disclosure
  slug: amazon-firewall-manager-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Firewall Manager Trust Center
  slug: amazon-firewall-manager-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-firewall-manager
tags:
- Compliance
- Firewall
- Network Security
- Security
use_cases:
- description: Enforce standard WAF rule sets across all CloudFront distributions and ALBs organization-wide.
  name: WAF Rule Standardization
- description: Mandate Shield Advanced protection for all internet-facing resources across accounts.
  name: DDoS Protection Baseline
- description: Audit and remediate overly permissive security group rules across EC2 and VPC resources.
  name: Security Group Governance
- description: Deploy and manage AWS Network Firewall across VPCs in multiple accounts from a central policy.
  name: Network Firewall Deployment
- description: Monitor and report on firewall policy compliance for SOC 2, PCI DSS, and regulatory requirements.
  name: Compliance Reporting
- description: Automatically apply security policies to new AWS accounts as they join the organization.
  name: New Account Onboarding
website: https://aws.amazon.com/firewall-manager/
---
