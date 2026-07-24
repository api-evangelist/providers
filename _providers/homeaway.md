---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: http://www.homeaway.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/homeaway
- group: auth
  title: ''
  type: Authentication
  url: authentication/homeaway-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/homeaway-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/homeaway-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/homeaway-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/homeaway-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/homeaway-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/homeaway-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/homeaway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.expediagroup.com/about/privacy-data-handling-requirements/
created: '2026-07-17'
description: 'HomeAway was an Austin, Texas vacation-rental marketplace that connected travelers with owners and property managers of holiday homes, cabins, condos, and beach houses worldwide. It published a first-party HomeAway API (OAuth 2.0) for listing management, availability and booking synchronization, pricing, and guest communication, along with a Ruby SDK and the hacurl command-line tool from its GitHub organization. HomeAway was acquired by Expedia Group in 2015 and the brand was retired into Vrbo: homeaway.com now redirects to Vrbo and the developer platform is no longer maintained. This profile captures the genuine historical first-party API surface (SDK, CLI, OAuth auth model) that remains publicly available.'
image: https://avatars.githubusercontent.com/u/349558?v=4
layout: provider
modified: '2026-07-19'
name: HomeAway *
nav: Providers
network: true
overview: 'HomeAway * is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Vacation Rentals, Travel, and Hospitality.


  HomeAway *''s developer surface includes authentication, CLI, and 9 more developer resources.'
random_paper: 43
score:
  band: minimal
  composite: 13.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 13.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Homeaway Authentication
  slug: homeaway-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Homeaway Domain Security
  slug: homeaway-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Homeaway Vulnerability Disclosure
  slug: homeaway-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: homeaway
tags:
- Company
- Consumer
- Vacation Rentals
- Travel
- Hospitality
- Marketplace
- Bookings
- Property Management
website: http://www.homeaway.com/
---
