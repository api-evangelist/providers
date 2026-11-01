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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Musical AI API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Musical AI API
  slug: musical-ai-api
artifact_total: 11
asyncapis:
- description: ''
  name: Musical Ai Webhooks
  slug: musical-ai-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/musical-ai/plans/musical-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/musical-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/musical-ai/rules/musical-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/musical-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/musical-ai/json-ld/musical-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/musical-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/musical-ai/vocabulary/musical-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/musical-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/musical-ai/asyncapi/musical-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/musical-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/musical-ai/data-model/musical-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/musical-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/musical-ai/authentication/musical-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/musical-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/musical-ai/conformance/musical-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/musical-ai-conformance.yml
- group: auth
  href: https://artifacts.apis.io/musical-ai/well-known/musical-ai-vercel-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/musical-ai-vercel-security.txt
- group: agent
  href: https://artifacts.apis.io/musical-ai/well-known/musical-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/musical-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/musical-ai/hosts/musical-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/musical-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/musical-ai/vendors/musical-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/musical-ai-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wearemusical.ai/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.wearemusical.ai/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.wearemusical.ai/press/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://vercel.com/docs/getting-started-with-vercel.md?from=llms-txt
- group: docs
  title: ''
  type: Documentation
  url: https://dev.wearemusical.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://vercel.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/musical-ai/security/musical-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/musical-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wearemusical.ai
coverage:
  checked: '2026-10-29'
  detail: Provider site returns a JavaScript shell that cannot be rendered to extract docs.
  evidence:
  - status: 200
    url: https://musical.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Musical AI provides an attribution and rights infrastructure for generative music, enabling rights holders to grant consent and track licensing for AI-generated works. The platform offers a consent layer, attribution metadata, and compliance tools for both rights holders and AI companies, ensuring that generated music respects existing catalogs and industry norms. It operates downstream of generation, focusing on output attribution without exposing model internals.
image: https://www.wearemusical.ai/images/og.jpg
json_schemas:
- name: PostV1BillingBuyRequest
  property_count: 2
  slug: musical-ai-post-v1-billing-buy-request
- name: PostV1BillingBuyResponse
  property_count: 3
  slug: musical-ai-post-v1-billing-buy-response
- name: PostV1RegistrarDomainsPriceRequest
  property_count: 1
  slug: musical-ai-post-v1-registrar-domains-price-request
- name: PostV1RegistrarDomainsSearchRequest
  property_count: 1
  slug: musical-ai-post-v1-registrar-domains-search-request
jsonld:
- class_count: 4
  name: Musical Ai Context
  property_count: 6
  slug: musical-ai-context
layout: provider
modified: '2026-10-29'
name: Musical AI
nav: Providers
network: true
overview: 'Musical AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, AI, Attribution, and RightsManagement.


  The Musical AI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Musical AI''s developer surface includes authentication, changelog, getting-started guide, documentation, API reference, and 15 more developer resources.'
plans:
- name: Musical Ai Plans Pricing
  plan_count: 1
  slug: musical-ai-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Musical AI API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: musical-ai-rules
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 59.0
    catalog_earned_first_party: 8.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 19.7
    contract_quality: 28.2
    developer_ergonomics: 40.5
    discoverability: 58.9
    operational_transparency: 34.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Musical Ai Authentication
  slug: musical-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Musical Ai Domain Security
  slug: musical-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: musical-ai
tags:
- Company
- Music
- AI
- Attribution
- RightsManagement
- GenerativeAI
website: https://www.wearemusical.ai
---
