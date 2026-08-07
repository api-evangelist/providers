---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
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
  score: 9.0
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nova-scotia-power-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nova-scotia-power-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nova-scotia-power-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nova-scotia-power-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nova-scotia-power-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nova-scotia-power-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.nspower.ca/
- group: company
  title: ''
  type: About
  url: https://www.nspower.ca/about-us/who-we-are
- group: other
  title: ''
  type: GreenButton
  url: https://www.nspower.ca/cleanandgreen/innovation
- group: start
  title: ''
  type: Portal
  url: https://greenbutton.nspower.ca/
- group: auth
  title: ''
  type: Authentication
  url: https://accounts.nspower.ca/
- group: start
  title: ''
  type: CustomerPortal
  url: https://myaccount.nspower.ca/
- group: other
  title: ''
  type: OpenData
  url: https://www.nspower.ca/oasis
- group: other
  title: ''
  type: OpenData
  url: https://oasis.nspower.ca/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nspower.ca/oasis/monthly-reports
- group: docs
  title: ''
  type: Documentation
  url: https://www.nspower.ca/oasis/system-reports-messages
- group: docs
  title: ''
  type: Documentation
  url: https://www.nspower.ca/oasis/distribution-hosting-capacity
- group: other
  title: ''
  type: OpenData
  url: https://www.nspower.ca/oasis/forecasts-assessments
- group: other
  title: ''
  type: OpenData
  url: https://www.nspower.ca/oasis/wholesale-market-documents
- group: other
  title: ''
  type: OpenData
  url: https://www.nspower.ca/oasis/standards-codes
- group: other
  title: ''
  type: OpenData
  url: https://www.nspower.ca/oasis/transmission-customer-procedures
- group: other
  title: ''
  type: OpenData
  url: https://www.nspower.ca/oasis/generation-interconnection-procedures
- group: other
  title: ''
  type: OpenData
  url: https://www.nspower.ca/oasis/regulatory-documents
- group: other
  title: ''
  type: Regulatory
  url: https://www.nspower.ca/about-us/regulations/regulatory-initiatives
- group: other
  title: ''
  type: Regulation
  url: https://nslegislature.ca/legc/bills/64th_1st/3rd_read/b145.htm
- group: other
  title: ''
  type: Standard
  url: https://www.greenbuttonalliance.org/canadian-initiatives
- group: commercial
  title: ''
  type: Legal
  url: https://www.nspower.ca/legal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nspower.ca/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nspower.ca/privacy-statement
- group: operate
  title: ''
  type: Support
  url: https://www.nspower.ca/customer-service
- group: company
  title: ''
  type: Blog
  url: https://www.nspower.ca/about-us/articles
- group: company
  title: ''
  type: News
  url: https://www.nspower.ca/about-us/press-releases
- group: company
  title: ''
  type: Careers
  url: https://www.nspower.ca/about-us/careers
- group: other
  title: ''
  type: OutageMap
  url: https://outagemap.nspower.ca/
created: '2026-07-27'
description: 'Nova Scotia Power Incorporated (NSPI) is the investor-owned, vertically integrated regulated electric utility serving roughly half a million customers across Nova Scotia, Canada. A subsidiary of Halifax-based Emera Inc., it owns generation, transmission and distribution and is regulated by the Nova Scotia Energy and Regulatory Boards Tribunal (formerly the NSUARB). It sits at the retail end of the value chain as a franchise monopoly rather than a competitor in an open market — Nova Scotia has no wholesale market equivalent to IESO or AESO. Its API posture is the sharpest mandate-versus-implementation split in Canadian energy: section 4F of the Electricity Act, added by Bill 145 (SNS 2022, c. 12), legally required NSPI to implement the NAESB ESPI standard and be certified by the Green Button Alliance to BOTH "Connect My Data" and "Download My Data" on or before April 1, 2023. As of July 2026 the Green Button Alliance lists NSPI as certified to ESPI v3.3 for Download My Data
  only, with Connect My Data certification still "planned", and NSPI''s own site states the Green Button Marketplace "is currently closed" to third-party applications. There is no developer portal, no published OpenAPI, no OAuth registration and no documented consumer data API — greenbutton.nspower.ca is live but every path redirects to a SAML customer login. By contrast NSPI is genuinely open on market and system data: its OASIS site publishes hourly net energy flow reports as anonymously downloadable CSV going back to 2012. Open market data, closed consumer data, and a statutory mandate whose API half is three years past its deadline.'
image: https://nspower.ca/images/default-source/default-album/brand/nsp-favicon.png
layout: provider
modified: '2026-07-27'
name: Nova Scotia Power
nav: Providers
network: true
overview: 'Nova Scotia Power is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Canada, Utilities, Electricity, and Energy Retailer.


  Nova Scotia Power''s developer surface includes authentication, developer portal, documentation, legal docs, support, engineering blog, product news, and 27 more developer resources.'
random_paper: 31
score:
  band: emerging
  composite: 21.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 21.7
  provenance:
    conformance: first-party
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
- kind: authentication
  name: Nova Scotia Power Authentication
  slug: nova-scotia-power-authentication
  summary_line: saml2 · 1 scheme
- kind: domain-security
  name: Nova Scotia Power Domain Security
  slug: nova-scotia-power-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nova-scotia-power
tags:
- Energy
- Canada
- Utilities
- Electricity
- Energy Retailer
- Green Button
- Smart Metering
- Grid
- Renewables
- Solar
- EV Charging
- Energy Markets
- Regulation
website: https://www.nspower.ca/
---
