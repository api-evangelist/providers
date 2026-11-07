---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 102
  human_in_the_loop: 4
  name: Send21 Io Agentic Access
  operation_count: 146
  slug: send21-io-agentic-access
  summary_line: 146 operations · 102 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://send21.io
  baseurl_source: declared
  description: The Account API from send21-io — 2 operation(s) for account.
  name: send21-io Account API
  slug: send21-io-account-api
- baseURL: https://send21.io
  baseurl_source: declared
  description: The Auth API from send21-io — 26 operation(s) for auth.
  name: send21-io Auth API
  slug: send21-io-auth-api
- baseURL: https://send21.io
  baseurl_source: declared
  description: The Checkout API from send21-io — 3 operation(s) for checkout.
  name: send21-io Checkout API
  slug: send21-io-checkout-api
- baseURL: https://send21.io
  baseurl_source: declared
  description: The Demo API from send21-io — 3 operation(s) for demo.
  name: send21-io Demo API
  slug: send21-io-demo-api
- baseURL: https://send21.io
  baseurl_source: declared
  description: The Drafts API from send21-io — 13 operation(s) for drafts.
  name: send21-io Drafts API
  slug: send21-io-drafts-api
- baseURL: https://send21.io
  baseurl_source: declared
  description: The Fees API from send21-io — 3 operation(s) for fees.
  name: send21-io Fees API
  slug: send21-io-fees-api
- baseURL: https://send21.io
  baseurl_source: declared
  description: The Rates API from send21-io — 1 operation(s) for rates.
  name: send21-io Rates API
  slug: send21-io-rates-api
- baseURL: https://send21.io
  baseurl_source: declared
  description: The RecurringTemplates API from send21-io — 4 operation(s) for recurringtemplates.
  name: send21-io Recurring Templates API
  slug: send21-io-recurringtemplates-api
- baseURL: https://send21.io
  baseurl_source: declared
  description: The Suggestions API from send21-io — 1 operation(s) for suggestions.
  name: send21-io Suggestions API
  slug: send21-io-suggestions-api
- baseURL: https://send21.io
  baseurl_source: declared
  description: '**send21 calls your server when a draft changes.** Register an endpoint with `POST /api/v1/webhooks` (scope `webhooks:manage`) and pick the events you want. The response contains the signing secret on'
  name: send21-io Webhooks API
  slug: send21-io-webhooks-api
- baseURL: https://send21.io
  baseurl_source: declared
  description: The Address Book API from send21-io — 2 operation(s) for address book.
  name: send21-io Address Book API
  slug: send21-io-address-book-api
- baseURL: https://send21.io
  baseurl_source: declared
  description: The API Keys API from send21-io — 2 operation(s) for api keys.
  name: send21-io API Keys API
  slug: send21-io-api-keys-api
- baseURL: https://send21.io
  baseurl_source: declared
  description: The Payment Requests API from send21-io — 3 operation(s) for payment requests.
  name: send21-io Payment Requests API
  slug: send21-io-payment-requests-api
artifact_total: 27
asyncapis:
- description: ''
  name: Send21 Io Webhooks
  slug: send21-io-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/send21-io/agentic-access/send21-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/send21-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/send21-io/plans/send21-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/send21-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/send21-io/rules/send21-io-rules.yml
  title: ''
  type: Spectral
  url: rules/send21-io-rules.yml
- group: design
  href: https://artifacts.apis.io/send21-io/json-ld/send21-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/send21-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/send21-io/vocabulary/send21-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/send21-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/send21-io/asyncapi/send21-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/send21-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/send21-io/data-model/send21-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/send21-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/send21-io/conventions/send21-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/send21-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/send21-io/conventions/send21-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/send21-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/send21-io/security/send21-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/send21-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/send21-io/authentication/send21-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/send21-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/send21-io/errors/send21-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/send21-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/send21-io/conformance/send21-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/send21-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/send21-io/llms/send21-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/send21-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/send21-io/well-known/send21-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/send21-io-security.txt
- group: agent
  href: https://artifacts.apis.io/send21-io/well-known/send21-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/send21-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/send21-io/hosts/send21-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/send21-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/send21-io/vendors/send21-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/send21-io-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://send21.io/login
- group: auth
  href: https://artifacts.apis.io/send21-io/security/send21-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/send21-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/send21-io/security/send21-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/send21-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://send21.io/
- group: docs
  title: ''
  type: Documentation
  url: https://send21.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://send21.io/swagger/v1/swagger.json
- group: start
  title: ''
  type: GettingStarted
  url: https://send21.io/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://send21.io/about
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/send21io
- group: commercial
  title: ''
  type: Pricing
  url: https://send21.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://send21.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://send21.io/privacy
created: '2026-10-31'
description: Send21 provides a non-custodial crypto payment link service and API for people and AI agents. Users can create pay links or invoices priced in various cryptocurrencies, including BTC, USDC, USDT, EURC, SOL, and ETH, and pay directly from their wallets via on-chain or Lightning. The platform emphasizes security, stating that it never holds users' money or private keys, and offers documentation, pricing, and demo pages for developers and businesses.
image: https://send21.io/og/send21-card.png
json_schemas:
- name: CreateDraftRequest
  property_count: 14
  slug: send21-io-create-draft-request
- name: DemoDraftResponse
  property_count: 14
  slug: send21-io-demo-draft-response
- name: DraftResponse
  property_count: 39
  slug: send21-io-draft-response
- name: FeeBreakdownResponse
  property_count: 13
  slug: send21-io-fee-breakdown-response
- name: PaymentRequestResponse
  property_count: 20
  slug: send21-io-payment-request-response
- name: QuoteInfo
  property_count: 18
  slug: send21-io-quote-info
jsonld:
- class_count: 100
  name: Send21 Io Context
  property_count: 257
  slug: send21-io-context
layout: provider
modified: '2026-10-31'
name: send21-io
nav: Providers
network: true
overview: 'send21-io publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Auth API, Checkout API, and 10 more. Tagged areas include Company, Payments, Cryptocurrency, Non-Custodial, and Artificial Intelligence.


  The send21-io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  send21-io''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 24 more developer resources.'
plans:
- name: Send21 Io Plans Pricing
  plan_count: 1
  slug: send21-io-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: send21-io API Rules
  rule_count: 50
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 2
  slug: send21-io-rules
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 43.4
    contract_governance: 35.6
    contract_quality: 67.0
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/send21-io/send21-io-2026-11-03T143012.png
security:
- kind: authentication
  name: Send21 Io Authentication
  slug: send21-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Send21 Io Domain Security
  slug: send21-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Send21 Io Vulnerability Disclosure
  slug: send21-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: send21-io
tags:
- Company
- Payments
- Cryptocurrency
- Non-Custodial
- Artificial Intelligence
website: https://send21.io/
---
