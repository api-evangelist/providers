---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-05'
api_count: 5
apis:
- description: Token endpoint for OAuth 2.0 Client Credentials authentication used to authorize requests to all USPS API products.
  name: USPS OAuth 2.0
  slug: oauth2
- description: Verify and standardize US addresses to USPS specifications, reducing shipping delays and errors.
  name: USPS Addresses API
  slug: addresses
- description: Retrieve tracking status and delivery events for shipped packages across USPS services.
  name: USPS Tracking API
  slug: tracking
- description: Create and cancel domestic shipping labels with integrated address standardization, pricing, and manifesting.
  name: USPS Labels API
  slug: labels
- description: Retrieve current pricing information for USPS domestic shipping products and services.
  name: USPS Domestic Prices API
  slug: prices
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usps-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usps
- group: company
  title: ''
  type: Website
  url: https://www.usps.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.usps.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.usps.com/getting-started
- group: start
  title: ''
  type: Signup
  url: https://developers.usps.com/apis
- group: build
  title: ''
  type: GitHub
  url: https://github.com/USPS/api-examples
- group: company
  title: ''
  type: Blog
  url: https://about.usps.com/news/latestnews.rss
created: '2026-05-11'
description: The United States Postal Service (USPS) provides a modern suite of RESTful APIs for address validation, domestic and international pricing, shipping label creation and cancellation, tracking, and service standards through its developer portal. The APIs replace the legacy Web Tools platform and use OAuth 2.0 Client Credentials for authentication. The platform supports both production and TEM (Testing Environment for Mailers) endpoints for developing and validating shipping integrations.
graphqls:
- description: Conceptual GraphQL schema for the United States Postal Service (USPS) APIs. This schema models the capabilities exposed by the USPS REST API developer portal at [https://developer.usps.com/](https://d
  name: USPS GraphQL Schema
  slug: usps-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usps.png
layout: provider
modified: '2026-05-11'
name: USPS
nav: Providers
network: true
overview: 'USPS publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, Postal, Address Validation, Tracking, and Labels.


  USPS''s developer surface includes documentation, getting-started guide, signup flow, GitHub presence, engineering blog, and 3 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 24.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/usps/refs/heads/main/screenshots/usps-2026-06-20T200718.png
security:
- kind: domain-security
  name: Usps Domain Security
  slug: usps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: usps
tags:
- Shipping
- Postal
- Address Validation
- Tracking
- Labels
- Logistics
website: https://www.usps.com
---
