---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: ReferralCandy provides referral and affiliate program software for e‑commerce platforms.
  name: ReferralCandy API
  slug: referralcandy-api-2
- baseURL: https://my.referralcandy.com
  baseurl_source: declared
  description: 'ReferralCandy API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: ReferralCandy API
  slug: referralcandy-api
artifact_total: 15
common:
- group: commercial
  href: https://artifacts.apis.io/referralcandy/plans/referralcandy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/referralcandy-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/referralcandy/rules/referralcandy-rules.yml
  title: ''
  type: Spectral
  url: rules/referralcandy-rules.yml
- group: design
  href: https://artifacts.apis.io/referralcandy/json-ld/referralcandy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/referralcandy-context.jsonld
- group: design
  href: https://artifacts.apis.io/referralcandy/vocabulary/referralcandy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/referralcandy-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/referralcandy/data-model/referralcandy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/referralcandy-data-model.yml
- group: design
  href: https://artifacts.apis.io/referralcandy/conformance/referralcandy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/referralcandy-conformance.yml
- group: agent
  href: https://artifacts.apis.io/referralcandy/llms/referralcandy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/referralcandy-llms.txt
- group: auth
  href: https://artifacts.apis.io/referralcandy/well-known/referralcandy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/referralcandy-security.txt
- group: auth
  href: https://artifacts.apis.io/referralcandy/well-known/referralcandy-referralcandy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/referralcandy-referralcandy-security.txt
- group: auth
  href: https://artifacts.apis.io/referralcandy/well-known/referralcandy-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/referralcandy-help-security.txt
- group: agent
  href: https://artifacts.apis.io/referralcandy/well-known/referralcandy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/referralcandy-well-known.yml
- group: other
  href: https://artifacts.apis.io/referralcandy/hosts/referralcandy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/referralcandy-hosts.yml
- group: other
  href: https://artifacts.apis.io/referralcandy/vendors/referralcandy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/referralcandy-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.referralcandy.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://help.referralcandy.com/en/
- group: auth
  title: ''
  type: Security
  url: https://www.referralcandy.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.referralcandy.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.referralcandy.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.referralcandy.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://help.referralcandy.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ReferralCandy
- group: auth
  href: https://artifacts.apis.io/referralcandy/security/referralcandy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/referralcandy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/referralcandy/security/referralcandy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/referralcandy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://referralcandy.com/
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, GraphQL, or other machine‑readable API specification was found on ReferralCandy's site; only HTML pages and 404 responses were returned.
  evidence:
  - status: 404
    url: https://www.referralcandy.com/api-docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: ReferralCandy provides a referral and affiliate program platform for e‑commerce businesses, enabling merchants to create, manage, and track customer referral campaigns. The service offers automated reward distribution, fraud protection, detailed analytics, and integrations with major e‑commerce platforms such as Shopify, WooCommerce, and Klaviyo. It helps brands grow through word‑of‑mouth marketing by turning satisfied customers into brand advocates.
image: https://www.referralcandy.com/images/og-default.png
json_schemas:
- name: GetApiV22ContactsJsonResponse
  property_count: 16
  slug: referralcandy-get-api-v22-contacts-json-response
- name: GetApiV22ReferralsJsonResponse
  property_count: 11
  slug: referralcandy-get-api-v22-referrals-json-response
- name: GetApiV22RewardsJsonResponse
  property_count: 9
  slug: referralcandy-get-api-v22-rewards-json-response
- name: PostApiV22PurchaseJsonRequest
  property_count: 16
  slug: referralcandy-post-api-v22-purchase-json-request
- name: PostApiV22RewardsJsonRequest
  property_count: 5
  slug: referralcandy-post-api-v22-rewards-json-request
- name: PostApiV22RewardsJsonResponse
  property_count: 4
  slug: referralcandy-post-api-v22-rewards-json-response
- name: PostApiV22SignupJsonRequest
  property_count: 8
  slug: referralcandy-post-api-v22-signup-json-request
- name: PostApiV22SignupJsonResponse
  property_count: 7
  slug: referralcandy-post-api-v22-signup-json-response
jsonld:
- class_count: 2
  name: Referralcandy Context
  property_count: 9
  slug: referralcandy-context
layout: provider
modified: '2026-10-27'
name: ReferralCandy
nav: Providers
network: true
overview: 'ReferralCandy is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Referrals, Affiliates, E-Commerce, and Marketing.


  The ReferralCandy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ReferralCandy''s developer surface includes support, pricing, engineering blog, documentation, and 20 more developer resources.'
plans:
- name: Referralcandy Plans Pricing
  plan_count: 4
  slug: referralcandy-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: ReferralCandy API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: referralcandy-rules
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 21.3
    developer_ergonomics: 8.3
    discoverability: 64.3
    operational_transparency: 7.9
  previous_composite: 34.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/referralcandy/referralcandy-2026-11-03T142114.png
security:
- kind: domain-security
  name: Referralcandy Domain Security
  slug: referralcandy-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Referralcandy Vulnerability Disclosure
  slug: referralcandy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: referralcandy
tags:
- Company
- Referrals
- Affiliates
- E-Commerce
- Marketing
website: https://referralcandy.com/
---
