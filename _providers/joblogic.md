---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Joblogic Agentic Access
  operation_count: 52
  slug: joblogic-agentic-access
  summary_line: 52 operations · 39 acting
api_count: 9
apis:
- description: Equipment and plant assets located at sites.
  name: Joblogic Assets API
  slug: joblogic-assets-api
- description: Contacts attached to customers, sites, suppliers, and subcontractors.
  name: Joblogic Contacts API
  slug: joblogic-contacts-api
- description: Customer account records.
  name: Joblogic Customers API
  slug: joblogic-customers-api
- description: Field engineers / mobile workforce.
  name: Joblogic Engineers API
  slug: joblogic-engineers-api
- description: Standard, customer-grouped, and PPM invoices.
  name: Joblogic Invoices API
  slug: joblogic-invoices-api
- description: Work orders and their costs.
  name: Joblogic Jobs API
  slug: joblogic-jobs-api
- description: Quotes and estimates.
  name: Joblogic Quotes API
  slug: joblogic-quotes-api
- description: Physical service locations belonging to a customer.
  name: Joblogic Sites API
  slug: joblogic-sites-api
- description: Engineer visits scheduled against jobs.
  name: Joblogic Visits API
  slug: joblogic-visits-api
artifact_total: 16
collections:
- collection_type: open
  name: Joblogic API
  slug: open-joblogic
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/joblogic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/joblogic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/joblogic-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/job-logic
- group: company
  title: ''
  type: Website
  url: https://www.joblogic.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.joblogic.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/joblogic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/joblogic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/joblogic-finops.yml
created: '2026-07-12'
description: Joblogic is a cloud field service management (FSM) platform for trades, service, and maintenance contractors - covering customers, sites, assets, jobs, engineer scheduling, mobile workforce, quotes, invoices, stock, and PPM (planned preventative maintenance) contracts. Joblogic exposes a REST API (base path /api/v1) secured with OAuth2 client-credentials tokens issued by a Joblogic IdentityServer, plus outbound webhooks for change events. API access is customer-provisioned - Joblogic issues a Client ID, Client Secret, and Tenant ID and IP-allowlists callers behind a firewall, with a UAT sandbox for integration development.
finops:
- name: Joblogic Finops
  service_category: Field Service Management Software
  slug: joblogic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/joblogic.png
layout: provider
modified: '2026-07-12'
name: Joblogic
nav: Providers
network: true
overview: 'Joblogic publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Contacts API, Customers API, and 6 more. Tagged areas include Field Service Management, Job Management, Scheduling, Maintenance, and Workforce.


  Joblogic''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Joblogic Plans Pricing
  plan_count: 3
  slug: joblogic-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 2
  name: Joblogic Rate Limits
  slug: joblogic-rate-limits
score:
  band: thin
  composite: 35.7
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.1
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/joblogic/refs/heads/main/screenshots/joblogic-2026-07-25T223221.png
security:
- kind: authentication
  name: Joblogic Authentication
  slug: joblogic-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Joblogic Domain Security
  slug: joblogic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: joblogic
tags:
- Field Service Management
- Job Management
- Scheduling
- Maintenance
- Workforce
- Mobile Workforce
- Trades
- CRM
- SaaS
website: https://www.joblogic.com
---
