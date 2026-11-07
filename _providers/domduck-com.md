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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public HTTP API providing domain reputation lookup and badge generation without authentication.
  name: Domduck API
  slug: domduck-api
- description: 'Domduck API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Domduck API
  slug: domduck-com-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/domduck-com/rules/domduck-com-rules.yml
  title: ''
  type: Spectral
  url: rules/domduck-com-rules.yml
- group: design
  href: https://artifacts.apis.io/domduck-com/json-ld/domduck-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/domduck-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/domduck-com/vocabulary/domduck-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/domduck-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/domduck-com/data-model/domduck-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/domduck-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/domduck-com/changelog/domduck-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/domduck-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/domduck-com/security/domduck-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/domduck-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/domduck-com/conformance/domduck-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/domduck-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/domduck-com/llms/domduck-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/domduck-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/domduck-com/well-known/domduck-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/domduck-com-security.txt
- group: agent
  href: https://artifacts.apis.io/domduck-com/well-known/domduck-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/domduck-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/domduck-com/hosts/domduck-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domduck-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/domduck-com/vendors/domduck-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/domduck-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://domduck.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://domduck.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://domduck.com/privacy
- group: start
  title: ''
  type: Login
  url: https://domduck.com/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://domduck.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://domduck.com/changelog
- group: auth
  href: https://artifacts.apis.io/domduck-com/security/domduck-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/domduck-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/domduck-com/security/domduck-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domduck-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://domduck.com/
coverage:
  checked: '2026-11-06'
  detail: The provider offers a public API documented in markdown but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract is published.
  evidence:
  - status: 200
    url: https://domduck.com/docs/api.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Domduck provides domain reputation tracking with historical data, offering free unlimited domain monitoring, daily Ahrefs Domain Rating, Tranco popularity rank, registration details, TLS status, and AI crawler policies. Users can access a model‑context protocol server and embed rating badges, all via a web‑based dashboard without requiring authentication.
json_schemas:
- name: GetApiBadgeDomainResponse
  property_count: 1
  slug: domduck-com-get-api-badge-domain-response
- name: PostApiLookupRequest
  property_count: 1
  slug: domduck-com-post-api-lookup-request
- name: PostApiMcpPublicRequest
  property_count: 4
  slug: domduck-com-post-api-mcp-public-request
- name: PostApiMcpRequest
  property_count: 3
  slug: domduck-com-post-api-mcp-request
- name: PostApiMcpResponse
  property_count: 5
  slug: domduck-com-post-api-mcp-response
jsonld:
- class_count: 5
  name: Domduck Com Context
  property_count: 10
  slug: domduck-com-context
layout: provider
modified: '2026-11-05'
name: Domduck
nav: Providers
network: true
overview: 'Domduck is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Domain Reputation, Monitoring, Free Tier, and Dashboards.


  The Domduck catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Domduck''s developer surface includes changelog, documentation, and 19 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Domduck API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: domduck-com-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 24.8
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Domduck Com Domain Security
  slug: domduck-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Domduck Com Vulnerability Disclosure
  slug: domduck-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: domduck-com
tags:
- Domain Reputation
- Monitoring
- Free Tier
- Dashboards
website: https://domduck.com/
---
