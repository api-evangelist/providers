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
  url: security/fortisbc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fortisbc.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fortisbc
- group: company
  title: ''
  type: Blog
  url: https://www.fortisbc.com/about-us/news-events/stories
- group: start
  title: ''
  type: Login
  url: https://accounts.fortisbc.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.fortisbc.com/accounts/open-close-or-move-your-account/my-energy-use
- group: docs
  title: ''
  type: Documentation
  url: https://www.fortisbc.com/accounts/open-close-or-move-your-account/manage-your-online-account
- group: docs
  title: ''
  type: Documentation
  url: https://www.fortisbc.com/services/commercial-industrial-services/energy-efficiency-tools-for-natural-gas-business-customers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fortisbc.com/services/commercial-industrial-services/energy-efficiency-tools-for-natural-gas-business-customers/portfolio-manager-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fortisbc.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://outages.fortisbc.com/outages
- group: operate
  title: ''
  type: Support
  url: https://www.fortisbc.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FortisBC
- group: design
  title: ''
  type: Conformance
  url: conformance/fortisbc-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fortisbc-llms.txt
created: '2026-07-27'
description: 'FortisBC is a British Columbia energy utility and a subsidiary of Fortis Inc., delivering natural gas to more than 1,054,000 customers and electricity directly to close to 185,000 customers across the province''s Southern Interior, plus liquefied natural gas from the Tilbury and Mt. Hayes facilities, renewable natural gas, and EV charging. It sits at the regulated distribution tier of the value chain — the wires-and-pipes monopoly that meters the customer — under British Columbia Utilities Commission oversight, in a province with no wholesale electricity market and no consumer energy data right. Its API posture is honestly none: no developer portal, no published API, no OpenAPI, and no Green Button. British Columbia sits outside Ontario''s Green Button regulation (O. Reg. 633/21) and outside Australia''s Consumer Data Right, and the Green Button Alliance reports only "minor discussions of Green Button in British Columbia to-date". Consumer usage data is reachable only by the
  account holder through a SiteMinder-protected customer login at accounts.fortisbc.com, or — for commercial gas customers only — pushed into the US EPA''s ENERGY STAR Portfolio Manager via that platform''s data exchange, an arrangement FortisBC participates in rather than an API it publishes. No open market, grid, or system data is published. Consumer data closed, market data closed.'
image: https://www.fortisbc.com/App_Themes/Images/apple-touch-icon-152x152.png
layout: provider
modified: '2026-07-27'
name: FortisBC
nav: Providers
network: true
overview: 'FortisBC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Canada, Utilities, Electricity, and Natural Gas.


  FortisBC''s developer surface includes engineering blog, documentation, support, and 12 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 18.5
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fortisbc/refs/heads/main/screenshots/fortisbc-2026-08-07T165419.png
security:
- kind: domain-security
  name: Fortisbc Domain Security
  slug: fortisbc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fortisbc
tags:
- Energy
- Canada
- Utilities
- Electricity
- Natural Gas
- Gas Distribution
- Smart Metering
- Renewables
- EV Charging
- LNG
website: https://www.fortisbc.com/
---
