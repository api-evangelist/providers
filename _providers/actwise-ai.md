---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Actwise API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: Actwise API
  slug: actwise-ai-api
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/actwise-ai/well-known/actwise-ai-vercel-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/actwise-ai-vercel-security.txt
- group: design
  href: https://artifacts.apis.io/actwise-ai/rules/actwise-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/actwise-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/actwise-ai/json-ld/actwise-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/actwise-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/actwise-ai/vocabulary/actwise-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/actwise-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/actwise-ai/data-model/actwise-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/actwise-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/actwise-ai/conformance/actwise-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/actwise-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/actwise-ai/well-known/actwise-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/actwise-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/actwise-ai/hosts/actwise-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/actwise-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/actwise-ai/vendors/actwise-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/actwise-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://actwise.ai/home/terms
- group: operate
  title: ''
  type: Support
  url: https://actwise.ai/home/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://actwise.ai/home/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://vercel.com/docs/getting-started-with-vercel.md?from=llms-txt
- group: docs
  title: ''
  type: Documentation
  url: https://dev.actwise.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://vercel.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/actwise-ai/security/actwise-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/actwise-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://actwise.ai/
coverage:
  checked: '2026-10-31'
  detail: Documentation pages render via JavaScript, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://actwise.ai/billing/onboarding
  - status: 302
    url: https://dev.actwise.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: Actwise provides an AI delivery infrastructure platform that enables teams to govern, reuse, and scale AI services. Their solution includes a shared foundation, reference architecture, and production‑grade components to accelerate AI deployments within weeks. Actwise emphasizes a governed delivery platform, reusable core services, and a collaborative approach to AI development, targeting enterprise customers seeking reliable, repeatable AI pipelines.
image: https://actwise.ai/home/brand/web/shared/actwise-hero-wide.png
json_schemas:
- name: PostV1BillingBuyRequest
  property_count: 2
  slug: actwise-ai-post-v1-billing-buy-request
- name: PostV1BillingBuyResponse
  property_count: 3
  slug: actwise-ai-post-v1-billing-buy-response
- name: PostV1RegistrarDomainsPriceRequest
  property_count: 1
  slug: actwise-ai-post-v1-registrar-domains-price-request
- name: PostV1RegistrarDomainsSearchRequest
  property_count: 1
  slug: actwise-ai-post-v1-registrar-domains-search-request
jsonld:
- class_count: 4
  name: Actwise Ai Context
  property_count: 6
  slug: actwise-ai-context
layout: provider
modified: '2026-10-31'
name: Actwise
nav: Providers
network: true
overview: 'Actwise is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Platform, Governance, Enterprise, and Delivery.


  The Actwise catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Actwise''s developer surface includes support, getting-started guide, documentation, API reference, and 13 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Actwise API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: actwise-ai-rules
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 26.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Actwise Ai Domain Security
  slug: actwise-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: actwise-ai
tags:
- Artificial Intelligence
- Platform
- Governance
- Enterprise
- Delivery
website: https://actwise.ai/
---
