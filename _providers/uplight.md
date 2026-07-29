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
api_count: 1
apis:
- description: Uplight markets a Developer Platform that exposes customer, program, eligibility, enrollment, device, and energy-flexibility data to utilities and ecosystem partners through APIs. The reference is pub
  name: Uplight Developer Platform API
  slug: uplight-developer-platform-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uplight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uplight.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.uplight.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.uplight.com/developer/reference
- group: company
  title: ''
  type: About
  url: https://uplight.com/about-us/
- group: other
  title: ''
  type: Platform
  url: https://uplight.com/platform/
- group: company
  title: ''
  type: Partners
  url: https://uplight.com/partners/
- group: company
  title: ''
  type: Blog
  url: https://uplight.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://uplight.com/blog/feed/
- group: company
  title: ''
  type: Press
  url: https://uplight.com/press/
- group: commercial
  title: ''
  type: Privacy
  url: https://uplight.com/privacy-policy/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uplight.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uplight.com/terms-of-service/
- group: other
  title: ''
  type: CookiePolicy
  url: https://uplight.com/cookie-policy/
- group: operate
  title: ''
  type: Contact
  url: https://uplight.com/contact-us/
- group: other
  title: ''
  type: Resources
  url: https://uplight.com/resources/
- group: auth
  title: ''
  type: Compliance
  url: https://uplight.com/resources/integrated-approach-security-privacy-compliance/
- group: design
  title: ''
  type: Conformance
  url: conformance/uplight-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uplight-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uplight-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Uplight-Inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uplight
created: '2026-07-27'
description: Uplight is a Boulder, Colorado energy technology company formed in 2019 from the merger of Tendril and Simple Energy and expanded through the acquisitions of EnergySavvy, FirstFuel, Ecotagious, EEme, and DERMS/VPP provider AutoGrid (closed February 2024). It sells software to electric and gas utilities and retailers in North America, Europe, and Asia rather than to consumers, covering energy efficiency and electrification marketplaces, home energy reports, rate engagement, demand response, distributed energy resource management (DERMS), virtual power plants, and a utility data lake with analytics. In the United States value chain Uplight sits on the utility side of the meter as a vendor and orchestration layer between the utility, its customers, and connected devices, and it publicly states support for OpenADR, IEEE 2030.5, Modbus, DNP3 and other SCADA protocols for DER control. Its API posture is honestly closed — a Developer Platform exists and is marketed to utilities and
  ecosystem partners, the documentation portal at docs.uplight.com serves a public landing shell but every Documentation and API Reference path redirects to a ReadMe login, and the production gateway at api.uplight.com answers anonymously only with HTTP 401 and a bearer-token error. No consumer usage-data API, no open market data, no downloadable OpenAPI, and no Green Button or ESPI reference could be found. Uplight is a software vendor, not a regulated data holder, so no consumer data mandate applies to it.
image: https://uplight.com/wp-content/uploads/2019/07/cropped-uplight-icon-1-192x192.png
layout: provider
modified: '2026-07-27'
name: Uplight
nav: Providers
network: true
overview: 'Uplight publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United States, Utilities, Electricity, and Gas.


  Uplight''s developer surface includes documentation, API reference, engineering blog, privacy policy, and 18 more developer resources.'
random_paper: 54
score:
  band: emerging
  composite: 22.0
  delta: 2.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 19.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 32.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Uplight Authentication
  slug: uplight-authentication
  summary_line: http-bearer · 1 scheme
- kind: domain-security
  name: Uplight Domain Security
  slug: uplight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uplight
tags:
- Energy
- United States
- Utilities
- Electricity
- Gas
- Demand Response
- DER
- Grid
- Virtual Power Plant
- DERMS
- Energy Efficiency
- Customer Engagement
website: https://uplight.com/
---
