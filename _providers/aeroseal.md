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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aeroseal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aeroseal.com/
- group: company
  title: ''
  type: Blog
  url: https://aeroseal.com/blog/
- group: company
  title: ''
  type: BlogFeeds
  url: https://aeroseal.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://support.aeroseal.com/
- group: start
  title: ''
  type: Login
  url: https://aeroseal.com/dealer-login/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aeroseal.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://aeroseal.com/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aeroseal-llc
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aeroseal-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Aeroseal sells computer-controlled duct/envelope sealing equipment and dealer software, not APIs — its live application backend at api.aeroseal.com answers the plain-text body "live (2.44)" at the root but returns 404 on every discovery path (/openapi.json, /swagger.json, /graphql, /api-docs, /docs, /.well-known/*), no developer/docs/portal subdomain resolves, no package exists on npm or PyPI, and the Aeroseal-LLC GitHub org has zero public repositories.
  evidence:
  - status: 200
    url: https://api.aeroseal.com/
  - status: 404
    url: https://api.aeroseal.com/openapi.json
  - status: 404
    url: https://api.aeroseal.com/graphql
  - status: 404
    url: https://aeroseal.com/llms.txt
  - status: 404
    url: https://aeroseal.com/.well-known/agent-card.json
  - status: 403
    url: https://aeroseal.com/
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'Aeroseal is a building-envelope and duct air-sealing technology company headquartered in Miamisburg, Ohio. Its patented aerosol sealing process — developed by Dr. Mark Modera under U.S. Department of Energy research at Lawrence Berkeley National Laboratory beginning in 1993 and commercialized as Aeroseal in 2010 — injects a fog of non-toxic sealant particles into a pressurized duct system or building envelope, where the particles collect at the edges of leaks and seal them from the inside. The company sells computer-controlled sealing equipment and software to a dealer network under the HomeSeal Connect and AeroBarrier Connect product lines; the on-machine software measures leakage in real time and issues a certificate of completion showing before-and-after leakage rates. Aeroseal reports operations in 27 countries and all 50 U.S. states, and has raised roughly $119M across three rounds, including a $67M Series B in July 2023 backed by Breakthrough Energy Ventures, Climate
  Investment and OGCI. It is an equipment, materials and contractor-software business rather than a developer platform: it publishes no public API, developer portal, SDK or machine-readable specification.'
image: https://aeroseal.co.uk/wp-content/uploads/2025/10/Aeroseal-Logo-WhiteText.png
layout: provider
modified: '2026-08-06'
name: Aeroseal
nav: Providers
network: true
overview: 'Aeroseal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy Efficiency, Climate Technology, HVAC, and Building Envelope.


  Aeroseal''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aeroseal/refs/heads/main/screenshots/aeroseal-2026-08-07T161005.png
security:
- kind: domain-security
  name: Aeroseal Domain Security
  slug: aeroseal-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: aeroseal
tags:
- Company
- Energy Efficiency
- Climate Technology
- HVAC
- Building Envelope
- Duct Sealing
- Indoor Air Quality
- Building Performance
- Construction Technology
website: https://aeroseal.com/
---
