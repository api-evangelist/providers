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
api_count: 2
apis:
- description: Fylamynt provides webhook integrations and API key management for automating cloud services.
  name: Fylamynt API
  slug: fylamynt-api-2
- description: 'Fylamynt API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Fylamynt API
  slug: fylamynt-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/fylamynt/rules/fylamynt-rules.yml
  title: ''
  type: Spectral
  url: rules/fylamynt-rules.yml
- group: design
  href: https://artifacts.apis.io/fylamynt/json-ld/fylamynt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fylamynt-context.jsonld
- group: design
  href: https://artifacts.apis.io/fylamynt/vocabulary/fylamynt-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fylamynt-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fylamynt/data-model/fylamynt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fylamynt-data-model.yml
- group: design
  href: https://artifacts.apis.io/fylamynt/conformance/fylamynt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fylamynt-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fylamynt/llms/fylamynt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fylamynt-llms.txt
- group: agent
  href: https://artifacts.apis.io/fylamynt/well-known/fylamynt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fylamynt-well-known.yml
- group: other
  href: https://artifacts.apis.io/fylamynt/hosts/fylamynt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fylamynt-hosts.yml
- group: other
  href: https://artifacts.apis.io/fylamynt/vendors/fylamynt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fylamynt-vendors.yml
- group: auth
  href: https://artifacts.apis.io/fylamynt/security/fylamynt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fylamynt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fylamynt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fylamynt.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fylamynt.com/getting-started-1/
- group: operate
  title: ''
  type: Support
  url: https://docs.fylamynt.com/support/contact-fylamynt.md
coverage:
  checked: '2026-10-29'
  detail: Documentation provides webhook integration guides but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://docs.fylamynt.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Fylamynt is a comprehensive cloud orchestration, automation and response platform that unifies case management, automation, real-time collaboration and incident remediation. It serves cloud engineering teams across the incident lifecycle, orchestrating across hundreds of cloud products to standardize and automate processes for faster response times and increased team productivity.
image: https://docs.fylamynt.com/~gitbook/ogimage/-MXYw3HF6oTHu5d7G6sL
json_schemas:
- name: GetClusterHealthResponse
  property_count: 15
  slug: fylamynt-get-cluster-health-response
- name: GetWatcherStatsResponse
  property_count: 4
  slug: fylamynt-get-watcher-stats-response
- name: GetWatcherWatchClusterHealthWatchResponse
  property_count: 4
  slug: fylamynt-get-watcher-watch-cluster-health-watch-response
jsonld:
- class_count: 3
  name: Fylamynt Context
  property_count: 22
  slug: fylamynt-context
layout: provider
modified: '2026-10-29'
name: Fylamynt
nav: Providers
network: true
overview: 'Fylamynt is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Automation, Incident-Response, and Orchestration.


  The Fylamynt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fylamynt''s developer surface includes documentation, getting-started guide, support, and 11 more developer resources.'
plans:
- name: Fylamynt Plans Pricing
  plan_count: 0
  slug: fylamynt-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Fylamynt API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: fylamynt-rules
scopes:
- name: Fylamynt Scopes
  scope_count: 0
  slug: fylamynt-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 22.2
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
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
  name: Fylamynt Authentication
  slug: fylamynt-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Fylamynt Domain Security
  slug: fylamynt-domain-security
  summary_line: DMARC
slug: fylamynt
tags:
- Company
- Cloud
- Automation
- Incident-Response
- Orchestration
- Platform
website: https://www.fylamynt.com/
---
