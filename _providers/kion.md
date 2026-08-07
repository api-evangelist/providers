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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 73
  human_in_the_loop: 6
  name: Kion Agentic Access
  operation_count: 126
  slug: kion-agentic-access
  summary_line: 126 operations · 73 acting · 6 human-in-the-loop
api_count: 25
apis:
- description: Manage cloud accounts across AWS, Azure, GCP, and OCI
  name: Kion Accounts API
  slug: kion-accounts-api
- description: Manage Kion application configuration settings
  name: Kion App Configuration API
  slug: kion-app-configuration-api
- description: Manage Azure ARM templates
  name: Kion Azure ARM Templates API
  slug: kion-azure-arm-templates-api
- description: Manage Azure policies
  name: Kion Azure Policies API
  slug: kion-azure-policies-api
- description: Manage Azure roles
  name: Kion Azure Roles API
  slug: kion-azure-roles-api
- description: Manage cloud access roles for OU and project level access
  name: Kion Cloud Access Roles API
  slug: kion-cloud-access-roles-api
- description: Manage cloud rules that enforce policies on cloud accounts
  name: Kion Cloud Rules API
  slug: kion-cloud-rules-api
- description: Manage AWS CloudFormation templates
  name: Kion CloudFormation Templates API
  slug: kion-cloudformation-templates-api
- description: Manage compliance checks for auditing cloud resources
  name: Kion Compliance Checks API
  slug: kion-compliance-checks-api
- description: Manage compliance standards grouping multiple compliance checks
  name: Kion Compliance Standards API
  slug: kion-compliance-standards-api
- description: Manage custom variables and overrides
  name: Kion Custom Variables API
  slug: kion-custom-variables-api
- description: Manage project enforcements
  name: Kion Enforcements API
  slug: kion-enforcements-api
- description: Manage funding sources for tracking and allocating cloud spend
  name: Kion Funding Sources API
  slug: kion-funding-sources-api
- description: Manage GCP IAM roles
  name: Kion GCP IAM Roles API
  slug: kion-gcp-iam-roles-api
- description: Manage AWS IAM policies
  name: Kion IAM Policies API
  slug: kion-iam-policies-api
- description: Manage identity management systems (IDMS)
  name: Kion Identity Management API
  slug: kion-identity-management-api
- description: Manage labels for organizing and categorizing resources
  name: Kion Labels API
  slug: kion-labels-api
- description: Manage organizational units (OUs) for hierarchical organization
  name: Kion Organizational Units API
  slug: kion-organizational-units-api
- description: Manage permission mappings at global, OU, project, and funding source levels
  name: Kion Permission Mappings API
  slug: kion-permission-mappings-api
- description: Manage projects which are the organizational unit for attaching cloud accounts
  name: Kion Projects API
  slug: kion-projects-api
- description: Manage SAML group associations for SSO integration
  name: Kion SAML Group Associations API
  slug: kion-saml-group-associations-api
- description: Manage AWS service control policies
  name: Kion Service Control Policies API
  slug: kion-service-control-policies-api
- description: Manage user groups for role-based access control
  name: Kion User Groups API
  slug: kion-user-groups-api
- description: Manage users within the Kion platform
  name: Kion Users API
  slug: kion-users-api
- description: Manage webhooks for event notifications
  name: Kion Webhooks API
  slug: kion-webhooks-api
artifact_total: 51
collections:
- collection_type: open
  name: Kion Cloud Operations API
  slug: open-kion-cloud-operations-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kion-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kion-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kion-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kion-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kiongroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kionsoftware
- group: company
  title: ''
  type: Website
  url: https://kion.io/
- group: company
  title: ''
  type: Blog
  url: https://kion.io/blog/?Type=blog
- group: other
  title: ''
  type: CaseStudies
  url: https://kion.io/resources/case-studies/?Type=case-study
- group: other
  title: ''
  type: Glossary
  url: https://kion.io/resources/glossary/
- group: operate
  title: ''
  type: Support
  url: https://kion.io/resources/support/
- group: company
  title: ''
  type: Partners
  url: https://kion.io/partners/providers/
- group: commercial
  title: ''
  type: Pricing
  url: https://kion.io/why-kion/pricing-and-licensing/
- group: start
  title: ''
  type: RequestDemo
  url: https://kion.io/platform/request-a-demo/
created: '2026-01-02'
description: Kion is a cloud operations platform that provides automated governance and FinOps capabilities across AWS, Azure, GCP, and OCI through a self-hosted deployment model. The platform consolidates multiple point solutions into a comprehensive system that helps organizations allocate and track cloud spending, identify savings opportunities, enforce budgets, and access real-time and forecasted financial data.
finops:
- name: Kion Finops
  service_category: API
  slug: kion-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kion.png
json_schemas:
- name: Kion Account
  property_count: 14
  slug: account
- name: Kion AWS IAM Policy
  property_count: 10
  slug: aws-iam-policy
- name: Kion Cloud Access Role
  property_count: 14
  slug: cloud-access-role
- name: Kion Cloud Rule
  property_count: 20
  slug: cloud-rule
- name: Kion CloudFormation Template
  property_count: 12
  slug: cloudformation-template
- name: Kion Compliance Check
  property_count: 16
  slug: compliance-check
- name: Kion Compliance Standard
  property_count: 8
  slug: compliance-standard
- name: Kion Custom Variable
  property_count: 6
  slug: custom-variable
- name: Kion Funding Source
  property_count: 11
  slug: funding-source
- name: Kion Label
  property_count: 5
  slug: label
- name: Kion Organizational Unit
  property_count: 7
  slug: ou
- name: Kion Project
  property_count: 12
  slug: project
- name: Kion Service Control Policy
  property_count: 8
  slug: service-control-policy
- name: Kion User Group
  property_count: 7
  slug: user-group
- name: Kion User
  property_count: 8
  slug: user
- name: Kion Webhook
  property_count: 10
  slug: webhook
jsonld:
- class_count: 0
  name: Kion Context
  property_count: 16
  slug: kion-context
layout: provider
modified: '2026-05-19'
name: Kion
nav: Providers
network: true
overview: 'Kion publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, App Configuration API, Azure ARM Templates API, and 22 more. Tagged areas include Cloud Operations, Compliance, Costs, FinOps, and Governance.


  The Kion catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kion''s developer surface includes authentication, engineering blog, support, pricing, and 10 more developer resources.'
plans:
- name: Kion Plans Pricing
  plan_count: 3
  slug: kion-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 5
  name: Kion Rate Limits
  slug: kion-rate-limits
rules:
- name: Kion API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: kion-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.1
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 73.8
    developer_ergonomics: 17.4
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kion/refs/heads/main/screenshots/kion-2026-06-20T184046.png
security:
- kind: authentication
  name: Kion Authentication
  slug: kion-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kion Domain Security
  slug: kion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kion Trust Center
  slug: kion-trust-center
  summary_line: SOC 2, CSA STAR
slug: kion
tags:
- Cloud Operations
- Compliance
- Costs
- FinOps
- Governance
- Spend
website: https://kion.io/
---
