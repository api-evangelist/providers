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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Fleetmatics Reveal API - delivered through the Fleetmatics Integration Manager (FIM) / Reveal Integration Services - exposes REST endpoints for vehicles, drivers, real-time and historical GPS posi
  name: Fleetmatics Reveal API
  slug: fleetmatics-reveal-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fleetmatics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.verizonconnect.com/solutions/gps-fleet-tracking-software/#fleetmatics
- group: start
  title: ''
  type: DeveloperPortal
  url: https://reveal-help.verizonconnect.com/hc/en-us/articles/10933751995539-Developer-portal-overview
- group: docs
  title: ''
  type: Documentation
  url: https://reveal-help.verizonconnect.com/hc/en-us/sections/5491620930451-API-integrations
- group: docs
  title: ''
  type: APIReference
  url: https://fim.us.fleetmatics.com/apis
- group: operate
  title: ''
  type: Support
  url: https://support.verizonconnect.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fleetmatics-llms.txt
created: '2026-07-17'
description: Fleetmatics was a fleet management, telematics, and GPS vehicle tracking SaaS company whose Reveal platform tracked commercial vehicles, drivers, and mobile assets for small and mid-sized fleets. Founded in Dublin and later headquartered in Massachusetts, Fleetmatics IPO'd on the NYSE in 2012 and was acquired by Verizon in 2016 for about USD 2.4 billion, becoming the core of Verizon Connect. Its Reveal platform exposes a documented REST API and webhook suite - the Fleetmatics Integration Manager (FIM) / Reveal Integration Services APIs - covering vehicles, drivers, GPS positions and history, trips and segments, driver status and safety, hours-of-service logbooks, geofences (places), groups, and non-powered asset tracking. The API gateway still runs on Fleetmatics-branded hosts (fim.api.us.fleetmatics.com); access is gated to Reveal customers and approved integration partners who request Integration Manager and Reveal REST credentials before calling the documented endpoints.
  The Fleetmatics brand now redirects to Verizon Connect.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fleetmatics.png
layout: provider
modified: '2026-07-19'
name: Fleetmatics
nav: Providers
network: true
overview: 'Fleetmatics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fleet Management, Telematics, GPS Tracking, Vehicle Tracking, and Fleet Tracking.


  Fleetmatics'' developer surface includes documentation, API reference, support, and 4 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 13.3
  delta: -1.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fleetmatics/refs/heads/main/screenshots/fleetmatics-2026-07-25T214737.png
security:
- kind: domain-security
  name: Fleetmatics Domain Security
  slug: fleetmatics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fleetmatics
tags:
- Fleet Management
- Telematics
- GPS Tracking
- Vehicle Tracking
- Fleet Tracking
- Logistics
- Verizon
- Fleetmatics
website: https://www.verizonconnect.com/solutions/gps-fleet-tracking-software/#fleetmatics
---
