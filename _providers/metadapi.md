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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Metadapi Agentic Access
  operation_count: 7
  slug: metadapi-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://global.metadapi.com
  baseurl_source: spec
  description: The Zipc API from Metadapi — 7 operation(s) for zipc.
  name: Metadapi Zipc API
  slug: metadapi-zipc-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/metadapi/agentic-access/metadapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/metadapi-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/metadapi/rules/metadapi-rules.yml
  title: ''
  type: Spectral
  url: rules/metadapi-rules.yml
- group: design
  href: https://artifacts.apis.io/metadapi/json-ld/metadapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/metadapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/metadapi/vocabulary/metadapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/metadapi-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/metadapi/data-model/metadapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/metadapi-data-model.yml
- group: design
  href: https://artifacts.apis.io/metadapi/errors/metadapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/metadapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/metadapi/conformance/metadapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/metadapi-conformance.yml
- group: other
  href: https://artifacts.apis.io/metadapi/hosts/metadapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/metadapi-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://www.metadapi.com/Support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Metadapi/
- group: auth
  href: https://artifacts.apis.io/metadapi/authentication/metadapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/metadapi-authentication.yml
- group: auth
  href: https://artifacts.apis.io/metadapi/security/metadapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/metadapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://metadapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.metadapi.com/Support/Documentation
- group: docs
  title: ''
  type: APIReference
  url: https://metadapi.stoplight.io/docs/api/fd43i6ofj720n-zip-code-data-api-v2
- group: start
  title: ''
  type: GettingStarted
  url: https://www.metadapi.com/Blog/getting-started-zip-code-api
- group: company
  title: ''
  type: Blog
  url: https://www.metadapi.com/Blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metadapi.com/Terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.metadapi.com/Privacy
created: '2026-10-20'
description: Metadapi provides reliable reference data APIs for applications, offering datasets such as zip code statistics, languages, continents, and countries. Their platform emphasizes fast, secure, and easy integration of standard JSON reference data, supporting developers with comprehensive documentation, change logs, and support resources.
json_schemas:
- name: links
  property_count: 5
  slug: metadapi-links
- name: ZipCodeResponse
  property_count: 3
  slug: metadapi-zip-code-response
- name: Zip Code
  property_count: 36
  slug: metadapi-zipcode
jsonld:
- class_count: 4
  name: Metadapi Context
  property_count: 45
  slug: metadapi-context
layout: provider
modified: '2026-10-20'
name: Metadapi
nav: Providers
network: true
overview: 'Metadapi publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Zipc API. Tagged areas include Company, Data, Reference, and JSON.


  The Metadapi catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Metadapi''s developer surface includes support, authentication, documentation, API reference, getting-started guide, engineering blog, and 13 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Metadapi API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: metadapi-rules
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 66.1
    developer_ergonomics: 47.6
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
  name: Metadapi Authentication
  slug: metadapi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Metadapi Domain Security
  slug: metadapi-domain-security
  summary_line: TLSv1.3
slug: metadapi
tags:
- Company
- Data
- Reference
- JSON
website: https://metadapi.com/
---
