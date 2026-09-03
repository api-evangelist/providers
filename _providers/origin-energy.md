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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Origin Energy Agentic Access
  operation_count: 54
  slug: origin-energy-agentic-access
  summary_line: 54 operations · 19 acting
api_count: 5
apis:
- description: The primary Kraken platform API for Origin Energy accounts, agreements, meter points, readings, payments, quotes and devices. Served at https://api.origin-kraken.energy/v1/graphql/ with a browser Grap
  name: Origin Energy Kraken GraphQL API
  slug: origin-energy-kraken-graphql-api
- description: Origin's publicly readable Kraken External Events reference, cataloguing several hundred versioned event types emitted by the platform. Confirmed HTTP 200 on 2026-07-27. The catalogue is explicitly Au
  name: Origin Energy Kraken External Events
  slug: origin-energy-kraken-events
- description: The OpenID Connect authorisation server issuing the bearer tokens used by both the Kraken REST and GraphQL APIs. Its discovery document at https://auth.origin-kraken.energy/.well-known/openid-configur
  name: Origin Energy Kraken Authorization Server
  slug: origin-energy-kraken-auth-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: APIs for importing accounts.
  name: Origin Energy Account Import API
  slug: origin-energy-account-import-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: APIs for importing businesses with business contracts
  name: Origin Energy Business Import API
  slug: origin-energy-business-import-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: Data Holder Customer endpoints
  name: Origin Energy Data Holder Customers API
  slug: origin-energy-data-holder-customers-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: Data Holder Operations endpoints
  name: Origin Energy Data Holder Operations API
  slug: origin-energy-data-holder-operations-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: The data-import API from Origin Energy — 1 operation(s) for data-import.
  name: Origin Energy Data Import API
  slug: origin-energy-data-import-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: Distributed Energy Resource endpoints
  name: Origin Energy Distributed Energy Resources API
  slug: origin-energy-distributed-energy-resources-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: Electricity Service Point endpoints
  name: Origin Energy Electricity Service Points API
  slug: origin-energy-electricity-service-points-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: Electricity Usage endpoints
  name: Origin Energy Electricity Usage API
  slug: origin-energy-electricity-usage-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: Energy Account Balance endpoints
  name: Origin Energy Energy Account Balances API
  slug: origin-energy-energy-account-balances-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: Energy Account Billing endpoints
  name: Origin Energy Energy Account Billing API
  slug: origin-energy-energy-account-billing-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: Energy Account endpoints
  name: Origin Energy Energy Accounts API
  slug: origin-energy-energy-accounts-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: Energy Plan endpoints
  name: Origin Energy Energy Plans API
  slug: origin-energy-energy-plans-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: The external-client-healthcheck API from Origin Energy — 1 operation(s) for external-client-healthcheck.
  name: Origin Energy External Client Healthcheck API
  slug: origin-energy-external-client-healthcheck-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: The external-events API from Origin Energy — 1 operation(s) for external-events.
  name: Origin Energy External Events API
  slug: origin-energy-external-events-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: APIs for placing and managing orders.
  name: Origin Energy Orders API
  slug: origin-energy-orders-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: APIs for importing additional data after an account has been imported.
  name: Origin Energy Post Account Import API
  slug: origin-energy-post-account-import-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: APIs for importing additional data after a business has been imported.
  name: Origin Energy Post Business Import API
  slug: origin-energy-post-business-import-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: APIs for querying import status and retrieving data
  name: Origin Energy Query API
  slug: origin-energy-query-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: The v1 API from Origin Energy — 5 operation(s) for v1.
  name: Origin Energy V1 API
  slug: origin-energy-v1-api
- baseURL: https://api.mydata.cdr.originenergy.com.au
  baseurl_source: declared
  description: The v2 API from Origin Energy — 1 operation(s) for v2.
  name: Origin Energy V2 API
  slug: origin-energy-v2-api
artifact_total: 47
asyncapis:
- description: ''
  name: Origin Energy Kraken External Events
  slug: origin-energy-kraken-external-events
collections:
- collection_type: open
  name: CDR Common API
  slug: open-consumer-data-standards-common-api
- collection_type: open
  name: CDR Energy API
  slug: open-consumer-data-standards-energy-api
- collection_type: open
  name: Kraken
  slug: open-origin-energy-kraken-data-import
- collection_type: open
  name: Kraken
  slug: open-origin-energy-kraken-default
- collection_type: open
  name: Kraken
  slug: open-origin-energy-kraken-orders
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/origin-energy-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/origin-energy-cds-energy-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/origin-energy-cdr-consented-energy-data.md
- group: other
  title: ''
  type: Overlay
  url: overlays/origin-energy-cds-common-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/origin-energy-retail-plan-comparison.md
- group: other
  title: ''
  type: Overlay
  url: overlays/origin-energy-kraken-default-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/origin-energy-kraken-data-import-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/origin-energy-kraken-orders-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/origin-energy-kraken-customer-migration.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/origin-energy-kraken-order-scheduling.md
- group: agent
  title: ''
  type: X-MCPServerCandidate
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
modified: '2026-07-27'
name: Origin Energy
nav: Providers
network: true
overview: 'Origin Energy publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Account Import API, Business Import API, Data Holder Customers API, and 17 more. Tagged areas include Energy, Australia, Utilities, Electricity, and Gas.


  The Origin Energy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Origin Energy''s developer surface includes authentication, documentation, changelog, engineering blog, support, pricing, signup flow, and 45 more developer resources.'
random_paper: 20
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
  band: developing
  composite: 53.6
  coverage:
    artifact_dirs: 24
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 62.9
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 84.2
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 55.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
