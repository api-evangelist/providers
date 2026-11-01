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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Welcome to the documentation for the Pnut API.
  name: Pnut API
  slug: pnut-api-2
- baseURL: https://api.pnut.io
  baseurl_source: declared
  description: 'pnut.io API as documented publicly: 201 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: pnut.io API
  slug: pnut-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/pnut/rules/pnut-rules.yml
  title: ''
  type: Spectral
  url: rules/pnut-rules.yml
- group: design
  href: https://artifacts.apis.io/pnut/json-ld/pnut-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pnut-context.jsonld
- group: design
  href: https://artifacts.apis.io/pnut/vocabulary/pnut-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pnut-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pnut/data-model/pnut-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pnut-data-model.yml
- group: design
  href: https://artifacts.apis.io/pnut/conformance/pnut-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pnut-conformance.yml
- group: other
  href: https://artifacts.apis.io/pnut/hosts/pnut-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pnut-hosts.yml
- group: build
  href: https://artifacts.apis.io/pnut/packages/pnut-packages.yml
  title: ''
  type: SDKs
  url: packages/pnut-packages.yml
- group: build
  href: https://artifacts.apis.io/pnut/packages/pnut-packages.yml
  title: ''
  type: Packages
  url: packages/pnut-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pnut.io/tos
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.pnut-api-1.org/v1
- group: auth
  href: https://artifacts.apis.io/pnut/security/pnut-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pnut-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pnut.io/
- group: docs
  title: ''
  type: Documentation
  url: https://pnut.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://pnut.io/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://pnut.io/join
- group: start
  title: ''
  type: SignUp
  url: https://pnut.io/join
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pnut.io/privacy
coverage:
  checked: '2026-10-28'
  detail: The provider's public documentation does not include a machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 404
    url: https://api.pnut.io/openapi.json
  - status: 404
    url: https://pnut.io/openapi.json
  - status: 403
    url: https://api.pnut.io/.well-known/agent-card.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Pnut is an API‑first social networking platform that emphasizes community ownership, developer empowerment, and sustainability. It offers a rich set of endpoints for managing posts, interactions, and user profiles, supporting features like badges, dance parties, and customizable content, all accessible via a well‑documented RESTful API.
image: https://pnut.io/static/images/header.svg?date=20180913
json_schemas:
- name: GetChannelsChannelidResponse
  property_count: 17
  slug: pnut-get-channels-channelid-response
- name: GetFilesFileidResponse
  property_count: 25
  slug: pnut-get-files-fileid-response
- name: GetSysOpsOpsidResponse
  property_count: 5
  slug: pnut-get-sys-ops-opsid-response
- name: PostPollsRequest
  property_count: 8
  slug: pnut-post-polls-request
- name: PostPostsRequest
  property_count: 6
  slug: pnut-post-posts-request
- name: PutPostsPostidRequest
  property_count: 5
  slug: pnut-put-posts-postid-request
jsonld:
- class_count: 120
  name: Pnut Context
  property_count: 91
  slug: pnut-context
layout: provider
modified: '2026-10-28'
name: pnut.io
nav: Providers
network: true
overview: 'pnut.io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, API-first, Community, and Sustainability.


  The pnut.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  pnut.io''s developer surface includes documentation, API reference, getting-started guide, signup flow, and 13 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: pnut.io API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: pnut-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 45.2
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 15
      marker_coverage: 100.0
      total: 15
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pnut Domain Security
  slug: pnut-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pnut
tags:
- Company
- Social
- API-first
- Community
- Sustainability
- Developer-friendly
website: https://pnut.io/
---
