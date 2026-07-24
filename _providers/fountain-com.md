---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Fountain Com Agentic Access
  operation_count: 44
  slug: fountain-com-agentic-access
  summary_line: 44 operations · 26 acting
api_count: 9
apis:
- description: Manage applicants moving through hiring funnels.
  name: Fountain Applicants API
  slug: fountain-com-applicants-api
- description: Manage secure applicant documents.
  name: Fountain Documents API
  slug: fountain-com-documents-api
- description: Assign and manage labels on applicants and stages.
  name: Fountain Labels API
  slug: fountain-com-labels-api
- description: Manage openings (funnels) - the hiring workflows.
  name: Fountain Openings API
  slug: fountain-com-openings-api
- description: Manage the job positions applicants are hired into.
  name: Fountain Positions API
  slug: fountain-com-positions-api
- description: Manage interview / calendar slots and bookings.
  name: Fountain Scheduling API
  slug: fountain-com-scheduling-api
- description: Retrieve stages and their available scheduling slots.
  name: Fountain Stages API
  slug: fountain-com-stages-api
- description: Manage webhook settings for hiring event notifications.
  name: Fountain Webhooks API
  slug: fountain-com-webhooks-api
- description: Manage post-hire workers.
  name: Fountain Workers API
  slug: fountain-com-workers-api
artifact_total: 17
collections:
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
random_paper: 8
rate_limits:
- limit_count: 3
  name: Fountain Com Rate Limits
  slug: fountain-com-rate-limits
score:
  band: thin
  composite: 36.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.1
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
