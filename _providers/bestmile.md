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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bestmile-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bestmile.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bestmile
coverage:
  checked: '2026-08-17'
  detail: bestmile.com refuses HTTPS entirely and its HTTP/80 root serves a Gandi.net registrar parking page; api., docs., developer., platform. and app.bestmile.com are NXDOMAIN, and the surviving github.com/Bestmile org holds only forks of third-party OSS (secor, alpakka, chimney, squants) with no spec or SDK, because ZF Friedrichshafen absorbed the technology into SCALAR in November 2021.
  evidence:
  - status: 0
    url: https://bestmile.com/
  - status: 200
    url: http://bestmile.com/
  - status: 200
    url: http://bestmile.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/bestmile
  - status: 404
    url: https://pypi.org/pypi/bestmile/json
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Bestmile was a Swiss fleet-orchestration SaaS company, spun out of EPFL in Lausanne in 2014, whose cloud platform planned, dispatched and optimized mixed fleets of autonomous and human-driven vehicles for on-demand mobility and transit operators. The platform was described by the company as API-first, with documented Fleet, Booking and Transportation APIs for integrating operator booking apps, fleet-management systems and traveler-information systems. The company no longer operates: ZF Friedrichshafen acquired Bestmile''s technology in November 2021 and folded it into its own SCALAR fleet-orchestration platform, so any successor API belongs to ZF rather than to Bestmile. As of 2026-08-17 bestmile.com is a parked Gandi.net registrar domain that refuses HTTPS, and no developer portal, documentation, OpenAPI, package or /.well-known surface survives. Surfaced originally as a Partech portfolio company.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bestmile.png
layout: provider
modified: '2026-08-17'
name: Bestmile
nav: Providers
network: true
overview: Bestmile is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Applicative Saas, Mobility, Fleet Orchestration, and Autonomous Vehicles.
random_paper: 108
score:
  band: minimal
  composite: 5.3
  delta: 1.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 4.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Bestmile Domain Security
  slug: bestmile-domain-security
  summary_line: no transport/DNS hardening detected
slug: bestmile
tags:
- Company
- Applicative Saas
- Mobility
- Fleet Orchestration
- Autonomous Vehicles
- Transportation
- Mobility As A Service
website: https://bestmile.com/
---
