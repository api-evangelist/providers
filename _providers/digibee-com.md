---
agent_readiness:
  band: agent-ready
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
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Integration platform API documented at Digibee docs.
  name: Digibee API
  slug: digibee-api
- description: 'Digibee API as documented publicly: 44 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Digibee API
  slug: digibee-com-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/digibee-com/rules/digibee-com-rules.yml
  title: ''
  type: Spectral
  url: rules/digibee-com-rules.yml
- group: design
  href: https://artifacts.apis.io/digibee-com/json-ld/digibee-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/digibee-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/digibee-com/vocabulary/digibee-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/digibee-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/digibee-com/data-model/digibee-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/digibee-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/digibee-com/conventions/digibee-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/digibee-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.digibee.com/
- group: auth
  href: https://artifacts.apis.io/digibee-com/authentication/digibee-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/digibee-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/digibee-com/conformance/digibee-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/digibee-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/digibee-com/llms/digibee-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/digibee-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/digibee-com/well-known/digibee-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/digibee-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/digibee-com/hosts/digibee-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digibee-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/digibee-com/vendors/digibee-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/digibee-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digibee.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.digibee.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.digibee.com/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.digibee.com/documentation/release-notes
- group: company
  title: ''
  type: Blog
  url: https://www.digibee.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.digibee.com/documentation/platform-administration/administration/digibeectl/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digibee.com/
- group: auth
  href: https://artifacts.apis.io/digibee-com/security/digibee-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/digibee-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/digibee-com/security/digibee-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digibee-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://digibee.com/
coverage:
  checked: '2026-10-20'
  detail: Docs site redirects to a JavaScript-rendered portal, preventing retrieval of a machine-readable OpenAPI spec.
  evidence:
  - status: 307
    url: https://docs.digibee.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: Digibee is an AI-native integration platform that enables enterprises to build, automate, and manage integration agents across various systems and services. It offers capabilities such as integration, agent building, automation, enterprise MCP, and AI Suite, targeting industries like financial services, hospitality, and manufacturing. The platform focuses on accelerating enterprise AI, ERP migration, legacy modernization, and mergers & acquisitions, providing a comprehensive solution for modern digital transformation.
image: https://cdn.prod.website-files.com/6a5e3bacf0ad99d84aec8167/6a5e3bacf0ad99d84aec817d_ogImage.png
json_schemas:
- name: GetApiV1UsersUseridPageViewsQueryQueryidResponse
  property_count: 5
  slug: digibee-com-get-api-v1-users-userid-page-views-query-queryid-response
- name: GetResponse
  property_count: 11
  slug: digibee-com-get-response
- name: PostApiV1UsersPageViewsQueryRequest
  property_count: 4
  slug: digibee-com-post-api-v1-users-page-views-query-request
- name: PostApiV1UsersUseridPageViewsQueryRequest
  property_count: 3
  slug: digibee-com-post-api-v1-users-userid-page-views-query-request
- name: PutRequest
  property_count: 2
  slug: digibee-com-put-request
- name: PutResponse
  property_count: 5
  slug: digibee-com-put-response
jsonld:
- class_count: 49
  name: Digibee Com Context
  property_count: 56
  slug: digibee-com-context
layout: provider
modified: '2026-10-20'
name: Digibee
nav: Providers
network: true
overview: 'Digibee is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, Artificial Intelligence, Automation, and Enterprise.


  The Digibee catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Digibee''s developer surface includes authentication, pricing, changelog, engineering blog, getting-started guide, documentation, and 16 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Digibee API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: digibee-com-rules
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 24.4
    developer_ergonomics: 35.7
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Digibee Com Authentication
  slug: digibee-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Digibee Com Domain Security
  slug: digibee-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Digibee Com Trust Center
  slug: digibee-com-trust-center
  summary_line: SOC 2, PCI DSS
slug: digibee-com
tags:
- Company
- Integration
- Artificial Intelligence
- Automation
- Enterprise
website: https://digibee.com/
---
