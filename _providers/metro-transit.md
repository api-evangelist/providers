---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Metro Transit Agentic Access
  operation_count: 24
  slug: metro-transit-agentic-access
  summary_line: 24 operations · 6 acting
api_count: 4
apis:
- description: The Alerts API from Metro Transit — 3 operation(s) for alerts.
  name: Metro Transit Alerts API
  slug: metro-transit-alerts-api
- description: The NexTrip API from Metro Transit — 8 operation(s) for nextrip.
  name: Metro Transit NexTrip API
  slug: metro-transit-nextrip-api
- description: The Planner API from Metro Transit — 8 operation(s) for planner.
  name: Metro Transit Planner API
  slug: metro-transit-planner-api
- description: The Schedule API from Metro Transit — 5 operation(s) for schedule.
  name: Metro Transit Schedule API
  slug: metro-transit-schedule-api
artifact_total: 14
collections:
- collection_type: open
  name: Service Alerts API
  slug: open-metro-transit-alerts
- collection_type: open
  name: NexTrip API
  slug: open-metro-transit-nextrip
- collection_type: open
  name: Schedule API
  slug: open-metro-transit-schedule
- collection_type: open
  name: Trip Planner API
  slug: open-metro-transit-tripplanner
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metro-transit-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/metro-transit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metro-transit-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metrotransit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/metro-transit
- group: start
  title: ''
  type: Portal
  url: https://www.metrotransit.org/developer-resources
- group: docs
  title: ''
  type: Documentation
  url: https://svc.metrotransit.org/swagger/index.html
- group: company
  title: ''
  type: Website
  url: https://www.metrotransit.org/
created: '2025-05-02'
description: Metro Transit provides real-time departure information, service alerts, trip planning, and schedule data APIs for the Minneapolis-Saint Paul metropolitan transit system. The APIs support creating transit departure displays and accessing real-time bus and train arrival data for the Twin Cities.
finops:
- name: Metro Transit Finops
  service_category: Public Transit Open Data
  slug: metro-transit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metro-transit.png
layout: provider
modified: '2026-05-19'
name: Metro Transit
nav: Providers
network: true
overview: 'Metro Transit publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, NexTrip API, Planner API, and 1 more. Tagged areas include Minneapolis, Minnesota, Public Transportation, Real-Time, and Transit.


  Metro Transit''s developer surface includes developer portal, documentation, and 6 more developer resources.'
plans:
- name: Metro Transit Plans Pricing
  plan_count: 1
  slug: metro-transit-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 3
  name: Metro Transit Rate Limits
  slug: metro-transit-rate-limits
score:
  band: thin
  composite: 29.1
  delta: -2.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 30.5
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 32.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metro-transit/refs/heads/main/screenshots/metro-transit-2026-06-20T185302.png
security:
- kind: domain-security
  name: Metro Transit Domain Security
  slug: metro-transit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Metro Transit Vulnerability Disclosure
  slug: metro-transit-vulnerability-disclosure
  summary_line: disclosure policy published
slug: metro-transit
tags:
- Minneapolis
- Minnesota
- Public Transportation
- Real-Time
- Transit
website: https://www.metrotransit.org/
---
