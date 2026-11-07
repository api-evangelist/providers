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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read-only access to the Dutch books catalogue.
  name: Boekenbase API
  slug: boekenbase-api
- baseURL: https://nhjisqchpvhuelilkoen.supabase.co/functions/v1/api
  baseurl_source: declared
  description: 'Read-only toegang tot de boekenbase: de catalogus van de Nederlandse'
  name: Boekenbase API V1 API
  slug: boekenbase-api-v1-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/boekenbase-nl/rules/boekenbase-nl-rules.yml
  title: ''
  type: Spectral
  url: rules/boekenbase-nl-rules.yml
- group: design
  href: https://artifacts.apis.io/boekenbase-nl/json-ld/boekenbase-nl-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/boekenbase-nl-context.jsonld
- group: design
  href: https://artifacts.apis.io/boekenbase-nl/vocabulary/boekenbase-nl-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/boekenbase-nl-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/boekenbase-nl/conformance/boekenbase-nl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boekenbase-nl-conformance.yml
- group: design
  href: https://artifacts.apis.io/boekenbase-nl/data-model/boekenbase-nl-data-model.yml
  title: ''
  type: DataModel
  url: data-model/boekenbase-nl-data-model.yml
- group: design
  href: https://artifacts.apis.io/boekenbase-nl/errors/boekenbase-nl-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/boekenbase-nl-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/boekenbase-nl/llms/boekenbase-nl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boekenbase-nl-llms.txt
- group: other
  href: https://artifacts.apis.io/boekenbase-nl/hosts/boekenbase-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boekenbase-nl-hosts.yml
- group: other
  href: https://artifacts.apis.io/boekenbase-nl/vendors/boekenbase-nl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boekenbase-nl-vendors.yml
- group: auth
  href: https://artifacts.apis.io/boekenbase-nl/security/boekenbase-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boekenbase-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boekenbase.nl/
- group: docs
  title: ''
  type: Documentation
  url: https://boekenbase.nl/developers/docs
- group: docs
  title: ''
  type: APIReference
  url: https://boekenbase.nl/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://boekenbase.nl/developers
- group: agent
  title: ''
  type: MCP
  url: https://boekenbase.nl/mcp
created: '2026-11-02'
description: BoekenBase is a Dutch online catalogue of the books market, offering searchable access to over 2.2 million titles in natural language. Users can create free accounts to manage personal bookshelves and wishlists, browse detailed book information, and discover new reads. The platform provides an API for developers to integrate book data into applications, supporting queries by title, author, ISBN, and more, with comprehensive metadata and multilingual support.
json_schemas:
- name: Book
  property_count: 29
  slug: boekenbase-nl-book
- name: SearchResult
  property_count: 15
  slug: boekenbase-nl-search-result
jsonld:
- class_count: 3
  name: Boekenbase Nl Context
  property_count: 36
  slug: boekenbase-nl-context
layout: provider
modified: '2026-11-02'
name: BoekenBase
nav: Providers
network: true
overview: 'BoekenBase publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API V1 API, and 1 more. Tagged areas include Books, Catalog, Netherlands, and Library.


  The BoekenBase catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BoekenBase''s developer surface includes documentation, API reference, getting-started guide, and 12 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: BoekenBase API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: boekenbase-nl-rules
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 46.9
    developer_ergonomics: 14.3
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boekenbase Nl Domain Security
  slug: boekenbase-nl-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: boekenbase-nl
tags:
- Books
- Catalog
- Netherlands
- Library
website: https://boekenbase.nl/
---
