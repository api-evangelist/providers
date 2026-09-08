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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-06'
  detail: The EquityZen listing (the only public record of AboutMovie found) names no company website, no GitHub organization exists under the name, and every same-name domain resolves to an unrelated third party — so there is no first-party host to run contract discovery against.
  evidence:
  - status: 200
    url: https://equityzen.com/company/aboutmovie
  - status: 200
    url: https://aboutmovie.com/
  - status: 200
    url: https://aboutmovie.com/openapi.json
  - status: 200
    url: https://aboutmovie.com/.well-known/agent-card.json
  - status: 200
    url: https://aboutmovie.org/openapi.json
  - status: 403
    url: https://aboutmovie.net/
  - status: 404
    url: https://api.github.com/orgs/aboutmovie
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: 'AboutMovie (listed as ticker ABMO on the EquityZen secondary marketplace) is described by that listing as an interactive platform providing comprehensive information, reviews, and recommendations for movies and TV shows, classified there under Software, Artificial Intelligence, and Data and Analytics. That listing is the only public record of the company this profile could locate; it names no company website, and a full contract-discovery pass found no first-party host for the brand. All three same-name domains probed belong to unrelated parties: aboutmovie.com is an Afternic for-sale parking lander that answers HTTP 200 with the same stub on every path, aboutmovie.net is behind a Cloudflare challenge, and aboutmovie.org is an untitled Hostinger Horizons single-page site carrying no AboutMovie branding. No developer program, API documentation, SDK, GitHub organization, or machine-readable contract could be found.'
layout: provider
modified: '2026-09-06'
name: Aboutmovie
nav: Providers
network: true
overview: Aboutmovie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Entertainment, Movies, and Television.
random_paper: 12
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 0
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  previous_composite: 4.6
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: aboutmovie
tags:
- Company
- Media
- Entertainment
- Movies
- Television
- Recommendations
- Consumer
- Artificial Intelligence
- Data and Analytics
---
