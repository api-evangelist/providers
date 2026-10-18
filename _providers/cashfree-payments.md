---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.4
  scored_at: '2026-10-17'
api_count: 3
apis:
- baseURL: https://sandbox.cashfree.com
  baseurl_source: declared
  description: The Orders API from Cashfree Payments — 1 operation(s) for orders.
  name: Cashfree Payments Orders API
  slug: cashfree-payments-orders-api
- baseURL: https://sandbox.cashfree.com
  baseurl_source: declared
  description: The Payout API from Cashfree Payments — 1 operation(s) for payout.
  name: Cashfree Payments Payout API
  slug: cashfree-payments-payout-api
- baseURL: https://sandbox.cashfree.com
  baseurl_source: declared
  description: The Pg API from Cashfree Payments — 6 operation(s) for pg.
  name: Cashfree Payments Pg API
  slug: cashfree-payments-pg-api
artifact_total: 16
asyncapis:
- description: ''
  name: Cashfree Payments Webhooks
  slug: cashfree-payments-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/well-known/cashfree-payments-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cashfree-payments-clarity-security.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/plans/cashfree-payments-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cashfree-payments-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/rules/cashfree-payments-rules.yml
  title: ''
  type: Spectral
  url: rules/cashfree-payments-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/json-ld/cashfree-payments-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cashfree-payments-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/vocabulary/cashfree-payments-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cashfree-payments-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/asyncapi/cashfree-payments-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cashfree-payments-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/data-model/cashfree-payments-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cashfree-payments-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/cli/cashfree-payments-cli.yml
  title: ''
  type: CLI
  url: cli/cashfree-payments-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/conventions/cashfree-payments-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cashfree-payments-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/conventions/cashfree-payments-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cashfree-payments-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/authentication/cashfree-payments-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cashfree-payments-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/conformance/cashfree-payments-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cashfree-payments-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/llms/cashfree-payments-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cashfree-payments-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/a2a/cashfree-payments-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cashfree-payments-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/well-known/cashfree-payments-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cashfree-payments-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/hosts/cashfree-payments-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cashfree-payments-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/vendors/cashfree-payments-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cashfree-payments-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/packages/cashfree-payments-packages.yml
  title: ''
  type: SDKs
  url: packages/cashfree-payments-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/packages/cashfree-payments-packages.yml
  title: ''
  type: Packages
  url: packages/cashfree-payments-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cashfree.com/
- group: operate
  title: ''
  type: Support
  url: https://www.cashfree.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cashfree.com/privacypolicy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://merchant.cashfree.com/merchants/pg/developers/api-keys
- group: company
  title: ''
  type: Blog
  url: https://www.cashfree.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://www.cashfree.com/docs/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cashfree.com/one-click-onboarding/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cashfree.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cashfree
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/security/cashfree-payments-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cashfree-payments-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cashfree-payments/refs/heads/main/security/cashfree-payments-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cashfree-payments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cashfree.com:443/
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI or other machine-readable contract was found on Cashfree's API hosts.
  evidence:
  - status: 404
    url: https://api.cashfree.com/openapi.json
  - status: 404
    url: https://docs.cashfree.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cashfree Payments provides a comprehensive payment gateway platform enabling businesses to collect online payments across multiple modes, including cards, UPI, wallets, and international payment methods. Their solutions cover hosted checkout, payment links, recurring subscriptions, payouts, and compliance tools, serving merchants in India and globally with fast settlements and extensive developer resources.
image: https://cdn.prod.website-files.com/6a60525e5f4d2e4f1faed952/6a972447c25b36b8b4c71325_Open%20Graph%20Image.webp
json_schemas:
- name: GetPgOrdersOrderidIdResponse
  property_count: 2
  slug: cashfree-payments-get-pg-orders-orderid-id-response
- name: PostPgOrdersOrderidRefundsResponse
  property_count: 22
  slug: cashfree-payments-post-pg-orders-orderid-refunds-response
- name: PostPgOrdersResponse
  property_count: 16
  slug: cashfree-payments-post-pg-orders-response
- name: PostPgOrdersSessionsResponse
  property_count: 6
  slug: cashfree-payments-post-pg-orders-sessions-response
- name: PostPgRequest
  property_count: 12
  slug: cashfree-payments-post-pg-request
- name: PostPgResponse
  property_count: 17
  slug: cashfree-payments-post-pg-response
jsonld:
- class_count: 6
  name: Cashfree Payments Context
  property_count: 44
  slug: cashfree-payments-context
layout: provider
modified: '2026-10-07'
name: Cashfree Payments
nav: Providers
network: true
overview: 'Cashfree Payments is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Orders API, Payout API, and Pg API. Tagged areas include Company, Payments, Fintech, and Gateways.


  The Cashfree Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Cashfree Payments'' developer surface includes CLI, authentication, support, engineering blog, API reference, getting-started guide, documentation, and 25 more developer resources.'
plans:
- name: Cashfree Payments Plans Pricing
  plan_count: 13
  slug: cashfree-payments-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Cashfree Payments API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: cashfree-payments-rules
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 33.9
    developer_ergonomics: 71.4
    discoverability: 69.6
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 28.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cashfree Payments Authentication
  slug: cashfree-payments-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Cashfree Payments Domain Security
  slug: cashfree-payments-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cashfree Payments Vulnerability Disclosure
  slug: cashfree-payments-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cashfree-payments
tags:
- Company
- Payments
- Fintech
- Gateways
website: https://www.cashfree.com:443/
---
