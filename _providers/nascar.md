---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Nascar Agentic Access
  operation_count: 41
  slug: nascar-agentic-access
  summary_line: 41 operations · 1 acting · 1 human-in-the-loop
api_count: 12
apis:
- description: The Companies API from NASCAR — 3 operation(s) for companies.
  name: NASCAR Companies API
  slug: nascar-companies-api
- description: The Drivers API from NASCAR — 2 operation(s) for drivers.
  name: NASCAR Drivers API
  slug: nascar-drivers-api
- description: The EntryList API from NASCAR — 1 operation(s) for entrylist.
  name: NASCAR EntryList API
  slug: nascar-entrylist-api
- description: The Inspection API from NASCAR — 5 operation(s) for inspection.
  name: NASCAR Inspection API
  slug: nascar-inspection-api
- description: The Live API from NASCAR — 7 operation(s) for live.
  name: NASCAR Live API
  slug: nascar-live-api
- description: The Points API from NASCAR — 3 operation(s) for points.
  name: NASCAR Points API
  slug: nascar-points-api
- description: The Races API from NASCAR — 5 operation(s) for races.
  name: NASCAR Races API
  slug: nascar-races-api
- description: The Series API from NASCAR — 2 operation(s) for series.
  name: NASCAR Series API
  slug: nascar-series-api
- description: The Stats API from NASCAR — 4 operation(s) for stats.
  name: NASCAR Stats API
  slug: nascar-stats-api
- description: The Tracks API from NASCAR — 3 operation(s) for tracks.
  name: NASCAR Tracks API
  slug: nascar-tracks-api
- description: The TrackTemp API from NASCAR — 3 operation(s) for tracktemp.
  name: NASCAR TrackTemp API
  slug: nascar-tracktemp-api
- description: The Weekend API from NASCAR — 3 operation(s) for weekend.
  name: NASCAR Weekend API
  slug: nascar-weekend-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NASCAR Feed Companies API
  slug: open-nascar-companies-api
- collection_type: open
  name: NASCAR Feed Companies Drivers API
  slug: open-nascar-drivers-api
- collection_type: open
  name: NASCAR Feed Companies EntryList API
  slug: open-nascar-entrylist-api
- collection_type: open
  name: NASCAR Feed Companies Inspection API
  slug: open-nascar-inspection-api
- collection_type: open
  name: NASCAR Feed Companies Live API
  slug: open-nascar-live-api
- collection_type: open
  name: NASCAR Feed Companies Points API
  slug: open-nascar-points-api
- collection_type: open
  name: NASCAR Feed Companies Races API
  slug: open-nascar-races-api
- collection_type: open
  name: NASCAR Feed Companies Series API
  slug: open-nascar-series-api
- collection_type: open
  name: NASCAR Feed Companies Stats API
  slug: open-nascar-stats-api
- collection_type: open
  name: NASCAR Feed Companies Tracks API
  slug: open-nascar-tracks-api
- collection_type: open
  name: NASCAR Feed Companies TrackTemp API
  slug: open-nascar-tracktemp-api
- collection_type: open
  name: NASCAR Feed Companies Weekend API
  slug: open-nascar-weekend-api
- collection_type: open
  name: NASCAR Feed API
  slug: open-nascar
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nascar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nascar-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nascar
- group: company
  title: ''
  type: Website
  url: https://www.nascar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://feed.nascar.com/swagger/ui/index
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nascar.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nascar.com/privacy-policy/
created: '2025-02-06'
description: NASCAR, the National Association for Stock Car Auto Racing, is a professional auto racing organization that sanctions and governs multiple racing series, including the popular NASCAR Cup Series. NASCAR exposes a feed API documented via Swagger that delivers race results, standings, schedules, driver and team information, and other motorsport data for partners, broadcasters, and fans.
finops:
- name: Nascar Finops
  service_category: API
  slug: nascar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nascar.png
layout: provider
modified: '2026-05-19'
name: NASCAR
nav: Providers
network: true
overview: 'NASCAR publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Drivers API, EntryList API, and 9 more. Tagged areas include Auto Racing, Sports, Stock Cars, Motorsports, and Race Results.


  NASCAR''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Nascar Plans Pricing
  plan_count: 3
  slug: nascar-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Nascar Rate Limits
  slug: nascar-rate-limits
score:
  band: thin
  composite: 29.1
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 50.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 29.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nascar/refs/heads/main/screenshots/nascar-2026-06-20T185957.png
security:
- kind: domain-security
  name: Nascar Domain Security
  slug: nascar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nascar
tags:
- Auto Racing
- Sports
- Stock Cars
- Motorsports
- Race Results
- Schedules
website: https://www.nascar.com/
---
