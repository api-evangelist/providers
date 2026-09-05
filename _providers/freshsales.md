---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Freshsales Agentic Access
  operation_count: 42
  slug: freshsales-agentic-access
  summary_line: 42 operations · 27 acting
api_count: 1
apis:
- description: REST API for managing contacts, sales accounts, deals, tasks, appointments, notes, and CPQ products in Freshsales. Authentication uses a token-based scheme via the Authorization header tied to a bundl
  name: Freshsales CRM API
  slug: crm-api
- baseURL: https://<bundle-alias>.myfreshworks.com/crm/sales/api
  baseurl_source: declared
  description: The Appointments API from Freshsales — 2 operation(s) for appointments.
  name: Freshsales Appointments API
  slug: freshsales-appointments-api
- baseURL: https://<bundle-alias>.myfreshworks.com/crm/sales/api
  baseurl_source: declared
  description: The Calls API from Freshsales — 1 operation(s) for calls.
  name: Freshsales Calls API
  slug: freshsales-calls-api
- baseURL: https://<bundle-alias>.myfreshworks.com/crm/sales/api
  baseurl_source: declared
  description: The Contacts API from Freshsales — 7 operation(s) for contacts.
  name: Freshsales Contacts API
  slug: freshsales-contacts-api
- baseURL: https://<bundle-alias>.myfreshworks.com/crm/sales/api
  baseurl_source: declared
  description: The Deals API from Freshsales — 3 operation(s) for deals.
  name: Freshsales Deals API
  slug: freshsales-deals-api
- baseURL: https://<bundle-alias>.myfreshworks.com/crm/sales/api
  baseurl_source: declared
  description: The Jobs API from Freshsales — 1 operation(s) for jobs.
  name: Freshsales Jobs API
  slug: freshsales-jobs-api
- baseURL: https://<bundle-alias>.myfreshworks.com/crm/sales/api
  baseurl_source: declared
  description: The Lists API from Freshsales — 2 operation(s) for lists.
  name: Freshsales Lists API
  slug: freshsales-lists-api
- baseURL: https://<bundle-alias>.myfreshworks.com/crm/sales/api
  baseurl_source: declared
  description: The Notes API from Freshsales — 2 operation(s) for notes.
  name: Freshsales Notes API
  slug: freshsales-notes-api
- baseURL: https://<bundle-alias>.myfreshworks.com/crm/sales/api
  baseurl_source: declared
  description: The Products API from Freshsales — 2 operation(s) for products.
  name: Freshsales Products API
  slug: freshsales-products-api
- baseURL: https://<bundle-alias>.myfreshworks.com/crm/sales/api
  baseurl_source: declared
  description: The SalesAccounts API from Freshsales — 3 operation(s) for salesaccounts.
  name: Freshsales SalesAccounts API
  slug: freshsales-salesaccounts-api
- baseURL: https://<bundle-alias>.myfreshworks.com/crm/sales/api
  baseurl_source: declared
  description: The SalesActivities API from Freshsales — 1 operation(s) for salesactivities.
  name: Freshsales SalesActivities API
  slug: freshsales-salesactivities-api
- baseURL: https://<bundle-alias>.myfreshworks.com/crm/sales/api
  baseurl_source: declared
  description: The Search API from Freshsales — 1 operation(s) for search.
  name: Freshsales Search API
  slug: freshsales-search-api
- baseURL: https://<bundle-alias>.myfreshworks.com/crm/sales/api
  baseurl_source: declared
  description: The Tasks API from Freshsales — 2 operation(s) for tasks.
  name: Freshsales Tasks API
  slug: freshsales-tasks-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Freshsales CRM Appointments API
  slug: open-freshsales-appointments-api
- collection_type: open
  name: Freshsales CRM Appointments Calls API
  slug: open-freshsales-calls-api
- collection_type: open
  name: Freshsales CRM Appointments Contacts API
  slug: open-freshsales-contacts-api
- collection_type: open
  name: Freshsales CRM Appointments Deals API
  slug: open-freshsales-deals-api
- collection_type: open
  name: Freshsales CRM Appointments Jobs API
  slug: open-freshsales-jobs-api
- collection_type: open
  name: Freshsales CRM Appointments Lists API
  slug: open-freshsales-lists-api
- collection_type: open
  name: Freshsales CRM Appointments Notes API
  slug: open-freshsales-notes-api
- collection_type: open
  name: Freshsales CRM Appointments Products API
  slug: open-freshsales-products-api
- collection_type: open
  name: Freshsales CRM Appointments SalesAccounts API
  slug: open-freshsales-salesaccounts-api
- collection_type: open
  name: Freshsales CRM Appointments SalesActivities API
  slug: open-freshsales-salesactivities-api
- collection_type: open
  name: Freshsales CRM Appointments Search API
  slug: open-freshsales-search-api
- collection_type: open
  name: Freshsales CRM Appointments Tasks API
  slug: open-freshsales-tasks-api
- collection_type: open
  name: Freshsales CRM API
  slug: open-freshsales
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freshsales-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/freshsales-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/freshsales-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freshsales-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freshsales-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freshworks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freshsales-crm
- group: company
  title: ''
  type: Website
  url: https://www.freshworks.com/crm/sales/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.freshworks.com/crm/api/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.freshworks.com/crm/api/
- group: start
  title: ''
  type: Signup
  url: https://www.freshworks.com/crm/sales/signup/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.freshworks.com/crm/sales/pricing/
- group: operate
  title: ''
  type: Support
  url: https://support.freshsales.io/
created: '2026-05-11'
description: Freshsales is the CRM application from Freshworks designed for sales teams, offering contact and account management, deal pipelines, AI-powered lead scoring, built-in phone and email, sales sequences, and CPQ. The Freshsales REST API enables CRUD access to contacts, accounts, deals, tasks, appointments, notes, and products for building integrations and sales workflow automation.
graphqls:
- description: This conceptual GraphQL schema represents the Freshsales CRM API domain model. Freshsales is the CRM application from Freshworks designed for sales teams, offering contact and account management, deal
  name: Freshsales GraphQL Schema
  slug: freshsales-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freshsales.png
layout: provider
modified: '2026-05-11'
name: Freshsales
nav: Providers
network: true
overview: 'Freshsales publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Calls API, Contacts API, and 9 more. Tagged areas include CRM, Sales, Contacts, Deals, and Pipeline.


  Freshsales'' developer surface includes authentication, documentation, signup flow, pricing, support, and 8 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 53.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 31.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freshsales/refs/heads/main/screenshots/freshsales-2026-06-20T181548.png
security:
- kind: authentication
  name: Freshsales Authentication
  slug: freshsales-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Freshsales Domain Security
  slug: freshsales-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Freshsales Vulnerability Disclosure
  slug: freshsales-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Freshsales Trust Center
  slug: freshsales-trust-center
  summary_line: SOC 2, ISO 27001, CSA STAR
slug: freshsales
tags:
- CRM
- Sales
- Contacts
- Deals
- Pipeline
- Lead Management
- Freshworks
website: https://www.freshworks.com/crm/sales/
---
