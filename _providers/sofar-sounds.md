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
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sofar-sounds-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sofarsounds.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sofarsounds
created: '2026-07-17'
description: Sofar Sounds curates secret, intimate live-music gigs in living rooms, small venues, and unexpected spaces in hundreds of cities around the world. The company connects independent and emerging artists with attentive local audiences through a mobile-first ticketing and events platform, and works with hosts who lend their spaces for the shows. Sofar operates a consumer-facing website and apps rather than a public developer program; probing its surface confirmed no documented public API, developer portal, SDKs, or OpenAPI. It runs a real GitHub organization (github.com/sofarsounds) of internal engineering repositories, and its production backend is served from api.sofarsounds.com (Heroku), but neither exposes a published, documented API for third-party developers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sofar-sounds.png
layout: provider
modified: '2026-07-21'
name: Sofar Sounds
nav: Providers
network: true
overview: Sofar Sounds is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Live Events, Concerts, and Ticketing.
random_paper: 13
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sofar-sounds/refs/heads/main/screenshots/sofar-sounds-2026-09-02T160056.png
security:
- kind: domain-security
  name: Sofar Sounds Domain Security
  slug: sofar-sounds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sofar-sounds
tags:
- Company
- Music
- Live Events
- Concerts
- Ticketing
- Entertainment
- Event
website: https://www.sofarsounds.com
---
