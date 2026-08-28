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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jetti-resources-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jetti-resources-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.jettiresources.com/
- group: company
  title: ''
  type: About
  url: https://www.jettiresources.com/about-jetti
- group: other
  title: ''
  type: Technology
  url: https://www.jettiresources.com/our-technology
- group: company
  title: ''
  type: News
  url: https://www.jettiresources.com/news-and-reports/press-releases
- group: other
  title: ''
  type: Reports
  url: https://www.jettiresources.com/news-and-reports/reports
- group: other
  title: ''
  type: Sustainability
  url: https://www.jettiresources.com/sustainability
- group: operate
  title: ''
  type: Support
  url: https://www.jettiresources.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://www.jettiresources.com/careers
- group: start
  title: ''
  type: CustomerPortal
  url: https://www.jettiresources.com/customer-portal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jettiresources.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jettiresources.com/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.jettiresources.com/cookie-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jetti-resources/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/jetti-resources_stock/
coverage:
  checked: '2026-08-23'
  detail: Jetti Resources licenses a copper-leaching catalyst and modular dosing plants to mine operators — the product is chemistry and metallurgy, not software — and its only authenticated surface is an Intralinks-hosted document room for existing licensees, reached by contacting a Jetti account manager rather than by signing up; every spec, llms.txt and .well-known discovery path on www.jettiresources.com returns a genuine Next.js 404, confirmed against an invalid control path.
  evidence:
  - status: 404
    url: https://www.jettiresources.com/openapi.json
  - status: 404
    url: https://www.jettiresources.com/.well-known/api-catalog
  - status: 404
    url: https://www.jettiresources.com/.well-known/agent-card.json
  - status: 404
    url: https://www.jettiresources.com/llms.txt
  - status: 404
    url: https://www.jettiresources.com/control-path-does-not-exist-9f3a2b
  - status: 200
    url: https://www.jettiresources.com/customer-portal
  - status: 200
    url: https://api.github.com/orgs/jetti-resources
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'Jetti Resources is a Boulder, Colorado based metallurgical technology company whose catalytic leaching process unlocks copper from low-grade primary sulfide ores such as chalcopyrite — roughly 70% of the world''s copper resources — that conventional pyrometallurgy cannot treat economically and that bioleaching cannot treat at all because of the passivation layer that halts extraction. Jetti''s catalyst prevents that layer from forming, allowing uninterrupted heap and stockpile leaching through existing bioleach and SX-EW circuits using modular, standardized micro plants that require no additional permits. The technology has been deployed commercially since 2019, including at Capstone''s Pinto Valley mine in Arizona and Freeport-McMoRan''s El Abra operation in Chile, and the company is backed by BHP, Freeport-McMoRan, Mitsubishi Corporation, BMW Group, BlackRock, T. Rowe Price, Orion Resource Partners, DNS Capital and Zoma Capital. Jetti sells a chemical and process technology
  licence to mine operators rather than software: it runs no developer program, publishes no public API, SDK or machine-readable specification, and its only authenticated surface is an Intralinks-hosted customer portal for existing licensees.'
image: https://www.jettiresources.com/opengraph-image
layout: provider
modified: '2026-08-23'
name: Jetti Resources
nav: Providers
network: true
overview: 'Jetti Resources is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mining, Copper, Critical Minerals, and Metals.


  Jetti Resources'' developer surface includes product news, support, and 14 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 10.1
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Jetti Resources Domain Security
  slug: jetti-resources-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jetti-resources
tags:
- Company
- Mining
- Copper
- Critical Minerals
- Metals
- Hydrometallurgy
- Cleantech
- Energy Transition
- Sustainability
- Industrial Technology
website: https://www.jettiresources.com/
---
