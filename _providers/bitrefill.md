---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bitrefill Agentic Access
  operation_count: 11
  slug: bitrefill-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.bitrefill.com
  baseurl_source: declared
  description: Orders and eSIMs for the paying wallet (SIWX).
  name: Bitrefill Account API
  slug: bitrefill-account-api
- baseURL: https://api.bitrefill.com
  baseurl_source: declared
  description: Product details and invoice creation.
  name: Bitrefill Checkout API
  slug: bitrefill-checkout-api
- baseURL: https://api.bitrefill.com
  baseurl_source: declared
  description: Search and browse the catalog (micro-fee per call).
  name: Bitrefill Discovery API
  slug: bitrefill-discovery-api
- baseURL: https://api.bitrefill.com
  baseurl_source: declared
  description: Invoice payment and status.
  name: Bitrefill Payments API
  slug: bitrefill-payments-api
artifact_total: 13
asyncapis:
- description: ''
  name: Bitrefill Webhooks
  slug: bitrefill-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/bitrefill/agentic-access/bitrefill-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bitrefill-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/bitrefill/rate-limits/bitrefill-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bitrefill-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/bitrefill/rules/bitrefill-rules.yml
  title: ''
  type: Spectral
  url: rules/bitrefill-rules.yml
- group: design
  href: https://artifacts.apis.io/bitrefill/json-ld/bitrefill-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bitrefill-context.jsonld
- group: design
  href: https://artifacts.apis.io/bitrefill/vocabulary/bitrefill-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bitrefill-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bitrefill/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bitrefill/asyncapi/bitrefill-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bitrefill-webhooks.yml
- group: design
  href: https://artifacts.apis.io/bitrefill/data-model/bitrefill-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bitrefill-data-model.yml
- group: auth
  href: https://artifacts.apis.io/bitrefill/security/bitrefill-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bitrefill-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bitrefill/authentication/bitrefill-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bitrefill-authentication.yml
- group: design
  href: https://artifacts.apis.io/bitrefill/errors/bitrefill-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bitrefill-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bitrefill/conformance/bitrefill-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bitrefill-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bitrefill/llms/bitrefill-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitrefill-llms.txt
- group: auth
  href: https://artifacts.apis.io/bitrefill/well-known/bitrefill-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bitrefill-security.txt
- group: auth
  href: https://artifacts.apis.io/bitrefill/well-known/bitrefill-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bitrefill-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/bitrefill/well-known/bitrefill-bitrefill-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bitrefill-bitrefill-security.txt
- group: agent
  href: https://artifacts.apis.io/bitrefill/well-known/bitrefill-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bitrefill-well-known.yml
- group: other
  href: https://artifacts.apis.io/bitrefill/hosts/bitrefill-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitrefill-hosts.yml
- group: other
  href: https://artifacts.apis.io/bitrefill/vendors/bitrefill-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitrefill-vendors.yml
- group: build
  href: https://artifacts.apis.io/bitrefill/packages/bitrefill-packages.yml
  title: ''
  type: SDKs
  url: packages/bitrefill-packages.yml
- group: build
  href: https://artifacts.apis.io/bitrefill/packages/bitrefill-packages.yml
  title: ''
  type: Packages
  url: packages/bitrefill-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.bitrefill.com
- group: start
  title: ''
  type: Login
  url: https://www.bitrefill.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.bitrefill.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitrefill
- group: auth
  href: https://artifacts.apis.io/bitrefill/security/bitrefill-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bitrefill-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bitrefill/security/bitrefill-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitrefill-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bitrefill.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bitrefill.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bitrefill.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bitrefill.com/docs/quickstart-2
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bitrefill.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.bitrefill.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bitrefill.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitrefill.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.bitrefill.com/openapi.json
  - status: 401
    url: https://api.bitrefill.com/mcp
  - status: 200
    url: https://www.bitrefill.com
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Bitrefill enables users to buy gift cards, top‑up mobile airtime, and purchase eSIMs using Bitcoin and other cryptocurrencies. The platform offers a wide range of digital and physical products, supports multiple currencies, and provides a crypto‑friendly payment experience for global customers.
image: https://cdn.bitrefill.com/content/cn/b_auto%2Cc_pad%2Ch_630%2Cw_1200/v23/landing%2Fsocial.webp
jsonld:
- class_count: 1
  name: Bitrefill Context
  property_count: 2
  slug: bitrefill-context
layout: provider
modified: '2026-11-02'
name: Bitrefill
nav: Providers
network: true
overview: 'Bitrefill publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Checkout API, Discovery API, and 1 more. Tagged areas include Company, Cryptocurrency, Payments, Gift Cards, and Mobile Top-Up.


  The Bitrefill catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bitrefill''s developer surface includes authentication, support, documentation, API reference, getting-started guide, pricing, engineering blog, and 28 more developer resources.'
random_paper: 21
rate_limits:
- limit_count: 1
  name: Bitrefill Rate Limits
  slug: bitrefill-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Bitrefill API Rules
  rule_count: 48
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 2
  slug: bitrefill-rules
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 55.8
    catalog_earned_first_party: 8.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 57.3
    developer_ergonomics: 43.5
    discoverability: 66.1
    operational_transparency: 42.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bitrefill Authentication
  slug: bitrefill-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bitrefill Domain Security
  slug: bitrefill-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bitrefill Vulnerability Disclosure
  slug: bitrefill-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: bitrefill-account-view-orders-and-esims
  slug: bitrefill-account-view-orders-and-esims
slug: bitrefill
tags:
- Company
- Cryptocurrency
- Payments
- Gift Cards
- Mobile Top-Up
website: https://www.bitrefill.com
---
