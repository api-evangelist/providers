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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evie-networks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://evie.com.au/
- group: company
  title: ''
  type: About
  url: https://evie.com.au/about-evie/
- group: company
  title: ''
  type: Blog
  url: https://evie.com.au/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://evie.com.au/feed/
- group: operate
  title: ''
  type: Support
  url: https://evie.com.au/help-center/
- group: operate
  title: ''
  type: FAQ
  url: https://evie.com.au/frequently-asked-questions/
- group: operate
  title: ''
  type: ContactUs
  url: https://evie.com.au/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://evie.com.au/about-evie/careers/
- group: other
  title: ''
  type: Team
  url: https://evie.com.au/about-evie/our-team/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evie-networks-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/evie-networks-conformance.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://evie.com.au/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://evie.com.au/terms-of-service/
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/evie-networks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goevie
created: '2026-07-27'
description: 'Evie Networks is an Australian electric-vehicle charging infrastructure company, founded in 2017 and backed by the St Baker Energy Innovation Fund, that owns and operates one of the country''s largest DC fast and ultrafast public charging networks across 300+ locations in every state and territory. It sits downstream of the electricity retail market as a charge point operator (CPO) and e-mobility service provider, buying energy and reselling it as charging sessions to drivers and fleets, and it also builds and operates charging assets for site hosts, councils, dealerships and commercial property owners. Its API posture is closed: as of 2026-07-27 there is no developer portal, no published API documentation, no OpenAPI or other machine-readable contract, and no named support for the EV charging interoperability standards (OCPP, OCPI, ISO 15118). Evie is not a designated data holder under Australia''s Consumer Data Right energy regime — the CDR Register''s public energy data-holder
  brand summary lists 84 brands and Evie is not among them — so the statutory data mandate that produced identical APIs across Australian banks and energy retailers does not reach the EV charging layer at all. A live production API host exists at api.goevie.com.au serving the Evie Charging mobile app, but it is undocumented, unadvertised and returns a Google Cloud Endpoints 404 to anonymous callers. Neither consumer charging-session data nor network/market data is published through any documented public interface; charger location data reaches developers only through third-party aggregators.'
image: https://evie.com.au/wp-content/uploads/2023/07/evie-favicon-300x300.png
layout: provider
modified: '2026-07-27'
name: Evie Networks
nav: Providers
network: true
overview: 'Evie Networks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Australia, EV Charging, Electricity, and Utilities.


  Evie Networks'' developer surface includes engineering blog, support, FAQ, and 13 more developer resources.'
random_paper: 87
score:
  band: emerging
  composite: 14.0
  delta: -2.2
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 16.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evie-networks/refs/heads/main/screenshots/evie-networks-2026-08-07T165052.png
security:
- kind: domain-security
  name: Evie Networks Domain Security
  slug: evie-networks-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: evie-networks
tags:
- Energy
- Australia
- EV Charging
- Electricity
- Utilities
- E-Mobility
- Charging Infrastructure
- Fleet
- Transport Electrification
website: https://evie.com.au/
---
