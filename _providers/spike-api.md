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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Spike Api Agentic Access
  operation_count: 39
  slug: spike-api-agentic-access
  summary_line: 39 operations · 17 acting
api_count: 1
apis:
- description: Outbound webhook event delivery. After data updates, Spike POSTs a JSON array of events - record_change, provider_integration_created, and provider_integration_deleted - to a webhook URL configured in
  name: Spike Webhooks API
  slug: spike-api-webhooks-api
- description: Authenticate end users and mint JWT access tokens.
  name: Spike Auth API
  slug: spike-api-auth-api
- description: Upload and query structured lab report biomarkers.
  name: Spike Lab Reports API
  slug: spike-api-lab-reports-api
- description: Analyze and manage nutrition records.
  name: Spike Nutrition AI API
  slug: spike-api-nutrition-ai-api
- description: Connect and disconnect a user's health data providers.
  name: Spike Provider Integrations API
  slug: spike-api-provider-integrations-api
- description: Query normalized provider health data records.
  name: Spike Provider Records API
  slug: spike-api-provider-records-api
- description: Ingest on-device health data pushed from the mobile SDKs.
  name: Spike SDK Push API
  slug: spike-api-sdk-push-api
- description: Query normalized sleep sessions and stages.
  name: Spike Sleep API
  slug: spike-api-sleep-api
- description: Query aggregated statistics for metrics over time.
  name: Spike Statistics API
  slug: spike-api-statistics-api
- description: Query high-resolution metric time series.
  name: Spike Time Series API
  slug: spike-api-time-series-api
- description: Current user, user properties, and application info.
  name: Spike Users API
  slug: spike-api-users-api
- description: Query normalized workouts and physical activities.
  name: Spike Workouts API
  slug: spike-api-workouts-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spike Application User Auth API
  slug: open-spike-api-auth-api
- collection_type: open
  name: Spike Application User Auth Lab Reports API
  slug: open-spike-api-lab-reports-api
- collection_type: open
  name: Spike Application User Auth Nutrition AI API
  slug: open-spike-api-nutrition-ai-api
- collection_type: open
  name: Spike Application User Auth Provider Integrations API
  slug: open-spike-api-provider-integrations-api
- collection_type: open
  name: Spike Application User Auth Provider Records API
  slug: open-spike-api-provider-records-api
- collection_type: open
  name: Spike Application User Auth SDK Push API
  slug: open-spike-api-sdk-push-api
- collection_type: open
  name: Spike Application User Auth Sleep API
  slug: open-spike-api-sleep-api
- collection_type: open
  name: Spike Application User Auth Statistics API
  slug: open-spike-api-statistics-api
- collection_type: open
  name: Spike Application User Auth Time Series API
  slug: open-spike-api-time-series-api
- collection_type: open
  name: Spike Application User Auth Users API
  slug: open-spike-api-users-api
- collection_type: open
  name: Spike Application User Auth Workouts API
  slug: open-spike-api-workouts-api
- collection_type: open
  name: Spike Application User API
  slug: open-spike-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spike-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spike-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spike-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Spike-API
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spike-api
- group: company
  title: ''
  type: Website
  url: https://www.spikeapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spikeapi.com
- group: commercial
  title: ''
  type: Plans
  url: plans/spike-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spike-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spike-api-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.spikeapi.com/blog
created: '2026-07-03'
description: Spike (Spike Technologies) provides a unified health and wearables data API that connects an application to 500+ wearables, IoT devices, CGMs, EMRs, labs, and nutrition sources through a single integration - aggregating Apple Health, Garmin, Fitbit, Oura, Whoop, Dexcom, Withings, Polar, Suunto, Strava, and more. Developers authenticate end users with HMAC signatures, connect providers via hosted OAuth-style integration flows, then query normalized health data - sleep, workouts, time series metrics (heart rate, HRV, glucose, weight, SpO2, steps), daily and interval statistics, nutrition, and lab reports - over a REST API at https://app-api.spikeapi.com/v3, with outbound webhooks pushing record-change events. Spike also ships mobile SDKs (iOS, Android, Flutter, React Native), a Nutrition AI scanner, and an MCP layer for AI-ready health data.
finops:
- name: Spike Api Finops
  service_category: Health Data and Wearables API
  slug: spike-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spike-api.png
layout: provider
modified: '2026-07-03'
name: Spike
nav: Providers
network: true
overview: 'Spike publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Lab Reports API, Nutrition AI API, and 8 more. Tagged areas include Health Data, Wearables, Fitness, Digital Health, and Data Aggregation.


  Spike''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Spike Api Plans Pricing
  plan_count: 4
  slug: spike-api-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Spike Api Rate Limits
  slug: spike-api-rate-limits
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.8
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Spike Api Authentication
  slug: spike-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spike Api Domain Security
  slug: spike-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spike-api
tags:
- Health Data
- Wearables
- Fitness
- Digital Health
- Data Aggregation
- HIPAA
website: https://www.spikeapi.com
---
