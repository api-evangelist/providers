---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 17.3
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: 'Amber Electric''s own documented REST API, described by a verbatim OpenAPI 3.0.0 contract the company publishes in its public GitHub repository. Five read-only operations: list the sites on your accoun'
  name: Amber Electric Public API
  slug: amber-electric-public-api
- description: Amber's Consumer Data Right energy data-holder surface, mandated by the Australian CDR regime extended from banking into energy and administered by the ACCC with standards set by the Data Standards Bo
  name: Amber Electric Consumer Data Right Energy API
  slug: amber-electric-cdr-energy-api
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://amber.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://app.amber.com.au/developers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amberelectric
- group: company
  title: ''
  type: Blog
  url: https://amber.com.au/blog
- group: operate
  title: ''
  type: Support
  url: https://help.amber.com.au/
- group: commercial
  title: ''
  type: Privacy
  url: https://amber.com.au/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.amber.com.au/developers
created: '2026-07-27'
description: 'Amber Electric is an Australian electricity retailer (ABN 98623603805) that sells wholesale National Electricity Market pricing straight through to residential customers on a flat monthly membership, rather than marking energy up, and automates home batteries, solar exports and EV charging against those half-hourly prices. It sits at the retail end of the Australian energy value chain, between AEMO''s wholesale market and the household meter. Its API posture is unusually honest and unusually split. Amber publishes a real, verbatim OpenAPI 3.0.0 contract for a REST API at https://api.amber.com.au/v1 covering sites, prices, forecasts and usage, but the token that unlocks it is generated inside the logged-in customer app at https://app.amber.com.au/developers, so the API is customer-account-required rather than self-serve — a developer who is not an Amber customer cannot obtain a key. One endpoint is the exception: the spec explicitly declares `security: []` on GET /state/{state}/renewables/current,
  and that grid renewables-percentage feed really does answer anonymously for NSW, VIC, QLD and SA, so open market data and gated consumer data live inside the same contract. Separately, Amber is a designated Consumer Data Right energy data holder that is genuinely live, not merely designated: it is listed on the ACCC CDR Register with a working public base URI at https://public.cdr.amber.com.au, whose CDS discovery endpoints and anonymously-served OpenID Connect configuration advertise the full Consumer Data Standards energy scope set behind private_key_jwt and CDR accreditation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amber-electric.png
layout: provider
modified: '2026-07-27'
name: Amber Electric
nav: Providers
network: true
overview: 'Amber Electric publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Energy, Australia, Electricity, Utilities, and Consumer Data Right.


  Amber Electric''s developer surface includes documentation, engineering blog, support, privacy policy, signup flow, and 2 more developer resources.'
random_paper: 47
score:
  band: emerging
  composite: 24.4
  facets:
    commercial_clarity: 23.7
    contract_quality: 37.7
    developer_ergonomics: 15.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 8.7
  schema_version: 0.5
  scored_at: '2026-07-27'
slug: amber-electric
tags:
- Energy
- Australia
- Electricity
- Utilities
- Consumer Data Right
- Energy Markets
- Renewables
- Solar
- Batteries
- DER
- Smart Metering
- Wholesale Pricing
website: https://amber.com.au/
---
