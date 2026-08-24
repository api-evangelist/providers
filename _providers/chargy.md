---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Chargy Agentic Access
  operation_count: 2
  slug: chargy-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: char.gy's statutory open data feed, published to satisfy Part 4 regulation 10 of the UK Public Charge Point Regulations 2023, which requires reference data and availability data to be made available t
  name: char.gy Open Charge Point Data API
  slug: chargy-open-charge-point-data-api
- description: char.gy's commercial Open Charge Point Interface implementation in the Charge Point Operator role, used so that another network's drivers can authorise, charge and be settled on char.gy infrastructure
  name: char.gy OCPI CPO Roaming API
  slug: chargy-ocpi-cpo-api
artifact_total: 9
collections:
- collection_type: open
  name: char.gy Open Charge Point Data API
  slug: open-chargy-open-charge-point-data
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chargy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chargy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chargy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chargy-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chargy-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://help.char.gy/support/solutions/articles/77000576948-public-charge-point-regulations-2023
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chargy-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/chargy-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chargy-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://char.gy/
- group: docs
  title: ''
  type: Documentation
  url: https://help.char.gy/support/solutions/articles/77000576948-public-charge-point-regulations-2023
- group: company
  title: ''
  type: About
  url: https://char.gy/us/about
- group: other
  title: ''
  type: Products
  url: https://char.gy/us/our-products-ev-charging
- group: company
  title: ''
  type: Partners
  url: https://char.gy/us/partners
- group: other
  title: ''
  type: Drivers
  url: https://char.gy/us/drivers
- group: commercial
  title: ''
  type: Pricing
  url: https://char.gy/us/pricing
- group: company
  title: ''
  type: Blog
  url: https://char.gy/us/news
- group: operate
  title: ''
  type: Support
  url: https://help.char.gy/
- group: operate
  title: ''
  type: Contact
  url: https://char.gy/us/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://char.gy/us/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://char.gy/us/terms-of-use
- group: start
  title: ''
  type: SignUp
  url: https://char.gy/users/payg_registrations/new
- group: start
  title: ''
  type: Login
  url: https://char.gy/users/sign_in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/char-gy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/char.gy
- group: other
  title: ''
  type: Application
  url: https://apps.apple.com/app/1636840750
- group: other
  title: ''
  type: Application
  url: https://play.google.com/store/apps/details?id=com.chargy_limited.driverapp
created: '2026-07-27'
description: 'char.gy is a British public electric-vehicle charge point operator that specialises in on-street charging for the roughly forty percent of UK households with no off-street parking, and it is best known for putting the charger inside the lamp post. Founded by Richard Stobart out of the digital agency Unboxed, it installed its first public charger in Marlow, Buckinghamshire in 2018, is now led by CEO John Lewis from Floor 5, 55 King William St, London EC4R 9AD, and is backed with £100m by Zouk Capital through the UK Government-backed Charging Infrastructure Investment Fund. Its own about page claims over 5,000 charge points and 28.3 million kg of CO2 saved, and its live open data feed returned an x-total-count of 5,409 locations on 2026-07-27. In the UK energy value chain it sits at the very end of the wire: it is not a licensed supplier, not a network operator and not a metering agent, it operates charge points on street furniture owned by local authorities — Haringey, Southwark,
  Brent, Barnet, Harrow, Coventry, Brighton and Hove, Richmond and Wandsworth, Enfield and others — authorising drivers, metering the session and pricing it. Britain has no consumer data-portability mandate for energy equivalent to Australia''s Consumer Data Right, so nothing compels char.gy to expose an individual driver''s usage or billing data through an API, and it does not: there is no consumer API, no OAuth server, no OpenID Connect discovery document and no accredited-recipient scheme anywhere on the domain. What Britain DID mandate here is open infrastructure data. The Public Charge Point Regulations 2023 (SI 2023/1168), Part 4 regulation 10(5), require every charge point operator to make reference data and availability data available to the public free of charge, in a machine readable format, and — the crucial clause — "without any requirement to agree to terms and conditions regarding the use of that data". char.gy complies, and the compliance is real rather than claimed: it publishes
  an OCPI-shaped Locations feed and an OCPI-shaped Tariffs feed at https://char.gy/open-ocpi/locations and https://char.gy/open-ocpi/tariffs, both of which returned HTTP 200 with application/json to a completely anonymous GET on 2026-07-27, paginated with x-total-count, x-limit and RFC 5988 Link rel="next" headers, carrying real GB*CGY*E*NNNNN EVSE identifiers, IEC 62196 Type 2 connectors, per-connector tariff_ids and time-of-day restricted pence-per-kWh price components. The posture is therefore the clean split this sector keeps producing, but rotated: market and infrastructure data wide open and genuinely ungated because a regulation forbids gating it, consumer data entirely absent because no regulation asks for it, and the commercial OCPI CPO roaming interface at /ocpi/cpo/ closed behind OCPI Token authorization for partner e-mobility service providers. There is no developer portal — the entire public documentation for the open API is a single Freshdesk help-centre article.'
examples:
- key_count: 4
  name: Chargy Locations Response
  slug: chargy-locations-response
- key_count: 4
  name: Chargy Tariffs Response
  slug: chargy-tariffs-response
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chargy.png
layout: provider
mcp_servers:
- description: char.gy operates NO Model Context Protocol server. mcp.char.gy does not resolve, https://char.gy/mcp returns 404, and a search of the public MCP registry (registry.modelcontextprotocol.io) for "char.g
  name: char.gy MCP Server
  slug: chargy-mcp-server
modified: '2026-07-27'
name: char.gy
nav: Providers
network: true
overview: 'char.gy publishes 1 API on the [APIs.io](https://apis.io/) network: Open Charge Point Data API. Tagged areas include Energy, United Kingdom, EV Charging, Electricity, and Utilities.


  char.gy''s developer surface includes authentication, documentation, pricing, engineering blog, support, signup flow, and 22 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 47.9
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 30.3
    contract_quality: 55.9
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 2.6
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 58.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chargy/refs/heads/main/screenshots/chargy-2026-08-07T163259.png
security:
- kind: authentication
  name: Chargy Authentication
  slug: chargy-authentication
  summary_line: none/http · 2 schemes
- kind: domain-security
  name: Chargy Domain Security
  slug: chargy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chargy
tags:
- Energy
- United Kingdom
- EV Charging
- Electricity
- Utilities
- OCPI
- Charge Point Operator
- Open Data
- Roaming
- Tariffs
- Mobility
- Electrification
website: https://char.gy/
---
