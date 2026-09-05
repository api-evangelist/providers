---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    delegated_identity: documented
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
  score: 22.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Accelo Agentic Access
  operation_count: 29
  slug: accelo-agentic-access
  summary_line: 29 operations · 14 acting
api_count: 1
apis:
- description: REST API for Accelo with CRUD access to companies, contacts, activities, tasks, projects (jobs), milestones, invoices, contracts, quotes, prospects, time entries, staff, and webhooks. Uses OAuth 2.0 (
  name: Accelo REST API
  slug: accelo-api
- baseURL: https://{deployment}.api.accelo.com/api/v0
  baseurl_source: declared
  description: The Activities API from Accelo — 4 operation(s) for activities.
  name: Accelo Activities API
  slug: accelo-activities-api
- baseURL: https://{deployment}.api.accelo.com/api/v0
  baseurl_source: declared
  description: The Companies API from Accelo — 2 operation(s) for companies.
  name: Accelo Companies API
  slug: accelo-companies-api
- baseURL: https://{deployment}.api.accelo.com/api/v0
  baseurl_source: declared
  description: The Contacts API from Accelo — 2 operation(s) for contacts.
  name: Accelo Contacts API
  slug: accelo-contacts-api
- baseURL: https://{deployment}.api.accelo.com/api/v0
  baseurl_source: declared
  description: The Issues API from Accelo — 2 operation(s) for issues.
  name: Accelo Issues API
  slug: accelo-issues-api
- baseURL: https://{deployment}.api.accelo.com/api/v0
  baseurl_source: declared
  description: The Jobs API from Accelo — 2 operation(s) for jobs.
  name: Accelo Jobs API
  slug: accelo-jobs-api
- baseURL: https://{deployment}.api.accelo.com/api/v0
  baseurl_source: declared
  description: The OAuth API from Accelo — 1 operation(s) for oauth.
  name: Accelo OAuth API
  slug: accelo-oauth-api
- baseURL: https://{deployment}.api.accelo.com/api/v0
  baseurl_source: declared
  description: The Tasks API from Accelo — 2 operation(s) for tasks.
  name: Accelo Tasks API
  slug: accelo-tasks-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Accelo REST Activities API
  slug: open-accelo-activities-api
- collection_type: open
  name: Accelo REST Activities Companies API
  slug: open-accelo-companies-api
- collection_type: open
  name: Accelo REST Activities Contacts API
  slug: open-accelo-contacts-api
- collection_type: open
  name: Accelo REST Activities Issues API
  slug: open-accelo-issues-api
- collection_type: open
  name: Accelo REST Activities Jobs API
  slug: open-accelo-jobs-api
- collection_type: open
  name: Accelo REST Activities OAuth API
  slug: open-accelo-oauth-api
- collection_type: open
  name: Accelo REST Activities Tasks API
  slug: open-accelo-tasks-api
- collection_type: open
  name: Accelo REST API
  slug: open-accelo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/accelo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accelo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/accelo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/accelo-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Accelo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/accelo
- group: company
  title: ''
  type: Website
  url: https://www.accelo.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.accelo.com/docs/
- group: start
  title: ''
  type: Signup
  url: https://www.accelo.com/signup/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.accelo.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.accelo.com/login/
- group: operate
  title: ''
  type: Support
  url: https://help.accelo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.accelo.com/resources/blog/
created: '2026-05-11'
description: Accelo is a cloud-based service operations automation (ServOps) platform that unifies project management, client relationship management (CRM), time tracking, retainers, quotes, billing, and invoicing for professional services businesses. The Accelo REST API exposes resources such as companies, contacts, activities, tasks, jobs (projects), milestones, invoices, contracts, and webhooks using OAuth 2.0 authentication scoped to a deployment subdomain.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/accelo.png
layout: provider
modified: '2026-05-11'
name: Accelo
nav: Providers
network: true
overview: 'Accelo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Companies API, Contacts API, and 4 more. Tagged areas include Professional Services Automation, Project Management, CRM, Time Tracking, and Invoicing.


  Accelo''s developer surface includes authentication, documentation, signup flow, pricing, support, engineering blog, and 7 more developer resources.'
random_paper: 6
scopes:
- name: Accelo Scopes
  scope_count: 4
  slug: accelo-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 44.9
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 27.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/accelo/refs/heads/main/screenshots/accelo-2026-06-20T163557.png
security:
- kind: authentication
  name: Accelo Authentication
  slug: accelo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Accelo Domain Security
  slug: accelo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: accelo
tags:
- Professional Services Automation
- Project Management
- CRM
- Time Tracking
- Invoicing
- Service Operations
website: https://www.accelo.com
---
