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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Cflow Agentic Access
  operation_count: 12
  slug: cflow-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 3
apis:
- description: Operations for managing workflow requests.
  name: Cflow Requests API
  slug: cflow-requests-api
- description: Operations for managing users and roles.
  name: Cflow Users API
  slug: cflow-users-api
- description: Operations for managing workflows.
  name: Cflow Workflows API
  slug: cflow-workflows-api
artifact_total: 56
collections:
- collection_type: postman
  name: Cflow Requests API
  slug: postman-cflow-requests-api
- collection_type: postman
  name: Cflow Requests Users API
  slug: postman-cflow-users-api
- collection_type: postman
  name: Cflow Requests Workflows API
  slug: postman-cflow-workflows-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cflow Requests API
  slug: open-cflow-requests-api
- collection_type: open
  name: Cflow Requests Users API
  slug: open-cflow-users-api
- collection_type: open
  name: Cflow Requests Workflows API
  slug: open-cflow-workflows-api
- collection_type: open
  name: Cflow API
  slug: open-cflow
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cflow/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cflow-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cflow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cflow-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cflowapps
- group: company
  title: ''
  type: Website
  url: https://www.cflowapps.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.cflowapps.com/workflow/workflow-api/
- group: start
  title: ''
  type: Signup
  url: https://www.cflowapps.com/sign-up/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cflowapps.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.cflowapps.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.cflowapps.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cflowapps.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cflowapps.com/privacy-policy/
- group: agent
  title: ''
  type: LlmsText
  url: https://cflowapps.com/llms.txt
created: '2025-01-08'
description: Cflow is a cloud-based workflow automation platform that helps organizations streamline and optimize business processes. It offers a drag-and-drop workflow builder, customizable forms, rule-based routing, approval flows, integrations with popular business applications, and real-time analytics. Cflow exposes a REST API allowing developers to list workflows, submit and manage requests, approve or reject tasks, and manage users and roles programmatically.
features:
- name: Drag-and-Drop Workflow Builder
- name: Custom Forms
- name: Conditional Rules
- name: Multi-Level Approvals
- name: Role-Based Access Control
- name: Real-Time Analytics
- name: Dashboards
- name: Email Notifications
- name: Mobile Access
- name: Audit Trails
- name: REST API
- name: Webhooks
- name: Integrations
- name: No-Code
- name: Low-Code
- name: Parallel Approvals
- name: Sequential Approvals
- name: Escalations
- name: Reminders
- name: Reports
finops:
- name: Cflow Finops
  service_category: API
  slug: cflow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cflow.png
json_schemas:
- name: Cflow Request
  property_count: 8
  slug: request
- name: Cflow Role
  property_count: 3
  slug: role
- name: Cflow Stage
  property_count: 4
  slug: stage
- name: Cflow User
  property_count: 5
  slug: user
- name: Cflow Workflow
  property_count: 7
  slug: workflow
jsonld:
- class_count: 3
  name: Cflow Context
  property_count: 15
  slug: cflow-context
layout: provider
modified: '2026-05-19'
name: Cflow
nav: Providers
network: true
overview: 'Cflow publishes 3 APIs on the [APIs.io](https://apis.io/) network: Requests API, Users API, and Workflows API. Tagged areas include Automations, Business Process Automation, Integrations, No-Code, and Platform.


  The Cflow catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cflow''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, support, and 8 more developer resources.'
plans:
- name: Cflow Plans Pricing
  plan_count: 3
  slug: cflow-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 5
  name: Cflow Rate Limits
  slug: cflow-rate-limits
rules:
- name: Cflow API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cflow-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.4
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 76.1
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 7.9
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cflow/refs/heads/main/screenshots/cflow-2026-06-20T174158.png
security:
- kind: authentication
  name: Cflow Authentication
  slug: cflow-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Cflow Domain Security
  slug: cflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cflow
tags:
- Automations
- Business Process Automation
- Integrations
- No-Code
- Platform
- Protocols
- Rules
- Workflows
use_cases:
- name: Purchase Request Approval
- name: Employee Onboarding
- name: Leave Requests
- name: Expense Approval
- name: Travel Requests
- name: Vendor Onboarding
- name: Invoice Approval
- name: Capital Expenditure Requests
- name: Document Approval
- name: Change Management
- name: Compliance Workflows
- name: Help Desk Ticketing
website: https://www.cflowapps.com
---
