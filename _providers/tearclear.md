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
artifact_total: 1
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tearclear
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/tearclear-stock
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tearclear-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tearclear-llms.txt
coverage:
  checked: '2026-08-29'
  detail: TearClear is a clinical-stage ophthalmic pharmaceutical company whose product is a BAK-removing eye-drop bottle filter and the latanoprost/timolol/brimonidine drugs dispensed through it, so there is no software product to expose an API on; separately, its own domain tearclear.com now answers 403 from an unprovisioned SiteGround default vhost, and no api./developer./docs. subdomain resolves at all.
  evidence:
  - status: 403
    url: https://tearclear.com/
  - status: 403
    url: https://tearclear.com/openapi.json
  - status: 403
    url: https://tearclear.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/tearclear
  - status: 200
    url: https://www.linkedin.com/company/tearclear
  reason: not-a-software-company
  state: none
created: '2026-08-29'
description: 'TearClear Corp. is a clinical-stage ophthalmic pharmaceutical company founded in 2015 that develops a preservative-removing drug delivery platform: a chemical filter built into a conventional multi-dose eye-drop bottle that captures benzalkonium chloride (BAK) at the point of instillation, so the medication stays preserved in the bottle but reaches the ocular surface preservative-free. Its lead candidate TC-002 (latanoprost ophthalmic solution 0.005%) met the primary and all secondary endpoints in the CLEAR Phase 3 pivotal glaucoma trial, with TC-001 (timolol), TC-003 (brimonidine/timolol) and TC-004 (brimonidine) behind it. TearClear ships drug products and delivery hardware, not software: it operates no developer program and publishes no API, SDK or machine-readable contract, and its own corporate domain no longer resolves to a served website.'
layout: provider
modified: '2026-08-29'
name: Tearclear
nav: Providers
network: true
overview: Tearclear is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Ophthalmology, Drug Delivery, and Life Sciences.
random_paper: 2
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 3
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
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Tearclear Domain Security
  slug: tearclear-domain-security
  summary_line: no transport/DNS hardening detected
slug: tearclear
tags:
- Company
- Pharmaceuticals
- Ophthalmology
- Drug Delivery
- Life Sciences
- Medical Devices
- Glaucoma
- Clinical Stage
---
