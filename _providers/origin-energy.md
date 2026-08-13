---
access_model:
  confidence: high
  label: Gated · CDR accreditation or Origin partner/customer account required
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - cdr-register
  - well-known
  - documentation
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Origin Energy Agentic Access
  operation_count: 54
  slug: origin-energy-agentic-access
  summary_line: 54 operations · 19 acting
api_count: 7
apis:
- description: Origin Energy's Consumer Data Right energy data holder resource endpoint, serving the Consumer Data Standards energy APIs (accounts, invoices, billing, balances, concessions, payment schedules, electr
  name: Origin Energy CDR Energy API
  slug: origin-energy-cdr-energy-api
- description: The unauthenticated portion of Origin Energy's Consumer Data Right surface, published as the brand's publicBaseUri on the CDR Register. Verified anonymously on 2026-07-27 — GET /cds-au/v1/discovery/st
  name: Origin Energy CDR Public Discovery API
  slug: origin-energy-cdr-discovery-api
- description: Origin Energy's retail electricity and gas plan reference data, exposed under the Consumer Data Standards Get Generic Plans and Get Generic Plan Detail endpoints. Hosted by the Australian Energy Regul
  name: Origin Energy Plan Reference Data API (AER Energy Made Easy)
  slug: origin-energy-plan-reference-data-api
- description: The REST half of the Kraken platform API that Origin Energy runs its retail business on, documented at Origin's own publicly readable Kraken developer portal and described as available to "customers a
  name: Origin Energy Kraken REST API
  slug: origin-energy-kraken-rest-api
- description: The primary Kraken platform API for Origin Energy accounts, agreements, meter points, readings, payments, quotes and devices. Served at https://api.origin-kraken.energy/v1/graphql/ with a browser Grap
  name: Origin Energy Kraken GraphQL API
  slug: origin-energy-kraken-graphql-api
- description: Origin's publicly readable Kraken External Events reference, cataloguing several hundred versioned event types emitted by the platform. Confirmed HTTP 200 on 2026-07-27. The catalogue is explicitly Au
  name: Origin Energy Kraken External Events
  slug: origin-energy-kraken-events
- description: The OpenID Connect authorisation server issuing the bearer tokens used by both the Kraken REST and GraphQL APIs. Its discovery document at https://auth.origin-kraken.energy/.well-known/openid-configur
  name: Origin Energy Kraken Authorization Server
  slug: origin-energy-kraken-auth-api
artifact_total: 27
asyncapis:
- description: ''
  name: Origin Energy Kraken External Events
  slug: origin-energy-kraken-external-events
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/origin-energy-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/origin-energy-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/origin-energy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/origin-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/origin-energy-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.originenergy.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.origin-kraken.energy/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.origin-kraken.energy/
- group: other
  title: ''
  type: OpenIDConfiguration
  url: well-known/origin-energy-kraken-openid-configuration.json
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.origin-kraken.energy/announcements/
- group: company
  title: ''
  type: Blog
  url: https://www.originenergy.com.au/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/origin-energy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/origin-energy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.originenergy.com.au/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.originenergy.com.au/terms-of-use/
- group: other
  title: ''
  type: Registration
  url: https://www.cdr.gov.au/for-providers/accreditation
- group: other
  title: ''
  type: Regulation
  url: https://www.cdr.gov.au/
- group: operate
  title: ''
  type: Support
  url: https://www.originenergy.com.au/help-support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.originenergy.com.au/electricity-gas/plans.html
- group: start
  title: ''
  type: SignUp
  url: https://www.originenergy.com.au/sign-up/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.origin-kraken.energy/graphql/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.origin-kraken.energy/graphql/guides/basics/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/origin-energy-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/origin-energy-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/origin-energy-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/origin-energy-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/origin-energy-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/origin-energy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/origin-energy-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://public.mydata.cdr.originenergy.com.au/cds-au/v1/discovery/status
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.origin-kraken.energy/announcements/
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/origin-energy-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/origin-energy-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/engagements/originenergy-og1
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/origin-energy-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/origin-energy-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/origin-energy-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/origin-energy-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/origin-energy-api-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/origin-energy-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/origin-energy-kraken-external-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-27'
description: 'Origin Energy Limited is Australia''s largest energy retailer, an ASX-listed integrated gas and electricity company headquartered in Sydney that supplies roughly 4.5 million electricity, natural gas, LPG and broadband customer accounts, operates the Eraring Power Station and a large gas-fired and renewable generation portfolio, holds a stake in the Australia Pacific LNG project, and runs the Origin Loop virtual power plant. It sits at the retail end of the National Electricity Market value chain, buying and generating wholesale energy and selling it to households and businesses. Its API posture is defined almost entirely by regulation rather than by a developer strategy: Origin is a designated energy data holder under Australia''s Consumer Data Right and that obligation is genuinely implemented — it appears on the CDR Register with its own public base URI, serves the Consumer Data Standards discovery endpoints anonymously, and presents an mTLS resource endpoint whose TLS certificate
  is issued by the ACCC''s own CDR Certificate Authority — but every byte of actual customer usage, billing and DER data behind that surface is reachable only by an accredited data recipient acting on a consumer''s consent. Alongside the mandate, Origin runs its retail business on Octopus Energy''s Kraken platform (Origin holds an equity stake in Octopus and Kraken Technologies), which exposes a publicly readable partner developer portal with downloadable OpenAPI definitions, a GraphQL API, an external events catalogue and an OpenID Connect authorisation server — none of it self-serve. Origin publishes no open grid, market or system data of its own; the only anonymously retrievable data is its retail plan reference data, and that is served from the Australian Energy Regulator''s Energy Made Easy CDR gateway, not from an Origin host.'
features:
- description: Sells electricity and natural gas to residential and business customers across the National Electricity Market and Western Australian gas market.
  name: Electricity and Gas Retail
- description: Operates the Eraring Power Station, gas-fired peaking plant and renewable assets, and holds an interest in Australia Pacific LNG.
  name: Generation and LNG
- description: Aggregates customer solar, batteries and connected devices into one of Australia's largest virtual power plants for demand response and grid services.
  name: Origin Loop Virtual Power Plant
- description: Runs its retail billing, CRM and customer operations on Octopus Energy's Kraken platform, in which Origin holds an equity stake.
  name: Kraken Retail Platform
- description: Designated energy data holder under the Consumer Data Right, sharing customer usage, billing and DER data with accredited data recipients on consumer consent.
  name: Consumer Data Right Data Holding
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/origin-energy.png
integrations:
- description: Origin's retail platform is Octopus Energy's Kraken, tenanted at origin-kraken.energy; Origin holds an equity stake in both Octopus Energy and Kraken Technologies.
  name: Kraken Technologies
- description: The Australian Energy Market Operator is the secondary data holder in the CDR energy sector, holding metering and NMI standing data that complements the retailer's own.
  name: AEMO
- description: The Australian Energy Regulator hosts Origin's Consumer Data Standards plan reference data endpoints at cdr.energymadeeasy.gov.au/origin.
  name: AER Energy Made Easy
layout: provider
mcp_servers:
- description: ''
  name: origin-energy-mcp.yml
  slug: origin-energy-mcpyml
modified: '2026-07-27'
name: Origin Energy
nav: Providers
network: true
overview: 'Origin Energy publishes 4 APIs on the [APIs.io](https://apis.io/) network, including CDR Energy API, CDR Public Discovery API, Plan Reference Data API (AER Energy Made Easy), and 1 more. Tagged areas include Energy, Australia, Utilities, Electricity, and Gas.


  The Origin Energy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Origin Energy''s developer surface includes authentication, documentation, changelog, engineering blog, support, pricing, signup flow, and 35 more developer resources.'
random_paper: 23
rate_limits:
- limit_count: 6
  name: Origin Energy Rate Limits
  slug: origin-energy-rate-limits
scopes:
- name: Origin Energy Scopes
  scope_count: 113
  slug: origin-energy-scopes
  summary_line: 113 scopes
score:
  band: strong
  composite: 60.8
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 63.5
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 94.7
  previous_composite: 60.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/origin-energy/refs/heads/main/screenshots/origin-energy-2026-08-07T190934.png
security:
- kind: authentication
  name: Origin Energy Authentication
  slug: origin-energy-authentication
  summary_line: openIdConnect/oauth2/apiKey/http/mutualTLS · 8 schemes
- kind: domain-security
  name: Origin Energy Domain Security
  slug: origin-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Origin Energy Vulnerability Disclosure
  slug: origin-energy-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: origin-energy
tags:
- Energy
- Australia
- Utilities
- Electricity
- Gas
- Energy Retail
- Consumer Data Right
- Smart Metering
- Solar
- DER
- Demand Response
- Energy Markets
use_cases:
- description: An accredited CDR data recipient obtains an Origin customer's usage, billing and service point data with that customer's consent, for comparison, budgeting or energy management.
  name: Consented Energy Data Sharing
- description: Anyone can pull Origin's 3,595 published electricity and gas plans anonymously from the AER Energy Made Easy CDR gateway to build a comparison or switching tool.
  name: Retail Plan Comparison
- description: Origin partner organisations integrate with the Kraken REST and GraphQL APIs for account, payment, order and meter reading workflows.
  name: Partner Platform Integration
- description: The Kraken data-import REST API ingests accounts, historical statements, transactions and payment instructions when customers are migrated onto the platform.
  name: Customer Migration
website: https://www.originenergy.com.au/
---
