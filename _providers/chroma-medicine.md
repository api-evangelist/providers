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
common:
- group: company
  title: ''
  type: Website
  url: https://www.nchromabio.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nchromabio.com/privacy-policy/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/chroma-medicine_stock/
coverage:
  checked: '2026-08-09'
  detail: Chroma Medicine no longer exists as a standalone company — it merged with Nvelop Therapeutics in December 2024 to form nChroma Bio, and chromamedicine.com now 301s to www.nchromabio.com, a six-page WordPress marketing site for a clinical-stage genetic medicines developer with no developer, API, or documentation section.
  evidence:
  - status: 301
    url: https://chromamedicine.com
  - status: 200
    url: https://www.nchromabio.com/
  - status: 404
    url: https://www.nchromabio.com/openapi.json
  - status: 404
    url: https://www.nchromabio.com/.well-known/agent-card.json
  - status: 404
    url: https://www.nchromabio.com/developers
  - status: 404
    url: https://api.github.com/orgs/chromamedicine
  reason: defunct
  state: none
created: '2026-08-09'
description: Chroma Medicine was a Boston-based, clinical-stage biotechnology company developing epigenetic editors — CRISPR-derived medicines that silence or activate genes by writing epigenetic marks rather than cutting DNA — with CRMA-1001, a liver-targeted epigenetic editing therapy for chronic hepatitis B and hepatitis D, as its lead program. In December 2024 it merged with Nvelop Therapeutics, pairing Chroma's epigenetic editors with Nvelop's non-viral in vivo delivery vehicles, to form nChroma Bio with $75 million in new financing. chromamedicine.com now redirects to nchromabio.com. As a therapeutics developer it publishes no developer program, public API, SDK, or machine-readable specification of any kind.
image: https://www.nchromabio.com/wp-content/uploads/2026/03/cropped-nChroma-Isolated-Logo-270x270.jpg
layout: provider
modified: '2026-08-09'
name: Chroma Medicine
nav: Providers
network: true
overview: Chroma Medicine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Genetic Medicine, and Epigenetic Editing.
random_paper: 18
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 5.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 5.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chroma-medicine/refs/heads/main/screenshots/chroma-medicine-2026-09-02T145036.png
slug: chroma-medicine
tags:
- Company
- Biotechnology
- Life Sciences
- Genetic Medicine
- Epigenetic Editing
- Therapeutics
website: https://www.nchromabio.com/
---
