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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: WriteStack provides tools for Substack creators to schedule, analyze, and monetize newsletters via a developer portal.
  name: WriteStack API
  slug: writestack-api-2
- description: 'WriteStack API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: WriteStack API
  slug: writestack-api
artifact_total: 12
asyncapis:
- description: ''
  name: Writestack Webhooks
  slug: writestack-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/writestack/plans/writestack-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/writestack-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/writestack/rules/writestack-rules.yml
  title: ''
  type: Spectral
  url: rules/writestack-rules.yml
- group: design
  href: https://artifacts.apis.io/writestack/json-ld/writestack-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/writestack-context.jsonld
- group: design
  href: https://artifacts.apis.io/writestack/vocabulary/writestack-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/writestack-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/writestack/asyncapi/writestack-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/writestack-webhooks.yml
- group: design
  href: https://artifacts.apis.io/writestack/data-model/writestack-data-model.yml
  title: ''
  type: DataModel
  url: data-model/writestack-data-model.yml
- group: auth
  href: https://artifacts.apis.io/writestack/authentication/writestack-authentication.yml
  title: ''
  type: Authentication
  url: authentication/writestack-authentication.yml
- group: design
  href: https://artifacts.apis.io/writestack/conformance/writestack-conformance.yml
  title: ''
  type: Conformance
  url: conformance/writestack-conformance.yml
- group: agent
  href: https://artifacts.apis.io/writestack/llms/writestack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/writestack-llms.txt
- group: auth
  href: https://artifacts.apis.io/writestack/well-known/writestack-vercel-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/writestack-vercel-security.txt
- group: agent
  href: https://artifacts.apis.io/writestack/well-known/writestack-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/writestack-well-known.yml
- group: other
  href: https://artifacts.apis.io/writestack/hosts/writestack-hosts.yml
  title: ''
  type: Hosts
  url: hosts/writestack-hosts.yml
- group: other
  href: https://artifacts.apis.io/writestack/vendors/writestack-vendors.yml
  title: ''
  type: Vendors
  url: vendors/writestack-vendors.yml
- group: auth
  href: https://artifacts.apis.io/writestack/security/writestack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/writestack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.writestack.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.writestack.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.writestack.io/tools
- group: start
  title: ''
  type: GettingStarted
  url: https://www.writestack.io/#pricing
- group: company
  title: ''
  type: Blog
  url: https://www.writestack.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.writestack.io/pricing.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.writestack.io/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.writestack.io/privacy
coverage:
  checked: '2026-10-27'
  detail: The developer portal pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.writestack.io/tools
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: WriteStack is a Substack growth platform that helps creators schedule, analyze, and monetize their Substack newsletters. It offers tools to draft notes, schedule posts, track audience engagement, and provides a writing coach to generate outlines. The service aims to streamline content creation, improve subscriber growth, and give creators analytics to optimize their newsletters.
json_schemas:
- name: PostV1BillingBuyRequest
  property_count: 2
  slug: writestack-post-v1-billing-buy-request
- name: PostV1BillingBuyResponse
  property_count: 3
  slug: writestack-post-v1-billing-buy-response
- name: PostV1RegistrarDomainsPriceRequest
  property_count: 1
  slug: writestack-post-v1-registrar-domains-price-request
- name: PostV1RegistrarDomainsSearchRequest
  property_count: 1
  slug: writestack-post-v1-registrar-domains-search-request
jsonld:
- class_count: 4
  name: Writestack Context
  property_count: 6
  slug: writestack-context
layout: provider
modified: '2026-10-27'
name: WriteStack
nav: Providers
network: true
overview: 'WriteStack is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Substack, Growth, Analytics, and ContentCreation.


  The WriteStack catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  WriteStack''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Writestack Plans Pricing
  plan_count: 3
  slug: writestack-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: WriteStack API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: writestack-rules
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 61.0
    catalog_earned_first_party: 12.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 19.7
    contract_quality: 28.2
    developer_ergonomics: 45.2
    discoverability: 53.6
    operational_transparency: 18.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
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
  name: Writestack Authentication
  slug: writestack-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Writestack Domain Security
  slug: writestack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: writestack
tags:
- Company
- Substack
- Growth
- Analytics
- ContentCreation
website: https://www.writestack.io/
---
