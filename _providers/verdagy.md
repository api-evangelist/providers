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
  url: security/verdagy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://verdagy.com/
- group: other
  title: ''
  type: Product
  url: https://verdagy.com/product-electrolyzers-clean-hydrogen/
- group: company
  title: ''
  type: Blog
  url: https://verdagy.com/news/
- group: company
  title: ''
  type: News
  url: https://verdagy.com/news/
- group: operate
  title: ''
  type: Support
  url: https://verdagy.com/contact/
- group: operate
  title: ''
  type: Contact
  url: https://verdagy.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://verdagy.com/hydrogen-jobs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://verdagy.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/verdagy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Verdagy
- group: other
  title: ''
  type: Simulator
  url: https://simulator.verdagy.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/verdagy-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Verdagy manufactures alkaline electrolyzer hardware for industrial hydrogen plants; its only web application, the Energize simulator, is a client-side Angular calculator whose bundle contains no first-party API host, and every OpenAPI, GraphQL, MCP and agent-card path on verdagy.com returns 404.
  evidence:
  - status: 404
    url: https://verdagy.com/openapi.json
  - status: 404
    url: https://verdagy.com/llms.txt
  - status: 404
    url: https://verdagy.com/.well-known/agent-card.json
  - status: 404
    url: https://verdagy.com/.well-known/security.txt
  - status: 200
    url: https://simulator.verdagy.com/definitely-not-a-real-path-zzz9
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: Verdagy is a Moss Landing, California clean-energy hardware company that designs and manufactures dynamic alkaline water electrolysis systems for large-scale green hydrogen production. Its eDynamic platform runs very large-area membrane-based electrochemical cells at high current density with dynamic turndown, so electrolyzers can follow intermittent renewable power, targeting fossil-fuel cost parity for clean hydrogen by 2028 without subsidies. The company operates a 2 MW eDynamic demonstration plant at Moss Landing with more than 21,000 commercial cell hours, plus 500 kW and 100 kW test plants, and opened a DOE-supported gigawatt-scale manufacturing facility of more than 100,000 square feet in Newark, California. Verdagy sells electrolyzer hardware and project capacity to industrial hydrogen buyers — refining, ammonia, methanol, e-fuels and SAF — rather than software; it publishes no developer program, no public API, and no machine-readable API contract.
image: https://verdagy.com/wp-content/themes/verdagy/img/logo.png
layout: provider
modified: '2026-08-05'
name: Verdagy
nav: Providers
network: true
overview: 'Verdagy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Clean Energy, Green Hydrogen, and Hydrogen.


  Verdagy''s developer surface includes engineering blog, product news, support, and 10 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Verdagy Domain Security
  slug: verdagy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: verdagy
tags:
- Company
- Energy
- Clean Energy
- Green Hydrogen
- Hydrogen
- Electrolyzers
- Industrial Equipment
- Manufacturing
- Decarbonization
- Climate Tech
website: https://verdagy.com/
---
