---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: N3Rgy Agentic Access
  operation_count: 26
  slug: n3rgy-agentic-access
  summary_line: 26 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'The consent-scoped smart-meter data API of the n3rgy platform. A business holding a valid n3rgy API key lists the properties (MPxNs) it has active consent for, discovers which utilities (electricity, '
  name: n3rgy Customer Service API V2
  slug: customer-service-api-v2
artifact_total: 14
asyncapis:
- description: ''
  name: N3Rgy Push Notifications Webhooks
  slug: n3rgy-push-notifications-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/n3rgy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/n3rgy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/n3rgy-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.n3rgy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://customer-api-user-manuals.data.n3rgy.com/
- group: start
  title: ''
  type: SignUp
  url: https://data.n3rgy.com/business-sign-up
- group: start
  title: ''
  type: Login
  url: https://www.n3rgy.com/business-login/
- group: start
  title: ''
  type: Portal
  url: https://data.n3rgy.com/consumer-login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.n3rgy.com/business/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.n3rgy.com/wp-content/uploads/2023/04/N3rgyDataLimited.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.n3rgy.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.n3rgy.com/contact-us/
- group: company
  title: ''
  type: About
  url: https://www.n3rgy.com/about-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/n3rgy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://customer-api-user-manuals.data.n3rgy.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.n3rgy.com/support/home
- group: build
  title: ''
  type: Packages
  url: packages/n3rgy-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/n3rgy-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/n3rgy-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/n3rgy-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/n3rgy-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/n3rgy-changelog.yml
created: '2026-07-27'
description: 'n3rgy data limited is a United Kingdom smart-energy data platform, registered in England (No. 11712674) and owned by Smart Metering Systems Ltd. It sits between Great Britain''s mandated smart-metering infrastructure — the DCC network, SMETS2 home area networks (HANs), and the ESME/GSME electricity and gas meters behind them — and the organisations that want to read from it, letting a business collect consumption, production, and tariff data for a property (addressed by MPAN/MPRN, collectively MPxN) once the occupant has granted consent, without that business having to become a DCC user in its own right. Its API posture is public in documentation and closed in access: a genuinely anonymous MkDocs developer guide and a complete OpenAPI 3.0.1 contract for the Customer Service API V2 are served to anyone, while every operation is x-api-key gated and live keys must be enabled by the n3rgy back office after a business sign-up. Britain mandated the metering infrastructure, not a
  consumer data right, so nothing here is a Consumer Data Right or Green Button implementation — n3rgy publishes no open grid or market data at all, and the formerly public consumer API is, by the company''s own statement, no longer available.'
examples:
- key_count: 1
  name: N3Rgy Error Bad Request Example
  slug: n3rgy-error-bad-request-example
- key_count: 1
  name: N3Rgy Error Forbidden Example
  slug: n3rgy-error-forbidden-example
- key_count: 3
  name: N3Rgy Push Configuration Request Example
  slug: n3rgy-push-configuration-request-example
- key_count: 2
  name: N3Rgy Push Configuration Response Example
  slug: n3rgy-push-configuration-response-example
- key_count: 3
  name: N3Rgy Push Status Response Example
  slug: n3rgy-push-status-response-example
- key_count: 6
  name: N3Rgy Retrieve Consented Mpxns Empty Example
  slug: n3rgy-retrieve-consented-mpxns-empty-example
- key_count: 6
  name: N3Rgy Retrieve Consented Mpxns Example
  slug: n3rgy-retrieve-consented-mpxns-example
image: https://www.n3rgy.com/wp-content/uploads/2023/03/Group.png
layout: provider
mcp_servers:
- description: ''
  name: n3rgy-mcp.yml
  slug: n3rgy-mcpyml
modified: '2026-07-27'
name: n3rgy
nav: Providers
network: true
overview: 'n3rgy publishes 1 API on the [APIs.io](https://apis.io/) network: Customer Service API V2. Tagged areas include Energy, United Kingdom, Utilities, Smart Metering, and Electricity.


  The n3rgy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  n3rgy''s developer surface includes authentication, documentation, signup flow, developer portal, pricing, support, changelog, and 15 more developer resources.'
random_paper: 52
rate_limits:
- limit_count: 4
  name: N3Rgy Rate Limits
  slug: n3rgy-rate-limits
score:
  band: developing
  composite: 52.0
  delta: 5.6
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 16.7
    contract_quality: 62.9
    developer_ergonomics: 26.2
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 50.0
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    conformance: derived
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
    score: 60.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/n3rgy/refs/heads/main/screenshots/n3rgy-2026-08-07T184554.png
security:
- kind: authentication
  name: N3Rgy Authentication
  slug: n3rgy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: N3Rgy Domain Security
  slug: n3rgy-domain-security
  summary_line: TLSv1.3 · HSTS
slug: n3rgy
tags:
- Energy
- United Kingdom
- Utilities
- Smart Metering
- Electricity
- Gas
- Smart Meter Data
- Consent
- Metering
- Energy Data
website: https://www.n3rgy.com/
---
