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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-02'
  detail: Vascular Therapies is a clinical-stage biopharma developing Sirogen, a sirolimus-eluting collagen implant for hemodialysis vascular access — there is no software product to expose an API for, and its own web presence is additionally offline, with www.vasculartx.com returning Webflow's unpublished-domain 404 catch-all on the site root and on every indexed path.
  evidence:
  - status: 404
    url: https://www.vasculartx.com/
  - status: 404
    url: https://www.vasculartx.com/news
  - status: 403
    url: https://vasculartx.com/
  - status: 403
    url: https://vasculartx.com/openapi.json
  - status: 403
    url: https://vasculartx.com/.well-known/agent-card.json
  - status: 0
    url: https://api.vasculartx.com/
  - status: 0
    url: https://developer.vasculartx.com/
  - status: 404
    url: https://github.com/vasculartx
  reason: not-a-software-company
  state: none
created: '2026-09-02'
description: 'Vascular Therapies, Inc. is a privately held, clinical-stage biopharmaceutical company headquartered in Cresskill, New Jersey, developing Sirogen, a proprietary sirolimus formulation delivered from a bioabsorbable collagen implant placed perivascularly at the time of surgery. The product is aimed at reducing surgical stenosis and improving arteriovenous fistula maturation and patency in end-stage renal disease patients who need hemodialysis vascular access. Sirolimus for dialysis vascular access carries FDA Fast Track status and Orphan Drug designation in both the United States and the European Union. The company ran the Phase 3 ACCESS trial (243 ESRD patients across 20 US sites) and the multinational Phase 3 ACCESS 2 trial, whose topline results presented in April 2025 did not meet the primary clinical fistula maturation endpoint. Vascular Therapies is a therapeutics developer, not a software company: it ships a drug-device combination product through clinical trials and regulatory
  review, and publishes no API, SDK, developer portal or machine-readable contract of any kind.'
layout: provider
modified: '2026-09-02'
name: Vascular Therapies
nav: Providers
network: true
overview: Vascular Therapies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Medical Devices, and Drug Delivery.
random_paper: 6
score:
  band: minimal
  composite: 1.8
  coverage:
    artifact_dirs: 1
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
slug: vascular-therapies
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Medical Devices
- Drug Delivery
- Clinical Trials
- Nephrology
- Healthcare
---
