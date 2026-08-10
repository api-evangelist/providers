---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: Programming Quotes — JWT login / register exchange.
  name: Programming Quotes Authentication API
  slug: programming-quotes-authentication-api
- description: Programming Quotes — Public read and authenticated write endpoints for quotes.
  name: Programming Quotes Quotes API
  slug: programming-quotes-quotes-api
artifact_total: 24
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/programming-quotes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/skolakoda/programming-quotes-api
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/skolakoda/programming-quotes-api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skolakoda
- group: commercial
  title: Unlicensed (community / open-source)
  type: License
  url: https://github.com/skolakoda/programming-quotes-api
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/programming-quotes-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/programming-quotes-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/programming-quotes-context.jsonld
created: '2026-05-28'
description: Free, open-source REST API serving a curated collection of programming-related quotes. Public endpoints return random quotes, paginated lists, author filters, and single quote lookups; authenticated endpoints support voting, favoriting, and quote authorship (CRUD). Originally seeded from the skolakoda community project on GitHub, the API is widely used as a demo data source and a free data feed for developer portfolio sites, tutorials, CLIs, and IDE extensions.
examples:
- key_count: 2
  name: Programming Quotes Auth Request Example
  slug: programming-quotes-auth-request-example
- key_count: 1
  name: Programming Quotes Auth Response Example
  slug: programming-quotes-auth-response-example
- key_count: 8
  name: Programming Quotes Quote Example
  slug: programming-quotes-quote-example
- key_count: 3
  name: Programming Quotes Quote Input Example
  slug: programming-quotes-quote-input-example
- key_count: 2
  name: Programming Quotes Quote Update Example
  slug: programming-quotes-quote-update-example
- key_count: 1
  name: Programming Quotes Vote Input Example
  slug: programming-quotes-vote-input-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/programming-quotes.png
json_schemas:
- name: AuthRequest
  property_count: 2
  slug: programming-quotes-auth-request
- name: AuthResponse
  property_count: 1
  slug: programming-quotes-auth-response
- name: QuoteInput
  property_count: 3
  slug: programming-quotes-quote-input
- name: Quote
  property_count: 8
  slug: programming-quotes-quote
- name: QuoteUpdate
  property_count: 3
  slug: programming-quotes-quote-update
- name: VoteInput
  property_count: 1
  slug: programming-quotes-vote-input
json_structures:
- name: Programming Quotes Auth Request Structure
  property_count: 2
  slug: programming-quotes-auth-request-structure
- name: Programming Quotes Auth Response Structure
  property_count: 1
  slug: programming-quotes-auth-response-structure
- name: Programming Quotes Quote Input Structure
  property_count: 3
  slug: programming-quotes-quote-input-structure
- name: Programming Quotes Quote Structure
  property_count: 8
  slug: programming-quotes-quote-structure
- name: Programming Quotes Quote Update Structure
  property_count: 3
  slug: programming-quotes-quote-update-structure
- name: Programming Quotes Vote Input Structure
  property_count: 1
  slug: programming-quotes-vote-input-structure
jsonld:
- class_count: 6
  name: Programming Quotes Context
  property_count: 12
  slug: programming-quotes-context
layout: provider
modified: '2026-05-30'
name: Programming Quotes
nav: Providers
network: true
overview: 'Programming Quotes publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Quotes API. Tagged areas include Personality, Public APIs, Open Source, Quotes, and Programming.


  The Programming Quotes catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
random_paper: 49
rules:
- name: Programming Quotes API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: programming-quotes-jsonschema-spectral-rules
- name: Programming Quotes API Rules
  rule_count: 42
  severity_counts:
    error: 15
    hint: 0
    info: 3
    warn: 24
  slug: programming-quotes-rules
score:
  band: emerging
  composite: 23.6
  delta: -0.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 31.3
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 23.8
  provenance:
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/programming-quotes/refs/heads/main/screenshots/programming-quotes-2026-06-20T192146.png
security:
- kind: domain-security
  name: Programming Quotes Domain Security
  slug: programming-quotes-domain-security
  summary_line: no transport/DNS hardening detected
slug: programming-quotes
tags:
- Personality
- Public APIs
- Open Source
- Quotes
- Programming
- Developer Tools
---
