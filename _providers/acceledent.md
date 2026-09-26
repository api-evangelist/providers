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
  checked: '2026-09-06'
  detail: OrthoAccel Technologies built AcceleDent as a physical FDA-cleared Class II orthodontic device and never ran a developer program; the company is now defunct, orthoaccel.com no longer resolves at all, and acceledent.com was re-registered in August 2022 as a GoDaddy aftermarket "for sale" listing whose parking system returns the same 114-byte HTML stub with HTTP 200 for every path probed, including /openapi.json and every /.well-known/ path.
  evidence:
  - status: 200
    url: https://acceledent.com/
  - status: 403
    url: https://acceledent.com/lander
  - status: 200
    url: https://acceledent.com/openapi.json
  - status: 200
    url: https://acceledent.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/orthoaccel
  - status: 403
    url: https://forgeglobal.com/acceledent_stock/
  reason: defunct
  state: none
created: '2026-09-06'
description: 'AcceleDent was the flagship product of OrthoAccel Technologies, Inc., a privately held medical-device company founded in 2007 and headquartered in Bellaire, Texas, outside Houston. AcceleDent is an FDA-cleared Class II device built around the company''s patented SoftPulse Technology: a hands-free mouthpiece and activator that a patient bit down on for about twenty minutes a day, delivering gentle micropulses intended to speed bone remodeling during orthodontic treatment and reduce the discomfort of braces and clear aligners. The line ran through three generations — the original AcceleDent, AcceleDent Aura in 2013, and AcceleDent Optima, cleared by the FDA in 2017 — sold to orthodontists and dentists rather than direct to consumers, with an e-commerce ordering site at shop.acceledent.com for practices. The company raised roughly $63.1M across sixteen rounds, the last a Series C in January 2017, and a later debt-and-equity financing led by S3 Ventures. It was a physical medical-device
  business, not a software business: OrthoAccel never operated a developer program, never published an API, SDK, webhook surface or machine-readable specification of any kind, and shipped no client libraries to any package registry. OrthoAccel is now reported defunct — orthoaccel.com no longer resolves, and acceledent.com was re-registered on 2022-08-30 and today sits on Afternic name servers as a GoDaddy aftermarket "for sale" listing whose parking system answers HTTP 200 with an identical 114-byte HTML stub on every path, including every /.well-known/ and spec path. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-09-06'
name: AcceleDent
nav: Providers
network: true
overview: AcceleDent is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Medical Devices, Dental, and Orthodontics.
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: acceledent
tags:
- Company
- Defunct
- Medical Devices
- Dental
- Orthodontics
- Healthcare
- Hardware
- Consumer Health
---
