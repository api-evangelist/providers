---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
  name: Agl Energy Agentic Access
  operation_count: 27
  slug: agl-energy-agentic-access
  summary_line: 27 operations
api_count: 2
apis:
- baseURL: https://public.cdr.agl.com.au/cds-au/v1
  baseurl_source: declared
  description: Data Holder Customer endpoints
  name: AGL Energy Data Holder Customers API
  slug: agl-energy-data-holder-customers-api
- baseURL: https://public.cdr.agl.com.au/cds-au/v1
  baseurl_source: declared
  description: Data Holder Operations endpoints
  name: AGL Energy Data Holder Operations API
  slug: agl-energy-data-holder-operations-api
- baseURL: https://public.cdr.agl.com.au/cds-au/v1
  baseurl_source: declared
  description: Distributed Energy Resource endpoints
  name: AGL Energy Distributed Energy Resources API
  slug: agl-energy-distributed-energy-resources-api
- baseURL: https://public.cdr.agl.com.au/cds-au/v1
  baseurl_source: declared
  description: Electricity Service Point endpoints
  name: AGL Energy Electricity Service Points API
  slug: agl-energy-electricity-service-points-api
- baseURL: https://public.cdr.agl.com.au/cds-au/v1
  baseurl_source: declared
  description: Electricity Usage endpoints
  name: AGL Energy Electricity Usage API
  slug: agl-energy-electricity-usage-api
- baseURL: https://public.cdr.agl.com.au/cds-au/v1
  baseurl_source: declared
  description: Energy Account Balance endpoints
  name: AGL Energy Account Balances API
  slug: agl-energy-energy-account-balances-api
- baseURL: https://public.cdr.agl.com.au/cds-au/v1
  baseurl_source: declared
  description: Energy Account Billing endpoints
  name: AGL Energy Account Billing API
  slug: agl-energy-energy-account-billing-api
- baseURL: https://public.cdr.agl.com.au/cds-au/v1
  baseurl_source: declared
  description: Energy Account endpoints
  name: AGL Energy Accounts API
  slug: agl-energy-energy-accounts-api
- baseURL: https://cdr.energymadeeasy.gov.au/agl/cds-au/v1
  baseurl_source: declared
  description: Energy Plan endpoints
  name: AGL Energy Plans API
  slug: agl-energy-energy-plans-api
artifact_total: 43
collections:
- collection_type: open
  name: CDR Common API
  slug: open-agl-energy-cds-common
- collection_type: open
  name: CDR Energy API
  slug: open-agl-energy-cds-energy
common:
- group: operate
  href: https://artifacts.apis.io/agl-energy/rate-limits/agl-energy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agl-energy-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/agl-energy/rules/agl-energy-rules.yml
  title: ''
  type: Spectral
  url: rules/agl-energy-rules.yml
- group: design
  href: https://artifacts.apis.io/agl-energy/json-ld/agl-energy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agl-energy-context.jsonld
- group: design
  href: https://artifacts.apis.io/agl-energy/vocabulary/agl-energy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agl-energy-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/agl-energy/overlays/agl-energy-data-holder-customers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agl-energy-data-holder-customers-overlay.yaml
- group: other
  href: https://artifacts.apis.io/agl-energy/hosts/agl-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agl-energy-hosts.yml
- group: build
  href: https://artifacts.apis.io/agl-energy/integrations/agl-energy-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/agl-energy-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/agl-energy/vendors/agl-energy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agl-energy-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agl-energy/security/agl-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agl-energy-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/agl-energy/agentic-access/agl-energy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agl-energy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/agl-energy/authentication/agl-energy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agl-energy-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agl-energy/scopes/agl-energy-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agl-energy-scopes.yml
- group: design
  href: https://artifacts.apis.io/agl-energy/conventions/agl-energy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agl-energy-conventions.yml
- group: design
  href: https://artifacts.apis.io/agl-energy/errors/agl-energy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agl-energy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agl-energy/data-model/agl-energy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agl-energy-data-model.yml
- group: design
  href: https://artifacts.apis.io/agl-energy/lifecycle/agl-energy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agl-energy-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://public.cdr.agl.com.au/cds-au/v1/discovery/status
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#endpoint-version-schedule
- group: operate
  href: https://artifacts.apis.io/agl-energy/changelog/agl-energy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agl-energy-changelog.yml
- group: design
  href: https://artifacts.apis.io/agl-energy/conformance/agl-energy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agl-energy-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agl-energy/mcp/agl-energy-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/agl-energy-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agl-energy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/agl-energy/llms/agl-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agl-energy-llms.txt
- group: auth
  href: https://artifacts.apis.io/agl-energy/security/agl-energy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agl-energy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.agl.com.au/terms-conditions/responsible-disclosure-policy
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#energy-apis
- group: company
  title: ''
  type: Website
  url: https://www.agl.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.agl.com.au/consumer-data-right-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agl.com.au/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agl.com.au/terms-conditions/online-services
- group: operate
  title: ''
  type: Support
  url: https://www.agl.com.au/help-support/account-setup-management/manage-consumer-data-right
- group: operate
  title: ''
  type: Forum
  url: https://neighbourhood.agl.com.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AGLEnergy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agl-energy
- group: other
  title: ''
  type: Registration
  url: https://api.cdr.gov.au/cdr-register/v1/all/data-holders/brands/summary
created: '2026-07-27'
description: 'AGL Energy Limited (ASX:AGL) is Australia''s oldest listed company — founded in Sydney in 1837 as the Australian Gas Light Company — and one of the country''s largest integrated energy businesses, retailing electricity, gas, broadband and mobile to roughly four million customer accounts while owning the nation''s largest electricity generation portfolio (Bayswater and Loy Yang A coal, gas peakers, hydro, wind, utility-scale solar and grid-scale batteries). It sits at both ends of the Australian value chain: generator and wholesale market participant in the NEM, and the retailer of record that holds the customer relationship, the billing account and the metering data. Its API posture is entirely a product of regulation, not of product strategy. AGL publishes no public developer portal and no self-serve API programme — apideveloper.agl.com.au resolves through Akamai but returns HTTP 403 to every anonymous client, and agl.com.au itself is bot-blocked at 403. What AGL does expose
  is the Consumer Data Right: it is a designated CDR energy data holder, listed on the CDR Register under brand "AGL" with public base URI https://public.cdr.agl.com.au, and that surface is real and verified — GET /cds-au/v1/discovery/status and /cds-au/v1/discovery/outages both return HTTP 200 with conformant Consumer Data Standards envelopes, and AGL''s own outage notices describe scheduled downtime of the "AGL CDR Consent flow". Its energy plan Product Reference Data is genuinely open and anonymous — 1,343 plans at https://cdr.energymadeeasy.gov.au/agl/cds-au/v1/energy/plans — but that endpoint is operated centrally by the Australian Energy Regulator, not by AGL, which is the structural difference from CDR banking where every bank serves its own PRD. Consumer usage, billing, service point, DER and account data is available only to Accredited Data Recipients, over mTLS, under a consumer authorisation, with the base URI distributed through the CDR Register rather than published. AGL is
  therefore open on product data, closed to everyone but accredited recipients on consumer data, and silent everywhere else — it publishes no open grid or market data of its own. It is also migrating around four million customer services onto the Kaluza platform under a A$150m, 20 percent stake taken in 2024, so the retail data layer behind these mandated endpoints is being rebuilt on a third-party energy operating system.'
image: https://agl.com.au/content/dam/digital/agl/images/logos/agl/agl-vertical-gradient.svg
json_schemas:
- name: EnergyAccountDetailResponseV4
  property_count: 3
  slug: agl-energy-energy-account-detail-response-v4
- name: EnergyAccountListResponseV2
  property_count: 3
  slug: agl-energy-energy-account-list-response-v2
- name: EnergyBalanceListResponse
  property_count: 3
  slug: agl-energy-energy-balance-list-response
- name: EnergyBalanceResponse
  property_count: 3
  slug: agl-energy-energy-balance-response
- name: EnergyBillingListResponseV3
  property_count: 3
  slug: agl-energy-energy-billing-list-response-v3
- name: EnergyConcessionsResponse
  property_count: 3
  slug: agl-energy-energy-concessions-response
- name: EnergyDerDetailResponse
  property_count: 3
  slug: agl-energy-energy-der-detail-response
- name: EnergyDerListResponse
  property_count: 3
  slug: agl-energy-energy-der-list-response
- name: EnergyInvoiceListResponse
  property_count: 3
  slug: agl-energy-energy-invoice-list-response
- name: EnergyPaymentScheduleResponse
  property_count: 3
  slug: agl-energy-energy-payment-schedule-response
- name: EnergyPlanListResponse
  property_count: 3
  slug: agl-energy-energy-plan-list-response
- name: EnergyPlanResponseV3
  property_count: 3
  slug: agl-energy-energy-plan-response-v3
- name: EnergyServicePointDetailResponseV2
  property_count: 3
  slug: agl-energy-energy-service-point-detail-response-v2
- name: EnergyServicePointListResponseV2
  property_count: 3
  slug: agl-energy-energy-service-point-list-response-v2
- name: EnergyUsageListResponse
  property_count: 3
  slug: agl-energy-energy-usage-list-response
- name: ResponseCommonCustomerDetailV2
  property_count: 3
  slug: agl-energy-response-common-customer-detail-v2
- name: ResponseCommonCustomer
  property_count: 3
  slug: agl-energy-response-common-customer
- name: ResponseCommonDiscoveryStatus
  property_count: 3
  slug: agl-energy-response-common-discovery-status
- name: ResponseDiscoveryOutagesList
  property_count: 3
  slug: agl-energy-response-discovery-outages-list
jsonld:
- class_count: 120
  name: Agl Energy Context
  property_count: 300
  slug: agl-energy-context
layout: provider
modified: '2026-10-20'
name: AGL Energy
nav: Providers
network: true
overview: 'AGL Energy publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data Holder Customers API, Data Holder Operations API, Distributed Energy Resources API, and 6 more. Tagged areas include Energy, Australia, Utilities, Electricity, and Gas.


  The AGL Energy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AGL Energy''s developer surface includes authentication, changelog, API reference, documentation, support, and 30 more developer resources.'
plans:
- name: Agl Energy Plans Pricing
  plan_count: 0
  slug: agl-energy-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 7
  name: Agl Energy Rate Limits
  slug: agl-energy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: AGL Energy API Rules
  rule_count: 16
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 0
  slug: agl-energy-rules
scopes:
- name: Agl Energy Scopes
  scope_count: 11
  slug: agl-energy-scopes
  summary_line: 11 scopes
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 74.0
    catalog_earned_first_party: 12.0
    catalog_gap: 41.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 33.3
    contract_quality: 26.0
    developer_ergonomics: 35.1
    discoverability: 66.1
    operational_transparency: 86.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 39.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agl Energy Authentication
  slug: agl-energy-authentication
  summary_line: oauth2/openIdConnect/mutualTLS/none · 3 schemes
- kind: domain-security
  name: Agl Energy Domain Security
  slug: agl-energy-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Agl Energy Vulnerability Disclosure
  slug: agl-energy-vulnerability-disclosure
  summary_line: Hackerone · security.txt
skill_count: 4
skills:
- name: agl-energy-account-billing-review
  slug: agl-energy-account-billing-review
- name: agl-energy-check-cdr-availability
  slug: agl-energy-check-cdr-availability
- name: agl-energy-compare-retail-plans
  slug: agl-energy-compare-retail-plans
- name: agl-energy-consumer-usage-and-der
  slug: agl-energy-consumer-usage-and-der
slug: agl-energy
tags:
- Energy
- Australia
- Utilities
- Electricity
- Gas
- Energy Retailer
- Consumer Data Right
- CDR
- Smart Metering
- Solar
- DER
- Renewables
- Energy Markets
website: https://www.agl.com.au/
---
