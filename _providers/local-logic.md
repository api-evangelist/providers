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
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
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
  score: 9.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for location intelligence — location scores, neighborhood profiles, geographies, points of interest, demographics, schools, value drivers, similar neighborhoods, location snapshot, market sta
  name: Local Logic API
  slug: local-logic-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://locallogic.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.locallogic.co/
- group: operate
  title: ''
  type: Support
  url: https://support.locallogic.co/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://locallogic.co/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://locallogic.co/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://neighborhoodintel.locallogic.co/auth/signup
- group: start
  title: ''
  type: Login
  url: https://neighborhoodintel.locallogic.co/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://locallogic.co/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://locallogic.co/privacy-policy/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/LocalLogic
- group: auth
  title: ''
  type: Authentication
  url: authentication/local-logic-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/local-logic-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/local-logic-domain-security.yml
created: '2026-07-17'
description: Local Logic is a location intelligence platform for real estate, founded in 2015, that turns 100B+ data points across 250 million addresses in the US and Canada into 18 proprietary location scores, points of interest, demographics, school ratings, market statistics, value drivers, and climate-risk signals. Its REST API at api.locallogic.co exposes Location Scores, Profiles, Geographies, Points of Interest, Demographics, Schools, Value Drivers, Similar Neighborhoods, Location Snapshot, Market Statistics, and Climate Risk endpoints to real estate brokerages, portals, lenders, and proptech platforms, authenticated with a client ID and secret.
image: https://locallogic.co/wp-content/uploads/2023/01/local-logic-logo.png
layout: provider
modified: '2026-07-20'
name: Local Logic
nav: Providers
network: true
overview: 'Local Logic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Location Intelligence, Real Estate, Geospatial, and Neighborhoods.


  Local Logic''s developer surface includes documentation, support, engineering blog, pricing, signup flow, GitHub presence, authentication, and 6 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 23.5
  delta: -0.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 24.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/local-logic/refs/heads/main/screenshots/local-logic-2026-07-25T225422.png
security:
- kind: authentication
  name: Local Logic Authentication
  slug: local-logic-authentication
  summary_line: clientCredentials · 1 scheme
- kind: domain-security
  name: Local Logic Domain Security
  slug: local-logic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: local-logic
tags:
- Company
- Location Intelligence
- Real Estate
- Geospatial
- Neighborhoods
- Demographics
- Points of Interest
- Proptech
- Climate Risk
- Location Scores
website: https://locallogic.co
---
