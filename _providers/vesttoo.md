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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vesttoo-domain-security.yml
coverage:
  checked: '2026-09-02'
  detail: Vesttoo was liquidated in Chapter 11 (plan effective April 2024) and its domain now publishes MX and TXT records but no A, AAAA or CNAME, so vesttoo.com has no web host at all and every HTTPS probe fails at connection setup rather than returning a page.
  evidence:
  - status: 0
    url: https://vesttoo.com/
  - status: 0
    url: https://www.vesttoo.com/
  - status: 0
    url: https://vesttoo.com/.well-known/security.txt
  - status: 0
    url: https://vesttoo.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/vesttoo
  reason: defunct
  state: none
created: '2026-09-02'
description: Vesttoo Ltd. was an Israeli insurtech, founded in Tel Aviv in 2018, that operated a technology platform for insurance-linked securities and alternative risk transfer — matching insurers, reinsurers and MGAs seeking capacity with institutional investors in the capital markets, with an emphasis on non-catastrophe life and property/casualty risk. The company collapsed in 2023 after billions of dollars of counterfeit letters of credit were discovered being used as collateral on its platform. Vesttoo filed for Chapter 11 in Delaware in August 2023; a creditors' plan of liquidation was confirmed in early 2024 and went effective in April 2024, and the estate is now administered by the Vesttoo Creditors Liquidating Trust, which continues to pursue recovery litigation. The company no longer operates. Its domain publishes no web host, and no developer portal, API documentation, SDK or machine-readable contract survives at any reachable address.
layout: provider
modified: '2026-09-02'
name: Vesttoo
nav: Providers
network: true
overview: Vesttoo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Reinsurance, and Insurance-Linked Securities.
random_paper: 11
score:
  band: minimal
  composite: 1.9
  coverage:
    artifact_dirs: 2
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
  previous_composite: 1.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Vesttoo Domain Security
  slug: vesttoo-domain-security
  summary_line: DMARC
slug: vesttoo
tags:
- Company
- Insurance
- Insurtech
- Reinsurance
- Insurance-Linked Securities
- Alternative Risk Transfer
- Capital Markets
- Financial Services
- Defunct
---
