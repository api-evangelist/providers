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
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/lula_stock/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/lula/
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/lula
coverage:
  checked: '2026-08-25'
  detail: Lula Technologies divested its insurance division to Nantucket Capital Corp and was sold by its founders in 2024, and its domain has since been released rather than redirected — lula.is now delegates to ns1/ns2.parkingcrew.net, serves no TLS certificate at all (the HTTPS handshake fails outright), returns 410 Gone on the HTTP apex, and answers every deeper path with one identical 32KB "This domain may be for sale!" holding page, so all 21 /.well-known/ and 27 contract-discovery probes are catch-all HTML rather than documents; the historical developer portal at www.lula.is/developers was last archived on 2022-12-07 and the Postman collection that was Lula's public API reference now returns 404.
  evidence:
  - status: 410
    url: http://lula.is/
  - status: 200
    url: http://api.lula.is/openapi.json
  - status: 200
    url: http://lula.is/.well-known/agent-card.json
  - status: 404
    url: https://documenter.getpostman.com/view/6602648/TzRRCTzg
  - status: 200
    url: https://equityzen.com/company/lula/
  reason: defunct
  state: none
created: '2026-08-25'
description: 'Lula Technologies, Inc. was a Miami, Florida insurance-infrastructure company founded by twin brothers Matthew Vega-Sanz (CEO) and Michael Vega-Sanz (President). It started as the car-sharing startup Lula Rides and pivoted during the COVID-19 pandemic into an API-first — widely described at the time as "Stripe-like" — insurance platform for small and mid-sized car rental, car-sharing, trucking and logistics fleet operators, bundling driver vetting and risk assessment, fraud detection, driver-history checks, episodic/on-demand policy issuance and claims handling behind a single API underwritten through licensed insurance partners. It raised an $18M Series A in July 2021 and a $35.5M Series B, and its public developer surface was a Postman documenter collection alongside a developer portal at www.lula.is/developers. In 2024 Lula divested its insurance division to Nantucket Capital Corp, a San Diego MGA, headcount fell from roughly 150 to about 19, and the founders sold the company.
  The domain lula.is has since left the company''s control — it now delegates to parkingcrew.net and serves a "This domain may be for sale!" holding page — the API host api.lula.is is gone, and the Postman collection returns 404. No public API surface remains. NOTE FOR FUTURE PASSES — the same founders later built a SEPARATE company, Gail (legal entity Nothing Technologies, Inc., meetgail.com), which does operate a live developer surface; Gail is not a rename of Lula and none of its artifacts may be attributed to this profile. Two other unrelated companies also trade as "Lula": Lula (lula.life, property maintenance) and Lula Commerce (lulacommerce.com, convenience retail). This profile is retained as a historical company record.'
layout: provider
modified: '2026-08-25'
name: Lula
nav: Providers
network: true
overview: Lula is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Embedded Insurance, and Car Rental.
random_paper: 10
score:
  band: minimal
  composite: 0.5
  coverage:
    artifact_dirs: 1
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
      reason: no_resolvable_host
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
slug: lula
tags:
- Company
- Insurance
- Insurtech
- Embedded Insurance
- Car Rental
- Car Sharing
- Fleet Management
- Risk Assessment
- Claims Management
- Logistics
---
