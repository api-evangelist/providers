---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Build on DreamerOS – live REST and MCP paths for checked answers.
  name: DreamerOS API
  slug: dreameros-api
- baseURL: https://api.dreameros.app
  baseurl_source: declared
  description: 'DreamerOS API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: DreamerOS API
  slug: dreameros-app-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/dreameros-app/plans/dreameros-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dreameros-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dreameros-app/rules/dreameros-app-rules.yml
  title: ''
  type: Spectral
  url: rules/dreameros-app-rules.yml
- group: design
  href: https://artifacts.apis.io/dreameros-app/json-ld/dreameros-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dreameros-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/dreameros-app/vocabulary/dreameros-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dreameros-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dreameros-app/data-model/dreameros-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dreameros-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/dreameros-app/conformance/dreameros-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dreameros-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dreameros-app/llms/dreameros-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dreameros-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/dreameros-app/well-known/dreameros-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dreameros-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/dreameros-app/hosts/dreameros-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dreameros-app-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.dreameros.app/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dreameros.app/terms.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dreameros.app/privacy.php
- group: commercial
  title: ''
  type: Pricing
  url: https://dreameros.app/plans.php
- group: start
  title: ''
  type: GettingStarted
  url: https://dreameros.app/getting-started.php
- group: auth
  href: https://artifacts.apis.io/dreameros-app/security/dreameros-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dreameros-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dreameros.app/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.dreameros.app/mcp
  - status: 200
    url: https://dreameros.app/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: DreamerOS offers an AI operating system that sits between users and the AI tools they already use. It checks questions and answers, adds a second AI reviewer from a different maker, records verification receipts, and maintains a single account memory that can be recalled across connected AI applications. The service is aimed at developers and other users who need reliable AI output and traceable proof of its accuracy.
image: https://dreameros.app/assets/fingerprint-og.png
json_schemas:
- name: PostApiV1VerifyRequest
  property_count: 2
  slug: dreameros-app-post-api-v1-verify-request
jsonld:
- class_count: 1
  name: Dreameros App Context
  property_count: 2
  slug: dreameros-app-context
layout: provider
modified: '2026-11-05'
name: DreamerOS
nav: Providers
network: true
overview: 'DreamerOS is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI verification, AI memory, AI Operating System, and Developer Tools.


  The DreamerOS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DreamerOS''s developer surface includes pricing, getting-started guide, and 14 more developer resources.'
plans:
- name: Dreameros App Plans Pricing
  plan_count: 5
  slug: dreameros-app-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: DreamerOS API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: dreameros-app-rules
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 55.2
    catalog_earned_first_party: 12.0
    catalog_gap: 59.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dreameros App Domain Security
  slug: dreameros-app-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dreameros-app
tags:
- AI verification
- AI memory
- AI Operating System
- Developer Tools
website: https://dreameros.app/
---
