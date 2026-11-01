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
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Vikunja provides a task management API documented at the public documentation site. No machine‑readable contract (OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL) was found.
  name: Vikunja API
  slug: vikunja-api-2
- baseURL: https://dl.vikunja.io
  baseurl_source: declared
  description: 'Vikunja API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Vikunja API
  slug: vikunja-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/vikunja/plans/vikunja-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vikunja-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/vikunja/rules/vikunja-rules.yml
  title: ''
  type: Spectral
  url: rules/vikunja-rules.yml
- group: design
  href: https://artifacts.apis.io/vikunja/json-ld/vikunja-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vikunja-context.jsonld
- group: design
  href: https://artifacts.apis.io/vikunja/vocabulary/vikunja-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vikunja-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/vikunja/data-model/vikunja-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vikunja-data-model.yml
- group: auth
  href: https://artifacts.apis.io/vikunja/authentication/vikunja-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vikunja-authentication.yml
- group: design
  href: https://artifacts.apis.io/vikunja/conformance/vikunja-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vikunja-conformance.yml
- group: agent
  href: https://artifacts.apis.io/vikunja/llms/vikunja-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vikunja-llms.txt
- group: other
  href: https://artifacts.apis.io/vikunja/hosts/vikunja-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vikunja-hosts.yml
- group: other
  href: https://artifacts.apis.io/vikunja/vendors/vikunja-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vikunja-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://vikunja.io/security
- group: start
  title: ''
  type: Login
  url: https://console.vikunja.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://vikunja.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://vikunja.io/docs/fail2ban
- group: auth
  href: https://artifacts.apis.io/vikunja/security/vikunja-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vikunja-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vikunja/security/vikunja-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vikunja-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vikunja.io/
- group: docs
  title: ''
  type: Documentation
  url: https://vikunja.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://vikunja.io/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vikunja.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://vikunja.io/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/go-vikunja
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but no OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL spec could be retrieved.
  evidence:
  - status: 404
    url: https://api.vikunja.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Vikunja is an open-source, self‑hostable task management platform offering lists, Kanban, Gantt, and table views. It emphasizes data ownership, privacy, and European hosting, with optional cloud hosting. The software is released under AGPL‑v3 and provides import tools for Todoist, Trello, and Microsoft To‑Do.
image: https://vikunja.io/og/index.webp
json_schemas:
- name: GetApiV1FiltersIdResponse
  property_count: 7
  slug: vikunja-get-api-v1-filters-id-response
- name: GetApiV1FiltersResponse
  property_count: 7
  slug: vikunja-get-api-v1-filters-response
- name: PostApiV1FiltersIdRequest
  property_count: 4
  slug: vikunja-post-api-v1-filters-id-request
- name: PostApiV1FiltersIdResponse
  property_count: 7
  slug: vikunja-post-api-v1-filters-id-response
- name: PutApiV1FiltersRequest
  property_count: 4
  slug: vikunja-put-api-v1-filters-request
- name: PutApiV1FiltersResponse
  property_count: 7
  slug: vikunja-put-api-v1-filters-response
jsonld:
- class_count: 8
  name: Vikunja Context
  property_count: 8
  slug: vikunja-context
layout: provider
modified: '2026-10-28'
name: Vikunja
nav: Providers
network: true
overview: 'Vikunja is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OpenSource, TaskManagement, SelfHostable, and European.


  The Vikunja catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Vikunja''s developer surface includes authentication, changelog, getting-started guide, documentation, pricing, support, and 16 more developer resources.'
plans:
- name: Vikunja Plans Pricing
  plan_count: 3
  slug: vikunja-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Vikunja API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: vikunja-rules
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 24.0
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Vikunja Authentication
  slug: vikunja-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Vikunja Domain Security
  slug: vikunja-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Vikunja Vulnerability Disclosure
  slug: vikunja-vulnerability-disclosure
  summary_line: no policy recorded
slug: vikunja
tags:
- Company
- OpenSource
- TaskManagement
- SelfHostable
- European
website: https://vikunja.io/
---
