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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Setlistfm Agentic Access
  operation_count: 15
  slug: setlistfm-agentic-access
  summary_line: 15 operations
api_count: 7
apis:
- description: Artists keyed by MusicBrainz MBID and their setlists.
  name: setlist.fm Artists API
  slug: setlistfm-artists-api
- description: Cities resolved by GeoNames geoId.
  name: setlist.fm Cities API
  slug: setlistfm-cities-api
- description: The reference list of countries.
  name: setlist.fm Countries API
  slug: setlistfm-countries-api
- description: Full-text search across artists, venues, cities, and setlists.
  name: setlist.fm Search API
  slug: setlistfm-search-api
- description: Individual setlists and their historical versions.
  name: setlist.fm Setlists API
  slug: setlistfm-setlists-api
- description: Community members and their attended/edited setlists.
  name: setlist.fm User API
  slug: setlistfm-user-api
- description: Concert venues and the setlists performed at them.
  name: setlist.fm Venues API
  slug: setlistfm-venues-api
artifact_total: 14
collections:
- collection_type: open
  name: setlist.fm REST API
  slug: open-setlistfm
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/setlistfm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/setlistfm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/setlistfm-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/setlist-fm/
- group: company
  title: ''
  type: Website
  url: https://www.setlist.fm/
- group: docs
  title: ''
  type: Documentation
  url: https://api.setlist.fm/docs/1.0/index.html
- group: commercial
  title: ''
  type: Plans
  url: plans/setlistfm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/setlistfm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/setlistfm-finops.yml
created: '2026-07-03'
description: setlist.fm is the world's largest crowd-sourced concert setlist database and community, letting fans document, share, and explore which songs artists play at live shows. The setlist.fm REST API gives read-only access to that data - artists (keyed by MusicBrainz MBID), setlists and their revision history, venues, cities, and countries, plus full-text search across each - so developers can build music apps, tour trackers, and research tools. setlist.fm is owned by Live Nation Entertainment through its Ticketmaster subsidiary. The API is free for non-commercial use with an API key; commercial use requires contacting setlist.fm.
finops:
- name: Setlistfm Finops
  service_category: Music and Entertainment Data
  slug: setlistfm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/setlistfm.png
layout: provider
modified: '2026-07-03'
name: setlist.fm
nav: Providers
network: true
overview: 'setlist.fm publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Artists API, Cities API, Countries API, and 4 more. Tagged areas include Music, Concerts, Setlists, Live Music, and Database.


  setlist.fm''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Setlistfm Plans Pricing
  plan_count: 3
  slug: setlistfm-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 3
  name: Setlistfm Rate Limits
  slug: setlistfm-rate-limits
score:
  band: thin
  composite: 38.3
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.7
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Setlistfm Authentication
  slug: setlistfm-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Setlistfm Domain Security
  slug: setlistfm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: setlistfm
tags:
- Music
- Concerts
- Setlists
- Live Music
- Database
- Crowd-Sourced
- Entertainment
website: https://www.setlist.fm/
---
