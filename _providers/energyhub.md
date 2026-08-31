---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: Mercury Edge Connect is EnergyHub's standardized integration framework for connecting DER providers (thermostat, battery, EV, EV charger, and solar inverter manufacturers) to the Mercury/Edge DERMS pl
  name: EnergyHub Mercury Edge Connect API
  slug: mercury-edge-connect-api
- description: The Marketplace API integrates the Mercury/Edge DERMS platform with utility marketplace providers and online retailers so that a consumer buying a DER device can be pre-enrolled in a utility demand-re
  name: EnergyHub Marketplace API
  slug: marketplace-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/energyhub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/energyhub-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/energyhub-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/energyhub-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/energyhub-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/energyhub-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.energyhub.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.energyhub.com/home/en-us/
- group: other
  title: ''
  type: Platform
  url: https://www.energyhub.com/edge-derms-platform/platform-overview
- group: company
  title: ''
  type: Partners
  url: https://www.energyhub.com/der-partner-ecosystem
- group: start
  title: ''
  type: Signup
  url: https://www.energyhub.com/der-partner-ecosystem/become-a-partner
- group: company
  title: ''
  type: Blog
  url: https://www.energyhub.com/news-announcements
- group: company
  title: ''
  type: About
  url: https://www.energyhub.com/company
- group: company
  title: ''
  type: Careers
  url: https://www.energyhub.com/careers
- group: operate
  title: ''
  type: Support
  url: https://www.energyhub.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.energyhub.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.energyhub.com/privacy-policy
- group: docs
  title: ''
  type: UserGuide
  url: https://help.energyhub.com/articles/chargingrewards/overview
- group: other
  title: ''
  type: Patents
  url: https://www.energyhub.com/patents
- group: other
  title: ''
  type: Resources
  url: https://www.energyhub.com/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/energyhub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/energyhub/
created: '2026-07-27'
description: 'EnergyHub is a Brooklyn, New York distributed energy resource management system (DERMS) vendor and an independent subsidiary of Alarm.com (Nasdaq ALRM), operating in its home market of the United States. Its Edge DERMS platform (formerly marketed as Mercury DERMS) lets electric utilities enroll, forecast, dispatch, and measure customer-owned distributed energy resources - smart thermostats, batteries, electric vehicles and EV chargers, solar inverters, and commercial and industrial loads - as virtual power plants, and the company says it has been running load control programs since 2009. EnergyHub sits squarely in the private middle layer of the energy value chain. It is not a utility, not a retailer, and not a market operator, so no consumer energy data mandate applies to it: there is no Green Button obligation, no Consumer Data Right designation, and no Ontario regulation in play. Its API posture is honestly partner-only and entirely undocumented in public. Two APIs are publicly
  announced by the company - the Mercury Edge Connect API, which EnergyHub states is "based on the Open ADR standard", and a Marketplace API for demand-response pre-enrollment at the device point of sale - but neither has public reference documentation, a published base URI, a schema, or a self-serve signup. The knowledge base at help.energyhub.com serves a public landing page while every technical guide and device-partner integration article behind it is gated by an Okta SSO login. A live host at mec.energyhub.com answers TLS with a valid DigiCert certificate and rejects every anonymous request with "400 No required SSL certificate was sent", which is mutual-TLS client-certificate enforcement rather than a public API. No consumer usage or billing data API exists for third parties, and no open grid or market data is published, so EnergyHub is closed on both the consumer-data and the market-data axis, and a developer gets in only by signing a commercial or DER partner agreement.'
image: https://ez7jkrb8oox.exactdn.com/app/uploads/2024/10/favicon.png
layout: provider
modified: '2026-07-27'
name: EnergyHub
nav: Providers
network: true
overview: 'EnergyHub publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United States, Utilities, Electricity, and Grid.


  EnergyHub''s developer surface includes authentication, documentation, signup flow, engineering blog, support, and 17 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/energyhub/refs/heads/main/screenshots/energyhub-2026-08-07T164917.png
security:
- kind: authentication
  name: Energyhub Authentication
  slug: energyhub-authentication
  summary_line: mutualTLS · 2 schemes
- kind: domain-security
  name: Energyhub Domain Security
  slug: energyhub-domain-security
  summary_line: TLSv1.3 · DMARC
slug: energyhub
tags:
- Energy
- United States
- Utilities
- Electricity
- Grid
- DERMS
- Distributed Energy Resources
- Demand Response
- Virtual Power Plant
- OpenADR
- EV Charging
- Solar
- Energy Storage
- Smart Thermostats
website: https://www.energyhub.com/
---
