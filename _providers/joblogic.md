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
    agentic_commerce: false
    auth_clarity: negotiable
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
  score: 22.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Joblogic Agentic Access
  operation_count: 52
  slug: joblogic-agentic-access
  summary_line: 52 operations · 39 acting
api_count: 1
apis:
- baseURL: https://api.joblogic.com/api/v1
  baseurl_source: declared
  description: Equipment and plant assets located at sites.
  name: Joblogic Assets API
  slug: joblogic-assets-api
- baseURL: https://api.joblogic.com/api/v1
  baseurl_source: declared
  description: Contacts attached to customers, sites, suppliers, and subcontractors.
  name: Joblogic Contacts API
  slug: joblogic-contacts-api
- baseURL: https://api.joblogic.com/api/v1
  baseurl_source: declared
  description: Customer account records.
  name: Joblogic Customers API
  slug: joblogic-customers-api
- baseURL: https://api.joblogic.com/api/v1
  baseurl_source: declared
  description: Field engineers / mobile workforce.
  name: Joblogic Engineers API
  slug: joblogic-engineers-api
- baseURL: https://api.joblogic.com/api/v1
  baseurl_source: declared
  description: Standard, customer-grouped, and PPM invoices.
  name: Joblogic Invoices API
  slug: joblogic-invoices-api
- baseURL: https://api.joblogic.com/api/v1
  baseurl_source: declared
  description: Work orders and their costs.
  name: Joblogic Jobs API
  slug: joblogic-jobs-api
- baseURL: https://api.joblogic.com/api/v1
  baseurl_source: declared
  description: Quotes and estimates.
  name: Joblogic Quotes API
  slug: joblogic-quotes-api
- baseURL: https://api.joblogic.com/api/v1
  baseurl_source: declared
  description: Physical service locations belonging to a customer.
  name: Joblogic Sites API
  slug: joblogic-sites-api
- baseURL: https://api.joblogic.com/api/v1
  baseurl_source: declared
  description: Engineer visits scheduled against jobs.
  name: Joblogic Visits API
  slug: joblogic-visits-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Joblogic Assets API
  slug: open-joblogic-assets-api
- collection_type: open
  name: Joblogic Assets Contacts API
  slug: open-joblogic-contacts-api
- collection_type: open
  name: Joblogic Assets Customers API
  slug: open-joblogic-customers-api
- collection_type: open
  name: Joblogic Assets Engineers API
  slug: open-joblogic-engineers-api
- collection_type: open
  name: Joblogic Assets Invoices API
  slug: open-joblogic-invoices-api
- collection_type: open
  name: Joblogic Assets Jobs API
  slug: open-joblogic-jobs-api
- collection_type: open
  name: Joblogic Assets Quotes API
  slug: open-joblogic-quotes-api
- collection_type: open
  name: Joblogic Assets Sites API
  slug: open-joblogic-sites-api
- collection_type: open
  name: Joblogic Assets Visits API
  slug: open-joblogic-visits-api
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
random_paper: 1
rate_limits:
- limit_count: 2
  name: Joblogic Rate Limits
  slug: joblogic-rate-limits
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.8
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- Software-as-a-Service
website: https://www.joblogic.com
---
