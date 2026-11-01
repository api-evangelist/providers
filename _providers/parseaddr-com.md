---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Parseaddr Com Agentic Access
  operation_count: 16
  slug: parseaddr-com-agentic-access
  summary_line: 16 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.parseaddr.com
  baseurl_source: declared
  description: The Checkout API from parseaddr-com — 2 operation(s) for checkout.
  name: parseaddr-com Checkout API
  slug: parseaddr-com-checkout-api
- baseURL: https://api.parseaddr.com
  baseurl_source: declared
  description: The Credits API from parseaddr-com — 1 operation(s) for credits.
  name: parseaddr-com Credits API
  slug: parseaddr-com-credits-api
- baseURL: https://api.parseaddr.com
  baseurl_source: declared
  description: The Expand API from parseaddr-com — 1 operation(s) for expand.
  name: parseaddr-com Expand API
  slug: parseaddr-com-expand-api
- baseURL: https://api.parseaddr.com
  baseurl_source: declared
  description: The Health API from parseaddr-com — 1 operation(s) for health.
  name: parseaddr-com Health API
  slug: parseaddr-com-health-api
- baseURL: https://api.parseaddr.com
  baseurl_source: declared
  description: The Parse API from parseaddr-com — 1 operation(s) for parse.
  name: parseaddr-com Parse API
  slug: parseaddr-com-parse-api
- baseURL: https://api.parseaddr.com
  baseurl_source: declared
  description: The Signup API from parseaddr-com — 1 operation(s) for signup.
  name: parseaddr-com Signup API
  slug: parseaddr-com-signup-api
- baseURL: https://api.parseaddr.com
  baseurl_source: declared
  description: The Usage API from parseaddr-com — 1 operation(s) for usage.
  name: parseaddr-com Usage API
  slug: parseaddr-com-usage-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/parseaddr-com/agentic-access/parseaddr-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/parseaddr-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/parseaddr-com/plans/parseaddr-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/parseaddr-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/parseaddr-com/rules/parseaddr-com-rules.yml
  title: ''
  type: Spectral
  url: rules/parseaddr-com-rules.yml
- group: design
  href: https://artifacts.apis.io/parseaddr-com/json-ld/parseaddr-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/parseaddr-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/parseaddr-com/vocabulary/parseaddr-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/parseaddr-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/parseaddr-com/data-model/parseaddr-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/parseaddr-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/parseaddr-com/changelog/parseaddr-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/parseaddr-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/parseaddr-com/errors/parseaddr-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/parseaddr-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/parseaddr-com/conformance/parseaddr-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/parseaddr-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/parseaddr-com/llms/parseaddr-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/parseaddr-com-llms.txt
- group: other
  href: https://artifacts.apis.io/parseaddr-com/hosts/parseaddr-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/parseaddr-com-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://parseaddr.com/changelog
- group: auth
  href: https://artifacts.apis.io/parseaddr-com/authentication/parseaddr-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/parseaddr-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/parseaddr-com/security/parseaddr-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/parseaddr-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://parseaddr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://parseaddr.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://parseaddr.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://parseaddr.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://parseaddr.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://parseaddr.com/terms
created: '2026-10-30'
description: Parseaddr provides a hosted address parsing API built on libpostal, turning messy free‑text postal addresses into clean, structured components via a simple REST interface. It offers a generous free tier with 2,000 parses per month, transparent usage‑based pricing, and strong privacy guarantees – address data is processed in memory only and never stored. The service includes comprehensive OpenAPI documentation, a developer portal, pricing details, privacy policy, and support resources, enabling developers to integrate address normalization quickly and securely into applications.
json_schemas:
- name: CheckoutIn
  property_count: 2
  slug: parseaddr-com-checkout-in
- name: ExpandIn
  property_count: 1
  slug: parseaddr-com-expand-in
- name: ParseIn
  property_count: 2
  slug: parseaddr-com-parse-in
- name: SignupIn
  property_count: 2
  slug: parseaddr-com-signup-in
- name: TopupIn
  property_count: 1
  slug: parseaddr-com-topup-in
jsonld:
- class_count: 7
  name: Parseaddr Com Context
  property_count: 10
  slug: parseaddr-com-context
layout: provider
modified: '2026-10-30'
name: parseaddr-com
nav: Providers
network: true
overview: 'parseaddr-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Checkout API, Credits API, Expand API, and 4 more. Tagged areas include Company, Address, Parsing, API, and libpostal.


  The parseaddr-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  parseaddr-com''s developer surface includes changelog, authentication, documentation, API reference, pricing, and 15 more developer resources.'
plans:
- name: Parseaddr Com Plans Pricing
  plan_count: 4
  slug: parseaddr-com-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: parseaddr-com API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: parseaddr-com-rules
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 86.5
    catalog_earned_first_party: 0.0
    catalog_gap: 28.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 55.8
    developer_ergonomics: 28.6
    discoverability: 62.5
    operational_transparency: 15.8
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Parseaddr Com Authentication
  slug: parseaddr-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Parseaddr Com Domain Security
  slug: parseaddr-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: parseaddr-com
tags:
- Company
- Address
- Parsing
- API
- libpostal
website: https://parseaddr.com/
---
