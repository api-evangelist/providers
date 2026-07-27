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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Productiv Agentic Access
  operation_count: 15
  slug: productiv-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 11
apis:
- description: Fetch detailed information about a particular app.
  name: Productiv App Details API
  slug: productiv-app-details-api
- description: Query the list of apps in your company portfolio.
  name: Productiv App Summaries API
  slug: productiv-app-summaries-api
- description: Set up and manage custom applications within Productiv.
  name: Productiv Applications API
  slug: productiv-applications-api
- description: Fetch audit events for activities performed on the Productiv platform.
  name: Productiv Audit Events API
  slug: productiv-audit-events-api
- description: OAuth2 token endpoint for obtaining access tokens.
  name: Productiv Authentication API
  slug: productiv-authentication-api
- description: Upload files in batch for applications.
  name: Productiv Batch Upload API
  slug: productiv-batch-upload-api
- description: Publish organizational chart data.
  name: Productiv Org Chart API
  slug: productiv-org-chart-api
- description: Manage users provisioned to custom integrations.
  name: Productiv Provisioned Users API
  slug: productiv-provisioned-users-api
- description: Fetch provisioning workflows and execution details.
  name: Productiv Provisioning Workflows API
  slug: productiv-provisioning-workflows-api
- description: Publish spend data for applications.
  name: Productiv Spend Data API
  slug: productiv-spend-data-api
- description: Publish usage events for applications.
  name: Productiv Usage Events API
  slug: productiv-usage-events-api
artifact_total: 60
collections:
- collection_type: open
  name: Productiv Developer API
  slug: open-productiv-developer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/productiv-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/productiv-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/productiv-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/productiv-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BeProductiv
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/productiv
- group: docs
  title: ''
  type: Documentation
  url: https://docs.app.productiv.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://productiv.com/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.app.productiv.com/developer-api/authorization.html
- group: design
  title: ''
  type: Rules
  url: rules/productiv-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/productiv-vocabulary.yaml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/shared/developer-api.yaml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/saas-management.yaml
- group: company
  title: ''
  type: Blog
  url: https://productiv.com/blog
created: '2025-07-11'
description: The SaaS Management Platform that delivers the industrys most comprehensive view of your SaaS portfolio with deep usage analytics, spend data, and feature-level insights to power the technology decisions that support your business.
examples:
- key_count: 10
  name: Productiv Developer App Details Example
  slug: productiv-developer-app-details-example
- key_count: 5
  name: Productiv Developer App Summary Example
  slug: productiv-developer-app-summary-example
features:
- name: SaaS Portfolio Management
- name: Usage Analytics
- name: Spend Data Tracking
- name: Provisioning Workflows
- name: Audit Events
- name: Org Chart Integration
- name: Custom Application Connectors
- name: Batch File Upload
- name: Data Export
- name: OAuth2 Authentication
finops:
- name: Productiv Finops
  service_category: API
  slug: productiv-finops
image: /assets/icons/productiv.png
integrations:
- name: Okta
- name: Azure Active Directory
- name: Salesforce
- name: ServiceNow
- name: Workday
- name: Slack
json_schemas:
- name: AppDetails
  property_count: 10
  slug: app-details
- name: AppSummary
  property_count: 5
  slug: app-summary
- name: Application
  property_count: 5
  slug: application
- name: AuditEvent
  property_count: 5
  slug: audit-event
- name: OrgChartUser
  property_count: 6
  slug: org-chart-user
- name: AppDetails
  property_count: 10
  slug: productiv-developer-app-details
- name: AppSummary
  property_count: 5
  slug: productiv-developer-app-summary
- name: ProvisionedUser
  property_count: 4
  slug: provisioned-user
- name: ProvisioningWorkflow
  property_count: 4
  slug: provisioning-workflow
- name: SpendData
  property_count: 4
  slug: spend-data
- name: UsageEvent
  property_count: 3
  slug: usage-event
json_structures:
- name: Productiv Developer App Details Structure
  property_count: 10
  slug: productiv-developer-app-details-structure
- name: Productiv Developer App Summary Structure
  property_count: 5
  slug: productiv-developer-app-summary-structure
jsonld:
- class_count: 49
  name: Productiv Context
  property_count: 5
  slug: productiv-context
- class_count: 0
  name: Productiv Developer Context
  property_count: 0
  slug: productiv-developer-context
layout: provider
modified: '2026-05-19'
name: Productiv
nav: Providers
network: true
overview: 'Productiv publishes 11 APIs on the [APIs.io](https://apis.io/) network, including App Details API, App Summaries API, Applications API, and 8 more. Tagged areas include Application Portfolio, Provisioning, SaaS Management, Spend Management, and Usage Analytics.


  The Productiv catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Productiv''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Productiv Plans Pricing
  plan_count: 3
  slug: productiv-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Productiv Rate Limits
  slug: productiv-rate-limits
rules:
- name: Productiv API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: productiv-jsonschema-spectral-rules
- name: Productiv API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 7
  slug: productiv-spectral-rules
score:
  band: strong
  composite: 60.7
  delta: 5.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 79.6
    developer_ergonomics: 30.4
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 55.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/productiv/refs/heads/main/screenshots/productiv-2026-06-20T192136.png
security:
- kind: authentication
  name: Productiv Authentication
  slug: productiv-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Productiv Domain Security
  slug: productiv-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Productiv Trust Center
  slug: productiv-trust-center
  summary_line: SOC 2
slug: productiv
tags:
- Application Portfolio
- Provisioning
- SaaS Management
- Spend Management
- Usage Analytics
use_cases:
- name: Track SaaS Application Usage
- name: Optimize Software Spend
- name: Automate User Provisioning
- name: Audit Platform Activity
- name: Integrate Custom Applications
- name: Export App Portfolio Data
website: https://productiv.com/
---
