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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-09-24'
api_count: 2
apis:
- description: Fossil SCM provides a web interface and command-line tool but does not expose a public REST API.
  name: Fossil SCM API
  slug: fossil-scm-api-2
- baseURL: https://fossil.wanderinghorse.net
  baseurl_source: declared
  description: 'Fossil SCM API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: Fossil SCM API
  slug: fossil-scm-api
artifact_total: 8
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fossil-scm/refs/heads/main/rules/fossil-scm-rules.yml
  title: ''
  type: Spectral
  url: rules/fossil-scm-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fossil-scm/refs/heads/main/json-ld/fossil-scm-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fossil-scm-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fossil-scm/refs/heads/main/vocabulary/fossil-scm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fossil-scm-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fossil-scm/refs/heads/main/data-model/fossil-scm-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fossil-scm-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fossil-scm/refs/heads/main/changelog/fossil-scm-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fossil-scm-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fossil-scm/refs/heads/main/authentication/fossil-scm-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fossil-scm-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fossil-scm/refs/heads/main/conformance/fossil-scm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fossil-scm-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fossil-scm/refs/heads/main/security/fossil-scm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fossil-scm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fossil-scm.org/
- group: docs
  title: ''
  type: Documentation
  url: https://fossil-scm.org/home/doc/trunk/www/index.wiki
- group: other
  title: ''
  type: Download
  url: https://fossil-scm.org/home/uv/download.html
- group: start
  title: ''
  type: QuickStart
  url: https://fossil-scm.org/home/doc/trunk/www/quickstart.wiki
- group: operate
  title: ''
  type: Support
  url: https://fossil-scm.org/forum/forum
coverage:
  checked: 2026-09-22
  detail: Fossil SCM is a version control system without a public API.
  evidence:
  - status: 200
    url: https://fossil-scm.org/home/doc/trunk/www/index.wiki
  reason: not-a-software-company
  state: none
created: '2026-09-22'
description: Fossil SCM is an open-source, distributed version control system that includes an integrated bug tracking, wiki, and web interface. It provides a self-contained, easy-to-deploy solution for software configuration management, suitable for both small projects and large codebases. The system emphasizes simplicity, reliability, and a single-file repository model, making it a coherent alternative to other SCM tools.
json_schemas:
- name: PostJsonUserGetRequest
  property_count: 1
  slug: fossil-scm-post-json-user-get-request
- name: PostJsonUserGetResponse
  property_count: 5
  slug: fossil-scm-post-json-user-get-response
jsonld:
- class_count: 2
  name: Fossil Scm Context
  property_count: 5
  slug: fossil-scm-context
layout: provider
modified: '2026-09-22'
name: Fossil SCM
nav: Providers
network: true
overview: 'Fossil SCM publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Version Control, Open Source, SCM, Distributed, and Configuration Management.


  The Fossil SCM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fossil SCM''s developer surface includes changelog, authentication, documentation, quickstart, support, and 8 more developer resources.'
random_paper: 12
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Fossil SCM API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: fossil-scm-rules
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.8
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 22.1
    developer_ergonomics: 26.2
    discoverability: 55.6
    operational_transparency: 15.8
  previous_composite: 34.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Fossil Scm Authentication
  slug: fossil-scm-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Fossil Scm Domain Security
  slug: fossil-scm-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fossil-scm
tags:
- Version Control
- Open Source
- SCM
- Distributed
- Configuration Management
website: https://fossil-scm.org/
---
