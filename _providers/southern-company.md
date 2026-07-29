---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/southern-company-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/southern-company-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/southern-company-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/southern-company-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.southerncompany.com/
- group: company
  title: ''
  type: About
  url: https://www.southerncompany.com/about.html
- group: company
  title: ''
  type: Blog
  url: https://www.southerncompany.com/newsroom.html
- group: operate
  title: ''
  type: Support
  url: https://customerservice2.southerncompany.com/CustService/Overview?mnuOpco=GPC
- group: start
  title: ''
  type: Login
  url: https://customerservice2.southerncompany.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.southerncompany.com/contact-us.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.southerncompany.com/privacy-statement.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.southerncompany.com/terms-and-conditions.html
- group: company
  title: ''
  type: Investors
  url: https://investor.southerncompany.com/
- group: company
  title: ''
  type: Careers
  url: https://southerncompany.jobs/
- group: other
  title: ''
  type: Sustainability
  url: https://www.southerncompany.com/sustainability.html
- group: other
  title: ''
  type: Reports
  url: https://www.southerncompany.com/solutions/sustainability/data-downloads-reports.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/southern-company
created: '2026-07-27'
description: Southern Company is an Atlanta-headquartered energy holding company and one of the largest producers of electricity in the United States, serving approximately 9 million electric and natural gas customers through Alabama Power, Georgia Power, Mississippi Power, Southern Power, Southern Company Gas (Atlanta Gas Light, Nicor Gas, Virginia Natural Gas, Chattanooga Gas), Southern Nuclear, PowerSecure, Southern Linc and Southern Telecom. It sits at the vertically-integrated regulated-utility layer of the value chain — it owns generation, transmission and distribution, operates its own balancing authority rather than belonging to an ISO/RTO, and runs a FERC-approved bid-based energy auction for wholesale power in the Southeast. Its API posture is honestly closed on both sides of the sector's two-speed split. There is no consumer data mandate in Alabama, Georgia or Mississippi and Southern Company does not implement Green Button Download My Data or Connect My Data, is not listed by
  the Green Button Alliance, and publishes no ESPI endpoint — a customer can only export their own interval data as a spreadsheet after logging into My Power Usage, and a third party gets billing history only through a signed paper release form. On the market side the FERC-required auction clearing prices and weighted-average hour-ahead transaction prices are posted as public web pages, but they are JavaScript-rendered HTML with no CSV, no feed and no API behind them. A production Apigee API gateway is live at api.southernco.com and developer.southernco.com resolves behind an Imperva edge, so the platform machinery exists internally, but no proxy, no specification and no documentation are published to anyone outside the company.
image: https://www.southerncompany.com/etc.clientlibs/global/clientlibs/clientlib-site/resources/icon-192x192.png
layout: provider
modified: '2026-07-27'
name: Southern Company
nav: Providers
network: true
overview: 'Southern Company is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United States, Utilities, Electricity, and Gas.


  Southern Company''s developer surface includes engineering blog, support, and 15 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 16.9
  delta: 2.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 14.9
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Southern Company Domain Security
  slug: southern-company-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: southern-company
tags:
- Energy
- United States
- Utilities
- Electricity
- Gas
- Grid
- Smart Metering
- Nuclear
- Energy Markets
- Renewables
website: https://www.southerncompany.com/
---
