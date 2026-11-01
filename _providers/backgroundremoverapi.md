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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Drop-in replacement API for remove.bg providing background removal via simple HTTP endpoints.
  name: Background Remover API
  slug: background-remover-api
- description: 'Background Remover API API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Background Remover API API
  slug: backgroundremoverapi-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/backgroundremoverapi/rules/backgroundremoverapi-rules.yml
  title: ''
  type: Spectral
  url: rules/backgroundremoverapi-rules.yml
- group: design
  href: https://artifacts.apis.io/backgroundremoverapi/json-ld/backgroundremoverapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/backgroundremoverapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/backgroundremoverapi/vocabulary/backgroundremoverapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/backgroundremoverapi-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/backgroundremoverapi/data-model/backgroundremoverapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/backgroundremoverapi-data-model.yml
- group: auth
  href: https://artifacts.apis.io/backgroundremoverapi/authentication/backgroundremoverapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/backgroundremoverapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/backgroundremoverapi/conformance/backgroundremoverapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/backgroundremoverapi-conformance.yml
- group: other
  href: https://artifacts.apis.io/backgroundremoverapi/hosts/backgroundremoverapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backgroundremoverapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/backgroundremoverapi/vendors/backgroundremoverapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/backgroundremoverapi-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://backgroundremoverapi.com/status
- group: start
  title: ''
  type: Sandbox
  url: https://backgroundremoverapi.com/playground
- group: start
  title: ''
  type: Login
  url: https://backgroundremoverapi.com/login
- group: auth
  href: https://artifacts.apis.io/backgroundremoverapi/security/backgroundremoverapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backgroundremoverapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://backgroundremoverapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://backgroundremoverapi.com/api-docs
coverage:
  checked: '2026-10-20'
  detail: Documentation provides endpoint details but no OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://backgroundremoverapi.com/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Background Remover API provides an API to remove image backgrounds using AI-powered U2Net engine. It offers a wire-compatible clone of remove.bg with up to 100 free credits for testing. The service targets developers needing automated background removal for photos, product images, or graphics, supporting JSON responses and simple HTTP endpoints.
image: https://backgroundremoverapi.com/og-image.png
json_schemas:
- name: GetV10AccountResponse
  property_count: 1
  slug: backgroundremoverapi-get-v10-account-response
- name: PostV1GenerationsRequest
  property_count: 1
  slug: backgroundremoverapi-post-v1-generations-request
- name: PostV1GenerationsResponse
  property_count: 3
  slug: backgroundremoverapi-post-v1-generations-response
jsonld:
- class_count: 3
  name: Backgroundremoverapi Context
  property_count: 5
  slug: backgroundremoverapi-context
layout: provider
modified: '2026-10-20'
name: Background Remover API
nav: Providers
network: true
overview: 'Background Remover API is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Image Processing, Artificial Intelligence, Background Removal, and Developer Tools.


  The Background Remover API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Background Remover API''s developer surface includes authentication, sandbox, documentation, and 11 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Background Remover API API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: backgroundremoverapi-rules
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Backgroundremoverapi Authentication
  slug: backgroundremoverapi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Backgroundremoverapi Domain Security
  slug: backgroundremoverapi-domain-security
  summary_line: TLSv1.3
slug: backgroundremoverapi
tags:
- Company
- Image Processing
- Artificial Intelligence
- Background Removal
- Developer Tools
website: https://backgroundremoverapi.com
---
