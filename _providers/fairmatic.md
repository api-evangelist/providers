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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://leeoinsurance.com/
coverage:
  checked: '2026-08-12'
  detail: Fairmatic was renamed LEEO Insurance Services in December 2025 and every Fairmatic host now redirects to leeoinsurance.com (api.fairmatic.com 404s outright), so the live API surface is already profiled under all/leeo-insurance-services and nothing remains to enrich here.
  evidence:
  - status: 301
    url: https://fairmatic.com/
  - status: 302
    url: https://docs.fairmatic.com/
  - status: 301
    url: https://app.fairmatic.com/login/
  - status: 404
    url: https://api.fairmatic.com/
  - status: 404
    url: https://api.fairmatic.com/openapi.json
  - status: 403
    url: https://forgeglobal.com/fairmatic_stock/
  reason: defunct
  state: none
created: '2026-08-12'
description: 'Fairmatic was a San Francisco commercial-auto insurance MGA founded in 2017 that underwrote and priced fleet policies from phone-collected telematics. It rebranded to LEEO Insurance Services on 2025-12-15, and every Fairmatic-branded web surface now 301/302 redirects to leeoinsurance.com: fairmatic.com and www.fairmatic.com to leeoinsurance.com, docs.fairmatic.com to docs.leeoinsurance.com, app.fairmatic.com to app.leeoinsurance.com. The old API host api.fairmatic.com returns 404 at its root; the live REST Fleet Telematics API is served from api.leeoinsurance.com/api/v1. This repository is therefore a DUPLICATE STUB, created by the harvest backlog from a secondary-market share-listing page rather than from the company''s own domain. The canonical, fully enriched profile of this company is all/leeo-insurance-services, which already carries the four OpenAPIs, the authentication, conventions, error, lifecycle, changelog, conformance, data-model, MCP, llms.txt, skills, agentic-access
  and domain-security artifacts, and the complete Fairmatic-branded SDK line (npm, Maven Central, NuGet, CocoaPods). No artifacts are wired here on purpose: duplicating them would split one company across two listings and two Kin Scores.'
layout: provider
modified: '2026-08-12'
name: Fairmatic
nav: Providers
network: true
overview: Fairmatic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Commercial Auto Insurance, and Telematics.
random_paper: 20
score:
  band: minimal
  composite: 0.5
  coverage:
    artifact_dirs: 0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
      reason: never_enriched
  previous_composite: 0.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 0.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
slug: fairmatic
tags:
- Company
- Insurance
- Insurtech
- Commercial Auto Insurance
- Telematics
- Fleet Management
- Managing General Agent
- Renamed
website: https://leeoinsurance.com/
---
