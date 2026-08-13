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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Octopus Energy Agentic Access
  operation_count: 13
  slug: octopus-energy-agentic-access
  summary_line: 13 operations
api_count: 9
apis:
- description: The Octopus Energy developer portal exposes a Kraken-backed REST API alongside the public GraphQL surface. The REST API is generated from an OpenAPI specification published in the developer portal Ref
  name: Octopus Energy Kraken REST API
  slug: octopus-energy-kraken-rest-api
- description: The Octopus Energy GraphQL API is the primary Kraken interface for partner and customer-facing integrations. A single /v1/graphql/ endpoint exposes queries and mutations grouped into API Collections b
  name: Octopus Energy Kraken GraphQL API
  slug: octopus-energy-kraken-graphql-api
- description: Half-hourly smart-meter consumption readings.
  name: Octopus Energy Consumption API
  slug: octopus-energy-consumption-api
- description: Electricity meter points (MPAN) and registered meters.
  name: Octopus Energy ElectricityMeterPoints API
  slug: octopus-energy-electricitymeterpoints-api
- description: Electricity tariff unit rates and standing charges.
  name: Octopus Energy ElectricityTariffs API
  slug: octopus-energy-electricitytariffs-api
- description: Gas meter points (MPRN) and registered meters.
  name: Octopus Energy GasMeterPoints API
  slug: octopus-energy-gasmeterpoints-api
- description: Gas tariff unit rates and standing charges.
  name: Octopus Energy GasTariffs API
  slug: octopus-energy-gastariffs-api
- description: UK industry references such as grid supply points.
  name: Octopus Energy Industry API
  slug: octopus-energy-industry-api
- description: Octopus Energy product catalog and tariff lookups.
  name: Octopus Energy Products API
  slug: octopus-energy-products-api
artifact_total: 44
collections:
- collection_type: open
  name: Octopus Energy Public API
  slug: open-octopus-energy-public-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/octopus-energy-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/octopus-energy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/octopus-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/octopus-energy-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://octopus.energy
- group: start
  title: ''
  type: Portal
  url: https://developer.octopus.energy/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.octopus.energy/docs/api/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.octopus.energy/rest/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.octopus.energy/graphql/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.octopus.energy/announcements/
- group: start
  title: ''
  type: Signup
  url: https://developer.octopus.energy/auth/login/
- group: start
  title: ''
  type: Signup
  url: https://octopus.energy/dashboard/
- group: operate
  title: ''
  type: Support
  url: https://octopus.energy/help-and-faqs/articles/api-information/
- group: auth
  title: ''
  type: Security
  url: https://octopus.energy/help-and-faqs/articles/security-at-octopus-energy/
- group: docs
  title: ''
  type: Documentation
  url: https://octopus.energy/policies/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://octopus.energy/privacy/
- group: company
  title: ''
  type: Blog
  url: https://octopus.energy/blog/
- group: company
  title: ''
  type: Press
  url: https://octopus.energy/press/
- group: company
  title: ''
  type: Careers
  url: https://octopus.energy/careers/
- group: company
  title: ''
  type: AboutUs
  url: https://octopus.energy/about-us/
- group: operate
  title: ''
  type: ContactUs
  url: https://octopus.energy/contact-us/
- group: start
  title: ''
  type: Portal
  url: https://kraken.tech/
- group: company
  title: ''
  type: Blog
  url: https://kraken.tech/news
- group: docs
  title: ''
  type: Documentation
  url: https://kraken.tech/customer-management
- group: docs
  title: ''
  type: Documentation
  url: https://kraken.tech/residential-flexibility
- group: docs
  title: ''
  type: Documentation
  url: https://kraken.tech/field-operations
- group: docs
  title: ''
  type: Documentation
  url: https://kraken.tech/infrastructure-flexibility
- group: docs
  title: ''
  type: Documentation
  url: https://octopus.energy/agile/
- group: docs
  title: ''
  type: Documentation
  url: https://octopus.energy/smart/tracker/
- group: docs
  title: ''
  type: Documentation
  url: https://octopus.energy/smart/intelligent-octopus-go/
- group: docs
  title: ''
  type: Documentation
  url: https://octopus.energy/electric-vehicles/electroverse/
- group: docs
  title: ''
  type: Documentation
  url: https://octopus.energy/heat-pumps/
- group: docs
  title: ''
  type: Documentation
  url: https://octopusev.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/octoenergy
- group: build
  title: ''
  type: Tools
  url: https://github.com/octoenergy/public-conventions
- group: build
  title: ''
  type: SDKs
  url: https://github.com/octoenergy/xocto
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/octoenergy/oejp-api-example
- group: build
  title: ''
  type: Tools
  url: https://github.com/octoenergy/octotools
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/octoenergy/techzero-hackathon-2024
- group: build
  title: ''
  type: Tools
  url: https://github.com/octoenergy/timeserio
- group: build
  title: ''
  type: Tools
  url: https://github.com/octoenergy/terraform-provider-splitpolicies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/octopus-energy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/krakentech
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/octopus_energy
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@OctopusEnergy
- group: commercial
  title: ''
  type: Plans
  url: plans/octopus-energy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/octopus-energy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/octopus-energy-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: Octopus Energy is a UK-founded retail energy supplier and the parent of Kraken Technologies, the AI-powered energy operating system that runs both Octopus and many of the world's largest utilities. Octopus operates a free, open REST API at api.octopus.energy/v1/ that exposes the full UK product catalog, electricity and gas tariff pricing (including the half-hourly wholesale-linked Agile Octopus and Tracker tariffs), meter-point details, half-hourly smart-meter consumption, and industry grid supply points. The Kraken developer portal at developer.octopus.energy adds a second REST surface generated from an OpenAPI spec plus a GraphQL API at /v1/graphql/ with API Collections grouping partner-facing queries and mutations for accounts, ledgers, billing, smart meters, EV charging, heat pumps, batteries, and Intelligent Octopus dispatch. Through Kraken Technologies the same platform powers 90M+ customer accounts at EDF, E.ON, Origin Energy, Tokyo Gas, Plentitude, National Grid, Severn
  Trent, and other utilities in 30 countries — making Octopus one of the most consequential open and programmable surfaces in retail energy.
examples:
- key_count: 4
  name: Octopus Energy List Electricity Consumption Example
  slug: octopus-energy-list-electricity-consumption-example
- key_count: 4
  name: Octopus Energy List Electricity Standard Unit Rates Example
  slug: octopus-energy-list-electricity-standard-unit-rates-example
- key_count: 4
  name: Octopus Energy List Products Example
  slug: octopus-energy-list-products-example
features:
- Public REST API at api.octopus.energy/v1/ — open product catalog, electricity/gas tariffs, meter points, half-hourly consumption, and industry grid supply points
- HTTP Basic authentication with a per-customer API key for account, meter-point, and consumption endpoints; products and tariffs endpoints are open and unauthenticated
- Half-hourly Agile Octopus and 30-minute Octopus Tracker pricing endpoints for wholesale-linked smart tariffs that publish 16-48 hours of forward unit rates
- Industry grid supply points lookup so consumers can resolve the correct distribution region from a postcode
- JSON request/response over HTTPS with cursor-style pagination on collection endpoints
- Half-hourly smart-meter consumption pulls for electricity (MPAN + serial number) and gas (MPRN + serial number)
- Kraken developer portal at developer.octopus.energy with REST API Reference generated from an OpenAPI specification
- Kraken developer portal GraphQL API at /v1/graphql/ with introspection, API Collections, and a public changelog
- API Collections that group GraphQL queries and mutations by feature — accounts, ledgers, billing, smart meters, half-hourly consumption, EV charging, heat pumps, batteries, Octopus Electroverse
- Intelligent Octopus dispatch schedules exposed via GraphQL for partners to read EV-charging and heat-pump optimization windows
- Public conventions repository documenting Octopus Energy's internal Python and Django style guide
- xocto open-source Python/Django utility library from Kraken Technologies — typed money, ranges, settlement periods, and event sourcing primitives
- oejp-api-example reference application showing how to consume the Octopus Energy Japan API
- octotools Python utilities for the UK energy market — DNO/GSP lookups and tariff parsing helpers
- Kraken Technologies SaaS platform powering 90M+ customer accounts across EDF, E.ON, Origin Energy, Tokyo Gas, Plentitude, Severn Trent, National Grid, and other partners in 30 countries
- Kraken product suites — Customer Management, Residential Flexibility, Field Operations, Infrastructure Flexibility — covering retail energy, water, and telecom utilities
- Domain coverage for electricity and gas retail, electric vehicles via Octopus Electroverse, heat pumps via Cosy Octopus, solar, batteries, and tariff-aware smart device control
- UK-first API surface with parallel Octopus Energy Japan, Australia, New Zealand, Germany, France, Italy, Spain, and United States deployments via the same Kraken platform
finops:
- name: Octopus Energy Finops
  service_category: ''
  slug: octopus-energy-finops
graphqls:
- description: The Octopus Energy GraphQL API is the primary Kraken interface for partner and customer-facing integrations. A single /v1/graphql/ endpoint exposes queries and mutations grouped into API Collections b
  name: Octopus Energy GraphQL API
  slug: octopus-energy-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/octopus-energy.png
json_schemas:
- name: OctopusEnergyConsumptionReading
  property_count: 3
  slug: octopus-energy-consumption
- name: OctopusEnergyProduct
  property_count: 15
  slug: octopus-energy-product
jsonld:
- class_count: 31
  name: Octopus Energy Context
  property_count: 0
  slug: octopus-energy-context
layout: provider
modified: '2026-05-25'
name: Octopus Energy
nav: Providers
network: true
overview: 'Octopus Energy publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Consumption API, ElectricityMeterPoints API, ElectricityTariffs API, and 4 more. Tagged areas include Energy, Electricity, Gas, Renewable Energy, and Smart Meter.


  The Octopus Energy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Octopus Energy''s developer surface includes authentication, developer portal, documentation, changelog, signup flow, support, engineering blog, and 41 more developer resources.'
plans:
- name: Octopus Energy Plans Pricing
  plan_count: 2
  slug: octopus-energy-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 3
  name: Octopus Energy Rate Limits
  slug: octopus-energy-rate-limits
rules:
- name: Octopus Energy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: octopus-energy-jsonschema-spectral-rules
- name: Octopus Energy API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 2
  slug: octopus-energy-rules
score:
  band: developing
  composite: 54.6
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 69.1
    developer_ergonomics: 41.3
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 63.2
  previous_composite: 54.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 36.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/octopus-energy/refs/heads/main/screenshots/octopus-energy-2026-06-20T190615.png
security:
- kind: authentication
  name: Octopus Energy Authentication
  slug: octopus-energy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Octopus Energy Domain Security
  slug: octopus-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Octopus Energy Vulnerability Disclosure
  slug: octopus-energy-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: octopus-energy
tags:
- Energy
- Electricity
- Gas
- Renewable Energy
- Smart Meter
- Tariffs
- Kraken
- UK
- DER
- Electric Vehicles
- Heat Pumps
- Solar
- Battery
website: https://octopus.energy
---
