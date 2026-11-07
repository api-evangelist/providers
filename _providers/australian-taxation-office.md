---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Australian Taxation Office Agentic Access
  operation_count: 20
  slug: australian-taxation-office-agentic-access
  summary_line: 20 operations · 8 acting
api_count: 8
apis:
- baseURL: https://api.ato.gov.au/idp/v1/relyingparties
  baseurl_source: declared
  description: This will return the status and version of the API
  name: Australian Taxation Office API Info API
  slug: australian-taxation-office-apiinfo-api
- baseURL: https://api.ato.gov.au/idp/v1/relyingparties
  baseurl_source: declared
  description: The Combined Global and Domestic Group Entity Tax Return API from Australian Taxation Office — 1 operation(s) for combined global and domestic group entity tax return.
  name: Australian Taxation Office Combined Global and Domestic Group Entity Tax Return API
  slug: australian-taxation-office-combined-global-and-domestic-group-entity-tax-return-api
- baseURL: https://api.ato.gov.au/idp/v1/relyingparties
  baseurl_source: declared
  description: The Combined Global and Domestic Minimum Tax Return API from Australian Taxation Office — 1 operation(s) for combined global and domestic minimum tax return.
  name: Australian Taxation Office Combined Global and Domestic Minimum Tax Return API
  slug: australian-taxation-office-combined-global-and-domestic-minimum-tax-return-api
- baseURL: https://api.ato.gov.au/idp/v1/relyingparties
  baseurl_source: declared
  description: The Get Payee Stapled Super Fund for Receipt API from Australian Taxation Office — 1 operation(s) for get payee stapled super fund for receipt.
  name: Australian Taxation Office Get Payee Stapled Super Fund for Receipt API
  slug: australian-taxation-office-get-payee-stapled-super-fund-for-receipt-api
- baseURL: https://api.ato.gov.au/idp/v1/relyingparties
  baseurl_source: declared
  description: The Get Payment Reference Number API from Australian Taxation Office — 1 operation(s) for get payment reference number.
  name: Australian Taxation Office Get Payment Reference Number API
  slug: australian-taxation-office-get-payment-reference-number-api
- baseURL: https://api.ato.gov.au/idp/v1/relyingparties
  baseurl_source: declared
  description: The GST Property Settlement Date Confirmation API from Australian Taxation Office — 2 operation(s) for gst property settlement date confirmation.
  name: Australian Taxation Office GST Property Settlement Date Confirmation API
  slug: australian-taxation-office-gst-property-settlement-date-confirmation-api
- baseURL: https://api.ato.gov.au/idp/v1/relyingparties
  baseurl_source: declared
  description: The GST Property Settlement Withholding Notification API from Australian Taxation Office — 2 operation(s) for gst property settlement withholding notification.
  name: Australian Taxation Office GST Property Settlement Withholding Notification API
  slug: australian-taxation-office-gst-property-settlement-withholding-notification-api
- baseURL: https://api.ato.gov.au/idp/v1/relyingparties
  baseurl_source: declared
  description: This will make sure the DSG is running successfully and will return a successful response
  name: Australian Taxation Office Heartbeat API
  slug: australian-taxation-office-heartbeat-api
- baseURL: https://api.ato.gov.au/idp/v1/relyingparties
  baseurl_source: declared
  description: This endpoint returns a list of SMSF messaging providers
  name: Australian Taxation Office Providers API
  slug: australian-taxation-office-providers-api
- baseURL: https://api.ato.gov.au/idp/v1/relyingparties
  baseurl_source: declared
  description: The Register a new software application instance API from Australian Taxation Office — 1 operation(s) for register a new software application instance.
  name: Australian Taxation Office Register a new software application instance API
  slug: australian-taxation-office-register-a-new-software-application-instance-api
- baseURL: https://api.ato.gov.au/idp/v1/relyingparties
  baseurl_source: declared
  description: The Request Stapled Super Fund for Payee API from Australian Taxation Office — 1 operation(s) for request stapled super fund for payee.
  name: Australian Taxation Office Request Stapled Super Fund for Payee API
  slug: australian-taxation-office-request-stapled-super-fund-for-payee-api
- baseURL: https://api.ato.gov.au/idp/v1/relyingparties
  baseurl_source: declared
  description: This will allow the specs to be viewed either in a browser or do a file download of the API spec
  name: Australian Taxation Office Spec API
  slug: australian-taxation-office-spec-api
artifact_total: 36
common:
- group: agent
  href: https://artifacts.apis.io/australian-taxation-office/agentic-access/australian-taxation-office-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/australian-taxation-office-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/australian-taxation-office/rate-limits/australian-taxation-office-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/australian-taxation-office-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/australian-taxation-office/rules/australian-taxation-office-rules.yml
  title: ''
  type: Spectral
  url: rules/australian-taxation-office-rules.yml
- group: design
  href: https://artifacts.apis.io/australian-taxation-office/json-ld/australian-taxation-office-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/australian-taxation-office-context.jsonld
- group: design
  href: https://artifacts.apis.io/australian-taxation-office/vocabulary/australian-taxation-office-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/australian-taxation-office-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/australian-taxation-office/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/australian-taxation-office/data-model/australian-taxation-office-data-model.yml
  title: ''
  type: DataModel
  url: data-model/australian-taxation-office-data-model.yml
- group: operate
  href: https://artifacts.apis.io/australian-taxation-office/changelog/australian-taxation-office-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/australian-taxation-office-changelog.yml
- group: design
  href: https://artifacts.apis.io/australian-taxation-office/conventions/australian-taxation-office-conventions.yml
  title: ''
  type: Conventions
  url: conventions/australian-taxation-office-conventions.yml
- group: start
  href: https://artifacts.apis.io/australian-taxation-office/sandbox/australian-taxation-office-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/australian-taxation-office-sandbox.yml
- group: design
  href: https://artifacts.apis.io/australian-taxation-office/lifecycle/australian-taxation-office-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/australian-taxation-office-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/australian-taxation-office/errors/australian-taxation-office-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/australian-taxation-office-error-codes.yml
- group: design
  href: https://artifacts.apis.io/australian-taxation-office/errors/australian-taxation-office-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/australian-taxation-office-problem-types.yml
- group: design
  href: https://artifacts.apis.io/australian-taxation-office/conformance/australian-taxation-office-conformance.yml
  title: ''
  type: Conformance
  url: conformance/australian-taxation-office-conformance.yml
- group: other
  href: https://artifacts.apis.io/australian-taxation-office/overlays/australian-taxation-office-global-domestic-minimum-group-entity-tax-return-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/australian-taxation-office-global-domestic-minimum-group-entity-tax-return-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/australian-taxation-office/well-known/australian-taxation-office-apiportal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/australian-taxation-office-apiportal-security.txt
- group: auth
  href: https://artifacts.apis.io/australian-taxation-office/well-known/australian-taxation-office-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/australian-taxation-office-api-security.txt
- group: agent
  href: https://artifacts.apis.io/australian-taxation-office/well-known/australian-taxation-office-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/australian-taxation-office-well-known.yml
- group: other
  href: https://artifacts.apis.io/australian-taxation-office/hosts/australian-taxation-office-hosts.yml
  title: ''
  type: Hosts
  url: hosts/australian-taxation-office-hosts.yml
- group: other
  href: https://artifacts.apis.io/australian-taxation-office/vendors/australian-taxation-office-vendors.yml
  title: ''
  type: Vendors
  url: vendors/australian-taxation-office-vendors.yml
- group: auth
  href: https://artifacts.apis.io/australian-taxation-office/scopes/australian-taxation-office-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/australian-taxation-office-scopes.yml
- group: auth
  href: https://artifacts.apis.io/australian-taxation-office/authentication/australian-taxation-office-authentication.yml
  title: ''
  type: Authentication
  url: authentication/australian-taxation-office-authentication.yml
- group: auth
  href: https://artifacts.apis.io/australian-taxation-office/security/australian-taxation-office-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/australian-taxation-office-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ato.gov.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apiportal.ato.gov.au/
- group: docs
  title: ''
  type: APIReference
  url: https://apiportal.ato.gov.au/api-products
- group: start
  title: ''
  type: GettingStarted
  url: https://apiportal.ato.gov.au/getting-started
- group: operate
  title: ''
  type: Support
  url: https://apiportal.ato.gov.au/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apiportal.ato.gov.au/conditions-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apiportal.ato.gov.au/privacy
created: '2026-10-22'
description: The Australian Taxation Office (ATO) is the Australian Government's principal revenue collection agency, administering the tax and superannuation systems. Through the ATO API Portal (apiportal.ato.gov.au) it gives digital service providers (DSPs) an API product catalogue with documentation and subscriptions, listing APIs such as SMSF Alias Lookup, the Digital Services Gateway Health Check, Stapled Super Fund, OAuth Dynamic Client Registration, Global and Domestic Minimum Tax lodgment and the GST Property Settlement Service.
image: https://apiportal.ato.gov.au/themes/custom/b5_apigee/logo.svg
json_schemas:
- name: CombinedMinimumGlobalDomesticReturnRequest
  property_count: 8
  slug: australian-taxation-office-combined-minimum-global-domestic-return-request
- name: GlobalDomesticMinimumGroupEntityTaxReturnRequest
  property_count: 2
  slug: australian-taxation-office-global-domestic-minimum-group-entity-tax-return-request
- name: GlobalDomesticMinimumGroupEntityTaxReturnResponse
  property_count: 1
  slug: australian-taxation-office-global-domestic-minimum-group-entity-tax-return-response
- name: GlobalDomesticMinimumTaxReturnResponse
  property_count: 2
  slug: australian-taxation-office-global-domestic-minimum-tax-return-response
- name: GSTPropertySettlementDateConfirmationRequest
  property_count: 1
  slug: australian-taxation-office-gstproperty-settlement-date-confirmation-request
- name: GSTPropertySettlementWithholdingNotificationRequest
  property_count: 1
  slug: australian-taxation-office-gstproperty-settlement-withholding-notification-request
- name: HeartbeatInfoResponse
  property_count: 3
  slug: australian-taxation-office-heartbeat-info-response
- name: ProviderListResponse
  property_count: 1
  slug: australian-taxation-office-provider-list-response
- name: RelyingParty
  property_count: 13
  slug: australian-taxation-office-relying-party
- name: StapledSuperFundRequest
  property_count: 2
  slug: australian-taxation-office-stapled-super-fund-request
- name: StapledSuperFundResponse
  property_count: 2
  slug: australian-taxation-office-stapled-super-fund-response
- name: TransactionPaymentReferenceNumberResponse
  property_count: 1
  slug: australian-taxation-office-transaction-payment-reference-number-response
jsonld:
- class_count: 73
  name: Australian Taxation Office Context
  property_count: 177
  slug: australian-taxation-office-context
layout: provider
modified: '2026-10-22'
name: Australian Taxation Office
nav: Providers
network: true
overview: 'Australian Taxation Office publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Info API, Combined Global and Domestic Group Entity Tax Return API, Combined Global and Domestic Minimum Tax Return API, and 9 more. Tagged areas include Company, Government, Taxation, Superannuation, and Australia.


  The Australian Taxation Office catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Australian Taxation Office''s developer surface includes changelog, sandbox, authentication, API reference, getting-started guide, support, and 24 more developer resources.'
plans:
- name: Australian Taxation Office Plans Pricing
  plan_count: 0
  slug: australian-taxation-office-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Australian Taxation Office Rate Limits
  slug: australian-taxation-office-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Australian Taxation Office API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: australian-taxation-office-rules
scopes:
- name: Australian Taxation Office Scopes
  scope_count: 4
  slug: australian-taxation-office-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 59.9
    developer_ergonomics: 42.3
    discoverability: 71.4
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/australian-taxation-office/australian-taxation-office-2026-11-03T121349.png
security:
- kind: authentication
  name: Australian Taxation Office Authentication
  slug: australian-taxation-office-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Australian Taxation Office Domain Security
  slug: australian-taxation-office-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: dsg-health-check
  slug: australian-taxation-office-dsg-health-check
- name: global-domestic-minimum-tax-return
  slug: australian-taxation-office-global-domestic-minimum-tax-return
- name: payment-reference-number
  slug: australian-taxation-office-payment-reference-number
- name: stapled-super-fund-lookup
  slug: australian-taxation-office-stapled-super-fund-lookup
slug: australian-taxation-office
tags:
- Company
- Government
- Taxation
- Superannuation
- Australia
- Digital Service Providers
- Public Sector
website: https://ato.gov.au/
---
