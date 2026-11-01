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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API reference for Metal Build Token API as described in the Quick Start Guide.
  name: Metal API
  slug: metal-api-2
- baseURL: https://api.metal.build
  baseurl_source: declared
  description: 'Metal API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Metal API
  slug: metal-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/metal/rules/metal-rules.yml
  title: ''
  type: Spectral
  url: rules/metal-rules.yml
- group: design
  href: https://artifacts.apis.io/metal/json-ld/metal-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/metal-context.jsonld
- group: design
  href: https://artifacts.apis.io/metal/vocabulary/metal-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/metal-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/metal/data-model/metal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/metal-data-model.yml
- group: auth
  href: https://artifacts.apis.io/metal/authentication/metal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/metal-authentication.yml
- group: design
  href: https://artifacts.apis.io/metal/conformance/metal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/metal-conformance.yml
- group: agent
  href: https://artifacts.apis.io/metal/llms/metal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/metal-llms.txt
- group: auth
  href: https://artifacts.apis.io/metal/well-known/metal-calendly-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/metal-calendly-security.txt
- group: auth
  href: https://artifacts.apis.io/metal/well-known/metal-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/metal-api-security.txt
- group: agent
  href: https://artifacts.apis.io/metal/well-known/metal-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/metal-well-known.yml
- group: other
  href: https://artifacts.apis.io/metal/hosts/metal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/metal-hosts.yml
- group: other
  href: https://artifacts.apis.io/metal/vendors/metal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/metal-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/0xmetropolis
- group: auth
  href: https://artifacts.apis.io/metal/security/metal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/metal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://metal.build/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metal.build/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.metal.build/
- group: start
  title: ''
  type: GettingStarted
  url: https://withmetal.typeform.com/to/ydK6iuaR
- group: operate
  title: ''
  type: Support
  url: https://calendly.com/d/cnjz-839-zmx/metal-onboarding
- group: commercial
  title: ''
  type: TermsOfService
  url: https://metal.build/terms
coverage:
  checked: '2026-10-18'
  detail: Docs site renders via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.metal.build/quickstart
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Metal is a technology company that provides a comprehensive platform for building, deploying, and managing modern web applications. Their services include cloud infrastructure, developer tools, and API integrations that enable businesses to accelerate digital transformation. Metal focuses on scalability, security, and performance, offering solutions such as continuous integration pipelines, automated testing, and real-time monitoring. The company aims to simplify complex development workflows and empower developers to deliver high-quality software faster, while maintaining robust security and compliance standards across the entire lifecycle of their applications.
image: https://metal.build/new/logo-wordmark-black.png
json_schemas:
- name: GetHolderHolderaddressTokenTokenaddressResponse
  property_count: 6
  slug: metal-get-holder-holderaddress-token-tokenaddress-response
- name: GetHolderUser123TransactionsResponse
  property_count: 2
  slug: metal-get-holder-user123-transactions-response
- name: GetTokenTokenaddressResponse
  property_count: 11
  slug: metal-get-token-tokenaddress-response
- name: PostHolderUseridSpendResponse
  property_count: 2
  slug: metal-post-holder-userid-spend-response
- name: PostHolderUseridTransferResponse
  property_count: 2
  slug: metal-post-holder-userid-transfer-response
- name: PostTokenTokenaddressDistributeRequest
  property_count: 2
  slug: metal-post-token-tokenaddress-distribute-request
jsonld:
- class_count: 17
  name: Metal Context
  property_count: 24
  slug: metal-context
layout: provider
modified: '2026-10-18'
name: Metal
nav: Providers
network: true
overview: 'Metal is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Platform, Cloud, Developer Tools, and Web Applications.


  The Metal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Metal''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 15 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Metal API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: metal-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 26.5
    developer_ergonomics: 45.2
    discoverability: 57.1
    operational_transparency: 15.8
  previous_composite: 29.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Metal Authentication
  slug: metal-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Metal Domain Security
  slug: metal-domain-security
  summary_line: TLSv1.3 · HSTS
slug: metal
tags:
- Company
- Platform
- Cloud
- Developer Tools
- Web Applications
website: https://metal.build/
---
