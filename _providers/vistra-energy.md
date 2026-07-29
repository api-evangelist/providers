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
  url: security/vistra-energy-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vistra-energy-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vistra-energy-llms.txt
- group: other
  title: ''
  type: DiscoveryProbe
  url: well-known/vistra-energy-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.vistracorp.com/
- group: company
  title: ''
  type: About
  url: https://vistracorp.com/about/
- group: other
  title: ''
  type: Retail
  url: https://vistracorp.com/retail/
- group: other
  title: ''
  type: Sustainability
  url: https://vistracorp.com/sustainability/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.vistracorp.com/
- group: company
  title: ''
  type: Blog
  url: https://vistracorp.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://vistracorp.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vistracorp.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vistracorp.com/terms-of-use/
- group: build
  title: ''
  type: CodeOfConduct
  url: https://vistracorp.com/code-of-conduct/
- group: other
  title: ''
  type: CorporateGovernance
  url: https://vistracorp.com/corporate-governance/
- group: other
  title: ''
  type: Reporting
  url: https://vistracorp.com/sustainability/reporting/
- group: company
  title: ''
  type: Careers
  url: https://vistracorp.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vistra-energy
- group: operate
  title: ''
  type: LegislativeHub
  url: https://hub.vistracorp.com/our-companies/
- group: other
  title: ''
  type: RetailBrand
  url: https://www.txu.com/
- group: other
  title: ''
  type: RetailBrand
  url: https://www.dynegy.com/
- group: other
  title: ''
  type: RetailBrand
  url: https://www.ambitenergy.com/
- group: other
  title: ''
  type: RetailBrand
  url: https://www.homefieldenergy.com/
- group: other
  title: ''
  type: RetailBrand
  url: https://www.trieagleenergy.com/
- group: start
  title: ''
  type: CustomerPortal
  url: https://services.txu.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.txu.com/help
- group: docs
  title: ''
  type: Documentation
  url: https://www.txu.com/help/manage-usage/my-energy-dashboard
- group: docs
  title: ''
  type: Documentation
  url: https://www.txu.com/help/manage-usage/smart-meters
- group: other
  title: ''
  type: Standard
  url: https://www.energy.gov/data/green-button
- group: other
  title: ''
  type: ThirdPartyDataPlatform
  url: https://smartmetertexas.com/
created: '2026-07-27'
description: 'Vistra Corp (NYSE: VST) is an Irving, Texas integrated retail electricity and power generation company and the largest competitive power generator in the United States, operating roughly 41,000-44,000 MW of natural gas, nuclear, coal, solar and battery storage capacity alongside a retail business serving nearly 5 million residential, commercial and industrial customers across 16 states and the District of Columbia through TXU Energy, Dynegy, Ambit Energy, Energy Harbor, Homefield Energy and U.S. Gas & Electric. Its home market is the United States, where it sits on both sides of the competitive value chain, a merchant generator selling into ERCOT, PJM, ISO-NE, NYISO, MISO and CAISO, and a retail electricity provider (REP) reselling that power to end customers. Its API posture is honestly none. No developer portal, no API subdomain and no machine-readable contract of any kind was found: developer., developers., docs., api. and data. on vistracorp.com do not resolve; /developers,
  /api, /docs, /data, /openapi.json, /swagger.json and /.well-known/openid-configuration all return 404; and TXU Energy''s 758-URL sitemap contains no developer or API page. The United States has no consumer energy data mandate. Green Button is an NAESB/NIST ESPI standard adopted voluntarily, and TXU Energy appears on the US Department of Energy''s list of "Utilities Committed to Implementing Green Button", a 2012-era commitment list and not evidence of a live endpoint. The only customer-data surface found is Download-My-Data-style export behind the TXU Energy MyAccount login, whose interval readings are themselves sourced from Smart Meter Texas, the shared ERCOT meter-data platform operated by the transmission and distribution utilities (Oncor, CenterPoint, AEP Texas, TNMP) rather than by Vistra. Because Vistra is a retailer and generator and not a wires company, the third-party interval-data API in its home Texas market belongs to Smart Meter Texas and not to Vistra. Vistra likewise publishes
  no open market or grid data of its own; ERCOT, the other ISOs/RTOs and the EIA publish the market data about Vistra''s fleet. Both sides are therefore closed at the company boundary. Not to be confused with Vistra Limited (vistra.com), the unrelated corporate-services and fund-administration firm that does run a real API developer portal at devportal.vistra.com.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-27'
name: Vistra Corp
nav: Providers
network: true
overview: 'Vistra Corp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United States, Utilities, Electricity, and Natural Gas.


  Vistra Corp''s developer surface includes engineering blog, documentation, and 28 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 16.2
  delta: 2.2
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 14.0
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
  name: Vistra Energy Domain Security
  slug: vistra-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vistra-energy
tags:
- Energy
- United States
- Utilities
- Electricity
- Natural Gas
- Power Generation
- Retail Energy
- Smart Metering
- Green Button
- Energy Markets
- Nuclear
- Solar
- Battery Storage
- Texas
- ERCOT
website: https://www.vistracorp.com/
---
