---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'pieterpost-com API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: pieterpost-com API
  slug: pieterpost-com-api
artifact_total: 19
common:
- group: design
  href: https://artifacts.apis.io/pieterpost-com/rules/pieterpost-com-rules.yml
  title: ''
  type: Spectral
  url: rules/pieterpost-com-rules.yml
- group: design
  href: https://artifacts.apis.io/pieterpost-com/json-ld/pieterpost-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pieterpost-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/pieterpost-com/vocabulary/pieterpost-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pieterpost-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/pieterpost-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/pieterpost-com/data-model/pieterpost-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pieterpost-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/pieterpost-com/changelog/pieterpost-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pieterpost-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/pieterpost-com/conventions/pieterpost-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/pieterpost-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/pieterpost-com/conventions/pieterpost-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pieterpost-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/pieterpost-com/security/pieterpost-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/pieterpost-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pieterpost-com/authentication/pieterpost-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pieterpost-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/pieterpost-com/conformance/pieterpost-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pieterpost-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pieterpost-com/llms/pieterpost-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pieterpost-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/pieterpost-com/well-known/pieterpost-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pieterpost-com-security.txt
- group: auth
  href: https://artifacts.apis.io/pieterpost-com/well-known/pieterpost-com-partner-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pieterpost-com-partner-security.txt
- group: agent
  href: https://artifacts.apis.io/pieterpost-com/well-known/pieterpost-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pieterpost-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/pieterpost-com/hosts/pieterpost-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pieterpost-com-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://pieterpost.com/en/registered-mail-delivery-times/
- group: company
  title: ''
  type: Newsroom
  url: https://pieterpost.com/en/press/
- group: operate
  title: ''
  type: ChangeLog
  url: https://pieterpost.com/en/changelog/
- group: auth
  href: https://artifacts.apis.io/pieterpost-com/security/pieterpost-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pieterpost-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pieterpost-com/security/pieterpost-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pieterpost-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pieterpost.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pieterpost.com/api/docs.md
- group: docs
  title: ''
  type: APIReference
  url: https://pieterpost.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://pieterpost.com/api/docs.md
- group: operate
  title: ''
  type: Support
  url: https://pieterpost.com/en/help/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pieterpost.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pieterpost.com/en/privacy/
created: '2026-10-30'
description: PieterPost provides an online service that enables users to compose letters and postcards in a web interface or upload PDF/image files, then have them printed, stamped, and mailed through postal partners. The platform handles address entry, bulk mailing, and offers API endpoints for creating orders, adding test credits, checking order status, and managing address books, eliminating the need for physical stamps or visits to a post office. It serves both personal and business communications, supporting international delivery and offering features such as registered mail, tracking, and secure handling of content.
image: https://pieterpost.com/svgs/pieterpost_stamp.svg
json_schemas:
- name: GetV1OrdersOrderidResponse
  property_count: 6
  slug: pieterpost-com-get-v1-orders-orderid-response
- name: GetV1WalletResponse
  property_count: 7
  slug: pieterpost-com-get-v1-wallet-response
- name: PostV1CheckoutLinksRequest
  property_count: 5
  slug: pieterpost-com-post-v1-checkout-links-request
- name: PostV1CreditsTopupsResponse
  property_count: 10
  slug: pieterpost-com-post-v1-credits-topups-response
- name: PostV1OrdersRequest
  property_count: 5
  slug: pieterpost-com-post-v1-orders-request
- name: PostV1OrdersResponse
  property_count: 21
  slug: pieterpost-com-post-v1-orders-response
jsonld:
- class_count: 7
  name: Pieterpost Com Context
  property_count: 40
  slug: pieterpost-com-context
layout: provider
modified: '2026-10-30'
name: pieterpost-com
nav: Providers
network: true
overview: 'pieterpost-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mail, Postal, Printing, API, and Letters.


  The pieterpost-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  pieterpost-com''s developer surface includes changelog, authentication, signup flow, documentation, API reference, getting-started guide, support, and 21 more developer resources.'
plans:
- name: Pieterpost Com Plans Pricing
  plan_count: 0
  slug: pieterpost-com-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: pieterpost-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: pieterpost-com-rules
scopes:
- name: Pieterpost Com Scopes
  scope_count: 0
  slug: pieterpost-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 51.7
    discoverability: 58.9
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pieterpost Com Authentication
  slug: pieterpost-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pieterpost Com Domain Security
  slug: pieterpost-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pieterpost Com Vulnerability Disclosure
  slug: pieterpost-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: pieterpost-com-checkout-links
  slug: pieterpost-com-checkout-links
- name: pieterpost-com-credits
  slug: pieterpost-com-credits
- name: pieterpost-com-orders
  slug: pieterpost-com-orders
- name: pieterpost-com-uploads
  slug: pieterpost-com-uploads
- name: pieterpost-com-wallet
  slug: pieterpost-com-wallet
slug: pieterpost-com
tags:
- Mail
- Postal
- Printing
- API
- Letters
- Postcards
website: https://pieterpost.com/
---
