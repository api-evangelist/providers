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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/utility-global-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://utilityglobal.com/
- group: company
  title: ''
  type: About
  url: https://utilityglobal.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://utilityglobal.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://utilityglobal.com/feed/
- group: company
  title: ''
  type: Newsroom
  url: https://media.utilityglobal.com/news
- group: operate
  title: ''
  type: Contact
  url: https://utilityglobal.com/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/utilityglobal/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/utility-global-llms.txt
coverage:
  checked: '2026-09-02'
  detail: Utility Global sells hydrogen-producing reactor hardware (H2Gen/eXERO) into steel and refining plants; utilityglobal.com is a WordPress marketing site with no developer section, no api./developer./docs. subdomain in DNS at all, and the only machine-readable endpoint on the domain is the stock WordPress core /wp-json/ CMS route index, which is infrastructure rather than a product API.
  evidence:
  - status: 404
    url: https://utilityglobal.com/openapi.json
  - status: 404
    url: https://utilityglobal.com/.well-known/agent-card.json
  - status: 404
    url: https://utilityglobal.com/llms.txt
  - status: 0
    url: https://api.utilityglobal.com/
  - status: 404
    url: https://api.github.com/orgs/utilityglobal
  - status: 200
    url: https://utilityglobal.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-09-02'
description: 'Utility Global is a Houston, Texas industrial decarbonization company founded in 2018. Its proprietary H2Gen and eXERO platform converts water into high-purity hydrogen using the residual electrochemical energy already present in industrial off-gases and biogenic gases — driving water electrolysis without electricity — while concentrating CO2 into a separate capture-ready stream. The company sells into steel, low-carbon fuels, and refining, petrochemicals and chemicals, and has run demonstration programs on blast-furnace off-gas at commercial steel facilities. It is a hardware and process-technology business, not a software vendor: its public web presence is a marketing site with no developer program, no API documentation, and no machine-readable contract of any kind.'
image: https://utilityglobal.com/wp-content/uploads/2025/04/UtilityGlobal_Logo_Primary-1024x232.webp
layout: provider
modified: '2026-09-02'
name: Utility Global
nav: Providers
network: true
overview: 'Utility Global is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Hydrogen, Decarbonization, and Clean Energy.


  Utility Global''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: domain-security
  name: Utility Global Domain Security
  slug: utility-global-domain-security
  summary_line: TLSv1.2 · DMARC
slug: utility-global
tags:
- Company
- Energy
- Hydrogen
- Decarbonization
- Clean Energy
- Industrial
- Steel
- Climate Tech
- Chemicals
website: https://utilityglobal.com/
---
