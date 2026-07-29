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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: GraphQL `vessels` query returning up to 1,000 vessels per page - static data (name, MMSI, IMO, callsign, flag, shipType, dimensions), last position update (lat/long, course, heading, speed, collection
  name: Spire Maritime Vessels API
  slug: spire-maritime-vessels-api
- description: GraphQL query surface for decoded AIS messages (position and static/voyage reports) filtered by MMSI and time window, returned in large paginated batches. Used to pull recent and historical AIS messag
  name: Spire Maritime Messages API
  slug: spire-maritime-messages-api
- description: 'GraphQL port-event queries - `portEventsByVessel`, `portEventsByLocation`, and `portEventsByShipType` - surfacing vessel arrivals and departures (ATA/ATD), port calls, and berth/anchorage events with '
  name: Spire Maritime Port Events API
  slug: spire-maritime-port-events-api
- description: Predicted vessel routing and ETA - a `predictedVesselRoute` query taking an origin, destination, and vessel and returning the predicted sea route, distance, and estimated time of arrival / voyage dura
  name: Spire Maritime Predicted ETA / Routing API
  slug: spire-maritime-predicted-eta-api
- description: 'Always-on real-time AIS feed delivered over a RAW TCP SOCKET (not HTTP, not WebSocket). Client opens a TCP connection to streamingv2.ais.spire.com port 56784, authenticates with a token, and receives '
  name: Spire Maritime AIS TCP Stream
  slug: spire-maritime-ais-tcp-stream
artifact_total: 11
collections:
- collection_type: open
  name: Spire Maritime 2.0 (GraphQL)
  slug: open-spire-maritime
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spire-maritime-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spire-maritime-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spireglobal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spire-global
- group: company
  title: ''
  type: Website
  url: https://spire.com/maritime/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.spire.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/spire-maritime-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spire-maritime-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spire-maritime-finops.yml
created: '2026-07-12'
description: Spire Maritime (Spire Global) delivers satellite and terrestrial AIS vessel data - global ship positions, static vessel characteristics, voyage and destination data, port events, and predicted ETAs. The flagship Maritime 2.0 service is GraphQL-first at a single endpoint (https://api.spire.com/graphql, Bearer token auth), with a separate raw-TCP AIS stream for real-time message delivery in NMEA 0183 format. Access is enterprise / contact-sales. NOTE - following Spire Maritime's acquisition by Kpler, these APIs are being migrated/discontinued; new integrations are directed to developers.kpler.com.
finops:
- name: Spire Maritime Finops
  service_category: Data and Analytics
  slug: spire-maritime-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spire-maritime.png
layout: provider
modified: '2026-07-12'
name: Spire Maritime
nav: Providers
network: true
overview: 'Spire Maritime publishes 1 API on the [APIs.io](https://apis.io/) network: Vessels API. Tagged areas include Vessel Tracking, AIS, Maritime, Satellite AIS, and Ship Tracking.


  Spire Maritime''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Spire Maritime Plans Pricing
  plan_count: 1
  slug: spire-maritime-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Spire Maritime Rate Limits
  slug: spire-maritime-rate-limits
score:
  band: thin
  composite: 32.7
  delta: 8.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 43.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 24.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Spire Maritime Authentication
  slug: spire-maritime-authentication
  summary_line: http/token · 2 schemes
- kind: domain-security
  name: Spire Maritime Domain Security
  slug: spire-maritime-domain-security
  summary_line: TLSv1.3 · DMARC
slug: spire-maritime
tags:
- Vessel Tracking
- AIS
- Maritime
- Satellite AIS
- Ship Tracking
- Real-Time Data
- Maritime Data
- Predicted ETA
- Port Events
- Location
- GraphQL
website: https://spire.com/maritime/
---
