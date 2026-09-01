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
    delegated_identity: documented
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
  score: 21.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 36
  human_in_the_loop: 0
  name: Servicem8 Agentic Access
  operation_count: 63
  slug: servicem8-agentic-access
  summary_line: 63 operations · 36 acting
api_count: 1
apis:
- description: Files linked to jobs - photos, PDFs, signed documents.
  name: ServiceM8 Attachments API
  slug: servicem8-attachments-api
- description: Coloured labels used to tag jobs and clients.
  name: ServiceM8 Badges API
  slug: servicem8-badges-api
- description: Companies (clients/customers) and their contacts.
  name: ServiceM8 Clients API
  slug: servicem8-clients-api
- description: Scheduled bookings and recorded time entries on a job.
  name: ServiceM8 Job Activities API
  slug: servicem8-job-activities-api
- description: People attached to a specific job (billing, site, etc.).
  name: ServiceM8 Job Contacts API
  slug: servicem8-job-contacts-api
- description: Jobs - the central record for a piece of work.
  name: ServiceM8 Jobs API
  slug: servicem8-jobs-api
- description: Materials catalog and job material line items.
  name: ServiceM8 Materials API
  slug: servicem8-materials-api
- description: Workflow stages jobs move through.
  name: ServiceM8 Queues API
  slug: servicem8-queues-api
- description: Staff members - technicians and office users.
  name: ServiceM8 Staff API
  slug: servicem8-staff-api
- description: ServiceM8 account records an integration operates against.
  name: ServiceM8 Vendors API
  slug: servicem8-vendors-api
- description: Object and event webhook subscriptions.
  name: ServiceM8 Webhooks API
  slug: servicem8-webhooks-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ServiceM8 REST Attachments API
  slug: open-servicem8-attachments-api
- collection_type: open
  name: ServiceM8 REST Attachments Badges API
  slug: open-servicem8-badges-api
- collection_type: open
  name: ServiceM8 REST Attachments Clients API
  slug: open-servicem8-clients-api
- collection_type: open
  name: ServiceM8 REST Attachments Job Activities API
  slug: open-servicem8-job-activities-api
- collection_type: open
  name: ServiceM8 REST Attachments Job Contacts API
  slug: open-servicem8-job-contacts-api
- collection_type: open
  name: ServiceM8 REST Attachments Jobs API
  slug: open-servicem8-jobs-api
- collection_type: open
  name: ServiceM8 REST Attachments Materials API
  slug: open-servicem8-materials-api
- collection_type: open
  name: ServiceM8 REST Attachments Queues API
  slug: open-servicem8-queues-api
- collection_type: open
  name: ServiceM8 REST Attachments Staff API
  slug: open-servicem8-staff-api
- collection_type: open
  name: ServiceM8 REST Attachments Vendors API
  slug: open-servicem8-vendors-api
- collection_type: open
  name: ServiceM8 REST Attachments Webhooks API
  slug: open-servicem8-webhooks-api
- collection_type: open
  name: ServiceM8 REST API
  slug: open-servicem8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/servicem8-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/servicem8-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/servicem8-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/servicem8-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/servicem8-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/servicem8
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/servicem8
- group: company
  title: ''
  type: Website
  url: https://www.servicem8.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.servicem8.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/servicem8-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/servicem8-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/servicem8-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.servicem8.com/feed/
created: '2026-07-03'
description: ServiceM8 is field service and job management software for trade and home-service businesses - electricians, plumbers, HVAC, cleaners, landscapers, and similar contractors. It manages the full job lifecycle from lead and quote through scheduling, dispatch, on-site work, materials, invoicing, and payment. ServiceM8 publishes a documented REST API at https://api.servicem8.com/api_1.0 that exposes its core objects - Jobs, Job Activities, Clients (Companies), Contacts, Staff, Materials, Job Materials, Attachments, Queues, Vendors, and Badges - as plain JSON over HTTP using GET, POST, and DELETE. Private integrations authenticate with an API key (X-API-Key header); public add-ons use OAuth 2.0. Object and event webhook subscriptions push change notifications to a callback URL.
finops:
- name: Servicem8 Finops
  service_category: Field Service Management Software
  slug: servicem8-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/servicem8.png
layout: provider
modified: '2026-07-03'
name: ServiceM8
nav: Providers
network: true
overview: 'ServiceM8 publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Attachments API, Badges API, Clients API, and 8 more. Tagged areas include Field Service, Job Management, Trades, Scheduling, and Dispatch.


  ServiceM8''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Servicem8 Plans Pricing
  plan_count: 5
  slug: servicem8-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Servicem8 Rate Limits
  slug: servicem8-rate-limits
scopes:
- name: Servicem8 Scopes
  scope_count: 11
  slug: servicem8-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: developing
  composite: 39.5
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
    contract_quality: 52.6
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Servicem8 Authentication
  slug: servicem8-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Servicem8 Domain Security
  slug: servicem8-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Servicem8 Vulnerability Disclosure
  slug: servicem8-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: servicem8
tags:
- Field Service
- Job Management
- Trades
- Scheduling
- Dispatch
- Invoicing
- Home Services
website: https://www.servicem8.com
---
