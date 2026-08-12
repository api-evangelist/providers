---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
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
  score: 11.7
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: 'The OpenID Connect / OAuth 2.0 identity provider behind Good Energy''s customer hub at account.goodenergy.co.uk. It is NOT a developer-facing API and Good Energy publishes no documentation for it — it '
  name: Good Energy Customer Identity (OpenID Connect)
  slug: good-energy-customer-identity-openid-connect
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/good-energy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/good-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.goodenergy.co.uk/
- group: company
  title: ''
  type: Blog
  url: https://www.goodenergy.co.uk/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.goodenergy.co.uk/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/goodenergyuk
- group: other
  title: ''
  type: SignIn
  url: https://account.goodenergy.co.uk/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/good-energy-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.goodenergy.co.uk/.well-known/security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/good-energy-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/good-energy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/good-energy-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/good-energy-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/good-energy-llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://www.goodenergy.co.uk/good-energy-tariffs/
- group: start
  title: ''
  type: SignUp
  url: https://www.goodenergy.co.uk/join/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goodenergy.co.uk/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goodenergy.co.uk/privacy-policy/
- group: company
  title: ''
  type: Partners
  url: https://www.goodenergy.co.uk/partners/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.goodenergy.co.uk/investors/
- group: operate
  title: ''
  type: Support
  url: https://www.goodenergy.co.uk/help/
created: '2026-07-27'
description: 'Good Energy is a British renewable energy supplier and green-technology installer founded in 1999 and headquartered in Chippenham, Wiltshire, acquired outright by Abu Dhabi based Esyasoft Investment Holding in March 2025 for GBP 99.4 million. It sits on the retail edge of the GB electricity value chain: a licensed supplier buying 100% renewable power directly from more than 2,000 British generators, the largest voluntary administrator of the Feed-in Tariff, an export/Smart Export Guarantee counterparty, and an installer of solar, batteries, heat pumps and EV chargers. Its API posture is honest and thin. The United Kingdom mandated smart-metering INFRASTRUCTURE, not a consumer data right: Good Energy is a Balancing and Settlement Code and Retail Energy Code party operating DCC-adopted SMETS2 smart meters — verified through an Ofgem regulatory-sandbox decision naming Good Energy Ltd and through Elexon BSC modification P459, which Good Energy itself raised to allow different supplier
  agents on import and export MSIDs where DCC-adopted smart meters are installed. That obligation produces no public API whatsoever. There is no UK equivalent of the Australian Consumer Data Right binding Good Energy, no Green Button, and no accredited-recipient scheme. No developer portal exists (developer., developers., docs. and data. subdomains do not resolve; /developers, /api and /docs return 404). Both sides are closed: consumer usage and billing data are reachable only by the account holder through the login-gated customer hub, and no open grid or market data is published — GB open energy data comes from NESO, Elexon and the DNOs, not from the supplier. The single machine-readable API artifact Good Energy exposes anonymously is the OpenID Connect discovery document of its customer-login identity provider.'
image: https://www.goodenergy.co.uk/wp-content/uploads/2021/11/cropped-good-energy-favicon-192x192.png
layout: provider
modified: '2026-07-27'
name: Good Energy
nav: Providers
network: true
overview: 'Good Energy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Gas.


  Good Energy''s developer surface includes engineering blog, authentication, pricing, signup flow, support, and 16 more developer resources.'
random_paper: 76
scopes:
- name: Good Energy Scopes
  scope_count: 6
  slug: good-energy-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials/implicit/deviceCode/ciba
score:
  band: thin
  composite: 28.2
  delta: -1.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 10.5
  previous_composite: 29.2
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/good-energy/refs/heads/main/screenshots/good-energy-2026-08-07T165801.png
security:
- kind: authentication
  name: Good Energy Authentication
  slug: good-energy-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Good Energy Domain Security
  slug: good-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Good Energy Vulnerability Disclosure
  slug: good-energy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: good-energy
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Renewables
- Smart Metering
- Solar
- EV Charging
- Energy Retail
website: https://www.goodenergy.co.uk/
---
