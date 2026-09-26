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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/1smHQ
coverage:
  checked: '2026-09-05'
  detail: 1sm's product never left the beta waitlist stage and its former domain 1sm.io now answers from a third party — WHOIS registrant "Nocode ltd" (Paphos, CY) — serving the archived 2020 marketing page (Last-Modified 2020-07-14) with injected Latenode affiliate copy and a "Contact the Domain Owner" footer, while its GitHub org 1smHQ holds zero public repositories and no api/docs/developer subdomain resolves.
  evidence:
  - status: 200
    url: https://1sm.io/
  - status: 200
    url: https://1sm.io/openapi.json
  - status: 200
    url: https://1sm.io/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/1smHQ/repos
  - status: 404
    url: https://pypi.org/pypi/1sm/json
  reason: defunct
  state: none
created: '2026-09-05'
description: 1sm was a New York City revenue-operations (RevOps) analytics startup founded in 2020 by James Weitzman, Chris Lonardo and Jordan Josloff. It raised a $375K pre-seed round announced in July 2020 while in the Techstars NYC 2020 accelerator class, and pitched itself as the first no-code RevOps analytics platform — integrating a company's existing sales and marketing tools into one unified view of buyer personas and ideal customer profiles, with forward-looking analytics predicting which messaging would drive clicks, meetings and closed deals. The product never advanced past a public beta waitlist and no public API, SDK, webhook surface or developer program was ever shipped. As of September 2026 the company's former domain, 1sm.io, is registered to a third party — Nocode ltd of Paphos, Cyprus, the entity behind the Latenode automation platform — which republishes the archived July 2020 marketing page with injected affiliate copy and a "Contact the Domain Owner" footer, so that
  host is deliberately NOT wired as this company's Website pointer.
layout: provider
modified: '2026-09-16'
name: 1sm
nav: Providers
network: true
overview: 1sm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Revenue Operations, Sales, and Marketing.
random_paper: 9
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 2
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
slug: 1sm
tags:
- Company
- Analytics
- Revenue Operations
- Sales
- Marketing
- Business Intelligence
- Software-as-a-Service
- Defunct
---
