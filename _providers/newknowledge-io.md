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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: YonderAPI provides access to text and image analysis services for building pipelines, as described in the YonderAPI v1 Reference.
  name: YonderAPI
  slug: yonderapi
- baseURL: https://api.yonderlabs.com
  baseurl_source: declared
  description: 'Yonder API as documented publicly: 80 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Yonder API
  slug: newknowledge-io-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/newknowledge-io/rules/newknowledge-io-rules.yml
  title: ''
  type: Spectral
  url: rules/newknowledge-io-rules.yml
- group: design
  href: https://artifacts.apis.io/newknowledge-io/json-ld/newknowledge-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/newknowledge-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/newknowledge-io/vocabulary/newknowledge-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/newknowledge-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/newknowledge-io/data-model/newknowledge-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/newknowledge-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/newknowledge-io/authentication/newknowledge-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/newknowledge-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/newknowledge-io/errors/newknowledge-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/newknowledge-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/newknowledge-io/conformance/newknowledge-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/newknowledge-io-conformance.yml
- group: other
  href: https://artifacts.apis.io/newknowledge-io/hosts/newknowledge-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/newknowledge-io-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yonderlabs.com/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yonderlabs
- group: auth
  href: https://artifacts.apis.io/newknowledge-io/security/newknowledge-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/newknowledge-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yonderlabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-v2-docs.yonderlabs.com/
coverage:
  checked: '2026-10-29'
  detail: Documentation pages are HTML only and no OpenAPI/AsyncAPI/GraphQL spec was found despite probing common spec URLs.
  evidence:
  - status: 404
    url: https://api.yonderlabs.com/openapi.json
  - status: 200
    url: https://api-docs.yonderlabs.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Yonder, formerly named New Knowledge and Popily, is a company from Austin, Texas, that specializes in disinformation research. It is known for supporting the Senate Select Committee on Intelligence's investigation of Russian interference in the 2016 US presidential election and was involved in a disinformation operation during the 2017 US Senate special election in Alabama. Its CEO and researchers have provided expert commentary to major media on topics such as 5G and COVID-19 misinformation.
image: https://yonderlabs.com/og-image.png
json_schemas:
- name: Get10TextcollectionDocumentclusteringResponse
  property_count: 6
  slug: newknowledge-io-get10-textcollection-documentclustering-response
- name: Get10TextcollectionEntitygraphResponse
  property_count: 4
  slug: newknowledge-io-get10-textcollection-entitygraph-response
- name: Get10UserUserinfoResponse
  property_count: 9
  slug: newknowledge-io-get10-user-userinfo-response
- name: Post10ImageFaceanalysisFromimageResponse
  property_count: 6
  slug: newknowledge-io-post10-image-faceanalysis-fromimage-response
- name: Post10TextcollectionDocumentclusteringResponse
  property_count: 6
  slug: newknowledge-io-post10-textcollection-documentclustering-response
- name: Post10TextcollectionEntitygraphResponse
  property_count: 4
  slug: newknowledge-io-post10-textcollection-entitygraph-response
jsonld:
- class_count: 75
  name: Newknowledge Io Context
  property_count: 54
  slug: newknowledge-io-context
layout: provider
modified: '2026-10-29'
name: Yonder
nav: Providers
network: true
overview: 'Yonder is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Disinformation, Research, AI, and Austin.


  The Yonder catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Yonder''s developer surface includes authentication, documentation, and 11 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Yonder API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: newknowledge-io-rules
scopes:
- name: Newknowledge Io Scopes
  scope_count: 0
  slug: newknowledge-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 19.7
    contract_quality: 26.3
    developer_ergonomics: 21.4
    discoverability: 66.1
    operational_transparency: 5.3
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
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Newknowledge Io Authentication
  slug: newknowledge-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Newknowledge Io Domain Security
  slug: newknowledge-io-domain-security
  summary_line: TLSv1.3
slug: newknowledge-io
tags:
- Company
- Disinformation
- Research
- AI
- Austin
website: https://yonderlabs.com/
---
