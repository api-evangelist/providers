---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.2
  scored_at: '2026-10-17'
api_count: 6
apis:
- baseURL: https://{siren-investigate-host}
  baseurl_source: declared
  description: The Collections API from Siren — 1 operation(s) for collections.
  name: Siren Collections API
  slug: siren-io-collections-api
- baseURL: https://{siren-investigate-host}
  baseurl_source: declared
  description: The Entity Tables API from Siren — 1 operation(s) for entity tables.
  name: Siren Entity Tables API
  slug: siren-io-entity-tables-api
- baseURL: https://{siren-investigate-host}
  baseurl_source: declared
  description: The Generate Query API from Siren — 2 operation(s) for generate query.
  name: Siren Generate Query API
  slug: siren-io-generate-query-api
- baseURL: https://{siren-investigate-host}
  baseurl_source: declared
  description: The Health API from Siren — 1 operation(s) for health.
  name: Siren Health API
  slug: siren-io-health-api
- baseURL: https://{siren-investigate-host}
  baseurl_source: declared
  description: The Operations API from Siren — 3 operation(s) for operations.
  name: Siren Operations API
  slug: siren-io-operations-api
- baseURL: https://{siren-investigate-host}
  baseurl_source: declared
  description: The Status API from Siren — 1 operation(s) for status.
  name: Siren Status API
  slug: siren-io-status-api
artifact_total: 13
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/siren-io/refs/heads/main/rules/siren-io-rules.yml
  title: ''
  type: Spectral
  url: rules/siren-io-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/siren-io/refs/heads/main/json-ld/siren-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/siren-io-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/siren-io/refs/heads/main/vocabulary/siren-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/siren-io-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/siren-io/refs/heads/main/data-model/siren-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/siren-io-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/siren-io/refs/heads/main/conformance/siren-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/siren-io-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/siren-io/refs/heads/main/llms/siren-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/siren-io-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/siren-io/refs/heads/main/hosts/siren-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/siren-io-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://siren.io/newsroom/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/siren-io/refs/heads/main/security/siren-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/siren-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://siren.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.siren.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.siren.io/siren-platform-user-guide/16.0/siren-investigate/c_rest-apis.html
- group: start
  title: ''
  type: GettingStarted
  url: https://siren.io/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://siren.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sirensolutions
- group: operate
  title: ''
  type: Support
  url: https://support.siren.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://siren.io/legal/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://siren.io/contact/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://info.siren.io/mcp
  - status: 200
    url: https://siren.io
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: 'Siren (Siren Solutions, siren.io) builds the Siren Platform for investigative intelligence: Siren Investigate, an Elasticsearch/OpenSearch-based investigation, link-analysis and search application used by law enforcement, intelligence, cyber and financial-crime teams. Siren Investigate exposes documented REST APIs (Status, Health, Query Generator, Dashboard, Search, Object Definitions, Reconciliation, Refresh Fields) plus a JavaScript scripting API, served from each customer''s own self-hosted Siren Investigate instance.'
image: https://siren.io/wp-content/uploads/img-siren-logo-power-investigations-hq-2400x1260-1.jpg
json_schemas:
- name: PostApiCollectionsReconciliationRequest
  property_count: 1
  slug: siren-io-post-api-collections-reconciliation-request
- name: PostApiCollectionsReconciliationResponse
  property_count: 1
  slug: siren-io-post-api-collections-reconciliation-response
- name: PostApiEntityTablesRefreshFieldsRequest
  property_count: 1
  slug: siren-io-post-api-entity-tables-refresh-fields-request
- name: PostApiEntityTablesRefreshFieldsResponse
  property_count: 1
  slug: siren-io-post-api-entity-tables-refresh-fields-response
jsonld:
- class_count: 7
  name: Siren Io Context
  property_count: 18
  slug: siren-io-context
layout: provider
modified: '2026-10-14'
name: Siren
nav: Providers
network: true
overview: 'Siren is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Entity Tables API, Generate Query API, and 3 more. Tagged areas include Company, Investigative Intelligence, Search, Link Analysis, and Elasticsearch.


  The Siren catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Siren''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, and 13 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Siren API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: siren-io-rules
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 23.7
    developer_ergonomics: 35.7
    discoverability: 80.4
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Siren Io Domain Security
  slug: siren-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: siren-io
tags:
- Company
- Investigative Intelligence
- Search
- Link Analysis
- Elasticsearch
- Data Analytics
website: https://siren.io
---
