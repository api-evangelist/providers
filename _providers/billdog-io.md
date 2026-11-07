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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.billdog.io
  baseurl_source: declared
  description: 'BillDog API as documented publicly: 41 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: BillDog API
  slug: billdog-io-api
artifact_total: 16
asyncapis:
- description: ''
  name: Billdog Io Webhooks
  slug: billdog-io-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/billdog-io/rate-limits/billdog-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/billdog-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/billdog-io/plans/billdog-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/billdog-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/billdog-io/rules/billdog-io-rules.yml
  title: ''
  type: Spectral
  url: rules/billdog-io-rules.yml
- group: design
  href: https://artifacts.apis.io/billdog-io/json-ld/billdog-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/billdog-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/billdog-io/vocabulary/billdog-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/billdog-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/billdog-io/asyncapi/billdog-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/billdog-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/billdog-io/data-model/billdog-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/billdog-io-data-model.yml
- group: build
  href: https://artifacts.apis.io/billdog-io/cli/billdog-io-cli.yml
  title: ''
  type: CLI
  url: cli/billdog-io-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://billdog.io/security
- group: auth
  href: https://artifacts.apis.io/billdog-io/authentication/billdog-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/billdog-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/billdog-io/conformance/billdog-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/billdog-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/billdog-io/llms/billdog-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/billdog-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/billdog-io/well-known/billdog-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/billdog-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/billdog-io/hosts/billdog-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billdog-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/billdog-io/vendors/billdog-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billdog-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/billdog-io/packages/billdog-io-packages.yml
  title: ''
  type: SDKs
  url: packages/billdog-io-packages.yml
- group: build
  href: https://artifacts.apis.io/billdog-io/packages/billdog-io-packages.yml
  title: ''
  type: Packages
  url: packages/billdog-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://billdog.io/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://billdog.io/status
- group: auth
  title: ''
  type: Security
  url: https://billdog.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://billdog.io/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://billdog.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://billdog.io/blog
- group: docs
  title: ''
  type: APIReference
  url: https://billdog.io/docs/api-reference
- group: auth
  href: https://artifacts.apis.io/billdog-io/security/billdog-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/billdog-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/billdog-io/security/billdog-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/billdog-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/billdog-io/security/billdog-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billdog-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://billdog.io/
- group: docs
  title: ''
  type: Documentation
  url: https://billdog.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://billdog.io/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://billdog.io/demo
- group: operate
  title: ''
  type: Support
  url: https://billdog.io/contact
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was found on the API host.
  evidence:
  - status: 404
    url: https://api.billdog.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BillDog provides AI‑native paywalls, product analytics, and a unified platform for monetization, user engagement, and data insights. It offers tools for paywall creation, analytics dashboards, messaging, surveys, journeys, authentication, virtual currency, session replay, and feature flags, targeting developers and product teams seeking integrated revenue and analytics solutions.
image: https://billdog.io/og-default.png
json_schemas:
- name: PostFunctionsV1CreateWebCheckoutRequest
  property_count: 10
  slug: billdog-io-post-functions-v1-create-web-checkout-request
- name: PostFunctionsV1CreateWebCheckoutResponse
  property_count: 11
  slug: billdog-io-post-functions-v1-create-web-checkout-response
- name: PostFunctionsV1RedeemPurchaseRequest
  property_count: 1
  slug: billdog-io-post-functions-v1-redeem-purchase-request
- name: PostFunctionsV1RedeemPurchaseResponse
  property_count: 18
  slug: billdog-io-post-functions-v1-redeem-purchase-response
- name: PostV1IngestEventsRequest
  property_count: 4
  slug: billdog-io-post-v1-ingest-events-request
- name: PostV1VirtualCurrencyTransactionsRequest
  property_count: 5
  slug: billdog-io-post-v1-virtual-currency-transactions-request
jsonld:
- class_count: 6
  name: Billdog Io Context
  property_count: 40
  slug: billdog-io-context
layout: provider
modified: '2026-11-02'
name: BillDog
nav: Providers
network: true
overview: 'BillDog is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Analytics, Monetization, Software-as-a-Service, and Platform.


  The BillDog catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BillDog''s developer surface includes CLI, authentication, changelog, engineering blog, API reference, documentation, pricing, and 25 more developer resources.'
plans:
- name: Billdog Io Plans Pricing
  plan_count: 5
  slug: billdog-io-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Billdog Io Rate Limits
  slug: billdog-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: BillDog API Rules
  rule_count: 44
  severity_counts:
    error: 40
    hint: 0
    info: 2
    warn: 2
  slug: billdog-io-rules
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 33.7
    developer_ergonomics: 44.0
    discoverability: 66.1
    operational_transparency: 60.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Billdog Io Authentication
  slug: billdog-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Billdog Io Domain Security
  slug: billdog-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Billdog Io Vulnerability Disclosure
  slug: billdog-io-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Billdog Io Trust Center
  slug: billdog-io-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: billdog-io
tags:
- Artificial Intelligence
- Analytics
- Monetization
- Software-as-a-Service
- Platform
- Company
website: https://billdog.io/
---
