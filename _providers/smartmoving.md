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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Smartmoving Agentic Access
  operation_count: 24
  slug: smartmoving-agentic-access
  summary_line: 24 operations · 6 acting
api_count: 6
apis:
- description: Customer (contact / account) records.
  name: SmartMoving Customers API
  slug: smartmoving-customers-api
- description: Jobs (booked moves) attached to opportunities.
  name: SmartMoving Jobs API
  slug: smartmoving-jobs-api
- description: Inbound lead intake from websites and third-party providers.
  name: SmartMoving Lead Provider API
  slug: smartmoving-lead-provider-api
- description: Sales pipeline leads and their statuses.
  name: SmartMoving Leads API
  slug: smartmoving-leads-api
- description: Sales opportunities - quotes and estimates.
  name: SmartMoving Opportunities API
  slug: smartmoving-opportunities-api
- description: Account lookup data - branches, users, service types, referral sources.
  name: SmartMoving Reference Data API
  slug: smartmoving-reference-data-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SmartMoving Open Customers API
  slug: open-smartmoving-customers-api
- collection_type: open
  name: SmartMoving Open Customers Jobs API
  slug: open-smartmoving-jobs-api
- collection_type: open
  name: SmartMoving Open Customers Lead Provider API
  slug: open-smartmoving-lead-provider-api
- collection_type: open
  name: SmartMoving Open Customers Leads API
  slug: open-smartmoving-leads-api
- collection_type: open
  name: SmartMoving Open Customers Opportunities API
  slug: open-smartmoving-opportunities-api
- collection_type: open
  name: SmartMoving Open Customers Reference Data API
  slug: open-smartmoving-reference-data-api
- collection_type: open
  name: SmartMoving Open API
  slug: open-smartmoving
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smartmoving-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smartmoving-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smartmoving-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.smartmoving.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smartmoving-software
- group: docs
  title: ''
  type: Documentation
  url: https://help.smartmoving.com/en/articles/9739804-smartmoving-s-open-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://smartmoving-prod-api-management.developer.azure-api.net/
- group: commercial
  title: ''
  type: Plans
  url: plans/smartmoving-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smartmoving-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smartmoving-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.smartmoving.com/blog/rss.xml
created: '2026-07-04'
description: SmartMoving is an all-in-one CRM and operations platform for moving companies, covering lead capture, sales and estimating, booking, dispatch and scheduling, storage, and customer follow-up. SmartMoving exposes a documented Open API (Azure API Management) to Growth Plan customers, authenticated with an x-api-key header, that reads and writes the platform's core CRM objects - customers, opportunities (quotes/estimates), leads, jobs/moves, payments, and follow-ups - plus a free, universally available Lead API for pushing new leads into an account from any lead provider or website. The API is offered in two tiers - Basic (read-only, for reporting and analytics) and Premium (read/write plus webhooks, for full integration and automation).
finops:
- name: Smartmoving Finops
  service_category: Business Software - Moving CRM
  slug: smartmoving-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smartmoving.png
layout: provider
modified: '2026-07-04'
name: SmartMoving
nav: Providers
network: true
overview: 'SmartMoving publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Jobs API, Lead Provider API, and 3 more. Tagged areas include Moving Software, CRM, Field Service, Moving Company, and Operations.


  SmartMoving''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Smartmoving Plans Pricing
  plan_count: 3
  slug: smartmoving-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Smartmoving Rate Limits
  slug: smartmoving-rate-limits
score:
  band: developing
  composite: 40.4
  delta: -0.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 57.3
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Smartmoving Authentication
  slug: smartmoving-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Smartmoving Domain Security
  slug: smartmoving-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smartmoving
tags:
- Moving Software
- CRM
- Field Service
- Moving Company
- Operations
- Lead Management
- Dispatch
website: https://www.smartmoving.com
---
