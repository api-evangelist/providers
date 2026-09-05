---
access_model:
  confidence: medium
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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Productiv Agentic Access
  operation_count: 15
  slug: productiv-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 1
apis:
- baseURL: https://public-api.productiv.com
  baseurl_source: declared
  description: Fetch detailed information about a particular app.
  name: Productiv App Details API
  slug: productiv-app-details-api
- baseURL: https://public-api.productiv.com
  baseurl_source: declared
  description: Query the list of apps in your company portfolio.
  name: Productiv App Summaries API
  slug: productiv-app-summaries-api
- baseURL: https://public-api.productiv.com
  baseurl_source: declared
  description: Set up and manage custom applications within Productiv.
  name: Productiv Applications API
  slug: productiv-applications-api
- baseURL: https://public-api.productiv.com
  baseurl_source: declared
  description: Fetch audit events for activities performed on the Productiv platform.
  name: Productiv Audit Events API
  slug: productiv-audit-events-api
- baseURL: https://public-api.productiv.com
  baseurl_source: declared
  description: OAuth2 token endpoint for obtaining access tokens.
  name: Productiv Authentication API
  slug: productiv-authentication-api
- baseURL: https://public-api.productiv.com
  baseurl_source: declared
  description: Upload files in batch for applications.
  name: Productiv Batch Upload API
  slug: productiv-batch-upload-api
- baseURL: https://public-api.productiv.com
  baseurl_source: declared
  description: Publish organizational chart data.
  name: Productiv Org Chart API
  slug: productiv-org-chart-api
- baseURL: https://public-api.productiv.com
  baseurl_source: declared
  description: Manage users provisioned to custom integrations.
  name: Productiv Provisioned Users API
  slug: productiv-provisioned-users-api
- baseURL: https://public-api.productiv.com
  baseurl_source: declared
  description: Fetch provisioning workflows and execution details.
  name: Productiv Provisioning Workflows API
  slug: productiv-provisioning-workflows-api
- baseURL: https://public-api.productiv.com
  baseurl_source: declared
  description: Publish spend data for applications.
  name: Productiv Spend Data API
  slug: productiv-spend-data-api
- baseURL: https://public-api.productiv.com
  baseurl_source: declared
  description: Publish usage events for applications.
  name: Productiv Usage Events API
  slug: productiv-usage-events-api
artifact_total: 83
collections:
- collection_type: postman
  name: Productiv Developer App Details API
  slug: postman-productiv-app-details-api
- collection_type: postman
  name: Productiv Developer App Details App Summaries API
  slug: postman-productiv-app-summaries-api
- collection_type: postman
  name: Productiv Developer App Details Applications API
  slug: postman-productiv-applications-api
- collection_type: postman
  name: Productiv Developer App Details Audit Events API
  slug: postman-productiv-audit-events-api
- collection_type: postman
  name: Productiv Developer App Details Authentication API
  slug: postman-productiv-authentication-api
- collection_type: postman
  name: Productiv Developer App Details Batch Upload API
  slug: postman-productiv-batch-upload-api
- collection_type: postman
  name: Productiv Developer App Details Org Chart API
  slug: postman-productiv-org-chart-api
- collection_type: postman
  name: Productiv Developer App Details Provisioned Users API
  slug: postman-productiv-provisioned-users-api
- collection_type: postman
  name: Productiv Developer App Details Provisioning Workflows API
  slug: postman-productiv-provisioning-workflows-api
- collection_type: postman
  name: Productiv Developer App Details Spend Data API
  slug: postman-productiv-spend-data-api
- collection_type: postman
  name: Productiv Developer App Details Usage Events API
  slug: postman-productiv-usage-events-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Productiv Developer App Details API
  slug: open-productiv-app-details-api
- collection_type: open
  name: Productiv Developer App Details App Summaries API
  slug: open-productiv-app-summaries-api
- collection_type: open
  name: Productiv Developer App Details Applications API
  slug: open-productiv-applications-api
- collection_type: open
  name: Productiv Developer App Details Audit Events API
  slug: open-productiv-audit-events-api
- collection_type: open
  name: Productiv Developer App Details Authentication API
  slug: open-productiv-authentication-api
- collection_type: open
  name: Productiv Developer App Details Batch Upload API
  slug: open-productiv-batch-upload-api
- collection_type: open
  name: Productiv Developer API
  slug: open-productiv-developer
- collection_type: open
  name: Productiv Developer App Details Org Chart API
  slug: open-productiv-org-chart-api
- collection_type: open
  name: Productiv Developer App Details Provisioned Users API
  slug: open-productiv-provisioned-users-api
- collection_type: open
  name: Productiv Developer App Details Provisioning Workflows API
  slug: open-productiv-provisioning-workflows-api
- collection_type: open
  name: Productiv Developer App Details Spend Data API
  slug: open-productiv-spend-data-api
- collection_type: open
  name: Productiv Developer App Details Usage Events API
  slug: open-productiv-usage-events-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/productiv/overview
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


  Productiv''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Productiv Plans Pricing
  plan_count: 3
  slug: productiv-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Productiv Rate Limits
  slug: productiv-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Productiv API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: productiv-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: Productiv API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 7
  slug: productiv-spectral-rules
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 73.5
    catalog_earned_first_party: 0.0
    catalog_gap: 41.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 28.8
    contract_quality: 72.1
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
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
