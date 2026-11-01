---
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://demoshop.skyramp.dev
  baseurl_source: declared
  description: 'Skyramp API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Skyramp API
  slug: skyramp-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/skyramp/rules/skyramp-rules.yml
  title: ''
  type: Spectral
  url: rules/skyramp-rules.yml
- group: design
  href: https://artifacts.apis.io/skyramp/json-ld/skyramp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/skyramp-context.jsonld
- group: design
  href: https://artifacts.apis.io/skyramp/vocabulary/skyramp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/skyramp-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/skyramp/data-model/skyramp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/skyramp-data-model.yml
- group: auth
  href: https://artifacts.apis.io/skyramp/authentication/skyramp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/skyramp-authentication.yml
- group: design
  href: https://artifacts.apis.io/skyramp/conformance/skyramp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/skyramp-conformance.yml
- group: other
  href: https://artifacts.apis.io/skyramp/hosts/skyramp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skyramp-hosts.yml
- group: other
  href: https://artifacts.apis.io/skyramp/vendors/skyramp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/skyramp-vendors.yml
- group: build
  href: https://artifacts.apis.io/skyramp/packages/skyramp-packages.yml
  title: ''
  type: SDKs
  url: packages/skyramp-packages.yml
- group: build
  href: https://artifacts.apis.io/skyramp/packages/skyramp-packages.yml
  title: ''
  type: Packages
  url: packages/skyramp-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.skyramp.dev/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.skyramp.dev/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.skyramp.dev/privacy
- group: company
  title: ''
  type: Blog
  url: https://skyramp.dev/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.skyramp.dev/quickstart/first-test
- group: docs
  title: ''
  type: Documentation
  url: https://docs.skyramp.dev/
- group: auth
  href: https://artifacts.apis.io/skyramp/security/skyramp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skyramp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skyramp.dev/
created: '2026-10-23'
description: Skyramp provides AI‑powered deterministic test generation for developers, eliminating flaky tests by automatically creating reliable test suites for complex applications. The platform offers tools for test generation, execution, and analysis, helping dev teams accelerate delivery and improve software quality.
image: https://framerusercontent.com/assets/VBqTuh9qkw1in0UuOX2lIfz8R0.png
json_schemas:
- name: PostApiV1OrdersRequest
  property_count: 2
  slug: skyramp-post-api-v1-orders-request
- name: PostApiV1ProductsRequest
  property_count: 6
  slug: skyramp-post-api-v1-products-request
jsonld:
- class_count: 2
  name: Skyramp Context
  property_count: 8
  slug: skyramp-context
layout: provider
modified: '2026-10-23'
name: Skyramp
nav: Providers
network: true
overview: 'Skyramp is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Testing, DeveloperTools, and Automation.


  The Skyramp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Skyramp''s developer surface includes authentication, engineering blog, getting-started guide, documentation, and 14 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Skyramp API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: skyramp-rules
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Skyramp Authentication
  slug: skyramp-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Skyramp Domain Security
  slug: skyramp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skyramp
tags:
- Company
- AI
- Testing
- DeveloperTools
- Automation
website: https://skyramp.dev/
---
