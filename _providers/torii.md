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
  name: Torii Agentic Access
  operation_count: 19
  slug: torii-agentic-access
  summary_line: 19 operations · 7 acting
api_count: 10
apis:
- description: Manage applications discovered and tracked in your organization.
  name: Torii Apps API
  slug: torii-apps-api
- description: Retrieve admin audit log entries.
  name: Torii Audit API
  slug: torii-audit-api
- description: Manage SaaS contracts and renewal information.
  name: Torii Contracts API
  slug: torii-contracts-api
- description: Upload and manage files.
  name: Torii Files API
  slug: torii-files-api
- description: Retrieve field metadata for apps, users, and contracts.
  name: Torii Metadata API
  slug: torii-metadata-api
- description: Manage file parsing and column mapping.
  name: Torii Parsings API
  slug: torii-parsings-api
- description: SCIM 2.0 user provisioning endpoints.
  name: Torii SCIM API
  slug: torii-scim-api
- description: The Services API from Torii — 1 operation(s) for services.
  name: Torii Services API
  slug: torii-services-api
- description: Manage users in your organization.
  name: Torii Users API
  slug: torii-users-api
- description: The Workflows API from Torii — 1 operation(s) for workflows.
  name: Torii Workflows API
  slug: torii-workflows-api
artifact_total: 70
collections:
- collection_type: open
  name: Torii API
  slug: open-torii-torii
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/torii-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/torii-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/torii-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/torii-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/toriihq/
- group: company
  title: ''
  type: Website
  url: https://www.toriihq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.toriihq.com
- group: company
  title: ''
  type: About
  url: https://www.toriihq.com/about
- group: commercial
  title: ''
  type: Pricing
  url: https://www.toriihq.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.toriihq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.toriihq.com/security
- group: other
  title: ''
  type: Customers
  url: https://www.toriihq.com/customers
- group: company
  title: ''
  type: Partners
  url: https://www.toriihq.com/partners
- group: other
  title: ''
  type: Branding
  url: https://www.toriihq.com/brand-guidelines
- group: start
  title: ''
  type: Login
  url: https://app.toriihq.com/login
- group: design
  title: ''
  type: JSONLD
  url: json-ld/torii-context.jsonld
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/torii-app-structure.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/torii-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/torii-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.toriihq.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.toriihq.com/feed/
created: '2025-07-15'
description: Torii is the market leading SaaS Management Platform built to bring all your software into one place. Discover shadow IT, enforce governance, cut costs, and operationalize every app. Torii integrates with 180+ SaaS applications to provide license and usage data, automate user onboarding and offboarding workflows, manage SaaS contracts and renewals, and maintain compliance audit trails.
examples:
- key_count: 4
  name: Torii List Apps Example
  slug: torii-list-apps-example
- key_count: 4
  name: Torii Sync Custom Integration Example
  slug: torii-sync-custom-integration-example
features:
- name: SaaS Management Platform
- name: Shadow IT Discovery
- name: App Lifecycle Management
- name: License Optimization
- name: Contract and Renewal Management
- name: Workflow Automation
- name: User Onboarding and Offboarding
- name: SCIM 2.0 Provisioning
- name: Compliance Audit Logs
- name: Custom Integrations
- name: Browser Extension
- name: 180+ Native Integrations
finops:
- name: Torii Finops
  service_category: API
  slug: torii-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/torii.png
integrations:
- name: Okta
- name: Microsoft Entra ID
- name: Google Workspace
- name: Slack
- name: Salesforce
- name: Jira Cloud
- name: GitHub Enterprise
- name: Azure DevOps
- name: Zoom
- name: Microsoft Teams
- name: Datadog
- name: ServiceNow
- name: BambooHR
- name: Workday HCM
- name: Rippling
- name: HubSpot
- name: Zendesk
- name: PagerDuty
- name: Confluence
- name: Notion
json_schemas:
- name: Torii App
  property_count: 11
  slug: app
- name: Torii Audit Log Entry
  property_count: 7
  slug: audit-log-entry
- name: Torii Contract
  property_count: 12
  slug: contract
- name: Torii Field Metadata
  property_count: 5
  slug: field-metadata
- name: Torii Parsing Request
  property_count: 5
  slug: parsing-request
- name: Torii SCIM User
  property_count: 8
  slug: scim-user
- name: Torii User
  property_count: 9
  slug: user
json_structures:
- name: Torii App Structure
  property_count: 0
  slug: torii-app-structure
jsonld:
- class_count: 48
  name: Torii Context
  property_count: 0
  slug: torii-context
layout: provider
modified: '2026-05-19'
name: Torii
nav: Providers
network: true
overview: 'Torii publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Audit API, Contracts API, and 7 more. Tagged areas include Apps, Compliance, Cost Optimization, Governance, and IT Management.


  The Torii catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Torii''s developer surface includes authentication, documentation, pricing, engineering blog, and 17 more developer resources.'
plans:
- name: Torii Plans Pricing
  plan_count: 3
  slug: torii-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Torii Rate Limits
  slug: torii-rate-limits
rules:
- name: Torii API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: torii-jsonschema-spectral-rules
- name: Torii API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 1
    info: 0
    warn: 5
  slug: torii-rules
score:
  band: strong
  composite: 65.2
  delta: 4.3
  facets:
    commercial_clarity: 92.1
    contract_quality: 76.5
    developer_ergonomics: 21.7
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 31.6
  previous_composite: 60.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/torii/refs/heads/main/screenshots/torii-2026-06-20T195457.png
security:
- kind: authentication
  name: Torii Authentication
  slug: torii-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Torii Domain Security
  slug: torii-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Torii Trust Center
  slug: torii-trust-center
  summary_line: SOC 2
slug: torii
tags:
- Apps
- Compliance
- Cost Optimization
- Governance
- IT Management
- SaaS Management
use_cases:
- name: Shadow IT Discovery
- name: Onboarding and Offboarding Automation
- name: SaaS Spend Management
- name: SaaS Vendor and Renewal Management
- name: Compliance and Governance
- name: Open Platform Integration
- name: AI Powered SaaS Management
website: https://www.toriihq.com/
---
