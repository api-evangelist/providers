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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://aispera.com/en
coverage:
  checked: 2026-09-21
  detail: The provider's website renders documentation via JavaScript and offers no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://aispera.com/en
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-21'
description: Aispera is a cybersecurity company leveraging artificial intelligence to predict and mitigate threats. It offers a proactive security framework that integrates Attack Surface Management and Threat Intelligence, providing comprehensive visibility into known and unknown attack vectors. The platform helps organizations make faster, more accurate risk decisions through advanced analytics and automated insights.
layout: provider
modified: '2026-09-21'
name: Aispera
nav: Providers
network: true
overview: Aispera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Artificial Intelligence, Threat Intelligence, and Attack Surface Management.
random_paper: 15
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  previous_composite: 4.6
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: aispera
tags:
- Company
- Cybersecurity
- Artificial Intelligence
- Threat Intelligence
- Attack Surface Management
website: https://aispera.com/en
---
