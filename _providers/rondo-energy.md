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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.rondo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.rondo.com/news-press
- group: operate
  title: ''
  type: Support
  url: https://www.rondo.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rondo.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rondo.com/purchase-order-terms-conditions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rondo-energy/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rondo-energy-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rondo-energy-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rondo-energy-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Rondo Energy sells a physical product - a refractory-brick industrial heat battery, bought outright, leased, or paid for as delivered steam - and its entire web surface is a 44-page Next.js marketing site plus a Jetty login portal; there is no developer section, no API host (api/developer/docs .rondo.com do not resolve), and the one identity host that exists, login.rondo.com, is an Okta custom domain whose TLS certificate does not match the name.
  evidence:
  - status: 404
    url: https://www.rondo.com/openapi.json
  - status: 404
    url: https://www.rondo.com/docs
  - status: 404
    url: https://www.rondo.com/llms.txt
  - status: 404
    url: https://www.rondo.com/.well-known/agent-card.json
  - status: 302
    url: https://portal.rondo.com/web/home
  - status: 200
    url: https://www.rondo.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Rondo Energy is an Alameda, California industrial decarbonization company led by CEO John O''Donnell that builds the Rondo Heat Battery (RHB), a thermal energy storage system that converts intermittent wind and solar electricity into heat stored in thousands of tons of refractory brick at temperatures up to 1,500C and returns it as continuous steam, thermal oil, superheated air, or combined heat and power at rated outputs from 2MWth to over 100MWth. The RHB is sold as a drop-in replacement for a fossil-fuel boiler, via capital purchase, lease, or heat purchase agreement, into cement, food and beverage, chemicals, fuels and ethanol, textiles, pulp and paper, mining, pharmaceuticals, and direct air capture. Rondo operates the world''s largest industrial heat battery and has announced a 90GWh factory plan with Siam Cement Group, backed by Breakthrough Energy Ventures and Catalyst, Energy Impact Partners, Microsoft''s Climate Innovation Fund, Rio Tinto, SABIC, Aramco Ventures,
  and the European Investment Bank. Rondo sells hardware and delivered heat, not software: it publishes no developer portal, API reference, or machine-readable specification.'
image: https://www.rondo.com/favicon.png
layout: provider
modified: '2026-08-05'
name: Rondo Energy
nav: Providers
network: true
overview: 'Rondo Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Energy Storage, Thermal Energy Storage, and Industrial Heat.


  Rondo Energy''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 13.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Rondo Energy Domain Security
  slug: rondo-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rondo-energy
tags:
- Company
- Energy
- Energy Storage
- Thermal Energy Storage
- Industrial Heat
- Decarbonization
- Climate Tech
- Renewable Energy
- Manufacturing
- Hardware
website: https://www.rondo.com/
---
