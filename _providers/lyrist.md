---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 0
common:
- group: other
  href: https://artifacts.apis.io/lyrist/hosts/lyrist-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lyrist-hosts.yml
- group: other
  href: https://artifacts.apis.io/lyrist/vendors/lyrist-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lyrist-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/asrvd/lyrist
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/asrvd/lyrist#readme
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/asrvd/lyrist/blob/main/README.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/asrvd/lyrist#overview
created: '2026-10-28'
description: Lyrist provides a simple, RESTful API that returns song lyrics based on a song title and artist name. Built with Next.js and Tailwind CSS, the service is hosted on Vercel and uses the LyricsDumper package to fetch lyrics. It includes rate limiting of 50 requests per hour per IP to prevent abuse. The API is intended as a learning project and a quick way for developers to integrate lyric lookup into applications.
layout: provider
modified: '2026-10-28'
name: Lyrist
nav: Providers
network: true
overview: 'Lyrist is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Lyrics, API, Next.js, and Vercel.


  Lyrist''s developer surface includes documentation, API reference, getting-started guide, and 3 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: lyrist
tags:
- Music
- Lyrics
- API
- Next.js
- Vercel
---
