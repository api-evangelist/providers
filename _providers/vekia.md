---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.1
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.vekia.fr/
- group: company
  title: ''
  type: Blog
  url: https://www.vekia.fr/en/supply-chain-blog/
- group: operate
  title: ''
  type: Contact
  url: https://www.vekia.fr/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vekia.fr/en/privacy-policy/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vekia-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vekia-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vekia-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vekia-llms.txt
coverage:
  checked: '2026-08-17'
  detail: Vekia sells Vekia Engine as an enterprise supply-chain platform that its own team wires into a customer's ERP, and publishes no developer program at all — api.vekia.fr, docs.vekia.fr and developer.vekia.fr do not resolve, /developers and /api return the site 404, and the only machine-readable surfaces on www.vekia.fr are its WordPress REST namespace and an OAuth-gated WordPress MCP endpoint, neither of which is the product API.
  evidence:
  - status: 404
    url: https://www.vekia.fr/developers
  - status: 404
    url: https://www.vekia.fr/api
  - status: 404
    url: https://www.vekia.fr/openapi.json
  - status: 404
    url: https://www.vekia.fr/.well-known/agent-card.json
  - status: 403
    url: https://www.vekia.fr/wp-json/mcp/mcp-oauth-server
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: Vekia is a French supply-chain software vendor founded in 2008 in Lille by Manuel Davy (Vekia SAS, 143 rue d'Athènes, 59800 Lille, RCS Lille Métropole 503 225 716). Its platform, Vekia Engine, applies probabilistic artificial intelligence and machine learning to demand and stock forecasting, then generates optimised purchase-order proposals that are pushed back into the customer's existing ERP rather than replacing it, alongside shortage-risk alerting and a logistics control tower. Vekia Disrupt covers disruption and shortage management. The platform is hosted on Microsoft Azure in Europe and marketed to retail and specialised distribution, e-commerce, industry, energy and telecom, with published case studies at ENGIE, Mr Bricolage and Okaïdi. Vekia publishes no public API, no developer portal, no API reference and no machine-readable contract; ERP, WMS and TMS integration is delivered as a project by Vekia rather than through a self-serve developer surface.
image: https://www.vekia.fr/wp-content/uploads/2019/04/solution-supply-chain-vekia.png
layout: provider
modified: '2026-08-17'
name: Vekia
nav: Providers
network: true
overview: 'Vekia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Supply Chain, Demand Forecasting, Inventory Optimization, and Replenishment.


  Vekia''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Vekia Plans Pricing
  plan_count: 0
  slug: vekia-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Vekia Rate Limits
  slug: vekia-rate-limits
score:
  band: minimal
  composite: 10.5
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: domain-security
  name: Vekia Domain Security
  slug: vekia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vekia
tags:
- Company
- Supply Chain
- Demand Forecasting
- Inventory Optimization
- Replenishment
- Retail
- Machine Learning
- Artificial Intelligence
- Logistics
- France
website: https://www.vekia.fr/
---
