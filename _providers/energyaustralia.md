---
access_model:
  confidence: high
  label: Public CDR product data · Consumer data accredited-only
  onboarding: unknown
  pricing: free
  public: true
  source:
  - review
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Energyaustralia Agentic Access
  operation_count: 27
  slug: energyaustralia-agentic-access
  summary_line: 27 operations
api_count: 2
apis:
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Data Holder Customer endpoints
  name: EnergyAustralia Data Holder Customers API
  slug: energyaustralia-data-holder-customers-api
- baseURL: https://cdr.energymadeeasy.gov.au/energyaustralia/cds-au/v1
  baseurl_source: declared
  description: Data Holder Operations endpoints
  name: EnergyAustralia Data Holder Operations API
  slug: energyaustralia-data-holder-operations-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Distributed Energy Resource endpoints
  name: EnergyAustralia Distributed Energy Resources API
  slug: energyaustralia-distributed-energy-resources-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Electricity Service Point endpoints
  name: EnergyAustralia Electricity Service Points API
  slug: energyaustralia-electricity-service-points-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Electricity Usage endpoints
  name: EnergyAustralia Electricity Usage API
  slug: energyaustralia-electricity-usage-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Energy Account Balance endpoints
  name: EnergyAustralia Energy Account Balances API
  slug: energyaustralia-energy-account-balances-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Energy Account Billing endpoints
  name: EnergyAustralia Energy Account Billing API
  slug: energyaustralia-energy-account-billing-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Energy Account endpoints
  name: EnergyAustralia Energy Accounts API
  slug: energyaustralia-energy-accounts-api
- baseURL: https://cdr.energymadeeasy.gov.au/energyaustralia/cds-au/v1
  baseurl_source: declared
  description: Energy Plan endpoints
  name: EnergyAustralia Energy Plans API
  slug: energyaustralia-energy-plans-api
artifact_total: 42
collections:
- collection_type: open
  name: CDR Common API
  slug: open-energyaustralia-cds-common-api
- collection_type: open
  name: CDR Energy API
  slug: open-energyaustralia-cds-energy-api
common:
- group: operate
  href: https://artifacts.apis.io/energyaustralia/rate-limits/energyaustralia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/energyaustralia-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/energyaustralia/rules/energyaustralia-rules.yml
  title: ''
  type: Spectral
  url: rules/energyaustralia-rules.yml
- group: design
  href: https://artifacts.apis.io/energyaustralia/json-ld/energyaustralia-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/energyaustralia-context.jsonld
- group: design
  href: https://artifacts.apis.io/energyaustralia/vocabulary/energyaustralia-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/energyaustralia-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/energyaustralia/overlays/energyaustralia-data-holder-customers-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/energyaustralia-data-holder-customers-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/energyaustralia/hosts/energyaustralia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/energyaustralia-hosts.yml
- group: build
  href: https://artifacts.apis.io/energyaustralia/integrations/energyaustralia-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/energyaustralia-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/energyaustralia/vendors/energyaustralia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/energyaustralia-vendors.yml
- group: agent
  href: https://artifacts.apis.io/energyaustralia/skills/energyaustralia-compare-energy-plans.md
  title: ''
  type: AgentSkill
  url: skills/energyaustralia-compare-energy-plans.md
- group: agent
  href: https://artifacts.apis.io/energyaustralia/skills/energyaustralia-check-status-and-outages.md
  title: ''
  type: AgentSkill
  url: skills/energyaustralia-check-status-and-outages.md
- group: agent
  href: https://artifacts.apis.io/energyaustralia/skills/energyaustralia-consumer-data-sharing.md
  title: ''
  type: AgentSkill
  url: skills/energyaustralia-consumer-data-sharing.md
- group: agent
  href: https://artifacts.apis.io/energyaustralia/skills/energyaustralia-usage-and-der.md
  title: ''
  type: AgentSkill
  url: skills/energyaustralia-usage-and-der.md
- group: agent
  href: https://artifacts.apis.io/energyaustralia/agentic-access/energyaustralia-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/energyaustralia-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/energyaustralia/security/energyaustralia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/energyaustralia-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/energyaustralia/authentication/energyaustralia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/energyaustralia-authentication.yml
- group: auth
  href: https://artifacts.apis.io/energyaustralia/scopes/energyaustralia-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/energyaustralia-scopes.yml
- group: design
  href: https://artifacts.apis.io/energyaustralia/conventions/energyaustralia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/energyaustralia-conventions.yml
- group: design
  href: https://artifacts.apis.io/energyaustralia/errors/energyaustralia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/energyaustralia-problem-types.yml
- group: design
  href: https://artifacts.apis.io/energyaustralia/lifecycle/energyaustralia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/energyaustralia-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://cdr.energymadeeasy.gov.au/energyaustralia/cds-au/v1/discovery/status
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#future-dated-obligations
- group: operate
  href: https://artifacts.apis.io/energyaustralia/changelog/energyaustralia-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/energyaustralia-changelog.yml
- group: design
  href: https://artifacts.apis.io/energyaustralia/conformance/energyaustralia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/energyaustralia-conformance.yml
- group: design
  href: https://artifacts.apis.io/energyaustralia/data-model/energyaustralia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/energyaustralia-data-model.yml
- group: agent
  href: https://artifacts.apis.io/energyaustralia/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.energyaustralia.com.au/
- group: other
  title: ''
  type: ConsumerDataRight
  url: https://www.energyaustralia.com.au/home/help-support/faqs/consumer-data-right
- group: other
  title: ''
  type: APIStandards
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#energy-apis
- group: docs
  title: ''
  type: Documentation
  url: https://www.energymadeeasy.gov.au/frequently-asked-questions/how-can-i-get-access-to-the-energy-made-easy-plan-data
- group: start
  title: ''
  type: CDRRegister
  url: https://api.cdr.gov.au/cdr-register/v1/energy/data-holders/brands/summary
- group: operate
  title: ''
  type: Support
  url: https://www.energyaustralia.com.au/home/help-and-support
- group: start
  title: ''
  type: SignUp
  url: https://www.energyaustralia.com.au/myaccount-login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.energyaustralia.com.au/home/electricity-and-gas/plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.energyaustralia.com.au/energyaustralia-website-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.energyaustralia.com.au/sites/default/files/2024-07/Privacy%20Policy.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/energyaustralia
created: '2026-07-27'
description: 'EnergyAustralia is one of Australia''s "big three" gentailers — a vertically integrated electricity and gas business owned by Hong Kong''s CLP Group and headquartered in Melbourne, generating from Yallourn, Mount Piper and Hallett alongside wind assets and retailing to more than 1.7 million residential and business customers across Victoria, New South Wales, Queensland, South Australia and the ACT. It sits on both sides of the National Electricity Market value chain: a scheduled generator into the NEM, and a retailer of record holding the customer relationship, the billing account and the meter data. Its API posture is entirely a function of the Consumer Data Right rather than of any product strategy. EnergyAustralia is a designated and live CDR energy data holder — brand id 1cc7833a-b834-ed11-a832-000d3a8830d6 in the ACCC CDR Register, public base URI https://authncdr.energyaustralia.com.au — but the only anonymously reachable contract carrying its name is the Product Reference
  Data surface, and that is hosted by the Australian Energy Regulator''s Energy Made Easy CDR gateway, not by EnergyAustralia. The company publishes no developer portal, no OpenAPI of its own, no open market or generation data, and no self-serve signup; its own gateway at api.energyaustralia.com.au (MuleSoft Anypoint) answers 403 to the public. Consumer usage, billing and DER data is real, standardised and live, but reachable only by an ACCC-accredited data recipient under consent. Open on plans, closed on everything else.'
image: https://www.energyaustralia.com.au/themes/custom/ea/assets/images/EA_logo.svg
json_schemas:
- name: EnergyAccountDetailResponseV4
  property_count: 3
  slug: energyaustralia-energy-account-detail-response-v4
- name: EnergyAccountListResponseV2
  property_count: 3
  slug: energyaustralia-energy-account-list-response-v2
- name: EnergyBalanceListResponse
  property_count: 3
  slug: energyaustralia-energy-balance-list-response
- name: EnergyBalanceResponse
  property_count: 3
  slug: energyaustralia-energy-balance-response
- name: EnergyBillingListResponseV3
  property_count: 3
  slug: energyaustralia-energy-billing-list-response-v3
- name: EnergyConcessionsResponse
  property_count: 3
  slug: energyaustralia-energy-concessions-response
- name: EnergyDerDetailResponse
  property_count: 3
  slug: energyaustralia-energy-der-detail-response
- name: EnergyDerListResponse
  property_count: 3
  slug: energyaustralia-energy-der-list-response
- name: EnergyInvoiceListResponse
  property_count: 3
  slug: energyaustralia-energy-invoice-list-response
- name: EnergyPaymentScheduleResponse
  property_count: 3
  slug: energyaustralia-energy-payment-schedule-response
- name: EnergyPlanListResponse
  property_count: 3
  slug: energyaustralia-energy-plan-list-response
- name: EnergyPlanResponseV3
  property_count: 3
  slug: energyaustralia-energy-plan-response-v3
- name: EnergyServicePointDetailResponseV2
  property_count: 3
  slug: energyaustralia-energy-service-point-detail-response-v2
- name: EnergyServicePointListResponseV2
  property_count: 3
  slug: energyaustralia-energy-service-point-list-response-v2
- name: EnergyUsageListResponse
  property_count: 3
  slug: energyaustralia-energy-usage-list-response
- name: ResponseCommonCustomerDetailV2
  property_count: 3
  slug: energyaustralia-response-common-customer-detail-v2
- name: ResponseCommonCustomer
  property_count: 3
  slug: energyaustralia-response-common-customer
- name: ResponseCommonDiscoveryStatus
  property_count: 3
  slug: energyaustralia-response-common-discovery-status
- name: ResponseDiscoveryOutagesList
  property_count: 3
  slug: energyaustralia-response-discovery-outages-list
jsonld:
- class_count: 120
  name: Energyaustralia Context
  property_count: 308
  slug: energyaustralia-context
layout: provider
modified: '2026-10-21'
name: EnergyAustralia
nav: Providers
network: true
overview: 'EnergyAustralia publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data Holder Customers API, Data Holder Operations API, Distributed Energy Resources API, and 6 more. Tagged areas include Energy, Australia, Utilities, Electricity, and Gas.


  The EnergyAustralia catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EnergyAustralia''s developer surface includes authentication, changelog, API reference, documentation, support, signup flow, pricing, and 30 more developer resources.'
plans:
- name: Energyaustralia Plans Pricing
  plan_count: 0
  slug: energyaustralia-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 15
  name: Energyaustralia Rate Limits
  slug: energyaustralia-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: EnergyAustralia API Rules
  rule_count: 16
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 0
  slug: energyaustralia-rules
scopes:
- name: Energyaustralia Scopes
  scope_count: 12
  slug: energyaustralia-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 19.7
    contract_quality: 58.3
    developer_ergonomics: 35.1
    discoverability: 57.1
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 34.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/energyaustralia/energyaustralia-2026-08-07T164911.png
security:
- kind: authentication
  name: Energyaustralia Authentication
  slug: energyaustralia-authentication
  summary_line: none/mutualTLS/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Energyaustralia Domain Security
  slug: energyaustralia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: energyaustralia-check-status-and-outages
  slug: energyaustralia-check-status-and-outages
- name: energyaustralia-compare-energy-plans
  slug: energyaustralia-compare-energy-plans
- name: energyaustralia-consumer-data-sharing
  slug: energyaustralia-consumer-data-sharing
- name: energyaustralia-usage-and-der
  slug: energyaustralia-usage-and-der
slug: energyaustralia
tags:
- Energy
- Australia
- Utilities
- Electricity
- Gas
- Energy Retailer
- Consumer Data Right
- CDR
- Product Reference Data
- Smart Metering
- Energy Markets
- Renewables
website: https://www.energyaustralia.com.au/
---
