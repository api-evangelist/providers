---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Fountain Com Agentic Access
  operation_count: 44
  slug: fountain-com-agentic-access
  summary_line: 44 operations · 26 acting
api_count: 1
apis:
- baseURL: https://api.fountain.com/v2
  baseurl_source: declared
  description: Manage applicants moving through hiring funnels.
  name: Fountain Applicants API
  slug: fountain-com-applicants-api
- baseURL: https://api.fountain.com/v2
  baseurl_source: declared
  description: Manage secure applicant documents.
  name: Fountain Documents API
  slug: fountain-com-documents-api
- baseURL: https://api.fountain.com/v2
  baseurl_source: declared
  description: Assign and manage labels on applicants and stages.
  name: Fountain Labels API
  slug: fountain-com-labels-api
- baseURL: https://api.fountain.com/v2
  baseurl_source: declared
  description: Manage openings (funnels) - the hiring workflows.
  name: Fountain Openings API
  slug: fountain-com-openings-api
- baseURL: https://api.fountain.com/v2
  baseurl_source: declared
  description: Manage the job positions applicants are hired into.
  name: Fountain Positions API
  slug: fountain-com-positions-api
- baseURL: https://api.fountain.com/v2
  baseurl_source: declared
  description: Manage interview / calendar slots and bookings.
  name: Fountain Scheduling API
  slug: fountain-com-scheduling-api
- baseURL: https://api.fountain.com/v2
  baseurl_source: declared
  description: Retrieve stages and their available scheduling slots.
  name: Fountain Stages API
  slug: fountain-com-stages-api
- baseURL: https://api.fountain.com/v2
  baseurl_source: declared
  description: Manage webhook settings for hiring event notifications.
  name: Fountain Webhooks API
  slug: fountain-com-webhooks-api
- baseURL: https://api.fountain.com/v2
  baseurl_source: declared
  description: Manage post-hire workers.
  name: Fountain Workers API
  slug: fountain-com-workers-api
- description: REST API for the Fountain Hire product, covering applicants (create, retrieve, update, delete, list, latest applicant, duplicate detection, notes, labels, file uploads, transitions, bulk advance, bulk
  name: Fountain Hire API v2
  slug: hire-api
- description: Post-hire REST API covering worker profiles (activation and deactivation), employment records, document submissions, I-9 verification processing, attendance, shift creation and assignment, demands, al
  name: Fountain Worker API
  slug: worker-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fountain Developer API (Hire API v2) Applicants API
  slug: open-fountain-com-applicants-api
- collection_type: open
  name: Fountain Developer API (Hire API v2) Applicants Documents API
  slug: open-fountain-com-documents-api
- collection_type: open
  name: Fountain Developer API (Hire API v2) Applicants Labels API
  slug: open-fountain-com-labels-api
- collection_type: open
  name: Fountain Developer API (Hire API v2) Applicants Openings API
  slug: open-fountain-com-openings-api
- collection_type: open
  name: Fountain Developer API (Hire API v2) Applicants Positions API
  slug: open-fountain-com-positions-api
- collection_type: open
  name: Fountain Developer API (Hire API v2) Applicants Scheduling API
  slug: open-fountain-com-scheduling-api
- collection_type: open
  name: Fountain Developer API (Hire API v2) Applicants Stages API
  slug: open-fountain-com-stages-api
- collection_type: open
  name: Fountain Developer API (Hire API v2) Applicants Webhooks API
  slug: open-fountain-com-webhooks-api
- collection_type: open
  name: Fountain Developer API (Hire API v2) Applicants Workers API
  slug: open-fountain-com-workers-api
- collection_type: open
  name: Fountain Developer API (Hire API v2)
  slug: open-fountain-com
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fountain-com-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fountain-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fountain-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fountain-com-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fountaininc
- group: company
  title: ''
  type: Website
  url: https://www.fountain.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fountain.com/reference
- group: commercial
  title: ''
  type: Plans
  url: plans/fountain-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fountain-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fountain-com-finops.yml
created: '2026-07-01'
description: Fountain is a high-volume, frontline hourly hiring and workforce management platform used by enterprises to source, screen, schedule, and hire large numbers of hourly workers. The Fountain Developer API (Hire API v2) lets customers programmatically manage applicants, openings, positions, stages, labels, documents, scheduling slots, and webhooks across their hiring funnels.
finops:
- name: Fountain Com Finops
  service_category: Human Resources
  slug: fountain-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fountain-com.png
layout: provider
modified: '2026-07-01'
name: Fountain
nav: Providers
network: true
overview: 'Fountain publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Applicants API, Documents API, Labels API, and 6 more. Tagged areas include Hiring, Recruiting, Applicant Tracking, Frontline Hiring, and Hourly Workforce.


  Fountain''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Fountain Com Plans Pricing
  plan_count: 4
  slug: fountain-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Fountain Com Rate Limits
  slug: fountain-com-rate-limits
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.8
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 35.5
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fountain-com/refs/heads/main/screenshots/fountain-com-2026-07-25T215044.png
security:
- kind: authentication
  name: Fountain Com Authentication
  slug: fountain-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fountain Com Domain Security
  slug: fountain-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fountain Com Vulnerability Disclosure
  slug: fountain-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: fountain-com
tags:
- Hiring
- Recruiting
- Applicant Tracking
- Frontline Hiring
- Hourly Workforce
- HR Tech
- Onboarding
website: https://www.fountain.com
---
