---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The OpenID Connect / OAuth 2.0 authorization server that authenticates E.ON Next customers into the online account and mobile app. It is an Auth0-hosted E.ON group CIAM tenant (certificate CN eon-next
  name: E.ON Next Customer Identity (OpenID Connect)
  slug: identity
artifact_total: 5
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eon-next-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/eon-next-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/eon-next-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/eon-next-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eon-next-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eon-next-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/eon-next-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.eonnext.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eon-next-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eonnext.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/e-on-next
- group: company
  title: ''
  type: Blog
  url: https://www.eonnext.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.eonnext.com/help
- group: operate
  title: ''
  type: Forum
  url: https://community.eonnext.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eonnext.com/tariffs
- group: company
  title: ''
  type: About
  url: https://www.eonnext.com/about
- group: start
  title: ''
  type: Login
  url: https://www.eonnext.com/dashboard/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eonnext.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eonnext.com/privacy
created: '2026-07-27'
description: 'E.ON Next Energy Limited is the United Kingdom retail supply arm of the E.ON Group, formed after E.ON''s 2019 acquisition of npower and serving roughly five million British households and small businesses with electricity, gas, smart meters, solar, home batteries, heat pumps and EV charging tariffs. It sits at the retail end of the GB energy value chain — buying wholesale, settling through Elexon, reading SMETS2 smart meters over the licensed Smart DCC network, and billing the customer — and it runs its entire operation on Kraken, the API-first, GraphQL-based energy operating system licensed from Kraken Technologies (Octopus Energy Group), onto which 5.8 million customers were migrated between June 2020 and June 2022. Its API posture is the exact opposite of its platform''s reputation: the Kraken architecture underneath is API-first, but almost nothing is published outward. There is no developer portal, no API documentation, no OpenAPI, and no third-party route to a customer''s
  usage or billing data; developer.eonnext.com and docs.eonnext.com do not resolve, and both api.eonnext.com and data.eonnext.com answer every path with an unauthenticated AWS API Gateway 403 "Missing Authentication Token". The one machine-readable contract E.ON Next does publish is its customer identity layer — auth.eonnext.com, an Auth0 CIAM tenant, serves a complete anonymous OpenID Connect / RFC 8414 discovery document and JWKS — which describes how a customer signs in, not how a developer gets access. Britain mandated the metering infrastructure, not the data right: E.ON Next is bound by the Smart Energy Code and the DCC, which is live and implemented, but no consumer data-portability mandate equivalent to Australia''s CDR or Ontario''s Green Button applies to it, and none of the open GB market data (NESO Carbon Intensity, Elexon BSC, DNO open-data portals) originates here. Consumer data is closed, market data is published by other parties, and the only public contract is identity.'
image: https://images.ctfassets.net/fxmb2pqc184n/5oYVaG0Ukc9ErXnwbIcXe8/c18e22523f4b37a96b9b41997100ad8c/social-logo.png
layout: provider
modified: '2026-07-27'
name: E.ON Next
nav: Providers
network: true
overview: 'E.ON Next publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Gas.


  E.ON Next''s developer surface includes authentication, engineering blog, support, pricing, and 15 more developer resources.'
random_paper: 76
scopes:
- name: Eon Next Scopes
  scope_count: 14
  slug: eon-next-scopes
  summary_line: 14 scopes · authorizationCode/implicit/clientCredentials/deviceCode
score:
  band: thin
  composite: 30.1
  delta: 7.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 23.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Eon Next Authentication
  slug: eon-next-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Eon Next Domain Security
  slug: eon-next-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Eon Next Vulnerability Disclosure
  slug: eon-next-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: eon-next
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Smart Metering
- Energy Retail
- Kraken
- Solar
- EV Charging
- Identity
website: https://www.eonnext.com/
---
