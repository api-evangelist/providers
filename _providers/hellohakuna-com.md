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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.hellohakuna.com
  baseurl_source: declared
  description: 'Hakuna API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Hakuna API
  slug: hellohakuna-com-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/hellohakuna-com/rules/hellohakuna-com-rules.yml
  title: ''
  type: Spectral
  url: rules/hellohakuna-com-rules.yml
- group: design
  href: https://artifacts.apis.io/hellohakuna-com/json-ld/hellohakuna-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hellohakuna-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/hellohakuna-com/vocabulary/hellohakuna-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hellohakuna-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/hellohakuna-com/data-model/hellohakuna-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hellohakuna-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/hellohakuna-com/authentication/hellohakuna-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hellohakuna-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/hellohakuna-com/lifecycle/hellohakuna-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hellohakuna-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hellohakuna-com/conformance/hellohakuna-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hellohakuna-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hellohakuna-com/llms/hellohakuna-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hellohakuna-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/hellohakuna-com/well-known/hellohakuna-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hellohakuna-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/hellohakuna-com/hosts/hellohakuna-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hellohakuna-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/hellohakuna-com/vendors/hellohakuna-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hellohakuna-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.hellohakuna.com/press
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hellohakuna.com/resources/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hellohakuna.com/integration-guides/shopify-app-integration/initial-setup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hellohakuna
- group: auth
  href: https://artifacts.apis.io/hellohakuna-com/security/hellohakuna-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hellohakuna-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hellohakuna.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hellohakuna.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.hellohakuna.com/
- group: operate
  title: ''
  type: Support
  url: https://www.hellohakuna.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hellohakuna.com/datenschutz
- group: commercial
  title: ''
  type: Legal
  url: https://www.hellohakuna.com/impressum
created: '2026-10-24'
description: Hakuna provides a product protection platform for retail businesses, enabling merchants to create customized protection plans, set pricing and branding, and manage claims. The platform helps increase revenue and customer satisfaction by offering flexible protection options across sales channels. Founded in Germany, Hakuna serves merchants worldwide with a focus on seamless integration and excellent support.
json_schemas:
- name: PostCartUpdatesRequest
  property_count: 4
  slug: hellohakuna-com-post-cart-updates-request
- name: PostCheckoutsRequest
  property_count: 6
  slug: hellohakuna-com-post-checkouts-request
- name: PostEventsRequest
  property_count: 2
  slug: hellohakuna-com-post-events-request
- name: PostOffersRequest
  property_count: 4
  slug: hellohakuna-com-post-offers-request
- name: PostOffersResponse
  property_count: 7
  slug: hellohakuna-com-post-offers-response
- name: PostSandboxEventsRequest
  property_count: 2
  slug: hellohakuna-com-post-sandbox-events-request
jsonld:
- class_count: 12
  name: Hellohakuna Com Context
  property_count: 26
  slug: hellohakuna-com-context
layout: provider
modified: '2026-10-24'
name: Hakuna
nav: Providers
network: true
overview: 'Hakuna is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, ProductProtection, SaaS, and Germany.


  The Hakuna catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hakuna''s developer surface includes authentication, API reference, getting-started guide, documentation, engineering blog, support, legal docs, and 15 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Hakuna API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: hellohakuna-com-rules
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 26.1
    developer_ergonomics: 47.6
    discoverability: 64.3
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hellohakuna Com Authentication
  slug: hellohakuna-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hellohakuna Com Domain Security
  slug: hellohakuna-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hellohakuna-com
tags:
- Company
- Retail
- ProductProtection
- SaaS
- Germany
website: https://www.hellohakuna.com
---
