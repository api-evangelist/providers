---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST-like API for managing contacts, jobs, tasks, files, and workflow automation in JobNimbus. Supports GET, PUT, and POST methods with JSON payloads. Authentication uses an API key generated from the
  name: JobNimbus Open API
  slug: open-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jobnimbus-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JobNimbus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jobnimbus
- group: company
  title: ''
  type: Website
  url: https://www.jobnimbus.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.jobnimbus.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jobnimbus.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.jobnimbus.com/signup
- group: operate
  title: ''
  type: Support
  url: https://support.jobnimbus.com
- group: company
  title: ''
  type: Blog
  url: https://www.jobnimbus.com/blog
created: '2026-05-11'
description: JobNimbus is a CRM and project management platform built for contractors, particularly in roofing, restoration, and home services industries. The platform enables lead tracking, job scheduling, estimating, invoicing, document management, and workflow automation. JobNimbus exposes a REST-like Open API supporting GET, PUT, and POST requests with JSON payloads, authenticated via API keys generated from the user dashboard.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jobnimbus.png
layout: provider
modified: '2026-05-11'
name: JobNimbus
nav: Providers
network: true
overview: 'JobNimbus publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CRM, Project Management, Contractors, Roofing, and Construction.


  JobNimbus'' developer surface includes documentation, pricing, signup flow, support, engineering blog, and 4 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 17.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jobnimbus/refs/heads/main/screenshots/jobnimbus-2026-06-20T183745.png
security:
- kind: domain-security
  name: Jobnimbus Domain Security
  slug: jobnimbus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jobnimbus
tags:
- CRM
- Project Management
- Contractors
- Roofing
- Construction
- Field Service
website: https://www.jobnimbus.com
---
