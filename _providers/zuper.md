---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Zuper Agentic Access
  operation_count: 69
  slug: zuper-agentic-access
  summary_line: 69 operations · 43 acting
api_count: 14
apis:
- description: Asset tracking — lifecycle management, inspection forms, bulk operations, and history
  name: Zuper Assets API
  slug: zuper-assets-api
- description: API key generation and base URL discovery
  name: Zuper Authentication API
  slug: zuper-authentication-api
- description: Customer relationship management — create, update, search, and manage customer records
  name: Zuper Customers API
  slug: zuper-customers-api
- description: Invoice generation, management, and status tracking
  name: Zuper Invoices API
  slug: zuper-invoices-api
- description: Job lifecycle management — creation, scheduling, assignment, status updates, and route optimization
  name: Zuper Jobs API
  slug: zuper-jobs-api
- description: Customer organization (account) management
  name: Zuper Organizations API
  slug: zuper-organizations-api
- description: Multi-job project management with phases, milestones, and dependencies
  name: Zuper Projects API
  slug: zuper-projects-api
- description: Service property management and service task assignment
  name: Zuper Properties API
  slug: zuper-properties-api
- description: Vendor purchase order management
  name: Zuper Purchase Orders API
  slug: zuper-purchase-orders-api
- description: Field team management and assignments
  name: Zuper Teams API
  slug: zuper-teams-api
- description: Field staff timesheet and time-off management
  name: Zuper Timesheets API
  slug: zuper-timesheets-api
- description: Platform user management and skills tracking
  name: Zuper Users API
  slug: zuper-users-api
- description: Vendor management and catalog operations
  name: Zuper Vendors API
  slug: zuper-vendors-api
- description: Webhook registration and event subscription management
  name: Zuper Webhooks API
  slug: zuper-webhooks-api
artifact_total: 44
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zuper REST Assets API
  slug: open-zuper-assets-api
- collection_type: open
  name: Zuper REST Assets Authentication API
  slug: open-zuper-authentication-api
- collection_type: open
  name: Zuper REST Assets Customers API
  slug: open-zuper-customers-api
- collection_type: open
  name: Zuper REST Assets Invoices API
  slug: open-zuper-invoices-api
- collection_type: open
  name: Zuper REST Assets Jobs API
  slug: open-zuper-jobs-api
- collection_type: open
  name: Zuper REST Assets Organizations API
  slug: open-zuper-organizations-api
- collection_type: open
  name: Zuper REST Assets Projects API
  slug: open-zuper-projects-api
- collection_type: open
  name: Zuper REST Assets Properties API
  slug: open-zuper-properties-api
- collection_type: open
  name: Zuper REST Assets Purchase Orders API
  slug: open-zuper-purchase-orders-api
- collection_type: open
  name: Zuper REST Assets Teams API
  slug: open-zuper-teams-api
- collection_type: open
  name: Zuper REST Assets Timesheets API
  slug: open-zuper-timesheets-api
- collection_type: open
  name: Zuper REST Assets Users API
  slug: open-zuper-users-api
- collection_type: open
  name: Zuper REST Assets Vendors API
  slug: open-zuper-vendors-api
- collection_type: open
  name: Zuper REST Assets Webhooks API
  slug: open-zuper-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zuper-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zuper-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zuper-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zuper-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.zuper.co/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.zuper.co/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ZuperHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zuperco/
- group: company
  title: ''
  type: Blog
  url: https://www.zuper.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zuper.co/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zuper.co/
- group: other
  title: ''
  type: X
  url: https://x.com/zuperinc
- group: commercial
  title: ''
  type: Plans
  url: plans/zuper-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zuper-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zuper-finops.yml
created: '2026-06-13'
description: Zuper is an intelligent field service management platform that consolidates job scheduling, dispatching, customer management, invoicing, timesheets, and field team operations into a single AI-powered operating system. The Zuper REST API gives developers programmatic access to all platform data, enabling seamless integration with third-party systems across jobs, assets, projects, inventory, contracts, and financials. Authentication is handled via API keys transmitted through the x-api-key header, with region-specific base URLs discovered at runtime. The API supports over 300 endpoints organized across functional areas including customers, jobs, scheduling, proposals, purchase orders, timesheets, teams, and communications. Zuper also provides a server-side SDK via npm (zuper-sdk) and a Model Context Protocol (MCP) server for AI agent integration.
examples:
- key_count: 3
  name: Zuper Create Customer Example
  slug: zuper-create-customer-example
- key_count: 3
  name: Zuper Create Job Example
  slug: zuper-create-job-example
- key_count: 3
  name: Zuper Get Jobs Example
  slug: zuper-get-jobs-example
finops:
- name: Zuper Finops
  service_category: ''
  slug: zuper-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zuper.png
json_schemas:
- name: Zuper Asset
  property_count: 20
  slug: zuper-asset
- name: Zuper Customer
  property_count: 19
  slug: zuper-customer
- name: Zuper Job
  property_count: 21
  slug: zuper-job
jsonld:
- class_count: 12
  name: Zuper Context
  property_count: 65
  slug: zuper-context
layout: provider
modified: '2026-06-13'
name: Zuper
nav: Providers
network: true
overview: 'Zuper publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Authentication API, Customers API, and 11 more. Tagged areas include Field Service Management, Scheduling, Dispatching, Invoicing, and Timesheets.


  The Zuper catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zuper''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Zuper Plans Pricing
  plan_count: 3
  slug: zuper-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Zuper Rate Limits
  slug: zuper-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Zuper API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zuper-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.3
  delta: -9.8
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 67.0
    developer_ergonomics: 13.1
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 54.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/zuper/refs/heads/main/screenshots/zuper-2026-06-20T202002.png
security:
- kind: authentication
  name: Zuper Authentication
  slug: zuper-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Zuper Domain Security
  slug: zuper-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Zuper Trust Center
  slug: zuper-trust-center
  summary_line: SOC 2, ISO 27001
slug: zuper
tags:
- Field Service Management
- Scheduling
- Dispatching
- Invoicing
- Timesheets
- Asset Management
- Work Orders
- Customer Management
- Inventory
- Projects
website: https://www.zuper.co/
---
