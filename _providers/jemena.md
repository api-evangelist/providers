---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Jemena Electricity Networks' CSIP-AUS compliant control server — an IEEE 2030.5 (Smart Energy Profile 2.0) implementation of the Common Smart Inverter Profile Australia (SA TS 5573) — used to discover
  name: Jemena CSIP-AUS Utility Server (IEEE 2030.5)
  slug: jemena-csip-aus-utility-server
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jemena-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jemena.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.jemena.com.au/electricity/solar-connections/victoria-emergency-backstop-mechanism/emergency-backstop-mechanism-documents/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jemena
- group: start
  title: ''
  type: SignUp
  url: https://myportal.jemena.com.au/
- group: start
  title: ''
  type: CustomerPortal
  url: https://myservices.jemena.com.au/edp/login/auth
- group: operate
  title: ''
  type: StatusPage
  url: https://poweroutages.jemena.com.au/
- group: operate
  title: ''
  type: Support
  url: https://www.jemena.com.au/help-support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jemena.com.au/about-us/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jemena.com.au/about-us/terms-of-use/
- group: company
  title: ''
  type: Blog
  url: https://www.jemena.com.au/about-us/news-media/
- group: auth
  title: ''
  type: Authentication
  url: authentication/jemena-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jemena-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jemena-error-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/jemena-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jemena-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jemena-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jemena-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jemena-llms.txt
created: '2026-07-27'
description: 'Jemena is an Australian energy infrastructure owner-operator, headquartered in Melbourne and owned by SGSP (Australia) Assets — 60% State Grid Corporation of China, 40% Singapore Power. It sits on the poles-and-pipes side of the value chain, not the retail side: it runs the Jemena Electricity Network distributing power to north and north-west Melbourne, the Jemena Gas Network distributing gas across New South Wales, the Eastern, Queensland and Northern Gas Pipelines, the Colongra storage facility, and holds 50% of ActewAGL''s ACT distribution networks. Its API posture is the inverse of what the Australian Consumer Data Right story would predict. Jemena is NOT a designated CDR energy data holder — the CDR energy designation covers retailers as primary data holders and AEMO as secondary data holder, and the live CDR Register energy brand list contains 84 brands, all of them retailers and none of them a distribution network. There is consequently no Jemena consumer usage or billing
  API, and the Electricity Outlook customer smart-meter portal no longer resolves in DNS. Jemena also publishes no open market or network data API; its outage map is CloudFront geo-restricted and its Daily Gas Data product is a paid annual email subscription. What Jemena does run is a real, live, standards-conformant machine-to-machine API for grid control: the JEN CSIP-AUS Utility Server, an IEEE 2030.5 / SEP2 implementation of the CSIP-AUS (SA TS 5573) profile, stood up to satisfy the Victorian Government''s emergency backstop mandate for remotely curtailable rooftop solar. It is fully documented in public PDF handbooks, has published staging and production base URIs, and is gated behind Jemena-issued mTLS PKI certificates, IP whitelisting and an OEM conformance-testing programme.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jemena.png
layout: provider
modified: '2026-07-27'
name: Jemena
nav: Providers
network: true
overview: 'Jemena publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Australia, Utilities, Electricity, and Gas.


  Jemena''s developer surface includes documentation, signup flow, support, engineering blog, authentication, sandbox, and 13 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 26.8
  delta: 2.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 24.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Jemena Authentication
  slug: jemena-authentication
  summary_line: mutualTLS · 2 schemes
- kind: domain-security
  name: Jemena Domain Security
  slug: jemena-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jemena
tags:
- Energy
- Australia
- Utilities
- Electricity
- Gas
- Grid
- Network Distributor
- DER
- Solar
- Smart Metering
- Demand Response
- IEEE 2030.5
website: https://www.jemena.com.au/
---
