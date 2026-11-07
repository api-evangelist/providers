---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: Fossil SCM provides a web interface and command-line tool but does not expose a public REST API.
  name: Fossil SCM API
  slug: fossil-scm-api-2
- baseURL: https://fossil.wanderinghorse.net
  baseurl_source: declared
  description: The Home API from Fossil SCM — 1 operation(s) for home.
  name: Fossil SCM Home API
  slug: fossil-scm-home-api
- baseURL: https://fossil.wanderinghorse.net
  baseurl_source: declared
  description: The Json API from Fossil SCM — 2 operation(s) for json.
  name: Fossil SCM JSON API
  slug: fossil-scm-json-api
- baseURL: https://fossil.wanderinghorse.net
  baseurl_source: declared
  description: The Wikis API from Fossil SCM — 1 operation(s) for wikis.
  name: Fossil SCM Wikis API
  slug: fossil-scm-wikis-api
artifact_total: 10
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://fossil-scm.org/home/timeline.rss
- group: design
  href: https://artifacts.apis.io/fossil-scm/rules/fossil-scm-rules.yml
  title: ''
  type: Spectral
  url: rules/fossil-scm-rules.yml
- group: design
  href: https://artifacts.apis.io/fossil-scm/json-ld/fossil-scm-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fossil-scm-context.jsonld
- group: design
  href: https://artifacts.apis.io/fossil-scm/vocabulary/fossil-scm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fossil-scm-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fossil-scm/data-model/fossil-scm-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fossil-scm-data-model.yml
- group: operate
  href: https://artifacts.apis.io/fossil-scm/changelog/fossil-scm-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fossil-scm-changelog.yml
- group: auth
  href: https://artifacts.apis.io/fossil-scm/authentication/fossil-scm-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fossil-scm-authentication.yml
- group: design
  href: https://artifacts.apis.io/fossil-scm/conformance/fossil-scm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fossil-scm-conformance.yml
- group: auth
  href: https://artifacts.apis.io/fossil-scm/security/fossil-scm-domain-security.yml
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
modified: '2026-10-06'
name: Fossil SCM
nav: Providers
network: true
overview: 'Fossil SCM is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Home API, JSON API, Wikis API, and 1 more. Tagged areas include Version Control, Open Source, SCM, Distributed, and Configuration Management.


  The Fossil SCM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fossil SCM''s developer surface includes changelog, authentication, documentation, quickstart, support, and 9 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 53
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
  composite: 19.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 19.0
    discoverability: 58.9
    operational_transparency: 15.8
  previous_composite: 20.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fossil-scm/fossil-scm-2026-10-11T104630.png
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
