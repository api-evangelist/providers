---
agent_readiness:
  band: agent-ready
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Aranya API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Aranya API
  slug: aranya-api
artifact_total: 10
asyncapis:
- description: ''
  name: Aranya Webhooks
  slug: aranya-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/aranya/plans/aranya-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aranya-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aranya/rules/aranya-rules.yml
  title: ''
  type: Spectral
  url: rules/aranya-rules.yml
- group: design
  href: https://artifacts.apis.io/aranya/json-ld/aranya-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aranya-context.jsonld
- group: design
  href: https://artifacts.apis.io/aranya/vocabulary/aranya-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aranya-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aranya/asyncapi/aranya-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/aranya-webhooks.yml
- group: design
  href: https://artifacts.apis.io/aranya/data-model/aranya-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aranya-data-model.yml
- group: auth
  href: https://artifacts.apis.io/aranya/authentication/aranya-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aranya-authentication.yml
- group: design
  href: https://artifacts.apis.io/aranya/conformance/aranya-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aranya-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aranya/llms/aranya-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aranya-llms.txt
- group: auth
  href: https://artifacts.apis.io/aranya/well-known/aranya-vercel-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aranya-vercel-security.txt
- group: agent
  href: https://artifacts.apis.io/aranya/well-known/aranya-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aranya-well-known.yml
- group: other
  href: https://artifacts.apis.io/aranya/hosts/aranya-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aranya-hosts.yml
- group: other
  href: https://artifacts.apis.io/aranya/vendors/aranya-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aranya-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aranya.tech/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aranya.tech/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://aranya.tech/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://aranya.tech/news
- group: company
  title: ''
  type: Blog
  url: https://aranya.tech/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://vercel.com/docs/getting-started-with-vercel.md?from=llms-txt
- group: docs
  title: ''
  type: Documentation
  url: https://dev.aranya.tech/
- group: docs
  title: ''
  type: APIReference
  url: https://vercel.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/aranya/security/aranya-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aranya-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aranya.tech/
coverage:
  checked: '2026-10-29'
  detail: Aranya's website provides documentation links but no publicly accessible OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications were found.
  evidence:
  - status: 200
    url: https://aranya.tech/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Aranya provides a multicluster operating system that transforms any bare‑metal hardware into custom, production‑ready clusters within 48 hours. Powered by clusterdOS, it enables rapid deployment of scalable infrastructure for cloud, edge, and on‑premises workloads, simplifying management and accelerating time‑to‑value for enterprises.
image: https://cdn.prod.website-files.com/699e87bdb4e7a4dd631d2af7/6a722c90c074f3a375f80b6e_aranya-og-dark.png
json_schemas:
- name: PostV1BillingBuyResponse
  property_count: 3
  slug: aranya-post-v1-billing-buy-response
- name: PostV1RegistrarDomainsPriceRequest
  property_count: 1
  slug: aranya-post-v1-registrar-domains-price-request
- name: PostV1RegistrarDomainsSearchRequest
  property_count: 1
  slug: aranya-post-v1-registrar-domains-search-request
jsonld:
- class_count: 3
  name: Aranya Context
  property_count: 4
  slug: aranya-context
layout: provider
modified: '2026-10-29'
name: Aranya
nav: Providers
network: true
overview: 'Aranya is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Cloud, Edge, and Automation.


  The Aranya catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Aranya''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, API reference, and 17 more developer resources.'
plans:
- name: Aranya Plans Pricing
  plan_count: 2
  slug: aranya-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Aranya API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: aranya-rules
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 59.0
    catalog_earned_first_party: 8.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 19.7
    contract_quality: 28.2
    developer_ergonomics: 42.9
    discoverability: 58.9
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
  name: Aranya Authentication
  slug: aranya-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aranya Domain Security
  slug: aranya-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aranya
tags:
- Company
- Infrastructure
- Cloud
- Edge
- Automation
website: https://aranya.tech/
---
