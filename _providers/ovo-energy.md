---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ovo-energy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ovo-energy-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ovo-energy-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ovo-energy-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/ovo-energy-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ovo-energy-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ovoenergy.com/
- group: company
  title: ''
  type: About
  url: https://www.ovoenergy.com/about
- group: company
  title: ''
  type: GroupWebsite
  url: https://company.ovo.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ovotech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ovoenergy
- group: company
  title: ''
  type: Blog
  url: https://www.ovoenergy.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.ovoenergy.com/help
- group: operate
  title: ''
  type: Forum
  url: https://forum.ovoenergy.com/
- group: start
  title: ''
  type: CustomerPortal
  url: https://my.ovoenergy.com/login
- group: start
  title: ''
  type: Login
  url: https://my.ovoenergy.com/login
- group: start
  title: ''
  type: SignUp
  url: https://www.ovoenergy.com/get-energy-quote
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ovoenergy.com/home-energy-plans
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ovoenergy.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ovoenergy.com/terms
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ovo-energy-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.ovoenergy.com/security
- group: company
  title: ''
  type: Careers
  url: https://careers.ovo.com/
created: '2026-07-27'
description: 'OVO Energy is a United Kingdom household electricity and gas supplier founded in Bristol in 2009 by Stephen Fitzpatrick, and — after absorbing SSE''s household energy business in January 2020 — the third-largest domestic supplier in Great Britain with roughly four million home energy customers. It sits at the retail end of the GB energy value chain: buying wholesale, holding an Ofgem supply licence, settling through Elexon, reading SMETS2 smart meters over the licensed Smart DCC network, and billing the customer, alongside solar, home battery, heat pump, EV smart-charging (Charge Anytime) and demand-flexibility (Power Move) propositions. Its parent OVO Group also owns Kaluza, an API-first energy intelligence platform licensed to utilities worldwide — the direct British analogue to Octopus Energy''s Kraken — but that platform is a separate brand on a separate domain, and none of its API surface is published under OVO Energy. OVO Energy''s own API posture is closed: no developer
  portal, no API documentation, no machine-readable contract, and no third-party route to a customer''s usage or billing data. developer.ovoenergy.com, developers.ovoenergy.com, docs.ovoenergy.com and data.ovoenergy.com do not resolve; /developers, /api, /docs, /openapi.json and /.well-known/openid-configuration all return 404; api.ovoenergy.com resolves and is live but answers every path with a bare text/plain 404 ("No context-path matches the request URI"). The only consumer data surface found is undocumented and unsupported — smartpaymapi.ovoenergy.com/usage/api/half-hourly returns HTTP 401 JSON to an anonymous caller and serves half-hourly smart-meter consumption only to a signed-in OVO customer session. Britain mandated the metering INFRASTRUCTURE, not a data right: OVO is bound by the Smart Energy Code and the DCC, which is live and implemented, but no consumer data-portability mandate equivalent to Australia''s Consumer Data Right or Ontario''s Green Button applies to it. The Australian
  namesake, OVO Energy Pty Ltd, IS a designated CDR energy data holder — but it was acquired outright by AGL Energy in April 2024 and is no longer part of this organization, so that obligation does not attach here. Consumer data is closed, open market data is published by other GB parties (NESO, Elexon, the DNOs), and on 11 May 2026 OVO agreed the sale of this retail business to E.ON, with Kaluza explicitly excluded from the deal.'
image: https://www.ovoenergy.com/apple-touch-icon.png
layout: provider
modified: '2026-07-27'
name: OVO Energy
nav: Providers
network: true
overview: 'OVO Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Gas.


  OVO Energy''s developer surface includes engineering blog, support, signup flow, pricing, and 19 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 21.7
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 15.8
  previous_composite: 21.7
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Ovo Energy Domain Security
  slug: ovo-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ovo Energy Vulnerability Disclosure
  slug: ovo-energy-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ovo-energy
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Smart Metering
- Energy Retail
- Solar
- EV Charging
- Demand Response
website: https://www.ovoenergy.com/
---
