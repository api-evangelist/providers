---
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zeroavia-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zeroavia-llms.txt
- group: company
  title: ''
  type: Website
  url: https://zeroavia.com/
- group: company
  title: ''
  type: Blog
  url: https://zeroavia.com/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://zeroavia.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://zeroavia.com/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://zeroavia.com/faq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zeroavia.com/tc/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zeroavia.com/zeroavia-general-privacy-notice/
- group: company
  title: ''
  type: Careers
  url: https://careers.zeroavia.com/
- group: other
  title: ''
  type: MediaKit
  url: https://zeroavia.com/media-kit/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zeroavia
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/zeroavia_stock/
coverage:
  checked: '2026-08-05'
  detail: ZeroAvia sells certified hydrogen-electric aerospace hardware — powertrains, fuel cell stacks and airport refuelling equipment — and its WordPress page sitemap lists no developer, docs or API page at all; api., docs., developer. and developers.zeroavia.com do not resolve in DNS, and there is no ZeroAvia GitHub organization.
  evidence:
  - status: 404
    url: https://zeroavia.com/openapi.json
  - status: 404
    url: https://zeroavia.com/.well-known/agent-card.json
  - status: 404
    url: https://zeroavia.com/llms.txt
  - status: 200
    url: https://zeroavia.com/page-sitemap.xml
  - status: 404
    url: https://api.github.com/orgs/zeroavia
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: ZeroAvia is a UK/US hydrogen-electric aviation company founded in 2017 by Valery Miftakhov, developing hydrogen fuel cell and electric propulsion systems for commercial aircraft. Its powertrain line runs from the ZA600 (600kW, 10-20 seat regional turboprops) through the ZA2000 (2-5MW, 40-80 seat turboprops) to the ZA2000 RJ (5MW+, up to 90 seat regional jets), alongside a component business selling electric propulsion systems, inverters, electric motors and HTPEM/SuperStack fuel cell stacks to other clean-aviation manufacturers, plus a hydrogen airport refuelling ecosystem of electrolyzers, mobile refuelers and LH2 development. It operates from Cotswold Airport in Kemble, UK and from Everett, Washington, and holds FAA and CAA experimental certificates for its flight-test aircraft. ZeroAvia sells certified aerospace hardware to airframers, airlines, lessors and defense customers; it publishes no public developer API, SDK or developer portal.
image: https://zeroavia.com/wp-content/themes/zero-avia5/images/zeroavia-logo.svg
layout: provider
modified: '2026-08-05'
name: ZeroAvia
nav: Providers
network: true
overview: 'ZeroAvia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aviation, Aerospace, Hydrogen, and Fuel Cells.


  ZeroAvia''s developer surface includes engineering blog, support, FAQ, and 10 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 11.3
  delta: -1.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Zeroavia Domain Security
  slug: zeroavia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zeroavia
tags:
- Company
- Aviation
- Aerospace
- Hydrogen
- Fuel Cells
- Electric Propulsion
- Clean Energy
- Manufacturing
- Defense
website: https://zeroavia.com/
---
