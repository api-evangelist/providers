---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
api_count: 8
apis:
- baseURL: https://beta.api.ofx.com
  baseurl_source: declared
  description: The Authorization Code API from OFX — 1 operation(s) for authorization code.
  name: OFX Authorization Code API
  slug: ofx-authorization-code-api
- baseURL: https://beta.api.ofx.com
  baseurl_source: declared
  description: The Authorize API from OFX — 1 operation(s) for authorize.
  name: OFX Authorize API
  slug: ofx-authorize-api
- baseURL: https://beta.api.ofx.com
  baseurl_source: declared
  description: The Business API from OFX — 18 operation(s) for business.
  name: OFX Business API
  slug: ofx-business-api
- baseURL: https://beta.api.ofx.com
  baseurl_source: declared
  description: The Oauth API from OFX — 2 operation(s) for oauth.
  name: OFX OAuth API
  slug: ofx-oauth-api
- baseURL: https://beta.api.ofx.com
  baseurl_source: declared
  description: The Ofxrates API from OFX — 3 operation(s) for ofxrates.
  name: OFX Ofxrates API
  slug: ofx-ofxrates-api
- baseURL: https://beta.api.ofx.com
  baseurl_source: declared
  description: The Open Banking API from OFX — 5 operation(s) for open banking.
  name: OFX Open Banking API
  slug: ofx-open-banking-api
- baseURL: https://beta.api.ofx.com
  baseurl_source: declared
  description: The Refresh Token API from OFX — 1 operation(s) for refresh token.
  name: OFX Refresh Token API
  slug: ofx-refresh-token-api
- baseURL: https://beta.api.ofx.com
  baseurl_source: declared
  description: The Token API from OFX — 1 operation(s) for token.
  name: OFX Token API
  slug: ofx-token-api
artifact_total: 34
common:
- group: other
  href: https://artifacts.apis.io/ofx/vendors/ofx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ofx-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ofx/scopes/ofx-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ofx-scopes.yml
- group: auth
  href: https://artifacts.apis.io/ofx/authentication/ofx-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ofx-authentication.yml
- group: operate
  href: https://artifacts.apis.io/ofx/rate-limits/ofx-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ofx-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ofx/plans/ofx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ofx-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/ofx/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.ofx.com/docs/aisp-api/ZG9jOjQ1Mg-introduction
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.ofx.com/
- group: design
  href: https://artifacts.apis.io/ofx/rules/ofx-rules.yml
  title: ''
  type: Spectral
  url: rules/ofx-rules.yml
- group: design
  href: https://artifacts.apis.io/ofx/json-ld/ofx-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ofx-context.jsonld
- group: design
  href: https://artifacts.apis.io/ofx/vocabulary/ofx-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ofx-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ofx/data-model/ofx-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ofx-data-model.yml
- group: design
  href: https://artifacts.apis.io/ofx/conformance/ofx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ofx-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ofx/well-known/ofx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ofx-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://www.ofx.com/en-us/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ofx.com/en-us/legal/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://login.ofx.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ofx.com/
- group: auth
  href: https://artifacts.apis.io/ofx/security/ofx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ofx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ofx.com/en-us/
- group: company
  title: ''
  type: Blog
  url: https://www.ofx.com/en-us/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ofx.com/en-us/business/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.ofx.com/en-us/business/help/
created: '2026-09-22'
description: OFX provides a global money transfer platform enabling businesses and individuals to send payments in over 30 currencies to 180+ countries. It offers corporate cards, multi‑currency accounts, FX solutions, and integrated tools for accounting software like QuickBooks and Xero. The service includes spend management, fraud prevention, and a control hub for approvals and budgeting, catering to both personal and business financial needs.
finops:
- has_sources: true
  method: derived
  name: Ofx Finops
  primary_unit: seat
  service_category: ''
  slug: ofx-finops
  template: false
image: https://www.ofx.com/wp-content/uploads/2025/12/one-financial-platform-for-your-business-us-1024x858.png
json_schemas:
- name: GetOpenBankingV31AispAccountsResponse
  property_count: 10
  slug: ofx-get-open-banking-v31-aisp-accounts-response
- name: GetOpenBankingV31PispDealDealidResponse
  property_count: 17
  slug: ofx-get-open-banking-v31-pisp-deal-dealid-response
- name: GetV1BusinessBeneficiariesBeneficiaryidResponse
  property_count: 31
  slug: ofx-get-v1-business-beneficiaries-beneficiaryid-response
- name: GetV1BusinessConversionsConversionidResponse
  property_count: 22
  slug: ofx-get-v1-business-conversions-conversionid-response
- name: GetV1BusinessUsersUseridResponse
  property_count: 47
  slug: ofx-get-v1-business-users-userid-response
- name: GetV1OfxratesFromcurrencyTocurrencyAmountResponse
  property_count: 3
  slug: ofx-get-v1-ofxrates-fromcurrency-tocurrency-amount-response
- name: PatchV1BusinessBeneficiariesBeneficiaryidRequest
  property_count: 30
  slug: ofx-patch-v1-business-beneficiaries-beneficiaryid-request
- name: PatchV1BusinessBeneficiariesBeneficiaryidResponse
  property_count: 31
  slug: ofx-patch-v1-business-beneficiaries-beneficiaryid-response
- name: PostOpenBankingV31AispAccountAccessConsentsRequest
  property_count: 6
  slug: ofx-post-open-banking-v31-aisp-account-access-consents-request
- name: PostOpenBankingV31AispAccountAccessConsentsResponse
  property_count: 7
  slug: ofx-post-open-banking-v31-aisp-account-access-consents-response
- name: PostOpenBankingV31PispPaymentConsentRequest
  property_count: 2
  slug: ofx-post-open-banking-v31-pisp-payment-consent-request
- name: PostOpenBankingV31PispPaymentConsentResponse
  property_count: 6
  slug: ofx-post-open-banking-v31-pisp-payment-consent-response
- name: PostRefreshTokenResponse
  property_count: 5
  slug: ofx-post-refresh-token-response
- name: PostTokenRequest
  property_count: 4
  slug: ofx-post-token-request
- name: PostV1BusinessConversionsResponse
  property_count: 20
  slug: ofx-post-v1-business-conversions-response
- name: PostV1OauthTokenRequest
  property_count: 4
  slug: ofx-post-v1-oauth-token-request
jsonld:
- class_count: 45
  name: Ofx Context
  property_count: 213
  slug: ofx-context
layout: provider
modified: '2026-09-22'
name: OFX
nav: Providers
network: true
overview: 'OFX is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including Authorization Code API, Authorize API, Business API, and 5 more. Tagged areas include Company, Payments, Money Transfer, Fintech, and Banking.


  The OFX catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OFX''s developer surface includes authentication, getting-started guide, documentation, engineering blog, pricing, support, and 17 more developer resources.'
plans:
- name: Ofx Plans Pricing
  plan_count: 3
  slug: ofx-plans-pricing
- name: Ofx Price Estimates
  plan_count: 0
  slug: ofx-price-estimates
random_paper: 21
rate_limits:
- limit_count: 2
  name: Ofx Rate Limits
  slug: ofx-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: OFX API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: ofx-rules
scopes:
- name: Ofx Scopes
  scope_count: 1
  slug: ofx-scopes
  summary_line: 1 scope · clientCredentials/authorizationCode
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 88.8
    catalog_earned_first_party: 20.0
    catalog_gap: 26.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 61.8
    contract_governance: 22.0
    contract_quality: 25.4
    developer_ergonomics: 29.2
    discoverability: 71.4
    operational_transparency: 26.3
  previous_composite: 46.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 29.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ofx/ofx-2026-10-11T111819.png
security:
- kind: authentication
  name: Ofx Authentication
  slug: ofx-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ofx Domain Security
  slug: ofx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: ofx-create-beneficiary
  slug: ofx-create-beneficiary
slug: ofx
tags:
- Company
- Payments
- Money Transfer
- Fintech
- Banking
website: https://www.ofx.com/en-us/
---
