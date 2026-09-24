---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-09-24'
api_count: 4
apis:
- baseURL: https://beta.api.ofx.com
  baseurl_source: declared
  description: 'OFX AISP API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: OFX AISP API
  slug: aisp-api
- baseURL: https://beta.api.ofx.com
  baseurl_source: declared
  description: 'OFX NCP API as documented publicly: 22 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: OFX NCP API
  slug: ncp-api
- baseURL: https://beta.api.ofx.com
  baseurl_source: declared
  description: 'OFX PISP API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: OFX PISP API
  slug: pisp-api
- baseURL: https://beta.api.ofx.com
  baseurl_source: declared
  description: 'OFX Rates API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: OFX Rates API
  slug: rates-api
artifact_total: 27
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ofx/refs/heads/main/vendors/ofx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ofx-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ofx/refs/heads/main/scopes/ofx-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ofx-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ofx/refs/heads/main/authentication/ofx-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ofx-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ofx/refs/heads/main/rate-limits/ofx-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ofx-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ofx/refs/heads/main/plans/ofx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ofx-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ofx/refs/heads/main/skills/_index.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/ofx/refs/heads/main/rules/ofx-rules.yml
  title: ''
  type: Spectral
  url: rules/ofx-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ofx/refs/heads/main/json-ld/ofx-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ofx-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ofx/refs/heads/main/vocabulary/ofx-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ofx-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ofx/refs/heads/main/data-model/ofx-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ofx-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ofx/refs/heads/main/conformance/ofx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ofx-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ofx/refs/heads/main/well-known/ofx-well-known.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/ofx/refs/heads/main/security/ofx-domain-security.yml
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
overview: 'OFX publishes 4 APIs on the [APIs.io](https://apis.io/) network, including AISP API, NCP API, PISP API, and 1 more. Tagged areas include Company, Payments, Money Transfer, Fintech, and Banking.


  The OFX catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OFX''s developer surface includes authentication, getting-started guide, documentation, engineering blog, pricing, support, and 17 more developer resources.'
plans:
- name: Ofx Plans Pricing
  plan_count: 3
  slug: ofx-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Ofx Rate Limits
  slug: ofx-rate-limits
rules:
- effective_rule_count: 51
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
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 86.8
    catalog_earned_first_party: 20.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.7
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 51.8
    discoverability: 74.1
    operational_transparency: 31.6
  previous_composite: 60.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 48.1
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ofx Authentication
  slug: ofx-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ofx Domain Security
  slug: ofx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ofx
tags:
- Company
- Payments
- Money Transfer
- Fintech
- Banking
website: https://www.ofx.com/en-us/
---
