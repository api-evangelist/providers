---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
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
  score: 25.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.cross-deck.com
  baseurl_source: declared
  description: 'Crossdeck API as documented publicly: 33 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Crossdeck API
  slug: cross-deck-com-api
artifact_total: 13
asyncapis:
- description: ''
  name: Cross Deck Com Webhooks
  slug: cross-deck-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/cross-deck-com/plans/cross-deck-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cross-deck-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cross-deck-com/rules/cross-deck-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cross-deck-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cross-deck-com/json-ld/cross-deck-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cross-deck-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cross-deck-com/vocabulary/cross-deck-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cross-deck-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cross-deck-com/asyncapi/cross-deck-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cross-deck-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/cross-deck-com/data-model/cross-deck-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cross-deck-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/cross-deck-com/cli/cross-deck-com-cli.yml
  title: ''
  type: CLI
  url: cli/cross-deck-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/cross-deck-com/changelog/cross-deck-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cross-deck-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/cross-deck-com/conventions/cross-deck-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cross-deck-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/cross-deck-com/conventions/cross-deck-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cross-deck-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/cross-deck-com/authentication/cross-deck-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cross-deck-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/cross-deck-com/conformance/cross-deck-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cross-deck-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cross-deck-com/llms/cross-deck-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cross-deck-com-llms.txt
- group: other
  href: https://artifacts.apis.io/cross-deck-com/hosts/cross-deck-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cross-deck-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cross-deck-com/vendors/cross-deck-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cross-deck-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cross-deck.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cross-deck.com/
- group: auth
  title: ''
  type: Security
  url: https://cross-deck.com/legal/security/
- group: start
  title: ''
  type: Login
  url: https://cross-deck.com/sign-in/
- group: operate
  title: ''
  type: ChangeLog
  url: https://cross-deck.com/docs/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://cross-deck.com/docs/quickstart-web
- group: auth
  href: https://artifacts.apis.io/cross-deck-com/security/cross-deck-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cross-deck-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cross-deck.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cross-deck.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://cross-deck.com/docs/api-reference/
- group: commercial
  title: ''
  type: Pricing
  url: https://cross-deck.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://cross-deck.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cross-deck.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cross-deck.com/legal/privacy/
- group: operate
  title: ''
  type: Support
  url: https://cross-deck.com/contact/
coverage:
  checked: '2026-11-04'
  detail: The provider's documentation pages are HTML without a discoverable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec.
  evidence:
  - status: 200
    url: https://cross-deck.com/docs/api-reference/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Crossdeck provides a unified SDK for subscription revenue, product analytics, and error tracking across platforms. It consolidates signals into a single customer timeline, supporting Apple, Google Play, Stripe, and web integrations. The service offers a free tier until your app generates revenue, aiming to simplify monetization and insight for developers.
image: https://cross-deck.com/assets/og-card.jpg
json_schemas:
- name: GetV1ConfigResponse
  property_count: 10
  slug: cross-deck-com-get-v1-config-response
- name: GetV1EntitlementsVerifyResponse
  property_count: 10
  slug: cross-deck-com-get-v1-entitlements-verify-response
- name: PostV1IdentityAliasRequest
  property_count: 6
  slug: cross-deck-com-post-v1-identity-alias-request
- name: PostV1MigrationUsersRequest
  property_count: 11
  slug: cross-deck-com-post-v1-migration-users-request
- name: PostV1MigrationUsersResponse
  property_count: 14
  slug: cross-deck-com-post-v1-migration-users-response
- name: PostV1ServerCustomersCustomeridGrantRequest
  property_count: 3
  slug: cross-deck-com-post-v1-server-customers-customerid-grant-request
jsonld:
- class_count: 41
  name: Cross Deck Com Context
  property_count: 80
  slug: cross-deck-com-context
layout: provider
modified: '2026-11-04'
name: Crossdeck
nav: Providers
network: true
overview: 'Crossdeck is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SDK, Monetization, Analytics, Error Tracking, and Subscription.


  The Crossdeck catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Crossdeck''s developer surface includes CLI, changelog, authentication, getting-started guide, documentation, API reference, pricing, and 23 more developer resources.'
plans:
- name: Cross Deck Com Plans Pricing
  plan_count: 5
  slug: cross-deck-com-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Crossdeck API Rules
  rule_count: 47
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 3
  slug: cross-deck-com-rules
score:
  band: strong
  composite: 56.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 35.6
    contract_quality: 36.1
    developer_ergonomics: 54.8
    discoverability: 66.1
    operational_transparency: 50.0
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
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cross Deck Com Authentication
  slug: cross-deck-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cross Deck Com Domain Security
  slug: cross-deck-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cross-deck-com
tags:
- SDK
- Monetization
- Analytics
- Error Tracking
- Subscription
website: https://cross-deck.com/
---
