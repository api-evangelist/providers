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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Airbrake Agentic Access
  operation_count: 27
  slug: airbrake-agentic-access
  summary_line: 27 operations · 13 acting
api_count: 1
apis:
- description: REST API for submitting error notices, managing projects, tracking deployments, querying notices and groups, and uploading source maps. Authentication uses project keys, user keys, or time-limited use
  name: Airbrake API
  slug: api
- description: The Activities API from Airbrake — 2 operation(s) for activities.
  name: Airbrake Activities API
  slug: airbrake-activities-api
- description: The Deploys API from Airbrake — 2 operation(s) for deploys.
  name: Airbrake Deploys API
  slug: airbrake-deploys-api
- description: The Groups API from Airbrake — 6 operation(s) for groups.
  name: Airbrake Groups API
  slug: airbrake-groups-api
- description: The iOS Crash Reports API from Airbrake — 1 operation(s) for ios crash reports.
  name: Airbrake iOS Crash Reports API
  slug: airbrake-ios-crash-reports-api
- description: The Notices API from Airbrake — 3 operation(s) for notices.
  name: Airbrake Notices API
  slug: airbrake-notices-api
- description: The Performance API from Airbrake — 4 operation(s) for performance.
  name: Airbrake Performance API
  slug: airbrake-performance-api
- description: The Projects API from Airbrake — 2 operation(s) for projects.
  name: Airbrake Projects API
  slug: airbrake-projects-api
- description: The Sessions API from Airbrake — 1 operation(s) for sessions.
  name: Airbrake Sessions API
  slug: airbrake-sessions-api
- description: The Source Maps API from Airbrake — 2 operation(s) for source maps.
  name: Airbrake Source Maps API
  slug: airbrake-source-maps-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Airbrake REST Activities API
  slug: open-airbrake-activities-api
- collection_type: open
  name: Airbrake REST Activities Deploys API
  slug: open-airbrake-deploys-api
- collection_type: open
  name: Airbrake REST Activities Groups API
  slug: open-airbrake-groups-api
- collection_type: open
  name: Airbrake REST Activities iOS Crash Reports API
  slug: open-airbrake-ios-crash-reports-api
- collection_type: open
  name: Airbrake REST Activities Notices API
  slug: open-airbrake-notices-api
- collection_type: open
  name: Airbrake REST Activities Performance API
  slug: open-airbrake-performance-api
- collection_type: open
  name: Airbrake REST Activities Projects API
  slug: open-airbrake-projects-api
- collection_type: open
  name: Airbrake REST Activities Sessions API
  slug: open-airbrake-sessions-api
- collection_type: open
  name: Airbrake REST Activities Source Maps API
  slug: open-airbrake-source-maps-api
- collection_type: open
  name: Airbrake REST API
  slug: open-airbrake
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airbrake-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airbrake-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airbrake-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/airbrake
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airbrake-io
- group: company
  title: ''
  type: Website
  url: https://www.airbrake.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.airbrake.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.airbrake.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://airbrake.io/account/new
created: '2026-05-11'
description: Airbrake is an error monitoring and application performance management platform that captures exceptions, deployments, and performance traces across web, mobile, and backend applications using language-specific notifier libraries. The platform aggregates errors with smart grouping, routing alerts to engineering teams, and provides deploy tracking and source map management for stack trace deminification. The Airbrake REST API exposes error notices, projects, deployments, and groups using query parameter API keys.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airbrake.png
layout: provider
modified: '2026-05-11'
name: Airbrake
nav: Providers
network: true
overview: 'Airbrake publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Deploys API, Groups API, and 6 more. Tagged areas include Error Monitoring, Application Performance Monitoring, Observability, DevOps, and Logging.


  Airbrake''s developer surface includes authentication, documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 28.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airbrake/refs/heads/main/screenshots/airbrake-2026-06-20T171417.png
security:
- kind: authentication
  name: Airbrake Authentication
  slug: airbrake-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Airbrake Domain Security
  slug: airbrake-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airbrake
tags:
- Error Monitoring
- Application Performance Monitoring
- Observability
- DevOps
- Logging
- Exception Tracking
website: https://www.airbrake.io
---
