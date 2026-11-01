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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Yappes API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Yappes API
  slug: yappes-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/yappes/rules/yappes-rules.yml
  title: ''
  type: Spectral
  url: rules/yappes-rules.yml
- group: design
  href: https://artifacts.apis.io/yappes/json-ld/yappes-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/yappes-context.jsonld
- group: design
  href: https://artifacts.apis.io/yappes/vocabulary/yappes-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/yappes-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/yappes/data-model/yappes-data-model.yml
  title: ''
  type: DataModel
  url: data-model/yappes-data-model.yml
- group: auth
  href: https://artifacts.apis.io/yappes/authentication/yappes-authentication.yml
  title: ''
  type: Authentication
  url: authentication/yappes-authentication.yml
- group: design
  href: https://artifacts.apis.io/yappes/conformance/yappes-conformance.yml
  title: ''
  type: Conformance
  url: conformance/yappes-conformance.yml
- group: agent
  href: https://artifacts.apis.io/yappes/llms/yappes-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yappes-llms.txt
- group: other
  href: https://artifacts.apis.io/yappes/hosts/yappes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yappes-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://yappes.com/news
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.yappes.com/admin_console/sso-setup/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.yappes.com/
- group: auth
  href: https://artifacts.apis.io/yappes/security/yappes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yappes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yappes.com/
created: '2026-10-21'
description: Yappes provides a unified API management platform that enables enterprises to design, secure, publish, monitor, and monetize APIs at scale. The solution offers a graphical interface for lifecycle management, policy enforcement, analytics, and developer portal capabilities, helping organizations avoid fragmented tooling and improve governance across their API ecosystem.
image: https://framerusercontent.com/assets/wHckNQSOBev9EjMmlz8F9R2Y7A.png
json_schemas:
- name: GetV1MintOrganizationsOrgreferenceidTransactionsUsersUserref
  property_count: 13
  slug: yappes-get-v1-mint-organizations-orgreferenceid-transactions-users-userref
- name: GetV1OrganizationsOrgreferenceidApisProxynameResponse
  property_count: 13
  slug: yappes-get-v1-organizations-orgreferenceid-apis-proxyname-response
- name: GetV1OrganizationsOrgreferenceidApisResponse
  property_count: 13
  slug: yappes-get-v1-organizations-orgreferenceid-apis-response
- name: GetV1OrganizationsOrgreferenceidAppsAppreferenceidResponse
  property_count: 12
  slug: yappes-get-v1-organizations-orgreferenceid-apps-appreferenceid-response
- name: PostV1OrganizationsOrgreferenceidApiproductsApiproductrefere2
  property_count: 11
  slug: yappes-post-v1-organizations-orgreferenceid-apiproducts-apiproductrefere2
- name: PostV1OrganizationsOrgreferenceidEnvironmentsEnvnameQueriesR
  property_count: 5
  slug: yappes-post-v1-organizations-orgreferenceid-environments-envname-queries-r
jsonld:
- class_count: 25
  name: Yappes Context
  property_count: 70
  slug: yappes-context
layout: provider
modified: '2026-10-21'
name: Yappes
nav: Providers
network: true
overview: 'Yappes is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Management, Unified Platform, Developer Portal, and Analytics.


  The Yappes catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Yappes'' developer surface includes authentication, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Yappes API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: yappes-rules
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 33.3
    discoverability: 58.9
    operational_transparency: 0.0
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
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Yappes Authentication
  slug: yappes-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Yappes Domain Security
  slug: yappes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yappes
tags:
- Company
- API Management
- Unified Platform
- Developer Portal
- Analytics
website: https://yappes.com/
---
