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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Neighbortunes Agentic Access
  operation_count: 17
  slug: neighbortunes-agentic-access
  summary_line: 17 operations
api_count: 16
apis:
- description: The Albums.{format} API from Neighbortunes — 1 operation(s) for albums.{format}.
  name: Neighbortunes Albums.{format} API
  slug: neighbortunes-albums-format-api
- description: The Appearances.{format} API from Neighbortunes — 1 operation(s) for appearances.{format}.
  name: Neighbortunes Appearances.{format} API
  slug: neighbortunes-appearances-format-api
- description: The Jamcharts.{format} API from Neighbortunes — 1 operation(s) for jamcharts.{format}.
  name: Neighbortunes Jamcharts.{format} API
  slug: neighbortunes-jamcharts-format-api
- description: The Latest.{format} API from Neighbortunes — 1 operation(s) for latest.{format}.
  name: Neighbortunes Latest.{format} API
  slug: neighbortunes-latest-format-api
- description: The Links.{format} API from Neighbortunes — 1 operation(s) for links.{format}.
  name: Neighbortunes Links.{format} API
  slug: neighbortunes-links-format-api
- description: The List API from Neighbortunes — 1 operation(s) for list.
  name: Neighbortunes List API
  slug: neighbortunes-list-api
- description: The Metadata.{format} API from Neighbortunes — 1 operation(s) for metadata.{format}.
  name: Neighbortunes Metadata.{format} API
  slug: neighbortunes-metadata-format-api
- description: The Setlists API from Neighbortunes — 2 operation(s) for setlists.
  name: Neighbortunes Setlists API
  slug: neighbortunes-setlists-api
- description: The Setlists.{format} API from Neighbortunes — 1 operation(s) for setlists.{format}.
  name: Neighbortunes Setlists.{format} API
  slug: neighbortunes-setlists-format-api
- description: The Shows API from Neighbortunes — 1 operation(s) for shows.
  name: Neighbortunes Shows API
  slug: neighbortunes-shows-api
- description: The Shows.{format} API from Neighbortunes — 1 operation(s) for shows.{format}.
  name: Neighbortunes Shows.{format} API
  slug: neighbortunes-shows-format-api
- description: The Songs API from Neighbortunes — 1 operation(s) for songs.
  name: Neighbortunes Songs API
  slug: neighbortunes-songs-api
- description: The Songs.{format} API from Neighbortunes — 1 operation(s) for songs.{format}.
  name: Neighbortunes Songs.{format} API
  slug: neighbortunes-songs-format-api
- description: The Uploads.{format} API from Neighbortunes — 1 operation(s) for uploads.{format}.
  name: Neighbortunes Uploads.{format} API
  slug: neighbortunes-uploads-format-api
- description: The Venues API from Neighbortunes — 1 operation(s) for venues.
  name: Neighbortunes Venues API
  slug: neighbortunes-venues-api
- description: The Venues.{format} API from Neighbortunes — 1 operation(s) for venues.{format}.
  name: Neighbortunes Venues.{format} API
  slug: neighbortunes-venues-format-api
artifact_total: 22
collections:
- collection_type: open
  name: Neighbortunes API
  slug: open-neighbortunes
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/neighbortunes-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neighbortunes-domain-security.yml
created: '2025-02-09'
description: Welcome to NEIGHBORTUNES! The officially unofficial home of all things Neighbor. This site is a work in progress but we hope you enjoy being able to look up setlists, songs, teases, venues, band stats, and much more!
finops:
- name: Neighbortunes Finops
  service_category: API
  slug: neighbortunes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neighbortunes.png
layout: provider
modified: '2026-05-19'
name: Neighbortunes
nav: Providers
network: true
overview: Neighbortunes publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Albums.{format} API, Appearances.{format} API, Jamcharts.{format} API, and 13 more. Tagged areas include Music, Setlists, and Fan Site.
plans:
- name: Neighbortunes Plans Pricing
  plan_count: 3
  slug: neighbortunes-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 5
  name: Neighbortunes Rate Limits
  slug: neighbortunes-rate-limits
score:
  band: emerging
  composite: 22.8
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 48.5
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 22.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neighbortunes/refs/heads/main/screenshots/neighbortunes-2026-06-20T190127.png
security:
- kind: domain-security
  name: Neighbortunes Domain Security
  slug: neighbortunes-domain-security
  summary_line: TLSv1.3
slug: neighbortunes
tags:
- Music
- Setlists
- Fan Site
---
