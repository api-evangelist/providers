---
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'canopypay-io API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: canopypay-io API
  slug: canopypay-io-api
artifact_total: 13
asyncapis:
- description: ''
  name: Canopypay Io Webhooks
  slug: canopypay-io-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/canopypay-io/rate-limits/canopypay-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/canopypay-io-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/canopypay-io/rules/canopypay-io-rules.yml
  title: ''
  type: Spectral
  url: rules/canopypay-io-rules.yml
- group: design
  href: https://artifacts.apis.io/canopypay-io/json-ld/canopypay-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/canopypay-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/canopypay-io/vocabulary/canopypay-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/canopypay-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/canopypay-io/asyncapi/canopypay-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/canopypay-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/canopypay-io/data-model/canopypay-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/canopypay-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/canopypay-io/authentication/canopypay-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/canopypay-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/canopypay-io/conformance/canopypay-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canopypay-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/canopypay-io/llms/canopypay-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canopypay-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/canopypay-io/well-known/canopypay-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canopypay-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/canopypay-io/hosts/canopypay-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canopypay-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/canopypay-io/vendors/canopypay-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canopypay-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/canopypay-io/packages/canopypay-io-packages.yml
  title: ''
  type: Packages
  url: packages/canopypay-io-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.canopypay.io/webhooks
- group: build
  title: ''
  type: SDKs
  url: https://www.canopypay.io/sdk/events
- group: auth
  href: https://artifacts.apis.io/canopypay-io/security/canopypay-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canopypay-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canopypay.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.canopypay.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.canopypay.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.canopay.io/quickstart
- group: auth
  href: https://artifacts.apis.io/canopypay-io/security/canopypay-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canopypay-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canopypay.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.canopypay.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.canopypay.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.canopypay.io/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://www.canopypay.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.canopypay.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.canopypay.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.canopypay.io/support
- group: company
  title: ''
  type: Blog
  url: https://www.canopypay.io/articles
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://www.canopypay.io/api/mcp
  - status: 200
    url: https://canopypay.io/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Canopy provides a universal crypto deposit API that enables per‑user deposit addresses across multiple blockchains. Developers can integrate deposit, checkout, and withdrawal flows directly into their applications, allowing users to fund with any supported token and receive payouts to chosen wallets. The platform supports over ten networks, offers webhooks, and includes comprehensive documentation and SDKs for seamless integration.
image: https://www.canopypay.io/opengraph-image?bc7770cec7442438
json_schemas:
- name: GetApiV1IntentsResponse
  property_count: 4
  slug: canopypay-io-get-api-v1-intents-response
- name: GetAuthMethodsResponse
  property_count: 1
  slug: canopypay-io-get-auth-methods-response
- name: PostApiV1IntentsIdSourceInboxRequest
  property_count: 4
  slug: canopypay-io-post-api-v1-intents-id-source-inbox-request
- name: PostApiV1IntentsRequest
  property_count: 2
  slug: canopypay-io-post-api-v1-intents-request
- name: PostApiV1IntentsResponse
  property_count: 4
  slug: canopypay-io-post-api-v1-intents-response
- name: PostAuthMagicLinksRequest
  property_count: 1
  slug: canopypay-io-post-auth-magic-links-request
jsonld:
- class_count: 11
  name: Canopypay Io Context
  property_count: 18
  slug: canopypay-io-context
layout: provider
modified: '2026-10-30'
name: canopypay-io
nav: Providers
network: true
overview: 'canopypay-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include FinTech, Crypto, Payments, API, and Deposit.


  The canopypay-io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  canopypay-io''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 23 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 5
  name: Canopypay Io Rate Limits
  slug: canopypay-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: canopypay-io API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: canopypay-io-rules
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 83.5
    catalog_earned_first_party: 0.0
    catalog_gap: 31.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 79.1
    contract_quality: 61.0
    developer_ergonomics: 54.8
    discoverability: 57.1
    operational_transparency: 36.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Canopypay Io Authentication
  slug: canopypay-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Canopypay Io Domain Security
  slug: canopypay-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: canopypay-io
tags:
- FinTech
- Crypto
- Payments
- API
- Deposit
website: https://canopypay.io/
---
