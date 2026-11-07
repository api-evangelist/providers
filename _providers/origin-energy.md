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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Origin Energy Agentic Access
  operation_count: 54
  slug: origin-energy-agentic-access
  summary_line: 54 operations · 14 acting
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
- baseURL: https://api.origin-kraken.energy
  baseurl_source: declared
  description: APIs for importing accounts.
  name: Origin Energy Account Import API
  slug: origin-energy-account-import-api
- baseURL: https://api.origin-kraken.energy
  baseurl_source: declared
  description: APIs for importing businesses with business contracts
  name: Origin Energy Business Import API
  slug: origin-energy-business-import-api
- baseURL: https://api.mydata.cdr.originenergy.com.au/cds-au/v1
  baseurl_source: declared
  description: Data Holder Customer endpoints
  name: Origin Energy Data Holder Customers API
  slug: origin-energy-data-holder-customers-api
- baseURL: https://public.mydata.cdr.originenergy.com.au/cds-au/v1
  baseurl_source: declared
  description: Data Holder Operations endpoints
  name: Origin Energy Data Holder Operations API
  slug: origin-energy-data-holder-operations-api
- baseURL: https://api.origin-kraken.energy
  baseurl_source: declared
  description: The data-import API from Origin Energy — 1 operation(s) for data-import.
  name: Origin Energy Data Import API
  slug: origin-energy-data-import-api
- baseURL: https://api.mydata.cdr.originenergy.com.au/cds-au/v1
  baseurl_source: declared
  description: Distributed Energy Resource endpoints
  name: Origin Energy Distributed Energy Resources API
  slug: origin-energy-distributed-energy-resources-api
- baseURL: https://api.mydata.cdr.originenergy.com.au/cds-au/v1
  baseurl_source: declared
  description: Electricity Service Point endpoints
  name: Origin Energy Electricity Service Points API
  slug: origin-energy-electricity-service-points-api
- baseURL: https://api.mydata.cdr.originenergy.com.au/cds-au/v1
  baseurl_source: declared
  description: Electricity Usage endpoints
  name: Origin Energy Electricity Usage API
  slug: origin-energy-electricity-usage-api
- baseURL: https://api.mydata.cdr.originenergy.com.au/cds-au/v1
  baseurl_source: declared
  description: Energy Account Balance endpoints
  name: Origin Energy Account Balances API
  slug: origin-energy-energy-account-balances-api
- baseURL: https://api.mydata.cdr.originenergy.com.au/cds-au/v1
  baseurl_source: declared
  description: Energy Account Billing endpoints
  name: Origin Energy Account Billing API
  slug: origin-energy-energy-account-billing-api
- baseURL: https://api.mydata.cdr.originenergy.com.au/cds-au/v1
  baseurl_source: declared
  description: Energy Account endpoints
  name: Origin Energy Accounts API
  slug: origin-energy-energy-accounts-api
- baseURL: https://cdr.energymadeeasy.gov.au/origin/cds-au/v1
  baseurl_source: declared
  description: Energy Plan endpoints
  name: Origin Energy Plans API
  slug: origin-energy-energy-plans-api
- baseURL: https://api.origin-kraken.energy
  baseurl_source: declared
  description: The external-client-healthcheck API from Origin Energy — 1 operation(s) for external-client-healthcheck.
  name: Origin Energy External Client Healthcheck API
  slug: origin-energy-external-client-healthcheck-api
- baseURL: https://api.origin-kraken.energy
  baseurl_source: declared
  description: The external-events API from Origin Energy — 1 operation(s) for external-events.
  name: Origin Energy External Events API
  slug: origin-energy-external-events-api
- baseURL: https://api.origin-kraken.energy
  baseurl_source: declared
  description: APIs for placing and managing orders.
  name: Origin Energy Orders API
  slug: origin-energy-orders-api
- baseURL: https://api.origin-kraken.energy
  baseurl_source: declared
  description: APIs for importing additional data after an account has been imported.
  name: Origin Energy Post Account Import API
  slug: origin-energy-post-account-import-api
- baseURL: https://api.origin-kraken.energy
  baseurl_source: declared
  description: APIs for importing additional data after a business has been imported.
  name: Origin Energy Post Business Import API
  slug: origin-energy-post-business-import-api
- baseURL: https://api.origin-kraken.energy
  baseurl_source: declared
  description: APIs for querying import status and retrieving data
  name: Origin Energy Query API
  slug: origin-energy-query-api
- baseURL: https://api.origin-kraken.energy
  baseurl_source: declared
  description: The Accounts API from Origin Energy — 1 operation(s) for accounts.
  name: Origin Energy Accounts API
  slug: origin-energy-accounts-api
- baseURL: https://api.origin-kraken.energy
  baseurl_source: declared
  description: The Energetiq Public Key API from Origin Energy — 1 operation(s) for energetiq public key.
  name: Origin Energy Energetiq Public Key API
  slug: origin-energy-energetiq-public-key-api
- baseURL: https://api.origin-kraken.energy
  baseurl_source: declared
  description: The Unbundled Network Charges API from Origin Energy — 1 operation(s) for unbundled network charges.
  name: Origin Energy Unbundled Network Charges API
  slug: origin-energy-unbundled-network-charges-api
- baseURL: https://api.origin-kraken.energy
  baseurl_source: declared
  description: The Voice API from Origin Energy — 2 operation(s) for voice.
  name: Origin Energy Voice API
  slug: origin-energy-voice-api
artifact_total: 96
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/origin-energy/overview
- group: design
  href: https://artifacts.apis.io/origin-energy/rules/origin-energy-rules.yml
  title: ''
  type: Spectral
  url: rules/origin-energy-rules.yml
- group: design
  href: https://artifacts.apis.io/origin-energy/json-ld/origin-energy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/origin-energy-context.jsonld
- group: design
  href: https://artifacts.apis.io/origin-energy/vocabulary/origin-energy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/origin-energy-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/origin-energy/hosts/origin-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/origin-energy-hosts.yml
- group: build
  href: https://artifacts.apis.io/origin-energy/integrations/origin-energy-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/origin-energy-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/origin-energy/vendors/origin-energy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/origin-energy-vendors.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.originenergy.com.au/blog/feed/
- group: other
  href: https://artifacts.apis.io/origin-energy/capabilities/origin-energy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/origin-energy-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/origin-energy/overlays/origin-energy-cds-energy-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/origin-energy-cds-energy-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/origin-energy/skills/origin-energy-cdr-consented-energy-data.md
  title: ''
  type: AgentSkill
  url: skills/origin-energy-cdr-consented-energy-data.md
- group: other
  href: https://artifacts.apis.io/origin-energy/overlays/origin-energy-cds-common-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/origin-energy-cds-common-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/origin-energy/skills/origin-energy-retail-plan-comparison.md
  title: ''
  type: AgentSkill
  url: skills/origin-energy-retail-plan-comparison.md
- group: other
  href: https://artifacts.apis.io/origin-energy/overlays/origin-energy-kraken-default-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/origin-energy-kraken-default-overlay.yaml
- group: other
  href: https://artifacts.apis.io/origin-energy/overlays/origin-energy-kraken-data-import-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/origin-energy-kraken-data-import-overlay.yaml
- group: other
  href: https://artifacts.apis.io/origin-energy/overlays/origin-energy-kraken-orders-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/origin-energy-kraken-orders-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/origin-energy/skills/origin-energy-kraken-customer-migration.md
  title: ''
  type: AgentSkill
  url: skills/origin-energy-kraken-customer-migration.md
- group: agent
  href: https://artifacts.apis.io/origin-energy/skills/origin-energy-kraken-order-scheduling.md
  title: ''
  type: AgentSkill
  url: skills/origin-energy-kraken-order-scheduling.md
- group: agent
  href: https://artifacts.apis.io/origin-energy/mcp/origin-energy-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/origin-energy-mcp.yml
- group: agent
  href: https://artifacts.apis.io/origin-energy/agentic-access/origin-energy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/origin-energy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/origin-energy/security/origin-energy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/origin-energy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/origin-energy/security/origin-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/origin-energy-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/origin-energy/authentication/origin-energy-authentication.yml
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
  href: https://artifacts.apis.io/origin-energy/well-known/origin-energy-kraken-openid-configuration.json
  title: ''
  type: OpenIDConfiguration
  url: well-known/origin-energy-kraken-openid-configuration.json
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.origin-kraken.energy/announcements/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/origin-energy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/origin-energy
- group: other
  title: ''
  type: Registration
  url: https://www.cdr.gov.au/for-providers/accreditation
- group: other
  title: ''
  type: Regulation
  url: https://www.cdr.gov.au/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.origin-kraken.energy/graphql/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.origin-kraken.energy/graphql/guides/basics/
- group: operate
  href: https://artifacts.apis.io/origin-energy/changelog/origin-energy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/origin-energy-changelog.yml
- group: design
  href: https://artifacts.apis.io/origin-energy/conventions/origin-energy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/origin-energy-conventions.yml
- group: design
  href: https://artifacts.apis.io/origin-energy/conventions/origin-energy-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/origin-energy-conventions.yml
- group: operate
  href: https://artifacts.apis.io/origin-energy/rate-limits/origin-energy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/origin-energy-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/origin-energy/errors/origin-energy-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/origin-energy-error-codes.yml
- group: design
  href: https://artifacts.apis.io/origin-energy/errors/origin-energy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/origin-energy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/origin-energy/lifecycle/origin-energy-lifecycle.yml
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
  href: https://artifacts.apis.io/origin-energy/scopes/origin-energy-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/origin-energy-scopes.yml
- group: design
  href: https://artifacts.apis.io/origin-energy/conformance/origin-energy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/origin-energy-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/engagements/originenergy-og1
- group: auth
  href: https://artifacts.apis.io/origin-energy/well-known/origin-energy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/origin-energy-security.txt
- group: agent
  href: https://artifacts.apis.io/origin-energy/well-known/origin-energy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/origin-energy-well-known.yml
- group: agent
  href: https://artifacts.apis.io/origin-energy/llms/origin-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/origin-energy-llms.txt
- group: agent
  href: https://artifacts.apis.io/origin-energy/llms/origin-energy-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/origin-energy-api-llms.txt
- group: design
  href: https://artifacts.apis.io/origin-energy/data-model/origin-energy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/origin-energy-data-model.yml
- group: design
  href: https://artifacts.apis.io/origin-energy/asyncapi/origin-energy-kraken-external-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/origin-energy-kraken-external-events.yml
- group: agent
  href: https://artifacts.apis.io/origin-energy/skills/_index.yml
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
image: https://www.originenergy.com.au/static/tal-client/apple-touch-icon.png
integrations:
- description: Origin's retail platform is Octopus Energy's Kraken, tenanted at origin-kraken.energy; Origin holds an equity stake in both Octopus Energy and Kraken Technologies.
  name: Kraken Technologies
- description: The Australian Energy Market Operator is the secondary data holder in the CDR energy sector, holding metering and NMI standing data that complements the retailer's own.
  name: AEMO
- description: The Australian Energy Regulator hosts Origin's Consumer Data Standards plan reference data endpoints at cdr.energymadeeasy.gov.au/origin.
  name: AER Energy Made Easy
json_schemas:
- name: AccountNote
  property_count: 4
  slug: origin-energy-account-note
- name: AccountTransferStatus
  property_count: 3
  slug: origin-energy-account-transfer-status
- name: AdHocResponse
  property_count: 4
  slug: origin-energy-ad-hoc-response
- name: AdHoc
  property_count: 5
  slug: origin-energy-ad-hoc
- name: BusinessImportProcessCreation
  property_count: 2
  slug: origin-energy-business-import-process-creation
- name: BusinessImportProcess
  property_count: 3
  slug: origin-energy-business-import-process
- name: BusinessPaymentInstruction
  property_count: 7
  slug: origin-energy-business-payment-instruction
- name: CreateAccountNotesResponse
  property_count: 8
  slug: origin-energy-create-account-notes-response
- name: CreateBusinessPaymentInstructionResponse
  property_count: 2
  slug: origin-energy-create-business-payment-instruction-response
- name: CreateOrUpdateAccountImportProcess
  property_count: 2
  slug: origin-energy-create-or-update-account-import-process
- name: CreatePaymentInstructionResponse
  property_count: 3
  slug: origin-energy-create-payment-instruction-response
- name: EnergyAccountDetailResponseV4
  property_count: 3
  slug: origin-energy-energy-account-detail-response-v4
- name: EnergyAccountListResponseV2
  property_count: 3
  slug: origin-energy-energy-account-list-response-v2
- name: EnergyBalanceListResponse
  property_count: 3
  slug: origin-energy-energy-balance-list-response
- name: EnergyBalanceResponse
  property_count: 3
  slug: origin-energy-energy-balance-response
- name: EnergyBillingListResponseV3
  property_count: 3
  slug: origin-energy-energy-billing-list-response-v3
- name: EnergyConcessionsResponse
  property_count: 3
  slug: origin-energy-energy-concessions-response
- name: EnergyDerDetailResponse
  property_count: 3
  slug: origin-energy-energy-der-detail-response
- name: EnergyDerListResponse
  property_count: 3
  slug: origin-energy-energy-der-list-response
- name: EnergyInvoiceListResponse
  property_count: 3
  slug: origin-energy-energy-invoice-list-response
- name: EnergyPaymentScheduleResponse
  property_count: 3
  slug: origin-energy-energy-payment-schedule-response
- name: EnergyPlanListResponse
  property_count: 3
  slug: origin-energy-energy-plan-list-response
- name: EnergyPlanResponseV3
  property_count: 3
  slug: origin-energy-energy-plan-response-v3
- name: EnergyServicePointDetailResponseV2
  property_count: 3
  slug: origin-energy-energy-service-point-detail-response-v2
- name: EnergyServicePointListResponseV2
  property_count: 3
  slug: origin-energy-energy-service-point-list-response-v2
- name: EnergyUsageListResponse
  property_count: 3
  slug: origin-energy-energy-usage-list-response
- name: HistoricalStatements
  property_count: 3
  slug: origin-energy-historical-statements
- name: ImportProcess
  property_count: 3
  slug: origin-energy-import-process
- name: ImportStatusResponse
  property_count: 6
  slug: origin-energy-import-status-response
- name: LegacyPaymentInstruction
  property_count: 9
  slug: origin-energy-legacy-payment-instruction
- name: OriginAccount
  property_count: 69
  slug: origin-energy-origin-account
- name: ProcessAccountImportProcessCreation
  property_count: 3
  slug: origin-energy-process-account-import-process-creation
- name: ProcessAccountImportProcess
  property_count: 4
  slug: origin-energy-process-account-import-process
- name: ResponseCommonCustomerDetailV2
  property_count: 3
  slug: origin-energy-response-common-customer-detail-v2
- name: ResponseCommonCustomer
  property_count: 3
  slug: origin-energy-response-common-customer
- name: ResponseCommonDiscoveryStatus
  property_count: 3
  slug: origin-energy-response-common-discovery-status
- name: ResponseDiscoveryOutagesList
  property_count: 3
  slug: origin-energy-response-discovery-outages-list
- name: ScheduleOrder
  property_count: 2
  slug: origin-energy-schedule-order
- name: Transactions
  property_count: 5
  slug: origin-energy-transactions
jsonld:
- class_count: 120
  name: Origin Energy Context
  property_count: 504
  slug: origin-energy-context
layout: provider
modified: '2026-10-20'
name: Origin Energy
nav: Providers
network: true
overview: 'Origin Energy publishes 25 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Import API, Business Import API, Data Holder Customers API, and 22 more. Tagged areas include Energy, Australia, Utilities, Electricity, and Gas.


  The Origin Energy catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Origin Energy''s developer surface includes authentication, documentation, changelog, API reference, getting-started guide, and 48 more developer resources.'
plans:
- name: Origin Energy Plans Pricing
  plan_count: 0
  slug: origin-energy-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 7
  name: Origin Energy Rate Limits
  slug: origin-energy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Origin Energy API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: origin-energy-rules
scopes:
- name: Origin Energy Scopes
  scope_count: 113
  slug: origin-energy-scopes
  summary_line: 113 scopes
score:
  band: strong
  composite: 62.2
  coverage:
    artifact_dirs: 36
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.6
  facets:
    access_clarity: 13.2
    contract_governance: 35.6
    contract_quality: 70.7
    developer_ergonomics: 53.0
    discoverability: 78.6
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 59.1
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 39.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/origin-energy/origin-energy-2026-08-07T190934.png
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
skill_count: 5
skills:
- name: origin-energy-cdr-consented-energy-data
  slug: origin-energy-cdr-consented-energy-data
- name: origin-energy-kraken-customer-migration
  slug: origin-energy-kraken-customer-migration
- name: origin-energy-kraken-graphql-account-operations
  slug: origin-energy-kraken-graphql-account-operations
- name: origin-energy-kraken-order-scheduling
  slug: origin-energy-kraken-order-scheduling
- name: origin-energy-retail-plan-comparison
  slug: origin-energy-retail-plan-comparison
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
