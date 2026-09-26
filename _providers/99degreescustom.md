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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-05'
  detail: 99Degrees is a Lawrence, Massachusetts contract apparel manufacturer that never published a developer program, and it no longer controls its own domain — 99degreescustom.com was re-registered by a broker on 2026-05-24 and now answers every ordinary path with the same "99degreescustom.com for sale" parking lander while 404ing every /.well-known/ path.
  evidence:
  - status: 200
    url: https://99degreescustom.com/
  - status: 404
    url: https://99degreescustom.com/openapi.json
  - status: 404
    url: https://99degreescustom.com/.well-known/agent-card.json
  - status: 200
    url: https://99degreescustom.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/99degreescustom
  - status: 200
    url: https://equityzen.com/company/99degreescustom/
  reason: defunct
  state: none
created: '2026-09-05'
description: '99Degrees (99Degrees Custom, Inc.) is a Lawrence, Massachusetts contract apparel manufacturer founded in 2013 by Brenna Nan Schneider, operating out of the historic Everett Mills. It produces performance activewear, workwear, uniforms and technology-integrated apparel for global and growth-stage brands, and runs an R&D operation focused on Design for Manufacturing, rapid prototyping and applied research — including integrating sensors, electronics, robotics and hardware into textiles for wearable medical and industrial safety products. During the COVID-19 pandemic it pivoted its Lawrence floor to medical gowns and PPE. The company raised roughly $2.35M across four rounds, won the MIT Inclusive Innovation Competition top prize and MassChallenge''s $100k Diamond Prize, and entered a manufacturing partnership with Reliable Source Industrial. 99Degrees is a physical-goods manufacturer, not a software company: no source, live or archived, shows it ever published a developer program,
  public API, SDK, webhook surface or machine-readable specification. Its canonical host 99degreescustom.com lapsed and was re-registered by a domain broker on 2026-05-24; it now serves a "for sale" parking lander and is deliberately not wired as a Website pointer. This profile is retained as a historical record — there is no API surface to catalog.'
layout: provider
modified: '2026-09-05'
name: 99degrees Custom
nav: Providers
network: true
overview: 99degrees Custom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Contract Manufacturing, Apparel, and Textiles.
random_paper: 20
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: 99degreescustom
tags:
- Company
- Manufacturing
- Contract Manufacturing
- Apparel
- Textiles
- Activewear
- Wearables
- Advanced Manufacturing
- Defunct
---
