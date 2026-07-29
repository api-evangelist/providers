---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: N2Yo Agentic Access
  operation_count: 5
  slug: n2yo-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: Satellites currently above an observer location.
  name: N2YO Above API
  slug: n2yo-above-api
- description: Future satellite positions over an observer location.
  name: N2YO Positions API
  slug: n2yo-positions-api
- description: Radio-communication satellite pass predictions.
  name: N2YO Radio Passes API
  slug: n2yo-radio-passes-api
- description: Two-Line Element data for satellites.
  name: N2YO TLE API
  slug: n2yo-tle-api
- description: Optically visible satellite pass predictions.
  name: N2YO Visual Passes API
  slug: n2yo-visual-passes-api
artifact_total: 12
collections:
- collection_type: open
  name: N2YO Satellite Tracking API
  slug: open-n2yo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/n2yo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/n2yo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/n2yo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/n2yo
- group: company
  title: ''
  type: Website
  url: https://www.n2yo.com/
- group: start
  title: ''
  type: Signup
  url: https://www.n2yo.com/login/register/
- group: start
  title: ''
  type: Login
  url: https://www.n2yo.com/login/
- group: operate
  title: ''
  type: Contact
  url: https://www.n2yo.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.n2yo.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.n2yo.com/terms/
created: '2024-03-30'
description: N2YO.com is a website that provides real-time tracking and information about satellites and space stations using space surveillance data from Space Track, operated by the US Air Force Space Command.
finops:
- name: N2Yo Finops
  service_category: API
  slug: n2yo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/n2yo.png
layout: provider
modified: '2026-05-19'
name: N2YO
nav: Providers
network: true
overview: 'N2YO publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Above API, Positions API, Radio Passes API, and 2 more. Tagged areas include Satellites, Space, and Tracking.


  N2YO''s developer surface includes authentication, signup flow, and 8 more developer resources.'
plans:
- name: N2Yo Plans Pricing
  plan_count: 3
  slug: n2yo-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 5
  name: N2Yo Rate Limits
  slug: n2yo-rate-limits
score:
  band: developing
  composite: 42.2
  delta: -0.7
  facets:
    commercial_clarity: 73.7
    contract_quality: 56.8
    developer_ergonomics: 10.9
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/n2yo/refs/heads/main/screenshots/n2yo-2026-06-20T185921.png
security:
- kind: authentication
  name: N2Yo Authentication
  slug: n2yo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: N2Yo Domain Security
  slug: n2yo-domain-security
  summary_line: TLSv1.2 · DMARC
slug: n2yo
tags:
- Satellites
- Space
- Tracking
website: https://www.n2yo.com/
---
