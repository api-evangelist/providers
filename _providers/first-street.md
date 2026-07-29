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
- acting_count: 2
  human_in_the_loop: 0
  name: First Street Agentic Access
  operation_count: 3
  slug: first-street-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 6
apis:
- description: The Climate Risk API provides physical climate risk data globally, delivering property-level insights into hazards including flood, wildfire, heat, wind, and air quality.
  name: First Street Climate Risk API
  slug: climate-risk
- description: The Enterprise API offers aggregated climate risk views for portfolios, enabling enterprise users to assess risk across multiple properties and geographic regions.
  name: First Street Enterprise API
  slug: enterprise
- description: The Raster Map API delivers visual raster layers of climate perils for mapping and visualization use cases.
  name: First Street Raster Map API
  slug: raster-map
- description: The Enterprise API from First Street — 1 operation(s) for enterprise.
  name: First Street Enterprise API
  slug: first-street-enterprise-api
- description: The Graphql API from First Street — 1 operation(s) for graphql.
  name: First Street Graphql API
  slug: first-street-graphql-api
- description: The Maps API from First Street — 1 operation(s) for maps.
  name: First Street Maps API
  slug: first-street-maps-api
artifact_total: 15
collections:
- collection_type: open
  name: First Street API
  slug: open-first-street
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/first-street-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/first-street-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/first-street-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/first-street-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/first-street-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FirstStreet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/first-street-foundation
- group: company
  title: ''
  type: Website
  url: https://firststreet.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.firststreet.org/api
- group: agent
  title: ''
  type: LlmsText
  url: https://firststreet.org/llms.txt
created: '2025-03-01'
description: First Street models use validated and proven methodologies to ensure model accuracy. We measure and predict the impact of a peril based on the underlying physics of how an actual event would transpire. First Street exposes Climate Risk, Enterprise, and Raster Map APIs for property-level climate risk data.
finops:
- name: First Street Finops
  service_category: API
  slug: first-street-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/first-street.png
layout: provider
modified: '2026-04-28'
name: First Street
nav: Providers
network: true
overview: 'First Street publishes 3 APIs on the [APIs.io](https://apis.io/) network: Enterprise API, Graphql API, and Maps API. Tagged areas include Environment, Modeling, Risk, and Climate.


  First Street''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: First Street Plans Pricing
  plan_count: 3
  slug: first-street-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: First Street Rate Limits
  slug: first-street-rate-limits
score:
  band: thin
  composite: 37.9
  delta: -1.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 56.8
    developer_ergonomics: 19.6
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/first-street/refs/heads/main/screenshots/first-street-2026-06-20T181242.png
security:
- kind: authentication
  name: First Street Authentication
  slug: first-street-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: First Street Domain Security
  slug: first-street-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: First Street Vulnerability Disclosure
  slug: first-street-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: First Street Trust Center
  slug: first-street-trust-center
  summary_line: SOC 2
slug: first-street
tags:
- Environment
- Modeling
- Risk
- Climate
website: https://firststreet.org/
---
