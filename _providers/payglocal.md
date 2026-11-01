---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: PayGlocal API provides endpoints for cross‑border payment operations as documented in the API Reference.
  name: PayGlocal API
  slug: payglocal-api-2
- baseURL: https://api.onboard.payglocal.in
  baseurl_source: declared
  description: 'PayGlocal API as documented publicly: 26 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: PayGlocal API
  slug: payglocal-api
artifact_total: 16
asyncapis:
- description: ''
  name: Payglocal Webhooks
  slug: payglocal-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/payglocal/plans/payglocal-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/payglocal-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/payglocal/rules/payglocal-rules.yml
  title: ''
  type: Spectral
  url: rules/payglocal-rules.yml
- group: design
  href: https://artifacts.apis.io/payglocal/json-ld/payglocal-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/payglocal-context.jsonld
- group: design
  href: https://artifacts.apis.io/payglocal/vocabulary/payglocal-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/payglocal-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/payglocal/asyncapi/payglocal-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/payglocal-webhooks.yml
- group: design
  href: https://artifacts.apis.io/payglocal/data-model/payglocal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/payglocal-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://payglocal.in/compliance
- group: auth
  href: https://artifacts.apis.io/payglocal/security/payglocal-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/payglocal-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/payglocal/authentication/payglocal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/payglocal-authentication.yml
- group: design
  href: https://artifacts.apis.io/payglocal/conformance/payglocal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/payglocal-conformance.yml
- group: agent
  href: https://artifacts.apis.io/payglocal/llms/payglocal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/payglocal-llms.txt
- group: other
  href: https://artifacts.apis.io/payglocal/a2a/payglocal-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/payglocal-a2a.yml
- group: auth
  href: https://artifacts.apis.io/payglocal/well-known/payglocal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/payglocal-security.txt
- group: auth
  href: https://artifacts.apis.io/payglocal/well-known/payglocal-partner-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/payglocal-partner-security.txt
- group: auth
  href: https://artifacts.apis.io/payglocal/well-known/payglocal-merchant-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/payglocal-merchant-security.txt
- group: auth
  href: https://artifacts.apis.io/payglocal/well-known/payglocal-dashboard-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/payglocal-dashboard-security.txt
- group: auth
  href: https://artifacts.apis.io/payglocal/well-known/payglocal-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/payglocal-api-security.txt
- group: agent
  href: https://artifacts.apis.io/payglocal/well-known/payglocal-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/payglocal-well-known.yml
- group: other
  href: https://artifacts.apis.io/payglocal/hosts/payglocal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/payglocal-hosts.yml
- group: other
  href: https://artifacts.apis.io/payglocal/vendors/payglocal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/payglocal-vendors.yml
- group: auth
  href: https://artifacts.apis.io/payglocal/security/payglocal-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/payglocal-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/payglocal/security/payglocal-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/payglocal-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/payglocal/security/payglocal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/payglocal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://payglocal.in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://payglocal.in/developers
- group: docs
  title: ''
  type: Documentation
  url: https://payglocal.in/docs/integration/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://payglocal.in/
- group: operate
  title: ''
  type: Support
  url: https://payglocal.in/contact
- group: company
  title: ''
  type: Blog
  url: https://payglocal.in/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://payglocal.in/pricing
coverage:
  checked: '2026-10-26'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://payglocal.in/docs/api-reference/onboarding-overview
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: PayGlocal provides a full‑stack cross‑border payments infrastructure authorised by the RBI in India. It enables merchants to accept international payments in multiple currencies, offering high success rates, real‑time FX, and biometric‑secured checkout. Serving over 12,000 merchants and 1 million global customers, PayGlocal supports Apple Pay, Google Pay, and a range of payment methods, helping businesses expand globally.
image: https://static.payglocal.in/icons/PayGlocalIconSquare.png
json_schemas:
- name: PostGccV2PartnerMerchantOnboardResponse
  property_count: 4
  slug: payglocal-post-gcc-v2-partner-merchant-onboard-response
- name: PostGlV1PaymentsGidRefundResponse
  property_count: 5
  slug: payglocal-post-gl-v1-payments-gid-refund-response
- name: PostGlV1PaymentsInitiatePaycollectRequest
  property_count: 15
  slug: payglocal-post-gl-v1-payments-initiate-paycollect-request
- name: PostGlV1PaymentsInitiateRequest
  property_count: 6
  slug: payglocal-post-gl-v1-payments-initiate-request
- name: PostGlV1PaymentsSiSaleRequest
  property_count: 6
  slug: payglocal-post-gl-v1-payments-si-sale-request
- name: PutGlV1PaymentsSiStatusRequest
  property_count: 4
  slug: payglocal-put-gl-v1-payments-si-status-request
jsonld:
- class_count: 13
  name: Payglocal Context
  property_count: 27
  slug: payglocal-context
layout: provider
modified: '2026-10-26'
name: PayGlocal
nav: Providers
network: true
overview: 'PayGlocal is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, FinTech, Cross-Border, and RBI-Authorized.


  The PayGlocal catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  PayGlocal''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Payglocal Plans Pricing
  plan_count: 4
  slug: payglocal-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: PayGlocal API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: payglocal-rules
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.9
    contract_governance: 22.0
    contract_quality: 32.6
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 18.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 28.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Payglocal Authentication
  slug: payglocal-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Payglocal Domain Security
  slug: payglocal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Payglocal Vulnerability Disclosure
  slug: payglocal-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Payglocal Trust Center
  slug: payglocal-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: payglocal
tags:
- Company
- Payments
- FinTech
- Cross-Border
- RBI-Authorized
website: https://payglocal.in/
---
