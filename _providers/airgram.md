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
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airgram
- group: other
  title: ''
  type: Successor
  url: https://www.notta.ai/en/welcome-airgram
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/airgram
coverage:
  checked: '2026-09-19'
  detail: Airgram was an end-user AI meeting-notes app with no developer program that merged into Notta and was discontinued from 8 March 2024; airgram.io and www.airgram.io have no DNS record, airgram.com 301s into that dead host, and the only surviving first-party statement is Notta's welcome-airgram page.
  evidence:
  - status: 0
    url: https://airgram.io/
  - status: 0
    url: https://www.airgram.io/
  - status: 301
    url: https://airgram.com/
  - status: 200
    url: https://www.notta.ai/en/welcome-airgram
  - status: 404
    url: https://zapier.com/apps/airgram/integrations
  - status: 403
    url: https://equityzen.com/company/airgram
  reason: defunct
  state: none
created: '2026-09-19'
description: 'Airgram was a Singapore-headquartered AI meeting assistant founded in 2020 by Ryan Zhang. Its web app joined Zoom, Google Meet and Microsoft Teams calls to record and transcribe them in real time, then produced collaborative notes, agendas, action items, AI summaries and shareable clips, with exports to Notion, Slack and HubSpot and an automation connector listed on Zapier. It sold the product to end users on free and paid plans and never published a public developer program: no API reference, OpenAPI, SDK, webhook catalog or developer portal was ever offered, and the Zapier connector was the only integration surface. In early 2024 Airgram merged into Notta (notta.ai), the AI transcription company, and the Airgram service was discontinued from 8 March 2024; Notta hosts a "Airgram Has Joined Notta" welcome page and the LinkedIn company page is renamed "Airgram (merged into Notta)". No first-party host survives — airgram.io and www.airgram.io have no DNS record and airgram.com
  301s into the dead www.airgram.io — so no Website pointer is wired. This record is retained as an honest zero: an end-user software company, absorbed into an acquirer, with no API surface to profile.'
layout: provider
modified: '2026-09-19'
name: Airgram
nav: Providers
network: true
overview: Airgram is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Meetings, Transcription, Meeting Notes, and Productivity.
random_paper: 13
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 0
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
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
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
slug: airgram
tags:
- Company
- Meetings
- Transcription
- Meeting Notes
- Productivity
- Artificial Intelligence
- Defunct
---
