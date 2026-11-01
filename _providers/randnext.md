---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Randnext Agentic Access
  operation_count: 64
  slug: randnext-agentic-access
  summary_line: 64 operations · 3 acting
api_count: 1
apis:
- baseURL: https://randnext.com
  baseurl_source: declared
  description: The Draws API from RandNext — 6 operation(s) for draws.
  name: RandNext Draws API
  slug: randnext-draws-api
- baseURL: https://randnext.com
  baseurl_source: declared
  description: The Health API from RandNext — 1 operation(s) for health.
  name: RandNext Health API
  slug: randnext-health-api
- baseURL: https://randnext.com
  baseurl_source: declared
  description: The Jokes API from RandNext — 3 operation(s) for jokes.
  name: RandNext Jokes API
  slug: randnext-jokes-api
- baseURL: https://randnext.com
  baseurl_source: declared
  description: The Questions API from RandNext — 3 operation(s) for questions.
  name: RandNext Questions API
  slug: randnext-questions-api
- baseURL: https://randnext.com
  baseurl_source: declared
  description: The Quotes API from RandNext — 3 operation(s) for quotes.
  name: RandNext Quotes API
  slug: randnext-quotes-api
- baseURL: https://randnext.com
  baseurl_source: declared
  description: The Tools API from RandNext — 44 operation(s) for tools.
  name: RandNext Tools API
  slug: randnext-tools-api
- baseURL: https://randnext.com
  baseurl_source: declared
  description: The Words API from RandNext — 3 operation(s) for words.
  name: RandNext Words API
  slug: randnext-words-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/randnext/agentic-access/randnext-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/randnext-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/randnext/rules/randnext-rules.yml
  title: ''
  type: Spectral
  url: rules/randnext-rules.yml
- group: design
  href: https://artifacts.apis.io/randnext/json-ld/randnext-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/randnext-context.jsonld
- group: design
  href: https://artifacts.apis.io/randnext/vocabulary/randnext-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/randnext-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/randnext/data-model/randnext-data-model.yml
  title: ''
  type: DataModel
  url: data-model/randnext-data-model.yml
- group: design
  href: https://artifacts.apis.io/randnext/errors/randnext-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/randnext-problem-types.yml
- group: design
  href: https://artifacts.apis.io/randnext/conformance/randnext-conformance.yml
  title: ''
  type: Conformance
  url: conformance/randnext-conformance.yml
- group: other
  href: https://artifacts.apis.io/randnext/hosts/randnext-hosts.yml
  title: ''
  type: Hosts
  url: hosts/randnext-hosts.yml
- group: other
  href: https://artifacts.apis.io/randnext/vendors/randnext-vendors.yml
  title: ''
  type: Vendors
  url: vendors/randnext-vendors.yml
- group: auth
  href: https://artifacts.apis.io/randnext/authentication/randnext-authentication.yml
  title: ''
  type: Authentication
  url: authentication/randnext-authentication.yml
- group: auth
  href: https://artifacts.apis.io/randnext/security/randnext-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/randnext-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://randnext.com
- group: docs
  title: ''
  type: Documentation
  url: https://randnext.com/generators
- group: docs
  title: ''
  type: APIReference
  url: https://randnext.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://randnext.com
created: '2026-10-28'
description: RandNext provides a collection of free random data generators accessible via a simple HTTP API. The service offers 48 distinct endpoints delivering random jokes, emojis, quotes, names, passwords, colors, and many other fun or utility values. All endpoints are publicly available without authentication, returning JSON responses suitable for integration into applications, games, or testing environments. The platform emphasizes ease of use, low latency, and a broad variety of random content to support developers and creators looking for quick, unpredictable data.
image: https://randnext.com/opengraph-image
json_schemas:
- name: Draw
  property_count: 29
  slug: randnext-draw
- name: DrawSettings
  property_count: 2
  slug: randnext-draw-settings
- name: Item
  property_count: 13
  slug: randnext-item
- name: ToolResponse
  property_count: 4
  slug: randnext-tool-response
jsonld:
- class_count: 5
  name: Randnext Context
  property_count: 46
  slug: randnext-context
layout: provider
modified: '2026-10-28'
name: RandNext
nav: Providers
network: true
overview: 'RandNext publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Draws API, Health API, Jokes API, and 4 more. Tagged areas include Company, Random, Generator, API, and Fun.


  The RandNext catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RandNext''s developer surface includes authentication, documentation, API reference, getting-started guide, and 11 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: RandNext API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 3
  slug: randnext-rules
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 58.0
    developer_ergonomics: 40.5
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Randnext Authentication
  slug: randnext-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Randnext Domain Security
  slug: randnext-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: randnext
tags:
- Company
- Random
- Generator
- API
- Fun
website: https://randnext.com
---
