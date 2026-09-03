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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Smartmoving Agentic Access
  operation_count: 24
  slug: smartmoving-agentic-access
  summary_line: 24 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.smartmoving.com/api
  baseurl_source: declared
  description: Customer (contact / account) records.
  name: SmartMoving Customers API
  slug: smartmoving-customers-api
- baseURL: https://api.smartmoving.com/api
  baseurl_source: declared
  description: Jobs (booked moves) attached to opportunities.
  name: SmartMoving Jobs API
  slug: smartmoving-jobs-api
- baseURL: https://api.smartmoving.com/api
  baseurl_source: declared
  description: Inbound lead intake from websites and third-party providers.
  name: SmartMoving Lead Provider API
  slug: smartmoving-lead-provider-api
- baseURL: https://api.smartmoving.com/api
  baseurl_source: declared
  description: Sales pipeline leads and their statuses.
  name: SmartMoving Leads API
  slug: smartmoving-leads-api
- baseURL: https://api.smartmoving.com/api
  baseurl_source: declared
  description: Sales opportunities - quotes and estimates.
  name: SmartMoving Opportunities API
  slug: smartmoving-opportunities-api
- baseURL: https://api.smartmoving.com/api
  baseurl_source: declared
  description: Account lookup data - branches, users, service types, referral sources.
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
overview: 'SmartMoving publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Jobs API, Lead Provider API, and 3 more. Tagged areas include Moving Software, CRM, Field Service, Moving Company, and Lead Management.


  SmartMoving''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Smartmoving Plans Pricing
  plan_count: 3
  slug: smartmoving-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Smartmoving Rate Limits
  slug: smartmoving-rate-limits
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 13.9
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smartmoving/refs/heads/main/screenshots/smartmoving-2026-09-02T155934.png
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
- Lead Management
- Dispatch
website: https://www.smartmoving.com
---
