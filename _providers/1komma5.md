---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 40
  human_in_the_loop: 0
  name: 1Komma5 Agentic Access
  operation_count: 73
  slug: 1komma5-agentic-access
  summary_line: 73 operations · 40 acting
api_count: 2
apis:
- description: 'The Offer Tool API backs 1KOMMA5°''s sales configuration and quoting workflow — customers and sites, product and pricebook catalogues, concepts, effective-price simulation for the German market, offer '
  name: 1KOMMA5° Offer Tool API
  slug: 1komma5-offer-tool-api
- description: The Heartbeat API is the customer-facing energy API behind the 1KOMMA5° mobile apps and the Heartbeat AI platform — sites and systems, live power snapshots for PV, battery, heat pump and EV charger, e
  name: 1KOMMA5° Heartbeat API
  slug: 1komma5-heartbeat-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/1komma5-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1komma5-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1komma5.com/en/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/1komma5-stock
- group: operate
  title: ''
  type: Support
  url: https://1komma5.com/en/about-us/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.1komma5.com.au/
- group: company
  title: ''
  type: Blog
  url: https://1komma5.com/en/press/press-releases/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://1komma5.com/de/legal/agb/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://1komma5.com/en/legal/privacy-policy/
- group: other
  title: ''
  type: Imprint
  url: https://1komma5.com/en/legal/imprint/
- group: company
  title: ''
  type: Careers
  url: https://1komma5.com/en/about-us/jobs/
- group: auth
  title: ''
  type: Security
  url: https://1komma5.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/1komma5-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/1komma5-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/1komma5-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/1komma5-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/1komma5-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/1komma5-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/1komma5-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/1komma5-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/1komma5-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/1komma5-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/1komma5-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/1komma5-packages.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/1komma5-vulnerability-disclosure.yml
created: '2026-08-02'
description: '1KOMMA5° (1Komma5 Grad) is a Hamburg, Germany headquartered smart-energy company that sells, installs and operates integrated residential energy systems — rooftop photovoltaics, battery storage, heat pumps and EV charging — and ties them together with Heartbeat AI, its energy-management platform. Heartbeat aggregates customer hardware into one of Europe''s largest residential virtual power plants, optimising self-consumption and trading household flexibility against day-ahead and intraday electricity markets. The company operates across Germany, Australia, the Netherlands, Sweden, Finland, Denmark and Belgium. Its machine-readable surface is small and mostly internal: a live OpenAPI 3.0 for the Offer Tool API used by its sales and partner network, an Auth0-backed OIDC provider at auth.1komma5grad.com, and the undocumented Heartbeat customer API that its mobile apps and community-built Home Assistant integrations consume.'
image: https://1komma5.com/icon.svg
layout: provider
modified: '2026-08-02'
name: 1KOMMA5°
nav: Providers
network: true
overview: '1KOMMA5° publishes 1 API on the [APIs.io](https://apis.io/) network: Offer Tool API. Tagged areas include Company, Energy, Solar, Renewable Energy, and Smart Home.


  1KOMMA5°''s developer surface includes support, engineering blog, authentication, and 23 more developer resources.'
random_paper: 65
scopes:
- name: 1Komma5 Scopes
  scope_count: 14
  slug: 1komma5-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: thin
  composite: 35.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 43.4
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: 1Komma5 Authentication
  slug: 1komma5-authentication
  summary_line: openIdConnect/oauth2/http · 3 schemes
- kind: domain-security
  name: 1Komma5 Domain Security
  slug: 1komma5-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: 1Komma5 Vulnerability Disclosure
  slug: 1komma5-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: 1komma5
tags:
- Company
- Energy
- Solar
- Renewable Energy
- Smart Home
- Electric Vehicles
- Heat Pumps
- Virtual Power Plant
- Energy Management
- Germany
website: https://1komma5.com/en/
---
