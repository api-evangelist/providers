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
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blink-charging-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blinkcharging.com
- group: company
  title: ''
  type: Blog
  url: https://blinkcharging.com/blog
- group: company
  title: ''
  type: News
  url: https://blinkcharging.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blinkcharging.com/legal/blink-network-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blinkcharging.com/legal/privacy-policy
- group: other
  title: ''
  type: OpenData
  url: https://blinkcharging.com/en-gb/getintouch/blink-open-data-request
- group: operate
  title: ''
  type: Support
  url: https://blinkcharging.com/getintouch/driver-support
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blinkcharging
- group: other
  title: ''
  type: X
  url: https://twitter.com/BlinkCharging
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blinkcharging
- group: start
  title: ''
  type: Login
  url: https://host.blinknetwork.com/
- group: operate
  title: ''
  type: Contact
  url: https://blinkcharging.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://blinkcharging.com/charge/driver-faq
- group: operate
  title: ''
  type: FAQ
  url: https://blinkcharging.com/host-a-station/host-faq
- group: company
  title: ''
  type: Careers
  url: https://blinkcharging.com/company/careers
- group: company
  title: ''
  type: Investors
  url: https://ir.blinkcharging.com/
- group: other
  title: ''
  type: Applications
  url: https://apps.apple.com/us/app/blink-charging-mobile-app/id1612678852
- group: other
  title: ''
  type: Applications
  url: https://play.google.com/store/apps/details?id=com.blinknetwork.mobile2
- group: auth
  title: ''
  type: Compliance
  url: https://blinkcharging.com/news/blink-charging-achieves-in-process-fedramp-status
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.blinkcharging.com
- group: design
  title: ''
  type: Conformance
  url: conformance/blink-charging-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blink-charging-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/blink-charging-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blink-charging-llms.txt
created: '2026-07-27'
description: 'Blink Charging Co. (Nasdaq BLNK) is a United States electric vehicle charging company headquartered at 17301 Melford Boulevard, Bowie, Maryland, with additional offices in California, the United Kingdom, Belgium and India. It designs and sells Level 2 and DC fast chargers (Series 7, 8 and 9, Shasta, the EQ/PQ line and the HYC DC fast chargers), owns and operates chargers under both owner-operator and host-owned business models, and runs the Blink Network - the proprietary cloud platform behind its host portal, driver mobile app and fleet management product. In the energy value chain Blink is a charge point operator and a load on the distribution grid, not a utility, retailer or system operator. It publishes no electricity usage, tariff, grid or market data of its own, and no consumer energy data right obligation applies to it in its home market of the United States - Green Button is a voluntary NAESB/NIST standard aimed at utilities, and Blink is not a utility. Its API posture
  is a closed door behind a live legal surface. The Blink Network Terms and Conditions, last modified 2 December 2025, explicitly govern "the Blink API" and state that use is "under your username", but no live developer portal, API reference, base URL or machine-readable contract is published anywhere on blinkcharging.com. The historical BlinkMap API developer page at prod.blinknetwork.com/developer.html - an application form gated by a Blink Network, LLC Data License Agreement - now refuses connections and was last archived in July 2021. The only live data-access surface Blink publishes is a United Kingdom open data request page citing the Public Charge Point Regulations 2023, where a Google Form request is reviewed by Blink''s data team, shared with the aggregator Eco-Movement and answered "in api format" - an application-approval gate, not an open feed. Blink''s real standards adoption sits below the API layer: OCPP 2.0.1 certification for its Series 7, 8 and 9 chargers announced September
  2025, and OpenADR 2.0 approval for the Blink Network announced March 2020 enabling utility load management across its charging network.'
image: https://a-us.storyblok.com/f/1016941/220x110/e14930a9c8/blink-logo.svg
layout: provider
modified: '2026-07-27'
name: Blink Charging
nav: Providers
network: true
overview: 'Blink Charging is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United States, EV Charging, Electric Vehicles, and Charging Stations.


  Blink Charging''s developer surface includes engineering blog, product news, support, FAQ, and 21 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 22.1
  delta: 3.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 18.7
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
  name: Blink Charging Authentication
  slug: blink-charging-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Blink Charging Domain Security
  slug: blink-charging-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Blink Charging Trust Center
  slug: blink-charging-trust-center
  summary_line: trust center published
slug: blink-charging
tags:
- Energy
- United States
- EV Charging
- Electric Vehicles
- Charging Stations
- Grid
- Demand Response
- Fleet Management
- OCPP
- OpenADR
- Roaming
website: https://blinkcharging.com
---
