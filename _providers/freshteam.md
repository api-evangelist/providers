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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Freshteam Agentic Access
  operation_count: 25
  slug: freshteam-agentic-access
  summary_line: 25 operations · 8 acting
api_count: 1
apis:
- baseURL: https://{domain}.freshteam.com/api
  baseurl_source: declared
  description: Applicants (candidates) and candidate sources (ATS).
  name: Freshteam Applicants API
  slug: freshteam-applicants-api
- baseURL: https://{domain}.freshteam.com/api
  baseurl_source: declared
  description: Employee records, custom fields, and organization structure (HRIS).
  name: Freshteam Employees API
  slug: freshteam-employees-api
- baseURL: https://{domain}.freshteam.com/api
  baseurl_source: declared
  description: Job postings and their custom fields (recruiting).
  name: Freshteam Job Postings API
  slug: freshteam-job-postings-api
- baseURL: https://{domain}.freshteam.com/api
  baseurl_source: declared
  description: New-hire records for pre-boarding and onboarding.
  name: Freshteam Onboarding API
  slug: freshteam-onboarding-api
- baseURL: https://{domain}.freshteam.com/api
  baseurl_source: declared
  description: Time-off (leave) requests and types.
  name: Freshteam Time-off API
  slug: freshteam-time-off-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Freshteam Applicants API
  slug: open-freshteam-applicants-api
- collection_type: open
  name: Freshteam Applicants Employees API
  slug: open-freshteam-employees-api
- collection_type: open
  name: Freshteam Applicants Job Postings API
  slug: open-freshteam-job-postings-api
- collection_type: open
  name: Freshteam Applicants Onboarding API
  slug: open-freshteam-onboarding-api
- collection_type: open
  name: Freshteam Applicants Time-off API
  slug: open-freshteam-time-off-api
- collection_type: open
  name: Freshteam API
  slug: open-freshteam
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freshteam-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freshteam-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freshworks-inc
- group: company
  title: ''
  type: Website
  url: https://www.freshworks.com/hrms/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.freshteam.com/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/freshteam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/freshteam-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/freshteam-finops.yml
created: '2026-07-11'
description: Freshteam is the HR and applicant tracking (ATS) product from Freshworks, covering recruiting, applicant tracking, employee information management (HRIS), onboarding, and time-off. It exposes a documented REST API on a per-domain base (https://{domain}.freshteam.com/api) with token auth over Employees, Job Postings, Applicants, Interviews, Time-off, and organization structure (Departments, Branches, Teams). IMPORTANT STATUS - Freshworks has announced the end-of-life of Freshteam - new subscriptions and renewals are halted starting March 7, 2026, and existing customers retain access only through the end of their term (reported through approximately April 2027). This entry documents the API honestly as an existing but sunsetting product; the API remains usable for current customers during the transition but is not available to new signups.
finops:
- name: Freshteam Finops
  service_category: Human Resources and Recruiting Software
  slug: freshteam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freshteam.png
layout: provider
modified: '2026-07-11'
name: Freshteam
nav: Providers
network: true
overview: 'Freshteam publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Applicants API, Employees API, Job Postings API, and 2 more. Tagged areas include Human Resources, HRIS, Applicant Tracking, ATS, and Recruiting.


  Freshteam''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Freshteam Plans Pricing
  plan_count: 4
  slug: freshteam-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Freshteam Rate Limits
  slug: freshteam-rate-limits
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freshteam/refs/heads/main/screenshots/freshteam-2026-07-25T215212.png
security:
- kind: authentication
  name: Freshteam Authentication
  slug: freshteam-authentication
  summary_line: http · 1 scheme
slug: freshteam
tags:
- Human Resources
- HRIS
- Applicant Tracking
- ATS
- Recruiting
- Employee Management
- Onboarding
- Time Off
- HR Software
- End of Life
website: https://www.freshworks.com/hrms/
---
