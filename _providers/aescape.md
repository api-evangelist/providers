---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.aescape.com/
- group: company
  title: ''
  type: About
  url: https://www.aescape.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.aescape.com/news
- group: company
  title: ''
  type: Press
  url: https://www.aescape.com/press
- group: operate
  title: ''
  type: Support
  url: https://www.aescape.com/faqs
- group: operate
  title: ''
  type: Contact
  url: https://www.aescape.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aescape.com/sessions
- group: start
  title: ''
  type: SignUp
  url: https://app.aescape.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aescape.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aescape.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aescape-inc
- group: company
  title: ''
  type: Partners
  url: https://www.aescape.com/partner
- group: company
  title: ''
  type: Careers
  url: https://www.aescape.com/careers
- group: other
  title: ''
  type: Technology
  url: https://www.aescape.com/technology
- group: other
  title: ''
  type: Locations
  url: https://app.aescape.com/map
- group: other
  title: ''
  type: Store
  url: https://store.aescape.com/
- group: docs
  title: ''
  type: Manual
  url: https://www.aescape.com/manual
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aescape-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aescape-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aescape-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/aescape-openid-configuration.json
- group: design
  title: ''
  type: Conformance
  url: conformance/aescape-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aescape-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aescape-llms.txt
created: '2026-07-31'
description: 'Aescape is a New York City lifestyle-robotics company, founded in 2017 by Eric Litman, that builds a fully automated AI-powered robotic massage platform. Its table uses sensors and computer vision to map over one million 3D data points of a person''s body, then drives heated robotic arms through massage techniques at a user-selected pressure, duration and focus area, with sessions booked and controlled through a mobile/web app. Sessions run 15 to 60 minutes and the tables are deployed in Equinox clubs, Four Seasons, Marriott and Ritz-Carlton properties, spas and corporate wellness sites across North America, alongside an Aescape One home product. Aescape publishes no public developer API: its consumer app is served by a private AWS API Gateway host (api.aescape.com) and its developer documentation site (developer.aescape.com) is gated behind HTTP Basic auth. The one machine-readable, anonymously reachable contract Aescape does publish is the OpenID Connect discovery document
  for its Zitadel identity tenant.'
image: https://aescape-assets.b-cdn.net/_1200x630_crop_center-center_82_none/Garrett-Table-Hero.jpg?mtime=1708106180
layout: provider
modified: '2026-07-31'
name: Aescape
nav: Providers
network: true
overview: 'Aescape is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Health and Wellness, Fitness, and Massage.


  Aescape''s developer surface includes engineering blog, support, pricing, signup flow, authentication, and 19 more developer resources.'
random_paper: 57
scopes:
- name: Aescape Scopes
  scope_count: 6
  slug: aescape-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials/deviceCode/implicit
score:
  band: emerging
  composite: 21.5
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 5.3
  provenance:
    conformance: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Aescape Authentication
  slug: aescape-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Aescape Domain Security
  slug: aescape-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aescape
tags:
- Company
- Robotics
- Health and Wellness
- Fitness
- Massage
- Artificial Intelligence
- Consumer Hardware
- Hospitality
- Recovery
- Identity
website: https://www.aescape.com/
---
