---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
agentic_access:
- acting_count: 40
  human_in_the_loop: 0
  name: Userclouds Agentic Access
  operation_count: 65
  slug: userclouds-agentic-access
  summary_line: 65 operations · 40 acting
api_count: 1
apis:
- baseURL: https://your-tenant-name.tenant.userclouds.com
  baseurl_source: declared
  description: The Accessors API from UserClouds — 3 operation(s) for accessors.
  name: UserClouds Accessors API
  slug: userclouds-accessors-api
- baseURL: https://your-tenant-name.tenant.userclouds.com
  baseurl_source: declared
  description: The ColumnRetentionDurations API from UserClouds — 12 operation(s) for columnretentiondurations.
  name: UserClouds Column Retention Durations API
  slug: userclouds-columnretentiondurations-api
- baseURL: https://your-tenant-name.tenant.userclouds.com
  baseurl_source: declared
  description: The Columns API from UserClouds — 2 operation(s) for columns.
  name: UserClouds Columns API
  slug: userclouds-columns-api
- baseURL: https://your-tenant-name.tenant.userclouds.com
  baseurl_source: declared
  description: The Data Types API from UserClouds — 2 operation(s) for data types.
  name: UserClouds Data Types API
  slug: userclouds-data-types-api
- baseURL: https://your-tenant-name.tenant.userclouds.com
  baseurl_source: declared
  description: The Mutators API from UserClouds — 3 operation(s) for mutators.
  name: UserClouds Mutators API
  slug: userclouds-mutators-api
- baseURL: https://your-tenant-name.tenant.userclouds.com
  baseurl_source: declared
  description: The Purposes API from UserClouds — 3 operation(s) for purposes.
  name: UserClouds Purposes API
  slug: userclouds-purposes-api
- baseURL: https://your-tenant-name.tenant.userclouds.com
  baseurl_source: declared
  description: The User Search Indices API from UserClouds — 2 operation(s) for user search indices.
  name: UserClouds User Search Indices API
  slug: userclouds-user-search-indices-api
- baseURL: https://your-tenant-name.tenant.userclouds.com
  baseurl_source: declared
  description: The Users API from UserClouds — 2 operation(s) for users.
  name: UserClouds Users API
  slug: userclouds-users-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/userclouds/agentic-access/userclouds-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/userclouds-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/userclouds/rules/userclouds-rules.yml
  title: ''
  type: Spectral
  url: rules/userclouds-rules.yml
- group: design
  href: https://artifacts.apis.io/userclouds/json-ld/userclouds-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/userclouds-context.jsonld
- group: design
  href: https://artifacts.apis.io/userclouds/vocabulary/userclouds-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/userclouds-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/userclouds/data-model/userclouds-data-model.yml
  title: ''
  type: DataModel
  url: data-model/userclouds-data-model.yml
- group: design
  href: https://artifacts.apis.io/userclouds/errors/userclouds-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/userclouds-problem-types.yml
- group: design
  href: https://artifacts.apis.io/userclouds/conformance/userclouds-conformance.yml
  title: ''
  type: Conformance
  url: conformance/userclouds-conformance.yml
- group: other
  href: https://artifacts.apis.io/userclouds/hosts/userclouds-hosts.yml
  title: ''
  type: Hosts
  url: hosts/userclouds-hosts.yml
- group: other
  href: https://artifacts.apis.io/userclouds/vendors/userclouds-vendors.yml
  title: ''
  type: Vendors
  url: vendors/userclouds-vendors.yml
- group: build
  href: https://artifacts.apis.io/userclouds/packages/userclouds-packages.yml
  title: ''
  type: SDKs
  url: packages/userclouds-packages.yml
- group: build
  href: https://artifacts.apis.io/userclouds/packages/userclouds-packages.yml
  title: ''
  type: Packages
  url: packages/userclouds-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://userclouds.com/docs/
- group: auth
  href: https://artifacts.apis.io/userclouds/security/userclouds-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/userclouds-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://userclouds.com
created: '2026-10-29'
description: UserClouds is a SaaS company that offers a developer‑focused identity and access management platform. It provides APIs for authentication, authorization, user provisioning, and policy enforcement, enabling applications to integrate secure login, single sign‑on, and fine‑grained permissions. The service includes SDKs, documentation, and a developer portal to help teams build and manage user identities across web, mobile, and enterprise environments. Founded with backing from decibel, UserClouds aims to simplify security for modern applications.
image: https://docs.userclouds.com/logo.png
json_schemas:
- name: IdpExecuteAccessorResponse
  property_count: 7
  slug: userclouds-idp-execute-accessor-response
- name: SearchUserSearchIndex
  property_count: 13
  slug: userclouds-search-user-search-index
- name: UserstoreAccessor
  property_count: 15
  slug: userclouds-userstore-accessor
- name: UserstoreColumnDataType
  property_count: 6
  slug: userclouds-userstore-column-data-type
- name: UserstoreColumn
  property_count: 14
  slug: userclouds-userstore-column
- name: UserstoreMutator
  property_count: 8
  slug: userclouds-userstore-mutator
jsonld:
- class_count: 64
  name: Userclouds Context
  property_count: 92
  slug: userclouds-context
layout: provider
modified: '2026-10-29'
name: UserClouds
nav: Providers
network: true
overview: 'UserClouds publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accessors API, Column Retention Durations API, Columns API, and 5 more. Tagged areas include Company.


  The UserClouds catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  UserClouds'' developer surface includes documentation and 13 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: UserClouds API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: userclouds-rules
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 55.9
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Userclouds Domain Security
  slug: userclouds-domain-security
  summary_line: TLSv1.3 · DMARC
slug: userclouds
tags:
- Company
website: https://userclouds.com
---
