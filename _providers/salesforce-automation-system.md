---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 29.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Salesforce Automation System Agentic Access
  operation_count: 6
  slug: salesforce-automation-system-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- description: Visual automation tool for building screen flows, autolaunched flows, record-triggered flows, and scheduled flows without code.
  name: Salesforce Flow Builder
  slug: salesforce-flow-builder
- description: Multi-step approval automation for routing records through review chains with configurable criteria, approvers, and post-approval actions.
  name: Salesforce Approval Processes
  slug: salesforce-approval-processes
- baseURL: https://{instance}.salesforce.com/services/data/v59.0
  baseurl_source: declared
  description: Manage Salesforce Flow definitions and metadata.
  name: Salesforce Automation System Flows API
  slug: salesforce-automation-system-flows-api
- baseURL: https://{instance}.salesforce.com/services/data/v59.0
  baseurl_source: declared
  description: Query and invoke automation processes.
  name: Salesforce Automation System Process Automation API
  slug: salesforce-automation-system-process-automation-api
artifact_total: 25
collections:
- collection_type: postman
  name: Salesforce Flow Automation Flows API
  slug: postman-salesforce-automation-system-flows-api
- collection_type: postman
  name: Salesforce Flow Automation Flows Process Automation API
  slug: postman-salesforce-automation-system-process-automation-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Salesforce Flow Automation API
  slug: open-salesforce-automation-flow
- collection_type: open
  name: Salesforce Flow Automation Flows API
  slug: open-salesforce-automation-system-flows-api
- collection_type: open
  name: Salesforce Flow Automation Flows Process Automation API
  slug: open-salesforce-automation-system-process-automation-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/salesforce-automation-system/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salesforce-automation-system-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salesforce-automation-system-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/salesforce-automation-system-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/salesforce-automation-system-scopes.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.salesforce.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/
- group: other
  title: ''
  type: Trailhead
  url: https://trailhead.salesforce.com/content/learn/trails/automate_business_processes
- group: auth
  title: ''
  type: Authentication
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
- group: company
  title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesforce.com/
- group: operate
  title: ''
  type: Support
  url: https://help.salesforce.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/agreements/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salesforce
- group: operate
  title: ''
  type: Community
  url: https://trailhead.salesforce.com/trailblazer-community/topics/salesforcedeveloper
created: '2024-01-15'
description: Salesforce Automation System refers to the collection of APIs and tools within Salesforce for automating business processes, including Flow Builder, approval processes, Process Builder, and Workflow Rules. These capabilities enable organizations to automate CRM, sales, marketing, and customer service workflows programmatically via the Salesforce REST API.
examples:
- key_count: 6
  name: Salesforce Invoke Flow Example
  slug: salesforce-invoke-flow-example
- key_count: 6
  name: Salesforce Submit Approval Example
  slug: salesforce-submit-approval-example
finops:
- name: Salesforce Automation System Finops
  service_category: CRM / Automation
  slug: salesforce-automation-system-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/salesforce-automation-system.png
json_schemas:
- name: Salesforce Approval Request
  property_count: 1
  slug: salesforce-approval-request
- name: Salesforce Flow Definition
  property_count: 12
  slug: salesforce-flow-definition
json_structures:
- name: Salesforce Automation System Structure
  property_count: 0
  slug: salesforce-automation-system-structure
jsonld:
- class_count: 1
  name: Salesforce Automation System Context
  property_count: 20
  slug: salesforce-automation-system-context
layout: provider
modified: '2026-05-19'
name: Salesforce Automation System
nav: Providers
network: true
overview: 'Salesforce Automation System publishes 2 APIs on the [APIs.io](https://apis.io/) network: Flows API and Process Automation API. Tagged areas include Approval Process, Automation, CRM, Flow, and Process Builder.


  The Salesforce Automation System catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Salesforce Automation System''s developer surface includes authentication, documentation, engineering blog, support, and 12 more developer resources.'
plans:
- name: Salesforce Automation System Plans Pricing
  plan_count: 1
  slug: salesforce-automation-system-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Salesforce Automation System Rate Limits
  slug: salesforce-automation-system-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Salesforce Automation System API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: salesforce-automation-system-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Salesforce Automation System API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: salesforce-automation-system-rules
scopes:
- name: Salesforce Automation System Scopes
  scope_count: 2
  slug: salesforce-automation-system-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 47.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 28.8
    contract_quality: 70.9
    developer_ergonomics: 61.9
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salesforce-automation-system/refs/heads/main/screenshots/salesforce-automation-system-2026-06-20T193343.png
security:
- kind: authentication
  name: Salesforce Automation System Authentication
  slug: salesforce-automation-system-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Salesforce Automation System Domain Security
  slug: salesforce-automation-system-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: salesforce-automation-system
tags:
- Approval Process
- Automation
- CRM
- Flow
- Process Builder
- Salesforce
- Workflows
website: https://developer.salesforce.com/
---
