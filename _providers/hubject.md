---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 47
  human_in_the_loop: 14
  name: Hubject Agentic Access
  operation_count: 64
  slug: hubject-agentic-access
  summary_line: 64 operations · 47 acting · 14 human-in-the-loop
api_count: 3
apis:
- description: Open InterCharge Protocol (OICP) API for eRoaming services
  name: OICP eRoaming API
  slug: oicp-eroaming-api
artifact_total: 22
asyncapis:
- description: ''
  name: Hubject Webhooks
  slug: hubject-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.hubject.com/
- group: commercial
  href: https://artifacts.apis.io/hubject/plans/hubject-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hubject-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/hubject/hosts/hubject-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hubject-hosts.yml
- group: other
  href: https://artifacts.apis.io/hubject/vendors/hubject-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hubject-vendors.yml
- group: build
  href: https://artifacts.apis.io/hubject/packages/hubject-packages.yml
  title: ''
  type: SDKs
  url: packages/hubject-packages.yml
- group: build
  href: https://artifacts.apis.io/hubject/packages/hubject-packages.yml
  title: ''
  type: Packages
  url: packages/hubject-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.hubject.com/company/newsroom
- group: auth
  href: https://artifacts.apis.io/hubject/security/hubject-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hubject-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hubject.com
- group: operate
  title: ''
  type: Support
  url: https://support.hubject.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.hubject.com/newsroom
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hubject.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hubject.com/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hubject.com/imprint
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hubject
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://info.hubject.com/api/mcp
  - status: 401
    url: https://pardot.hubject.com/api/mcp
  - status: 403
    url: https://portal.hubject.com/mcp
  - status: 200
    url: https://www.hubject.com
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Hubject provides the world’s largest international eRoaming network for electric vehicle charging, connecting charge point operators, eMobility service providers and vehicle manufacturers across borders. Their intercharge platform enables seamless access to charging infrastructure, supporting plug‑and‑charge, settlement, analytics and certification services for a global EV ecosystem.
image: https://cdn.prod.website-files.com/602cf2b08109ccbc93d7f9ed/605b6eb0adff115b326d5c57_OpenGraph%20Hubject%20Image.png
json_schemas:
- name: eRoamingAuthorizationStart
  property_count: 7
  slug: hubject-e-roaming-authorization-start
- name: eRoamingChargeDetailRecord
  property_count: 18
  slug: hubject-e-roaming-charge-detail-record
- name: eRoamingChargeDetailRecords
  property_count: 11
  slug: hubject-e-roaming-charge-detail-records
- name: eRoamingChargingNotificationEnd
  property_count: 17
  slug: hubject-e-roaming-charging-notification-end
- name: eRoamingChargingNotificationError
  property_count: 9
  slug: hubject-e-roaming-charging-notification-error
- name: eRoamingChargingNotificationProgress
  property_count: 15
  slug: hubject-e-roaming-charging-notification-progress
- name: eRoamingPullEVSEData
  property_count: 12
  slug: hubject-e-roaming-pull-evsedata
- name: eRoamingPushEvseData
  property_count: 2
  slug: hubject-e-roaming-push-evse-data
- name: GetSignedContractDataRequest
  property_count: 3
  slug: hubject-get-signed-contract-data-request
- name: GetSignedContractDataResponse
  property_count: 1
  slug: hubject-get-signed-contract-data-response
- name: LookupContractResponse
  property_count: 1
  slug: hubject-lookup-contract-response
- name: ProvideSignedContractDataResponse
  property_count: 3
  slug: hubject-provide-contract-data-response
- name: SignedContractData
  property_count: 6
  slug: hubject-signed-contract-data-request
jsonld:
- class_count: 85
  name: Hubject Context
  property_count: 205
  slug: hubject-context
layout: provider
modified: '2026-10-14'
name: Hubject
nav: Providers
network: true
overview: 'Hubject publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Mobility, EV Charging, and Interoperability.


  The Hubject catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Hubject''s developer surface includes support, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Hubject Plans Pricing
  plan_count: 5
  slug: hubject-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Hubject API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 4
    warn: 1
  slug: hubject-rules
scopes:
- name: Hubject Scopes
  scope_count: 0
  slug: hubject-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 62.5
    catalog_earned_first_party: 12.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 64.2
    developer_ergonomics: 15.5
    discoverability: 63.4
    operational_transparency: 2.6
  previous_composite: 47.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 36.8
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 26.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/hubject/hubject-2026-11-03T133528.png
security:
- kind: authentication
  name: Hubject Authentication
  slug: hubject-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hubject Domain Security
  slug: hubject-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hubject
tags:
- Company
- E-Mobility
- EV Charging
- Interoperability
website: https://www.hubject.com
---
